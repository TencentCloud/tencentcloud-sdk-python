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


class CosBackup(AbstractModel):
    """ES cos自动备份信息

    """

    def __init__(self):
        """
        :param IsAutoBackup: 是否开启cos自动备份\n        :type IsAutoBackup: bool\n        :param BackupTime: 自动备份执行时间（精确到小时）, e.g. "22:00"\n        :type BackupTime: str\n        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        :param EsVersion: 实例版本（支持"5.6.4"、"6.4.3"、"6.8.2"、"7.5.1"、"7.10.1"）\n        :type EsVersion: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param Password: 访问密码（密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）\n        :type Password: str\n        :param InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）\n        :type InstanceName: str\n        :param NodeNum: 已废弃请使用NodeInfoList
节点数量（2-50个）\n        :type NodeNum: int\n        :param ChargeType: 计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR\n        :type ChargeType: str\n        :param ChargePeriod: 包年包月购买时长（单位由参数TimeUnit决定）\n        :type ChargePeriod: int\n        :param RenewFlag: 自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费\n        :type RenewFlag: str\n        :param NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type NodeType: str\n        :param DiskType: 已废弃请使用NodeInfoList
节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD\n        :type DiskType: str\n        :param DiskSize: 已废弃请使用NodeInfoList
节点磁盘容量（单位GB）\n        :type DiskSize: int\n        :param TimeUnit: 计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）\n        :type TimeUnit: str\n        :param AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）\n        :type VoucherIds: list of str\n        :param EnableDedicatedMaster: 已废弃请使用NodeInfoList
是否创建专用主节点<li>true：开启专用主节点</li><li>false：不开启专用主节点</li>默认值false\n        :type EnableDedicatedMaster: bool\n        :param MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个和5个，EnableDedicatedMaster为true时该值必传）\n        :type MasterNodeNum: int\n        :param MasterNodeType: 已废弃请使用NodeInfoList
专用主节点类型（EnableDedicatedMaster为true时必传）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type MasterNodeType: str\n        :param MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB，非必传，若传递则必须为50，暂不支持自定义）\n        :type MasterNodeDiskSize: int\n        :param ClusterNameInConf: 集群配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）\n        :type ClusterNameInConf: str\n        :param DeployMode: 集群部署方式<li>0：单可用区部署</li><li>1：多可用区部署</li>默认为0\n        :type DeployMode: int\n        :param MultiZoneInfo: 多可用区部署时可用区的详细信息(DeployMode为1时必传)\n        :type MultiZoneInfo: list of ZoneDetail\n        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum\n        :type LicenseType: str\n        :param NodeInfoList: 节点信息列表， 用于描述集群各类节点的规格信息如节点类型，节点个数，节点规格，磁盘类型，磁盘大小等\n        :type NodeInfoList: list of NodeInfo\n        :param TagList: 节点标签信息列表\n        :type TagList: list of TagInfo\n        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>\n        :type BasicSecurityType: int\n        :param SceneType: 场景化模板类型 0：不启用 1：通用 2：日志 3：搜索\n        :type SceneType: int\n        :param WebNodeTypeInfo: 可视化节点配置\n        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`\n        """
        self.Zone = None
        self.EsVersion = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.NodeNum = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None
        self.DeployMode = None
        self.MultiZoneInfo = None
        self.LicenseType = None
        self.NodeInfoList = None
        self.TagList = None
        self.BasicSecurityType = None
        self.SceneType = None
        self.WebNodeTypeInfo = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.EsVersion = params.get("EsVersion")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")
        self.DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID\n        :type InstanceId: str\n        :param LogType: 日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 搜索慢日志</li>
