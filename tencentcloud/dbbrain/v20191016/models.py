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
        :param _Name: 联系人姓名，大小写字母+数字+下划线，最小 2 位最大 60 位的长度， 不能以"_"开头，且联系人名保持唯一。
        :type Name: str
        :param _ContactInfo: 邮箱地址，大小写字母、数字及下划线组成， 不能以"_"开头。
        :type ContactInfo: str
        :param _Product: 服务产品类型，固定值："mysql"。
        :type Product: str
        """
        self._Name = None
        self._ContactInfo = None
        self._Product = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContactInfo(self):
        return self._ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, ContactInfo):
        self._ContactInfo = ContactInfo

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContactInfo = params.get("ContactInfo")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserContactResponse(AbstractModel):
    """AddUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 添加成功的联系人id。
        :type Id: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ContactItem(AbstractModel):
    """联系人contact描述。

    """

    def __init__(self):
        r"""
        :param _Id: 联系人id。
        :type Id: int
        :param _Name: 联系人姓名。
        :type Name: str
        :param _Mail: 联系人绑定的邮箱。
        :type Mail: str
        """
        self._Id = None
        self._Name = None
        self._Mail = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskRequest(AbstractModel):
    """CreateDBDiagReportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2020-11-08T14:00:00+08:00”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2020-11-09T14:00:00+08:00”。
        :type EndTime: str
        :param _SendMailFlag: 是否发送邮件: 0 - 否，1 - 是。
        :type SendMailFlag: int
        :param _ContactPerson: 接收邮件的联系人ID数组。
        :type ContactPerson: list of int
        :param _ContactGroup: 接收邮件的联系组ID数组。
        :type ContactGroup: list of int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认值为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SendMailFlag = None
        self._ContactPerson = None
        self._ContactGroup = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SendMailFlag(self):
        return self._SendMailFlag

    @SendMailFlag.setter
    def SendMailFlag(self, SendMailFlag):
        self._SendMailFlag = SendMailFlag

    @property
    def ContactPerson(self):
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SendMailFlag = params.get("SendMailFlag")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportTaskResponse(AbstractModel):
    """CreateDBDiagReportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBDiagReportUrlRequest(AbstractModel):
    """CreateDBDiagReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _AsyncRequestId: 健康报告相应的任务ID，可通过DescribeDBDiagReportTasks查询。
        :type AsyncRequestId: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBDiagReportUrlResponse(AbstractModel):
    """CreateDBDiagReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportUrl: 健康报告浏览地址。
        :type ReportUrl: str
        :param _ExpireTime: 健康报告浏览地址到期时间戳（秒）。
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportUrl = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportUrl = params.get("ReportUrl")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateMailProfileRequest(AbstractModel):
    """CreateMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        :param _ProfileLevel: 配置级别，支持值包括："User" - 用户级别，"Instance" - 实例级别，其中数据库巡检邮件配置为用户级别，定期生成邮件配置为实例级别。
        :type ProfileLevel: str
        :param _ProfileName: 配置名称，需要保持唯一性，数据库巡检邮件配置名称自拟；定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param _ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :type Product: str
        :param _BindInstanceIds: 配置绑定的实例ID，当配置级别为"Instance"时需要传入且只能为一个实例；当配置级别为“User”时，此参数不填。
        :type BindInstanceIds: list of str
        """
        self._ProfileInfo = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileType = None
        self._Product = None
        self._BindInstanceIds = None

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileLevel(self):
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def BindInstanceIds(self):
        return self._BindInstanceIds

    @BindInstanceIds.setter
    def BindInstanceIds(self, BindInstanceIds):
        self._BindInstanceIds = BindInstanceIds


    def _deserialize(self, params):
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._BindInstanceIds = params.get("BindInstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMailProfileResponse(AbstractModel):
    """CreateMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSchedulerMailProfileRequest(AbstractModel):
    """CreateSchedulerMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WeekConfiguration: 取值范围1-7，分别代表周一至周日。
        :type WeekConfiguration: list of int
        :param _ProfileInfo: 邮件配置内容。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        :param _ProfileName: 配置名称，需要保持唯一性，定期生成邮件配置命名格式："scheduler_" + {instanceId}，如"schduler_cdb-test"。
        :type ProfileName: str
        :param _BindInstanceId: 配置订阅的实例ID。
        :type BindInstanceId: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._WeekConfiguration = None
        self._ProfileInfo = None
        self._ProfileName = None
        self._BindInstanceId = None
        self._Product = None

    @property
    def WeekConfiguration(self):
        return self._WeekConfiguration

    @WeekConfiguration.setter
    def WeekConfiguration(self, WeekConfiguration):
        self._WeekConfiguration = WeekConfiguration

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def BindInstanceId(self):
        return self._BindInstanceId

    @BindInstanceId.setter
    def BindInstanceId(self, BindInstanceId):
        self._BindInstanceId = BindInstanceId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._WeekConfiguration = params.get("WeekConfiguration")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        self._ProfileName = params.get("ProfileName")
        self._BindInstanceId = params.get("BindInstanceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulerMailProfileResponse(AbstractModel):
    """CreateSchedulerMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSecurityAuditLogExportTaskRequest(AbstractModel):
    """CreateSecurityAuditLogExportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _StartTime: 导出日志开始时间，例如2020-12-28 00:00:00。
        :type StartTime: str
        :param _EndTime: 导出日志结束时间，例如2020-12-28 01:00:00。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param _DangerLevels: 日志风险等级列表，支持值包括：0 无风险；1 低风险；2 中风险；3 高风险。
        :type DangerLevels: list of int
        """
        self._SecAuditGroupId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None
        self._DangerLevels = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def DangerLevels(self):
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityAuditLogExportTaskResponse(AbstractModel):
    """CreateSecurityAuditLogExportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 日志导出任务Id。
        :type AsyncRequestId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class DeleteSecurityAuditLogExportTasksRequest(AbstractModel):
    """DeleteSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _AsyncRequestIds: 日志导出任务Id列表，接口会忽略不存在或已删除的任务Id。
        :type AsyncRequestIds: list of int non-negative
        :param _Product: 服务产品类型，支持值： "mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestIds = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityAuditLogExportTasksResponse(AbstractModel):
    """DeleteSecurityAuditLogExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAllUserContactRequest(AbstractModel):
    """DescribeAllUserContact请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param _Names: 联系人名数组，支持模糊搜索。
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserContactResponse(AbstractModel):
    """DescribeAllUserContact返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 联系人的总数量。
        :type TotalCount: int
        :param _Contacts: 联系人的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Contacts: list of ContactItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Contacts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Contacts(self):
        return self._Contacts

    @Contacts.setter
    def Contacts(self, Contacts):
        self._Contacts = Contacts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Contacts") is not None:
            self._Contacts = []
            for item in params.get("Contacts"):
                obj = ContactItem()
                obj._deserialize(item)
                self._Contacts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllUserGroupRequest(AbstractModel):
    """DescribeAllUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 服务产品类型，固定值：mysql。
        :type Product: str
        :param _Names: 联系组名称数组，支持模糊搜索。
        :type Names: list of str
        """
        self._Product = None
        self._Names = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllUserGroupResponse(AbstractModel):
    """DescribeAllUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 组总数。
        :type TotalCount: int
        :param _Groups: 组信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GroupItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupItem()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _EventId: 事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。
        :type EventId: int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._EventId = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EventId = params.get("EventId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiagItem: 诊断项。
        :type DiagItem: str
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _EventId: 事件 ID 。
        :type EventId: int
        :param _Explanation: 事件详情。
        :type Explanation: str
        :param _Outline: 概要。
        :type Outline: str
        :param _Problem: 诊断出的问题。
        :type Problem: str
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Suggestions: 建议。
        :type Suggestions: str
        :param _Metric: 保留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiagItem = None
        self._DiagType = None
        self._EventId = None
        self._Explanation = None
        self._Outline = None
        self._Problem = None
        self._Severity = None
        self._StartTime = None
        self._Suggestions = None
        self._Metric = None
        self._EndTime = None
        self._RequestId = None

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Explanation(self):
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Problem(self):
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Suggestions(self):
        return self._Suggestions

    @Suggestions.setter
    def Suggestions(self, Suggestions):
        self._Suggestions = Suggestions

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._DiagType = params.get("DiagType")
        self._EventId = params.get("EventId")
        self._Explanation = params.get("Explanation")
        self._Outline = params.get("Outline")
        self._Problem = params.get("Problem")
        self._Severity = params.get("Severity")
        self._StartTime = params.get("StartTime")
        self._Suggestions = params.get("Suggestions")
        self._Metric = params.get("Metric")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 事件描述。
        :type Events: list of DiagHistoryEventItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBDiagReportTasksRequest(AbstractModel):
    """DescribeDBDiagReportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 第一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param _EndTime: 最后一个任务的开始时间，用于范围查询，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param _InstanceIds: 实例ID数组，用于筛选指定实例的任务列表。
        :type InstanceIds: list of str
        :param _Sources: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :type Sources: list of str
        :param _HealthLevels: 报告的健康等级，支持的取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK" - 危险；"HIGH_RISK" - 高危。
        :type HealthLevels: str
        :param _TaskStatuses: 任务的状态，支持的取值包括："created" - 新建；"chosen" - 待执行； "running" - 执行中；"failed" - 失败；"finished" - 已完成。
        :type TaskStatuses: str
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 返回数量，默认20。
        :type Limit: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._Sources = None
        self._HealthLevels = None
        self._TaskStatuses = None
        self._Offset = None
        self._Limit = None
        self._Product = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Sources(self):
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def HealthLevels(self):
        return self._HealthLevels

    @HealthLevels.setter
    def HealthLevels(self, HealthLevels):
        self._HealthLevels = HealthLevels

    @property
    def TaskStatuses(self):
        return self._TaskStatuses

    @TaskStatuses.setter
    def TaskStatuses(self, TaskStatuses):
        self._TaskStatuses = TaskStatuses

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._Sources = params.get("Sources")
        self._HealthLevels = params.get("HealthLevels")
        self._TaskStatuses = params.get("TaskStatuses")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBDiagReportTasksResponse(AbstractModel):
    """DescribeDBDiagReportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数目。
        :type TotalCount: int
        :param _Tasks: 任务列表。
        :type Tasks: list of HealthReportTask
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = HealthReportTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _RangeDays: 时间段天数，截止日期为当日，默认为7天。
        :type RangeDays: int
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._RangeDays = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RangeDays(self):
        return self._RangeDays

    @RangeDays.setter
    def RangeDays(self, RangeDays):
        self._RangeDays = RangeDays

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RangeDays = params.get("RangeDays")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Growth: 磁盘增长量(MB)。
        :type Growth: int
        :param _Remain: 磁盘剩余(MB)。
        :type Remain: int
        :param _Total: 磁盘总量(MB)。
        :type Total: int
        :param _AvailableDays: 预计可用天数。
        :type AvailableDays: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Growth = None
        self._Remain = None
        self._Total = None
        self._AvailableDays = None
        self._RequestId = None

    @property
    def Growth(self):
        return self._Growth

    @Growth.setter
    def Growth(self, Growth):
        self._Growth = Growth

    @property
    def Remain(self):
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AvailableDays(self):
        return self._AvailableDays

    @AvailableDays.setter
    def AvailableDays(self, AvailableDays):
        self._AvailableDays = AvailableDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Growth = params.get("Growth")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._AvailableDays = params.get("AvailableDays")
        self._RequestId = params.get("RequestId")


class DescribeDiagDBInstancesRequest(AbstractModel):
    """DescribeDiagDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsSupported: 是否是DBbrain支持的实例，固定传 true。
        :type IsSupported: bool
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param _Offset: 分页参数，偏移量。
        :type Offset: int
        :param _Limit: 分页参数，分页值。
        :type Limit: int
        :param _InstanceNames: 根据实例名称条件查询。
        :type InstanceNames: list of str
        :param _InstanceIds: 根据实例ID条件查询。
        :type InstanceIds: list of str
        :param _Regions: 根据地域条件查询。
        :type Regions: list of str
        """
        self._IsSupported = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._InstanceNames = None
        self._InstanceIds = None
        self._Regions = None

    @property
    def IsSupported(self):
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._IsSupported = params.get("IsSupported")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceIds = params.get("InstanceIds")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagDBInstancesResponse(AbstractModel):
    """DescribeDiagDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _DbScanStatus: 全实例巡检状态：0：开启全实例巡检；1：未开启全实例巡检。
        :type DbScanStatus: int
        :param _Items: 实例相关信息。
        :type Items: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DbScanStatus = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DbScanStatus(self):
        return self._DbScanStatus

    @DbScanStatus.setter
    def DbScanStatus(self, DbScanStatus):
        self._DbScanStatus = DbScanStatus

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._DbScanStatus = params.get("DbScanStatus")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHealthScoreRequest(AbstractModel):
    """DescribeHealthScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要获取健康得分的实例ID。
        :type InstanceId: str
        :param _Time: 获取健康得分的时间。
        :type Time: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Time = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Time = params.get("Time")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthScoreResponse(AbstractModel):
    """DescribeHealthScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 健康得分以及异常扣分项。
        :type Data: :class:`tencentcloud.dbbrain.v20191016.models.HealthScoreInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = HealthScoreInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMailProfileRequest(AbstractModel):
    """DescribeMailProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileType: 配置类型，支持值包括："dbScan_mail_configuration" - 数据库巡检邮件配置，"scheduler_mail_configuration" - 定期生成邮件配置。
        :type ProfileType: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 分页单位，最大支持50。
        :type Limit: int
        :param _ProfileName: 根据邮件配置名称查询，定期发送的邮件配置名称遵循："scheduler_"+{instanceId}的规则。
        :type ProfileName: str
        """
        self._ProfileType = None
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._ProfileName = None

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName


    def _deserialize(self, params):
        self._ProfileType = params.get("ProfileType")
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProfileName = params.get("ProfileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMailProfileResponse(AbstractModel):
    """DescribeMailProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProfileList: 邮件配置详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileList: list of UserProfile
        :param _TotalCount: 邮件模版总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProfileList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProfileList(self):
        return self._ProfileList

    @ProfileList.setter
    def ProfileList(self, ProfileList):
        self._ProfileList = ProfileList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProfileList") is not None:
            self._ProfileList = []
            for item in params.get("ProfileList"):
                obj = UserProfile()
                obj._deserialize(item)
                self._ProfileList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogDownloadUrlsRequest(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        """
        self._SecAuditGroupId = None
        self._AsyncRequestId = None
        self._Product = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogDownloadUrlsResponse(AbstractModel):
    """DescribeSecurityAuditLogDownloadUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 导出结果的COS链接列表。当结果集很大时，可能会切分为多个url下载。
        :type Urls: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Urls = None
        self._RequestId = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._RequestId = params.get("RequestId")


class DescribeSecurityAuditLogExportTasksRequest(AbstractModel):
    """DescribeSecurityAuditLogExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecAuditGroupId: 安全审计组Id。
        :type SecAuditGroupId: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL。
        :type Product: str
        :param _AsyncRequestIds: 日志导出任务Id列表。
        :type AsyncRequestIds: list of int non-negative
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 返回数量，默认20。
        :type Limit: int
        """
        self._SecAuditGroupId = None
        self._Product = None
        self._AsyncRequestIds = None
        self._Offset = None
        self._Limit = None

    @property
    def SecAuditGroupId(self):
        return self._SecAuditGroupId

    @SecAuditGroupId.setter
    def SecAuditGroupId(self, SecAuditGroupId):
        self._SecAuditGroupId = SecAuditGroupId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SecAuditGroupId = params.get("SecAuditGroupId")
        self._Product = params.get("Product")
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAuditLogExportTasksResponse(AbstractModel):
    """DescribeSecurityAuditLogExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 安全审计日志导出任务列表。
        :type Tasks: list of SecLogExportTaskInfo
        :param _TotalCount: 安全审计日志导出任务总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = SecLogExportTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 结束时间，如“2019-09-10 12:13:14”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 柱间单位时间间隔，单位为秒。
        :type Period: int
        :param _TimeSeries: 单位时间间隔内慢日志数量统计。
        :type TimeSeries: list of TimeSlice
        :param _SeriesData: 单位时间间隔内的实例 cpu 利用率监控数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Period = None
        self._TimeSeries = None
        self._SeriesData = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimeSeries(self):
        return self._TimeSeries

    @TimeSeries.setter
    def TimeSeries(self, TimeSeries):
        self._TimeSeries = TimeSeries

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self._TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self._TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        self._RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param _EndTime: 截止时间，如“2019-09-10 12:13:14”，截止时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param _SortBy: 排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键。
        :type SortBy: str
        :param _OrderBy: 排序方式，支持ASC（升序）以及DESC（降序）。
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _SchemaList: 数据库名称数组。
        :type SchemaList: list of SchemaItem
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SortBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._SchemaList = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SchemaList(self):
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _Rows: 慢日志 top sql 列表
        :type Rows: list of SlowLogTopSqlItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogUserHostStatsRequest(AbstractModel):
    """DescribeSlowLogUserHostStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _StartTime: 查询范围的开始时间，时间格式如：2019-09-10 12:13:14。
        :type StartTime: str
        :param _EndTime: 查询范围的结束时间，时间格式如：2019-09-10 12:13:14。
        :type EndTime: str
        :param _Product: 服务产品类型，支持值："mysql" - 云数据库 MySQL；"cynosdb" - 云数据库 TDSQL-C for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogUserHostStatsResponse(AbstractModel):
    """DescribeSlowLogUserHostStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 来源地址数目。
        :type TotalCount: int
        :param _Items: 各来源地址的慢日志占比详情列表。
        :type Items: list of SlowLogHost
        :param _UserNameItems: 各来源用户名的慢日志占比详情列表。
        :type UserNameItems: list of SlowLogUser
        :param _UserTotalCount: 来源用户数目。
        :type UserTotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._UserNameItems = None
        self._UserTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def UserNameItems(self):
        return self._UserNameItems

    @UserNameItems.setter
    def UserNameItems(self, UserNameItems):
        self._UserNameItems = UserNameItems

    @property
    def UserTotalCount(self):
        return self._UserTotalCount

    @UserTotalCount.setter
    def UserTotalCount(self, UserTotalCount):
        self._UserTotalCount = UserTotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogHost()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("UserNameItems") is not None:
            self._UserNameItems = []
            for item in params.get("UserNameItems"):
                obj = SlowLogUser()
                obj._deserialize(item)
                self._UserNameItems.append(obj)
        self._UserTotalCount = params.get("UserTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemaTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param _EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemaTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceSchemaTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemaTimeSeries: 返回的Top库空间统计信息的时序数据列表。
        :type TopSpaceSchemaTimeSeries: list of SchemaSpaceTimeSeries
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceSchemaTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceSchemaTimeSeries(self):
        return self._TopSpaceSchemaTimeSeries

    @TopSpaceSchemaTimeSeries.setter
    def TopSpaceSchemaTimeSeries(self, TopSpaceSchemaTimeSeries):
        self._TopSpaceSchemaTimeSeries = TopSpaceSchemaTimeSeries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemaTimeSeries") is not None:
            self._TopSpaceSchemaTimeSeries = []
            for item in params.get("TopSpaceSchemaTimeSeries"):
                obj = SchemaSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceSchemaTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceSchemasRequest(AbstractModel):
    """DescribeTopSpaceSchemas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top库数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top库所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceSchemasResponse(AbstractModel):
    """DescribeTopSpaceSchemas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceSchemas: 返回的Top库空间统计信息列表。
        :type TopSpaceSchemas: list of SchemaSpaceData
        :param _Timestamp: 采集库空间数据的时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceSchemas = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceSchemas(self):
        return self._TopSpaceSchemas

    @TopSpaceSchemas.setter
    def TopSpaceSchemas(self, TopSpaceSchemas):
        self._TopSpaceSchemas = TopSpaceSchemas

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceSchemas") is not None:
            self._TopSpaceSchemas = []
            for item in params.get("TopSpaceSchemas"):
                obj = SchemaSpaceData()
                obj._deserialize(item)
                self._TopSpaceSchemas.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :type SortBy: str
        :param _StartDate: 开始日期，如“2021-01-01”，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param _EndDate: 截止日期，如“2021-01-01”，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._StartDate = None
        self._EndDate = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceTableTimeSeries: 返回的Top表空间统计信息的时序数据列表。
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceTableTimeSeries = None
        self._RequestId = None

    @property
    def TopSpaceTableTimeSeries(self):
        return self._TopSpaceTableTimeSeries

    @TopSpaceTableTimeSeries.setter
    def TopSpaceTableTimeSeries(self, TopSpaceTableTimeSeries):
        self._TopSpaceTableTimeSeries = TopSpaceTableTimeSeries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self._TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self._TopSpaceTableTimeSeries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID 。
        :type InstanceId: str
        :param _Limit: 返回的Top表数量，最大值为100，默认为20。
        :type Limit: int
        :param _SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize（仅云数据库 MySQL实例支持），云数据库 MySQL实例默认为 PhysicalFileSize，其他产品实例默认为TotalLength。
        :type SortBy: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self._InstanceId = None
        self._Limit = None
        self._SortBy = None
        self._Product = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopSpaceTables: 返回的Top表空间统计信息列表。
        :type TopSpaceTables: list of TableSpaceData
        :param _Timestamp: 采集表空间数据的时间戳（秒）。
        :type Timestamp: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopSpaceTables = None
        self._Timestamp = None
        self._RequestId = None

    @property
    def TopSpaceTables(self):
        return self._TopSpaceTables

    @TopSpaceTables.setter
    def TopSpaceTables(self, TopSpaceTables):
        self._TopSpaceTables = TopSpaceTables

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self._TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self._TopSpaceTables.append(obj)
        self._Timestamp = params.get("Timestamp")
        self._RequestId = params.get("RequestId")


class DescribeUserSqlAdviceRequest(AbstractModel):
    """DescribeUserSqlAdvice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _Schema: 库名。
        :type Schema: str
        """
        self._InstanceId = None
        self._SqlText = None
        self._Schema = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSqlAdviceResponse(AbstractModel):
    """DescribeUserSqlAdvice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Advices: SQL优化建议，可解析为JSON数组。
        :type Advices: str
        :param _Comments: SQL优化建议备注，可解析为String数组。
        :type Comments: str
        :param _SqlText: SQL语句。
        :type SqlText: str
        :param _Schema: 库名。
        :type Schema: str
        :param _Tables: 相关表的DDL信息，可解析为JSON数组。
        :type Tables: str
        :param _SqlPlan: SQL执行计划，可解析为JSON。
        :type SqlPlan: str
        :param _Cost: SQL优化后的成本节约详情，可解析为JSON。
        :type Cost: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Advices = None
        self._Comments = None
        self._SqlText = None
        self._Schema = None
        self._Tables = None
        self._SqlPlan = None
        self._Cost = None
        self._RequestId = None

    @property
    def Advices(self):
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices

    @property
    def Comments(self):
        return self._Comments

    @Comments.setter
    def Comments(self, Comments):
        self._Comments = Comments

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def SqlPlan(self):
        return self._SqlPlan

    @SqlPlan.setter
    def SqlPlan(self, SqlPlan):
        self._SqlPlan = SqlPlan

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Advices = params.get("Advices")
        self._Comments = params.get("Comments")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._Tables = params.get("Tables")
        self._SqlPlan = params.get("SqlPlan")
        self._Cost = params.get("Cost")
        self._RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """实例诊断历史事件

    """

    def __init__(self):
        r"""
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EventId: 事件 ID 。
        :type EventId: int
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _Outline: 概要。
        :type Outline: str
        :param _DiagItem: 诊断项。
        :type DiagItem: str
        :param _InstanceId: 实例 ID 。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Metric: 保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._DiagType = None
        self._EndTime = None
        self._StartTime = None
        self._EventId = None
        self._Severity = None
        self._Outline = None
        self._DiagItem = None
        self._InstanceId = None
        self._Metric = None
        self._Region = None

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DiagType = params.get("DiagType")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._EventId = params.get("EventId")
        self._Severity = params.get("Severity")
        self._Outline = params.get("Outline")
        self._DiagItem = params.get("DiagItem")
        self._InstanceId = params.get("InstanceId")
        self._Metric = params.get("Metric")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    """异常事件信息。

    """

    def __init__(self):
        r"""
        :param _EventId: 事件 ID 。
        :type EventId: int
        :param _DiagType: 诊断类型。
        :type DiagType: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Outline: 概要。
        :type Outline: str
        :param _Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param _ScoreLost: 扣分。
        :type ScoreLost: int
        :param _Metric: 保留字段。
        :type Metric: str
        :param _Count: 告警数目。
        :type Count: int
        """
        self._EventId = None
        self._DiagType = None
        self._StartTime = None
        self._EndTime = None
        self._Outline = None
        self._Severity = None
        self._ScoreLost = None
        self._Metric = None
        self._Count = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def DiagType(self):
        return self._DiagType

    @DiagType.setter
    def DiagType(self, DiagType):
        self._DiagType = DiagType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._DiagType = params.get("DiagType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Outline = params.get("Outline")
        self._Severity = params.get("Severity")
        self._ScoreLost = params.get("ScoreLost")
        self._Metric = params.get("Metric")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """描述组信息。

    """

    def __init__(self):
        r"""
        :param _Id: 组id。
        :type Id: int
        :param _Name: 组名称。
        :type Name: str
        :param _MemberCount: 组成员数量。
        :type MemberCount: int
        """
        self._Id = None
        self._Name = None
        self._MemberCount = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthReportTask(AbstractModel):
    """健康报告任务详情。

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务请求 ID。
        :type AsyncRequestId: int
        :param _Source: 任务的触发来源，支持的取值包括："DAILY_INSPECTION" - 实例巡检；"SCHEDULED" - 定时生成；"MANUAL" - 手动触发。
        :type Source: str
        :param _Progress: 任务完成进度，单位%。
        :type Progress: int
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _StartTime: 任务开始执行时间。
        :type StartTime: str
        :param _EndTime: 任务完成执行时间。
        :type EndTime: str
        :param _InstanceInfo: 任务所属实例的基础信息。
        :type InstanceInfo: :class:`tencentcloud.dbbrain.v20191016.models.InstanceBasicInfo`
        :param _HealthStatus: 健康报告中的健康信息。
        :type HealthStatus: :class:`tencentcloud.dbbrain.v20191016.models.HealthStatus`
        """
        self._AsyncRequestId = None
        self._Source = None
        self._Progress = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceInfo = None
        self._HealthStatus = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceInfo(self):
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Source = params.get("Source")
        self._Progress = params.get("Progress")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceBasicInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        if params.get("HealthStatus") is not None:
            self._HealthStatus = HealthStatus()
            self._HealthStatus._deserialize(params.get("HealthStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthScoreInfo(AbstractModel):
    """获取健康得分返回的详情。

    """

    def __init__(self):
        r"""
        :param _IssueTypes: 异常详情。
        :type IssueTypes: list of IssueTypeInfo
        :param _EventsTotalCount: 异常事件总数。
        :type EventsTotalCount: int
        :param _HealthScore: 健康得分。
        :type HealthScore: int
        :param _HealthLevel: 健康等级, 如："HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"。
        :type HealthLevel: str
        """
        self._IssueTypes = None
        self._EventsTotalCount = None
        self._HealthScore = None
        self._HealthLevel = None

    @property
    def IssueTypes(self):
        return self._IssueTypes

    @IssueTypes.setter
    def IssueTypes(self, IssueTypes):
        self._IssueTypes = IssueTypes

    @property
    def EventsTotalCount(self):
        return self._EventsTotalCount

    @EventsTotalCount.setter
    def EventsTotalCount(self, EventsTotalCount):
        self._EventsTotalCount = EventsTotalCount

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel


    def _deserialize(self, params):
        if params.get("IssueTypes") is not None:
            self._IssueTypes = []
            for item in params.get("IssueTypes"):
                obj = IssueTypeInfo()
                obj._deserialize(item)
                self._IssueTypes.append(obj)
        self._EventsTotalCount = params.get("EventsTotalCount")
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthStatus(AbstractModel):
    """实例健康详情。

    """

    def __init__(self):
        r"""
        :param _HealthScore: 健康分数，满分100。
        :type HealthScore: int
        :param _HealthLevel: 健康等级，取值包括："HEALTH" - 健康；"SUB_HEALTH" - 亚健康；"RISK"- 危险；"HIGH_RISK" - 高危。
        :type HealthLevel: str
        :param _ScoreLost: 总扣分分数。
        :type ScoreLost: int
        :param _ScoreDetails: 扣分详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScoreDetails: list of ScoreDetail
        """
        self._HealthScore = None
        self._HealthLevel = None
        self._ScoreLost = None
        self._ScoreDetails = None

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def HealthLevel(self):
        return self._HealthLevel

    @HealthLevel.setter
    def HealthLevel(self, HealthLevel):
        self._HealthLevel = HealthLevel

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreDetails(self):
        return self._ScoreDetails

    @ScoreDetails.setter
    def ScoreDetails(self, ScoreDetails):
        self._ScoreDetails = ScoreDetails


    def _deserialize(self, params):
        self._HealthScore = params.get("HealthScore")
        self._HealthLevel = params.get("HealthLevel")
        self._ScoreLost = params.get("ScoreLost")
        if params.get("ScoreDetails") is not None:
            self._ScoreDetails = []
            for item in params.get("ScoreDetails"):
                obj = ScoreDetail()
                obj._deserialize(item)
                self._ScoreDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceBasicInfo(AbstractModel):
    """实例基础信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Vip: 实例内网IP。
        :type Vip: str
        :param _Vport: 实例内网Port。
        :type Vport: int
        :param _Product: 实例产品。
        :type Product: str
        :param _EngineVersion: 实例引擎版本。
        :type EngineVersion: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Product = None
        self._EngineVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Product = params.get("Product")
        self._EngineVersion = params.get("EngineVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfs(AbstractModel):
    """实例配置。

    """

    def __init__(self):
        r"""
        :param _DailyInspection: 数据库巡检开关, Yes/No。
        :type DailyInspection: str
        :param _OverviewDisplay: 实例概览开关，Yes/No。
        :type OverviewDisplay: str
        :param _KeyDelimiters: redis大key分析的自定义分割符，仅redis使用
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyDelimiters: list of str
        """
        self._DailyInspection = None
        self._OverviewDisplay = None
        self._KeyDelimiters = None

    @property
    def DailyInspection(self):
        return self._DailyInspection

    @DailyInspection.setter
    def DailyInspection(self, DailyInspection):
        self._DailyInspection = DailyInspection

    @property
    def OverviewDisplay(self):
        return self._OverviewDisplay

    @OverviewDisplay.setter
    def OverviewDisplay(self, OverviewDisplay):
        self._OverviewDisplay = OverviewDisplay

    @property
    def KeyDelimiters(self):
        return self._KeyDelimiters

    @KeyDelimiters.setter
    def KeyDelimiters(self, KeyDelimiters):
        self._KeyDelimiters = KeyDelimiters


    def _deserialize(self, params):
        self._DailyInspection = params.get("DailyInspection")
        self._OverviewDisplay = params.get("OverviewDisplay")
        self._KeyDelimiters = params.get("KeyDelimiters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """查询实例列表，返回实例的相关信息的对象。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Region: 实例所属地域。
        :type Region: str
        :param _HealthScore: 健康得分。
        :type HealthScore: int
        :param _Product: 所属产品。
        :type Product: str
        :param _EventCount: 异常事件数量。
        :type EventCount: int
        :param _InstanceType: 实例类型：1:MASTER；2:DR，3：RO，4:SDR。
        :type InstanceType: int
        :param _Cpu: 核心数。
        :type Cpu: int
        :param _Memory: 内存，单位MB。
        :type Memory: int
        :param _Volume: 硬盘存储，单位GB。
        :type Volume: int
        :param _EngineVersion: 数据库版本。
        :type EngineVersion: str
        :param _Vip: 内网地址。
        :type Vip: str
        :param _Vport: 内网端口。
        :type Vport: int
        :param _Source: 接入来源。
        :type Source: str
        :param _GroupId: 分组ID。
        :type GroupId: str
        :param _GroupName: 分组组名。
        :type GroupName: str
        :param _Status: 实例状态：0：发货中；1：运行正常；4：销毁中；5：隔离中。
        :type Status: int
        :param _UniqSubnetId: 子网统一ID。
        :type UniqSubnetId: str
        :param _DeployMode: cdb类型。
        :type DeployMode: str
        :param _InitFlag: cdb实例初始化标志：0：未初始化；1：已初始化。
        :type InitFlag: int
        :param _TaskStatus: 任务状态。
        :type TaskStatus: int
        :param _UniqVpcId: 私有网络统一ID。
        :type UniqVpcId: str
        :param _InstanceConf: 实例巡检/概览的状态。
        :type InstanceConf: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        :param _DeadlineTime: 资源到期时间。
        :type DeadlineTime: str
        :param _IsSupported: 是否是DBbrain支持的实例。
        :type IsSupported: bool
        :param _SecAuditStatus: 实例安全审计日志开启状态：ON： 安全审计开启；OFF： 未开启安全审计。
        :type SecAuditStatus: str
        :param _AuditPolicyStatus: 实例审计日志开启状态，ALL_AUDIT： 开启全审计；RULE_AUDIT： 开启规则审计；UNBOUND： 未开启审计。
        :type AuditPolicyStatus: str
        :param _AuditRunningStatus: 实例审计日志运行状态：normal： 运行中； paused： 欠费暂停。
        :type AuditRunningStatus: str
        :param _InternalVip: 内网vip。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalVip: str
        :param _InternalVport: 内网port。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalVport: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ClusterId: 所属集群ID（仅对集群数据库产品该字段非空，如TDSQL-C）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 所属集群名称（仅对集群数据库产品该字段非空，如TDSQL-C）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._HealthScore = None
        self._Product = None
        self._EventCount = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._Vip = None
        self._Vport = None
        self._Source = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._UniqSubnetId = None
        self._DeployMode = None
        self._InitFlag = None
        self._TaskStatus = None
        self._UniqVpcId = None
        self._InstanceConf = None
        self._DeadlineTime = None
        self._IsSupported = None
        self._SecAuditStatus = None
        self._AuditPolicyStatus = None
        self._AuditRunningStatus = None
        self._InternalVip = None
        self._InternalVport = None
        self._CreateTime = None
        self._ClusterId = None
        self._ClusterName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def EventCount(self):
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def InstanceConf(self):
        return self._InstanceConf

    @InstanceConf.setter
    def InstanceConf(self, InstanceConf):
        self._InstanceConf = InstanceConf

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def IsSupported(self):
        return self._IsSupported

    @IsSupported.setter
    def IsSupported(self, IsSupported):
        self._IsSupported = IsSupported

    @property
    def SecAuditStatus(self):
        return self._SecAuditStatus

    @SecAuditStatus.setter
    def SecAuditStatus(self, SecAuditStatus):
        self._SecAuditStatus = SecAuditStatus

    @property
    def AuditPolicyStatus(self):
        return self._AuditPolicyStatus

    @AuditPolicyStatus.setter
    def AuditPolicyStatus(self, AuditPolicyStatus):
        self._AuditPolicyStatus = AuditPolicyStatus

    @property
    def AuditRunningStatus(self):
        return self._AuditRunningStatus

    @AuditRunningStatus.setter
    def AuditRunningStatus(self, AuditRunningStatus):
        self._AuditRunningStatus = AuditRunningStatus

    @property
    def InternalVip(self):
        return self._InternalVip

    @InternalVip.setter
    def InternalVip(self, InternalVip):
        self._InternalVip = InternalVip

    @property
    def InternalVport(self):
        return self._InternalVport

    @InternalVport.setter
    def InternalVport(self, InternalVport):
        self._InternalVport = InternalVport

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._HealthScore = params.get("HealthScore")
        self._Product = params.get("Product")
        self._EventCount = params.get("EventCount")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Source = params.get("Source")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._DeployMode = params.get("DeployMode")
        self._InitFlag = params.get("InitFlag")
        self._TaskStatus = params.get("TaskStatus")
        self._UniqVpcId = params.get("UniqVpcId")
        if params.get("InstanceConf") is not None:
            self._InstanceConf = InstanceConfs()
            self._InstanceConf._deserialize(params.get("InstanceConf"))
        self._DeadlineTime = params.get("DeadlineTime")
        self._IsSupported = params.get("IsSupported")
        self._SecAuditStatus = params.get("SecAuditStatus")
        self._AuditPolicyStatus = params.get("AuditPolicyStatus")
        self._AuditRunningStatus = params.get("AuditRunningStatus")
        self._InternalVip = params.get("InternalVip")
        self._InternalVport = params.get("InternalVport")
        self._CreateTime = params.get("CreateTime")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueTypeInfo(AbstractModel):
    """指标信息。

    """

    def __init__(self):
        r"""
        :param _IssueType: 指标分类：AVAILABILITY：可用性，MAINTAINABILITY：可维护性，PERFORMANCE，性能，RELIABILITY可靠性。
        :type IssueType: str
        :param _Events: 异常事件。
        :type Events: list of EventInfo
        :param _TotalCount: 异常事件总数。
        :type TotalCount: int
        """
        self._IssueType = None
        self._Events = None
        self._TotalCount = None

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MailConfiguration(AbstractModel):
    """邮件发送配置

    """

    def __init__(self):
        r"""
        :param _SendMail: 是否开启邮件发送: 0, 否; 1, 是。
        :type SendMail: int
        :param _Region: 地域配置, 如["ap-guangzhou", "ap-shanghai"]。巡检的邮件发送模版，配置需要发送巡检邮件的地域；订阅的邮件发送模版，配置当前订阅实例的所属地域。
        :type Region: list of str
        :param _HealthStatus: 发送指定的健康等级的报告, 如["HEALTH", "SUB_HEALTH", "RISK", "HIGH_RISK"]。
        :type HealthStatus: list of str
        :param _ContactPerson: 联系人id, 联系人/联系组不能都为空。
        :type ContactPerson: list of int
        :param _ContactGroup: 联系组id, 联系人/联系组不能都为空。
        :type ContactGroup: list of int
        """
        self._SendMail = None
        self._Region = None
        self._HealthStatus = None
        self._ContactPerson = None
        self._ContactGroup = None

    @property
    def SendMail(self):
        return self._SendMail

    @SendMail.setter
    def SendMail(self, SendMail):
        self._SendMail = SendMail

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ContactPerson(self):
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactGroup(self):
        return self._ContactGroup

    @ContactGroup.setter
    def ContactGroup(self, ContactGroup):
        self._ContactGroup = ContactGroup


    def _deserialize(self, params):
        self._SendMail = params.get("SendMail")
        self._Region = params.get("Region")
        self._HealthStatus = params.get("HealthStatus")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactGroup = params.get("ContactGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfRequest(AbstractModel):
    """ModifyDiagDBInstanceConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceConfs: 巡检开关。
        :type InstanceConfs: :class:`tencentcloud.dbbrain.v20191016.models.InstanceConfs`
        :param _Regions: 生效实例地域，取值为"All"，代表全地域。
        :type Regions: str
        :param _Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL。
        :type Product: str
        :param _InstanceIds: 指定更改巡检状态的实例ID。
        :type InstanceIds: list of str
        """
        self._InstanceConfs = None
        self._Regions = None
        self._Product = None
        self._InstanceIds = None

    @property
    def InstanceConfs(self):
        return self._InstanceConfs

    @InstanceConfs.setter
    def InstanceConfs(self, InstanceConfs):
        self._InstanceConfs = InstanceConfs

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        if params.get("InstanceConfs") is not None:
            self._InstanceConfs = InstanceConfs()
            self._InstanceConfs._deserialize(params.get("InstanceConfs"))
        self._Regions = params.get("Regions")
        self._Product = params.get("Product")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDiagDBInstanceConfResponse(AbstractModel):
    """ModifyDiagDBInstanceConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorFloatMetric(AbstractModel):
    """监控数据（浮点型）

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称。
        :type Metric: str
        :param _Unit: 指标单位。
        :type Unit: str
        :param _Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorFloatMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据（浮点型）

    """

    def __init__(self):
        r"""
        :param _Series: 监控指标。
        :type Series: list of MonitorFloatMetric
        :param _Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetric(AbstractModel):
    """监控数据

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称。
        :type Metric: str
        :param _Unit: 指标单位。
        :type Unit: str
        :param _Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of int
        """
        self._Metric = None
        self._Unit = None
        self._Values = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Unit = params.get("Unit")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据

    """

    def __init__(self):
        r"""
        :param _Series: 监控指标。
        :type Series: list of MonitorMetric
        :param _Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self._Series = None
        self._Timestamp = None

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProfileInfo(AbstractModel):
    """用户配置的信息

    """

    def __init__(self):
        r"""
        :param _Language: 语言, 如"zh"。
        :type Language: str
        :param _MailConfiguration: 邮件模板的内容。
        :type MailConfiguration: :class:`tencentcloud.dbbrain.v20191016.models.MailConfiguration`
        """
        self._Language = None
        self._MailConfiguration = None

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def MailConfiguration(self):
        return self._MailConfiguration

    @MailConfiguration.setter
    def MailConfiguration(self, MailConfiguration):
        self._MailConfiguration = MailConfiguration


    def _deserialize(self, params):
        self._Language = params.get("Language")
        if params.get("MailConfiguration") is not None:
            self._MailConfiguration = MailConfiguration()
            self._MailConfiguration._deserialize(params.get("MailConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaItem(AbstractModel):
    """SchemaItem数组

    """

    def __init__(self):
        r"""
        :param _Schema: 数据库名称
        :type Schema: str
        """
        self._Schema = None

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceData(AbstractModel):
    """库空间统计数据。

    """

    def __init__(self):
        r"""
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _DataLength: 数据空间（MB）。
        :type DataLength: float
        :param _IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param _DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param _TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param _FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param _TableRows: 行数。
        :type TableRows: int
        :param _PhysicalFileSize: 库中所有表对应的独立物理文件大小加和（MB）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalFileSize: float
        """
        self._TableSchema = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def DataLength(self):
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaSpaceTimeSeries(AbstractModel):
    """库空间时序数据

    """

    def __init__(self):
        r"""
        :param _TableSchema: 库名
        :type TableSchema: str
        :param _SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        """
        self._TableSchema = None
        self._SeriesData = None

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableSchema = params.get("TableSchema")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreDetail(AbstractModel):
    """扣分详情。

    """

    def __init__(self):
        r"""
        :param _IssueType: 扣分项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param _ScoreLost: 扣分总分。
        :type ScoreLost: int
        :param _ScoreLostMax: 扣分总分上限。
        :type ScoreLostMax: int
        :param _Items: 扣分项列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ScoreItem
        """
        self._IssueType = None
        self._ScoreLost = None
        self._ScoreLostMax = None
        self._Items = None

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost

    @property
    def ScoreLostMax(self):
        return self._ScoreLostMax

    @ScoreLostMax.setter
    def ScoreLostMax(self, ScoreLostMax):
        self._ScoreLostMax = ScoreLostMax

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._IssueType = params.get("IssueType")
        self._ScoreLost = params.get("ScoreLost")
        self._ScoreLostMax = params.get("ScoreLostMax")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ScoreItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreItem(AbstractModel):
    """诊断扣分项。

    """

    def __init__(self):
        r"""
        :param _DiagItem: 异常诊断项名称。
        :type DiagItem: str
        :param _IssueType: 诊断项分类，取值包括：可用性、可维护性、性能及可靠性。
        :type IssueType: str
        :param _TopSeverity: 健康等级，取值包括：信息、提示、告警、严重、致命。
        :type TopSeverity: str
        :param _Count: 该异常诊断项出现次数。
        :type Count: int
        :param _ScoreLost: 扣分分数。
        :type ScoreLost: int
        """
        self._DiagItem = None
        self._IssueType = None
        self._TopSeverity = None
        self._Count = None
        self._ScoreLost = None

    @property
    def DiagItem(self):
        return self._DiagItem

    @DiagItem.setter
    def DiagItem(self, DiagItem):
        self._DiagItem = DiagItem

    @property
    def IssueType(self):
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def TopSeverity(self):
        return self._TopSeverity

    @TopSeverity.setter
    def TopSeverity(self, TopSeverity):
        self._TopSeverity = TopSeverity

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ScoreLost(self):
        return self._ScoreLost

    @ScoreLost.setter
    def ScoreLost(self, ScoreLost):
        self._ScoreLost = ScoreLost


    def _deserialize(self, params):
        self._DiagItem = params.get("DiagItem")
        self._IssueType = params.get("IssueType")
        self._TopSeverity = params.get("TopSeverity")
        self._Count = params.get("Count")
        self._ScoreLost = params.get("ScoreLost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecLogExportTaskInfo(AbstractModel):
    """安全审计日志导出任务信息

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 异步任务Id。
        :type AsyncRequestId: int
        :param _StartTime: 任务开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _Status: 任务状态。
        :type Status: str
        :param _Progress: 任务执行进度。
        :type Progress: int
        :param _LogStartTime: 导出日志开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogStartTime: str
        :param _LogEndTime: 导出日志结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEndTime: str
        :param _TotalSize: 日志文件总大小，单位KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        :param _DangerLevels: 风险等级列表。0 无风险；1 低风险；2 中风险；3 高风险。
注意：此字段可能返回 null，表示取不到有效值。
        :type DangerLevels: list of int non-negative
        """
        self._AsyncRequestId = None
        self._StartTime = None
        self._EndTime = None
        self._CreateTime = None
        self._Status = None
        self._Progress = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._TotalSize = None
        self._DangerLevels = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def DangerLevels(self):
        return self._DangerLevels

    @DangerLevels.setter
    def DangerLevels(self, DangerLevels):
        self._DangerLevels = DangerLevels


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._TotalSize = params.get("TotalSize")
        self._DangerLevels = params.get("DangerLevels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogHost(AbstractModel):
    """慢日志来源地址详情。

    """

    def __init__(self):
        r"""
        :param _UserHost: 来源地址。
        :type UserHost: str
        :param _Ratio: 该来源地址的慢日志数目占总数目的比例，单位%。
        :type Ratio: float
        :param _Count: 该来源地址的慢日志数目。
        :type Count: int
        """
        self._UserHost = None
        self._Ratio = None
        self._Count = None

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserHost = params.get("UserHost")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogTopSqlItem(AbstractModel):
    """慢日志TopSql

    """

    def __init__(self):
        r"""
        :param _LockTime: sql总锁等待时间
        :type LockTime: float
        :param _LockTimeMax: 最大锁等待时间
        :type LockTimeMax: float
        :param _LockTimeMin: 最小锁等待时间
        :type LockTimeMin: float
        :param _RowsExamined: 总扫描行数
        :type RowsExamined: int
        :param _RowsExaminedMax: 最大扫描行数
        :type RowsExaminedMax: int
        :param _RowsExaminedMin: 最小扫描行数
        :type RowsExaminedMin: int
        :param _QueryTime: 总耗时
        :type QueryTime: float
        :param _QueryTimeMax: 最大执行时间
        :type QueryTimeMax: float
        :param _QueryTimeMin: 最小执行时间
        :type QueryTimeMin: float
        :param _RowsSent: 总返回行数
        :type RowsSent: int
        :param _RowsSentMax: 最大返回行数
        :type RowsSentMax: int
        :param _RowsSentMin: 最小返回行数
        :type RowsSentMin: int
        :param _ExecTimes: 执行次数
        :type ExecTimes: int
        :param _SqlTemplate: sql模板
        :type SqlTemplate: str
        :param _SqlText: 带参数SQL（随机）
        :type SqlText: str
        :param _Schema: 数据库名
        :type Schema: str
        :param _QueryTimeRatio: 总耗时占比
        :type QueryTimeRatio: float
        :param _LockTimeRatio: sql总锁等待时间占比
        :type LockTimeRatio: float
        :param _RowsExaminedRatio: 总扫描行数占比
        :type RowsExaminedRatio: float
        :param _RowsSentRatio: 总返回行数占比
        :type RowsSentRatio: float
        :param _QueryTimeAvg: 平均执行时间
        :type QueryTimeAvg: float
        :param _RowsSentAvg: 平均返回行数
        :type RowsSentAvg: float
        :param _LockTimeAvg: 平均锁等待时间
        :type LockTimeAvg: float
        :param _RowsExaminedAvg: 平均扫描行数
        :type RowsExaminedAvg: float
        :param _Md5: SOL模板的MD5值
        :type Md5: str
        """
        self._LockTime = None
        self._LockTimeMax = None
        self._LockTimeMin = None
        self._RowsExamined = None
        self._RowsExaminedMax = None
        self._RowsExaminedMin = None
        self._QueryTime = None
        self._QueryTimeMax = None
        self._QueryTimeMin = None
        self._RowsSent = None
        self._RowsSentMax = None
        self._RowsSentMin = None
        self._ExecTimes = None
        self._SqlTemplate = None
        self._SqlText = None
        self._Schema = None
        self._QueryTimeRatio = None
        self._LockTimeRatio = None
        self._RowsExaminedRatio = None
        self._RowsSentRatio = None
        self._QueryTimeAvg = None
        self._RowsSentAvg = None
        self._LockTimeAvg = None
        self._RowsExaminedAvg = None
        self._Md5 = None

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def LockTimeMax(self):
        return self._LockTimeMax

    @LockTimeMax.setter
    def LockTimeMax(self, LockTimeMax):
        self._LockTimeMax = LockTimeMax

    @property
    def LockTimeMin(self):
        return self._LockTimeMin

    @LockTimeMin.setter
    def LockTimeMin(self, LockTimeMin):
        self._LockTimeMin = LockTimeMin

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsExaminedMax(self):
        return self._RowsExaminedMax

    @RowsExaminedMax.setter
    def RowsExaminedMax(self, RowsExaminedMax):
        self._RowsExaminedMax = RowsExaminedMax

    @property
    def RowsExaminedMin(self):
        return self._RowsExaminedMin

    @RowsExaminedMin.setter
    def RowsExaminedMin(self, RowsExaminedMin):
        self._RowsExaminedMin = RowsExaminedMin

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def QueryTimeMax(self):
        return self._QueryTimeMax

    @QueryTimeMax.setter
    def QueryTimeMax(self, QueryTimeMax):
        self._QueryTimeMax = QueryTimeMax

    @property
    def QueryTimeMin(self):
        return self._QueryTimeMin

    @QueryTimeMin.setter
    def QueryTimeMin(self, QueryTimeMin):
        self._QueryTimeMin = QueryTimeMin

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def RowsSentMax(self):
        return self._RowsSentMax

    @RowsSentMax.setter
    def RowsSentMax(self, RowsSentMax):
        self._RowsSentMax = RowsSentMax

    @property
    def RowsSentMin(self):
        return self._RowsSentMin

    @RowsSentMin.setter
    def RowsSentMin(self, RowsSentMin):
        self._RowsSentMin = RowsSentMin

    @property
    def ExecTimes(self):
        return self._ExecTimes

    @ExecTimes.setter
    def ExecTimes(self, ExecTimes):
        self._ExecTimes = ExecTimes

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def QueryTimeRatio(self):
        return self._QueryTimeRatio

    @QueryTimeRatio.setter
    def QueryTimeRatio(self, QueryTimeRatio):
        self._QueryTimeRatio = QueryTimeRatio

    @property
    def LockTimeRatio(self):
        return self._LockTimeRatio

    @LockTimeRatio.setter
    def LockTimeRatio(self, LockTimeRatio):
        self._LockTimeRatio = LockTimeRatio

    @property
    def RowsExaminedRatio(self):
        return self._RowsExaminedRatio

    @RowsExaminedRatio.setter
    def RowsExaminedRatio(self, RowsExaminedRatio):
        self._RowsExaminedRatio = RowsExaminedRatio

    @property
    def RowsSentRatio(self):
        return self._RowsSentRatio

    @RowsSentRatio.setter
    def RowsSentRatio(self, RowsSentRatio):
        self._RowsSentRatio = RowsSentRatio

    @property
    def QueryTimeAvg(self):
        return self._QueryTimeAvg

    @QueryTimeAvg.setter
    def QueryTimeAvg(self, QueryTimeAvg):
        self._QueryTimeAvg = QueryTimeAvg

    @property
    def RowsSentAvg(self):
        return self._RowsSentAvg

    @RowsSentAvg.setter
    def RowsSentAvg(self, RowsSentAvg):
        self._RowsSentAvg = RowsSentAvg

    @property
    def LockTimeAvg(self):
        return self._LockTimeAvg

    @LockTimeAvg.setter
    def LockTimeAvg(self, LockTimeAvg):
        self._LockTimeAvg = LockTimeAvg

    @property
    def RowsExaminedAvg(self):
        return self._RowsExaminedAvg

    @RowsExaminedAvg.setter
    def RowsExaminedAvg(self, RowsExaminedAvg):
        self._RowsExaminedAvg = RowsExaminedAvg

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._LockTime = params.get("LockTime")
        self._LockTimeMax = params.get("LockTimeMax")
        self._LockTimeMin = params.get("LockTimeMin")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsExaminedMax = params.get("RowsExaminedMax")
        self._RowsExaminedMin = params.get("RowsExaminedMin")
        self._QueryTime = params.get("QueryTime")
        self._QueryTimeMax = params.get("QueryTimeMax")
        self._QueryTimeMin = params.get("QueryTimeMin")
        self._RowsSent = params.get("RowsSent")
        self._RowsSentMax = params.get("RowsSentMax")
        self._RowsSentMin = params.get("RowsSentMin")
        self._ExecTimes = params.get("ExecTimes")
        self._SqlTemplate = params.get("SqlTemplate")
        self._SqlText = params.get("SqlText")
        self._Schema = params.get("Schema")
        self._QueryTimeRatio = params.get("QueryTimeRatio")
        self._LockTimeRatio = params.get("LockTimeRatio")
        self._RowsExaminedRatio = params.get("RowsExaminedRatio")
        self._RowsSentRatio = params.get("RowsSentRatio")
        self._QueryTimeAvg = params.get("QueryTimeAvg")
        self._RowsSentAvg = params.get("RowsSentAvg")
        self._LockTimeAvg = params.get("LockTimeAvg")
        self._RowsExaminedAvg = params.get("RowsExaminedAvg")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogUser(AbstractModel):
    """慢日志来源用户详情。

    """

    def __init__(self):
        r"""
        :param _UserName: 来源用户名。
        :type UserName: str
        :param _Ratio: 该来源用户名的慢日志数目占总数目的比例，单位%。
        :type Ratio: float
        :param _Count: 该来源用户名的慢日志数目。
        :type Count: int
        """
        self._UserName = None
        self._Ratio = None
        self._Count = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Ratio = params.get("Ratio")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceData(AbstractModel):
    """库表空间统计数据。

    """

    def __init__(self):
        r"""
        :param _TableName: 表名。
        :type TableName: str
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _Engine: 库表的存储引擎。
        :type Engine: str
        :param _DataLength: 数据空间（MB）。
        :type DataLength: float
        :param _IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param _DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param _TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param _FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param _TableRows: 行数。
        :type TableRows: int
        :param _PhysicalFileSize: 表对应的独立物理文件大小（MB）。
        :type PhysicalFileSize: float
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._DataLength = None
        self._IndexLength = None
        self._DataFree = None
        self._TotalLength = None
        self._FragRatio = None
        self._TableRows = None
        self._PhysicalFileSize = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def DataLength(self):
        return self._DataLength

    @DataLength.setter
    def DataLength(self, DataLength):
        self._DataLength = DataLength

    @property
    def IndexLength(self):
        return self._IndexLength

    @IndexLength.setter
    def IndexLength(self, IndexLength):
        self._IndexLength = IndexLength

    @property
    def DataFree(self):
        return self._DataFree

    @DataFree.setter
    def DataFree(self, DataFree):
        self._DataFree = DataFree

    @property
    def TotalLength(self):
        return self._TotalLength

    @TotalLength.setter
    def TotalLength(self, TotalLength):
        self._TotalLength = TotalLength

    @property
    def FragRatio(self):
        return self._FragRatio

    @FragRatio.setter
    def FragRatio(self, FragRatio):
        self._FragRatio = FragRatio

    @property
    def TableRows(self):
        return self._TableRows

    @TableRows.setter
    def TableRows(self, TableRows):
        self._TableRows = TableRows

    @property
    def PhysicalFileSize(self):
        return self._PhysicalFileSize

    @PhysicalFileSize.setter
    def PhysicalFileSize(self, PhysicalFileSize):
        self._PhysicalFileSize = PhysicalFileSize


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        self._DataLength = params.get("DataLength")
        self._IndexLength = params.get("IndexLength")
        self._DataFree = params.get("DataFree")
        self._TotalLength = params.get("TotalLength")
        self._FragRatio = params.get("FragRatio")
        self._TableRows = params.get("TableRows")
        self._PhysicalFileSize = params.get("PhysicalFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableSpaceTimeSeries(AbstractModel):
    """库表空间时序数据

    """

    def __init__(self):
        r"""
        :param _TableName: 表名。
        :type TableName: str
        :param _TableSchema: 库名。
        :type TableSchema: str
        :param _Engine: 库表的存储引擎。
        :type Engine: str
        :param _SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorFloatMetricSeriesData`
        """
        self._TableName = None
        self._TableSchema = None
        self._Engine = None
        self._SeriesData = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def TableSchema(self):
        return self._TableSchema

    @TableSchema.setter
    def TableSchema(self, TableSchema):
        self._TableSchema = TableSchema

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def SeriesData(self):
        return self._SeriesData

    @SeriesData.setter
    def SeriesData(self, SeriesData):
        self._SeriesData = SeriesData


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._TableSchema = params.get("TableSchema")
        self._Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self._SeriesData = MonitorFloatMetricSeriesData()
            self._SeriesData._deserialize(params.get("SeriesData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSlice(AbstractModel):
    """单位时间间隔内的慢日志统计

    """

    def __init__(self):
        r"""
        :param _Count: 总数
        :type Count: int
        :param _Timestamp: 统计开始时间
        :type Timestamp: int
        """
        self._Count = None
        self._Timestamp = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProfile(AbstractModel):
    """用户配置的相关信息，包括邮件配置。

    """

    def __init__(self):
        r"""
        :param _ProfileId: 配置的id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileId: str
        :param _ProfileType: 配置类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileType: str
        :param _ProfileLevel: 配置级别，"User"或"Instance"。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileLevel: str
        :param _ProfileName: 配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfileName: str
        :param _ProfileInfo: 配置详情。
        :type ProfileInfo: :class:`tencentcloud.dbbrain.v20191016.models.ProfileInfo`
        """
        self._ProfileId = None
        self._ProfileType = None
        self._ProfileLevel = None
        self._ProfileName = None
        self._ProfileInfo = None

    @property
    def ProfileId(self):
        return self._ProfileId

    @ProfileId.setter
    def ProfileId(self, ProfileId):
        self._ProfileId = ProfileId

    @property
    def ProfileType(self):
        return self._ProfileType

    @ProfileType.setter
    def ProfileType(self, ProfileType):
        self._ProfileType = ProfileType

    @property
    def ProfileLevel(self):
        return self._ProfileLevel

    @ProfileLevel.setter
    def ProfileLevel(self, ProfileLevel):
        self._ProfileLevel = ProfileLevel

    @property
    def ProfileName(self):
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, ProfileName):
        self._ProfileName = ProfileName

    @property
    def ProfileInfo(self):
        return self._ProfileInfo

    @ProfileInfo.setter
    def ProfileInfo(self, ProfileInfo):
        self._ProfileInfo = ProfileInfo


    def _deserialize(self, params):
        self._ProfileId = params.get("ProfileId")
        self._ProfileType = params.get("ProfileType")
        self._ProfileLevel = params.get("ProfileLevel")
        self._ProfileName = params.get("ProfileName")
        if params.get("ProfileInfo") is not None:
            self._ProfileInfo = ProfileInfo()
            self._ProfileInfo._deserialize(params.get("ProfileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        