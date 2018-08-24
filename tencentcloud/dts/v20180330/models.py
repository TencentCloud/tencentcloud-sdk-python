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


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConsistencyParams(AbstractModel):
    """抽样检验时的抽样参数

    """

    def __init__(self):
        """
        :param SelectRowsPerTable: 1-100的整数值，select(*)对比时每张表的抽样行数比例
        :type SelectRowsPerTable: int
        :param TablesSelectAll: 1-100的整数值，select(*)对比的表的比例
        :type TablesSelectAll: int
        :param TablesSelectCount: 1-100的整数值，select count(*)对比的表的比例
        :type TablesSelectCount: int
        """
        self.SelectRowsPerTable = None
        self.TablesSelectAll = None
        self.TablesSelectCount = None


    def _deserialize(self, params):
        self.SelectRowsPerTable = params.get("SelectRowsPerTable")
        self.TablesSelectAll = params.get("TablesSelectAll")
        self.TablesSelectCount = params.get("TablesSelectCount")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源实例数据库类型:mysql,redis,mongodb
        :type SrcDatabaseType: str
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标实例数据库类型,mysql,redis,mongodb
        :type DstDatabaseType: str
        :param DstAccessType: 目标实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例). 目前只支持cdb.
        :type DstAccessType: str
        :param DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要迁移的源数据库表信息，用json格式的字符串描述。
