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


class Account(AbstractModel):
    """数据库账户信息

    """

    def __init__(self):
        r"""
        :param AccountName: 数据库账号名
        :type AccountName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AccountDescription: 数据库账号描述
        :type AccountDescription: str
        :param CreateTime: 数据库账号创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param UpdateTime: 数据库账号信息更新时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type UpdateTime: str
        """
        self.AccountName = None
        self.ClusterId = None
        self.AccountDescription = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.ClusterId = params.get("ClusterId")
        self.AccountDescription = params.get("AccountDescription")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRecoveryTimeRange(AbstractModel):
    """可以回档时间范围

    """

    def __init__(self):
        r"""
        :param AvailableBeginTime: 可回档起始时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type AvailableBeginTime: str
        :param AvailableEndTime: 可回档结束时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type AvailableEndTime: str
        """
        self.AvailableBeginTime = None
        self.AvailableEndTime = None


    def _deserialize(self, params):
        self.AvailableBeginTime = params.get("AvailableBeginTime")
        self.AvailableEndTime = params.get("AvailableEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Backup(AbstractModel):
    """集群备份集信息

    """

    def __init__(self):
        r"""
        :param BackupId: 备份集ID，集群内唯一
        :type BackupId: int
        :param BackupType: 备份集类型，目前只支持 SNAPSHOT：快照
        :type BackupType: str
        :param BackupMethod: 备份集产生的方案，目前只支持 AUTO：自动
        :type BackupMethod: str
        :param BackupDataTime: 备份集对应的数据时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupDataTime: str
        :param BackupDataSize: 备份集数据大小，单位GiB
        :type BackupDataSize: int
        :param BackupTaskStartTime: 备份集对应的任务开始时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupTaskStartTime: str
        :param BackupTaskEndTime: 备份集对应的任务结束时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupTaskEndTime: str
        :param BackupTaskStatus: 备份集对应的任务状态  SUCCESS：成功
        :type BackupTaskStatus: str
        """
        self.BackupId = None
        self.BackupType = None
        self.BackupMethod = None
        self.BackupDataTime = None
        self.BackupDataSize = None
        self.BackupTaskStartTime = None
        self.BackupTaskEndTime = None
        self.BackupTaskStatus = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupDataTime = params.get("BackupDataTime")
        self.BackupDataSize = params.get("BackupDataSize")
        self.BackupTaskStartTime = params.get("BackupTaskStartTime")
        self.BackupTaskEndTime = params.get("BackupTaskEndTime")
        self.BackupTaskStatus = params.get("BackupTaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneClusterToPointInTimeRequest(AbstractModel):
    """CloneClusterToPointInTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param DBVersion: 数据库版本，目前仅支持 10.17
        :type DBVersion: str
        :param CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 已配置的私有网络中的子网ID
        :type SubnetId: str
        :param PayMode: 集群付费模式
- PREPAID：预付费，即包年包月
- POSTPAID_BY_HOUR：按小时后付费
        :type PayMode: str
        :param SourceClusterId: 对应的备份数据来源集群ID
        :type SourceClusterId: str
        :param SourceDataPoint: 对应的备份数据时间点。按照RFC3339标准表示，并且使用东八区时区时间。格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type SourceDataPoint: str
        :param ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与ClusterId保持一致。
        :type ClusterName: str
        :param ProjectId: 项目Id，默认为0表示默认项目
        :type ProjectId: int
        :param Port: 连接数据库时，Endpoint使用的端口。取值范围为[1,65534]，默认值为5432
        :type Port: int
        :param InstanceCount: 集群下实例数量。取值范围为[1,4]，默认值为1
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        :param AutoRenewFlag: 是否自动续费，0-不 1-是。默认为0，只有当PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        """
        self.Zone = None
        self.DBVersion = None
        self.CPU = None
        self.Memory = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.SourceClusterId = None
        self.SourceDataPoint = None
        self.ClusterName = None
        self.ProjectId = None
        self.Port = None
        self.InstanceCount = None
        self.Period = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBVersion = params.get("DBVersion")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.SourceClusterId = params.get("SourceClusterId")
        self.SourceDataPoint = params.get("SourceDataPoint")
        self.ClusterName = params.get("ClusterName")
        self.ProjectId = params.get("ProjectId")
        self.Port = params.get("Port")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneClusterToPointInTimeResponse(AbstractModel):
    """CloneClusterToPointInTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNameSet: 订单号
        :type DealNameSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNameSet = params.get("DealNameSet")
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID，集群的唯一标识
        :type ClusterId: str
        :param ClusterName: 集群名字，不修改时默认和集群ID相同
        :type ClusterName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param DBVersion: 数据库版本
        :type DBVersion: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Status: 集群状态。目前包括
 - creating ：创建中
 - running : 运行中
 - isolating : 隔离中
 - isolated : 已隔离
 - recovering : 恢复中
 - deleting : 删除中
 - deleted : 已删除
        :type Status: str
        :param StatusDesc: 集群状态中文含义
        :type StatusDesc: str
        :param CreateTime: 集群创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param StorageUsed: 存储当前使用量，单位GiB
        :type StorageUsed: float
        :param StorageLimit: 存储最大使用量，单位GiB
        :type StorageLimit: int
        :param PayMode: 付费模式：
 - PREPAID : 预付费，即包年包月
 - POSTPAID_BY_HOUR : 按小时结算后付费
        :type PayMode: str
        :param PayPeriodEndTime: 预付费集群到期时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type PayPeriodEndTime: str
        :param AutoRenewFlag: 预付费集群自动续费标签
 - 0 : 到期不自动续费
 - 1 : 到期自动续费
        :type AutoRenewFlag: int
        :param DBCharset: 数据库字符集
        :type DBCharset: str
        :param InstanceCount: 集群内实例的数量
        :type InstanceCount: int
        :param EndpointSet: 集群内访问点信息
        :type EndpointSet: list of Endpoint
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.Zone = None
        self.DBVersion = None
        self.ProjectId = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.StorageUsed = None
        self.StorageLimit = None
        self.PayMode = None
        self.PayPeriodEndTime = None
        self.AutoRenewFlag = None
        self.DBCharset = None
        self.InstanceCount = None
        self.EndpointSet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.DBVersion = params.get("DBVersion")
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.StorageUsed = params.get("StorageUsed")
        self.StorageLimit = params.get("StorageLimit")
        self.PayMode = params.get("PayMode")
        self.PayPeriodEndTime = params.get("PayPeriodEndTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DBCharset = params.get("DBCharset")
        self.InstanceCount = params.get("InstanceCount")
        if params.get("EndpointSet") is not None:
            self.EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = Endpoint()
                obj._deserialize(item)
                self.EndpointSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param InstanceName: 实例名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与InstanceId一致。
        :type InstanceName: str
        :param InstanceCount: 新建实例的数量，默认为1。单集群下实例数量目前不能超过4个。
        :type InstanceCount: int
        """
        self.ClusterId = None
        self.CPU = None
        self.Memory = None
        self.InstanceName = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.InstanceName = params.get("InstanceName")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNameSet: 订单号
        :type DealNameSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNameSet = params.get("DealNameSet")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param DBVersion: 数据库版本，目前仅支持 10.17
        :type DBVersion: str
        :param MasterUserPassword: 数据库用户密码，必须满足 8-64个字符，至少包含 大写字母、小写字母、数字和符号~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/中的任意三种
        :type MasterUserPassword: str
        :param CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 已配置的私有网络中的子网ID
        :type SubnetId: str
        :param PayMode: 集群付费模式
 - PREPAID：预付费，即包年包月
 - POSTPAID_BY_HOUR：按小时后付费
        :type PayMode: str
        :param ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与ClusterId保持一致
        :type ClusterName: str
        :param ProjectId: 项目Id，默认为0表示默认项目
        :type ProjectId: int
        :param Port: 连接数据库时，Endpoint使用的端口。取值范围为[1,65534]，默认值为5432
        :type Port: int
        :param InstanceCount: 集群下实例数量。取值范围为[1,4]，默认值为1
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        :param AutoRenewFlag: 是否自动续费，0-不 1-是。默认值为0，只有当PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        """
        self.Zone = None
        self.DBVersion = None
        self.MasterUserPassword = None
        self.CPU = None
        self.Memory = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.ClusterName = None
        self.ProjectId = None
        self.Port = None
        self.InstanceCount = None
        self.Period = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBVersion = params.get("DBVersion")
        self.MasterUserPassword = params.get("MasterUserPassword")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.ClusterName = params.get("ClusterName")
        self.ProjectId = params.get("ProjectId")
        self.Port = params.get("Port")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNameSet: 订单号
        :type DealNameSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNameSet = params.get("DealNameSet")
        self.RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self.ClusterId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param AccountSet: 账号信息列表
        :type AccountSet: list of Account
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterBackupsRequest(AbstractModel):
    """DescribeClusterBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param PageSize: 每页个数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        """
        self.ClusterId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterBackupsResponse(AbstractModel):
    """DescribeClusterBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param BackupSet: 备份列表信息
        :type BackupSet: list of Backup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = Backup()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointsRequest(AbstractModel):
    """DescribeClusterEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointsResponse(AbstractModel):
    """DescribeClusterEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param EndpointSet: 接入点列表
        :type EndpointSet: list of Endpoint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EndpointSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EndpointSet") is not None:
            self.EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = Endpoint()
                obj._deserialize(item)
                self.EndpointSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param PageSize: 每页个数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        :param Filters: 目前支持查询条件包括：
 - InstanceId : 实例ID
 - InstanceName : 实例名
 - EndpointId : 接入点ID
 - Status : 实例状态
 - InstanceType : 实例类型
        :type Filters: list of Filter
        :param OrderBy: 排序字段，可选字段：
- CreateTime : 实例创建时间(默认值)
- PayPeriodEndTime : 实例过期时间
        :type OrderBy: str
        :param OrderByType: 排序方式，可选字段：
- DESC : 降序(默认值)
- ASC : 升序
        :type OrderByType: str
        """
        self.ClusterId = None
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param InstanceSet: 实例列表信息
        :type InstanceSet: list of Instance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRecoveryTimeRangeRequest(AbstractModel):
    """DescribeClusterRecoveryTimeRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param DataPoint: 期望的回档时间点，传入从集群创建时间到当前时间之间的时间点。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type DataPoint: str
        """
        self.ClusterId = None
        self.DataPoint = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DataPoint = params.get("DataPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRecoveryTimeRangeResponse(AbstractModel):
    """DescribeClusterRecoveryTimeRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param AvailableRecoveryTimeRangeSet: 可回档时间范围列表
        :type AvailableRecoveryTimeRangeSet: list of AvailableRecoveryTimeRange
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AvailableRecoveryTimeRangeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AvailableRecoveryTimeRangeSet") is not None:
            self.AvailableRecoveryTimeRangeSet = []
            for item in params.get("AvailableRecoveryTimeRangeSet"):
                obj = AvailableRecoveryTimeRange()
                obj._deserialize(item)
                self.AvailableRecoveryTimeRangeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param PageSize: 每页条数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        :param Filters: 目前支持查询条件包括：
 - ClusterId : 集群ID
 - ClusterName : 集群名
 - ProjectId : 项目ID
 - Status : 集群状态
 - PayMode : 付费模式
        :type Filters: list of Filter
        :param OrderBy: 排序字段，可选字段：
 - CreateTime : 集群创建时间(默认值)
 - PayPeriodEndTime : 集群过期时间
        :type OrderBy: str
        :param OrderByType: 排序方式，可选字段：
 - DESC : 降序(默认值)
 - ASC : 升序
        :type OrderByType: str
        """
        self.PageNumber = None
        self.PageSize = None
        self.Filters = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param ClusterSet: 集群列表信息
        :type ClusterSet: list of Cluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 计费订单id（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）
        :type DealName: str
        """
        self.DealName = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIdInfoSet: 资源ID信息列表
        :type ResourceIdInfoSet: list of ResourceIdInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceIdInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceIdInfoSet") is not None:
            self.ResourceIdInfoSet = []
            for item in params.get("ResourceIdInfoSet"):
                obj = ResourceIdInfo()
                obj._deserialize(item)
                self.ResourceIdInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class Endpoint(AbstractModel):
    """集群的连接点信息，包含访问数据库的相关网络信息

    """

    def __init__(self):
        r"""
        :param EndpointId: 连接点ID，集群内唯一
        :type EndpointId: str
        :param ClusterId: 连接点所属的集群ID
        :type ClusterId: str
        :param EndpointName: 连接点名字，默认和连接点ID一致
        :type EndpointName: str
        :param EndpointType: 连接点类型
 - RW : 读写
 - RO : 只读
        :type EndpointType: str
        :param VpcId: 私有网络VPC实例ID
        :type VpcId: str
        :param SubnetId: 私有网络VPC下子网实例ID
        :type SubnetId: str
        :param PrivateIp: 私有网络VPC下用于访问数据库的IP
        :type PrivateIp: str
        :param PrivatePort: 私有网络VPC下用于访问数据库的端口
        :type PrivatePort: int
        :param WanIp: 公共网络用户访问数据库的IP
        :type WanIp: str
        :param WanPort: 公共网络用户访问数据库的端口
        :type WanPort: int
        :param WanDomain: 公共网络用户访问数据库的域名
        :type WanDomain: str
        """
        self.EndpointId = None
        self.ClusterId = None
        self.EndpointName = None
        self.EndpointType = None
        self.VpcId = None
        self.SubnetId = None
        self.PrivateIp = None
        self.PrivatePort = None
        self.WanIp = None
        self.WanPort = None
        self.WanDomain = None


    def _deserialize(self, params):
        self.EndpointId = params.get("EndpointId")
        self.ClusterId = params.get("ClusterId")
        self.EndpointName = params.get("EndpointName")
        self.EndpointType = params.get("EndpointType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PrivateIp = params.get("PrivateIp")
        self.PrivatePort = params.get("PrivatePort")
        self.WanIp = params.get("WanIp")
        self.WanPort = params.get("WanPort")
        self.WanDomain = params.get("WanDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤条件名
        :type Name: str
        :param Values: 过滤条件值数组
        :type Values: list of str
        :param ExactMatch: true:精确匹配(默认值) false:(模糊匹配)
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """集群下的实例信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，集群下唯一
        :type InstanceId: str
        :param InstanceName: 实例名字，默认和实例ID一致
        :type InstanceName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param EndpointId: 实例所在的访问点ID
        :type EndpointId: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param DBVersion: 数据库版本
        :type DBVersion: str
        :param Status: 实例状态
        :type Status: str
        :param StatusDesc: 实例状态中文含义
        :type StatusDesc: str
        :param CreateTime: 实例创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param PayMode: 付费模式：
- PREPAID : 预付费
- POSTPAID_BY_HOUR : 按小时结算后付费

同一集群下付费模式需要保持一致。
        :type PayMode: str
        :param PayPeriodEndTime: 实例到期时间。同一集群下到期时间需要保持一致。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type PayPeriodEndTime: str
        :param CPU: CPU核数
        :type CPU: int
        :param Memory: 内存大小，单位GiB
        :type Memory: int
        :param InstanceType: 实例类型
 - RW：读写实例
 - RO：只读实例
        :type InstanceType: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.ClusterId = None
        self.EndpointId = None
        self.Region = None
        self.Zone = None
        self.DBVersion = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PayMode = None
        self.PayPeriodEndTime = None
        self.CPU = None
        self.Memory = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ClusterId = params.get("ClusterId")
        self.EndpointId = params.get("EndpointId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.DBVersion = params.get("DBVersion")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PayPeriodEndTime = params.get("PayPeriodEndTime")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterInstancesRequest(AbstractModel):
    """IsolateClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self.ClusterId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterInstancesResponse(AbstractModel):
    """IsolateClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AccountName: 账号名字
        :type AccountName: str
        :param AccountDescription: 账号描述，0-256个字符
        :type AccountDescription: str
        """
        self.ClusterId = None
        self.AccountName = None
        self.AccountDescription = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AccountName = params.get("AccountName")
        self.AccountDescription = params.get("AccountDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointWanStatusRequest(AbstractModel):
    """ModifyClusterEndpointWanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param EndpointId: 接入点ID
        :type EndpointId: str
        :param WanStatus: 取值为： 
 - OPEN：开启外网 
 - CLOSE：关闭外网
        :type WanStatus: str
        """
        self.ClusterId = None
        self.EndpointId = None
        self.WanStatus = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.EndpointId = params.get("EndpointId")
        self.WanStatus = params.get("WanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointWanStatusResponse(AbstractModel):
    """ModifyClusterEndpointWanStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterInstancesSpecRequest(AbstractModel):
    """ModifyClusterInstancesSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表，目前只支持单个实例修改
        :type InstanceIdSet: list of str
        :param CPU: 修改后的CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param Memory: 修改后的内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param OperationTiming: 操作时机
 - IMMEDIATE：立即执行 
 - MAINTAIN_PERIOD：维护窗口期执行
        :type OperationTiming: str
        """
        self.ClusterId = None
        self.InstanceIdSet = None
        self.CPU = None
        self.Memory = None
        self.OperationTiming = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OperationTiming = params.get("OperationTiming")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterInstancesSpecResponse(AbstractModel):
    """ModifyClusterInstancesSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClustersAutoRenewFlagRequest(AbstractModel):
    """ModifyClustersAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIdSet: 集群ID列表
        :type ClusterIdSet: list of str
        :param AutoRenewFlag: 是否自动续费，0-不 1-是。默认为0，只有当集群的PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        """
        self.ClusterIdSet = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.ClusterIdSet = params.get("ClusterIdSet")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClustersAutoRenewFlagResponse(AbstractModel):
    """ModifyClustersAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecoverClusterInstancesRequest(AbstractModel):
    """RecoverClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        """
        self.ClusterId = None
        self.InstanceIdSet = None
        self.Period = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverClusterInstancesResponse(AbstractModel):
    """RecoverClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecoverClusterRequest(AbstractModel):
    """RecoverCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        """
        self.ClusterId = None
        self.Period = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverClusterResponse(AbstractModel):
    """RecoverCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewClusterRequest(AbstractModel):
    """RenewCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Period: 续费时间，单位：月。取值范围为[1,60]，默认值为1。
        :type Period: int
        """
        self.ClusterId = None
        self.Period = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewClusterResponse(AbstractModel):
    """RenewCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AccountName: 账号名字
        :type AccountName: str
        :param AccountPassword: 数据库用户密码，必须满足 8-64个字符，至少包含 大写字母、小写字母、数字和符号~!@#$%^&*_-+=`|(){}[]:;'<>,.?/中的任意三种
        :type AccountPassword: str
        """
        self.ClusterId = None
        self.AccountName = None
        self.AccountPassword = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceIdInfo(AbstractModel):
    """资源ID信息，包括ClusterID和InstanceID

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self.ClusterId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterInstancesRequest(AbstractModel):
    """RestartClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdSet: 实例ID列表，目前只支持单个实例重启
        :type InstanceIdSet: list of str
        """
        self.ClusterId = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterInstancesResponse(AbstractModel):
    """RestartClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TransformClusterPayModeRequest(AbstractModel):
    """TransformClusterPayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CurrentPayMode: 当前付费模式，目前只支持：POSTPAID_BY_HOUR(按小时后付费)
        :type CurrentPayMode: str
        :param TargetPayMode: 目标付费模式，目前只支持：PREPAID(预付费)
        :type TargetPayMode: str
        :param Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
        :type Period: int
        """
        self.ClusterId = None
        self.CurrentPayMode = None
        self.TargetPayMode = None
        self.Period = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.CurrentPayMode = params.get("CurrentPayMode")
        self.TargetPayMode = params.get("TargetPayMode")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformClusterPayModeResponse(AbstractModel):
    """TransformClusterPayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")