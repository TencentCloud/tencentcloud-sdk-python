# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 注册引擎实例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeSREInstanceAccessAddressResponse(AbstractModel):
    """DescribeSREInstanceAccessAddress返回参数结构体

    """

    def __init__(self):
        """
        :param IntranetAddress: 内网访问地址
        :type IntranetAddress: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntranetAddress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntranetAddress = params.get("IntranetAddress")
        self.RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 请求过滤参数
        :type Filters: list of Filter
        :param Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSREInstancesResponse(AbstractModel):
    """DescribeSREInstances返回参数结构体

    """

    def __init__(self):
        """
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


class Filter(AbstractModel):
    """查询过滤通用对象

    """

    def __init__(self):
        """
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


class ManageConfigRequest(AbstractModel):
    """ManageConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Type: 配置中心类型（consul、zookeeper、apollo等）
        :type Type: str
        :param Command: 请求命名 PUT GET DELETE
        :type Command: str
        :param Key: 配置的Key
        :type Key: str
        :param Value: 配置的Value
        :type Value: str
        """
        self.InstanceId = None
        self.Type = None
        self.Command = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Command = params.get("Command")
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class ManageConfigResponse(AbstractModel):
    """ManageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 对配置中心操作配置之后的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        """
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