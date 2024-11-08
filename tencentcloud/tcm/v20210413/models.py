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


class APM(AbstractModel):
    """腾讯云应用性能管理服务参数

    """

    def __init__(self):
        r"""
        :param _Enable: 是否启用
        :type Enable: bool
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _InstanceId: APM 实例，如果创建时传入的参数为空，则表示自动创建 APM 实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _NeedDelete: 是否要删除APM实例
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedDelete: bool
        """
        self._Enable = None
        self._Region = None
        self._InstanceId = None
        self._NeedDelete = None

    @property
    def Enable(self):
        """是否启用
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        """APM 实例，如果创建时传入的参数为空，则表示自动创建 APM 实例。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NeedDelete(self):
        """是否要删除APM实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NeedDelete

    @NeedDelete.setter
    def NeedDelete(self, NeedDelete):
        self._NeedDelete = NeedDelete


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._NeedDelete = params.get("NeedDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogConfig(AbstractModel):
    """AccessLog 配置

    """

    def __init__(self):
        r"""
        :param _Enable: 是否启用
        :type Enable: bool
        :param _Template: 采用的模板，可选值：istio（默认）、trace
        :type Template: str
        :param _SelectedRange: 选中的范围
        :type SelectedRange: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        :param _CLS: 腾讯云日志服务相关参数
        :type CLS: :class:`tencentcloud.tcm.v20210413.models.CLS`
        :param _Encoding: 编码格式，可选值：TEXT、JSON
        :type Encoding: str
        :param _Format: 日志格式
        :type Format: str
        :param _Address: GRPC第三方服务器地址
        :type Address: str
        :param _EnableServer: 是否启用GRPC第三方服务器
        :type EnableServer: bool
        :param _EnableStdout: 是否启用标准输出
        :type EnableStdout: bool
        """
        self._Enable = None
        self._Template = None
        self._SelectedRange = None
        self._CLS = None
        self._Encoding = None
        self._Format = None
        self._Address = None
        self._EnableServer = None
        self._EnableStdout = None

    @property
    def Enable(self):
        """是否启用
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Template(self):
        """采用的模板，可选值：istio（默认）、trace
        :rtype: str
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def SelectedRange(self):
        """选中的范围
        :rtype: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        """
        return self._SelectedRange

    @SelectedRange.setter
    def SelectedRange(self, SelectedRange):
        self._SelectedRange = SelectedRange

    @property
    def CLS(self):
        """腾讯云日志服务相关参数
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CLS`
        """
        return self._CLS

    @CLS.setter
    def CLS(self, CLS):
        self._CLS = CLS

    @property
    def Encoding(self):
        """编码格式，可选值：TEXT、JSON
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Format(self):
        """日志格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Address(self):
        """GRPC第三方服务器地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def EnableServer(self):
        """是否启用GRPC第三方服务器
        :rtype: bool
        """
        return self._EnableServer

    @EnableServer.setter
    def EnableServer(self, EnableServer):
        self._EnableServer = EnableServer

    @property
    def EnableStdout(self):
        """是否启用标准输出
        :rtype: bool
        """
        return self._EnableStdout

    @EnableStdout.setter
    def EnableStdout(self, EnableStdout):
        self._EnableStdout = EnableStdout


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Template = params.get("Template")
        if params.get("SelectedRange") is not None:
            self._SelectedRange = SelectedRange()
            self._SelectedRange._deserialize(params.get("SelectedRange"))
        if params.get("CLS") is not None:
            self._CLS = CLS()
            self._CLS._deserialize(params.get("CLS"))
        self._Encoding = params.get("Encoding")
        self._Format = params.get("Format")
        self._Address = params.get("Address")
        self._EnableServer = params.get("EnableServer")
        self._EnableStdout = params.get("EnableStdout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveOperation(AbstractModel):
    """正在执行的异步操作

    """

    def __init__(self):
        r"""
        :param _OperationId: 操作Id
        :type OperationId: str
        :param _Type: 操作类型，取值范围：
- LINK_CLUSTERS: 关联集群
- RELINK_CLUSTERS: 重新关联集群
- UNLINK_CLUSTERS: 解关联集群
- INSTALL_MESH: 安装网格
        :type Type: str
        """
        self._OperationId = None
        self._Type = None

    @property
    def OperationId(self):
        """操作Id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Type(self):
        """操作类型，取值范围：
- LINK_CLUSTERS: 关联集群
- RELINK_CLUSTERS: 重新关联集群
- UNLINK_CLUSTERS: 解关联集群
- INSTALL_MESH: 安装网格
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._OperationId = params.get("OperationId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoInjectionNamespaceState(AbstractModel):
    """描述某一网格在特定命名空间下的自动注入状态

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _State: 注入状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        """
        self._Namespace = None
        self._State = None

    @property
    def Namespace(self):
        """命名空间名称
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def State(self):
        """注入状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLS(AbstractModel):
    """腾讯云日志服务相关参数

    """

    def __init__(self):
        r"""
        :param _Enable: 是否启用
        :type Enable: bool
        :param _LogSet: 日志集
        :type LogSet: str
        :param _Topic: 日志主题
        :type Topic: str
        :param _NeedDelete: 是否删除
        :type NeedDelete: bool
        :param _Region: cls 主题创建的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Enable = None
        self._LogSet = None
        self._Topic = None
        self._NeedDelete = None
        self._Region = None

    @property
    def Enable(self):
        """是否启用
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def LogSet(self):
        """日志集
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def Topic(self):
        """日志主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def NeedDelete(self):
        """是否删除
        :rtype: bool
        """
        return self._NeedDelete

    @NeedDelete.setter
    def NeedDelete(self, NeedDelete):
        self._NeedDelete = NeedDelete

    @property
    def Region(self):
        """cls 主题创建的地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._LogSet = params.get("LogSet")
        self._Topic = params.get("Topic")
        self._NeedDelete = params.get("NeedDelete")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cluster(AbstractModel):
    """Mesh集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: str
        :param _Region: 地域
        :type Region: str
        :param _Role: 集群角色，取值范围：
- MASTER：控制面所在的主集群
- REMOTE：主集群管理的远端集群
        :type Role: str
        :param _VpcId: 私有网络Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _DisplayName: 名称，只读
        :type DisplayName: str
        :param _State: 状态，只读
        :type State: str
        :param _LinkedTime: 关联时间，只读
        :type LinkedTime: str
        :param _Config: 集群配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.ClusterConfig`
        :param _Status: 详细状态，只读
        :type Status: :class:`tencentcloud.tcm.v20210413.models.ClusterStatus`
        :param _Type: 类型，取值范围：
- TKE
- EKS
        :type Type: str
        :param _HostedNamespaces: 集群关联的 Namespace 列表
        :type HostedNamespaces: list of str
        """
        self._ClusterId = None
        self._Region = None
        self._Role = None
        self._VpcId = None
        self._SubnetId = None
        self._DisplayName = None
        self._State = None
        self._LinkedTime = None
        self._Config = None
        self._Status = None
        self._Type = None
        self._HostedNamespaces = None

    @property
    def ClusterId(self):
        """集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Role(self):
        """集群角色，取值范围：
- MASTER：控制面所在的主集群
- REMOTE：主集群管理的远端集群
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def VpcId(self):
        """私有网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DisplayName(self):
        """名称，只读
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def State(self):
        """状态，只读
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def LinkedTime(self):
        """关联时间，只读
        :rtype: str
        """
        return self._LinkedTime

    @LinkedTime.setter
    def LinkedTime(self, LinkedTime):
        self._LinkedTime = LinkedTime

    @property
    def Config(self):
        """集群配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ClusterConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """详细状态，只读
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ClusterStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """类型，取值范围：
- TKE
- EKS
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostedNamespaces(self):
        """集群关联的 Namespace 列表
        :rtype: list of str
        """
        return self._HostedNamespaces

    @HostedNamespaces.setter
    def HostedNamespaces(self, HostedNamespaces):
        self._HostedNamespaces = HostedNamespaces


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._Role = params.get("Role")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DisplayName = params.get("DisplayName")
        self._State = params.get("State")
        self._LinkedTime = params.get("LinkedTime")
        if params.get("Config") is not None:
            self._Config = ClusterConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("Status") is not None:
            self._Status = ClusterStatus()
            self._Status._deserialize(params.get("Status"))
        self._Type = params.get("Type")
        self._HostedNamespaces = params.get("HostedNamespaces")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfig(AbstractModel):
    """集群配置

    """

    def __init__(self):
        r"""
        :param _AutoInjectionNamespaceList: 自动注入SideCar的NameSpace
        :type AutoInjectionNamespaceList: list of str
        :param _IngressGatewayList: Ingress配置列表
        :type IngressGatewayList: list of IngressGateway
        :param _EgressGatewayList: Egress配置列表
        :type EgressGatewayList: list of EgressGateway
        :param _Istiod: Istiod配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Istiod: :class:`tencentcloud.tcm.v20210413.models.IstiodConfig`
        :param _DeployConfig: 部署配置
        :type DeployConfig: :class:`tencentcloud.tcm.v20210413.models.DeployConfig`
        :param _AutoInjectionNamespaceStateList: 自动注入命名空间状态列表
        :type AutoInjectionNamespaceStateList: list of AutoInjectionNamespaceState
        """
        self._AutoInjectionNamespaceList = None
        self._IngressGatewayList = None
        self._EgressGatewayList = None
        self._Istiod = None
        self._DeployConfig = None
        self._AutoInjectionNamespaceStateList = None

    @property
    def AutoInjectionNamespaceList(self):
        """自动注入SideCar的NameSpace
        :rtype: list of str
        """
        return self._AutoInjectionNamespaceList

    @AutoInjectionNamespaceList.setter
    def AutoInjectionNamespaceList(self, AutoInjectionNamespaceList):
        self._AutoInjectionNamespaceList = AutoInjectionNamespaceList

    @property
    def IngressGatewayList(self):
        """Ingress配置列表
        :rtype: list of IngressGateway
        """
        return self._IngressGatewayList

    @IngressGatewayList.setter
    def IngressGatewayList(self, IngressGatewayList):
        self._IngressGatewayList = IngressGatewayList

    @property
    def EgressGatewayList(self):
        """Egress配置列表
        :rtype: list of EgressGateway
        """
        return self._EgressGatewayList

    @EgressGatewayList.setter
    def EgressGatewayList(self, EgressGatewayList):
        self._EgressGatewayList = EgressGatewayList

    @property
    def Istiod(self):
        """Istiod配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.IstiodConfig`
        """
        return self._Istiod

    @Istiod.setter
    def Istiod(self, Istiod):
        self._Istiod = Istiod

    @property
    def DeployConfig(self):
        """部署配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.DeployConfig`
        """
        return self._DeployConfig

    @DeployConfig.setter
    def DeployConfig(self, DeployConfig):
        self._DeployConfig = DeployConfig

    @property
    def AutoInjectionNamespaceStateList(self):
        """自动注入命名空间状态列表
        :rtype: list of AutoInjectionNamespaceState
        """
        return self._AutoInjectionNamespaceStateList

    @AutoInjectionNamespaceStateList.setter
    def AutoInjectionNamespaceStateList(self, AutoInjectionNamespaceStateList):
        self._AutoInjectionNamespaceStateList = AutoInjectionNamespaceStateList


    def _deserialize(self, params):
        self._AutoInjectionNamespaceList = params.get("AutoInjectionNamespaceList")
        if params.get("IngressGatewayList") is not None:
            self._IngressGatewayList = []
            for item in params.get("IngressGatewayList"):
                obj = IngressGateway()
                obj._deserialize(item)
                self._IngressGatewayList.append(obj)
        if params.get("EgressGatewayList") is not None:
            self._EgressGatewayList = []
            for item in params.get("EgressGatewayList"):
                obj = EgressGateway()
                obj._deserialize(item)
                self._EgressGatewayList.append(obj)
        if params.get("Istiod") is not None:
            self._Istiod = IstiodConfig()
            self._Istiod._deserialize(params.get("Istiod"))
        if params.get("DeployConfig") is not None:
            self._DeployConfig = DeployConfig()
            self._DeployConfig._deserialize(params.get("DeployConfig"))
        if params.get("AutoInjectionNamespaceStateList") is not None:
            self._AutoInjectionNamespaceStateList = []
            for item in params.get("AutoInjectionNamespaceStateList"):
                obj = AutoInjectionNamespaceState()
                obj._deserialize(item)
                self._AutoInjectionNamespaceStateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterStatus(AbstractModel):
    """集群状态

    """

    def __init__(self):
        r"""
        :param _LinkState: 关联状态，取值范围：
