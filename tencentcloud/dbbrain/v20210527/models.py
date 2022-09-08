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


class AddUserContactRequest(AbstractModel):
    """AddUserContact请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 联系人姓名，由中英文、数字、空格、!@#$%^&*()_+-=（）组成，不能以下划线开头，长度在20以内。
        :type Name: str
        :param ContactInfo: 邮箱地址，支持大小写字母、数字、下划线及@字符， 不能以下划线开头，邮箱地址不可重复。
        :type ContactInfo: str
        :param Product: 服务产品类型，固定值："mysql"。
        :type Product: str
        """
        self.Name = None
        self.ContactInfo = None
        self.Product = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ContactInfo = params.get("ContactInfo")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 添加成功的联系人id。
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CancelKillTaskRequest(AbstractModel):
    """CancelKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKillTaskResponse(AbstractModel):
    """CancelKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: kill会话任务终止成功返回1。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ContactItem(AbstractModel):
    """联系人contact描述。

    """

    def __init__(self):
        r"""
        :param Id: 联系人id。
        :type Id: int
        :param Name: 联系人姓名。
        :type Name: str
        :param Mail: 联系人绑定的邮箱。
        :type Mail: str
        """
        self.Id = None
        self.Name = None
        self.Mail = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param StartTime: 开始时间，如“2020-11-08T14:00:00+08:00”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2020-11-09T14:00:00+08:00”。
        :type EndTime: str
        :param SendMailFlag: 是否发送邮件: 0 - 否，1 - 是。
        :type SendMailFlag: int
        :param ContactPerson: 接收邮件的联系人ID数组。
        :type ContactPerson: list of int
        :param ContactGroup: 接收邮件的联系组ID数组。
        :type ContactGroup: list of int
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认值为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SendMailFlag = None
        self.ContactPerson = None
        self.ContactGroup = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SendMailFlag = params.get("SendMailFlag")
        self.ContactPerson = params.get("ContactPerson")
        self.ContactGroup = params.get("ContactGroup")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param AsyncRequestId: 健康报告相应的任务ID，可通过DescribeDBDiagReportTasks查询。
        :type AsyncRequestId: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportUrl: 健康报告浏览地址。
        :type ReportUrl: str
        :param ExpireTime: 健康报告浏览地址到期时间戳（秒）。
        :type ExpireTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportUrl = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")


class CreateKillTaskRequest(AbstractModel):
    """CreateKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: kill会话任务的关联实例ID。
        :type InstanceId: str
        :param Duration: 任务持续时间，单位秒，手动关闭任务传-1。
        :type Duration: int
        :param Host: 任务过滤条件，客户端IP。
        :type Host: str
        :param DB: 任务过滤条件，数据库库名,多个","隔开。
        :type DB: str
        :param Command: 任务过滤条件，相关命令，多个","隔开。
        :type Command: str
        :param Info: 任务过滤条件，支持单条件前缀匹配。
        :type Info: str
        :param User: 任务过滤条件，用户类型。
        :type User: str
        :param Time: 任务过滤条件，会话持续时长，单位秒。
        :type Time: int
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Duration = None
        self.Host = None
        self.DB = None
        self.Command = None
        self.Info = None
        self.User = None
        self.Time = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Duration = params.get("Duration")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.Command = params.get("Command")
        self.Info = params.get("Info")
        self.User = params.get("User")
        self.Time = params.get("Time")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKillTaskResponse(AbstractModel):
    """CreateKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: kill会话任务创建成功返回1
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param ProfileLevel: 配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :type ProfileLevel: str
        :param ProfileName: 配置名称，需要保持唯一性，数据库巡检邮件配置名称自拟；定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :type Product: str
        :param BindInstanceIds: 配置绑定的实例ID，当配置级别为"Instance"时需要传入且只能为一个实例；当配置级别为“User”时，此参数不填。
        :type BindInstanceIds: list of str
        """
        self.ProfileInfo = None
        self.ProfileLevel = None
        self.ProfileName = None
        self.ProfileType = None
        self.Product = None
        self.BindInstanceIds = None


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        self.ProfileLevel = params.get("ProfileLevel")
        self.ProfileName = params.get("ProfileName")
        self.ProfileType = params.get("ProfileType")
        self.Product = params.get("Product")
        self.BindInstanceIds = params.get("BindInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProxySessionKillTaskRequest(AbstractModel):
    """CreateProxySessionKillTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self.InstanceId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxySessionKillTaskResponse(AbstractModel):
    """CreateProxySessionKillTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 创建 kill 会话任务返回的异步任务 id
        :type AsyncRequestId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param WeekConfiguration: 取值范围1-7，分别代表周一至周日。
        :type WeekConfiguration: list of int
        :param ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        :param ProfileName: 配置名称，需要保持唯一性，定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param BindInstanceId: 配置订阅的实例ID。
        :type BindInstanceId: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.WeekConfiguration = None
        self.ProfileInfo = None
        self.ProfileName = None
        self.BindInstanceId = None
        self.Product = None


    def _deserialize(self, params):
        self.WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        self.ProfileName = params.get("ProfileName")
        self.BindInstanceId = params.get("BindInstanceId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityAuditLogExportTaskRequest(AbstractModel):
    """CreateSecurityAuditLogExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param StartTime: 导出日志开始时间，例如2020-12-28 00:00:00。
        :type StartTime: str
        :param EndTime: 导出日志结束时间，例如2020-12-28 01:00:00。
        :type EndTime: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param DangerLevels: 日志风险等级列表，支持值包括：0 无风险；1 低风险；2 中风险；3 高风险。
        :type DangerLevels: list of int
        """
        self.SecAuditGroupId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None
        self.DangerLevels = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        self.DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityAuditLogExportTaskResponse(AbstractModel):
    """CreateSecurityAuditLogExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 日志导出任务Id。
        :type AsyncRequestId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateSqlFilterRequest(AbstractModel):
    """CreateSqlFilter请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param SqlType: SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :type SqlType: str
        :param FilterKey: 关键字，用于筛选SQL语句，多个关键字用英文逗号分隔，逗号不能作为关键词，多个关键词之间的关系为“逻辑与”。
        :type FilterKey: str
        :param MaxConcurrency: 最大并发度，取值不能小于0，如果该值设为 0，则表示限制所有匹配的SQL执行。
        :type MaxConcurrency: int
        :param Duration: 限流时长，单位秒，支持-1和小于2147483647的正整数，-1表示永不过期。
        :type Duration: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.SessionToken = None
        self.SqlType = None
        self.FilterKey = None
        self.MaxConcurrency = None
        self.Duration = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SessionToken = params.get("SessionToken")
        self.SqlType = params.get("SqlType")
        self.FilterKey = params.get("FilterKey")
        self.MaxConcurrency = params.get("MaxConcurrency")
        self.Duration = params.get("Duration")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSqlFilterResponse(AbstractModel):
    """CreateSqlFilter返回参数结构体

    """

    def __init__(self):
        r"""
        :param FilterId: 限流任务ID。
        :type FilterId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FilterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FilterId = params.get("FilterId")
        self.RequestId = params.get("RequestId")


