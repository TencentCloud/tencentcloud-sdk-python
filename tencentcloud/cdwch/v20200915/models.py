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


class ActionAlterCkUserRequest(AbstractModel):
    """ActionAlterCkUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.cdwch.v20200915.models.CkUserAlterInfo`
        :param ApiType: api接口类型
        :type ApiType: str
        """
        self.UserInfo = None
        self.ApiType = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = CkUserAlterInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.ApiType = params.get("ApiType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterCkUserResponse(AbstractModel):
    """ActionAlterCkUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class BackupTableContent(AbstractModel):
    """备份表信息

    """

    def __init__(self):
        r"""
        :param Database: 数据库
        :type Database: str
        :param Table: 表
        :type Table: str
        :param TotalBytes: 表总字节数
        :type TotalBytes: int
        :param VCluster: 虚拟cluster
        :type VCluster: str
        :param Ips: 表ip
        :type Ips: str
        """
        self.Database = None
        self.Table = None
        self.TotalBytes = None
        self.VCluster = None
        self.Ips = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.TotalBytes = params.get("TotalBytes")
        self.VCluster = params.get("VCluster")
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkUserAlterInfo(AbstractModel):
    """新增或是修改ck用户

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例id
        :type InstanceId: str
        :param UserName: 用户名
        :type UserName: str
        :param PassWord: 密码
        :type PassWord: str
        :param Describe: 描述
        :type Describe: str
        """
        self.InstanceId = None
        self.UserName = None
        self.PassWord = None
        self.Describe = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSubmitContext(AbstractModel):
    """配置文件修改信息

    """

    def __init__(self):
        r"""
        :param FileName: 配置文件名称
        :type FileName: str
        :param OldConfValue: 配置文件旧内容，base64编码
        :type OldConfValue: str
        :param NewConfValue: 配置文件新内容，base64编码
        :type NewConfValue: str
        :param FilePath: 保存配置文件的路径
        :type FilePath: str
        """
        self.FileName = None
        self.OldConfValue = None
        self.NewConfValue = None
        self.FilePath = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.OldConfValue = params.get("OldConfValue")
        self.NewConfValue = params.get("NewConfValue")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleRequest(AbstractModel):
    """CreateBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScheduleId: 编辑时需要传
        :type ScheduleId: int
        :param WeekDays: 选择的星期 逗号分隔
        :type WeekDays: str
        :param ExecuteHour: 执行小时
        :type ExecuteHour: int
        :param BackUpTables: 备份表列表
        :type BackUpTables: list of BackupTableContent
        """
        self.ScheduleId = None
        self.WeekDays = None
        self.ExecuteHour = None
        self.BackUpTables = None


    def _deserialize(self, params):
        self.ScheduleId = params.get("ScheduleId")
        self.WeekDays = params.get("WeekDays")
        self.ExecuteHour = params.get("ExecuteHour")
        if params.get("BackUpTables") is not None:
            self.BackUpTables = []
            for item in params.get("BackUpTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self.BackUpTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleResponse(AbstractModel):
    """CreateBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCkSqlApisRequest(AbstractModel):
    """DescribeCkSqlApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param ApiType: api接口名称
        :type ApiType: str
        :param Cluster: 集群名称
        :type Cluster: str
        :param UserName: 用户名称
        :type UserName: str
        """
        self.InstanceId = None
        self.ApiType = None
        self.Cluster = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ApiType = params.get("ApiType")
        self.Cluster = params.get("Cluster")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkSqlApisResponse(AbstractModel):
    """DescribeCkSqlApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReturnData: 返回的查询数据，大部分情况是list，也可能是bool
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnData = params.get("ReturnData")
        self.RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceShardsList: 实例shard信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceShardsList: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceShardsList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceShardsList = params.get("InstanceShardsList")
        self.RequestId = params.get("RequestId")


class ModifyClusterConfigsRequest(AbstractModel):
    """ModifyClusterConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param ModifyConfContext: 配置文件修改信息
        :type ModifyConfContext: list of ConfigSubmitContext
        :param Remark: 修改原因
        :type Remark: str
        """
        self.InstanceId = None
        self.ModifyConfContext = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ModifyConfContext") is not None:
            self.ModifyConfContext = []
            for item in params.get("ModifyConfContext"):
                obj = ConfigSubmitContext()
                obj._deserialize(item)
                self.ModifyConfContext.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsResponse(AbstractModel):
    """ModifyClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程相关信息
        :type FlowId: int
        :param ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ModifyUserNewPrivilegeRequest(AbstractModel):
    """ModifyUserNewPrivilege请求参数结构体

    """


class ModifyUserNewPrivilegeResponse(AbstractModel):
    """ModifyUserNewPrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenBackUpRequest(AbstractModel):
    """OpenBackUp请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群id
        :type InstanceId: str
        :param OperationType: OPEN 或者CLOSE
        :type OperationType: str
        :param CosBucketName: 桶名字
        :type CosBucketName: str
        """
        self.InstanceId = None
        self.OperationType = None
        self.CosBucketName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OperationType = params.get("OperationType")
        self.CosBucketName = params.get("CosBucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBackUpResponse(AbstractModel):
    """OpenBackUp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")