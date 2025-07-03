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


class Address(AbstractModel):
    """添加地址池地址

    """

    def __init__(self):
        r"""
        :param _Addr: 地址值：只支持ipv4、ipv6和域名格式；
不支持回环地址、保留地址、内网地址与腾讯保留网段
注意：此字段可能返回 null，表示取不到有效值。
        :type Addr: str
        :param _IsEnable: 是否启用:DISABLED不启用；ENABLED启用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnable: str
        :param _AddressId: 地址id
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressId: int
        :param _Location: 地址名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _Status: OK正常，DOWN故障，WARN风险，UNKNOWN探测中，UNMONITORED未知
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Weight: 权重，流量策略为WEIGHT时，必填；范围1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        """
        self._Addr = None
        self._IsEnable = None
        self._AddressId = None
        self._Location = None
        self._Status = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def Addr(self):
        """地址值：只支持ipv4、ipv6和域名格式；
不支持回环地址、保留地址、内网地址与腾讯保留网段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Addr

    @Addr.setter
    def Addr(self, Addr):
        self._Addr = Addr

    @property
    def IsEnable(self):
        """是否启用:DISABLED不启用；ENABLED启用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable

    @property
    def AddressId(self):
        """地址id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def Location(self):
        """地址名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Status(self):
        """OK正常，DOWN故障，WARN风险，UNKNOWN探测中，UNMONITORED未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        """权重，流量策略为WEIGHT时，必填；范围1-100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._Addr = params.get("Addr")
        self._IsEnable = params.get("IsEnable")
        self._AddressId = params.get("AddressId")
        self._Location = params.get("Location")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressLocation(AbstractModel):
    """地址所属地域

    """

    def __init__(self):
        r"""
        :param _Addr: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Addr: str
        :param _Location: 所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        """
        self._Addr = None
        self._Location = None

    @property
    def Addr(self):
        """ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Addr

    @Addr.setter
    def Addr(self, Addr):
        self._Addr = Addr

    @property
    def Location(self):
        """所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Addr = params.get("Addr")
        self._Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressPool(AbstractModel):
    """地址池

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池 id
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: int
        :param _PoolName: 地址池名
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolName: str
        :param _AddrType: 地址池地址类型：IPV4、IPV6、DOMAIN
注意：此字段可能返回 null，表示取不到有效值。
        :type AddrType: str
        :param _TrafficStrategy: 流量策略: WEIGHT负载均衡，ALL解析全部
注意：此字段可能返回 null，表示取不到有效值。
        :type TrafficStrategy: str
        :param _MonitorId: 监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorId: int
        :param _Status: OK正常，DOWN故障，WARN风险，UNKNOWN未知
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _AddressNum: 地址数
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressNum: int
        :param _MonitorGroupNum: 探点数
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorGroupNum: int
        :param _MonitorTaskNum: 探测任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorTaskNum: int
        :param _InstanceInfo: 实例相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceInfo: list of InstanceInfo
        :param _AddressSet: 地址池地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressSet: list of Address
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        """
        self._PoolId = None
        self._PoolName = None
        self._AddrType = None
        self._TrafficStrategy = None
        self._MonitorId = None
        self._Status = None
        self._AddressNum = None
        self._MonitorGroupNum = None
        self._MonitorTaskNum = None
        self._InstanceInfo = None
        self._AddressSet = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def PoolId(self):
        """地址池 id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def PoolName(self):
        """地址池名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName

    @property
    def AddrType(self):
        """地址池地址类型：IPV4、IPV6、DOMAIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def TrafficStrategy(self):
        """流量策略: WEIGHT负载均衡，ALL解析全部
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrafficStrategy

    @TrafficStrategy.setter
    def TrafficStrategy(self, TrafficStrategy):
        self._TrafficStrategy = TrafficStrategy

    @property
    def MonitorId(self):
        """监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def Status(self):
        """OK正常，DOWN故障，WARN风险，UNKNOWN未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddressNum(self):
        """地址数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AddressNum

    @AddressNum.setter
    def AddressNum(self, AddressNum):
        self._AddressNum = AddressNum

    @property
    def MonitorGroupNum(self):
        """探点数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorGroupNum

    @MonitorGroupNum.setter
    def MonitorGroupNum(self, MonitorGroupNum):
        self._MonitorGroupNum = MonitorGroupNum

    @property
    def MonitorTaskNum(self):
        """探测任务数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorTaskNum

    @MonitorTaskNum.setter
    def MonitorTaskNum(self, MonitorTaskNum):
        self._MonitorTaskNum = MonitorTaskNum

    @property
    def InstanceInfo(self):
        """实例相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceInfo
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def AddressSet(self):
        """地址池地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._PoolName = params.get("PoolName")
        self._AddrType = params.get("AddrType")
        self._TrafficStrategy = params.get("TrafficStrategy")
        self._MonitorId = params.get("MonitorId")
        self._Status = params.get("Status")
        self._AddressNum = params.get("AddressNum")
        self._MonitorGroupNum = params.get("MonitorGroupNum")
        self._MonitorTaskNum = params.get("MonitorTaskNum")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = []
            for item in params.get("InstanceInfo"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceInfo.append(obj)
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressPoolDetail(AbstractModel):
    """地址池详情

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池 id
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: int
        :param _PoolName: 地址池名
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolName: str
        :param _AddrType: 地址池地址类型：IPV4、IPV6、DOMAIN
注意：此字段可能返回 null，表示取不到有效值。
        :type AddrType: str
        :param _TrafficStrategy: 流量策略: WEIGHT负载均衡，ALL解析全部
