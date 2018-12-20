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


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param ReplicateSetNum: 副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10
        :type ReplicateSetNum: int
        :param SecondaryNum: 每个副本集内从节点个数，目前只支持从节点数为2
        :type SecondaryNum: int
        :param EngineVersion: MongoDB引擎版本，值包括：MONGO_2、MONGO_3_MMAP、MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT
        :type EngineVersion: str
        :param Machine: 实例类型，GIO：高IO版；TGIO：高IO万兆
        :type Machine: str
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 可用区信息，格式如：ap-guangzhou-2
        :type Zone: str
        :param InstanceRole: 实例角色，支持值包括：MASTER-表示主实例，DR-表示灾备实例，RO-表示只读实例
        :type InstanceRole: str
        :param InstanceType: 实例类型，REPLSET-副本集，SHARD-分片集群
        :type InstanceType: str
        :param Encrypt: 数据是否加密，当且仅当引擎版本为MONGO_3_ROCKS，可以选择加密
        :type Encrypt: int
        :param VpcId: 私有网络ID，如果不传则默认选择基础网络
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type SubnetId: str
        :param ProjectId: 项目ID，不填为默认项目
        :type ProjectId: int
        :param SecurityGroup: 安全组参数
        :type SecurityGroup: list of str
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.EngineVersion = None
        self.Machine = None
        self.GoodsNum = None
        self.Zone = None
        self.InstanceRole = None
        self.InstanceType = None
        self.Encrypt = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.EngineVersion = params.get("EngineVersion")
        self.Machine = params.get("Machine")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.InstanceRole = params.get("InstanceRole")
        self.InstanceType = params.get("InstanceType")
        self.Encrypt = params.get("Encrypt")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param SecondaryNum: 每个副本集内从节点个数
        :type SecondaryNum: int
        :param Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param MongoVersion: 版本号，当前仅支持 MONGO_3_WT
        :type MongoVersion: str
        :param MachineCode: 机器类型，GIO：高IO版；TGIO：高IO万兆
        :type MachineCode: str
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2
        :type Zone: str
        :param TimeSpan: 时长，购买月数
        :type TimeSpan: int
        :param Password: 实例密码
        :type Password: str
        :param ProjectId: 项目ID，不填为默认项目
        :type ProjectId: int
        :param SecurityGroup: 安全组参数
        :type SecurityGroup: list of str
        :param UniqVpcId: 私有网络ID，如果不传则默认选择基础网络
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type UniqSubnetId: str
        """
        self.SecondaryNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.TimeSpan = None
        self.Password = None
        self.ProjectId = None
        self.SecurityGroup = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.SecondaryNum = params.get("SecondaryNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.TimeSpan = params.get("TimeSpan")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 订单ID，表示注销实例成功
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    """UpgradeDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：GB
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB
        :type Volume: int
        :param OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceHourResponse(AbstractModel):
    """UpgradeDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：GB
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB
        :type Volume: int
        :param OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")