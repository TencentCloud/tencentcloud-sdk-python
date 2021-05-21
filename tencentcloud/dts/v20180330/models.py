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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ActivateSubscribeRequest(AbstractModel):
    """ActivateSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 订阅实例ID。
        :type SubscribeId: str
        :param InstanceId: 数据库实例ID
        :type InstanceId: str
        :param SubscribeObjectType: 数据订阅类型0-全实例订阅，1数据订阅，2结构订阅，3数据订阅与结构订阅
        :type SubscribeObjectType: int
        :param Objects: 订阅对象
        :type Objects: :class:`tencentcloud.dts.v20180330.models.SubscribeObject`
        :param UniqSubnetId: 数据订阅服务所在子网。默认为数据库实例所在的子网内。
        :type UniqSubnetId: str
        :param Vport: 订阅服务端口；默认为7507
        :type Vport: int
        """
        self.SubscribeId = None
        self.InstanceId = None
        self.SubscribeObjectType = None
        self.Objects = None
        self.UniqSubnetId = None
        self.Vport = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.InstanceId = params.get("InstanceId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = SubscribeObject()
            self.Objects._deserialize(params.get("Objects"))
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 配置数据订阅任务ID。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ConsistencyParams(AbstractModel):
    """抽样检验时的抽样参数

    """

    def __init__(self):
        """
        :param SelectRowsPerTable: 数据内容检测参数。表中选出用来数据对比的行，占表的总行数的百分比。取值范围是整数[1-100]
        :type SelectRowsPerTable: int
        :param TablesSelectAll: 数据内容检测参数。迁移库表中，要进行数据内容检测的表，占所有表的百分比。取值范围是整数[1-100]
        :type TablesSelectAll: int
        :param TablesSelectCount: 数据数量检测，检测表行数是否一致。迁移库表中，要进行数据数量检测的表，占所有表的百分比。取值范围是整数[1-100]
        :type TablesSelectCount: int
        """
        self.SelectRowsPerTable = None
        self.TablesSelectAll = None
        self.TablesSelectCount = None


    def _deserialize(self, params):
        self.SelectRowsPerTable = params.get("SelectRowsPerTable")
        self.TablesSelectAll = params.get("TablesSelectAll")
        self.TablesSelectCount = params.get("TablesSelectCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobName: 数据迁移任务名称
        :type JobName: str
        :param MigrateOption: 迁移任务配置选项
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :type SrcDatabaseType: str
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。
        :type DstDatabaseType: str
        :param DstAccessType: 目标实例接入类型，目前支持：cdb（腾讯云数据库实例）
        :type DstAccessType: str
        :param DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要迁移的源数据库表信息，用json格式的字符串描述。当MigrateOption.MigrateObject配置为2（指定库表迁移）时必填。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 数据迁移任务ID
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 订阅的数据库类型，目前支持的有 mysql
        :type Product: str
        :param PayType: 实例付费类型，1小时计费，0包年包月
        :type PayType: int
        :param Duration: 购买时长。PayType为0时必填。单位为月，最大支持120
        :type Duration: int
        :param Count: 购买数量,默认为1，最大为10
        :type Count: int
        :param AutoRenew: 是否自动续费，默认为0，1表示自动续费。小时计费实例设置该标识无效。
        :type AutoRenew: int
        :param Tags: 实例资源标签
        :type Tags: list of TagItem
        """
        self.Product = None
        self.PayType = None
        self.Duration = None
        self.Count = None
        self.AutoRenew = None
        self.Tags = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.PayType = params.get("PayType")
        self.Duration = params.get("Duration")
        self.Count = params.get("Count")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param SubscribeIds: 数据订阅实例的ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscribeIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeIds = params.get("SubscribeIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateSyncCheckJobResponse(AbstractModel):
    """CreateSyncCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 灾备同步任务ID
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteSyncJobResponse(AbstractModel):
    """DeleteSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 任务 ID
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Info: 任务执行结果信息
        :type Info: str
        :param Status: 任务执行状态，可能的值有：success，failed，running
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数目
        :type TotalCount: int
        :param JobList: 任务详情数组
        :type JobList: list of MigrateJobInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRegionConfRequest(AbstractModel):
    """DescribeRegionConf请求参数结构体

    """


class DescribeRegionConfResponse(AbstractModel):
    """DescribeRegionConf返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 可售卖地域的数量
        :type TotalCount: int
        :param Items: 可售卖地域详情
        :type Items: list of SubscribeRegionConf
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeRegionConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf返回参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 订阅实例ID
        :type SubscribeId: str
        :param SubscribeName: 订阅实例名称
        :type SubscribeName: str
        :param ChannelId: 订阅通道
        :type ChannelId: str
        :param Product: 订阅数据库类型
        :type Product: str
        :param InstanceId: 被订阅的实例
        :type InstanceId: str
        :param InstanceStatus: 被订阅的实例的状态，可能的值有running,offline,isolate
        :type InstanceStatus: str
        :param SubsStatus: 订阅实例状态，可能的值有unconfigure-未配置，configuring-配置中，configured-已配置
        :type SubsStatus: str
        :param Status: 订阅实例生命周期状态，可能的值有：normal-正常，isolating-隔离中，isolated-已隔离，offlining-下线中
        :type Status: str
        :param CreateTime: 订阅实例创建时间
        :type CreateTime: str
        :param IsolateTime: 订阅实例被隔离时间
        :type IsolateTime: str
        :param ExpireTime: 订阅实例到期时间
        :type ExpireTime: str
        :param OfflineTime: 订阅实例下线时间
        :type OfflineTime: str
        :param ConsumeStartTime: 订阅实例消费时间起点。
        :type ConsumeStartTime: str
        :param PayType: 订阅实例计费类型，1-小时计费，0-包年包月
        :type PayType: int
        :param Vip: 订阅通道Vip
        :type Vip: str
        :param Vport: 订阅通道Port
        :type Vport: int
        :param UniqVpcId: 订阅通道所在VpcId
        :type UniqVpcId: str
        :param UniqSubnetId: 订阅通道所在SubnetId
        :type UniqSubnetId: str
        :param SdkConsumedTime: 当前SDK消费时间位点
        :type SdkConsumedTime: str
        :param SdkHost: 订阅SDK IP地址
        :type SdkHost: str
        :param SubscribeObjectType: 订阅对象类型0-全实例订阅，1-DDL数据订阅，2-DML结构订阅，3-DDL数据订阅+DML结构订阅
        :type SubscribeObjectType: int
        :param SubscribeObjects: 订阅对象，当SubscribeObjectType 为0时，此字段为空数组
        :type SubscribeObjects: list of SubscribeObject
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Region: 地域
        :type Region: str
        :param Tags: 订阅实例的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param AutoRenewFlag: 自动续费标识,0-不自动续费，1-自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.Status = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.SdkConsumedTime = None
        self.SdkHost = None
        self.SubscribeObjectType = None
        self.SubscribeObjects = None
        self.ModifyTime = None
        self.Region = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.SdkConsumedTime = params.get("SdkConsumedTime")
        self.SdkHost = params.get("SdkHost")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("SubscribeObjects") is not None:
            self.SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.SubscribeObjects.append(obj)
        self.ModifyTime = params.get("ModifyTime")
        self.Region = params.get("Region")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSubscribesRequest(AbstractModel):
    """DescribeSubscribes请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅的实例ID
        :type SubscribeId: str
        :param SubscribeName: 数据订阅的实例名称
        :type SubscribeName: str
        :param InstanceId: 绑定数据库实例的ID
        :type InstanceId: str
        :param ChannelId: 数据订阅实例的通道ID
        :type ChannelId: str
        :param PayType: 计费模式筛选，可能的值：0-包年包月，1-按量计费
        :type PayType: str
        :param Product: 订阅的数据库产品，如mysql
        :type Product: str
        :param Status: 数据订阅实例的状态，creating - 创建中，normal - 正常运行，isolating - 隔离中，isolated - 已隔离，offlining - 下线中
        :type Status: list of str
        :param SubsStatus: 数据订阅实例的配置状态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :type SubsStatus: list of str
        :param Offset: 返回记录的起始偏移量
        :type Offset: int
        :param Limit: 单次返回的记录数量
        :type Limit: int
        :param OrderDirection: 排序方向，可选的值为"DESC"和"ASC"，默认为"DESC"，按创建时间逆序排序
        :type OrderDirection: str
        :param TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param SubscribeVersion: 订阅实例版本;txdts-旧版数据订阅，kafka-kafka版本数据订阅
        :type SubscribeVersion: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.InstanceId = None
        self.ChannelId = None
        self.PayType = None
        self.Product = None
        self.Status = None
        self.SubsStatus = None
        self.Offset = None
        self.Limit = None
        self.OrderDirection = None
        self.TagFilters = None
        self.SubscribeVersion = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.InstanceId = params.get("InstanceId")
        self.ChannelId = params.get("ChannelId")
        self.PayType = params.get("PayType")
        self.Product = params.get("Product")
        self.Status = params.get("Status")
        self.SubsStatus = params.get("SubsStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderDirection = params.get("OrderDirection")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param Items: 数据订阅实例的信息列表
        :type Items: list of SubscribeInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSyncCheckJobResponse(AbstractModel):
    """DescribeSyncCheckJob返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务校验状态： starting(开始中)，running(校验中)，finished(校验完成)
        :type Status: str
        :param ErrorCode: 任务校验结果代码
        :type ErrorCode: int
        :param ErrorMessage: 提示信息
        :type ErrorMessage: str
        :param StepInfo: 任务执行步骤描述
        :type StepInfo: list of SyncCheckStepInfo
        :param CheckFlag: 校验标志：0（尚未校验成功） ， 1（校验成功）
        :type CheckFlag: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务数目
        :type TotalCount: int
        :param JobList: 任务详情数组
        :type JobList: list of SyncJobInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DstInfo(AbstractModel):
    """目的实例信息，具体内容跟迁移任务类型相关

    """

    def __init__(self):
        """
        :param InstanceId: 目标实例ID，如cdb-jd92ijd8
        :type InstanceId: str
        :param Region: 目标实例地域，如ap-guangzhou
        :type Region: str
        :param Ip: 目标实例vip。已废弃，无需填写
        :type Ip: str
        :param Port: 目标实例vport。已废弃，无需填写
        :type Port: int
        :param ReadOnly: 目前只对MySQL有效。当为整实例迁移时，1-只读，0-可读写。
        :type ReadOnly: int
        :param User: 目标数据库账号
        :type User: str
        :param Password: 目标数据库密码
        :type Password: str
        """
        self.InstanceId = None
        self.Region = None
        self.Ip = None
        self.Port = None
        self.ReadOnly = None
        self.User = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.ReadOnly = params.get("ReadOnly")
        self.User = params.get("User")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ErrorInfo(AbstractModel):
    """迁移任务错误信息及提示

    """

    def __init__(self):
        """
        :param ErrorLog: 具体的报错日志, 包含错误码和错误信息
        :type ErrorLog: str
        :param HelpDoc: 报错对应的帮助文档Ur
        :type HelpDoc: str
        """
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 订阅实例ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MigrateDetailInfo(AbstractModel):
    """描述详细迁移过程

    """

    def __init__(self):
        """
        :param StepAll: 总步骤数
        :type StepAll: int
        :param StepNow: 当前步骤
        :type StepNow: int
        :param Progress: 总进度,如："10"
        :type Progress: str
        :param CurrentStepProgress: 当前步骤进度,如:"1"
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主从差距，MB；在增量同步阶段有效，目前支持产品为：redis和mysql
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主从差距，秒；在增量同步阶段有效，目前支持产品为：mysql
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param SrcDatabaseType: 源实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type SrcDatabaseType: str
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标实例数据库类型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type DstDatabaseType: str
        :param DstAccessType: 目标实例接入类型，目前支持：cdb(腾讯云数据库实例)
        :type DstAccessType: str
        :param DstInfo: 目标实例信息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要迁移的源数据库表信息，如果需要迁移的是整个实例，该字段为[]
        :type DatabaseInfo: str
        :param CreateTime: 任务创建(提交)时间
        :type CreateTime: str
        :param StartTime: 任务开始执行时间
        :type StartTime: str
        :param EndTime: 任务执行结束时间
        :type EndTime: str
        :param Status: 任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）
        :type Status: int
        :param Detail: 任务详情
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
        :param ErrorInfo: 任务错误信息提示，当任务发生错误时，不为null或者空值
        :type ErrorInfo: list of ErrorInfo
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
        self.ErrorInfo = None


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
        if params.get("ErrorInfo") is not None:
            self.ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfo()
                obj._deserialize(item)
                self.ErrorInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param ConsistencyType: 抽样数据一致性检测参数，1-未配置,2-全量检测,3-抽样检测, 4-仅校验不一致表,5-不检测
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
MySQL暂不支持额外参数设置。
        :type ExternParams: str
        :param ConsistencyParams: 仅用于“抽样数据一致性检测”，ConsistencyType配置为抽样检测时，必选
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param StartTime: 当前步骤开始的时间，格式为"yyyy-mm-dd hh:mm:ss"，该字段不存在或者为空是无意义
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param SrcAccessType: 源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(云上CDB实例)
        :type SrcAccessType: str
        :param SrcInfo: 源实例信息，具体内容跟迁移任务类型相关
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstAccessType: 目标实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例)，cdb(云上CDB实例). 目前只支持cdb.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeAutoRenewFlagRequest(AbstractModel):
    """ModifySubscribeAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 订阅实例ID，例如：subs-8uey736k
        :type SubscribeId: str
        :param AutoRenewFlag: 自动续费标识。1-自动续费，0-不自动续费
        :type AutoRenewFlag: int
        """
        self.SubscribeId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeAutoRenewFlagResponse(AbstractModel):
    """ModifySubscribeAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param ConsumeStartTime: 消费时间起点，也即是指定订阅数据的时间起点，时间格式如：Y-m-d h:m:s，取值范围为过去24小时之内
        :type ConsumeStartTime: str
        """
        self.SubscribeId = None
        self.ConsumeStartTime = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param SubscribeName: 数据订阅实例的名称，长度限制为[1,60]
        :type SubscribeName: str
        """
        self.SubscribeId = None
        self.SubscribeName = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param SubscribeObjectType: 数据订阅的类型，可选的值有：0 - 全实例订阅；1 - 数据订阅；2 - 结构订阅；3 - 数据订阅+结构订阅
        :type SubscribeObjectType: int
        :param Objects: 订阅的数据库表信息
        :type Objects: list of SubscribeObject
        """
        self.SubscribeId = None
        self.SubscribeObjectType = None
        self.Objects = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = []
            for item in params.get("Objects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.Objects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的ID
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeVipVportRequest(AbstractModel):
    """ModifySubscribeVipVport请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        :param DstUniqSubnetId: 指定目的子网，如果传此参数，DstIp必须在目的子网内
        :type DstUniqSubnetId: str
        :param DstIp: 目标IP，与DstPort至少传一个
        :type DstIp: str
        :param DstPort: 目标PORT，支持范围为：[1025-65535]
        :type DstPort: int
        """
        self.SubscribeId = None
        self.DstUniqSubnetId = None
        self.DstIp = None
        self.DstPort = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.DstUniqSubnetId = params.get("DstUniqSubnetId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySyncJobResponse(AbstractModel):
    """ModifySyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅实例的ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SrcInfo(AbstractModel):
    """源实例信息

    """

    def __init__(self):
        """
        :param AccessKey: 阿里云AccessKey。源库是阿里云RDS5.6适用
        :type AccessKey: str
        :param Ip: 实例的IP地址
        :type Ip: str
        :param Port: 实例的端口
        :type Port: int
        :param User: 实例的用户名
        :type User: str
        :param Password: 实例的密码
        :type Password: str
        :param RdsInstanceId: 阿里云RDS实例ID。源库是阿里云RDS5.6/5.6适用
        :type RdsInstanceId: str
        :param CvmInstanceId: CVM实例短ID，格式如：ins-olgl39y8，与云服务器控制台页面显示的实例ID相同。如果是CVM自建实例，需要传递此字段
        :type CvmInstanceId: str
        :param UniqDcgId: 专线网关ID，格式如：dcg-0rxtqqxb
        :type UniqDcgId: str
        :param VpcId: 私有网络ID，格式如：vpc-92jblxto
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID，格式如：subnet-3paxmkdz
        :type SubnetId: str
        :param UniqVpnGwId: VPN网关ID，格式如：vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param InstanceId: 数据库实例ID，格式如：cdb-powiqx8q
        :type InstanceId: str
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param Supplier: 当实例为RDS实例时，填写为aliyun, 其他情况均填写others
        :type Supplier: str
        :param CcnId: 云联网ID，如：ccn-afp6kltc
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnId: str
        :param EngineVersion: 数据库版本，当实例为RDS实例时才有效，格式如：5.6或者5.7，默认为5.6
        :type EngineVersion: str
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
        self.CcnId = None
        self.EngineVersion = None


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
        self.CcnId = params.get("CcnId")
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubscribeInfo(AbstractModel):
    """订阅实例信息

    """

    def __init__(self):
        """
        :param SubscribeId: 数据订阅的实例ID
        :type SubscribeId: str
        :param SubscribeName: 数据订阅实例的名称
        :type SubscribeName: str
        :param ChannelId: 数据订阅实例绑定的通道ID
        :type ChannelId: str
        :param Product: 数据订阅绑定实例对应的产品名称
        :type Product: str
        :param InstanceId: 数据订阅实例绑定的数据库实例ID
        :type InstanceId: str
        :param InstanceStatus: 数据订阅实例绑定的数据库实例状态
        :type InstanceStatus: str
        :param SubsStatus: 数据订阅实例的配置状态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :type SubsStatus: str
        :param ModifyTime: 上次修改时间
        :type ModifyTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param IsolateTime: 隔离时间
        :type IsolateTime: str
        :param ExpireTime: 到期时间
        :type ExpireTime: str
        :param OfflineTime: 下线时间
        :type OfflineTime: str
        :param ConsumeStartTime: 最近一次修改的消费时间起点，如果从未修改则为零值
        :type ConsumeStartTime: str
        :param Region: 数据订阅实例所属地域
        :type Region: str
        :param PayType: 计费方式，0 - 包年包月，1 - 按量计费
        :type PayType: int
        :param Vip: 数据订阅实例的Vip
        :type Vip: str
        :param Vport: 数据订阅实例的Vport
        :type Vport: int
        :param UniqVpcId: 数据订阅实例Vip所在VPC的唯一ID
        :type UniqVpcId: str
        :param UniqSubnetId: 数据订阅实例Vip所在子网的唯一ID
        :type UniqSubnetId: str
        :param Status: 数据订阅实例的状态，creating - 创建中，normal - 正常运行，isolating - 隔离中，isolated - 已隔离，offlining - 下线中，offline - 已下线
        :type Status: str
        :param SdkConsumedTime: SDK最后一条确认消息的时间戳，如果SDK一直消费，也可以作为SDK当前消费时间点
        :type SdkConsumedTime: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagItem
        :param AutoRenewFlag: 自动续费标识。0-不自动续费，1-自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param SubscribeVersion: 订阅实例版本；txdts-旧版数据订阅,kafka-kafka版本数据订阅
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeVersion: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.ModifyTime = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.Region = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.Status = None
        self.SdkConsumedTime = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.SubscribeVersion = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.ModifyTime = params.get("ModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.Region = params.get("Region")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Status = params.get("Status")
        self.SdkConsumedTime = params.get("SdkConsumedTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SubscribeVersion = params.get("SubscribeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubscribeObject(AbstractModel):
    """数据数据订阅的对象

    """

    def __init__(self):
        """
        :param ObjectsType: 数据订阅对象的类型，0-数据库，1-数据库内的表
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectsType: int
        :param DatabaseName: 订阅数据库的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param TableNames: 订阅数据库中表名称数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TableNames: list of str
        """
        self.ObjectsType = None
        self.DatabaseName = None
        self.TableNames = None


    def _deserialize(self, params):
        self.ObjectsType = params.get("ObjectsType")
        self.DatabaseName = params.get("DatabaseName")
        self.TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SubscribeRegionConf(AbstractModel):
    """数据订阅地域售卖信息

    """

    def __init__(self):
        """
        :param RegionName: 地域名称，如广州
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param Region: 地区标识，如ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Area: 地域名称，如华南地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param IsDefaultRegion: 是否为默认地域，0 - 不是，1 - 是的
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultRegion: int
        :param Status: 当前地域的售卖情况，1 - 正常， 2-灰度，3 - 停售
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.RegionName = None
        self.Region = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Region = params.get("Region")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SwitchDrToMasterResponse(AbstractModel):
    """SwitchDrToMaster返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 后台异步任务请求id
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncInstanceInfo(AbstractModel):
    """灾备同步的实例信息，记录主实例或灾备实例的信息

    """

    def __init__(self):
        """
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param InstanceId: 实例短ID
        :type InstanceId: str
        """
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncOption(AbstractModel):
    """灾备同步任务配置选项

    """

    def __init__(self):
        """
        :param SyncObject: 同步对象，1-整个实例，2-指定库表
        :type SyncObject: int
        :param RunMode: 同步开始设置，1-立即开始
        :type RunMode: int
        :param SyncType: 同步模式， 3-全量且增量同步
        :type SyncType: int
        :param ConsistencyType: 数据一致性检测， 1-无需配置
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagFilter(AbstractModel):
    """标签过滤

    """

    def __init__(self):
        """
        :param TagKey: 标签键值
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagItem(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签键值
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        