# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class CreateCustomerRequest(AbstractModel):
    """CreateCustomer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 企业名称
        :type Name: str
        :param _ScanType: 资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :type ScanType: str
        :param _Percent: 百分比取值范围为30-100
        :type Percent: int
        :param _ScanCron: 周期测绘时间
        :type ScanCron: str
        :param _IsScanNow: 是否立即启动
        :type IsScanNow: bool
        :param _EnableCron: 是否启用周期测绘
        :type EnableCron: bool
        :param _EnableScanSubEnterprise: 是否扫描子公司
        :type EnableScanSubEnterprise: bool
        :param _EnableAuth: 是否授权
        :type EnableAuth: bool
        :param _AuthStartAt: 授权开始时间
        :type AuthStartAt: str
        :param _AuthEndAt: 授权结束时间
        :type AuthEndAt: str
        :param _AuthFile: 授权文件id
        :type AuthFile: str
        :param _ScanTime: 测绘时间配置项，采用json字符串格式
        :type ScanTime: str
        :param _Keywords: 企业相关的关键字
        :type Keywords: str
        :param _Icon: 图标
        :type Icon: str
        :param _Qps: 并发设置
        :type Qps: int
        :param _SubCompanyLevel: 限制子公司层级，-1表示不限制
        :type SubCompanyLevel: int
        :param _IsIncludeFullScan: 是否以企业名称为起点做完整扫描(包含手动上传),如只想扫描特定的某几个域名，则传false。
        :type IsIncludeFullScan: bool
        """
        self._Name = None
        self._ScanType = None
        self._Percent = None
        self._ScanCron = None
        self._IsScanNow = None
        self._EnableCron = None
        self._EnableScanSubEnterprise = None
        self._EnableAuth = None
        self._AuthStartAt = None
        self._AuthEndAt = None
        self._AuthFile = None
        self._ScanTime = None
        self._Keywords = None
        self._Icon = None
        self._Qps = None
        self._SubCompanyLevel = None
        self._IsIncludeFullScan = None

    @property
    def Name(self):
        """企业名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScanType(self):
        """资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :rtype: str
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType

    @property
    def Percent(self):
        """百分比取值范围为30-100
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanCron(self):
        """周期测绘时间
        :rtype: str
        """
        return self._ScanCron

    @ScanCron.setter
    def ScanCron(self, ScanCron):
        self._ScanCron = ScanCron

    @property
    def IsScanNow(self):
        """是否立即启动
        :rtype: bool
        """
        return self._IsScanNow

    @IsScanNow.setter
    def IsScanNow(self, IsScanNow):
        self._IsScanNow = IsScanNow

    @property
    def EnableCron(self):
        """是否启用周期测绘
        :rtype: bool
        """
        return self._EnableCron

    @EnableCron.setter
    def EnableCron(self, EnableCron):
        self._EnableCron = EnableCron

    @property
    def EnableScanSubEnterprise(self):
        """是否扫描子公司
        :rtype: bool
        """
        return self._EnableScanSubEnterprise

    @EnableScanSubEnterprise.setter
    def EnableScanSubEnterprise(self, EnableScanSubEnterprise):
        self._EnableScanSubEnterprise = EnableScanSubEnterprise

    @property
    def EnableAuth(self):
        """是否授权
        :rtype: bool
        """
        return self._EnableAuth

    @EnableAuth.setter
    def EnableAuth(self, EnableAuth):
        self._EnableAuth = EnableAuth

    @property
    def AuthStartAt(self):
        """授权开始时间
        :rtype: str
        """
        return self._AuthStartAt

    @AuthStartAt.setter
    def AuthStartAt(self, AuthStartAt):
        self._AuthStartAt = AuthStartAt

    @property
    def AuthEndAt(self):
        """授权结束时间
        :rtype: str
        """
        return self._AuthEndAt

    @AuthEndAt.setter
    def AuthEndAt(self, AuthEndAt):
        self._AuthEndAt = AuthEndAt

    @property
    def AuthFile(self):
        """授权文件id
        :rtype: str
        """
        return self._AuthFile

    @AuthFile.setter
    def AuthFile(self, AuthFile):
        self._AuthFile = AuthFile

    @property
    def ScanTime(self):
        """测绘时间配置项，采用json字符串格式
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def Keywords(self):
        """企业相关的关键字
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Icon(self):
        """图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Qps(self):
        """并发设置
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def SubCompanyLevel(self):
        """限制子公司层级，-1表示不限制
        :rtype: int
        """
        return self._SubCompanyLevel

    @SubCompanyLevel.setter
    def SubCompanyLevel(self, SubCompanyLevel):
        self._SubCompanyLevel = SubCompanyLevel

    @property
    def IsIncludeFullScan(self):
        """是否以企业名称为起点做完整扫描(包含手动上传),如只想扫描特定的某几个域名，则传false。
        :rtype: bool
        """
        return self._IsIncludeFullScan

    @IsIncludeFullScan.setter
    def IsIncludeFullScan(self, IsIncludeFullScan):
        self._IsIncludeFullScan = IsIncludeFullScan


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ScanType = params.get("ScanType")
        self._Percent = params.get("Percent")
        self._ScanCron = params.get("ScanCron")
        self._IsScanNow = params.get("IsScanNow")
        self._EnableCron = params.get("EnableCron")
        self._EnableScanSubEnterprise = params.get("EnableScanSubEnterprise")
        self._EnableAuth = params.get("EnableAuth")
        self._AuthStartAt = params.get("AuthStartAt")
        self._AuthEndAt = params.get("AuthEndAt")
        self._AuthFile = params.get("AuthFile")
        self._ScanTime = params.get("ScanTime")
        self._Keywords = params.get("Keywords")
        self._Icon = params.get("Icon")
        self._Qps = params.get("Qps")
        self._SubCompanyLevel = params.get("SubCompanyLevel")
        self._IsIncludeFullScan = params.get("IsIncludeFullScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomerResponse(AbstractModel):
    """CreateCustomer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateJobRecordRequest(AbstractModel):
    """CreateJobRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _TaskType: 任务类型：即时任务
        :type TaskType: str
        :param _ScanType: 资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :type ScanType: str
        :param _Qps: qps设置
        :type Qps: int
        :param _IsIncludeFullScan: 是否包含完整扫描
        :type IsIncludeFullScan: bool
        """
        self._CustomerId = None
        self._TaskType = None
        self._ScanType = None
        self._Qps = None
        self._IsIncludeFullScan = None

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def TaskType(self):
        """任务类型：即时任务
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ScanType(self):
        """资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :rtype: str
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType

    @property
    def Qps(self):
        """qps设置
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def IsIncludeFullScan(self):
        """是否包含完整扫描
        :rtype: bool
        """
        return self._IsIncludeFullScan

    @IsIncludeFullScan.setter
    def IsIncludeFullScan(self, IsIncludeFullScan):
        self._IsIncludeFullScan = IsIncludeFullScan


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._TaskType = params.get("TaskType")
        self._ScanType = params.get("ScanType")
        self._Qps = params.get("Qps")
        self._IsIncludeFullScan = params.get("IsIncludeFullScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobRecordResponse(AbstractModel):
    """CreateJobRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务Id
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """任务Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class Customer(AbstractModel):
    """企业详情

    """

    def __init__(self):
        r"""
        :param _Id: 企业ID
        :type Id: int
        :param _Name: 企业名称
        :type Name: str
        :param _Percent: 股权占比
        :type Percent: int
        :param _ScanType: 资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :type ScanType: str
        :param _Creator: 创建账号
        :type Creator: str
        :param _AppId: 腾讯云客户AppId
        :type AppId: int
        :param _Uin: 腾讯云客户Uin
        :type Uin: str
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 更新时间
        :type UpdateAt: str
        :param _ScanCron: 周期测绘时间
        :type ScanCron: str
        :param _EnableCron: 是否启用周期测绘
        :type EnableCron: bool
        :param _EnableScanSubEnterprise: 是否扫描子公司
        :type EnableScanSubEnterprise: bool
        :param _EnableAuth: 是否授权
        :type EnableAuth: bool
        :param _AuthStartAt: 授权开始时间
        :type AuthStartAt: str
        :param _AuthEndAt: 授权结束时间
        :type AuthEndAt: str
        :param _AuthFile: 授权文件id
        :type AuthFile: str
        :param _ScanTime: 测绘时间配置项
        :type ScanTime: str
        :param _Icon: 图标
        :type Icon: str
        :param _Keywords: 关键字
        :type Keywords: str
        :param _Qps: Qps设置，10-500，默认100
        :type Qps: int
        :param _SubCompanyLevel: 子公司拓展层次
        :type SubCompanyLevel: int
        :param _IsIncludeFullScan: 是否包含完整扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIncludeFullScan: bool
        :param _EnableGroupMemberDiscovered: 是否识别集团成员
        :type EnableGroupMemberDiscovered: bool
        """
        self._Id = None
        self._Name = None
        self._Percent = None
        self._ScanType = None
        self._Creator = None
        self._AppId = None
        self._Uin = None
        self._CreateAt = None
        self._UpdateAt = None
        self._ScanCron = None
        self._EnableCron = None
        self._EnableScanSubEnterprise = None
        self._EnableAuth = None
        self._AuthStartAt = None
        self._AuthEndAt = None
        self._AuthFile = None
        self._ScanTime = None
        self._Icon = None
        self._Keywords = None
        self._Qps = None
        self._SubCompanyLevel = None
        self._IsIncludeFullScan = None
        self._EnableGroupMemberDiscovered = None

    @property
    def Id(self):
        """企业ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """企业名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Percent(self):
        """股权占比
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanType(self):
        """资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :rtype: str
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType

    @property
    def Creator(self):
        """创建账号
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def AppId(self):
        """腾讯云客户AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """腾讯云客户Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateAt(self):
        """创建时间
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def ScanCron(self):
        """周期测绘时间
        :rtype: str
        """
        return self._ScanCron

    @ScanCron.setter
    def ScanCron(self, ScanCron):
        self._ScanCron = ScanCron

    @property
    def EnableCron(self):
        """是否启用周期测绘
        :rtype: bool
        """
        return self._EnableCron

    @EnableCron.setter
    def EnableCron(self, EnableCron):
        self._EnableCron = EnableCron

    @property
    def EnableScanSubEnterprise(self):
        """是否扫描子公司
        :rtype: bool
        """
        return self._EnableScanSubEnterprise

    @EnableScanSubEnterprise.setter
    def EnableScanSubEnterprise(self, EnableScanSubEnterprise):
        self._EnableScanSubEnterprise = EnableScanSubEnterprise

    @property
    def EnableAuth(self):
        """是否授权
        :rtype: bool
        """
        return self._EnableAuth

    @EnableAuth.setter
    def EnableAuth(self, EnableAuth):
        self._EnableAuth = EnableAuth

    @property
    def AuthStartAt(self):
        """授权开始时间
        :rtype: str
        """
        return self._AuthStartAt

    @AuthStartAt.setter
    def AuthStartAt(self, AuthStartAt):
        self._AuthStartAt = AuthStartAt

    @property
    def AuthEndAt(self):
        """授权结束时间
        :rtype: str
        """
        return self._AuthEndAt

    @AuthEndAt.setter
    def AuthEndAt(self, AuthEndAt):
        self._AuthEndAt = AuthEndAt

    @property
    def AuthFile(self):
        """授权文件id
        :rtype: str
        """
        return self._AuthFile

    @AuthFile.setter
    def AuthFile(self, AuthFile):
        self._AuthFile = AuthFile

    @property
    def ScanTime(self):
        """测绘时间配置项
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def Icon(self):
        """图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Keywords(self):
        """关键字
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Qps(self):
        """Qps设置，10-500，默认100
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def SubCompanyLevel(self):
        """子公司拓展层次
        :rtype: int
        """
        return self._SubCompanyLevel

    @SubCompanyLevel.setter
    def SubCompanyLevel(self, SubCompanyLevel):
        self._SubCompanyLevel = SubCompanyLevel

    @property
    def IsIncludeFullScan(self):
        """是否包含完整扫描
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsIncludeFullScan

    @IsIncludeFullScan.setter
    def IsIncludeFullScan(self, IsIncludeFullScan):
        self._IsIncludeFullScan = IsIncludeFullScan

    @property
    def EnableGroupMemberDiscovered(self):
        """是否识别集团成员
        :rtype: bool
        """
        return self._EnableGroupMemberDiscovered

    @EnableGroupMemberDiscovered.setter
    def EnableGroupMemberDiscovered(self, EnableGroupMemberDiscovered):
        self._EnableGroupMemberDiscovered = EnableGroupMemberDiscovered


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Percent = params.get("Percent")
        self._ScanType = params.get("ScanType")
        self._Creator = params.get("Creator")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._ScanCron = params.get("ScanCron")
        self._EnableCron = params.get("EnableCron")
        self._EnableScanSubEnterprise = params.get("EnableScanSubEnterprise")
        self._EnableAuth = params.get("EnableAuth")
        self._AuthStartAt = params.get("AuthStartAt")
        self._AuthEndAt = params.get("AuthEndAt")
        self._AuthFile = params.get("AuthFile")
        self._ScanTime = params.get("ScanTime")
        self._Icon = params.get("Icon")
        self._Keywords = params.get("Keywords")
        self._Qps = params.get("Qps")
        self._SubCompanyLevel = params.get("SubCompanyLevel")
        self._IsIncludeFullScan = params.get("IsIncludeFullScan")
        self._EnableGroupMemberDiscovered = params.get("EnableGroupMemberDiscovered")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppsRequest(AbstractModel):
    """DescribeApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._EnterpriseUidList = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppsResponse(AbstractModel):
    """DescribeApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 移动资产数组
        :type List: list of DisplayApp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """移动资产数组
        :rtype: list of DisplayApp
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayApp()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetsRequest(AbstractModel):
    """DescribeAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetsResponse(AbstractModel):
    """DescribeAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 主机资产数组
        :type List: list of DisplayAsset
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """主机资产数组
        :rtype: list of DisplayAsset
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayAsset()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayConfig
        :param _AllConfigNum: 全部路径数量
        :type AllConfigNum: int
        :param _HighRiskConfigNum: 高风险路径数量
        :type HighRiskConfigNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._AllConfigNum = None
        self._HighRiskConfigNum = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayConfig
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def AllConfigNum(self):
        """全部路径数量
        :rtype: int
        """
        return self._AllConfigNum

    @AllConfigNum.setter
    def AllConfigNum(self, AllConfigNum):
        self._AllConfigNum = AllConfigNum

    @property
    def HighRiskConfigNum(self):
        """高风险路径数量
        :rtype: int
        """
        return self._HighRiskConfigNum

    @HighRiskConfigNum.setter
    def HighRiskConfigNum(self, HighRiskConfigNum):
        self._HighRiskConfigNum = HighRiskConfigNum

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayConfig()
                obj._deserialize(item)
                self._List.append(obj)
        self._AllConfigNum = params.get("AllConfigNum")
        self._HighRiskConfigNum = params.get("HighRiskConfigNum")
        self._RequestId = params.get("RequestId")


