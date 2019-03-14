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


class CosBackup(AbstractModel):
    """ES cos自动备份信息

    """

    def __init__(self):
        """
        :param IsAutoBackup: 是否开启cos自动备份
        :type IsAutoBackup: bool
        :param BackupTime: 自动备份时间
        :type BackupTime: str
        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区
        :type Zone: str
        :param NodeNum: 节点数量
        :type NodeNum: int
        :param EsVersion: 实例版本,支持"5.6.4"、"6.4.3"
        :type EsVersion: str
        :param NodeType: 节点规格： 
ES.S1.SMALL2: 1核2G
ES.S1.MEDIUM4: 2核4G
ES.S1.MEDIUM8: 2核8G
ES.S1.LARGE16: 4核16G
ES.S1.2XLARGE32: 8核32G
ES.S1.4XLARGE64: 16核64G
        :type NodeType: str
        :param DiskSize: 节点存储容量，单位GB
        :type DiskSize: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Password: 访问密码，密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[()`~!@#$%^&*-+=_|{}:;' <>,.?/]的特殊符号
        :type Password: str
        :param InstanceName: 实例名称，1-50 个英文、汉字、数字、连接线-或下划线_
        :type InstanceName: str
        :param ChargeType: 计费类型: 
PREPAID：预付费，即包年包月 
POSTPAID_BY_HOUR：按小时后付费，默认值
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长，单位由TimeUint决定，默认为月
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识，取值范围： 
RENEW_FLAG_AUTO：自动续费
RENEW_FLAG_MANUAL：不自动续费，用户手动续费
如不传递该参数，普通用于默认不自动续费，SVIP用户自动续费
        :type RenewFlag: str
        :param DiskType: 节点存储类型,取值范围:    
CLOUD_PREMIUM: 高硬能云硬盘  
CLOUD_SSD: SSD云硬盘
        :type DiskType: str
        :param TimeUnit: 计费时长单位，当前只支持“m”，表示月
        :type TimeUnit: str
        :param AutoVoucher: 是否自动使用代金券，1是，0否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        :param EnableDedicatedMaster: 是否创建专用主节点
        :type EnableDedicatedMaster: bool
        :param MasterNodeNum: 专用主节点个数
        :type MasterNodeNum: int
        :param MasterNodeType: 专用主节点类型，与NodeType支持的规格相同
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 专用主节点磁盘大小，单位GB（系统默认配置50GB，暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param ClusterNameInConf: 配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）
        :type ClusterNameInConf: str
        """
        self.Zone = None
        self.NodeNum = None
        self.EsVersion = None
        self.NodeType = None
        self.DiskSize = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.DiskType = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.EsVersion = params.get("EsVersion")
        self.NodeType = params.get("NodeType")
        self.DiskSize = params.get("DiskSize")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.DiskType = params.get("DiskType")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要销毁的实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param LogType: 日志类型
        :type LogType: int
        :param SearchKey: 搜索词
        :type SearchKey: str
        :param StartTime: 日志开始时间
        :type StartTime: str
        :param EndTime: 日志结束时间
        :type EndTime: str
        :param Offset: 分页起始值
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        :param OrderByType: 时间排序方式
        :type OrderByType: int
        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的日志条数
        :type TotalCount: int
        :param InstanceLogList: 日志详细信息列表
        :type InstanceLogList: list of InstanceLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 分页起始值
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 操作记录总数
        :type TotalCount: int
        :param Operations: 操作记录
        :type Operations: list of Operation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 集群实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param InstanceIds: 一个或多个集群实例ID
        :type InstanceIds: list of str
        :param InstanceNames: 一个或多个集群实例名称
        :type InstanceNames: list of str
        :param Offset: 分页起始值, 默认值0
        :type Offset: int
        :param Limit: 分页大小，默认值20
        :type Limit: int
        :param OrderByKey: 排序字段：1，实例ID；2，实例名称；3，可用区；4，创建时间，若orderKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param OrderByType: 排序方式：0，升序；1，降序；若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的实例个数
        :type TotalCount: int
        :param InstanceList: 实例详细信息列表
        :type InstanceList: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """ik插件词典新

    """

    def __init__(self):
        """
        :param Key: 词典键值
        :type Key: str
        :param Name: 词典名称
        :type Name: str
        :param Size: 词典大小，单位B
        :type Size: int
        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")


class EsAcl(AbstractModel):
    """ES集群配置项

    """

    def __init__(self):
        """
        :param BlackIpList: kibana访问黑名单
        :type BlackIpList: list of str
        :param WhiteIpList: kibana访问白名单
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")


