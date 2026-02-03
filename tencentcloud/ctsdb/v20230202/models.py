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


class Cluster(AbstractModel):
    r"""实例相关信息

    """

    def __init__(self):
        r"""
        :param _AppID: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: int
        :param _ClusterID: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        :param _AccountID: 账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountID: str
        :param _Name: 自定义实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zones: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: str
        :param _Networks: 网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Networks: list of Network
        :param _Spec: 实例规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: :class:`tencentcloud.ctsdb.v20230202.models.Spec`
        :param _Status: 实例状态：0：运行中,1：创建中 ,16：变配中,17：隔离中,18：待销毁,19：恢复中,20：关机 , 21：销毁中 ,22：已销毁 
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Period: 实例有效期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: :class:`tencentcloud.ctsdb.v20230202.models.Period`
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _Tenant: 产品内部特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Tenant: :class:`tencentcloud.ctsdb.v20230202.models.Tenant`
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Security: 安全组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Security: list of str
        """
        self._AppID = None
        self._ClusterID = None
        self._AccountID = None
        self._Name = None
        self._Region = None
        self._Zones = None
        self._Networks = None
        self._Spec = None
        self._Status = None
        self._Period = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Tenant = None
        self._Tags = None
        self._Security = None

    @property
    def AppID(self):
        r"""用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ClusterID(self):
        r"""实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def AccountID(self):
        r"""账号id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountID

    @AccountID.setter
    def AccountID(self, AccountID):
        self._AccountID = AccountID

    @property
    def Name(self):
        r"""自定义实例名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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

    @property
    def Zones(self):
        r"""可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Networks(self):
        warnings.warn("parameter `Networks` is deprecated", DeprecationWarning) 

        r"""网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Network
        """
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        warnings.warn("parameter `Networks` is deprecated", DeprecationWarning) 

        self._Networks = Networks

    @property
    def Spec(self):
        warnings.warn("parameter `Spec` is deprecated", DeprecationWarning) 

        r"""实例规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Spec`
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        warnings.warn("parameter `Spec` is deprecated", DeprecationWarning) 

        self._Spec = Spec

    @property
    def Status(self):
        r"""实例状态：0：运行中,1：创建中 ,16：变配中,17：隔离中,18：待销毁,19：恢复中,20：关机 , 21：销毁中 ,22：已销毁 
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Period(self):
        r"""实例有效期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Period`
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def CreatedAt(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Tenant(self):
        r"""产品内部特性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Tenant`
        """
        return self._Tenant

    @Tenant.setter
    def Tenant(self, Tenant):
        self._Tenant = Tenant

    @property
    def Tags(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Security(self):
        r"""安全组信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Security

    @Security.setter
    def Security(self, Security):
        self._Security = Security


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._ClusterID = params.get("ClusterID")
        self._AccountID = params.get("AccountID")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._Zones = params.get("Zones")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        if params.get("Spec") is not None:
            self._Spec = Spec()
            self._Spec._deserialize(params.get("Spec"))
        self._Status = params.get("Status")
        if params.get("Period") is not None:
            self._Period = Period()
            self._Period._deserialize(params.get("Period"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Tenant") is not None:
            self._Tenant = Tenant()
            self._Tenant._deserialize(params.get("Tenant"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Security = params.get("Security")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterDetail(AbstractModel):
    r"""实例详情信息

    """

    def __init__(self):
        r"""
        :param _AppID: <p>用户APPID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: int
        :param _ClusterID: <p>实例id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        :param _AccountID: <p>账号id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountID: str
        :param _Name: <p>自定义实例名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Region: <p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Networks: <p>网络信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Networks: list of Network
        :param _Status: <p>实例状态</p>枚举值：<ul><li> 0： 运行中</li><li> 1： 创建中</li><li> 16： 变配中</li><li> 17： 隔离中</li><li> 18： 已隔离</li><li> 19： 恢复中</li><li> 20： 已关机</li><li> 21： 销毁中</li><li> 22： 已销毁</li><li> 30： 扩展节点添加中</li><li> 31： 扩展节点变配中</li><li> 32： 扩展节点删除中</li><li> 33： 扩展节点禁用中</li><li> 34： 扩展节点启用中</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: <p>最后修改时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _Tags: <p>标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Security: <p>安全组信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Security: list of str
        :param _Components: <p>组件信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of Component
        :param _ExpiredAt: <p>过期时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: str
        :param _RenewFlag: <p>续费标识</p>枚举值：<ul><li> 0： 默认</li><li> 1： 自动续费</li><li> 2： 不自动续费</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _ShutdownAt: <p>关机时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ShutdownAt: str
        :param _IsolatedAt: <p>隔离时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedAt: str
        :param _Type: <p>实例类型</p>枚举值：<ul><li> 0： 共享型</li><li> 1： 独享型</li><li> 2： 标准型</li></ul>
        :type Type: int
        """
        self._AppID = None
        self._ClusterID = None
        self._AccountID = None
        self._Name = None
        self._Region = None
        self._Networks = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Tags = None
        self._Security = None
        self._Components = None
        self._ExpiredAt = None
        self._RenewFlag = None
        self._ShutdownAt = None
        self._IsolatedAt = None
        self._Type = None

    @property
    def AppID(self):
        r"""<p>用户APPID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ClusterID(self):
        r"""<p>实例id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def AccountID(self):
        r"""<p>账号id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountID

    @AccountID.setter
    def AccountID(self, AccountID):
        self._AccountID = AccountID

    @property
    def Name(self):
        r"""<p>自定义实例名</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        r"""<p>地域</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Networks(self):
        r"""<p>网络信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Network
        """
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        self._Networks = Networks

    @property
    def Status(self):
        r"""<p>实例状态</p>枚举值：<ul><li> 0： 运行中</li><li> 1： 创建中</li><li> 16： 变配中</li><li> 17： 隔离中</li><li> 18： 已隔离</li><li> 19： 恢复中</li><li> 20： 已关机</li><li> 21： 销毁中</li><li> 22： 已销毁</li><li> 30： 扩展节点添加中</li><li> 31： 扩展节点变配中</li><li> 32： 扩展节点删除中</li><li> 33： 扩展节点禁用中</li><li> 34： 扩展节点启用中</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>最后修改时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Tags(self):
        r"""<p>标签</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Security(self):
        r"""<p>安全组信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Security

    @Security.setter
    def Security(self, Security):
        self._Security = Security

    @property
    def Components(self):
        r"""<p>组件信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Component
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def ExpiredAt(self):
        r"""<p>过期时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def RenewFlag(self):
        r"""<p>续费标识</p>枚举值：<ul><li> 0： 默认</li><li> 1： 自动续费</li><li> 2： 不自动续费</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ShutdownAt(self):
        r"""<p>关机时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShutdownAt

    @ShutdownAt.setter
    def ShutdownAt(self, ShutdownAt):
        self._ShutdownAt = ShutdownAt

    @property
    def IsolatedAt(self):
        r"""<p>隔离时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def Type(self):
        r"""<p>实例类型</p>枚举值：<ul><li> 0： 共享型</li><li> 1： 独享型</li><li> 2： 标准型</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._ClusterID = params.get("ClusterID")
        self._AccountID = params.get("AccountID")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Security = params.get("Security")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._ExpiredAt = params.get("ExpiredAt")
        self._RenewFlag = params.get("RenewFlag")
        self._ShutdownAt = params.get("ShutdownAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    r"""实例组件信息

    """

    def __init__(self):
        r"""
        :param _InstanceID: <p>所属实例id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param _Name: <p>名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: <p>组件类型</p>枚举值：<ul><li> gateway： 时序节点</li><li> database： 数据节点</li><li> gateway-worker： 扩展节点</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Cpu: <p>cpu</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: <p>内存</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Disk: <p>磁盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: int
        :param _Shards: <p>节点数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Shards: int
        :param _Replicas: <p>副本数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _Networks: <p>网络</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Networks: list of Network
        :param _State: <p>组件状态</p>枚举值：<ul><li> 0： 运行中</li><li> 1： 创建中</li><li> 2： 变配中</li><li> 3： 隔离中</li><li> 4： 已隔离</li><li> 5： 删除中</li><li> 6： 已删除</li><li> 7： 禁用中</li><li> 8： 已禁用</li><li> 9： 启用中</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _ID: <p>组件内部ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        """
        self._InstanceID = None
        self._Name = None
        self._Type = None
        self._Cpu = None
        self._Memory = None
        self._Disk = None
        self._Shards = None
        self._Replicas = None
        self._Networks = None
        self._State = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""<p>所属实例id</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""<p>名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>组件类型</p>枚举值：<ul><li> gateway： 时序节点</li><li> database： 数据节点</li><li> gateway-worker： 扩展节点</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Cpu(self):
        r"""<p>cpu</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""<p>内存</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        r"""<p>磁盘</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def Shards(self):
        r"""<p>节点数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def Replicas(self):
        r"""<p>副本数量</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Networks(self):
        r"""<p>网络</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Network
        """
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        self._Networks = Networks

    @property
    def State(self):
        r"""<p>组件状态</p>枚举值：<ul><li> 0： 运行中</li><li> 1： 创建中</li><li> 2： 变配中</li><li> 3： 隔离中</li><li> 4： 已隔离</li><li> 5： 删除中</li><li> 6： 已删除</li><li> 7： 禁用中</li><li> 8： 已禁用</li><li> 9： 启用中</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ID(self):
        r"""<p>组件内部ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._Shards = params.get("Shards")
        self._Replicas = params.get("Replicas")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        self._State = params.get("State")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    r"""数据库相关信息

    """

    def __init__(self):
        r"""
        :param _ClusterID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        :param _Name: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _CoolDownInDays: 降冷时间（天）
注意：此字段可能返回 null，表示取不到有效值。
        :type CoolDownInDays: int
        :param _RetentionInDays: 数据保留时间（天）
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionInDays: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Status: 状态：0: 资源初始化中， 1: 资源创建中， 2: 正常状态， 3: 资源删除中， 4: 资源已删除， 5: 资源禁用中， 6: 资源已禁用， 7: 资源异常，需要人工操作
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self._ClusterID = None
        self._Name = None
        self._CoolDownInDays = None
        self._RetentionInDays = None
        self._Remark = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def ClusterID(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def Name(self):
        r"""数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CoolDownInDays(self):
        r"""降冷时间（天）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CoolDownInDays

    @CoolDownInDays.setter
    def CoolDownInDays(self, CoolDownInDays):
        self._CoolDownInDays = CoolDownInDays

    @property
    def RetentionInDays(self):
        r"""数据保留时间（天）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetentionInDays

    @RetentionInDays.setter
    def RetentionInDays(self, RetentionInDays):
        self._RetentionInDays = RetentionInDays

    @property
    def Remark(self):
        r"""备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        r"""状态：0: 资源初始化中， 1: 资源创建中， 2: 正常状态， 3: 资源删除中， 4: 资源已删除， 5: 资源禁用中， 6: 资源已禁用， 7: 资源异常，需要人工操作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._Name = params.get("Name")
        self._CoolDownInDays = params.get("CoolDownInDays")
        self._RetentionInDays = params.get("RetentionInDays")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailRequest(AbstractModel):
    r"""DescribeClusterDetail请求参数结构体

    """


class DescribeClusterDetailResponse(AbstractModel):
    r"""DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cluster: <p>实例详情</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: :class:`tencentcloud.ctsdb.v20230202.models.ClusterDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cluster = None
        self._RequestId = None

    @property
    def Cluster(self):
        r"""<p>实例详情</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.ClusterDetail`
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

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
        if params.get("Cluster") is not None:
            self._Cluster = ClusterDetail()
            self._Cluster._deserialize(params.get("Cluster"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    r"""DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页数	
        :type PageNumber: int
        :param _PageSize: 单页大小
        :type PageSize: int
        :param _Filters: 查询参数：支持通过实例ID（cluster_id）和实例名称（name）进行过滤查询
        :type Filters: list of Filter
        :param _Orders: 排序参数：支持通过创建时间字段（created_at）进行排序，Type可指定为DESC（降序）或ASC（升序）
        :type Orders: list of Order
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None
        self._Orders = None

    @property
    def PageNumber(self):
        r"""当前页数	
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""单页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""查询参数：支持通过实例ID（cluster_id）和实例名称（name）进行过滤查询
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Orders(self):
        r"""排序参数：支持通过创建时间字段（created_at）进行排序，Type可指定为DESC（降序）或ASC（升序）
        :rtype: list of Order
        """
        return self._Orders

    @Orders.setter
    def Orders(self, Orders):
        self._Orders = Orders


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Orders") is not None:
            self._Orders = []
            for item in params.get("Orders"):
                obj = Order()
                obj._deserialize(item)
                self._Orders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    r"""DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 当前条件下的总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Clusters: 符合条件的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Clusters: list of Cluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Clusters = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""当前条件下的总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Clusters(self):
        r"""符合条件的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Cluster
        """
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters

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
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = Cluster()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Database: 数据库参数
        :type Database: :class:`tencentcloud.ctsdb.v20230202.models.Database`
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _PageNumber: 分页页面
        :type PageNumber: int
        """
        self._Database = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Database(self):
        r"""数据库参数
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Database`
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""分页页面
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Database") is not None:
            self._Database = Database()
            self._Database._deserialize(params.get("Database"))
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    r"""DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Databases: 数据库列表
        :type Databases: list of Database
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Databases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Databases(self):
        r"""数据库列表
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def TotalCount(self):
        r"""数量
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
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤参数
        :type Name: str
        :param _Op: 过滤表达式
        :type Op: str
        :param _Values: 参与过滤的值
        :type Values: list of str
        """
        self._Name = None
        self._Op = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤参数
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Op(self):
        r"""过滤表达式
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def Values(self):
        r"""参与过滤的值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Op = params.get("Op")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Network(AbstractModel):
    r"""实例网络信息(influxdb)

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: vpc subnet id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _VIP: vpc ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VIP: str
        :param _Port: vpc port地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._VIP = None
        self._Port = None

    @property
    def VpcId(self):
        r"""vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""vpc subnet id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VIP(self):
        r"""vpc ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def Port(self):
        r"""vpc port地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VIP = params.get("VIP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    r"""排序参数，用于排序查询结果

    """

    def __init__(self):
        r"""
        :param _Name: 排序字段
        :type Name: str
        :param _Type: 排序方式
        :type Type: str
        """
        self._Name = None
        self._Type = None

    @property
    def Name(self):
        r"""排序字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""排序方式
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Period(AbstractModel):
    r"""有效期

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
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
        


class Spec(AbstractModel):
    r"""实例规格信息(influxdb)

    """

    def __init__(self):
        r"""
        :param _PayMode: 1：包年包月、2：按小时计费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _RequestUnit: 请求单元，为0则表示走资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestUnit: int
        :param _CpuLimit: CPU 核数最大限制
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: float
        :param _MemoryLimit: 内存 最大限制(Gi)
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLimit: float
        :param _DiskLimit: 磁盘 最大限制(Gi)
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskLimit: int
        :param _Shards: 业务分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type Shards: int
        :param _Replicas: 业务节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        """
        self._PayMode = None
        self._RequestUnit = None
        self._CpuLimit = None
        self._MemoryLimit = None
        self._DiskLimit = None
        self._Shards = None
        self._Replicas = None

    @property
    def PayMode(self):
        r"""1：包年包月、2：按小时计费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RequestUnit(self):
        r"""请求单元，为0则表示走资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RequestUnit

    @RequestUnit.setter
    def RequestUnit(self, RequestUnit):
        self._RequestUnit = RequestUnit

    @property
    def CpuLimit(self):
        r"""CPU 核数最大限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CpuLimit

    @CpuLimit.setter
    def CpuLimit(self, CpuLimit):
        self._CpuLimit = CpuLimit

    @property
    def MemoryLimit(self):
        r"""内存 最大限制(Gi)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def DiskLimit(self):
        r"""磁盘 最大限制(Gi)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskLimit

    @DiskLimit.setter
    def DiskLimit(self, DiskLimit):
        self._DiskLimit = DiskLimit

    @property
    def Shards(self):
        r"""业务分片数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def Replicas(self):
        r"""业务节点数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._RequestUnit = params.get("RequestUnit")
        self._CpuLimit = params.get("CpuLimit")
        self._MemoryLimit = params.get("MemoryLimit")
        self._DiskLimit = params.get("DiskLimit")
        self._Shards = params.get("Shards")
        self._Replicas = params.get("Replicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Key: 键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class Tenant(AbstractModel):
    r"""产品内部特性

    """

    def __init__(self):
        r"""
        :param _IsPasswordEncrypted: 密码是否已加密
        :type IsPasswordEncrypted: bool
        """
        self._IsPasswordEncrypted = None

    @property
    def IsPasswordEncrypted(self):
        r"""密码是否已加密
        :rtype: bool
        """
        return self._IsPasswordEncrypted

    @IsPasswordEncrypted.setter
    def IsPasswordEncrypted(self, IsPasswordEncrypted):
        self._IsPasswordEncrypted = IsPasswordEncrypted


    def _deserialize(self, params):
        self._IsPasswordEncrypted = params.get("IsPasswordEncrypted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        