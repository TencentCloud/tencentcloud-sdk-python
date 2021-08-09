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


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 注册引擎实例Id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        """
        :param IntranetAddress: 内网访问地址\n        :type IntranetAddress: str\n        :param InternetAddress: 公网访问地址\n        :type InternetAddress: str\n        :param EnvAddressInfos: apollo多环境公网ip\n        :type EnvAddressInfos: list of EnvAddressInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IntranetAddress = None
        self.InternetAddress = None
        self.EnvAddressInfos = None
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
        self.RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 请求过滤参数\n        :type Filters: list of Filter\n        :param Limit: 翻页单页查询限制数量[0,1000], 默认值0\n        :type Limit: int\n        :param Offset: 翻页单页偏移量，默认值0\n        :type Offset: int\n        :param QueryType: 查询类型\n        :type QueryType: str\n        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.QueryType = None


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
        """
        :param TotalCount: 总数量\n        :type TotalCount: int\n        :param Content: 实例记录\n        :type Content: list of SREInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param EnvName: 环境名\n        :type EnvName: str\n        :param EnableConfigInternet: 是否开启config公网\n        :type EnableConfigInternet: bool\n        :param ConfigInternetServiceIp: config公网ip\n        :type ConfigInternetServiceIp: str\n        """
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
        """
        :param EnvName: 环境名称\n        :type EnvName: str\n        :param VpcInfos: 环境对应的网络信息\n        :type VpcInfos: list of VpcInfo\n        :param StorageCapacity: 云硬盘容量\n        :type StorageCapacity: int\n        :param Status: 运行状态\n        :type Status: str\n        :param AdminServiceIp: Admin service 访问地址\n        :type AdminServiceIp: str\n        :param ConfigServiceIp: Config service访问地址\n        :type ConfigServiceIp: str\n        :param EnableConfigInternet: 是否开启config-server公网\n        :type EnableConfigInternet: bool\n        :param ConfigInternetServiceIp: config-server公网访问地址\n        :type ConfigInternetServiceIp: str\n        """
        self.EnvName = None
        self.VpcInfos = None
        self.StorageCapacity = None
        self.Status = None
        self.AdminServiceIp = None
        self.ConfigServiceIp = None
        self.EnableConfigInternet = None
        self.ConfigInternetServiceIp = None


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
        """
        :param Name: 过滤参数名\n        :type Name: str\n        :param Values: 过滤参数值\n        :type Values: list of str\n        """
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
        


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Name: 名称\n        :type Name: str\n        :param Edition: 版本号\n        :type Edition: str\n        :param Status: 状态, 枚举值:creating/create_fail/running/updating/update_fail/restarting/restart_fail/destroying/destroy_fail\n        :type Status: str\n        :param SpecId: 规格ID\n        :type SpecId: str\n        :param Replica: 副本数\n        :type Replica: int\n        :param Type: 类型\n        :type Type: str\n        :param VpcId: Vpc iD\n        :type VpcId: str\n        :param SubnetIds: 子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetIds: list of str\n        :param EnableStorage: 是否开启持久化存储
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableStorage: bool\n        :param StorageType: 数据存储方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageType: str\n        :param StorageCapacity: 云硬盘容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageCapacity: int\n        :param Paymode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type Paymode: str\n        :param EKSClusterID: EKS集群的ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EKSClusterID: str\n        :param CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param EnvInfos: 环境配置信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvInfos: list of EnvInfo\n        :param EngineRegion: 引擎所在的区域
注意：此字段可能返回 null，表示取不到有效值。\n        :type EngineRegion: str\n        :param EnableInternet: 注册引擎是否开启公网
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableInternet: bool\n        """
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
        """
        :param VpcId: Vpc Id\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        