注意：此字段可能返回 null，表示取不到有效值。
        :type TrafficStrategy: str
        :param _MonitorId: 监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorId: int
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        """
        self._PoolId = None
        self._PoolName = None
        self._AddrType = None
        self._TrafficStrategy = None
        self._MonitorId = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def PoolId(self):
        """地址池 id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def PoolName(self):
        """地址池名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName

    @property
    def AddrType(self):
        """地址池地址类型：IPV4、IPV6、DOMAIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def TrafficStrategy(self):
        """流量策略: WEIGHT负载均衡，ALL解析全部
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrafficStrategy

    @TrafficStrategy.setter
    def TrafficStrategy(self, TrafficStrategy):
        self._TrafficStrategy = TrafficStrategy

    @property
    def MonitorId(self):
        """监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._PoolName = params.get("PoolName")
        self._AddrType = params.get("AddrType")
        self._TrafficStrategy = params.get("TrafficStrategy")
        self._MonitorId = params.get("MonitorId")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressPoolRequest(AbstractModel):
    """CreateAddressPool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PoolName: 地址池名称，不允许重复
        :type PoolName: str
        :param _TrafficStrategy: 流量策略：WEIGHT负载均衡，ALL解析所有健康地址
        :type TrafficStrategy: str
        :param _AddressSet: 地址列表
        :type AddressSet: list of Address
        :param _MonitorId: 监控器id
        :type MonitorId: int
        """
        self._PoolName = None
        self._TrafficStrategy = None
        self._AddressSet = None
        self._MonitorId = None

    @property
    def PoolName(self):
        """地址池名称，不允许重复
        :rtype: str
        """
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName

    @property
    def TrafficStrategy(self):
        """流量策略：WEIGHT负载均衡，ALL解析所有健康地址
        :rtype: str
        """
        return self._TrafficStrategy

    @TrafficStrategy.setter
    def TrafficStrategy(self, TrafficStrategy):
        self._TrafficStrategy = TrafficStrategy

    @property
    def AddressSet(self):
        """地址列表
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def MonitorId(self):
        """监控器id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._PoolName = params.get("PoolName")
        self._TrafficStrategy = params.get("TrafficStrategy")
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressPoolResponse(AbstractModel):
    """CreateAddressPool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressPoolId: 地址池id
        :type AddressPoolId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressPoolId = None
        self._RequestId = None

    @property
    def AddressPoolId(self):
        """地址池id
        :rtype: int
        """
        return self._AddressPoolId

    @AddressPoolId.setter
    def AddressPoolId(self, AddressPoolId):
        self._AddressPoolId = AddressPoolId

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
        self._AddressPoolId = params.get("AddressPoolId")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 业务域名
        :type Domain: str
        :param _AccessType: CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :type AccessType: str
        :param _GlobalTtl: 解析生效时间	
        :type GlobalTtl: int
        :param _PackageType: 套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
        :type PackageType: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _AccessDomain: 接入主域名
        :type AccessDomain: str
        :param _AccessSubDomain: 接入子域名
        :type AccessSubDomain: str
        :param _Remark: 备注
        :type Remark: str
        :param _ResourceId: 套餐资源id，必填
        :type ResourceId: str
        """
        self._Domain = None
        self._AccessType = None
        self._GlobalTtl = None
        self._PackageType = None
        self._InstanceName = None
        self._AccessDomain = None
        self._AccessSubDomain = None
        self._Remark = None
        self._ResourceId = None

    @property
    def Domain(self):
        """业务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AccessType(self):
        """CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def GlobalTtl(self):
        """解析生效时间	
        :rtype: int
        """
        return self._GlobalTtl

    @GlobalTtl.setter
    def GlobalTtl(self, GlobalTtl):
        self._GlobalTtl = GlobalTtl

    @property
    def PackageType(self):
        """套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AccessDomain(self):
        """接入主域名
        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain

    @property
    def AccessSubDomain(self):
        """接入子域名
        :rtype: str
        """
        return self._AccessSubDomain

    @AccessSubDomain.setter
    def AccessSubDomain(self, AccessSubDomain):
        self._AccessSubDomain = AccessSubDomain

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ResourceId(self):
        """套餐资源id，必填
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._AccessType = params.get("AccessType")
        self._GlobalTtl = params.get("GlobalTtl")
        self._PackageType = params.get("PackageType")
        self._InstanceName = params.get("InstanceName")
        self._AccessDomain = params.get("AccessDomain")
        self._AccessSubDomain = params.get("AccessSubDomain")
        self._Remark = params.get("Remark")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

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


class CreateMonitorRequest(AbstractModel):
    """CreateMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorName: 监控器名称
        :type MonitorName: str
        :param _CheckProtocol: 探测协议，可选值 PING TCP HTTP HTTPS
        :type CheckProtocol: str
        :param _CheckInterval: 检查间隔（秒），可选值有15 60 120 300
        :type CheckInterval: int
        :param _Timeout: 超时时间，单位秒，可选值为2 3 5 10
        :type Timeout: int
        :param _FailTimes: 重试次数，可选值为 0，1，2
        :type FailTimes: int
        :param _FailRate: 失败比例，取值为 20 30 40 50 60 70 80 100，默认值50
        :type FailRate: int
        :param _DetectorStyle: 监控节点类型，可选值有AUTO INTERNAL OVERSEAS IPV6 ALL
        :type DetectorStyle: str
        :param _DetectorGroupIds: 探测器组id列表以,分隔
        :type DetectorGroupIds: list of int non-negative
        :param _PingNum: PING 包数目，当CheckProtocol=ping时必填，可选值有20 50 100
        :type PingNum: int
        :param _TcpPort: 检查端口，可选值在1-65535之间
        :type TcpPort: int
        :param _Host: Host 设置，默认为业务域名
        :type Host: str
        :param _Path: URL 路径，默认为“/”
        :type Path: str
        :param _ReturnCodeThreshold: 返回错误码阈值, 可选值为 400 和 500, 默认值500
        :type ReturnCodeThreshold: int
        :param _EnableRedirect: 跟随 3XX 重定向 ，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :type EnableRedirect: str
        :param _EnableSni: 启用 SNI，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :type EnableSni: str
        :param _PacketLossRate: 丢包率告警阈值，当CheckProtocol=ping时必填取值为10 30 50 80 90 100
        :type PacketLossRate: int
        :param _ContinuePeriod: 持续周期数，可选值1-5
        :type ContinuePeriod: int
        """
        self._MonitorName = None
        self._CheckProtocol = None
        self._CheckInterval = None
        self._Timeout = None
        self._FailTimes = None
        self._FailRate = None
        self._DetectorStyle = None
        self._DetectorGroupIds = None
        self._PingNum = None
        self._TcpPort = None
        self._Host = None
        self._Path = None
        self._ReturnCodeThreshold = None
        self._EnableRedirect = None
        self._EnableSni = None
        self._PacketLossRate = None
        self._ContinuePeriod = None

    @property
    def MonitorName(self):
        """监控器名称
        :rtype: str
        """
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def CheckProtocol(self):
        """探测协议，可选值 PING TCP HTTP HTTPS
        :rtype: str
        """
        return self._CheckProtocol

    @CheckProtocol.setter
    def CheckProtocol(self, CheckProtocol):
        self._CheckProtocol = CheckProtocol

    @property
    def CheckInterval(self):
        """检查间隔（秒），可选值有15 60 120 300
        :rtype: int
        """
        return self._CheckInterval

    @CheckInterval.setter
    def CheckInterval(self, CheckInterval):
        self._CheckInterval = CheckInterval

    @property
    def Timeout(self):
        """超时时间，单位秒，可选值为2 3 5 10
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FailTimes(self):
        """重试次数，可选值为 0，1，2
        :rtype: int
        """
        return self._FailTimes

    @FailTimes.setter
    def FailTimes(self, FailTimes):
        self._FailTimes = FailTimes

    @property
    def FailRate(self):
        """失败比例，取值为 20 30 40 50 60 70 80 100，默认值50
        :rtype: int
        """
        return self._FailRate

    @FailRate.setter
    def FailRate(self, FailRate):
        self._FailRate = FailRate

    @property
    def DetectorStyle(self):
        """监控节点类型，可选值有AUTO INTERNAL OVERSEAS IPV6 ALL
        :rtype: str
        """
        return self._DetectorStyle

    @DetectorStyle.setter
    def DetectorStyle(self, DetectorStyle):
        self._DetectorStyle = DetectorStyle

    @property
    def DetectorGroupIds(self):
        """探测器组id列表以,分隔
        :rtype: list of int non-negative
        """
        return self._DetectorGroupIds

    @DetectorGroupIds.setter
    def DetectorGroupIds(self, DetectorGroupIds):
        self._DetectorGroupIds = DetectorGroupIds

    @property
    def PingNum(self):
        """PING 包数目，当CheckProtocol=ping时必填，可选值有20 50 100
        :rtype: int
        """
        return self._PingNum

    @PingNum.setter
    def PingNum(self, PingNum):
        self._PingNum = PingNum

    @property
    def TcpPort(self):
        """检查端口，可选值在1-65535之间
        :rtype: int
        """
        return self._TcpPort

    @TcpPort.setter
    def TcpPort(self, TcpPort):
        self._TcpPort = TcpPort

    @property
    def Host(self):
        """Host 设置，默认为业务域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        """URL 路径，默认为“/”
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ReturnCodeThreshold(self):
        """返回错误码阈值, 可选值为 400 和 500, 默认值500
        :rtype: int
        """
        return self._ReturnCodeThreshold

    @ReturnCodeThreshold.setter
    def ReturnCodeThreshold(self, ReturnCodeThreshold):
        self._ReturnCodeThreshold = ReturnCodeThreshold

    @property
    def EnableRedirect(self):
        """跟随 3XX 重定向 ，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :rtype: str
        """
        return self._EnableRedirect

    @EnableRedirect.setter
    def EnableRedirect(self, EnableRedirect):
        self._EnableRedirect = EnableRedirect

    @property
    def EnableSni(self):
        """启用 SNI，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :rtype: str
        """
        return self._EnableSni

    @EnableSni.setter
    def EnableSni(self, EnableSni):
        self._EnableSni = EnableSni

    @property
    def PacketLossRate(self):
        """丢包率告警阈值，当CheckProtocol=ping时必填取值为10 30 50 80 90 100
        :rtype: int
        """
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def ContinuePeriod(self):
        """持续周期数，可选值1-5
        :rtype: int
        """
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod


    def _deserialize(self, params):
        self._MonitorName = params.get("MonitorName")
        self._CheckProtocol = params.get("CheckProtocol")
        self._CheckInterval = params.get("CheckInterval")
        self._Timeout = params.get("Timeout")
        self._FailTimes = params.get("FailTimes")
        self._FailRate = params.get("FailRate")
        self._DetectorStyle = params.get("DetectorStyle")
        self._DetectorGroupIds = params.get("DetectorGroupIds")
        self._PingNum = params.get("PingNum")
        self._TcpPort = params.get("TcpPort")
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._ReturnCodeThreshold = params.get("ReturnCodeThreshold")
        self._EnableRedirect = params.get("EnableRedirect")
        self._EnableSni = params.get("EnableSni")
        self._PacketLossRate = params.get("PacketLossRate")
        self._ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMonitorResponse(AbstractModel):
    """CreateMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorId = None
        self._RequestId = None

    @property
    def MonitorId(self):
        """监控器id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

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
        self._MonitorId = params.get("MonitorId")
        self._RequestId = params.get("RequestId")