class EsDictionaryInfo(AbstractModel):
    """ES IK词库信息

    """

    def __init__(self):
        """
        :param MainDict: 启用词词典列表
        :type MainDict: list of DictInfo
        :param Stopwords: 停用词词典列表
        :type Stopwords: list of DictInfo
        """
        self.MainDict = None
        self.Stopwords = None


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self.MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self.Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Stopwords.append(obj)


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param AppId: 用户ID
        :type AppId: int
        :param Uin: 用户UIN
        :type Uin: str
        :param VpcUid: 实例所属VPC的UID
        :type VpcUid: str
        :param SubnetUid: 实例所属子网的UID
        :type SubnetUid: str
        :param Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :type Status: int
        :param ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param NodeType: 节点规格:  ES.S1.SMALL2 : 1核2G  ES.S1.MEDIUM4 : 2核4G  ES.S1.MEDIUM8 : 2核8G  ES.S1.LARGE16 : 4核16G  ES.S1.2XLARGE32 : 8核32G  ES.S1.3XLARGE32 : 12核32G  ES.S1.6XLARGE32 : 24核32G
        :type NodeType: str
        :param NodeNum: 节点个数
        :type NodeNum: int
        :param CpuNum: 节点CPU核数
        :type CpuNum: int
        :param MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param DiskType: 节点磁盘类型
        :type DiskType: str
        :param DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param EsDomain: ES域名
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES端口
        :type EsPort: int
        :param KibanaUrl: Kibana访问url
        :type KibanaUrl: str
        :param EsVersion: ES版本号
        :type EsVersion: str
        :param EsConfig: ES配置项
        :type EsConfig: str
        :param EsAcl: ES访问控制配置
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        :param Deadline: 实例到期时间
        :type Deadline: str
        :param InstanceType: 实例类型（实例类型标识，当前只有1,2两种）
        :type InstanceType: int
        :param IkConfig: Ik分词器配置
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param MasterNodeInfo: 专用主节点配置
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param CosBackup: cos自动备份配置
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param AllowCosBackup: 是否允许cos自动备份
        :type AllowCosBackup: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.InstanceType = None
        self.IkConfig = None
        self.MasterNodeInfo = None
        self.CosBackup = None
        self.AllowCosBackup = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        self.InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self.IkConfig = EsDictionaryInfo()
            self.IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self.MasterNodeInfo = MasterNodeInfo()
            self.MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        self.AllowCosBackup = params.get("AllowCosBackup")


class InstanceLog(AbstractModel):
    """ES集群日志详细信息

    """

    def __init__(self):
        """
        :param Time: 日志时间
        :type Time: str
        :param Level: 日志级别
        :type Level: str
        :param Ip: 集群节点ip
        :type Ip: str
        :param Message: 日志内容
        :type Message: str
        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")


class KeyValue(AbstractModel):
    """OperationDetail使用此结构的数组描述新旧配置

    """

    def __init__(self):
        """
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


class MasterNodeInfo(AbstractModel):
    """实例专用主节点相关信息

    """

    def __init__(self):
        """
        :param EnableDedicatedMaster: 是否启用了专用主节点
        :type EnableDedicatedMaster: bool
        :param MasterNodeType: 专用主节点规格
        :type MasterNodeType: str
        :param MasterNodeNum: 专用主节点个数
        :type MasterNodeNum: int
        :param MasterNodeCpuNum: 专用主节点CPU核数
        :type MasterNodeCpuNum: int
        :param MasterNodeMemSize: 专用主节点内存大小，单位GB
        :type MasterNodeMemSize: int
        :param MasterNodeDiskSize: 专用主节点磁盘大小，单位GB
        :type MasterNodeDiskSize: int
        :param MasterNodeDiskType: 专用主节点磁盘类型
        :type MasterNodeDiskType: str
        """
        self.EnableDedicatedMaster = None
        self.MasterNodeType = None
        self.MasterNodeNum = None
        self.MasterNodeCpuNum = None
        self.MasterNodeMemSize = None
        self.MasterNodeDiskSize = None
        self.MasterNodeDiskType = None


    def _deserialize(self, params):
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self.MasterNodeMemSize = params.get("MasterNodeMemSize")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.MasterNodeDiskType = params.get("MasterNodeDiskType")