class DescribeCustomersRequest(AbstractModel):
    """DescribeCustomers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Keyword: 企业名称模糊搜索
        :type Keyword: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Keyword = None

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Keyword(self):
        """企业名称模糊搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomersResponse(AbstractModel):
    """DescribeCustomers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 企业列表
        :type List: list of Customer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """企业列表
        :rtype: list of Customer
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Customer()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDarkWebsRequest(AbstractModel):
    """DescribeDarkWebs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDarkWebsResponse(AbstractModel):
    """DescribeDarkWebs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayDarkWeb
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayDarkWeb
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayDarkWeb()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayDomain
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayDomain
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayDomain()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnterprisesRequest(AbstractModel):
    """DescribeEnterprises请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        :param _IsShowStatistics: 是否展示统计数据
        :type IsShowStatistics: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None
        self._IsShowStatistics = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored

    @property
    def IsShowStatistics(self):
        """是否展示统计数据
        :rtype: bool
        """
        return self._IsShowStatistics

    @IsShowStatistics.setter
    def IsShowStatistics(self, IsShowStatistics):
        self._IsShowStatistics = IsShowStatistics


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        self._IsShowStatistics = params.get("IsShowStatistics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnterprisesResponse(AbstractModel):
    """DescribeEnterprises返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayEnterprise
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayEnterprise
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayEnterprise()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFakeAppsRequest(AbstractModel):
    """DescribeFakeApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFakeAppsResponse(AbstractModel):
    """DescribeFakeApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 仿冒应用
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayFakeApp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """仿冒应用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayFakeApp
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayFakeApp()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFakeMiniProgramsRequest(AbstractModel):
    """DescribeFakeMiniPrograms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFakeMiniProgramsResponse(AbstractModel):
    """DescribeFakeMiniPrograms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 仿冒小程序
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayFakeMiniProgram
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """仿冒小程序
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayFakeMiniProgram
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayFakeMiniProgram()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFakeWebsitesRequest(AbstractModel):
    """DescribeFakeWebsites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFakeWebsitesResponse(AbstractModel):
    """DescribeFakeWebsites返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 仿冒网站
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayFakeWebsite
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """仿冒网站
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayFakeWebsite
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayFakeWebsite()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFakeWechatOfficialsRequest(AbstractModel):
    """DescribeFakeWechatOfficials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFakeWechatOfficialsResponse(AbstractModel):
    """DescribeFakeWechatOfficials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 仿冒公众号
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayFakeWechatOfficial
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """仿冒公众号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayFakeWechatOfficial
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayFakeWechatOfficial()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGithubsRequest(AbstractModel):
    """DescribeGithubs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGithubsResponse(AbstractModel):
    """DescribeGithubs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayGithub
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayGithub
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayGithub()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHttpsRequest(AbstractModel):
    """DescribeHttps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        :param _IsShowChange: 是否显示变更
        :type IsShowChange: bool
        :param _HasExpirationRisk: 是否仅显示过期风险资产
        :type HasExpirationRisk: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None
        self._IsShowChange = None
        self._HasExpirationRisk = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored

    @property
    def IsShowChange(self):
        """是否显示变更
        :rtype: bool
        """
        return self._IsShowChange

    @IsShowChange.setter
    def IsShowChange(self, IsShowChange):
        self._IsShowChange = IsShowChange

    @property
    def HasExpirationRisk(self):
        """是否仅显示过期风险资产
        :rtype: bool
        """
        return self._HasExpirationRisk

    @HasExpirationRisk.setter
    def HasExpirationRisk(self, HasExpirationRisk):
        self._HasExpirationRisk = HasExpirationRisk


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        self._IsShowChange = params.get("IsShowChange")
        self._HasExpirationRisk = params.get("HasExpirationRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHttpsResponse(AbstractModel):
    """DescribeHttps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayHttp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayHttp
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayHttp()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobRecordDetailsRequest(AbstractModel):
    """DescribeJobRecordDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 数据类型，包括：enterprise(企业架构)，domain(主域名)，sub_domain(子域名)，asset(主机资产)，port(端口服务)，http(网站资产)，vul(漏洞信息)，app(APP)，wechat_applet(微信小程序)，wechat_official_account(微信公众号)，github(Github泄露)，manage(后台识别)，config(目录爆破)，dark_web(暗网泄露)，net_disk(文库网盘泄露)，social_engineering(员工信息)，supply_chain(供应链信息)，weak_password(弱口令)，sensitive_info(敏感信息泄露)，suspicious_asset(影子资产)
        :type Module: str
        :param _Id: 结果id
        :type Id: int
        :param _JobRecordId: 任务id
        :type JobRecordId: int
        """
        self._Module = None
        self._Id = None
        self._JobRecordId = None

    @property
    def Module(self):
        """数据类型，包括：enterprise(企业架构)，domain(主域名)，sub_domain(子域名)，asset(主机资产)，port(端口服务)，http(网站资产)，vul(漏洞信息)，app(APP)，wechat_applet(微信小程序)，wechat_official_account(微信公众号)，github(Github泄露)，manage(后台识别)，config(目录爆破)，dark_web(暗网泄露)，net_disk(文库网盘泄露)，social_engineering(员工信息)，supply_chain(供应链信息)，weak_password(弱口令)，sensitive_info(敏感信息泄露)，suspicious_asset(影子资产)
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Id(self):
        """结果id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def JobRecordId(self):
        """任务id
        :rtype: int
        """
        return self._JobRecordId

    @JobRecordId.setter
    def JobRecordId(self, JobRecordId):
        self._JobRecordId = JobRecordId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Id = params.get("Id")
        self._JobRecordId = params.get("JobRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobRecordDetailsResponse(AbstractModel):
    """DescribeJobRecordDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayJobRecordDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayJobRecordDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayJobRecordDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobRecordsRequest(AbstractModel):
    """DescribeJobRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Filters: 查询数组
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobRecordsResponse(AbstractModel):
    """DescribeJobRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayJobRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayJobRecord
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayJobRecord()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLeakageCodesRequest(AbstractModel):
    """DescribeLeakageCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLeakageCodesResponse(AbstractModel):
    """DescribeLeakageCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayLeakageCode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayLeakageCode
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayLeakageCode()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLeakageDatasRequest(AbstractModel):
    """DescribeLeakageDatas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLeakageDatasResponse(AbstractModel):
    """DescribeLeakageDatas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayLeakageData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayLeakageData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayLeakageData()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLeakageEmailsRequest(AbstractModel):
    """DescribeLeakageEmails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLeakageEmailsResponse(AbstractModel):
    """DescribeLeakageEmails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DisplayLeakageEmail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DisplayLeakageEmail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayLeakageEmail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeManagesRequest(AbstractModel):
    """DescribeManages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagesResponse(AbstractModel):
    """DescribeManages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayManage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayManage
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayManage()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNetDisksRequest(AbstractModel):
    """DescribeNetDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetDisksResponse(AbstractModel):
    """DescribeNetDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayNetDisk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayNetDisk
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayNetDisk()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePortsRequest(AbstractModel):
    """DescribePorts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePortsResponse(AbstractModel):
    """DescribePorts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayPort
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayPort
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayPort()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSensitiveInfosRequest(AbstractModel):
    """DescribeSensitiveInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSensitiveInfosResponse(AbstractModel):
    """DescribeSensitiveInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplaySensitiveInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplaySensitiveInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplaySensitiveInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubDomainsRequest(AbstractModel):
    """DescribeSubDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._IsAggregation = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._IsAggregation = params.get("IsAggregation")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubDomainsResponse(AbstractModel):
    """DescribeSubDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplaySubDomain
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplaySubDomain
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplaySubDomain()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSuspiciousAssetsRequest(AbstractModel):
    """DescribeSuspiciousAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsAggregation: 是否聚合数据
        :type IsAggregation: bool
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsAggregation = None
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsAggregation(self):
        """是否聚合数据
        :rtype: bool
        """
        return self._IsAggregation

    @IsAggregation.setter
    def IsAggregation(self, IsAggregation):
        self._IsAggregation = IsAggregation

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsAggregation = params.get("IsAggregation")
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSuspiciousAssetsResponse(AbstractModel):
    """DescribeSuspiciousAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplaySuspiciousAsset
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplaySuspiciousAsset
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplaySuspiciousAsset()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayVul
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayVul
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayVul()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWeakPasswordsRequest(AbstractModel):
    """DescribeWeakPasswords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeakPasswordsResponse(AbstractModel):
    """DescribeWeakPasswords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayWeakPassword
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayWeakPassword
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayWeakPassword()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWechatAppletsRequest(AbstractModel):
    """DescribeWechatApplets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._CustomerId = None
        self._IsNew = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._IsNew = params.get("IsNew")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWechatAppletsResponse(AbstractModel):
    """DescribeWechatApplets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayWechatApplet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayWechatApplet
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayWechatApplet()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWechatOfficialAccountsRequest(AbstractModel):
    """DescribeWechatOfficialAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsNew: 是否新增数据
        :type IsNew: bool
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        :param _EnterpriseUidList: 子公司ID列表
        :type EnterpriseUidList: list of str
        :param _Format: 数据输出格式：json、file，默认不填为json
        :type Format: str
        :param _CreateAtStart: 创建时间-开始
        :type CreateAtStart: str
        :param _CreateAtEnd: 创建时间-结束
        :type CreateAtEnd: str
        :param _UpdateAtStart: 更新时间-开始
        :type UpdateAtStart: str
        :param _UpdateAtEnd: 更新时间-结束
        :type UpdateAtEnd: str
        :param _Filters: 查询数组
        :type Filters: list of Filter
        :param _Ignored: 是否显示被忽略的数据
        :type Ignored: bool
        """
        self._IsNew = None
        self._CustomerId = None
        self._Limit = None
        self._Offset = None
        self._EnterpriseUidList = None
        self._Format = None
        self._CreateAtStart = None
        self._CreateAtEnd = None
        self._UpdateAtStart = None
        self._UpdateAtEnd = None
        self._Filters = None
        self._Ignored = None

    @property
    def IsNew(self):
        """是否新增数据
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnterpriseUidList(self):
        """子公司ID列表
        :rtype: list of str
        """
        return self._EnterpriseUidList

    @EnterpriseUidList.setter
    def EnterpriseUidList(self, EnterpriseUidList):
        self._EnterpriseUidList = EnterpriseUidList

    @property
    def Format(self):
        """数据输出格式：json、file，默认不填为json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateAtStart(self):
        """创建时间-开始
        :rtype: str
        """
        return self._CreateAtStart

    @CreateAtStart.setter
    def CreateAtStart(self, CreateAtStart):
        self._CreateAtStart = CreateAtStart

    @property
    def CreateAtEnd(self):
        """创建时间-结束
        :rtype: str
        """
        return self._CreateAtEnd

    @CreateAtEnd.setter
    def CreateAtEnd(self, CreateAtEnd):
        self._CreateAtEnd = CreateAtEnd

    @property
    def UpdateAtStart(self):
        """更新时间-开始
        :rtype: str
        """
        return self._UpdateAtStart

    @UpdateAtStart.setter
    def UpdateAtStart(self, UpdateAtStart):
        self._UpdateAtStart = UpdateAtStart

    @property
    def UpdateAtEnd(self):
        """更新时间-结束
        :rtype: str
        """
        return self._UpdateAtEnd

    @UpdateAtEnd.setter
    def UpdateAtEnd(self, UpdateAtEnd):
        self._UpdateAtEnd = UpdateAtEnd

    @property
    def Filters(self):
        """查询数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Ignored(self):
        """是否显示被忽略的数据
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored


    def _deserialize(self, params):
        self._IsNew = params.get("IsNew")
        self._CustomerId = params.get("CustomerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnterpriseUidList = params.get("EnterpriseUidList")
        self._Format = params.get("Format")
        self._CreateAtStart = params.get("CreateAtStart")
        self._CreateAtEnd = params.get("CreateAtEnd")
        self._UpdateAtStart = params.get("UpdateAtStart")
        self._UpdateAtEnd = params.get("UpdateAtEnd")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Ignored = params.get("Ignored")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWechatOfficialAccountsResponse(AbstractModel):
    """DescribeWechatOfficialAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 数组
        :type List: list of DisplayWechatOfficialAccount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """数组
        :rtype: list of DisplayWechatOfficialAccount
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DisplayWechatOfficialAccount()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DisplayApp(AbstractModel):
    """移动资产详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Name: APP名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _Developer: 开发者
        :type Developer: str
        :param _DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param _Logo: 图片
        :type Logo: str
        :param _PackageName: 包名
        :type PackageName: str
        :param _Platform: 平台
        :type Platform: str
        :param _ServerUrl: 服务端地址
        :type ServerUrl: str
        :param _AppVersion: app版本
        :type AppVersion: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Name = None
        self._Description = None
        self._Developer = None
        self._DownloadUrl = None
        self._Logo = None
        self._PackageName = None
        self._Platform = None
        self._ServerUrl = None
        self._AppVersion = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Name(self):
        """APP名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Developer(self):
        """开发者
        :rtype: str
        """
        return self._Developer

    @Developer.setter
    def Developer(self, Developer):
        self._Developer = Developer

    @property
    def DownloadUrl(self):
        """下载地址
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Logo(self):
        """图片
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def PackageName(self):
        """包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        """平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ServerUrl(self):
        """服务端地址
        :rtype: str
        """
        return self._ServerUrl

    @ServerUrl.setter
    def ServerUrl(self, ServerUrl):
        self._ServerUrl = ServerUrl

    @property
    def AppVersion(self):
        """app版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Developer = params.get("Developer")
        self._DownloadUrl = params.get("DownloadUrl")
        self._Logo = params.get("Logo")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._ServerUrl = params.get("ServerUrl")
        self._AppVersion = params.get("AppVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayAsset(AbstractModel):
    """主机资产详情

    """

    def __init__(self):
        r"""
        :param _Id: 主机资产Id
        :type Id: int
        :param _Os: 操作系统类型
        :type Os: str
        :param _Ip: 主机地址
        :type Ip: str
        :param _Country: 国家
        :type Country: str
        :param _Province: 省份
        :type Province: str
        :param _City: 地域
        :type City: str
        :param _Isp: 运营商
        :type Isp: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._Os = None
        self._Ip = None
        self._Country = None
        self._Province = None
        self._City = None
        self._Isp = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主机资产Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Os(self):
        """操作系统类型
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Ip(self):
        """主机地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Country(self):
        """国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """地域
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Isp(self):
        """运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Os = params.get("Os")
        self._Ip = params.get("Ip")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Isp = params.get("Isp")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayConfig(AbstractModel):
    """目录爆破详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键Id
        :type Id: int
        :param _Url: 地址
        :type Url: str
        :param _Title: 站点标题
        :type Title: str
        :param _Code: 状态码
        :type Code: int
        :param _ContentLength: 响应长度
        :type ContentLength: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Ip: Ip数据
        :type Ip: str
        :param _AIRating: AI评分
        :type AIRating: int
        :param _AIAnalysis: AI分析
        :type AIAnalysis: str
        :param _RiskLevel: 风险等级: 1-低危, 2-中危, 3-高危, 4-危级, 5-误报
        :type RiskLevel: int
        :param _Suggestion: 建议
        :type Suggestion: str
        """
        self._Id = None
        self._Url = None
        self._Title = None
        self._Code = None
        self._ContentLength = None
        self._DisplayToolCommon = None
        self._Ip = None
        self._AIRating = None
        self._AIAnalysis = None
        self._RiskLevel = None
        self._Suggestion = None

    @property
    def Id(self):
        """主键Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Title(self):
        """站点标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        """状态码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def ContentLength(self):
        """响应长度
        :rtype: int
        """
        return self._ContentLength

    @ContentLength.setter
    def ContentLength(self, ContentLength):
        self._ContentLength = ContentLength

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Ip(self):
        """Ip数据
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def AIRating(self):
        """AI评分
        :rtype: int
        """
        return self._AIRating

    @AIRating.setter
    def AIRating(self, AIRating):
        self._AIRating = AIRating

    @property
    def AIAnalysis(self):
        """AI分析
        :rtype: str
        """
        return self._AIAnalysis

    @AIAnalysis.setter
    def AIAnalysis(self, AIAnalysis):
        self._AIAnalysis = AIAnalysis

    @property
    def RiskLevel(self):
        """风险等级: 1-低危, 2-中危, 3-高危, 4-危级, 5-误报
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Suggestion(self):
        """建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._ContentLength = params.get("ContentLength")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Ip = params.get("Ip")
        self._AIRating = params.get("AIRating")
        self._AIAnalysis = params.get("AIAnalysis")
        self._RiskLevel = params.get("RiskLevel")
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayDarkWeb(AbstractModel):
    """暗网详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Content: 内容
        :type Content: str
        :param _MatchedKeywords: 命中关键字
        :type MatchedKeywords: str
        :param _Url: APP地址
        :type Url: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._Content = None
        self._MatchedKeywords = None
        self._Url = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MatchedKeywords(self):
        """命中关键字
        :rtype: str
        """
        return self._MatchedKeywords

    @MatchedKeywords.setter
    def MatchedKeywords(self, MatchedKeywords):
        self._MatchedKeywords = MatchedKeywords

    @property
    def Url(self):
        """APP地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Content = params.get("Content")
        self._MatchedKeywords = params.get("MatchedKeywords")
        self._Url = params.get("Url")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayDomain(AbstractModel):
    """主域名详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Domain: 主域名
        :type Domain: str
        :param _ICP: ICP
        :type ICP: str
        :param _RegisteredTime: 注册时间
        :type RegisteredTime: str
        :param _ExpiredTime: 过期时间
        :type ExpiredTime: str
        :param _Company: 公司
        :type Company: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._Domain = None
        self._ICP = None
        self._RegisteredTime = None
        self._ExpiredTime = None
        self._Company = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        """主域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ICP(self):
        """ICP
        :rtype: str
        """
        return self._ICP

    @ICP.setter
    def ICP(self, ICP):
        self._ICP = ICP

    @property
    def RegisteredTime(self):
        """注册时间
        :rtype: str
        """
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def ExpiredTime(self):
        """过期时间
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Company(self):
        """公司
        :rtype: str
        """
        return self._Company

    @Company.setter
    def Company(self, Company):
        self._Company = Company

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._ICP = params.get("ICP")
        self._RegisteredTime = params.get("RegisteredTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Company = params.get("Company")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayEnterprise(AbstractModel):
    """企业架构详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键Id
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _ParentEnterpriseUid: 子公司上级
        :type ParentEnterpriseUid: str
        :param _Name: 企业名称
        :type Name: str
        :param _Abbreviation: 公司简称
        :type Abbreviation: str
        :param _CreditCode: 统一社会信用代码
        :type CreditCode: str
        :param _Status: 企业状态
        :type Status: str
        :param _RegisteredCapital: 注册资本
        :type RegisteredCapital: str
        :param _ShareholdingRatio: 持股比例
        :type ShareholdingRatio: str
        :param _LegalPerson: 法人代表
        :type LegalPerson: str
        :param _Type: 类型
        :type Type: str
        :param _Industry: 行业类型
        :type Industry: str
        :param _EnterpriseUid: 子公司唯一uid
        :type EnterpriseUid: str
        :param _DomainCount: 主域名数量
        :type DomainCount: int
        :param _SubDomainCount: 子域名数量
        :type SubDomainCount: int
        :param _HttpCount: 网站数量
        :type HttpCount: int
        :param _VulCount: 漏洞数量
        :type VulCount: int
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._ParentEnterpriseUid = None
        self._Name = None
        self._Abbreviation = None
        self._CreditCode = None
        self._Status = None
        self._RegisteredCapital = None
        self._ShareholdingRatio = None
        self._LegalPerson = None
        self._Type = None
        self._Industry = None
        self._EnterpriseUid = None
        self._DomainCount = None
        self._SubDomainCount = None
        self._HttpCount = None
        self._VulCount = None

    @property
    def Id(self):
        """主键Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def ParentEnterpriseUid(self):
        """子公司上级
        :rtype: str
        """
        return self._ParentEnterpriseUid

    @ParentEnterpriseUid.setter
    def ParentEnterpriseUid(self, ParentEnterpriseUid):
        self._ParentEnterpriseUid = ParentEnterpriseUid

    @property
    def Name(self):
        """企业名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Abbreviation(self):
        """公司简称
        :rtype: str
        """
        return self._Abbreviation

    @Abbreviation.setter
    def Abbreviation(self, Abbreviation):
        self._Abbreviation = Abbreviation

    @property
    def CreditCode(self):
        """统一社会信用代码
        :rtype: str
        """
        return self._CreditCode

    @CreditCode.setter
    def CreditCode(self, CreditCode):
        self._CreditCode = CreditCode

    @property
    def Status(self):
        """企业状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegisteredCapital(self):
        """注册资本
        :rtype: str
        """
        return self._RegisteredCapital

    @RegisteredCapital.setter
    def RegisteredCapital(self, RegisteredCapital):
        self._RegisteredCapital = RegisteredCapital

    @property
    def ShareholdingRatio(self):
        """持股比例
        :rtype: str
        """
        return self._ShareholdingRatio

    @ShareholdingRatio.setter
    def ShareholdingRatio(self, ShareholdingRatio):
        self._ShareholdingRatio = ShareholdingRatio

    @property
    def LegalPerson(self):
        """法人代表
        :rtype: str
        """
        return self._LegalPerson

    @LegalPerson.setter
    def LegalPerson(self, LegalPerson):
        self._LegalPerson = LegalPerson

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Industry(self):
        """行业类型
        :rtype: str
        """
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def EnterpriseUid(self):
        """子公司唯一uid
        :rtype: str
        """
        return self._EnterpriseUid

    @EnterpriseUid.setter
    def EnterpriseUid(self, EnterpriseUid):
        self._EnterpriseUid = EnterpriseUid

    @property
    def DomainCount(self):
        """主域名数量
        :rtype: int
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def SubDomainCount(self):
        """子域名数量
        :rtype: int
        """
        return self._SubDomainCount

    @SubDomainCount.setter
    def SubDomainCount(self, SubDomainCount):
        self._SubDomainCount = SubDomainCount

    @property
    def HttpCount(self):
        """网站数量
        :rtype: int
        """
        return self._HttpCount

    @HttpCount.setter
    def HttpCount(self, HttpCount):
        self._HttpCount = HttpCount

    @property
    def VulCount(self):
        """漏洞数量
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._ParentEnterpriseUid = params.get("ParentEnterpriseUid")
        self._Name = params.get("Name")
        self._Abbreviation = params.get("Abbreviation")
        self._CreditCode = params.get("CreditCode")
        self._Status = params.get("Status")
        self._RegisteredCapital = params.get("RegisteredCapital")
        self._ShareholdingRatio = params.get("ShareholdingRatio")
        self._LegalPerson = params.get("LegalPerson")
        self._Type = params.get("Type")
        self._Industry = params.get("Industry")
        self._EnterpriseUid = params.get("EnterpriseUid")
        self._DomainCount = params.get("DomainCount")
        self._SubDomainCount = params.get("SubDomainCount")
        self._HttpCount = params.get("HttpCount")
        self._VulCount = params.get("VulCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayFakeApp(AbstractModel):
    """仿冒应用详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _AppName: 仿冒应用名称
        :type AppName: str
        :param _PackageName: 仿冒应用包名称
        :type PackageName: str
        :param _DownloadUrl: 下载链接
        :type DownloadUrl: str
        :param _HandlingStatus: 处置状态：0-待处理 1-处理中 2-已处理
        :type HandlingStatus: int
        :param _ShutdownStatus: 关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :type ShutdownStatus: int
        :param _ShutdownTime: 关停时间
        :type ShutdownTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._AppName = None
        self._PackageName = None
        self._DownloadUrl = None
        self._HandlingStatus = None
        self._ShutdownStatus = None
        self._ShutdownTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def AppName(self):
        """仿冒应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PackageName(self):
        """仿冒应用包名称
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def DownloadUrl(self):
        """下载链接
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def HandlingStatus(self):
        """处置状态：0-待处理 1-处理中 2-已处理
        :rtype: int
        """
        return self._HandlingStatus

    @HandlingStatus.setter
    def HandlingStatus(self, HandlingStatus):
        self._HandlingStatus = HandlingStatus

    @property
    def ShutdownStatus(self):
        """关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :rtype: int
        """
        return self._ShutdownStatus

    @ShutdownStatus.setter
    def ShutdownStatus(self, ShutdownStatus):
        self._ShutdownStatus = ShutdownStatus

    @property
    def ShutdownTime(self):
        """关停时间
        :rtype: str
        """
        return self._ShutdownTime

    @ShutdownTime.setter
    def ShutdownTime(self, ShutdownTime):
        self._ShutdownTime = ShutdownTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._AppName = params.get("AppName")
        self._PackageName = params.get("PackageName")
        self._DownloadUrl = params.get("DownloadUrl")
        self._HandlingStatus = params.get("HandlingStatus")
        self._ShutdownStatus = params.get("ShutdownStatus")
        self._ShutdownTime = params.get("ShutdownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayFakeMiniProgram(AbstractModel):
    """仿冒小程序详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _ProgramName: 仿冒小程序名称
        :type ProgramName: str
        :param _ProgramId: 小程序ID
        :type ProgramId: str
        :param _Category: 类别
        :type Category: str
        :param _QrCode: 二维码
        :type QrCode: str
        :param _HandlingStatus: 处置状态：0-待处理 1-处理中 2-已处理
        :type HandlingStatus: int
        :param _ShutdownStatus: 关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :type ShutdownStatus: int
        :param _ShutdownTime: 关停时间
        :type ShutdownTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._ProgramName = None
        self._ProgramId = None
        self._Category = None
        self._QrCode = None
        self._HandlingStatus = None
        self._ShutdownStatus = None
        self._ShutdownTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def ProgramName(self):
        """仿冒小程序名称
        :rtype: str
        """
        return self._ProgramName

    @ProgramName.setter
    def ProgramName(self, ProgramName):
        self._ProgramName = ProgramName

    @property
    def ProgramId(self):
        """小程序ID
        :rtype: str
        """
        return self._ProgramId

    @ProgramId.setter
    def ProgramId(self, ProgramId):
        self._ProgramId = ProgramId

    @property
    def Category(self):
        """类别
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def QrCode(self):
        """二维码
        :rtype: str
        """
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def HandlingStatus(self):
        """处置状态：0-待处理 1-处理中 2-已处理
        :rtype: int
        """
        return self._HandlingStatus

    @HandlingStatus.setter
    def HandlingStatus(self, HandlingStatus):
        self._HandlingStatus = HandlingStatus

    @property
    def ShutdownStatus(self):
        """关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :rtype: int
        """
        return self._ShutdownStatus

    @ShutdownStatus.setter
    def ShutdownStatus(self, ShutdownStatus):
        self._ShutdownStatus = ShutdownStatus

    @property
    def ShutdownTime(self):
        """关停时间
        :rtype: str
        """
        return self._ShutdownTime

    @ShutdownTime.setter
    def ShutdownTime(self, ShutdownTime):
        self._ShutdownTime = ShutdownTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._ProgramName = params.get("ProgramName")
        self._ProgramId = params.get("ProgramId")
        self._Category = params.get("Category")
        self._QrCode = params.get("QrCode")
        self._HandlingStatus = params.get("HandlingStatus")
        self._ShutdownStatus = params.get("ShutdownStatus")
        self._ShutdownTime = params.get("ShutdownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayFakeWebsite(AbstractModel):
    """仿冒网站详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Website: 仿冒网站
        :type Website: str
        :param _IPLocation: ip位置
        :type IPLocation: str
        :param _Screenshot: 截图
        :type Screenshot: str
        :param _HandlingStatus: 处置状态：0-待处理 1-处理中 2-已处理
        :type HandlingStatus: int
        :param _ShutdownStatus: 关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :type ShutdownStatus: int
        :param _ShutdownTime: 关停时间
        :type ShutdownTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Website = None
        self._IPLocation = None
        self._Screenshot = None
        self._HandlingStatus = None
        self._ShutdownStatus = None
        self._ShutdownTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Website(self):
        """仿冒网站
        :rtype: str
        """
        return self._Website

    @Website.setter
    def Website(self, Website):
        self._Website = Website

    @property
    def IPLocation(self):
        """ip位置
        :rtype: str
        """
        return self._IPLocation

    @IPLocation.setter
    def IPLocation(self, IPLocation):
        self._IPLocation = IPLocation

    @property
    def Screenshot(self):
        """截图
        :rtype: str
        """
        return self._Screenshot

    @Screenshot.setter
    def Screenshot(self, Screenshot):
        self._Screenshot = Screenshot

    @property
    def HandlingStatus(self):
        """处置状态：0-待处理 1-处理中 2-已处理
        :rtype: int
        """
        return self._HandlingStatus

    @HandlingStatus.setter
    def HandlingStatus(self, HandlingStatus):
        self._HandlingStatus = HandlingStatus

    @property
    def ShutdownStatus(self):
        """关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :rtype: int
        """
        return self._ShutdownStatus

    @ShutdownStatus.setter
    def ShutdownStatus(self, ShutdownStatus):
        self._ShutdownStatus = ShutdownStatus

    @property
    def ShutdownTime(self):
        """关停时间
        :rtype: str
        """
        return self._ShutdownTime

    @ShutdownTime.setter
    def ShutdownTime(self, ShutdownTime):
        self._ShutdownTime = ShutdownTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Website = params.get("Website")
        self._IPLocation = params.get("IPLocation")
        self._Screenshot = params.get("Screenshot")
        self._HandlingStatus = params.get("HandlingStatus")
        self._ShutdownStatus = params.get("ShutdownStatus")
        self._ShutdownTime = params.get("ShutdownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayFakeWechatOfficial(AbstractModel):
    """仿冒公众号详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _AccountName: 仿冒公众号名称
        :type AccountName: str
        :param _WechatId: 公众号ID
        :type WechatId: str
        :param _Avatar: 头像
        :type Avatar: str
        :param _QrCode: 二维码
        :type QrCode: str
        :param _HandlingStatus: 处置状态：0-待处理 1-处理中 2-已处理
        :type HandlingStatus: int
        :param _ShutdownStatus: 关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :type ShutdownStatus: int
        :param _ShutdownTime: 关停时间
        :type ShutdownTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._AccountName = None
        self._WechatId = None
        self._Avatar = None
        self._QrCode = None
        self._HandlingStatus = None
        self._ShutdownStatus = None
        self._ShutdownTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def AccountName(self):
        """仿冒公众号名称
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def WechatId(self):
        """公众号ID
        :rtype: str
        """
        return self._WechatId

    @WechatId.setter
    def WechatId(self, WechatId):
        self._WechatId = WechatId

    @property
    def Avatar(self):
        """头像
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def QrCode(self):
        """二维码
        :rtype: str
        """
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def HandlingStatus(self):
        """处置状态：0-待处理 1-处理中 2-已处理
        :rtype: int
        """
        return self._HandlingStatus

    @HandlingStatus.setter
    def HandlingStatus(self, HandlingStatus):
        self._HandlingStatus = HandlingStatus

    @property
    def ShutdownStatus(self):
        """关停状态：0-(默认状态) 1-关停审核中 2-已拦截 3-已拒绝 4-下线流程中 5-已下线 6-下线失败
        :rtype: int
        """
        return self._ShutdownStatus

    @ShutdownStatus.setter
    def ShutdownStatus(self, ShutdownStatus):
        self._ShutdownStatus = ShutdownStatus

    @property
    def ShutdownTime(self):
        """关停时间
        :rtype: str
        """
        return self._ShutdownTime

    @ShutdownTime.setter
    def ShutdownTime(self, ShutdownTime):
        self._ShutdownTime = ShutdownTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._AccountName = params.get("AccountName")
        self._WechatId = params.get("WechatId")
        self._Avatar = params.get("Avatar")
        self._QrCode = params.get("QrCode")
        self._HandlingStatus = params.get("HandlingStatus")
        self._ShutdownStatus = params.get("ShutdownStatus")
        self._ShutdownTime = params.get("ShutdownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayGithub(AbstractModel):
    """Github泄露详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Content: 内容
        :type Content: str
        :param _MatchedKeywords: 命中关键字
        :type MatchedKeywords: str
        :param _Url: 泄露地址
        :type Url: str
        :param _Status: 状态
        :type Status: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._Content = None
        self._MatchedKeywords = None
        self._Url = None
        self._Status = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MatchedKeywords(self):
        """命中关键字
        :rtype: str
        """
        return self._MatchedKeywords

    @MatchedKeywords.setter
    def MatchedKeywords(self, MatchedKeywords):
        self._MatchedKeywords = MatchedKeywords

    @property
    def Url(self):
        """泄露地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Content = params.get("Content")
        self._MatchedKeywords = params.get("MatchedKeywords")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayHttp(AbstractModel):
    """Http详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Url: Url
        :type Url: str
        :param _Title: 标题
        :type Title: str
        :param _ContentLength: 报文长度
        :type ContentLength: int
        :param _Content: 报文内容
        :type Content: str
        :param _ScreenshotThumbUrl: 截图缩略图URL
        :type ScreenshotThumbUrl: str
        :param _ScreenshotUrl: 截图URL
        :type ScreenshotUrl: str
        :param _Code: 状态码
        :type Code: int
        :param _Api: Api地址
        :type Api: str
        :param _Ip: 解析的IP
        :type Ip: str
        :param _Ssl: 证书信息
        :type Ssl: str
        :param _SslExpiredTime: ssl证书过期时间
        :type SslExpiredTime: str
        :param _IsChange: 资产是否发生变动
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChange: bool
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Url = None
        self._Title = None
        self._ContentLength = None
        self._Content = None
        self._ScreenshotThumbUrl = None
        self._ScreenshotUrl = None
        self._Code = None
        self._Api = None
        self._Ip = None
        self._Ssl = None
        self._SslExpiredTime = None
        self._IsChange = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Url(self):
        """Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Title(self):
        """标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ContentLength(self):
        """报文长度
        :rtype: int
        """
        return self._ContentLength

    @ContentLength.setter
    def ContentLength(self, ContentLength):
        self._ContentLength = ContentLength

    @property
    def Content(self):
        """报文内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ScreenshotThumbUrl(self):
        """截图缩略图URL
        :rtype: str
        """
        return self._ScreenshotThumbUrl

    @ScreenshotThumbUrl.setter
    def ScreenshotThumbUrl(self, ScreenshotThumbUrl):
        self._ScreenshotThumbUrl = ScreenshotThumbUrl

    @property
    def ScreenshotUrl(self):
        """截图URL
        :rtype: str
        """
        return self._ScreenshotUrl

    @ScreenshotUrl.setter
    def ScreenshotUrl(self, ScreenshotUrl):
        self._ScreenshotUrl = ScreenshotUrl

    @property
    def Code(self):
        """状态码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Api(self):
        """Api地址
        :rtype: str
        """
        return self._Api

    @Api.setter
    def Api(self, Api):
        self._Api = Api

    @property
    def Ip(self):
        """解析的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Ssl(self):
        """证书信息
        :rtype: str
        """
        return self._Ssl

    @Ssl.setter
    def Ssl(self, Ssl):
        self._Ssl = Ssl

    @property
    def SslExpiredTime(self):
        """ssl证书过期时间
        :rtype: str
        """
        return self._SslExpiredTime

    @SslExpiredTime.setter
    def SslExpiredTime(self, SslExpiredTime):
        self._SslExpiredTime = SslExpiredTime

    @property
    def IsChange(self):
        """资产是否发生变动
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsChange

    @IsChange.setter
    def IsChange(self, IsChange):
        self._IsChange = IsChange


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Url = params.get("Url")
        self._Title = params.get("Title")
        self._ContentLength = params.get("ContentLength")
        self._Content = params.get("Content")
        self._ScreenshotThumbUrl = params.get("ScreenshotThumbUrl")
        self._ScreenshotUrl = params.get("ScreenshotUrl")
        self._Code = params.get("Code")
        self._Api = params.get("Api")
        self._Ip = params.get("Ip")
        self._Ssl = params.get("Ssl")
        self._SslExpiredTime = params.get("SslExpiredTime")
        self._IsChange = params.get("IsChange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayJobRecord(AbstractModel):
    """任务详情

    """

    def __init__(self):
        r"""
        :param _Id: 任务Id
        :type Id: int
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _CustomerName: 企业名称
        :type CustomerName: str
        :param _Crontab: 周期任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Crontab: str
        :param _Status: 状态：2-错误/已停止，3-进行中，1-已完成, 4-停止
        :type Status: int
        :param _NewCount: 新增数据
        :type NewCount: int
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 更新时间
        :type UpdateAt: str
        :param _Progress: 子任务进度
        :type Progress: :class:`tencentcloud.ctem.v20231128.models.JobRecordProgress`
        :param _Qps: 并发设置
        :type Qps: int
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _Uin: 客户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _AppId: 客户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._Id = None
        self._CustomerId = None
        self._CustomerName = None
        self._Crontab = None
        self._Status = None
        self._NewCount = None
        self._CreateAt = None
        self._UpdateAt = None
        self._Progress = None
        self._Qps = None
        self._TaskType = None
        self._Uin = None
        self._AppId = None

    @property
    def Id(self):
        """任务Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """企业名称
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def Crontab(self):
        """周期任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab

    @property
    def Status(self):
        """状态：2-错误/已停止，3-进行中，1-已完成, 4-停止
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NewCount(self):
        """新增数据
        :rtype: int
        """
        return self._NewCount

    @NewCount.setter
    def NewCount(self, NewCount):
        self._NewCount = NewCount

    @property
    def CreateAt(self):
        """创建时间
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def Progress(self):
        """子任务进度
        :rtype: :class:`tencentcloud.ctem.v20231128.models.JobRecordProgress`
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Qps(self):
        """并发设置
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def TaskType(self):
        """任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Uin(self):
        """客户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        """客户appid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._Crontab = params.get("Crontab")
        self._Status = params.get("Status")
        self._NewCount = params.get("NewCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        if params.get("Progress") is not None:
            self._Progress = JobRecordProgress()
            self._Progress._deserialize(params.get("Progress"))
        self._Qps = params.get("Qps")
        self._TaskType = params.get("TaskType")
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayJobRecordDetail(AbstractModel):
    """链路详情

    """

    def __init__(self):
        r"""
        :param _TimeAt: 发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeAt: str
        :param _Module: 模块
注意：此字段可能返回 null，表示取不到有效值。
        :type Module: str
        :param _ModuleName: 模块名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleName: str
        :param _JobRecordId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobRecordId: int
        :param _Data: 目标
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of IdndValue
        """
        self._TimeAt = None
        self._Module = None
        self._ModuleName = None
        self._JobRecordId = None
        self._Data = None

    @property
    def TimeAt(self):
        """发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeAt

    @TimeAt.setter
    def TimeAt(self, TimeAt):
        self._TimeAt = TimeAt

    @property
    def Module(self):
        """模块
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ModuleName(self):
        """模块名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName

    @property
    def JobRecordId(self):
        """任务id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobRecordId

    @JobRecordId.setter
    def JobRecordId(self, JobRecordId):
        self._JobRecordId = JobRecordId

    @property
    def Data(self):
        """目标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IdndValue
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._TimeAt = params.get("TimeAt")
        self._Module = params.get("Module")
        self._ModuleName = params.get("ModuleName")
        self._JobRecordId = params.get("JobRecordId")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IdndValue()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayLeakageCode(AbstractModel):
    """代码泄露详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Url: 链接
        :type Url: str
        """
        self._Id = None
        self._Url = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayLeakageData(AbstractModel):
    """数据泄露详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Url: 链接
        :type Url: str
        """
        self._Id = None
        self._Url = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayLeakageEmail(AbstractModel):
    """邮箱泄露详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Email: 邮箱
        :type Email: str
        """
        self._Id = None
        self._Email = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayManage(AbstractModel):
    """后台详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Url: Url
        :type Url: str
        :param _Title: 标题
        :type Title: str
        :param _Icon: Icon
        :type Icon: str
        :param _Screenshot: 缩略图
        :type Screenshot: str
        :param _Code: 状态码
        :type Code: int
        :param _Host: 后台Host
        :type Host: str
        :param _Status: 状态：not_converged:未收敛, converged:已收敛, ignore:已忽略

        :type Status: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Url = None
        self._Title = None
        self._Icon = None
        self._Screenshot = None
        self._Code = None
        self._Host = None
        self._Status = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Url(self):
        """Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Title(self):
        """标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Icon(self):
        """Icon
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Screenshot(self):
        """缩略图
        :rtype: str
        """
        return self._Screenshot

    @Screenshot.setter
    def Screenshot(self, Screenshot):
        self._Screenshot = Screenshot

    @property
    def Code(self):
        """状态码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Host(self):
        """后台Host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Status(self):
        """状态：not_converged:未收敛, converged:已收敛, ignore:已忽略

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Url = params.get("Url")
        self._Title = params.get("Title")
        self._Icon = params.get("Icon")
        self._Screenshot = params.get("Screenshot")
        self._Code = params.get("Code")
        self._Host = params.get("Host")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayNetDisk(AbstractModel):
    """网盘泄露详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _Content: 内容
        :type Content: str
        :param _MatchedKeywords: 命中关键字
        :type MatchedKeywords: str
        :param _Url: 泄露地址
        :type Url: str
        :param _Status: 状态
        :type Status: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Platform: 泄露平台
        :type Platform: str
        """
        self._Id = None
        self._Content = None
        self._MatchedKeywords = None
        self._Url = None
        self._Status = None
        self._DisplayToolCommon = None
        self._Platform = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MatchedKeywords(self):
        """命中关键字
        :rtype: str
        """
        return self._MatchedKeywords

    @MatchedKeywords.setter
    def MatchedKeywords(self, MatchedKeywords):
        self._MatchedKeywords = MatchedKeywords

    @property
    def Url(self):
        """泄露地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Platform(self):
        """泄露平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Content = params.get("Content")
        self._MatchedKeywords = params.get("MatchedKeywords")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayPort(AbstractModel):
    """端口详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Asset: IP或域名地址
        :type Asset: str
        :param _Ip: 解析的IP
        :type Ip: str
        :param _Port: 端口
        :type Port: int
        :param _IsHighRisk: 是否高危
        :type IsHighRisk: bool
        :param _App: 组件名称
        :type App: str
        :param _Service: 服务名称
        :type Service: str
        :param _Banner: 端口响应详情
        :type Banner: str
        :param _LastCheckTime: 上次检测时间
        :type LastCheckTime: str
        :param _Status: 状态，close:连接超时，端口可能已关闭，open:端口开放, checking:复测中, ignore:已忽略
        :type Status: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Asset = None
        self._Ip = None
        self._Port = None
        self._IsHighRisk = None
        self._App = None
        self._Service = None
        self._Banner = None
        self._LastCheckTime = None
        self._Status = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Asset(self):
        """IP或域名地址
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Ip(self):
        """解析的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def IsHighRisk(self):
        """是否高危
        :rtype: bool
        """
        return self._IsHighRisk

    @IsHighRisk.setter
    def IsHighRisk(self, IsHighRisk):
        self._IsHighRisk = IsHighRisk

    @property
    def App(self):
        """组件名称
        :rtype: str
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def Service(self):
        """服务名称
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Banner(self):
        """端口响应详情
        :rtype: str
        """
        return self._Banner

    @Banner.setter
    def Banner(self, Banner):
        self._Banner = Banner

    @property
    def LastCheckTime(self):
        """上次检测时间
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime

    @property
    def Status(self):
        """状态，close:连接超时，端口可能已关闭，open:端口开放, checking:复测中, ignore:已忽略
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Asset = params.get("Asset")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._IsHighRisk = params.get("IsHighRisk")
        self._App = params.get("App")
        self._Service = params.get("Service")
        self._Banner = params.get("Banner")
        self._LastCheckTime = params.get("LastCheckTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplaySensitiveInfo(AbstractModel):
    """敏感信息泄露数据

    """

    def __init__(self):
        r"""
        :param _Id: 主键Id
        :type Id: int
        :param _Type: 类型
        :type Type: str
        :param _Source: 来源
        :type Source: str
        :param _Value: 值
        :type Value: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._Type = None
        self._Source = None
        self._Value = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主键Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Source(self):
        """来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Value(self):
        """值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Source = params.get("Source")
        self._Value = params.get("Value")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplaySubDomain(AbstractModel):
    """子域名详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _SubDomain: 子域名
        :type SubDomain: str
        :param _Ip: Ip
        :type Ip: str
        :param _Country: 国家
        :type Country: str
        :param _Province: 省份
        :type Province: str
        :param _City: 城市
        :type City: str
        :param _Isp: 互联网服务提供商
        :type Isp: str
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        self._Id = None
        self._SubDomain = None
        self._Ip = None
        self._Country = None
        self._Province = None
        self._City = None
        self._Isp = None
        self._DisplayToolCommon = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SubDomain(self):
        """子域名
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Ip(self):
        """Ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Country(self):
        """国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Isp(self):
        """互联网服务提供商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SubDomain = params.get("SubDomain")
        self._Ip = params.get("Ip")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Isp = params.get("Isp")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplaySuspiciousAsset(AbstractModel):
    """影子资产详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Url: Url
        :type Url: str
        :param _Title: 标题
        :type Title: str
        :param _ContentLength: 报文长度
        :type ContentLength: int
        :param _Content: 报文内容
        :type Content: str
        :param _ScreenshotThumbUrl: 截图缩略图URL
        :type ScreenshotThumbUrl: str
        :param _ScreenshotUrl: 截图URL
        :type ScreenshotUrl: str
        :param _Code: 状态码
        :type Code: int
        :param _Api: Api
        :type Api: str
        :param _Ip: 解析的IP
        :type Ip: str
        :param _Ssl: 证书信息
        :type Ssl: str
        :param _SslExpiredTime: ssl证书过期时间
        :type SslExpiredTime: str
        :param _SourceType: 来源类型
        :type SourceType: str
        :param _SourceValue: 来源值
        :type SourceValue: str
        :param _Trusted: 是否信任
        :type Trusted: bool
        :param _Owner: 所属者
        :type Owner: str
        :param _RootDomain: 根域名
        :type RootDomain: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Url = None
        self._Title = None
        self._ContentLength = None
        self._Content = None
        self._ScreenshotThumbUrl = None
        self._ScreenshotUrl = None
        self._Code = None
        self._Api = None
        self._Ip = None
        self._Ssl = None
        self._SslExpiredTime = None
        self._SourceType = None
        self._SourceValue = None
        self._Trusted = None
        self._Owner = None
        self._RootDomain = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Url(self):
        """Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Title(self):
        """标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ContentLength(self):
        """报文长度
        :rtype: int
        """
        return self._ContentLength

    @ContentLength.setter
    def ContentLength(self, ContentLength):
        self._ContentLength = ContentLength

    @property
    def Content(self):
        """报文内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ScreenshotThumbUrl(self):
        """截图缩略图URL
        :rtype: str
        """
        return self._ScreenshotThumbUrl

    @ScreenshotThumbUrl.setter
    def ScreenshotThumbUrl(self, ScreenshotThumbUrl):
        self._ScreenshotThumbUrl = ScreenshotThumbUrl

    @property
    def ScreenshotUrl(self):
        """截图URL
        :rtype: str
        """
        return self._ScreenshotUrl

    @ScreenshotUrl.setter
    def ScreenshotUrl(self, ScreenshotUrl):
        self._ScreenshotUrl = ScreenshotUrl

    @property
    def Code(self):
        """状态码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Api(self):
        """Api
        :rtype: str
        """
        return self._Api

    @Api.setter
    def Api(self, Api):
        self._Api = Api

    @property
    def Ip(self):
        """解析的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Ssl(self):
        """证书信息
        :rtype: str
        """
        return self._Ssl

    @Ssl.setter
    def Ssl(self, Ssl):
        self._Ssl = Ssl

    @property
    def SslExpiredTime(self):
        """ssl证书过期时间
        :rtype: str
        """
        return self._SslExpiredTime

    @SslExpiredTime.setter
    def SslExpiredTime(self, SslExpiredTime):
        self._SslExpiredTime = SslExpiredTime

    @property
    def SourceType(self):
        """来源类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceValue(self):
        """来源值
        :rtype: str
        """
        return self._SourceValue

    @SourceValue.setter
    def SourceValue(self, SourceValue):
        self._SourceValue = SourceValue

    @property
    def Trusted(self):
        """是否信任
        :rtype: bool
        """
        return self._Trusted

    @Trusted.setter
    def Trusted(self, Trusted):
        self._Trusted = Trusted

    @property
    def Owner(self):
        """所属者
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def RootDomain(self):
        """根域名
        :rtype: str
        """
        return self._RootDomain

    @RootDomain.setter
    def RootDomain(self, RootDomain):
        self._RootDomain = RootDomain


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Url = params.get("Url")
        self._Title = params.get("Title")
        self._ContentLength = params.get("ContentLength")
        self._Content = params.get("Content")
        self._ScreenshotThumbUrl = params.get("ScreenshotThumbUrl")
        self._ScreenshotUrl = params.get("ScreenshotUrl")
        self._Code = params.get("Code")
        self._Api = params.get("Api")
        self._Ip = params.get("Ip")
        self._Ssl = params.get("Ssl")
        self._SslExpiredTime = params.get("SslExpiredTime")
        self._SourceType = params.get("SourceType")
        self._SourceValue = params.get("SourceValue")
        self._Trusted = params.get("Trusted")
        self._Owner = params.get("Owner")
        self._RootDomain = params.get("RootDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayToolCommon(AbstractModel):
    """数据管理公共字段

    """

    def __init__(self):
        r"""
        :param _EnterpriseUid: 子公司ID
        :type EnterpriseUid: str
        :param _EnterpriseName: 子公司名称
        :type EnterpriseName: str
        :param _JobId: 主任务ID
        :type JobId: int
        :param _JobStageId: 单任务ID
        :type JobStageId: int
        :param _Ignored: 是否忽略
        :type Ignored: bool
        :param _JobRecordId: 子任务ID
        :type JobRecordId: int
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _CustomerName: 企业名称
        :type CustomerName: str
        :param _Detail: 详情
        :type Detail: str
        :param _Md5: Md5值
        :type Md5: str
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 更新时间
        :type UpdateAt: str
        :param _Labels: 标签列表，json格式：{\"tag1\":[\"责任人xxx\"],\"tag2\":[\"测试站\"]}
        :type Labels: str
        """
        self._EnterpriseUid = None
        self._EnterpriseName = None
        self._JobId = None
        self._JobStageId = None
        self._Ignored = None
        self._JobRecordId = None
        self._CustomerId = None
        self._CustomerName = None
        self._Detail = None
        self._Md5 = None
        self._CreateAt = None
        self._UpdateAt = None
        self._Labels = None

    @property
    def EnterpriseUid(self):
        """子公司ID
        :rtype: str
        """
        return self._EnterpriseUid

    @EnterpriseUid.setter
    def EnterpriseUid(self, EnterpriseUid):
        self._EnterpriseUid = EnterpriseUid

    @property
    def EnterpriseName(self):
        """子公司名称
        :rtype: str
        """
        return self._EnterpriseName

    @EnterpriseName.setter
    def EnterpriseName(self, EnterpriseName):
        self._EnterpriseName = EnterpriseName

    @property
    def JobId(self):
        """主任务ID
        :rtype: int
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobStageId(self):
        """单任务ID
        :rtype: int
        """
        return self._JobStageId

    @JobStageId.setter
    def JobStageId(self, JobStageId):
        self._JobStageId = JobStageId

    @property
    def Ignored(self):
        """是否忽略
        :rtype: bool
        """
        return self._Ignored

    @Ignored.setter
    def Ignored(self, Ignored):
        self._Ignored = Ignored

    @property
    def JobRecordId(self):
        """子任务ID
        :rtype: int
        """
        return self._JobRecordId

    @JobRecordId.setter
    def JobRecordId(self, JobRecordId):
        self._JobRecordId = JobRecordId

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """企业名称
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def Detail(self):
        """详情
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Md5(self):
        """Md5值
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def CreateAt(self):
        """创建时间
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def Labels(self):
        """标签列表，json格式：{\"tag1\":[\"责任人xxx\"],\"tag2\":[\"测试站\"]}
        :rtype: str
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._EnterpriseUid = params.get("EnterpriseUid")
        self._EnterpriseName = params.get("EnterpriseName")
        self._JobId = params.get("JobId")
        self._JobStageId = params.get("JobStageId")
        self._Ignored = params.get("Ignored")
        self._JobRecordId = params.get("JobRecordId")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._Detail = params.get("Detail")
        self._Md5 = params.get("Md5")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._Labels = params.get("Labels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayVul(AbstractModel):
    """漏洞详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Ip: 解析的IP
        :type Ip: str
        :param _Port: 端口
        :type Port: int
        :param _Url: Url地址
        :type Url: str
        :param _Level: 风险等级：1：提示, 2:低危, 3:中危, 4:高危, 5: 严重
        :type Level: int
        :param _Name: 漏洞名称
        :type Name: str
        :param _RepairStatus: 是否修复，0:未修复，1:已修复
        :type RepairStatus: int
        :param _Suggestion: 建议
        :type Suggestion: str
        :param _DiscoverTime: 发现时间
        :type DiscoverTime: str
        :param _AiJudge: AI研判
        :type AiJudge: str
        :param _Status: 状态：unrepaired:未修复，repaired:已修复, offline:资产已下线, ignore:已忽略
        :type Status: str
        :param _LastCheckTime: 上次复测时间
        :type LastCheckTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Ip = None
        self._Port = None
        self._Url = None
        self._Level = None
        self._Name = None
        self._RepairStatus = None
        self._Suggestion = None
        self._DiscoverTime = None
        self._AiJudge = None
        self._Status = None
        self._LastCheckTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Ip(self):
        """解析的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Url(self):
        """Url地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Level(self):
        """风险等级：1：提示, 2:低危, 3:中危, 4:高危, 5: 严重
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Name(self):
        """漏洞名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RepairStatus(self):
        """是否修复，0:未修复，1:已修复
        :rtype: int
        """
        return self._RepairStatus

    @RepairStatus.setter
    def RepairStatus(self, RepairStatus):
        self._RepairStatus = RepairStatus

    @property
    def Suggestion(self):
        """建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def DiscoverTime(self):
        """发现时间
        :rtype: str
        """
        return self._DiscoverTime

    @DiscoverTime.setter
    def DiscoverTime(self, DiscoverTime):
        self._DiscoverTime = DiscoverTime

    @property
    def AiJudge(self):
        """AI研判
        :rtype: str
        """
        return self._AiJudge

    @AiJudge.setter
    def AiJudge(self, AiJudge):
        self._AiJudge = AiJudge

    @property
    def Status(self):
        """状态：unrepaired:未修复，repaired:已修复, offline:资产已下线, ignore:已忽略
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastCheckTime(self):
        """上次复测时间
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Url = params.get("Url")
        self._Level = params.get("Level")
        self._Name = params.get("Name")
        self._RepairStatus = params.get("RepairStatus")
        self._Suggestion = params.get("Suggestion")
        self._DiscoverTime = params.get("DiscoverTime")
        self._AiJudge = params.get("AiJudge")
        self._Status = params.get("Status")
        self._LastCheckTime = params.get("LastCheckTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayWeakPassword(AbstractModel):
    """弱口令详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Ip: 解析的IP
        :type Ip: str
        :param _Port: 端口
        :type Port: int
        :param _Url: Url地址
        :type Url: str
        :param _Type: 弱口令类型
        :type Type: str
        :param _Account: 弱口令账号
        :type Account: str
        :param _Password: 弱口令密码
        :type Password: str
        :param _IsHoneypot: 是否蜜罐
        :type IsHoneypot: bool
        :param _ScreenshotUrl: 截图
        :type ScreenshotUrl: str
        :param _Status: 状态：unrepaired:未修复，repaired:已修复, offline:资产已下线, ignore:已忽略, checking:复测中
        :type Status: str
        :param _LastCheckTime: 上次复测时间
        :type LastCheckTime: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Ip = None
        self._Port = None
        self._Url = None
        self._Type = None
        self._Account = None
        self._Password = None
        self._IsHoneypot = None
        self._ScreenshotUrl = None
        self._Status = None
        self._LastCheckTime = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Ip(self):
        """解析的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Url(self):
        """Url地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        """弱口令类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Account(self):
        """弱口令账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Password(self):
        """弱口令密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsHoneypot(self):
        """是否蜜罐
        :rtype: bool
        """
        return self._IsHoneypot

    @IsHoneypot.setter
    def IsHoneypot(self, IsHoneypot):
        self._IsHoneypot = IsHoneypot

    @property
    def ScreenshotUrl(self):
        """截图
        :rtype: str
        """
        return self._ScreenshotUrl

    @ScreenshotUrl.setter
    def ScreenshotUrl(self, ScreenshotUrl):
        self._ScreenshotUrl = ScreenshotUrl

    @property
    def Status(self):
        """状态：unrepaired:未修复，repaired:已修复, offline:资产已下线, ignore:已忽略, checking:复测中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastCheckTime(self):
        """上次复测时间
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        self._Account = params.get("Account")
        self._Password = params.get("Password")
        self._IsHoneypot = params.get("IsHoneypot")
        self._ScreenshotUrl = params.get("ScreenshotUrl")
        self._Status = params.get("Status")
        self._LastCheckTime = params.get("LastCheckTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayWechatApplet(AbstractModel):
    """微信小程序详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Name: 名称
        :type Name: str
        :param _Logo: 图片地址
        :type Logo: str
        :param _AccountId: 账号
        :type AccountId: str
        :param _QrCode: 二维码
        :type QrCode: str
        :param _Description: 描述
        :type Description: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Name = None
        self._Logo = None
        self._AccountId = None
        self._QrCode = None
        self._Description = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Logo(self):
        """图片地址
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def AccountId(self):
        """账号
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def QrCode(self):
        """二维码
        :rtype: str
        """
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Name = params.get("Name")
        self._Logo = params.get("Logo")
        self._AccountId = params.get("AccountId")
        self._QrCode = params.get("QrCode")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisplayWechatOfficialAccount(AbstractModel):
    """微信公众号详情

    """

    def __init__(self):
        r"""
        :param _Id: 主键ID
        :type Id: int
        :param _DisplayToolCommon: 公共字段
        :type DisplayToolCommon: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        :param _Name: 名称
        :type Name: str
        :param _Logo: 图片地址
        :type Logo: str
        :param _AccountId: 账号
        :type AccountId: str
        :param _QrCode: 二维码
        :type QrCode: str
        :param _Description: 描述
        :type Description: str
        """
        self._Id = None
        self._DisplayToolCommon = None
        self._Name = None
        self._Logo = None
        self._AccountId = None
        self._QrCode = None
        self._Description = None

    @property
    def Id(self):
        """主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DisplayToolCommon(self):
        """公共字段
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DisplayToolCommon`
        """
        return self._DisplayToolCommon

    @DisplayToolCommon.setter
    def DisplayToolCommon(self, DisplayToolCommon):
        self._DisplayToolCommon = DisplayToolCommon

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Logo(self):
        """图片地址
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def AccountId(self):
        """账号
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def QrCode(self):
        """二维码
        :rtype: str
        """
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("DisplayToolCommon") is not None:
            self._DisplayToolCommon = DisplayToolCommon()
            self._DisplayToolCommon._deserialize(params.get("DisplayToolCommon"))
        self._Name = params.get("Name")
        self._Logo = params.get("Logo")
        self._AccountId = params.get("AccountId")
        self._QrCode = params.get("QrCode")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """支持按照各字段过滤

    """

    def __init__(self):
        r"""
        :param _Name: 要搜索的字段
        :type Name: str
        :param _Values: 目标值列表
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """要搜索的字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """目标值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdndValue(AbstractModel):
    """链路详情扫描目标和ID

    """

    def __init__(self):
        r"""
        :param _Id: 详情ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Value: 目标
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Id = None
        self._Value = None

    @property
    def Id(self):
        """详情ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Value(self):
        """目标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobRecordProgress(AbstractModel):
    """子任务进度

    """

    def __init__(self):
        r"""
        :param _Doing: 正在执行的任务数
        :type Doing: int
        :param _Done: 已完成的任务数
        :type Done: int
        :param _Error: 发生错误的任务数
        :type Error: int
        :param _Timeout: 超时
        :type Timeout: int
        :param _Stop: 停止
        :type Stop: int
        :param _Todo: 暂停
        :type Todo: int
        """
        self._Doing = None
        self._Done = None
        self._Error = None
        self._Timeout = None
        self._Stop = None
        self._Todo = None

    @property
    def Doing(self):
        """正在执行的任务数
        :rtype: int
        """
        return self._Doing

    @Doing.setter
    def Doing(self, Doing):
        self._Doing = Doing

    @property
    def Done(self):
        """已完成的任务数
        :rtype: int
        """
        return self._Done

    @Done.setter
    def Done(self, Done):
        self._Done = Done

    @property
    def Error(self):
        """发生错误的任务数
        :rtype: int
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Timeout(self):
        """超时
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Stop(self):
        """停止
        :rtype: int
        """
        return self._Stop

    @Stop.setter
    def Stop(self, Stop):
        self._Stop = Stop

    @property
    def Todo(self):
        """暂停
        :rtype: int
        """
        return self._Todo

    @Todo.setter
    def Todo(self, Todo):
        self._Todo = Todo


    def _deserialize(self, params):
        self._Doing = params.get("Doing")
        self._Done = params.get("Done")
        self._Error = params.get("Error")
        self._Timeout = params.get("Timeout")
        self._Stop = params.get("Stop")
        self._Todo = params.get("Todo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerRequest(AbstractModel):
    """ModifyCustomer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 企业名称
        :type Name: str
        :param _Percent: 百分比取值范围为30-100
        :type Percent: int
        :param _ScanType: 资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :type ScanType: str
        :param _Id: 企业ID
        :type Id: int
        :param _ScanCron: 周期测绘时间
        :type ScanCron: str
        :param _IsScanNow: 是否立即启动
        :type IsScanNow: bool
        :param _EnableCron: 是否启用周期测绘
        :type EnableCron: bool
        :param _EnableScanSubEnterprise: 是否扫描子公司
        :type EnableScanSubEnterprise: bool
        :param _EnableAuth: 是否授权
        :type EnableAuth: bool
        :param _AuthStartAt: 授权开始时间
        :type AuthStartAt: str
        :param _AuthEndAt: 授权结束时间
        :type AuthEndAt: str
        :param _AuthFile: 授权文件id
        :type AuthFile: str
        :param _ScanTime: 测绘时间配置项，采用json字符串格式
        :type ScanTime: str
        :param _Icon: 企业图标
        :type Icon: str
        :param _Qps: 并发
        :type Qps: int
        :param _SubCompanyLevel: 子公司拓展层次
        :type SubCompanyLevel: int
        :param _IsIncludeFullScan: 是否包含完整的扫描
        :type IsIncludeFullScan: bool
        """
        self._Name = None
        self._Percent = None
        self._ScanType = None
        self._Id = None
        self._ScanCron = None
        self._IsScanNow = None
        self._EnableCron = None
        self._EnableScanSubEnterprise = None
        self._EnableAuth = None
        self._AuthStartAt = None
        self._AuthEndAt = None
        self._AuthFile = None
        self._ScanTime = None
        self._Icon = None
        self._Qps = None
        self._SubCompanyLevel = None
        self._IsIncludeFullScan = None

    @property
    def Name(self):
        """企业名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Percent(self):
        """百分比取值范围为30-100
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanType(self):
        """资产收集、漏洞信息、弱口令、目录爆破、暗网泄露、Github泄露、文库网盘泄露、敏感信息泄露，其中资产收集必包含，多个用英文逗号隔离，例如：资产收集,漏洞信息
        :rtype: str
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType

    @property
    def Id(self):
        """企业ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ScanCron(self):
        """周期测绘时间
        :rtype: str
        """
        return self._ScanCron

    @ScanCron.setter
    def ScanCron(self, ScanCron):
        self._ScanCron = ScanCron

    @property
    def IsScanNow(self):
        """是否立即启动
        :rtype: bool
        """
        return self._IsScanNow

    @IsScanNow.setter
    def IsScanNow(self, IsScanNow):
        self._IsScanNow = IsScanNow

    @property
    def EnableCron(self):
        """是否启用周期测绘
        :rtype: bool
        """
        return self._EnableCron

    @EnableCron.setter
    def EnableCron(self, EnableCron):
        self._EnableCron = EnableCron

    @property
    def EnableScanSubEnterprise(self):
        """是否扫描子公司
        :rtype: bool
        """
        return self._EnableScanSubEnterprise

    @EnableScanSubEnterprise.setter
    def EnableScanSubEnterprise(self, EnableScanSubEnterprise):
        self._EnableScanSubEnterprise = EnableScanSubEnterprise

    @property
    def EnableAuth(self):
        """是否授权
        :rtype: bool
        """
        return self._EnableAuth

    @EnableAuth.setter
    def EnableAuth(self, EnableAuth):
        self._EnableAuth = EnableAuth

    @property
    def AuthStartAt(self):
        """授权开始时间
        :rtype: str
        """
        return self._AuthStartAt

    @AuthStartAt.setter
    def AuthStartAt(self, AuthStartAt):
        self._AuthStartAt = AuthStartAt

    @property
    def AuthEndAt(self):
        """授权结束时间
        :rtype: str
        """
        return self._AuthEndAt

    @AuthEndAt.setter
    def AuthEndAt(self, AuthEndAt):
        self._AuthEndAt = AuthEndAt

    @property
    def AuthFile(self):
        """授权文件id
        :rtype: str
        """
        return self._AuthFile

    @AuthFile.setter
    def AuthFile(self, AuthFile):
        self._AuthFile = AuthFile

    @property
    def ScanTime(self):
        """测绘时间配置项，采用json字符串格式
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def Icon(self):
        """企业图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Qps(self):
        """并发
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def SubCompanyLevel(self):
        """子公司拓展层次
        :rtype: int
        """
        return self._SubCompanyLevel

    @SubCompanyLevel.setter
    def SubCompanyLevel(self, SubCompanyLevel):
        self._SubCompanyLevel = SubCompanyLevel

    @property
    def IsIncludeFullScan(self):
        """是否包含完整的扫描
        :rtype: bool
        """
        return self._IsIncludeFullScan

    @IsIncludeFullScan.setter
    def IsIncludeFullScan(self, IsIncludeFullScan):
        self._IsIncludeFullScan = IsIncludeFullScan


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Percent = params.get("Percent")
        self._ScanType = params.get("ScanType")
        self._Id = params.get("Id")
        self._ScanCron = params.get("ScanCron")
        self._IsScanNow = params.get("IsScanNow")
        self._EnableCron = params.get("EnableCron")
        self._EnableScanSubEnterprise = params.get("EnableScanSubEnterprise")
        self._EnableAuth = params.get("EnableAuth")
        self._AuthStartAt = params.get("AuthStartAt")
        self._AuthEndAt = params.get("AuthEndAt")
        self._AuthFile = params.get("AuthFile")
        self._ScanTime = params.get("ScanTime")
        self._Icon = params.get("Icon")
        self._Qps = params.get("Qps")
        self._SubCompanyLevel = params.get("SubCompanyLevel")
        self._IsIncludeFullScan = params.get("IsIncludeFullScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerResponse(AbstractModel):
    """ModifyCustomer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 企业ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """企业ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class StopJobRecordRequest(AbstractModel):
    """StopJobRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerId: 企业ID
        :type CustomerId: int
        :param _JobRecordId: 任务ID
        :type JobRecordId: int
        """
        self._CustomerId = None
        self._JobRecordId = None

    @property
    def CustomerId(self):
        """企业ID
        :rtype: int
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def JobRecordId(self):
        """任务ID
        :rtype: int
        """
        return self._JobRecordId

    @JobRecordId.setter
    def JobRecordId(self, JobRecordId):
        self._JobRecordId = JobRecordId


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._JobRecordId = params.get("JobRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobRecordResponse(AbstractModel):
    """StopJobRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")