class CreateStrategyRequest(AbstractModel):
    """CreateStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _StrategyName: 策略名称，不允许重复
        :type StrategyName: str
        :param _Source: 解析线路
        :type Source: list of Source
        :param _MainAddressPoolSet: 主力地址池集合，最多允许配置四级
        :type MainAddressPoolSet: list of MainAddressPool
        :param _FallbackAddressPoolSet: 兜底地址池集合，只允许配置一级，且地址池数量为1
        :type FallbackAddressPoolSet: list of MainAddressPool
        :param _KeepDomainRecords: 是否开启策略强制保留默认线路 disabled, enabled，默认不开启且只有一个策略能开启
        :type KeepDomainRecords: str
        :param _SwitchPoolType: 策略调度模式：AUTO默认切换；STOP仅暂停不切换
        :type SwitchPoolType: str
        """
        self._InstanceId = None
        self._StrategyName = None
        self._Source = None
        self._MainAddressPoolSet = None
        self._FallbackAddressPoolSet = None
        self._KeepDomainRecords = None
        self._SwitchPoolType = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyName(self):
        """策略名称，不允许重复
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Source(self):
        """解析线路
        :rtype: list of Source
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def MainAddressPoolSet(self):
        """主力地址池集合，最多允许配置四级
        :rtype: list of MainAddressPool
        """
        return self._MainAddressPoolSet

    @MainAddressPoolSet.setter
    def MainAddressPoolSet(self, MainAddressPoolSet):
        self._MainAddressPoolSet = MainAddressPoolSet

    @property
    def FallbackAddressPoolSet(self):
        """兜底地址池集合，只允许配置一级，且地址池数量为1
        :rtype: list of MainAddressPool
        """
        return self._FallbackAddressPoolSet

    @FallbackAddressPoolSet.setter
    def FallbackAddressPoolSet(self, FallbackAddressPoolSet):
        self._FallbackAddressPoolSet = FallbackAddressPoolSet

    @property
    def KeepDomainRecords(self):
        """是否开启策略强制保留默认线路 disabled, enabled，默认不开启且只有一个策略能开启
        :rtype: str
        """
        return self._KeepDomainRecords

    @KeepDomainRecords.setter
    def KeepDomainRecords(self, KeepDomainRecords):
        self._KeepDomainRecords = KeepDomainRecords

    @property
    def SwitchPoolType(self):
        """策略调度模式：AUTO默认切换；STOP仅暂停不切换
        :rtype: str
        """
        return self._SwitchPoolType

    @SwitchPoolType.setter
    def SwitchPoolType(self, SwitchPoolType):
        self._SwitchPoolType = SwitchPoolType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyName = params.get("StrategyName")
        if params.get("Source") is not None:
            self._Source = []
            for item in params.get("Source"):
                obj = Source()
                obj._deserialize(item)
                self._Source.append(obj)
        if params.get("MainAddressPoolSet") is not None:
            self._MainAddressPoolSet = []
            for item in params.get("MainAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._MainAddressPoolSet.append(obj)
        if params.get("FallbackAddressPoolSet") is not None:
            self._FallbackAddressPoolSet = []
            for item in params.get("FallbackAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._FallbackAddressPoolSet.append(obj)
        self._KeepDomainRecords = params.get("KeepDomainRecords")
        self._SwitchPoolType = params.get("SwitchPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStrategyResponse(AbstractModel):
    """CreateStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 新增策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StrategyId = None
        self._RequestId = None

    @property
    def StrategyId(self):
        """新增策略id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

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
        self._StrategyId = params.get("StrategyId")
        self._RequestId = params.get("RequestId")


class DeleteAddressPoolRequest(AbstractModel):
    """DeleteAddressPool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池id
        :type PoolId: int
        """
        self._PoolId = None

    @property
    def PoolId(self):
        """地址池id
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressPoolResponse(AbstractModel):
    """DeleteAddressPool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteMonitorRequest(AbstractModel):
    """DeleteMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监控器id
        :type MonitorId: int
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        """监控器id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMonitorResponse(AbstractModel):
    """DeleteMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 成功返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """成功返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteStrategyRequest(AbstractModel):
    """DeleteStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略id
        :type StrategyId: int
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._StrategyId = None
        self._InstanceId = None

    @property
    def StrategyId(self):
        """策略id
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStrategyResponse(AbstractModel):
    """DeleteStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeAddressLocationRequest(AbstractModel):
    """DescribeAddressLocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Address: 地址数组
        :type Address: list of str
        """
        self._Address = None

    @property
    def Address(self):
        """地址数组
        :rtype: list of str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressLocationResponse(AbstractModel):
    """DescribeAddressLocation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressLocation: 所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressLocation: list of AddressLocation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressLocation = None
        self._RequestId = None

    @property
    def AddressLocation(self):
        """所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AddressLocation
        """
        return self._AddressLocation

    @AddressLocation.setter
    def AddressLocation(self, AddressLocation):
        self._AddressLocation = AddressLocation

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
        if params.get("AddressLocation") is not None:
            self._AddressLocation = []
            for item in params.get("AddressLocation"):
                obj = AddressLocation()
                obj._deserialize(item)
                self._AddressLocation.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAddressPoolDetailRequest(AbstractModel):
    """DescribeAddressPoolDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池id
        :type PoolId: int
        """
        self._PoolId = None

    @property
    def PoolId(self):
        """地址池id
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressPoolDetailResponse(AbstractModel):
    """DescribeAddressPoolDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressPool: 资源组详情描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressPool: :class:`tencentcloud.igtm.v20231024.models.AddressPoolDetail`
        :param _AddressSet: 资源组中的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressSet: list of Address
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressPool = None
        self._AddressSet = None
        self._RequestId = None

    @property
    def AddressPool(self):
        """资源组详情描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.igtm.v20231024.models.AddressPoolDetail`
        """
        return self._AddressPool

    @AddressPool.setter
    def AddressPool(self, AddressPool):
        self._AddressPool = AddressPool

    @property
    def AddressSet(self):
        """资源组中的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

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
        if params.get("AddressPool") is not None:
            self._AddressPool = AddressPoolDetail()
            self._AddressPool._deserialize(params.get("AddressPool"))
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAddressPoolListRequest(AbstractModel):
    """DescribeAddressPoolList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 告警过滤条件：PoolName：地址池名称；MonitorId：监控器id
        :type Filters: list of ResourceFilter
        :param _Offset: 页数
        :type Offset: int
        :param _Limit: 每页数
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """告警过滤条件：PoolName：地址池名称；MonitorId：监控器id
        :rtype: list of ResourceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """页数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ResourceFilter()
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
        


class DescribeAddressPoolListResponse(AbstractModel):
    """DescribeAddressPoolList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressPoolSet: 资源组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressPoolSet: list of AddressPool
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressPoolSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AddressPoolSet(self):
        """资源组列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AddressPool
        """
        return self._AddressPoolSet

    @AddressPoolSet.setter
    def AddressPoolSet(self, AddressPoolSet):
        self._AddressPoolSet = AddressPoolSet

    @property
    def TotalCount(self):
        """总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("AddressPoolSet") is not None:
            self._AddressPoolSet = []
            for item in params.get("AddressPoolSet"):
                obj = AddressPool()
                obj._deserialize(item)
                self._AddressPoolSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDetectorsRequest(AbstractModel):
    """DescribeDetectors请求参数结构体

    """


class DescribeDetectorsResponse(AbstractModel):
    """DescribeDetectors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetectorGroupSet: 探测器组列表
        :type DetectorGroupSet: list of DetectorGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetectorGroupSet = None
        self._RequestId = None

    @property
    def DetectorGroupSet(self):
        """探测器组列表
        :rtype: list of DetectorGroup
        """
        return self._DetectorGroupSet

    @DetectorGroupSet.setter
    def DetectorGroupSet(self, DetectorGroupSet):
        self._DetectorGroupSet = DetectorGroupSet

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
        if params.get("DetectorGroupSet") is not None:
            self._DetectorGroupSet = []
            for item in params.get("DetectorGroupSet"):
                obj = DetectorGroup()
                obj._deserialize(item)
                self._DetectorGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDnsLineListRequest(AbstractModel):
    """DescribeDnsLineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例id
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
        


class DescribeDnsLineListResponse(AbstractModel):
    """DescribeDnsLineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DnsLineSet: 地址池列表
        :type DnsLineSet: list of GroupLine
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DnsLineSet = None
        self._RequestId = None

    @property
    def DnsLineSet(self):
        """地址池列表
        :rtype: list of GroupLine
        """
        return self._DnsLineSet

    @DnsLineSet.setter
    def DnsLineSet(self, DnsLineSet):
        self._DnsLineSet = DnsLineSet

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
        if params.get("DnsLineSet") is not None:
            self._DnsLineSet = []
            for item in params.get("DnsLineSet"):
                obj = GroupLine()
                obj._deserialize(item)
                self._DnsLineSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

    """


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instance: 实例详情
        :type Instance: :class:`tencentcloud.igtm.v20231024.models.InstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instance = None
        self._RequestId = None

    @property
    def Instance(self):
        """实例详情
        :rtype: :class:`tencentcloud.igtm.v20231024.models.InstanceDetail`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

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
        if params.get("Instance") is not None:
            self._Instance = InstanceDetail()
            self._Instance._deserialize(params.get("Instance"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页数
        :type Limit: int
        :param _Filters: Name: "实例名称" 模糊查询Domain: "域名" 模糊查询MonitorId: "监控器 id" PoolId: "地址池id", AccessDomain接入主域名
        :type Filters: list of ResourceFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
        """分页数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Name: "实例名称" 模糊查询Domain: "域名" 模糊查询MonitorId: "监控器 id" PoolId: "地址池id", AccessDomain接入主域名
        :rtype: list of ResourceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ResourceFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
        :param _TotalCount: 列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _SystemAccessEnabled: 是否支持系统域名接入：true支持；false不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemAccessEnabled: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._SystemAccessEnabled = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        """实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        """列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SystemAccessEnabled(self):
        """是否支持系统域名接入：true支持；false不支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SystemAccessEnabled

    @SystemAccessEnabled.setter
    def SystemAccessEnabled(self, SystemAccessEnabled):
        self._SystemAccessEnabled = SystemAccessEnabled

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._SystemAccessEnabled = params.get("SystemAccessEnabled")
        self._RequestId = params.get("RequestId")


class DescribeMonitorDetailRequest(AbstractModel):
    """DescribeMonitorDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监控器id
        :type MonitorId: int
        """
        self._MonitorId = None

    @property
    def MonitorId(self):
        """监控器id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorDetailResponse(AbstractModel):
    """DescribeMonitorDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorDetail: 探测规则
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorDetail: :class:`tencentcloud.igtm.v20231024.models.MonitorDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorDetail = None
        self._RequestId = None

    @property
    def MonitorDetail(self):
        """探测规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.igtm.v20231024.models.MonitorDetail`
        """
        return self._MonitorDetail

    @MonitorDetail.setter
    def MonitorDetail(self, MonitorDetail):
        self._MonitorDetail = MonitorDetail

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
        if params.get("MonitorDetail") is not None:
            self._MonitorDetail = MonitorDetail()
            self._MonitorDetail._deserialize(params.get("MonitorDetail"))
        self._RequestId = params.get("RequestId")


class DescribeMonitorsRequest(AbstractModel):
    """DescribeMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页，偏移值
        :type Offset: int
        :param _Limit: 分页，当前分页记录数
        :type Limit: int
        :param _IsDetectNum: 是否查探测次数0否1是
        :type IsDetectNum: int
        """
        self._Offset = None
        self._Limit = None
        self._IsDetectNum = None

    @property
    def Offset(self):
        """分页，偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页，当前分页记录数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IsDetectNum(self):
        """是否查探测次数0否1是
        :rtype: int
        """
        return self._IsDetectNum

    @IsDetectNum.setter
    def IsDetectNum(self, IsDetectNum):
        self._IsDetectNum = IsDetectNum


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IsDetectNum = params.get("IsDetectNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorsResponse(AbstractModel):
    """DescribeMonitors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorDataSet: 监控器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorDataSet: list of MonitorDetail
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorDataSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MonitorDataSet(self):
        """监控器列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MonitorDetail
        """
        return self._MonitorDataSet

    @MonitorDataSet.setter
    def MonitorDataSet(self, MonitorDataSet):
        self._MonitorDataSet = MonitorDataSet

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("MonitorDataSet") is not None:
            self._MonitorDataSet = []
            for item in params.get("MonitorDataSet"):
                obj = MonitorDetail()
                obj._deserialize(item)
                self._MonitorDataSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeQuotasRequest(AbstractModel):
    """DescribeQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessDomain: 接入域名
        :type AccessDomain: str
        """
        self._AccessDomain = None

    @property
    def AccessDomain(self):
        """接入域名
        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain


    def _deserialize(self, params):
        self._AccessDomain = params.get("AccessDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotasResponse(AbstractModel):
    """DescribeQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Quotas: 配额id
注意：此字段可能返回 null，表示取不到有效值。
        :type Quotas: :class:`tencentcloud.igtm.v20231024.models.Quota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Quotas = None
        self._RequestId = None

    @property
    def Quotas(self):
        """配额id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.igtm.v20231024.models.Quota`
        """
        return self._Quotas

    @Quotas.setter
    def Quotas(self, Quotas):
        self._Quotas = Quotas

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
        if params.get("Quotas") is not None:
            self._Quotas = Quota()
            self._Quotas._deserialize(params.get("Quotas"))
        self._RequestId = params.get("RequestId")


class DescribeStrategyDetailRequest(AbstractModel):
    """DescribeStrategyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _StrategyId: 策略 id
        :type StrategyId: int
        """
        self._InstanceId = None
        self._StrategyId = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyId(self):
        """策略 id
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategyDetailResponse(AbstractModel):
    """DescribeStrategyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyDetail: 策略详情
        :type StrategyDetail: :class:`tencentcloud.igtm.v20231024.models.StrategyDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StrategyDetail = None
        self._RequestId = None

    @property
    def StrategyDetail(self):
        """策略详情
        :rtype: :class:`tencentcloud.igtm.v20231024.models.StrategyDetail`
        """
        return self._StrategyDetail

    @StrategyDetail.setter
    def StrategyDetail(self, StrategyDetail):
        self._StrategyDetail = StrategyDetail

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
        if params.get("StrategyDetail") is not None:
            self._StrategyDetail = StrategyDetail()
            self._StrategyDetail._deserialize(params.get("StrategyDetail"))
        self._RequestId = params.get("RequestId")


class DescribeStrategyListRequest(AbstractModel):
    """DescribeStrategyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 每页条数
        :type Limit: int
        :param _Filters: 策略过滤条件：StrategyName：策略名称
        :type Filters: list of ResourceFilter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        """实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """策略过滤条件：StrategyName：策略名称
        :rtype: list of ResourceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ResourceFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategyListResponse(AbstractModel):
    """DescribeStrategyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategySet: 策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategySet: list of Strategy
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StrategySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def StrategySet(self):
        """策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Strategy
        """
        return self._StrategySet

    @StrategySet.setter
    def StrategySet(self, StrategySet):
        self._StrategySet = StrategySet

    @property
    def TotalCount(self):
        """总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("StrategySet") is not None:
            self._StrategySet = []
            for item in params.get("StrategySet"):
                obj = Strategy()
                obj._deserialize(item)
                self._StrategySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetectorGroup(AbstractModel):
    """探测组

    """

    def __init__(self):
        r"""
        :param _Gid: 线路组id GroupLineId
        :type Gid: int
        :param _GroupType: bgp, international, isp
        :type GroupType: str
        :param _GroupName: 组名
        :type GroupName: str
        :param _InternetFamily: ipv4, ipv6
        :type InternetFamily: str
        :param _PackageSet: 支持的套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageSet: list of str
        """
        self._Gid = None
        self._GroupType = None
        self._GroupName = None
        self._InternetFamily = None
        self._PackageSet = None

    @property
    def Gid(self):
        """线路组id GroupLineId
        :rtype: int
        """
        return self._Gid

    @Gid.setter
    def Gid(self, Gid):
        self._Gid = Gid

    @property
    def GroupType(self):
        """bgp, international, isp
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def GroupName(self):
        """组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InternetFamily(self):
        """ipv4, ipv6
        :rtype: str
        """
        return self._InternetFamily

    @InternetFamily.setter
    def InternetFamily(self, InternetFamily):
        self._InternetFamily = InternetFamily

    @property
    def PackageSet(self):
        """支持的套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PackageSet

    @PackageSet.setter
    def PackageSet(self, PackageSet):
        self._PackageSet = PackageSet


    def _deserialize(self, params):
        self._Gid = params.get("Gid")
        self._GroupType = params.get("GroupType")
        self._GroupName = params.get("GroupName")
        self._InternetFamily = params.get("InternetFamily")
        self._PackageSet = params.get("PackageSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupLine(AbstractModel):
    """线路列表

    """

    def __init__(self):
        r"""
        :param _DnsLineId: 分组线路id
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsLineId: int
        :param _Parent: 父节点 0为根节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Parent: int
        :param _LineName: 线路名
注意：此字段可能返回 null，表示取不到有效值。
        :type LineName: str
        :param _LineId: 10=9 DNSPod 线路 id
注意：此字段可能返回 null，表示取不到有效值。
        :type LineId: str
        :param _Useful: 是否已使用过
注意：此字段可能返回 null，表示取不到有效值。
        :type Useful: bool
        :param _SubGroup: 0为未使用
注意：此字段可能返回 null，表示取不到有效值。
        :type SubGroup: int
        :param _LinePackage: 权限标识
注意：此字段可能返回 null，表示取不到有效值。
        :type LinePackage: int
        :param _Weight: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._DnsLineId = None
        self._Parent = None
        self._LineName = None
        self._LineId = None
        self._Useful = None
        self._SubGroup = None
        self._LinePackage = None
        self._Weight = None

    @property
    def DnsLineId(self):
        """分组线路id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DnsLineId

    @DnsLineId.setter
    def DnsLineId(self, DnsLineId):
        self._DnsLineId = DnsLineId

    @property
    def Parent(self):
        """父节点 0为根节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Parent

    @Parent.setter
    def Parent(self, Parent):
        self._Parent = Parent

    @property
    def LineName(self):
        """线路名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LineName

    @LineName.setter
    def LineName(self, LineName):
        self._LineName = LineName

    @property
    def LineId(self):
        """10=9 DNSPod 线路 id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId

    @property
    def Useful(self):
        """是否已使用过
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Useful

    @Useful.setter
    def Useful(self, Useful):
        self._Useful = Useful

    @property
    def SubGroup(self):
        """0为未使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubGroup

    @SubGroup.setter
    def SubGroup(self, SubGroup):
        self._SubGroup = SubGroup

    @property
    def LinePackage(self):
        """权限标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LinePackage

    @LinePackage.setter
    def LinePackage(self, LinePackage):
        self._LinePackage = LinePackage

    @property
    def Weight(self):
        """1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._DnsLineId = params.get("DnsLineId")
        self._Parent = params.get("Parent")
        self._LineName = params.get("LineName")
        self._LineId = params.get("LineId")
        self._Useful = params.get("Useful")
        self._SubGroup = params.get("SubGroup")
        self._LinePackage = params.get("LinePackage")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """返回实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _ResourceId: 资源 id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Domain: 业务域名
        :type Domain: str
        :param _AccessType: Cname域名接入方式
CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :type AccessType: str
        :param _AccessDomain: 接入域名
        :type AccessDomain: str
        :param _AccessSubDomain: 接入子域名
        :type AccessSubDomain: str
        :param _GlobalTtl: 全局记录过期时间
        :type GlobalTtl: int
        :param _PackageType: 套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _WorkingStatus: 实例运行状态
NORMAL: 健康
FAULTY: 有风险
DOWN: 宕机
UNKNOWN: 未知
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkingStatus: str
        :param _Status: 实例状态
ENABLED: 正常
DISABLED: 禁用
        :type Status: str
        :param _IsCnameConfigured: 是否cname接入：true已接入；false未接入
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCnameConfigured: bool
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _StrategyNum: 策略数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyNum: int
        :param _AddressPoolNum: 绑定地址池个数
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressPoolNum: int
        :param _MonitorNum: 绑定监控器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorNum: int
        :param _PoolId: 地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: int
        :param _PoolName: 地址池名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolName: str
        :param _CreatedOn: 实例创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 实例更新时间
        :type UpdatedOn: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._ResourceId = None
        self._Domain = None
        self._AccessType = None
        self._AccessDomain = None
        self._AccessSubDomain = None
        self._GlobalTtl = None
        self._PackageType = None
        self._WorkingStatus = None
        self._Status = None
        self._IsCnameConfigured = None
        self._Remark = None
        self._StrategyNum = None
        self._AddressPoolNum = None
        self._MonitorNum = None
        self._PoolId = None
        self._PoolName = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceId(self):
        """资源 id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Domain(self):
        """业务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AccessType(self):
        """Cname域名接入方式
CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AccessDomain(self):
        """接入域名
        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain

    @property
    def AccessSubDomain(self):
        """接入子域名
        :rtype: str
        """
        return self._AccessSubDomain

    @AccessSubDomain.setter
    def AccessSubDomain(self, AccessSubDomain):
        self._AccessSubDomain = AccessSubDomain

    @property
    def GlobalTtl(self):
        """全局记录过期时间
        :rtype: int
        """
        return self._GlobalTtl

    @GlobalTtl.setter
    def GlobalTtl(self, GlobalTtl):
        self._GlobalTtl = GlobalTtl

    @property
    def PackageType(self):
        """套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def WorkingStatus(self):
        """实例运行状态
NORMAL: 健康
FAULTY: 有风险
DOWN: 宕机
UNKNOWN: 未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkingStatus

    @WorkingStatus.setter
    def WorkingStatus(self, WorkingStatus):
        self._WorkingStatus = WorkingStatus

    @property
    def Status(self):
        """实例状态
ENABLED: 正常
DISABLED: 禁用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCnameConfigured(self):
        """是否cname接入：true已接入；false未接入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsCnameConfigured

    @IsCnameConfigured.setter
    def IsCnameConfigured(self, IsCnameConfigured):
        self._IsCnameConfigured = IsCnameConfigured

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StrategyNum(self):
        """策略数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StrategyNum

    @StrategyNum.setter
    def StrategyNum(self, StrategyNum):
        self._StrategyNum = StrategyNum

    @property
    def AddressPoolNum(self):
        """绑定地址池个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AddressPoolNum

    @AddressPoolNum.setter
    def AddressPoolNum(self, AddressPoolNum):
        self._AddressPoolNum = AddressPoolNum

    @property
    def MonitorNum(self):
        """绑定监控器数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorNum

    @MonitorNum.setter
    def MonitorNum(self, MonitorNum):
        self._MonitorNum = MonitorNum

    @property
    def PoolId(self):
        """地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def PoolName(self):
        """地址池名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName

    @property
    def CreatedOn(self):
        """实例创建时间
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """实例更新时间
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ResourceId = params.get("ResourceId")
        self._Domain = params.get("Domain")
        self._AccessType = params.get("AccessType")
        self._AccessDomain = params.get("AccessDomain")
        self._AccessSubDomain = params.get("AccessSubDomain")
        self._GlobalTtl = params.get("GlobalTtl")
        self._PackageType = params.get("PackageType")
        self._WorkingStatus = params.get("WorkingStatus")
        self._Status = params.get("Status")
        self._IsCnameConfigured = params.get("IsCnameConfigured")
        self._Remark = params.get("Remark")
        self._StrategyNum = params.get("StrategyNum")
        self._AddressPoolNum = params.get("AddressPoolNum")
        self._MonitorNum = params.get("MonitorNum")
        self._PoolId = params.get("PoolId")
        self._PoolName = params.get("PoolName")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfig(AbstractModel):
    """实例配置详情

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Domain: 业务域名
        :type Domain: str
        :param _AccessType: CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :type AccessType: str
        :param _Remark: 备注
        :type Remark: str
        :param _GlobalTtl: 全局记录过期时间	
        :type GlobalTtl: int
        :param _AccessDomain: 接入主域名，自定义接入域名时必填

        :type AccessDomain: str
        :param _AccessSubDomain: 接入子域名，自定义接入域名时必填
        :type AccessSubDomain: str
        """
        self._InstanceName = None
        self._Domain = None
        self._AccessType = None
        self._Remark = None
        self._GlobalTtl = None
        self._AccessDomain = None
        self._AccessSubDomain = None

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Domain(self):
        """业务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AccessType(self):
        """CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GlobalTtl(self):
        """全局记录过期时间	
        :rtype: int
        """
        return self._GlobalTtl

    @GlobalTtl.setter
    def GlobalTtl(self, GlobalTtl):
        self._GlobalTtl = GlobalTtl

    @property
    def AccessDomain(self):
        """接入主域名，自定义接入域名时必填

        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain

    @property
    def AccessSubDomain(self):
        """接入子域名，自定义接入域名时必填
        :rtype: str
        """
        return self._AccessSubDomain

    @AccessSubDomain.setter
    def AccessSubDomain(self, AccessSubDomain):
        self._AccessSubDomain = AccessSubDomain


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Domain = params.get("Domain")
        self._AccessType = params.get("AccessType")
        self._Remark = params.get("Remark")
        self._GlobalTtl = params.get("GlobalTtl")
        self._AccessDomain = params.get("AccessDomain")
        self._AccessSubDomain = params.get("AccessSubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """返回实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _Domain: 业务域名
        :type Domain: str
        :param _AccessType: Cname域名接入方式
CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :type AccessType: str
        :param _AccessSubDomain: 接入子域名	
        :type AccessSubDomain: str
        :param _AccessDomain: 接入域名	
        :type AccessDomain: str
        :param _GlobalTtl: 解析生效时间
        :type GlobalTtl: int
        :param _PackageType: 套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _WorkingStatus: 实例运行状态
NORMAL: 健康
FAULTY: 有风险
DOWN: 宕机
UNKNOWN: 未知
        :type WorkingStatus: str
        :param _Status: 实例状态
ENABLED: 正常
DISABLED: 禁用
        :type Status: str
        :param _IsCnameConfigured: cname是否接入：true已接入；false未接入
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCnameConfigured: bool
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _StrategyNum: 策略数量
        :type StrategyNum: int
        :param _AddressPoolNum: 绑定地址池个数
        :type AddressPoolNum: int
        :param _MonitorNum: 绑定监控器数量
        :type MonitorNum: int
        :param _ResourceId: 实例绑定套餐资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _NotifyEventSet: 订阅事件列表
        :type NotifyEventSet: list of str
        :param _CreatedOn: 实例创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 实例更新时间
        :type UpdatedOn: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Domain = None
        self._AccessType = None
        self._AccessSubDomain = None
        self._AccessDomain = None
        self._GlobalTtl = None
        self._PackageType = None
        self._WorkingStatus = None
        self._Status = None
        self._IsCnameConfigured = None
        self._Remark = None
        self._StrategyNum = None
        self._AddressPoolNum = None
        self._MonitorNum = None
        self._ResourceId = None
        self._NotifyEventSet = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Domain(self):
        """业务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AccessType(self):
        """Cname域名接入方式
CUSTOM: 自定义接入域名
SYSTEM: 系统接入域名
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AccessSubDomain(self):
        """接入子域名	
        :rtype: str
        """
        return self._AccessSubDomain

    @AccessSubDomain.setter
    def AccessSubDomain(self, AccessSubDomain):
        self._AccessSubDomain = AccessSubDomain

    @property
    def AccessDomain(self):
        """接入域名	
        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain

    @property
    def GlobalTtl(self):
        """解析生效时间
        :rtype: int
        """
        return self._GlobalTtl

    @GlobalTtl.setter
    def GlobalTtl(self, GlobalTtl):
        self._GlobalTtl = GlobalTtl

    @property
    def PackageType(self):
        """套餐类型
FREE: 免费版
STANDARD：标准版
ULTIMATE：旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def WorkingStatus(self):
        """实例运行状态
NORMAL: 健康
FAULTY: 有风险
DOWN: 宕机
UNKNOWN: 未知
        :rtype: str
        """
        return self._WorkingStatus

    @WorkingStatus.setter
    def WorkingStatus(self, WorkingStatus):
        self._WorkingStatus = WorkingStatus

    @property
    def Status(self):
        """实例状态
ENABLED: 正常
DISABLED: 禁用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCnameConfigured(self):
        """cname是否接入：true已接入；false未接入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsCnameConfigured

    @IsCnameConfigured.setter
    def IsCnameConfigured(self, IsCnameConfigured):
        self._IsCnameConfigured = IsCnameConfigured

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StrategyNum(self):
        """策略数量
        :rtype: int
        """
        return self._StrategyNum

    @StrategyNum.setter
    def StrategyNum(self, StrategyNum):
        self._StrategyNum = StrategyNum

    @property
    def AddressPoolNum(self):
        """绑定地址池个数
        :rtype: int
        """
        return self._AddressPoolNum

    @AddressPoolNum.setter
    def AddressPoolNum(self, AddressPoolNum):
        self._AddressPoolNum = AddressPoolNum

    @property
    def MonitorNum(self):
        """绑定监控器数量
        :rtype: int
        """
        return self._MonitorNum

    @MonitorNum.setter
    def MonitorNum(self, MonitorNum):
        self._MonitorNum = MonitorNum

    @property
    def ResourceId(self):
        """实例绑定套餐资源id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def NotifyEventSet(self):
        """订阅事件列表
        :rtype: list of str
        """
        return self._NotifyEventSet

    @NotifyEventSet.setter
    def NotifyEventSet(self, NotifyEventSet):
        self._NotifyEventSet = NotifyEventSet

    @property
    def CreatedOn(self):
        """实例创建时间
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """实例更新时间
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Domain = params.get("Domain")
        self._AccessType = params.get("AccessType")
        self._AccessSubDomain = params.get("AccessSubDomain")
        self._AccessDomain = params.get("AccessDomain")
        self._GlobalTtl = params.get("GlobalTtl")
        self._PackageType = params.get("PackageType")
        self._WorkingStatus = params.get("WorkingStatus")
        self._Status = params.get("Status")
        self._IsCnameConfigured = params.get("IsCnameConfigured")
        self._Remark = params.get("Remark")
        self._StrategyNum = params.get("StrategyNum")
        self._AddressPoolNum = params.get("AddressPoolNum")
        self._MonitorNum = params.get("MonitorNum")
        self._ResourceId = params.get("ResourceId")
        self._NotifyEventSet = params.get("NotifyEventSet")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例相关信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class MainAddressPool(AbstractModel):
    """主力地址池

    """

    def __init__(self):
        r"""
        :param _AddressPools: 集合中的地址池id与权重，数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressPools: list of MainPoolWeight
        :param _MainAddressPoolId: 地址池集合id
注意：此字段可能返回 null，表示取不到有效值。
        :type MainAddressPoolId: int
        :param _MinSurviveNum: 切换阀值，不能大于主力集合内地址总数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinSurviveNum: int
        :param _TrafficStrategy: 切换策略:ALL解析所有地址；WEIGHT：负载均衡。当为ALL时，解析地址的权重值为1；当为WEIGHT时；权重为地址池权重*地址权重
注意：此字段可能返回 null，表示取不到有效值。
        :type TrafficStrategy: str
        """
        self._AddressPools = None
        self._MainAddressPoolId = None
        self._MinSurviveNum = None
        self._TrafficStrategy = None

    @property
    def AddressPools(self):
        """集合中的地址池id与权重，数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MainPoolWeight
        """
        return self._AddressPools

    @AddressPools.setter
    def AddressPools(self, AddressPools):
        self._AddressPools = AddressPools

    @property
    def MainAddressPoolId(self):
        """地址池集合id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MainAddressPoolId

    @MainAddressPoolId.setter
    def MainAddressPoolId(self, MainAddressPoolId):
        self._MainAddressPoolId = MainAddressPoolId

    @property
    def MinSurviveNum(self):
        """切换阀值，不能大于主力集合内地址总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinSurviveNum

    @MinSurviveNum.setter
    def MinSurviveNum(self, MinSurviveNum):
        self._MinSurviveNum = MinSurviveNum

    @property
    def TrafficStrategy(self):
        """切换策略:ALL解析所有地址；WEIGHT：负载均衡。当为ALL时，解析地址的权重值为1；当为WEIGHT时；权重为地址池权重*地址权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrafficStrategy

    @TrafficStrategy.setter
    def TrafficStrategy(self, TrafficStrategy):
        self._TrafficStrategy = TrafficStrategy


    def _deserialize(self, params):
        if params.get("AddressPools") is not None:
            self._AddressPools = []
            for item in params.get("AddressPools"):
                obj = MainPoolWeight()
                obj._deserialize(item)
                self._AddressPools.append(obj)
        self._MainAddressPoolId = params.get("MainAddressPoolId")
        self._MinSurviveNum = params.get("MinSurviveNum")
        self._TrafficStrategy = params.get("TrafficStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainPoolWeight(AbstractModel):
    """主力地址池id与权重

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: int
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._PoolId = None
        self._Weight = None

    @property
    def PoolId(self):
        """地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

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


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressPoolRequest(AbstractModel):
    """ModifyAddressPool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PoolId: 地址池id
        :type PoolId: int
        :param _PoolName: 地址池名称，不允许重复
        :type PoolName: str
        :param _TrafficStrategy: 流量策略: WEIGHT负载均衡，ALl解析全部
        :type TrafficStrategy: str
        :param _MonitorId: 监控器id
        :type MonitorId: int
        :param _AddressSet: 地址列表
        :type AddressSet: list of Address
        """
        self._PoolId = None
        self._PoolName = None
        self._TrafficStrategy = None
        self._MonitorId = None
        self._AddressSet = None

    @property
    def PoolId(self):
        """地址池id
        :rtype: int
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def PoolName(self):
        """地址池名称，不允许重复
        :rtype: str
        """
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName

    @property
    def TrafficStrategy(self):
        """流量策略: WEIGHT负载均衡，ALl解析全部
        :rtype: str
        """
        return self._TrafficStrategy

    @TrafficStrategy.setter
    def TrafficStrategy(self, TrafficStrategy):
        self._TrafficStrategy = TrafficStrategy

    @property
    def MonitorId(self):
        """监控器id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def AddressSet(self):
        """地址列表
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._PoolName = params.get("PoolName")
        self._TrafficStrategy = params.get("TrafficStrategy")
        self._MonitorId = params.get("MonitorId")
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressPoolResponse(AbstractModel):
    """ModifyAddressPool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 是否修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """是否修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyInstanceConfigRequest(AbstractModel):
    """ModifyInstanceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceConfig: 实例配置详情
        :type InstanceConfig: :class:`tencentcloud.igtm.v20231024.models.InstanceConfig`
        """
        self._InstanceConfig = None

    @property
    def InstanceConfig(self):
        """实例配置详情
        :rtype: :class:`tencentcloud.igtm.v20231024.models.InstanceConfig`
        """
        return self._InstanceConfig

    @InstanceConfig.setter
    def InstanceConfig(self, InstanceConfig):
        self._InstanceConfig = InstanceConfig


    def _deserialize(self, params):
        if params.get("InstanceConfig") is not None:
            self._InstanceConfig = InstanceConfig()
            self._InstanceConfig._deserialize(params.get("InstanceConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceConfigResponse(AbstractModel):
    """ModifyInstanceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instance: 实例详情
        :type Instance: :class:`tencentcloud.igtm.v20231024.models.InstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instance = None
        self._RequestId = None

    @property
    def Instance(self):
        """实例详情
        :rtype: :class:`tencentcloud.igtm.v20231024.models.InstanceDetail`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

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
        if params.get("Instance") is not None:
            self._Instance = InstanceDetail()
            self._Instance._deserialize(params.get("Instance"))
        self._RequestId = params.get("RequestId")


class ModifyMonitorRequest(AbstractModel):
    """ModifyMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监控器id
        :type MonitorId: int
        :param _MonitorName: 监控器名称
        :type MonitorName: str
        :param _CheckProtocol: 检查协议，可选值 PING TCP HTTP HTTPS
        :type CheckProtocol: str
        :param _CheckInterval: 检查间隔（秒），可选值 15 60 120 300
        :type CheckInterval: int
        :param _Timeout: 超时时间，单位:秒，可选值 2  3  5  10
        :type Timeout: int
        :param _FailTimes: 重试次数，可选值为 0，1，2
        :type FailTimes: int
        :param _FailRate: 失败比例，可选值为 20 30 40 50 60 70 80 100，默认值为50
        :type FailRate: int
        :param _DetectorStyle: 监控节点类型，可选值有AUTO INTERNAL OVERSEAS IPV6 ALL
        :type DetectorStyle: str
        :param _DetectorGroupIds: 探测器组id列表
        :type DetectorGroupIds: list of int non-negative
        :param _PingNum: PING 包数目， 当CheckProtocol=ping时必填，可选值 20 50 100
        :type PingNum: int
        :param _TcpPort: 检查端口，可选值为1-65535之间的整数
        :type TcpPort: int
        :param _Host: Host 设置，默认为业务域名
        :type Host: str
        :param _Path: URL 路径，默认为“/”
        :type Path: str
        :param _ReturnCodeThreshold: 返回错误码阈值, 可选值为 400 和 500, 默认值500
        :type ReturnCodeThreshold: int
        :param _EnableRedirect: 跟随 3XX 重定向 ，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :type EnableRedirect: str
        :param _EnableSni: 启用 SNI，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :type EnableSni: str
        :param _PacketLossRate: 丢包率告警阈值，当CheckProtocol=ping时必填，取值在10 30 50 80 90 100
        :type PacketLossRate: int
        :param _ContinuePeriod: 持续周期数，可选值1-5
        :type ContinuePeriod: int
        """
        self._MonitorId = None
        self._MonitorName = None
        self._CheckProtocol = None
        self._CheckInterval = None
        self._Timeout = None
        self._FailTimes = None
        self._FailRate = None
        self._DetectorStyle = None
        self._DetectorGroupIds = None
        self._PingNum = None
        self._TcpPort = None
        self._Host = None
        self._Path = None
        self._ReturnCodeThreshold = None
        self._EnableRedirect = None
        self._EnableSni = None
        self._PacketLossRate = None
        self._ContinuePeriod = None

    @property
    def MonitorId(self):
        """监控器id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MonitorName(self):
        """监控器名称
        :rtype: str
        """
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def CheckProtocol(self):
        """检查协议，可选值 PING TCP HTTP HTTPS
        :rtype: str
        """
        return self._CheckProtocol

    @CheckProtocol.setter
    def CheckProtocol(self, CheckProtocol):
        self._CheckProtocol = CheckProtocol

    @property
    def CheckInterval(self):
        """检查间隔（秒），可选值 15 60 120 300
        :rtype: int
        """
        return self._CheckInterval

    @CheckInterval.setter
    def CheckInterval(self, CheckInterval):
        self._CheckInterval = CheckInterval

    @property
    def Timeout(self):
        """超时时间，单位:秒，可选值 2  3  5  10
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FailTimes(self):
        """重试次数，可选值为 0，1，2
        :rtype: int
        """
        return self._FailTimes

    @FailTimes.setter
    def FailTimes(self, FailTimes):
        self._FailTimes = FailTimes

    @property
    def FailRate(self):
        """失败比例，可选值为 20 30 40 50 60 70 80 100，默认值为50
        :rtype: int
        """
        return self._FailRate

    @FailRate.setter
    def FailRate(self, FailRate):
        self._FailRate = FailRate

    @property
    def DetectorStyle(self):
        """监控节点类型，可选值有AUTO INTERNAL OVERSEAS IPV6 ALL
        :rtype: str
        """
        return self._DetectorStyle

    @DetectorStyle.setter
    def DetectorStyle(self, DetectorStyle):
        self._DetectorStyle = DetectorStyle

    @property
    def DetectorGroupIds(self):
        """探测器组id列表
        :rtype: list of int non-negative
        """
        return self._DetectorGroupIds

    @DetectorGroupIds.setter
    def DetectorGroupIds(self, DetectorGroupIds):
        self._DetectorGroupIds = DetectorGroupIds

    @property
    def PingNum(self):
        """PING 包数目， 当CheckProtocol=ping时必填，可选值 20 50 100
        :rtype: int
        """
        return self._PingNum

    @PingNum.setter
    def PingNum(self, PingNum):
        self._PingNum = PingNum

    @property
    def TcpPort(self):
        """检查端口，可选值为1-65535之间的整数
        :rtype: int
        """
        return self._TcpPort

    @TcpPort.setter
    def TcpPort(self, TcpPort):
        self._TcpPort = TcpPort

    @property
    def Host(self):
        """Host 设置，默认为业务域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        """URL 路径，默认为“/”
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ReturnCodeThreshold(self):
        """返回错误码阈值, 可选值为 400 和 500, 默认值500
        :rtype: int
        """
        return self._ReturnCodeThreshold

    @ReturnCodeThreshold.setter
    def ReturnCodeThreshold(self, ReturnCodeThreshold):
        self._ReturnCodeThreshold = ReturnCodeThreshold

    @property
    def EnableRedirect(self):
        """跟随 3XX 重定向 ，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :rtype: str
        """
        return self._EnableRedirect

    @EnableRedirect.setter
    def EnableRedirect(self, EnableRedirect):
        self._EnableRedirect = EnableRedirect

    @property
    def EnableSni(self):
        """启用 SNI，不开启为 DISABLED， 开启为 ENABLED，默认不开启
        :rtype: str
        """
        return self._EnableSni

    @EnableSni.setter
    def EnableSni(self, EnableSni):
        self._EnableSni = EnableSni

    @property
    def PacketLossRate(self):
        """丢包率告警阈值，当CheckProtocol=ping时必填，取值在10 30 50 80 90 100
        :rtype: int
        """
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def ContinuePeriod(self):
        """持续周期数，可选值1-5
        :rtype: int
        """
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MonitorName = params.get("MonitorName")
        self._CheckProtocol = params.get("CheckProtocol")
        self._CheckInterval = params.get("CheckInterval")
        self._Timeout = params.get("Timeout")
        self._FailTimes = params.get("FailTimes")
        self._FailRate = params.get("FailRate")
        self._DetectorStyle = params.get("DetectorStyle")
        self._DetectorGroupIds = params.get("DetectorGroupIds")
        self._PingNum = params.get("PingNum")
        self._TcpPort = params.get("TcpPort")
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._ReturnCodeThreshold = params.get("ReturnCodeThreshold")
        self._EnableRedirect = params.get("EnableRedirect")
        self._EnableSni = params.get("EnableSni")
        self._PacketLossRate = params.get("PacketLossRate")
        self._ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMonitorResponse(AbstractModel):
    """ModifyMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: success 为修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """success 为修改成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyStrategyRequest(AbstractModel):
    """ModifyStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _StrategyId: 策略id
        :type StrategyId: int
        :param _Source: 解析线路，需要全量传参
        :type Source: list of Source
        :param _MainAddressPoolSet: 主力地址池集合，需要全量传参
        :type MainAddressPoolSet: list of MainAddressPool
        :param _FallbackAddressPoolSet: 兜底地址池集合，需要全量传参
        :type FallbackAddressPoolSet: list of MainAddressPool
        :param _StrategyName: 策略名称，不允许重复
        :type StrategyName: str
        :param _IsEnabled: 策略开启状态：ENABLED开启；DISABLED关闭
        :type IsEnabled: str
        :param _KeepDomainRecords: 是否开启策略强制保留默认线路 disabled, enabled，默认不开启且只有一个策略能开启
        :type KeepDomainRecords: str
        :param _SwitchPoolType: 调度模式：AUTO默认；STOP仅暂停不切换
        :type SwitchPoolType: str
        """
        self._InstanceId = None
        self._StrategyId = None
        self._Source = None
        self._MainAddressPoolSet = None
        self._FallbackAddressPoolSet = None
        self._StrategyName = None
        self._IsEnabled = None
        self._KeepDomainRecords = None
        self._SwitchPoolType = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyId(self):
        """策略id
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Source(self):
        """解析线路，需要全量传参
        :rtype: list of Source
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def MainAddressPoolSet(self):
        """主力地址池集合，需要全量传参
        :rtype: list of MainAddressPool
        """
        return self._MainAddressPoolSet

    @MainAddressPoolSet.setter
    def MainAddressPoolSet(self, MainAddressPoolSet):
        self._MainAddressPoolSet = MainAddressPoolSet

    @property
    def FallbackAddressPoolSet(self):
        """兜底地址池集合，需要全量传参
        :rtype: list of MainAddressPool
        """
        return self._FallbackAddressPoolSet

    @FallbackAddressPoolSet.setter
    def FallbackAddressPoolSet(self, FallbackAddressPoolSet):
        self._FallbackAddressPoolSet = FallbackAddressPoolSet

    @property
    def StrategyName(self):
        """策略名称，不允许重复
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def IsEnabled(self):
        """策略开启状态：ENABLED开启；DISABLED关闭
        :rtype: str
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def KeepDomainRecords(self):
        """是否开启策略强制保留默认线路 disabled, enabled，默认不开启且只有一个策略能开启
        :rtype: str
        """
        return self._KeepDomainRecords

    @KeepDomainRecords.setter
    def KeepDomainRecords(self, KeepDomainRecords):
        self._KeepDomainRecords = KeepDomainRecords

    @property
    def SwitchPoolType(self):
        """调度模式：AUTO默认；STOP仅暂停不切换
        :rtype: str
        """
        return self._SwitchPoolType

    @SwitchPoolType.setter
    def SwitchPoolType(self, SwitchPoolType):
        self._SwitchPoolType = SwitchPoolType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyId = params.get("StrategyId")
        if params.get("Source") is not None:
            self._Source = []
            for item in params.get("Source"):
                obj = Source()
                obj._deserialize(item)
                self._Source.append(obj)
        if params.get("MainAddressPoolSet") is not None:
            self._MainAddressPoolSet = []
            for item in params.get("MainAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._MainAddressPoolSet.append(obj)
        if params.get("FallbackAddressPoolSet") is not None:
            self._FallbackAddressPoolSet = []
            for item in params.get("FallbackAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._FallbackAddressPoolSet.append(obj)
        self._StrategyName = params.get("StrategyName")
        self._IsEnabled = params.get("IsEnabled")
        self._KeepDomainRecords = params.get("KeepDomainRecords")
        self._SwitchPoolType = params.get("SwitchPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStrategyResponse(AbstractModel):
    """ModifyStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class MonitorDetail(AbstractModel):
    """监控器详情

    """

    def __init__(self):
        r"""
        :param _MonitorId: 探测规则id
        :type MonitorId: int
        :param _MonitorName: 监控器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorName: str
        :param _Uin: 所属用户
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _DetectorGroupIds: 监控节点id组
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectorGroupIds: list of int non-negative
        :param _CheckProtocol: 探测协议 PING TCP HTTP HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckProtocol: str
        :param _CheckInterval: 探测周期
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckInterval: int
        :param _PingNum: 发包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PingNum: int
        :param _TcpPort: tcp端口
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpPort: int
        :param _Host: 探测 host
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Path: 探测路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _ReturnCodeThreshold: 返回值阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCodeThreshold: int
        :param _EnableRedirect: 是否开启3xx重定向跟随 ENABLED DISABLED
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRedirect: str
        :param _EnableSni: 是否启用 sni
ENABLED DISABLED
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableSni: str
        :param _PacketLossRate: 丢包率上限
注意：此字段可能返回 null，表示取不到有效值。
        :type PacketLossRate: int
        :param _Timeout: 探测超时
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _FailTimes: 失败次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailTimes: int
        :param _FailRate: 失败率上限100
注意：此字段可能返回 null，表示取不到有效值。
        :type FailRate: int
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        :param _DetectorStyle: 监控节点类型
AUTO INTERNAL OVERSEAS IPV6 ALL
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectorStyle: str
        :param _DetectNum: 探测次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectNum: int
        :param _ContinuePeriod: 持续周期数
注意：此字段可能返回 null，表示取不到有效值。
        :type ContinuePeriod: int
        """
        self._MonitorId = None
        self._MonitorName = None
        self._Uin = None
        self._DetectorGroupIds = None
        self._CheckProtocol = None
        self._CheckInterval = None
        self._PingNum = None
        self._TcpPort = None
        self._Host = None
        self._Path = None
        self._ReturnCodeThreshold = None
        self._EnableRedirect = None
        self._EnableSni = None
        self._PacketLossRate = None
        self._Timeout = None
        self._FailTimes = None
        self._FailRate = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._DetectorStyle = None
        self._DetectNum = None
        self._ContinuePeriod = None

    @property
    def MonitorId(self):
        """探测规则id
        :rtype: int
        """
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def MonitorName(self):
        """监控器名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MonitorName

    @MonitorName.setter
    def MonitorName(self, MonitorName):
        self._MonitorName = MonitorName

    @property
    def Uin(self):
        """所属用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DetectorGroupIds(self):
        """监控节点id组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._DetectorGroupIds

    @DetectorGroupIds.setter
    def DetectorGroupIds(self, DetectorGroupIds):
        self._DetectorGroupIds = DetectorGroupIds

    @property
    def CheckProtocol(self):
        """探测协议 PING TCP HTTP HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckProtocol

    @CheckProtocol.setter
    def CheckProtocol(self, CheckProtocol):
        self._CheckProtocol = CheckProtocol

    @property
    def CheckInterval(self):
        """探测周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CheckInterval

    @CheckInterval.setter
    def CheckInterval(self, CheckInterval):
        self._CheckInterval = CheckInterval

    @property
    def PingNum(self):
        """发包数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PingNum

    @PingNum.setter
    def PingNum(self, PingNum):
        self._PingNum = PingNum

    @property
    def TcpPort(self):
        """tcp端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TcpPort

    @TcpPort.setter
    def TcpPort(self, TcpPort):
        self._TcpPort = TcpPort

    @property
    def Host(self):
        """探测 host
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        """探测路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ReturnCodeThreshold(self):
        """返回值阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReturnCodeThreshold

    @ReturnCodeThreshold.setter
    def ReturnCodeThreshold(self, ReturnCodeThreshold):
        self._ReturnCodeThreshold = ReturnCodeThreshold

    @property
    def EnableRedirect(self):
        """是否开启3xx重定向跟随 ENABLED DISABLED
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnableRedirect

    @EnableRedirect.setter
    def EnableRedirect(self, EnableRedirect):
        self._EnableRedirect = EnableRedirect

    @property
    def EnableSni(self):
        """是否启用 sni
ENABLED DISABLED
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnableSni

    @EnableSni.setter
    def EnableSni(self, EnableSni):
        self._EnableSni = EnableSni

    @property
    def PacketLossRate(self):
        """丢包率上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def Timeout(self):
        """探测超时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FailTimes(self):
        """失败次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailTimes

    @FailTimes.setter
    def FailTimes(self, FailTimes):
        self._FailTimes = FailTimes

    @property
    def FailRate(self):
        """失败率上限100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailRate

    @FailRate.setter
    def FailRate(self, FailRate):
        self._FailRate = FailRate

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def DetectorStyle(self):
        """监控节点类型
AUTO INTERNAL OVERSEAS IPV6 ALL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DetectorStyle

    @DetectorStyle.setter
    def DetectorStyle(self, DetectorStyle):
        self._DetectorStyle = DetectorStyle

    @property
    def DetectNum(self):
        """探测次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DetectNum

    @DetectNum.setter
    def DetectNum(self, DetectNum):
        self._DetectNum = DetectNum

    @property
    def ContinuePeriod(self):
        """持续周期数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._MonitorName = params.get("MonitorName")
        self._Uin = params.get("Uin")
        self._DetectorGroupIds = params.get("DetectorGroupIds")
        self._CheckProtocol = params.get("CheckProtocol")
        self._CheckInterval = params.get("CheckInterval")
        self._PingNum = params.get("PingNum")
        self._TcpPort = params.get("TcpPort")
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._ReturnCodeThreshold = params.get("ReturnCodeThreshold")
        self._EnableRedirect = params.get("EnableRedirect")
        self._EnableSni = params.get("EnableSni")
        self._PacketLossRate = params.get("PacketLossRate")
        self._Timeout = params.get("Timeout")
        self._FailTimes = params.get("FailTimes")
        self._FailRate = params.get("FailRate")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._DetectorStyle = params.get("DetectorStyle")
        self._DetectNum = params.get("DetectNum")
        self._ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """配额

    """

    def __init__(self):
        r"""
        :param _TaskQuota: 探测任务配额
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskQuota: int
        :param _PoolQuota: 地址池配额
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolQuota: int
        :param _AddressQuota: 地址配额
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressQuota: int
        :param _MonitorQuota: 探点资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorQuota: int
        :param _MessageQuota: 消息资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageQuota: int
        :param _UsedTaskQuota: 已使用探测任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedTaskQuota: int
        :param _UsedFreeInstanceNum: 已使用体验实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedFreeInstanceNum: int
        :param _UsedBillInstanceNum: 已使用付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedBillInstanceNum: int
        :param _FreePackageNum: 体验套餐总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FreePackageNum: int
        :param _UsedBillPackageNum: 已使用付费套餐数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedBillPackageNum: int
        :param _BillPackageNum: 付费套餐总数
注意：此字段可能返回 null，表示取不到有效值。
        :type BillPackageNum: int
        """
        self._TaskQuota = None
        self._PoolQuota = None
        self._AddressQuota = None
        self._MonitorQuota = None
        self._MessageQuota = None
        self._UsedTaskQuota = None
        self._UsedFreeInstanceNum = None
        self._UsedBillInstanceNum = None
        self._FreePackageNum = None
        self._UsedBillPackageNum = None
        self._BillPackageNum = None

    @property
    def TaskQuota(self):
        """探测任务配额
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskQuota

    @TaskQuota.setter
    def TaskQuota(self, TaskQuota):
        self._TaskQuota = TaskQuota

    @property
    def PoolQuota(self):
        """地址池配额
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PoolQuota

    @PoolQuota.setter
    def PoolQuota(self, PoolQuota):
        self._PoolQuota = PoolQuota

    @property
    def AddressQuota(self):
        """地址配额
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AddressQuota

    @AddressQuota.setter
    def AddressQuota(self, AddressQuota):
        self._AddressQuota = AddressQuota

    @property
    def MonitorQuota(self):
        """探点资源数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorQuota

    @MonitorQuota.setter
    def MonitorQuota(self, MonitorQuota):
        self._MonitorQuota = MonitorQuota

    @property
    def MessageQuota(self):
        """消息资源数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageQuota

    @MessageQuota.setter
    def MessageQuota(self, MessageQuota):
        self._MessageQuota = MessageQuota

    @property
    def UsedTaskQuota(self):
        """已使用探测任务数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedTaskQuota

    @UsedTaskQuota.setter
    def UsedTaskQuota(self, UsedTaskQuota):
        self._UsedTaskQuota = UsedTaskQuota

    @property
    def UsedFreeInstanceNum(self):
        """已使用体验实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedFreeInstanceNum

    @UsedFreeInstanceNum.setter
    def UsedFreeInstanceNum(self, UsedFreeInstanceNum):
        self._UsedFreeInstanceNum = UsedFreeInstanceNum

    @property
    def UsedBillInstanceNum(self):
        """已使用付费实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedBillInstanceNum

    @UsedBillInstanceNum.setter
    def UsedBillInstanceNum(self, UsedBillInstanceNum):
        self._UsedBillInstanceNum = UsedBillInstanceNum

    @property
    def FreePackageNum(self):
        """体验套餐总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FreePackageNum

    @FreePackageNum.setter
    def FreePackageNum(self, FreePackageNum):
        self._FreePackageNum = FreePackageNum

    @property
    def UsedBillPackageNum(self):
        """已使用付费套餐数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedBillPackageNum

    @UsedBillPackageNum.setter
    def UsedBillPackageNum(self, UsedBillPackageNum):
        self._UsedBillPackageNum = UsedBillPackageNum

    @property
    def BillPackageNum(self):
        """付费套餐总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BillPackageNum

    @BillPackageNum.setter
    def BillPackageNum(self, BillPackageNum):
        self._BillPackageNum = BillPackageNum


    def _deserialize(self, params):
        self._TaskQuota = params.get("TaskQuota")
        self._PoolQuota = params.get("PoolQuota")
        self._AddressQuota = params.get("AddressQuota")
        self._MonitorQuota = params.get("MonitorQuota")
        self._MessageQuota = params.get("MessageQuota")
        self._UsedTaskQuota = params.get("UsedTaskQuota")
        self._UsedFreeInstanceNum = params.get("UsedFreeInstanceNum")
        self._UsedBillInstanceNum = params.get("UsedBillInstanceNum")
        self._FreePackageNum = params.get("FreePackageNum")
        self._UsedBillPackageNum = params.get("UsedBillPackageNum")
        self._BillPackageNum = params.get("BillPackageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFilter(AbstractModel):
    """查询时过滤条件。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名，支持的列表如下：
- type：主资源类型，CDN。
- instanceId：IGTM实例ID。此为必传参数，未传将导致接口查询失败。
        :type Name: str
        :param _Value: 过滤字段值。

        :type Value: list of str
        :param _Fuzzy: 是否启用模糊查询，仅支持过滤字段名为domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。(预留字段，暂未使用)
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        """过滤字段名，支持的列表如下：
- type：主资源类型，CDN。
- instanceId：IGTM实例ID。此为必传参数，未传将导致接口查询失败。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """过滤字段值。

        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        """是否启用模糊查询，仅支持过滤字段名为domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。(预留字段，暂未使用)
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Source(AbstractModel):
    """解析线路

    """

    def __init__(self):
        r"""
        :param _DnsLineId: 解析请求来源线路id
        :type DnsLineId: int
        :param _Name: 解析请求来源线路名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._DnsLineId = None
        self._Name = None

    @property
    def DnsLineId(self):
        """解析请求来源线路id
        :rtype: int
        """
        return self._DnsLineId

    @DnsLineId.setter
    def DnsLineId(self, DnsLineId):
        self._DnsLineId = DnsLineId

    @property
    def Name(self):
        """解析请求来源线路名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DnsLineId = params.get("DnsLineId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Strategy(AbstractModel):
    """地址池

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Name: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Source: 地址来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: list of Source
        :param _StrategyId: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _Status: 健康状态：ok健康、warn风险、down故障
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ActivateMainPoolId: 生效的主力池id，null则为未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivateMainPoolId: int
        :param _ActivateLevel: 当前生效地址池所在级数，为0则代表兜底生效，null则为未知
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivateLevel: int
        :param _ActivePoolType: 当前生效地址池集合类型：main主力；fallback兜底
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivePoolType: str
        :param _ActiveTrafficStrategy: 当前生效地址池流量策略：all解析所有；weight负载均衡
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTrafficStrategy: str
        :param _MonitorNum: 监控器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorNum: int
        :param _IsEnabled: 是否开启：ENABLED开启；DISABLED关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnabled: str
        :param _KeepDomainRecords: 是否保留线路：enabled保留，disabled不保留，只保留默认线路
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepDomainRecords: str
        :param _SwitchPoolType: 调度模式：AUTO默认；PAUSE仅暂停不切换
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchPoolType: str
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        """
        self._InstanceId = None
        self._Name = None
        self._Source = None
        self._StrategyId = None
        self._Status = None
        self._ActivateMainPoolId = None
        self._ActivateLevel = None
        self._ActivePoolType = None
        self._ActiveTrafficStrategy = None
        self._MonitorNum = None
        self._IsEnabled = None
        self._KeepDomainRecords = None
        self._SwitchPoolType = None
        self._CreatedOn = None
        self._UpdatedOn = None

    @property
    def InstanceId(self):
        """实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """策略名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        """地址来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Source
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def StrategyId(self):
        """策略id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Status(self):
        """健康状态：ok健康、warn风险、down故障
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActivateMainPoolId(self):
        """生效的主力池id，null则为未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActivateMainPoolId

    @ActivateMainPoolId.setter
    def ActivateMainPoolId(self, ActivateMainPoolId):
        self._ActivateMainPoolId = ActivateMainPoolId

    @property
    def ActivateLevel(self):
        """当前生效地址池所在级数，为0则代表兜底生效，null则为未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActivateLevel

    @ActivateLevel.setter
    def ActivateLevel(self, ActivateLevel):
        self._ActivateLevel = ActivateLevel

    @property
    def ActivePoolType(self):
        """当前生效地址池集合类型：main主力；fallback兜底
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActivePoolType

    @ActivePoolType.setter
    def ActivePoolType(self, ActivePoolType):
        self._ActivePoolType = ActivePoolType

    @property
    def ActiveTrafficStrategy(self):
        """当前生效地址池流量策略：all解析所有；weight负载均衡
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActiveTrafficStrategy

    @ActiveTrafficStrategy.setter
    def ActiveTrafficStrategy(self, ActiveTrafficStrategy):
        self._ActiveTrafficStrategy = ActiveTrafficStrategy

    @property
    def MonitorNum(self):
        """监控器数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MonitorNum

    @MonitorNum.setter
    def MonitorNum(self, MonitorNum):
        self._MonitorNum = MonitorNum

    @property
    def IsEnabled(self):
        """是否开启：ENABLED开启；DISABLED关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def KeepDomainRecords(self):
        """是否保留线路：enabled保留，disabled不保留，只保留默认线路
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeepDomainRecords

    @KeepDomainRecords.setter
    def KeepDomainRecords(self, KeepDomainRecords):
        self._KeepDomainRecords = KeepDomainRecords

    @property
    def SwitchPoolType(self):
        """调度模式：AUTO默认；PAUSE仅暂停不切换
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SwitchPoolType

    @SwitchPoolType.setter
    def SwitchPoolType(self, SwitchPoolType):
        self._SwitchPoolType = SwitchPoolType

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        if params.get("Source") is not None:
            self._Source = []
            for item in params.get("Source"):
                obj = Source()
                obj._deserialize(item)
                self._Source.append(obj)
        self._StrategyId = params.get("StrategyId")
        self._Status = params.get("Status")
        self._ActivateMainPoolId = params.get("ActivateMainPoolId")
        self._ActivateLevel = params.get("ActivateLevel")
        self._ActivePoolType = params.get("ActivePoolType")
        self._ActiveTrafficStrategy = params.get("ActiveTrafficStrategy")
        self._MonitorNum = params.get("MonitorNum")
        self._IsEnabled = params.get("IsEnabled")
        self._KeepDomainRecords = params.get("KeepDomainRecords")
        self._SwitchPoolType = params.get("SwitchPoolType")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyDetail(AbstractModel):
    """策略详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _StrategyId: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _Name: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Source: 线路
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: list of Source
        :param _MainAddressPoolSet: 主力地址池集合
注意：此字段可能返回 null，表示取不到有效值。
        :type MainAddressPoolSet: list of MainAddressPool
        :param _FallbackAddressPoolSet: 兜底地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :type FallbackAddressPoolSet: list of MainAddressPool
        :param _KeepDomainRecords: 是否保留线路：enabled保留，disabled不保留，只保留默认线路
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepDomainRecords: str
        :param _ActivateMainPoolId: 生效主力地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivateMainPoolId: int
        :param _CreatedOn: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: str
        :param _UpdatedOn: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: str
        :param _SwitchPoolType: 调度模式：AUTO默认；PAUSE仅暂停不切换
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchPoolType: str
        """
        self._InstanceId = None
        self._StrategyId = None
        self._Name = None
        self._Source = None
        self._MainAddressPoolSet = None
        self._FallbackAddressPoolSet = None
        self._KeepDomainRecords = None
        self._ActivateMainPoolId = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._SwitchPoolType = None

    @property
    def InstanceId(self):
        """实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StrategyId(self):
        """策略id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Name(self):
        """策略名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        """线路
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Source
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def MainAddressPoolSet(self):
        """主力地址池集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MainAddressPool
        """
        return self._MainAddressPoolSet

    @MainAddressPoolSet.setter
    def MainAddressPoolSet(self, MainAddressPoolSet):
        self._MainAddressPoolSet = MainAddressPoolSet

    @property
    def FallbackAddressPoolSet(self):
        """兜底地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MainAddressPool
        """
        return self._FallbackAddressPoolSet

    @FallbackAddressPoolSet.setter
    def FallbackAddressPoolSet(self, FallbackAddressPoolSet):
        self._FallbackAddressPoolSet = FallbackAddressPoolSet

    @property
    def KeepDomainRecords(self):
        """是否保留线路：enabled保留，disabled不保留，只保留默认线路
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeepDomainRecords

    @KeepDomainRecords.setter
    def KeepDomainRecords(self, KeepDomainRecords):
        self._KeepDomainRecords = KeepDomainRecords

    @property
    def ActivateMainPoolId(self):
        """生效主力地址池id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActivateMainPoolId

    @ActivateMainPoolId.setter
    def ActivateMainPoolId(self, ActivateMainPoolId):
        self._ActivateMainPoolId = ActivateMainPoolId

    @property
    def CreatedOn(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def SwitchPoolType(self):
        """调度模式：AUTO默认；PAUSE仅暂停不切换
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SwitchPoolType

    @SwitchPoolType.setter
    def SwitchPoolType(self, SwitchPoolType):
        self._SwitchPoolType = SwitchPoolType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StrategyId = params.get("StrategyId")
        self._Name = params.get("Name")
        if params.get("Source") is not None:
            self._Source = []
            for item in params.get("Source"):
                obj = Source()
                obj._deserialize(item)
                self._Source.append(obj)
        if params.get("MainAddressPoolSet") is not None:
            self._MainAddressPoolSet = []
            for item in params.get("MainAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._MainAddressPoolSet.append(obj)
        if params.get("FallbackAddressPoolSet") is not None:
            self._FallbackAddressPoolSet = []
            for item in params.get("FallbackAddressPoolSet"):
                obj = MainAddressPool()
                obj._deserialize(item)
                self._FallbackAddressPoolSet.append(obj)
        self._KeepDomainRecords = params.get("KeepDomainRecords")
        self._ActivateMainPoolId = params.get("ActivateMainPoolId")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._SwitchPoolType = params.get("SwitchPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        