- LINKING: 关联中
- LINKED: 已关联
- UNLINKING: 解关联中
- LINK_FAILED: 关联失败
- UNLINK_FAILED: 解关联失败
        :type LinkState: str
        :param _LinkErrorDetail: 关联错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkErrorDetail: str
        """
        self._LinkState = None
        self._LinkErrorDetail = None

    @property
    def LinkState(self):
        """关联状态，取值范围：
- LINKING: 关联中
- LINKED: 已关联
- UNLINKING: 解关联中
- LINK_FAILED: 关联失败
- UNLINK_FAILED: 解关联失败
        :rtype: str
        """
        return self._LinkState

    @LinkState.setter
    def LinkState(self, LinkState):
        self._LinkState = LinkState

    @property
    def LinkErrorDetail(self):
        """关联错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LinkErrorDetail

    @LinkErrorDetail.setter
    def LinkErrorDetail(self, LinkErrorDetail):
        self._LinkErrorDetail = LinkErrorDetail


    def _deserialize(self, params):
        self._LinkState = params.get("LinkState")
        self._LinkErrorDetail = params.get("LinkErrorDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMeshRequest(AbstractModel):
    """CreateMesh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: Mesh名称
        :type DisplayName: str
        :param _MeshVersion: Mesh版本
        :type MeshVersion: str
        :param _Type: Mesh类型，取值范围：
- HOSTED：托管网格
        :type Type: str
        :param _Config: Mesh配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        :param _ClusterList: 关联集群
        :type ClusterList: list of Cluster
        :param _TagList: 标签列表
        :type TagList: list of Tag
        """
        self._DisplayName = None
        self._MeshVersion = None
        self._Type = None
        self._Config = None
        self._ClusterList = None
        self._TagList = None

    @property
    def DisplayName(self):
        """Mesh名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def MeshVersion(self):
        """Mesh版本
        :rtype: str
        """
        return self._MeshVersion

    @MeshVersion.setter
    def MeshVersion(self, MeshVersion):
        self._MeshVersion = MeshVersion

    @property
    def Type(self):
        """Mesh类型，取值范围：
- HOSTED：托管网格
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        """Mesh配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ClusterList(self):
        """关联集群
        :rtype: list of Cluster
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TagList(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._MeshVersion = params.get("MeshVersion")
        self._Type = params.get("Type")
        if params.get("Config") is not None:
            self._Config = MeshConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterList.append(obj)
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
        


class CreateMeshResponse(AbstractModel):
    """CreateMesh返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 创建的Mesh的Id
        :type MeshId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MeshId = None
        self._RequestId = None

    @property
    def MeshId(self):
        """创建的Mesh的Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

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
        self._MeshId = params.get("MeshId")
        self._RequestId = params.get("RequestId")


class CrossRegionConfig(AbstractModel):
    """负载均衡跨域设置

    """


class CustomPromConfig(AbstractModel):
    """第三方 Prometheus 配置参数

    """

    def __init__(self):
        r"""
        :param _Url: Prometheus 访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _AuthType: 认证方式
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _IsPublicAddr: 是否公网地址，缺省为 false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublicAddr: bool
        :param _VpcId: 虚拟网络id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Username: Prometheus 用户名（用于 basic 认证方式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Password: Prometheus 密码（用于 basic 认证方式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self._Url = None
        self._AuthType = None
        self._IsPublicAddr = None
        self._VpcId = None
        self._Username = None
        self._Password = None

    @property
    def Url(self):
        """Prometheus 访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AuthType(self):
        """认证方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def IsPublicAddr(self):
        """是否公网地址，缺省为 false
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsPublicAddr

    @IsPublicAddr.setter
    def IsPublicAddr(self, IsPublicAddr):
        self._IsPublicAddr = IsPublicAddr

    @property
    def VpcId(self):
        """虚拟网络id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Username(self):
        """Prometheus 用户名（用于 basic 认证方式）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """Prometheus 密码（用于 basic 认证方式）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._AuthType = params.get("AuthType")
        self._IsPublicAddr = params.get("IsPublicAddr")
        self._VpcId = params.get("VpcId")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMeshRequest(AbstractModel):
    """DeleteMesh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 需要删除的MeshId
        :type MeshId: str
        :param _NeedDeleteCLS: CLS组件是否被删除
        :type NeedDeleteCLS: bool
        :param _NeedDeleteTMP: TMP组件是否被删除
        :type NeedDeleteTMP: bool
        :param _NeedDeleteAPM: APM组件是否被删除
        :type NeedDeleteAPM: bool
        :param _NeedDeleteGrafana: Grafana组件是否被删除
        :type NeedDeleteGrafana: bool
        """
        self._MeshId = None
        self._NeedDeleteCLS = None
        self._NeedDeleteTMP = None
        self._NeedDeleteAPM = None
        self._NeedDeleteGrafana = None

    @property
    def MeshId(self):
        """需要删除的MeshId
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def NeedDeleteCLS(self):
        """CLS组件是否被删除
        :rtype: bool
        """
        return self._NeedDeleteCLS

    @NeedDeleteCLS.setter
    def NeedDeleteCLS(self, NeedDeleteCLS):
        self._NeedDeleteCLS = NeedDeleteCLS

    @property
    def NeedDeleteTMP(self):
        """TMP组件是否被删除
        :rtype: bool
        """
        return self._NeedDeleteTMP

    @NeedDeleteTMP.setter
    def NeedDeleteTMP(self, NeedDeleteTMP):
        self._NeedDeleteTMP = NeedDeleteTMP

    @property
    def NeedDeleteAPM(self):
        """APM组件是否被删除
        :rtype: bool
        """
        return self._NeedDeleteAPM

    @NeedDeleteAPM.setter
    def NeedDeleteAPM(self, NeedDeleteAPM):
        self._NeedDeleteAPM = NeedDeleteAPM

    @property
    def NeedDeleteGrafana(self):
        """Grafana组件是否被删除
        :rtype: bool
        """
        return self._NeedDeleteGrafana

    @NeedDeleteGrafana.setter
    def NeedDeleteGrafana(self, NeedDeleteGrafana):
        self._NeedDeleteGrafana = NeedDeleteGrafana


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        self._NeedDeleteCLS = params.get("NeedDeleteCLS")
        self._NeedDeleteTMP = params.get("NeedDeleteTMP")
        self._NeedDeleteAPM = params.get("NeedDeleteAPM")
        self._NeedDeleteGrafana = params.get("NeedDeleteGrafana")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMeshResponse(AbstractModel):
    """DeleteMesh返回参数结构体

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


class DeployConfig(AbstractModel):
    """部署配置

    """

    def __init__(self):
        r"""
        :param _NodeSelectType: 部署类型，取值范围：
- SPECIFIC：专有模式
- AUTO：普通模式
        :type NodeSelectType: str
        :param _Nodes: 指定的节点
        :type Nodes: list of str
        """
        self._NodeSelectType = None
        self._Nodes = None

    @property
    def NodeSelectType(self):
        """部署类型，取值范围：
- SPECIFIC：专有模式
- AUTO：普通模式
        :rtype: str
        """
        return self._NodeSelectType

    @NodeSelectType.setter
    def NodeSelectType(self, NodeSelectType):
        self._NodeSelectType = NodeSelectType

    @property
    def Nodes(self):
        """指定的节点
        :rtype: list of str
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes


    def _deserialize(self, params):
        self._NodeSelectType = params.get("NodeSelectType")
        self._Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessLogConfigRequest(AbstractModel):
    """DescribeAccessLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: mesh名字
        :type MeshId: str
        """
        self._MeshId = None

    @property
    def MeshId(self):
        """mesh名字
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessLogConfigResponse(AbstractModel):
    """DescribeAccessLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _File: 访问日志输出路径。默认 /dev/stdout
        :type File: str
        :param _Format: 访问日志的格式。
        :type Format: str
        :param _Encoding: 访问日志输出编码，可取值为 "TEXT" 或 "JSON"，默认 TEXT"
        :type Encoding: str
        :param _SelectedRange: 选中的范围
注意：此字段可能返回 null，表示取不到有效值。
        :type SelectedRange: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        :param _Template: 采用的模板，可取值为"istio" 或 "trace"，默认为"istio"
        :type Template: str
        :param _CLS: 腾讯云日志服务相关参数
        :type CLS: :class:`tencentcloud.tcm.v20210413.models.CLS`
        :param _Address: GRPC第三方服务器地址
        :type Address: str
        :param _EnableServer: 是否启用GRPC第三方服务器
        :type EnableServer: bool
        :param _EnableStdout: 是否启用标准输出
        :type EnableStdout: bool
        :param _Enable: 是否启用访问日志采集
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._File = None
        self._Format = None
        self._Encoding = None
        self._SelectedRange = None
        self._Template = None
        self._CLS = None
        self._Address = None
        self._EnableServer = None
        self._EnableStdout = None
        self._Enable = None
        self._RequestId = None

    @property
    def File(self):
        """访问日志输出路径。默认 /dev/stdout
        :rtype: str
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File

    @property
    def Format(self):
        """访问日志的格式。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Encoding(self):
        """访问日志输出编码，可取值为 "TEXT" 或 "JSON"，默认 TEXT"
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def SelectedRange(self):
        """选中的范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        """
        return self._SelectedRange

    @SelectedRange.setter
    def SelectedRange(self, SelectedRange):
        self._SelectedRange = SelectedRange

    @property
    def Template(self):
        """采用的模板，可取值为"istio" 或 "trace"，默认为"istio"
        :rtype: str
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def CLS(self):
        """腾讯云日志服务相关参数
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CLS`
        """
        return self._CLS

    @CLS.setter
    def CLS(self, CLS):
        self._CLS = CLS

    @property
    def Address(self):
        """GRPC第三方服务器地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def EnableServer(self):
        """是否启用GRPC第三方服务器
        :rtype: bool
        """
        return self._EnableServer

    @EnableServer.setter
    def EnableServer(self, EnableServer):
        self._EnableServer = EnableServer

    @property
    def EnableStdout(self):
        """是否启用标准输出
        :rtype: bool
        """
        return self._EnableStdout

    @EnableStdout.setter
    def EnableStdout(self, EnableStdout):
        self._EnableStdout = EnableStdout

    @property
    def Enable(self):
        """是否启用访问日志采集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
        self._File = params.get("File")
        self._Format = params.get("Format")
        self._Encoding = params.get("Encoding")
        if params.get("SelectedRange") is not None:
            self._SelectedRange = SelectedRange()
            self._SelectedRange._deserialize(params.get("SelectedRange"))
        self._Template = params.get("Template")
        if params.get("CLS") is not None:
            self._CLS = CLS()
            self._CLS._deserialize(params.get("CLS"))
        self._Address = params.get("Address")
        self._EnableServer = params.get("EnableServer")
        self._EnableStdout = params.get("EnableStdout")
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeMeshListRequest(AbstractModel):
    """DescribeMeshList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Limit: 分页限制
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """分页限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
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
        


class DescribeMeshListResponse(AbstractModel):
    """DescribeMeshList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshList: 查询到的网格信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MeshList: list of Mesh
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MeshList = None
        self._Total = None
        self._RequestId = None

    @property
    def MeshList(self):
        """查询到的网格信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Mesh
        """
        return self._MeshList

    @MeshList.setter
    def MeshList(self, MeshList):
        self._MeshList = MeshList

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("MeshList") is not None:
            self._MeshList = []
            for item in params.get("MeshList"):
                obj = Mesh()
                obj._deserialize(item)
                self._MeshList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeMeshRequest(AbstractModel):
    """DescribeMesh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 需要查询的网格 Id
        :type MeshId: str
        """
        self._MeshId = None

    @property
    def MeshId(self):
        """需要查询的网格 Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMeshResponse(AbstractModel):
    """DescribeMesh返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Mesh: Mesh详细信息
        :type Mesh: :class:`tencentcloud.tcm.v20210413.models.Mesh`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Mesh = None
        self._RequestId = None

    @property
    def Mesh(self):
        """Mesh详细信息
        :rtype: :class:`tencentcloud.tcm.v20210413.models.Mesh`
        """
        return self._Mesh

    @Mesh.setter
    def Mesh(self, Mesh):
        self._Mesh = Mesh

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
        if params.get("Mesh") is not None:
            self._Mesh = Mesh()
            self._Mesh._deserialize(params.get("Mesh"))
        self._RequestId = params.get("RequestId")


class EgressGateway(AbstractModel):
    """Egress配置

    """

    def __init__(self):
        r"""
        :param _Name: Egress名称
        :type Name: str
        :param _Namespace: 所在的Namespace
        :type Namespace: str
        :param _Workload: 工作负载配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        :param _Status: 工作负载的状态
        :type Status: :class:`tencentcloud.tcm.v20210413.models.EgressGatewayStatus`
        """
        self._Name = None
        self._Namespace = None
        self._Workload = None
        self._Status = None

    @property
    def Name(self):
        """Egress名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        """所在的Namespace
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Workload(self):
        """工作负载配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def Status(self):
        """工作负载的状态
        :rtype: :class:`tencentcloud.tcm.v20210413.models.EgressGatewayStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        if params.get("Workload") is not None:
            self._Workload = WorkloadConfig()
            self._Workload._deserialize(params.get("Workload"))
        if params.get("Status") is not None:
            self._Status = EgressGatewayStatus()
            self._Status._deserialize(params.get("Status"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EgressGatewayStatus(AbstractModel):
    """egress gateway 的状态

    """

    def __init__(self):
        r"""
        :param _CurrentVersion: egress gateway的当前版本
        :type CurrentVersion: str
        :param _DesiredVersion: egress gateway的目标版本
        :type DesiredVersion: str
        :param _State: egress gateway的状态，取值：running，upgrading，rollbacking
        :type State: str
        """
        self._CurrentVersion = None
        self._DesiredVersion = None
        self._State = None

    @property
    def CurrentVersion(self):
        """egress gateway的当前版本
        :rtype: str
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion

    @property
    def DesiredVersion(self):
        """egress gateway的目标版本
        :rtype: str
        """
        return self._DesiredVersion

    @DesiredVersion.setter
    def DesiredVersion(self, DesiredVersion):
        self._DesiredVersion = DesiredVersion

    @property
    def State(self):
        """egress gateway的状态，取值：running，upgrading，rollbacking
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._CurrentVersion = params.get("CurrentVersion")
        self._DesiredVersion = params.get("DesiredVersion")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensiveCluster(AbstractModel):
    """内网独占集群配置

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._ClusterId = None
        self._Zone = None

    @property
    def ClusterId(self):
        """Cluster ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Zone(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensiveClusters(AbstractModel):
    """内网独占集群配置列表

    """

    def __init__(self):
        r"""
        :param _L4Clusters: 4层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :type L4Clusters: list of ExtensiveCluster
        :param _L7Clusters: 7层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :type L7Clusters: list of ExtensiveCluster
        """
        self._L4Clusters = None
        self._L7Clusters = None

    @property
    def L4Clusters(self):
        """4层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExtensiveCluster
        """
        return self._L4Clusters

    @L4Clusters.setter
    def L4Clusters(self, L4Clusters):
        self._L4Clusters = L4Clusters

    @property
    def L7Clusters(self):
        """7层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExtensiveCluster
        """
        return self._L7Clusters

    @L7Clusters.setter
    def L7Clusters(self, L7Clusters):
        self._L7Clusters = L7Clusters


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self._L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ExtensiveCluster()
                obj._deserialize(item)
                self._L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self._L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ExtensiveCluster()
                obj._deserialize(item)
                self._L7Clusters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """键值对过滤器，用于条件过滤查询。例如过滤ID、名称等

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
        


class GrafanaInfo(AbstractModel):
    """Grafana信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启
        :type Enabled: bool
        :param _InternalURL: 内网地址
        :type InternalURL: str
        :param _PublicURL: 公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicURL: str
        :param _PublicFailedReason: 公网失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicFailedReason: str
        :param _PublicFailedMessage: 公网失败详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicFailedMessage: str
        """
        self._Enabled = None
        self._InternalURL = None
        self._PublicURL = None
        self._PublicFailedReason = None
        self._PublicFailedMessage = None

    @property
    def Enabled(self):
        """是否开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def InternalURL(self):
        """内网地址
        :rtype: str
        """
        return self._InternalURL

    @InternalURL.setter
    def InternalURL(self, InternalURL):
        self._InternalURL = InternalURL

    @property
    def PublicURL(self):
        """公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicURL

    @PublicURL.setter
    def PublicURL(self, PublicURL):
        self._PublicURL = PublicURL

    @property
    def PublicFailedReason(self):
        """公网失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicFailedReason

    @PublicFailedReason.setter
    def PublicFailedReason(self, PublicFailedReason):
        self._PublicFailedReason = PublicFailedReason

    @property
    def PublicFailedMessage(self):
        """公网失败详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicFailedMessage

    @PublicFailedMessage.setter
    def PublicFailedMessage(self, PublicFailedMessage):
        self._PublicFailedMessage = PublicFailedMessage


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._InternalURL = params.get("InternalURL")
        self._PublicURL = params.get("PublicURL")
        self._PublicFailedReason = params.get("PublicFailedReason")
        self._PublicFailedMessage = params.get("PublicFailedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscalerSpec(AbstractModel):
    """HPA 配置

    """

    def __init__(self):
        r"""
        :param _MinReplicas: 最小副本数
        :type MinReplicas: int
        :param _MaxReplicas: 最大副本数
        :type MaxReplicas: int
        :param _Metrics: 用于计算副本数的指标
        :type Metrics: list of MetricSpec
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._Metrics = None

    @property
    def MinReplicas(self):
        """最小副本数
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        """最大副本数
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def Metrics(self):
        """用于计算副本数的指标
        :rtype: list of MetricSpec
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = MetricSpec()
                obj._deserialize(item)
                self._Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressGateway(AbstractModel):
    """IngressGateway 实例信息

    """

    def __init__(self):
        r"""
        :param _Name: IngressGateway 实例名字
        :type Name: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Service: Service 配置
        :type Service: :class:`tencentcloud.tcm.v20210413.models.Service`
        :param _Workload: Workload 配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        :param _LoadBalancer: 负载均衡配置，自动创建 CLB 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancer: :class:`tencentcloud.tcm.v20210413.models.LoadBalancer`
        :param _Status: IngressGateway 状态信息，只读
        :type Status: :class:`tencentcloud.tcm.v20210413.models.IngressGatewayStatus`
        :param _LoadBalancerId: 负载均衡实例ID，使用已有 CLB 时返回
        :type LoadBalancerId: str
        """
        self._Name = None
        self._Namespace = None
        self._ClusterId = None
        self._Service = None
        self._Workload = None
        self._LoadBalancer = None
        self._Status = None
        self._LoadBalancerId = None

    @property
    def Name(self):
        """IngressGateway 实例名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ClusterId(self):
        """集群 ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Service(self):
        """Service 配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.Service`
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Workload(self):
        """Workload 配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def LoadBalancer(self):
        """负载均衡配置，自动创建 CLB 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.LoadBalancer`
        """
        return self._LoadBalancer

    @LoadBalancer.setter
    def LoadBalancer(self, LoadBalancer):
        self._LoadBalancer = LoadBalancer

    @property
    def Status(self):
        """IngressGateway 状态信息，只读
        :rtype: :class:`tencentcloud.tcm.v20210413.models.IngressGatewayStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancerId(self):
        """负载均衡实例ID，使用已有 CLB 时返回
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._ClusterId = params.get("ClusterId")
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        if params.get("Workload") is not None:
            self._Workload = WorkloadConfig()
            self._Workload._deserialize(params.get("Workload"))
        if params.get("LoadBalancer") is not None:
            self._LoadBalancer = LoadBalancer()
            self._LoadBalancer._deserialize(params.get("LoadBalancer"))
        if params.get("Status") is not None:
            self._Status = IngressGatewayStatus()
            self._Status._deserialize(params.get("Status"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressGatewayStatus(AbstractModel):
    """IngressGateway状态

    """

    def __init__(self):
        r"""
        :param _LoadBalancer: 负载均衡实例状态
        :type LoadBalancer: :class:`tencentcloud.tcm.v20210413.models.LoadBalancerStatus`
        :param _CurrentVersion: ingress gateway 当前的版本
        :type CurrentVersion: str
        :param _DesiredVersion: ingress gateway 目标的版本
        :type DesiredVersion: str
        :param _State: ingress gateway的状态，取值running, upgrading, rollbacking
        :type State: str
        """
        self._LoadBalancer = None
        self._CurrentVersion = None
        self._DesiredVersion = None
        self._State = None

    @property
    def LoadBalancer(self):
        """负载均衡实例状态
        :rtype: :class:`tencentcloud.tcm.v20210413.models.LoadBalancerStatus`
        """
        return self._LoadBalancer

    @LoadBalancer.setter
    def LoadBalancer(self, LoadBalancer):
        self._LoadBalancer = LoadBalancer

    @property
    def CurrentVersion(self):
        """ingress gateway 当前的版本
        :rtype: str
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion

    @property
    def DesiredVersion(self):
        """ingress gateway 目标的版本
        :rtype: str
        """
        return self._DesiredVersion

    @DesiredVersion.setter
    def DesiredVersion(self, DesiredVersion):
        self._DesiredVersion = DesiredVersion

    @property
    def State(self):
        """ingress gateway的状态，取值running, upgrading, rollbacking
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        if params.get("LoadBalancer") is not None:
            self._LoadBalancer = LoadBalancerStatus()
            self._LoadBalancer._deserialize(params.get("LoadBalancer"))
        self._CurrentVersion = params.get("CurrentVersion")
        self._DesiredVersion = params.get("DesiredVersion")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InjectConfig(AbstractModel):
    """自动注入配置

    """

    def __init__(self):
        r"""
        :param _ExcludeIPRanges: 不需要进行代理的 ip 地址范围
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeIPRanges: list of str
        :param _HoldApplicationUntilProxyStarts: 是否等待sidecar启动
注意：此字段可能返回 null，表示取不到有效值。
        :type HoldApplicationUntilProxyStarts: bool
        :param _HoldProxyUntilApplicationEnds: 是否允许sidecar等待
注意：此字段可能返回 null，表示取不到有效值。
        :type HoldProxyUntilApplicationEnds: bool
        """
        self._ExcludeIPRanges = None
        self._HoldApplicationUntilProxyStarts = None
        self._HoldProxyUntilApplicationEnds = None

    @property
    def ExcludeIPRanges(self):
        """不需要进行代理的 ip 地址范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludeIPRanges

    @ExcludeIPRanges.setter
    def ExcludeIPRanges(self, ExcludeIPRanges):
        self._ExcludeIPRanges = ExcludeIPRanges

    @property
    def HoldApplicationUntilProxyStarts(self):
        """是否等待sidecar启动
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HoldApplicationUntilProxyStarts

    @HoldApplicationUntilProxyStarts.setter
    def HoldApplicationUntilProxyStarts(self, HoldApplicationUntilProxyStarts):
        self._HoldApplicationUntilProxyStarts = HoldApplicationUntilProxyStarts

    @property
    def HoldProxyUntilApplicationEnds(self):
        """是否允许sidecar等待
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HoldProxyUntilApplicationEnds

    @HoldProxyUntilApplicationEnds.setter
    def HoldProxyUntilApplicationEnds(self, HoldProxyUntilApplicationEnds):
        self._HoldProxyUntilApplicationEnds = HoldProxyUntilApplicationEnds


    def _deserialize(self, params):
        self._ExcludeIPRanges = params.get("ExcludeIPRanges")
        self._HoldApplicationUntilProxyStarts = params.get("HoldApplicationUntilProxyStarts")
        self._HoldProxyUntilApplicationEnds = params.get("HoldProxyUntilApplicationEnds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IstioConfig(AbstractModel):
    """Istio配置

    """

    def __init__(self):
        r"""
        :param _OutboundTrafficPolicy: 外部流量策略
        :type OutboundTrafficPolicy: str
        :param _Tracing: 调用链配置（Deprecated，请使用 MeshConfig.Tracing 进行配置）
        :type Tracing: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        :param _DisablePolicyChecks: 禁用策略检查功能
注意：此字段可能返回 null，表示取不到有效值。
        :type DisablePolicyChecks: bool
        :param _EnablePilotHTTP: 支持HTTP1.0协议
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePilotHTTP: bool
        :param _DisableHTTPRetry: 禁用HTTP重试策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableHTTPRetry: bool
        :param _SmartDNS: SmartDNS策略
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartDNS: :class:`tencentcloud.tcm.v20210413.models.SmartDNSConfig`
        """
        self._OutboundTrafficPolicy = None
        self._Tracing = None
        self._DisablePolicyChecks = None
        self._EnablePilotHTTP = None
        self._DisableHTTPRetry = None
        self._SmartDNS = None

    @property
    def OutboundTrafficPolicy(self):
        """外部流量策略
        :rtype: str
        """
        return self._OutboundTrafficPolicy

    @OutboundTrafficPolicy.setter
    def OutboundTrafficPolicy(self, OutboundTrafficPolicy):
        self._OutboundTrafficPolicy = OutboundTrafficPolicy

    @property
    def Tracing(self):
        """调用链配置（Deprecated，请使用 MeshConfig.Tracing 进行配置）
        :rtype: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        """
        return self._Tracing

    @Tracing.setter
    def Tracing(self, Tracing):
        self._Tracing = Tracing

    @property
    def DisablePolicyChecks(self):
        """禁用策略检查功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DisablePolicyChecks

    @DisablePolicyChecks.setter
    def DisablePolicyChecks(self, DisablePolicyChecks):
        self._DisablePolicyChecks = DisablePolicyChecks

    @property
    def EnablePilotHTTP(self):
        """支持HTTP1.0协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnablePilotHTTP

    @EnablePilotHTTP.setter
    def EnablePilotHTTP(self, EnablePilotHTTP):
        self._EnablePilotHTTP = EnablePilotHTTP

    @property
    def DisableHTTPRetry(self):
        """禁用HTTP重试策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DisableHTTPRetry

    @DisableHTTPRetry.setter
    def DisableHTTPRetry(self, DisableHTTPRetry):
        self._DisableHTTPRetry = DisableHTTPRetry

    @property
    def SmartDNS(self):
        """SmartDNS策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.SmartDNSConfig`
        """
        return self._SmartDNS

    @SmartDNS.setter
    def SmartDNS(self, SmartDNS):
        self._SmartDNS = SmartDNS


    def _deserialize(self, params):
        self._OutboundTrafficPolicy = params.get("OutboundTrafficPolicy")
        if params.get("Tracing") is not None:
            self._Tracing = TracingConfig()
            self._Tracing._deserialize(params.get("Tracing"))
        self._DisablePolicyChecks = params.get("DisablePolicyChecks")
        self._EnablePilotHTTP = params.get("EnablePilotHTTP")
        self._DisableHTTPRetry = params.get("DisableHTTPRetry")
        if params.get("SmartDNS") is not None:
            self._SmartDNS = SmartDNSConfig()
            self._SmartDNS._deserialize(params.get("SmartDNS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IstiodConfig(AbstractModel):
    """Istiod配置

    """

    def __init__(self):
        r"""
        :param _Workload: 工作负载配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        self._Workload = None

    @property
    def Workload(self):
        """工作负载配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload


    def _deserialize(self, params):
        if params.get("Workload") is not None:
            self._Workload = WorkloadConfig()
            self._Workload._deserialize(params.get("Workload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkClusterListRequest(AbstractModel):
    """LinkClusterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 网格Id
        :type MeshId: str
        :param _ClusterList: 关联集群
        :type ClusterList: list of Cluster
        """
        self._MeshId = None
        self._ClusterList = None

    @property
    def MeshId(self):
        """网格Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def ClusterList(self):
        """关联集群
        :rtype: list of Cluster
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkClusterListResponse(AbstractModel):
    """LinkClusterList返回参数结构体

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


class LinkPrometheusRequest(AbstractModel):
    """LinkPrometheus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshID: 网格ID
        :type MeshID: str
        :param _Prometheus: 配置
        :type Prometheus: :class:`tencentcloud.tcm.v20210413.models.PrometheusConfig`
        """
        self._MeshID = None
        self._Prometheus = None

    @property
    def MeshID(self):
        """网格ID
        :rtype: str
        """
        return self._MeshID

    @MeshID.setter
    def MeshID(self, MeshID):
        self._MeshID = MeshID

    @property
    def Prometheus(self):
        """配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.PrometheusConfig`
        """
        return self._Prometheus

    @Prometheus.setter
    def Prometheus(self, Prometheus):
        self._Prometheus = Prometheus


    def _deserialize(self, params):
        self._MeshID = params.get("MeshID")
        if params.get("Prometheus") is not None:
            self._Prometheus = PrometheusConfig()
            self._Prometheus._deserialize(params.get("Prometheus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkPrometheusResponse(AbstractModel):
    """LinkPrometheus返回参数结构体

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


class LoadBalancer(AbstractModel):
    """负载均衡配置

    """

    def __init__(self):
        r"""
        :param _LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
只读。
        :type LoadBalancerType: str
        :param _SubnetId: 负载均衡实例所在的子网（仅对内网VPC型LB有意义），只读。
        :type SubnetId: str
        :param _InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;只读。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 最大出带宽，单位Mbps，仅对公网属性的LB生效，默认值 10
        :type InternetMaxBandwidthOut: int
        :param _ZoneID: 可用区 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneID: str
        :param _VipIsp: 运营商类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param _TgwGroupName: TGW Group 名
注意：此字段可能返回 null，表示取不到有效值。
        :type TgwGroupName: str
        :param _AddressIPVersion: IP 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ExtensiveClusters: 内网独占集群配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensiveClusters: :class:`tencentcloud.tcm.v20210413.models.ExtensiveClusters`
        :param _CrossRegionConfig: 负载均衡跨地域配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossRegionConfig: :class:`tencentcloud.tcm.v20210413.models.CrossRegionConfig`
        :param _MasterZoneID: 设置跨可用区容灾时的主可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZoneID: str
        :param _SlaveZoneID: 设置跨可用区容灾时的备可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZoneID: str
        """
        self._LoadBalancerType = None
        self._SubnetId = None
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._ZoneID = None
        self._VipIsp = None
        self._TgwGroupName = None
        self._AddressIPVersion = None
        self._Tags = None
        self._ExtensiveClusters = None
        self._CrossRegionConfig = None
        self._MasterZoneID = None
        self._SlaveZoneID = None

    @property
    def LoadBalancerType(self):
        """负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
只读。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def SubnetId(self):
        """负载均衡实例所在的子网（仅对内网VPC型LB有意义），只读。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InternetChargeType(self):
        """TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;只读。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """最大出带宽，单位Mbps，仅对公网属性的LB生效，默认值 10
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ZoneID(self):
        """可用区 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneID

    @ZoneID.setter
    def ZoneID(self, ZoneID):
        self._ZoneID = ZoneID

    @property
    def VipIsp(self):
        """运营商类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def TgwGroupName(self):
        """TGW Group 名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TgwGroupName

    @TgwGroupName.setter
    def TgwGroupName(self, TgwGroupName):
        self._TgwGroupName = TgwGroupName

    @property
    def AddressIPVersion(self):
        """IP 类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Tags(self):
        """标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExtensiveClusters(self):
        """内网独占集群配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ExtensiveClusters`
        """
        return self._ExtensiveClusters

    @ExtensiveClusters.setter
    def ExtensiveClusters(self, ExtensiveClusters):
        self._ExtensiveClusters = ExtensiveClusters

    @property
    def CrossRegionConfig(self):
        """负载均衡跨地域配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CrossRegionConfig`
        """
        return self._CrossRegionConfig

    @CrossRegionConfig.setter
    def CrossRegionConfig(self, CrossRegionConfig):
        self._CrossRegionConfig = CrossRegionConfig

    @property
    def MasterZoneID(self):
        """设置跨可用区容灾时的主可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MasterZoneID

    @MasterZoneID.setter
    def MasterZoneID(self, MasterZoneID):
        self._MasterZoneID = MasterZoneID

    @property
    def SlaveZoneID(self):
        """设置跨可用区容灾时的备可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SlaveZoneID

    @SlaveZoneID.setter
    def SlaveZoneID(self, SlaveZoneID):
        self._SlaveZoneID = SlaveZoneID


    def _deserialize(self, params):
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._SubnetId = params.get("SubnetId")
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ZoneID = params.get("ZoneID")
        self._VipIsp = params.get("VipIsp")
        self._TgwGroupName = params.get("TgwGroupName")
        self._AddressIPVersion = params.get("AddressIPVersion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ExtensiveClusters") is not None:
            self._ExtensiveClusters = ExtensiveClusters()
            self._ExtensiveClusters._deserialize(params.get("ExtensiveClusters"))
        if params.get("CrossRegionConfig") is not None:
            self._CrossRegionConfig = CrossRegionConfig()
            self._CrossRegionConfig._deserialize(params.get("CrossRegionConfig"))
        self._MasterZoneID = params.get("MasterZoneID")
        self._SlaveZoneID = params.get("SlaveZoneID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerStatus(AbstractModel):
    """负载均衡状态信息

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名字
        :type LoadBalancerName: str
        :param _LoadBalancerVip: 负载均衡实例 VIP
        :type LoadBalancerVip: str
        :param _LoadBalancerHostname: 负载均衡实例 Hostname
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerHostname: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerVip = None
        self._LoadBalancerHostname = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """负载均衡实例名字
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerVip(self):
        """负载均衡实例 VIP
        :rtype: str
        """
        return self._LoadBalancerVip

    @LoadBalancerVip.setter
    def LoadBalancerVip(self, LoadBalancerVip):
        self._LoadBalancerVip = LoadBalancerVip

    @property
    def LoadBalancerHostname(self):
        """负载均衡实例 Hostname
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerHostname

    @LoadBalancerHostname.setter
    def LoadBalancerHostname(self, LoadBalancerHostname):
        self._LoadBalancerHostname = LoadBalancerHostname


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerVip = params.get("LoadBalancerVip")
        self._LoadBalancerHostname = params.get("LoadBalancerHostname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Mesh(AbstractModel):
    """Mesh信息

    """

    def __init__(self):
        r"""
        :param _MeshId: Mesh实例Id
        :type MeshId: str
        :param _DisplayName: Mesh名称
        :type DisplayName: str
        :param _Type: Mesh类型，取值范围：
- STANDALONE：独立网格
- HOSTED：托管网格
        :type Type: str
        :param _Region: 地域
        :type Region: str
        :param _Version: 版本
        :type Version: str
        :param _State: Mesh状态，取值范围：
- PENDING：等待中
- CREATING：创建中
- RUNNING：运行中
- ABNORMAL：异常
- UPGRADING：升级中
- CANARY_UPGRADED：升级灰度完成
- ROLLBACKING：升级回滚
- DELETING：删除中
- CREATE_FAILED：安装失败
- DELETE_FAILED：删除失败
- UPGRADE_FAILED：升级失败
- ROLLBACK_FAILED：回滚失败
        :type State: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param _ClusterList: 集群列表
        :type ClusterList: list of Cluster
        :param _Config: Mesh配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        :param _Status: Mesh详细状态
        :type Status: :class:`tencentcloud.tcm.v20210413.models.MeshStatus`
        :param _TagList: 标签列表
        :type TagList: list of Tag
        """
        self._MeshId = None
        self._DisplayName = None
        self._Type = None
        self._Region = None
        self._Version = None
        self._State = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._ClusterList = None
        self._Config = None
        self._Status = None
        self._TagList = None

    @property
    def MeshId(self):
        """Mesh实例Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def DisplayName(self):
        """Mesh名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Type(self):
        """Mesh类型，取值范围：
- STANDALONE：独立网格
- HOSTED：托管网格
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Version(self):
        """版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def State(self):
        """Mesh状态，取值范围：
- PENDING：等待中
- CREATING：创建中
- RUNNING：运行中
- ABNORMAL：异常
- UPGRADING：升级中
- CANARY_UPGRADED：升级灰度完成
- ROLLBACKING：升级回滚
- DELETING：删除中
- CREATE_FAILED：安装失败
- DELETE_FAILED：删除失败
- UPGRADE_FAILED：升级失败
- ROLLBACK_FAILED：回滚失败
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def ClusterList(self):
        """集群列表
        :rtype: list of Cluster
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def Config(self):
        """Mesh配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """Mesh详细状态
        :rtype: :class:`tencentcloud.tcm.v20210413.models.MeshStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagList(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        self._DisplayName = params.get("DisplayName")
        self._Type = params.get("Type")
        self._Region = params.get("Region")
        self._Version = params.get("Version")
        self._State = params.get("State")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        if params.get("Config") is not None:
            self._Config = MeshConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("Status") is not None:
            self._Status = MeshStatus()
            self._Status._deserialize(params.get("Status"))
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
        


class MeshConfig(AbstractModel):
    """网格配置项

    """

    def __init__(self):
        r"""
        :param _Istio: Istio配置
        :type Istio: :class:`tencentcloud.tcm.v20210413.models.IstioConfig`
        :param _AccessLog: AccessLog配置
        :type AccessLog: :class:`tencentcloud.tcm.v20210413.models.AccessLogConfig`
        :param _Prometheus: Prometheus配置
        :type Prometheus: :class:`tencentcloud.tcm.v20210413.models.PrometheusConfig`
        :param _Inject: 自动注入配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Inject: :class:`tencentcloud.tcm.v20210413.models.InjectConfig`
        :param _Tracing: 调用跟踪配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tracing: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        :param _SidecarResources: Sidecar自定义资源
注意：此字段可能返回 null，表示取不到有效值。
        :type SidecarResources: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        """
        self._Istio = None
        self._AccessLog = None
        self._Prometheus = None
        self._Inject = None
        self._Tracing = None
        self._SidecarResources = None

    @property
    def Istio(self):
        """Istio配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.IstioConfig`
        """
        return self._Istio

    @Istio.setter
    def Istio(self, Istio):
        self._Istio = Istio

    @property
    def AccessLog(self):
        """AccessLog配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.AccessLogConfig`
        """
        return self._AccessLog

    @AccessLog.setter
    def AccessLog(self, AccessLog):
        self._AccessLog = AccessLog

    @property
    def Prometheus(self):
        """Prometheus配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.PrometheusConfig`
        """
        return self._Prometheus

    @Prometheus.setter
    def Prometheus(self, Prometheus):
        self._Prometheus = Prometheus

    @property
    def Inject(self):
        """自动注入配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.InjectConfig`
        """
        return self._Inject

    @Inject.setter
    def Inject(self, Inject):
        self._Inject = Inject

    @property
    def Tracing(self):
        """调用跟踪配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        """
        return self._Tracing

    @Tracing.setter
    def Tracing(self, Tracing):
        self._Tracing = Tracing

    @property
    def SidecarResources(self):
        """Sidecar自定义资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        """
        return self._SidecarResources

    @SidecarResources.setter
    def SidecarResources(self, SidecarResources):
        self._SidecarResources = SidecarResources


    def _deserialize(self, params):
        if params.get("Istio") is not None:
            self._Istio = IstioConfig()
            self._Istio._deserialize(params.get("Istio"))
        if params.get("AccessLog") is not None:
            self._AccessLog = AccessLogConfig()
            self._AccessLog._deserialize(params.get("AccessLog"))
        if params.get("Prometheus") is not None:
            self._Prometheus = PrometheusConfig()
            self._Prometheus._deserialize(params.get("Prometheus"))
        if params.get("Inject") is not None:
            self._Inject = InjectConfig()
            self._Inject._deserialize(params.get("Inject"))
        if params.get("Tracing") is not None:
            self._Tracing = TracingConfig()
            self._Tracing._deserialize(params.get("Tracing"))
        if params.get("SidecarResources") is not None:
            self._SidecarResources = ResourceRequirements()
            self._SidecarResources._deserialize(params.get("SidecarResources"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MeshStatus(AbstractModel):
    """Mesh当前状态

    """

    def __init__(self):
        r"""
        :param _ServiceCount: 服务数量
        :type ServiceCount: int
        :param _CanaryVersion: 灰度升级的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CanaryVersion: str
        :param _Prometheus: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type Prometheus: list of PrometheusStatus
        :param _StateMessage: 状态附带信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StateMessage: str
        :param _ActiveOperationList: 正在执行的异步操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveOperationList: list of ActiveOperation
        :param _TPS: 获取TPS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TPS: :class:`tencentcloud.tcm.v20210413.models.PrometheusStatus`
        """
        self._ServiceCount = None
        self._CanaryVersion = None
        self._Prometheus = None
        self._StateMessage = None
        self._ActiveOperationList = None
        self._TPS = None

    @property
    def ServiceCount(self):
        """服务数量
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def CanaryVersion(self):
        """灰度升级的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CanaryVersion

    @CanaryVersion.setter
    def CanaryVersion(self, CanaryVersion):
        self._CanaryVersion = CanaryVersion

    @property
    def Prometheus(self):
        """已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PrometheusStatus
        """
        return self._Prometheus

    @Prometheus.setter
    def Prometheus(self, Prometheus):
        self._Prometheus = Prometheus

    @property
    def StateMessage(self):
        """状态附带信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StateMessage

    @StateMessage.setter
    def StateMessage(self, StateMessage):
        self._StateMessage = StateMessage

    @property
    def ActiveOperationList(self):
        """正在执行的异步操作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ActiveOperation
        """
        return self._ActiveOperationList

    @ActiveOperationList.setter
    def ActiveOperationList(self, ActiveOperationList):
        self._ActiveOperationList = ActiveOperationList

    @property
    def TPS(self):
        """获取TPS信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.PrometheusStatus`
        """
        return self._TPS

    @TPS.setter
    def TPS(self, TPS):
        self._TPS = TPS


    def _deserialize(self, params):
        self._ServiceCount = params.get("ServiceCount")
        self._CanaryVersion = params.get("CanaryVersion")
        if params.get("Prometheus") is not None:
            self._Prometheus = []
            for item in params.get("Prometheus"):
                obj = PrometheusStatus()
                obj._deserialize(item)
                self._Prometheus.append(obj)
        self._StateMessage = params.get("StateMessage")
        if params.get("ActiveOperationList") is not None:
            self._ActiveOperationList = []
            for item in params.get("ActiveOperationList"):
                obj = ActiveOperation()
                obj._deserialize(item)
                self._ActiveOperationList.append(obj)
        if params.get("TPS") is not None:
            self._TPS = PrometheusStatus()
            self._TPS._deserialize(params.get("TPS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricSpec(AbstractModel):
    """MetricSpec 描述如何通过指定指标进行自动扩缩容

    """

    def __init__(self):
        r"""
        :param _Type: 指标来源类型，支持 Pods/Resource
        :type Type: str
        :param _Pods: 使用自定义指标扩进行自动扩缩容
        :type Pods: :class:`tencentcloud.tcm.v20210413.models.PodsMetricSource`
        :param _Resource: 使用资源指标扩进行自动扩缩容
        :type Resource: :class:`tencentcloud.tcm.v20210413.models.ResourceMetricSource`
        """
        self._Type = None
        self._Pods = None
        self._Resource = None

    @property
    def Type(self):
        """指标来源类型，支持 Pods/Resource
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pods(self):
        """使用自定义指标扩进行自动扩缩容
        :rtype: :class:`tencentcloud.tcm.v20210413.models.PodsMetricSource`
        """
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        self._Pods = Pods

    @property
    def Resource(self):
        """使用资源指标扩进行自动扩缩容
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ResourceMetricSource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Pods") is not None:
            self._Pods = PodsMetricSource()
            self._Pods._deserialize(params.get("Pods"))
        if params.get("Resource") is not None:
            self._Resource = ResourceMetricSource()
            self._Resource._deserialize(params.get("Resource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessLogConfigRequest(AbstractModel):
    """ModifyAccessLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: mesh ID
        :type MeshId: str
        :param _SelectedRange: 选中的范围
        :type SelectedRange: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        :param _Template: 采用的模板，可选值：istio（默认）、trace、custom
        :type Template: str
        :param _Enable: 是否启用
        :type Enable: bool
        :param _CLS: 腾讯云日志服务相关参数
        :type CLS: :class:`tencentcloud.tcm.v20210413.models.CLS`
        :param _Encoding: 编码格式，可选值：TEXT、JSON
        :type Encoding: str
        :param _Format: 日志格式
        :type Format: str
        :param _EnableStdout: 是否启用标准输出
        :type EnableStdout: bool
        :param _EnableServer: 是否启动GRPC第三方服务器
        :type EnableServer: bool
        :param _Address: GRPC第三方服务器地址
        :type Address: str
        """
        self._MeshId = None
        self._SelectedRange = None
        self._Template = None
        self._Enable = None
        self._CLS = None
        self._Encoding = None
        self._Format = None
        self._EnableStdout = None
        self._EnableServer = None
        self._Address = None

    @property
    def MeshId(self):
        """mesh ID
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def SelectedRange(self):
        """选中的范围
        :rtype: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        """
        return self._SelectedRange

    @SelectedRange.setter
    def SelectedRange(self, SelectedRange):
        self._SelectedRange = SelectedRange

    @property
    def Template(self):
        """采用的模板，可选值：istio（默认）、trace、custom
        :rtype: str
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Enable(self):
        """是否启用
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CLS(self):
        """腾讯云日志服务相关参数
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CLS`
        """
        return self._CLS

    @CLS.setter
    def CLS(self, CLS):
        self._CLS = CLS

    @property
    def Encoding(self):
        """编码格式，可选值：TEXT、JSON
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Format(self):
        """日志格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def EnableStdout(self):
        """是否启用标准输出
        :rtype: bool
        """
        return self._EnableStdout

    @EnableStdout.setter
    def EnableStdout(self, EnableStdout):
        self._EnableStdout = EnableStdout

    @property
    def EnableServer(self):
        """是否启动GRPC第三方服务器
        :rtype: bool
        """
        return self._EnableServer

    @EnableServer.setter
    def EnableServer(self, EnableServer):
        self._EnableServer = EnableServer

    @property
    def Address(self):
        """GRPC第三方服务器地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        if params.get("SelectedRange") is not None:
            self._SelectedRange = SelectedRange()
            self._SelectedRange._deserialize(params.get("SelectedRange"))
        self._Template = params.get("Template")
        self._Enable = params.get("Enable")
        if params.get("CLS") is not None:
            self._CLS = CLS()
            self._CLS._deserialize(params.get("CLS"))
        self._Encoding = params.get("Encoding")
        self._Format = params.get("Format")
        self._EnableStdout = params.get("EnableStdout")
        self._EnableServer = params.get("EnableServer")
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessLogConfigResponse(AbstractModel):
    """ModifyAccessLogConfig返回参数结构体

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


class ModifyMeshRequest(AbstractModel):
    """ModifyMesh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 需要修改的网格Id
        :type MeshId: str
        :param _DisplayName: 修改的网格名称
        :type DisplayName: str
        :param _Config: 修改的网格配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        :param _ClusterList: 修改的集群配置
        :type ClusterList: list of Cluster
        """
        self._MeshId = None
        self._DisplayName = None
        self._Config = None
        self._ClusterList = None

    @property
    def MeshId(self):
        """需要修改的网格Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def DisplayName(self):
        """修改的网格名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Config(self):
        """修改的网格配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ClusterList(self):
        """修改的集群配置
        :rtype: list of Cluster
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        self._DisplayName = params.get("DisplayName")
        if params.get("Config") is not None:
            self._Config = MeshConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMeshResponse(AbstractModel):
    """ModifyMesh返回参数结构体

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


class ModifyTracingConfigRequest(AbstractModel):
    """ModifyTracingConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: mesh名字
        :type MeshId: str
        :param _Enable: 是否启用调用跟踪
        :type Enable: bool
        :param _APM: 腾讯云 APM 服务相关参数
        :type APM: :class:`tencentcloud.tcm.v20210413.models.APM`
        :param _Sampling: 调用跟踪采样值
        :type Sampling: float
        :param _Zipkin: 调用追踪Zipkin相关配置
        :type Zipkin: :class:`tencentcloud.tcm.v20210413.models.TracingZipkin`
        """
        self._MeshId = None
        self._Enable = None
        self._APM = None
        self._Sampling = None
        self._Zipkin = None

    @property
    def MeshId(self):
        """mesh名字
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def Enable(self):
        """是否启用调用跟踪
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def APM(self):
        """腾讯云 APM 服务相关参数
        :rtype: :class:`tencentcloud.tcm.v20210413.models.APM`
        """
        return self._APM

    @APM.setter
    def APM(self, APM):
        self._APM = APM

    @property
    def Sampling(self):
        """调用跟踪采样值
        :rtype: float
        """
        return self._Sampling

    @Sampling.setter
    def Sampling(self, Sampling):
        self._Sampling = Sampling

    @property
    def Zipkin(self):
        """调用追踪Zipkin相关配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.TracingZipkin`
        """
        return self._Zipkin

    @Zipkin.setter
    def Zipkin(self, Zipkin):
        self._Zipkin = Zipkin


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        self._Enable = params.get("Enable")
        if params.get("APM") is not None:
            self._APM = APM()
            self._APM._deserialize(params.get("APM"))
        self._Sampling = params.get("Sampling")
        if params.get("Zipkin") is not None:
            self._Zipkin = TracingZipkin()
            self._Zipkin._deserialize(params.get("Zipkin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTracingConfigResponse(AbstractModel):
    """ModifyTracingConfig返回参数结构体

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


class PodsMetricSource(AbstractModel):
    """PodsMetricSource 定义了如何根据特定指标进行扩缩容

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _TargetAverageValue: 目标值
        :type TargetAverageValue: str
        """
        self._MetricName = None
        self._TargetAverageValue = None

    @property
    def MetricName(self):
        """指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def TargetAverageValue(self):
        """目标值
        :rtype: str
        """
        return self._TargetAverageValue

    @TargetAverageValue.setter
    def TargetAverageValue(self, TargetAverageValue):
        self._TargetAverageValue = TargetAverageValue


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._TargetAverageValue = params.get("TargetAverageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfig(AbstractModel):
    """Prometheus 配置

    """

    def __init__(self):
        r"""
        :param _VpcId: 虚拟网络Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _Region: 地域
        :type Region: str
        :param _InstanceId: 关联已存在实例Id，不填则默认创建
        :type InstanceId: str
        :param _CustomProm: 第三方 Prometheus
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomProm: :class:`tencentcloud.tcm.v20210413.models.CustomPromConfig`
        """
        self._VpcId = None
        self._SubnetId = None
        self._Region = None
        self._InstanceId = None
        self._CustomProm = None

    @property
    def VpcId(self):
        """虚拟网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        """关联已存在实例Id，不填则默认创建
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CustomProm(self):
        """第三方 Prometheus
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.CustomPromConfig`
        """
        return self._CustomProm

    @CustomProm.setter
    def CustomProm(self, CustomProm):
        self._CustomProm = CustomProm


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        if params.get("CustomProm") is not None:
            self._CustomProm = CustomPromConfig()
            self._CustomProm._deserialize(params.get("CustomProm"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusStatus(AbstractModel):
    """Prometheus状态信息

    """

    def __init__(self):
        r"""
        :param _PrometheusId: Prometheus Id
        :type PrometheusId: str
        :param _DisplayName: 展示名称
        :type DisplayName: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VpcId: 虚拟网络Id
        :type VpcId: str
        :param _State: 状态
        :type State: str
        :param _Region: 地区
        :type Region: str
        :param _Grafana: Grafana信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Grafana: :class:`tencentcloud.tcm.v20210413.models.GrafanaInfo`
        :param _Type: Prometheus 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._PrometheusId = None
        self._DisplayName = None
        self._InstanceId = None
        self._VpcId = None
        self._State = None
        self._Region = None
        self._Grafana = None
        self._Type = None

    @property
    def PrometheusId(self):
        """Prometheus Id
        :rtype: str
        """
        return self._PrometheusId

    @PrometheusId.setter
    def PrometheusId(self, PrometheusId):
        self._PrometheusId = PrometheusId

    @property
    def DisplayName(self):
        """展示名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """虚拟网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def State(self):
        """状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Region(self):
        """地区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Grafana(self):
        """Grafana信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcm.v20210413.models.GrafanaInfo`
        """
        return self._Grafana

    @Grafana.setter
    def Grafana(self, Grafana):
        self._Grafana = Grafana

    @property
    def Type(self):
        """Prometheus 类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PrometheusId = params.get("PrometheusId")
        self._DisplayName = params.get("DisplayName")
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._State = params.get("State")
        self._Region = params.get("Region")
        if params.get("Grafana") is not None:
            self._Grafana = GrafanaInfo()
            self._Grafana._deserialize(params.get("Grafana"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """Resource 定义了资源类型和数量

    """

    def __init__(self):
        r"""
        :param _Name: 资源类型 cpu/memory
        :type Name: str
        :param _Quantity: 资源数量
        :type Quantity: str
        """
        self._Name = None
        self._Quantity = None

    @property
    def Name(self):
        """资源类型 cpu/memory
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quantity(self):
        """资源数量
        :rtype: str
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceMetricSource(AbstractModel):
    """ResourceMetricSource 定义了如何根据已知类型的资源指标进行扩缩容

    """

    def __init__(self):
        r"""
        :param _Name: 资源名称 cpu/memory
        :type Name: str
        :param _TargetAverageUtilization: 目标平均利用率
        :type TargetAverageUtilization: int
        :param _TargetAverageValue: 目标平均值
        :type TargetAverageValue: str
        """
        self._Name = None
        self._TargetAverageUtilization = None
        self._TargetAverageValue = None

    @property
    def Name(self):
        """资源名称 cpu/memory
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TargetAverageUtilization(self):
        """目标平均利用率
        :rtype: int
        """
        return self._TargetAverageUtilization

    @TargetAverageUtilization.setter
    def TargetAverageUtilization(self, TargetAverageUtilization):
        self._TargetAverageUtilization = TargetAverageUtilization

    @property
    def TargetAverageValue(self):
        """目标平均值
        :rtype: str
        """
        return self._TargetAverageValue

    @TargetAverageValue.setter
    def TargetAverageValue(self, TargetAverageValue):
        self._TargetAverageValue = TargetAverageValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TargetAverageUtilization = params.get("TargetAverageUtilization")
        self._TargetAverageValue = params.get("TargetAverageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRequirements(AbstractModel):
    """ResourceRequirements 描述了计算资源需求。

    """

    def __init__(self):
        r"""
        :param _Limits: Limits 描述了允许的最大计算资源量。
        :type Limits: list of Resource
        :param _Requests: Requests 描述所需的最小计算资源量。
        :type Requests: list of Resource
        """
        self._Limits = None
        self._Requests = None

    @property
    def Limits(self):
        """Limits 描述了允许的最大计算资源量。
        :rtype: list of Resource
        """
        return self._Limits

    @Limits.setter
    def Limits(self, Limits):
        self._Limits = Limits

    @property
    def Requests(self):
        """Requests 描述所需的最小计算资源量。
        :rtype: list of Resource
        """
        return self._Requests

    @Requests.setter
    def Requests(self, Requests):
        self._Requests = Requests


    def _deserialize(self, params):
        if params.get("Limits") is not None:
            self._Limits = []
            for item in params.get("Limits"):
                obj = Resource()
                obj._deserialize(item)
                self._Limits.append(obj)
        if params.get("Requests") is not None:
            self._Requests = []
            for item in params.get("Requests"):
                obj = Resource()
                obj._deserialize(item)
                self._Requests.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedItems(AbstractModel):
    """选中的项目

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _ItemName: 选中项目名字
        :type ItemName: str
        :param _Gateways: ingress gw的名称列表
        :type Gateways: list of str
        """
        self._Namespace = None
        self._ClusterName = None
        self._ItemName = None
        self._Gateways = None

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ItemName(self):
        """选中项目名字
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def Gateways(self):
        """ingress gw的名称列表
        :rtype: list of str
        """
        return self._Gateways

    @Gateways.setter
    def Gateways(self, Gateways):
        self._Gateways = Gateways


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._ClusterName = params.get("ClusterName")
        self._ItemName = params.get("ItemName")
        self._Gateways = params.get("Gateways")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedRange(AbstractModel):
    """被选中的范围

    """

    def __init__(self):
        r"""
        :param _Items: 选中的项目详细内容
        :type Items: list of SelectedItems
        :param _All: 是否全选
        :type All: bool
        """
        self._Items = None
        self._All = None

    @property
    def Items(self):
        """选中的项目详细内容
        :rtype: list of SelectedItems
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def All(self):
        """是否全选
        :rtype: bool
        """
        return self._All

    @All.setter
    def All(self, All):
        self._All = All


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SelectedItems()
                obj._deserialize(item)
                self._Items.append(obj)
        self._All = params.get("All")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """Service信息

    """

    def __init__(self):
        r"""
        :param _Type: ClusterIP/NodePort/LoadBalancer
        :type Type: str
        :param _CLBDirectAccess: 是否开启LB直通Pod
        :type CLBDirectAccess: bool
        :param _ExternalTrafficPolicy: 服务是否希望将外部流量路由到节点本地或集群范围的端点。 有两个可用选项：Cluster（默认）和 Local。Cluster 隐藏了客户端源 IP，可能导致第二跳到另一个节点；Local 保留客户端源 IP 并避免 LoadBalancer 和 NodePort 类型服务的第二跳。
        :type ExternalTrafficPolicy: str
        """
        self._Type = None
        self._CLBDirectAccess = None
        self._ExternalTrafficPolicy = None

    @property
    def Type(self):
        """ClusterIP/NodePort/LoadBalancer
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CLBDirectAccess(self):
        """是否开启LB直通Pod
        :rtype: bool
        """
        return self._CLBDirectAccess

    @CLBDirectAccess.setter
    def CLBDirectAccess(self, CLBDirectAccess):
        self._CLBDirectAccess = CLBDirectAccess

    @property
    def ExternalTrafficPolicy(self):
        """服务是否希望将外部流量路由到节点本地或集群范围的端点。 有两个可用选项：Cluster（默认）和 Local。Cluster 隐藏了客户端源 IP，可能导致第二跳到另一个节点；Local 保留客户端源 IP 并避免 LoadBalancer 和 NodePort 类型服务的第二跳。
        :rtype: str
        """
        return self._ExternalTrafficPolicy

    @ExternalTrafficPolicy.setter
    def ExternalTrafficPolicy(self, ExternalTrafficPolicy):
        self._ExternalTrafficPolicy = ExternalTrafficPolicy


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._CLBDirectAccess = params.get("CLBDirectAccess")
        self._ExternalTrafficPolicy = params.get("ExternalTrafficPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDNSConfig(AbstractModel):
    """智能DNS配置

    """

    def __init__(self):
        r"""
        :param _IstioMetaDNSCapture: 开启DNS代理
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMetaDNSCapture: bool
        :param _IstioMetaDNSAutoAllocate: 开启自动地址分配
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMetaDNSAutoAllocate: bool
        """
        self._IstioMetaDNSCapture = None
        self._IstioMetaDNSAutoAllocate = None

    @property
    def IstioMetaDNSCapture(self):
        """开启DNS代理
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IstioMetaDNSCapture

    @IstioMetaDNSCapture.setter
    def IstioMetaDNSCapture(self, IstioMetaDNSCapture):
        self._IstioMetaDNSCapture = IstioMetaDNSCapture

    @property
    def IstioMetaDNSAutoAllocate(self):
        """开启自动地址分配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IstioMetaDNSAutoAllocate

    @IstioMetaDNSAutoAllocate.setter
    def IstioMetaDNSAutoAllocate(self, IstioMetaDNSAutoAllocate):
        self._IstioMetaDNSAutoAllocate = IstioMetaDNSAutoAllocate


    def _deserialize(self, params):
        self._IstioMetaDNSCapture = params.get("IstioMetaDNSCapture")
        self._IstioMetaDNSAutoAllocate = params.get("IstioMetaDNSAutoAllocate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        :param _Passthrough: 是否透传给其他关联产品
        :type Passthrough: bool
        """
        self._Key = None
        self._Value = None
        self._Passthrough = None

    @property
    def Key(self):
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Passthrough(self):
        """是否透传给其他关联产品
        :rtype: bool
        """
        return self._Passthrough

    @Passthrough.setter
    def Passthrough(self, Passthrough):
        self._Passthrough = Passthrough


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Passthrough = params.get("Passthrough")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TracingConfig(AbstractModel):
    """调用链配置

    """

    def __init__(self):
        r"""
        :param _Sampling: 调用链采样率，百分比
        :type Sampling: float
        :param _Enable: 是否启用调用跟踪
        :type Enable: bool
        :param _APM: 腾讯云 APM 服务相关参数
        :type APM: :class:`tencentcloud.tcm.v20210413.models.APM`
        :param _Zipkin: 启动第三方服务器的地址
        :type Zipkin: :class:`tencentcloud.tcm.v20210413.models.TracingZipkin`
        """
        self._Sampling = None
        self._Enable = None
        self._APM = None
        self._Zipkin = None

    @property
    def Sampling(self):
        """调用链采样率，百分比
        :rtype: float
        """
        return self._Sampling

    @Sampling.setter
    def Sampling(self, Sampling):
        self._Sampling = Sampling

    @property
    def Enable(self):
        """是否启用调用跟踪
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def APM(self):
        """腾讯云 APM 服务相关参数
        :rtype: :class:`tencentcloud.tcm.v20210413.models.APM`
        """
        return self._APM

    @APM.setter
    def APM(self, APM):
        self._APM = APM

    @property
    def Zipkin(self):
        """启动第三方服务器的地址
        :rtype: :class:`tencentcloud.tcm.v20210413.models.TracingZipkin`
        """
        return self._Zipkin

    @Zipkin.setter
    def Zipkin(self, Zipkin):
        self._Zipkin = Zipkin


    def _deserialize(self, params):
        self._Sampling = params.get("Sampling")
        self._Enable = params.get("Enable")
        if params.get("APM") is not None:
            self._APM = APM()
            self._APM._deserialize(params.get("APM"))
        if params.get("Zipkin") is not None:
            self._Zipkin = TracingZipkin()
            self._Zipkin._deserialize(params.get("Zipkin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TracingZipkin(AbstractModel):
    """调用追踪的Zipkin设置

    """

    def __init__(self):
        r"""
        :param _Address: Zipkin调用地址
        :type Address: str
        """
        self._Address = None

    @property
    def Address(self):
        """Zipkin调用地址
        :rtype: str
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
        


class UnlinkClusterRequest(AbstractModel):
    """UnlinkCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshId: 网格Id
        :type MeshId: str
        :param _ClusterId: 取消关联的集群Id
        :type ClusterId: str
        """
        self._MeshId = None
        self._ClusterId = None

    @property
    def MeshId(self):
        """网格Id
        :rtype: str
        """
        return self._MeshId

    @MeshId.setter
    def MeshId(self, MeshId):
        self._MeshId = MeshId

    @property
    def ClusterId(self):
        """取消关联的集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._MeshId = params.get("MeshId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlinkClusterResponse(AbstractModel):
    """UnlinkCluster返回参数结构体

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


class UnlinkPrometheusRequest(AbstractModel):
    """UnlinkPrometheus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MeshID: 网格ID
        :type MeshID: str
        """
        self._MeshID = None

    @property
    def MeshID(self):
        """网格ID
        :rtype: str
        """
        return self._MeshID

    @MeshID.setter
    def MeshID(self, MeshID):
        self._MeshID = MeshID


    def _deserialize(self, params):
        self._MeshID = params.get("MeshID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlinkPrometheusResponse(AbstractModel):
    """UnlinkPrometheus返回参数结构体

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


class WorkloadConfig(AbstractModel):
    """工作负载配置

    """

    def __init__(self):
        r"""
        :param _Replicas: 工作副本数
        :type Replicas: int
        :param _Resources: 资源配置
        :type Resources: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        :param _HorizontalPodAutoscaler: HPA策略
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tcm.v20210413.models.HorizontalPodAutoscalerSpec`
        :param _SelectedNodeList: 部署到指定节点
        :type SelectedNodeList: list of str
        :param _DeployMode: 组件的部署模式，取值说明：
IN_GENERAL_NODE：常规节点
IN_EKLET：eklet 节点
IN_SHARED_NODE_POOL：共享节电池
IN_EXCLUSIVE_NODE_POOL：独占节点池
        :type DeployMode: str
        """
        self._Replicas = None
        self._Resources = None
        self._HorizontalPodAutoscaler = None
        self._SelectedNodeList = None
        self._DeployMode = None

    @property
    def Replicas(self):
        """工作副本数
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Resources(self):
        """资源配置
        :rtype: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def HorizontalPodAutoscaler(self):
        """HPA策略
        :rtype: :class:`tencentcloud.tcm.v20210413.models.HorizontalPodAutoscalerSpec`
        """
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def SelectedNodeList(self):
        """部署到指定节点
        :rtype: list of str
        """
        return self._SelectedNodeList

    @SelectedNodeList.setter
    def SelectedNodeList(self, SelectedNodeList):
        self._SelectedNodeList = SelectedNodeList

    @property
    def DeployMode(self):
        """组件的部署模式，取值说明：
IN_GENERAL_NODE：常规节点
IN_EKLET：eklet 节点
IN_SHARED_NODE_POOL：共享节电池
IN_EXCLUSIVE_NODE_POOL：独占节点池
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode


    def _deserialize(self, params):
        self._Replicas = params.get("Replicas")
        if params.get("Resources") is not None:
            self._Resources = ResourceRequirements()
            self._Resources._deserialize(params.get("Resources"))
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscalerSpec()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self._SelectedNodeList = params.get("SelectedNodeList")
        self._DeployMode = params.get("DeployMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        