class Operation(AbstractModel):
    """ES集群操作详细信息

    """

    def __init__(self):
        """
        :param Id: 操作唯一id
        :type Id: int
        :param StartTime: 操作开始时间
        :type StartTime: str
        :param Type: 操作类型
        :type Type: str
        :param Detail: 操作详情
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param Result: 操作结果
        :type Result: str
        :param Tasks: 流程任务信息
        :type Tasks: list of TaskDetail
        :param Progress: 操作进度
        :type Progress: float
        """
        self.Id = None
        self.StartTime = None
        self.Type = None
        self.Detail = None
        self.Result = None
        self.Tasks = None
        self.Progress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        if params.get("Detail") is not None:
            self.Detail = OperationDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.Result = params.get("Result")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Progress = params.get("Progress")


class OperationDetail(AbstractModel):
    """操作详情

    """

    def __init__(self):
        """
        :param OldInfo: 实例原始配置信息
        :type OldInfo: list of KeyValue
        :param NewInfo: 实例更新后配置信息
        :type NewInfo: list of KeyValue
        """
        self.OldInfo = None
        self.NewInfo = None


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self.OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self.NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.NewInfo.append(obj)


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要重启的实例ID
        :type InstanceId: str
        :param ForceRestart: 是否强制重启
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """实例操作记录流程任务中的子任务信息（如升级检查任务中的各个检查项）

    """

    def __init__(self):
        """
        :param Name: 子任务名
        :type Name: str
        :param Result: 子任务结果
        :type Result: bool
        :param ErrMsg: 子任务错误信息
        :type ErrMsg: str
        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")


class TaskDetail(AbstractModel):
    """实例操作记录中的流程任务信息

    """

    def __init__(self):
        """
        :param Name: 任务名
        :type Name: str
        :param Progress: 任务进度
        :type Progress: float
        :param FinishTime: 任务完成时间
        :type FinishTime: str
        :param SubTasks: 子任务
        :type SubTasks: list of SubTaskDetail
        """
        self.Name = None
        self.Progress = None
        self.FinishTime = None
        self.SubTasks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Progress = params.get("Progress")
        self.FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self.SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self.SubTasks.append(obj)


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要操作的实例ID
        :type InstanceId: str
        :param InstanceName: 修改后的实例名称, 1-50 个英文、汉字、数字、连接线-或下划线_
        :type InstanceName: str
        :param NodeNum: 横向扩缩容后的节点个数
        :type NodeNum: int
        :param EsConfig: 修改后的配置项, JSON格式字符串。当前仅支持以下配置项：
action.destructive_requires_name
indices.fielddata.cache.size
indices.query.bool.max_clause_count
        :type EsConfig: str
        :param Password: 重置后的Kibana密码, 8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号
        :type Password: str
        :param EsAcl: 修改后的访问控制列表
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param DiskSize: 磁盘大小,单位GB
        :type DiskSize: int
        :param NodeType: 节点规格: 
ES.S1.SMALL2: 1 核 2G
ES.S1.MEDIUM4: 2 核 4G 
ES.S1.MEDIUM8: 2 核 8G 
ES.S1.LARGE16: 4 核 16G 
ES.S1.2XLARGE32: 8 核 32G 
ES.S1.4XLARGE64: 16 核 64G
        :type NodeType: str
        :param MasterNodeNum: 专用主节点个数
        :type MasterNodeNum: int
        :param MasterNodeType: 专用主节点规格，与NodeType支持的规格相同
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 专用主节点磁盘大小， 单位GB（系统默认配置为50GB,暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param ForceRestart: 更新配置时是否强制重启
        :type ForceRestart: bool
        :param CosBackup: COS自动备份信息
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None
        self.DiskSize = None
        self.NodeType = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ForceRestart = None
        self.CosBackup = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.DiskSize = params.get("DiskSize")
        self.NodeType = params.get("NodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")