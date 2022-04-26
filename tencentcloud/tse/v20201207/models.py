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


class BoundK8SInfo(AbstractModel):
    """服务治理引擎绑定的kubernetes信息

    """

    def __init__(self):
        r"""
        :param BoundClusterId: 绑定的kubernetes集群ID
        :type BoundClusterId: str
        :param BoundClusterType: 绑定的kubernetes的集群类型，分tke和eks两种
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundClusterType: str
        :param SyncMode: 服务同步模式，all为全量同步，demand为按需同步
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncMode: str
        """
        self.BoundClusterId = None
        self.BoundClusterType = None
        self.SyncMode = None


    def _deserialize(self, params):
        self.BoundClusterId = params.get("BoundClusterId")
        self.BoundClusterType = params.get("BoundClusterType")
        self.SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 注册引擎实例Id
        :type InstanceId: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressResponse(AbstractModel):
    """DescribeSREInstanceAccessAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntranetAddress: 内网访问地址
        :type IntranetAddress: str
        :param InternetAddress: 公网访问地址
        :type InternetAddress: str
        :param EnvAddressInfos: apollo多环境公网ip
        :type EnvAddressInfos: list of EnvAddressInfo
        :param ConsoleInternetAddress: 控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetAddress: str
        :param ConsoleIntranetAddress: 控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleIntranetAddress: str
        :param InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        :param ConsoleInternetBandWidth: 控制台公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetBandWidth: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntranetAddress = None
        self.InternetAddress = None
        self.EnvAddressInfos = None
        self.ConsoleInternetAddress = None
        self.ConsoleIntranetAddress = None
        self.InternetBandWidth = None
        self.ConsoleInternetBandWidth = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntranetAddress = params.get("IntranetAddress")
        self.InternetAddress = params.get("InternetAddress")
        if params.get("EnvAddressInfos") is not None:
            self.EnvAddressInfos = []
            for item in params.get("EnvAddressInfos"):
                obj = EnvAddressInfo()
                obj._deserialize(item)
                self.EnvAddressInfos.append(obj)
        self.ConsoleInternetAddress = params.get("ConsoleInternetAddress")
        self.ConsoleIntranetAddress = params.get("ConsoleIntranetAddress")
        self.InternetBandWidth = params.get("InternetBandWidth")
        self.ConsoleInternetBandWidth = params.get("ConsoleInternetBandWidth")
        self.RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 请求过滤参数
        :type Filters: list of Filter
        :param Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        :param QueryType: 查询类型
        :type QueryType: str
        :param QuerySource: 调用方来源
        :type QuerySource: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.QueryType = None
        self.QuerySource = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.QueryType = params.get("QueryType")
        self.QuerySource = params.get("QuerySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstancesResponse(AbstractModel):
    """DescribeSREInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param Content: 实例记录
        :type Content: list of SREInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SREInstance()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class EnvAddressInfo(AbstractModel):
    """多环境网络信息

    """

    def __init__(self):
        r"""
        :param EnvName: 环境名
        :type EnvName: str
        :param EnableConfigInternet: 是否开启config公网
        :type EnableConfigInternet: bool
        :param ConfigInternetServiceIp: config公网ip
        :type ConfigInternetServiceIp: str
        """
        self.EnvName = None
        self.EnableConfigInternet = None
        self.ConfigInternetServiceIp = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        self.EnableConfigInternet = params.get("EnableConfigInternet")
        self.ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境具体信息

    """

    def __init__(self):
        r"""
        :param EnvName: 环境名称
        :type EnvName: str
        :param VpcInfos: 环境对应的网络信息
        :type VpcInfos: list of VpcInfo
        :param StorageCapacity: 云硬盘容量
        :type StorageCapacity: int
        :param Status: 运行状态
        :type Status: str
        :param AdminServiceIp: Admin service 访问地址
        :type AdminServiceIp: str
        :param ConfigServiceIp: Config service访问地址
        :type ConfigServiceIp: str
        :param EnableConfigInternet: 是否开启config-server公网
        :type EnableConfigInternet: bool
        :param ConfigInternetServiceIp: config-server公网访问地址
        :type ConfigInternetServiceIp: str
        :param SpecId: 规格ID
        :type SpecId: str
        :param EnvReplica: 环境的节点数
        :type EnvReplica: int
        :param RunningCount: 环境运行的节点数
        :type RunningCount: int
        """
        self.EnvName = None
        self.VpcInfos = None
        self.StorageCapacity = None
        self.Status = None
        self.AdminServiceIp = None
        self.ConfigServiceIp = None
        self.EnableConfigInternet = None
        self.ConfigInternetServiceIp = None
        self.SpecId = None
        self.EnvReplica = None
        self.RunningCount = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        self.StorageCapacity = params.get("StorageCapacity")
        self.Status = params.get("Status")
        self.AdminServiceIp = params.get("AdminServiceIp")
        self.ConfigServiceIp = params.get("ConfigServiceIp")
        self.EnableConfigInternet = params.get("EnableConfigInternet")
        self.ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self.SpecId = params.get("SpecId")
        self.EnvReplica = params.get("EnvReplica")
        self.RunningCount = params.get("RunningCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤通用对象

    """

    def __init__(self):
        r"""
        :param Name: 过滤参数名
        :type Name: str
        :param Values: 过滤参数值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Name: 名称
        :type Name: str
        :param Edition: 版本号
        :type Edition: str
        :param Status: 状态, 枚举值:creating/create_fail/running/updating/update_fail/restarting/restart_fail/destroying/destroy_fail
        :type Status: str
        :param SpecId: 规格ID
        :type SpecId: str
        :param Replica: 副本数
        :type Replica: int
        :param Type: 类型
        :type Type: str
        :param VpcId: Vpc iD
        :type VpcId: str
        :param SubnetIds: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param EnableStorage: 是否开启持久化存储
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableStorage: bool
        :param StorageType: 数据存储方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param StorageCapacity: 云硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageCapacity: int
        :param Paymode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param EKSClusterID: EKS集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSClusterID: str
        :param CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param EnvInfos: 环境配置信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvInfos: list of EnvInfo
        :param EngineRegion: 引擎所在的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param EnableInternet: 注册引擎是否开启公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableInternet: bool
        :param VpcInfos: 私有网络列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfos: list of VpcInfo
        :param ServiceGovernanceInfos: 服务治理相关信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGovernanceInfos: list of ServiceGovernanceInfo
        :param Tags: 实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of KVPair
        :param EnableConsoleInternet: 引擎实例是否开启控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleInternet: bool
        :param EnableConsoleIntranet: 引擎实例是否开启控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleIntranet: bool
        :param ConfigInfoVisible: 引擎实例是否展示参数配置页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigInfoVisible: bool
        :param ConsoleDefaultPwd: 引擎实例控制台默认密码
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleDefaultPwd: str
        :param TradeType: 交易付费类型，0后付费/1预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeType: int
        :param AutoRenewFlag: 自动续费标记：0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param CurDeadline: 预付费到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param IsolateTime: 隔离开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        """
        self.InstanceId = None
        self.Name = None
        self.Edition = None
        self.Status = None
        self.SpecId = None
        self.Replica = None
        self.Type = None
        self.VpcId = None
        self.SubnetIds = None
        self.EnableStorage = None
        self.StorageType = None
        self.StorageCapacity = None
        self.Paymode = None
        self.EKSClusterID = None
        self.CreateTime = None
        self.EnvInfos = None
        self.EngineRegion = None
        self.EnableInternet = None
        self.VpcInfos = None
        self.ServiceGovernanceInfos = None
        self.Tags = None
        self.EnableConsoleInternet = None
        self.EnableConsoleIntranet = None
        self.ConfigInfoVisible = None
        self.ConsoleDefaultPwd = None
        self.TradeType = None
        self.AutoRenewFlag = None
        self.CurDeadline = None
        self.IsolateTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Edition = params.get("Edition")
        self.Status = params.get("Status")
        self.SpecId = params.get("SpecId")
        self.Replica = params.get("Replica")
        self.Type = params.get("Type")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.EnableStorage = params.get("EnableStorage")
        self.StorageType = params.get("StorageType")
        self.StorageCapacity = params.get("StorageCapacity")
        self.Paymode = params.get("Paymode")
        self.EKSClusterID = params.get("EKSClusterID")
        self.CreateTime = params.get("CreateTime")
        if params.get("EnvInfos") is not None:
            self.EnvInfos = []
            for item in params.get("EnvInfos"):
                obj = EnvInfo()
                obj._deserialize(item)
                self.EnvInfos.append(obj)
        self.EngineRegion = params.get("EngineRegion")
        self.EnableInternet = params.get("EnableInternet")
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        if params.get("ServiceGovernanceInfos") is not None:
            self.ServiceGovernanceInfos = []
            for item in params.get("ServiceGovernanceInfos"):
                obj = ServiceGovernanceInfo()
                obj._deserialize(item)
                self.ServiceGovernanceInfos.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = KVPair()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnableConsoleInternet = params.get("EnableConsoleInternet")
        self.EnableConsoleIntranet = params.get("EnableConsoleIntranet")
        self.ConfigInfoVisible = params.get("ConfigInfoVisible")
        self.ConsoleDefaultPwd = params.get("ConsoleDefaultPwd")
        self.TradeType = params.get("TradeType")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CurDeadline = params.get("CurDeadline")
        self.IsolateTime = params.get("IsolateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGovernanceInfo(AbstractModel):
    """服务治理相关的信息

    """

    def __init__(self):
        r"""
        :param EngineRegion: 引擎所在的地域
        :type EngineRegion: str
        :param BoundK8SInfos: 服务治理引擎绑定的kubernetes集群信息
        :type BoundK8SInfos: list of BoundK8SInfo
        :param VpcInfos: 服务治理引擎绑定的网络信息
        :type VpcInfos: list of VpcInfo
        :param AuthOpen: 当前实例鉴权是否开启
        :type AuthOpen: bool
        :param Features: 该实例支持的功能，鉴权就是 Auth
        :type Features: list of str
        :param MainPassword: 主账户名默认为 polaris，该值为主账户的默认密码
        :type MainPassword: str
        """
        self.EngineRegion = None
        self.BoundK8SInfos = None
        self.VpcInfos = None
        self.AuthOpen = None
        self.Features = None
        self.MainPassword = None


    def _deserialize(self, params):
        self.EngineRegion = params.get("EngineRegion")
        if params.get("BoundK8SInfos") is not None:
            self.BoundK8SInfos = []
            for item in params.get("BoundK8SInfos"):
                obj = BoundK8SInfo()
                obj._deserialize(item)
                self.BoundK8SInfos.append(obj)
        if params.get("VpcInfos") is not None:
            self.VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcInfos.append(obj)
        self.AuthOpen = params.get("AuthOpen")
        self.Features = params.get("Features")
        self.MainPassword = params.get("MainPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """私有网络信息

    """

    def __init__(self):
        r"""
        :param VpcId: Vpc Id
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param IntranetAddress: 内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.IntranetAddress = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.IntranetAddress = params.get("IntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        