class DeleteSecurityAuditLogExportTasksRequest(AbstractModel):
    """DeleteSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param AsyncRequestIds: 日志导出任务Id列表，接口会忽略不存在或已删除的任务Id。
        :type AsyncRequestIds: list of int non-negative
        :param Product: 服务产品类型，支持值： "mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self.SecAuditGroupId = None
        self.AsyncRequestIds = None
        self.Product = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityAuditLogExportTasksResponse(AbstractModel):
    """DeleteSecurityAuditLogExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSqlFiltersRequest(AbstractModel):
    """DeleteSqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param FilterIds: 限流任务ID列表。
        :type FilterIds: list of int
        """
        self.InstanceId = None
        self.SessionToken = None
        self.FilterIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SessionToken = params.get("SessionToken")
        self.FilterIds = params.get("FilterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSqlFiltersResponse(AbstractModel):
    """DeleteSqlFilters返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param Names: 联系人名数组，支持模糊搜索。
        :type Names: list of str
        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 联系人的总数量。
        :type TotalCount: int
        :param Contacts: 联系人的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Contacts: list of ContactItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Contacts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Contacts") is not None:
            self.Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self.Contacts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param Names: 联系组名称数组，支持模糊搜索。
        :type Names: list of str
        """
        self.Product = None
        self.Names = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 组总数。
        :type TotalCount: int
        :param Groups: 组信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GroupItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param EventId: 事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。
        :type EventId: int
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.EventId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiagItem: 诊断项。
        :type DiagItem: str
        :param DiagType: 诊断类型。
        :type DiagType: str
        :param EventId: 事件 ID 。
        :type EventId: int
        :param Explanation: 诊断事件详情，若无附加解释信息则输出为空。
        :type Explanation: str
        :param Outline: 诊断概要。
        :type Outline: str
        :param Problem: 诊断出的问题。
        :type Problem: str
        :param Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param Suggestions: 诊断建议，若无建议则输出为空。
        :type Suggestions: str
        :param Metric: 保留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiagItem = None
        self.DiagType = None
        self.EventId = None
        self.Explanation = None
        self.Outline = None
        self.Problem = None
        self.Severity = None
        self.StartTime = None
        self.Suggestions = None
        self.Metric = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.DiagType = params.get("DiagType")
        self.EventId = params.get("EventId")
        self.Explanation = params.get("Explanation")
        self.Outline = params.get("Outline")
        self.Problem = params.get("Problem")
        self.Severity = params.get("Severity")
        self.StartTime = params.get("StartTime")
        self.Suggestions = params.get("Suggestions")
        self.Metric = params.get("Metric")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeDBDiagEventsRequest(AbstractModel):
    """DescribeDBDiagEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间，如“2021-05-27 00:00:00”，支持的最早查询时间为当前时间的前30天。
        :type StartTime: str
        :param EndTime: 结束时间，如“2021-05-27 01:00:00”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param Severities: 风险等级列表，取值按影响程度从高至低分别为：1 - 致命、2 -严重、3 - 告警、4 - 提示、5 -健康。
        :type Severities: list of int
        :param InstanceIds: 实例ID列表。
        :type InstanceIds: list of str
        :param Offset: 偏移量，默认0。
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值为50。
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Severities = None
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Severities = params.get("Severities")
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventsResponse(AbstractModel):
    """DescribeDBDiagEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 诊断事件的总数目。
        :type TotalCount: int
        :param Items: 诊断事件的列表。
        :type Items: list of DiagHistoryEventItem
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
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
        :type EndTime: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Events: 事件描述。
        :type Events: list of DiagHistoryEventItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 第一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param EndTime: 最后一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param InstanceIds: 实例ID数组，用于筛选指定实例的任务列表。
        :type InstanceIds: list of str
        :param Sources: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :type Sources: list of str
        :param HealthLevels: 报告的健康等级，支持的取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK" - 危险；"HIGH_RISK" - 高危。
        :type HealthLevels: str
        :param TaskStatuses: 任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :type TaskStatuses: str
        :param Offset: 偏移量，默认0。
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值为100。
        :type Limit: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceIds = None
        self.Sources = None
        self.HealthLevels = None
        self.TaskStatuses = None
        self.Offset = None
        self.Limit = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceIds = params.get("InstanceIds")
        self.Sources = params.get("Sources")
        self.HealthLevels = params.get("HealthLevels")
        self.TaskStatuses = params.get("TaskStatuses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 任务总数目。
        :type TotalCount: int
        :param Tasks: 任务列表。
        :type Tasks: list of HealthReportTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param RangeDays: 时间段天数，截止日期为当日，默认为7天。
        :type RangeDays: int
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.RangeDays = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RangeDays = params.get("RangeDays")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Growth: 磁盘增长量(MB)。
        :type Growth: int
        :param Remain: 磁盘剩余(MB)。
        :type Remain: int
        :param Total: 磁盘总量(MB)。
        :type Total: int
        :param AvailableDays: 预计可用天数。
        :type AvailableDays: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Growth = None
        self.Remain = None
        self.Total = None
        self.AvailableDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Growth = params.get("Growth")
        self.Remain = params.get("Remain")
        self.Total = params.get("Total")
        self.AvailableDays = params.get("AvailableDays")
        self.RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param IsSupported: 是否是DBbrain支持的实例，固定传 true。
        :type IsSupported: bool
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param Offset: 分页参数，偏移量。
        :type Offset: int
        :param Limit: 分页参数，分页值，最大值为100。
        :type Limit: int
        :param InstanceNames: 根据实例名称条件查询。
        :type InstanceNames: list of str
        :param InstanceIds: 根据实例ID条件查询。
        :type InstanceIds: list of str
        :param Regions: 根据地域条件查询。
        :type Regions: list of str
        """
        self.IsSupported = None
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.InstanceNames = None
        self.InstanceIds = None
        self.Regions = None


    def _deserialize(self, params):
        self.IsSupported = params.get("IsSupported")
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceNames = params.get("InstanceNames")
        self.InstanceIds = params.get("InstanceIds")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例总数。
        :type TotalCount: int
        :param DbScanStatus: 全实例巡检状态：0：开启全实例巡检；1：未开启全实例巡检。
        :type DbScanStatus: int
        :param Items: 实例相关信息。
        :type Items: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DbScanStatus = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 需要获取健康得分的实例ID。
        :type InstanceId: str
        :param Time: 获取健康得分的时间，时间格式如：2019-09-10 12:13:14。
        :type Time: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Time = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Time = params.get("Time")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 健康得分以及异常扣分项。
        :type Data: :class:`tencentcloud.dbbrain.v20210527.models.HealthScoreInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = HealthScoreInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页单位，最大支持50。
        :type Limit: int
        :param ProfileName: 根据邮件配置名称查询，定期发送的邮件配置名称遵循："scheduler_"+{instanceId}的规则。
        :type ProfileName: str
        """
        self.ProfileType = None
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.ProfileName = None


    def _deserialize(self, params):
        self.ProfileType = params.get("ProfileType")
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProfileList: 邮件配置详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileList: list of UserProfile
        :param TotalCount: 邮件配置总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProfileList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProfileList") is not None:
            self.ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self.ProfileList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMySqlProcessListRequest(AbstractModel):
    """DescribeMySqlProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param ID: 线程的ID，用于筛选线程列表。
        :type ID: int
        :param User: 线程的操作账号名，用于筛选线程列表。
        :type User: str
        :param Host: 线程的操作主机地址，用于筛选线程列表。
        :type Host: str
        :param DB: 线程的操作数据库，用于筛选线程列表。
        :type DB: str
        :param State: 线程的操作状态，用于筛选线程列表。
        :type State: str
        :param Command: 线程的执行类型，用于筛选线程列表。
        :type Command: str
        :param Time: 线程的操作时长最小值，单位秒，用于筛选操作时长大于该值的线程列表。
        :type Time: int
        :param Info: 线程的操作语句，用于筛选线程列表。
        :type Info: str
        :param Limit: 返回数量，默认20。
        :type Limit: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None
        self.Limit = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        self.Limit = params.get("Limit")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySqlProcessListResponse(AbstractModel):
    """DescribeMySqlProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProcessList: 实时线程列表。
        :type ProcessList: list of MySqlProcess
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProcessList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProcessList") is not None:
            self.ProcessList = []
            for item in params.get("ProcessList"):
                obj = MySqlProcess()
                obj._deserialize(item)
                self.ProcessList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNoPrimaryKeyTablesRequest(AbstractModel):
    """DescribeNoPrimaryKeyTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Date: 查询日期，如2021-05-27，最早为30天前的日期。
        :type Date: str
        :param Limit: 查询数目，默认为20，最大为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Date = None
        self.Limit = None
        self.Offset = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNoPrimaryKeyTablesResponse(AbstractModel):
    """DescribeNoPrimaryKeyTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param NoPrimaryKeyTableCount: 无主键表总数。
        :type NoPrimaryKeyTableCount: int
        :param NoPrimaryKeyTableCountDiff: 与昨日扫描无主键表的差值，正数为增加，负数为减少，0为无变化。
        :type NoPrimaryKeyTableCountDiff: int
        :param NoPrimaryKeyTableRecordCount: 记录的无主键表总数（不超过无主键表总数），可用于分页查询。
        :type NoPrimaryKeyTableRecordCount: int
        :param NoPrimaryKeyTables: 无主键表列表。
        :type NoPrimaryKeyTables: list of Table
        :param Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NoPrimaryKeyTableCount = None
        self.NoPrimaryKeyTableCountDiff = None
        self.NoPrimaryKeyTableRecordCount = None
        self.NoPrimaryKeyTables = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoPrimaryKeyTableCount = params.get("NoPrimaryKeyTableCount")
        self.NoPrimaryKeyTableCountDiff = params.get("NoPrimaryKeyTableCountDiff")
        self.NoPrimaryKeyTableRecordCount = params.get("NoPrimaryKeyTableRecordCount")
        if params.get("NoPrimaryKeyTables") is not None:
            self.NoPrimaryKeyTables = []
            for item in params.get("NoPrimaryKeyTables"):
                obj = Table()
                obj._deserialize(item)
                self.NoPrimaryKeyTables.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeProxySessionKillTasksRequest(AbstractModel):
    """DescribeProxySessionKillTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param AsyncRequestIds: kill 会话异步任务 ID,  接口 CreateProxySessionKillTask 调用成功后获取。
        :type AsyncRequestIds: list of int
        :param Product: 服务产品类型，支持值包括： "redis" - 云数据库 Redis。
        :type Product: str
        """
        self.InstanceId = None
        self.AsyncRequestIds = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySessionKillTasksResponse(AbstractModel):
    """DescribeProxySessionKillTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: kill 任务的详情。
        :type Tasks: list of TaskInfo
        :param TotalCount: 任务总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRedisTopBigKeysRequest(AbstractModel):
    """DescribeRedisTopBigKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Date: 查询日期，如2021-05-27，最早可为前30天的日期。
        :type Date: str
        :param Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param SortBy: 排序字段，取值包括Capacity - 内存，ItemCount - 元素数量，默认为Capacity。
        :type SortBy: str
        :param KeyType: key类型筛选条件，默认为不进行筛选，取值包括string, list, set, hash, sortedset, stream。
        :type KeyType: str
        :param Limit: 查询数目，默认为20，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Date = None
        self.Product = None
        self.SortBy = None
        self.KeyType = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.Product = params.get("Product")
        self.SortBy = params.get("SortBy")
        self.KeyType = params.get("KeyType")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopBigKeysResponse(AbstractModel):
    """DescribeRedisTopBigKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopKeys: top key列表。
        :type TopKeys: list of RedisKeySpaceData
        :param Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopKeys = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopKeys") is not None:
            self.TopKeys = []
            for item in params.get("TopKeys"):
                obj = RedisKeySpaceData()
                obj._deserialize(item)
                self.TopKeys.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeRedisTopKeyPrefixListRequest(AbstractModel):
    """DescribeRedisTopKeyPrefixList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Date: 查询日期，如2021-05-27，最早可为前30天的日期。
        :type Date: str
        :param Product: 服务产品类型，支持值包括 "redis" - 云数据库 Redis。
        :type Product: str
        :param Limit: 查询数目，默认为20，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Date = None
        self.Product = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.Product = params.get("Product")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRedisTopKeyPrefixListResponse(AbstractModel):
    """DescribeRedisTopKeyPrefixList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: top key前缀列表。
        :type Items: list of RedisPreKeySpaceData
        :param Timestamp: 采集时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RedisPreKeySpaceData()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeSecurityAuditLogDownloadUrlsRequest(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self.SecAuditGroupId = None
        self.AsyncRequestId = None
        self.Product = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogDownloadUrlsResponse(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param Urls: 导出结果的COS链接列表。当结果集很大时，可能会切分为多个url下载。
        :type Urls: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Urls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.RequestId = params.get("RequestId")


class DescribeSecurityAuditLogExportTasksRequest(AbstractModel):
    """DescribeSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param AsyncRequestIds: 日志导出任务Id列表。
        :type AsyncRequestIds: list of int non-negative
        :param Offset: 偏移量，默认0。
        :type Offset: int
        :param Limit: 返回数量，默认20，最大值为100。
        :type Limit: int
        """
        self.SecAuditGroupId = None
        self.Product = None
        self.AsyncRequestIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SecAuditGroupId = params.get("SecAuditGroupId")
        self.Product = params.get("Product")
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogExportTasksResponse(AbstractModel):
    """DescribeSecurityAuditLogExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 安全审计日志导出任务列表。
        :type Tasks: list of SecLogExportTaskInfo
        :param TotalCount: 安全审计日志导出任务总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = SecLogExportTaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2019-09-10 12:13:14”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param Period: 柱间单位时间间隔，单位为秒。
        :type Period: int
        :param TimeSeries: 单位时间间隔内慢日志数量统计。
        :type TimeSeries: list of TimeSlice
        :param SeriesData: 单位时间间隔内的实例 cpu 利用率监控数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.TimeSeries = None
        self.SeriesData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self.TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self.TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 截止时间，如“2019-09-11 10:13:14”，截止时间与开始时间的间隔小于7天。
        :type EndTime: str
        :param SortBy: 排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键，默认为QueryTime。
        :type SortBy: str
        :param OrderBy: 排序方式，支持ASC（升序）以及DESC（降序），默认为DESC。
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param SchemaList: 数据库名称数组。
        :type SchemaList: list of SchemaItem
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.SchemaList = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self.SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self.SchemaList.append(obj)
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param Rows: 慢日志 top sql 列表
        :type Rows: list of SlowLogTopSqlItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param StartTime: 查询范围的开始时间，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param EndTime: 查询范围的结束时间，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param Md5: SOL模板的MD5值
        :type Md5: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None
        self.Md5 = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 来源地址数目。
        :type TotalCount: int
        :param Items: 各来源地址的慢日志占比详情列表。
        :type Items: list of SlowLogHost
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
                obj = SlowLogHost()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSqlFiltersRequest(AbstractModel):
    """DescribeSqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param FilterIds: 任务ID列表，用于筛选任务列表。
        :type FilterIds: list of int
        :param Statuses: 任务状态列表，用于筛选任务列表，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :type Statuses: list of str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.FilterIds = None
        self.Statuses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FilterIds = params.get("FilterIds")
        self.Statuses = params.get("Statuses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlFiltersResponse(AbstractModel):
    """DescribeSqlFilters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 限流任务总数目。
        :type TotalCount: int
        :param Items: 限流任务列表。
        :type Items: list of SQLFilter
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
                obj = SQLFilter()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSqlTemplateRequest(AbstractModel):
    """DescribeSqlTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Schema: 数据库名。
        :type Schema: str
        :param SqlText: SQL语句。
        :type SqlText: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Schema = None
        self.SqlText = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Schema = params.get("Schema")
        self.SqlText = params.get("SqlText")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSqlTemplateResponse(AbstractModel):
    """DescribeSqlTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schema: 数据库名。
        :type Schema: str
        :param SqlText: SQL语句。
        :type SqlText: str
        :param SqlType: SQL类型。
        :type SqlType: str
        :param SqlTemplate: SQL模版内容。
        :type SqlTemplate: str
        :param SqlId: SQL模版ID。
        :type SqlId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schema = None
        self.SqlText = None
        self.SqlType = None
        self.SqlTemplate = None
        self.SqlId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schema = params.get("Schema")
        self.SqlText = params.get("SqlText")
        self.SqlType = params.get("SqlType")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlId = params.get("SqlId")
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.StartDate = None
        self.EndDate = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopSpaceSchemaTimeSeries: 返回的Top库空间统计信息的时序数据列表。
        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceSchemaTimeSeries = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self.TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self.TopSpaceSchemaTimeSeries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopSpaceSchemas: 返回的Top库空间统计信息列表。
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param Timestamp: 采集库空间数据的时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceSchemas = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self.TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self.TopSpaceSchemas.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :type SortBy: str
        :param StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.StartDate = None
        self.EndDate = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopSpaceTableTimeSeries: 返回的Top表空间统计信息的时序数据列表。
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceTableTimeSeries = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self.TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self.TopSpaceTableTimeSeries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopSpaceTables: 返回的Top表空间统计信息列表。
        :type TopSpaceTables: list of TableSpaceData
        :param Timestamp: 采集表空间数据的时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceTables = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self.TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self.TopSpaceTables.append(obj)
        self.Timestamp = params.get("Timestamp")
        self.RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param SqlText: SQL语句。
        :type SqlText: str
        :param Schema: 库名。
        :type Schema: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL；"dbbrain-mysql" - 自建 MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.SqlText = None
        self.Schema = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Advices: SQL优化建议，可解析为JSON数组，无需优化时输出为空。
        :type Advices: str
        :param Comments: SQL优化建议备注，可解析为String数组，无需优化时输出为空。
        :type Comments: str
        :param SqlText: SQL语句。
        :type SqlText: str
        :param Schema: 库名。
        :type Schema: str
        :param Tables: 相关表的DDL信息，可解析为JSON数组。
        :type Tables: str
        :param SqlPlan: SQL执行计划，可解析为JSON，无需优化时输出为空。
        :type SqlPlan: str
        :param Cost: SQL优化后的成本节约详情，可解析为JSON，无需优化时输出为空。
        :type Cost: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Advices = None
        self.Comments = None
        self.SqlText = None
        self.Schema = None
        self.Tables = None
        self.SqlPlan = None
        self.Cost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Advices = params.get("Advices")
        self.Comments = params.get("Comments")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.Tables = params.get("Tables")
        self.SqlPlan = params.get("SqlPlan")
        self.Cost = params.get("Cost")
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """实例诊断历史事件

    """

    def __init__(self):
        r"""
        :param DiagType: 诊断类型。
        :type DiagType: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EventId: 事件唯一ID 。
        :type EventId: int
        :param Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param Outline: 诊断概要。
        :type Outline: str
        :param DiagItem: 诊断项说明。
        :type DiagItem: str
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Metric: 保留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Region: 地域。
        :type Region: str
        """
        self.DiagType = None
        self.EndTime = None
        self.StartTime = None
        self.EventId = None
        self.Severity = None
        self.Outline = None
        self.DiagItem = None
        self.InstanceId = None
        self.Metric = None
        self.Region = None


    def _deserialize(self, params):
        self.DiagType = params.get("DiagType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.EventId = params.get("EventId")
        self.Severity = params.get("Severity")
        self.Outline = params.get("Outline")
        self.DiagItem = params.get("DiagItem")
        self.InstanceId = params.get("InstanceId")
        self.Metric = params.get("Metric")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """异常事件信息。

    """

    def __init__(self):
        r"""
        :param EventId: 事件 ID 。
        :type EventId: int
        :param DiagType: 诊断类型。
        :type DiagType: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param Outline: 概要。
        :type Outline: str
        :param Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param ScoreLost: 扣分。
        :type ScoreLost: int
        :param Metric: 保留字段。
        :type Metric: str
        :param Count: 告警数目。
        :type Count: int
        """
        self.EventId = None
        self.DiagType = None
        self.StartTime = None
        self.EndTime = None
        self.Outline = None
        self.Severity = None
        self.ScoreLost = None
        self.Metric = None
        self.Count = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.DiagType = params.get("DiagType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Outline = params.get("Outline")
        self.Severity = params.get("Severity")
        self.ScoreLost = params.get("ScoreLost")
        self.Metric = params.get("Metric")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """描述组信息。

    """

    def __init__(self):
        r"""
        :param Id: 组id。
        :type Id: int
        :param Name: 组名称。
        :type Name: str
        :param MemberCount: 组成员数量。
        :type MemberCount: int
        """
        self.Id = None
        self.Name = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """健康报告任务详情。

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务请求 ID。
        :type AsyncRequestId: int
        :param Source: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :type Source: str
        :param Progress: 任务完成进度，单位%。
        :type Progress: int
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param StartTime: 任务开始执行时间。
        :type StartTime: str
        :param EndTime: 任务完成执行时间。
        :type EndTime: str
        :param InstanceInfo: 任务所属实例的基础信息。
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20210527.models.InstanceBasicInfo`
        :param HealthStatus: 健康报告中的健康信息。
        :type HealthStatus: :class:`tencentcloud.dbbrain.v20210527.models.HealthStatus`
        """
        self.AsyncRequestId = None
        self.Source = None
        self.Progress = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceInfo = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Source = params.get("Source")
        self.Progress = params.get("Progress")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self.InstanceInfo = InstanceBasicInfo()
            self.InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self.HealthStatus = HealthStatus()
            self.HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """获取健康得分返回的详情。

    """

    def __init__(self):
        r"""
        :param IssueTypes: 异常详情。
        :type IssueTypes: list of IssueTypeInfo
        :param EventsTotalCount: 异常事件总数。
        :type EventsTotalCount: int
        :param HealthScore: 健康得分。
        :type HealthScore: int
        :param HealthLevel: 健康等级, 如："HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"。
        :type HealthLevel: str
        """
        self.IssueTypes = None
        self.EventsTotalCount = None
        self.HealthScore = None
        self.HealthLevel = None


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self.IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self.IssueTypes.append(obj)
        self.EventsTotalCount = params.get("EventsTotalCount")
        self.HealthScore = params.get("HealthScore")
        self.HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """实例健康详情。

    """

    def __init__(self):
        r"""
        :param HealthScore: 健康分数，满分100。
        :type HealthScore: int
        :param HealthLevel: 健康等级，取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK"- 危险；"HIGH_RISK" - 高危。
        :type HealthLevel: str
        :param ScoreLost: 总扣分分数。
        :type ScoreLost: int
        :param ScoreDetails: 扣分详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScoreDetails: list of ScoreDetail
        """
        self.HealthScore = None
        self.HealthLevel = None
        self.ScoreLost = None
        self.ScoreDetails = None


    def _deserialize(self, params):
        self.HealthScore = params.get("HealthScore")
        self.HealthLevel = params.get("HealthLevel")
        self.ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self.ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self.ScoreDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """实例基础信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param Vip: 实例内网IP。
        :type Vip: str
        :param Vport: 实例内网Port。
        :type Vport: int
        :param Product: 实例产品。
        :type Product: str
        :param EngineVersion: 实例引擎版本。
        :type EngineVersion: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.Product = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Product = params.get("Product")
        self.EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """实例配置。

    """

    def __init__(self):
        r"""
        :param DailyInspection: 数据库巡检开关, Yes/No。
        :type DailyInspection: str
        :param OverviewDisplay: 实例概览开关，Yes/No。
        :type OverviewDisplay: str
        """
        self.DailyInspection = None
        self.OverviewDisplay = None


    def _deserialize(self, params):
        self.DailyInspection = params.get("DailyInspection")
        self.OverviewDisplay = params.get("OverviewDisplay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """查询实例列表，返回实例的相关信息的对象。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param Region: 实例所属地域。
        :type Region: str
        :param HealthScore: 健康得分。
        :type HealthScore: int
        :param Product: 所属产品。
        :type Product: str
        :param EventCount: 异常事件数量。
        :type EventCount: int
        :param InstanceType: 实例类型：1:MASTER；2:DR，3：RO，4:SDR。
        :type InstanceType: int
        :param Cpu: 核心数。
        :type Cpu: int
        :param Memory: 内存，单位MB。
        :type Memory: int
        :param Volume: 硬盘存储，单位GB。
        :type Volume: int
        :param EngineVersion: 数据库版本。
        :type EngineVersion: str
        :param Vip: 内网地址。
        :type Vip: str
        :param Vport: 内网端口。
        :type Vport: int
        :param Source: 接入来源。
        :type Source: str
        :param GroupId: 分组ID。
        :type GroupId: str
        :param GroupName: 分组组名。
        :type GroupName: str
        :param Status: 实例状态：0：发货中；1：运行正常；4：销毁中；5：隔离中。
        :type Status: int
        :param UniqSubnetId: 子网统一ID。
        :type UniqSubnetId: str
        :param DeployMode: cdb类型。
        :type DeployMode: str
        :param InitFlag: cdb实例初始化标志：0：未初始化；1：已初始化。
        :type InitFlag: int
        :param TaskStatus: 任务状态。
        :type TaskStatus: int
        :param UniqVpcId: 私有网络统一ID。
        :type UniqVpcId: str
        :param InstanceConf: 实例巡检/概览的状态。
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param DeadlineTime: 资源到期时间。
        :type DeadlineTime: str
        :param IsSupported: 是否是DBbrain支持的实例。
        :type IsSupported: bool
        :param SecAuditStatus: 实例安全审计日志开启状态：ON： 安全审计开启；OFF： 未开启安全审计。
        :type SecAuditStatus: str
        :param AuditPolicyStatus: 实例审计日志开启状态，ALL_AUDIT： 开启全审计；RULE_AUDIT： 开启规则审计；UNBOUND： 未开启审计。
        :type AuditPolicyStatus: str
        :param AuditRunningStatus: 实例审计日志运行状态：normal： 运行中； paused： 欠费暂停。
        :type AuditRunningStatus: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.HealthScore = None
        self.Product = None
        self.EventCount = None
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.Vip = None
        self.Vport = None
        self.Source = None
        self.GroupId = None
        self.GroupName = None
        self.Status = None
        self.UniqSubnetId = None
        self.DeployMode = None
        self.InitFlag = None
        self.TaskStatus = None
        self.UniqVpcId = None
        self.InstanceConf = None
        self.DeadlineTime = None
        self.IsSupported = None
        self.SecAuditStatus = None
        self.AuditPolicyStatus = None
        self.AuditRunningStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.HealthScore = params.get("HealthScore")
        self.Product = params.get("Product")
        self.EventCount = params.get("EventCount")
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Source = params.get("Source")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Status = params.get("Status")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.DeployMode = params.get("DeployMode")
        self.InitFlag = params.get("InitFlag")
        self.TaskStatus = params.get("TaskStatus")
        self.UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self.InstanceConf = InstanceConfs()
            self.InstanceConf._deserialize(params.get("InstanceConf"))
        self.DeadlineTime = params.get("DeadlineTime")
        self.IsSupported = params.get("IsSupported")
        self.SecAuditStatus = params.get("SecAuditStatus")
        self.AuditPolicyStatus = params.get("AuditPolicyStatus")
        self.AuditRunningStatus = params.get("AuditRunningStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """指标信息。

    """

    def __init__(self):
        r"""
        :param IssueType: 指标分类：AVAILABILITY：可用性，MAINTAINABILITY：可维护性，PERFORMANCE，性能，RELIABILITY可靠性。
        :type IssueType: str
        :param Events: 异常事件。
        :type Events: list of EventInfo
        :param TotalCount: 异常事件总数。
        :type TotalCount: int
        """
        self.IssueType = None
        self.Events = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self.Events.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsRequest(AbstractModel):
    """KillMySqlThreads请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Stage: kill会话任务的阶段，取值包括："Prepare"-准备阶段，"Commit"-提交阶段。
        :type Stage: str
        :param Threads: 需要kill的sql会话ID列表，此参数用于Prepare阶段。
        :type Threads: list of int
        :param SqlExecId: 执行ID，此参数用于Commit阶段。
        :type SqlExecId: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Stage = None
        self.Threads = None
        self.SqlExecId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Stage = params.get("Stage")
        self.Threads = params.get("Threads")
        self.SqlExecId = params.get("SqlExecId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMySqlThreadsResponse(AbstractModel):
    """KillMySqlThreads返回参数结构体

    """

    def __init__(self):
        r"""
        :param Threads: kill完成的sql会话ID列表。
        :type Threads: list of int
        :param SqlExecId: 执行ID， Prepare阶段的任务输出，用于Commit阶段中指定执行kill操作的会话ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlExecId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Threads = None
        self.SqlExecId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Threads = params.get("Threads")
        self.SqlExecId = params.get("SqlExecId")
        self.RequestId = params.get("RequestId")


class MailConfiguration(AbstractModel):
    """邮件发送配置

    """

    def __init__(self):
        r"""
        :param SendMail: 是否开启邮件发送: 0, 否; 1, 是。
        :type SendMail: int
        :param Region: 地域配置, 如["ap-guangzhou", "ap-shanghai"]。巡检的邮件发送模板，配置需要发送巡检邮件的地域；订阅的邮件发送模板，配置当前订阅实例的所属地域。
        :type Region: list of str
        :param HealthStatus: 发送指定的健康等级的报告, 如["HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"]。
        :type HealthStatus: list of str
        :param ContactPerson: 联系人id, 联系人/联系组不能都为空。
        :type ContactPerson: list of int
        :param ContactGroup: 联系组id, 联系人/联系组不能都为空。
        :type ContactGroup: list of int
        """
        self.SendMail = None
        self.Region = None
        self.HealthStatus = None
        self.ContactPerson = None
        self.ContactGroup = None


    def _deserialize(self, params):
        self.SendMail = params.get("SendMail")
        self.Region = params.get("Region")
        self.HealthStatus = params.get("HealthStatus")
        self.ContactPerson = params.get("ContactPerson")
        self.ContactGroup = params.get("ContactGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceConfs: 实例配置，包括巡检、概览开关等。
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20210527.models.InstanceConfs`
        :param Regions: 生效实例地域，取值为"All"，代表全地域。
        :type Regions: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :type Product: str
        :param InstanceIds: 指定更改巡检状态的实例ID。
        :type InstanceIds: list of str
        """
        self.InstanceConfs = None
        self.Regions = None
        self.Product = None
        self.InstanceIds = None


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self.InstanceConfs = InstanceConfs()
            self.InstanceConfs._deserialize(params.get("InstanceConfs"))
        self.Regions = params.get("Regions")
        self.Product = params.get("Product")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySqlFiltersRequest(AbstractModel):
    """ModifySqlFilters请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param SessionToken: 通过VerifyUserAccount获取有效期为5分钟的会话token，使用后会自动延长token有效期至五分钟后。
        :type SessionToken: str
        :param FilterIds: SQL限流任务ID列表。
        :type FilterIds: list of int
        :param Status: 限流任务状态，取值支持TERMINATED - 终止。
        :type Status: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.SessionToken = None
        self.FilterIds = None
        self.Status = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SessionToken = params.get("SessionToken")
        self.FilterIds = params.get("FilterIds")
        self.Status = params.get("Status")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySqlFiltersResponse(AbstractModel):
    """ModifySqlFilters返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """监控数据（浮点型）

    """

    def __init__(self):
        r"""
        :param Metric: 指标名称。
        :type Metric: str
        :param Unit: 指标单位。
        :type Unit: str
        :param Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据（浮点型）

    """

    def __init__(self):
        r"""
        :param Series: 监控指标。
        :type Series: list of MonitorFloatMetric
        :param Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """监控数据

    """

    def __init__(self):
        r"""
        :param Metric: 指标名称。
        :type Metric: str
        :param Unit: 指标单位。
        :type Unit: str
        :param Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据

    """

    def __init__(self):
        r"""
        :param Series: 监控指标。
        :type Series: list of MonitorMetric
        :param Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySqlProcess(AbstractModel):
    """关系型数据库线程

    """

    def __init__(self):
        r"""
        :param ID: 线程ID。
        :type ID: str
        :param User: 线程的操作账号名。
        :type User: str
        :param Host: 线程的操作主机地址。
        :type Host: str
        :param DB: 线程的操作数据库。
        :type DB: str
        :param State: 线程的操作状态。
        :type State: str
        :param Command: 线程的执行类型。
        :type Command: str
        :param Time: 线程的操作时长，单位秒。
        :type Time: str
        :param Info: 线程的操作语句。
        :type Info: str
        """
        self.ID = None
        self.User = None
        self.Host = None
        self.DB = None
        self.State = None
        self.Command = None
        self.Time = None
        self.Info = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.DB = params.get("DB")
        self.State = params.get("State")
        self.Command = params.get("Command")
        self.Time = params.get("Time")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """用户配置的信息

    """

    def __init__(self):
        r"""
        :param Language: 语言, 如"zh"。
        :type Language: str
        :param MailConfiguration: 邮件模板的内容。
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20210527.models.MailConfiguration`
        """
        self.Language = None
        self.MailConfiguration = None


    def _deserialize(self, params):
        self.Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self.MailConfiguration = MailConfiguration()
            self.MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisKeySpaceData(AbstractModel):
    """redis key空间信息。

    """

    def __init__(self):
        r"""
        :param Key: key名。
        :type Key: str
        :param Type: key类型。
        :type Type: str
        :param Encoding: key编码方式。
        :type Encoding: str
        :param ExpireTime: key过期时间戳（毫秒），0代表未设置过期时间。
        :type ExpireTime: int
        :param Length: key内存大小，单位Byte。
        :type Length: int
        :param ItemCount: 元素个数。
        :type ItemCount: int
        :param MaxElementSize: 最大元素长度。
        :type MaxElementSize: int
        """
        self.Key = None
        self.Type = None
        self.Encoding = None
        self.ExpireTime = None
        self.Length = None
        self.ItemCount = None
        self.MaxElementSize = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Encoding = params.get("Encoding")
        self.ExpireTime = params.get("ExpireTime")
        self.Length = params.get("Length")
        self.ItemCount = params.get("ItemCount")
        self.MaxElementSize = params.get("MaxElementSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisPreKeySpaceData(AbstractModel):
    """redis key前缀空间信息

    """

    def __init__(self):
        r"""
        :param AveElementSize: 平均元素长度。
        :type AveElementSize: int
        :param Length: 总占用内存（Byte）。
        :type Length: int
        :param KeyPreIndex: key前缀。
        :type KeyPreIndex: str
        :param ItemCount: 元素数量。
        :type ItemCount: int
        :param Count: key个数。
        :type Count: int
        :param MaxElementSize: 最大元素长度。
        :type MaxElementSize: int
        """
        self.AveElementSize = None
        self.Length = None
        self.KeyPreIndex = None
        self.ItemCount = None
        self.Count = None
        self.MaxElementSize = None


    def _deserialize(self, params):
        self.AveElementSize = params.get("AveElementSize")
        self.Length = params.get("Length")
        self.KeyPreIndex = params.get("KeyPreIndex")
        self.ItemCount = params.get("ItemCount")
        self.Count = params.get("Count")
        self.MaxElementSize = params.get("MaxElementSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLFilter(AbstractModel):
    """实例SQL限流任务。

    """

    def __init__(self):
        r"""
        :param Id: 任务ID。
        :type Id: int
        :param Status: 任务状态，取值包括RUNNING - 运行中, FINISHED - 已完成, TERMINATED - 已终止。
        :type Status: str
        :param SqlType: SQL类型，取值包括SELECT, UPDATE, DELETE, INSERT, REPLACE。
        :type SqlType: str
        :param OriginKeys: 筛选SQL的关键词，多个关键词用英文逗号拼接。
        :type OriginKeys: str
        :param OriginRule: 筛选SQL的规则。
        :type OriginRule: str
        :param RejectedSqlCount: 已拒绝SQL数目。
        :type RejectedSqlCount: int
        :param CurrentConcurrency: 当前并发数。
        :type CurrentConcurrency: int
        :param MaxConcurrency: 最大并发数。
        :type MaxConcurrency: int
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param CurrentTime: 当前时间。
        :type CurrentTime: str
        :param ExpireTime: 限流过期时间。
        :type ExpireTime: str
        """
        self.Id = None
        self.Status = None
        self.SqlType = None
        self.OriginKeys = None
        self.OriginRule = None
        self.RejectedSqlCount = None
        self.CurrentConcurrency = None
        self.MaxConcurrency = None
        self.CreateTime = None
        self.CurrentTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.SqlType = params.get("SqlType")
        self.OriginKeys = params.get("OriginKeys")
        self.OriginRule = params.get("OriginRule")
        self.RejectedSqlCount = params.get("RejectedSqlCount")
        self.CurrentConcurrency = params.get("CurrentConcurrency")
        self.MaxConcurrency = params.get("MaxConcurrency")
        self.CreateTime = params.get("CreateTime")
        self.CurrentTime = params.get("CurrentTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """SchemaItem数组

    """

    def __init__(self):
        r"""
        :param Schema: 数据库名称
        :type Schema: str
        """
        self.Schema = None


    def _deserialize(self, params):
        self.Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """库空间统计数据。

    """

    def __init__(self):
        r"""
        :param TableSchema: 库名。
        :type TableSchema: str
        :param DataLength: 数据空间（MB）。
        :type DataLength: float
        :param IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param TableRows: 行数。
        :type TableRows: int
        :param PhysicalFileSize: 库中所有表对应的独立物理文件大小加和（MB）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalFileSize: float
        """
        self.TableSchema = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """库空间时序数据

    """

    def __init__(self):
        r"""
        :param TableSchema: 库名
        :type TableSchema: str
        :param SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorMetricSeriesData`
        """
        self.TableSchema = None
        self.SeriesData = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """扣分详情。

    """

    def __init__(self):
        r"""
        :param IssueType: 扣分项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param ScoreLost: 扣分总分。
        :type ScoreLost: int
        :param ScoreLostMax: 扣分总分上限。
        :type ScoreLostMax: int
        :param Items: 扣分项列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ScoreItem
        """
        self.IssueType = None
        self.ScoreLost = None
        self.ScoreLostMax = None
        self.Items = None


    def _deserialize(self, params):
        self.IssueType = params.get("IssueType")
        self.ScoreLost = params.get("ScoreLost")
        self.ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """诊断扣分项。

    """

    def __init__(self):
        r"""
        :param DiagItem: 异常诊断项名称。
        :type DiagItem: str
        :param IssueType: 诊断项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param TopSeverity: 健康等级，取值包括：信息、提示、告警、严重、致命。
        :type TopSeverity: str
        :param Count: 该异常诊断项出现次数。
        :type Count: int
        :param ScoreLost: 扣分分数。
        :type ScoreLost: int
        """
        self.DiagItem = None
        self.IssueType = None
        self.TopSeverity = None
        self.Count = None
        self.ScoreLost = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.IssueType = params.get("IssueType")
        self.TopSeverity = params.get("TopSeverity")
        self.Count = params.get("Count")
        self.ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogExportTaskInfo(AbstractModel):
    """安全审计日志导出任务信息

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param StartTime: 任务开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param Status: 任务状态。
        :type Status: str
        :param Progress: 任务执行进度。
        :type Progress: int
        :param LogStartTime: 导出日志开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogStartTime: str
        :param LogEndTime: 导出日志结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEndTime: str
        :param TotalSize: 日志文件总大小，单位KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        :param DangerLevels: 风险等级列表。0 无风险；1 低风险；2 中风险；3 高风险。
注意：此字段可能返回 null，表示取不到有效值。
        :type DangerLevels: list of int non-negative
        """
        self.AsyncRequestId = None
        self.StartTime = None
        self.EndTime = None
        self.CreateTime = None
        self.Status = None
        self.Progress = None
        self.LogStartTime = None
        self.LogEndTime = None
        self.TotalSize = None
        self.DangerLevels = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.LogStartTime = params.get("LogStartTime")
        self.LogEndTime = params.get("LogEndTime")
        self.TotalSize = params.get("TotalSize")
        self.DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """慢日志来源地址详情。

    """

    def __init__(self):
        r"""
        :param UserHost: 来源地址。
        :type UserHost: str
        :param Ratio: 该来源地址的慢日志数目占总数目的比例，单位%。
        :type Ratio: float
        :param Count: 该来源地址的慢日志数目。
        :type Count: int
        """
        self.UserHost = None
        self.Ratio = None
        self.Count = None


    def _deserialize(self, params):
        self.UserHost = params.get("UserHost")
        self.Ratio = params.get("Ratio")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """慢日志TopSql

    """

    def __init__(self):
        r"""
        :param LockTime: sql总锁等待时间，单位秒
        :type LockTime: float
        :param LockTimeMax: 最大锁等待时间，单位秒
        :type LockTimeMax: float
        :param LockTimeMin: 最小锁等待时间，单位秒
        :type LockTimeMin: float
        :param RowsExamined: 总扫描行数
        :type RowsExamined: int
        :param RowsExaminedMax: 最大扫描行数
        :type RowsExaminedMax: int
        :param RowsExaminedMin: 最小扫描行数
        :type RowsExaminedMin: int
        :param QueryTime: 总耗时，单位秒
        :type QueryTime: float
        :param QueryTimeMax: 最大执行时间，单位秒
        :type QueryTimeMax: float
        :param QueryTimeMin: 最小执行时间，单位秒
        :type QueryTimeMin: float
        :param RowsSent: 总返回行数
        :type RowsSent: int
        :param RowsSentMax: 最大返回行数
        :type RowsSentMax: int
        :param RowsSentMin: 最小返回行数
        :type RowsSentMin: int
        :param ExecTimes: 执行次数
        :type ExecTimes: int
        :param SqlTemplate: sql模板
        :type SqlTemplate: str
        :param SqlText: 带参数SQL（随机）
        :type SqlText: str
        :param Schema: 数据库名
        :type Schema: str
        :param QueryTimeRatio: 总耗时占比，单位%
        :type QueryTimeRatio: float
        :param LockTimeRatio: sql总锁等待时间占比，单位%
        :type LockTimeRatio: float
        :param RowsExaminedRatio: 总扫描行数占比，单位%
        :type RowsExaminedRatio: float
        :param RowsSentRatio: 总返回行数占比，单位%
        :type RowsSentRatio: float
        :param QueryTimeAvg: 平均执行时间，单位秒
        :type QueryTimeAvg: float
        :param RowsSentAvg: 平均返回行数
        :type RowsSentAvg: float
        :param LockTimeAvg: 平均锁等待时间，单位秒
        :type LockTimeAvg: float
        :param RowsExaminedAvg: 平均扫描行数
        :type RowsExaminedAvg: float
        :param Md5: SOL模板的MD5值
        :type Md5: str
        """
        self.LockTime = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.RowsExamined = None
        self.RowsExaminedMax = None
        self.RowsExaminedMin = None
        self.QueryTime = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.RowsSent = None
        self.RowsSentMax = None
        self.RowsSentMin = None
        self.ExecTimes = None
        self.SqlTemplate = None
        self.SqlText = None
        self.Schema = None
        self.QueryTimeRatio = None
        self.LockTimeRatio = None
        self.RowsExaminedRatio = None
        self.RowsSentRatio = None
        self.QueryTimeAvg = None
        self.RowsSentAvg = None
        self.LockTimeAvg = None
        self.RowsExaminedAvg = None
        self.Md5 = None


    def _deserialize(self, params):
        self.LockTime = params.get("LockTime")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsExaminedMax = params.get("RowsExaminedMax")
        self.RowsExaminedMin = params.get("RowsExaminedMin")
        self.QueryTime = params.get("QueryTime")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.RowsSent = params.get("RowsSent")
        self.RowsSentMax = params.get("RowsSentMax")
        self.RowsSentMin = params.get("RowsSentMin")
        self.ExecTimes = params.get("ExecTimes")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.QueryTimeRatio = params.get("QueryTimeRatio")
        self.LockTimeRatio = params.get("LockTimeRatio")
        self.RowsExaminedRatio = params.get("RowsExaminedRatio")
        self.RowsSentRatio = params.get("RowsSentRatio")
        self.QueryTimeAvg = params.get("QueryTimeAvg")
        self.RowsSentAvg = params.get("RowsSentAvg")
        self.LockTimeAvg = params.get("LockTimeAvg")
        self.RowsExaminedAvg = params.get("RowsExaminedAvg")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """表结构。

    """

    def __init__(self):
        r"""
        :param TableSchema: 库名。
        :type TableSchema: str
        :param TableName: 表名。
        :type TableName: str
        :param Engine: 库表的存储引擎。
        :type Engine: str
        :param TableRows: 行数。
        :type TableRows: int
        :param TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        """
        self.TableSchema = None
        self.TableName = None
        self.Engine = None
        self.TableRows = None
        self.TotalLength = None


    def _deserialize(self, params):
        self.TableSchema = params.get("TableSchema")
        self.TableName = params.get("TableName")
        self.Engine = params.get("Engine")
        self.TableRows = params.get("TableRows")
        self.TotalLength = params.get("TotalLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """库表空间统计数据。

    """

    def __init__(self):
        r"""
        :param TableName: 表名。
        :type TableName: str
        :param TableSchema: 库名。
        :type TableSchema: str
        :param Engine: 库表的存储引擎。
        :type Engine: str
        :param DataLength: 数据空间（MB）。
        :type DataLength: float
        :param IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param TableRows: 行数。
        :type TableRows: int
        :param PhysicalFileSize: 表对应的独立物理文件大小（MB）。
        :type PhysicalFileSize: float
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """库表空间时序数据

    """

    def __init__(self):
        r"""
        :param TableName: 表名。
        :type TableName: str
        :param TableSchema: 库名。
        :type TableSchema: str
        :param Engine: 库表的存储引擎。
        :type Engine: str
        :param SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20210527.models.MonitorFloatMetricSeriesData`
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.SeriesData = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorFloatMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """展示 redis kill 会话任务状态。

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: int
        :param InstProxyList: 当前实例所有 proxy 列表。
        :type InstProxyList: list of str
        :param InstProxyCount: 当前实例所有 proxy 数量。
        :type InstProxyCount: int
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param StartTime: 任务启动时间。
        :type StartTime: str
        :param TaskStatus: 任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :type TaskStatus: str
        :param FinishedProxyList: 完成 kill 任务的 proxyId。
        :type FinishedProxyList: list of str
        :param FailedProxyList: kill 任务实行失败的 proxyId。
        :type FailedProxyList: list of str
        :param EndTime: 任务结束时间。
        :type EndTime: str
        :param Progress: 任务执行进度。
        :type Progress: int
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self.AsyncRequestId = None
        self.InstProxyList = None
        self.InstProxyCount = None
        self.CreateTime = None
        self.StartTime = None
        self.TaskStatus = None
        self.FinishedProxyList = None
        self.FailedProxyList = None
        self.EndTime = None
        self.Progress = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.InstProxyList = params.get("InstProxyList")
        self.InstProxyCount = params.get("InstProxyCount")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.TaskStatus = params.get("TaskStatus")
        self.FinishedProxyList = params.get("FinishedProxyList")
        self.FailedProxyList = params.get("FailedProxyList")
        self.EndTime = params.get("EndTime")
        self.Progress = params.get("Progress")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """单位时间间隔内的慢日志统计

    """

    def __init__(self):
        r"""
        :param Count: 总数
        :type Count: int
        :param Timestamp: 统计开始时间
        :type Timestamp: int
        """
        self.Count = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProfile(AbstractModel):
    """用户配置的相关信息，包括邮件配置。

    """

    def __init__(self):
        r"""
        :param ProfileId: 配置的id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileId: str
        :param ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileType: str
        :param ProfileLevel: 配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileLevel: str
        :param ProfileName: 配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileName: str
        :param ProfileInfo: 配置详情。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20210527.models.ProfileInfo`
        """
        self.ProfileId = None
        self.ProfileType = None
        self.ProfileLevel = None
        self.ProfileName = None
        self.ProfileInfo = None


    def _deserialize(self, params):
        self.ProfileId = params.get("ProfileId")
        self.ProfileType = params.get("ProfileType")
        self.ProfileLevel = params.get("ProfileLevel")
        self.ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self.ProfileInfo = ProfileInfo()
            self.ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserAccountRequest(AbstractModel):
    """VerifyUserAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param User: 数据库账号名。
        :type User: str
        :param Password: 数据库账号密码。
        :type Password: str
        :param Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.User = None
        self.Password = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserAccountResponse(AbstractModel):
    """VerifyUserAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionToken: 会话token，有效期为5分钟。
        :type SessionToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionToken = params.get("SessionToken")
        self.RequestId = params.get("RequestId")