对于database-table两级结构的数据库：
[{Database:db1,Table:[table1,table2]},{Database:db2}]
对于database-schema-table三级结构：
[{Database:db1,Schema:s1
Table:[table1,table2]},{Database:db1,Schema:s2
Table:[table1,table2]},{Database:db2,Schema:s1
Table:[table1,table2]},{Database:db3},{Database:db4
Schema:s1}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateSyncCheckJobRequest(AbstractModel):
    """CreateSyncCheckJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 灾备同步任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateSyncCheckJobResponse(AbstractModel):
    """CreateSyncCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobName: 灾备同步任务名
        :type JobName: str
        :param SyncOption: 灾备同步任务配置选项
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcDatabaseType: 源实例数据库类型，目前仅包括：mysql
        :type SrcDatabaseType: str
        :param SrcAccessType: 源实例接入类型，目前仅包括：cdb(云上cdb实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstDatabaseType: 目标实例数据库类型，目前仅包括：mysql
        :type DstDatabaseType: str
        :param DstAccessType: 目标实例接入类型，目前仅包括：cdb(云上cdb实例)
        :type DstAccessType: str
        :param DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseInfo: 需要同步的源数据库表信息，用json格式的字符串描述。
对于database-table两级结构的数据库：
[{Database:db1,Table:[table1,table2]},{Database:db2}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.SyncOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 灾备同步任务ID
        :type JobId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class DeleteMigrateJobRequest(AbstractModel):
    """DeleteMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSyncJobRequest(AbstractModel):
    """DeleteSyncJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 待删除的灾备同步任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteSyncJobResponse(AbstractModel):
    """DeleteSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 校验任务状态：unavailable(当前不可用), starting(开始中)，running(校验中)，finished(校验完成)
        :type Status: str
        :param ErrorCode: 任务的错误码
        :type ErrorCode: int
        :param ErrorMessage: 任务的错误信息
        :type ErrorMessage: str
        :param Progress: Check任务总进度,如："30"表示30%
        :type Progress: str
        :param CheckFlag: 校验是否通过,0-未通过，1-校验通过, 3-未校验
        :type CheckFlag: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Progress = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Progress = params.get("Progress")
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeMigrateJobsRequest(AbstractModel):
    """DescribeMigrateJobs请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param Order: 排序字段，可以取值为JobId、Status、JobName、MigrateType、RunMode、CreateTime
        :type Order: str
        :param OrderSeq: 排序方式，升序为ASC，降序为DESC
        :type OrderSeq: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回实例数量，默认20，有效区间[1,100]
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数目
        :type TotalCount: int
        :param JobList: 任务详情数组
        :type JobList: list of MigrateJobInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = MigrateJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncCheckJobRequest(AbstractModel):
    """DescribeSyncCheckJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 要查询的灾备同步任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeSyncCheckJobResponse(AbstractModel):
    """DescribeSyncCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务校验状态
        :type Status: str
        :param ErrorCode: 任务校验结果代码
        :type ErrorCode: int
        :param ErrorMessage: 提示信息
        :type ErrorMessage: str
        :param StepInfo: 任务执行步骤描述
        :type StepInfo: list of SyncCheckStepInfo
        :param CheckFlag: 校验标志
        :type CheckFlag: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.StepInfo = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncCheckStepInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 灾备同步任务ID
        :type JobId: str
        :param JobName: 灾备同步任务名
        :type JobName: str
        :param Order: 排序字段，可以取值为JobId、Status、JobName、CreateTime
        :type Order: str
        :param OrderSeq: 排序方式，升序为ASC，降序为DESC
        :type OrderSeq: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回实例数量，默认20，有效区间[1,100]
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数目
        :type TotalCount: int
        :param JobList: 任务详情数组
        :type JobList: list of SyncJobInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """目的实例信息，具体内容跟迁移任务类型相关

    """

    def __init__(self):
        """
        :param InstanceId: 目标实例Id
        :type InstanceId: str
        :param Ip: 目标实例vip
        :type Ip: str
        :param Port: 目标实例vport
        :type Port: int
        :param Region: 目标实例Id
        :type Region: str
        :param ReadOnly: 只读开关
        :type ReadOnly: int
        """
        self.InstanceId = None
        self.Ip = None
        self.Port = None
        self.Region = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Region = params.get("Region")
        self.ReadOnly = params.get("ReadOnly")


class MigrateDetailInfo(AbstractModel):
    """描述详细迁移过程

    """

    def __init__(self):
        """
        :param StepAll: 总步骤数
        :type StepAll: int
        :param StepNow: 当前步骤
        :type StepNow: int
        :param Progress: 总进度,如：
        :type Progress: str
        :param CurrentStepProgress: 当前步骤进度,如:
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主从差距，MB
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主从差距，秒
        :type SecondsBehindMaster: int
        :param StepInfo: 步骤信息
        :type StepInfo: list of MigrateStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrateStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class MigrateJobInfo(AbstractModel):
    """迁移任务详情

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源实例数据库类型:mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type SrcDatabaseType: str
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标实例数据库类型,mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type DstDatabaseType: str
        :param DstAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type DstAccessType: str
        :param DstInfo: 目的实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要迁移的源数据库表信息，如果需要迁移的是整个实例，该字段为[]
        :type DatabaseInfo: str
        :param CreateTime: 任务创建(提交)时间
        :type CreateTime: str
        :param StartTime: 任务开始执行时间
        :type StartTime: str
        :param EndTime: 任务执行结束时间
        :type EndTime: str
        :param Status: 任务状态,取值为：1-创建中(Creating),2-创建完成(Created),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,6-准备运行(ReadyRun),7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-中止中（Stoping）,12-完成中（Completing）
        :type Status: int
        :param Detail: 任务详情
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Detail = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Detail") is not None:
            self.Detail = MigrateDetailInfo()
            self.Detail._deserialize(params.get("Detail"))


class MigrateOption(AbstractModel):
    """迁移任务配置选项

    """

    def __init__(self):
        """
        :param RunMode: 任务运行模式，值包括：1-立即执行，2-定时执行
        :type RunMode: int
        :param ExpectTime: 期望执行时间，当runMode=2时，该字段必填，时间格式：yyyy-mm-dd hh:mm:ss
        :type ExpectTime: str
        :param MigrateType: 数据迁移类型，值包括：1-结构迁移,2-全量迁移,3-全量+增量迁移
        :type MigrateType: int
        :param MigrateObject: 迁移对象，1-整个实例，2-指定库表
        :type MigrateObject: int
        :param ConsistencyType: 数据对比类型，1-未配置,2-全量检测,3-抽样检测, 4-仅校验不一致表,5-不检测
        :type ConsistencyType: int
        :param IsOverrideRoot: 是否用源库Root账户覆盖目标库，值包括：0-不覆盖，1-覆盖，选择库表或者结构迁移时应该为0
        :type IsOverrideRoot: int
        :param ExternParams: 不同数据库用到的额外参数.以JSON格式描述. 
Redis可定义如下的参数: 
{ 
	"ClientOutputBufferHardLimit":512, 	从机缓冲区的硬性容量限制(MB) 
	"ClientOutputBufferSoftLimit":512, 	从机缓冲区的软性容量限制(MB) 
	"ClientOutputBufferPersistTime":60, 从机缓冲区的软性限制持续时间(秒) 
	"ReplBacklogSize":512, 	环形缓冲区容量限制(MB) 
	"ReplTimeout":120，		复制超时时间(秒) 
}
MongoDB可定义如下的参数: 
{
	'SrcAuthDatabase':'admin', 
	'SrcAuthFlag': "1", 
	'SrcAuthMechanism':"SCRAM-SHA-1"
}
        :type ExternParams: str
        :param ConsistencyParams: 抽样检验时的抽样参数
        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
        """
        self.RunMode = None
        self.ExpectTime = None
        self.MigrateType = None
        self.MigrateObject = None
        self.ConsistencyType = None
        self.IsOverrideRoot = None
        self.ExternParams = None
        self.ConsistencyParams = None


    def _deserialize(self, params):
        self.RunMode = params.get("RunMode")
        self.ExpectTime = params.get("ExpectTime")
        self.MigrateType = params.get("MigrateType")
        self.MigrateObject = params.get("MigrateObject")
        self.ConsistencyType = params.get("ConsistencyType")
        self.IsOverrideRoot = params.get("IsOverrideRoot")
        self.ExternParams = params.get("ExternParams")
        if params.get("ConsistencyParams") is not None:
            self.ConsistencyParams = ConsistencyParams()
            self.ConsistencyParams._deserialize(params.get("ConsistencyParams"))


class MigrateStepDetailInfo(AbstractModel):
    """迁移中的步骤信息

    """

    def __init__(self):
        """
        :param StepNo: 步骤序列
        :type StepNo: int
        :param StepName: 步骤展现名称
        :type StepName: str
        :param StepId: 步骤英文标识
        :type StepId: str
        :param Status: 步骤状态:0-默认值,1-成功,2-失败,3-执行中,4-未执行
        :type Status: int
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 待修改的数据迁移任务ID
        :type JobId: str
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstAccessType: 目标实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例). 目前只支持cdb.
        :type DstAccessType: str
        :param DstInfo: 目标实例信息, 其中目标实例地域不允许修改.
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 当选择'指定库表'迁移的时候, 需要设置待迁移的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。

对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
对于database-schema-table三级结构：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

如果是'整个实例'的迁移模式,不需设置该字段
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySyncJobRequest(AbstractModel):
    """ModifySyncJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 待修改的灾备同步任务ID
        :type JobId: str
        :param JobName: 灾备同步任务名称
        :type JobName: str
        :param SyncOption: 灾备同步任务配置选项
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param DatabaseInfo: 当选择'指定库表'灾备同步的时候, 需要设置待同步的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。
对于database-table两级结构的数据库：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifySyncJobResponse(AbstractModel):
    """ModifySyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """源实例信息

    """

    def __init__(self):
        """
        :param AccessKey: 阿里云AccessKey
        :type AccessKey: str
        :param Ip: 实例的IP地址
        :type Ip: str
        :param Port: 实例的端口
        :type Port: int
        :param User: 实例的用户名
        :type User: str
        :param Password: 实例的密码
        :type Password: str
        :param RdsInstanceId: 阿里云rds实例id
        :type RdsInstanceId: str
        :param CvmInstanceId: CVM实例短ID，格式如：ins-olgl89y8，与云主机控制台页面显示的实例ID相同，如果是CVM自建实例或者通过自建VPN接入的公网实例，需要传递此字段
        :type CvmInstanceId: str
        :param UniqDcgId: 专线网关ID
        :type UniqDcgId: str
        :param VpcId: 私有网络ID，和原来的数字vpcId对应，需要调vpc的接口去转换
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID, 和原来的数字子网ID对应，需要调用vpc的接口去转换
        :type SubnetId: str
        :param UniqVpnGwId: 系统分配的VPN网关ID
        :type UniqVpnGwId: str
        :param InstanceId: 实例短Id
        :type InstanceId: str
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param Supplier: 服务提供商，如:aliyun,others
        :type Supplier: str
        """
        self.AccessKey = None
        self.Ip = None
        self.Port = None
        self.User = None
        self.Password = None
        self.RdsInstanceId = None
        self.CvmInstanceId = None
        self.UniqDcgId = None
        self.VpcId = None
        self.SubnetId = None
        self.UniqVpnGwId = None
        self.InstanceId = None
        self.Region = None
        self.Supplier = None


    def _deserialize(self, params):
        self.AccessKey = params.get("AccessKey")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.RdsInstanceId = params.get("RdsInstanceId")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Supplier = params.get("Supplier")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 灾备同步任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchDrToMasterRequest(AbstractModel):
    """SwitchDrToMaster请求参数结构体

    """

    def __init__(self):
        """
        :param DstInfo: 灾备实例的信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseType: 数据库的类型  （如 mysql）
        :type DatabaseType: str
        """
        self.DstInfo = None
        self.DatabaseType = None


    def _deserialize(self, params):
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseType = params.get("DatabaseType")


class SwitchDrToMasterResponse(AbstractModel):
    """SwitchDrToMaster返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 后台异步任务请求id
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SyncCheckStepInfo(AbstractModel):
    """灾备任务校验步骤

    """

    def __init__(self):
        """
        :param StepNo: 步骤序列
        :type StepNo: int
        :param StepName: 步骤展现名称
        :type StepName: str
        :param StepCode: 步骤执行结果代码
        :type StepCode: int
        :param StepMessage: 步骤执行结果提示
        :type StepMessage: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepCode = None
        self.StepMessage = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepCode = params.get("StepCode")
        self.StepMessage = params.get("StepMessage")


class SyncDetailInfo(AbstractModel):
    """描述详细同步任务过程

    """

    def __init__(self):
        """
        :param StepAll: 总步骤数
        :type StepAll: int
        :param StepNow: 当前步骤
        :type StepNow: int
        :param Progress: 总进度
        :type Progress: str
        :param CurrentStepProgress: 当前步骤进度
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主从差距，MB
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主从差距，秒
        :type SecondsBehindMaster: int
        :param StepInfo: 步骤信息
        :type StepInfo: list of SyncStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class SyncInstanceInfo(AbstractModel):
    """灾备同步的实例信息，记录主实例或灾备实例的信息

    """

    def __init__(self):
        """
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param InstanceId: 实例短Id
        :type InstanceId: str
        """
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")


class SyncJobInfo(AbstractModel):
    """灾备同步任务信息

    """

    def __init__(self):
        """
        :param JobId: 灾备任务id
        :type JobId: str
        :param JobName: 灾备任务名
        :type JobName: str
        :param SyncOption: 任务同步
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcAccessType: 源接入类型
        :type SrcAccessType: str
        :param SrcDatabaseType: 源数据类型
        :type SrcDatabaseType: str
        :param SrcInfo: 源实例信息
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstAccessType: 灾备接入类型
        :type DstAccessType: str
        :param DstDatabaseType: 灾备数据类型
        :type DstDatabaseType: str
        :param DstInfo: 灾备实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param Detail: 任务信息
        :type Detail: :class:`tencentcloud.dts.v20180330.models.SyncDetailInfo`
        :param Status: 任务状态
        :type Status: int
        :param DatabaseInfo: 迁移库表
        :type DatabaseInfo: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstDatabaseType = None
        self.DstInfo = None
        self.Detail = None
        self.Status = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("Detail") is not None:
            self.Detail = SyncDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.Status = params.get("Status")
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class SyncOption(AbstractModel):
    """灾备同步任务配置选项

    """

    def __init__(self):
        """
        :param SyncObject: 同步对象，1-整个实例，2-指定库表
        :type SyncObject: int
        :param RunMode: 同步开始设置，1-立即开始
        :type RunMode: int
        :param SyncType: 同步模式， 3-增量同步
        :type SyncType: int
        :param ConsistencyType: 数据一致性检测， 1-不配置
        :type ConsistencyType: int
        """
        self.SyncObject = None
        self.RunMode = None
        self.SyncType = None
        self.ConsistencyType = None


    def _deserialize(self, params):
        self.SyncObject = params.get("SyncObject")
        self.RunMode = params.get("RunMode")
        self.SyncType = params.get("SyncType")
        self.ConsistencyType = params.get("ConsistencyType")


class SyncStepDetailInfo(AbstractModel):
    """同步任务进度

    """

    def __init__(self):
        """
        :param StepNo: 步骤编号
        :type StepNo: int
        :param StepName: 步骤名
        :type StepName: str
        :param CanStop: 能否中止
        :type CanStop: int
        :param StepId: 步骤号
        :type StepId: int
        """
        self.StepNo = None
        self.StepName = None
        self.CanStop = None
        self.StepId = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.CanStop = params.get("CanStop")
        self.StepId = params.get("StepId")