<li>3, 索引慢日志</li>
<li>4, GC日志</li>\n        :type LogType: int\n        :param SearchKey: 搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等\n        :type SearchKey: str\n        :param StartTime: 日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53\n        :type StartTime: str\n        :param EndTime: 日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53\n        :type EndTime: str\n        :param Offset: 分页起始值, 默认值为0\n        :type Offset: int\n        :param Limit: 分页大小，默认值为100，最大值100\n        :type Limit: int\n        :param OrderByType: 时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>\n        :type OrderByType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的日志条数\n        :type TotalCount: int\n        :param InstanceLogList: 日志详细信息列表\n        :type InstanceLogList: list of InstanceLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 集群实例ID\n        :type InstanceId: str\n        :param StartTime: 起始时间, e.g. "2019-03-07 16:30:39"\n        :type StartTime: str\n        :param EndTime: 结束时间, e.g. "2019-03-30 20:18:03"\n        :type EndTime: str\n        :param Offset: 分页起始值\n        :type Offset: int\n        :param Limit: 分页大小\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 操作记录总数\n        :type TotalCount: int\n        :param Operations: 操作记录\n        :type Operations: list of Operation\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Zone: 集群实例所属可用区，不传则默认所有可用区\n        :type Zone: str\n        :param InstanceIds: 集群实例ID列表\n        :type InstanceIds: list of str\n        :param InstanceNames: 集群实例名称列表\n        :type InstanceNames: list of str\n        :param Offset: 分页起始值, 默认值0\n        :type Offset: int\n        :param Limit: 分页大小，默认值20\n        :type Limit: int\n        :param OrderByKey: 排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序\n        :type OrderByKey: int\n        :param OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序\n        :type OrderByType: int\n        :param TagList: 节点标签信息列表\n        :type TagList: list of TagInfo\n        :param IpList: 私有网络vip列表\n        :type IpList: list of str\n        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None
        self.TagList = None
        self.IpList = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的实例个数\n        :type TotalCount: int\n        :param InstanceList: 实例详细信息列表\n        :type InstanceList: list of InstanceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DiagnoseInstanceRequest(AbstractModel):
    """DiagnoseInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: ES实例ID\n        :type InstanceId: str\n        :param DiagnoseJobs: 需要触发的诊断项\n        :type DiagnoseJobs: list of str\n        :param DiagnoseIndices: 需要诊断的索引，支持通配符\n        :type DiagnoseIndices: str\n        """
        self.InstanceId = None
        self.DiagnoseJobs = None
        self.DiagnoseIndices = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DiagnoseJobs = params.get("DiagnoseJobs")
        self.DiagnoseIndices = params.get("DiagnoseIndices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseInstanceResponse(AbstractModel):
    """DiagnoseInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """ik插件词典信息

    """

    def __init__(self):
        """
        :param Key: 词典键值\n        :type Key: str\n        :param Name: 词典名称\n        :type Name: str\n        :param Size: 词典大小，单位B\n        :type Size: int\n        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    """ES集群配置项

    """

    def __init__(self):
        """
        :param BlackIpList: kibana访问黑名单\n        :type BlackIpList: list of str\n        :param WhiteIpList: kibana访问白名单\n        :type WhiteIpList: list of str\n        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    """ES 词库信息

    """

    def __init__(self):
        """
        :param MainDict: 启用词词典列表\n        :type MainDict: list of DictInfo\n        :param Stopwords: 停用词词典列表\n        :type Stopwords: list of DictInfo\n        :param QQDict: QQ分词词典列表\n        :type QQDict: list of DictInfo\n        :param Synonym: 同义词词典列表\n        :type Synonym: list of DictInfo\n        :param UpdateType: 更新词典类型\n        :type UpdateType: str\n        """
        self.MainDict = None
        self.Stopwords = None
        self.QQDict = None
        self.Synonym = None
        self.UpdateType = None


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
        if params.get("QQDict") is not None:
            self.QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.QQDict.append(obj)
        if params.get("Synonym") is not None:
            self.Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Synonym.append(obj)
        self.UpdateType = params.get("UpdateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    """ES公网访问访问控制信息

    """

    def __init__(self):
        """
        :param BlackIpList: 访问黑名单\n        :type BlackIpList: list of str\n        :param WhiteIpList: 访问白名单\n        :type WhiteIpList: list of str\n        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesRequest(AbstractModel):
    """GetRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    """GetRequestTargetNodeTypes返回参数结构体

    """

    def __init__(self):
        """
        :param TargetNodeTypes: 接收请求的目标节点类型列表\n        :type TargetNodeTypes: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TargetNodeTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param Region: 地域\n        :type Region: str\n        :param Zone: 可用区\n        :type Zone: str\n        :param AppId: 用户ID\n        :type AppId: int\n        :param Uin: 用户UIN\n        :type Uin: str\n        :param VpcUid: 实例所属VPC的UID\n        :type VpcUid: str\n        :param SubnetUid: 实例所属子网的UID\n        :type SubnetUid: str\n        :param Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁\n        :type Status: int\n        :param ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。\n        :type ChargeType: str\n        :param ChargePeriod: 包年包月购买时长,单位:月\n        :type ChargePeriod: int\n        :param RenewFlag: 自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。\n        :type RenewFlag: str\n        :param NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type NodeType: str\n        :param NodeNum: 节点个数\n        :type NodeNum: int\n        :param CpuNum: 节点CPU核数\n        :type CpuNum: int\n        :param MemSize: 节点内存大小，单位GB\n        :type MemSize: int\n        :param DiskType: 节点磁盘类型\n        :type DiskType: str\n        :param DiskSize: 节点磁盘大小，单位GB\n        :type DiskSize: int\n        :param EsDomain: ES域名\n        :type EsDomain: str\n        :param EsVip: ES VIP\n        :type EsVip: str\n        :param EsPort: ES端口\n        :type EsPort: int\n        :param KibanaUrl: Kibana访问url\n        :type KibanaUrl: str\n        :param EsVersion: ES版本号\n        :type EsVersion: str\n        :param EsConfig: ES配置项\n        :type EsConfig: str\n        :param EsAcl: Kibana访问控制配置\n        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param CreateTime: 实例创建时间\n        :type CreateTime: str\n        :param UpdateTime: 实例最后修改操作时间\n        :type UpdateTime: str\n        :param Deadline: 实例到期时间\n        :type Deadline: str\n        :param InstanceType: 实例类型（实例类型标识，当前只有1,2两种）\n        :type InstanceType: int\n        :param IkConfig: Ik分词器配置\n        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`\n        :param MasterNodeInfo: 专用主节点配置\n        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`\n        :param CosBackup: cos自动备份配置\n        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`\n        :param AllowCosBackup: 是否允许cos自动备份\n        :type AllowCosBackup: bool\n        :param TagList: 实例拥有的标签列表\n        :type TagList: list of TagInfo\n        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum\n        :type LicenseType: str\n        :param EnableHotWarmMode: 是否为冷热集群<li>true: 冷热集群</li><li>false: 非冷热集群</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableHotWarmMode: bool\n        :param WarmNodeType: 冷节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmNodeType: str\n        :param WarmNodeNum: 冷节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmNodeNum: int\n        :param WarmCpuNum: 冷节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmCpuNum: int\n        :param WarmMemSize: 冷节点内存内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmMemSize: int\n        :param WarmDiskType: 冷节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmDiskType: str\n        :param WarmDiskSize: 冷节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarmDiskSize: int\n        :param NodeInfoList: 集群节点信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeInfoList: list of NodeInfo\n        :param EsPublicUrl: Es公网地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type EsPublicUrl: str\n        :param MultiZoneInfo: 多可用区网络信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type MultiZoneInfo: list of ZoneDetail\n        :param DeployMode: 部署模式<li>0：单可用区</li><li>1：多可用区</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployMode: int\n        :param PublicAccess: ES公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicAccess: str\n        :param EsPublicAcl: ES公网访问控制配置\n        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param KibanaPrivateUrl: Kibana内网地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type KibanaPrivateUrl: str\n        :param KibanaPublicAccess: Kibana公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type KibanaPublicAccess: str\n        :param KibanaPrivateAccess: Kibana内网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type KibanaPrivateAccess: str\n        :param SecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityType: int\n        :param SceneType: 场景化模板类型：0、不开启；1、通用场景；2、日志场景；3、搜索场景
注意：此字段可能返回 null，表示取不到有效值。\n        :type SceneType: int\n        :param KibanaConfig: Kibana配置项
注意：此字段可能返回 null，表示取不到有效值。\n        :type KibanaConfig: str\n        :param KibanaNodeInfo: Kibana节点信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`\n        """
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
        self.TagList = None
        self.LicenseType = None
        self.EnableHotWarmMode = None
        self.WarmNodeType = None
        self.WarmNodeNum = None
        self.WarmCpuNum = None
        self.WarmMemSize = None
        self.WarmDiskType = None
        self.WarmDiskSize = None
        self.NodeInfoList = None
        self.EsPublicUrl = None
        self.MultiZoneInfo = None
        self.DeployMode = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPrivateUrl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.SecurityType = None
        self.SceneType = None
        self.KibanaConfig = None
        self.KibanaNodeInfo = None


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
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.LicenseType = params.get("LicenseType")
        self.EnableHotWarmMode = params.get("EnableHotWarmMode")
        self.WarmNodeType = params.get("WarmNodeType")
        self.WarmNodeNum = params.get("WarmNodeNum")
        self.WarmCpuNum = params.get("WarmCpuNum")
        self.WarmMemSize = params.get("WarmMemSize")
        self.WarmDiskType = params.get("WarmDiskType")
        self.WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.SecurityType = params.get("SecurityType")
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self.KibanaNodeInfo = KibanaNodeInfo()
            self.KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """ES集群日志详细信息

    """

    def __init__(self):
        """
        :param Time: 日志时间\n        :type Time: str\n        :param Level: 日志级别\n        :type Level: str\n        :param Ip: 集群节点ip\n        :type Ip: str\n        :param Message: 日志内容\n        :type Message: str\n        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """OperationDetail使用此结构的数组描述新旧配置

    """

    def __init__(self):
        """
        :param Key: 键\n        :type Key: str\n        :param Value: 值\n        :type Value: str\n        """
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
        


class KibanaNodeInfo(AbstractModel):
    """实例Kibana节点相关信息

    """

    def __init__(self):
        """
        :param KibanaNodeType: Kibana节点规格\n        :type KibanaNodeType: str\n        :param KibanaNodeNum: Kibana节点个数\n        :type KibanaNodeNum: int\n        :param KibanaNodeCpuNum: Kibana节点CPU数\n        :type KibanaNodeCpuNum: int\n        :param KibanaNodeMemSize: Kibana节点内存GB\n        :type KibanaNodeMemSize: int\n        :param KibanaNodeDiskType: Kibana节点磁盘类型\n        :type KibanaNodeDiskType: str\n        :param KibanaNodeDiskSize: Kibana节点磁盘大小\n        :type KibanaNodeDiskSize: int\n        """
        self.KibanaNodeType = None
        self.KibanaNodeNum = None
        self.KibanaNodeCpuNum = None
        self.KibanaNodeMemSize = None
        self.KibanaNodeDiskType = None
        self.KibanaNodeDiskSize = None


    def _deserialize(self, params):
        self.KibanaNodeType = params.get("KibanaNodeType")
        self.KibanaNodeNum = params.get("KibanaNodeNum")
        self.KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self.KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self.KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self.KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    """节点本地盘信息

    """

    def __init__(self):
        """
        :param LocalDiskType: 本地盘类型<li>LOCAL_SATA：大数据型</li><li>NVME_SSD：高IO型</li>\n        :type LocalDiskType: str\n        :param LocalDiskSize: 本地盘单盘大小\n        :type LocalDiskSize: int\n        :param LocalDiskCount: 本地盘块数\n        :type LocalDiskCount: int\n        """
        self.LocalDiskType = None
        self.LocalDiskSize = None
        self.LocalDiskCount = None


    def _deserialize(self, params):
        self.LocalDiskType = params.get("LocalDiskType")
        self.LocalDiskSize = params.get("LocalDiskSize")
        self.LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    """实例专用主节点相关信息

    """

    def __init__(self):
        """
        :param EnableDedicatedMaster: 是否启用了专用主节点\n        :type EnableDedicatedMaster: bool\n        :param MasterNodeType: 专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type MasterNodeType: str\n        :param MasterNodeNum: 专用主节点个数\n        :type MasterNodeNum: int\n        :param MasterNodeCpuNum: 专用主节点CPU核数\n        :type MasterNodeCpuNum: int\n        :param MasterNodeMemSize: 专用主节点内存大小，单位GB\n        :type MasterNodeMemSize: int\n        :param MasterNodeDiskSize: 专用主节点磁盘大小，单位GB\n        :type MasterNodeDiskSize: int\n        :param MasterNodeDiskType: 专用主节点磁盘类型\n        :type MasterNodeDiskType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """集群中一种节点类型（如热数据节点，冷数据节点，专用主节点等）的规格描述信息，包括节点类型，节点个数，节点规格，磁盘类型，磁盘大小等, Type不指定时默认为热数据节点；如果节点为master节点，则DiskType和DiskSize参数会被忽略（主节点无数据盘）

    """

    def __init__(self):
        """
        :param NodeNum: 节点数量\n        :type NodeNum: int\n        :param NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type NodeType: str\n        :param Type: 节点类型<li>hotData: 热数据节点</li>
<li>warmData: 冷数据节点</li>
<li>dedicatedMaster: 专用主节点</li>
默认值为hotData\n        :type Type: str\n        :param DiskType: 节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD\n        :type DiskType: str\n        :param DiskSize: 节点磁盘容量（单位GB）\n        :type DiskSize: int\n        :param LocalDiskInfo: 节点本地盘信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`\n        :param DiskCount: 节点磁盘块数\n        :type DiskCount: int\n        :param DiskEncrypt: 节点磁盘是否加密 0: 不加密，1: 加密；默认不加密\n        :type DiskEncrypt: int\n        """
        self.NodeNum = None
        self.NodeType = None
        self.Type = None
        self.DiskType = None
        self.DiskSize = None
        self.LocalDiskInfo = None
        self.DiskCount = None
        self.DiskEncrypt = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        self.Type = params.get("Type")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self.LocalDiskInfo = LocalDiskInfo()
            self.LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self.DiskCount = params.get("DiskCount")
        self.DiskEncrypt = params.get("DiskEncrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    """ES集群操作详细信息

    """

    def __init__(self):
        """
        :param Id: 操作唯一id\n        :type Id: int\n        :param StartTime: 操作开始时间\n        :type StartTime: str\n        :param Type: 操作类型\n        :type Type: str\n        :param Detail: 操作详情\n        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`\n        :param Result: 操作结果\n        :type Result: str\n        :param Tasks: 流程任务信息\n        :type Tasks: list of TaskDetail\n        :param Progress: 操作进度\n        :type Progress: float\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    """操作详情

    """

    def __init__(self):
        """
        :param OldInfo: 实例原始配置信息\n        :type OldInfo: list of KeyValue\n        :param NewInfo: 实例更新后配置信息\n        :type NewInfo: list of KeyValue\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ForceRestart: 是否强制重启<li>true：强制重启</li><li>false：不强制重启</li>默认false\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartKibanaRequest(AbstractModel):
    """RestartKibana请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: ES实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartKibanaResponse(AbstractModel):
    """RestartKibana返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartNodesRequest(AbstractModel):
    """RestartNodes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID\n        :type InstanceId: str\n        :param NodeNames: 节点名称列表\n        :type NodeNames: list of str\n        :param ForceRestart: 是否强制重启\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.NodeNames = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeNames = params.get("NodeNames")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    """RestartNodes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """实例操作记录流程任务中的子任务信息（如升级检查任务中的各个检查项）

    """

    def __init__(self):
        """
        :param Name: 子任务名\n        :type Name: str\n        :param Result: 子任务结果\n        :type Result: bool\n        :param ErrMsg: 子任务错误信息\n        :type ErrMsg: str\n        :param Type: 子任务类型\n        :type Type: str\n        :param Status: 子任务状态，0处理中 1成功 -1失败\n        :type Status: int\n        :param FailedIndices: 升级检查失败的索引名\n        :type FailedIndices: list of str\n        :param FinishTime: 子任务结束时间\n        :type FinishTime: str\n        :param Level: 子任务等级，1警告 2失败\n        :type Level: int\n        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None
        self.Type = None
        self.Status = None
        self.FailedIndices = None
        self.FinishTime = None
        self.Level = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.FailedIndices = params.get("FailedIndices")
        self.FinishTime = params.get("FinishTime")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """实例标签信息

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """实例操作记录中的流程任务信息

    """

    def __init__(self):
        """
        :param Name: 任务名\n        :type Name: str\n        :param Progress: 任务进度\n        :type Progress: float\n        :param FinishTime: 任务完成时间\n        :type FinishTime: str\n        :param SubTasks: 子任务\n        :type SubTasks: list of SubTaskDetail\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsRequest(AbstractModel):
    """UpdateDiagnoseSettings请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: ES实例ID\n        :type InstanceId: str\n        :param Status: 0：开启智能运维；-1：关闭智能运维\n        :type Status: int\n        :param CronTime: 智能运维每天定时巡检时间\n        :type CronTime: str\n        """
        self.InstanceId = None
        self.Status = None
        self.CronTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.CronTime = params.get("CronTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsResponse(AbstractModel):
    """UpdateDiagnoseSettings返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）\n        :type InstanceName: str\n        :param NodeNum: 已废弃请使用NodeInfoList
节点个数（2-50个）\n        :type NodeNum: int\n        :param EsConfig: ES配置项（JSON格式字符串）\n        :type EsConfig: str\n        :param Password: 默认用户elastic的密码（8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）\n        :type Password: str\n        :param EsAcl: 访问控制列表\n        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`\n        :param DiskSize: 已废弃请使用NodeInfoList
磁盘大小（单位GB）\n        :type DiskSize: int\n        :param NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type NodeType: str\n        :param MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个或5个）\n        :type MasterNodeNum: int\n        :param MasterNodeType: 已废弃请使用NodeInfoList
专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>\n        :type MasterNodeType: str\n        :param MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB系统默认配置为50GB,暂不支持自定义）\n        :type MasterNodeDiskSize: int\n        :param ForceRestart: 更新配置时是否强制重启<li>true强制重启</li><li>false不强制重启</li>当前仅更新EsConfig时需要设置，默认值为false\n        :type ForceRestart: bool\n        :param CosBackup: COS自动备份信息\n        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`\n        :param NodeInfoList: 节点信息列表，可以只传递要更新的节点及其对应的规格信息。支持的操作包括<li>修改一种节点的个数</li><li>修改一种节点的节点规格及磁盘大小</li><li>增加一种节点类型（需要同时指定该节点的类型，个数，规格，磁盘等信息）</li>上述操作一次只能进行一种，且磁盘类型不支持修改\n        :type NodeInfoList: list of NodeInfo\n        :param PublicAccess: 公网访问状态\n        :type PublicAccess: str\n        :param EsPublicAcl: 公网访问控制列表\n        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`\n        :param KibanaPublicAccess: Kibana公网访问状态\n        :type KibanaPublicAccess: str\n        :param KibanaPrivateAccess: Kibana内网访问状态\n        :type KibanaPrivateAccess: str\n        :param BasicSecurityType: ES 6.8及以上版本基础版开启或关闭用户认证\n        :type BasicSecurityType: int\n        :param KibanaPrivatePort: Kibana内网端口\n        :type KibanaPrivatePort: int\n        :param ScaleType: 0: 蓝绿变更方式扩容，集群不重启 （默认） 1: 磁盘解挂载扩容，集群滚动重启\n        :type ScaleType: int\n        :param MultiZoneInfo: 多可用区部署\n        :type MultiZoneInfo: list of ZoneDetail\n        :param SceneType: 场景化模板类型 -1：不启用 1：通用 2：日志 3：搜索\n        :type SceneType: int\n        :param KibanaConfig: Kibana配置项（JSON格式字符串）\n        :type KibanaConfig: str\n        """
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
        self.NodeInfoList = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.BasicSecurityType = None
        self.KibanaPrivatePort = None
        self.ScaleType = None
        self.MultiZoneInfo = None
        self.SceneType = None
        self.KibanaConfig = None


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
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsPublicAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.KibanaPrivatePort = params.get("KibanaPrivatePort")
        self.ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    """UpdatePlugins请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstallPluginList: 需要安装的插件名列表\n        :type InstallPluginList: list of str\n        :param RemovePluginList: 需要卸载的插件名列表\n        :type RemovePluginList: list of str\n        :param ForceRestart: 是否强制重启\n        :type ForceRestart: bool\n        :param ForceUpdate: 是否重新安装\n        :type ForceUpdate: bool\n        """
        self.InstanceId = None
        self.InstallPluginList = None
        self.RemovePluginList = None
        self.ForceRestart = None
        self.ForceUpdate = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstallPluginList = params.get("InstallPluginList")
        self.RemovePluginList = params.get("RemovePluginList")
        self.ForceRestart = params.get("ForceRestart")
        self.ForceUpdate = params.get("ForceUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    """UpdatePlugins返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    """UpdateRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param TargetNodeTypes: 接收请求的目标节点类型列表\n        :type TargetNodeTypes: list of str\n        """
        self.InstanceId = None
        self.TargetNodeTypes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    """UpdateRequestTargetNodeTypes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param EsVersion: 目标ES版本，支持：”6.4.3“, "6.8.2"，"7.5.1"\n        :type EsVersion: str\n        :param CheckOnly: 是否只做升级检查，默认值为false\n        :type CheckOnly: bool\n        :param LicenseType: 目标商业特性版本：<li>oss 开源版</li><li>basic 基础版</li>当前仅在5.6.4升级6.x版本时使用，默认值为basic\n        :type LicenseType: str\n        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>\n        :type BasicSecurityType: int\n        :param UpgradeMode: 升级方式：<li>scale 蓝绿变更</li><li>restart 滚动重启</li>默认值为scale\n        :type UpgradeMode: str\n        """
        self.InstanceId = None
        self.EsVersion = None
        self.CheckOnly = None
        self.LicenseType = None
        self.BasicSecurityType = None
        self.UpgradeMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EsVersion = params.get("EsVersion")
        self.CheckOnly = params.get("CheckOnly")
        self.LicenseType = params.get("LicenseType")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.UpgradeMode = params.get("UpgradeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum\n        :type LicenseType: str\n        :param AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0\n        :type AutoVoucher: int\n        :param VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）\n        :type VoucherIds: list of str\n        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>\n        :type BasicSecurityType: int\n        :param ForceRestart: 是否强制重启<li>true强制重启</li><li>false不强制重启</li> 默认值false\n        :type ForceRestart: bool\n        """
        self.InstanceId = None
        self.LicenseType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.BasicSecurityType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LicenseType = params.get("LicenseType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    """可视化节点配置

    """

    def __init__(self):
        """
        :param NodeNum: 可视化节点个数，固定为1\n        :type NodeNum: int\n        :param NodeType: 可视化节点规格\n        :type NodeType: str\n        """
        self.NodeNum = None
        self.NodeType = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    """多可用区部署时可用区的详细信息

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        