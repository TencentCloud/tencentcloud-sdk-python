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


class Ability(AbstractModel):
    """集群支持的功能

    """

    def __init__(self):
        r"""
        :param _IsSupportSlaveZone: 是否支持从可用区
        :type IsSupportSlaveZone: str
        :param _NonsupportSlaveZoneReason: 不支持从可用区的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NonsupportSlaveZoneReason: str
        :param _IsSupportRo: 是否支持RO实例
        :type IsSupportRo: str
        :param _NonsupportRoReason: 不支持RO实例的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NonsupportRoReason: str
        :param _IsSupportManualSnapshot: 是否支持手动发起快照备份
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportManualSnapshot: str
        :param _IsSupportTransparentDataEncryption: 是否支持透明数据加密
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportTransparentDataEncryption: str
        :param _NoSupportTransparentDataEncryptionReason: 不支持透明数据加密原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NoSupportTransparentDataEncryptionReason: str
        :param _IsSupportManualLogic: 是否支持手动发起逻辑备份
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportManualLogic: str
        """
        self._IsSupportSlaveZone = None
        self._NonsupportSlaveZoneReason = None
        self._IsSupportRo = None
        self._NonsupportRoReason = None
        self._IsSupportManualSnapshot = None
        self._IsSupportTransparentDataEncryption = None
        self._NoSupportTransparentDataEncryptionReason = None
        self._IsSupportManualLogic = None

    @property
    def IsSupportSlaveZone(self):
        return self._IsSupportSlaveZone

    @IsSupportSlaveZone.setter
    def IsSupportSlaveZone(self, IsSupportSlaveZone):
        self._IsSupportSlaveZone = IsSupportSlaveZone

    @property
    def NonsupportSlaveZoneReason(self):
        return self._NonsupportSlaveZoneReason

    @NonsupportSlaveZoneReason.setter
    def NonsupportSlaveZoneReason(self, NonsupportSlaveZoneReason):
        self._NonsupportSlaveZoneReason = NonsupportSlaveZoneReason

    @property
    def IsSupportRo(self):
        return self._IsSupportRo

    @IsSupportRo.setter
    def IsSupportRo(self, IsSupportRo):
        self._IsSupportRo = IsSupportRo

    @property
    def NonsupportRoReason(self):
        return self._NonsupportRoReason

    @NonsupportRoReason.setter
    def NonsupportRoReason(self, NonsupportRoReason):
        self._NonsupportRoReason = NonsupportRoReason

    @property
    def IsSupportManualSnapshot(self):
        return self._IsSupportManualSnapshot

    @IsSupportManualSnapshot.setter
    def IsSupportManualSnapshot(self, IsSupportManualSnapshot):
        self._IsSupportManualSnapshot = IsSupportManualSnapshot

    @property
    def IsSupportTransparentDataEncryption(self):
        return self._IsSupportTransparentDataEncryption

    @IsSupportTransparentDataEncryption.setter
    def IsSupportTransparentDataEncryption(self, IsSupportTransparentDataEncryption):
        self._IsSupportTransparentDataEncryption = IsSupportTransparentDataEncryption

    @property
    def NoSupportTransparentDataEncryptionReason(self):
        return self._NoSupportTransparentDataEncryptionReason

    @NoSupportTransparentDataEncryptionReason.setter
    def NoSupportTransparentDataEncryptionReason(self, NoSupportTransparentDataEncryptionReason):
        self._NoSupportTransparentDataEncryptionReason = NoSupportTransparentDataEncryptionReason

    @property
    def IsSupportManualLogic(self):
        return self._IsSupportManualLogic

    @IsSupportManualLogic.setter
    def IsSupportManualLogic(self, IsSupportManualLogic):
        self._IsSupportManualLogic = IsSupportManualLogic


    def _deserialize(self, params):
        self._IsSupportSlaveZone = params.get("IsSupportSlaveZone")
        self._NonsupportSlaveZoneReason = params.get("NonsupportSlaveZoneReason")
        self._IsSupportRo = params.get("IsSupportRo")
        self._NonsupportRoReason = params.get("NonsupportRoReason")
        self._IsSupportManualSnapshot = params.get("IsSupportManualSnapshot")
        self._IsSupportTransparentDataEncryption = params.get("IsSupportTransparentDataEncryption")
        self._NoSupportTransparentDataEncryptionReason = params.get("NoSupportTransparentDataEncryptionReason")
        self._IsSupportManualLogic = params.get("IsSupportManualLogic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        r"""
        :param _AccountName: 数据库账号名
        :type AccountName: str
        :param _Description: 数据库账号描述
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Host: 主机
        :type Host: str
        :param _MaxUserConnections: 用户最大连接数
        :type MaxUserConnections: int
        """
        self._AccountName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Host = None
        self._MaxUserConnections = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Host = params.get("Host")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountParam(AbstractModel):
    """账号参数

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称，当前仅支持参数：max_user_connections
        :type ParamName: str
        :param _ParamValue: 参数值
        :type ParamValue: str
        """
        self._ParamName = None
        self._ParamValue = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamValue(self):
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceRequest(AbstractModel):
    """ActivateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdList: 实例 ID 列表，单个实例 ID 格式如：cynosdbmysql-ins-n7ocdslw，与TDSQL-C MySQL数据库控制台页面中显示的实例 ID 相同，可使用 查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIdList: list of str
        """
        self._ClusterId = None
        self._InstanceIdList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceResponse(AbstractModel):
    """ActivateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class AddClusterSlaveZoneRequest(AbstractModel):
    """AddClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _SlaveZone: 从可用区
        :type SlaveZone: str
        :param _BinlogSyncWay: binlog同步方式。默认值：async。可选值：sync、semisync、async
        :type BinlogSyncWay: str
        """
        self._ClusterId = None
        self._SlaveZone = None
        self._BinlogSyncWay = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BinlogSyncWay(self):
        return self._BinlogSyncWay

    @BinlogSyncWay.setter
    def BinlogSyncWay(self, BinlogSyncWay):
        self._BinlogSyncWay = BinlogSyncWay


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SlaveZone = params.get("SlaveZone")
        self._BinlogSyncWay = params.get("BinlogSyncWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterSlaveZoneResponse(AbstractModel):
    """AddClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步FlowId
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Cpu: Cpu核数
        :type Cpu: int
        :param _Memory: 内存，单位为GB
        :type Memory: int
        :param _ReadOnlyCount: 新增只读实例数，取值范围为(0,15]
        :type ReadOnlyCount: int
        :param _DeviceType: 实例机器类型
        :type DeviceType: str
        :param _InstanceGrpId: 实例组ID，在已有RO组中新增实例时使用，不传则新增RO组。当前版本不建议传输该值。
        :type InstanceGrpId: str
        :param _VpcId: 所属VPC网络ID。
        :type VpcId: str
        :param _SubnetId: 所属子网ID，如果设置了VpcId，则SubnetId必填。
        :type SubnetId: str
        :param _Port: 新增RO组时使用的Port，取值范围为[0,65535)
        :type Port: int
        :param _InstanceName: 实例名称，字符串长度范围为[0,64)，取值范围为大小写字母，0-9数字，'_','-','.'
        :type InstanceName: str
        :param _AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param _OrderSource: 订单来源，字符串长度范围为[0,64)
        :type OrderSource: str
        :param _DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        :param _ParamTemplateId: 参数模板ID
        :type ParamTemplateId: int
        :param _InstanceParams: 参数列表，ParamTemplateId 传入时InstanceParams才有效
        :type InstanceParams: list of ModifyParamItem
        :param _SecurityGroupIds: 安全组ID，新建只读实例时可以指定安全组。
        :type SecurityGroupIds: list of str
        :param _UpgradeProxy: proxy同步升级
        :type UpgradeProxy: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxy`
        """
        self._ClusterId = None
        self._Cpu = None
        self._Memory = None
        self._ReadOnlyCount = None
        self._DeviceType = None
        self._InstanceGrpId = None
        self._VpcId = None
        self._SubnetId = None
        self._Port = None
        self._InstanceName = None
        self._AutoVoucher = None
        self._DbType = None
        self._OrderSource = None
        self._DealMode = None
        self._ParamTemplateId = None
        self._InstanceParams = None
        self._SecurityGroupIds = None
        self._UpgradeProxy = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def ReadOnlyCount(self):
        return self._ReadOnlyCount

    @ReadOnlyCount.setter
    def ReadOnlyCount(self, ReadOnlyCount):
        self._ReadOnlyCount = ReadOnlyCount

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def InstanceParams(self):
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeProxy(self):
        return self._UpgradeProxy

    @UpgradeProxy.setter
    def UpgradeProxy(self, UpgradeProxy):
        self._UpgradeProxy = UpgradeProxy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._ReadOnlyCount = params.get("ReadOnlyCount")
        self._DeviceType = params.get("DeviceType")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Port = params.get("Port")
        self._InstanceName = params.get("InstanceName")
        self._AutoVoucher = params.get("AutoVoucher")
        self._DbType = params.get("DbType")
        self._OrderSource = params.get("OrderSource")
        self._DealMode = params.get("DealMode")
        self._ParamTemplateId = params.get("ParamTemplateId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeProxy") is not None:
            self._UpgradeProxy = UpgradeProxy()
            self._UpgradeProxy._deserialize(params.get("UpgradeProxy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 冻结流水，一次开通一个冻结流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _DealNames: 后付费订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _ResourceIds: 发货资源id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param _BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._DealNames = params.get("DealNames")
        self._ResourceIds = params.get("ResourceIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class Addr(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        r"""
        :param _IP: IP地址
        :type IP: str
        :param _Port: 端口
        :type Port: int
        """
        self._IP = None
        self._Port = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例组 ID 数组，cynosdbmysql-grp-前缀开头或集群 ID。
说明：要获取集群的实例组 ID，可通过 [查询集群实例组](https://cloud.tencent.com/document/product/1003/103934) 进行。
        :type InstanceIds: list of str
        :param _SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。
        :type SecurityGroupIds: list of str
        :param _Zone: 可用区
        :type Zone: str
        """
        self._InstanceIds = None
        self._SecurityGroupIds = None
        self._Zone = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

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


class AuditInstanceFilters(AbstractModel):
    """查询审计实例的过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件值。支持InstanceId-实例ID，InstanceName-实例名称，ProjectId-项目ID，TagKey-标签键，Tag-标签（以竖线分割，例：Tagkey|Tagvalue）。
        :type Name: str
        :param _ExactMatch: true表示精确查找，false表示模糊匹配。
        :type ExactMatch: bool
        :param _Values: 筛选值
        :type Values: list of str
        """
        self._Name = None
        self._ExactMatch = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ExactMatch = params.get("ExactMatch")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditInstanceInfo(AbstractModel):
    """审计实例详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _TagList: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        """
        self._ProjectId = None
        self._TagList = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """审计日志详细信息

    """

    def __init__(self):
        r"""
        :param _AffectRows: 影响行数。
        :type AffectRows: int
        :param _ErrCode: 错误码。
        :type ErrCode: int
        :param _SqlType: SQL类型。
        :type SqlType: str
        :param _TableName: 表名称。
        :type TableName: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _PolicyName: 审计策略名称。
        :type PolicyName: str
        :param _DBName: 数据库名称。
        :type DBName: str
        :param _Sql: SQL语句。
        :type Sql: str
        :param _Host: 客户端地址。
        :type Host: str
        :param _User: 用户名。
        :type User: str
        :param _ExecTime: 执行时间，微秒。
        :type ExecTime: int
        :param _Timestamp: 时间。
        :type Timestamp: str
        :param _SentRows: 返回行数。
        :type SentRows: int
        :param _ThreadId: 执行线程ID。
        :type ThreadId: int
        :param _CheckRows: 扫描行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRows: int
        :param _CpuTime: cpu执行时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuTime: float
        :param _IoWaitTime: IO等待时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type IoWaitTime: int
        :param _LockWaitTime: 锁等待时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockWaitTime: int
        :param _TrxLivingTime: 事物持续等待时间，微秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrxLivingTime: int
        :param _NsTime: 开始时间，与timestamp构成一个精确到纳秒的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type NsTime: int
        :param _TemplateInfo: 日志命中规则模板的基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateInfo: list of LogRuleTemplateInfo
        :param _TrxId: 事务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TrxId: int
        """
        self._AffectRows = None
        self._ErrCode = None
        self._SqlType = None
        self._TableName = None
        self._InstanceName = None
        self._PolicyName = None
        self._DBName = None
        self._Sql = None
        self._Host = None
        self._User = None
        self._ExecTime = None
        self._Timestamp = None
        self._SentRows = None
        self._ThreadId = None
        self._CheckRows = None
        self._CpuTime = None
        self._IoWaitTime = None
        self._LockWaitTime = None
        self._TrxLivingTime = None
        self._NsTime = None
        self._TemplateInfo = None
        self._TrxId = None

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ExecTime(self):
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SentRows(self):
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def ThreadId(self):
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId

    @property
    def CheckRows(self):
        return self._CheckRows

    @CheckRows.setter
    def CheckRows(self, CheckRows):
        self._CheckRows = CheckRows

    @property
    def CpuTime(self):
        return self._CpuTime

    @CpuTime.setter
    def CpuTime(self, CpuTime):
        self._CpuTime = CpuTime

    @property
    def IoWaitTime(self):
        return self._IoWaitTime

    @IoWaitTime.setter
    def IoWaitTime(self, IoWaitTime):
        self._IoWaitTime = IoWaitTime

    @property
    def LockWaitTime(self):
        return self._LockWaitTime

    @LockWaitTime.setter
    def LockWaitTime(self, LockWaitTime):
        self._LockWaitTime = LockWaitTime

    @property
    def TrxLivingTime(self):
        return self._TrxLivingTime

    @TrxLivingTime.setter
    def TrxLivingTime(self, TrxLivingTime):
        self._TrxLivingTime = TrxLivingTime

    @property
    def NsTime(self):
        return self._NsTime

    @NsTime.setter
    def NsTime(self, NsTime):
        self._NsTime = NsTime

    @property
    def TemplateInfo(self):
        return self._TemplateInfo

    @TemplateInfo.setter
    def TemplateInfo(self, TemplateInfo):
        self._TemplateInfo = TemplateInfo

    @property
    def TrxId(self):
        return self._TrxId

    @TrxId.setter
    def TrxId(self, TrxId):
        self._TrxId = TrxId


    def _deserialize(self, params):
        self._AffectRows = params.get("AffectRows")
        self._ErrCode = params.get("ErrCode")
        self._SqlType = params.get("SqlType")
        self._TableName = params.get("TableName")
        self._InstanceName = params.get("InstanceName")
        self._PolicyName = params.get("PolicyName")
        self._DBName = params.get("DBName")
        self._Sql = params.get("Sql")
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._ExecTime = params.get("ExecTime")
        self._Timestamp = params.get("Timestamp")
        self._SentRows = params.get("SentRows")
        self._ThreadId = params.get("ThreadId")
        self._CheckRows = params.get("CheckRows")
        self._CpuTime = params.get("CpuTime")
        self._IoWaitTime = params.get("IoWaitTime")
        self._LockWaitTime = params.get("LockWaitTime")
        self._TrxLivingTime = params.get("TrxLivingTime")
        self._NsTime = params.get("NsTime")
        if params.get("TemplateInfo") is not None:
            self._TemplateInfo = []
            for item in params.get("TemplateInfo"):
                obj = LogRuleTemplateInfo()
                obj._deserialize(item)
                self._TemplateInfo.append(obj)
        self._TrxId = params.get("TrxId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFile(AbstractModel):
    """审计日志文件

    """

    def __init__(self):
        r"""
        :param _FileName: 审计日志文件名称
        :type FileName: str
        :param _CreateTime: 审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param _Status: 文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :type Status: str
        :param _FileSize: 文件大小，单位为 KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _DownloadUrl: 审计日志下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _ErrMsg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self._FileName = None
        self._CreateTime = None
        self._Status = None
        self._FileSize = None
        self._DownloadUrl = None
        self._ErrMsg = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._FileSize = params.get("FileSize")
        self._DownloadUrl = params.get("DownloadUrl")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """审计日志过滤条件。查询审计日志时，用户过滤返回的审计日志。

    """

    def __init__(self):
        r"""
        :param _Host: 客户端地址。
        :type Host: list of str
        :param _User: 用户名。
        :type User: list of str
        :param _DBName: 数据库名称。
        :type DBName: list of str
        :param _TableName: 表名称。
        :type TableName: list of str
        :param _PolicyName: 审计策略名称。
        :type PolicyName: list of str
        :param _Sql: SQL 语句。支持模糊匹配。
        :type Sql: str
        :param _SqlType: SQL 类型。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlType: str
        :param _ExecTime: 执行时间。单位为：ms。表示筛选执行时间大于该值的审计日志。
        :type ExecTime: int
        :param _AffectRows: 影响行数。表示筛选影响行数大于该值的审计日志。
        :type AffectRows: int
        :param _SqlTypes: SQL 类型。支持多个类型同时查询。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlTypes: list of str
        :param _Sqls: SQL 语句。支持传递多个sql语句。
        :type Sqls: list of str
        :param _SentRows: 返回行数。
        :type SentRows: int
        :param _ThreadId: 线程ID。
        :type ThreadId: list of str
        """
        self._Host = None
        self._User = None
        self._DBName = None
        self._TableName = None
        self._PolicyName = None
        self._Sql = None
        self._SqlType = None
        self._ExecTime = None
        self._AffectRows = None
        self._SqlTypes = None
        self._Sqls = None
        self._SentRows = None
        self._ThreadId = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def ExecTime(self):
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def SqlTypes(self):
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Sqls(self):
        return self._Sqls

    @Sqls.setter
    def Sqls(self, Sqls):
        self._Sqls = Sqls

    @property
    def SentRows(self):
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def ThreadId(self):
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._DBName = params.get("DBName")
        self._TableName = params.get("TableName")
        self._PolicyName = params.get("PolicyName")
        self._Sql = params.get("Sql")
        self._SqlType = params.get("SqlType")
        self._ExecTime = params.get("ExecTime")
        self._AffectRows = params.get("AffectRows")
        self._SqlTypes = params.get("SqlTypes")
        self._Sqls = params.get("Sqls")
        self._SentRows = params.get("SentRows")
        self._ThreadId = params.get("ThreadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleFilters(AbstractModel):
    """规则审计的过滤条件

    """

    def __init__(self):
        r"""
        :param _RuleFilters: 单条审计规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleFilters: list of RuleFilters
        """
        self._RuleFilters = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleTemplateInfo(AbstractModel):
    """审计规则模板的详情

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: 规则模板ID。
        :type RuleTemplateId: str
        :param _RuleTemplateName: 规则模板名称。
        :type RuleTemplateName: str
        :param _RuleFilters: 规则模板的过滤条件
        :type RuleFilters: list of RuleFilters
        :param _Description: 规则模板描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateAt: 规则模板创建时间。
        :type CreateAt: str
        :param _UpdateAt: 规则模板修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: str
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: int
        :param _AlarmPolicy: 告警策略。0-不告警，1-告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmPolicy: int
        :param _Status: 模板状态。0-无任务 ，1-修改中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _AffectedInstances: 规则模板应用在哪些在实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedInstances: list of str
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._RuleFilters = None
        self._Description = None
        self._CreateAt = None
        self._UpdateAt = None
        self._AlarmLevel = None
        self._AlarmPolicy = None
        self._Status = None
        self._AffectedInstances = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AffectedInstances(self):
        return self._AffectedInstances

    @AffectedInstances.setter
    def AffectedInstances(self, AffectedInstances):
        self._AffectedInstances = AffectedInstances


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RuleTemplateName = params.get("RuleTemplateName")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._Description = params.get("Description")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._Status = params.get("Status")
        self._AffectedInstances = params.get("AffectedInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFileInfo(AbstractModel):
    """备份文件信息

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照文件ID，已废弃，请使用BackupId
        :type SnapshotId: int
        :param _FileName: 备份文件名
        :type FileName: str
        :param _FileSize: 备份文件大小
        :type FileSize: int
        :param _StartTime: 备份开始时间
        :type StartTime: str
        :param _FinishTime: 备份完成时间
        :type FinishTime: str
        :param _BackupType: 备份类型：snapshot，快照备份；logic，逻辑备份
        :type BackupType: str
        :param _BackupMethod: 备份方式：auto，自动备份；manual，手动备份
        :type BackupMethod: str
        :param _BackupStatus: 备份文件状态：success：备份成功；fail：备份失败；creating：备份文件创建中；deleting：备份文件删除中
        :type BackupStatus: str
        :param _SnapshotTime: 备份文件时间
        :type SnapshotTime: str
        :param _BackupId: 备份ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupId: int
        :param _SnapShotType: 快照类型，可选值：full，全量；increment，增量
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapShotType: str
        :param _BackupName: 备份文件备注
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupName: str
        """
        self._SnapshotId = None
        self._FileName = None
        self._FileSize = None
        self._StartTime = None
        self._FinishTime = None
        self._BackupType = None
        self._BackupMethod = None
        self._BackupStatus = None
        self._SnapshotTime = None
        self._BackupId = None
        self._SnapShotType = None
        self._BackupName = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStatus(self):
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def SnapShotType(self):
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStatus = params.get("BackupStatus")
        self._SnapshotTime = params.get("SnapshotTime")
        self._BackupId = params.get("BackupId")
        self._SnapShotType = params.get("SnapShotType")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingResourceInfo(AbstractModel):
    """计费资源信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _DealName: 订单ID
        :type DealName: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._DealName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindClusterResourcePackagesRequest(AbstractModel):
    """BindClusterResourcePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageIds: 资源包唯一ID
        :type PackageIds: list of str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._PackageIds = None
        self._ClusterId = None

    @property
    def PackageIds(self):
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._PackageIds = params.get("PackageIds")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindClusterResourcePackagesResponse(AbstractModel):
    """BindClusterResourcePackages返回参数结构体

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


class BindInstanceInfo(AbstractModel):
    """资源包绑定的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 绑定的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceRegion: 绑定的实例所在的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceRegion: str
        :param _InstanceType: 绑定的实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _ExtendIds: 绑定集群下的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtendIds: list of str
        """
        self._InstanceId = None
        self._InstanceRegion = None
        self._InstanceType = None
        self._ExtendIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRegion(self):
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExtendIds(self):
        return self._ExtendIds

    @ExtendIds.setter
    def ExtendIds(self, ExtendIds):
        self._ExtendIds = ExtendIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRegion = params.get("InstanceRegion")
        self._InstanceType = params.get("InstanceType")
        self._ExtendIds = params.get("ExtendIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogConfigInfo(AbstractModel):
    """binlog配置信息

    """

    def __init__(self):
        r"""
        :param _BinlogSaveDays: binlog保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogSaveDays: int
        :param _BinlogCrossRegionsEnable: binlog异地地域备份是否开启
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogCrossRegionsEnable: str
        :param _BinlogCrossRegions: binlog异地地域
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogCrossRegions: list of str
        """
        self._BinlogSaveDays = None
        self._BinlogCrossRegionsEnable = None
        self._BinlogCrossRegions = None

    @property
    def BinlogSaveDays(self):
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays

    @property
    def BinlogCrossRegionsEnable(self):
        return self._BinlogCrossRegionsEnable

    @BinlogCrossRegionsEnable.setter
    def BinlogCrossRegionsEnable(self, BinlogCrossRegionsEnable):
        self._BinlogCrossRegionsEnable = BinlogCrossRegionsEnable

    @property
    def BinlogCrossRegions(self):
        return self._BinlogCrossRegions

    @BinlogCrossRegions.setter
    def BinlogCrossRegions(self, BinlogCrossRegions):
        self._BinlogCrossRegions = BinlogCrossRegions


    def _deserialize(self, params):
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        self._BinlogCrossRegionsEnable = params.get("BinlogCrossRegionsEnable")
        self._BinlogCrossRegions = params.get("BinlogCrossRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogItem(AbstractModel):
    """Binlog描述

    """

    def __init__(self):
        r"""
        :param _FileName: Binlog文件名称
        :type FileName: str
        :param _FileSize: 文件大小，单位：字节
        :type FileSize: int
        :param _StartTime: 事务最早时间
        :type StartTime: str
        :param _FinishTime: 事务最晚时间
        :type FinishTime: str
        :param _BinlogId: Binlog文件ID
        :type BinlogId: int
        """
        self._FileName = None
        self._FileSize = None
        self._StartTime = None
        self._FinishTime = None
        self._BinlogId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def BinlogId(self):
        return self._BinlogId

    @BinlogId.setter
    def BinlogId(self, BinlogId):
        self._BinlogId = BinlogId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BizTaskInfo(AbstractModel):
    """任务信息

    """

    def __init__(self):
        r"""
        :param _ID: 任务id
        :type ID: int
        :param _AppId: 用户appid
        :type AppId: int
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _DelayTime: 延迟执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayTime: str
        :param _ErrMsg: 任务失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _FlowId: 异步任务流id
        :type FlowId: int
        :param _Input: 任务输入信息
        :type Input: str
        :param _InstanceGrpId: 实例组id
        :type InstanceGrpId: str
        :param _InstanceGroupId: 实例组id
        :type InstanceGroupId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ObjectId: 任务操作对象id
        :type ObjectId: str
        :param _ObjectType: 任务操作对象类型
        :type ObjectType: str
        :param _Operator: 操作者uin
        :type Operator: str
        :param _Output: 任务输出信息
        :type Output: str
        :param _Status: 任务状态
        :type Status: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _TriggerTaskId: 触发本任务的父任务ID
        :type TriggerTaskId: int
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _StartTime: 任务开始时间
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Process: 任务进度
        :type Process: int
        :param _ModifyParamsData: 修改参数任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyParamsData: list of ModifyParamsData
        :param _CreateClustersData: 创建集群任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateClustersData: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersData`
        :param _RollbackData: 集群回档任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackData: :class:`tencentcloud.cynosdb.v20190107.models.RollbackData`
        :param _ModifyInstanceData: 实例变配任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyInstanceData: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceData`
        :param _ManualBackupData: 手动备份任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualBackupData: :class:`tencentcloud.cynosdb.v20190107.models.ManualBackupData`
        :param _ModifyDbVersionData: 修改内核版本任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyDbVersionData: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDbVersionData`
        :param _ClusterSlaveData: 集群可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterSlaveData: :class:`tencentcloud.cynosdb.v20190107.models.ClusterSlaveData`
        :param _SwitchClusterLogBin: 转换集群日志
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchClusterLogBin: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterLogBin`
        :param _ModifyInstanceParamsData: 修改实例参数数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyInstanceParamsData: :class:`tencentcloud.cynosdb.v20190107.models.BizTaskModifyParamsData`
        :param _TaskMaintainInfo: 维护时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMaintainInfo: :class:`tencentcloud.cynosdb.v20190107.models.TaskMaintainInfo`
        :param _InstanceCLSDeliveryInfos: 实例日志投递信息

注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCLSDeliveryInfos: list of InstanceCLSDeliveryInfo
        """
        self._ID = None
        self._AppId = None
        self._ClusterId = None
        self._Region = None
        self._CreateTime = None
        self._DelayTime = None
        self._ErrMsg = None
        self._FlowId = None
        self._Input = None
        self._InstanceGrpId = None
        self._InstanceGroupId = None
        self._InstanceId = None
        self._ObjectId = None
        self._ObjectType = None
        self._Operator = None
        self._Output = None
        self._Status = None
        self._TaskType = None
        self._TriggerTaskId = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._ClusterName = None
        self._InstanceName = None
        self._Process = None
        self._ModifyParamsData = None
        self._CreateClustersData = None
        self._RollbackData = None
        self._ModifyInstanceData = None
        self._ManualBackupData = None
        self._ModifyDbVersionData = None
        self._ClusterSlaveData = None
        self._SwitchClusterLogBin = None
        self._ModifyInstanceParamsData = None
        self._TaskMaintainInfo = None
        self._InstanceCLSDeliveryInfos = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DelayTime(self):
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ObjectId(self):
        return self._ObjectId

    @ObjectId.setter
    def ObjectId(self, ObjectId):
        self._ObjectId = ObjectId

    @property
    def ObjectType(self):
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TriggerTaskId(self):
        return self._TriggerTaskId

    @TriggerTaskId.setter
    def TriggerTaskId(self, TriggerTaskId):
        self._TriggerTaskId = TriggerTaskId

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
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Process(self):
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def ModifyParamsData(self):
        warnings.warn("parameter `ModifyParamsData` is deprecated", DeprecationWarning) 

        return self._ModifyParamsData

    @ModifyParamsData.setter
    def ModifyParamsData(self, ModifyParamsData):
        warnings.warn("parameter `ModifyParamsData` is deprecated", DeprecationWarning) 

        self._ModifyParamsData = ModifyParamsData

    @property
    def CreateClustersData(self):
        return self._CreateClustersData

    @CreateClustersData.setter
    def CreateClustersData(self, CreateClustersData):
        self._CreateClustersData = CreateClustersData

    @property
    def RollbackData(self):
        return self._RollbackData

    @RollbackData.setter
    def RollbackData(self, RollbackData):
        self._RollbackData = RollbackData

    @property
    def ModifyInstanceData(self):
        return self._ModifyInstanceData

    @ModifyInstanceData.setter
    def ModifyInstanceData(self, ModifyInstanceData):
        self._ModifyInstanceData = ModifyInstanceData

    @property
    def ManualBackupData(self):
        return self._ManualBackupData

    @ManualBackupData.setter
    def ManualBackupData(self, ManualBackupData):
        self._ManualBackupData = ManualBackupData

    @property
    def ModifyDbVersionData(self):
        return self._ModifyDbVersionData

    @ModifyDbVersionData.setter
    def ModifyDbVersionData(self, ModifyDbVersionData):
        self._ModifyDbVersionData = ModifyDbVersionData

    @property
    def ClusterSlaveData(self):
        return self._ClusterSlaveData

    @ClusterSlaveData.setter
    def ClusterSlaveData(self, ClusterSlaveData):
        self._ClusterSlaveData = ClusterSlaveData

    @property
    def SwitchClusterLogBin(self):
        return self._SwitchClusterLogBin

    @SwitchClusterLogBin.setter
    def SwitchClusterLogBin(self, SwitchClusterLogBin):
        self._SwitchClusterLogBin = SwitchClusterLogBin

    @property
    def ModifyInstanceParamsData(self):
        return self._ModifyInstanceParamsData

    @ModifyInstanceParamsData.setter
    def ModifyInstanceParamsData(self, ModifyInstanceParamsData):
        self._ModifyInstanceParamsData = ModifyInstanceParamsData

    @property
    def TaskMaintainInfo(self):
        return self._TaskMaintainInfo

    @TaskMaintainInfo.setter
    def TaskMaintainInfo(self, TaskMaintainInfo):
        self._TaskMaintainInfo = TaskMaintainInfo

    @property
    def InstanceCLSDeliveryInfos(self):
        return self._InstanceCLSDeliveryInfos

    @InstanceCLSDeliveryInfos.setter
    def InstanceCLSDeliveryInfos(self, InstanceCLSDeliveryInfos):
        self._InstanceCLSDeliveryInfos = InstanceCLSDeliveryInfos


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._DelayTime = params.get("DelayTime")
        self._ErrMsg = params.get("ErrMsg")
        self._FlowId = params.get("FlowId")
        self._Input = params.get("Input")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceId = params.get("InstanceId")
        self._ObjectId = params.get("ObjectId")
        self._ObjectType = params.get("ObjectType")
        self._Operator = params.get("Operator")
        self._Output = params.get("Output")
        self._Status = params.get("Status")
        self._TaskType = params.get("TaskType")
        self._TriggerTaskId = params.get("TriggerTaskId")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ClusterName = params.get("ClusterName")
        self._InstanceName = params.get("InstanceName")
        self._Process = params.get("Process")
        if params.get("ModifyParamsData") is not None:
            self._ModifyParamsData = []
            for item in params.get("ModifyParamsData"):
                obj = ModifyParamsData()
                obj._deserialize(item)
                self._ModifyParamsData.append(obj)
        if params.get("CreateClustersData") is not None:
            self._CreateClustersData = CreateClustersData()
            self._CreateClustersData._deserialize(params.get("CreateClustersData"))
        if params.get("RollbackData") is not None:
            self._RollbackData = RollbackData()
            self._RollbackData._deserialize(params.get("RollbackData"))
        if params.get("ModifyInstanceData") is not None:
            self._ModifyInstanceData = ModifyInstanceData()
            self._ModifyInstanceData._deserialize(params.get("ModifyInstanceData"))
        if params.get("ManualBackupData") is not None:
            self._ManualBackupData = ManualBackupData()
            self._ManualBackupData._deserialize(params.get("ManualBackupData"))
        if params.get("ModifyDbVersionData") is not None:
            self._ModifyDbVersionData = ModifyDbVersionData()
            self._ModifyDbVersionData._deserialize(params.get("ModifyDbVersionData"))
        if params.get("ClusterSlaveData") is not None:
            self._ClusterSlaveData = ClusterSlaveData()
            self._ClusterSlaveData._deserialize(params.get("ClusterSlaveData"))
        if params.get("SwitchClusterLogBin") is not None:
            self._SwitchClusterLogBin = SwitchClusterLogBin()
            self._SwitchClusterLogBin._deserialize(params.get("SwitchClusterLogBin"))
        if params.get("ModifyInstanceParamsData") is not None:
            self._ModifyInstanceParamsData = BizTaskModifyParamsData()
            self._ModifyInstanceParamsData._deserialize(params.get("ModifyInstanceParamsData"))
        if params.get("TaskMaintainInfo") is not None:
            self._TaskMaintainInfo = TaskMaintainInfo()
            self._TaskMaintainInfo._deserialize(params.get("TaskMaintainInfo"))
        if params.get("InstanceCLSDeliveryInfos") is not None:
            self._InstanceCLSDeliveryInfos = []
            for item in params.get("InstanceCLSDeliveryInfos"):
                obj = InstanceCLSDeliveryInfo()
                obj._deserialize(item)
                self._InstanceCLSDeliveryInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BizTaskModifyInstanceParam(AbstractModel):
    """实例参数修改任务详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ModifyInstanceParamList: 实例参数修改任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyInstanceParamList: list of ModifyParamItem
        """
        self._InstanceId = None
        self._ModifyInstanceParamList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyInstanceParamList(self):
        return self._ModifyInstanceParamList

    @ModifyInstanceParamList.setter
    def ModifyInstanceParamList(self, ModifyInstanceParamList):
        self._ModifyInstanceParamList = ModifyInstanceParamList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ModifyInstanceParamList") is not None:
            self._ModifyInstanceParamList = []
            for item in params.get("ModifyInstanceParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ModifyInstanceParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BizTaskModifyParamsData(AbstractModel):
    """修改参数任务数据

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterParamList: 集群参数修改数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterParamList: list of ModifyParamItem
        :param _ModifyInstanceParams: 实例参数修改数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyInstanceParams: list of BizTaskModifyInstanceParam
        """
        self._ClusterId = None
        self._ClusterParamList = None
        self._ModifyInstanceParams = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterParamList(self):
        return self._ClusterParamList

    @ClusterParamList.setter
    def ClusterParamList(self, ClusterParamList):
        self._ClusterParamList = ClusterParamList

    @property
    def ModifyInstanceParams(self):
        return self._ModifyInstanceParams

    @ModifyInstanceParams.setter
    def ModifyInstanceParams(self, ModifyInstanceParams):
        self._ModifyInstanceParams = ModifyInstanceParams


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ClusterParamList") is not None:
            self._ClusterParamList = []
            for item in params.get("ClusterParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ClusterParamList.append(obj)
        if params.get("ModifyInstanceParams") is not None:
            self._ModifyInstanceParams = []
            for item in params.get("ModifyInstanceParams"):
                obj = BizTaskModifyInstanceParam()
                obj._deserialize(item)
                self._ModifyInstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLSInfo(AbstractModel):
    """CLS日志投递配置

    """

    def __init__(self):
        r"""
        :param _TopicOperation: 日志主题操作：可选create,reuse。
create:新增日志主题，使用TopicName创建日志主题。
reuse:使用已有日志主题，使用TopicId指定日志主题。
不允许使用已有日志主题且新建日志集的组合。
        :type TopicOperation: str
        :param _GroupOperation: 日志集操作：可选create,reuse。
create:新增日志集，使用GroupName创建日志集。
reuse:使用已有日志集，使用GroupId指定日志集。
不允许使用已有日志主题且新建日志集的组合。
        :type GroupOperation: str
        :param _Region: 日志投递地域
        :type Region: str
        :param _TopicId: 日志主题id
        :type TopicId: str
        :param _TopicName: 日志主题name
        :type TopicName: str
        :param _GroupId: 日志集id
        :type GroupId: str
        :param _GroupName: 日志集name
        :type GroupName: str
        """
        self._TopicOperation = None
        self._GroupOperation = None
        self._Region = None
        self._TopicId = None
        self._TopicName = None
        self._GroupId = None
        self._GroupName = None

    @property
    def TopicOperation(self):
        return self._TopicOperation

    @TopicOperation.setter
    def TopicOperation(self, TopicOperation):
        self._TopicOperation = TopicOperation

    @property
    def GroupOperation(self):
        return self._GroupOperation

    @GroupOperation.setter
    def GroupOperation(self, GroupOperation):
        self._GroupOperation = GroupOperation

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._TopicOperation = params.get("TopicOperation")
        self._GroupOperation = params.get("GroupOperation")
        self._Region = params.get("Region")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAuditServiceRequest(AbstractModel):
    """CloseAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
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
        


class CloseAuditServiceResponse(AbstractModel):
    """CloseAuditService返回参数结构体

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


class CloseClusterPasswordComplexityRequest(AbstractModel):
    """CloseClusterPasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 集群ID数组
        :type ClusterIds: list of str
        """
        self._ClusterIds = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseClusterPasswordComplexityResponse(AbstractModel):
    """CloseClusterPasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CloseProxyRequest(AbstractModel):
    """CloseProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _OnlyCloseRW: 是否只关闭读写分离，取值：是 "true","false"
        :type OnlyCloseRW: bool
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._OnlyCloseRW = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OnlyCloseRW(self):
        return self._OnlyCloseRW

    @OnlyCloseRW.setter
    def OnlyCloseRW(self, OnlyCloseRW):
        self._OnlyCloseRW = OnlyCloseRW


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._OnlyCloseRW = params.get("OnlyCloseRW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxyResponse(AbstractModel):
    """CloseProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloseWanRequest(AbstractModel):
    """CloseWan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceGrpId: 实例组id
        :type InstanceGrpId: str
        :param _InstanceGroupId: 实例组id
        :type InstanceGroupId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceGrpId = None
        self._InstanceGroupId = None
        self._InstanceId = None

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanResponse(AbstractModel):
    """CloseWan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ClusterInstanceDetail(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceType: 引擎类型
        :type InstanceType: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param _InstanceCpu: cpu核数
        :type InstanceCpu: int
        :param _InstanceMemory: 内存
        :type InstanceMemory: int
        :param _InstanceStorage: 硬盘
        :type InstanceStorage: int
        :param _InstanceRole: 实例角色
        :type InstanceRole: str
        :param _MaintainStartTime: 执行开始时间(距离0点的秒数)	
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainStartTime: int
        :param _MaintainDuration: 持续的时间(单位：秒)	
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainDuration: int
        :param _MaintainWeekDays: 可以执行的时间，枚举值：["Mon","Tue","Wed","Thu","Fri", "Sat", "Sun"]
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainWeekDays: list of str
        :param _ServerlessStatus: serverless实例子状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerlessStatus: str
        :param _InstanceTasks: 实例任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTasks: list of ObjectTask
        :param _InstanceDeviceType: 实例机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceDeviceType: str
        :param _InstanceStorageType: 实例存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStorageType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._InstanceStatusDesc = None
        self._InstanceCpu = None
        self._InstanceMemory = None
        self._InstanceStorage = None
        self._InstanceRole = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None
        self._ServerlessStatus = None
        self._InstanceTasks = None
        self._InstanceDeviceType = None
        self._InstanceStorageType = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceStatusDesc(self):
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def InstanceCpu(self):
        return self._InstanceCpu

    @InstanceCpu.setter
    def InstanceCpu(self, InstanceCpu):
        self._InstanceCpu = InstanceCpu

    @property
    def InstanceMemory(self):
        return self._InstanceMemory

    @InstanceMemory.setter
    def InstanceMemory(self, InstanceMemory):
        self._InstanceMemory = InstanceMemory

    @property
    def InstanceStorage(self):
        return self._InstanceStorage

    @InstanceStorage.setter
    def InstanceStorage(self, InstanceStorage):
        self._InstanceStorage = InstanceStorage

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def InstanceTasks(self):
        return self._InstanceTasks

    @InstanceTasks.setter
    def InstanceTasks(self, InstanceTasks):
        self._InstanceTasks = InstanceTasks

    @property
    def InstanceDeviceType(self):
        return self._InstanceDeviceType

    @InstanceDeviceType.setter
    def InstanceDeviceType(self, InstanceDeviceType):
        self._InstanceDeviceType = InstanceDeviceType

    @property
    def InstanceStorageType(self):
        return self._InstanceStorageType

    @InstanceStorageType.setter
    def InstanceStorageType(self, InstanceStorageType):
        self._InstanceStorageType = InstanceStorageType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceStatusDesc = params.get("InstanceStatusDesc")
        self._InstanceCpu = params.get("InstanceCpu")
        self._InstanceMemory = params.get("InstanceMemory")
        self._InstanceStorage = params.get("InstanceStorage")
        self._InstanceRole = params.get("InstanceRole")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._ServerlessStatus = params.get("ServerlessStatus")
        if params.get("InstanceTasks") is not None:
            self._InstanceTasks = []
            for item in params.get("InstanceTasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._InstanceTasks.append(obj)
        self._InstanceDeviceType = params.get("InstanceDeviceType")
        self._InstanceStorageType = params.get("InstanceStorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterParamModifyLog(AbstractModel):
    """参数修改记录

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _CurrentValue: 当前值
        :type CurrentValue: str
        :param _UpdateValue: 修改后的值
        :type UpdateValue: str
        :param _Status: 修改状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._UpdateValue = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ClusterId = None
        self._InstanceId = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def UpdateValue(self):
        return self._UpdateValue

    @UpdateValue.setter
    def UpdateValue(self, UpdateValue):
        self._UpdateValue = UpdateValue

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

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._UpdateValue = params.get("UpdateValue")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ClusterId = params.get("ClusterId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterSlaveData(AbstractModel):
    """集群从可用区信息

    """

    def __init__(self):
        r"""
        :param _OldMasterZone: 旧主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type OldMasterZone: str
        :param _OldSlaveZone: 旧从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type OldSlaveZone: list of str
        :param _NewMasterZone: 新主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type NewMasterZone: str
        :param _NewSlaveZone: 新从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSlaveZone: list of str
        :param _NewSlaveZoneAttr: 新从可用区属性
注意：此字段可能返回 null，表示取不到有效值。
        :type NewSlaveZoneAttr: list of SlaveZoneAttrItem
        :param _OldSlaveZoneAttr: 旧可用区属性
注意：此字段可能返回 null，表示取不到有效值。
        :type OldSlaveZoneAttr: list of SlaveZoneAttrItem
        """
        self._OldMasterZone = None
        self._OldSlaveZone = None
        self._NewMasterZone = None
        self._NewSlaveZone = None
        self._NewSlaveZoneAttr = None
        self._OldSlaveZoneAttr = None

    @property
    def OldMasterZone(self):
        return self._OldMasterZone

    @OldMasterZone.setter
    def OldMasterZone(self, OldMasterZone):
        self._OldMasterZone = OldMasterZone

    @property
    def OldSlaveZone(self):
        return self._OldSlaveZone

    @OldSlaveZone.setter
    def OldSlaveZone(self, OldSlaveZone):
        self._OldSlaveZone = OldSlaveZone

    @property
    def NewMasterZone(self):
        return self._NewMasterZone

    @NewMasterZone.setter
    def NewMasterZone(self, NewMasterZone):
        self._NewMasterZone = NewMasterZone

    @property
    def NewSlaveZone(self):
        return self._NewSlaveZone

    @NewSlaveZone.setter
    def NewSlaveZone(self, NewSlaveZone):
        self._NewSlaveZone = NewSlaveZone

    @property
    def NewSlaveZoneAttr(self):
        return self._NewSlaveZoneAttr

    @NewSlaveZoneAttr.setter
    def NewSlaveZoneAttr(self, NewSlaveZoneAttr):
        self._NewSlaveZoneAttr = NewSlaveZoneAttr

    @property
    def OldSlaveZoneAttr(self):
        return self._OldSlaveZoneAttr

    @OldSlaveZoneAttr.setter
    def OldSlaveZoneAttr(self, OldSlaveZoneAttr):
        self._OldSlaveZoneAttr = OldSlaveZoneAttr


    def _deserialize(self, params):
        self._OldMasterZone = params.get("OldMasterZone")
        self._OldSlaveZone = params.get("OldSlaveZone")
        self._NewMasterZone = params.get("NewMasterZone")
        self._NewSlaveZone = params.get("NewSlaveZone")
        if params.get("NewSlaveZoneAttr") is not None:
            self._NewSlaveZoneAttr = []
            for item in params.get("NewSlaveZoneAttr"):
                obj = SlaveZoneAttrItem()
                obj._deserialize(item)
                self._NewSlaveZoneAttr.append(obj)
        if params.get("OldSlaveZoneAttr") is not None:
            self._OldSlaveZoneAttr = []
            for item in params.get("OldSlaveZoneAttr"):
                obj = SlaveZoneAttrItem()
                obj._deserialize(item)
                self._OldSlaveZoneAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyClusterPasswordComplexityRequest(AbstractModel):
    """CopyClusterPasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 复制集群ID数组，例如["cynosdbmysql-bzxxrmtq","cynosdbmysql-qwer"]
        :type ClusterIds: list of str
        :param _SourceClusterId: 集群id，例如"cynosdbmysql-bzxxrmtq"
        :type SourceClusterId: str
        """
        self._ClusterIds = None
        self._SourceClusterId = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def SourceClusterId(self):
        return self._SourceClusterId

    @SourceClusterId.setter
    def SourceClusterId(self, SourceClusterId):
        self._SourceClusterId = SourceClusterId


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._SourceClusterId = params.get("SourceClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyClusterPasswordComplexityResponse(AbstractModel):
    """CopyClusterPasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Accounts: 新账户列表
        :type Accounts: list of NewAccount
        """
        self._ClusterId = None
        self._Accounts = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = NewAccount()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回参数结构体

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


class CreateAuditLogFileRequest(AbstractModel):
    """CreateAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间，格式为："2017-07-12 10:29:20"。
        :type StartTime: str
        :param _EndTime: 结束时间，格式为："2017-07-12 10:29:20"。
        :type EndTime: str
        :param _Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param _OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param _Filter: 已废弃。
        :type Filter: :class:`tencentcloud.cynosdb.v20190107.models.AuditLogFilter`
        :param _LogFilter: 审计日志过滤条件
        :type LogFilter: list of InstanceAuditLogFilter
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None
        self._LogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def LogFilter(self):
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = AuditLogFilter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = InstanceAuditLogFilter()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditLogFileResponse(AbstractModel):
    """CreateAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileName: 审计日志文件名称。
        :type FileName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileName = None
        self._RequestId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._RequestId = params.get("RequestId")


class CreateAuditRuleTemplateRequest(AbstractModel):
    """CreateAuditRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleFilters: 审计规则。
        :type RuleFilters: list of RuleFilters
        :param _RuleTemplateName: 规则模板名称。
        :type RuleTemplateName: str
        :param _Description: 规则模板描述。
        :type Description: str
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险
        :type AlarmLevel: int
        :param _AlarmPolicy: 告警策略。0-不告警，1-告警。
        :type AlarmPolicy: int
        """
        self._RuleFilters = None
        self._RuleTemplateName = None
        self._Description = None
        self._AlarmLevel = None
        self._AlarmPolicy = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._RuleTemplateName = params.get("RuleTemplateName")
        self._Description = params.get("Description")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRuleTemplateResponse(AbstractModel):
    """CreateAuditRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: 生成的规则模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleTemplateId = None
        self._RequestId = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BackupType: 备份类型, 可选值：logic，逻辑备份；snapshot，物理备份
        :type BackupType: str
        :param _BackupDatabases: 备份的库, 只在 BackupType 为 logic 时有效
        :type BackupDatabases: list of str
        :param _BackupTables: 备份的表, 只在 BackupType 为 logic 时有效
        :type BackupTables: list of DatabaseTables
        :param _BackupName: 备注名
        :type BackupName: str
        """
        self._ClusterId = None
        self._BackupType = None
        self._BackupDatabases = None
        self._BackupTables = None
        self._BackupName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupDatabases(self):
        return self._BackupDatabases

    @BackupDatabases.setter
    def BackupDatabases(self, BackupDatabases):
        self._BackupDatabases = BackupDatabases

    @property
    def BackupTables(self):
        return self._BackupTables

    @BackupTables.setter
    def BackupTables(self, BackupTables):
        self._BackupTables = BackupTables

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupType = params.get("BackupType")
        self._BackupDatabases = params.get("BackupDatabases")
        if params.get("BackupTables") is not None:
            self._BackupTables = []
            for item in params.get("BackupTables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self._BackupTables.append(obj)
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateCLSDeliveryRequest(AbstractModel):
    """CreateCLSDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _CLSInfoList: 日志投递配置
        :type CLSInfoList: list of CLSInfo
        :param _LogType: 日志类型
        :type LogType: str
        :param _IsInMaintainPeriod: 是否维护时间运行
        :type IsInMaintainPeriod: str
        """
        self._InstanceId = None
        self._CLSInfoList = None
        self._LogType = None
        self._IsInMaintainPeriod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CLSInfoList(self):
        return self._CLSInfoList

    @CLSInfoList.setter
    def CLSInfoList(self, CLSInfoList):
        self._CLSInfoList = CLSInfoList

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("CLSInfoList") is not None:
            self._CLSInfoList = []
            for item in params.get("CLSInfoList"):
                obj = CLSInfo()
                obj._deserialize(item)
                self._CLSInfoList.append(obj)
        self._LogType = params.get("LogType")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCLSDeliveryResponse(AbstractModel):
    """CreateCLSDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateClusterDatabaseRequest(AbstractModel):
    """CreateClusterDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _DbName: 数据库名
        :type DbName: str
        :param _CharacterSet: 字符集类型
        :type CharacterSet: str
        :param _CollateRule: 排序规则
        :type CollateRule: str
        :param _UserHostPrivileges: 授权用户主机权限
        :type UserHostPrivileges: list of UserHostPrivilege
        :param _Description: 备注
        :type Description: str
        """
        self._ClusterId = None
        self._DbName = None
        self._CharacterSet = None
        self._CollateRule = None
        self._UserHostPrivileges = None
        self._Description = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def CollateRule(self):
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def UserHostPrivileges(self):
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbName = params.get("DbName")
        self._CharacterSet = params.get("CharacterSet")
        self._CollateRule = params.get("CollateRule")
        if params.get("UserHostPrivileges") is not None:
            self._UserHostPrivileges = []
            for item in params.get("UserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._UserHostPrivileges.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterDatabaseResponse(AbstractModel):
    """CreateClusterDatabase返回参数结构体

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


class CreateClustersData(AbstractModel):
    """创建集群任务信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 实例CPU
        :type Cpu: int
        :param _Memory: 实例内存
        :type Memory: int
        :param _StorageLimit: 集群存储上限
        :type StorageLimit: int
        """
        self._Cpu = None
        self._Memory = None
        self._StorageLimit = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageLimit = params.get("StorageLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersRequest(AbstractModel):
    """CreateClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcId: 所属VPC网络ID
        :type VpcId: str
        :param _SubnetId: 所属子网ID
        :type SubnetId: str
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param _DbVersion: 数据库版本，取值范围: 
<li> MYSQL可选值：5.7，8.0 </li>
        :type DbVersion: str
        :param _ProjectId: 所属项目ID
        :type ProjectId: int
        :param _Cpu: 当DbMode为NORMAL或不填时必选
普通实例Cpu核数
        :type Cpu: int
        :param _Memory: 当DbMode为NORMAL或不填时必选
普通实例内存,单位GB
        :type Memory: int
        :param _Storage: 该参数无实际意义，已废弃。
存储大小，单位GB。
        :type Storage: int
        :param _ClusterName: 集群名称，长度小于64个字符，每个字符取值范围：大/小写字母，数字，特殊符号（'-','_','.'）
        :type ClusterName: str
        :param _AdminPassword: 账号密码(8-64个字符，包含大小写英文字母、数字和符号~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/中的任意三种)
        :type AdminPassword: str
        :param _Port: 端口，默认3306，取值范围[0, 65535)
        :type Port: int
        :param _PayMode: 计费模式，按量计费：0，包年包月：1。默认按量计费。
        :type PayMode: int
        :param _Count: 购买集群数，可选值范围[1,50]，默认为1
        :type Count: int
        :param _RollbackStrategy: 回档类型：
noneRollback：不回档；
snapRollback，快照回档；
timeRollback，时间点回档
        :type RollbackStrategy: str
        :param _RollbackId: 快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效
        :type RollbackId: int
        :param _OriginalClusterId: 回档时，传入源集群ID，用于查找源poolId
        :type OriginalClusterId: str
        :param _ExpectTime: 时间点回档，指定时间；快照回档，快照时间
        :type ExpectTime: str
        :param _ExpectTimeThresh: 该参数无实际意义，已废弃。
时间点回档，指定时间允许范围
        :type ExpectTimeThresh: int
        :param _StorageLimit: 普通实例存储上限，单位GB
当DbType为MYSQL，且存储计费模式为预付费时，该参数需不大于cpu与memory对应存储规格上限
        :type StorageLimit: int
        :param _InstanceCount: 实例数量，数量范围为(0,16]
        :type InstanceCount: int
        :param _TimeSpan: 包年包月购买时长
        :type TimeSpan: int
        :param _TimeUnit: 包年包月购买时长单位，['s','d','m','y']
        :type TimeUnit: str
        :param _AutoRenewFlag: 包年包月购买是否自动续费，默认为0。
0标识默认续费方式，1表示自动续费，2表示不自动续费。
        :type AutoRenewFlag: int
        :param _AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param _HaCount: 实例数量（该参数已不再使用，只做存量兼容处理）
        :type HaCount: int
        :param _OrderSource: 订单来源
        :type OrderSource: str
        :param _ResourceTags: 集群创建需要绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param _DbMode: Db类型
当DbType为MYSQL时可选(默认NORMAL)：
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param _MinCpu: 当DbMode为SERVERLESS时必填
cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinCpu: float
        :param _MaxCpu: 当DbMode为SERVERLESS时必填：
cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxCpu: float
        :param _AutoPause: 当DbMode为SERVERLESS时，指定集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
默认值:yes
        :type AutoPause: str
        :param _AutoPauseDelay: 当DbMode为SERVERLESS时，指定集群自动暂停的延迟，单位秒，可选范围[600,691200]
默认值:600
        :type AutoPauseDelay: int
        :param _StoragePayMode: 集群存储计费模式，按量计费：0，包年包月：1。默认按量计费
当DbType为MYSQL时，在集群计算计费模式为后付费（包括DbMode为SERVERLESS）时，存储计费模式仅可为按量计费
回档与克隆均不支持包年包月存储
        :type StoragePayMode: int
        :param _SecurityGroupIds: 安全组id数组
        :type SecurityGroupIds: list of str
        :param _AlarmPolicyIds: 告警策略Id数组
        :type AlarmPolicyIds: list of str
        :param _ClusterParams: 参数数组，暂时支持character_set_server （utf8｜latin1｜gbk｜utf8mb4） ，lower_case_table_names，1-大小写不敏感，0-大小写敏感
        :type ClusterParams: list of ParamItem
        :param _DealMode: 交易模式，0-下单且支付，1-下单
        :type DealMode: int
        :param _ParamTemplateId: 参数模板ID，可以通过查询参数模板信息DescribeParamTemplates获得参数模板ID
        :type ParamTemplateId: int
        :param _SlaveZone: 多可用区地址
        :type SlaveZone: str
        :param _InstanceInitInfos: 实例初始化配置信息，主要用于购买集群时选不同规格实例
        :type InstanceInitInfos: list of InstanceInitInfo
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DbType = None
        self._DbVersion = None
        self._ProjectId = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._ClusterName = None
        self._AdminPassword = None
        self._Port = None
        self._PayMode = None
        self._Count = None
        self._RollbackStrategy = None
        self._RollbackId = None
        self._OriginalClusterId = None
        self._ExpectTime = None
        self._ExpectTimeThresh = None
        self._StorageLimit = None
        self._InstanceCount = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._HaCount = None
        self._OrderSource = None
        self._ResourceTags = None
        self._DbMode = None
        self._MinCpu = None
        self._MaxCpu = None
        self._AutoPause = None
        self._AutoPauseDelay = None
        self._StoragePayMode = None
        self._SecurityGroupIds = None
        self._AlarmPolicyIds = None
        self._ClusterParams = None
        self._DealMode = None
        self._ParamTemplateId = None
        self._SlaveZone = None
        self._InstanceInitInfos = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AdminPassword(self):
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackId(self):
        return self._RollbackId

    @RollbackId.setter
    def RollbackId(self, RollbackId):
        self._RollbackId = RollbackId

    @property
    def OriginalClusterId(self):
        return self._OriginalClusterId

    @OriginalClusterId.setter
    def OriginalClusterId(self, OriginalClusterId):
        self._OriginalClusterId = OriginalClusterId

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def ExpectTimeThresh(self):
        return self._ExpectTimeThresh

    @ExpectTimeThresh.setter
    def ExpectTimeThresh(self, ExpectTimeThresh):
        self._ExpectTimeThresh = ExpectTimeThresh

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def HaCount(self):
        return self._HaCount

    @HaCount.setter
    def HaCount(self, HaCount):
        self._HaCount = HaCount

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def AutoPause(self):
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AlarmPolicyIds(self):
        return self._AlarmPolicyIds

    @AlarmPolicyIds.setter
    def AlarmPolicyIds(self, AlarmPolicyIds):
        self._AlarmPolicyIds = AlarmPolicyIds

    @property
    def ClusterParams(self):
        return self._ClusterParams

    @ClusterParams.setter
    def ClusterParams(self, ClusterParams):
        self._ClusterParams = ClusterParams

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def InstanceInitInfos(self):
        return self._InstanceInitInfos

    @InstanceInitInfos.setter
    def InstanceInitInfos(self, InstanceInitInfos):
        self._InstanceInitInfos = InstanceInitInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._ProjectId = params.get("ProjectId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._ClusterName = params.get("ClusterName")
        self._AdminPassword = params.get("AdminPassword")
        self._Port = params.get("Port")
        self._PayMode = params.get("PayMode")
        self._Count = params.get("Count")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._RollbackId = params.get("RollbackId")
        self._OriginalClusterId = params.get("OriginalClusterId")
        self._ExpectTime = params.get("ExpectTime")
        self._ExpectTimeThresh = params.get("ExpectTimeThresh")
        self._StorageLimit = params.get("StorageLimit")
        self._InstanceCount = params.get("InstanceCount")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._HaCount = params.get("HaCount")
        self._OrderSource = params.get("OrderSource")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbMode = params.get("DbMode")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._AutoPause = params.get("AutoPause")
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._StoragePayMode = params.get("StoragePayMode")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AlarmPolicyIds = params.get("AlarmPolicyIds")
        if params.get("ClusterParams") is not None:
            self._ClusterParams = []
            for item in params.get("ClusterParams"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ClusterParams.append(obj)
        self._DealMode = params.get("DealMode")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._SlaveZone = params.get("SlaveZone")
        if params.get("InstanceInitInfos") is not None:
            self._InstanceInitInfos = []
            for item in params.get("InstanceInitInfos"):
                obj = InstanceInitInfo()
                obj._deserialize(item)
                self._InstanceInitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _ResourceIds: 资源ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取资源ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param _ClusterIds: 集群ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取集群ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param _BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._ClusterIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._DealNames = params.get("DealNames")
        self._ResourceIds = params.get("ResourceIds")
        self._ClusterIds = params.get("ClusterIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _EngineVersion: mysql版本号
        :type EngineVersion: str
        :param _TemplateDescription: 模板描述
        :type TemplateDescription: str
        :param _TemplateId: 可选参数，需要复制的模板ID
        :type TemplateId: int
        :param _DbMode: 数据库类型，可选值：NORMAL（默认值），SERVERLESS
        :type DbMode: str
        :param _ParamList: 参数列表
        :type ParamList: list of ParamItem
        """
        self._TemplateName = None
        self._EngineVersion = None
        self._TemplateDescription = None
        self._TemplateId = None
        self._DbMode = None
        self._ParamList = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateDescription = params.get("TemplateDescription")
        self._TemplateId = params.get("TemplateId")
        self._DbMode = params.get("DbMode")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateProxyEndPointRequest(AbstractModel):
    """CreateProxyEndPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _UniqueVpcId: 私有网络ID，默认与集群私有网络ID保持一致
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 私有网络子网ID，默认与集群子网ID保持一致
        :type UniqueSubnetId: str
        :param _ConnectionPoolType: 连接池类型：SessionConnectionPool(会话级别连接池 )
        :type ConnectionPoolType: str
        :param _OpenConnectionPool: 是否开启连接池,yes-开启，no-不开启
        :type OpenConnectionPool: str
        :param _ConnectionPoolTimeOut: 连接池阈值：单位（秒）
        :type ConnectionPoolTimeOut: int
        :param _SecurityGroupIds: 绑定的安全组ID数组
        :type SecurityGroupIds: list of str
        :param _Description: 描述说明
        :type Description: str
        :param _Vip: 想要绑定的vip信息，需与UniqueVpcId对应。
        :type Vip: str
        :param _WeightMode: 权重模式：
system-系统分配，custom-自定义
        :type WeightMode: str
        :param _AutoAddRo: 是否自动添加只读实例，yes-是，no-不自动添加
        :type AutoAddRo: str
        :param _FailOver: 是否开启故障转移。
yes：开启
no：不开启。
数据库代理出现故障时，链接地址将会路由到主实例
        :type FailOver: str
        :param _ConsistencyType: 一致性类型：
eventual,global,session
        :type ConsistencyType: str
        :param _RwType: 读写属性：
READWRITE,READONLY
        :type RwType: str
        :param _ConsistencyTimeOut: 一致性超时时间。取值范围：0~1000000（微秒）,设置0则表示若只读实例出现延迟, 导致一致性策略不满足, 请求将一直等待
        :type ConsistencyTimeOut: int
        :param _TransSplit: 是否开启事务拆分。在一个事务中拆分读和写到不同的实例上去执行
        :type TransSplit: bool
        :param _AccessMode: 连接模式：
nearby,balance
        :type AccessMode: str
        :param _InstanceWeights: 实例权重
        :type InstanceWeights: list of ProxyInstanceWeight
        """
        self._ClusterId = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._ConnectionPoolType = None
        self._OpenConnectionPool = None
        self._ConnectionPoolTimeOut = None
        self._SecurityGroupIds = None
        self._Description = None
        self._Vip = None
        self._WeightMode = None
        self._AutoAddRo = None
        self._FailOver = None
        self._ConsistencyType = None
        self._RwType = None
        self._ConsistencyTimeOut = None
        self._TransSplit = None
        self._AccessMode = None
        self._InstanceWeights = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Description = params.get("Description")
        self._Vip = params.get("Vip")
        self._WeightMode = params.get("WeightMode")
        self._AutoAddRo = params.get("AutoAddRo")
        self._FailOver = params.get("FailOver")
        self._ConsistencyType = params.get("ConsistencyType")
        self._RwType = params.get("RwType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyEndPointResponse(AbstractModel):
    """CreateProxyEndPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._ProxyGroupId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Cpu: cpu核数
        :type Cpu: int
        :param _Mem: 内存
        :type Mem: int
        :param _UniqueVpcId: 私有网络ID，默认与集群私有网络ID保持一致
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 私有网络子网ID，默认与集群子网ID保持一致
        :type UniqueSubnetId: str
        :param _ProxyCount: 数据库代理组节点个数（该参数不再建议使用，建议使用ProxyZones)
        :type ProxyCount: int
        :param _ConnectionPoolType: 连接池类型：SessionConnectionPool(会话级别连接池 )
        :type ConnectionPoolType: str
        :param _OpenConnectionPool: 是否开启连接池,yes-开启，no-不开启
        :type OpenConnectionPool: str
        :param _ConnectionPoolTimeOut: 连接池阈值：单位（秒）
        :type ConnectionPoolTimeOut: int
        :param _SecurityGroupIds: 安全组ID数组
        :type SecurityGroupIds: list of str
        :param _Description: 描述说明
        :type Description: str
        :param _ProxyZones: 数据库节点信息（该参数与ProxyCount需要任选一个输入）
        :type ProxyZones: list of ProxyZone
        """
        self._ClusterId = None
        self._Cpu = None
        self._Mem = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._ProxyCount = None
        self._ConnectionPoolType = None
        self._OpenConnectionPool = None
        self._ConnectionPoolTimeOut = None
        self._SecurityGroupIds = None
        self._Description = None
        self._ProxyZones = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProxyZones(self):
        return self._ProxyZones

    @ProxyZones.setter
    def ProxyZones(self, ProxyZones):
        self._ProxyZones = ProxyZones


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._ProxyCount = params.get("ProxyCount")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Description = params.get("Description")
        if params.get("ProxyZones") is not None:
            self._ProxyZones = []
            for item in params.get("ProxyZones"):
                obj = ProxyZone()
                obj._deserialize(item)
                self._ProxyZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyResponse(AbstractModel):
    """CreateProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._ProxyGroupId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._RequestId = params.get("RequestId")


class CreateResourcePackageRequest(AbstractModel):
    """CreateResourcePackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，目前固定传cynosdb-serverless
        :type InstanceType: str
        :param _PackageRegion: 资源包使用地域chineseMainland-中国内地通用，overseas-港澳台及海外通用
        :type PackageRegion: str
        :param _PackageType: 资源包类型：CCU-计算资源包，DISK-存储资源包
        :type PackageType: str
        :param _PackageVersion: 资源包版本
base-基础版本，common-通用版本，enterprise-企业版本
        :type PackageVersion: str
        :param _PackageSpec: 资源包大小，计算资源单位：万个；存储资源：GB
        :type PackageSpec: float
        :param _ExpireDay: 资源包有效期，单位:天
        :type ExpireDay: int
        :param _PackageCount: 购买资源包个数
        :type PackageCount: int
        :param _PackageName: 资源包名称
        :type PackageName: str
        """
        self._InstanceType = None
        self._PackageRegion = None
        self._PackageType = None
        self._PackageVersion = None
        self._PackageSpec = None
        self._ExpireDay = None
        self._PackageCount = None
        self._PackageName = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def PackageSpec(self):
        return self._PackageSpec

    @PackageSpec.setter
    def PackageSpec(self, PackageSpec):
        self._PackageSpec = PackageSpec

    @property
    def ExpireDay(self):
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay

    @property
    def PackageCount(self):
        return self._PackageCount

    @PackageCount.setter
    def PackageCount(self, PackageCount):
        self._PackageCount = PackageCount

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._PackageVersion = params.get("PackageVersion")
        self._PackageSpec = params.get("PackageSpec")
        self._ExpireDay = params.get("ExpireDay")
        self._PackageCount = params.get("PackageCount")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourcePackageResponse(AbstractModel):
    """CreateResourcePackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealIds: 付费总订单号
        :type BigDealIds: list of str
        :param _DealNames: 每个物品对应一个dealName，业务需要根据dealName保证发货接口幂等
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CrossRegionBackupItem(AbstractModel):
    """跨地域备份各地域备份信息

    """

    def __init__(self):
        r"""
        :param _CrossRegion: 备份的目标地域
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossRegion: str
        :param _BackupId: 目标地域的备份任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupId: str
        :param _BackupStatus: 目标地域的备份状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: str
        """
        self._CrossRegion = None
        self._BackupId = None
        self._BackupStatus = None

    @property
    def CrossRegion(self):
        return self._CrossRegion

    @CrossRegion.setter
    def CrossRegion(self, CrossRegion):
        self._CrossRegion = CrossRegion

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupStatus(self):
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus


    def _deserialize(self, params):
        self._CrossRegion = params.get("CrossRegion")
        self._BackupId = params.get("BackupId")
        self._BackupStatus = params.get("BackupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbCluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        r"""
        :param _Status: 集群状态， 可选值如下:
creating: 创建中
running:运行中
isolating:隔离中
isolated:已隔离
activating:解隔离中
offlining:下线中
offlined:已下线
deleting:删除中
deleted:已删除
        :type Status: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Zone: 可用区
        :type Zone: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _Region: 地域
        :type Region: str
        :param _DbVersion: 数据库版本
        :type DbVersion: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceNum: 实例数
        :type InstanceNum: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _DbType: 引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DbType: str
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _StatusDesc: 集群状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _PayMode: 付费模式。0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _PeriodEndTime: 截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodEndTime: str
        :param _Vip: 集群读写vip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: 集群读写vport
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _ProjectID: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectID: int
        :param _VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _CynosVersion: cynos内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CynosVersion: str
        :param _StorageLimit: 存储容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        :param _RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _ProcessingTask: 正在处理的任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessingTask: str
        :param _Tasks: 集群的任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param _ResourceTags: 集群绑定的tag数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of Tag
        :param _DbMode: Db类型(NORMAL, SERVERLESS)
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param _ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
pause
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerlessStatus: str
        :param _Storage: 集群预付费存储值大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: int
        :param _StorageId: 集群存储为预付费时的存储ID，用于预付费存储变配
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param _StoragePayMode: 集群存储付费模式。0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePayMode: int
        :param _MinStorageSize: 集群计算规格对应的最小存储值
注意：此字段可能返回 null，表示取不到有效值。
        :type MinStorageSize: int
        :param _MaxStorageSize: 集群计算规格对应的最大存储值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStorageSize: int
        :param _NetAddrs: 集群网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NetAddrs: list of NetAddr
        :param _PhysicalZone: 物理可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalZone: str
        :param _MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param _HasSlaveZone: 是否有从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSlaveZone: str
        :param _SlaveZones: 从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        :param _BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param _IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param _OrderSource: 订单来源
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderSource: str
        :param _Ability: 能力
注意：此字段可能返回 null，表示取不到有效值。
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _ResourcePackages: 实例绑定资源包信息（此处只返回存储资源包，即packageType=DISK）	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePackages: list of ResourcePackage
        """
        self._Status = None
        self._UpdateTime = None
        self._Zone = None
        self._ClusterName = None
        self._Region = None
        self._DbVersion = None
        self._ClusterId = None
        self._InstanceNum = None
        self._Uin = None
        self._DbType = None
        self._AppId = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._Vip = None
        self._Vport = None
        self._ProjectID = None
        self._VpcId = None
        self._SubnetId = None
        self._CynosVersion = None
        self._StorageLimit = None
        self._RenewFlag = None
        self._ProcessingTask = None
        self._Tasks = None
        self._ResourceTags = None
        self._DbMode = None
        self._ServerlessStatus = None
        self._Storage = None
        self._StorageId = None
        self._StoragePayMode = None
        self._MinStorageSize = None
        self._MaxStorageSize = None
        self._NetAddrs = None
        self._PhysicalZone = None
        self._MasterZone = None
        self._HasSlaveZone = None
        self._SlaveZones = None
        self._BusinessType = None
        self._IsFreeze = None
        self._OrderSource = None
        self._Ability = None
        self._ResourcePackages = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

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
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ProcessingTask(self):
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def NetAddrs(self):
        return self._NetAddrs

    @NetAddrs.setter
    def NetAddrs(self, NetAddrs):
        self._NetAddrs = NetAddrs

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def HasSlaveZone(self):
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def OrderSource(self):
        return self._OrderSource

    @OrderSource.setter
    def OrderSource(self, OrderSource):
        self._OrderSource = OrderSource

    @property
    def Ability(self):
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._Zone = params.get("Zone")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._DbVersion = params.get("DbVersion")
        self._ClusterId = params.get("ClusterId")
        self._InstanceNum = params.get("InstanceNum")
        self._Uin = params.get("Uin")
        self._DbType = params.get("DbType")
        self._AppId = params.get("AppId")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._ProjectID = params.get("ProjectID")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CynosVersion = params.get("CynosVersion")
        self._StorageLimit = params.get("StorageLimit")
        self._RenewFlag = params.get("RenewFlag")
        self._ProcessingTask = params.get("ProcessingTask")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbMode = params.get("DbMode")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._Storage = params.get("Storage")
        self._StorageId = params.get("StorageId")
        self._StoragePayMode = params.get("StoragePayMode")
        self._MinStorageSize = params.get("MinStorageSize")
        self._MaxStorageSize = params.get("MaxStorageSize")
        if params.get("NetAddrs") is not None:
            self._NetAddrs = []
            for item in params.get("NetAddrs"):
                obj = NetAddr()
                obj._deserialize(item)
                self._NetAddrs.append(obj)
        self._PhysicalZone = params.get("PhysicalZone")
        self._MasterZone = params.get("MasterZone")
        self._HasSlaveZone = params.get("HasSlaveZone")
        self._SlaveZones = params.get("SlaveZones")
        self._BusinessType = params.get("BusinessType")
        self._IsFreeze = params.get("IsFreeze")
        self._OrderSource = params.get("OrderSource")
        if params.get("Ability") is not None:
            self._Ability = Ability()
            self._Ability._deserialize(params.get("Ability"))
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbClusterDetail(AbstractModel):
    """集群详情详细信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _PhysicalZone: 物理可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalZone: str
        :param _Status: 状态
        :type Status: str
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
resuming
pause
pausing
        :type ServerlessStatus: str
        :param _StorageId: 存储Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param _Storage: 存储大小，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: int
        :param _MaxStorageSize: 最大存储规格，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStorageSize: int
        :param _MinStorageSize: 最小存储规格，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type MinStorageSize: int
        :param _StoragePayMode: 存储付费类型，1为包年包月，0为按量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePayMode: int
        :param _VpcName: VPC名称
        :type VpcName: str
        :param _VpcId: vpc唯一id
        :type VpcId: str
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Charset: 字符集
        :type Charset: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _DbType: 数据库类型
        :type DbType: str
        :param _DbMode: 数据库类型，normal，serverless
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param _DbVersion: 数据库版本
        :type DbVersion: str
        :param _StorageLimit: 存储空间上限
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        :param _UsedStorage: 使用容量
        :type UsedStorage: int
        :param _Vip: vip地址
        :type Vip: str
        :param _Vport: vport端口
        :type Vport: int
        :param _RoAddr: 集群只读实例的vip地址和vport端口
        :type RoAddr: list of Addr
        :param _Ability: 集群支持的功能
注意：此字段可能返回 null，表示取不到有效值。
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param _CynosVersion: cynos版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CynosVersion: str
        :param _BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param _HasSlaveZone: 是否有从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSlaveZone: str
        :param _IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param _Tasks: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param _MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param _SlaveZones: 从可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        :param _InstanceSet: 实例信息
        :type InstanceSet: list of ClusterInstanceDetail
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _ProjectID: 项目id
        :type ProjectID: int
        :param _ResourceTags: 实例绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param _ProxyStatus: Proxy状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyStatus: str
        :param _LogBin: binlog开关，可选值：ON, OFF
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBin: str
        :param _IsSkipTrade: 是否跳过交易
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSkipTrade: str
        :param _PitrType: pitr类型，可选值：normal, redo_pitr
注意：此字段可能返回 null，表示取不到有效值。
        :type PitrType: str
        :param _IsOpenPasswordComplexity: 是否打开密码复杂度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpenPasswordComplexity: str
        :param _NetworkStatus: 网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkStatus: str
        :param _ResourcePackages: 集群绑定的资源包信息	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePackages: list of ResourcePackage
        :param _RenewFlag: 自动续费标识，1为自动续费，0为到期不续
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _NetworkType: 节点网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkType: str
        :param _SlaveZoneAttr: 备可用区属性
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZoneAttr: list of SlaveZoneAttrItem
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._Zone = None
        self._PhysicalZone = None
        self._Status = None
        self._StatusDesc = None
        self._ServerlessStatus = None
        self._StorageId = None
        self._Storage = None
        self._MaxStorageSize = None
        self._MinStorageSize = None
        self._StoragePayMode = None
        self._VpcName = None
        self._VpcId = None
        self._SubnetName = None
        self._SubnetId = None
        self._Charset = None
        self._CreateTime = None
        self._DbType = None
        self._DbMode = None
        self._DbVersion = None
        self._StorageLimit = None
        self._UsedStorage = None
        self._Vip = None
        self._Vport = None
        self._RoAddr = None
        self._Ability = None
        self._CynosVersion = None
        self._BusinessType = None
        self._HasSlaveZone = None
        self._IsFreeze = None
        self._Tasks = None
        self._MasterZone = None
        self._SlaveZones = None
        self._InstanceSet = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._ProjectID = None
        self._ResourceTags = None
        self._ProxyStatus = None
        self._LogBin = None
        self._IsSkipTrade = None
        self._PitrType = None
        self._IsOpenPasswordComplexity = None
        self._NetworkStatus = None
        self._ResourcePackages = None
        self._RenewFlag = None
        self._NetworkType = None
        self._SlaveZoneAttr = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def UsedStorage(self):
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def RoAddr(self):
        return self._RoAddr

    @RoAddr.setter
    def RoAddr(self, RoAddr):
        self._RoAddr = RoAddr

    @property
    def Ability(self):
        return self._Ability

    @Ability.setter
    def Ability(self, Ability):
        self._Ability = Ability

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def HasSlaveZone(self):
        return self._HasSlaveZone

    @HasSlaveZone.setter
    def HasSlaveZone(self, HasSlaveZone):
        self._HasSlaveZone = HasSlaveZone

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ProxyStatus(self):
        return self._ProxyStatus

    @ProxyStatus.setter
    def ProxyStatus(self, ProxyStatus):
        self._ProxyStatus = ProxyStatus

    @property
    def LogBin(self):
        return self._LogBin

    @LogBin.setter
    def LogBin(self, LogBin):
        self._LogBin = LogBin

    @property
    def IsSkipTrade(self):
        return self._IsSkipTrade

    @IsSkipTrade.setter
    def IsSkipTrade(self, IsSkipTrade):
        self._IsSkipTrade = IsSkipTrade

    @property
    def PitrType(self):
        return self._PitrType

    @PitrType.setter
    def PitrType(self, PitrType):
        self._PitrType = PitrType

    @property
    def IsOpenPasswordComplexity(self):
        return self._IsOpenPasswordComplexity

    @IsOpenPasswordComplexity.setter
    def IsOpenPasswordComplexity(self, IsOpenPasswordComplexity):
        self._IsOpenPasswordComplexity = IsOpenPasswordComplexity

    @property
    def NetworkStatus(self):
        return self._NetworkStatus

    @NetworkStatus.setter
    def NetworkStatus(self, NetworkStatus):
        self._NetworkStatus = NetworkStatus

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def SlaveZoneAttr(self):
        return self._SlaveZoneAttr

    @SlaveZoneAttr.setter
    def SlaveZoneAttr(self, SlaveZoneAttr):
        self._SlaveZoneAttr = SlaveZoneAttr


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._PhysicalZone = params.get("PhysicalZone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._StorageId = params.get("StorageId")
        self._Storage = params.get("Storage")
        self._MaxStorageSize = params.get("MaxStorageSize")
        self._MinStorageSize = params.get("MinStorageSize")
        self._StoragePayMode = params.get("StoragePayMode")
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        self._Charset = params.get("Charset")
        self._CreateTime = params.get("CreateTime")
        self._DbType = params.get("DbType")
        self._DbMode = params.get("DbMode")
        self._DbVersion = params.get("DbVersion")
        self._StorageLimit = params.get("StorageLimit")
        self._UsedStorage = params.get("UsedStorage")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        if params.get("RoAddr") is not None:
            self._RoAddr = []
            for item in params.get("RoAddr"):
                obj = Addr()
                obj._deserialize(item)
                self._RoAddr.append(obj)
        if params.get("Ability") is not None:
            self._Ability = Ability()
            self._Ability._deserialize(params.get("Ability"))
        self._CynosVersion = params.get("CynosVersion")
        self._BusinessType = params.get("BusinessType")
        self._HasSlaveZone = params.get("HasSlaveZone")
        self._IsFreeze = params.get("IsFreeze")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ClusterInstanceDetail()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._ProjectID = params.get("ProjectID")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ProxyStatus = params.get("ProxyStatus")
        self._LogBin = params.get("LogBin")
        self._IsSkipTrade = params.get("IsSkipTrade")
        self._PitrType = params.get("PitrType")
        self._IsOpenPasswordComplexity = params.get("IsOpenPasswordComplexity")
        self._NetworkStatus = params.get("NetworkStatus")
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        self._NetworkType = params.get("NetworkType")
        if params.get("SlaveZoneAttr") is not None:
            self._SlaveZoneAttr = []
            for item in params.get("SlaveZoneAttr"):
                obj = SlaveZoneAttrItem()
                obj._deserialize(item)
                self._SlaveZoneAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbErrorLogItem(AbstractModel):
    """实例错误日志返回类型

    """

    def __init__(self):
        r"""
        :param _Timestamp: 日志时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _Level: 日志等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param _Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Level = params.get("Level")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _Uin: 用户Uin
        :type Uin: str
        :param _AppId: 用户AppId
        :type AppId: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Status: 实例状态
        :type Status: str
        :param _StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param _DbMode: 实例形态，是否为serverless实例
        :type DbMode: str
        :param _DbType: 数据库类型
        :type DbType: str
        :param _DbVersion: 数据库版本
        :type DbVersion: str
        :param _Cpu: Cpu，单位：核
        :type Cpu: int
        :param _Memory: 内存，单位：GB
        :type Memory: int
        :param _Storage: 存储量，单位：GB
        :type Storage: int
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VpcId: VPC网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Vip: 实例内网IP
        :type Vip: str
        :param _Vport: 实例内网端口
        :type Vport: int
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param _DestroyDeadlineText: 销毁期限
        :type DestroyDeadlineText: str
        :param _IsolateTime: 隔离时间
        :type IsolateTime: str
        :param _NetType: 网络类型
        :type NetType: int
        :param _WanDomain: 外网域名
        :type WanDomain: str
        :param _WanIP: 外网IP
        :type WanIP: str
        :param _WanPort: 外网端口
        :type WanPort: int
        :param _WanStatus: 外网状态
        :type WanStatus: str
        :param _DestroyTime: 实例销毁时间
        :type DestroyTime: str
        :param _CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param _ProcessingTask: 正在处理的任务
        :type ProcessingTask: str
        :param _RenewFlag: 续费标志
        :type RenewFlag: int
        :param _MinCpu: serverless实例cpu下限
        :type MinCpu: float
        :param _MaxCpu: serverless实例cpu上限
        :type MaxCpu: float
        :param _ServerlessStatus: serverless实例状态, 可选值：
resume
pause
        :type ServerlessStatus: str
        :param _StorageId: 预付费存储Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param _StoragePayMode: 存储付费类型
        :type StoragePayMode: int
        :param _PhysicalZone: 物理区
        :type PhysicalZone: str
        :param _BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param _Tasks: 任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param _IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param _ResourceTags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of Tag
        :param _MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param _SlaveZones: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        :param _InstanceNetInfo: 实例网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNetInfo: list of InstanceNetInfo
        :param _ResourcePackages: 实例绑定资源包信息（此处只返回计算资源包，即packageType=CCU）
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePackages: list of ResourcePackage
        :param _InstanceIndexMode: 实例索引形态,可选值【mixedRowColumn（行列混存），onlyRowIndex（仅行存）】
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIndexMode: str
        :param _InstanceAbility: 当前实例支持的能力
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAbility: :class:`tencentcloud.cynosdb.v20190107.models.InstanceAbility`
        :param _DeviceType: 实例机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _InstanceStorageType: 实例存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStorageType: str
        """
        self._Uin = None
        self._AppId = None
        self._ClusterId = None
        self._ClusterName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._StatusDesc = None
        self._DbMode = None
        self._DbType = None
        self._DbVersion = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._InstanceRole = None
        self._UpdateTime = None
        self._CreateTime = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vport = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._DestroyDeadlineText = None
        self._IsolateTime = None
        self._NetType = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None
        self._DestroyTime = None
        self._CynosVersion = None
        self._ProcessingTask = None
        self._RenewFlag = None
        self._MinCpu = None
        self._MaxCpu = None
        self._ServerlessStatus = None
        self._StorageId = None
        self._StoragePayMode = None
        self._PhysicalZone = None
        self._BusinessType = None
        self._Tasks = None
        self._IsFreeze = None
        self._ResourceTags = None
        self._MasterZone = None
        self._SlaveZones = None
        self._InstanceNetInfo = None
        self._ResourcePackages = None
        self._InstanceIndexMode = None
        self._InstanceAbility = None
        self._DeviceType = None
        self._InstanceStorageType = None

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

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
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def DestroyDeadlineText(self):
        return self._DestroyDeadlineText

    @DestroyDeadlineText.setter
    def DestroyDeadlineText(self, DestroyDeadlineText):
        self._DestroyDeadlineText = DestroyDeadlineText

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def ProcessingTask(self):
        return self._ProcessingTask

    @ProcessingTask.setter
    def ProcessingTask(self, ProcessingTask):
        self._ProcessingTask = ProcessingTask

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def StorageId(self):
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def IsFreeze(self):
        return self._IsFreeze

    @IsFreeze.setter
    def IsFreeze(self, IsFreeze):
        self._IsFreeze = IsFreeze

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZones(self):
        return self._SlaveZones

    @SlaveZones.setter
    def SlaveZones(self, SlaveZones):
        self._SlaveZones = SlaveZones

    @property
    def InstanceNetInfo(self):
        return self._InstanceNetInfo

    @InstanceNetInfo.setter
    def InstanceNetInfo(self, InstanceNetInfo):
        self._InstanceNetInfo = InstanceNetInfo

    @property
    def ResourcePackages(self):
        return self._ResourcePackages

    @ResourcePackages.setter
    def ResourcePackages(self, ResourcePackages):
        self._ResourcePackages = ResourcePackages

    @property
    def InstanceIndexMode(self):
        return self._InstanceIndexMode

    @InstanceIndexMode.setter
    def InstanceIndexMode(self, InstanceIndexMode):
        self._InstanceIndexMode = InstanceIndexMode

    @property
    def InstanceAbility(self):
        return self._InstanceAbility

    @InstanceAbility.setter
    def InstanceAbility(self, InstanceAbility):
        self._InstanceAbility = InstanceAbility

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceStorageType(self):
        return self._InstanceStorageType

    @InstanceStorageType.setter
    def InstanceStorageType(self, InstanceStorageType):
        self._InstanceStorageType = InstanceStorageType


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DbMode = params.get("DbMode")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._InstanceRole = params.get("InstanceRole")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._DestroyDeadlineText = params.get("DestroyDeadlineText")
        self._IsolateTime = params.get("IsolateTime")
        self._NetType = params.get("NetType")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        self._DestroyTime = params.get("DestroyTime")
        self._CynosVersion = params.get("CynosVersion")
        self._ProcessingTask = params.get("ProcessingTask")
        self._RenewFlag = params.get("RenewFlag")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._StorageId = params.get("StorageId")
        self._StoragePayMode = params.get("StoragePayMode")
        self._PhysicalZone = params.get("PhysicalZone")
        self._BusinessType = params.get("BusinessType")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._IsFreeze = params.get("IsFreeze")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._MasterZone = params.get("MasterZone")
        self._SlaveZones = params.get("SlaveZones")
        if params.get("InstanceNetInfo") is not None:
            self._InstanceNetInfo = []
            for item in params.get("InstanceNetInfo"):
                obj = InstanceNetInfo()
                obj._deserialize(item)
                self._InstanceNetInfo.append(obj)
        if params.get("ResourcePackages") is not None:
            self._ResourcePackages = []
            for item in params.get("ResourcePackages"):
                obj = ResourcePackage()
                obj._deserialize(item)
                self._ResourcePackages.append(obj)
        self._InstanceIndexMode = params.get("InstanceIndexMode")
        if params.get("InstanceAbility") is not None:
            self._InstanceAbility = InstanceAbility()
            self._InstanceAbility._deserialize(params.get("InstanceAbility"))
        self._DeviceType = params.get("DeviceType")
        self._InstanceStorageType = params.get("InstanceStorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        r"""
        :param _Uin: 用户Uin
        :type Uin: str
        :param _AppId: 用户AppId
        :type AppId: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Status: 实例状态
        :type Status: str
        :param _StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param _ServerlessStatus: serverless实例状态, 可能值：
resume
pause
        :type ServerlessStatus: str
        :param _DbType: 数据库类型
        :type DbType: str
        :param _DbVersion: 数据库版本
        :type DbVersion: str
        :param _Cpu: Cpu，单位：核
        :type Cpu: int
        :param _Memory: 内存，单位：GB
        :type Memory: int
        :param _Storage: 存储量，单位：GB
        :type Storage: int
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param _NetType: 网络类型
        :type NetType: int
        :param _VpcId: VPC网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Vip: 实例内网IP
        :type Vip: str
        :param _Vport: 实例内网端口
        :type Vport: int
        :param _WanDomain: 实例外网域名
        :type WanDomain: str
        :param _Charset: 字符集
        :type Charset: str
        :param _CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param _RenewFlag: 续费标志
        :type RenewFlag: int
        :param _MinCpu: serverless实例cpu下限
        :type MinCpu: float
        :param _MaxCpu: serverless实例cpu上限
        :type MaxCpu: float
        """
        self._Uin = None
        self._AppId = None
        self._ClusterId = None
        self._ClusterName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._StatusDesc = None
        self._ServerlessStatus = None
        self._DbType = None
        self._DbVersion = None
        self._Cpu = None
        self._Memory = None
        self._Storage = None
        self._InstanceType = None
        self._InstanceRole = None
        self._UpdateTime = None
        self._CreateTime = None
        self._PayMode = None
        self._PeriodEndTime = None
        self._NetType = None
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._Charset = None
        self._CynosVersion = None
        self._RenewFlag = None
        self._MinCpu = None
        self._MaxCpu = None

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ServerlessStatus(self):
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

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
    def PeriodEndTime(self):
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._ServerlessStatus = params.get("ServerlessStatus")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        self._InstanceType = params.get("InstanceType")
        self._InstanceRole = params.get("InstanceRole")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._NetType = params.get("NetType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._Charset = params.get("Charset")
        self._CynosVersion = params.get("CynosVersion")
        self._RenewFlag = params.get("RenewFlag")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGroup(AbstractModel):
    """实例组信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户appId
        :type AppId: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _DeletedTime: 删除时间
        :type DeletedTime: str
        :param _InstanceGroupId: 实例组ID
        :type InstanceGroupId: str
        :param _Status: 状态
        :type Status: str
        :param _Type: 实例组类型。ha-ha组；ro-只读组
        :type Type: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _Vip: 内网IP
        :type Vip: str
        :param _Vport: 内网端口
        :type Vport: int
        :param _WanDomain: 外网域名
        :type WanDomain: str
        :param _WanIP: 外网ip
        :type WanIP: str
        :param _WanPort: 外网端口
        :type WanPort: int
        :param _WanStatus: 外网状态
        :type WanStatus: str
        :param _InstanceSet: 实例组包含实例信息
        :type InstanceSet: list of CynosdbInstance
        :param _UniqVpcId: VPC的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _OldAddrInfo: 正在回收IP信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OldAddrInfo: :class:`tencentcloud.cynosdb.v20190107.models.OldAddrInfo`
        :param _ProcessingTasks: 正在进行的任务
        :type ProcessingTasks: list of str
        :param _Tasks: 任务列表
        :type Tasks: list of ObjectTask
        :param _NetServiceId: biz_net_service表id
        :type NetServiceId: int
        """
        self._AppId = None
        self._ClusterId = None
        self._CreatedTime = None
        self._DeletedTime = None
        self._InstanceGroupId = None
        self._Status = None
        self._Type = None
        self._UpdatedTime = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None
        self._InstanceSet = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldAddrInfo = None
        self._ProcessingTasks = None
        self._Tasks = None
        self._NetServiceId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DeletedTime(self):
        return self._DeletedTime

    @DeletedTime.setter
    def DeletedTime(self, DeletedTime):
        self._DeletedTime = DeletedTime

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldAddrInfo(self):
        return self._OldAddrInfo

    @OldAddrInfo.setter
    def OldAddrInfo(self, OldAddrInfo):
        self._OldAddrInfo = OldAddrInfo

    @property
    def ProcessingTasks(self):
        return self._ProcessingTasks

    @ProcessingTasks.setter
    def ProcessingTasks(self, ProcessingTasks):
        self._ProcessingTasks = ProcessingTasks

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def NetServiceId(self):
        return self._NetServiceId

    @NetServiceId.setter
    def NetServiceId(self, NetServiceId):
        self._NetServiceId = NetServiceId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._CreatedTime = params.get("CreatedTime")
        self._DeletedTime = params.get("DeletedTime")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("OldAddrInfo") is not None:
            self._OldAddrInfo = OldAddrInfo()
            self._OldAddrInfo._deserialize(params.get("OldAddrInfo"))
        self._ProcessingTasks = params.get("ProcessingTasks")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._NetServiceId = params.get("NetServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGrp(AbstractModel):
    """实例组信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户appId
        :type AppId: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _DeletedTime: 删除时间
        :type DeletedTime: str
        :param _InstanceGrpId: 实例组ID
        :type InstanceGrpId: str
        :param _Status: 状态
        :type Status: str
        :param _Type: 实例组类型。ha-ha组；ro-只读组
        :type Type: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _Vip: 内网IP
        :type Vip: str
        :param _Vport: 内网端口
        :type Vport: int
        :param _WanDomain: 外网域名
        :type WanDomain: str
        :param _WanIP: 外网ip
        :type WanIP: str
        :param _WanPort: 外网端口
        :type WanPort: int
        :param _WanStatus: 外网状态
        :type WanStatus: str
        :param _InstanceSet: 实例组包含实例信息
        :type InstanceSet: list of CynosdbInstance
        :param _UniqVpcId: VPC的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _OldAddrInfo: 正在回收IP信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OldAddrInfo: :class:`tencentcloud.cynosdb.v20190107.models.OldAddrInfo`
        :param _ProcessingTasks: 正在进行的任务
        :type ProcessingTasks: list of str
        :param _Tasks: 任务列表
        :type Tasks: list of ObjectTask
        :param _NetServiceId: biz_net_service表id
        :type NetServiceId: int
        """
        self._AppId = None
        self._ClusterId = None
        self._CreatedTime = None
        self._DeletedTime = None
        self._InstanceGrpId = None
        self._Status = None
        self._Type = None
        self._UpdatedTime = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None
        self._InstanceSet = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldAddrInfo = None
        self._ProcessingTasks = None
        self._Tasks = None
        self._NetServiceId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DeletedTime(self):
        return self._DeletedTime

    @DeletedTime.setter
    def DeletedTime(self, DeletedTime):
        self._DeletedTime = DeletedTime

    @property
    def InstanceGrpId(self):
        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        self._InstanceGrpId = InstanceGrpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldAddrInfo(self):
        return self._OldAddrInfo

    @OldAddrInfo.setter
    def OldAddrInfo(self, OldAddrInfo):
        self._OldAddrInfo = OldAddrInfo

    @property
    def ProcessingTasks(self):
        return self._ProcessingTasks

    @ProcessingTasks.setter
    def ProcessingTasks(self, ProcessingTasks):
        self._ProcessingTasks = ProcessingTasks

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def NetServiceId(self):
        return self._NetServiceId

    @NetServiceId.setter
    def NetServiceId(self, NetServiceId):
        self._NetServiceId = NetServiceId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._CreatedTime = params.get("CreatedTime")
        self._DeletedTime = params.get("DeletedTime")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("OldAddrInfo") is not None:
            self._OldAddrInfo = OldAddrInfo()
            self._OldAddrInfo._deserialize(params.get("OldAddrInfo"))
        self._ProcessingTasks = params.get("ProcessingTasks")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._NetServiceId = params.get("NetServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivileges(AbstractModel):
    """数据库权限列表

    """

    def __init__(self):
        r"""
        :param _Db: 数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param _Privileges: 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Privileges: list of str
        """
        self._Db = None
        self._Privileges = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTables(AbstractModel):
    """数据库表信息

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Tables: 表名称列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of str
        """
        self._Database = None
        self._Tables = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbInfo(AbstractModel):
    """数据库详细信息

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _CharacterSet: 字符集类型
        :type CharacterSet: str
        :param _Status: 数据库状态
        :type Status: str
        :param _CollateRule: 排序规则
        :type CollateRule: str
        :param _Description: 数据库备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _UserHostPrivileges: 用户权限
注意：此字段可能返回 null，表示取不到有效值。
        :type UserHostPrivileges: list of UserHostPrivilege
        :param _DbId: 数据库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DbId: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _ClusterId: 集群Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._DbName = None
        self._CharacterSet = None
        self._Status = None
        self._CollateRule = None
        self._Description = None
        self._UserHostPrivileges = None
        self._DbId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Uin = None
        self._ClusterId = None

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CollateRule(self):
        return self._CollateRule

    @CollateRule.setter
    def CollateRule(self, CollateRule):
        self._CollateRule = CollateRule

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserHostPrivileges(self):
        return self._UserHostPrivileges

    @UserHostPrivileges.setter
    def UserHostPrivileges(self, UserHostPrivileges):
        self._UserHostPrivileges = UserHostPrivileges

    @property
    def DbId(self):
        return self._DbId

    @DbId.setter
    def DbId(self, DbId):
        self._DbId = DbId

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
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._CharacterSet = params.get("CharacterSet")
        self._Status = params.get("Status")
        self._CollateRule = params.get("CollateRule")
        self._Description = params.get("Description")
        if params.get("UserHostPrivileges") is not None:
            self._UserHostPrivileges = []
            for item in params.get("UserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._UserHostPrivileges.append(obj)
        self._DbId = params.get("DbId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbTable(AbstractModel):
    """数据库表

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名称
        :type Db: str
        :param _TableName: 数据库表名称
        :type TableName: str
        """
        self._Db = None
        self._TableName = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Accounts: 账号数组，包含account和host
        :type Accounts: list of InputAccount
        """
        self._ClusterId = None
        self._Accounts = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = InputAccount()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts返回参数结构体

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


class DeleteAuditLogFileRequest(AbstractModel):
    """DeleteAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileName: 审计日志文件名称。
        :type FileName: str
        """
        self._InstanceId = None
        self._FileName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditLogFileResponse(AbstractModel):
    """DeleteAuditLogFile返回参数结构体

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


class DeleteAuditRuleTemplatesRequest(AbstractModel):
    """DeleteAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: 审计规则模板ID。
        :type RuleTemplateIds: list of str
        """
        self._RuleTemplateIds = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditRuleTemplatesResponse(AbstractModel):
    """DeleteAuditRuleTemplates返回参数结构体

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


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _SnapshotIdList: 备份文件ID，旧版本使用的字段，不推荐使用
        :type SnapshotIdList: list of int
        :param _BackupIds: 备份文件ID，推荐使用
        :type BackupIds: list of int
        """
        self._ClusterId = None
        self._SnapshotIdList = None
        self._BackupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SnapshotIdList(self):
        return self._SnapshotIdList

    @SnapshotIdList.setter
    def SnapshotIdList(self, SnapshotIdList):
        self._SnapshotIdList = SnapshotIdList

    @property
    def BackupIds(self):
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SnapshotIdList = params.get("SnapshotIdList")
        self._BackupIds = params.get("BackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回参数结构体

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


class DeleteCLSDeliveryRequest(AbstractModel):
    """DeleteCLSDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _CLSTopicIds: 日志主题id
        :type CLSTopicIds: list of str
        :param _LogType: 日志类型
        :type LogType: str
        :param _IsInMaintainPeriod: 是否维护时间运行
        :type IsInMaintainPeriod: str
        """
        self._InstanceId = None
        self._CLSTopicIds = None
        self._LogType = None
        self._IsInMaintainPeriod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CLSTopicIds(self):
        return self._CLSTopicIds

    @CLSTopicIds.setter
    def CLSTopicIds(self, CLSTopicIds):
        self._CLSTopicIds = CLSTopicIds

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CLSTopicIds = params.get("CLSTopicIds")
        self._LogType = params.get("LogType")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCLSDeliveryResponse(AbstractModel):
    """DeleteCLSDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务id

        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteClusterDatabaseRequest(AbstractModel):
    """DeleteClusterDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _DbNames: 数据库名
        :type DbNames: list of str
        """
        self._ClusterId = None
        self._DbNames = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbNames(self):
        return self._DbNames

    @DbNames.setter
    def DbNames(self, DbNames):
        self._DbNames = DbNames


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbNames = params.get("DbNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterDatabaseResponse(AbstractModel):
    """DeleteClusterDatabase返回参数结构体

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


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate返回参数结构体

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


class DeliverSummary(AbstractModel):
    """日志投递信息

    """

    def __init__(self):
        r"""
        :param _DeliverType: 投递类型，store（存储类），mq（消息通道）
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverType: str
        :param _DeliverSubType: 投递子类型：cls，ckafka。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverSubType: str
        """
        self._DeliverType = None
        self._DeliverSubType = None

    @property
    def DeliverType(self):
        return self._DeliverType

    @DeliverType.setter
    def DeliverType(self, DeliverType):
        self._DeliverType = DeliverType

    @property
    def DeliverSubType(self):
        return self._DeliverSubType

    @DeliverSubType.setter
    def DeliverSubType(self, DeliverSubType):
        self._DeliverSubType = DeliverSubType


    def _deserialize(self, params):
        self._DeliverType = params.get("DeliverType")
        self._DeliverSubType = params.get("DeliverSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountAllGrantPrivilegesRequest(AbstractModel):
    """DescribeAccountAllGrantPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
        self._ClusterId = None
        self._Account = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountAllGrantPrivilegesResponse(AbstractModel):
    """DescribeAccountAllGrantPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivilegeStatements: 权限语句
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivilegeStatements: list of str
        :param _GlobalPrivileges: 全局权限
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: 数据库权限
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabasePrivileges: list of DatabasePrivileges
        :param _TablePrivileges: 数据库表权限
注意：此字段可能返回 null，表示取不到有效值。
        :type TablePrivileges: list of TablePrivileges
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivilegeStatements = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._RequestId = None

    @property
    def PrivilegeStatements(self):
        return self._PrivilegeStatements

    @PrivilegeStatements.setter
    def PrivilegeStatements(self, PrivilegeStatements):
        self._PrivilegeStatements = PrivilegeStatements

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PrivilegeStatements = params.get("PrivilegeStatements")
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _AccountName: 账户名
        :type AccountName: str
        :param _Host: 主机
        :type Host: str
        :param _Db: 数据库名，为*时，忽略Type/TableName, 表示修改用户全局权限；
        :type Db: str
        :param _Type: 指定数据库下的对象类型，可选"table"，"*"
        :type Type: str
        :param _TableName: 当Type="table"时，用来指定表名
        :type TableName: str
        """
        self._ClusterId = None
        self._AccountName = None
        self._Host = None
        self._Db = None
        self._Type = None
        self._TableName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountName = params.get("AccountName")
        self._Host = params.get("Host")
        self._Db = params.get("Db")
        self._Type = params.get("Type")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Privileges: 权限列表，示例值为：["","select","update","delete","create","drop","references","index","alter","show_db","create_tmp_table","lock_tables","execute","create_view","show_view","create_routine","alter_routine","event","trigger"]
        :type Privileges: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Privileges = None
        self._RequestId = None

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _AccountNames: 需要过滤的账户列表
        :type AccountNames: list of str
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
该参数已废用
        :type DbType: str
        :param _Hosts: 需要过滤的账户列表
        :type Hosts: list of str
        :param _Limit: 限制量
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _AccountRegular: 模糊匹配关键字(同时匹配AccountName和AccountHost，返回并集结果，支持正则)
        :type AccountRegular: str
        """
        self._ClusterId = None
        self._AccountNames = None
        self._DbType = None
        self._Hosts = None
        self._Limit = None
        self._Offset = None
        self._AccountRegular = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountNames(self):
        return self._AccountNames

    @AccountNames.setter
    def AccountNames(self, AccountNames):
        self._AccountNames = AccountNames

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

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
    def AccountRegular(self):
        return self._AccountRegular

    @AccountRegular.setter
    def AccountRegular(self, AccountRegular):
        self._AccountRegular = AccountRegular


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountNames = params.get("AccountNames")
        self._DbType = params.get("DbType")
        self._Hosts = params.get("Hosts")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountRegular = params.get("AccountRegular")
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
        :param _AccountSet: 数据库账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountSet: list of Account
        :param _TotalCount: 账号总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

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
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAuditInstanceListRequest(AbstractModel):
    """DescribeAuditInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditSwitch: 实例审计开启的状态。1-已开启审计；0-未开启审计。
        :type AuditSwitch: int
        :param _Filters: 查询实例列表的过滤条件。
        :type Filters: list of AuditInstanceFilters
        :param _AuditMode: 实例的审计规则模式。1-规则审计；0-全审计。
        :type AuditMode: int
        :param _Limit: 单次请求返回的数量。默认值为30，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认值为 0。
        :type Offset: int
        """
        self._AuditSwitch = None
        self._Filters = None
        self._AuditMode = None
        self._Limit = None
        self._Offset = None

    @property
    def AuditSwitch(self):
        return self._AuditSwitch

    @AuditSwitch.setter
    def AuditSwitch(self, AuditSwitch):
        self._AuditSwitch = AuditSwitch

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AuditMode(self):
        return self._AuditMode

    @AuditMode.setter
    def AuditMode(self, AuditMode):
        self._AuditMode = AuditMode

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
        self._AuditSwitch = params.get("AuditSwitch")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AuditInstanceFilters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AuditMode = params.get("AuditMode")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditInstanceListResponse(AbstractModel):
    """DescribeAuditInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 审计实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of InstanceAuditStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceAuditStatus()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogFilesRequest(AbstractModel):
    """DescribeAuditLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _FileName: 审计日志文件名。
        :type FileName: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._FileName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogFilesResponse(AbstractModel):
    """DescribeAuditLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计日志文件个数。
        :type TotalCount: int
        :param _Items: 审计日志文件详情。
        :type Items: list of AuditLogFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLogFile()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogsRequest(AbstractModel):
    """DescribeAuditLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 开始时间，格式为："2017-07-12 10:29:20"。
        :type StartTime: str
        :param _EndTime: 结束时间，格式为："2017-07-12 10:29:20"。
        :type EndTime: str
        :param _Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param _OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param _Filter: 已废弃。
        :type Filter: :class:`tencentcloud.cynosdb.v20190107.models.AuditLogFilter`
        :param _Limit: 分页参数，单次返回的数据条数。默认值为100，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _LogFilter: 过滤条件。多个值之前是且的关系。
        :type LogFilter: list of InstanceAuditLogFilter
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None
        self._Limit = None
        self._Offset = None
        self._LogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

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
    def LogFilter(self):
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = AuditLogFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = InstanceAuditLogFilter()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogsResponse(AbstractModel):
    """DescribeAuditLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的审计日志条数。
        :type TotalCount: int
        :param _Items: 审计日志详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLog()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditRuleTemplatesRequest(AbstractModel):
    """DescribeAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: 规则模板ID。
        :type RuleTemplateIds: list of str
        :param _RuleTemplateNames: 规则模板名称
        :type RuleTemplateNames: list of str
        :param _Limit: 单次请求返回的数量。默认值20。
        :type Limit: int
        :param _Offset: 偏移量，默认值为 0。
        :type Offset: int
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险。
        :type AlarmLevel: int
        :param _AlarmPolicy: 告警策略。0-不告警，1-告警。
        :type AlarmPolicy: int
        """
        self._RuleTemplateIds = None
        self._RuleTemplateNames = None
        self._Limit = None
        self._Offset = None
        self._AlarmLevel = None
        self._AlarmPolicy = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleTemplateNames(self):
        return self._RuleTemplateNames

    @RuleTemplateNames.setter
    def RuleTemplateNames(self, RuleTemplateNames):
        self._RuleTemplateNames = RuleTemplateNames

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
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        self._RuleTemplateNames = params.get("RuleTemplateNames")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleTemplatesResponse(AbstractModel):
    """DescribeAuditRuleTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param _Items: 规则模板详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditRuleTemplateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditRuleTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditRuleWithInstanceIdsRequest(AbstractModel):
    """DescribeAuditRuleWithInstanceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID。目前仅支持单个实例的查询。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleWithInstanceIdsResponse(AbstractModel):
    """DescribeAuditRuleWithInstanceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 无
        :type TotalCount: int
        :param _Items: 实例审计规则信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of InstanceAuditRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceAuditRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param _BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param _ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800
        :type ReserveDuration: int
        :param _BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupFreq: list of str
        :param _BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupType: str
        :param _LogicCrossRegionsConfigUpdateTime: 跨地域逻辑备份配置修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicCrossRegionsConfigUpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None
        self._LogicCrossRegionsConfigUpdateTime = None
        self._RequestId = None

    @property
    def BackupTimeBeg(self):
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def LogicCrossRegionsConfigUpdateTime(self):
        return self._LogicCrossRegionsConfigUpdateTime

    @LogicCrossRegionsConfigUpdateTime.setter
    def LogicCrossRegionsConfigUpdateTime(self, LogicCrossRegionsConfigUpdateTime):
        self._LogicCrossRegionsConfigUpdateTime = LogicCrossRegionsConfigUpdateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupTimeBeg = params.get("BackupTimeBeg")
        self._BackupTimeEnd = params.get("BackupTimeEnd")
        self._ReserveDuration = params.get("ReserveDuration")
        self._BackupFreq = params.get("BackupFreq")
        self._BackupType = params.get("BackupType")
        self._LogicCrossRegionsConfigUpdateTime = params.get("LogicCrossRegionsConfigUpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadUrlRequest(AbstractModel):
    """DescribeBackupDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BackupId: 备份ID
        :type BackupId: int
        """
        self._ClusterId = None
        self._BackupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadUrlResponse(AbstractModel):
    """DescribeBackupDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 备份下载地址
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

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
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Limit: 返回数量，取值范围(0,100]
        :type Limit: int
        :param _Offset: 记录偏移量，取值范围[0,INF)
        :type Offset: int
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param _BackupIds: 备份ID
        :type BackupIds: list of int
        :param _BackupType: 备份类型，可选值：snapshot，快照备份； logic，逻辑备份
        :type BackupType: str
        :param _BackupMethod: 备份方式，可选值：auto，自动备份；manual，手动备份
        :type BackupMethod: str
        :param _SnapShotType: 快照类型，可选值：full，全量；increment，增量
        :type SnapShotType: str
        :param _StartTime: 备份开始时间
        :type StartTime: str
        :param _EndTime: 备份结束时间
        :type EndTime: str
        :param _FileNames: 备份文件名，模糊查询
        :type FileNames: list of str
        :param _BackupNames: 备份备注名，模糊查询
        :type BackupNames: list of str
        :param _SnapshotIdList: 快照备份Id列表
        :type SnapshotIdList: list of int
        :param _BackupRegion: 备份地域
        :type BackupRegion: str
        :param _IsCrossRegionsBackup: 是否跨地域备份
        :type IsCrossRegionsBackup: str
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._DbType = None
        self._BackupIds = None
        self._BackupType = None
        self._BackupMethod = None
        self._SnapShotType = None
        self._StartTime = None
        self._EndTime = None
        self._FileNames = None
        self._BackupNames = None
        self._SnapshotIdList = None
        self._BackupRegion = None
        self._IsCrossRegionsBackup = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def BackupIds(self):
        return self._BackupIds

    @BackupIds.setter
    def BackupIds(self, BackupIds):
        self._BackupIds = BackupIds

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def SnapShotType(self):
        return self._SnapShotType

    @SnapShotType.setter
    def SnapShotType(self, SnapShotType):
        self._SnapShotType = SnapShotType

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
    def FileNames(self):
        return self._FileNames

    @FileNames.setter
    def FileNames(self, FileNames):
        self._FileNames = FileNames

    @property
    def BackupNames(self):
        return self._BackupNames

    @BackupNames.setter
    def BackupNames(self, BackupNames):
        self._BackupNames = BackupNames

    @property
    def SnapshotIdList(self):
        return self._SnapshotIdList

    @SnapshotIdList.setter
    def SnapshotIdList(self, SnapshotIdList):
        self._SnapshotIdList = SnapshotIdList

    @property
    def BackupRegion(self):
        return self._BackupRegion

    @BackupRegion.setter
    def BackupRegion(self, BackupRegion):
        self._BackupRegion = BackupRegion

    @property
    def IsCrossRegionsBackup(self):
        return self._IsCrossRegionsBackup

    @IsCrossRegionsBackup.setter
    def IsCrossRegionsBackup(self, IsCrossRegionsBackup):
        self._IsCrossRegionsBackup = IsCrossRegionsBackup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DbType = params.get("DbType")
        self._BackupIds = params.get("BackupIds")
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._SnapShotType = params.get("SnapShotType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FileNames = params.get("FileNames")
        self._BackupNames = params.get("BackupNames")
        self._SnapshotIdList = params.get("SnapshotIdList")
        self._BackupRegion = params.get("BackupRegion")
        self._IsCrossRegionsBackup = params.get("IsCrossRegionsBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总共备份文件个数
        :type TotalCount: int
        :param _BackupList: 备份文件列表
        :type BackupList: list of BackupFileInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupList(self):
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = BackupFileInfo()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBinlogConfigRequest(AbstractModel):
    """DescribeBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogConfigResponse(AbstractModel):
    """DescribeBinlogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BinlogCrossRegionsConfigUpdateTime: Binlog跨地域配置更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogCrossRegionsConfigUpdateTime: str
        :param _BinlogConfig: Binlog配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogConfig: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BinlogCrossRegionsConfigUpdateTime = None
        self._BinlogConfig = None
        self._RequestId = None

    @property
    def BinlogCrossRegionsConfigUpdateTime(self):
        return self._BinlogCrossRegionsConfigUpdateTime

    @BinlogCrossRegionsConfigUpdateTime.setter
    def BinlogCrossRegionsConfigUpdateTime(self, BinlogCrossRegionsConfigUpdateTime):
        self._BinlogCrossRegionsConfigUpdateTime = BinlogCrossRegionsConfigUpdateTime

    @property
    def BinlogConfig(self):
        return self._BinlogConfig

    @BinlogConfig.setter
    def BinlogConfig(self, BinlogConfig):
        self._BinlogConfig = BinlogConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogCrossRegionsConfigUpdateTime = params.get("BinlogCrossRegionsConfigUpdateTime")
        if params.get("BinlogConfig") is not None:
            self._BinlogConfig = BinlogConfigInfo()
            self._BinlogConfig._deserialize(params.get("BinlogConfig"))
        self._RequestId = params.get("RequestId")


class DescribeBinlogDownloadUrlRequest(AbstractModel):
    """DescribeBinlogDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BinlogId: Binlog文件ID
        :type BinlogId: int
        """
        self._ClusterId = None
        self._BinlogId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogId(self):
        return self._BinlogId

    @BinlogId.setter
    def BinlogId(self, BinlogId):
        self._BinlogId = BinlogId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogDownloadUrlResponse(AbstractModel):
    """DescribeBinlogDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

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
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeBinlogSaveDaysRequest(AbstractModel):
    """DescribeBinlogSaveDays请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogSaveDaysResponse(AbstractModel):
    """DescribeBinlogSaveDays返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BinlogSaveDays: Binlog保留天数
        :type BinlogSaveDays: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BinlogSaveDays = None
        self._RequestId = None

    @property
    def BinlogSaveDays(self):
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        self._RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制条数
        :type Limit: int
        """
        self._ClusterId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._StartTime = params.get("StartTime")
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
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总条数
        :type TotalCount: int
        :param _Binlogs: Binlog列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Binlogs: list of BinlogItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Binlogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Binlogs(self):
        return self._Binlogs

    @Binlogs.setter
    def Binlogs(self, Binlogs):
        self._Binlogs = Binlogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Binlogs") is not None:
            self._Binlogs = []
            for item in params.get("Binlogs"):
                obj = BinlogItem()
                obj._deserialize(item)
                self._Binlogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChangedParamsAfterUpgradeRequest(AbstractModel):
    """DescribeChangedParamsAfterUpgrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _DstCpu: 变配后的CPU
        :type DstCpu: int
        :param _DstMem: 变配后的MEM，单位G
        :type DstMem: int
        """
        self._InstanceId = None
        self._DstCpu = None
        self._DstMem = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DstCpu(self):
        return self._DstCpu

    @DstCpu.setter
    def DstCpu(self, DstCpu):
        self._DstCpu = DstCpu

    @property
    def DstMem(self):
        return self._DstMem

    @DstMem.setter
    def DstMem(self, DstMem):
        self._DstMem = DstMem


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DstCpu = params.get("DstCpu")
        self._DstMem = params.get("DstMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChangedParamsAfterUpgradeResponse(AbstractModel):
    """DescribeChangedParamsAfterUpgrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数个数
        :type TotalCount: int
        :param _Items: 实例参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ParamItemInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamItemInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterDatabasesRequest(AbstractModel):
    """DescribeClusterDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页限制数量
        :type Limit: int
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDatabasesResponse(AbstractModel):
    """DescribeClusterDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Databases: 数据库列表
        :type Databases: list of str
        :param _Limit: 分页限制数
        :type Limit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Databases = None
        self._Limit = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Databases = params.get("Databases")
        self._Limit = params.get("Limit")
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailDatabasesRequest(AbstractModel):
    """DescribeClusterDetailDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 返回数量，默认20,最大100
        :type Limit: int
        :param _DbName: 数据库名称
        :type DbName: str
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._DbName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailDatabasesResponse(AbstractModel):
    """DescribeClusterDetailDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DbInfos: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DbInfos: list of DbInfo
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DbInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DbInfos(self):
        return self._DbInfos

    @DbInfos.setter
    def DbInfos(self, DbInfos):
        self._DbInfos = DbInfos

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
        if params.get("DbInfos") is not None:
            self._DbInfos = []
            for item in params.get("DbInfos"):
                obj = DbInfo()
                obj._deserialize(item)
                self._DbInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Detail: 集群详细信息
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self._Detail = CynosdbClusterDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeClusterInstanceGroupsRequest(AbstractModel):
    """DescribeClusterInstanceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstanceGroupsResponse(AbstractModel):
    """DescribeClusterInstanceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例组个数
        :type TotalCount: int
        :param _InstanceGroupInfoList: 实例组列表
        :type InstanceGroupInfoList: list of CynosdbInstanceGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceGroupInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceGroupInfoList(self):
        return self._InstanceGroupInfoList

    @InstanceGroupInfoList.setter
    def InstanceGroupInfoList(self, InstanceGroupInfoList):
        self._InstanceGroupInfoList = InstanceGroupInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceGroupInfoList") is not None:
            self._InstanceGroupInfoList = []
            for item in params.get("InstanceGroupInfoList"):
                obj = CynosdbInstanceGroup()
                obj._deserialize(item)
                self._InstanceGroupInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例组个数
        :type TotalCount: int
        :param _InstanceGrpInfoList: 实例组列表
        :type InstanceGrpInfoList: list of CynosdbInstanceGrp
        :param _InstanceGroupInfoList: 实例组列表
        :type InstanceGroupInfoList: list of CynosdbInstanceGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceGrpInfoList = None
        self._InstanceGroupInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceGrpInfoList(self):
        warnings.warn("parameter `InstanceGrpInfoList` is deprecated", DeprecationWarning) 

        return self._InstanceGrpInfoList

    @InstanceGrpInfoList.setter
    def InstanceGrpInfoList(self, InstanceGrpInfoList):
        warnings.warn("parameter `InstanceGrpInfoList` is deprecated", DeprecationWarning) 

        self._InstanceGrpInfoList = InstanceGrpInfoList

    @property
    def InstanceGroupInfoList(self):
        return self._InstanceGroupInfoList

    @InstanceGroupInfoList.setter
    def InstanceGroupInfoList(self, InstanceGroupInfoList):
        self._InstanceGroupInfoList = InstanceGroupInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceGrpInfoList") is not None:
            self._InstanceGrpInfoList = []
            for item in params.get("InstanceGrpInfoList"):
                obj = CynosdbInstanceGrp()
                obj._deserialize(item)
                self._InstanceGrpInfoList.append(obj)
        if params.get("InstanceGroupInfoList") is not None:
            self._InstanceGroupInfoList = []
            for item in params.get("InstanceGroupInfoList"):
                obj = CynosdbInstanceGroup()
                obj._deserialize(item)
                self._InstanceGroupInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterParamLogsRequest(AbstractModel):
    """DescribeClusterParamLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIds: 实例ID列表，用来记录具体操作哪些实例
        :type InstanceIds: list of str
        :param _OrderBy: 排序字段，定义在回返结果的基于哪个字段进行排序
        :type OrderBy: str
        :param _OrderByType: 定义具体的排序规则，限定为desc,asc,DESC,ASC其中之一
        :type OrderByType: str
        :param _Limit: 返回数量，默认为 20，取值范围为(0,100]
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0，取值范围为[0,INF)
        :type Offset: int
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._OrderBy = None
        self._OrderByType = None
        self._Limit = None
        self._Offset = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

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
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamLogsResponse(AbstractModel):
    """DescribeClusterParamLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _ClusterParamLogs: 参数修改记录
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterParamLogs: list of ClusterParamModifyLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterParamLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterParamLogs(self):
        return self._ClusterParamLogs

    @ClusterParamLogs.setter
    def ClusterParamLogs(self, ClusterParamLogs):
        self._ClusterParamLogs = ClusterParamLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterParamLogs") is not None:
            self._ClusterParamLogs = []
            for item in params.get("ClusterParamLogs"):
                obj = ClusterParamModifyLog()
                obj._deserialize(item)
                self._ClusterParamLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterParamsRequest(AbstractModel):
    """DescribeClusterParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ParamName: 参数名字
        :type ParamName: str
        :param _IsGlobal: 是否为全局参数
        :type IsGlobal: str
        """
        self._ClusterId = None
        self._ParamName = None
        self._IsGlobal = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ParamName = params.get("ParamName")
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamsResponse(AbstractModel):
    """DescribeClusterParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数个数
        :type TotalCount: int
        :param _Items: 实例参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ParamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPasswordComplexityRequest(AbstractModel):
    """DescribeClusterPasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPasswordComplexityResponse(AbstractModel):
    """DescribeClusterPasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ValidatePasswordDictionary: 数据字典参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordDictionary: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordLength: 密码长度
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordLength: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordMixedCaseCount: 大小写敏感字符个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordMixedCaseCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordNumberCount: 数字个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordNumberCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordPolicy: 密码等级
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordPolicy: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _ValidatePasswordSpecialCharCount: 特殊字符个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidatePasswordSpecialCharCount: :class:`tencentcloud.cynosdb.v20190107.models.ParamInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ValidatePasswordDictionary = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordSpecialCharCount = None
        self._RequestId = None

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ValidatePasswordDictionary") is not None:
            self._ValidatePasswordDictionary = ParamInfo()
            self._ValidatePasswordDictionary._deserialize(params.get("ValidatePasswordDictionary"))
        if params.get("ValidatePasswordLength") is not None:
            self._ValidatePasswordLength = ParamInfo()
            self._ValidatePasswordLength._deserialize(params.get("ValidatePasswordLength"))
        if params.get("ValidatePasswordMixedCaseCount") is not None:
            self._ValidatePasswordMixedCaseCount = ParamInfo()
            self._ValidatePasswordMixedCaseCount._deserialize(params.get("ValidatePasswordMixedCaseCount"))
        if params.get("ValidatePasswordNumberCount") is not None:
            self._ValidatePasswordNumberCount = ParamInfo()
            self._ValidatePasswordNumberCount._deserialize(params.get("ValidatePasswordNumberCount"))
        if params.get("ValidatePasswordPolicy") is not None:
            self._ValidatePasswordPolicy = ParamInfo()
            self._ValidatePasswordPolicy._deserialize(params.get("ValidatePasswordPolicy"))
        if params.get("ValidatePasswordSpecialCharCount") is not None:
            self._ValidatePasswordSpecialCharCount = ParamInfo()
            self._ValidatePasswordSpecialCharCount._deserialize(params.get("ValidatePasswordSpecialCharCount"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param _OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param _OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param _Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        """
        self._DbType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DbType = params.get("DbType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群数
        :type TotalCount: int
        :param _ClusterSet: 集群列表
        :type ClusterSet: list of CynosdbCluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = CynosdbCluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceGroupId: 实例组ID
        :type InstanceGroupId: str
        """
        self._InstanceId = None
        self._InstanceGroupId = None

    @property
    def InstanceId(self):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        warnings.warn("parameter `InstanceId` is deprecated", DeprecationWarning) 

        self._InstanceId = InstanceId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组信息
        :type Groups: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务流状态。0-成功，1-失败，2-处理中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeInstanceCLSLogDeliveryRequest(AbstractModel):
    """DescribeInstanceCLSLogDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _LogType: 日志类型
        :type LogType: str
        """
        self._InstanceId = None
        self._LogType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceCLSLogDeliveryResponse(AbstractModel):
    """DescribeInstanceCLSLogDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量

        :type TotalCount: int
        :param _InstanceCLSDeliveryInfos: 实例投递信息

        :type InstanceCLSDeliveryInfos: list of InstanceCLSDeliveryInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceCLSDeliveryInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceCLSDeliveryInfos(self):
        return self._InstanceCLSDeliveryInfos

    @InstanceCLSDeliveryInfos.setter
    def InstanceCLSDeliveryInfos(self, InstanceCLSDeliveryInfos):
        self._InstanceCLSDeliveryInfos = InstanceCLSDeliveryInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceCLSDeliveryInfos") is not None:
            self._InstanceCLSDeliveryInfos = []
            for item in params.get("InstanceCLSDeliveryInfos"):
                obj = InstanceCLSDeliveryInfo()
                obj._deserialize(item)
                self._InstanceCLSDeliveryInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Detail: 实例详情
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self._Detail = CynosdbInstanceDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceErrorLogsRequest(AbstractModel):
    """DescribeInstanceErrorLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Limit: 日志条数限制
        :type Limit: int
        :param _Offset: 日志条数偏移量
        :type Offset: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _OrderBy: 排序字段，有Timestamp枚举值
        :type OrderBy: str
        :param _OrderByType: 排序类型，有ASC,DESC枚举值
        :type OrderByType: str
        :param _LogLevels: 日志等级，有error、warning、note三种，支持多个等级同时搜索
        :type LogLevels: list of str
        :param _KeyWords: 关键字，支持模糊搜索
        :type KeyWords: list of str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._OrderBy = None
        self._OrderByType = None
        self._LogLevels = None
        self._KeyWords = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def LogLevels(self):
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._LogLevels = params.get("LogLevels")
        self._KeyWords = params.get("KeyWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceErrorLogsResponse(AbstractModel):
    """DescribeInstanceErrorLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 日志条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ErrorLogs: 错误日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLogs: list of CynosdbErrorLogItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorLogs(self):
        return self._ErrorLogs

    @ErrorLogs.setter
    def ErrorLogs(self, ErrorLogs):
        self._ErrorLogs = ErrorLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ErrorLogs") is not None:
            self._ErrorLogs = []
            for item in params.get("ErrorLogs"):
                obj = CynosdbErrorLogItem()
                obj._deserialize(item)
                self._ErrorLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIds: 实例ID，支持批量查询
        :type InstanceIds: list of str
        :param _ParamKeyword: 参数名搜索条件，支持模糊匹配
        :type ParamKeyword: str
        :param _IsGlobal: 是否为全局参数
        :type IsGlobal: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._ParamKeyword = None
        self._IsGlobal = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamKeyword(self):
        return self._ParamKeyword

    @ParamKeyword.setter
    def ParamKeyword(self, ParamKeyword):
        self._ParamKeyword = ParamKeyword

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._ParamKeyword = params.get("ParamKeyword")
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 实例参数列表
        :type Items: list of InstanceParamItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceParamItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSlowQueriesRequest(AbstractModel):
    """DescribeInstanceSlowQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 事务开始最早时间
        :type StartTime: str
        :param _EndTime: 事务开始最晚时间
        :type EndTime: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Username: 用户名
        :type Username: str
        :param _Host: 客户端host
        :type Host: str
        :param _Database: 数据库名
        :type Database: str
        :param _OrderBy: 排序字段，可选值：QueryTime,LockTime,RowsExamined,RowsSent
        :type OrderBy: str
        :param _OrderByType: 排序类型，可选值：asc,desc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Username = None
        self._Host = None
        self._Database = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Username = params.get("Username")
        self._Host = params.get("Host")
        self._Database = params.get("Database")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSlowQueriesResponse(AbstractModel):
    """DescribeInstanceSlowQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _SlowQueries: 慢查询记录
        :type SlowQueries: list of SlowQueriesItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowQueries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowQueries(self):
        return self._SlowQueries

    @SlowQueries.setter
    def SlowQueries(self, SlowQueries):
        self._SlowQueries = SlowQueries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SlowQueries") is not None:
            self._SlowQueries = []
            for item in params.get("SlowQueries"):
                obj = SlowQueriesItem()
                obj._deserialize(item)
                self._SlowQueries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param _IncludeZoneStocks: 是否需要返回可用区信息
        :type IncludeZoneStocks: bool
        :param _DeviceType: 实例机器类型
        :type DeviceType: str
        """
        self._DbType = None
        self._IncludeZoneStocks = None
        self._DeviceType = None

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def IncludeZoneStocks(self):
        return self._IncludeZoneStocks

    @IncludeZoneStocks.setter
    def IncludeZoneStocks(self, IncludeZoneStocks):
        self._IncludeZoneStocks = IncludeZoneStocks

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._DbType = params.get("DbType")
        self._IncludeZoneStocks = params.get("IncludeZoneStocks")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSpecSet: 规格信息
        :type InstanceSpecSet: list of InstanceSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSpecSet = None
        self._RequestId = None

    @property
    def InstanceSpecSet(self):
        return self._InstanceSpecSet

    @InstanceSpecSet.setter
    def InstanceSpecSet(self, InstanceSpecSet):
        self._InstanceSpecSet = InstanceSpecSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSpecSet") is not None:
            self._InstanceSpecSet = []
            for item in params.get("InstanceSpecSet"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self._InstanceSpecSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，取值范围为(0,100]
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param _OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param _OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param _Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        :param _DbType: 引擎类型：目前支持“MYSQL”
        :type DbType: str
        :param _Status: 实例状态, 可选值:
creating 创建中
running 运行中
isolating 隔离中
isolated 已隔离
activating 恢复中
offlining 下线中
offlined 已下线
        :type Status: str
        :param _InstanceIds: 实例id列表
        :type InstanceIds: list of str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None
        self._DbType = None
        self._Status = None
        self._InstanceIds = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DbType = params.get("DbType")
        self._Status = params.get("Status")
        self._InstanceIds = params.get("InstanceIds")
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
        :param _TotalCount: 实例个数
        :type TotalCount: int
        :param _InstanceSet: 实例列表
        :type InstanceSet: list of CynosdbInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIsolatedInstancesRequest(AbstractModel):
    """DescribeIsolatedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param _OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param _OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param _Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        :param _DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None
        self._DbType = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIsolatedInstancesResponse(AbstractModel):
    """DescribeIsolatedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例个数
        :type TotalCount: int
        :param _InstanceSet: 实例列表
        :type InstanceSet: list of CynosdbInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaintainWeekDays: 维护week days
        :type MaintainWeekDays: list of str
        :param _MaintainStartTime: 维护开始时间，单位秒
        :type MaintainStartTime: int
        :param _MaintainDuration: 维护时长，单位秒
        :type MaintainDuration: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaintainWeekDays = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._RequestId = None

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateDetailRequest(AbstractModel):
    """DescribeParamTemplateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateDetailResponse(AbstractModel):
    """DescribeParamTemplateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 参数模板ID
        :type TemplateId: int
        :param _TemplateName: 参数模板名称
        :type TemplateName: str
        :param _TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        :param _EngineVersion: 引擎版本
        :type EngineVersion: str
        :param _TotalCount: 参数总条数
        :type TotalCount: int
        :param _Items: 参数列表
        :type Items: list of ParamDetail
        :param _DbMode: 数据库类型，可选值：NORMAL，SERVERLESS
        :type DbMode: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._EngineVersion = None
        self._TotalCount = None
        self._Items = None
        self._DbMode = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        self._EngineVersion = params.get("EngineVersion")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._DbMode = params.get("DbMode")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineVersions: 数据库引擎版本号
        :type EngineVersions: list of str
        :param _TemplateNames: 模板名称
        :type TemplateNames: list of str
        :param _TemplateIds: 模板ID
        :type TemplateIds: list of int
        :param _DbModes: 数据库类型，可选值：NORMAL，SERVERLESS
        :type DbModes: list of str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询限制条数
        :type Limit: int
        :param _Products: 查询的模板对应的产品类型
        :type Products: list of str
        :param _TemplateTypes: 模板类型
        :type TemplateTypes: list of str
        :param _EngineTypes: 版本类型
        :type EngineTypes: list of str
        :param _OrderBy: 返回结果的排序字段
        :type OrderBy: str
        :param _OrderDirection: 排序方式（asc、desc）
        :type OrderDirection: str
        """
        self._EngineVersions = None
        self._TemplateNames = None
        self._TemplateIds = None
        self._DbModes = None
        self._Offset = None
        self._Limit = None
        self._Products = None
        self._TemplateTypes = None
        self._EngineTypes = None
        self._OrderBy = None
        self._OrderDirection = None

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds

    @property
    def DbModes(self):
        return self._DbModes

    @DbModes.setter
    def DbModes(self, DbModes):
        self._DbModes = DbModes

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
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TemplateTypes(self):
        return self._TemplateTypes

    @TemplateTypes.setter
    def TemplateTypes(self, TemplateTypes):
        self._TemplateTypes = TemplateTypes

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._EngineVersions = params.get("EngineVersions")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        self._DbModes = params.get("DbModes")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Products = params.get("Products")
        self._TemplateTypes = params.get("TemplateTypes")
        self._EngineTypes = params.get("EngineTypes")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 参数模板数量
        :type TotalCount: int
        :param _Items: 参数模板信息
        :type Items: list of ParamTemplateListInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamTemplateListInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Limit: 限制量
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _SearchKey: 搜索关键字
        :type SearchKey: str
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._SearchKey = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组详情
        :type Groups: list of SecurityGroup
        :param _Total: 总数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID（该参数必传，例如cynosdbmysql-xxxxxx）
        :type ClusterId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param _OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param _OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param _Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryParamFilter
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryParamFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据库代理组数
        :type TotalCount: int
        :param _ProxyGroupInfos: 数据库代理组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroupInfos: list of ProxyGroupInfo
        :param _ProxyNodeInfos: 数据库代理节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodeInfos: list of ProxyNodeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyGroupInfos = None
        self._ProxyNodeInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyGroupInfos(self):
        return self._ProxyGroupInfos

    @ProxyGroupInfos.setter
    def ProxyGroupInfos(self, ProxyGroupInfos):
        self._ProxyGroupInfos = ProxyGroupInfos

    @property
    def ProxyNodeInfos(self):
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProxyGroupInfos") is not None:
            self._ProxyGroupInfos = []
            for item in params.get("ProxyGroupInfos"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyGroupInfos.append(obj)
        if params.get("ProxyNodeInfos") is not None:
            self._ProxyNodeInfos = []
            for item in params.get("ProxyNodeInfos"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyNodesRequest(AbstractModel):
    """DescribeProxyNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param _OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param _OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param _Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Filters = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyNodesResponse(AbstractModel):
    """DescribeProxyNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据库代理节点总数
        :type TotalCount: int
        :param _ProxyNodeInfos: 数据库代理节点列表
        :type ProxyNodeInfos: list of ProxyNodeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyNodeInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyNodeInfos(self):
        return self._ProxyNodeInfos

    @ProxyNodeInfos.setter
    def ProxyNodeInfos(self, ProxyNodeInfos):
        self._ProxyNodeInfos = ProxyNodeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProxyNodeInfos") is not None:
            self._ProxyNodeInfos = []
            for item in params.get("ProxyNodeInfos"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxySpecsRequest(AbstractModel):
    """DescribeProxySpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySpecsResponse(AbstractModel):
    """DescribeProxySpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxySpecs: 数据库代理规格列表
        :type ProxySpecs: list of ProxySpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxySpecs = None
        self._RequestId = None

    @property
    def ProxySpecs(self):
        return self._ProxySpecs

    @ProxySpecs.setter
    def ProxySpecs(self, ProxySpecs):
        self._ProxySpecs = ProxySpecs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProxySpecs") is not None:
            self._ProxySpecs = []
            for item in params.get("ProxySpecs"):
                obj = ProxySpec()
                obj._deserialize(item)
                self._ProxySpecs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageDetailRequest(AbstractModel):
    """DescribeResourcePackageDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包唯一ID
        :type PackageId: str
        :param _ClusterIds: 集群ID
        :type ClusterIds: list of str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: str
        :param _Limit: 限制
        :type Limit: str
        :param _InstanceIds: 实例D
        :type InstanceIds: list of str
        """
        self._PackageId = None
        self._ClusterIds = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._ClusterIds = params.get("ClusterIds")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageDetailResponse(AbstractModel):
    """DescribeResourcePackageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 资源包抵扣总数
        :type Total: int
        :param _Detail: 资源包明细说明
        :type Detail: list of PackageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = PackageDetail()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageListRequest(AbstractModel):
    """DescribeResourcePackageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包唯一ID
        :type PackageId: list of str
        :param _PackageName: 资源包名称
        :type PackageName: list of str
        :param _PackageType: 资源包类型
CCU-计算资源包，DISK-存储资源包
        :type PackageType: list of str
        :param _PackageRegion: 资源包使用地域
china-中国内地通用，overseas-港澳台及海外通用
        :type PackageRegion: list of str
        :param _Status: 资源包状态
creating-创建中；
using-使用中；
expired-已过期；
normal_finish-使用完；
apply_refund-申请退费中；
refund-已退费。
        :type Status: list of str
        :param _OrderBy: 排序条件，支持排序条件:startTime-生效时间，
expireTime-过期时间，packageUsedSpec-使用容量，packageTotalSpec-总存储量。
按照数组顺序排列；
        :type OrderBy: list of str
        :param _OrderDirection: 排序方式，DESC-降序，ASC-升序
        :type OrderDirection: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制
        :type Limit: int
        """
        self._PackageId = None
        self._PackageName = None
        self._PackageType = None
        self._PackageRegion = None
        self._Status = None
        self._OrderBy = None
        self._OrderDirection = None
        self._Offset = None
        self._Limit = None

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
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

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
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._PackageType = params.get("PackageType")
        self._PackageRegion = params.get("PackageRegion")
        self._Status = params.get("Status")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageListResponse(AbstractModel):
    """DescribeResourcePackageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 资源包总数
        :type Total: int
        :param _Detail: 资源包明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of Package
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = Package()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcePackageSaleSpecRequest(AbstractModel):
    """DescribeResourcePackageSaleSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _PackageRegion: 资源包使用地域
china-中国内地通用，overseas-港澳台及海外通用
        :type PackageRegion: str
        :param _PackageType: 资源包类型
CCU-计算资源包
DISK-存储资源包
        :type PackageType: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制
        :type Limit: int
        """
        self._InstanceType = None
        self._PackageRegion = None
        self._PackageType = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

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
        self._InstanceType = params.get("InstanceType")
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcePackageSaleSpecResponse(AbstractModel):
    """DescribeResourcePackageSaleSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 可售卖资源包规格总数
        :type Total: int
        :param _Detail: 资源包明细说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of SalePackageSpec
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Detail = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = SalePackageSpec()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 计费订单ID（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）。
DealName与DealNames至少应输入一项，两者都传时以DealName为准。
        :type DealName: str
        :param _DealNames: 计费订单ID列表，可以一次查询若干条订单ID对应资源信息（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）。
DealName与DealNames至少应输入一项，两者都传时以DealName为准。
        :type DealNames: list of str
        """
        self._DealName = None
        self._DealNames = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BillingResourceInfos: 计费资源id信息数组
        :type BillingResourceInfos: list of BillingResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BillingResourceInfos = None
        self._RequestId = None

    @property
    def BillingResourceInfos(self):
        return self._BillingResourceInfos

    @BillingResourceInfos.setter
    def BillingResourceInfos(self, BillingResourceInfos):
        self._BillingResourceInfos = BillingResourceInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BillingResourceInfos") is not None:
            self._BillingResourceInfos = []
            for item in params.get("BillingResourceInfos"):
                obj = BillingResourceInfo()
                obj._deserialize(item)
                self._BillingResourceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRangeStart: 有效回归时间范围开始时间点（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeRangeStart: str
        :param _TimeRangeEnd: 有效回归时间范围结束时间点（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeRangeEnd: str
        :param _RollbackTimeRanges: 可回档时间范围
        :type RollbackTimeRanges: list of RollbackTimeRange
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._RollbackTimeRanges = None
        self._RequestId = None

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def RollbackTimeRanges(self):
        return self._RollbackTimeRanges

    @RollbackTimeRanges.setter
    def RollbackTimeRanges(self, RollbackTimeRanges):
        self._RollbackTimeRanges = RollbackTimeRanges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        if params.get("RollbackTimeRanges") is not None:
            self._RollbackTimeRanges = []
            for item in params.get("RollbackTimeRanges"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self._RollbackTimeRanges.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServerlessStrategyRequest(AbstractModel):
    """DescribeServerlessStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: serverless集群id
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessStrategyResponse(AbstractModel):
    """DescribeServerlessStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoPauseDelay: cpu负载为 0 时持续多久（秒）发起自动暂停
        :type AutoPauseDelay: int
        :param _AutoScaleUpDelay: cpu负载超过当前规格核数时，持续多久（秒）发起自动扩容
        :type AutoScaleUpDelay: int
        :param _AutoScaleDownDelay: cpu 负载低于低一级规格核数时，持续多久（秒）发起自动缩容
        :type AutoScaleDownDelay: int
        :param _AutoPause: 是否自动暂停，可能值：
yes
no
        :type AutoPause: str
        :param _AutoScaleUp: 集群是否允许向上扩容，可选范围<li>yes</li><li>no</li>
        :type AutoScaleUp: str
        :param _AutoScaleDown: 集群是否允许向下缩容，可选范围<li>yes</li><li>no</li>
        :type AutoScaleDown: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoPauseDelay = None
        self._AutoScaleUpDelay = None
        self._AutoScaleDownDelay = None
        self._AutoPause = None
        self._AutoScaleUp = None
        self._AutoScaleDown = None
        self._RequestId = None

    @property
    def AutoPauseDelay(self):
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def AutoScaleUpDelay(self):
        return self._AutoScaleUpDelay

    @AutoScaleUpDelay.setter
    def AutoScaleUpDelay(self, AutoScaleUpDelay):
        self._AutoScaleUpDelay = AutoScaleUpDelay

    @property
    def AutoScaleDownDelay(self):
        return self._AutoScaleDownDelay

    @AutoScaleDownDelay.setter
    def AutoScaleDownDelay(self, AutoScaleDownDelay):
        self._AutoScaleDownDelay = AutoScaleDownDelay

    @property
    def AutoPause(self):
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoScaleUp(self):
        return self._AutoScaleUp

    @AutoScaleUp.setter
    def AutoScaleUp(self, AutoScaleUp):
        self._AutoScaleUp = AutoScaleUp

    @property
    def AutoScaleDown(self):
        return self._AutoScaleDown

    @AutoScaleDown.setter
    def AutoScaleDown(self, AutoScaleDown):
        self._AutoScaleDown = AutoScaleDown

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._AutoScaleUpDelay = params.get("AutoScaleUpDelay")
        self._AutoScaleDownDelay = params.get("AutoScaleDownDelay")
        self._AutoPause = params.get("AutoPause")
        self._AutoScaleUp = params.get("AutoScaleUp")
        self._AutoScaleDown = params.get("AutoScaleDown")
        self._RequestId = params.get("RequestId")


class DescribeSupportProxyVersionRequest(AbstractModel):
    """DescribeSupportProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportProxyVersionResponse(AbstractModel):
    """DescribeSupportProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SupportProxyVersions: 支持的数据库代理版本集合
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportProxyVersions: list of str
        :param _CurrentProxyVersion: 当前proxy版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentProxyVersion: str
        :param _SupportProxyVersionDetail: 代理版本详情
        :type SupportProxyVersionDetail: list of ProxyVersionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SupportProxyVersions = None
        self._CurrentProxyVersion = None
        self._SupportProxyVersionDetail = None
        self._RequestId = None

    @property
    def SupportProxyVersions(self):
        return self._SupportProxyVersions

    @SupportProxyVersions.setter
    def SupportProxyVersions(self, SupportProxyVersions):
        self._SupportProxyVersions = SupportProxyVersions

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def SupportProxyVersionDetail(self):
        return self._SupportProxyVersionDetail

    @SupportProxyVersionDetail.setter
    def SupportProxyVersionDetail(self, SupportProxyVersionDetail):
        self._SupportProxyVersionDetail = SupportProxyVersionDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SupportProxyVersions = params.get("SupportProxyVersions")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        if params.get("SupportProxyVersionDetail") is not None:
            self._SupportProxyVersionDetail = []
            for item in params.get("SupportProxyVersionDetail"):
                obj = ProxyVersionInfo()
                obj._deserialize(item)
                self._SupportProxyVersionDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTimeBegin: 任务开始时间起始值
        :type StartTimeBegin: str
        :param _StartTimeEnd: 任务开始时间结束值
        :type StartTimeEnd: str
        :param _Filters: 过滤条件
        :type Filters: list of QueryFilter
        :param _Limit: 查询列表长度
        :type Limit: int
        :param _Offset: 查询列表偏移量
        :type Offset: int
        """
        self._StartTimeBegin = None
        self._StartTimeEnd = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTimeBegin(self):
        return self._StartTimeBegin

    @StartTimeBegin.setter
    def StartTimeBegin(self, StartTimeBegin):
        self._StartTimeBegin = StartTimeBegin

    @property
    def StartTimeEnd(self):
        return self._StartTimeEnd

    @StartTimeEnd.setter
    def StartTimeEnd(self, StartTimeEnd):
        self._StartTimeEnd = StartTimeEnd

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._StartTimeBegin = params.get("StartTimeBegin")
        self._StartTimeEnd = params.get("StartTimeEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        :param _TotalCount: 任务列表总条数
        :type TotalCount: int
        :param _TaskList: 任务列表
        :type TaskList: list of BizTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskList(self):
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = BizTaskInfo()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IncludeVirtualZones: 是否包含虚拟区
        :type IncludeVirtualZones: bool
        :param _ShowPermission: 是否展示地域下所有可用区，并显示用户每个可用区权限
        :type ShowPermission: bool
        """
        self._IncludeVirtualZones = None
        self._ShowPermission = None

    @property
    def IncludeVirtualZones(self):
        return self._IncludeVirtualZones

    @IncludeVirtualZones.setter
    def IncludeVirtualZones(self, IncludeVirtualZones):
        self._IncludeVirtualZones = IncludeVirtualZones

    @property
    def ShowPermission(self):
        return self._ShowPermission

    @ShowPermission.setter
    def ShowPermission(self, ShowPermission):
        self._ShowPermission = ShowPermission


    def _deserialize(self, params):
        self._IncludeVirtualZones = params.get("IncludeVirtualZones")
        self._ShowPermission = params.get("ShowPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域信息
        :type RegionSet: list of SaleRegion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = SaleRegion()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例组 ID 数组，cynosdbmysql-grp-前缀开头或集群 ID。
说明：要获取集群的实例组 ID，可通过 [查询集群实例组](https://cloud.tencent.com/document/product/1003/103934) 进行。
        :type InstanceIds: list of str
        :param _SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组ID组成的数组。
        :type SecurityGroupIds: list of str
        :param _Zone: 可用区。
说明：请正确输入集群所在的主可用区，若输入非集群所在的主可用区可能显示调用成功，但实际执行会失败。
        :type Zone: str
        """
        self._InstanceIds = None
        self._SecurityGroupIds = None
        self._Zone = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

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


class ErrorLogItemExport(AbstractModel):
    """错误日志导出格式

    """

    def __init__(self):
        r"""
        :param _Timestamp: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Level: 日志等级，可选值note, warning，error
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param _Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Timestamp = None
        self._Level = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Level = params.get("Level")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExchangeInstanceInfo(AbstractModel):
    """交换实例信息

    """

    def __init__(self):
        r"""
        :param _SrcInstanceInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcInstanceInfo: :class:`tencentcloud.cynosdb.v20190107.models.RollbackInstanceInfo`
        :param _DstInstanceInfo: 目标实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstInstanceInfo: :class:`tencentcloud.cynosdb.v20190107.models.RollbackInstanceInfo`
        """
        self._SrcInstanceInfo = None
        self._DstInstanceInfo = None

    @property
    def SrcInstanceInfo(self):
        return self._SrcInstanceInfo

    @SrcInstanceInfo.setter
    def SrcInstanceInfo(self, SrcInstanceInfo):
        self._SrcInstanceInfo = SrcInstanceInfo

    @property
    def DstInstanceInfo(self):
        return self._DstInstanceInfo

    @DstInstanceInfo.setter
    def DstInstanceInfo(self, DstInstanceInfo):
        self._DstInstanceInfo = DstInstanceInfo


    def _deserialize(self, params):
        if params.get("SrcInstanceInfo") is not None:
            self._SrcInstanceInfo = RollbackInstanceInfo()
            self._SrcInstanceInfo._deserialize(params.get("SrcInstanceInfo"))
        if params.get("DstInstanceInfo") is not None:
            self._DstInstanceInfo = RollbackInstanceInfo()
            self._DstInstanceInfo._deserialize(params.get("DstInstanceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExchangeRoGroupInfo(AbstractModel):
    """交换RO组信息

    """

    def __init__(self):
        r"""
        :param _SrcRoGroupInfo: 源RO组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcRoGroupInfo: :class:`tencentcloud.cynosdb.v20190107.models.RollbackRoGroupInfo`
        :param _DstRoGroupInfo: 目标RO组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DstRoGroupInfo: :class:`tencentcloud.cynosdb.v20190107.models.RollbackRoGroupInfo`
        """
        self._SrcRoGroupInfo = None
        self._DstRoGroupInfo = None

    @property
    def SrcRoGroupInfo(self):
        return self._SrcRoGroupInfo

    @SrcRoGroupInfo.setter
    def SrcRoGroupInfo(self, SrcRoGroupInfo):
        self._SrcRoGroupInfo = SrcRoGroupInfo

    @property
    def DstRoGroupInfo(self):
        return self._DstRoGroupInfo

    @DstRoGroupInfo.setter
    def DstRoGroupInfo(self, DstRoGroupInfo):
        self._DstRoGroupInfo = DstRoGroupInfo


    def _deserialize(self, params):
        if params.get("SrcRoGroupInfo") is not None:
            self._SrcRoGroupInfo = RollbackRoGroupInfo()
            self._SrcRoGroupInfo._deserialize(params.get("SrcRoGroupInfo"))
        if params.get("DstRoGroupInfo") is not None:
            self._DstRoGroupInfo = RollbackRoGroupInfo()
            self._DstRoGroupInfo._deserialize(params.get("DstRoGroupInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceErrorLogsRequest(AbstractModel):
    """ExportInstanceErrorLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 日志最早时间
        :type StartTime: str
        :param _EndTime: 日志最晚时间
        :type EndTime: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _LogLevels: 日志等级
        :type LogLevels: list of str
        :param _KeyWords: 关键字
        :type KeyWords: list of str
        :param _FileType: 文件类型，可选值：csv, original
        :type FileType: str
        :param _OrderBy: 可选值Timestamp
        :type OrderBy: str
        :param _OrderByType: ASC或DESC
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._LogLevels = None
        self._KeyWords = None
        self._FileType = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def LogLevels(self):
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._LogLevels = params.get("LogLevels")
        self._KeyWords = params.get("KeyWords")
        self._FileType = params.get("FileType")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceErrorLogsResponse(AbstractModel):
    """ExportInstanceErrorLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorLogItems: 错误日志导出内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLogItems: list of ErrorLogItemExport
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorLogItems = None
        self._RequestId = None

    @property
    def ErrorLogItems(self):
        return self._ErrorLogItems

    @ErrorLogItems.setter
    def ErrorLogItems(self, ErrorLogItems):
        self._ErrorLogItems = ErrorLogItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorLogItems") is not None:
            self._ErrorLogItems = []
            for item in params.get("ErrorLogItems"):
                obj = ErrorLogItemExport()
                obj._deserialize(item)
                self._ErrorLogItems.append(obj)
        self._RequestId = params.get("RequestId")


class ExportInstanceSlowQueriesRequest(AbstractModel):
    """ExportInstanceSlowQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 事务开始最早时间
        :type StartTime: str
        :param _EndTime: 事务开始最晚时间
        :type EndTime: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Username: 用户名
        :type Username: str
        :param _Host: 客户端host
        :type Host: str
        :param _Database: 数据库名
        :type Database: str
        :param _FileType: 文件类型，可选值：csv, original
        :type FileType: str
        :param _OrderBy: 排序字段，可选值： QueryTime,LockTime,RowsExamined,RowsSent
        :type OrderBy: str
        :param _OrderByType: 排序类型，可选值：asc,desc
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Username = None
        self._Host = None
        self._Database = None
        self._FileType = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Username = params.get("Username")
        self._Host = params.get("Host")
        self._Database = params.get("Database")
        self._FileType = params.get("FileType")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceSlowQueriesResponse(AbstractModel):
    """ExportInstanceSlowQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 慢查询导出内容
        :type FileContent: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileContent = None
        self._RequestId = None

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._RequestId = params.get("RequestId")


class ExportResourcePackageDeductDetailsRequest(AbstractModel):
    """ExportResourcePackageDeductDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 需要导出的资源包ID
        :type PackageId: str
        :param _ClusterIds: 使用资源包容量的cynos集群ID
        :type ClusterIds: list of str
        :param _OrderBy: 排序字段，目前支持：createTime（资源包被抵扣时间），successDeductSpec（资源包抵扣量）
        :type OrderBy: str
        :param _OrderByType: 排序类型，支持ASC、DESC、asc、desc
        :type OrderByType: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 单次最大导出数据行数，目前最大支持2000行
        :type Limit: str
        :param _Offset: 偏移量页数
        :type Offset: str
        :param _FileType: 导出数据格式，目前仅支持csv格式，留作扩展
        :type FileType: str
        """
        self._PackageId = None
        self._ClusterIds = None
        self._OrderBy = None
        self._OrderByType = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._FileType = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

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
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._ClusterIds = params.get("ClusterIds")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportResourcePackageDeductDetailsResponse(AbstractModel):
    """ExportResourcePackageDeductDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileContent: 文件详情
        :type FileContent: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileContent = None
        self._RequestId = None

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileContent = params.get("FileContent")
        self._RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param _DbTablePrivileges: 数据库表权限码数组
        :type DbTablePrivileges: list of str
        :param _DbTables: 数据库表信息
        :type DbTables: list of DbTable
        """
        self._ClusterId = None
        self._Account = None
        self._DbTablePrivileges = None
        self._DbTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DbTablePrivileges(self):
        return self._DbTablePrivileges

    @DbTablePrivileges.setter
    def DbTablePrivileges(self, DbTablePrivileges):
        self._DbTablePrivileges = DbTablePrivileges

    @property
    def DbTables(self):
        return self._DbTables

    @DbTables.setter
    def DbTables(self, DbTables):
        self._DbTables = DbTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        self._DbTablePrivileges = params.get("DbTablePrivileges")
        if params.get("DbTables") is not None:
            self._DbTables = []
            for item in params.get("DbTables"):
                obj = DbTable()
                obj._deserialize(item)
                self._DbTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

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


class InputAccount(AbstractModel):
    """账号，包含accountName和host

    """

    def __init__(self):
        r"""
        :param _AccountName: 账号
        :type AccountName: str
        :param _Host: 主机，默认‘%’
        :type Host: str
        """
        self._AccountName = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateRequest(AbstractModel):
    """InquirePriceCreate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区,每个地域提供最佳实践
        :type Zone: str
        :param _GoodsNum: 购买计算节点个数
        :type GoodsNum: int
        :param _InstancePayMode: 实例购买类型，可选值为：PREPAID, POSTPAID, SERVERLESS
        :type InstancePayMode: str
        :param _StoragePayMode: 存储购买类型，可选值为：PREPAID, POSTPAID
        :type StoragePayMode: str
        :param _DeviceType: 实例设备类型
        :type DeviceType: str
        :param _Cpu: CPU核数，PREPAID与POSTPAID实例类型必传
        :type Cpu: int
        :param _Memory: 内存大小，单位G，PREPAID与POSTPAID实例类型必传
        :type Memory: int
        :param _Ccu: Ccu大小，serverless类型必传
        :type Ccu: float
        :param _StorageLimit: 存储大小，PREPAID存储类型必传
        :type StorageLimit: int
        :param _TimeSpan: 购买时长，PREPAID购买类型必传
        :type TimeSpan: int
        :param _TimeUnit: 时长单位，可选值为：m,d。PREPAID购买类型必传
        :type TimeUnit: str
        """
        self._Zone = None
        self._GoodsNum = None
        self._InstancePayMode = None
        self._StoragePayMode = None
        self._DeviceType = None
        self._Cpu = None
        self._Memory = None
        self._Ccu = None
        self._StorageLimit = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def InstancePayMode(self):
        return self._InstancePayMode

    @InstancePayMode.setter
    def InstancePayMode(self, InstancePayMode):
        self._InstancePayMode = InstancePayMode

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Ccu(self):
        return self._Ccu

    @Ccu.setter
    def Ccu(self, Ccu):
        self._Ccu = Ccu

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._GoodsNum = params.get("GoodsNum")
        self._InstancePayMode = params.get("InstancePayMode")
        self._StoragePayMode = params.get("StoragePayMode")
        self._DeviceType = params.get("DeviceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Ccu = params.get("Ccu")
        self._StorageLimit = params.get("StorageLimit")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateResponse(AbstractModel):
    """InquirePriceCreate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _StoragePrice: 存储价格
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstancePrice = None
        self._StoragePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def StoragePrice(self):
        return self._StoragePrice

    @StoragePrice.setter
    def StoragePrice(self, StoragePrice):
        self._StoragePrice = StoragePrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = TradePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("StoragePrice") is not None:
            self._StoragePrice = TradePrice()
            self._StoragePrice._deserialize(params.get("StoragePrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceModifyRequest(AbstractModel):
    """InquirePriceModify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Cpu: CPU核数
        :type Cpu: int
        :param _Memory: 内存大小
        :type Memory: int
        :param _StorageLimit: 存储大小，存储资源变配：ClusterId,StorageLimit
        :type StorageLimit: int
        :param _InstanceId: 实例ID，计算资源变配必传: ClusterId,InstanceId,Cpu,Memory 
        :type InstanceId: str
        :param _DeviceType: 实例设备类型
        :type DeviceType: str
        :param _Ccu: serverless实例ccu大小
        :type Ccu: float
        """
        self._ClusterId = None
        self._Cpu = None
        self._Memory = None
        self._StorageLimit = None
        self._InstanceId = None
        self._DeviceType = None
        self._Ccu = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Ccu(self):
        return self._Ccu

    @Ccu.setter
    def Ccu(self, Ccu):
        self._Ccu = Ccu


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageLimit = params.get("StorageLimit")
        self._InstanceId = params.get("InstanceId")
        self._DeviceType = params.get("DeviceType")
        self._Ccu = params.get("Ccu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyResponse(AbstractModel):
    """InquirePriceModify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _StoragePrice: 存储价格
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstancePrice = None
        self._StoragePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def StoragePrice(self):
        return self._StoragePrice

    @StoragePrice.setter
    def StoragePrice(self, StoragePrice):
        self._StoragePrice = StoragePrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = TradePrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("StoragePrice") is not None:
            self._StoragePrice = TradePrice()
            self._StoragePrice._deserialize(params.get("StoragePrice"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewRequest(AbstractModel):
    """InquirePriceRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _TimeSpan: 购买时长,与TimeUnit组合才能生效
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位, 与TimeSpan组合生效，可选:日:d,月:m
        :type TimeUnit: str
        """
        self._ClusterId = None
        self._TimeSpan = None
        self._TimeUnit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewResponse(AbstractModel):
    """InquirePriceRenew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _Prices: 对应的询价结果数组
        :type Prices: list of TradePrice
        :param _InstanceRealTotalPrice: 续费计算节点的总价格
        :type InstanceRealTotalPrice: int
        :param _StorageRealTotalPrice: 续费存储节点的总价格
        :type StorageRealTotalPrice: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._Prices = None
        self._InstanceRealTotalPrice = None
        self._StorageRealTotalPrice = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Prices(self):
        return self._Prices

    @Prices.setter
    def Prices(self, Prices):
        self._Prices = Prices

    @property
    def InstanceRealTotalPrice(self):
        return self._InstanceRealTotalPrice

    @InstanceRealTotalPrice.setter
    def InstanceRealTotalPrice(self, InstanceRealTotalPrice):
        self._InstanceRealTotalPrice = InstanceRealTotalPrice

    @property
    def StorageRealTotalPrice(self):
        return self._StorageRealTotalPrice

    @StorageRealTotalPrice.setter
    def StorageRealTotalPrice(self, StorageRealTotalPrice):
        self._StorageRealTotalPrice = StorageRealTotalPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Prices") is not None:
            self._Prices = []
            for item in params.get("Prices"):
                obj = TradePrice()
                obj._deserialize(item)
                self._Prices.append(obj)
        self._InstanceRealTotalPrice = params.get("InstanceRealTotalPrice")
        self._StorageRealTotalPrice = params.get("StorageRealTotalPrice")
        self._RequestId = params.get("RequestId")


class InstanceAbility(AbstractModel):
    """实例允许的操作列表

    """

    def __init__(self):
        r"""
        :param _IsSupportForceRestart: 实例是否支持强制重启，可选值：yes：支持，no：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportForceRestart: str
        :param _NonsupportForceRestartReason: 不支持强制重启的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NonsupportForceRestartReason: str
        """
        self._IsSupportForceRestart = None
        self._NonsupportForceRestartReason = None

    @property
    def IsSupportForceRestart(self):
        return self._IsSupportForceRestart

    @IsSupportForceRestart.setter
    def IsSupportForceRestart(self, IsSupportForceRestart):
        self._IsSupportForceRestart = IsSupportForceRestart

    @property
    def NonsupportForceRestartReason(self):
        return self._NonsupportForceRestartReason

    @NonsupportForceRestartReason.setter
    def NonsupportForceRestartReason(self, NonsupportForceRestartReason):
        self._NonsupportForceRestartReason = NonsupportForceRestartReason


    def _deserialize(self, params):
        self._IsSupportForceRestart = params.get("IsSupportForceRestart")
        self._NonsupportForceRestartReason = params.get("NonsupportForceRestartReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAuditLogFilter(AbstractModel):
    """审计日志搜索条件

    """

    def __init__(self):
        r"""
        :param _Type: 过滤项。目前支持以下搜索条件：

包含、不包含、包含（分词维度）、不包含（分词维度）: sql - SQL详情；alarmLevel - 告警等级；ruleTemplateId - 规则模板Id

等于、不等于、包含、不包含： host - 客户端地址； user - 用户名； dbName - 数据库名称；

等于、不等于： sqlType - SQL类型； errCode - 错误码； threadId - 线程ID；

范围搜索（时间类型统一为微秒）： execTime - 执行时间； lockWaitTime - 执行时间； ioWaitTime - IO等待时间； trxLivingTime - 事物持续时间； cpuTime - cpu时间； checkRows - 扫描行数； affectRows - 影响行数； sentRows - 返回行数。
        :type Type: str
        :param _Compare: 过滤条件。支持以下条件：
WINC-包含（分词维度），
WEXC-不包含（分词维度）,
INC - 包含,
EXC - 不包含,
EQS - 等于,
NEQ - 不等于,
RA - 范围。
        :type Compare: str
        :param _Value: 过滤的值。反向查询时，多个值之前是且的关系，正向查询多个值是或的关系。
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAuditRule(AbstractModel):
    """实例的审计规则详情。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AuditRule: 是否是规则审计。true-规则审计，false-全审计。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditRule: bool
        :param _AuditRuleFilters: 审计规则详情。仅当AuditRule=true时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _OldRule: 是否是审计策略
注意：此字段可能返回 null，表示取不到有效值。
        :type OldRule: bool
        :param _RuleTemplates: 实例应用的规则模板详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplates: list of RuleTemplateInfo
        """
        self._InstanceId = None
        self._AuditRule = None
        self._AuditRuleFilters = None
        self._OldRule = None
        self._RuleTemplates = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AuditRule(self):
        return self._AuditRule

    @AuditRule.setter
    def AuditRule(self, AuditRule):
        self._AuditRule = AuditRule

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def OldRule(self):
        return self._OldRule

    @OldRule.setter
    def OldRule(self, OldRule):
        self._OldRule = OldRule

    @property
    def RuleTemplates(self):
        return self._RuleTemplates

    @RuleTemplates.setter
    def RuleTemplates(self, RuleTemplates):
        self._RuleTemplates = RuleTemplates


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AuditRule = params.get("AuditRule")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._OldRule = params.get("OldRule")
        if params.get("RuleTemplates") is not None:
            self._RuleTemplates = []
            for item in params.get("RuleTemplates"):
                obj = RuleTemplateInfo()
                obj._deserialize(item)
                self._RuleTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAuditStatus(AbstractModel):
    """实例审计详情信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AuditStatus: 审计状态。ON-表示审计已开启，OFF-表示审计关闭。
        :type AuditStatus: str
        :param _LogExpireDay: 日志保留时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogExpireDay: int
        :param _HighLogExpireDay: 高频存储时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighLogExpireDay: int
        :param _LowLogExpireDay: 低频存储时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type LowLogExpireDay: int
        :param _BillingAmount: 日志存储量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingAmount: float
        :param _HighRealStorage: 高频存储量。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighRealStorage: float
        :param _LowRealStorage: 低频存储量。
注意：此字段可能返回 null，表示取不到有效值。
        :type LowRealStorage: float
        :param _AuditAll: 是否为全审计。true-表示全审计。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditAll: bool
        :param _CreateAt: 审计开通时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: str
        :param _InstanceInfo: 实例相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceInfo: :class:`tencentcloud.cynosdb.v20190107.models.AuditInstanceInfo`
        :param _RealStorage: 总存储量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealStorage: float
        :param _RuleTemplateIds: 实例所应用的规则模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateIds: list of str
        :param _Deliver: 是否开启日志投递：ON，OFF
注意：此字段可能返回 null，表示取不到有效值。
        :type Deliver: str
        :param _DeliverSummary: 日志投递类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverSummary: list of DeliverSummary
        """
        self._InstanceId = None
        self._AuditStatus = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._LowLogExpireDay = None
        self._BillingAmount = None
        self._HighRealStorage = None
        self._LowRealStorage = None
        self._AuditAll = None
        self._CreateAt = None
        self._InstanceInfo = None
        self._RealStorage = None
        self._RuleTemplateIds = None
        self._Deliver = None
        self._DeliverSummary = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def LowLogExpireDay(self):
        return self._LowLogExpireDay

    @LowLogExpireDay.setter
    def LowLogExpireDay(self, LowLogExpireDay):
        self._LowLogExpireDay = LowLogExpireDay

    @property
    def BillingAmount(self):
        return self._BillingAmount

    @BillingAmount.setter
    def BillingAmount(self, BillingAmount):
        self._BillingAmount = BillingAmount

    @property
    def HighRealStorage(self):
        return self._HighRealStorage

    @HighRealStorage.setter
    def HighRealStorage(self, HighRealStorage):
        self._HighRealStorage = HighRealStorage

    @property
    def LowRealStorage(self):
        return self._LowRealStorage

    @LowRealStorage.setter
    def LowRealStorage(self, LowRealStorage):
        self._LowRealStorage = LowRealStorage

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def InstanceInfo(self):
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def RealStorage(self):
        return self._RealStorage

    @RealStorage.setter
    def RealStorage(self, RealStorage):
        self._RealStorage = RealStorage

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def Deliver(self):
        return self._Deliver

    @Deliver.setter
    def Deliver(self, Deliver):
        self._Deliver = Deliver

    @property
    def DeliverSummary(self):
        return self._DeliverSummary

    @DeliverSummary.setter
    def DeliverSummary(self, DeliverSummary):
        self._DeliverSummary = DeliverSummary


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AuditStatus = params.get("AuditStatus")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        self._LowLogExpireDay = params.get("LowLogExpireDay")
        self._BillingAmount = params.get("BillingAmount")
        self._HighRealStorage = params.get("HighRealStorage")
        self._LowRealStorage = params.get("LowRealStorage")
        self._AuditAll = params.get("AuditAll")
        self._CreateAt = params.get("CreateAt")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = AuditInstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RealStorage = params.get("RealStorage")
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        self._Deliver = params.get("Deliver")
        if params.get("DeliverSummary") is not None:
            self._DeliverSummary = []
            for item in params.get("DeliverSummary"):
                obj = DeliverSummary()
                obj._deserialize(item)
                self._DeliverSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCLSDeliveryInfo(AbstractModel):
    """实例日志投递信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 实例name

注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _TopicId: 日志主题id

注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 日志主题name
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _GroupId: 日志集id

注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 日志集name

注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Region: 日志投递地域

注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 投递状态creating,running,offlining,offlined

注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _LogType: 日志类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LogType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._TopicId = None
        self._TopicName = None
        self._GroupId = None
        self._GroupName = None
        self._Region = None
        self._Status = None
        self._LogType = None

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
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInitInfo(AbstractModel):
    """实例初始化配置信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 实例cpu
        :type Cpu: int
        :param _Memory: 实例内存
        :type Memory: int
        :param _InstanceType: 实例类型 rw/ro
        :type InstanceType: str
        :param _InstanceCount: 实例个数,范围[1,15]
        :type InstanceCount: int
        :param _MinRoCount: Serverless实例个数最小值，范围[1,15]
        :type MinRoCount: int
        :param _MaxRoCount: Serverless实例个数最大值，范围[1,15]
        :type MaxRoCount: int
        :param _MinRoCpu: Serverless实例最小规格
        :type MinRoCpu: float
        :param _MaxRoCpu: Serverless实例最大规格
        :type MaxRoCpu: float
        :param _DeviceType: 实例机器类型
        :type DeviceType: str
        """
        self._Cpu = None
        self._Memory = None
        self._InstanceType = None
        self._InstanceCount = None
        self._MinRoCount = None
        self._MaxRoCount = None
        self._MinRoCpu = None
        self._MaxRoCpu = None
        self._DeviceType = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def MinRoCount(self):
        return self._MinRoCount

    @MinRoCount.setter
    def MinRoCount(self, MinRoCount):
        self._MinRoCount = MinRoCount

    @property
    def MaxRoCount(self):
        return self._MaxRoCount

    @MaxRoCount.setter
    def MaxRoCount(self, MaxRoCount):
        self._MaxRoCount = MaxRoCount

    @property
    def MinRoCpu(self):
        return self._MinRoCpu

    @MinRoCpu.setter
    def MinRoCpu(self, MinRoCpu):
        self._MinRoCpu = MinRoCpu

    @property
    def MaxRoCpu(self):
        return self._MaxRoCpu

    @MaxRoCpu.setter
    def MaxRoCpu(self, MaxRoCpu):
        self._MaxRoCpu = MaxRoCpu

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceType = params.get("InstanceType")
        self._InstanceCount = params.get("InstanceCount")
        self._MinRoCount = params.get("MinRoCount")
        self._MaxRoCount = params.get("MaxRoCount")
        self._MinRoCpu = params.get("MinRoCpu")
        self._MaxRoCpu = params.get("MaxRoCpu")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetInfo(AbstractModel):
    """实例网络信息

    """

    def __init__(self):
        r"""
        :param _InstanceGroupType: 网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupType: str
        :param _InstanceGroupId: 实例组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: str
        :param _VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _NetType: 网络类型, 0-基础网络, 1-vpc网络, 2-黑石网络
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: int
        :param _Vip: 私有网络IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: 私有网络端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _WanDomain: 外网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type WanDomain: str
        :param _WanIP: 外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIP: str
        :param _WanPort: 外网端口
注意：此字段可能返回 null，表示取不到有效值。
        :type WanPort: int
        :param _WanStatus: 外网开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WanStatus: str
        """
        self._InstanceGroupType = None
        self._InstanceGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._NetType = None
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanIP = None
        self._WanPort = None
        self._WanStatus = None

    @property
    def InstanceGroupType(self):
        return self._InstanceGroupType

    @InstanceGroupType.setter
    def InstanceGroupType(self, InstanceGroupType):
        self._InstanceGroupType = InstanceGroupType

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus


    def _deserialize(self, params):
        self._InstanceGroupType = params.get("InstanceGroupType")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._NetType = params.get("NetType")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanIP = params.get("WanIP")
        self._WanPort = params.get("WanPort")
        self._WanStatus = params.get("WanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParamItem(AbstractModel):
    """实例参数信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ParamsItems: 实例参数列表
        :type ParamsItems: list of ParamItemDetail
        """
        self._InstanceId = None
        self._ParamsItems = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamsItems(self):
        return self._ParamsItems

    @ParamsItems.setter
    def ParamsItems(self, ParamsItems):
        self._ParamsItems = ParamsItems


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ParamsItems") is not None:
            self._ParamsItems = []
            for item in params.get("ParamsItems"):
                obj = ParamItemDetail()
                obj._deserialize(item)
                self._ParamsItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSpec(AbstractModel):
    """实例可售卖规格详细信息，创建实例时Cpu/Memory确定实例规格，存储可选大小为[MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        r"""
        :param _Cpu: 实例CPU，单位：核
        :type Cpu: int
        :param _Memory: 实例内存，单位：GB
        :type Memory: int
        :param _MaxStorageSize: 实例最大可用存储，单位：GB
        :type MaxStorageSize: int
        :param _MinStorageSize: 实例最小可用存储，单位：GB
        :type MinStorageSize: int
        :param _HasStock: 是否有库存
        :type HasStock: bool
        :param _MachineType: 机器类型
        :type MachineType: str
        :param _MaxIops: 最大IOPS
        :type MaxIops: int
        :param _MaxIoBandWidth: 最大IO带宽
        :type MaxIoBandWidth: int
        :param _ZoneStockInfos: 地域库存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneStockInfos: list of ZoneStockInfo
        :param _StockCount: 库存数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StockCount: int
        """
        self._Cpu = None
        self._Memory = None
        self._MaxStorageSize = None
        self._MinStorageSize = None
        self._HasStock = None
        self._MachineType = None
        self._MaxIops = None
        self._MaxIoBandWidth = None
        self._ZoneStockInfos = None
        self._StockCount = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def MaxStorageSize(self):
        return self._MaxStorageSize

    @MaxStorageSize.setter
    def MaxStorageSize(self, MaxStorageSize):
        self._MaxStorageSize = MaxStorageSize

    @property
    def MinStorageSize(self):
        return self._MinStorageSize

    @MinStorageSize.setter
    def MinStorageSize(self, MinStorageSize):
        self._MinStorageSize = MinStorageSize

    @property
    def HasStock(self):
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MaxIops(self):
        return self._MaxIops

    @MaxIops.setter
    def MaxIops(self, MaxIops):
        self._MaxIops = MaxIops

    @property
    def MaxIoBandWidth(self):
        return self._MaxIoBandWidth

    @MaxIoBandWidth.setter
    def MaxIoBandWidth(self, MaxIoBandWidth):
        self._MaxIoBandWidth = MaxIoBandWidth

    @property
    def ZoneStockInfos(self):
        return self._ZoneStockInfos

    @ZoneStockInfos.setter
    def ZoneStockInfos(self, ZoneStockInfos):
        self._ZoneStockInfos = ZoneStockInfos

    @property
    def StockCount(self):
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._MaxStorageSize = params.get("MaxStorageSize")
        self._MinStorageSize = params.get("MinStorageSize")
        self._HasStock = params.get("HasStock")
        self._MachineType = params.get("MachineType")
        self._MaxIops = params.get("MaxIops")
        self._MaxIoBandWidth = params.get("MaxIoBandWidth")
        if params.get("ZoneStockInfos") is not None:
            self._ZoneStockInfos = []
            for item in params.get("ZoneStockInfos"):
                obj = ZoneStockInfo()
                obj._deserialize(item)
                self._ZoneStockInfos.append(obj)
        self._StockCount = params.get("StockCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _DbType: 该参数已废用
        :type DbType: str
        :param _IsolateReasonTypes: 实例退还原因类型
        :type IsolateReasonTypes: list of int
        :param _IsolateReason: 实例退还原因补充
        :type IsolateReason: str
        """
        self._ClusterId = None
        self._DbType = None
        self._IsolateReasonTypes = None
        self._IsolateReason = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def IsolateReasonTypes(self):
        return self._IsolateReasonTypes

    @IsolateReasonTypes.setter
    def IsolateReasonTypes(self, IsolateReasonTypes):
        self._IsolateReasonTypes = IsolateReasonTypes

    @property
    def IsolateReason(self):
        return self._IsolateReason

    @IsolateReason.setter
    def IsolateReason(self, IsolateReason):
        self._IsolateReason = IsolateReason


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbType = params.get("DbType")
        self._IsolateReasonTypes = params.get("IsolateReasonTypes")
        self._IsolateReason = params.get("IsolateReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _DealNames: 退款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdList: 实例ID数组，例如["cynosdbbmysql-ins-asd","cynosdbmysql-ins-zxc"]
        :type InstanceIdList: list of str
        :param _DbType: 该参数已废弃
        :type DbType: str
        :param _IsolateReasonTypes: 实例退还原因类型
        :type IsolateReasonTypes: list of int
        :param _IsolateReason: 实例退还原因补充
        :type IsolateReason: str
        """
        self._ClusterId = None
        self._InstanceIdList = None
        self._DbType = None
        self._IsolateReasonTypes = None
        self._IsolateReason = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def IsolateReasonTypes(self):
        return self._IsolateReasonTypes

    @IsolateReasonTypes.setter
    def IsolateReasonTypes(self, IsolateReasonTypes):
        self._IsolateReasonTypes = IsolateReasonTypes

    @property
    def IsolateReason(self):
        return self._IsolateReason

    @IsolateReason.setter
    def IsolateReason(self, IsolateReason):
        self._IsolateReason = IsolateReason


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        self._DbType = params.get("DbType")
        self._IsolateReasonTypes = params.get("IsolateReasonTypes")
        self._IsolateReason = params.get("IsolateReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流id
        :type FlowId: int
        :param _DealNames: 隔离实例的订单id（预付费实例）
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._DealNames = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class LogRuleTemplateInfo(AbstractModel):
    """审计日志命中规则模板的基本信息

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateId: str
        :param _RuleTemplateName: 规则模板名
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateName: str
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: str
        :param _RuleTemplateStatus: 规则模板变更状态：0-未变更；1-已变更；2-已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateStatus: int
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._AlarmLevel = None
        self._RuleTemplateStatus = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def RuleTemplateStatus(self):
        return self._RuleTemplateStatus

    @RuleTemplateStatus.setter
    def RuleTemplateStatus(self, RuleTemplateStatus):
        self._RuleTemplateStatus = RuleTemplateStatus


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RuleTemplateName = params.get("RuleTemplateName")
        self._AlarmLevel = params.get("AlarmLevel")
        self._RuleTemplateStatus = params.get("RuleTemplateStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogicBackupConfigInfo(AbstractModel):
    """逻辑备份配置信息

    """

    def __init__(self):
        r"""
        :param _LogicBackupEnable: 是否开启自动逻辑备份
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicBackupEnable: str
        :param _LogicBackupTimeBeg: 自动逻辑备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicBackupTimeBeg: int
        :param _LogicBackupTimeEnd: 自动逻辑备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicBackupTimeEnd: int
        :param _LogicReserveDuration: 自动逻辑备份保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicReserveDuration: int
        :param _LogicCrossRegionsEnable: 是否开启跨地域逻辑备份
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicCrossRegionsEnable: str
        :param _LogicCrossRegions: 逻辑备份所跨地域
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicCrossRegions: list of str
        """
        self._LogicBackupEnable = None
        self._LogicBackupTimeBeg = None
        self._LogicBackupTimeEnd = None
        self._LogicReserveDuration = None
        self._LogicCrossRegionsEnable = None
        self._LogicCrossRegions = None

    @property
    def LogicBackupEnable(self):
        return self._LogicBackupEnable

    @LogicBackupEnable.setter
    def LogicBackupEnable(self, LogicBackupEnable):
        self._LogicBackupEnable = LogicBackupEnable

    @property
    def LogicBackupTimeBeg(self):
        return self._LogicBackupTimeBeg

    @LogicBackupTimeBeg.setter
    def LogicBackupTimeBeg(self, LogicBackupTimeBeg):
        self._LogicBackupTimeBeg = LogicBackupTimeBeg

    @property
    def LogicBackupTimeEnd(self):
        return self._LogicBackupTimeEnd

    @LogicBackupTimeEnd.setter
    def LogicBackupTimeEnd(self, LogicBackupTimeEnd):
        self._LogicBackupTimeEnd = LogicBackupTimeEnd

    @property
    def LogicReserveDuration(self):
        return self._LogicReserveDuration

    @LogicReserveDuration.setter
    def LogicReserveDuration(self, LogicReserveDuration):
        self._LogicReserveDuration = LogicReserveDuration

    @property
    def LogicCrossRegionsEnable(self):
        return self._LogicCrossRegionsEnable

    @LogicCrossRegionsEnable.setter
    def LogicCrossRegionsEnable(self, LogicCrossRegionsEnable):
        self._LogicCrossRegionsEnable = LogicCrossRegionsEnable

    @property
    def LogicCrossRegions(self):
        return self._LogicCrossRegions

    @LogicCrossRegions.setter
    def LogicCrossRegions(self, LogicCrossRegions):
        self._LogicCrossRegions = LogicCrossRegions


    def _deserialize(self, params):
        self._LogicBackupEnable = params.get("LogicBackupEnable")
        self._LogicBackupTimeBeg = params.get("LogicBackupTimeBeg")
        self._LogicBackupTimeEnd = params.get("LogicBackupTimeEnd")
        self._LogicReserveDuration = params.get("LogicReserveDuration")
        self._LogicCrossRegionsEnable = params.get("LogicCrossRegionsEnable")
        self._LogicCrossRegions = params.get("LogicCrossRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualBackupData(AbstractModel):
    """手动备份任务信息

    """

    def __init__(self):
        r"""
        :param _BackupType: 备份类型。snapshot-快照备份
        :type BackupType: str
        :param _BackupMethod: 备份方式。auto-自动备份，manual-手动
        :type BackupMethod: str
        :param _SnapshotTime: 备份时间
        :type SnapshotTime: str
        :param _CrossRegionBackupInfos: 跨地域备份项详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossRegionBackupInfos: list of CrossRegionBackupItem
        """
        self._BackupType = None
        self._BackupMethod = None
        self._SnapshotTime = None
        self._CrossRegionBackupInfos = None

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def CrossRegionBackupInfos(self):
        return self._CrossRegionBackupInfos

    @CrossRegionBackupInfos.setter
    def CrossRegionBackupInfos(self, CrossRegionBackupInfos):
        self._CrossRegionBackupInfos = CrossRegionBackupInfos


    def _deserialize(self, params):
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._SnapshotTime = params.get("SnapshotTime")
        if params.get("CrossRegionBackupInfos") is not None:
            self._CrossRegionBackupInfos = []
            for item in params.get("CrossRegionBackupInfos"):
                obj = CrossRegionBackupItem()
                obj._deserialize(item)
                self._CrossRegionBackupInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifiableInfo(AbstractModel):
    """参数是否可修改的详细信息

    """

    def __init__(self):
        r"""
        :param _IsModifiable: 参数是否可被修改, 1:可以 0:不可以
        :type IsModifiable: int
        """
        self._IsModifiable = None

    @property
    def IsModifiable(self):
        return self._IsModifiable

    @IsModifiable.setter
    def IsModifiable(self, IsModifiable):
        self._IsModifiable = IsModifiable


    def _deserialize(self, params):
        self._IsModifiable = params.get("IsModifiable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountName: 数据库账号名
        :type AccountName: str
        :param _Description: 数据库账号描述信息
        :type Description: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Host: 主机，默认为"%"
        :type Host: str
        """
        self._AccountName = None
        self._Description = None
        self._ClusterId = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

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


class ModifyAccountHostRequest(AbstractModel):
    """ModifyAccountHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _NewHost: 新主机
        :type NewHost: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
        self._ClusterId = None
        self._NewHost = None
        self._Account = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NewHost(self):
        return self._NewHost

    @NewHost.setter
    def NewHost(self, NewHost):
        self._NewHost = NewHost

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NewHost = params.get("NewHost")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountHostResponse(AbstractModel):
    """ModifyAccountHost返回参数结构体

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


class ModifyAccountParamsRequest(AbstractModel):
    """ModifyAccountParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id，不超过32个字符
        :type ClusterId: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param _AccountParams: 数据库表权限数组,当前仅支持参数：max_user_connections，max_user_connections不能大于10240
        :type AccountParams: list of AccountParam
        """
        self._ClusterId = None
        self._Account = None
        self._AccountParams = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountParams(self):
        return self._AccountParams

    @AccountParams.setter
    def AccountParams(self, AccountParams):
        self._AccountParams = AccountParams


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        if params.get("AccountParams") is not None:
            self._AccountParams = []
            for item in params.get("AccountParams"):
                obj = AccountParam()
                obj._deserialize(item)
                self._AccountParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountParamsResponse(AbstractModel):
    """ModifyAccountParams返回参数结构体

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


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param _GlobalPrivileges: 全局权限数组
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: 数据库权限数组
        :type DatabasePrivileges: list of DatabasePrivileges
        :param _TablePrivileges: 表权限数组
        :type TablePrivileges: list of TablePrivileges
        """
        self._ClusterId = None
        self._Account = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回参数结构体

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


class ModifyAuditRuleTemplatesRequest(AbstractModel):
    """ModifyAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleTemplateIds: 审计规则模板ID。
        :type RuleTemplateIds: list of str
        :param _RuleFilters: 修改后的审计规则。
        :type RuleFilters: list of RuleFilters
        :param _RuleTemplateName: 修改后的规则模板名称。
        :type RuleTemplateName: str
        :param _Description: 修改后的规则模板描述。
        :type Description: str
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险。
        :type AlarmLevel: int
        :param _AlarmPolicy: 告警策略。0-不告警，1-告警。
        :type AlarmPolicy: int
        """
        self._RuleTemplateIds = None
        self._RuleFilters = None
        self._RuleTemplateName = None
        self._Description = None
        self._AlarmLevel = None
        self._AlarmPolicy = None

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy


    def _deserialize(self, params):
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._RuleTemplateName = params.get("RuleTemplateName")
        self._Description = params.get("Description")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditRuleTemplatesResponse(AbstractModel):
    """ModifyAuditRuleTemplates返回参数结构体

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


class ModifyAuditServiceRequest(AbstractModel):
    """ModifyAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _LogExpireDay: 日志保留时长。
        :type LogExpireDay: int
        :param _HighLogExpireDay: 高频日志保留时长。
        :type HighLogExpireDay: int
        :param _AuditAll: 修改实例审计规则为全审计。
        :type AuditAll: bool
        :param _AuditRuleFilters: 规则审计。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: 规则模板ID。
        :type RuleTemplateIds: list of str
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditAll = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        self._AuditAll = params.get("AuditAll")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditServiceResponse(AbstractModel):
    """ModifyAuditService返回参数结构体

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


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param _BackupTimeEnd: 表示全备结束时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param _ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800，最大为158112000
        :type ReserveDuration: int
        :param _BackupFreq: 该参数目前不支持修改，无需填写。备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
        :type BackupFreq: list of str
        :param _BackupType: 该参数目前不支持修改，无需填写。备份方式，logic-逻辑备份，snapshot-快照备份
        :type BackupType: str
        :param _LogicBackupConfig: 逻辑备份配置
        :type LogicBackupConfig: :class:`tencentcloud.cynosdb.v20190107.models.LogicBackupConfigInfo`
        :param _DeleteAutoLogicBackup: 是否删除自动逻辑备份
        :type DeleteAutoLogicBackup: bool
        """
        self._ClusterId = None
        self._BackupTimeBeg = None
        self._BackupTimeEnd = None
        self._ReserveDuration = None
        self._BackupFreq = None
        self._BackupType = None
        self._LogicBackupConfig = None
        self._DeleteAutoLogicBackup = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupTimeBeg(self):
        return self._BackupTimeBeg

    @BackupTimeBeg.setter
    def BackupTimeBeg(self, BackupTimeBeg):
        self._BackupTimeBeg = BackupTimeBeg

    @property
    def BackupTimeEnd(self):
        return self._BackupTimeEnd

    @BackupTimeEnd.setter
    def BackupTimeEnd(self, BackupTimeEnd):
        self._BackupTimeEnd = BackupTimeEnd

    @property
    def ReserveDuration(self):
        return self._ReserveDuration

    @ReserveDuration.setter
    def ReserveDuration(self, ReserveDuration):
        self._ReserveDuration = ReserveDuration

    @property
    def BackupFreq(self):
        return self._BackupFreq

    @BackupFreq.setter
    def BackupFreq(self, BackupFreq):
        self._BackupFreq = BackupFreq

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def LogicBackupConfig(self):
        return self._LogicBackupConfig

    @LogicBackupConfig.setter
    def LogicBackupConfig(self, LogicBackupConfig):
        self._LogicBackupConfig = LogicBackupConfig

    @property
    def DeleteAutoLogicBackup(self):
        return self._DeleteAutoLogicBackup

    @DeleteAutoLogicBackup.setter
    def DeleteAutoLogicBackup(self, DeleteAutoLogicBackup):
        self._DeleteAutoLogicBackup = DeleteAutoLogicBackup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupTimeBeg = params.get("BackupTimeBeg")
        self._BackupTimeEnd = params.get("BackupTimeEnd")
        self._ReserveDuration = params.get("ReserveDuration")
        self._BackupFreq = params.get("BackupFreq")
        self._BackupType = params.get("BackupType")
        if params.get("LogicBackupConfig") is not None:
            self._LogicBackupConfig = LogicBackupConfigInfo()
            self._LogicBackupConfig._deserialize(params.get("LogicBackupConfig"))
        self._DeleteAutoLogicBackup = params.get("DeleteAutoLogicBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

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


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BackupId: 备份文件ID
        :type BackupId: int
        :param _BackupName: 备注名，长度不能超过60个字符
        :type BackupName: str
        """
        self._ClusterId = None
        self._BackupId = None
        self._BackupName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupName(self):
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BackupId = params.get("BackupId")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName返回参数结构体

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


class ModifyBinlogConfigRequest(AbstractModel):
    """ModifyBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BinlogConfig: Binlog配置信息
        :type BinlogConfig: :class:`tencentcloud.cynosdb.v20190107.models.BinlogConfigInfo`
        """
        self._ClusterId = None
        self._BinlogConfig = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogConfig(self):
        return self._BinlogConfig

    @BinlogConfig.setter
    def BinlogConfig(self, BinlogConfig):
        self._BinlogConfig = BinlogConfig


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("BinlogConfig") is not None:
            self._BinlogConfig = BinlogConfigInfo()
            self._BinlogConfig._deserialize(params.get("BinlogConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBinlogConfigResponse(AbstractModel):
    """ModifyBinlogConfig返回参数结构体

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


class ModifyBinlogSaveDaysRequest(AbstractModel):
    """ModifyBinlogSaveDays请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _BinlogSaveDays: Binlog保留天数
        :type BinlogSaveDays: int
        """
        self._ClusterId = None
        self._BinlogSaveDays = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def BinlogSaveDays(self):
        return self._BinlogSaveDays

    @BinlogSaveDays.setter
    def BinlogSaveDays(self, BinlogSaveDays):
        self._BinlogSaveDays = BinlogSaveDays


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._BinlogSaveDays = params.get("BinlogSaveDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBinlogSaveDaysResponse(AbstractModel):
    """ModifyBinlogSaveDays返回参数结构体

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


class ModifyClusterDatabaseRequest(AbstractModel):
    """ModifyClusterDatabase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _DbName: 数据库名
        :type DbName: str
        :param _NewUserHostPrivileges: 新授权用户主机权限
        :type NewUserHostPrivileges: list of UserHostPrivilege
        :param _Description: 备注
        :type Description: str
        :param _OldUserHostPrivileges: 历史授权用户主机权限
        :type OldUserHostPrivileges: list of UserHostPrivilege
        """
        self._ClusterId = None
        self._DbName = None
        self._NewUserHostPrivileges = None
        self._Description = None
        self._OldUserHostPrivileges = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewUserHostPrivileges(self):
        return self._NewUserHostPrivileges

    @NewUserHostPrivileges.setter
    def NewUserHostPrivileges(self, NewUserHostPrivileges):
        self._NewUserHostPrivileges = NewUserHostPrivileges

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OldUserHostPrivileges(self):
        return self._OldUserHostPrivileges

    @OldUserHostPrivileges.setter
    def OldUserHostPrivileges(self, OldUserHostPrivileges):
        self._OldUserHostPrivileges = OldUserHostPrivileges


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DbName = params.get("DbName")
        if params.get("NewUserHostPrivileges") is not None:
            self._NewUserHostPrivileges = []
            for item in params.get("NewUserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._NewUserHostPrivileges.append(obj)
        self._Description = params.get("Description")
        if params.get("OldUserHostPrivileges") is not None:
            self._OldUserHostPrivileges = []
            for item in params.get("OldUserHostPrivileges"):
                obj = UserHostPrivilege()
                obj._deserialize(item)
                self._OldUserHostPrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterDatabaseResponse(AbstractModel):
    """ModifyClusterDatabase返回参数结构体

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


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名
        :type ClusterName: str
        """
        self._ClusterId = None
        self._ClusterName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

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


class ModifyClusterParamRequest(AbstractModel):
    """ModifyClusterParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ParamList: 要修改的参数列表。每一个元素是ParamName、CurrentValue和OldValue的组合。ParamName是参数名称，CurrentValue是当前值，OldValue是之前值且不做校验
        :type ParamList: list of ParamItem
        :param _IsInMaintainPeriod: 维护期间执行-yes,立即执行-no
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._ParamList = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterParamResponse(AbstractModel):
    """ModifyClusterParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步请求Id，用于查询结果
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyClusterPasswordComplexityRequest(AbstractModel):
    """ModifyClusterPasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ValidatePasswordLength: 密码长度
        :type ValidatePasswordLength: int
        :param _ValidatePasswordMixedCaseCount: 大小写字符个数
        :type ValidatePasswordMixedCaseCount: int
        :param _ValidatePasswordSpecialCharCount: 特殊字符个数
        :type ValidatePasswordSpecialCharCount: int
        :param _ValidatePasswordNumberCount: 数字个数
        :type ValidatePasswordNumberCount: int
        :param _ValidatePasswordPolicy: 密码强度（"MEDIUM", "STRONG"）
        :type ValidatePasswordPolicy: str
        :param _ValidatePasswordDictionary: 数据字典
        :type ValidatePasswordDictionary: list of str
        """
        self._ClusterId = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordSpecialCharCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordDictionary = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ValidatePasswordLength = params.get("ValidatePasswordLength")
        self._ValidatePasswordMixedCaseCount = params.get("ValidatePasswordMixedCaseCount")
        self._ValidatePasswordSpecialCharCount = params.get("ValidatePasswordSpecialCharCount")
        self._ValidatePasswordNumberCount = params.get("ValidatePasswordNumberCount")
        self._ValidatePasswordPolicy = params.get("ValidatePasswordPolicy")
        self._ValidatePasswordDictionary = params.get("ValidatePasswordDictionary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterPasswordComplexityResponse(AbstractModel):
    """ModifyClusterPasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyClusterSlaveZoneRequest(AbstractModel):
    """ModifyClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: str
        :param _OldSlaveZone: 旧从可用区
        :type OldSlaveZone: str
        :param _NewSlaveZone: 新从可用区
        :type NewSlaveZone: str
        :param _BinlogSyncWay: binlog同步方式。默认值：async。可选值：sync、semisync、async
        :type BinlogSyncWay: str
        """
        self._ClusterId = None
        self._OldSlaveZone = None
        self._NewSlaveZone = None
        self._BinlogSyncWay = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldSlaveZone(self):
        return self._OldSlaveZone

    @OldSlaveZone.setter
    def OldSlaveZone(self, OldSlaveZone):
        self._OldSlaveZone = OldSlaveZone

    @property
    def NewSlaveZone(self):
        return self._NewSlaveZone

    @NewSlaveZone.setter
    def NewSlaveZone(self, NewSlaveZone):
        self._NewSlaveZone = NewSlaveZone

    @property
    def BinlogSyncWay(self):
        return self._BinlogSyncWay

    @BinlogSyncWay.setter
    def BinlogSyncWay(self, BinlogSyncWay):
        self._BinlogSyncWay = BinlogSyncWay


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldSlaveZone = params.get("OldSlaveZone")
        self._NewSlaveZone = params.get("NewSlaveZone")
        self._BinlogSyncWay = params.get("BinlogSyncWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterSlaveZoneResponse(AbstractModel):
    """ModifyClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步FlowId
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyClusterStorageRequest(AbstractModel):
    """ModifyClusterStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NewStorageLimit: 集群新存储大小（单位G）
        :type NewStorageLimit: int
        :param _OldStorageLimit: 集群原存储大小（单位G）
        :type OldStorageLimit: int
        :param _DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        """
        self._ClusterId = None
        self._NewStorageLimit = None
        self._OldStorageLimit = None
        self._DealMode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NewStorageLimit(self):
        return self._NewStorageLimit

    @NewStorageLimit.setter
    def NewStorageLimit(self, NewStorageLimit):
        self._NewStorageLimit = NewStorageLimit

    @property
    def OldStorageLimit(self):
        return self._OldStorageLimit

    @OldStorageLimit.setter
    def OldStorageLimit(self, OldStorageLimit):
        self._OldStorageLimit = OldStorageLimit

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NewStorageLimit = params.get("NewStorageLimit")
        self._OldStorageLimit = params.get("OldStorageLimit")
        self._DealMode = params.get("DealMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterStorageResponse(AbstractModel):
    """ModifyClusterStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 网络组id(cynosdbmysql-grp-前缀开头)或集群id
        :type InstanceId: str
        :param _SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组ID组成的数组。
        :type SecurityGroupIds: list of str
        :param _Zone: 可用区
        :type Zone: str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None
        self._Zone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

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


class ModifyDbVersionData(AbstractModel):
    """修改数据库内核版本任务信息

    """

    def __init__(self):
        r"""
        :param _OldVersion: 修改前版本
        :type OldVersion: str
        :param _NewVersion: 修改后版本
        :type NewVersion: str
        :param _UpgradeType: 升级方式
        :type UpgradeType: str
        """
        self._OldVersion = None
        self._NewVersion = None
        self._UpgradeType = None

    @property
    def OldVersion(self):
        return self._OldVersion

    @OldVersion.setter
    def OldVersion(self, OldVersion):
        self._OldVersion = OldVersion

    @property
    def NewVersion(self):
        return self._NewVersion

    @NewVersion.setter
    def NewVersion(self, NewVersion):
        self._NewVersion = NewVersion

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType


    def _deserialize(self, params):
        self._OldVersion = params.get("OldVersion")
        self._NewVersion = params.get("NewVersion")
        self._UpgradeType = params.get("UpgradeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceData(AbstractModel):
    """实例变配任务信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 变配后CPU
        :type Cpu: int
        :param _Memory: 变配后内存
        :type Memory: int
        :param _StorageLimit: 变配后存储上限
        :type StorageLimit: int
        :param _OldCpu: 变配前CPU
        :type OldCpu: int
        :param _OldMemory: 变配前内存
        :type OldMemory: int
        :param _OldStorageLimit: 变配前存储上限
        :type OldStorageLimit: int
        :param _OldDeviceType: 变配前实例机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OldDeviceType: str
        :param _DeviceType: 变配后实例机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _UpgradeType: 升级方式。升级完成后切换或维护时间内切换
        :type UpgradeType: str
        """
        self._Cpu = None
        self._Memory = None
        self._StorageLimit = None
        self._OldCpu = None
        self._OldMemory = None
        self._OldStorageLimit = None
        self._OldDeviceType = None
        self._DeviceType = None
        self._UpgradeType = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def OldCpu(self):
        return self._OldCpu

    @OldCpu.setter
    def OldCpu(self, OldCpu):
        self._OldCpu = OldCpu

    @property
    def OldMemory(self):
        return self._OldMemory

    @OldMemory.setter
    def OldMemory(self, OldMemory):
        self._OldMemory = OldMemory

    @property
    def OldStorageLimit(self):
        return self._OldStorageLimit

    @OldStorageLimit.setter
    def OldStorageLimit(self, OldStorageLimit):
        self._OldStorageLimit = OldStorageLimit

    @property
    def OldDeviceType(self):
        return self._OldDeviceType

    @OldDeviceType.setter
    def OldDeviceType(self, OldDeviceType):
        self._OldDeviceType = OldDeviceType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageLimit = params.get("StorageLimit")
        self._OldCpu = params.get("OldCpu")
        self._OldMemory = params.get("OldMemory")
        self._OldStorageLimit = params.get("OldStorageLimit")
        self._OldDeviceType = params.get("OldDeviceType")
        self._DeviceType = params.get("DeviceType")
        self._UpgradeType = params.get("UpgradeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName返回参数结构体

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


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIds: 实例ID
        :type InstanceIds: list of str
        :param _ClusterParamList: 集群参数列表，例如 [{           "CurrentValue":"2",        "ParamName":"auto_increment_increment"}]
        :type ClusterParamList: list of ModifyParamItem
        :param _InstanceParamList: 实例参数列表，例如[{           "CurrentValue":"2",        "ParamName":"innodb_stats_transient_sample_pages"}]
        :type InstanceParamList: list of ModifyParamItem
        :param _IsInMaintainPeriod: yes：在运维时间窗内修改，no：立即执行（默认值）
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._ClusterParamList = None
        self._InstanceParamList = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClusterParamList(self):
        return self._ClusterParamList

    @ClusterParamList.setter
    def ClusterParamList(self, ClusterParamList):
        self._ClusterParamList = ClusterParamList

    @property
    def InstanceParamList(self):
        return self._InstanceParamList

    @InstanceParamList.setter
    def InstanceParamList(self, InstanceParamList):
        self._InstanceParamList = InstanceParamList

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ClusterParamList") is not None:
            self._ClusterParamList = []
            for item in params.get("ClusterParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ClusterParamList.append(obj)
        if params.get("InstanceParamList") is not None:
            self._InstanceParamList = []
            for item in params.get("InstanceParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._InstanceParamList.append(obj)
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceUpgradeLimitDaysRequest(AbstractModel):
    """ModifyInstanceUpgradeLimitDays请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _UpgradeLimitDays: 升级限制时间
        :type UpgradeLimitDays: int
        """
        self._ClusterId = None
        self._InstanceId = None
        self._UpgradeLimitDays = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeLimitDays(self):
        return self._UpgradeLimitDays

    @UpgradeLimitDays.setter
    def UpgradeLimitDays(self, UpgradeLimitDays):
        self._UpgradeLimitDays = UpgradeLimitDays


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceId = params.get("InstanceId")
        self._UpgradeLimitDays = params.get("UpgradeLimitDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceUpgradeLimitDaysResponse(AbstractModel):
    """ModifyInstanceUpgradeLimitDays返回参数结构体

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


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _MaintainStartTime: 维护开始时间，单位为秒，如3:00为10800
        :type MaintainStartTime: int
        :param _MaintainDuration: 维护持续时间，单位为秒，如1小时为3600
        :type MaintainDuration: int
        :param _MaintainWeekDays: 每周维护日期，日期取值范围[Mon, Tue, Wed, Thu, Fri, Sat, Sun]
        :type MaintainWeekDays: list of str
        """
        self._InstanceId = None
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig返回参数结构体

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


class ModifyParamItem(AbstractModel):
    """修改的实例参数信息

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _CurrentValue: 参数当前值
        :type CurrentValue: str
        :param _OldValue: 参数旧值（只在出参时有用）
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._OldValue = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: int
        :param _TemplateName: 模板名
        :type TemplateName: str
        :param _TemplateDescription: 模板描述
        :type TemplateDescription: str
        :param _ParamList: 参数列表
        :type ParamList: list of ModifyParamItem
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._ParamList = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate返回参数结构体

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


class ModifyParamsData(AbstractModel):
    """修改参数信息

    """

    def __init__(self):
        r"""
        :param _Name: 参数名
        :type Name: str
        :param _OldValue: 修改前参数值
        :type OldValue: str
        :param _CurValue: 修改后参数值
        :type CurValue: str
        """
        self._Name = None
        self._OldValue = None
        self._CurValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def CurValue(self):
        return self._CurValue

    @CurValue.setter
    def CurValue(self, CurValue):
        self._CurValue = CurValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._OldValue = params.get("OldValue")
        self._CurValue = params.get("CurValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyDescRequest(AbstractModel):
    """ModifyProxyDesc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _Description: 数据库代理描述
        :type Description: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._Description = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyDescResponse(AbstractModel):
    """ModifyProxyDesc返回参数结构体

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


class ModifyProxyRwSplitRequest(AbstractModel):
    """ModifyProxyRwSplit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID，例如cynosdbmysql-asd123
        :type ClusterId: str
        :param _ProxyGroupId: 数据库代理组ID，例如cynosdbmysql-proxy-qwe123
        :type ProxyGroupId: str
        :param _ConsistencyType: 一致性类型；“eventual"-最终一致性, "session"-会话一致性, "global"-全局一致性
        :type ConsistencyType: str
        :param _ConsistencyTimeOut: 一致性超时时间。
取值范围：0~1000000（微秒）,设置0则表示若只读实例出现延迟, 导致一致性策略不满足, 请求将一直等待。
        :type ConsistencyTimeOut: str
        :param _WeightMode: 读写权重分配模式；系统自动分配："system"， 自定义："custom"
        :type WeightMode: str
        :param _InstanceWeights: 实例只读权重。
该参数必填。
        :type InstanceWeights: list of ProxyInstanceWeight
        :param _FailOver: 是否开启故障转移，代理出现故障后，连接地址将路由到主实例，取值："yes" , "no"
        :type FailOver: str
        :param _AutoAddRo: 是否自动添加只读实例，取值："yes" , "no"
        :type AutoAddRo: str
        :param _OpenRw: 是否打开读写分离。
该参数已废弃，请通过RwType设置读写属性。
        :type OpenRw: str
        :param _RwType: 读写类型：
READWRITE,READONLY
        :type RwType: str
        :param _TransSplit: 事务拆分。
在一个事务中拆分读和写到不同的实例上去执行。
        :type TransSplit: bool
        :param _AccessMode: 连接模式：
nearby,balance
        :type AccessMode: str
        :param _OpenConnectionPool: 是否打开连接池：
yes,no
        :type OpenConnectionPool: str
        :param _ConnectionPoolType: 连接池类型：
SessionConnectionPool
        :type ConnectionPoolType: str
        :param _ConnectionPoolTimeOut: 连接池时间。
可选范围:0~300（秒）
        :type ConnectionPoolTimeOut: int
        """
        self._ClusterId = None
        self._ProxyGroupId = None
        self._ConsistencyType = None
        self._ConsistencyTimeOut = None
        self._WeightMode = None
        self._InstanceWeights = None
        self._FailOver = None
        self._AutoAddRo = None
        self._OpenRw = None
        self._RwType = None
        self._TransSplit = None
        self._AccessMode = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None
        self._ConnectionPoolTimeOut = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ConsistencyType = params.get("ConsistencyType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._WeightMode = params.get("WeightMode")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._OpenRw = params.get("OpenRw")
        self._RwType = params.get("RwType")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyRwSplitResponse(AbstractModel):
    """ModifyProxyRwSplit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步FlowId
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyResourcePackageClustersRequest(AbstractModel):
    """ModifyResourcePackageClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包唯一ID
        :type PackageId: str
        :param _BindClusterIds: 需要建立绑定关系的集群ID
        :type BindClusterIds: list of str
        :param _UnbindClusterIds: 需要解除绑定关系的集群ID
        :type UnbindClusterIds: list of str
        """
        self._PackageId = None
        self._BindClusterIds = None
        self._UnbindClusterIds = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def BindClusterIds(self):
        return self._BindClusterIds

    @BindClusterIds.setter
    def BindClusterIds(self, BindClusterIds):
        self._BindClusterIds = BindClusterIds

    @property
    def UnbindClusterIds(self):
        return self._UnbindClusterIds

    @UnbindClusterIds.setter
    def UnbindClusterIds(self, UnbindClusterIds):
        self._UnbindClusterIds = UnbindClusterIds


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._BindClusterIds = params.get("BindClusterIds")
        self._UnbindClusterIds = params.get("UnbindClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackageClustersResponse(AbstractModel):
    """ModifyResourcePackageClusters返回参数结构体

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


class ModifyResourcePackageNameRequest(AbstractModel):
    """ModifyResourcePackageName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包唯一ID
        :type PackageId: str
        :param _PackageName: 自定义的资源包名称，最长支持120个字符
        :type PackageName: str
        """
        self._PackageId = None
        self._PackageName = None

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


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackageNameResponse(AbstractModel):
    """ModifyResourcePackageName返回参数结构体

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


class ModifyResourcePackagesDeductionPriorityRequest(AbstractModel):
    """ModifyResourcePackagesDeductionPriority请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageType: 需要修改优先级的资源包类型，CCU：计算资源包，DISK：存储资源包
        :type PackageType: str
        :param _ClusterId: 修改后的抵扣优先级对于哪个cynos资源生效
        :type ClusterId: str
        :param _DeductionPriorities: 资源包抵扣优先级
        :type DeductionPriorities: list of PackagePriority
        """
        self._PackageType = None
        self._ClusterId = None
        self._DeductionPriorities = None

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DeductionPriorities(self):
        return self._DeductionPriorities

    @DeductionPriorities.setter
    def DeductionPriorities(self, DeductionPriorities):
        self._DeductionPriorities = DeductionPriorities


    def _deserialize(self, params):
        self._PackageType = params.get("PackageType")
        self._ClusterId = params.get("ClusterId")
        if params.get("DeductionPriorities") is not None:
            self._DeductionPriorities = []
            for item in params.get("DeductionPriorities"):
                obj = PackagePriority()
                obj._deserialize(item)
                self._DeductionPriorities.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePackagesDeductionPriorityResponse(AbstractModel):
    """ModifyResourcePackagesDeductionPriority返回参数结构体

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


class ModifyServerlessStrategyRequest(AbstractModel):
    """ModifyServerlessStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: serverless集群id
        :type ClusterId: str
        :param _AutoPause: 集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
        :type AutoPause: str
        :param _AutoPauseDelay: 集群自动暂停的延迟，单位秒，可选范围[600,691200]，默认600
        :type AutoPauseDelay: int
        :param _AutoScaleUpDelay: 该参数暂时无效
        :type AutoScaleUpDelay: int
        :param _AutoScaleDownDelay: 该参数暂时无效
        :type AutoScaleDownDelay: int
        :param _MinCpu: cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinCpu: float
        :param _MaxCpu: cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxCpu: float
        :param _MinRoCpu: 只读实例cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinRoCpu: float
        :param _MaxRoCpu: 只读cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxRoCpu: float
        :param _MinRoCount: 只读节点最小个数
        :type MinRoCount: int
        :param _MaxRoCount: 只读节点最大个数
        :type MaxRoCount: int
        :param _AutoScaleUp: 集群是否允许扩容，可选范围<li>yes</li><li>no</li>
        :type AutoScaleUp: str
        :param _AutoScaleDown: 集群是否允许缩容，可选范围<li>yes</li><li>no</li>
        :type AutoScaleDown: str
        """
        self._ClusterId = None
        self._AutoPause = None
        self._AutoPauseDelay = None
        self._AutoScaleUpDelay = None
        self._AutoScaleDownDelay = None
        self._MinCpu = None
        self._MaxCpu = None
        self._MinRoCpu = None
        self._MaxRoCpu = None
        self._MinRoCount = None
        self._MaxRoCount = None
        self._AutoScaleUp = None
        self._AutoScaleDown = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoPause(self):
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def AutoScaleUpDelay(self):
        return self._AutoScaleUpDelay

    @AutoScaleUpDelay.setter
    def AutoScaleUpDelay(self, AutoScaleUpDelay):
        self._AutoScaleUpDelay = AutoScaleUpDelay

    @property
    def AutoScaleDownDelay(self):
        return self._AutoScaleDownDelay

    @AutoScaleDownDelay.setter
    def AutoScaleDownDelay(self, AutoScaleDownDelay):
        self._AutoScaleDownDelay = AutoScaleDownDelay

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def MinRoCpu(self):
        return self._MinRoCpu

    @MinRoCpu.setter
    def MinRoCpu(self, MinRoCpu):
        self._MinRoCpu = MinRoCpu

    @property
    def MaxRoCpu(self):
        return self._MaxRoCpu

    @MaxRoCpu.setter
    def MaxRoCpu(self, MaxRoCpu):
        self._MaxRoCpu = MaxRoCpu

    @property
    def MinRoCount(self):
        return self._MinRoCount

    @MinRoCount.setter
    def MinRoCount(self, MinRoCount):
        self._MinRoCount = MinRoCount

    @property
    def MaxRoCount(self):
        return self._MaxRoCount

    @MaxRoCount.setter
    def MaxRoCount(self, MaxRoCount):
        self._MaxRoCount = MaxRoCount

    @property
    def AutoScaleUp(self):
        return self._AutoScaleUp

    @AutoScaleUp.setter
    def AutoScaleUp(self, AutoScaleUp):
        self._AutoScaleUp = AutoScaleUp

    @property
    def AutoScaleDown(self):
        return self._AutoScaleDown

    @AutoScaleDown.setter
    def AutoScaleDown(self, AutoScaleDown):
        self._AutoScaleDown = AutoScaleDown


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AutoPause = params.get("AutoPause")
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._AutoScaleUpDelay = params.get("AutoScaleUpDelay")
        self._AutoScaleDownDelay = params.get("AutoScaleDownDelay")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._MinRoCpu = params.get("MinRoCpu")
        self._MaxRoCpu = params.get("MaxRoCpu")
        self._MinRoCount = params.get("MinRoCount")
        self._MaxRoCount = params.get("MaxRoCount")
        self._AutoScaleUp = params.get("AutoScaleUp")
        self._AutoScaleDown = params.get("AutoScaleDown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServerlessStrategyResponse(AbstractModel):
    """ModifyServerlessStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyVipVportRequest(AbstractModel):
    """ModifyVipVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _InstanceGrpId: 实例组id
        :type InstanceGrpId: str
        :param _InstanceGroupId: 实例组id
        :type InstanceGroupId: str
        :param _Vip: 需要修改的目的ip
        :type Vip: str
        :param _Vport: 需要修改的目的端口
        :type Vport: int
        :param _DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param _OldIpReserveHours: 旧ip回收前的保留时间，单位小时，0表示立即回收
        :type OldIpReserveHours: int
        """
        self._ClusterId = None
        self._InstanceGrpId = None
        self._InstanceGroupId = None
        self._Vip = None
        self._Vport = None
        self._DbType = None
        self._OldIpReserveHours = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._DbType = params.get("DbType")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVipVportResponse(AbstractModel):
    """ModifyVipVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class Module(AbstractModel):
    """系统支持的模块

    """

    def __init__(self):
        r"""
        :param _IsDisable: 是否支持，可选值:yes,no
        :type IsDisable: str
        :param _ModuleName: 模块名
        :type ModuleName: str
        """
        self._IsDisable = None
        self._ModuleName = None

    @property
    def IsDisable(self):
        return self._IsDisable

    @IsDisable.setter
    def IsDisable(self, IsDisable):
        self._IsDisable = IsDisable

    @property
    def ModuleName(self):
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._IsDisable = params.get("IsDisable")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetAddr(AbstractModel):
    """网络信息

    """

    def __init__(self):
        r"""
        :param _Vip: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: 内网端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _WanDomain: 外网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type WanDomain: str
        :param _WanPort: 外网端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type WanPort: int
        :param _NetType: 网络类型（ro-只读,rw/ha-读写）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        :param _UniqSubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _UniqVpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _WanIP: 外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIP: str
        :param _WanStatus: 外网状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WanStatus: str
        :param _InstanceGroupId: 实例组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: str
        """
        self._Vip = None
        self._Vport = None
        self._WanDomain = None
        self._WanPort = None
        self._NetType = None
        self._UniqSubnetId = None
        self._UniqVpcId = None
        self._Description = None
        self._WanIP = None
        self._WanStatus = None
        self._InstanceGroupId = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WanIP(self):
        return self._WanIP

    @WanIP.setter
    def WanIP(self, WanIP):
        self._WanIP = WanIP

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._WanDomain = params.get("WanDomain")
        self._WanPort = params.get("WanPort")
        self._NetType = params.get("NetType")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Description = params.get("Description")
        self._WanIP = params.get("WanIP")
        self._WanStatus = params.get("WanStatus")
        self._InstanceGroupId = params.get("InstanceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAccount(AbstractModel):
    """x08新创建的账号

    """

    def __init__(self):
        r"""
        :param _AccountName: 账户名，包含字母数字_,以字母开头，字母或数字结尾，长度1-30
        :type AccountName: str
        :param _AccountPassword: 密码，密码长度范围为8到64个字符
        :type AccountPassword: str
        :param _Host: 主机(%或ipv4地址)
        :type Host: str
        :param _Description: 描述
        :type Description: str
        :param _MaxUserConnections: 用户最大连接数，不能大于10240
        :type MaxUserConnections: int
        """
        self._AccountName = None
        self._AccountPassword = None
        self._Host = None
        self._Description = None
        self._MaxUserConnections = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._Host = params.get("Host")
        self._Description = params.get("Description")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTask(AbstractModel):
    """任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务自增ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param _ObjectId: 任务ID（集群ID|实例组ID|实例ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectId: str
        :param _ObjectType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectType: str
        """
        self._TaskId = None
        self._TaskType = None
        self._TaskStatus = None
        self._ObjectId = None
        self._ObjectType = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ObjectId(self):
        return self._ObjectId

    @ObjectId.setter
    def ObjectId(self, ObjectId):
        self._ObjectId = ObjectId

    @property
    def ObjectType(self):
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._TaskStatus = params.get("TaskStatus")
        self._ObjectId = params.get("ObjectId")
        self._ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdList: 实例ID数组
        :type InstanceIdList: list of str
        """
        self._ClusterId = None
        self._InstanceIdList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OldAddrInfo(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        r"""
        :param _Vip: IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _ReturnTime: 期望执行回收时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnTime: str
        """
        self._Vip = None
        self._Vport = None
        self._ReturnTime = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def ReturnTime(self):
        return self._ReturnTime

    @ReturnTime.setter
    def ReturnTime(self, ReturnTime):
        self._ReturnTime = ReturnTime


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._ReturnTime = params.get("ReturnTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _LogExpireDay: 日志保留时长。
        :type LogExpireDay: int
        :param _HighLogExpireDay: 高频日志保留时长。
        :type HighLogExpireDay: int
        :param _AuditRuleFilters: 审计规则。同RuleTemplateIds都不填是全审计。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: 规则模板ID。同AuditRuleFilters都不填是全审计。
        :type RuleTemplateIds: list of str
        :param _AuditAll: 审计类型。true-全审计；默认false-规则审计。
        :type AuditAll: bool
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None
        self._AuditAll = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        self._AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceResponse(AbstractModel):
    """OpenAuditService返回参数结构体

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


class OpenClusterPasswordComplexityRequest(AbstractModel):
    """OpenClusterPasswordComplexity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ValidatePasswordLength: 密码长度
        :type ValidatePasswordLength: int
        :param _ValidatePasswordMixedCaseCount: 大小写字符个数
        :type ValidatePasswordMixedCaseCount: int
        :param _ValidatePasswordSpecialCharCount: 特殊字符个数
        :type ValidatePasswordSpecialCharCount: int
        :param _ValidatePasswordNumberCount: 数字个数
        :type ValidatePasswordNumberCount: int
        :param _ValidatePasswordPolicy: 密码强度（"MEDIUM", "STRONG"）
        :type ValidatePasswordPolicy: str
        :param _ValidatePasswordDictionary: 数据字典
        :type ValidatePasswordDictionary: list of str
        """
        self._ClusterId = None
        self._ValidatePasswordLength = None
        self._ValidatePasswordMixedCaseCount = None
        self._ValidatePasswordSpecialCharCount = None
        self._ValidatePasswordNumberCount = None
        self._ValidatePasswordPolicy = None
        self._ValidatePasswordDictionary = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ValidatePasswordLength(self):
        return self._ValidatePasswordLength

    @ValidatePasswordLength.setter
    def ValidatePasswordLength(self, ValidatePasswordLength):
        self._ValidatePasswordLength = ValidatePasswordLength

    @property
    def ValidatePasswordMixedCaseCount(self):
        return self._ValidatePasswordMixedCaseCount

    @ValidatePasswordMixedCaseCount.setter
    def ValidatePasswordMixedCaseCount(self, ValidatePasswordMixedCaseCount):
        self._ValidatePasswordMixedCaseCount = ValidatePasswordMixedCaseCount

    @property
    def ValidatePasswordSpecialCharCount(self):
        return self._ValidatePasswordSpecialCharCount

    @ValidatePasswordSpecialCharCount.setter
    def ValidatePasswordSpecialCharCount(self, ValidatePasswordSpecialCharCount):
        self._ValidatePasswordSpecialCharCount = ValidatePasswordSpecialCharCount

    @property
    def ValidatePasswordNumberCount(self):
        return self._ValidatePasswordNumberCount

    @ValidatePasswordNumberCount.setter
    def ValidatePasswordNumberCount(self, ValidatePasswordNumberCount):
        self._ValidatePasswordNumberCount = ValidatePasswordNumberCount

    @property
    def ValidatePasswordPolicy(self):
        return self._ValidatePasswordPolicy

    @ValidatePasswordPolicy.setter
    def ValidatePasswordPolicy(self, ValidatePasswordPolicy):
        self._ValidatePasswordPolicy = ValidatePasswordPolicy

    @property
    def ValidatePasswordDictionary(self):
        return self._ValidatePasswordDictionary

    @ValidatePasswordDictionary.setter
    def ValidatePasswordDictionary(self, ValidatePasswordDictionary):
        self._ValidatePasswordDictionary = ValidatePasswordDictionary


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ValidatePasswordLength = params.get("ValidatePasswordLength")
        self._ValidatePasswordMixedCaseCount = params.get("ValidatePasswordMixedCaseCount")
        self._ValidatePasswordSpecialCharCount = params.get("ValidatePasswordSpecialCharCount")
        self._ValidatePasswordNumberCount = params.get("ValidatePasswordNumberCount")
        self._ValidatePasswordPolicy = params.get("ValidatePasswordPolicy")
        self._ValidatePasswordDictionary = params.get("ValidatePasswordDictionary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenClusterPasswordComplexityResponse(AbstractModel):
    """OpenClusterPasswordComplexity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenClusterReadOnlyInstanceGroupAccessRequest(AbstractModel):
    """OpenClusterReadOnlyInstanceGroupAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Port: 端口
        :type Port: str
        :param _SecurityGroupIds: 安全组ID 
        :type SecurityGroupIds: list of str
        """
        self._ClusterId = None
        self._Port = None
        self._SecurityGroupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Port = params.get("Port")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenClusterReadOnlyInstanceGroupAccessResponse(AbstractModel):
    """OpenClusterReadOnlyInstanceGroupAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 开启流程ID
        :type FlowId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenReadOnlyInstanceExclusiveAccessRequest(AbstractModel):
    """OpenReadOnlyInstanceExclusiveAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 请使用 [集群信息描述](https://cloud.tencent.com/document/api/1003/48086) 获取 clusterId。
        :type ClusterId: str
        :param _InstanceId: 请使用 [集群信息描述](https://cloud.tencent.com/document/api/1003/48086) 获取 instanceId。
        :type InstanceId: str
        :param _VpcId: 指定的 vpc ID，请使用 [查询私有网络列表](https://cloud.tencent.com/document/api/215/15778) 获取 vpc ID。
        :type VpcId: str
        :param _SubnetId: 指定的子网 ID，如果设置了 vpc ID，则 SubnetId 必填，请使用 [查询子网列表](https://cloud.tencent.com/document/api/215/15784) 获取 SubnetId。
        :type SubnetId: str
        :param _Port: 用户自定义的端口。
        :type Port: int
        :param _SecurityGroupIds: 安全组 ID，请使用 [查看安全组](https://cloud.tencent.com/document/api/215/15808) 获取 SecurityGroupId。
        :type SecurityGroupIds: list of str
        """
        self._ClusterId = None
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Port = None
        self._SecurityGroupIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Port = params.get("Port")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenReadOnlyInstanceExclusiveAccessResponse(AbstractModel):
    """OpenReadOnlyInstanceExclusiveAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 开通流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class OpenWanRequest(AbstractModel):
    """OpenWan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceGrpId: 实例组id
        :type InstanceGrpId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceGroupId: 实例组id
        :type InstanceGroupId: str
        """
        self._InstanceGrpId = None
        self._InstanceId = None
        self._InstanceGroupId = None

    @property
    def InstanceGrpId(self):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        return self._InstanceGrpId

    @InstanceGrpId.setter
    def InstanceGrpId(self, InstanceGrpId):
        warnings.warn("parameter `InstanceGrpId` is deprecated", DeprecationWarning) 

        self._InstanceGrpId = InstanceGrpId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._InstanceGrpId = params.get("InstanceGrpId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanResponse(AbstractModel):
    """OpenWan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class Package(AbstractModel):
    """资源包

    """

    def __init__(self):
        r"""
        :param _AppId: AppID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _PackageId: 资源包唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _PackageName: 资源包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageType: 资源包类型
CCU-计算资源包，DISK-存储资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _PackageRegion: 资源包使用地域
china-中国内地通用，overseas-港澳台及海外通用
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageRegion: str
        :param _Status: 资源包状态
creating-创建中；
using-使用中；
expired-已过期；
normal_finish-使用完；
apply_refund-申请退费中；
refund-已退费。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _PackageTotalSpec: 资源包总量
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTotalSpec: float
        :param _PackageUsedSpec: 资源包已使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageUsedSpec: float
        :param _HasQuota: 是否还有库存余量
注意：此字段可能返回 null，表示取不到有效值。
        :type HasQuota: bool
        :param _BindInstanceInfos: 绑定实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BindInstanceInfos: list of BindInstanceInfo
        :param _StartTime: 生效时间：2022-07-01 00:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _ExpireTime: 失效时间：2022-08-01 00:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _HistoryBindResourceInfos: 资源包历史绑定（已解绑）实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HistoryBindResourceInfos: list of BindInstanceInfo
        """
        self._AppId = None
        self._PackageId = None
        self._PackageName = None
        self._PackageType = None
        self._PackageRegion = None
        self._Status = None
        self._PackageTotalSpec = None
        self._PackageUsedSpec = None
        self._HasQuota = None
        self._BindInstanceInfos = None
        self._StartTime = None
        self._ExpireTime = None
        self._HistoryBindResourceInfos = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PackageTotalSpec(self):
        return self._PackageTotalSpec

    @PackageTotalSpec.setter
    def PackageTotalSpec(self, PackageTotalSpec):
        self._PackageTotalSpec = PackageTotalSpec

    @property
    def PackageUsedSpec(self):
        return self._PackageUsedSpec

    @PackageUsedSpec.setter
    def PackageUsedSpec(self, PackageUsedSpec):
        self._PackageUsedSpec = PackageUsedSpec

    @property
    def HasQuota(self):
        return self._HasQuota

    @HasQuota.setter
    def HasQuota(self, HasQuota):
        self._HasQuota = HasQuota

    @property
    def BindInstanceInfos(self):
        return self._BindInstanceInfos

    @BindInstanceInfos.setter
    def BindInstanceInfos(self, BindInstanceInfos):
        self._BindInstanceInfos = BindInstanceInfos

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
    def HistoryBindResourceInfos(self):
        return self._HistoryBindResourceInfos

    @HistoryBindResourceInfos.setter
    def HistoryBindResourceInfos(self, HistoryBindResourceInfos):
        self._HistoryBindResourceInfos = HistoryBindResourceInfos


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        self._PackageType = params.get("PackageType")
        self._PackageRegion = params.get("PackageRegion")
        self._Status = params.get("Status")
        self._PackageTotalSpec = params.get("PackageTotalSpec")
        self._PackageUsedSpec = params.get("PackageUsedSpec")
        self._HasQuota = params.get("HasQuota")
        if params.get("BindInstanceInfos") is not None:
            self._BindInstanceInfos = []
            for item in params.get("BindInstanceInfos"):
                obj = BindInstanceInfo()
                obj._deserialize(item)
                self._BindInstanceInfos.append(obj)
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("HistoryBindResourceInfos") is not None:
            self._HistoryBindResourceInfos = []
            for item in params.get("HistoryBindResourceInfos"):
                obj = BindInstanceInfo()
                obj._deserialize(item)
                self._HistoryBindResourceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageDetail(AbstractModel):
    """资源包明细说明

    """

    def __init__(self):
        r"""
        :param _AppId: AppId账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _PackageId: 资源包唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _SuccessDeductSpec: 成功抵扣容量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessDeductSpec: float
        :param _PackageTotalUsedSpec: 截止当前，资源包已使用的容量
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTotalUsedSpec: float
        :param _StartTime: 抵扣开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 抵扣结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ExtendInfo: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtendInfo: str
        """
        self._AppId = None
        self._PackageId = None
        self._InstanceId = None
        self._SuccessDeductSpec = None
        self._PackageTotalUsedSpec = None
        self._StartTime = None
        self._EndTime = None
        self._ExtendInfo = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SuccessDeductSpec(self):
        return self._SuccessDeductSpec

    @SuccessDeductSpec.setter
    def SuccessDeductSpec(self, SuccessDeductSpec):
        self._SuccessDeductSpec = SuccessDeductSpec

    @property
    def PackageTotalUsedSpec(self):
        return self._PackageTotalUsedSpec

    @PackageTotalUsedSpec.setter
    def PackageTotalUsedSpec(self, PackageTotalUsedSpec):
        self._PackageTotalUsedSpec = PackageTotalUsedSpec

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
    def ExtendInfo(self):
        return self._ExtendInfo

    @ExtendInfo.setter
    def ExtendInfo(self, ExtendInfo):
        self._ExtendInfo = ExtendInfo


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PackageId = params.get("PackageId")
        self._InstanceId = params.get("InstanceId")
        self._SuccessDeductSpec = params.get("SuccessDeductSpec")
        self._PackageTotalUsedSpec = params.get("PackageTotalUsedSpec")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExtendInfo = params.get("ExtendInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackagePriority(AbstractModel):
    """资源包抵扣优先级

    """

    def __init__(self):
        r"""
        :param _PackageId: 需要自定义抵扣优先级的资源包
        :type PackageId: str
        :param _DeductionPriority: 自定义的抵扣优先级
        :type DeductionPriority: int
        """
        self._PackageId = None
        self._DeductionPriority = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeductionPriority(self):
        return self._DeductionPriority

    @DeductionPriority.setter
    def DeductionPriority(self, DeductionPriority):
        self._DeductionPriority = DeductionPriority


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._DeductionPriority = params.get("DeductionPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDetail(AbstractModel):
    """实例参数详细描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _ParamType: 参数类型：integer，enum，float，string，func
        :type ParamType: str
        :param _SupportFunc: true-支持"func"，false-不支持公式
        :type SupportFunc: bool
        :param _Default: 默认值
        :type Default: str
        :param _Description: 参数描述
        :type Description: str
        :param _CurrentValue: 参数当前值
        :type CurrentValue: str
        :param _NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。0-不需要重启，1-需要重启。
        :type NeedReboot: int
        :param _Max: 参数容许的最大值
        :type Max: str
        :param _Min: 参数容许的最小值
        :type Min: str
        :param _EnumValue: 参数的可选枚举值。如果为非枚举值，则为空
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param _IsGlobal: 1：全局参数，0：非全局参数
        :type IsGlobal: int
        :param _MatchType: 匹配类型，multiVal
        :type MatchType: str
        :param _MatchValue: 匹配目标值，当multiVal时，各个key用，分割
        :type MatchValue: str
        :param _IsFunc: true-为公式，false-非公式
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFunc: bool
        :param _Func: 参数设置为公式时，Func返回设置的公式内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Func: str
        :param _ModifiableInfo: 参数是否可修改
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param _FuncPattern: 支持公式的参数的默认公式样式
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncPattern: str
        """
        self._ParamName = None
        self._ParamType = None
        self._SupportFunc = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._IsGlobal = None
        self._MatchType = None
        self._MatchValue = None
        self._IsFunc = None
        self._Func = None
        self._ModifiableInfo = None
        self._FuncPattern = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def SupportFunc(self):
        return self._SupportFunc

    @SupportFunc.setter
    def SupportFunc(self, SupportFunc):
        self._SupportFunc = SupportFunc

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def ModifiableInfo(self):
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo

    @property
    def FuncPattern(self):
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        self._SupportFunc = params.get("SupportFunc")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._IsGlobal = params.get("IsGlobal")
        self._MatchType = params.get("MatchType")
        self._MatchValue = params.get("MatchValue")
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        if params.get("ModifiableInfo") is not None:
            self._ModifiableInfo = ModifiableInfo()
            self._ModifiableInfo._deserialize(params.get("ModifiableInfo"))
        self._FuncPattern = params.get("FuncPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """参数信息

    """

    def __init__(self):
        r"""
        :param _CurrentValue: 当前值
        :type CurrentValue: str
        :param _Default: 默认值
        :type Default: str
        :param _EnumValue: 参数为enum/string/bool时，可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param _Max: 参数类型为float/integer时的最大值
        :type Max: str
        :param _Min: 参数类型为float/integer时的最小值
        :type Min: str
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _NeedReboot: 是否需要重启生效
        :type NeedReboot: int
        :param _ParamType: 参数类型：integer/float/string/enum/bool
        :type ParamType: str
        :param _MatchType: 匹配类型，multiVal, regex在参数类型是string时使用
        :type MatchType: str
        :param _MatchValue: 匹配目标值，当multiVal时，各个key用;分割
        :type MatchValue: str
        :param _Description: 参数描述
        :type Description: str
        :param _IsGlobal: 是否为全局参数
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGlobal: int
        :param _ModifiableInfo: 参数是否可修改
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param _IsFunc: 是否为函数
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFunc: bool
        :param _Func: 函数
注意：此字段可能返回 null，表示取不到有效值。
        :type Func: str
        :param _FuncPattern: 支持公式的参数的默认公式样式
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncPattern: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._Max = None
        self._Min = None
        self._ParamName = None
        self._NeedReboot = None
        self._ParamType = None
        self._MatchType = None
        self._MatchValue = None
        self._Description = None
        self._IsGlobal = None
        self._ModifiableInfo = None
        self._IsFunc = None
        self._Func = None
        self._FuncPattern = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def ModifiableInfo(self):
        return self._ModifiableInfo

    @ModifiableInfo.setter
    def ModifiableInfo(self, ModifiableInfo):
        self._ModifiableInfo = ModifiableInfo

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def FuncPattern(self):
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._ParamName = params.get("ParamName")
        self._NeedReboot = params.get("NeedReboot")
        self._ParamType = params.get("ParamType")
        self._MatchType = params.get("MatchType")
        self._MatchValue = params.get("MatchValue")
        self._Description = params.get("Description")
        self._IsGlobal = params.get("IsGlobal")
        if params.get("ModifiableInfo") is not None:
            self._ModifiableInfo = ModifiableInfo()
            self._ModifiableInfo._deserialize(params.get("ModifiableInfo"))
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        self._FuncPattern = params.get("FuncPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    """修改参数时，传入参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _CurrentValue: 当前值
        :type CurrentValue: str
        :param _OldValue: 原有值
        :type OldValue: str
        """
        self._ParamName = None
        self._CurrentValue = None
        self._OldValue = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._CurrentValue = params.get("CurrentValue")
        self._OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItemDetail(AbstractModel):
    """实例参数信息

    """

    def __init__(self):
        r"""
        :param _CurrentValue: 当前值
        :type CurrentValue: str
        :param _Default: 默认值
        :type Default: str
        :param _EnumValue: 参数的可选枚举值。如果为非枚举值，则为空
        :type EnumValue: list of str
        :param _IsGlobal: 1：全局参数，0：非全局参数
        :type IsGlobal: int
        :param _Max: 最大值
        :type Max: str
        :param _Min: 最小值
        :type Min: str
        :param _NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。0-不需要重启，1-需要重启。
        :type NeedReboot: int
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _ParamType: 参数类型：integer，enum，float，string，func
        :type ParamType: str
        :param _Description: 参数描述
        :type Description: str
        :param _IsFunc: 类型是否为公式
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFunc: bool
        :param _Func: 参数配置公式
注意：此字段可能返回 null，表示取不到有效值。
        :type Func: str
        :param _FuncPattern: 支持公式的参数的默认公式样式
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncPattern: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._IsGlobal = None
        self._Max = None
        self._Min = None
        self._NeedReboot = None
        self._ParamName = None
        self._ParamType = None
        self._Description = None
        self._IsFunc = None
        self._Func = None
        self._FuncPattern = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsFunc(self):
        return self._IsFunc

    @IsFunc.setter
    def IsFunc(self, IsFunc):
        self._IsFunc = IsFunc

    @property
    def Func(self):
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func

    @property
    def FuncPattern(self):
        return self._FuncPattern

    @FuncPattern.setter
    def FuncPattern(self, FuncPattern):
        self._FuncPattern = FuncPattern


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._IsGlobal = params.get("IsGlobal")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._NeedReboot = params.get("NeedReboot")
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        self._Description = params.get("Description")
        self._IsFunc = params.get("IsFunc")
        self._Func = params.get("Func")
        self._FuncPattern = params.get("FuncPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItemInfo(AbstractModel):
    """参数变化信息

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamName: str
        :param _NewValue: 参数新值

注意：此字段可能返回 null，表示取不到有效值。
        :type NewValue: str
        :param _OldValue: 参数旧值

注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        :param _ValueFunction: 参数公式

注意：此字段可能返回 null，表示取不到有效值。
        :type ValueFunction: str
        """
        self._ParamName = None
        self._NewValue = None
        self._OldValue = None
        self._ValueFunction = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def ValueFunction(self):
        return self._ValueFunction

    @ValueFunction.setter
    def ValueFunction(self, ValueFunction):
        self._ValueFunction = ValueFunction


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._NewValue = params.get("NewValue")
        self._OldValue = params.get("OldValue")
        self._ValueFunction = params.get("ValueFunction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateListInfo(AbstractModel):
    """参数模板信息

    """

    def __init__(self):
        r"""
        :param _Id: 参数模板ID
        :type Id: int
        :param _TemplateName: 参数模板名称
        :type TemplateName: str
        :param _TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        :param _EngineVersion: 引擎版本
        :type EngineVersion: str
        :param _DbMode: 数据库类型，可选值：NORMAL，SERVERLESS
        :type DbMode: str
        :param _ParamInfoSet: 参数模板详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of TemplateParamInfo
        """
        self._Id = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._EngineVersion = None
        self._DbMode = None
        self._ParamInfoSet = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def ParamInfoSet(self):
        return self._ParamInfoSet

    @ParamInfoSet.setter
    def ParamInfoSet(self, ParamInfoSet):
        self._ParamInfoSet = ParamInfoSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        self._EngineVersion = params.get("EngineVersion")
        self._DbMode = params.get("DbMode")
        if params.get("ParamInfoSet") is not None:
            self._ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = TemplateParamInfo()
                obj._deserialize(item)
                self._ParamInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessRequest(AbstractModel):
    """PauseServerless请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ForcePause: 是否强制暂停，忽略当前的用户链接  0:不强制  1:强制， 默认为1
        :type ForcePause: int
        """
        self._ClusterId = None
        self._ForcePause = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ForcePause(self):
        return self._ForcePause

    @ForcePause.setter
    def ForcePause(self, ForcePause):
        self._ForcePause = ForcePause


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ForcePause = params.get("ForcePause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessResponse(AbstractModel):
    """PauseServerless返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: 端口
        :type PortRange: str
        :param _IpProtocol: 网络协议，支持udp、tcp等
        :type IpProtocol: str
        :param _ServiceModule: 协议端口ID或者协议端口组ID。
        :type ServiceModule: str
        :param _AddressModule: IP地址ID或者ID地址组ID。
        :type AddressModule: str
        :param _Id: id
        :type Id: str
        :param _Desc: 描述
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._ServiceModule = None
        self._AddressModule = None
        self._Id = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._ServiceModule = params.get("ServiceModule")
        self._AddressModule = params.get("AddressModule")
        self._Id = params.get("Id")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyConnectionPoolInfo(AbstractModel):
    """数据库代理连接池信息

    """

    def __init__(self):
        r"""
        :param _ConnectionPoolTimeOut: 连接池保持阈值：单位（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolTimeOut: int
        :param _OpenConnectionPool: 是否开启了连接池
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenConnectionPool: str
        :param _ConnectionPoolType: 连接池类型：SessionConnectionPool（会话级别连接池）
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolType: str
        """
        self._ConnectionPoolTimeOut = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None

    @property
    def ConnectionPoolTimeOut(self):
        return self._ConnectionPoolTimeOut

    @ConnectionPoolTimeOut.setter
    def ConnectionPoolTimeOut(self, ConnectionPoolTimeOut):
        self._ConnectionPoolTimeOut = ConnectionPoolTimeOut

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType


    def _deserialize(self, params):
        self._ConnectionPoolTimeOut = params.get("ConnectionPoolTimeOut")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroup(AbstractModel):
    """proxy组

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _ProxyNodeCount: 数据库代理组节点个数
        :type ProxyNodeCount: int
        :param _Status: 数据库代理组状态
        :type Status: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _CurrentProxyVersion: 当前代理版本
        :type CurrentProxyVersion: str
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _OpenRw: 读写节点开通数据库代理
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenRw: str
        """
        self._ProxyGroupId = None
        self._ProxyNodeCount = None
        self._Status = None
        self._Region = None
        self._Zone = None
        self._CurrentProxyVersion = None
        self._ClusterId = None
        self._AppId = None
        self._OpenRw = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyNodeCount(self):
        return self._ProxyNodeCount

    @ProxyNodeCount.setter
    def ProxyNodeCount(self, ProxyNodeCount):
        self._ProxyNodeCount = ProxyNodeCount

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
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyNodeCount = params.get("ProxyNodeCount")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._ClusterId = params.get("ClusterId")
        self._AppId = params.get("AppId")
        self._OpenRw = params.get("OpenRw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """数据库代理组详细信息

    """

    def __init__(self):
        r"""
        :param _ProxyGroup: 数据库代理组
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroup: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroup`
        :param _ProxyGroupRwInfo: 数据库代理组读写分离信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroupRwInfo: :class:`tencentcloud.cynosdb.v20190107.models.ProxyGroupRwInfo`
        :param _ProxyNodes: 数据库代理节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodes: list of ProxyNodeInfo
        :param _ConnectionPool: 数据库代理连接池信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPool: :class:`tencentcloud.cynosdb.v20190107.models.ProxyConnectionPoolInfo`
        :param _NetAddrInfos: 数据库代理网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NetAddrInfos: list of NetAddr
        :param _Tasks: 数据库代理任务集
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        """
        self._ProxyGroup = None
        self._ProxyGroupRwInfo = None
        self._ProxyNodes = None
        self._ConnectionPool = None
        self._NetAddrInfos = None
        self._Tasks = None

    @property
    def ProxyGroup(self):
        return self._ProxyGroup

    @ProxyGroup.setter
    def ProxyGroup(self, ProxyGroup):
        self._ProxyGroup = ProxyGroup

    @property
    def ProxyGroupRwInfo(self):
        return self._ProxyGroupRwInfo

    @ProxyGroupRwInfo.setter
    def ProxyGroupRwInfo(self, ProxyGroupRwInfo):
        self._ProxyGroupRwInfo = ProxyGroupRwInfo

    @property
    def ProxyNodes(self):
        return self._ProxyNodes

    @ProxyNodes.setter
    def ProxyNodes(self, ProxyNodes):
        self._ProxyNodes = ProxyNodes

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def NetAddrInfos(self):
        return self._NetAddrInfos

    @NetAddrInfos.setter
    def NetAddrInfos(self, NetAddrInfos):
        self._NetAddrInfos = NetAddrInfos

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks


    def _deserialize(self, params):
        if params.get("ProxyGroup") is not None:
            self._ProxyGroup = ProxyGroup()
            self._ProxyGroup._deserialize(params.get("ProxyGroup"))
        if params.get("ProxyGroupRwInfo") is not None:
            self._ProxyGroupRwInfo = ProxyGroupRwInfo()
            self._ProxyGroupRwInfo._deserialize(params.get("ProxyGroupRwInfo"))
        if params.get("ProxyNodes") is not None:
            self._ProxyNodes = []
            for item in params.get("ProxyNodes"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNodes.append(obj)
        if params.get("ConnectionPool") is not None:
            self._ConnectionPool = ProxyConnectionPoolInfo()
            self._ConnectionPool._deserialize(params.get("ConnectionPool"))
        if params.get("NetAddrInfos") is not None:
            self._NetAddrInfos = []
            for item in params.get("NetAddrInfos"):
                obj = NetAddr()
                obj._deserialize(item)
                self._NetAddrInfos.append(obj)
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupRwInfo(AbstractModel):
    """数据库代理组读写分离信息

    """

    def __init__(self):
        r"""
        :param _ConsistencyType: 一致性类型 eventual-最终一致性,global-全局一致性,session-会话一致性
        :type ConsistencyType: str
        :param _ConsistencyTimeOut: 一致性超时时间
        :type ConsistencyTimeOut: int
        :param _WeightMode: 权重模式 system-系统分配，custom-自定义
        :type WeightMode: str
        :param _FailOver: 是否开启故障转移
        :type FailOver: str
        :param _AutoAddRo: 是否自动添加只读实例，yes-是，no-不自动添加
        :type AutoAddRo: str
        :param _InstanceWeights: 实例权重数组
        :type InstanceWeights: list of ProxyInstanceWeight
        :param _OpenRw: 是否开通读写节点，yse-是，no-否
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenRw: str
        :param _RwType: 读写属性，可选值：READWRITE,READONLY
        :type RwType: str
        :param _TransSplit: 事务拆分
        :type TransSplit: bool
        :param _AccessMode: 连接模式，可选值：balance，nearby
        :type AccessMode: str
        """
        self._ConsistencyType = None
        self._ConsistencyTimeOut = None
        self._WeightMode = None
        self._FailOver = None
        self._AutoAddRo = None
        self._InstanceWeights = None
        self._OpenRw = None
        self._RwType = None
        self._TransSplit = None
        self._AccessMode = None

    @property
    def ConsistencyType(self):
        return self._ConsistencyType

    @ConsistencyType.setter
    def ConsistencyType(self, ConsistencyType):
        self._ConsistencyType = ConsistencyType

    @property
    def ConsistencyTimeOut(self):
        return self._ConsistencyTimeOut

    @ConsistencyTimeOut.setter
    def ConsistencyTimeOut(self, ConsistencyTimeOut):
        self._ConsistencyTimeOut = ConsistencyTimeOut

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def InstanceWeights(self):
        return self._InstanceWeights

    @InstanceWeights.setter
    def InstanceWeights(self, InstanceWeights):
        self._InstanceWeights = InstanceWeights

    @property
    def OpenRw(self):
        return self._OpenRw

    @OpenRw.setter
    def OpenRw(self, OpenRw):
        self._OpenRw = OpenRw

    @property
    def RwType(self):
        return self._RwType

    @RwType.setter
    def RwType(self, RwType):
        self._RwType = RwType

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode


    def _deserialize(self, params):
        self._ConsistencyType = params.get("ConsistencyType")
        self._ConsistencyTimeOut = params.get("ConsistencyTimeOut")
        self._WeightMode = params.get("WeightMode")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        if params.get("InstanceWeights") is not None:
            self._InstanceWeights = []
            for item in params.get("InstanceWeights"):
                obj = ProxyInstanceWeight()
                obj._deserialize(item)
                self._InstanceWeights.append(obj)
        self._OpenRw = params.get("OpenRw")
        self._RwType = params.get("RwType")
        self._TransSplit = params.get("TransSplit")
        self._AccessMode = params.get("AccessMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInstanceWeight(AbstractModel):
    """数据库代理，读写分离实例权重

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Weight: 实例权重
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """数据库代理组节点

    """

    def __init__(self):
        r"""
        :param _ProxyNodeId: 数据库代理节点ID
        :type ProxyNodeId: str
        :param _ProxyNodeConnections: 节点当前连接数, DescribeProxyNodes接口此字段值不返回
        :type ProxyNodeConnections: int
        :param _Cpu: 数据库代理节点cpu
        :type Cpu: int
        :param _Mem: 数据库代理节点内存
        :type Mem: int
        :param _Status: 数据库代理节点状态
        :type Status: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _AppId: 用户AppID
        :type AppId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _OssProxyNodeName: 数据库代理节点名字
        :type OssProxyNodeName: str
        """
        self._ProxyNodeId = None
        self._ProxyNodeConnections = None
        self._Cpu = None
        self._Mem = None
        self._Status = None
        self._ProxyGroupId = None
        self._ClusterId = None
        self._AppId = None
        self._Region = None
        self._Zone = None
        self._OssProxyNodeName = None

    @property
    def ProxyNodeId(self):
        return self._ProxyNodeId

    @ProxyNodeId.setter
    def ProxyNodeId(self, ProxyNodeId):
        self._ProxyNodeId = ProxyNodeId

    @property
    def ProxyNodeConnections(self):
        return self._ProxyNodeConnections

    @ProxyNodeConnections.setter
    def ProxyNodeConnections(self, ProxyNodeConnections):
        self._ProxyNodeConnections = ProxyNodeConnections

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
    def OssProxyNodeName(self):
        return self._OssProxyNodeName

    @OssProxyNodeName.setter
    def OssProxyNodeName(self, OssProxyNodeName):
        self._OssProxyNodeName = OssProxyNodeName


    def _deserialize(self, params):
        self._ProxyNodeId = params.get("ProxyNodeId")
        self._ProxyNodeConnections = params.get("ProxyNodeConnections")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Status = params.get("Status")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ClusterId = params.get("ClusterId")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._OssProxyNodeName = params.get("OssProxyNodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxySpec(AbstractModel):
    """数据库代理规格

    """

    def __init__(self):
        r"""
        :param _Cpu: 数据库代理cpu核数
        :type Cpu: int
        :param _Mem: 数据库代理内存
        :type Mem: int
        """
        self._Cpu = None
        self._Mem = None

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


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyVersionInfo(AbstractModel):
    """TDSQL-C MySQL支持的proxy版本信息

    """

    def __init__(self):
        r"""
        :param _ProxyVersion: proxy版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyVersion: str
        :param _ProxyVersionType: 版本描述：GA:稳定版  BETA:尝鲜版，DEPRECATED:过旧，
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyVersionType: str
        """
        self._ProxyVersion = None
        self._ProxyVersionType = None

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def ProxyVersionType(self):
        return self._ProxyVersionType

    @ProxyVersionType.setter
    def ProxyVersionType(self, ProxyVersionType):
        self._ProxyVersionType = ProxyVersionType


    def _deserialize(self, params):
        self._ProxyVersion = params.get("ProxyVersion")
        self._ProxyVersionType = params.get("ProxyVersionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyZone(AbstractModel):
    """proxy节点可用区内个数

    """

    def __init__(self):
        r"""
        :param _ProxyNodeZone: proxy节点可用区
        :type ProxyNodeZone: str
        :param _ProxyNodeCount: proxy节点数量
        :type ProxyNodeCount: int
        """
        self._ProxyNodeZone = None
        self._ProxyNodeCount = None

    @property
    def ProxyNodeZone(self):
        return self._ProxyNodeZone

    @ProxyNodeZone.setter
    def ProxyNodeZone(self, ProxyNodeZone):
        self._ProxyNodeZone = ProxyNodeZone

    @property
    def ProxyNodeCount(self):
        return self._ProxyNodeCount

    @ProxyNodeCount.setter
    def ProxyNodeCount(self, ProxyNodeCount):
        self._ProxyNodeCount = ProxyNodeCount


    def _deserialize(self, params):
        self._ProxyNodeZone = params.get("ProxyNodeZone")
        self._ProxyNodeCount = params.get("ProxyNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Names: 搜索字段，目前支持："InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param _Values: 搜索字符串
        :type Values: list of str
        :param _ExactMatch: 是否精确匹配
        :type ExactMatch: bool
        :param _Name: 搜索字段
        :type Name: str
        :param _Operator: 操作符
        :type Operator: str
        """
        self._Names = None
        self._Values = None
        self._ExactMatch = None
        self._Name = None
        self._Operator = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryParamFilter(AbstractModel):
    """查询参数过滤器

    """

    def __init__(self):
        r"""
        :param _Names: 搜索字段，目前支持："InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param _Values: 搜索字符串
        :type Values: list of str
        :param _ExactMatch: 是否精确匹配
        :type ExactMatch: bool
        """
        self._Names = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResourcePackageRequest(AbstractModel):
    """RefundResourcePackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包唯一ID
        :type PackageId: str
        """
        self._PackageId = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResourcePackageResponse(AbstractModel):
    """RefundResourcePackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNames: 每个物品对应一个dealName，业务需要根据dealName保证发货接口幂等
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNames = None
        self._RequestId = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class ReloadBalanceProxyNodeRequest(AbstractModel):
    """ReloadBalanceProxyNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeResponse(AbstractModel):
    """ReloadBalanceProxyNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RemoveClusterSlaveZoneRequest(AbstractModel):
    """RemoveClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _SlaveZone: 从可用区
        :type SlaveZone: str
        """
        self._ClusterId = None
        self._SlaveZone = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneResponse(AbstractModel):
    """RemoveClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步FlowId
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RenewClustersRequest(AbstractModel):
    """RenewClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _TimeSpan: 续费时长
        :type TimeSpan: float
        :param _TimeUnit: 时间单位 y,m,d,h,i,s
        :type TimeUnit: str
        :param _DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        """
        self._ClusterId = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._DealMode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._DealMode = params.get("DealMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewClustersResponse(AbstractModel):
    """RenewClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealIds: 预付费总订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _DealNames: 退款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _TranId: 冻结流水，一次开通一个冻结流水
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _ResourceIds: 每个订单号对应的发货资源id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param _ClusterIds: 集群id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigDealIds = None
        self._DealNames = None
        self._TranId = None
        self._ResourceIds = None
        self._ClusterIds = None
        self._RequestId = None

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._TranId = params.get("TranId")
        self._ResourceIds = params.get("ResourceIds")
        self._ClusterIds = params.get("ClusterIds")
        self._RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountName: 数据库账号名
        :type AccountName: str
        :param _AccountPassword: 数据库账号新密码
        :type AccountPassword: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Host: 主机，不填默认为"%"
        :type Host: str
        """
        self._AccountName = None
        self._AccountPassword = None
        self._ClusterId = None
        self._Host = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._ClusterId = params.get("ClusterId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

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


class ResourcePackage(AbstractModel):
    """资源包信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 资源包的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _PackageType: 资源包类型：CCU：计算资源包
DISK：存储资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _DeductionPriority: 当前资源包绑定在当前实例下的抵扣优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductionPriority: int
        """
        self._PackageId = None
        self._PackageType = None
        self._DeductionPriority = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def DeductionPriority(self):
        return self._DeductionPriority

    @DeductionPriority.setter
    def DeductionPriority(self, DeductionPriority):
        self._DeductionPriority = DeductionPriority


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._PackageType = params.get("PackageType")
        self._DeductionPriority = params.get("DeductionPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
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
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResumeServerlessRequest(AbstractModel):
    """ResumeServerless请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeServerlessResponse(AbstractModel):
    """ResumeServerless返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RevokeAccountPrivilegesRequest(AbstractModel):
    """RevokeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param _DbTablePrivileges: 数据库表权限数组
        :type DbTablePrivileges: list of str
        :param _DbTables: 数据库表信息
        :type DbTables: list of DbTable
        """
        self._ClusterId = None
        self._Account = None
        self._DbTablePrivileges = None
        self._DbTables = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DbTablePrivileges(self):
        return self._DbTablePrivileges

    @DbTablePrivileges.setter
    def DbTablePrivileges(self, DbTablePrivileges):
        self._DbTablePrivileges = DbTablePrivileges

    @property
    def DbTables(self):
        return self._DbTables

    @DbTables.setter
    def DbTables(self, DbTables):
        self._DbTables = DbTables


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self._Account = InputAccount()
            self._Account._deserialize(params.get("Account"))
        self._DbTablePrivileges = params.get("DbTablePrivileges")
        if params.get("DbTables") is not None:
            self._DbTables = []
            for item in params.get("DbTables"):
                obj = DbTable()
                obj._deserialize(item)
                self._DbTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeAccountPrivilegesResponse(AbstractModel):
    """RevokeAccountPrivileges返回参数结构体

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


class RollBackClusterRequest(AbstractModel):
    """RollBackCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RollbackStrategy: 回档策略 timeRollback-按时间点回档 snapRollback-按备份文件回档
        :type RollbackStrategy: str
        :param _RollbackId: 备份文件ID。
回档策略为按备份文件回档时必填。
        :type RollbackId: int
        :param _ExpectTime: 期望回档时间。
回档策略为timeRollback按时间点回档时必填。
        :type ExpectTime: str
        :param _ExpectTimeThresh: 期望阈值（已废弃）
        :type ExpectTimeThresh: int
        :param _RollbackDatabases: 回档数据库列表
        :type RollbackDatabases: list of RollbackDatabase
        :param _RollbackTables: 回档数据库表列表
        :type RollbackTables: list of RollbackTable
        :param _RollbackMode: 按时间点回档模式，full: 普通; db: 快速; table: 极速  （默认是普通）
        :type RollbackMode: str
        """
        self._ClusterId = None
        self._RollbackStrategy = None
        self._RollbackId = None
        self._ExpectTime = None
        self._ExpectTimeThresh = None
        self._RollbackDatabases = None
        self._RollbackTables = None
        self._RollbackMode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackId(self):
        return self._RollbackId

    @RollbackId.setter
    def RollbackId(self, RollbackId):
        self._RollbackId = RollbackId

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def ExpectTimeThresh(self):
        return self._ExpectTimeThresh

    @ExpectTimeThresh.setter
    def ExpectTimeThresh(self, ExpectTimeThresh):
        self._ExpectTimeThresh = ExpectTimeThresh

    @property
    def RollbackDatabases(self):
        return self._RollbackDatabases

    @RollbackDatabases.setter
    def RollbackDatabases(self, RollbackDatabases):
        self._RollbackDatabases = RollbackDatabases

    @property
    def RollbackTables(self):
        return self._RollbackTables

    @RollbackTables.setter
    def RollbackTables(self, RollbackTables):
        self._RollbackTables = RollbackTables

    @property
    def RollbackMode(self):
        return self._RollbackMode

    @RollbackMode.setter
    def RollbackMode(self, RollbackMode):
        self._RollbackMode = RollbackMode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._RollbackId = params.get("RollbackId")
        self._ExpectTime = params.get("ExpectTime")
        self._ExpectTimeThresh = params.get("ExpectTimeThresh")
        if params.get("RollbackDatabases") is not None:
            self._RollbackDatabases = []
            for item in params.get("RollbackDatabases"):
                obj = RollbackDatabase()
                obj._deserialize(item)
                self._RollbackDatabases.append(obj)
        if params.get("RollbackTables") is not None:
            self._RollbackTables = []
            for item in params.get("RollbackTables"):
                obj = RollbackTable()
                obj._deserialize(item)
                self._RollbackTables.append(obj)
        self._RollbackMode = params.get("RollbackMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollBackClusterResponse(AbstractModel):
    """RollBackCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 任务流ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class RollbackData(AbstractModel):
    """回档任务信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 实例CPU
        :type Cpu: int
        :param _Memory: 实例内存
        :type Memory: int
        :param _StorageLimit: 集群存储上限
        :type StorageLimit: int
        :param _OriginalClusterId: 原集群id
        :type OriginalClusterId: str
        :param _OriginalClusterName: 原集群名
        :type OriginalClusterName: str
        :param _RollbackStrategy: 回档方式
        :type RollbackStrategy: str
        :param _SnapshotTime: 快照时间
        :type SnapshotTime: str
        :param _MinCpu: 回档到serverlessls集群时最小CPU
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCpu: int
        :param _MaxCpu: 回档到serverlessls集群时最大CPU
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCpu: int
        :param _SnapShotId: 快照ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapShotId: int
        :param _RollbackDatabases: 回档数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackDatabases: list of RollbackDatabase
        :param _RollbackTables: 回档数据表
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackTables: list of RollbackTable
        :param _BackupFileName: 备份文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupFileName: str
        :param _RollbackProcess: 回档进程
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackProcess: :class:`tencentcloud.cynosdb.v20190107.models.RollbackProcessInfo`
        """
        self._Cpu = None
        self._Memory = None
        self._StorageLimit = None
        self._OriginalClusterId = None
        self._OriginalClusterName = None
        self._RollbackStrategy = None
        self._SnapshotTime = None
        self._MinCpu = None
        self._MaxCpu = None
        self._SnapShotId = None
        self._RollbackDatabases = None
        self._RollbackTables = None
        self._BackupFileName = None
        self._RollbackProcess = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def OriginalClusterId(self):
        return self._OriginalClusterId

    @OriginalClusterId.setter
    def OriginalClusterId(self, OriginalClusterId):
        self._OriginalClusterId = OriginalClusterId

    @property
    def OriginalClusterName(self):
        return self._OriginalClusterName

    @OriginalClusterName.setter
    def OriginalClusterName(self, OriginalClusterName):
        self._OriginalClusterName = OriginalClusterName

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def SnapshotTime(self):
        return self._SnapshotTime

    @SnapshotTime.setter
    def SnapshotTime(self, SnapshotTime):
        self._SnapshotTime = SnapshotTime

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def SnapShotId(self):
        return self._SnapShotId

    @SnapShotId.setter
    def SnapShotId(self, SnapShotId):
        self._SnapShotId = SnapShotId

    @property
    def RollbackDatabases(self):
        return self._RollbackDatabases

    @RollbackDatabases.setter
    def RollbackDatabases(self, RollbackDatabases):
        self._RollbackDatabases = RollbackDatabases

    @property
    def RollbackTables(self):
        return self._RollbackTables

    @RollbackTables.setter
    def RollbackTables(self, RollbackTables):
        self._RollbackTables = RollbackTables

    @property
    def BackupFileName(self):
        return self._BackupFileName

    @BackupFileName.setter
    def BackupFileName(self, BackupFileName):
        self._BackupFileName = BackupFileName

    @property
    def RollbackProcess(self):
        return self._RollbackProcess

    @RollbackProcess.setter
    def RollbackProcess(self, RollbackProcess):
        self._RollbackProcess = RollbackProcess


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._StorageLimit = params.get("StorageLimit")
        self._OriginalClusterId = params.get("OriginalClusterId")
        self._OriginalClusterName = params.get("OriginalClusterName")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._SnapshotTime = params.get("SnapshotTime")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._SnapShotId = params.get("SnapShotId")
        if params.get("RollbackDatabases") is not None:
            self._RollbackDatabases = []
            for item in params.get("RollbackDatabases"):
                obj = RollbackDatabase()
                obj._deserialize(item)
                self._RollbackDatabases.append(obj)
        if params.get("RollbackTables") is not None:
            self._RollbackTables = []
            for item in params.get("RollbackTables"):
                obj = RollbackTable()
                obj._deserialize(item)
                self._RollbackTables.append(obj)
        self._BackupFileName = params.get("BackupFileName")
        if params.get("RollbackProcess") is not None:
            self._RollbackProcess = RollbackProcessInfo()
            self._RollbackProcess._deserialize(params.get("RollbackProcess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDatabase(AbstractModel):
    """回滚数据库信息

    """

    def __init__(self):
        r"""
        :param _OldDatabase: 旧数据库名称
        :type OldDatabase: str
        :param _NewDatabase: 新数据库名称
        :type NewDatabase: str
        """
        self._OldDatabase = None
        self._NewDatabase = None

    @property
    def OldDatabase(self):
        return self._OldDatabase

    @OldDatabase.setter
    def OldDatabase(self, OldDatabase):
        self._OldDatabase = OldDatabase

    @property
    def NewDatabase(self):
        return self._NewDatabase

    @NewDatabase.setter
    def NewDatabase(self, NewDatabase):
        self._NewDatabase = NewDatabase


    def _deserialize(self, params):
        self._OldDatabase = params.get("OldDatabase")
        self._NewDatabase = params.get("NewDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceInfo(AbstractModel):
    """回档实例信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _UniqVpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _Vip: vip信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: vport信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Cpu: cpu大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Mem: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param _StorageLimit: 存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._Vport = None
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._Cpu = None
        self._Mem = None
        self._StorageLimit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._StorageLimit = params.get("StorageLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackProcessInfo(AbstractModel):
    """回档进度详情

    """

    def __init__(self):
        r"""
        :param _IsVipSwitchable: 是否可以交换vip
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVipSwitchable: bool
        :param _VipSwitchableTime: vip可交换时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VipSwitchableTime: str
        :param _ExchangeInstanceInfoList: 交换实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExchangeInstanceInfoList: list of ExchangeInstanceInfo
        :param _ExchangeRoGroupInfoList: 交换RO组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExchangeRoGroupInfoList: list of ExchangeRoGroupInfo
        :param _CurrentStep: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStep: str
        :param _CurrentStepProgress: 当前步骤进度
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStepProgress: int
        :param _CurrentStepRemainingTime: 当前步骤剩余时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStepRemainingTime: str
        """
        self._IsVipSwitchable = None
        self._VipSwitchableTime = None
        self._ExchangeInstanceInfoList = None
        self._ExchangeRoGroupInfoList = None
        self._CurrentStep = None
        self._CurrentStepProgress = None
        self._CurrentStepRemainingTime = None

    @property
    def IsVipSwitchable(self):
        return self._IsVipSwitchable

    @IsVipSwitchable.setter
    def IsVipSwitchable(self, IsVipSwitchable):
        self._IsVipSwitchable = IsVipSwitchable

    @property
    def VipSwitchableTime(self):
        return self._VipSwitchableTime

    @VipSwitchableTime.setter
    def VipSwitchableTime(self, VipSwitchableTime):
        self._VipSwitchableTime = VipSwitchableTime

    @property
    def ExchangeInstanceInfoList(self):
        return self._ExchangeInstanceInfoList

    @ExchangeInstanceInfoList.setter
    def ExchangeInstanceInfoList(self, ExchangeInstanceInfoList):
        self._ExchangeInstanceInfoList = ExchangeInstanceInfoList

    @property
    def ExchangeRoGroupInfoList(self):
        return self._ExchangeRoGroupInfoList

    @ExchangeRoGroupInfoList.setter
    def ExchangeRoGroupInfoList(self, ExchangeRoGroupInfoList):
        self._ExchangeRoGroupInfoList = ExchangeRoGroupInfoList

    @property
    def CurrentStep(self):
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def CurrentStepProgress(self):
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def CurrentStepRemainingTime(self):
        return self._CurrentStepRemainingTime

    @CurrentStepRemainingTime.setter
    def CurrentStepRemainingTime(self, CurrentStepRemainingTime):
        self._CurrentStepRemainingTime = CurrentStepRemainingTime


    def _deserialize(self, params):
        self._IsVipSwitchable = params.get("IsVipSwitchable")
        self._VipSwitchableTime = params.get("VipSwitchableTime")
        if params.get("ExchangeInstanceInfoList") is not None:
            self._ExchangeInstanceInfoList = []
            for item in params.get("ExchangeInstanceInfoList"):
                obj = ExchangeInstanceInfo()
                obj._deserialize(item)
                self._ExchangeInstanceInfoList.append(obj)
        if params.get("ExchangeRoGroupInfoList") is not None:
            self._ExchangeRoGroupInfoList = []
            for item in params.get("ExchangeRoGroupInfoList"):
                obj = ExchangeRoGroupInfo()
                obj._deserialize(item)
                self._ExchangeRoGroupInfoList.append(obj)
        self._CurrentStep = params.get("CurrentStep")
        self._CurrentStepProgress = params.get("CurrentStepProgress")
        self._CurrentStepRemainingTime = params.get("CurrentStepRemainingTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackRoGroupInfo(AbstractModel):
    """回档RO组信息

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: 实例组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceGroupId: str
        :param _UniqVpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _Vip: vip信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: vport信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        """
        self._InstanceGroupId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._Vport = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTable(AbstractModel):
    """回档数据库及表

    """

    def __init__(self):
        r"""
        :param _Database: 数据库名称
        :type Database: str
        :param _Tables: 数据库表
        :type Tables: list of RollbackTableInfo
        """
        self._Database = None
        self._Tables = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._Database = params.get("Database")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = RollbackTableInfo()
                obj._deserialize(item)
                self._Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableInfo(AbstractModel):
    """回档表信息

    """

    def __init__(self):
        r"""
        :param _OldTable: 旧表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OldTable: str
        :param _NewTable: 新表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTable: str
        """
        self._OldTable = None
        self._NewTable = None

    @property
    def OldTable(self):
        return self._OldTable

    @OldTable.setter
    def OldTable(self, OldTable):
        self._OldTable = OldTable

    @property
    def NewTable(self):
        return self._NewTable

    @NewTable.setter
    def NewTable(self, NewTable):
        self._NewTable = NewTable


    def _deserialize(self, params):
        self._OldTable = params.get("OldTable")
        self._NewTable = params.get("NewTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """可回档的时间范围

    """

    def __init__(self):
        r"""
        :param _TimeRangeStart: 开始时间
        :type TimeRangeStart: str
        :param _TimeRangeEnd: 结束时间
        :type TimeRangeEnd: str
        """
        self._TimeRangeStart = None
        self._TimeRangeEnd = None

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd


    def _deserialize(self, params):
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackToNewClusterRequest(AbstractModel):
    """RollbackToNewCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _OriginalClusterId: 回档时，传入源集群ID，用于查找源poolId
        :type OriginalClusterId: str
        :param _UniqVpcId: 所属VPC网络ID
        :type UniqVpcId: str
        :param _UniqSubnetId: 所属子网ID
        :type UniqSubnetId: str
        :param _ClusterName: 集群名称，长度小于64个字符，每个字符取值范围：大/小写字母，数字，特殊符号（'-','_','.'）
        :type ClusterName: str
        :param _RollbackId: 快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效
        :type RollbackId: int
        :param _ExpectTime: 时间点回档，指定时间；快照回档，快照时间
        :type ExpectTime: str
        :param _AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param _ResourceTags: 集群创建需要绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param _DbMode: Db类型
当DbType为MYSQL时可选(默认NORMAL)：
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param _MinCpu: 当DbMode为SEVERLESS时必填
cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinCpu: float
        :param _MaxCpu: 当DbMode为SEVERLESS时必填：
cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxCpu: float
        :param _AutoPause: 当DbMode为SEVERLESS时，指定集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
默认值:yes
        :type AutoPause: str
        :param _AutoPauseDelay: 当DbMode为SEVERLESS时，指定集群自动暂停的延迟，单位秒，可选范围[600,691200]
默认值:600
        :type AutoPauseDelay: int
        :param _SecurityGroupIds: 安全组id数组
        :type SecurityGroupIds: list of str
        :param _AlarmPolicyIds: 告警策略Id数组
        :type AlarmPolicyIds: list of str
        :param _ClusterParams: 参数数组，暂时支持character_set_server （utf8｜latin1｜gbk｜utf8mb4） ，lower_case_table_names，1-大小写不敏感，0-大小写敏感
        :type ClusterParams: list of ParamItem
        :param _ParamTemplateId: 参数模板ID，可以通过查询参数模板信息DescribeParamTemplates获得参数模板ID
        :type ParamTemplateId: int
        :param _InstanceInitInfos: 实例初始化配置信息，主要用于购买集群时选不同规格实例
        :type InstanceInitInfos: list of InstanceInitInfo
        :param _DealMode: 0-下单并支付 1-下单
        :type DealMode: int
        :param _PayMode: 计算节点付费模式：0-按量计费，1-预付费
        :type PayMode: int
        :param _TimeSpan: 时间
        :type TimeSpan: int
        :param _TimeUnit: 单位
        :type TimeUnit: str
        :param _RollbackDatabases: 回档库信息
        :type RollbackDatabases: list of RollbackDatabase
        :param _RollbackTables: 回档表信息
        :type RollbackTables: list of RollbackTable
        :param _OriginalROInstanceList: 原ro实例信息
        :type OriginalROInstanceList: list of str
        """
        self._Zone = None
        self._OriginalClusterId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ClusterName = None
        self._RollbackId = None
        self._ExpectTime = None
        self._AutoVoucher = None
        self._ResourceTags = None
        self._DbMode = None
        self._MinCpu = None
        self._MaxCpu = None
        self._AutoPause = None
        self._AutoPauseDelay = None
        self._SecurityGroupIds = None
        self._AlarmPolicyIds = None
        self._ClusterParams = None
        self._ParamTemplateId = None
        self._InstanceInitInfos = None
        self._DealMode = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._RollbackDatabases = None
        self._RollbackTables = None
        self._OriginalROInstanceList = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OriginalClusterId(self):
        return self._OriginalClusterId

    @OriginalClusterId.setter
    def OriginalClusterId(self, OriginalClusterId):
        self._OriginalClusterId = OriginalClusterId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def RollbackId(self):
        return self._RollbackId

    @RollbackId.setter
    def RollbackId(self, RollbackId):
        self._RollbackId = RollbackId

    @property
    def ExpectTime(self):
        return self._ExpectTime

    @ExpectTime.setter
    def ExpectTime(self, ExpectTime):
        self._ExpectTime = ExpectTime

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DbMode(self):
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def MinCpu(self):
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def MaxCpu(self):
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def AutoPause(self):
        return self._AutoPause

    @AutoPause.setter
    def AutoPause(self, AutoPause):
        self._AutoPause = AutoPause

    @property
    def AutoPauseDelay(self):
        return self._AutoPauseDelay

    @AutoPauseDelay.setter
    def AutoPauseDelay(self, AutoPauseDelay):
        self._AutoPauseDelay = AutoPauseDelay

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AlarmPolicyIds(self):
        return self._AlarmPolicyIds

    @AlarmPolicyIds.setter
    def AlarmPolicyIds(self, AlarmPolicyIds):
        self._AlarmPolicyIds = AlarmPolicyIds

    @property
    def ClusterParams(self):
        return self._ClusterParams

    @ClusterParams.setter
    def ClusterParams(self, ClusterParams):
        self._ClusterParams = ClusterParams

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def InstanceInitInfos(self):
        return self._InstanceInitInfos

    @InstanceInitInfos.setter
    def InstanceInitInfos(self, InstanceInitInfos):
        self._InstanceInitInfos = InstanceInitInfos

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def RollbackDatabases(self):
        return self._RollbackDatabases

    @RollbackDatabases.setter
    def RollbackDatabases(self, RollbackDatabases):
        self._RollbackDatabases = RollbackDatabases

    @property
    def RollbackTables(self):
        return self._RollbackTables

    @RollbackTables.setter
    def RollbackTables(self, RollbackTables):
        self._RollbackTables = RollbackTables

    @property
    def OriginalROInstanceList(self):
        return self._OriginalROInstanceList

    @OriginalROInstanceList.setter
    def OriginalROInstanceList(self, OriginalROInstanceList):
        self._OriginalROInstanceList = OriginalROInstanceList


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._OriginalClusterId = params.get("OriginalClusterId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ClusterName = params.get("ClusterName")
        self._RollbackId = params.get("RollbackId")
        self._ExpectTime = params.get("ExpectTime")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DbMode = params.get("DbMode")
        self._MinCpu = params.get("MinCpu")
        self._MaxCpu = params.get("MaxCpu")
        self._AutoPause = params.get("AutoPause")
        self._AutoPauseDelay = params.get("AutoPauseDelay")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AlarmPolicyIds = params.get("AlarmPolicyIds")
        if params.get("ClusterParams") is not None:
            self._ClusterParams = []
            for item in params.get("ClusterParams"):
                obj = ParamItem()
                obj._deserialize(item)
                self._ClusterParams.append(obj)
        self._ParamTemplateId = params.get("ParamTemplateId")
        if params.get("InstanceInitInfos") is not None:
            self._InstanceInitInfos = []
            for item in params.get("InstanceInitInfos"):
                obj = InstanceInitInfo()
                obj._deserialize(item)
                self._InstanceInitInfos.append(obj)
        self._DealMode = params.get("DealMode")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        if params.get("RollbackDatabases") is not None:
            self._RollbackDatabases = []
            for item in params.get("RollbackDatabases"):
                obj = RollbackDatabase()
                obj._deserialize(item)
                self._RollbackDatabases.append(obj)
        if params.get("RollbackTables") is not None:
            self._RollbackTables = []
            for item in params.get("RollbackTables"):
                obj = RollbackTable()
                obj._deserialize(item)
                self._RollbackTables.append(obj)
        self._OriginalROInstanceList = params.get("OriginalROInstanceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackToNewClusterResponse(AbstractModel):
    """RollbackToNewCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _ResourceIds: 资源ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取资源ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param _ClusterIds: 集群ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取集群ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param _BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._DealNames = None
        self._ResourceIds = None
        self._ClusterIds = None
        self._BigDealIds = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._DealNames = params.get("DealNames")
        self._ResourceIds = params.get("ResourceIds")
        self._ClusterIds = params.get("ClusterIds")
        self._BigDealIds = params.get("BigDealIds")
        self._RequestId = params.get("RequestId")


class RuleFilters(AbstractModel):
    """审计规则的规则过滤条件

    """

    def __init__(self):
        r"""
        :param _Type: 审计规则过滤条件的参数名称。可选值：host – 客户端 IP；user – 数据库账户；dbName – 数据库名称；sqlType-SQL类型；sql-sql语句；affectRows -影响行数；sentRows-返回行数；checkRows-扫描行数；execTime-执行时间。
        :type Type: str
        :param _Compare: 审计规则过滤条件的匹配类型。可选值：INC – 包含；EXC – 不包含；EQS – 等于；NEQ – 不等于；REG-正则；GT-大于；LT-小于。
        :type Compare: str
        :param _Value: 审计规则过滤条件的匹配值。
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTemplateInfo(AbstractModel):
    """规则模板内容

    """

    def __init__(self):
        r"""
        :param _RuleTemplateId: 规则模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateId: str
        :param _RuleTemplateName: 规则模板名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateName: str
        :param _RuleFilters: 规则内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleFilters: list of RuleFilters
        :param _AlarmLevel: 告警等级。1-低风险，2-中风险，3-高风险。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmLevel: int
        :param _AlarmPolicy: 告警策略。0-不告警，1-告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmPolicy: int
        :param _Description: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._RuleTemplateId = None
        self._RuleTemplateName = None
        self._RuleFilters = None
        self._AlarmLevel = None
        self._AlarmPolicy = None
        self._Description = None

    @property
    def RuleTemplateId(self):
        return self._RuleTemplateId

    @RuleTemplateId.setter
    def RuleTemplateId(self, RuleTemplateId):
        self._RuleTemplateId = RuleTemplateId

    @property
    def RuleTemplateName(self):
        return self._RuleTemplateName

    @RuleTemplateName.setter
    def RuleTemplateName(self, RuleTemplateName):
        self._RuleTemplateName = RuleTemplateName

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmPolicy(self):
        return self._AlarmPolicy

    @AlarmPolicy.setter
    def AlarmPolicy(self, AlarmPolicy):
        self._AlarmPolicy = AlarmPolicy

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RuleTemplateId = params.get("RuleTemplateId")
        self._RuleTemplateName = params.get("RuleTemplateName")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmPolicy = params.get("AlarmPolicy")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SalePackageSpec(AbstractModel):
    """资源包明细说明

    """

    def __init__(self):
        r"""
        :param _PackageRegion: 资源包使用地域
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageRegion: str
        :param _PackageType: 资源包类型
CCU-计算资源包
DISK-存储资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _PackageVersion: 资源包版本
base-基础版本，common-通用版本，enterprise-企业版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param _MinPackageSpec: 当前版本资源包最小资源数，计算资源单位：个；存储资源：GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MinPackageSpec: float
        :param _MaxPackageSpec: 当前版本资源包最大资源数，计算资源单位：个；存储资源：GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPackageSpec: float
        :param _ExpireDay: 资源包有效期，单位:天
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireDay: int
        """
        self._PackageRegion = None
        self._PackageType = None
        self._PackageVersion = None
        self._MinPackageSpec = None
        self._MaxPackageSpec = None
        self._ExpireDay = None

    @property
    def PackageRegion(self):
        return self._PackageRegion

    @PackageRegion.setter
    def PackageRegion(self, PackageRegion):
        self._PackageRegion = PackageRegion

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def MinPackageSpec(self):
        return self._MinPackageSpec

    @MinPackageSpec.setter
    def MinPackageSpec(self, MinPackageSpec):
        self._MinPackageSpec = MinPackageSpec

    @property
    def MaxPackageSpec(self):
        return self._MaxPackageSpec

    @MaxPackageSpec.setter
    def MaxPackageSpec(self, MaxPackageSpec):
        self._MaxPackageSpec = MaxPackageSpec

    @property
    def ExpireDay(self):
        return self._ExpireDay

    @ExpireDay.setter
    def ExpireDay(self, ExpireDay):
        self._ExpireDay = ExpireDay


    def _deserialize(self, params):
        self._PackageRegion = params.get("PackageRegion")
        self._PackageType = params.get("PackageType")
        self._PackageVersion = params.get("PackageVersion")
        self._MinPackageSpec = params.get("MinPackageSpec")
        self._MaxPackageSpec = params.get("MaxPackageSpec")
        self._ExpireDay = params.get("ExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleRegion(AbstractModel):
    """售卖地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域英文名
        :type Region: str
        :param _RegionId: 地域数字ID
        :type RegionId: int
        :param _RegionZh: 地域中文名
        :type RegionZh: str
        :param _ZoneSet: 可售卖可用区列表
        :type ZoneSet: list of SaleZone
        :param _DbType: 引擎类型
        :type DbType: str
        :param _Modules: 地域模块支持情况
        :type Modules: list of Module
        """
        self._Region = None
        self._RegionId = None
        self._RegionZh = None
        self._ZoneSet = None
        self._DbType = None
        self._Modules = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionZh(self):
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Modules(self):
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionZh = params.get("RegionZh")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = SaleZone()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._DbType = params.get("DbType")
        if params.get("Modules") is not None:
            self._Modules = []
            for item in params.get("Modules"):
                obj = Module()
                obj._deserialize(item)
                self._Modules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleZone(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区英文名
        :type Zone: str
        :param _ZoneId: 可用区数字ID
        :type ZoneId: int
        :param _ZoneZh: 可用区中文名
        :type ZoneZh: str
        :param _IsSupportServerless: 是否支持serverless集群<br>
0:不支持<br>
1:支持
        :type IsSupportServerless: int
        :param _IsSupportNormal: 是否支持普通集群<br>
0:不支持<br>
1:支持
        :type IsSupportNormal: int
        :param _PhysicalZone: 物理区
        :type PhysicalZone: str
        :param _HasPermission: 用户是否有可用区权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasPermission: bool
        :param _IsWholeRdmaZone: 是否为全链路RDMA可用区
        :type IsWholeRdmaZone: str
        :param _IsSupportCreateCluster: 当前可用区是否允许新购集群，1:允许，0:不允许
        :type IsSupportCreateCluster: int
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneZh = None
        self._IsSupportServerless = None
        self._IsSupportNormal = None
        self._PhysicalZone = None
        self._HasPermission = None
        self._IsWholeRdmaZone = None
        self._IsSupportCreateCluster = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneZh(self):
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def IsSupportServerless(self):
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless

    @property
    def IsSupportNormal(self):
        return self._IsSupportNormal

    @IsSupportNormal.setter
    def IsSupportNormal(self, IsSupportNormal):
        self._IsSupportNormal = IsSupportNormal

    @property
    def PhysicalZone(self):
        return self._PhysicalZone

    @PhysicalZone.setter
    def PhysicalZone(self, PhysicalZone):
        self._PhysicalZone = PhysicalZone

    @property
    def HasPermission(self):
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

    @property
    def IsWholeRdmaZone(self):
        return self._IsWholeRdmaZone

    @IsWholeRdmaZone.setter
    def IsWholeRdmaZone(self, IsWholeRdmaZone):
        self._IsWholeRdmaZone = IsWholeRdmaZone

    @property
    def IsSupportCreateCluster(self):
        return self._IsSupportCreateCluster

    @IsSupportCreateCluster.setter
    def IsSupportCreateCluster(self, IsSupportCreateCluster):
        self._IsSupportCreateCluster = IsSupportCreateCluster


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneZh = params.get("ZoneZh")
        self._IsSupportServerless = params.get("IsSupportServerless")
        self._IsSupportNormal = params.get("IsSupportNormal")
        self._PhysicalZone = params.get("PhysicalZone")
        self._HasPermission = params.get("HasPermission")
        self._IsWholeRdmaZone = params.get("IsWholeRdmaZone")
        self._IsSupportCreateCluster = params.get("IsSupportCreateCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesRequest(AbstractModel):
    """SearchClusterDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Database: 数据库名
        :type Database: str
        :param _MatchType: 是否精确搜索。
0: 模糊搜索 1:精确搜索 
默认为0
        :type MatchType: int
        """
        self._ClusterId = None
        self._Database = None
        self._MatchType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Database = params.get("Database")
        self._MatchType = params.get("MatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesResponse(AbstractModel):
    """SearchClusterDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Databases: 数据库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Databases = None
        self._RequestId = None

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Databases = params.get("Databases")
        self._RequestId = params.get("RequestId")


class SearchClusterTablesRequest(AbstractModel):
    """SearchClusterTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _Database: 数据库名
        :type Database: str
        :param _Table: 数据表名
        :type Table: str
        :param _TableType: 数据表类型：
view：只返回 view，
base_table： 只返回基本表，
all：返回 view 和表
        :type TableType: str
        """
        self._ClusterId = None
        self._Database = None
        self._Table = None
        self._TableType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def TableType(self):
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._TableType = params.get("TableType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterTablesResponse(AbstractModel):
    """SearchClusterTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tables: 数据表列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of DatabaseTables
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tables = None
        self._RequestId = None

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _Inbound: 入站规则
        :type Inbound: list of PolicyRule
        :param _Outbound: 出站规则
        :type Outbound: list of PolicyRule
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 需操作的集群ID
        :type ResourceIds: list of str
        :param _AutoRenewFlag: 自动续费标志位，续费标记 0:正常续费  1:自动续费 2:到期不续
        :type AutoRenewFlag: int
        """
        self._ResourceIds = None
        self._AutoRenewFlag = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 操作成功实例数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class SlaveZoneAttrItem(AbstractModel):
    """可用区属性项

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _BinlogSyncWay: binlog同步方式
注意：此字段可能返回 null，表示取不到有效值。
        :type BinlogSyncWay: str
        """
        self._Zone = None
        self._BinlogSyncWay = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def BinlogSyncWay(self):
        return self._BinlogSyncWay

    @BinlogSyncWay.setter
    def BinlogSyncWay(self, BinlogSyncWay):
        self._BinlogSyncWay = BinlogSyncWay


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._BinlogSyncWay = params.get("BinlogSyncWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveZoneStockInfo(AbstractModel):
    """备可用区库存信息

    """

    def __init__(self):
        r"""
        :param _SlaveZone: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZone: str
        :param _StockCount: 备可用区的库存数量	
注意：此字段可能返回 null，表示取不到有效值。
        :type StockCount: int
        :param _HasStock: 备可用区是否有库存	
注意：此字段可能返回 null，表示取不到有效值。
        :type HasStock: bool
        """
        self._SlaveZone = None
        self._StockCount = None
        self._HasStock = None

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def StockCount(self):
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def HasStock(self):
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock


    def _deserialize(self, params):
        self._SlaveZone = params.get("SlaveZone")
        self._StockCount = params.get("StockCount")
        self._HasStock = params.get("HasStock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowQueriesItem(AbstractModel):
    """实例慢查询信息

    """

    def __init__(self):
        r"""
        :param _Timestamp: 执行时间戳
        :type Timestamp: int
        :param _QueryTime: 执行时长，单位秒
        :type QueryTime: float
        :param _SqlText: sql语句
        :type SqlText: str
        :param _UserHost: 客户端host
        :type UserHost: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Database: 数据库名
        :type Database: str
        :param _LockTime: 锁时长，单位秒
        :type LockTime: float
        :param _RowsExamined: 扫描行数
        :type RowsExamined: int
        :param _RowsSent: 返回行数
        :type RowsSent: int
        :param _SqlTemplate: sql模板
        :type SqlTemplate: str
        :param _SqlMd5: sql语句md5
        :type SqlMd5: str
        :param _SyncReadCountRemote: 远程读取次数
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncReadCountRemote: int
        :param _SyncReadBytesRemote: 远程读取的字节数
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncReadBytesRemote: int
        :param _SyncReadTimeRemote: 远程读取所花费的时间（微秒）
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncReadTimeRemote: int
        :param _SyncWriteCountRemote: 远程写入次数
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncWriteCountRemote: int
        :param _SyncWriteBytesRemote: 远程写入的字节数。
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncWriteBytesRemote: int
        :param _SyncWriteTimeRemote: 远程写入所花费的时间（微秒）。
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncWriteTimeRemote: int
        :param _TrxCommitDelay: 事务提交延迟（微秒）
数据库内核版本大于3.1.12
注意：此字段可能返回 null，表示取不到有效值。
        :type TrxCommitDelay: int
        """
        self._Timestamp = None
        self._QueryTime = None
        self._SqlText = None
        self._UserHost = None
        self._UserName = None
        self._Database = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None
        self._SqlTemplate = None
        self._SqlMd5 = None
        self._SyncReadCountRemote = None
        self._SyncReadBytesRemote = None
        self._SyncReadTimeRemote = None
        self._SyncWriteCountRemote = None
        self._SyncWriteBytesRemote = None
        self._SyncWriteTimeRemote = None
        self._TrxCommitDelay = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlMd5(self):
        return self._SqlMd5

    @SqlMd5.setter
    def SqlMd5(self, SqlMd5):
        self._SqlMd5 = SqlMd5

    @property
    def SyncReadCountRemote(self):
        return self._SyncReadCountRemote

    @SyncReadCountRemote.setter
    def SyncReadCountRemote(self, SyncReadCountRemote):
        self._SyncReadCountRemote = SyncReadCountRemote

    @property
    def SyncReadBytesRemote(self):
        return self._SyncReadBytesRemote

    @SyncReadBytesRemote.setter
    def SyncReadBytesRemote(self, SyncReadBytesRemote):
        self._SyncReadBytesRemote = SyncReadBytesRemote

    @property
    def SyncReadTimeRemote(self):
        return self._SyncReadTimeRemote

    @SyncReadTimeRemote.setter
    def SyncReadTimeRemote(self, SyncReadTimeRemote):
        self._SyncReadTimeRemote = SyncReadTimeRemote

    @property
    def SyncWriteCountRemote(self):
        return self._SyncWriteCountRemote

    @SyncWriteCountRemote.setter
    def SyncWriteCountRemote(self, SyncWriteCountRemote):
        self._SyncWriteCountRemote = SyncWriteCountRemote

    @property
    def SyncWriteBytesRemote(self):
        return self._SyncWriteBytesRemote

    @SyncWriteBytesRemote.setter
    def SyncWriteBytesRemote(self, SyncWriteBytesRemote):
        self._SyncWriteBytesRemote = SyncWriteBytesRemote

    @property
    def SyncWriteTimeRemote(self):
        return self._SyncWriteTimeRemote

    @SyncWriteTimeRemote.setter
    def SyncWriteTimeRemote(self, SyncWriteTimeRemote):
        self._SyncWriteTimeRemote = SyncWriteTimeRemote

    @property
    def TrxCommitDelay(self):
        return self._TrxCommitDelay

    @TrxCommitDelay.setter
    def TrxCommitDelay(self, TrxCommitDelay):
        self._TrxCommitDelay = TrxCommitDelay


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._QueryTime = params.get("QueryTime")
        self._SqlText = params.get("SqlText")
        self._UserHost = params.get("UserHost")
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlMd5 = params.get("SqlMd5")
        self._SyncReadCountRemote = params.get("SyncReadCountRemote")
        self._SyncReadBytesRemote = params.get("SyncReadBytesRemote")
        self._SyncReadTimeRemote = params.get("SyncReadTimeRemote")
        self._SyncWriteCountRemote = params.get("SyncWriteCountRemote")
        self._SyncWriteBytesRemote = params.get("SyncWriteBytesRemote")
        self._SyncWriteTimeRemote = params.get("SyncWriteTimeRemote")
        self._TrxCommitDelay = params.get("TrxCommitDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCLSDeliveryRequest(AbstractModel):
    """StartCLSDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _CLSTopicIds: 开通的日志主题id
        :type CLSTopicIds: list of str
        :param _LogType: 日志类型
        :type LogType: str
        :param _IsInMaintainPeriod: 是否维护时间运行
        :type IsInMaintainPeriod: str
        """
        self._InstanceId = None
        self._CLSTopicIds = None
        self._LogType = None
        self._IsInMaintainPeriod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CLSTopicIds(self):
        return self._CLSTopicIds

    @CLSTopicIds.setter
    def CLSTopicIds(self, CLSTopicIds):
        self._CLSTopicIds = CLSTopicIds

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CLSTopicIds = params.get("CLSTopicIds")
        self._LogType = params.get("LogType")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCLSDeliveryResponse(AbstractModel):
    """StartCLSDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopCLSDeliveryRequest(AbstractModel):
    """StopCLSDelivery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _CLSTopicIds: 日志主题id
        :type CLSTopicIds: list of str
        :param _LogType: 日志类型
        :type LogType: str
        :param _IsInMaintainPeriod: 是否维护时间运行
        :type IsInMaintainPeriod: str
        """
        self._InstanceId = None
        self._CLSTopicIds = None
        self._LogType = None
        self._IsInMaintainPeriod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CLSTopicIds(self):
        return self._CLSTopicIds

    @CLSTopicIds.setter
    def CLSTopicIds(self, CLSTopicIds):
        self._CLSTopicIds = CLSTopicIds

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CLSTopicIds = params.get("CLSTopicIds")
        self._LogType = params.get("LogType")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCLSDeliveryResponse(AbstractModel):
    """StopCLSDelivery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务id

        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SwitchClusterLogBin(AbstractModel):
    """转换集群log bin开关

    """

    def __init__(self):
        r"""
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcRequest(AbstractModel):
    """SwitchClusterVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _UniqVpcId: 字符串vpc id
        :type UniqVpcId: str
        :param _UniqSubnetId: 字符串子网id
        :type UniqSubnetId: str
        :param _OldIpReserveHours: 旧地址回收时间
        :type OldIpReserveHours: int
        """
        self._ClusterId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldIpReserveHours = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcResponse(AbstractModel):
    """SwitchClusterVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务id。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SwitchClusterZoneRequest(AbstractModel):
    """SwitchClusterZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: str
        :param _OldZone: 当前可用区
        :type OldZone: str
        :param _NewZone: 要切换到的可用区
        :type NewZone: str
        :param _IsInMaintainPeriod: 维护期间执行-yes,立即执行-no
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._OldZone = None
        self._NewZone = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def OldZone(self):
        return self._OldZone

    @OldZone.setter
    def OldZone(self, OldZone):
        self._OldZone = OldZone

    @property
    def NewZone(self):
        return self._NewZone

    @NewZone.setter
    def NewZone(self, NewZone):
        self._NewZone = NewZone

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._OldZone = params.get("OldZone")
        self._NewZone = params.get("NewZone")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterZoneResponse(AbstractModel):
    """SwitchClusterZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步FlowId
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SwitchProxyVpcRequest(AbstractModel):
    """SwitchProxyVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _UniqVpcId: 字符串vpc id
        :type UniqVpcId: str
        :param _UniqSubnetId: 字符串子网id
        :type UniqSubnetId: str
        :param _OldIpReserveHours: 旧地址回收时间
        :type OldIpReserveHours: int
        :param _ProxyGroupId: 数据库代理组Id（该参数为必填项，可以通过DescribeProxies接口获得）
        :type ProxyGroupId: str
        """
        self._ClusterId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._OldIpReserveHours = None
        self._ProxyGroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def OldIpReserveHours(self):
        return self._OldIpReserveHours

    @OldIpReserveHours.setter
    def OldIpReserveHours(self, OldIpReserveHours):
        self._OldIpReserveHours = OldIpReserveHours

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._OldIpReserveHours = params.get("OldIpReserveHours")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyVpcResponse(AbstractModel):
    """SwitchProxyVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务id。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TablePrivileges(AbstractModel):
    """mysql表权限

    """

    def __init__(self):
        r"""
        :param _Db: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Db: str
        :param _TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _Privileges: 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Privileges: list of str
        """
        self._Db = None
        self._TableName = None
        self._Privileges = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._TableName = params.get("TableName")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """集群绑定的标签信息，包含标签键TagKey和标签值TagValue

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class TaskMaintainInfo(AbstractModel):
    """TaskMaintainInfo

    """

    def __init__(self):
        r"""
        :param _MaintainStartTime: 执行开始时间(距离0点的秒数)
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainStartTime: int
        :param _MaintainDuration: 持续的时间(单位：秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainDuration: int
        :param _MaintainWeekDays: 可以执行的时间，枚举值：["Mon","Tue","Wed","Thu","Fri", "Sat", "Sun"]
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainWeekDays: list of str
        """
        self._MaintainStartTime = None
        self._MaintainDuration = None
        self._MaintainWeekDays = None

    @property
    def MaintainStartTime(self):
        return self._MaintainStartTime

    @MaintainStartTime.setter
    def MaintainStartTime(self, MaintainStartTime):
        self._MaintainStartTime = MaintainStartTime

    @property
    def MaintainDuration(self):
        return self._MaintainDuration

    @MaintainDuration.setter
    def MaintainDuration(self, MaintainDuration):
        self._MaintainDuration = MaintainDuration

    @property
    def MaintainWeekDays(self):
        return self._MaintainWeekDays

    @MaintainWeekDays.setter
    def MaintainWeekDays(self, MaintainWeekDays):
        self._MaintainWeekDays = MaintainWeekDays


    def _deserialize(self, params):
        self._MaintainStartTime = params.get("MaintainStartTime")
        self._MaintainDuration = params.get("MaintainDuration")
        self._MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateParamInfo(AbstractModel):
    """参数模板详情

    """

    def __init__(self):
        r"""
        :param _CurrentValue: 当前值
        :type CurrentValue: str
        :param _Default: 默认值
        :type Default: str
        :param _EnumValue: 参数类型为enum时可选的值类型集合
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param _Max: 参数类型为float/integer时的最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        :param _Min: 参数类型为float/integer时的最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _NeedReboot: 是否需要重启
        :type NeedReboot: int
        :param _Description: 参数描述
        :type Description: str
        :param _ParamType: 参数类型，integer/float/string/enum
        :type ParamType: str
        """
        self._CurrentValue = None
        self._Default = None
        self._EnumValue = None
        self._Max = None
        self._Min = None
        self._ParamName = None
        self._NeedReboot = None
        self._Description = None
        self._ParamType = None

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._Default = params.get("Default")
        self._EnumValue = params.get("EnumValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._ParamName = params.get("ParamName")
        self._NeedReboot = params.get("NeedReboot")
        self._Description = params.get("Description")
        self._ParamType = params.get("ParamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradePrice(AbstractModel):
    """计费询价结果

    """

    def __init__(self):
        r"""
        :param _TotalPrice: 预付费模式下资源总价，不包含优惠，单位:分
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPrice: int
        :param _Discount: 总的折扣，100表示100%不打折
        :type Discount: float
        :param _TotalPriceDiscount: 预付费模式下的优惠后总价, 单位: 分,例如用户享有折扣 =TotalPrice × Discount
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPriceDiscount: int
        :param _UnitPrice: 后付费模式下的单位资源价格，不包含优惠，单位:分
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: int
        :param _UnitPriceDiscount: 优惠后后付费模式下的单位资源价格, 单位: 分,例如用户享有折扣=UnitPricet × Discount
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: int
        :param _ChargeUnit: 计费价格单位
        :type ChargeUnit: str
        """
        self._TotalPrice = None
        self._Discount = None
        self._TotalPriceDiscount = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._ChargeUnit = None

    @property
    def TotalPrice(self):
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def TotalPriceDiscount(self):
        return self._TotalPriceDiscount

    @TotalPriceDiscount.setter
    def TotalPriceDiscount(self, TotalPriceDiscount):
        self._TotalPriceDiscount = TotalPriceDiscount

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit


    def _deserialize(self, params):
        self._TotalPrice = params.get("TotalPrice")
        self._Discount = params.get("Discount")
        self._TotalPriceDiscount = params.get("TotalPriceDiscount")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindClusterResourcePackagesRequest(AbstractModel):
    """UnbindClusterResourcePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _PackageIds: 资源包唯一ID,如果不传，解绑该实例绑定的所有资源包
        :type PackageIds: list of str
        """
        self._ClusterId = None
        self._PackageIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PackageIds(self):
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._PackageIds = params.get("PackageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindClusterResourcePackagesResponse(AbstractModel):
    """UnbindClusterResourcePackages返回参数结构体

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


class UpgradeClusterVersionRequest(AbstractModel):
    """UpgradeClusterVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _CynosVersion: 内核版本
        :type CynosVersion: str
        :param _UpgradeType: 升级时间类型，可选：upgradeImmediate,upgradeInMaintain
        :type UpgradeType: str
        """
        self._ClusterId = None
        self._CynosVersion = None
        self._UpgradeType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CynosVersion(self):
        return self._CynosVersion

    @CynosVersion.setter
    def CynosVersion(self, CynosVersion):
        self._CynosVersion = CynosVersion

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._CynosVersion = params.get("CynosVersion")
        self._UpgradeType = params.get("UpgradeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterVersionResponse(AbstractModel):
    """UpgradeClusterVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步任务id
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Cpu: 数据库CPU
        :type Cpu: int
        :param _Memory: 数据库内存，单位GB
        :type Memory: int
        :param _UpgradeType: 升级类型：upgradeImmediate，upgradeInMaintain
        :type UpgradeType: str
        :param _DeviceType: 实例机器类型
        :type DeviceType: str
        :param _StorageLimit: 该参数已废弃
        :type StorageLimit: int
        :param _AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param _DbType: 该参数已废弃
        :type DbType: str
        :param _DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        :param _UpgradeMode: NormalUpgrade：普通变配，FastUpgrade：极速变配，若变配过程判断会造成闪断，变配流程会终止。
        :type UpgradeMode: str
        :param _UpgradeProxy: proxy同步升级
        :type UpgradeProxy: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxy`
        """
        self._InstanceId = None
        self._Cpu = None
        self._Memory = None
        self._UpgradeType = None
        self._DeviceType = None
        self._StorageLimit = None
        self._AutoVoucher = None
        self._DbType = None
        self._DealMode = None
        self._UpgradeMode = None
        self._UpgradeProxy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DealMode(self):
        return self._DealMode

    @DealMode.setter
    def DealMode(self, DealMode):
        self._DealMode = DealMode

    @property
    def UpgradeMode(self):
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def UpgradeProxy(self):
        return self._UpgradeProxy

    @UpgradeProxy.setter
    def UpgradeProxy(self, UpgradeProxy):
        self._UpgradeProxy = UpgradeProxy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._UpgradeType = params.get("UpgradeType")
        self._DeviceType = params.get("DeviceType")
        self._StorageLimit = params.get("StorageLimit")
        self._AutoVoucher = params.get("AutoVoucher")
        self._DbType = params.get("DbType")
        self._DealMode = params.get("DealMode")
        self._UpgradeMode = params.get("UpgradeMode")
        if params.get("UpgradeProxy") is not None:
            self._UpgradeProxy = UpgradeProxy()
            self._UpgradeProxy._deserialize(params.get("UpgradeProxy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param _DealNames: 订单号
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._BigDealIds = None
        self._DealNames = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def BigDealIds(self):
        return self._BigDealIds

    @BigDealIds.setter
    def BigDealIds(self, BigDealIds):
        self._BigDealIds = BigDealIds

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._BigDealIds = params.get("BigDealIds")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class UpgradeProxy(AbstractModel):
    """添加实例或者变配实例时同步升级proxy.

    """

    def __init__(self):
        r"""
        :param _Cpu: cpu
        :type Cpu: int
        :param _Mem: memory
        :type Mem: int
        :param _ProxyZones: 代理节点信息
        :type ProxyZones: list of ProxyZone
        :param _ReloadBalance: 重新负载均衡
        :type ReloadBalance: str
        """
        self._Cpu = None
        self._Mem = None
        self._ProxyZones = None
        self._ReloadBalance = None

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
    def ProxyZones(self):
        return self._ProxyZones

    @ProxyZones.setter
    def ProxyZones(self, ProxyZones):
        self._ProxyZones = ProxyZones

    @property
    def ReloadBalance(self):
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        if params.get("ProxyZones") is not None:
            self._ProxyZones = []
            for item in params.get("ProxyZones"):
                obj = ProxyZone()
                obj._deserialize(item)
                self._ProxyZones.append(obj)
        self._ReloadBalance = params.get("ReloadBalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyRequest(AbstractModel):
    """UpgradeProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Cpu: cpu核数
        :type Cpu: int
        :param _Mem: 内存
        :type Mem: int
        :param _ProxyCount: 数据库代理组节点个数
        :type ProxyCount: int
        :param _ProxyGroupId: 数据库代理组ID（已废弃）
        :type ProxyGroupId: str
        :param _ReloadBalance: 重新负载均衡：auto（自动），manual（手动）
        :type ReloadBalance: str
        :param _IsInMaintainPeriod: 升级时间 ：no（升级完成时）yes（实例维护时间）
        :type IsInMaintainPeriod: str
        :param _ProxyZones: 数据库代理节点信息
        :type ProxyZones: list of ProxyZone
        """
        self._ClusterId = None
        self._Cpu = None
        self._Mem = None
        self._ProxyCount = None
        self._ProxyGroupId = None
        self._ReloadBalance = None
        self._IsInMaintainPeriod = None
        self._ProxyZones = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ReloadBalance(self):
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod

    @property
    def ProxyZones(self):
        return self._ProxyZones

    @ProxyZones.setter
    def ProxyZones(self, ProxyZones):
        self._ProxyZones = ProxyZones


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._ProxyCount = params.get("ProxyCount")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ReloadBalance = params.get("ReloadBalance")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        if params.get("ProxyZones") is not None:
            self._ProxyZones = []
            for item in params.get("ProxyZones"):
                obj = ProxyZone()
                obj._deserialize(item)
                self._ProxyZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyResponse(AbstractModel):
    """UpgradeProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpgradeProxyVersionRequest(AbstractModel):
    """UpgradeProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _SrcProxyVersion: 数据库代理当前版本
        :type SrcProxyVersion: str
        :param _DstProxyVersion: 数据库代理升级版本
        :type DstProxyVersion: str
        :param _ProxyGroupId: 数据库代理组ID
        :type ProxyGroupId: str
        :param _IsInMaintainPeriod: 升级时间 ：no（升级完成时）yes（实例维护时间）
        :type IsInMaintainPeriod: str
        """
        self._ClusterId = None
        self._SrcProxyVersion = None
        self._DstProxyVersion = None
        self._ProxyGroupId = None
        self._IsInMaintainPeriod = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SrcProxyVersion(self):
        return self._SrcProxyVersion

    @SrcProxyVersion.setter
    def SrcProxyVersion(self, SrcProxyVersion):
        self._SrcProxyVersion = SrcProxyVersion

    @property
    def DstProxyVersion(self):
        return self._DstProxyVersion

    @DstProxyVersion.setter
    def DstProxyVersion(self, DstProxyVersion):
        self._DstProxyVersion = DstProxyVersion

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def IsInMaintainPeriod(self):
        return self._IsInMaintainPeriod

    @IsInMaintainPeriod.setter
    def IsInMaintainPeriod(self, IsInMaintainPeriod):
        self._IsInMaintainPeriod = IsInMaintainPeriod


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SrcProxyVersion = params.get("SrcProxyVersion")
        self._DstProxyVersion = params.get("DstProxyVersion")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyVersionResponse(AbstractModel):
    """UpgradeProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 异步流程ID
        :type FlowId: int
        :param _TaskId: 异步任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UserHostPrivilege(AbstractModel):
    """用户主机权限

    """

    def __init__(self):
        r"""
        :param _DbUserName: 授权用户
        :type DbUserName: str
        :param _DbHost: 客户端ip
注意：此字段可能返回 null，表示取不到有效值。
        :type DbHost: str
        :param _DbPrivilege: 用户权限
注意：此字段可能返回 null，表示取不到有效值。
        :type DbPrivilege: str
        """
        self._DbUserName = None
        self._DbHost = None
        self._DbPrivilege = None

    @property
    def DbUserName(self):
        return self._DbUserName

    @DbUserName.setter
    def DbUserName(self, DbUserName):
        self._DbUserName = DbUserName

    @property
    def DbHost(self):
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPrivilege(self):
        return self._DbPrivilege

    @DbPrivilege.setter
    def DbPrivilege(self, DbPrivilege):
        self._DbPrivilege = DbPrivilege


    def _deserialize(self, params):
        self._DbUserName = params.get("DbUserName")
        self._DbHost = params.get("DbHost")
        self._DbPrivilege = params.get("DbPrivilege")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneStockInfo(AbstractModel):
    """可用区库存信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _HasStock: 是否有库存
        :type HasStock: bool
        :param _StockCount: 库存数量
        :type StockCount: int
        :param _SlaveZoneStockInfos: 备可用区库存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZoneStockInfos: list of SlaveZoneStockInfo
        """
        self._Zone = None
        self._HasStock = None
        self._StockCount = None
        self._SlaveZoneStockInfos = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def HasStock(self):
        return self._HasStock

    @HasStock.setter
    def HasStock(self, HasStock):
        self._HasStock = HasStock

    @property
    def StockCount(self):
        return self._StockCount

    @StockCount.setter
    def StockCount(self, StockCount):
        self._StockCount = StockCount

    @property
    def SlaveZoneStockInfos(self):
        return self._SlaveZoneStockInfos

    @SlaveZoneStockInfos.setter
    def SlaveZoneStockInfos(self, SlaveZoneStockInfos):
        self._SlaveZoneStockInfos = SlaveZoneStockInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._HasStock = params.get("HasStock")
        self._StockCount = params.get("StockCount")
        if params.get("SlaveZoneStockInfos") is not None:
            self._SlaveZoneStockInfos = []
            for item in params.get("SlaveZoneStockInfos"):
                obj = SlaveZoneStockInfo()
                obj._deserialize(item)
                self._SlaveZoneStockInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        