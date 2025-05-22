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


class AKSKLeak(AbstractModel):
    """AKSK泄漏信息

    """

    def __init__(self):
        r"""
        :param _AK: AK编码
        :type AK: str
        :param _SK: SK编码
        :type SK: str
        :param _URL: URL编码
        :type URL: str
        """
        self._AK = None
        self._SK = None
        self._URL = None

    @property
    def AK(self):
        """AK编码
        :rtype: str
        """
        return self._AK

    @AK.setter
    def AK(self, AK):
        self._AK = AK

    @property
    def SK(self):
        """SK编码
        :rtype: str
        """
        return self._SK

    @SK.setter
    def SK(self, SK):
        self._SK = SK

    @property
    def URL(self):
        """URL编码
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL


    def _deserialize(self, params):
        self._AK = params.get("AK")
        self._SK = params.get("SK")
        self._URL = params.get("URL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountRisk(AbstractModel):
    """账户风险

    """

    def __init__(self):
        r"""
        :param _Id: id（可不参考）
        :type Id: str
        :param _RiskAccount: 风险账户
        :type RiskAccount: str
        """
        self._Id = None
        self._RiskAccount = None

    @property
    def Id(self):
        """id（可不参考）
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RiskAccount(self):
        """风险账户
        :rtype: str
        """
        return self._RiskAccount

    @RiskAccount.setter
    def RiskAccount(self, RiskAccount):
        self._RiskAccount = RiskAccount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RiskAccount = params.get("RiskAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessmentControlItem(AbstractModel):
    """DSPA评估控制项

    """

    def __init__(self):
        r"""
        :param _ItemId: 评估项Id
        :type ItemId: str
        :param _ItemName: 评估项名称
        :type ItemName: str
        :param _Description: 评估项描述
        :type Description: str
        :param _Source: 评估项来源，内置/用户自定，取值（system，user）
        :type Source: str
        :param _ItemType: 评估项类型，问卷/自动化，取值（questionnaire，auto）
        :type ItemType: str
        :param _ItemSubType: 评估项子类型，单选/多选/时间/文本/AKSK等，取值（singlechoice，multichoice，date，text，AKSK……等）
        :type ItemSubType: str
        :param _CreatedTime: 评估项创建时间
        :type CreatedTime: str
        :param _Status: 评估项启用状态，启用/未启用，取值draft / launched
        :type Status: str
        :param _TemplateCount: 评估项关联的模板数量
        :type TemplateCount: int
        """
        self._ItemId = None
        self._ItemName = None
        self._Description = None
        self._Source = None
        self._ItemType = None
        self._ItemSubType = None
        self._CreatedTime = None
        self._Status = None
        self._TemplateCount = None

    @property
    def ItemId(self):
        """评估项Id
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemName(self):
        """评估项名称
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def Description(self):
        """评估项描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        """评估项来源，内置/用户自定，取值（system，user）
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def ItemType(self):
        """评估项类型，问卷/自动化，取值（questionnaire，auto）
        :rtype: str
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def ItemSubType(self):
        """评估项子类型，单选/多选/时间/文本/AKSK等，取值（singlechoice，multichoice，date，text，AKSK……等）
        :rtype: str
        """
        return self._ItemSubType

    @ItemSubType.setter
    def ItemSubType(self, ItemSubType):
        self._ItemSubType = ItemSubType

    @property
    def CreatedTime(self):
        """评估项创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Status(self):
        """评估项启用状态，启用/未启用，取值draft / launched
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TemplateCount(self):
        """评估项关联的模板数量
        :rtype: int
        """
        return self._TemplateCount

    @TemplateCount.setter
    def TemplateCount(self, TemplateCount):
        self._TemplateCount = TemplateCount


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemName = params.get("ItemName")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._ItemType = params.get("ItemType")
        self._ItemSubType = params.get("ItemSubType")
        self._CreatedTime = params.get("CreatedTime")
        self._Status = params.get("Status")
        self._TemplateCount = params.get("TemplateCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessmentRisk(AbstractModel):
    """DSPA评估风险项

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险项Id
        :type RiskId: str
        :param _RiskDescription: 风险项描述
        :type RiskDescription: str
        :param _TemplateId: 评估模板Id
        :type TemplateId: str
        :param _TemplateName: 评估模板名称
        :type TemplateName: str
        :param _ControlItemId: 评估项Id
        :type ControlItemId: str
        :param _ControlItemName: 评估项名称
        :type ControlItemName: str
        :param _ControlItemDesc: 评估描述
        :type ControlItemDesc: str
        :param _RiskLevel: 风险等级，取值（high，medium，low）
        :type RiskLevel: str
        :param _RiskMitigation: 风险缓解措施
        :type RiskMitigation: str
        :param _Status: 风险处理状态。(waiting待处理, processing处理中, finished已处理)
        :type Status: str
        :param _CreatedTime: 风险生成时间
        :type CreatedTime: str
        :param _RiskOwner: 风险负责人
        :type RiskOwner: str
        :param _RelatedAsset: 风险涉及资产
        :type RelatedAsset: str
        :param _DataSourceId: 风险涉及资产id
        :type DataSourceId: str
        :param _DataSourceName: 风险涉及资产名称
        :type DataSourceName: str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _SecurityProduct: 建议使用安全产品
        :type SecurityProduct: list of SecurityProduct
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _RiskSide: 风险面
        :type RiskSide: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        """
        self._RiskId = None
        self._RiskDescription = None
        self._TemplateId = None
        self._TemplateName = None
        self._ControlItemId = None
        self._ControlItemName = None
        self._ControlItemDesc = None
        self._RiskLevel = None
        self._RiskMitigation = None
        self._Status = None
        self._CreatedTime = None
        self._RiskOwner = None
        self._RelatedAsset = None
        self._DataSourceId = None
        self._DataSourceName = None
        self._AssetName = None
        self._SecurityProduct = None
        self._RiskType = None
        self._RiskSide = None
        self._DataSourceType = None

    @property
    def RiskId(self):
        """风险项Id
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def RiskDescription(self):
        """风险项描述
        :rtype: str
        """
        return self._RiskDescription

    @RiskDescription.setter
    def RiskDescription(self, RiskDescription):
        self._RiskDescription = RiskDescription

    @property
    def TemplateId(self):
        """评估模板Id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """评估模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def ControlItemId(self):
        """评估项Id
        :rtype: str
        """
        return self._ControlItemId

    @ControlItemId.setter
    def ControlItemId(self, ControlItemId):
        self._ControlItemId = ControlItemId

    @property
    def ControlItemName(self):
        """评估项名称
        :rtype: str
        """
        return self._ControlItemName

    @ControlItemName.setter
    def ControlItemName(self, ControlItemName):
        self._ControlItemName = ControlItemName

    @property
    def ControlItemDesc(self):
        """评估描述
        :rtype: str
        """
        return self._ControlItemDesc

    @ControlItemDesc.setter
    def ControlItemDesc(self, ControlItemDesc):
        self._ControlItemDesc = ControlItemDesc

    @property
    def RiskLevel(self):
        """风险等级，取值（high，medium，low）
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskMitigation(self):
        """风险缓解措施
        :rtype: str
        """
        return self._RiskMitigation

    @RiskMitigation.setter
    def RiskMitigation(self, RiskMitigation):
        self._RiskMitigation = RiskMitigation

    @property
    def Status(self):
        """风险处理状态。(waiting待处理, processing处理中, finished已处理)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        """风险生成时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def RiskOwner(self):
        """风险负责人
        :rtype: str
        """
        return self._RiskOwner

    @RiskOwner.setter
    def RiskOwner(self, RiskOwner):
        self._RiskOwner = RiskOwner

    @property
    def RelatedAsset(self):
        """风险涉及资产
        :rtype: str
        """
        return self._RelatedAsset

    @RelatedAsset.setter
    def RelatedAsset(self, RelatedAsset):
        self._RelatedAsset = RelatedAsset

    @property
    def DataSourceId(self):
        """风险涉及资产id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceName(self):
        """风险涉及资产名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def AssetName(self):
        """资产名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def SecurityProduct(self):
        """建议使用安全产品
        :rtype: list of SecurityProduct
        """
        return self._SecurityProduct

    @SecurityProduct.setter
    def SecurityProduct(self, SecurityProduct):
        self._SecurityProduct = SecurityProduct

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def RiskSide(self):
        """风险面
        :rtype: str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._RiskDescription = params.get("RiskDescription")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._ControlItemId = params.get("ControlItemId")
        self._ControlItemName = params.get("ControlItemName")
        self._ControlItemDesc = params.get("ControlItemDesc")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskMitigation = params.get("RiskMitigation")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._RiskOwner = params.get("RiskOwner")
        self._RelatedAsset = params.get("RelatedAsset")
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceName = params.get("DataSourceName")
        self._AssetName = params.get("AssetName")
        if params.get("SecurityProduct") is not None:
            self._SecurityProduct = []
            for item in params.get("SecurityProduct"):
                obj = SecurityProduct()
                obj._deserialize(item)
                self._SecurityProduct.append(obj)
        self._RiskType = params.get("RiskType")
        self._RiskSide = params.get("RiskSide")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessmentRiskItem(AbstractModel):
    """风险项列表详细数据

    """

    def __init__(self):
        r"""
        :param _Id: 脆弱项id
        :type Id: int
        :param _RiskName: 名称
        :type RiskName: str
        :param _Level: 脆弱性级别
        :type Level: str
        :param _Description: 说明
        :type Description: str
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _ReferTemplateCount: 关联模板个数
        :type ReferTemplateCount: int
        :param _SupportDataSource: 支持的数据源
        :type SupportDataSource: list of str
        :param _RiskSide: 风险面
        :type RiskSide: str
        :param _ReferTemplateList: 关联模板列表
        :type ReferTemplateList: list of TemplateInfo
        """
        self._Id = None
        self._RiskName = None
        self._Level = None
        self._Description = None
        self._RiskType = None
        self._ReferTemplateCount = None
        self._SupportDataSource = None
        self._RiskSide = None
        self._ReferTemplateList = None

    @property
    def Id(self):
        """脆弱项id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RiskName(self):
        """名称
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def Level(self):
        """脆弱性级别
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Description(self):
        """说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def ReferTemplateCount(self):
        """关联模板个数
        :rtype: int
        """
        return self._ReferTemplateCount

    @ReferTemplateCount.setter
    def ReferTemplateCount(self, ReferTemplateCount):
        self._ReferTemplateCount = ReferTemplateCount

    @property
    def SupportDataSource(self):
        """支持的数据源
        :rtype: list of str
        """
        return self._SupportDataSource

    @SupportDataSource.setter
    def SupportDataSource(self, SupportDataSource):
        self._SupportDataSource = SupportDataSource

    @property
    def RiskSide(self):
        """风险面
        :rtype: str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide

    @property
    def ReferTemplateList(self):
        """关联模板列表
        :rtype: list of TemplateInfo
        """
        return self._ReferTemplateList

    @ReferTemplateList.setter
    def ReferTemplateList(self, ReferTemplateList):
        self._ReferTemplateList = ReferTemplateList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RiskName = params.get("RiskName")
        self._Level = params.get("Level")
        self._Description = params.get("Description")
        self._RiskType = params.get("RiskType")
        self._ReferTemplateCount = params.get("ReferTemplateCount")
        self._SupportDataSource = params.get("SupportDataSource")
        self._RiskSide = params.get("RiskSide")
        if params.get("ReferTemplateList") is not None:
            self._ReferTemplateList = []
            for item in params.get("ReferTemplateList"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self._ReferTemplateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessmentTask(AbstractModel):
    """DSPA评估任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 评估任务Id
        :type TaskId: str
        :param _TaskUid: 评估任务的自增ID

        :type TaskUid: int
        :param _TaskName: 评估任务名称
        :type TaskName: str
        :param _BusinessName: 业务名称
        :type BusinessName: str
        :param _BusinessDept: 业务所属部门
        :type BusinessDept: str
        :param _BusinessOwner: 业务负责人
        :type BusinessOwner: str
        :param _TemplateId: 评估模板Id
        :type TemplateId: str
        :param _TemplateName: 评估模板名称
        :type TemplateName: str
        :param _ComplianceGroupId: 分类分级模板Id
        :type ComplianceGroupId: int
        :param _ComplianceGroupName: 分类分级模板名称
        :type ComplianceGroupName: str
        :param _ControlItemCount: 评估项数量
        :type ControlItemCount: int
        :param _RiskCount: 风险项数量（仅状态为finished的风险项不计入总数，其余状态均算入该数量）
        :type RiskCount: int
        :param _FinishedTime: 评估任务完成时间
        :type FinishedTime: str
        :param _CreatedTime: 评估任务发起时间
        :type CreatedTime: str
        :param _Status: 评估状态。(waiting待评估，processing评估中, , finished已评估, failed评估失败)
        :type Status: str
        :param _RiskCountInfoList: 待处理各等级风险项信息
        :type RiskCountInfoList: list of RiskCountInfo
        :param _DiscoveryCondition: 数据源信息
        :type DiscoveryCondition: :class:`tencentcloud.dsgc.v20190723.models.DiscoveryCondition`
        :param _ErrorInfo: 评估任务失败信息
        :type ErrorInfo: str
        :param _TemplateUid: 模板主键id
        :type TemplateUid: int
        :param _ProgressPercent: 进度百分比
        :type ProgressPercent: int
        """
        self._TaskId = None
        self._TaskUid = None
        self._TaskName = None
        self._BusinessName = None
        self._BusinessDept = None
        self._BusinessOwner = None
        self._TemplateId = None
        self._TemplateName = None
        self._ComplianceGroupId = None
        self._ComplianceGroupName = None
        self._ControlItemCount = None
        self._RiskCount = None
        self._FinishedTime = None
        self._CreatedTime = None
        self._Status = None
        self._RiskCountInfoList = None
        self._DiscoveryCondition = None
        self._ErrorInfo = None
        self._TemplateUid = None
        self._ProgressPercent = None

    @property
    def TaskId(self):
        """评估任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskUid(self):
        """评估任务的自增ID

        :rtype: int
        """
        return self._TaskUid

    @TaskUid.setter
    def TaskUid(self, TaskUid):
        self._TaskUid = TaskUid

    @property
    def TaskName(self):
        """评估任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def BusinessName(self):
        """业务名称
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def BusinessDept(self):
        """业务所属部门
        :rtype: str
        """
        return self._BusinessDept

    @BusinessDept.setter
    def BusinessDept(self, BusinessDept):
        self._BusinessDept = BusinessDept

    @property
    def BusinessOwner(self):
        """业务负责人
        :rtype: str
        """
        return self._BusinessOwner

    @BusinessOwner.setter
    def BusinessOwner(self, BusinessOwner):
        self._BusinessOwner = BusinessOwner

    @property
    def TemplateId(self):
        """评估模板Id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """评估模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def ComplianceGroupId(self):
        """分类分级模板Id
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def ComplianceGroupName(self):
        """分类分级模板名称
        :rtype: str
        """
        return self._ComplianceGroupName

    @ComplianceGroupName.setter
    def ComplianceGroupName(self, ComplianceGroupName):
        self._ComplianceGroupName = ComplianceGroupName

    @property
    def ControlItemCount(self):
        """评估项数量
        :rtype: int
        """
        return self._ControlItemCount

    @ControlItemCount.setter
    def ControlItemCount(self, ControlItemCount):
        self._ControlItemCount = ControlItemCount

    @property
    def RiskCount(self):
        """风险项数量（仅状态为finished的风险项不计入总数，其余状态均算入该数量）
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def FinishedTime(self):
        """评估任务完成时间
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def CreatedTime(self):
        """评估任务发起时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Status(self):
        """评估状态。(waiting待评估，processing评估中, , finished已评估, failed评估失败)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskCountInfoList(self):
        """待处理各等级风险项信息
        :rtype: list of RiskCountInfo
        """
        return self._RiskCountInfoList

    @RiskCountInfoList.setter
    def RiskCountInfoList(self, RiskCountInfoList):
        self._RiskCountInfoList = RiskCountInfoList

    @property
    def DiscoveryCondition(self):
        """数据源信息
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DiscoveryCondition`
        """
        return self._DiscoveryCondition

    @DiscoveryCondition.setter
    def DiscoveryCondition(self, DiscoveryCondition):
        self._DiscoveryCondition = DiscoveryCondition

    @property
    def ErrorInfo(self):
        """评估任务失败信息
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def TemplateUid(self):
        """模板主键id
        :rtype: int
        """
        return self._TemplateUid

    @TemplateUid.setter
    def TemplateUid(self, TemplateUid):
        self._TemplateUid = TemplateUid

    @property
    def ProgressPercent(self):
        """进度百分比
        :rtype: int
        """
        return self._ProgressPercent

    @ProgressPercent.setter
    def ProgressPercent(self, ProgressPercent):
        self._ProgressPercent = ProgressPercent


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskUid = params.get("TaskUid")
        self._TaskName = params.get("TaskName")
        self._BusinessName = params.get("BusinessName")
        self._BusinessDept = params.get("BusinessDept")
        self._BusinessOwner = params.get("BusinessOwner")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._ComplianceGroupName = params.get("ComplianceGroupName")
        self._ControlItemCount = params.get("ControlItemCount")
        self._RiskCount = params.get("RiskCount")
        self._FinishedTime = params.get("FinishedTime")
        self._CreatedTime = params.get("CreatedTime")
        self._Status = params.get("Status")
        if params.get("RiskCountInfoList") is not None:
            self._RiskCountInfoList = []
            for item in params.get("RiskCountInfoList"):
                obj = RiskCountInfo()
                obj._deserialize(item)
                self._RiskCountInfoList.append(obj)
        if params.get("DiscoveryCondition") is not None:
            self._DiscoveryCondition = DiscoveryCondition()
            self._DiscoveryCondition._deserialize(params.get("DiscoveryCondition"))
        self._ErrorInfo = params.get("ErrorInfo")
        self._TemplateUid = params.get("TemplateUid")
        self._ProgressPercent = params.get("ProgressPercent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessmentTemplate(AbstractModel):
    """DSPA评估模板

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _TemplateId: 评估模板Id
        :type TemplateId: str
        :param _TemplateName: 评估模板名称
        :type TemplateName: str
        :param _Description: 描述信息
        :type Description: str
        :param _Source: 模板来源，内置/用户自定，取值（system，user）
        :type Source: str
        :param _UseType: 模板类型，自动化/半自动化/问卷，取值（auto，semi-auto，law）等
        :type UseType: str
        :param _CreatedTime: 评估模板创建时间
        :type CreatedTime: str
        :param _ControlItemCount: 模板关联的评估项数量
        :type ControlItemCount: int
        :param _AppliedItemCount: 模板已启用的评估项数量
        :type AppliedItemCount: int
        :param _Status: 模板启用状态，草稿/已启用，取值draft / launched
        :type Status: str
        :param _SupportDataSource: 支持的数据源类型
        :type SupportDataSource: list of str
        :param _IsASMTemplate: 是否包含攻击面风险
        :type IsASMTemplate: bool
        :param _IdentifyComplianceId: 合规组id
        :type IdentifyComplianceId: int
        """
        self._Id = None
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._Source = None
        self._UseType = None
        self._CreatedTime = None
        self._ControlItemCount = None
        self._AppliedItemCount = None
        self._Status = None
        self._SupportDataSource = None
        self._IsASMTemplate = None
        self._IdentifyComplianceId = None

    @property
    def Id(self):
        """id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateId(self):
        """评估模板Id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """评估模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        """描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        """模板来源，内置/用户自定，取值（system，user）
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UseType(self):
        """模板类型，自动化/半自动化/问卷，取值（auto，semi-auto，law）等
        :rtype: str
        """
        return self._UseType

    @UseType.setter
    def UseType(self, UseType):
        self._UseType = UseType

    @property
    def CreatedTime(self):
        """评估模板创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ControlItemCount(self):
        """模板关联的评估项数量
        :rtype: int
        """
        return self._ControlItemCount

    @ControlItemCount.setter
    def ControlItemCount(self, ControlItemCount):
        self._ControlItemCount = ControlItemCount

    @property
    def AppliedItemCount(self):
        """模板已启用的评估项数量
        :rtype: int
        """
        return self._AppliedItemCount

    @AppliedItemCount.setter
    def AppliedItemCount(self, AppliedItemCount):
        self._AppliedItemCount = AppliedItemCount

    @property
    def Status(self):
        """模板启用状态，草稿/已启用，取值draft / launched
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SupportDataSource(self):
        """支持的数据源类型
        :rtype: list of str
        """
        return self._SupportDataSource

    @SupportDataSource.setter
    def SupportDataSource(self, SupportDataSource):
        self._SupportDataSource = SupportDataSource

    @property
    def IsASMTemplate(self):
        """是否包含攻击面风险
        :rtype: bool
        """
        return self._IsASMTemplate

    @IsASMTemplate.setter
    def IsASMTemplate(self, IsASMTemplate):
        self._IsASMTemplate = IsASMTemplate

    @property
    def IdentifyComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._IdentifyComplianceId

    @IdentifyComplianceId.setter
    def IdentifyComplianceId(self, IdentifyComplianceId):
        self._IdentifyComplianceId = IdentifyComplianceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._UseType = params.get("UseType")
        self._CreatedTime = params.get("CreatedTime")
        self._ControlItemCount = params.get("ControlItemCount")
        self._AppliedItemCount = params.get("AppliedItemCount")
        self._Status = params.get("Status")
        self._SupportDataSource = params.get("SupportDataSource")
        self._IsASMTemplate = params.get("IsASMTemplate")
        self._IdentifyComplianceId = params.get("IdentifyComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCosDetail(AbstractModel):
    """数据资产报告-cos的资产详情

    """

    def __init__(self):
        r"""
        :param _Bucket: 桶的名
        :type Bucket: str
        :param _DataType: 数据源类型
        :type DataType: str
        :param _FileNums: 文件的个数
        :type FileNums: int
        :param _SensitiveFileNums: 敏感的文件个数
        :type SensitiveFileNums: int
        :param _DistributionData: 敏感分布
        :type DistributionData: list of Note
        :param _MatchedNum: cos文件的敏感数据个数
        :type MatchedNum: int
        """
        self._Bucket = None
        self._DataType = None
        self._FileNums = None
        self._SensitiveFileNums = None
        self._DistributionData = None
        self._MatchedNum = None

    @property
    def Bucket(self):
        """桶的名
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def DataType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def FileNums(self):
        """文件的个数
        :rtype: int
        """
        return self._FileNums

    @FileNums.setter
    def FileNums(self, FileNums):
        self._FileNums = FileNums

    @property
    def SensitiveFileNums(self):
        """敏感的文件个数
        :rtype: int
        """
        return self._SensitiveFileNums

    @SensitiveFileNums.setter
    def SensitiveFileNums(self, SensitiveFileNums):
        self._SensitiveFileNums = SensitiveFileNums

    @property
    def DistributionData(self):
        """敏感分布
        :rtype: list of Note
        """
        return self._DistributionData

    @DistributionData.setter
    def DistributionData(self, DistributionData):
        self._DistributionData = DistributionData

    @property
    def MatchedNum(self):
        """cos文件的敏感数据个数
        :rtype: int
        """
        return self._MatchedNum

    @MatchedNum.setter
    def MatchedNum(self, MatchedNum):
        self._MatchedNum = MatchedNum


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._DataType = params.get("DataType")
        self._FileNums = params.get("FileNums")
        self._SensitiveFileNums = params.get("SensitiveFileNums")
        if params.get("DistributionData") is not None:
            self._DistributionData = []
            for item in params.get("DistributionData"):
                obj = Note()
                obj._deserialize(item)
                self._DistributionData.append(obj)
        self._MatchedNum = params.get("MatchedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDBDetail(AbstractModel):
    """RDB敏感资产详情列表

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DdName: 数据库名称
        :type DdName: str
        :param _DataType: 数据库类型
        :type DataType: str
        :param _TableNums: 表的数量
        :type TableNums: int
        :param _SensitiveTableNums: 敏感表数量
        :type SensitiveTableNums: int
        :param _FieldNums: 字段的数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感字段的数量
        :type SensitiveFieldNums: int
        :param _DistributionData: 敏感数据分布
        :type DistributionData: list of Note
        """
        self._DataSourceId = None
        self._DdName = None
        self._DataType = None
        self._TableNums = None
        self._SensitiveTableNums = None
        self._FieldNums = None
        self._SensitiveFieldNums = None
        self._DistributionData = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DdName(self):
        """数据库名称
        :rtype: str
        """
        return self._DdName

    @DdName.setter
    def DdName(self, DdName):
        self._DdName = DdName

    @property
    def DataType(self):
        """数据库类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TableNums(self):
        """表的数量
        :rtype: int
        """
        return self._TableNums

    @TableNums.setter
    def TableNums(self, TableNums):
        self._TableNums = TableNums

    @property
    def SensitiveTableNums(self):
        """敏感表数量
        :rtype: int
        """
        return self._SensitiveTableNums

    @SensitiveTableNums.setter
    def SensitiveTableNums(self, SensitiveTableNums):
        self._SensitiveTableNums = SensitiveTableNums

    @property
    def FieldNums(self):
        """字段的数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感字段的数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums

    @property
    def DistributionData(self):
        """敏感数据分布
        :rtype: list of Note
        """
        return self._DistributionData

    @DistributionData.setter
    def DistributionData(self, DistributionData):
        self._DistributionData = DistributionData


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DdName = params.get("DdName")
        self._DataType = params.get("DataType")
        self._TableNums = params.get("TableNums")
        self._SensitiveTableNums = params.get("SensitiveTableNums")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        if params.get("DistributionData") is not None:
            self._DistributionData = []
            for item in params.get("DistributionData"):
                obj = Note()
                obj._deserialize(item)
                self._DistributionData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetList(AbstractModel):
    """数据资产报告页面-用户查询入参

    """

    def __init__(self):
        r"""
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        :param _DataSourceInfo: 数据源信息
        :type DataSourceInfo: list of DataSourceInfo
        """
        self._DataSourceType = None
        self._DataSourceInfo = None

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def DataSourceInfo(self):
        """数据源信息
        :rtype: list of DataSourceInfo
        """
        return self._DataSourceInfo

    @DataSourceInfo.setter
    def DataSourceInfo(self, DataSourceInfo):
        self._DataSourceInfo = DataSourceInfo


    def _deserialize(self, params):
        self._DataSourceType = params.get("DataSourceType")
        if params.get("DataSourceInfo") is not None:
            self._DataSourceInfo = []
            for item in params.get("DataSourceInfo"):
                obj = DataSourceInfo()
                obj._deserialize(item)
                self._DataSourceInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeDSPAMetaResourcesRequest(AbstractModel):
    """AuthorizeDSPAMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _AuthType: 授权方式，可选：automatic(一键自动授权) 、 account(指定用户名授权)。
        :type AuthType: str
        :param _MetaType: 资源类型。
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourcesAccount: 用户授权的账户信息，如果是一键自动授权模式，则不需要填写账户名与密码。
        :type ResourcesAccount: list of DspaResourceAccount
        :param _CreateDefaultTask: 创建默认主模板扫描任务
        :type CreateDefaultTask: bool
        :param _AuthRange: 授权范围（all:授权整个数据源 manual:手动指定数据库）
        :type AuthRange: str
        """
        self._DspaId = None
        self._AuthType = None
        self._MetaType = None
        self._ResourceRegion = None
        self._ResourcesAccount = None
        self._CreateDefaultTask = None
        self._AuthRange = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def AuthType(self):
        """授权方式，可选：automatic(一键自动授权) 、 account(指定用户名授权)。
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def MetaType(self):
        """资源类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcesAccount(self):
        """用户授权的账户信息，如果是一键自动授权模式，则不需要填写账户名与密码。
        :rtype: list of DspaResourceAccount
        """
        return self._ResourcesAccount

    @ResourcesAccount.setter
    def ResourcesAccount(self, ResourcesAccount):
        self._ResourcesAccount = ResourcesAccount

    @property
    def CreateDefaultTask(self):
        """创建默认主模板扫描任务
        :rtype: bool
        """
        return self._CreateDefaultTask

    @CreateDefaultTask.setter
    def CreateDefaultTask(self, CreateDefaultTask):
        self._CreateDefaultTask = CreateDefaultTask

    @property
    def AuthRange(self):
        """授权范围（all:授权整个数据源 manual:手动指定数据库）
        :rtype: str
        """
        return self._AuthRange

    @AuthRange.setter
    def AuthRange(self, AuthRange):
        self._AuthRange = AuthRange


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._AuthType = params.get("AuthType")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        if params.get("ResourcesAccount") is not None:
            self._ResourcesAccount = []
            for item in params.get("ResourcesAccount"):
                obj = DspaResourceAccount()
                obj._deserialize(item)
                self._ResourcesAccount.append(obj)
        self._CreateDefaultTask = params.get("CreateDefaultTask")
        self._AuthRange = params.get("AuthRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeDSPAMetaResourcesResponse(AbstractModel):
    """AuthorizeDSPAMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _Results: 授权结果。
        :type Results: list of DspaTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DspaId = None
        self._Results = None
        self._RequestId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Results(self):
        """授权结果。
        :rtype: list of DspaTaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        self._DspaId = params.get("DspaId")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DspaTaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class BindDSPAResourceCosBucketsRequest(AbstractModel):
    """BindDSPAResourceCosBuckets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _BindCosResourceItems: 绑定的COS桶信息。
        :type BindCosResourceItems: list of CosResourceItem
        :param _UnbindCosResourceItems: 解绑的COS桶信息。
        :type UnbindCosResourceItems: list of CosResourceItem
        """
        self._DspaId = None
        self._BindCosResourceItems = None
        self._UnbindCosResourceItems = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def BindCosResourceItems(self):
        """绑定的COS桶信息。
        :rtype: list of CosResourceItem
        """
        return self._BindCosResourceItems

    @BindCosResourceItems.setter
    def BindCosResourceItems(self, BindCosResourceItems):
        self._BindCosResourceItems = BindCosResourceItems

    @property
    def UnbindCosResourceItems(self):
        """解绑的COS桶信息。
        :rtype: list of CosResourceItem
        """
        return self._UnbindCosResourceItems

    @UnbindCosResourceItems.setter
    def UnbindCosResourceItems(self, UnbindCosResourceItems):
        self._UnbindCosResourceItems = UnbindCosResourceItems


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        if params.get("BindCosResourceItems") is not None:
            self._BindCosResourceItems = []
            for item in params.get("BindCosResourceItems"):
                obj = CosResourceItem()
                obj._deserialize(item)
                self._BindCosResourceItems.append(obj)
        if params.get("UnbindCosResourceItems") is not None:
            self._UnbindCosResourceItems = []
            for item in params.get("UnbindCosResourceItems"):
                obj = CosResourceItem()
                obj._deserialize(item)
                self._UnbindCosResourceItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDSPAResourceCosBucketsResponse(AbstractModel):
    """BindDSPAResourceCosBuckets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosTaskResults: 绑定结果数组
        :type CosTaskResults: list of CosTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosTaskResults = None
        self._RequestId = None

    @property
    def CosTaskResults(self):
        """绑定结果数组
        :rtype: list of CosTaskResult
        """
        return self._CosTaskResults

    @CosTaskResults.setter
    def CosTaskResults(self, CosTaskResults):
        self._CosTaskResults = CosTaskResults

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
        if params.get("CosTaskResults") is not None:
            self._CosTaskResults = []
            for item in params.get("CosTaskResults"):
                obj = CosTaskResult()
                obj._deserialize(item)
                self._CosTaskResults.append(obj)
        self._RequestId = params.get("RequestId")


class BindDSPAResourceDatabasesRequest(AbstractModel):
    """BindDSPAResourceDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceId: 数据库实例ID。
        :type ResourceId: str
        :param _MetaType: 数据库实例类型。
        :type MetaType: str
        :param _BindDbItems: 绑定DB列表。
        :type BindDbItems: list of DbResourceItem
        :param _UnbindDbItems: 解绑DB列表。
        :type UnbindDbItems: list of DbResourceItem
        """
        self._DspaId = None
        self._ResourceId = None
        self._MetaType = None
        self._BindDbItems = None
        self._UnbindDbItems = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceId(self):
        """数据库实例ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def MetaType(self):
        """数据库实例类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def BindDbItems(self):
        """绑定DB列表。
        :rtype: list of DbResourceItem
        """
        return self._BindDbItems

    @BindDbItems.setter
    def BindDbItems(self, BindDbItems):
        self._BindDbItems = BindDbItems

    @property
    def UnbindDbItems(self):
        """解绑DB列表。
        :rtype: list of DbResourceItem
        """
        return self._UnbindDbItems

    @UnbindDbItems.setter
    def UnbindDbItems(self, UnbindDbItems):
        self._UnbindDbItems = UnbindDbItems


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceId = params.get("ResourceId")
        self._MetaType = params.get("MetaType")
        if params.get("BindDbItems") is not None:
            self._BindDbItems = []
            for item in params.get("BindDbItems"):
                obj = DbResourceItem()
                obj._deserialize(item)
                self._BindDbItems.append(obj)
        if params.get("UnbindDbItems") is not None:
            self._UnbindDbItems = []
            for item in params.get("UnbindDbItems"):
                obj = DbResourceItem()
                obj._deserialize(item)
                self._UnbindDbItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDSPAResourceDatabasesResponse(AbstractModel):
    """BindDSPAResourceDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DbTaskResults: 绑定结果数组
        :type DbTaskResults: list of DbTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DbTaskResults = None
        self._RequestId = None

    @property
    def DbTaskResults(self):
        """绑定结果数组
        :rtype: list of DbTaskResult
        """
        return self._DbTaskResults

    @DbTaskResults.setter
    def DbTaskResults(self, DbTaskResults):
        self._DbTaskResults = DbTaskResults

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
        if params.get("DbTaskResults") is not None:
            self._DbTaskResults = []
            for item in params.get("DbTaskResults"):
                obj = DbTaskResult()
                obj._deserialize(item)
                self._DbTaskResults.append(obj)
        self._RequestId = params.get("RequestId")


class COSDataRule(AbstractModel):
    """COS敏感数据识别规则

    """

    def __init__(self):
        r"""
        :param _Operator: 只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一.
默认值为or
        :type Operator: str
        :param _Contents: 规则内容
        :type Contents: list of DataContent
        """
        self._Operator = None
        self._Contents = None

    @property
    def Operator(self):
        """只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一.
默认值为or
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Contents(self):
        """规则内容
        :rtype: list of DataContent
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = DataContent()
                obj._deserialize(item)
                self._Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSInstance(AbstractModel):
    """COS数据源实例信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源Id
        :type DataSourceId: str
        :param _BucketName: 桶名
        :type BucketName: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        """
        self._DataSourceId = None
        self._BucketName = None
        self._ResourceRegion = None

    @property
    def DataSourceId(self):
        """数据源Id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def BucketName(self):
        """桶名
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._BucketName = params.get("BucketName")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CategoryRule(AbstractModel):
    """分类规则信息

    """

    def __init__(self):
        r"""
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _RuleId: 规则id
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _LevelId: 级别id
        :type LevelId: int
        :param _LevelName: 级别名称
        :type LevelName: str
        :param _Id: 分类规则绑定关系id
        :type Id: int
        :param _AliasRuleId: 别名ID
        :type AliasRuleId: int
        :param _AliasRuleName: 别名规则名称
        :type AliasRuleName: str
        :param _RuleEffectItems: 各类分类分级规则数量
        :type RuleEffectItems: list of RuleEffectItem
        :param _RuleStatus: 规则状态
        :type RuleStatus: int
        """
        self._CategoryId = None
        self._RuleId = None
        self._RuleName = None
        self._LevelId = None
        self._LevelName = None
        self._Id = None
        self._AliasRuleId = None
        self._AliasRuleName = None
        self._RuleEffectItems = None
        self._RuleStatus = None

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def LevelId(self):
        """级别id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """级别名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def Id(self):
        """分类规则绑定关系id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AliasRuleId(self):
        """别名ID
        :rtype: int
        """
        return self._AliasRuleId

    @AliasRuleId.setter
    def AliasRuleId(self, AliasRuleId):
        self._AliasRuleId = AliasRuleId

    @property
    def AliasRuleName(self):
        """别名规则名称
        :rtype: str
        """
        return self._AliasRuleName

    @AliasRuleName.setter
    def AliasRuleName(self, AliasRuleName):
        self._AliasRuleName = AliasRuleName

    @property
    def RuleEffectItems(self):
        """各类分类分级规则数量
        :rtype: list of RuleEffectItem
        """
        return self._RuleEffectItems

    @RuleEffectItems.setter
    def RuleEffectItems(self, RuleEffectItems):
        self._RuleEffectItems = RuleEffectItems

    @property
    def RuleStatus(self):
        """规则状态
        :rtype: int
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        self._Id = params.get("Id")
        self._AliasRuleId = params.get("AliasRuleId")
        self._AliasRuleName = params.get("AliasRuleName")
        if params.get("RuleEffectItems") is not None:
            self._RuleEffectItems = []
            for item in params.get("RuleEffectItems"):
                obj = RuleEffectItem()
                obj._deserialize(item)
                self._RuleEffectItems.append(obj)
        self._RuleStatus = params.get("RuleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CategoryRuleStatistic(AbstractModel):
    """分类规则统计信息

    """

    def __init__(self):
        r"""
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _RuleCount: 规则数量
        :type RuleCount: int
        :param _CategoryName: 分类名称
        :type CategoryName: str
        """
        self._CategoryId = None
        self._RuleCount = None
        self._CategoryName = None

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def RuleCount(self):
        """规则数量
        :rtype: int
        """
        return self._RuleCount

    @RuleCount.setter
    def RuleCount(self, RuleCount):
        self._RuleCount = RuleCount

    @property
    def CategoryName(self):
        """分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._RuleCount = params.get("RuleCount")
        self._CategoryName = params.get("CategoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudResourceItem(AbstractModel):
    """云数据库资源项

    """

    def __init__(self):
        r"""
        :param _Region: 资源所处地域。
        :type Region: str
        :param _Items: 	云上资源列表。
        :type Items: list of DspaCloudResourceMeta
        """
        self._Region = None
        self._Items = None

    @property
    def Region(self):
        """资源所处地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Items(self):
        """	云上资源列表。
        :rtype: list of DspaCloudResourceMeta
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaCloudResourceMeta()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceGroupDetail(AbstractModel):
    """模板详情

    """

    def __init__(self):
        r"""
        :param _Id: 模板id
        :type Id: int
        :param _Name: 模板名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _ComplianceGroupType: 模板类型
        :type ComplianceGroupType: int
        :param _LevelGroupId: 模板分级方案id
        :type LevelGroupId: int
        :param _LevelGroupName: 模板分级方案名称
        :type LevelGroupName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 更新时间
        :type ModifyTime: str
        :param _IsAlias: 是否开启别名
        :type IsAlias: bool
        """
        self._Id = None
        self._Name = None
        self._Description = None
        self._ComplianceGroupType = None
        self._LevelGroupId = None
        self._LevelGroupName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._IsAlias = None

    @property
    def Id(self):
        """模板id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """模板名称
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
    def ComplianceGroupType(self):
        """模板类型
        :rtype: int
        """
        return self._ComplianceGroupType

    @ComplianceGroupType.setter
    def ComplianceGroupType(self, ComplianceGroupType):
        self._ComplianceGroupType = ComplianceGroupType

    @property
    def LevelGroupId(self):
        """模板分级方案id
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

    @property
    def LevelGroupName(self):
        """模板分级方案名称
        :rtype: str
        """
        return self._LevelGroupName

    @LevelGroupName.setter
    def LevelGroupName(self, LevelGroupName):
        self._LevelGroupName = LevelGroupName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """更新时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def IsAlias(self):
        """是否开启别名
        :rtype: bool
        """
        return self._IsAlias

    @IsAlias.setter
    def IsAlias(self, IsAlias):
        self._IsAlias = IsAlias


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ComplianceGroupType = params.get("ComplianceGroupType")
        self._LevelGroupId = params.get("LevelGroupId")
        self._LevelGroupName = params.get("LevelGroupName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._IsAlias = params.get("IsAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceGroupRuleIdInfo(AbstractModel):
    """合规组中规则信息：包括规则ID，数据分类ID, 数据分级标识ID

    """

    def __init__(self):
        r"""
        :param _RuleId: 敏感数据识别规则ID
        :type RuleId: int
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _LevelId: 敏感数据分级标识ID, 系统支持高、中、低三级，也支持自定义分级
        :type LevelId: int
        """
        self._RuleId = None
        self._CategoryId = None
        self._LevelId = None

    @property
    def RuleId(self):
        """敏感数据识别规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """敏感数据分级标识ID, 系统支持高、中、低三级，也支持自定义分级
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyDSPATemplateRequest(AbstractModel):
    """CopyDSPATemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TemplateId: 合规组ID
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """合规组ID
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyDSPATemplateResponse(AbstractModel):
    """CopyDSPATemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CosAsset(AbstractModel):
    """数据资产报告-cos的敏感资产报告详情

    """

    def __init__(self):
        r"""
        :param _BucketNums: 桶的个数
        :type BucketNums: int
        :param _SensitiveBucketNums: 敏感桶的个数
        :type SensitiveBucketNums: int
        :param _FileNums: 文件个数
        :type FileNums: int
        :param _SensitiveFileNums: 敏感文件的个数
        :type SensitiveFileNums: int
        """
        self._BucketNums = None
        self._SensitiveBucketNums = None
        self._FileNums = None
        self._SensitiveFileNums = None

    @property
    def BucketNums(self):
        """桶的个数
        :rtype: int
        """
        return self._BucketNums

    @BucketNums.setter
    def BucketNums(self, BucketNums):
        self._BucketNums = BucketNums

    @property
    def SensitiveBucketNums(self):
        """敏感桶的个数
        :rtype: int
        """
        return self._SensitiveBucketNums

    @SensitiveBucketNums.setter
    def SensitiveBucketNums(self, SensitiveBucketNums):
        self._SensitiveBucketNums = SensitiveBucketNums

    @property
    def FileNums(self):
        """文件个数
        :rtype: int
        """
        return self._FileNums

    @FileNums.setter
    def FileNums(self, FileNums):
        self._FileNums = FileNums

    @property
    def SensitiveFileNums(self):
        """敏感文件的个数
        :rtype: int
        """
        return self._SensitiveFileNums

    @SensitiveFileNums.setter
    def SensitiveFileNums(self, SensitiveFileNums):
        self._SensitiveFileNums = SensitiveFileNums


    def _deserialize(self, params):
        self._BucketNums = params.get("BucketNums")
        self._SensitiveBucketNums = params.get("SensitiveBucketNums")
        self._FileNums = params.get("FileNums")
        self._SensitiveFileNums = params.get("SensitiveFileNums")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosBucketItem(AbstractModel):
    """cos桶资源项

    """

    def __init__(self):
        r"""
        :param _Region: 资源所处地域。
        :type Region: str
        :param _Buckets: COS桶列表。
        :type Buckets: list of str
        """
        self._Region = None
        self._Buckets = None

    @property
    def Region(self):
        """资源所处地域。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Buckets(self):
        """COS桶列表。
        :rtype: list of str
        """
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Buckets = params.get("Buckets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosResourceItem(AbstractModel):
    """COS资源的桶信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: cos数据源ID。
        :type ResourceId: str
        :param _ResourceRegion: 桶所在地域。
        :type ResourceRegion: str
        :param _ResourceName: 桶名称。
        :type ResourceName: str
        """
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        """cos数据源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """桶所在地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceName(self):
        """桶名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosTaskResult(AbstractModel):
    """cos批量操作返回结果结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果类型。
        :type Result: str
        :param _ResultDescription: 结果描述。
        :type ResultDescription: str
        :param _ErrDescription: 错误信息描述。
        :type ErrDescription: :class:`tencentcloud.dsgc.v20190723.models.ErrDescription`
        :param _ResourceId: 资源ID。
        :type ResourceId: str
        """
        self._Result = None
        self._ResultDescription = None
        self._ErrDescription = None
        self._ResourceId = None

    @property
    def Result(self):
        """结果类型。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultDescription(self):
        """结果描述。
        :rtype: str
        """
        return self._ResultDescription

    @ResultDescription.setter
    def ResultDescription(self, ResultDescription):
        self._ResultDescription = ResultDescription

    @property
    def ErrDescription(self):
        """错误信息描述。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ErrDescription`
        """
        return self._ErrDescription

    @ErrDescription.setter
    def ErrDescription(self, ErrDescription):
        self._ErrDescription = ErrDescription

    @property
    def ResourceId(self):
        """资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ResultDescription = params.get("ResultDescription")
        if params.get("ErrDescription") is not None:
            self._ErrDescription = ErrDescription()
            self._ErrDescription._deserialize(params.get("ErrDescription"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetSortingReportRetryTaskRequest(AbstractModel):
    """CreateAssetSortingReportRetryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportTaskId: 任务id
        :type ReportTaskId: int
        :param _DspaId: dspa实例id
        :type DspaId: str
        """
        self._ReportTaskId = None
        self._DspaId = None

    @property
    def ReportTaskId(self):
        """任务id
        :rtype: int
        """
        return self._ReportTaskId

    @ReportTaskId.setter
    def ReportTaskId(self, ReportTaskId):
        self._ReportTaskId = ReportTaskId

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._ReportTaskId = params.get("ReportTaskId")
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetSortingReportRetryTaskResponse(AbstractModel):
    """CreateAssetSortingReportRetryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportTaskId: 任务id
        :type ReportTaskId: int
        :param _Remark: 提示信息
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportTaskId = None
        self._Remark = None
        self._RequestId = None

    @property
    def ReportTaskId(self):
        """任务id
        :rtype: int
        """
        return self._ReportTaskId

    @ReportTaskId.setter
    def ReportTaskId(self, ReportTaskId):
        self._ReportTaskId = ReportTaskId

    @property
    def Remark(self):
        """提示信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
        self._ReportTaskId = params.get("ReportTaskId")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class CreateAssetSortingReportTaskRequest(AbstractModel):
    """CreateAssetSortingReportTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 识别模板id
        :type ComplianceId: int
        :param _AssetList: 选中资产列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """识别模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """选中资产列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetSortingReportTaskResponse(AbstractModel):
    """CreateAssetSortingReportTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportTaskId: 报表任务id
        :type ReportTaskId: int
        :param _Remark: 提示信息
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportTaskId = None
        self._Remark = None
        self._RequestId = None

    @property
    def ReportTaskId(self):
        """报表任务id
        :rtype: int
        """
        return self._ReportTaskId

    @ReportTaskId.setter
    def ReportTaskId(self, ReportTaskId):
        self._ReportTaskId = ReportTaskId

    @property
    def Remark(self):
        """提示信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
        self._ReportTaskId = params.get("ReportTaskId")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class CreateComplianceRules(AbstractModel):
    """合规组分类关联规则信息

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则id
        :type RuleId: int
        :param _LevelId: 级别id
        :type LevelId: int
        """
        self._RuleId = None
        self._LevelId = None

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def LevelId(self):
        """级别id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._LevelId = params.get("LevelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAAssessmentRiskLevelRequest(AbstractModel):
    """CreateDSPAAssessmentRiskLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _RiskLevelName: 风险等级名称
        :type RiskLevelName: str
        :param _IdentifyComplianceId: 识别模板
        :type IdentifyComplianceId: int
        :param _RiskLevelRule: 风险等级矩阵
        :type RiskLevelRule: list of RiskLevelMatrix
        :param _RiskLevelDescription: 风险等级的描述
        :type RiskLevelDescription: str
        """
        self._DspaId = None
        self._RiskLevelName = None
        self._IdentifyComplianceId = None
        self._RiskLevelRule = None
        self._RiskLevelDescription = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def RiskLevelName(self):
        """风险等级名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def IdentifyComplianceId(self):
        """识别模板
        :rtype: int
        """
        return self._IdentifyComplianceId

    @IdentifyComplianceId.setter
    def IdentifyComplianceId(self, IdentifyComplianceId):
        self._IdentifyComplianceId = IdentifyComplianceId

    @property
    def RiskLevelRule(self):
        """风险等级矩阵
        :rtype: list of RiskLevelMatrix
        """
        return self._RiskLevelRule

    @RiskLevelRule.setter
    def RiskLevelRule(self, RiskLevelRule):
        self._RiskLevelRule = RiskLevelRule

    @property
    def RiskLevelDescription(self):
        """风险等级的描述
        :rtype: str
        """
        return self._RiskLevelDescription

    @RiskLevelDescription.setter
    def RiskLevelDescription(self, RiskLevelDescription):
        self._RiskLevelDescription = RiskLevelDescription


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._RiskLevelName = params.get("RiskLevelName")
        self._IdentifyComplianceId = params.get("IdentifyComplianceId")
        if params.get("RiskLevelRule") is not None:
            self._RiskLevelRule = []
            for item in params.get("RiskLevelRule"):
                obj = RiskLevelMatrix()
                obj._deserialize(item)
                self._RiskLevelRule.append(obj)
        self._RiskLevelDescription = params.get("RiskLevelDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAAssessmentRiskLevelResponse(AbstractModel):
    """CreateDSPAAssessmentRiskLevel返回参数结构体

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


class CreateDSPAAssessmentRiskTemplateRequest(AbstractModel):
    """CreateDSPAAssessmentRiskTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _RiskLevelId: 风险等级id
        :type RiskLevelId: int
        :param _RiskIdList: 风险id列表
        :type RiskIdList: list of int
        :param _TemplateDescription: 模板描述
        :type TemplateDescription: str
        """
        self._DspaId = None
        self._TemplateName = None
        self._RiskLevelId = None
        self._RiskIdList = None
        self._TemplateDescription = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def RiskLevelId(self):
        """风险等级id
        :rtype: int
        """
        return self._RiskLevelId

    @RiskLevelId.setter
    def RiskLevelId(self, RiskLevelId):
        self._RiskLevelId = RiskLevelId

    @property
    def RiskIdList(self):
        """风险id列表
        :rtype: list of int
        """
        return self._RiskIdList

    @RiskIdList.setter
    def RiskIdList(self, RiskIdList):
        self._RiskIdList = RiskIdList

    @property
    def TemplateDescription(self):
        """模板描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateName = params.get("TemplateName")
        self._RiskLevelId = params.get("RiskLevelId")
        self._RiskIdList = params.get("RiskIdList")
        self._TemplateDescription = params.get("TemplateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAAssessmentRiskTemplateResponse(AbstractModel):
    """CreateDSPAAssessmentRiskTemplate返回参数结构体

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


class CreateDSPAAssessmentTaskRequest(AbstractModel):
    """CreateDSPAAssessmentTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _Name: 评估任务名称。1-20个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :type Name: str
        :param _TemplateId: 评估模板Id，格式“template-xxxxxxxx”
        :type TemplateId: str
        :param _BusinessName: 评估业务名称。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :type BusinessName: str
        :param _BusinessDept: 业务所属部门。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :type BusinessDept: str
        :param _BusinessOwner: 业务负责人。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :type BusinessOwner: str
        :param _ComplianceId: 分类分级模板Id
        :type ComplianceId: int
        :param _DiscoveryCondition: 敏感数据扫描数据源条件。
        :type DiscoveryCondition: :class:`tencentcloud.dsgc.v20190723.models.DiscoveryCondition`
        :param _Description: 说明
        :type Description: str
        """
        self._DspaId = None
        self._Name = None
        self._TemplateId = None
        self._BusinessName = None
        self._BusinessDept = None
        self._BusinessOwner = None
        self._ComplianceId = None
        self._DiscoveryCondition = None
        self._Description = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """评估任务名称。1-20个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TemplateId(self):
        """评估模板Id，格式“template-xxxxxxxx”
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def BusinessName(self):
        warnings.warn("parameter `BusinessName` is deprecated", DeprecationWarning) 

        """评估业务名称。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        warnings.warn("parameter `BusinessName` is deprecated", DeprecationWarning) 

        self._BusinessName = BusinessName

    @property
    def BusinessDept(self):
        warnings.warn("parameter `BusinessDept` is deprecated", DeprecationWarning) 

        """业务所属部门。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :rtype: str
        """
        return self._BusinessDept

    @BusinessDept.setter
    def BusinessDept(self, BusinessDept):
        warnings.warn("parameter `BusinessDept` is deprecated", DeprecationWarning) 

        self._BusinessDept = BusinessDept

    @property
    def BusinessOwner(self):
        warnings.warn("parameter `BusinessOwner` is deprecated", DeprecationWarning) 

        """业务负责人。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字
        :rtype: str
        """
        return self._BusinessOwner

    @BusinessOwner.setter
    def BusinessOwner(self, BusinessOwner):
        warnings.warn("parameter `BusinessOwner` is deprecated", DeprecationWarning) 

        self._BusinessOwner = BusinessOwner

    @property
    def ComplianceId(self):
        """分类分级模板Id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def DiscoveryCondition(self):
        """敏感数据扫描数据源条件。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DiscoveryCondition`
        """
        return self._DiscoveryCondition

    @DiscoveryCondition.setter
    def DiscoveryCondition(self, DiscoveryCondition):
        self._DiscoveryCondition = DiscoveryCondition

    @property
    def Description(self):
        """说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._TemplateId = params.get("TemplateId")
        self._BusinessName = params.get("BusinessName")
        self._BusinessDept = params.get("BusinessDept")
        self._BusinessOwner = params.get("BusinessOwner")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("DiscoveryCondition") is not None:
            self._DiscoveryCondition = DiscoveryCondition()
            self._DiscoveryCondition._deserialize(params.get("DiscoveryCondition"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAAssessmentTaskResponse(AbstractModel):
    """CreateDSPAAssessmentTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 评估任务Id，格式“task-xxxxxxxx”
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """评估任务Id，格式“task-xxxxxxxx”
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDSPACOSDiscoveryTaskRequest(AbstractModel):
    """CreateDSPACOSDiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _Enable: 任务开关，0 关闭，1 启用
        :type Enable: int
        :param _Bucket: 桶名
        :type Bucket: str
        :param _Plan: 执行计划， 0立即 1定时，选择“立即”时，扫描周期只能选择单次。
        :type Plan: int
        :param _Period: 扫描周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _FileTypes: 待扫描文件类型，用逗号隔开，格式如：[".txt", ".csv", ".log", ".xml",".html", ".json"]。
        :type FileTypes: list of str
        :param _FileSizeLimit: 文件大小上限，单位为KB，如1000, 目前单个文件最大只支持100MB（102400KB）
        :type FileSizeLimit: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _Description: 任务描述，最大长度为1024个字符
        :type Description: str
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _ComplianceGroupIds: 合规组ID列表，最多支持添加5个
        :type ComplianceGroupIds: list of int
        :param _TimingStartTime: 任务定时启动时间，格式如：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :type TimingStartTime: str
        """
        self._DspaId = None
        self._Name = None
        self._DataSourceId = None
        self._Enable = None
        self._Bucket = None
        self._Plan = None
        self._Period = None
        self._FileTypes = None
        self._FileSizeLimit = None
        self._ResourceRegion = None
        self._Description = None
        self._GeneralRuleSetEnable = None
        self._ComplianceGroupIds = None
        self._TimingStartTime = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def Enable(self):
        """任务开关，0 关闭，1 启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Bucket(self):
        """桶名
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Plan(self):
        """执行计划， 0立即 1定时，选择“立即”时，扫描周期只能选择单次。
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Period(self):
        """扫描周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FileTypes(self):
        """待扫描文件类型，用逗号隔开，格式如：[".txt", ".csv", ".log", ".xml",".html", ".json"]。
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def FileSizeLimit(self):
        """文件大小上限，单位为KB，如1000, 目前单个文件最大只支持100MB（102400KB）
        :rtype: int
        """
        return self._FileSizeLimit

    @FileSizeLimit.setter
    def FileSizeLimit(self, FileSizeLimit):
        self._FileSizeLimit = FileSizeLimit

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def Description(self):
        """任务描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def ComplianceGroupIds(self):
        """合规组ID列表，最多支持添加5个
        :rtype: list of int
        """
        return self._ComplianceGroupIds

    @ComplianceGroupIds.setter
    def ComplianceGroupIds(self, ComplianceGroupIds):
        self._ComplianceGroupIds = ComplianceGroupIds

    @property
    def TimingStartTime(self):
        """任务定时启动时间，格式如：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._DataSourceId = params.get("DataSourceId")
        self._Enable = params.get("Enable")
        self._Bucket = params.get("Bucket")
        self._Plan = params.get("Plan")
        self._Period = params.get("Period")
        self._FileTypes = params.get("FileTypes")
        self._FileSizeLimit = params.get("FileSizeLimit")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Description = params.get("Description")
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        self._ComplianceGroupIds = params.get("ComplianceGroupIds")
        self._TimingStartTime = params.get("TimingStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPACOSDiscoveryTaskResponse(AbstractModel):
    """CreateDSPACOSDiscoveryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _ResultId: 扫描结果ID
        :type ResultId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResultId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResultId(self):
        """扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

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
        self._TaskId = params.get("TaskId")
        self._ResultId = params.get("ResultId")
        self._RequestId = params.get("RequestId")


class CreateDSPACategoryRelationRequest(AbstractModel):
    """CreateDSPACategoryRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _ParentCategoryId: 父级分类id（无父级分类传-1）
        :type ParentCategoryId: int
        :param _ComplianceId: 分类模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._CategoryId = None
        self._ParentCategoryId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ParentCategoryId(self):
        """父级分类id（无父级分类传-1）
        :rtype: int
        """
        return self._ParentCategoryId

    @ParentCategoryId.setter
    def ParentCategoryId(self, ParentCategoryId):
        self._ParentCategoryId = ParentCategoryId

    @property
    def ComplianceId(self):
        """分类模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._ParentCategoryId = params.get("ParentCategoryId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPACategoryRelationResponse(AbstractModel):
    """CreateDSPACategoryRelation返回参数结构体

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


class CreateDSPACategoryRequest(AbstractModel):
    """CreateDSPACategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 敏感数据分类名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        """
        self._DspaId = None
        self._Name = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """敏感数据分类名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPACategoryResponse(AbstractModel):
    """CreateDSPACategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryId = None
        self._RequestId = None

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
        self._CategoryId = params.get("CategoryId")
        self._RequestId = params.get("RequestId")


class CreateDSPAComplianceGroupRequest(AbstractModel):
    """CreateDSPAComplianceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 合规组名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _Description: 合规组描述，最大长度为1024个字符
        :type Description: str
        :param _ComplianceGroupRules: 合规组规则配置（参数已废弃，请传空数组）
        :type ComplianceGroupRules: list of ComplianceGroupRuleIdInfo
        :param _LevelGroupId: 分级组ID，默认值为1，新增参数，可选
        :type LevelGroupId: int
        :param _Status: 1代表模版开启，0代表模版关闭
        :type Status: int
        :param _CloseComplianceId: 该complianceId的开启状态将被关闭
        :type CloseComplianceId: int
        """
        self._DspaId = None
        self._Name = None
        self._Description = None
        self._ComplianceGroupRules = None
        self._LevelGroupId = None
        self._Status = None
        self._CloseComplianceId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """合规组名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """合规组描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ComplianceGroupRules(self):
        """合规组规则配置（参数已废弃，请传空数组）
        :rtype: list of ComplianceGroupRuleIdInfo
        """
        return self._ComplianceGroupRules

    @ComplianceGroupRules.setter
    def ComplianceGroupRules(self, ComplianceGroupRules):
        self._ComplianceGroupRules = ComplianceGroupRules

    @property
    def LevelGroupId(self):
        """分级组ID，默认值为1，新增参数，可选
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

    @property
    def Status(self):
        """1代表模版开启，0代表模版关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CloseComplianceId(self):
        """该complianceId的开启状态将被关闭
        :rtype: int
        """
        return self._CloseComplianceId

    @CloseComplianceId.setter
    def CloseComplianceId(self, CloseComplianceId):
        self._CloseComplianceId = CloseComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ComplianceGroupRules") is not None:
            self._ComplianceGroupRules = []
            for item in params.get("ComplianceGroupRules"):
                obj = ComplianceGroupRuleIdInfo()
                obj._deserialize(item)
                self._ComplianceGroupRules.append(obj)
        self._LevelGroupId = params.get("LevelGroupId")
        self._Status = params.get("Status")
        self._CloseComplianceId = params.get("CloseComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAComplianceGroupResponse(AbstractModel):
    """CreateDSPAComplianceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ComplianceGroupId = None
        self._RequestId = None

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

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
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._RequestId = params.get("RequestId")


class CreateDSPAComplianceRulesRequest(AbstractModel):
    """CreateDSPAComplianceRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _ComplianceId: 合规组模板id
        :type ComplianceId: int
        :param _Rules: 规则列表
        :type Rules: list of CreateComplianceRules
        """
        self._DspaId = None
        self._CategoryId = None
        self._ComplianceId = None
        self._Rules = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ComplianceId(self):
        """合规组模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def Rules(self):
        """规则列表
        :rtype: list of CreateComplianceRules
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateComplianceRules()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAComplianceRulesResponse(AbstractModel):
    """CreateDSPAComplianceRules返回参数结构体

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


class CreateDSPACosMetaResourcesRequest(AbstractModel):
    """CreateDSPACosMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _Buckets: COS桶列表
        :type Buckets: list of str
        :param _CosBucketItems: 必填，COS资源列表
        :type CosBucketItems: list of CosBucketItem
        """
        self._DspaId = None
        self._ResourceRegion = None
        self._Buckets = None
        self._CosBucketItems = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceRegion(self):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        self._ResourceRegion = ResourceRegion

    @property
    def Buckets(self):
        warnings.warn("parameter `Buckets` is deprecated", DeprecationWarning) 

        """COS桶列表
        :rtype: list of str
        """
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        warnings.warn("parameter `Buckets` is deprecated", DeprecationWarning) 

        self._Buckets = Buckets

    @property
    def CosBucketItems(self):
        """必填，COS资源列表
        :rtype: list of CosBucketItem
        """
        return self._CosBucketItems

    @CosBucketItems.setter
    def CosBucketItems(self, CosBucketItems):
        self._CosBucketItems = CosBucketItems


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Buckets = params.get("Buckets")
        if params.get("CosBucketItems") is not None:
            self._CosBucketItems = []
            for item in params.get("CosBucketItems"):
                obj = CosBucketItem()
                obj._deserialize(item)
                self._CosBucketItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPACosMetaResourcesResponse(AbstractModel):
    """CreateDSPACosMetaResources返回参数结构体

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


class CreateDSPADbMetaResourcesRequest(AbstractModel):
    """CreateDSPADbMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _UpdateStatus: 用来标记本次更新是否已经是最后一次，可选值：continue（后续还需要更新）、finished（本次是最后一次更新）。
        :type UpdateStatus: str
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _Items: 云上资源列表。
        :type Items: list of DspaCloudResourceMeta
        :param _CloudResourceItems: 必填，云数据库资源列表。
        :type CloudResourceItems: list of CloudResourceItem
        """
        self._DspaId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._UpdateStatus = None
        self._UpdateId = None
        self._Items = None
        self._CloudResourceItems = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MetaType(self):
        """资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        self._ResourceRegion = ResourceRegion

    @property
    def UpdateStatus(self):
        warnings.warn("parameter `UpdateStatus` is deprecated", DeprecationWarning) 

        """用来标记本次更新是否已经是最后一次，可选值：continue（后续还需要更新）、finished（本次是最后一次更新）。
        :rtype: str
        """
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        warnings.warn("parameter `UpdateStatus` is deprecated", DeprecationWarning) 

        self._UpdateStatus = UpdateStatus

    @property
    def UpdateId(self):
        warnings.warn("parameter `UpdateId` is deprecated", DeprecationWarning) 

        """本次更新的ID号，用来标记一次完整的更新过程。
        :rtype: str
        """
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        warnings.warn("parameter `UpdateId` is deprecated", DeprecationWarning) 

        self._UpdateId = UpdateId

    @property
    def Items(self):
        warnings.warn("parameter `Items` is deprecated", DeprecationWarning) 

        """云上资源列表。
        :rtype: list of DspaCloudResourceMeta
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        warnings.warn("parameter `Items` is deprecated", DeprecationWarning) 

        self._Items = Items

    @property
    def CloudResourceItems(self):
        """必填，云数据库资源列表。
        :rtype: list of CloudResourceItem
        """
        return self._CloudResourceItems

    @CloudResourceItems.setter
    def CloudResourceItems(self, CloudResourceItems):
        self._CloudResourceItems = CloudResourceItems


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._UpdateStatus = params.get("UpdateStatus")
        self._UpdateId = params.get("UpdateId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaCloudResourceMeta()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("CloudResourceItems") is not None:
            self._CloudResourceItems = []
            for item in params.get("CloudResourceItems"):
                obj = CloudResourceItem()
                obj._deserialize(item)
                self._CloudResourceItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPADbMetaResourcesResponse(AbstractModel):
    """CreateDSPADbMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpdateId = None
        self._MetaType = None
        self._DspaId = None
        self._ResourceRegion = None
        self._RequestId = None

    @property
    def UpdateId(self):
        warnings.warn("parameter `UpdateId` is deprecated", DeprecationWarning) 

        """本次更新的ID号，用来标记一次完整的更新过程。
        :rtype: str
        """
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        warnings.warn("parameter `UpdateId` is deprecated", DeprecationWarning) 

        self._UpdateId = UpdateId

    @property
    def MetaType(self):
        """资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceRegion(self):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        warnings.warn("parameter `ResourceRegion` is deprecated", DeprecationWarning) 

        self._ResourceRegion = ResourceRegion

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
        self._UpdateId = params.get("UpdateId")
        self._MetaType = params.get("MetaType")
        self._DspaId = params.get("DspaId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._RequestId = params.get("RequestId")


class CreateDSPADiscoveryRuleRequest(AbstractModel):
    """CreateDSPADiscoveryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 规则名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _Description: 规则描述，最大长度为1024个字符
        :type Description: str
        :param _RDBRules: RDB类敏感数据识别规则
        :type RDBRules: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryRDBRules`
        :param _COSRules: COS类敏感数据识别规则
        :type COSRules: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSRules`
        :param _Status: 规则状态；0 不启用, 1 启用
        :type Status: int
        """
        self._DspaId = None
        self._Name = None
        self._Description = None
        self._RDBRules = None
        self._COSRules = None
        self._Status = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """规则名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """规则描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RDBRules(self):
        """RDB类敏感数据识别规则
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryRDBRules`
        """
        return self._RDBRules

    @RDBRules.setter
    def RDBRules(self, RDBRules):
        self._RDBRules = RDBRules

    @property
    def COSRules(self):
        """COS类敏感数据识别规则
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSRules`
        """
        return self._COSRules

    @COSRules.setter
    def COSRules(self, COSRules):
        self._COSRules = COSRules

    @property
    def Status(self):
        """规则状态；0 不启用, 1 启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("RDBRules") is not None:
            self._RDBRules = DspaDiscoveryRDBRules()
            self._RDBRules._deserialize(params.get("RDBRules"))
        if params.get("COSRules") is not None:
            self._COSRules = DspaDiscoveryCOSRules()
            self._COSRules._deserialize(params.get("COSRules"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPADiscoveryRuleResponse(AbstractModel):
    """CreateDSPADiscoveryRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateDSPADiscoveryTaskRequest(AbstractModel):
    """CreateDSPADiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _Enable: 任务开关，0 关闭，1 启用
        :type Enable: int
        :param _Plan: 执行计划， 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :type Plan: int
        :param _Period: 扫描周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _DataSourceType: 数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :type DataSourceType: str
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _Description: 任务描述，最大长度为1024个字符
        :type Description: str
        :param _Condition: 用于传入的数据源的条件，目前只支持数据库，所以目前表示数据库的名称，选择多个数据库，之间通过逗号分隔，若不选，则默认选择全部数据库
        :type Condition: str
        :param _ComplianceGroupIds: 合规组ID列表，最多支持添加5个
        :type ComplianceGroupIds: list of int
        :param _TimingStartTime: 任务定时启动时间，格式如：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :type TimingStartTime: str
        :param _Order: random-随机，asc生序，desc降序
        :type Order: str
        :param _Rows: 抽样的条数，范围30-1000
        :type Rows: int
        :param _GlobalOrderField: 抽样的排序字段
        :type GlobalOrderField: str
        """
        self._DspaId = None
        self._Name = None
        self._DataSourceId = None
        self._Enable = None
        self._Plan = None
        self._Period = None
        self._ResourceRegion = None
        self._DataSourceType = None
        self._GeneralRuleSetEnable = None
        self._Description = None
        self._Condition = None
        self._ComplianceGroupIds = None
        self._TimingStartTime = None
        self._Order = None
        self._Rows = None
        self._GlobalOrderField = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def Enable(self):
        """任务开关，0 关闭，1 启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Plan(self):
        """执行计划， 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Period(self):
        """扫描周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DataSourceType(self):
        """数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def GeneralRuleSetEnable(self):
        warnings.warn("parameter `GeneralRuleSetEnable` is deprecated", DeprecationWarning) 

        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        warnings.warn("parameter `GeneralRuleSetEnable` is deprecated", DeprecationWarning) 

        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def Description(self):
        """任务描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Condition(self):
        """用于传入的数据源的条件，目前只支持数据库，所以目前表示数据库的名称，选择多个数据库，之间通过逗号分隔，若不选，则默认选择全部数据库
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ComplianceGroupIds(self):
        """合规组ID列表，最多支持添加5个
        :rtype: list of int
        """
        return self._ComplianceGroupIds

    @ComplianceGroupIds.setter
    def ComplianceGroupIds(self, ComplianceGroupIds):
        self._ComplianceGroupIds = ComplianceGroupIds

    @property
    def TimingStartTime(self):
        """任务定时启动时间，格式如：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def Order(self):
        """random-随机，asc生序，desc降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Rows(self):
        """抽样的条数，范围30-1000
        :rtype: int
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def GlobalOrderField(self):
        """抽样的排序字段
        :rtype: str
        """
        return self._GlobalOrderField

    @GlobalOrderField.setter
    def GlobalOrderField(self, GlobalOrderField):
        self._GlobalOrderField = GlobalOrderField


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._DataSourceId = params.get("DataSourceId")
        self._Enable = params.get("Enable")
        self._Plan = params.get("Plan")
        self._Period = params.get("Period")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DataSourceType = params.get("DataSourceType")
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        self._Description = params.get("Description")
        self._Condition = params.get("Condition")
        self._ComplianceGroupIds = params.get("ComplianceGroupIds")
        self._TimingStartTime = params.get("TimingStartTime")
        self._Order = params.get("Order")
        self._Rows = params.get("Rows")
        self._GlobalOrderField = params.get("GlobalOrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPADiscoveryTaskResponse(AbstractModel):
    """CreateDSPADiscoveryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _ResultId: 扫描结果ID
        :type ResultId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResultId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResultId(self):
        """扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

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
        self._TaskId = params.get("TaskId")
        self._ResultId = params.get("ResultId")
        self._RequestId = params.get("RequestId")


class CreateDSPALevelGroupRequest(AbstractModel):
    """CreateDSPALevelGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 分级组名称，唯一性约束，最多60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _ItemLevels: 分级标识配置
        :type ItemLevels: list of ItemLevel
        :param _Description: 分级组描述，最多1024字符
        :type Description: str
        """
        self._DspaId = None
        self._Name = None
        self._ItemLevels = None
        self._Description = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """分级组名称，唯一性约束，最多60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ItemLevels(self):
        """分级标识配置
        :rtype: list of ItemLevel
        """
        return self._ItemLevels

    @ItemLevels.setter
    def ItemLevels(self, ItemLevels):
        self._ItemLevels = ItemLevels

    @property
    def Description(self):
        """分级组描述，最多1024字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        if params.get("ItemLevels") is not None:
            self._ItemLevels = []
            for item in params.get("ItemLevels"):
                obj = ItemLevel()
                obj._deserialize(item)
                self._ItemLevels.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPALevelGroupResponse(AbstractModel):
    """CreateDSPALevelGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LevelGroupId: 分级组ID
        :type LevelGroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LevelGroupId = None
        self._RequestId = None

    @property
    def LevelGroupId(self):
        """分级组ID
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

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
        self._LevelGroupId = params.get("LevelGroupId")
        self._RequestId = params.get("RequestId")


class CreateDSPAMetaResourcesRequest(AbstractModel):
    """CreateDSPAMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _UpdateStatus: 用来标记本次更新是否已经是最后一次，可选值：continue（后续还需要更新）、finished（本次是最后一次更新）。
        :type UpdateStatus: str
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _Items: 资源列表。
        :type Items: list of DspaUserResourceMeta
        """
        self._MetaType = None
        self._ResourceRegion = None
        self._DspaId = None
        self._UpdateStatus = None
        self._UpdateId = None
        self._Items = None

    @property
    def MetaType(self):
        """资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def UpdateStatus(self):
        """用来标记本次更新是否已经是最后一次，可选值：continue（后续还需要更新）、finished（本次是最后一次更新）。
        :rtype: str
        """
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def UpdateId(self):
        """本次更新的ID号，用来标记一次完整的更新过程。
        :rtype: str
        """
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        self._UpdateId = UpdateId

    @property
    def Items(self):
        """资源列表。
        :rtype: list of DspaUserResourceMeta
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DspaId = params.get("DspaId")
        self._UpdateStatus = params.get("UpdateStatus")
        self._UpdateId = params.get("UpdateId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaUserResourceMeta()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPAMetaResourcesResponse(AbstractModel):
    """CreateDSPAMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpdateId = None
        self._MetaType = None
        self._DspaId = None
        self._ResourceRegion = None
        self._RequestId = None

    @property
    def UpdateId(self):
        """本次更新的ID号，用来标记一次完整的更新过程。
        :rtype: str
        """
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        self._UpdateId = UpdateId

    @property
    def MetaType(self):
        """资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

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
        self._UpdateId = params.get("UpdateId")
        self._MetaType = params.get("MetaType")
        self._DspaId = params.get("DspaId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._RequestId = params.get("RequestId")


class CreateDSPASelfBuildMetaResourceRequest(AbstractModel):
    """CreateDSPASelfBuildMetaResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: Dspa实例ID。
        :type DspaId: str
        :param _MetaType: 自建数据库类型。目前支持的自建数据库类型按照协议进行区分，支持两种开源数据库协议：
mysql_like_proto -- Mysql协议类关系型数据库，
postgre_like_proto -- Postgre协议类关系型数据库。
其他闭源协议的数据库如SqlServer、Oracle等暂不支持。
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourceId: 自建云资源ID。
        :type ResourceId: str
        :param _ResourceUniqueVpcId: 自建云资源的VPC ID。
        :type ResourceUniqueVpcId: str
        :param _ResourceUniqueSubnetId: 自建云资源的Subnet ID。
        :type ResourceUniqueSubnetId: str
        :param _ResourceAccessType: 自建云资源所处的服务类型，可选：
cvm - 通过云服务器直接访问。
clb - 通过LB的方式进行访问。
        :type ResourceAccessType: str
        :param _ResourceVip: 可用于访问自建云资源的IP。
emr的连接不需要使用该字段
        :type ResourceVip: str
        :param _ResourceVPort: 可用于访问自建云资源的端口。
emr的连接不需要使用该字段
        :type ResourceVPort: int
        :param _UserName: 账户名。如果emr_hive的连接方式为“LDAP”，则复用该字段
        :type UserName: str
        :param _Password: 账户密码。如果emr_hive的连接方式为“LDAP”，则复用该字段
        :type Password: str
        :param _ResourceName: 资源名称，1-60个字符。
        :type ResourceName: str
        :param _InstanceType: 实例类型
databse
sid
serviceName
        :type InstanceType: str
        :param _InstanceValue: 实例值
        :type InstanceValue: str
        :param _AuthRange: 授权范围（all:授权整个数据源 manual:手动指定数据库）
        :type AuthRange: str
        """
        self._DspaId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._ResourceId = None
        self._ResourceUniqueVpcId = None
        self._ResourceUniqueSubnetId = None
        self._ResourceAccessType = None
        self._ResourceVip = None
        self._ResourceVPort = None
        self._UserName = None
        self._Password = None
        self._ResourceName = None
        self._InstanceType = None
        self._InstanceValue = None
        self._AuthRange = None

    @property
    def DspaId(self):
        """Dspa实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MetaType(self):
        """自建数据库类型。目前支持的自建数据库类型按照协议进行区分，支持两种开源数据库协议：
mysql_like_proto -- Mysql协议类关系型数据库，
postgre_like_proto -- Postgre协议类关系型数据库。
其他闭源协议的数据库如SqlServer、Oracle等暂不支持。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceId(self):
        """自建云资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceUniqueVpcId(self):
        """自建云资源的VPC ID。
        :rtype: str
        """
        return self._ResourceUniqueVpcId

    @ResourceUniqueVpcId.setter
    def ResourceUniqueVpcId(self, ResourceUniqueVpcId):
        self._ResourceUniqueVpcId = ResourceUniqueVpcId

    @property
    def ResourceUniqueSubnetId(self):
        """自建云资源的Subnet ID。
        :rtype: str
        """
        return self._ResourceUniqueSubnetId

    @ResourceUniqueSubnetId.setter
    def ResourceUniqueSubnetId(self, ResourceUniqueSubnetId):
        self._ResourceUniqueSubnetId = ResourceUniqueSubnetId

    @property
    def ResourceAccessType(self):
        """自建云资源所处的服务类型，可选：
cvm - 通过云服务器直接访问。
clb - 通过LB的方式进行访问。
        :rtype: str
        """
        return self._ResourceAccessType

    @ResourceAccessType.setter
    def ResourceAccessType(self, ResourceAccessType):
        self._ResourceAccessType = ResourceAccessType

    @property
    def ResourceVip(self):
        """可用于访问自建云资源的IP。
emr的连接不需要使用该字段
        :rtype: str
        """
        return self._ResourceVip

    @ResourceVip.setter
    def ResourceVip(self, ResourceVip):
        self._ResourceVip = ResourceVip

    @property
    def ResourceVPort(self):
        """可用于访问自建云资源的端口。
emr的连接不需要使用该字段
        :rtype: int
        """
        return self._ResourceVPort

    @ResourceVPort.setter
    def ResourceVPort(self, ResourceVPort):
        self._ResourceVPort = ResourceVPort

    @property
    def UserName(self):
        """账户名。如果emr_hive的连接方式为“LDAP”，则复用该字段
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """账户密码。如果emr_hive的连接方式为“LDAP”，则复用该字段
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ResourceName(self):
        """资源名称，1-60个字符。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def InstanceType(self):
        """实例类型
databse
sid
serviceName
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceValue(self):
        """实例值
        :rtype: str
        """
        return self._InstanceValue

    @InstanceValue.setter
    def InstanceValue(self, InstanceValue):
        self._InstanceValue = InstanceValue

    @property
    def AuthRange(self):
        """授权范围（all:授权整个数据源 manual:手动指定数据库）
        :rtype: str
        """
        return self._AuthRange

    @AuthRange.setter
    def AuthRange(self, AuthRange):
        self._AuthRange = AuthRange


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceId = params.get("ResourceId")
        self._ResourceUniqueVpcId = params.get("ResourceUniqueVpcId")
        self._ResourceUniqueSubnetId = params.get("ResourceUniqueSubnetId")
        self._ResourceAccessType = params.get("ResourceAccessType")
        self._ResourceVip = params.get("ResourceVip")
        self._ResourceVPort = params.get("ResourceVPort")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._ResourceName = params.get("ResourceName")
        self._InstanceType = params.get("InstanceType")
        self._InstanceValue = params.get("InstanceValue")
        self._AuthRange = params.get("AuthRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPASelfBuildMetaResourceResponse(AbstractModel):
    """CreateDSPASelfBuildMetaResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectivityStatus: 连通性测试情况，success表示可正常访问，failed表示无法访问。
        :type ConnectivityStatus: str
        :param _ConnectivityDescription: 连通性描述字段，如果连通性测试失败，这里会返回无法访问的相关信息说明。
        :type ConnectivityDescription: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConnectivityStatus = None
        self._ConnectivityDescription = None
        self._RequestId = None

    @property
    def ConnectivityStatus(self):
        """连通性测试情况，success表示可正常访问，failed表示无法访问。
        :rtype: str
        """
        return self._ConnectivityStatus

    @ConnectivityStatus.setter
    def ConnectivityStatus(self, ConnectivityStatus):
        self._ConnectivityStatus = ConnectivityStatus

    @property
    def ConnectivityDescription(self):
        """连通性描述字段，如果连通性测试失败，这里会返回无法访问的相关信息说明。
        :rtype: str
        """
        return self._ConnectivityDescription

    @ConnectivityDescription.setter
    def ConnectivityDescription(self, ConnectivityDescription):
        self._ConnectivityDescription = ConnectivityDescription

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
        self._ConnectivityStatus = params.get("ConnectivityStatus")
        self._ConnectivityDescription = params.get("ConnectivityDescription")
        self._RequestId = params.get("RequestId")


class CreateIdentifyRuleAnotherNameRequest(AbstractModel):
    """CreateIdentifyRuleAnotherName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _CategoryId: 规则绑定的分类id
        :type CategoryId: int
        :param _RuleId: 规则id
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _AnotherName: 规则别名
        :type AnotherName: str
        :param _AliasRuleId: 别名规则id
        :type AliasRuleId: int
        :param _AliasRuleName: 别名规则名称
        :type AliasRuleName: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._CategoryId = None
        self._RuleId = None
        self._RuleName = None
        self._AnotherName = None
        self._AliasRuleId = None
        self._AliasRuleName = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def CategoryId(self):
        """规则绑定的分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def AnotherName(self):
        """规则别名
        :rtype: str
        """
        return self._AnotherName

    @AnotherName.setter
    def AnotherName(self, AnotherName):
        self._AnotherName = AnotherName

    @property
    def AliasRuleId(self):
        """别名规则id
        :rtype: int
        """
        return self._AliasRuleId

    @AliasRuleId.setter
    def AliasRuleId(self, AliasRuleId):
        self._AliasRuleId = AliasRuleId

    @property
    def AliasRuleName(self):
        """别名规则名称
        :rtype: str
        """
        return self._AliasRuleName

    @AliasRuleName.setter
    def AliasRuleName(self, AliasRuleName):
        self._AliasRuleName = AliasRuleName


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._CategoryId = params.get("CategoryId")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._AnotherName = params.get("AnotherName")
        self._AliasRuleId = params.get("AliasRuleId")
        self._AliasRuleName = params.get("AliasRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIdentifyRuleAnotherNameResponse(AbstractModel):
    """CreateIdentifyRuleAnotherName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasRuleId: 创建的别名规则id
        :type AliasRuleId: int
        :param _AliasRuleName: 别名规则名称
        :type AliasRuleName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AliasRuleId = None
        self._AliasRuleName = None
        self._RequestId = None

    @property
    def AliasRuleId(self):
        """创建的别名规则id
        :rtype: int
        """
        return self._AliasRuleId

    @AliasRuleId.setter
    def AliasRuleId(self, AliasRuleId):
        self._AliasRuleId = AliasRuleId

    @property
    def AliasRuleName(self):
        """别名规则名称
        :rtype: str
        """
        return self._AliasRuleName

    @AliasRuleName.setter
    def AliasRuleName(self, AliasRuleName):
        self._AliasRuleName = AliasRuleName

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
        self._AliasRuleId = params.get("AliasRuleId")
        self._AliasRuleName = params.get("AliasRuleName")
        self._RequestId = params.get("RequestId")


class DBInstanceInfo(AbstractModel):
    """绑定的实例信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 数据源id
        :type ResourceId: str
        :param _DbInfos: 数据源绑定的db信息
        :type DbInfos: list of DbInfo
        """
        self._ResourceId = None
        self._DbInfos = None

    @property
    def ResourceId(self):
        """数据源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DbInfos(self):
        """数据源绑定的db信息
        :rtype: list of DbInfo
        """
        return self._DbInfos

    @DbInfos.setter
    def DbInfos(self, DbInfos):
        self._DbInfos = DbInfos


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        if params.get("DbInfos") is not None:
            self._DbInfos = []
            for item in params.get("DbInfos"):
                obj = DbInfo()
                obj._deserialize(item)
                self._DbInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBStatements(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        r"""
        :param _DBName: 数据库名称
        :type DBName: str
        :param _DBSchema: 数据库Schema
        :type DBSchema: str
        """
        self._DBName = None
        self._DBSchema = None

    @property
    def DBName(self):
        """数据库名称
        :rtype: str
        """
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def DBSchema(self):
        """数据库Schema
        :rtype: str
        """
        return self._DBSchema

    @DBSchema.setter
    def DBSchema(self, DBSchema):
        self._DBSchema = DBSchema


    def _deserialize(self, params):
        self._DBName = params.get("DBName")
        self._DBSchema = params.get("DBSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DSPACosMetaDataInfo(AbstractModel):
    """COS元数据信息

    """

    def __init__(self):
        r"""
        :param _Bucket: COS桶名
        :type Bucket: str
        :param _CreateTime: COS桶创建时间
        :type CreateTime: str
        :param _Valid: 1 -- 有效，0 -- 无效，资源可能已被删除。
        :type Valid: int
        :param _ResourceId: DSPA为COS资源生成的资源ID
        :type ResourceId: str
        :param _ResourceRegion: COS资源所处的地域
        :type ResourceRegion: str
        :param _BindStatus: COS桶绑定状态
        :type BindStatus: str
        :param _Storage: COS桶存储量
        :type Storage: float
        :param _GovernAuthStatus: 治理授权状态，0:关闭 1：开启
        :type GovernAuthStatus: int
        """
        self._Bucket = None
        self._CreateTime = None
        self._Valid = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._BindStatus = None
        self._Storage = None
        self._GovernAuthStatus = None

    @property
    def Bucket(self):
        """COS桶名
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def CreateTime(self):
        """COS桶创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Valid(self):
        """1 -- 有效，0 -- 无效，资源可能已被删除。
        :rtype: int
        """
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid

    @property
    def ResourceId(self):
        """DSPA为COS资源生成的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """COS资源所处的地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def BindStatus(self):
        """COS桶绑定状态
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def Storage(self):
        """COS桶存储量
        :rtype: float
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def GovernAuthStatus(self):
        """治理授权状态，0:关闭 1：开启
        :rtype: int
        """
        return self._GovernAuthStatus

    @GovernAuthStatus.setter
    def GovernAuthStatus(self, GovernAuthStatus):
        self._GovernAuthStatus = GovernAuthStatus


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._CreateTime = params.get("CreateTime")
        self._Valid = params.get("Valid")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._BindStatus = params.get("BindStatus")
        self._Storage = params.get("Storage")
        self._GovernAuthStatus = params.get("GovernAuthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DSPADataSourceDbInfo(AbstractModel):
    """DSPA数据源的数据库信息

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DSPAMetaType(AbstractModel):
    """元数据类型

    """

    def __init__(self):
        r"""
        :param _MetaType: 元数据类型
        :type MetaType: str
        :param _Regions: 支持的此元数据类型的地域列表
        :type Regions: list of str
        :param _SupportedAuthTypes: 此元数据类型支持的授权类型：
account    -- 账户名密码授权，账户的最高只读权限需要由用户自行赋予；
automatic -- 一键授权，由DSPA自动生成账户名密码并自动在实例中给账户名赋予最高只读权限；
如果此列表为空，表明此类资源不支持以上的授权机制，无法通过后台进行授权。
        :type SupportedAuthTypes: list of str
        """
        self._MetaType = None
        self._Regions = None
        self._SupportedAuthTypes = None

    @property
    def MetaType(self):
        """元数据类型
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def Regions(self):
        """支持的此元数据类型的地域列表
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def SupportedAuthTypes(self):
        """此元数据类型支持的授权类型：
account    -- 账户名密码授权，账户的最高只读权限需要由用户自行赋予；
automatic -- 一键授权，由DSPA自动生成账户名密码并自动在实例中给账户名赋予最高只读权限；
如果此列表为空，表明此类资源不支持以上的授权机制，无法通过后台进行授权。
        :rtype: list of str
        """
        return self._SupportedAuthTypes

    @SupportedAuthTypes.setter
    def SupportedAuthTypes(self, SupportedAuthTypes):
        self._SupportedAuthTypes = SupportedAuthTypes


    def _deserialize(self, params):
        self._MetaType = params.get("MetaType")
        self._Regions = params.get("Regions")
        self._SupportedAuthTypes = params.get("SupportedAuthTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DSPATableInfo(AbstractModel):
    """DSPA分类分级任务扫描的表信息

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
        :type TableName: str
        """
        self._TableName = None

    @property
    def TableName(self):
        """表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCategory(AbstractModel):
    """敏感数据分类

    """

    def __init__(self):
        r"""
        :param _CategoryId: 分类ID
        :type CategoryId: int
        :param _Name: 敏感数据分类名称
        :type Name: str
        :param _Source: 敏感数据分类来源，取值：0 内置, 1 自定义
        :type Source: int
        :param _RelateComplianceCount: 关联模板数量
        :type RelateComplianceCount: int
        """
        self._CategoryId = None
        self._Name = None
        self._Source = None
        self._RelateComplianceCount = None

    @property
    def CategoryId(self):
        """分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Name(self):
        """敏感数据分类名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        """敏感数据分类来源，取值：0 内置, 1 自定义
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def RelateComplianceCount(self):
        """关联模板数量
        :rtype: int
        """
        return self._RelateComplianceCount

    @RelateComplianceCount.setter
    def RelateComplianceCount(self, RelateComplianceCount):
        self._RelateComplianceCount = RelateComplianceCount


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._RelateComplianceCount = params.get("RelateComplianceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataContent(AbstractModel):
    """扫描规则内容

    """

    def __init__(self):
        r"""
        :param _RuleContent: 规则内容，可以是正则规则，关键词，
忽略词扥
        :type RuleContent: str
        :param _IsIgnoreCase: 是否区分大小写
false: 不区分大小写
true:区分大小写
        :type IsIgnoreCase: bool
        """
        self._RuleContent = None
        self._IsIgnoreCase = None

    @property
    def RuleContent(self):
        """规则内容，可以是正则规则，关键词，
忽略词扥
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def IsIgnoreCase(self):
        """是否区分大小写
false: 不区分大小写
true:区分大小写
        :rtype: bool
        """
        return self._IsIgnoreCase

    @IsIgnoreCase.setter
    def IsIgnoreCase(self, IsIgnoreCase):
        self._IsIgnoreCase = IsIgnoreCase


    def _deserialize(self, params):
        self._RuleContent = params.get("RuleContent")
        self._IsIgnoreCase = params.get("IsIgnoreCase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataRule(AbstractModel):
    """敏感数据识别规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型；取值：
keyword 关键字, 
regex 正则
        :type RuleType: str
        :param _RuleContent: 内容
        :type RuleContent: str
        :param _ExtendParameters: 该字段是针对规则类型RuleType为keyword类型时的一个扩展属性
        :type ExtendParameters: list of DatagovRuleExtendParameter
        """
        self._RuleType = None
        self._RuleContent = None
        self._ExtendParameters = None

    @property
    def RuleType(self):
        """规则类型；取值：
keyword 关键字, 
regex 正则
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleContent(self):
        """内容
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def ExtendParameters(self):
        """该字段是针对规则类型RuleType为keyword类型时的一个扩展属性
        :rtype: list of DatagovRuleExtendParameter
        """
        return self._ExtendParameters

    @ExtendParameters.setter
    def ExtendParameters(self, ExtendParameters):
        self._ExtendParameters = ExtendParameters


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleContent = params.get("RuleContent")
        if params.get("ExtendParameters") is not None:
            self._ExtendParameters = []
            for item in params.get("ExtendParameters"):
                obj = DatagovRuleExtendParameter()
                obj._deserialize(item)
                self._ExtendParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataRules(AbstractModel):
    """敏感数据识别规则集

    """

    def __init__(self):
        r"""
        :param _Operator: 操作符；只能取and, or的其中一种
        :type Operator: str
        :param _Contents: 规则
        :type Contents: list of DataRule
        """
        self._Operator = None
        self._Contents = None

    @property
    def Operator(self):
        """操作符；只能取and, or的其中一种
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Contents(self):
        """规则
        :rtype: list of DataRule
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = DataRule()
                obj._deserialize(item)
                self._Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceInfo(AbstractModel):
    """dsgc-资产梳理报表-数据源信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _BindList: 针对rbd-就是绑定的db_name
        :type BindList: list of str
        """
        self._DataSourceId = None
        self._BindList = None

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def BindList(self):
        """针对rbd-就是绑定的db_name
        :rtype: list of str
        """
        return self._BindList

    @BindList.setter
    def BindList(self, BindList):
        self._BindList = BindList


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._BindList = params.get("BindList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatagovRuleExtendParameter(AbstractModel):
    """敏感数据识别规则扩展参数

    """

    def __init__(self):
        r"""
        :param _Name: 扩展参数名称，目前支持如下两个扩展属性名称：
IsFullWordMatch，表示是否全文匹配，该Name对应的Value可取值为"true"或"false":，默认值为"false"，
IsIgnoreCase，表示是否忽略大小写，该Name对应的Value可取值为"true"或"false"，默认值为"true"
        :type Name: str
        :param _Value: 扩展参数值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """扩展参数名称，目前支持如下两个扩展属性名称：
IsFullWordMatch，表示是否全文匹配，该Name对应的Value可取值为"true"或"false":，默认值为"false"，
IsIgnoreCase，表示是否忽略大小写，该Name对应的Value可取值为"true"或"false"，默认值为"true"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """扩展参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbInfo(AbstractModel):
    """查询绑定的db信息

    """

    def __init__(self):
        r"""
        :param _DbName: 数据库名称
        :type DbName: str
        :param _ValidStatus: 绑定的状态
        :type ValidStatus: str
        :param _BindType: 绑定的类型
        :type BindType: str
        """
        self._DbName = None
        self._ValidStatus = None
        self._BindType = None

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def ValidStatus(self):
        """绑定的状态
        :rtype: str
        """
        return self._ValidStatus

    @ValidStatus.setter
    def ValidStatus(self, ValidStatus):
        self._ValidStatus = ValidStatus

    @property
    def BindType(self):
        """绑定的类型
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._ValidStatus = params.get("ValidStatus")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbRelationStatusItem(AbstractModel):
    """数据库实例的DB绑定关系状态信息。

    """

    def __init__(self):
        r"""
        :param _DbName: DB名称。
        :type DbName: str
        :param _BindStatus: DB绑定状态。
        :type BindStatus: str
        :param _ValidStatus: DB有效性状态。
        :type ValidStatus: str
        """
        self._DbName = None
        self._BindStatus = None
        self._ValidStatus = None

    @property
    def DbName(self):
        """DB名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def BindStatus(self):
        """DB绑定状态。
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ValidStatus(self):
        """DB有效性状态。
        :rtype: str
        """
        return self._ValidStatus

    @ValidStatus.setter
    def ValidStatus(self, ValidStatus):
        self._ValidStatus = ValidStatus


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._BindStatus = params.get("BindStatus")
        self._ValidStatus = params.get("ValidStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbResourceItem(AbstractModel):
    """数据库DB资源项

    """

    def __init__(self):
        r"""
        :param _DbName: DB名称。
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        """DB名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbTaskResult(AbstractModel):
    """database批量操作返回结果结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果类型。
        :type Result: str
        :param _ResultDescription: 结果描述。
        :type ResultDescription: str
        :param _ErrDescription: 错误信息描述。
        :type ErrDescription: :class:`tencentcloud.dsgc.v20190723.models.ErrDescription`
        :param _ResourceId: 资源ID。
        :type ResourceId: str
        :param _DbName: database名称。
        :type DbName: str
        """
        self._Result = None
        self._ResultDescription = None
        self._ErrDescription = None
        self._ResourceId = None
        self._DbName = None

    @property
    def Result(self):
        """结果类型。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultDescription(self):
        """结果描述。
        :rtype: str
        """
        return self._ResultDescription

    @ResultDescription.setter
    def ResultDescription(self, ResultDescription):
        self._ResultDescription = ResultDescription

    @property
    def ErrDescription(self):
        """错误信息描述。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ErrDescription`
        """
        return self._ErrDescription

    @ErrDescription.setter
    def ErrDescription(self, ErrDescription):
        self._ErrDescription = ErrDescription

    @property
    def ResourceId(self):
        """资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DbName(self):
        """database名称。
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ResultDescription = params.get("ResultDescription")
        if params.get("ErrDescription") is not None:
            self._ErrDescription = ErrDescription()
            self._ErrDescription._deserialize(params.get("ErrDescription"))
        self._ResourceId = params.get("ResourceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecribeSuggestRiskLevelMatrixRequest(AbstractModel):
    """DecribeSuggestRiskLevelMatrix请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspaId

        :type DspaId: str
        :param _SensitiveLevelList: 分类分级等级列表
        :type SensitiveLevelList: list of RiskMatrixLevel
        :param _VulnerabilityLevelList: 脆弱项等级列表
        :type VulnerabilityLevelList: list of RiskMatrixLevel
        """
        self._DspaId = None
        self._SensitiveLevelList = None
        self._VulnerabilityLevelList = None

    @property
    def DspaId(self):
        """dspaId

        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def SensitiveLevelList(self):
        """分类分级等级列表
        :rtype: list of RiskMatrixLevel
        """
        return self._SensitiveLevelList

    @SensitiveLevelList.setter
    def SensitiveLevelList(self, SensitiveLevelList):
        self._SensitiveLevelList = SensitiveLevelList

    @property
    def VulnerabilityLevelList(self):
        """脆弱项等级列表
        :rtype: list of RiskMatrixLevel
        """
        return self._VulnerabilityLevelList

    @VulnerabilityLevelList.setter
    def VulnerabilityLevelList(self, VulnerabilityLevelList):
        self._VulnerabilityLevelList = VulnerabilityLevelList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        if params.get("SensitiveLevelList") is not None:
            self._SensitiveLevelList = []
            for item in params.get("SensitiveLevelList"):
                obj = RiskMatrixLevel()
                obj._deserialize(item)
                self._SensitiveLevelList.append(obj)
        if params.get("VulnerabilityLevelList") is not None:
            self._VulnerabilityLevelList = []
            for item in params.get("VulnerabilityLevelList"):
                obj = RiskMatrixLevel()
                obj._deserialize(item)
                self._VulnerabilityLevelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecribeSuggestRiskLevelMatrixResponse(AbstractModel):
    """DecribeSuggestRiskLevelMatrix返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuggestRiskLevelMatrix: 矩阵
        :type SuggestRiskLevelMatrix: list of SuggestRiskLevelMatrix
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuggestRiskLevelMatrix = None
        self._RequestId = None

    @property
    def SuggestRiskLevelMatrix(self):
        """矩阵
        :rtype: list of SuggestRiskLevelMatrix
        """
        return self._SuggestRiskLevelMatrix

    @SuggestRiskLevelMatrix.setter
    def SuggestRiskLevelMatrix(self, SuggestRiskLevelMatrix):
        self._SuggestRiskLevelMatrix = SuggestRiskLevelMatrix

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
        if params.get("SuggestRiskLevelMatrix") is not None:
            self._SuggestRiskLevelMatrix = []
            for item in params.get("SuggestRiskLevelMatrix"):
                obj = SuggestRiskLevelMatrix()
                obj._deserialize(item)
                self._SuggestRiskLevelMatrix.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteCosMetaResourceRequest(AbstractModel):
    """DeleteCosMetaResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: 实例Id。
        :type DspaId: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourceIds: 资源实例ID。
        :type ResourceIds: list of str
        """
        self._DspaId = None
        self._ResourceRegion = None
        self._ResourceIds = None

    @property
    def DspaId(self):
        """实例Id。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceIds(self):
        """资源实例ID。
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCosMetaResourceResponse(AbstractModel):
    """DeleteCosMetaResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 结果集合。
        :type Results: list of DspaTaskResult
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._DspaId = None
        self._RequestId = None

    @property
    def Results(self):
        """结果集合。
        :rtype: list of DspaTaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DspaTaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._DspaId = params.get("DspaId")
        self._RequestId = params.get("RequestId")


class DeleteDSPAAssessmentTaskRequest(AbstractModel):
    """DeleteDSPAAssessmentTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _TaskId: 评估任务Id，格式“task-xxxxxxxx”
        :type TaskId: str
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """评估任务Id，格式“task-xxxxxxxx”
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPAAssessmentTaskResponse(AbstractModel):
    """DeleteDSPAAssessmentTask返回参数结构体

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


class DeleteDSPACOSDiscoveryTaskRequest(AbstractModel):
    """DeleteDSPACOSDiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPACOSDiscoveryTaskResponse(AbstractModel):
    """DeleteDSPACOSDiscoveryTask返回参数结构体

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


class DeleteDSPACOSDiscoveryTaskResultRequest(AbstractModel):
    """DeleteDSPACOSDiscoveryTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _BucketResultId: 扫描bucket结果ID
        :type BucketResultId: int
        """
        self._DspaId = None
        self._BucketResultId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def BucketResultId(self):
        """扫描bucket结果ID
        :rtype: int
        """
        return self._BucketResultId

    @BucketResultId.setter
    def BucketResultId(self, BucketResultId):
        self._BucketResultId = BucketResultId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._BucketResultId = params.get("BucketResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPACOSDiscoveryTaskResultResponse(AbstractModel):
    """DeleteDSPACOSDiscoveryTaskResult返回参数结构体

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


class DeleteDSPADiscoveryTaskRequest(AbstractModel):
    """DeleteDSPADiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        """
        self._DspaId = None
        self._TaskId = None
        self._DataSourceType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPADiscoveryTaskResponse(AbstractModel):
    """DeleteDSPADiscoveryTask返回参数结构体

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


class DeleteDSPADiscoveryTaskResultRequest(AbstractModel):
    """DeleteDSPADiscoveryTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _DbResultId: 扫描数据库结果ID
        :type DbResultId: int
        """
        self._DspaId = None
        self._DbResultId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DbResultId(self):
        """扫描数据库结果ID
        :rtype: int
        """
        return self._DbResultId

    @DbResultId.setter
    def DbResultId(self, DbResultId):
        self._DbResultId = DbResultId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DbResultId = params.get("DbResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPADiscoveryTaskResultResponse(AbstractModel):
    """DeleteDSPADiscoveryTaskResult返回参数结构体

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


class DeleteDSPAMetaResourceRequest(AbstractModel):
    """DeleteDSPAMetaResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceIDs: 用户云资源ID。
        :type ResourceIDs: list of str
        """
        self._DspaId = None
        self._ResourceIDs = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceIDs(self):
        """用户云资源ID。
        :rtype: list of str
        """
        return self._ResourceIDs

    @ResourceIDs.setter
    def ResourceIDs(self, ResourceIDs):
        self._ResourceIDs = ResourceIDs


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceIDs = params.get("ResourceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDSPAMetaResourceResponse(AbstractModel):
    """DeleteDSPAMetaResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _Results: 删除结果。
        :type Results: list of DspaTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DspaId = None
        self._Results = None
        self._RequestId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Results(self):
        """删除结果。
        :rtype: list of DspaTaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        self._DspaId = params.get("DspaId")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DspaTaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetDetailDataExportResultRequest(AbstractModel):
    """DescribeAssetDetailDataExportResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportTaskId: 导出任务id
        :type ExportTaskId: int
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        """
        self._ExportTaskId = None
        self._DspaId = None

    @property
    def ExportTaskId(self):
        """导出任务id
        :rtype: int
        """
        return self._ExportTaskId

    @ExportTaskId.setter
    def ExportTaskId(self, ExportTaskId):
        self._ExportTaskId = ExportTaskId

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._ExportTaskId = params.get("ExportTaskId")
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailDataExportResultResponse(AbstractModel):
    """DescribeAssetDetailDataExportResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportResult: 导出结果
        :type ExportResult: str
        :param _ExportFileUrl: 导出文件地址
        :type ExportFileUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportResult = None
        self._ExportFileUrl = None
        self._RequestId = None

    @property
    def ExportResult(self):
        """导出结果
        :rtype: str
        """
        return self._ExportResult

    @ExportResult.setter
    def ExportResult(self, ExportResult):
        self._ExportResult = ExportResult

    @property
    def ExportFileUrl(self):
        """导出文件地址
        :rtype: str
        """
        return self._ExportFileUrl

    @ExportFileUrl.setter
    def ExportFileUrl(self, ExportFileUrl):
        self._ExportFileUrl = ExportFileUrl

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
        self._ExportResult = params.get("ExportResult")
        self._ExportFileUrl = params.get("ExportFileUrl")
        self._RequestId = params.get("RequestId")


class DescribeAssetOverviewRequest(AbstractModel):
    """DescribeAssetOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetOverviewResponse(AbstractModel):
    """DescribeAssetOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DBInstanceNums: 数据库实例id
        :type DBInstanceNums: int
        :param _DBNums: 数据库个数
        :type DBNums: int
        :param _TableNums: 表的个数
        :type TableNums: int
        :param _FieldNums: 字段个数
        :type FieldNums: int
        :param _DBInstanceDistribution: 数据库实例的分布情况
        :type DBInstanceDistribution: list of Note
        :param _DBDistribution: db分布情况
        :type DBDistribution: list of Note
        :param _BucketNums: cos桶的数量
        :type BucketNums: int
        :param _FileNums: 文件个数
        :type FileNums: int
        :param _Remark: 用于对用户进行提示信息
        :type Remark: str
        :param _EsInstanceNums: es实例数量
        :type EsInstanceNums: int
        :param _EsIndexNums: es索引数量
        :type EsIndexNums: int
        :param _EsFieldNums: es字段数量
        :type EsFieldNums: int
        :param _MongoInstanceNums: mongo实例数量
        :type MongoInstanceNums: int
        :param _MongoDbNums: mongo数据库数量
        :type MongoDbNums: int
        :param _MongoColNums: mongo集合数量
        :type MongoColNums: int
        :param _MongoFieldNums: mongo字段数量
        :type MongoFieldNums: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DBInstanceNums = None
        self._DBNums = None
        self._TableNums = None
        self._FieldNums = None
        self._DBInstanceDistribution = None
        self._DBDistribution = None
        self._BucketNums = None
        self._FileNums = None
        self._Remark = None
        self._EsInstanceNums = None
        self._EsIndexNums = None
        self._EsFieldNums = None
        self._MongoInstanceNums = None
        self._MongoDbNums = None
        self._MongoColNums = None
        self._MongoFieldNums = None
        self._RequestId = None

    @property
    def DBInstanceNums(self):
        """数据库实例id
        :rtype: int
        """
        return self._DBInstanceNums

    @DBInstanceNums.setter
    def DBInstanceNums(self, DBInstanceNums):
        self._DBInstanceNums = DBInstanceNums

    @property
    def DBNums(self):
        """数据库个数
        :rtype: int
        """
        return self._DBNums

    @DBNums.setter
    def DBNums(self, DBNums):
        self._DBNums = DBNums

    @property
    def TableNums(self):
        """表的个数
        :rtype: int
        """
        return self._TableNums

    @TableNums.setter
    def TableNums(self, TableNums):
        self._TableNums = TableNums

    @property
    def FieldNums(self):
        """字段个数
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def DBInstanceDistribution(self):
        """数据库实例的分布情况
        :rtype: list of Note
        """
        return self._DBInstanceDistribution

    @DBInstanceDistribution.setter
    def DBInstanceDistribution(self, DBInstanceDistribution):
        self._DBInstanceDistribution = DBInstanceDistribution

    @property
    def DBDistribution(self):
        """db分布情况
        :rtype: list of Note
        """
        return self._DBDistribution

    @DBDistribution.setter
    def DBDistribution(self, DBDistribution):
        self._DBDistribution = DBDistribution

    @property
    def BucketNums(self):
        """cos桶的数量
        :rtype: int
        """
        return self._BucketNums

    @BucketNums.setter
    def BucketNums(self, BucketNums):
        self._BucketNums = BucketNums

    @property
    def FileNums(self):
        """文件个数
        :rtype: int
        """
        return self._FileNums

    @FileNums.setter
    def FileNums(self, FileNums):
        self._FileNums = FileNums

    @property
    def Remark(self):
        """用于对用户进行提示信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EsInstanceNums(self):
        """es实例数量
        :rtype: int
        """
        return self._EsInstanceNums

    @EsInstanceNums.setter
    def EsInstanceNums(self, EsInstanceNums):
        self._EsInstanceNums = EsInstanceNums

    @property
    def EsIndexNums(self):
        """es索引数量
        :rtype: int
        """
        return self._EsIndexNums

    @EsIndexNums.setter
    def EsIndexNums(self, EsIndexNums):
        self._EsIndexNums = EsIndexNums

    @property
    def EsFieldNums(self):
        """es字段数量
        :rtype: int
        """
        return self._EsFieldNums

    @EsFieldNums.setter
    def EsFieldNums(self, EsFieldNums):
        self._EsFieldNums = EsFieldNums

    @property
    def MongoInstanceNums(self):
        """mongo实例数量
        :rtype: int
        """
        return self._MongoInstanceNums

    @MongoInstanceNums.setter
    def MongoInstanceNums(self, MongoInstanceNums):
        self._MongoInstanceNums = MongoInstanceNums

    @property
    def MongoDbNums(self):
        """mongo数据库数量
        :rtype: int
        """
        return self._MongoDbNums

    @MongoDbNums.setter
    def MongoDbNums(self, MongoDbNums):
        self._MongoDbNums = MongoDbNums

    @property
    def MongoColNums(self):
        """mongo集合数量
        :rtype: int
        """
        return self._MongoColNums

    @MongoColNums.setter
    def MongoColNums(self, MongoColNums):
        self._MongoColNums = MongoColNums

    @property
    def MongoFieldNums(self):
        """mongo字段数量
        :rtype: int
        """
        return self._MongoFieldNums

    @MongoFieldNums.setter
    def MongoFieldNums(self, MongoFieldNums):
        self._MongoFieldNums = MongoFieldNums

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
        self._DBInstanceNums = params.get("DBInstanceNums")
        self._DBNums = params.get("DBNums")
        self._TableNums = params.get("TableNums")
        self._FieldNums = params.get("FieldNums")
        if params.get("DBInstanceDistribution") is not None:
            self._DBInstanceDistribution = []
            for item in params.get("DBInstanceDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._DBInstanceDistribution.append(obj)
        if params.get("DBDistribution") is not None:
            self._DBDistribution = []
            for item in params.get("DBDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._DBDistribution.append(obj)
        self._BucketNums = params.get("BucketNums")
        self._FileNums = params.get("FileNums")
        self._Remark = params.get("Remark")
        self._EsInstanceNums = params.get("EsInstanceNums")
        self._EsIndexNums = params.get("EsIndexNums")
        self._EsFieldNums = params.get("EsFieldNums")
        self._MongoInstanceNums = params.get("MongoInstanceNums")
        self._MongoDbNums = params.get("MongoDbNums")
        self._MongoColNums = params.get("MongoColNums")
        self._MongoFieldNums = params.get("MongoFieldNums")
        self._RequestId = params.get("RequestId")


class DescribeBindDBListRequest(AbstractModel):
    """DescribeBindDBList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        """
        self._DspaId = None
        self._DataSourceType = None
        self._DataSourceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DataSourceType(self):
        warnings.warn("parameter `DataSourceType` is deprecated", DeprecationWarning) 

        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        warnings.warn("parameter `DataSourceType` is deprecated", DeprecationWarning) 

        self._DataSourceType = DataSourceType

    @property
    def DataSourceId(self):
        warnings.warn("parameter `DataSourceId` is deprecated", DeprecationWarning) 

        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        warnings.warn("parameter `DataSourceId` is deprecated", DeprecationWarning) 

        self._DataSourceId = DataSourceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DataSourceType = params.get("DataSourceType")
        self._DataSourceId = params.get("DataSourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindDBListResponse(AbstractModel):
    """DescribeBindDBList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindDBList: 绑定的DB列表（已废弃）
        :type BindDBList: list of str
        :param _BindList: 绑定信息
        :type BindList: list of DBInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindDBList = None
        self._BindList = None
        self._RequestId = None

    @property
    def BindDBList(self):
        """绑定的DB列表（已废弃）
        :rtype: list of str
        """
        return self._BindDBList

    @BindDBList.setter
    def BindDBList(self, BindDBList):
        self._BindDBList = BindDBList

    @property
    def BindList(self):
        """绑定信息
        :rtype: list of DBInstanceInfo
        """
        return self._BindList

    @BindList.setter
    def BindList(self, BindList):
        self._BindList = BindList

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
        self._BindDBList = params.get("BindDBList")
        if params.get("BindList") is not None:
            self._BindList = []
            for item in params.get("BindList"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._BindList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCOSAssetSensitiveDistributionRequest(AbstractModel):
    """DescribeCOSAssetSensitiveDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCOSAssetSensitiveDistributionResponse(AbstractModel):
    """DescribeCOSAssetSensitiveDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosAsset: cos的涉敏资产
        :type CosAsset: :class:`tencentcloud.dsgc.v20190723.models.CosAsset`
        :param _TopAsset: 涉敏top
        :type TopAsset: list of TopAsset
        :param _CosDetail: cos资产详情列表
        :type CosDetail: list of AssetCosDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosAsset = None
        self._TopAsset = None
        self._CosDetail = None
        self._RequestId = None

    @property
    def CosAsset(self):
        """cos的涉敏资产
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CosAsset`
        """
        return self._CosAsset

    @CosAsset.setter
    def CosAsset(self, CosAsset):
        self._CosAsset = CosAsset

    @property
    def TopAsset(self):
        """涉敏top
        :rtype: list of TopAsset
        """
        return self._TopAsset

    @TopAsset.setter
    def TopAsset(self, TopAsset):
        self._TopAsset = TopAsset

    @property
    def CosDetail(self):
        """cos资产详情列表
        :rtype: list of AssetCosDetail
        """
        return self._CosDetail

    @CosDetail.setter
    def CosDetail(self, CosDetail):
        self._CosDetail = CosDetail

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
        if params.get("CosAsset") is not None:
            self._CosAsset = CosAsset()
            self._CosAsset._deserialize(params.get("CosAsset"))
        if params.get("TopAsset") is not None:
            self._TopAsset = []
            for item in params.get("TopAsset"):
                obj = TopAsset()
                obj._deserialize(item)
                self._TopAsset.append(obj)
        if params.get("CosDetail") is not None:
            self._CosDetail = []
            for item in params.get("CosDetail"):
                obj = AssetCosDetail()
                obj._deserialize(item)
                self._CosDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentHighRiskTop10OverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentHighRiskTop10Overview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例Id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        :param _Filter: 过滤条件， rdb（数据库）cos（对象存储）
不传就是全部
        :type Filter: str
        """
        self._DspaId = None
        self._TemplateId = None
        self._Filter = None

    @property
    def DspaId(self):
        """dspa实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Filter(self):
        """过滤条件， rdb（数据库）cos（对象存储）
不传就是全部
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentHighRiskTop10OverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentHighRiskTop10Overview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetsList: 含高风险资产TOP10的列表数据
        :type AssetsList: list of HighRiskAssetsDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetsList = None
        self._RequestId = None

    @property
    def AssetsList(self):
        """含高风险资产TOP10的列表数据
        :rtype: list of HighRiskAssetsDetail
        """
        return self._AssetsList

    @AssetsList.setter
    def AssetsList(self, AssetsList):
        self._AssetsList = AssetsList

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
        if params.get("AssetsList") is not None:
            self._AssetsList = []
            for item in params.get("AssetsList"):
                obj = HighRiskAssetsDetail()
                obj._deserialize(item)
                self._AssetsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentLatestRiskDetailInfoRequest(AbstractModel):
    """DescribeDSPAAssessmentLatestRiskDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例Id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        :param _RiskId: 风险id
        :type RiskId: int
        """
        self._DspaId = None
        self._TemplateId = None
        self._RiskId = None

    @property
    def DspaId(self):
        """dspa实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RiskId(self):
        """风险id
        :rtype: int
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._RiskId = params.get("RiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentLatestRiskDetailInfoResponse(AbstractModel):
    """DescribeDSPAAssessmentLatestRiskDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DataSourceName: 数据源name
        :type DataSourceName: str
        :param _AssetName: 资产对象名称
        :type AssetName: str
        :param _AssessmentTemplateId: 风险评估模板id
        :type AssessmentTemplateId: int
        :param _IdentifyTemplateId: 分类分级的模板id
        :type IdentifyTemplateId: int
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _RiskName: 风险项
        :type RiskName: str
        :param _RiskDescription: 风险的描述
        :type RiskDescription: str
        :param _RiskLevel: 风险的级别
        :type RiskLevel: str
        :param _SuggestAction: 处置的建议
        :type SuggestAction: str
        :param _Status: 处置状态
        :type Status: int
        :param _Remark: 备注
        :type Remark: str
        :param _SecurityProduct: 安全产品
        :type SecurityProduct: list of SecurityProduct
        :param _RiskDimension: 风险归属
        :type RiskDimension: str
        :param _RelationAsset: 关联数据库（如果风险归属是instance）
        :type RelationAsset: list of str
        :param _AccountRiskDetail: 风险账号详情
        :type AccountRiskDetail: list of AccountRisk
        :param _PrivilegeRiskDetail: 权限风险详情
        :type PrivilegeRiskDetail: list of PrivilegeRisk
        :param _PolicyRiskCosFileList: 策略风险的cos风险文件列表
        :type PolicyRiskCosFileList: list of str
        :param _AKSKLeak: AKSK泄漏列表
        :type AKSKLeak: list of AKSKLeak
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataSourceId = None
        self._DataSourceName = None
        self._AssetName = None
        self._AssessmentTemplateId = None
        self._IdentifyTemplateId = None
        self._RiskType = None
        self._RiskName = None
        self._RiskDescription = None
        self._RiskLevel = None
        self._SuggestAction = None
        self._Status = None
        self._Remark = None
        self._SecurityProduct = None
        self._RiskDimension = None
        self._RelationAsset = None
        self._AccountRiskDetail = None
        self._PrivilegeRiskDetail = None
        self._PolicyRiskCosFileList = None
        self._AKSKLeak = None
        self._RequestId = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceName(self):
        """数据源name
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def AssetName(self):
        """资产对象名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssessmentTemplateId(self):
        """风险评估模板id
        :rtype: int
        """
        return self._AssessmentTemplateId

    @AssessmentTemplateId.setter
    def AssessmentTemplateId(self, AssessmentTemplateId):
        self._AssessmentTemplateId = AssessmentTemplateId

    @property
    def IdentifyTemplateId(self):
        """分类分级的模板id
        :rtype: int
        """
        return self._IdentifyTemplateId

    @IdentifyTemplateId.setter
    def IdentifyTemplateId(self, IdentifyTemplateId):
        self._IdentifyTemplateId = IdentifyTemplateId

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def RiskName(self):
        """风险项
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskDescription(self):
        """风险的描述
        :rtype: str
        """
        return self._RiskDescription

    @RiskDescription.setter
    def RiskDescription(self, RiskDescription):
        self._RiskDescription = RiskDescription

    @property
    def RiskLevel(self):
        """风险的级别
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def SuggestAction(self):
        """处置的建议
        :rtype: str
        """
        return self._SuggestAction

    @SuggestAction.setter
    def SuggestAction(self, SuggestAction):
        self._SuggestAction = SuggestAction

    @property
    def Status(self):
        """处置状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SecurityProduct(self):
        """安全产品
        :rtype: list of SecurityProduct
        """
        return self._SecurityProduct

    @SecurityProduct.setter
    def SecurityProduct(self, SecurityProduct):
        self._SecurityProduct = SecurityProduct

    @property
    def RiskDimension(self):
        """风险归属
        :rtype: str
        """
        return self._RiskDimension

    @RiskDimension.setter
    def RiskDimension(self, RiskDimension):
        self._RiskDimension = RiskDimension

    @property
    def RelationAsset(self):
        """关联数据库（如果风险归属是instance）
        :rtype: list of str
        """
        return self._RelationAsset

    @RelationAsset.setter
    def RelationAsset(self, RelationAsset):
        self._RelationAsset = RelationAsset

    @property
    def AccountRiskDetail(self):
        """风险账号详情
        :rtype: list of AccountRisk
        """
        return self._AccountRiskDetail

    @AccountRiskDetail.setter
    def AccountRiskDetail(self, AccountRiskDetail):
        self._AccountRiskDetail = AccountRiskDetail

    @property
    def PrivilegeRiskDetail(self):
        """权限风险详情
        :rtype: list of PrivilegeRisk
        """
        return self._PrivilegeRiskDetail

    @PrivilegeRiskDetail.setter
    def PrivilegeRiskDetail(self, PrivilegeRiskDetail):
        self._PrivilegeRiskDetail = PrivilegeRiskDetail

    @property
    def PolicyRiskCosFileList(self):
        """策略风险的cos风险文件列表
        :rtype: list of str
        """
        return self._PolicyRiskCosFileList

    @PolicyRiskCosFileList.setter
    def PolicyRiskCosFileList(self, PolicyRiskCosFileList):
        self._PolicyRiskCosFileList = PolicyRiskCosFileList

    @property
    def AKSKLeak(self):
        """AKSK泄漏列表
        :rtype: list of AKSKLeak
        """
        return self._AKSKLeak

    @AKSKLeak.setter
    def AKSKLeak(self, AKSKLeak):
        self._AKSKLeak = AKSKLeak

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
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceName = params.get("DataSourceName")
        self._AssetName = params.get("AssetName")
        self._AssessmentTemplateId = params.get("AssessmentTemplateId")
        self._IdentifyTemplateId = params.get("IdentifyTemplateId")
        self._RiskType = params.get("RiskType")
        self._RiskName = params.get("RiskName")
        self._RiskDescription = params.get("RiskDescription")
        self._RiskLevel = params.get("RiskLevel")
        self._SuggestAction = params.get("SuggestAction")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        if params.get("SecurityProduct") is not None:
            self._SecurityProduct = []
            for item in params.get("SecurityProduct"):
                obj = SecurityProduct()
                obj._deserialize(item)
                self._SecurityProduct.append(obj)
        self._RiskDimension = params.get("RiskDimension")
        self._RelationAsset = params.get("RelationAsset")
        if params.get("AccountRiskDetail") is not None:
            self._AccountRiskDetail = []
            for item in params.get("AccountRiskDetail"):
                obj = AccountRisk()
                obj._deserialize(item)
                self._AccountRiskDetail.append(obj)
        if params.get("PrivilegeRiskDetail") is not None:
            self._PrivilegeRiskDetail = []
            for item in params.get("PrivilegeRiskDetail"):
                obj = PrivilegeRisk()
                obj._deserialize(item)
                self._PrivilegeRiskDetail.append(obj)
        self._PolicyRiskCosFileList = params.get("PolicyRiskCosFileList")
        if params.get("AKSKLeak") is not None:
            self._AKSKLeak = []
            for item in params.get("AKSKLeak"):
                obj = AKSKLeak()
                obj._deserialize(item)
                self._AKSKLeak.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentLatestRiskListRequest(AbstractModel):
    """DescribeDSPAAssessmentLatestRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例Id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: str
        :param _DataSourceId: 资产名称，数据源id
        :type DataSourceId: str
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _ControlItemId: 风险项
        :type ControlItemId: str
        :param _Status: 风险状态
        :type Status: int
        :param _BeginTime: 扫描开始时间
        :type BeginTime: str
        :param _EndTime: 扫描结束时间
        :type EndTime: str
        :param _RiskLevel: 风险等级筛选
        :type RiskLevel: str
        :param _RiskSide: 风险面筛选
        :type RiskSide: list of str
        :param _TimeSort: ASC 正序，DESC倒叙
        :type TimeSort: str
        """
        self._DspaId = None
        self._TemplateId = None
        self._Limit = None
        self._Offset = None
        self._DataSourceId = None
        self._RiskType = None
        self._ControlItemId = None
        self._Status = None
        self._BeginTime = None
        self._EndTime = None
        self._RiskLevel = None
        self._RiskSide = None
        self._TimeSort = None

    @property
    def DspaId(self):
        """dspa实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DataSourceId(self):
        """资产名称，数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def ControlItemId(self):
        """风险项
        :rtype: str
        """
        return self._ControlItemId

    @ControlItemId.setter
    def ControlItemId(self, ControlItemId):
        self._ControlItemId = ControlItemId

    @property
    def Status(self):
        """风险状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginTime(self):
        """扫描开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """扫描结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RiskLevel(self):
        """风险等级筛选
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskSide(self):
        """风险面筛选
        :rtype: list of str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide

    @property
    def TimeSort(self):
        """ASC 正序，DESC倒叙
        :rtype: str
        """
        return self._TimeSort

    @TimeSort.setter
    def TimeSort(self, TimeSort):
        self._TimeSort = TimeSort


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._DataSourceId = params.get("DataSourceId")
        self._RiskType = params.get("RiskType")
        self._ControlItemId = params.get("ControlItemId")
        self._Status = params.get("Status")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskSide = params.get("RiskSide")
        self._TimeSort = params.get("TimeSort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentLatestRiskListResponse(AbstractModel):
    """DescribeDSPAAssessmentLatestRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LatestRiskList: 最新风险详情列表
        :type LatestRiskList: list of RiskItemInfo
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LatestRiskList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LatestRiskList(self):
        """最新风险详情列表
        :rtype: list of RiskItemInfo
        """
        return self._LatestRiskList

    @LatestRiskList.setter
    def LatestRiskList(self, LatestRiskList):
        self._LatestRiskList = LatestRiskList

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("LatestRiskList") is not None:
            self._LatestRiskList = []
            for item in params.get("LatestRiskList"):
                obj = RiskItemInfo()
                obj._deserialize(item)
                self._LatestRiskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentNewDiscoveredRiskOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentNewDiscoveredRiskOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentNewDiscoveredRiskOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentNewDiscoveredRiskOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NewDiscoveredRiskCount: 待处理的风险数
        :type NewDiscoveredRiskCount: int
        :param _AffectedAssetCount: 受影响的资产数
        :type AffectedAssetCount: int
        :param _WeekRatio: 周同比
        :type WeekRatio: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NewDiscoveredRiskCount = None
        self._AffectedAssetCount = None
        self._WeekRatio = None
        self._RequestId = None

    @property
    def NewDiscoveredRiskCount(self):
        """待处理的风险数
        :rtype: int
        """
        return self._NewDiscoveredRiskCount

    @NewDiscoveredRiskCount.setter
    def NewDiscoveredRiskCount(self, NewDiscoveredRiskCount):
        self._NewDiscoveredRiskCount = NewDiscoveredRiskCount

    @property
    def AffectedAssetCount(self):
        """受影响的资产数
        :rtype: int
        """
        return self._AffectedAssetCount

    @AffectedAssetCount.setter
    def AffectedAssetCount(self, AffectedAssetCount):
        self._AffectedAssetCount = AffectedAssetCount

    @property
    def WeekRatio(self):
        """周同比
        :rtype: float
        """
        return self._WeekRatio

    @WeekRatio.setter
    def WeekRatio(self, WeekRatio):
        self._WeekRatio = WeekRatio

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
        self._NewDiscoveredRiskCount = params.get("NewDiscoveredRiskCount")
        self._AffectedAssetCount = params.get("AffectedAssetCount")
        self._WeekRatio = params.get("WeekRatio")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentPendingRiskOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentPendingRiskOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentPendingRiskOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentPendingRiskOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PendingRiskCount: 待处理的风险数
        :type PendingRiskCount: int
        :param _AffectedAssetCount: 受影响的资产数
        :type AffectedAssetCount: int
        :param _WeekRatio: 周同比
        :type WeekRatio: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PendingRiskCount = None
        self._AffectedAssetCount = None
        self._WeekRatio = None
        self._RequestId = None

    @property
    def PendingRiskCount(self):
        """待处理的风险数
        :rtype: int
        """
        return self._PendingRiskCount

    @PendingRiskCount.setter
    def PendingRiskCount(self, PendingRiskCount):
        self._PendingRiskCount = PendingRiskCount

    @property
    def AffectedAssetCount(self):
        """受影响的资产数
        :rtype: int
        """
        return self._AffectedAssetCount

    @AffectedAssetCount.setter
    def AffectedAssetCount(self, AffectedAssetCount):
        self._AffectedAssetCount = AffectedAssetCount

    @property
    def WeekRatio(self):
        """周同比
        :rtype: float
        """
        return self._WeekRatio

    @WeekRatio.setter
    def WeekRatio(self, WeekRatio):
        self._WeekRatio = WeekRatio

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
        self._PendingRiskCount = params.get("PendingRiskCount")
        self._AffectedAssetCount = params.get("AffectedAssetCount")
        self._WeekRatio = params.get("WeekRatio")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentProcessingRiskOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentProcessingRiskOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentProcessingRiskOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentProcessingRiskOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProcessingRiskCount: 待处理的风险数
        :type ProcessingRiskCount: int
        :param _AffectedAssetCount: 受影响的资产数
        :type AffectedAssetCount: int
        :param _WeekRatio: 周同比
        :type WeekRatio: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProcessingRiskCount = None
        self._AffectedAssetCount = None
        self._WeekRatio = None
        self._RequestId = None

    @property
    def ProcessingRiskCount(self):
        """待处理的风险数
        :rtype: int
        """
        return self._ProcessingRiskCount

    @ProcessingRiskCount.setter
    def ProcessingRiskCount(self, ProcessingRiskCount):
        self._ProcessingRiskCount = ProcessingRiskCount

    @property
    def AffectedAssetCount(self):
        """受影响的资产数
        :rtype: int
        """
        return self._AffectedAssetCount

    @AffectedAssetCount.setter
    def AffectedAssetCount(self, AffectedAssetCount):
        self._AffectedAssetCount = AffectedAssetCount

    @property
    def WeekRatio(self):
        """周同比
        :rtype: float
        """
        return self._WeekRatio

    @WeekRatio.setter
    def WeekRatio(self, WeekRatio):
        self._WeekRatio = WeekRatio

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
        self._ProcessingRiskCount = params.get("ProcessingRiskCount")
        self._AffectedAssetCount = params.get("AffectedAssetCount")
        self._WeekRatio = params.get("WeekRatio")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskAmountOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskAmountOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskAmountOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskAmountOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalRiskCount: 风险总数
        :type TotalRiskCount: int
        :param _TotalAffectedAssetCount: 受影响的资产数
        :type TotalAffectedAssetCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalRiskCount = None
        self._TotalAffectedAssetCount = None
        self._RequestId = None

    @property
    def TotalRiskCount(self):
        """风险总数
        :rtype: int
        """
        return self._TotalRiskCount

    @TotalRiskCount.setter
    def TotalRiskCount(self, TotalRiskCount):
        self._TotalRiskCount = TotalRiskCount

    @property
    def TotalAffectedAssetCount(self):
        """受影响的资产数
        :rtype: int
        """
        return self._TotalAffectedAssetCount

    @TotalAffectedAssetCount.setter
    def TotalAffectedAssetCount(self, TotalAffectedAssetCount):
        self._TotalAffectedAssetCount = TotalAffectedAssetCount

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
        self._TotalRiskCount = params.get("TotalRiskCount")
        self._TotalAffectedAssetCount = params.get("TotalAffectedAssetCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskDatasourceTop5Request(AbstractModel):
    """DescribeDSPAAssessmentRiskDatasourceTop5请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskDatasourceTop5Response(AbstractModel):
    """DescribeDSPAAssessmentRiskDatasourceTop5返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 风险值
        :type Items: list of RiskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """风险值
        :rtype: list of RiskItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RiskItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskDealedOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskDealedOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskDealedOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskDealedOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 遗留待处理风险总数
        :type TotalCount: int
        :param _YesterdayDealedCount: 昨日完成风险处置数
        :type YesterdayDealedCount: int
        :param _UnDealedRiskWeekRatio: 遗留待处理风险数周同比
        :type UnDealedRiskWeekRatio: float
        :param _UnDealedRiskDayRatio: 遗留待处理风险数日环比
        :type UnDealedRiskDayRatio: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._YesterdayDealedCount = None
        self._UnDealedRiskWeekRatio = None
        self._UnDealedRiskDayRatio = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """遗留待处理风险总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def YesterdayDealedCount(self):
        """昨日完成风险处置数
        :rtype: int
        """
        return self._YesterdayDealedCount

    @YesterdayDealedCount.setter
    def YesterdayDealedCount(self, YesterdayDealedCount):
        self._YesterdayDealedCount = YesterdayDealedCount

    @property
    def UnDealedRiskWeekRatio(self):
        """遗留待处理风险数周同比
        :rtype: float
        """
        return self._UnDealedRiskWeekRatio

    @UnDealedRiskWeekRatio.setter
    def UnDealedRiskWeekRatio(self, UnDealedRiskWeekRatio):
        self._UnDealedRiskWeekRatio = UnDealedRiskWeekRatio

    @property
    def UnDealedRiskDayRatio(self):
        """遗留待处理风险数日环比
        :rtype: float
        """
        return self._UnDealedRiskDayRatio

    @UnDealedRiskDayRatio.setter
    def UnDealedRiskDayRatio(self, UnDealedRiskDayRatio):
        self._UnDealedRiskDayRatio = UnDealedRiskDayRatio

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
        self._TotalCount = params.get("TotalCount")
        self._YesterdayDealedCount = params.get("YesterdayDealedCount")
        self._UnDealedRiskWeekRatio = params.get("UnDealedRiskWeekRatio")
        self._UnDealedRiskDayRatio = params.get("UnDealedRiskDayRatio")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskDealedTrendRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskDealedTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _StartTime: 开始日期
        :type StartTime: str
        :param _EndTime: 结束日期
        :type EndTime: str
        :param _TemplateId: 评估模板id
        :type TemplateId: str
        """
        self._DspaId = None
        self._StartTime = None
        self._EndTime = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def StartTime(self):
        """开始日期
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束日期
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskDealedTrendResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskDealedTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 趋势统计结果
        :type Items: list of RiskDealedTrendItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """趋势统计结果
        :rtype: list of RiskDealedTrendItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RiskDealedTrendItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskDistributionOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskDistributionOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例Id
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        :param _Filter: 风险资产分布的过滤条件
（rdb，cos，不传就筛选全部）
        :type Filter: str
        """
        self._DspaId = None
        self._TemplateId = None
        self._Filter = None

    @property
    def DspaId(self):
        """dspa实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Filter(self):
        """风险资产分布的过滤条件
（rdb，cos，不传就筛选全部）
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskDistributionOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskDistributionOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskTypeDistribution: 风险类型分布
        :type RiskTypeDistribution: list of Note
        :param _RiskDetailDistribution: 风险详情分布
        :type RiskDetailDistribution: list of Note
        :param _RiskAssetsDistribution: 风险资产详情
        :type RiskAssetsDistribution: list of Note
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskTypeDistribution = None
        self._RiskDetailDistribution = None
        self._RiskAssetsDistribution = None
        self._RequestId = None

    @property
    def RiskTypeDistribution(self):
        """风险类型分布
        :rtype: list of Note
        """
        return self._RiskTypeDistribution

    @RiskTypeDistribution.setter
    def RiskTypeDistribution(self, RiskTypeDistribution):
        self._RiskTypeDistribution = RiskTypeDistribution

    @property
    def RiskDetailDistribution(self):
        """风险详情分布
        :rtype: list of Note
        """
        return self._RiskDetailDistribution

    @RiskDetailDistribution.setter
    def RiskDetailDistribution(self, RiskDetailDistribution):
        self._RiskDetailDistribution = RiskDetailDistribution

    @property
    def RiskAssetsDistribution(self):
        """风险资产详情
        :rtype: list of Note
        """
        return self._RiskAssetsDistribution

    @RiskAssetsDistribution.setter
    def RiskAssetsDistribution(self, RiskAssetsDistribution):
        self._RiskAssetsDistribution = RiskAssetsDistribution

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
        if params.get("RiskTypeDistribution") is not None:
            self._RiskTypeDistribution = []
            for item in params.get("RiskTypeDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._RiskTypeDistribution.append(obj)
        if params.get("RiskDetailDistribution") is not None:
            self._RiskDetailDistribution = []
            for item in params.get("RiskDetailDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._RiskDetailDistribution.append(obj)
        if params.get("RiskAssetsDistribution") is not None:
            self._RiskAssetsDistribution = []
            for item in params.get("RiskAssetsDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._RiskAssetsDistribution.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskItemTop5Request(AbstractModel):
    """DescribeDSPAAssessmentRiskItemTop5请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskItemTop5Response(AbstractModel):
    """DescribeDSPAAssessmentRiskItemTop5返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 风险结果
        :type Items: list of RiskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """风险结果
        :rtype: list of RiskItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RiskItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskLevelDetailRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _RiskLevelId: 风险级别id
        :type RiskLevelId: int
        """
        self._DspaId = None
        self._RiskLevelId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def RiskLevelId(self):
        """风险级别id
        :rtype: int
        """
        return self._RiskLevelId

    @RiskLevelId.setter
    def RiskLevelId(self, RiskLevelId):
        self._RiskLevelId = RiskLevelId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._RiskLevelId = params.get("RiskLevelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskLevelDetailResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskLevelName: 风险级别名称
        :type RiskLevelName: str
        :param _RiskLevelDescription: 风险级别描述
        :type RiskLevelDescription: str
        :param _IdentifyComplianceId: 分类分级id
        :type IdentifyComplianceId: int
        :param _IdentifyComplianceName: 分类分级模板名称
        :type IdentifyComplianceName: str
        :param _RiskLevelMatrix: 风险数据
        :type RiskLevelMatrix: list of RiskLevelMatrix
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskLevelName = None
        self._RiskLevelDescription = None
        self._IdentifyComplianceId = None
        self._IdentifyComplianceName = None
        self._RiskLevelMatrix = None
        self._RequestId = None

    @property
    def RiskLevelName(self):
        """风险级别名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def RiskLevelDescription(self):
        """风险级别描述
        :rtype: str
        """
        return self._RiskLevelDescription

    @RiskLevelDescription.setter
    def RiskLevelDescription(self, RiskLevelDescription):
        self._RiskLevelDescription = RiskLevelDescription

    @property
    def IdentifyComplianceId(self):
        """分类分级id
        :rtype: int
        """
        return self._IdentifyComplianceId

    @IdentifyComplianceId.setter
    def IdentifyComplianceId(self, IdentifyComplianceId):
        self._IdentifyComplianceId = IdentifyComplianceId

    @property
    def IdentifyComplianceName(self):
        """分类分级模板名称
        :rtype: str
        """
        return self._IdentifyComplianceName

    @IdentifyComplianceName.setter
    def IdentifyComplianceName(self, IdentifyComplianceName):
        self._IdentifyComplianceName = IdentifyComplianceName

    @property
    def RiskLevelMatrix(self):
        """风险数据
        :rtype: list of RiskLevelMatrix
        """
        return self._RiskLevelMatrix

    @RiskLevelMatrix.setter
    def RiskLevelMatrix(self, RiskLevelMatrix):
        self._RiskLevelMatrix = RiskLevelMatrix

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
        self._RiskLevelName = params.get("RiskLevelName")
        self._RiskLevelDescription = params.get("RiskLevelDescription")
        self._IdentifyComplianceId = params.get("IdentifyComplianceId")
        self._IdentifyComplianceName = params.get("IdentifyComplianceName")
        if params.get("RiskLevelMatrix") is not None:
            self._RiskLevelMatrix = []
            for item in params.get("RiskLevelMatrix"):
                obj = RiskLevelMatrix()
                obj._deserialize(item)
                self._RiskLevelMatrix.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskLevelListRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._DspaId = None
        self._Limit = None
        self._Offset = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskLevelListResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RiskLevelList: 风险等级列表
        :type RiskLevelList: list of RiskLevelRisk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RiskLevelList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RiskLevelList(self):
        """风险等级列表
        :rtype: list of RiskLevelRisk
        """
        return self._RiskLevelList

    @RiskLevelList.setter
    def RiskLevelList(self, RiskLevelList):
        self._RiskLevelList = RiskLevelList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("RiskLevelList") is not None:
            self._RiskLevelList = []
            for item in params.get("RiskLevelList"):
                obj = RiskLevelRisk()
                obj._deserialize(item)
                self._RiskLevelList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskLevelTrendRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _StartTime: 开始日期
        :type StartTime: str
        :param _EndTime: 结束时日期
        :type EndTime: str
        :param _TemplateId: 评估模板id
        :type TemplateId: str
        """
        self._DspaId = None
        self._StartTime = None
        self._EndTime = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def StartTime(self):
        """开始日期
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时日期
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskLevelTrendResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskLevelTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 结果集
        :type Items: list of RiskLevelTrendItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """结果集
        :rtype: list of RiskLevelTrendItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RiskLevelTrendItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskOverviewRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskOverviewResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 风险总数
        :type TotalCount: int
        :param _HighRiskCount: 高危风险数
        :type HighRiskCount: int
        :param _HighRiskWeekRatio: 周同比
        :type HighRiskWeekRatio: float
        :param _HighRiskDayRatio: 高危风险数日环比
        :type HighRiskDayRatio: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HighRiskCount = None
        self._HighRiskWeekRatio = None
        self._HighRiskDayRatio = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """风险总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HighRiskCount(self):
        """高危风险数
        :rtype: int
        """
        return self._HighRiskCount

    @HighRiskCount.setter
    def HighRiskCount(self, HighRiskCount):
        self._HighRiskCount = HighRiskCount

    @property
    def HighRiskWeekRatio(self):
        """周同比
        :rtype: float
        """
        return self._HighRiskWeekRatio

    @HighRiskWeekRatio.setter
    def HighRiskWeekRatio(self, HighRiskWeekRatio):
        self._HighRiskWeekRatio = HighRiskWeekRatio

    @property
    def HighRiskDayRatio(self):
        """高危风险数日环比
        :rtype: float
        """
        return self._HighRiskDayRatio

    @HighRiskDayRatio.setter
    def HighRiskDayRatio(self, HighRiskDayRatio):
        self._HighRiskDayRatio = HighRiskDayRatio

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
        self._TotalCount = params.get("TotalCount")
        self._HighRiskCount = params.get("HighRiskCount")
        self._HighRiskWeekRatio = params.get("HighRiskWeekRatio")
        self._HighRiskDayRatio = params.get("HighRiskDayRatio")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskProcessHistoryRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskProcessHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _RiskId: 风险id
        :type RiskId: int
        """
        self._DspaId = None
        self._RiskId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def RiskId(self):
        """风险id
        :rtype: int
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._RiskId = params.get("RiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskProcessHistoryResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskProcessHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProcessHistory: 处理的历史
        :type ProcessHistory: list of ProcessHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProcessHistory = None
        self._RequestId = None

    @property
    def ProcessHistory(self):
        """处理的历史
        :rtype: list of ProcessHistory
        """
        return self._ProcessHistory

    @ProcessHistory.setter
    def ProcessHistory(self, ProcessHistory):
        self._ProcessHistory = ProcessHistory

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
        if params.get("ProcessHistory") is not None:
            self._ProcessHistory = []
            for item in params.get("ProcessHistory"):
                obj = ProcessHistory()
                obj._deserialize(item)
                self._ProcessHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskSideDistributedRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskSideDistributed请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskSideDistributedResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskSideDistributed返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskSideDistributed: 风险面的分布
        :type RiskSideDistributed: list of RiskSideDistributed
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskSideDistributed = None
        self._RequestId = None

    @property
    def RiskSideDistributed(self):
        """风险面的分布
        :rtype: list of RiskSideDistributed
        """
        return self._RiskSideDistributed

    @RiskSideDistributed.setter
    def RiskSideDistributed(self, RiskSideDistributed):
        self._RiskSideDistributed = RiskSideDistributed

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
        if params.get("RiskSideDistributed") is not None:
            self._RiskSideDistributed = []
            for item in params.get("RiskSideDistributed"):
                obj = RiskSideDistributed()
                obj._deserialize(item)
                self._RiskSideDistributed.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskSideListRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskSideList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TemplateId: 评估模板id
        :type TemplateId: int
        """
        self._DspaId = None
        self._TemplateId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskSideListResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskSideList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskSideItmeList: 风险面列表
        :type RiskSideItmeList: list of Note
        :param _RiskSideItemList: 风险面列表
        :type RiskSideItemList: list of Note
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskSideItmeList = None
        self._RiskSideItemList = None
        self._RequestId = None

    @property
    def RiskSideItmeList(self):
        warnings.warn("parameter `RiskSideItmeList` is deprecated", DeprecationWarning) 

        """风险面列表
        :rtype: list of Note
        """
        return self._RiskSideItmeList

    @RiskSideItmeList.setter
    def RiskSideItmeList(self, RiskSideItmeList):
        warnings.warn("parameter `RiskSideItmeList` is deprecated", DeprecationWarning) 

        self._RiskSideItmeList = RiskSideItmeList

    @property
    def RiskSideItemList(self):
        """风险面列表
        :rtype: list of Note
        """
        return self._RiskSideItemList

    @RiskSideItemList.setter
    def RiskSideItemList(self, RiskSideItemList):
        self._RiskSideItemList = RiskSideItemList

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
        if params.get("RiskSideItmeList") is not None:
            self._RiskSideItmeList = []
            for item in params.get("RiskSideItmeList"):
                obj = Note()
                obj._deserialize(item)
                self._RiskSideItmeList.append(obj)
        if params.get("RiskSideItemList") is not None:
            self._RiskSideItemList = []
            for item in params.get("RiskSideItemList"):
                obj = Note()
                obj._deserialize(item)
                self._RiskSideItemList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskTemplateDetailRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskTemplateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._DspaId = None
        self._TemplateId = None
        self._Limit = None
        self._Offset = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskTemplateDetailResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskTemplateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateDescription: 模板的描述
        :type TemplateDescription: str
        :param _RiskLevelId: 风险等级
        :type RiskLevelId: int
        :param _RiskLevelName: 风险等级名称
        :type RiskLevelName: str
        :param _RiskItemList: 脆弱项配置列表
        :type RiskItemList: list of AssessmentRiskItem
        :param _TotalCount: 脆弱项配置条数
        :type TotalCount: int
        :param _TaskCitations: 被任务引用次数
        :type TaskCitations: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateDescription = None
        self._RiskLevelId = None
        self._RiskLevelName = None
        self._RiskItemList = None
        self._TotalCount = None
        self._TaskCitations = None
        self._RequestId = None

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateDescription(self):
        """模板的描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def RiskLevelId(self):
        """风险等级
        :rtype: int
        """
        return self._RiskLevelId

    @RiskLevelId.setter
    def RiskLevelId(self, RiskLevelId):
        self._RiskLevelId = RiskLevelId

    @property
    def RiskLevelName(self):
        """风险等级名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def RiskItemList(self):
        """脆弱项配置列表
        :rtype: list of AssessmentRiskItem
        """
        return self._RiskItemList

    @RiskItemList.setter
    def RiskItemList(self, RiskItemList):
        self._RiskItemList = RiskItemList

    @property
    def TotalCount(self):
        """脆弱项配置条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskCitations(self):
        """被任务引用次数
        :rtype: int
        """
        return self._TaskCitations

    @TaskCitations.setter
    def TaskCitations(self, TaskCitations):
        self._TaskCitations = TaskCitations

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
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateDescription = params.get("TemplateDescription")
        self._RiskLevelId = params.get("RiskLevelId")
        self._RiskLevelName = params.get("RiskLevelName")
        if params.get("RiskItemList") is not None:
            self._RiskItemList = []
            for item in params.get("RiskItemList"):
                obj = AssessmentRiskItem()
                obj._deserialize(item)
                self._RiskItemList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TaskCitations = params.get("TaskCitations")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRiskTemplateVulnerableListRequest(AbstractModel):
    """DescribeDSPAAssessmentRiskTemplateVulnerableList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _RiskName: 风险名称
        :type RiskName: str
        :param _RiskSide: 风险面
        :type RiskSide: str
        """
        self._DspaId = None
        self._Limit = None
        self._Offset = None
        self._RiskType = None
        self._RiskName = None
        self._RiskSide = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def RiskName(self):
        """风险名称
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskSide(self):
        """风险面
        :rtype: str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RiskType = params.get("RiskType")
        self._RiskName = params.get("RiskName")
        self._RiskSide = params.get("RiskSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRiskTemplateVulnerableListResponse(AbstractModel):
    """DescribeDSPAAssessmentRiskTemplateVulnerableList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskItemList: 脆弱项列表
        :type RiskItemList: list of AssessmentRiskItem
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskItemList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RiskItemList(self):
        """脆弱项列表
        :rtype: list of AssessmentRiskItem
        """
        return self._RiskItemList

    @RiskItemList.setter
    def RiskItemList(self, RiskItemList):
        self._RiskItemList = RiskItemList

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("RiskItemList") is not None:
            self._RiskItemList = []
            for item in params.get("RiskItemList"):
                obj = AssessmentRiskItem()
                obj._deserialize(item)
                self._RiskItemList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentRisksRequest(AbstractModel):
    """DescribeDSPAAssessmentRisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _TaskId: 评估任务Id，格式“task-xxxxxxxx”
        :type TaskId: str
        :param _Offset: 偏移量。默认为0
        :type Offset: int
        :param _Limit: 结果集个数限制。默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤项。
支持模糊搜索：ControlItemName。
支持过滤：
RiskLevel：风险等级（high，medium，low）
Status：风险处理状态(waiting待处理, processing处理中, stopped处理暂停, finished已处理, failed处理失败)
        :type Filters: list of DspaAssessmentFilter
        """
        self._DspaId = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """评估任务Id，格式“task-xxxxxxxx”
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        """偏移量。默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果集个数限制。默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤项。
支持模糊搜索：ControlItemName。
支持过滤：
RiskLevel：风险等级（high，medium，low）
Status：风险处理状态(waiting待处理, processing处理中, stopped处理暂停, finished已处理, failed处理失败)
        :rtype: list of DspaAssessmentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaAssessmentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentRisksResponse(AbstractModel):
    """DescribeDSPAAssessmentRisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的评估风险项数目
        :type TotalCount: int
        :param _Items: 评估风险项列表
        :type Items: list of AssessmentRisk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的评估风险项数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """评估风险项列表
        :rtype: list of AssessmentRisk
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AssessmentRisk()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentTasksRequest(AbstractModel):
    """DescribeDSPAAssessmentTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _Offset: 偏移量。默认为0
        :type Offset: int
        :param _Limit: 结果集个数限制。默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤项。支持模糊搜索：TaskId，TaskName支持过滤：BusinessName：业务名称BusinessDept：业务部门名称TemplateName：评估模板名称Status：评估状态 (waiting待评估，processing评估中, , finished已评估, failed评估失败)
        :type Filters: list of DspaAssessmentFilter
        """
        self._DspaId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Offset(self):
        """偏移量。默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果集个数限制。默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤项。支持模糊搜索：TaskId，TaskName支持过滤：BusinessName：业务名称BusinessDept：业务部门名称TemplateName：评估模板名称Status：评估状态 (waiting待评估，processing评估中, , finished已评估, failed评估失败)
        :rtype: list of DspaAssessmentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaAssessmentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentTasksResponse(AbstractModel):
    """DescribeDSPAAssessmentTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的评估任务数目
        :type TotalCount: int
        :param _Items: 评估任务列表
        :type Items: list of AssessmentTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的评估任务数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """评估任务列表
        :rtype: list of AssessmentTask
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AssessmentTask()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentTemplateControlItemsRequest(AbstractModel):
    """DescribeDSPAAssessmentTemplateControlItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id。格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _TemplateId: 评估模板Id。格式“template-xxxxxxxx”
        :type TemplateId: str
        :param _Offset: 偏移量。默认为0
        :type Offset: int
        :param _Limit: 结果集个数限制。默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤项。
支持模糊搜索：ItemId，ItemName
支持过滤：
Source：评估项来源，system / user
ItemType：评估项类型，questionnaire / auto
ItemSubType：评估项子类型
Status：评估项启用状态，draft / launched
        :type Filters: list of DspaAssessmentFilter
        """
        self._DspaId = None
        self._TemplateId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例Id。格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateId(self):
        """评估模板Id。格式“template-xxxxxxxx”
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Offset(self):
        """偏移量。默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果集个数限制。默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤项。
支持模糊搜索：ItemId，ItemName
支持过滤：
Source：评估项来源，system / user
ItemType：评估项类型，questionnaire / auto
ItemSubType：评估项子类型
Status：评估项启用状态，draft / launched
        :rtype: list of DspaAssessmentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateId = params.get("TemplateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaAssessmentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentTemplateControlItemsResponse(AbstractModel):
    """DescribeDSPAAssessmentTemplateControlItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的评估项数目
        :type TotalCount: int
        :param _Items: 模板关联的评估项列表
        :type Items: list of AssessmentControlItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的评估项数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """模板关联的评估项列表
        :rtype: list of AssessmentControlItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AssessmentControlItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAAssessmentTemplatesRequest(AbstractModel):
    """DescribeDSPAAssessmentTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _Offset: 偏移量。默认为0
        :type Offset: int
        :param _Limit: 结果集个数限制。默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤项。支持模糊搜索：（TemplateId，TemplateName）支持过滤：Source：模板来源，system / userUseType：模板类型，auto，semi-auto，law等Status：模板启用状态，draft / launched，ComplianceId：关联的分类分级模板id
        :type Filters: list of DspaAssessmentFilter
        """
        self._DspaId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Offset(self):
        """偏移量。默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果集个数限制。默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤项。支持模糊搜索：（TemplateId，TemplateName）支持过滤：Source：模板来源，system / userUseType：模板类型，auto，semi-auto，law等Status：模板启用状态，draft / launched，ComplianceId：关联的分类分级模板id
        :rtype: list of DspaAssessmentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaAssessmentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAAssessmentTemplatesResponse(AbstractModel):
    """DescribeDSPAAssessmentTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的模板数目
        :type TotalCount: int
        :param _Items: 模板列表。
        :type Items: list of AssessmentTemplate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的模板数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """模板列表。
        :rtype: list of AssessmentTemplate
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AssessmentTemplate()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDataAssetBucketsRequest(AbstractModel):
    """DescribeDSPACOSDataAssetBuckets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id
        :type DspaId: str
        :param _ComplianceId: 合规组Id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """DSPA实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组Id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDataAssetBucketsResponse(AbstractModel):
    """DescribeDSPACOSDataAssetBuckets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Buckets: COS对象存储敏感数据资产已扫描的桶集合。
        :type Buckets: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Buckets = None
        self._RequestId = None

    @property
    def Buckets(self):
        """COS对象存储敏感数据资产已扫描的桶集合。
        :rtype: list of str
        """
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets

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
        self._Buckets = params.get("Buckets")
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDataAssetByComplianceIdRequest(AbstractModel):
    """DescribeDSPACOSDataAssetByComplianceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDataAssetByComplianceIdResponse(AbstractModel):
    """DescribeDSPACOSDataAssetByComplianceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Stats: 符合条件的COS存储对象的敏感数据资产统计记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Stats: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDataAssetCount`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Stats = None
        self._RequestId = None

    @property
    def Stats(self):
        """符合条件的COS存储对象的敏感数据资产统计记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDataAssetCount`
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

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
        if params.get("Stats") is not None:
            self._Stats = DspaCOSDataAssetCount()
            self._Stats._deserialize(params.get("Stats"))
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDataAssetDetailRequest(AbstractModel):
    """DescribeDSPACOSDataAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDataAssetDetailResponse(AbstractModel):
    """DescribeDSPACOSDataAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: COS对象存储敏感数据资产详情列表
        :type Details: list of DspaCOSDataAssetDetail
        :param _TotalCount: 符合条件的COS对象存储敏感数据资产数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Details(self):
        """COS对象存储敏感数据资产详情列表
        :rtype: list of DspaCOSDataAssetDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def TotalCount(self):
        """符合条件的COS对象存储敏感数据资产数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DspaCOSDataAssetDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDiscoveryTaskDetailRequest(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDiscoveryTaskDetailResponse(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务详情
        :type Task: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        """任务详情
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDetail`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        if params.get("Task") is not None:
            self._Task = DspaCOSDiscoveryTaskDetail()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDiscoveryTaskFilesRequest(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id
        :type DspaId: str
        :param _TaskId: 扫描任务ID
        :type TaskId: int
        :param _BucketResultId: 扫描Bucket任务结果ID
        :type BucketResultId: int
        """
        self._DspaId = None
        self._TaskId = None
        self._BucketResultId = None

    @property
    def DspaId(self):
        """DSPA实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """扫描任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BucketResultId(self):
        """扫描Bucket任务结果ID
        :rtype: int
        """
        return self._BucketResultId

    @BucketResultId.setter
    def BucketResultId(self, BucketResultId):
        self._BucketResultId = BucketResultId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._BucketResultId = params.get("BucketResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDiscoveryTaskFilesResponse(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Files: 文件列表
        :type Files: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Files = None
        self._RequestId = None

    @property
    def Files(self):
        """文件列表
        :rtype: list of str
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
        self._Files = params.get("Files")
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDiscoveryTaskResultRequest(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Offset: 偏移量，默认值为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100
        :type Limit: int
        :param _Filters: Array of Filter	此参数对外不可见。过滤数组。支持的Name：
BucketName 对象桶名
TaskID 任务ID，
TaskName 任务名，
DataSourceId：数据源ID，
ResourceRegion：资源所在地域
每项过滤条件最多支持5个。
        :type Filters: list of Filter
        """
        self._DspaId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Offset(self):
        """偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Array of Filter	此参数对外不可见。过滤数组。支持的Name：
BucketName 对象桶名
TaskID 任务ID，
TaskName 任务名，
DataSourceId：数据源ID，
ResourceRegion：资源所在地域
每项过滤条件最多支持5个。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeDSPACOSDiscoveryTaskResultResponse(AbstractModel):
    """DescribeDSPACOSDiscoveryTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 扫描任务结果项
        :type Items: list of DspaCOSDiscoveryTaskResult
        :param _TotalCount: 符合条件的数据结果数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """扫描任务结果项
        :rtype: list of DspaCOSDiscoveryTaskResult
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的数据结果数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaCOSDiscoveryTaskResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSDiscoveryTasksRequest(AbstractModel):
    """DescribeDSPACOSDiscoveryTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Name: 任务名称
        :type Name: str
        :param _StatusList: 任务扫描结果状态，可供选择的状态值有：-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :type StatusList: list of int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :type Limit: int
        """
        self._DspaId = None
        self._TaskId = None
        self._Name = None
        self._StatusList = None
        self._Offset = None
        self._Limit = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StatusList(self):
        """任务扫描结果状态，可供选择的状态值有：-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :rtype: list of int
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._StatusList = params.get("StatusList")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSDiscoveryTasksResponse(AbstractModel):
    """DescribeDSPACOSDiscoveryTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 任务列表
        :type Items: list of DspaCOSDiscoveryTask
        :param _TotalCount: 符合条件的任务列表数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """任务列表
        :rtype: list of DspaCOSDiscoveryTask
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的任务列表数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaCOSDiscoveryTask()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPACOSTaskResultDetailRequest(AbstractModel):
    """DescribeDSPACOSTaskResultDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _BucketResultId: 扫描Bucket结果ID
        :type BucketResultId: int
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _FileName: 文件名
        :type FileName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _LevelId: 敏感数据分级ID
        :type LevelId: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100
        :type Limit: int
        :param _BucketName: 扫描桶名称。
        :type BucketName: str
        :param _CategoryIdList: 多级分类的分类ID集合
        :type CategoryIdList: list of int
        """
        self._DspaId = None
        self._TaskId = None
        self._BucketResultId = None
        self._ComplianceId = None
        self._FileName = None
        self._CategoryId = None
        self._LevelId = None
        self._Offset = None
        self._Limit = None
        self._BucketName = None
        self._CategoryIdList = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BucketResultId(self):
        """扫描Bucket结果ID
        :rtype: int
        """
        return self._BucketResultId

    @BucketResultId.setter
    def BucketResultId(self, BucketResultId):
        self._BucketResultId = BucketResultId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """敏感数据分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def BucketName(self):
        """扫描桶名称。
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def CategoryIdList(self):
        """多级分类的分类ID集合
        :rtype: list of int
        """
        return self._CategoryIdList

    @CategoryIdList.setter
    def CategoryIdList(self, CategoryIdList):
        self._CategoryIdList = CategoryIdList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._BucketResultId = params.get("BucketResultId")
        self._ComplianceId = params.get("ComplianceId")
        self._FileName = params.get("FileName")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._BucketName = params.get("BucketName")
        self._CategoryIdList = params.get("CategoryIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACOSTaskResultDetailResponse(AbstractModel):
    """DescribeDSPACOSTaskResultDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 扫描结果详情列表
        :type Items: list of DspaDiscoveryCOSTaskResultDetail
        :param _TotalCount: 符合条件的详情数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """扫描结果详情列表
        :rtype: list of DspaDiscoveryCOSTaskResultDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的详情数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryCOSTaskResultDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPACategoriesRequest(AbstractModel):
    """DescribeDSPACategories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _CategoryId: 数据分类ID
        :type CategoryId: int
        :param _Name: 敏感数据分类名称
        :type Name: str
        :param _Offset: 偏移量，默认值为0
        :type Offset: int
        :param _Limit: 返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :type Limit: int
        """
        self._DspaId = None
        self._CategoryId = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Name(self):
        """敏感数据分类名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACategoriesResponse(AbstractModel):
    """DescribeDSPACategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 敏感数据分类列表
        :type Items: list of DataCategory
        :param _TotalCount: 符合条件的敏感数据分类数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """敏感数据分类列表
        :rtype: list of DataCategory
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的敏感数据分类数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DataCategory()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPACategoryRuleStatisticRequest(AbstractModel):
    """DescribeDSPACategoryRuleStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACategoryRuleStatisticResponse(AbstractModel):
    """DescribeDSPACategoryRuleStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticSet: 分类规则统计信息
        :type StatisticSet: list of CategoryRuleStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticSet = None
        self._RequestId = None

    @property
    def StatisticSet(self):
        """分类规则统计信息
        :rtype: list of CategoryRuleStatistic
        """
        return self._StatisticSet

    @StatisticSet.setter
    def StatisticSet(self, StatisticSet):
        self._StatisticSet = StatisticSet

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
        if params.get("StatisticSet") is not None:
            self._StatisticSet = []
            for item in params.get("StatisticSet"):
                obj = CategoryRuleStatistic()
                obj._deserialize(item)
                self._StatisticSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPACategoryRulesRequest(AbstractModel):
    """DescribeDSPACategoryRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _ComplianceId: 合规组模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._CategoryId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ComplianceId(self):
        """合规组模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACategoryRulesResponse(AbstractModel):
    """DescribeDSPACategoryRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryRules: 分类规则信息
        :type CategoryRules: list of CategoryRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryRules = None
        self._RequestId = None

    @property
    def CategoryRules(self):
        """分类规则信息
        :rtype: list of CategoryRule
        """
        return self._CategoryRules

    @CategoryRules.setter
    def CategoryRules(self, CategoryRules):
        self._CategoryRules = CategoryRules

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
        if params.get("CategoryRules") is not None:
            self._CategoryRules = []
            for item in params.get("CategoryRules"):
                obj = CategoryRule()
                obj._deserialize(item)
                self._CategoryRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPACategoryTreeRequest(AbstractModel):
    """DescribeDSPACategoryTree请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACategoryTreeResponse(AbstractModel):
    """DescribeDSPACategoryTree返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultJson: 分类树json
        :type ResultJson: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultJson = None
        self._RequestId = None

    @property
    def ResultJson(self):
        """分类树json
        :rtype: str
        """
        return self._ResultJson

    @ResultJson.setter
    def ResultJson(self, ResultJson):
        self._ResultJson = ResultJson

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
        self._ResultJson = params.get("ResultJson")
        self._RequestId = params.get("RequestId")


class DescribeDSPACategoryTreeWithRulesRequest(AbstractModel):
    """DescribeDSPACategoryTreeWithRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组模板id
        :type ComplianceId: int
        :param _CategoryId: 分类id
        :type CategoryId: int
        """
        self._DspaId = None
        self._ComplianceId = None
        self._CategoryId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPACategoryTreeWithRulesResponse(AbstractModel):
    """DescribeDSPACategoryTreeWithRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultJson: 分类树json
        :type ResultJson: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultJson = None
        self._RequestId = None

    @property
    def ResultJson(self):
        """分类树json
        :rtype: str
        """
        return self._ResultJson

    @ResultJson.setter
    def ResultJson(self, ResultJson):
        self._ResultJson = ResultJson

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
        self._ResultJson = params.get("ResultJson")
        self._RequestId = params.get("RequestId")


class DescribeDSPAComplianceGroupDetailRequest(AbstractModel):
    """DescribeDSPAComplianceGroupDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAComplianceGroupDetailResponse(AbstractModel):
    """DescribeDSPAComplianceGroupDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Detail: 模板详情
        :type Detail: :class:`tencentcloud.dsgc.v20190723.models.ComplianceGroupDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Detail = None
        self._RequestId = None

    @property
    def Detail(self):
        """模板详情
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ComplianceGroupDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

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
        if params.get("Detail") is not None:
            self._Detail = ComplianceGroupDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeDSPAComplianceGroupsRequest(AbstractModel):
    """DescribeDSPAComplianceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _Name: 合规组名称
        :type Name: str
        :param _Offset: 偏移量，默认值为0
        :type Offset: int
        :param _Limit: 返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :type Limit: int
        :param _ComplianceGroupTypeList: 合规组类型可选值：0 默认合规组, 1 系统合规组, 2 自定义合规组
        :type ComplianceGroupTypeList: list of int
        :param _IsFilterCloseComplianceGroup: 是否仅显示已开启模版
        :type IsFilterCloseComplianceGroup: bool
        """
        self._DspaId = None
        self._ComplianceGroupId = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._ComplianceGroupTypeList = None
        self._IsFilterCloseComplianceGroup = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def Name(self):
        """合规组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ComplianceGroupTypeList(self):
        """合规组类型可选值：0 默认合规组, 1 系统合规组, 2 自定义合规组
        :rtype: list of int
        """
        return self._ComplianceGroupTypeList

    @ComplianceGroupTypeList.setter
    def ComplianceGroupTypeList(self, ComplianceGroupTypeList):
        self._ComplianceGroupTypeList = ComplianceGroupTypeList

    @property
    def IsFilterCloseComplianceGroup(self):
        """是否仅显示已开启模版
        :rtype: bool
        """
        return self._IsFilterCloseComplianceGroup

    @IsFilterCloseComplianceGroup.setter
    def IsFilterCloseComplianceGroup(self, IsFilterCloseComplianceGroup):
        self._IsFilterCloseComplianceGroup = IsFilterCloseComplianceGroup


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ComplianceGroupTypeList = params.get("ComplianceGroupTypeList")
        self._IsFilterCloseComplianceGroup = params.get("IsFilterCloseComplianceGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAComplianceGroupsResponse(AbstractModel):
    """DescribeDSPAComplianceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 合规组列表
        :type Items: list of DspaDiscoveryComplianceGroupInfo
        :param _TotalCount: 符合条件的合规组列表数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """合规组列表
        :rtype: list of DspaDiscoveryComplianceGroupInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的合规组列表数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryComplianceGroupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPAComplianceUpdateNotificationRequest(AbstractModel):
    """DescribeDSPAComplianceUpdateNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组分类模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组分类模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAComplianceUpdateNotificationResponse(AbstractModel):
    """DescribeDSPAComplianceUpdateNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsUpdated: 模板是否更新
        :type IsUpdated: bool
        :param _TaskNameSet: 任务名称集合
        :type TaskNameSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsUpdated = None
        self._TaskNameSet = None
        self._RequestId = None

    @property
    def IsUpdated(self):
        """模板是否更新
        :rtype: bool
        """
        return self._IsUpdated

    @IsUpdated.setter
    def IsUpdated(self, IsUpdated):
        self._IsUpdated = IsUpdated

    @property
    def TaskNameSet(self):
        """任务名称集合
        :rtype: list of str
        """
        return self._TaskNameSet

    @TaskNameSet.setter
    def TaskNameSet(self, TaskNameSet):
        self._TaskNameSet = TaskNameSet

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
        self._IsUpdated = params.get("IsUpdated")
        self._TaskNameSet = params.get("TaskNameSet")
        self._RequestId = params.get("RequestId")


class DescribeDSPADataSourceDbInfoRequest(AbstractModel):
    """DescribeDSPADataSourceDbInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        """
        self._DspaId = None
        self._DataSourceId = None
        self._DataSourceType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADataSourceDbInfoResponse(AbstractModel):
    """DescribeDSPADataSourceDbInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 数据库信息列表
        :type Items: list of DSPADataSourceDbInfo
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._DataSourceId = None
        self._RequestId = None

    @property
    def Items(self):
        """数据库信息列表
        :rtype: list of DSPADataSourceDbInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DSPADataSourceDbInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._DataSourceId = params.get("DataSourceId")
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryRulesRequest(AbstractModel):
    """DescribeDSPADiscoveryRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回上限，默认值10， 最大值10000。
        :type Limit: int
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Name: 规则名称
        :type Name: str
        :param _FilterRuleSource: 是否需要过滤别名
        :type FilterRuleSource: bool
        """
        self._DspaId = None
        self._Offset = None
        self._Limit = None
        self._RuleId = None
        self._Name = None
        self._FilterRuleSource = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回上限，默认值10， 最大值10000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        """规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FilterRuleSource(self):
        """是否需要过滤别名
        :rtype: bool
        """
        return self._FilterRuleSource

    @FilterRuleSource.setter
    def FilterRuleSource(self, FilterRuleSource):
        self._FilterRuleSource = FilterRuleSource


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._FilterRuleSource = params.get("FilterRuleSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryRulesResponse(AbstractModel):
    """DescribeDSPADiscoveryRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 规则ID
        :type TotalCount: int
        :param _Items: 规则集合
        :type Items: list of DspaDiscoveryRuleDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """规则ID
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """规则集合
        :rtype: list of DspaDiscoveryRuleDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryRuleDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryServiceStatusRequest(AbstractModel):
    """DescribeDSPADiscoveryServiceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryServiceStatusResponse(AbstractModel):
    """DescribeDSPADiscoveryServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: 分类分级服务是否开通，true 表示已开通，false表示未开通
        :type ServiceEnabled: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        """分类分级服务是否开通，true 表示已开通，false表示未开通
        :rtype: bool
        """
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

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
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryTaskDetailRequest(AbstractModel):
    """DescribeDSPADiscoveryTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryTaskDetailResponse(AbstractModel):
    """DescribeDSPADiscoveryTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务详情
        :type Task: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        """任务详情
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDetail`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        if params.get("Task") is not None:
            self._Task = DspaDiscoveryTaskDetail()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryTaskResultDetailRequest(AbstractModel):
    """DescribeDSPADiscoveryTaskResultDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _DbResultId: 扫描数据库结果ID
        :type DbResultId: int
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _DbName: 数据库名
        :type DbName: str
        :param _TableName: 所属数据表名
        :type TableName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _LevelId: 敏感数据分级ID
        :type LevelId: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100
        :type Limit: int
        :param _CategoryIdList: 多级分类的分类ID集合
        :type CategoryIdList: list of int
        """
        self._DspaId = None
        self._TaskId = None
        self._DbResultId = None
        self._ComplianceId = None
        self._DbName = None
        self._TableName = None
        self._CategoryId = None
        self._LevelId = None
        self._Offset = None
        self._Limit = None
        self._CategoryIdList = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DbResultId(self):
        """扫描数据库结果ID
        :rtype: int
        """
        return self._DbResultId

    @DbResultId.setter
    def DbResultId(self, DbResultId):
        self._DbResultId = DbResultId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def DbName(self):
        """数据库名
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """所属数据表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """敏感数据分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CategoryIdList(self):
        """多级分类的分类ID集合
        :rtype: list of int
        """
        return self._CategoryIdList

    @CategoryIdList.setter
    def CategoryIdList(self, CategoryIdList):
        self._CategoryIdList = CategoryIdList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._DbResultId = params.get("DbResultId")
        self._ComplianceId = params.get("ComplianceId")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CategoryIdList = params.get("CategoryIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryTaskResultDetailResponse(AbstractModel):
    """DescribeDSPADiscoveryTaskResultDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 扫描结果详情列表
        :type Items: list of DspaDiscoveryTaskResultDetail
        :param _TotalCount: 符合条件的扫描结果详情记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """扫描结果详情列表
        :rtype: list of DspaDiscoveryTaskResultDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的扫描结果详情记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryTaskResultDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryTaskResultRequest(AbstractModel):
    """DescribeDSPADiscoveryTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _DataSourceType: 数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :type DataSourceType: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _Offset: 偏移量，默认值为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100
        :type Limit: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        """
        self._DspaId = None
        self._DataSourceType = None
        self._TaskId = None
        self._TaskName = None
        self._DataSourceId = None
        self._DbName = None
        self._Offset = None
        self._Limit = None
        self._ResourceRegion = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DataSourceType(self):
        """数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Offset(self):
        """偏移量，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DataSourceType = params.get("DataSourceType")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._DataSourceId = params.get("DataSourceId")
        self._DbName = params.get("DbName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryTaskResultResponse(AbstractModel):
    """DescribeDSPADiscoveryTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 扫描任务结果项
        :type Items: list of DspaDiscoveryTaskDbResult
        :param _TotalCount: 符合条件的扫描任务结果记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """扫描任务结果项
        :rtype: list of DspaDiscoveryTaskDbResult
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的扫描任务结果记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryTaskDbResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryTaskTablesRequest(AbstractModel):
    """DescribeDSPADiscoveryTaskTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _DbResultId: 数据库扫描结果ID
        :type DbResultId: int
        :param _DbName: db名称
        :type DbName: str
        """
        self._DspaId = None
        self._TaskId = None
        self._DbResultId = None
        self._DbName = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DbResultId(self):
        """数据库扫描结果ID
        :rtype: int
        """
        return self._DbResultId

    @DbResultId.setter
    def DbResultId(self, DbResultId):
        self._DbResultId = DbResultId

    @property
    def DbName(self):
        """db名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._DbResultId = params.get("DbResultId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryTaskTablesResponse(AbstractModel):
    """DescribeDSPADiscoveryTaskTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 分类分级扫描表集合
        :type Items: list of DSPATableInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """分类分级扫描表集合
        :rtype: list of DSPATableInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DSPATableInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPADiscoveryTasksRequest(AbstractModel):
    """DescribeDSPADiscoveryTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _DataSourceType: 数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :type DataSourceType: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Name: 任务名称
        :type Name: str
        :param _StatusList: 任务扫描结果状态，可供选择的状态值有：-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :type StatusList: list of int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :type Limit: int
        """
        self._DspaId = None
        self._DataSourceType = None
        self._TaskId = None
        self._Name = None
        self._StatusList = None
        self._Offset = None
        self._Limit = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DataSourceType(self):
        """数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StatusList(self):
        """任务扫描结果状态，可供选择的状态值有：-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :rtype: list of int
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回结果集数量，默认值是10000，最大值为10000，根据该资源的个数限制条件，该资源的个数不会超过10000，所以如果不输入该字段，默认获取全量数据
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DataSourceType = params.get("DataSourceType")
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._StatusList = params.get("StatusList")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPADiscoveryTasksResponse(AbstractModel):
    """DescribeDSPADiscoveryTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 任务列表
        :type Items: list of DspaDiscoveryTask
        :param _TotalCount: 符合条件的任务列表数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """任务列表
        :rtype: list of DspaDiscoveryTask
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的任务列表数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryTask()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPAESDataAssetByComplianceIdRequest(AbstractModel):
    """DescribeDSPAESDataAssetByComplianceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _BuildType: 云上还是自建

        :type BuildType: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._BuildType = None
        self._DataSourceType = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def BuildType(self):
        """云上还是自建

        :rtype: str
        """
        return self._BuildType

    @BuildType.setter
    def BuildType(self, BuildType):
        self._BuildType = BuildType

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._BuildType = params.get("BuildType")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAESDataAssetByComplianceIdResponse(AbstractModel):
    """DescribeDSPAESDataAssetByComplianceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Stats: 概览统计结果
        :type Stats: :class:`tencentcloud.dsgc.v20190723.models.ESDataAssetCountDto`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Stats = None
        self._RequestId = None

    @property
    def Stats(self):
        """概览统计结果
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ESDataAssetCountDto`
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

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
        if params.get("Stats") is not None:
            self._Stats = ESDataAssetCountDto()
            self._Stats._deserialize(params.get("Stats"))
        self._RequestId = params.get("RequestId")


class DescribeDSPAESDataAssetDetailRequest(AbstractModel):
    """DescribeDSPAESDataAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制条目数
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _CreditScore: 可信分排序，ASC升序
DESC降序
        :type CreditScore: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._CreditScore = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制条目数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def CreditScore(self):
        """可信分排序，ASC升序
DESC降序
        :rtype: str
        """
        return self._CreditScore

    @CreditScore.setter
    def CreditScore(self, CreditScore):
        self._CreditScore = CreditScore


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._CreditScore = params.get("CreditScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAESDataAssetDetailResponse(AbstractModel):
    """DescribeDSPAESDataAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总的个数
        :type TotalCount: int
        :param _Details: 概览详情列表
        :type Details: list of ESDataAssetDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总的个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        """概览详情列表
        :rtype: list of ESDataAssetDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ESDataAssetDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDSPAESDataSampleRequest(AbstractModel):
    """DescribeDSPAESDataSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _FieldResultId: 字段扫描结果ID
        :type FieldResultId: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._DspaId = None
        self._FieldResultId = None
        self._Order = None
        self._OrderField = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def FieldResultId(self):
        """字段扫描结果ID
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def Order(self):
        """排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._FieldResultId = params.get("FieldResultId")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAESDataSampleResponse(AbstractModel):
    """DescribeDSPAESDataSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 数据样本列表，最多10条数据
        :type Items: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """数据样本列表，最多10条数据
        :rtype: list of str
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Items = params.get("Items")
        self._RequestId = params.get("RequestId")


class DescribeDSPAESDiscoveryTaskResultDetailRequest(AbstractModel):
    """DescribeDSPAESDiscoveryTaskResultDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100
        :type Limit: int
        :param _CategoryIdList: 多级分类的分类ID集合
        :type CategoryIdList: list of int
        :param _LevelId: 敏感数据分级ID
        :type LevelId: int
        :param _DbName: 数据库名称
        :type DbName: str
        """
        self._DspaId = None
        self._TaskId = None
        self._ComplianceId = None
        self._Offset = None
        self._Limit = None
        self._CategoryIdList = None
        self._LevelId = None
        self._DbName = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CategoryIdList(self):
        """多级分类的分类ID集合
        :rtype: list of int
        """
        return self._CategoryIdList

    @CategoryIdList.setter
    def CategoryIdList(self, CategoryIdList):
        self._CategoryIdList = CategoryIdList

    @property
    def LevelId(self):
        """敏感数据分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._ComplianceId = params.get("ComplianceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CategoryIdList = params.get("CategoryIdList")
        self._LevelId = params.get("LevelId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPAESDiscoveryTaskResultDetailResponse(AbstractModel):
    """DescribeDSPAESDiscoveryTaskResultDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: ES扫描结果详情列表
        :type Items: list of ESTaskResultDetail
        :param _TotalCount: 符合条件的扫描结果详情记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """ES扫描结果详情列表
        :rtype: list of ESTaskResultDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的扫描结果详情记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ESTaskResultDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPALevelDetailRequest(AbstractModel):
    """DescribeDSPALevelDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Filters: 过滤数组。支持的Name：
ComplianceId 合规组ID
LevelGroupId 敏感分级组ID
        :type Filters: list of Filter
        """
        self._DspaId = None
        self._Filters = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Filters(self):
        """过滤数组。支持的Name：
ComplianceId 合规组ID
LevelGroupId 敏感分级组ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
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
        


class DescribeDSPALevelDetailResponse(AbstractModel):
    """DescribeDSPALevelDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 符合条件的敏感数据分级标识记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of LevelItem
        :param _TotalCount: 符合条件的敏感数据分级标识记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """符合条件的敏感数据分级标识记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LevelItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的敏感数据分级标识记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = LevelItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPALevelGroupsRequest(AbstractModel):
    """DescribeDSPALevelGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 分级组名称
        :type Name: str
        :param _Limit: 每页返回的记录数
        :type Limit: int
        :param _Offset: 从第几条记录开始返回
        :type Offset: int
        """
        self._DspaId = None
        self._Name = None
        self._Limit = None
        self._Offset = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """分级组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Limit(self):
        """每页返回的记录数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """从第几条记录开始返回
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPALevelGroupsResponse(AbstractModel):
    """DescribeDSPALevelGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 符合条件的敏感数据分级标识记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DspaDiscoveryLevelDetail
        :param _TotalCount: 符合条件的敏感数据分级标识记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        """符合条件的敏感数据分级标识记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DspaDiscoveryLevelDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        """符合条件的敏感数据分级标识记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaDiscoveryLevelDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPARDBDataAssetByComplianceIdRequest(AbstractModel):
    """DescribeDSPARDBDataAssetByComplianceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _DataSourceType: 数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
        :type DataSourceType: str
        :param _BuildType: 自建还是云上
        :type BuildType: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._DataSourceType = None
        self._BuildType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def DataSourceType(self):
        """数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def BuildType(self):
        """自建还是云上
        :rtype: str
        """
        return self._BuildType

    @BuildType.setter
    def BuildType(self, BuildType):
        self._BuildType = BuildType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._DataSourceType = params.get("DataSourceType")
        self._BuildType = params.get("BuildType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPARDBDataAssetByComplianceIdResponse(AbstractModel):
    """DescribeDSPARDBDataAssetByComplianceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Stats: 符合条件的RDB关系数据库敏感数据资产统计记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Stats: :class:`tencentcloud.dsgc.v20190723.models.DspaRDBDataAssetCount`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Stats = None
        self._RequestId = None

    @property
    def Stats(self):
        """符合条件的RDB关系数据库敏感数据资产统计记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaRDBDataAssetCount`
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

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
        if params.get("Stats") is not None:
            self._Stats = DspaRDBDataAssetCount()
            self._Stats._deserialize(params.get("Stats"))
        self._RequestId = params.get("RequestId")


class DescribeDSPARDBDataAssetDetailRequest(AbstractModel):
    """DescribeDSPARDBDataAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id
        :type DspaId: str
        :param _ComplianceId: 合规组Id
        :type ComplianceId: int
        :param _Filters: 过滤数组。支持的Name：
DataSourceID 数据源ID
DbName 数据库名称
CategoryID 敏感数据分类ID
RuleID 规则ID
LevelID 敏感分级ID
ResourceRegion 资源所在地域
SensitiveField 过滤敏感字段，可选值为1，或者无此SensitiveField字段
DataSourceType 数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
注意：每个name默认支持最多5个values。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _CreditScore: 可信分排序，ASC-升序
DESC降序
        :type CreditScore: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._CreditScore = None

    @property
    def DspaId(self):
        """DSPA实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组Id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def Filters(self):
        """过滤数组。支持的Name：
DataSourceID 数据源ID
DbName 数据库名称
CategoryID 敏感数据分类ID
RuleID 规则ID
LevelID 敏感分级ID
ResourceRegion 资源所在地域
SensitiveField 过滤敏感字段，可选值为1，或者无此SensitiveField字段
DataSourceType 数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
注意：每个name默认支持最多5个values。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreditScore(self):
        """可信分排序，ASC-升序
DESC降序
        :rtype: str
        """
        return self._CreditScore

    @CreditScore.setter
    def CreditScore(self, CreditScore):
        self._CreditScore = CreditScore


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreditScore = params.get("CreditScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPARDBDataAssetDetailResponse(AbstractModel):
    """DescribeDSPARDBDataAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: RDB关系数据库敏感数据资产详情列表
        :type Details: list of DspaRDBDataAssetDetail
        :param _TotalCount: 符合条件的RDB关系数据库敏感数据资产数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Details(self):
        """RDB关系数据库敏感数据资产详情列表
        :rtype: list of DspaRDBDataAssetDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def TotalCount(self):
        """符合条件的RDB关系数据库敏感数据资产数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DspaRDBDataAssetDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDSPASupportedMetasRequest(AbstractModel):
    """DescribeDSPASupportedMetas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MetaTypes: 元数据类型
        :type MetaTypes: list of str
        """
        self._MetaTypes = None

    @property
    def MetaTypes(self):
        """元数据类型
        :rtype: list of str
        """
        return self._MetaTypes

    @MetaTypes.setter
    def MetaTypes(self, MetaTypes):
        self._MetaTypes = MetaTypes


    def _deserialize(self, params):
        self._MetaTypes = params.get("MetaTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPASupportedMetasResponse(AbstractModel):
    """DescribeDSPASupportedMetas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metas: 支持的元数据类型
        :type Metas: list of DSPAMetaType
        :param _MaxDBInstanceLimit: 最大支持每批次同步数量
        :type MaxDBInstanceLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metas = None
        self._MaxDBInstanceLimit = None
        self._RequestId = None

    @property
    def Metas(self):
        """支持的元数据类型
        :rtype: list of DSPAMetaType
        """
        return self._Metas

    @Metas.setter
    def Metas(self, Metas):
        self._Metas = Metas

    @property
    def MaxDBInstanceLimit(self):
        """最大支持每批次同步数量
        :rtype: int
        """
        return self._MaxDBInstanceLimit

    @MaxDBInstanceLimit.setter
    def MaxDBInstanceLimit(self, MaxDBInstanceLimit):
        self._MaxDBInstanceLimit = MaxDBInstanceLimit

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
        if params.get("Metas") is not None:
            self._Metas = []
            for item in params.get("Metas"):
                obj = DSPAMetaType()
                obj._deserialize(item)
                self._Metas.append(obj)
        self._MaxDBInstanceLimit = params.get("MaxDBInstanceLimit")
        self._RequestId = params.get("RequestId")


class DescribeDSPATaskResultDataSampleRequest(AbstractModel):
    """DescribeDSPATaskResultDataSample请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _FieldResultId: 字段扫描结果ID
        :type FieldResultId: int
        :param _Order: 排序方式
        :type Order: str
        :param _OrderField: 排序字段
        :type OrderField: str
        """
        self._DspaId = None
        self._FieldResultId = None
        self._Order = None
        self._OrderField = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def FieldResultId(self):
        """字段扫描结果ID
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def Order(self):
        """排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序字段
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._FieldResultId = params.get("FieldResultId")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDSPATaskResultDataSampleResponse(AbstractModel):
    """DescribeDSPATaskResultDataSample返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 数据样本列表，最多10条数据
        :type Items: list of DspaFieldResultDataSample
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """数据样本列表，最多10条数据
        :rtype: list of DspaFieldResultDataSample
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaFieldResultDataSample()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeESAssetSensitiveDistributionRequest(AbstractModel):
    """DescribeESAssetSensitiveDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESAssetSensitiveDistributionResponse(AbstractModel):
    """DescribeESAssetSensitiveDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ESAsset: ES的资产统计数据
        :type ESAsset: :class:`tencentcloud.dsgc.v20190723.models.ESAsset`
        :param _TopAsset: 涉敏top数据
        :type TopAsset: list of TopAsset
        :param _ESDetail: ES的详情列表
        :type ESDetail: list of ESAssetDBDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ESAsset = None
        self._TopAsset = None
        self._ESDetail = None
        self._RequestId = None

    @property
    def ESAsset(self):
        """ES的资产统计数据
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ESAsset`
        """
        return self._ESAsset

    @ESAsset.setter
    def ESAsset(self, ESAsset):
        self._ESAsset = ESAsset

    @property
    def TopAsset(self):
        """涉敏top数据
        :rtype: list of TopAsset
        """
        return self._TopAsset

    @TopAsset.setter
    def TopAsset(self, TopAsset):
        self._TopAsset = TopAsset

    @property
    def ESDetail(self):
        """ES的详情列表
        :rtype: list of ESAssetDBDetail
        """
        return self._ESDetail

    @ESDetail.setter
    def ESDetail(self, ESDetail):
        self._ESDetail = ESDetail

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
        if params.get("ESAsset") is not None:
            self._ESAsset = ESAsset()
            self._ESAsset._deserialize(params.get("ESAsset"))
        if params.get("TopAsset") is not None:
            self._TopAsset = []
            for item in params.get("TopAsset"):
                obj = TopAsset()
                obj._deserialize(item)
                self._TopAsset.append(obj)
        if params.get("ESDetail") is not None:
            self._ESDetail = []
            for item in params.get("ESDetail"):
                obj = ESAssetDBDetail()
                obj._deserialize(item)
                self._ESDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExportTaskResultRequest(AbstractModel):
    """DescribeExportTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ExportTaskId: 导出任务id
        :type ExportTaskId: int
        """
        self._DspaId = None
        self._ExportTaskId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ExportTaskId(self):
        """导出任务id
        :rtype: int
        """
        return self._ExportTaskId

    @ExportTaskId.setter
    def ExportTaskId(self, ExportTaskId):
        self._ExportTaskId = ExportTaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ExportTaskId = params.get("ExportTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportTaskResultResponse(AbstractModel):
    """DescribeExportTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportResult: 导出任务结果
        :type ExportResult: str
        :param _ExportFileUrl: 导出文件地址
        :type ExportFileUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportResult = None
        self._ExportFileUrl = None
        self._RequestId = None

    @property
    def ExportResult(self):
        """导出任务结果
        :rtype: str
        """
        return self._ExportResult

    @ExportResult.setter
    def ExportResult(self, ExportResult):
        self._ExportResult = ExportResult

    @property
    def ExportFileUrl(self):
        """导出文件地址
        :rtype: str
        """
        return self._ExportFileUrl

    @ExportFileUrl.setter
    def ExportFileUrl(self, ExportFileUrl):
        self._ExportFileUrl = ExportFileUrl

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
        self._ExportResult = params.get("ExportResult")
        self._ExportFileUrl = params.get("ExportFileUrl")
        self._RequestId = params.get("RequestId")


class DescribeMongoAssetSensitiveDistributionRequest(AbstractModel):
    """DescribeMongoAssetSensitiveDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMongoAssetSensitiveDistributionResponse(AbstractModel):
    """DescribeMongoAssetSensitiveDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MongoAsset: mongo的资产统计数据
        :type MongoAsset: :class:`tencentcloud.dsgc.v20190723.models.MongoAsset`
        :param _TopAsset: 涉敏top数据
        :type TopAsset: list of TopAsset
        :param _MongoDetail: mongo的详情列表
        :type MongoDetail: list of MongoAssetDBDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MongoAsset = None
        self._TopAsset = None
        self._MongoDetail = None
        self._RequestId = None

    @property
    def MongoAsset(self):
        """mongo的资产统计数据
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.MongoAsset`
        """
        return self._MongoAsset

    @MongoAsset.setter
    def MongoAsset(self, MongoAsset):
        self._MongoAsset = MongoAsset

    @property
    def TopAsset(self):
        """涉敏top数据
        :rtype: list of TopAsset
        """
        return self._TopAsset

    @TopAsset.setter
    def TopAsset(self, TopAsset):
        self._TopAsset = TopAsset

    @property
    def MongoDetail(self):
        """mongo的详情列表
        :rtype: list of MongoAssetDBDetail
        """
        return self._MongoDetail

    @MongoDetail.setter
    def MongoDetail(self, MongoDetail):
        self._MongoDetail = MongoDetail

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
        if params.get("MongoAsset") is not None:
            self._MongoAsset = MongoAsset()
            self._MongoAsset._deserialize(params.get("MongoAsset"))
        if params.get("TopAsset") is not None:
            self._TopAsset = []
            for item in params.get("TopAsset"):
                obj = TopAsset()
                obj._deserialize(item)
                self._TopAsset.append(obj)
        if params.get("MongoDetail") is not None:
            self._MongoDetail = []
            for item in params.get("MongoDetail"):
                obj = MongoAssetDBDetail()
                obj._deserialize(item)
                self._MongoDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRDBAssetSensitiveDistributionRequest(AbstractModel):
    """DescribeRDBAssetSensitiveDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRDBAssetSensitiveDistributionResponse(AbstractModel):
    """DescribeRDBAssetSensitiveDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RDBAsset: rdb的资产统计数据
        :type RDBAsset: :class:`tencentcloud.dsgc.v20190723.models.RDBAsset`
        :param _TopAsset: 涉敏top数据
        :type TopAsset: list of TopAsset
        :param _RDBDetail: rdb的详情列表
        :type RDBDetail: list of AssetDBDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RDBAsset = None
        self._TopAsset = None
        self._RDBDetail = None
        self._RequestId = None

    @property
    def RDBAsset(self):
        """rdb的资产统计数据
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.RDBAsset`
        """
        return self._RDBAsset

    @RDBAsset.setter
    def RDBAsset(self, RDBAsset):
        self._RDBAsset = RDBAsset

    @property
    def TopAsset(self):
        """涉敏top数据
        :rtype: list of TopAsset
        """
        return self._TopAsset

    @TopAsset.setter
    def TopAsset(self, TopAsset):
        self._TopAsset = TopAsset

    @property
    def RDBDetail(self):
        """rdb的详情列表
        :rtype: list of AssetDBDetail
        """
        return self._RDBDetail

    @RDBDetail.setter
    def RDBDetail(self, RDBDetail):
        self._RDBDetail = RDBDetail

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
        if params.get("RDBAsset") is not None:
            self._RDBAsset = RDBAsset()
            self._RDBAsset._deserialize(params.get("RDBAsset"))
        if params.get("TopAsset") is not None:
            self._TopAsset = []
            for item in params.get("TopAsset"):
                obj = TopAsset()
                obj._deserialize(item)
                self._TopAsset.append(obj)
        if params.get("RDBDetail") is not None:
            self._RDBDetail = []
            for item in params.get("RDBDetail"):
                obj = AssetDBDetail()
                obj._deserialize(item)
                self._RDBDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReportTaskDownloadUrlRequest(AbstractModel):
    """DescribeReportTaskDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportTaskId: 任务id
        :type ReportTaskId: int
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _IsWithSensitiveDetailReport: 是否同时下载敏感资产详情报告
        :type IsWithSensitiveDetailReport: bool
        """
        self._ReportTaskId = None
        self._DspaId = None
        self._IsWithSensitiveDetailReport = None

    @property
    def ReportTaskId(self):
        """任务id
        :rtype: int
        """
        return self._ReportTaskId

    @ReportTaskId.setter
    def ReportTaskId(self, ReportTaskId):
        self._ReportTaskId = ReportTaskId

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def IsWithSensitiveDetailReport(self):
        """是否同时下载敏感资产详情报告
        :rtype: bool
        """
        return self._IsWithSensitiveDetailReport

    @IsWithSensitiveDetailReport.setter
    def IsWithSensitiveDetailReport(self, IsWithSensitiveDetailReport):
        self._IsWithSensitiveDetailReport = IsWithSensitiveDetailReport


    def _deserialize(self, params):
        self._ReportTaskId = params.get("ReportTaskId")
        self._DspaId = params.get("DspaId")
        self._IsWithSensitiveDetailReport = params.get("IsWithSensitiveDetailReport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportTaskDownloadUrlResponse(AbstractModel):
    """DescribeReportTaskDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrlSet: 下载链接集合
        :type DownloadUrlSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrlSet = None
        self._RequestId = None

    @property
    def DownloadUrlSet(self):
        """下载链接集合
        :rtype: list of str
        """
        return self._DownloadUrlSet

    @DownloadUrlSet.setter
    def DownloadUrlSet(self, DownloadUrlSet):
        self._DownloadUrlSet = DownloadUrlSet

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
        self._DownloadUrlSet = params.get("DownloadUrlSet")
        self._RequestId = params.get("RequestId")


class DescribeReportTasksRequest(AbstractModel):
    """DescribeReportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _ReportName: 报表名称
        :type ReportName: str
        """
        self._DspaId = None
        self._Limit = None
        self._Offset = None
        self._ReportName = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

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
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ReportName(self):
        """报表名称
        :rtype: str
        """
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ReportName = params.get("ReportName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportTasksResponse(AbstractModel):
    """DescribeReportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _ItemSet: 报表信息
        :type ItemSet: list of ReportInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ItemSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ItemSet(self):
        """报表信息
        :rtype: list of ReportInfo
        """
        return self._ItemSet

    @ItemSet.setter
    def ItemSet(self, ItemSet):
        self._ItemSet = ItemSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("ItemSet") is not None:
            self._ItemSet = []
            for item in params.get("ItemSet"):
                obj = ReportInfo()
                obj._deserialize(item)
                self._ItemSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSensitiveCOSDataDistributionRequest(AbstractModel):
    """DescribeSensitiveCOSDataDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _ComplianceId: 2331
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """2331
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSensitiveCOSDataDistributionResponse(AbstractModel):
    """DescribeSensitiveCOSDataDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LevelDistribution: 分级分布
        :type LevelDistribution: list of Note
        :param _CategoryDistribution: 分类分布
        :type CategoryDistribution: list of Note
        :param _RuleDistribution: 规则分布详情
        :type RuleDistribution: list of RuleDistribution
        :param _SensitiveDataNum: 计算占比
        :type SensitiveDataNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LevelDistribution = None
        self._CategoryDistribution = None
        self._RuleDistribution = None
        self._SensitiveDataNum = None
        self._RequestId = None

    @property
    def LevelDistribution(self):
        """分级分布
        :rtype: list of Note
        """
        return self._LevelDistribution

    @LevelDistribution.setter
    def LevelDistribution(self, LevelDistribution):
        self._LevelDistribution = LevelDistribution

    @property
    def CategoryDistribution(self):
        """分类分布
        :rtype: list of Note
        """
        return self._CategoryDistribution

    @CategoryDistribution.setter
    def CategoryDistribution(self, CategoryDistribution):
        self._CategoryDistribution = CategoryDistribution

    @property
    def RuleDistribution(self):
        """规则分布详情
        :rtype: list of RuleDistribution
        """
        return self._RuleDistribution

    @RuleDistribution.setter
    def RuleDistribution(self, RuleDistribution):
        self._RuleDistribution = RuleDistribution

    @property
    def SensitiveDataNum(self):
        """计算占比
        :rtype: int
        """
        return self._SensitiveDataNum

    @SensitiveDataNum.setter
    def SensitiveDataNum(self, SensitiveDataNum):
        self._SensitiveDataNum = SensitiveDataNum

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
        if params.get("LevelDistribution") is not None:
            self._LevelDistribution = []
            for item in params.get("LevelDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._LevelDistribution.append(obj)
        if params.get("CategoryDistribution") is not None:
            self._CategoryDistribution = []
            for item in params.get("CategoryDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._CategoryDistribution.append(obj)
        if params.get("RuleDistribution") is not None:
            self._RuleDistribution = []
            for item in params.get("RuleDistribution"):
                obj = RuleDistribution()
                obj._deserialize(item)
                self._RuleDistribution.append(obj)
        self._SensitiveDataNum = params.get("SensitiveDataNum")
        self._RequestId = params.get("RequestId")


class DescribeSensitiveRDBDataDistributionRequest(AbstractModel):
    """DescribeSensitiveRDBDataDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa-实例id
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _AssetList: 查询的资产信息列表
        :type AssetList: list of AssetList
        """
        self._DspaId = None
        self._ComplianceId = None
        self._AssetList = None

    @property
    def DspaId(self):
        """dspa-实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def AssetList(self):
        """查询的资产信息列表
        :rtype: list of AssetList
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        if params.get("AssetList") is not None:
            self._AssetList = []
            for item in params.get("AssetList"):
                obj = AssetList()
                obj._deserialize(item)
                self._AssetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSensitiveRDBDataDistributionResponse(AbstractModel):
    """DescribeSensitiveRDBDataDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LevelDistribution: 分级分布
        :type LevelDistribution: list of Note
        :param _CategoryDistribution: 分类分布
        :type CategoryDistribution: list of Note
        :param _RuleDistribution: 敏感规则分布详情列表
        :type RuleDistribution: list of RuleDistribution
        :param _SensitiveDataNum: 计算占比字段
        :type SensitiveDataNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LevelDistribution = None
        self._CategoryDistribution = None
        self._RuleDistribution = None
        self._SensitiveDataNum = None
        self._RequestId = None

    @property
    def LevelDistribution(self):
        """分级分布
        :rtype: list of Note
        """
        return self._LevelDistribution

    @LevelDistribution.setter
    def LevelDistribution(self, LevelDistribution):
        self._LevelDistribution = LevelDistribution

    @property
    def CategoryDistribution(self):
        """分类分布
        :rtype: list of Note
        """
        return self._CategoryDistribution

    @CategoryDistribution.setter
    def CategoryDistribution(self, CategoryDistribution):
        self._CategoryDistribution = CategoryDistribution

    @property
    def RuleDistribution(self):
        """敏感规则分布详情列表
        :rtype: list of RuleDistribution
        """
        return self._RuleDistribution

    @RuleDistribution.setter
    def RuleDistribution(self, RuleDistribution):
        self._RuleDistribution = RuleDistribution

    @property
    def SensitiveDataNum(self):
        """计算占比字段
        :rtype: int
        """
        return self._SensitiveDataNum

    @SensitiveDataNum.setter
    def SensitiveDataNum(self, SensitiveDataNum):
        self._SensitiveDataNum = SensitiveDataNum

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
        if params.get("LevelDistribution") is not None:
            self._LevelDistribution = []
            for item in params.get("LevelDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._LevelDistribution.append(obj)
        if params.get("CategoryDistribution") is not None:
            self._CategoryDistribution = []
            for item in params.get("CategoryDistribution"):
                obj = Note()
                obj._deserialize(item)
                self._CategoryDistribution.append(obj)
        if params.get("RuleDistribution") is not None:
            self._RuleDistribution = []
            for item in params.get("RuleDistribution"):
                obj = RuleDistribution()
                obj._deserialize(item)
                self._RuleDistribution.append(obj)
        self._SensitiveDataNum = params.get("SensitiveDataNum")
        self._RequestId = params.get("RequestId")


class DisableDSPAMetaResourceAuthRequest(AbstractModel):
    """DisableDSPAMetaResourceAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _MetaType: 资源类型。
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourceIDs: 用户云资源ID列表。
        :type ResourceIDs: list of str
        """
        self._DspaId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._ResourceIDs = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MetaType(self):
        """资源类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceIDs(self):
        """用户云资源ID列表。
        :rtype: list of str
        """
        return self._ResourceIDs

    @ResourceIDs.setter
    def ResourceIDs(self, ResourceIDs):
        self._ResourceIDs = ResourceIDs


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceIDs = params.get("ResourceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableDSPAMetaResourceAuthResponse(AbstractModel):
    """DisableDSPAMetaResourceAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _Results: 授权结果。
        :type Results: list of DspaTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DspaId = None
        self._Results = None
        self._RequestId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Results(self):
        """授权结果。
        :rtype: list of DspaTaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        self._DspaId = params.get("DspaId")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DspaTaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DiscoveryCondition(AbstractModel):
    """DSPA敏感数据扫描数据源条件

    """

    def __init__(self):
        r"""
        :param _RDBInstances: RDB实例列表
        :type RDBInstances: list of RDBInstance
        :param _COSInstances: COS实例列表
        :type COSInstances: list of COSInstance
        :param _NOSQLInstances: Mongo实例列表
        :type NOSQLInstances: list of NOSQLInstance
        :param _ESInstances: ES实例列表
        :type ESInstances: list of ESInstance
        """
        self._RDBInstances = None
        self._COSInstances = None
        self._NOSQLInstances = None
        self._ESInstances = None

    @property
    def RDBInstances(self):
        """RDB实例列表
        :rtype: list of RDBInstance
        """
        return self._RDBInstances

    @RDBInstances.setter
    def RDBInstances(self, RDBInstances):
        self._RDBInstances = RDBInstances

    @property
    def COSInstances(self):
        """COS实例列表
        :rtype: list of COSInstance
        """
        return self._COSInstances

    @COSInstances.setter
    def COSInstances(self, COSInstances):
        self._COSInstances = COSInstances

    @property
    def NOSQLInstances(self):
        """Mongo实例列表
        :rtype: list of NOSQLInstance
        """
        return self._NOSQLInstances

    @NOSQLInstances.setter
    def NOSQLInstances(self, NOSQLInstances):
        self._NOSQLInstances = NOSQLInstances

    @property
    def ESInstances(self):
        """ES实例列表
        :rtype: list of ESInstance
        """
        return self._ESInstances

    @ESInstances.setter
    def ESInstances(self, ESInstances):
        self._ESInstances = ESInstances


    def _deserialize(self, params):
        if params.get("RDBInstances") is not None:
            self._RDBInstances = []
            for item in params.get("RDBInstances"):
                obj = RDBInstance()
                obj._deserialize(item)
                self._RDBInstances.append(obj)
        if params.get("COSInstances") is not None:
            self._COSInstances = []
            for item in params.get("COSInstances"):
                obj = COSInstance()
                obj._deserialize(item)
                self._COSInstances.append(obj)
        if params.get("NOSQLInstances") is not None:
            self._NOSQLInstances = []
            for item in params.get("NOSQLInstances"):
                obj = NOSQLInstance()
                obj._deserialize(item)
                self._NOSQLInstances.append(obj)
        if params.get("ESInstances") is not None:
            self._ESInstances = []
            for item in params.get("ESInstances"):
                obj = ESInstance()
                obj._deserialize(item)
                self._ESInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaAssessmentFilter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询

    """

    def __init__(self):
        r"""
        :param _Name: 过滤类型。
        :type Name: str
        :param _Values: 过滤类型的值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤类型。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """过滤类型的值。
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
        


class DspaCOSDataAssetCount(AbstractModel):
    """COS对象存储敏感数据资产统计

    """

    def __init__(self):
        r"""
        :param _DataAssetType: 数组资产类型，0代表关系型数据库资产，1代表对象存储COS资产
        :type DataAssetType: int
        :param _TotalBucketCnt: 已扫描的存储桶的个数
        :type TotalBucketCnt: int
        :param _TotalObjectCnt: 对象总数
        :type TotalObjectCnt: int
        :param _SensitiveCategoryCnt: 敏感数据类型个数
        :type SensitiveCategoryCnt: int
        :param _SensitiveDataCnt: 敏感数据条数
        :type SensitiveDataCnt: int
        :param _SensitiveLevel: 敏感等级分布
        :type SensitiveLevel: list of SensitiveLevel
        :param _SensitiveBucketCnt: 敏感存储桶个数
        :type SensitiveBucketCnt: int
        :param _SensitiveObjectCnt: 敏感对象个数
        :type SensitiveObjectCnt: int
        :param _CategoryDistributed: 数据分类分布
        :type CategoryDistributed: list of DspaDataCategoryDistributed
        """
        self._DataAssetType = None
        self._TotalBucketCnt = None
        self._TotalObjectCnt = None
        self._SensitiveCategoryCnt = None
        self._SensitiveDataCnt = None
        self._SensitiveLevel = None
        self._SensitiveBucketCnt = None
        self._SensitiveObjectCnt = None
        self._CategoryDistributed = None

    @property
    def DataAssetType(self):
        """数组资产类型，0代表关系型数据库资产，1代表对象存储COS资产
        :rtype: int
        """
        return self._DataAssetType

    @DataAssetType.setter
    def DataAssetType(self, DataAssetType):
        self._DataAssetType = DataAssetType

    @property
    def TotalBucketCnt(self):
        """已扫描的存储桶的个数
        :rtype: int
        """
        return self._TotalBucketCnt

    @TotalBucketCnt.setter
    def TotalBucketCnt(self, TotalBucketCnt):
        self._TotalBucketCnt = TotalBucketCnt

    @property
    def TotalObjectCnt(self):
        """对象总数
        :rtype: int
        """
        return self._TotalObjectCnt

    @TotalObjectCnt.setter
    def TotalObjectCnt(self, TotalObjectCnt):
        self._TotalObjectCnt = TotalObjectCnt

    @property
    def SensitiveCategoryCnt(self):
        """敏感数据类型个数
        :rtype: int
        """
        return self._SensitiveCategoryCnt

    @SensitiveCategoryCnt.setter
    def SensitiveCategoryCnt(self, SensitiveCategoryCnt):
        self._SensitiveCategoryCnt = SensitiveCategoryCnt

    @property
    def SensitiveDataCnt(self):
        """敏感数据条数
        :rtype: int
        """
        return self._SensitiveDataCnt

    @SensitiveDataCnt.setter
    def SensitiveDataCnt(self, SensitiveDataCnt):
        self._SensitiveDataCnt = SensitiveDataCnt

    @property
    def SensitiveLevel(self):
        """敏感等级分布
        :rtype: list of SensitiveLevel
        """
        return self._SensitiveLevel

    @SensitiveLevel.setter
    def SensitiveLevel(self, SensitiveLevel):
        self._SensitiveLevel = SensitiveLevel

    @property
    def SensitiveBucketCnt(self):
        """敏感存储桶个数
        :rtype: int
        """
        return self._SensitiveBucketCnt

    @SensitiveBucketCnt.setter
    def SensitiveBucketCnt(self, SensitiveBucketCnt):
        self._SensitiveBucketCnt = SensitiveBucketCnt

    @property
    def SensitiveObjectCnt(self):
        """敏感对象个数
        :rtype: int
        """
        return self._SensitiveObjectCnt

    @SensitiveObjectCnt.setter
    def SensitiveObjectCnt(self, SensitiveObjectCnt):
        self._SensitiveObjectCnt = SensitiveObjectCnt

    @property
    def CategoryDistributed(self):
        """数据分类分布
        :rtype: list of DspaDataCategoryDistributed
        """
        return self._CategoryDistributed

    @CategoryDistributed.setter
    def CategoryDistributed(self, CategoryDistributed):
        self._CategoryDistributed = CategoryDistributed


    def _deserialize(self, params):
        self._DataAssetType = params.get("DataAssetType")
        self._TotalBucketCnt = params.get("TotalBucketCnt")
        self._TotalObjectCnt = params.get("TotalObjectCnt")
        self._SensitiveCategoryCnt = params.get("SensitiveCategoryCnt")
        self._SensitiveDataCnt = params.get("SensitiveDataCnt")
        if params.get("SensitiveLevel") is not None:
            self._SensitiveLevel = []
            for item in params.get("SensitiveLevel"):
                obj = SensitiveLevel()
                obj._deserialize(item)
                self._SensitiveLevel.append(obj)
        self._SensitiveBucketCnt = params.get("SensitiveBucketCnt")
        self._SensitiveObjectCnt = params.get("SensitiveObjectCnt")
        if params.get("CategoryDistributed") is not None:
            self._CategoryDistributed = []
            for item in params.get("CategoryDistributed"):
                obj = DspaDataCategoryDistributed()
                obj._deserialize(item)
                self._CategoryDistributed.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCOSDataAssetDetail(AbstractModel):
    """COS对象存储数据资产详情

    """

    def __init__(self):
        r"""
        :param _BucketName: 对象桶
        :type BucketName: str
        :param _FileName: 对象名称
        :type FileName: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _SensitiveDataCount: 出现次数
        :type SensitiveDataCount: int
        :param _CategoryName: 敏感数据分类
        :type CategoryName: str
        :param _LevelRiskName: 敏感等级
        :type LevelRiskName: str
        :param _KMSEncrypted: KMS加密
        :type KMSEncrypted: bool
        :param _FileType: 文件类型
        :type FileType: str
        :param _FileSize: 文件大小
        :type FileSize: str
        :param _LevelRiskScore: 敏感数据分级分数
        :type LevelRiskScore: int
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _RuleId: 规则id
        :type RuleId: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _CategoryId: 分类ID
        :type CategoryId: int
        :param _LevelId: 分级ID
        :type LevelId: int
        :param _FileResultId: 文件扫描结果ID
        :type FileResultId: int
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _CategoryFullPath: 分类路径
        :type CategoryFullPath: str
        :param _IdentifyType: 0-系统识别
1-人工识别
        :type IdentifyType: int
        :param _CheckStatus: 0-系统识别
1-人工识别
        :type CheckStatus: int
        """
        self._BucketName = None
        self._FileName = None
        self._RuleName = None
        self._SensitiveDataCount = None
        self._CategoryName = None
        self._LevelRiskName = None
        self._KMSEncrypted = None
        self._FileType = None
        self._FileSize = None
        self._LevelRiskScore = None
        self._DataSourceId = None
        self._RuleId = None
        self._ResourceRegion = None
        self._CategoryId = None
        self._LevelId = None
        self._FileResultId = None
        self._DataSourceName = None
        self._CategoryFullPath = None
        self._IdentifyType = None
        self._CheckStatus = None

    @property
    def BucketName(self):
        """对象桶
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def FileName(self):
        """对象名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def SensitiveDataCount(self):
        """出现次数
        :rtype: int
        """
        return self._SensitiveDataCount

    @SensitiveDataCount.setter
    def SensitiveDataCount(self, SensitiveDataCount):
        self._SensitiveDataCount = SensitiveDataCount

    @property
    def CategoryName(self):
        """敏感数据分类
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def LevelRiskName(self):
        """敏感等级
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def KMSEncrypted(self):
        """KMS加密
        :rtype: bool
        """
        return self._KMSEncrypted

    @KMSEncrypted.setter
    def KMSEncrypted(self, KMSEncrypted):
        self._KMSEncrypted = KMSEncrypted

    @property
    def FileType(self):
        """文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileSize(self):
        """文件大小
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def LevelRiskScore(self):
        """敏感数据分级分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def CategoryId(self):
        """分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def FileResultId(self):
        """文件扫描结果ID
        :rtype: int
        """
        return self._FileResultId

    @FileResultId.setter
    def FileResultId(self, FileResultId):
        self._FileResultId = FileResultId

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def CategoryFullPath(self):
        """分类路径
        :rtype: str
        """
        return self._CategoryFullPath

    @CategoryFullPath.setter
    def CategoryFullPath(self, CategoryFullPath):
        self._CategoryFullPath = CategoryFullPath

    @property
    def IdentifyType(self):
        """0-系统识别
1-人工识别
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def CheckStatus(self):
        """0-系统识别
1-人工识别
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._FileName = params.get("FileName")
        self._RuleName = params.get("RuleName")
        self._SensitiveDataCount = params.get("SensitiveDataCount")
        self._CategoryName = params.get("CategoryName")
        self._LevelRiskName = params.get("LevelRiskName")
        self._KMSEncrypted = params.get("KMSEncrypted")
        self._FileType = params.get("FileType")
        self._FileSize = params.get("FileSize")
        self._LevelRiskScore = params.get("LevelRiskScore")
        self._DataSourceId = params.get("DataSourceId")
        self._RuleId = params.get("RuleId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        self._FileResultId = params.get("FileResultId")
        self._DataSourceName = params.get("DataSourceName")
        self._CategoryFullPath = params.get("CategoryFullPath")
        self._IdentifyType = params.get("IdentifyType")
        self._CheckStatus = params.get("CheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCOSDiscoveryTask(AbstractModel):
    """COS敏感数据扫描任务相关信息

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _Period: 执行周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _Plan: 执行计划，0立即 1定时
        :type Plan: int
        :param _Enable: 任务开关；1 打开，0 关闭
        :type Enable: int
        :param _DataSourceInfo: 数据源对象信息
        :type DataSourceInfo: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDataSourceInfo`
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _Result: 任务最新的一次执行结果信息，该字段用于查询任务列表接口
        :type Result: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskResult`
        :param _TimingStartTime: 定时开始时间
        :type TimingStartTime: str
        :param _ComplianceUpdate: 关联分类模板是否更新
        :type ComplianceUpdate: bool
        """
        self._Name = None
        self._Description = None
        self._Period = None
        self._Plan = None
        self._Enable = None
        self._DataSourceInfo = None
        self._GeneralRuleSetEnable = None
        self._Result = None
        self._TimingStartTime = None
        self._ComplianceUpdate = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Period(self):
        """执行周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Plan(self):
        """执行计划，0立即 1定时
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Enable(self):
        """任务开关；1 打开，0 关闭
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DataSourceInfo(self):
        """数据源对象信息
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDataSourceInfo`
        """
        return self._DataSourceInfo

    @DataSourceInfo.setter
    def DataSourceInfo(self, DataSourceInfo):
        self._DataSourceInfo = DataSourceInfo

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def Result(self):
        """任务最新的一次执行结果信息，该字段用于查询任务列表接口
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TimingStartTime(self):
        """定时开始时间
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def ComplianceUpdate(self):
        """关联分类模板是否更新
        :rtype: bool
        """
        return self._ComplianceUpdate

    @ComplianceUpdate.setter
    def ComplianceUpdate(self, ComplianceUpdate):
        self._ComplianceUpdate = ComplianceUpdate


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Period = params.get("Period")
        self._Plan = params.get("Plan")
        self._Enable = params.get("Enable")
        if params.get("DataSourceInfo") is not None:
            self._DataSourceInfo = DspaCOSDiscoveryTaskDataSourceInfo()
            self._DataSourceInfo._deserialize(params.get("DataSourceInfo"))
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        if params.get("Result") is not None:
            self._Result = ScanTaskResult()
            self._Result._deserialize(params.get("Result"))
        self._TimingStartTime = params.get("TimingStartTime")
        self._ComplianceUpdate = params.get("ComplianceUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCOSDiscoveryTaskDataSourceInfo(AbstractModel):
    """扫描任务元数据信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _ProxyAddress: 代理地址
        :type ProxyAddress: list of str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _Condition: 扫描任务条件
        :type Condition: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskCOSCondition`
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        """
        self._DataSourceId = None
        self._ProxyAddress = None
        self._DataSourceName = None
        self._Condition = None
        self._ResourceRegion = None

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def ProxyAddress(self):
        """代理地址
        :rtype: list of str
        """
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def Condition(self):
        """扫描任务条件
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskCOSCondition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._ProxyAddress = params.get("ProxyAddress")
        self._DataSourceName = params.get("DataSourceName")
        if params.get("Condition") is not None:
            self._Condition = DspaDiscoveryTaskCOSCondition()
            self._Condition._deserialize(params.get("Condition"))
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCOSDiscoveryTaskDetail(AbstractModel):
    """COS敏感数据扫描任务相关信息

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _Period: 执行周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _Plan: 执行计划，0立即 1定时
        :type Plan: int
        :param _Enable: 任务开关；1 打开，0 关闭
        :type Enable: int
        :param _DataSourceInfo: 数据源对象信息
        :type DataSourceInfo: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDataSourceInfo`
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _DefaultComplianceInfo: 当创建任务时，用户打开了通用规则集开关，则该字段就会保存默认合规组信息
        :type DefaultComplianceInfo: list of ScanTaskComplianceInfo
        :param _CustomComplianceInfo: 该任务中用户选择的合规组信息列表
        :type CustomComplianceInfo: list of ScanTaskComplianceInfo
        :param _TimingStartTime: 定时开始时间
        :type TimingStartTime: str
        """
        self._Name = None
        self._Description = None
        self._Period = None
        self._Plan = None
        self._Enable = None
        self._DataSourceInfo = None
        self._GeneralRuleSetEnable = None
        self._DefaultComplianceInfo = None
        self._CustomComplianceInfo = None
        self._TimingStartTime = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Period(self):
        """执行周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Plan(self):
        """执行计划，0立即 1定时
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Enable(self):
        """任务开关；1 打开，0 关闭
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DataSourceInfo(self):
        """数据源对象信息
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaCOSDiscoveryTaskDataSourceInfo`
        """
        return self._DataSourceInfo

    @DataSourceInfo.setter
    def DataSourceInfo(self, DataSourceInfo):
        self._DataSourceInfo = DataSourceInfo

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def DefaultComplianceInfo(self):
        """当创建任务时，用户打开了通用规则集开关，则该字段就会保存默认合规组信息
        :rtype: list of ScanTaskComplianceInfo
        """
        return self._DefaultComplianceInfo

    @DefaultComplianceInfo.setter
    def DefaultComplianceInfo(self, DefaultComplianceInfo):
        self._DefaultComplianceInfo = DefaultComplianceInfo

    @property
    def CustomComplianceInfo(self):
        """该任务中用户选择的合规组信息列表
        :rtype: list of ScanTaskComplianceInfo
        """
        return self._CustomComplianceInfo

    @CustomComplianceInfo.setter
    def CustomComplianceInfo(self, CustomComplianceInfo):
        self._CustomComplianceInfo = CustomComplianceInfo

    @property
    def TimingStartTime(self):
        """定时开始时间
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Period = params.get("Period")
        self._Plan = params.get("Plan")
        self._Enable = params.get("Enable")
        if params.get("DataSourceInfo") is not None:
            self._DataSourceInfo = DspaCOSDiscoveryTaskDataSourceInfo()
            self._DataSourceInfo._deserialize(params.get("DataSourceInfo"))
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        if params.get("DefaultComplianceInfo") is not None:
            self._DefaultComplianceInfo = []
            for item in params.get("DefaultComplianceInfo"):
                obj = ScanTaskComplianceInfo()
                obj._deserialize(item)
                self._DefaultComplianceInfo.append(obj)
        if params.get("CustomComplianceInfo") is not None:
            self._CustomComplianceInfo = []
            for item in params.get("CustomComplianceInfo"):
                obj = ScanTaskComplianceInfo()
                obj._deserialize(item)
                self._CustomComplianceInfo.append(obj)
        self._TimingStartTime = params.get("TimingStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCOSDiscoveryTaskResult(AbstractModel):
    """COS扫描任务结果，按照数据库级别展示

    """

    def __init__(self):
        r"""
        :param _BucketResultId: 扫描bucket结果ID
        :type BucketResultId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ResultId: 扫描任务最新一次扫描结果ID
        :type ResultId: int
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _BucketName: 桶名称
        :type BucketName: str
        :param _TotalFiles: 总文件数
        :type TotalFiles: int
        :param _SensitiveDataNums: 被识别出的敏感数据数
        :type SensitiveDataNums: int
        :param _EndTime: Bucket扫描的结束时间，格式如：2006-01-02 15:04:05
        :type EndTime: str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _Status: Bucket扫描状态，0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :type Status: int
        :param _ErrorInfo: Bucket扫描结果错误信息
        :type ErrorInfo: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _OverSize: 是否超额
        :type OverSize: str
        """
        self._BucketResultId = None
        self._TaskId = None
        self._TaskName = None
        self._ResultId = None
        self._DataSourceId = None
        self._BucketName = None
        self._TotalFiles = None
        self._SensitiveDataNums = None
        self._EndTime = None
        self._DataSourceName = None
        self._Status = None
        self._ErrorInfo = None
        self._ResourceRegion = None
        self._OverSize = None

    @property
    def BucketResultId(self):
        """扫描bucket结果ID
        :rtype: int
        """
        return self._BucketResultId

    @BucketResultId.setter
    def BucketResultId(self, BucketResultId):
        self._BucketResultId = BucketResultId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ResultId(self):
        """扫描任务最新一次扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def BucketName(self):
        """桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def TotalFiles(self):
        """总文件数
        :rtype: int
        """
        return self._TotalFiles

    @TotalFiles.setter
    def TotalFiles(self, TotalFiles):
        self._TotalFiles = TotalFiles

    @property
    def SensitiveDataNums(self):
        """被识别出的敏感数据数
        :rtype: int
        """
        return self._SensitiveDataNums

    @SensitiveDataNums.setter
    def SensitiveDataNums(self, SensitiveDataNums):
        self._SensitiveDataNums = SensitiveDataNums

    @property
    def EndTime(self):
        """Bucket扫描的结束时间，格式如：2006-01-02 15:04:05
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def Status(self):
        """Bucket扫描状态，0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorInfo(self):
        """Bucket扫描结果错误信息
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def OverSize(self):
        """是否超额
        :rtype: str
        """
        return self._OverSize

    @OverSize.setter
    def OverSize(self, OverSize):
        self._OverSize = OverSize


    def _deserialize(self, params):
        self._BucketResultId = params.get("BucketResultId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._ResultId = params.get("ResultId")
        self._DataSourceId = params.get("DataSourceId")
        self._BucketName = params.get("BucketName")
        self._TotalFiles = params.get("TotalFiles")
        self._SensitiveDataNums = params.get("SensitiveDataNums")
        self._EndTime = params.get("EndTime")
        self._DataSourceName = params.get("DataSourceName")
        self._Status = params.get("Status")
        self._ErrorInfo = params.get("ErrorInfo")
        self._ResourceRegion = params.get("ResourceRegion")
        self._OverSize = params.get("OverSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaCloudResourceMeta(AbstractModel):
    """云上资源元数据

    """

    def __init__(self):
        r"""
        :param _ResourceId: 用户资源ID。
        :type ResourceId: str
        :param _ResourceName: 资源名称。
        :type ResourceName: str
        :param _ResourceVip: 资源VIP。
        :type ResourceVip: str
        :param _ResourceVPort: 资源端口。
        :type ResourceVPort: int
        :param _ResourceCreateTime: 资源被创建时间。
        :type ResourceCreateTime: str
        :param _ResourceUniqueVpcId: 用户资源VPC ID 字符串。
        :type ResourceUniqueVpcId: str
        :param _ResourceUniqueSubnetId: 用户资源Subnet ID 字符串。
        :type ResourceUniqueSubnetId: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._ResourceVip = None
        self._ResourceVPort = None
        self._ResourceCreateTime = None
        self._ResourceUniqueVpcId = None
        self._ResourceUniqueSubnetId = None

    @property
    def ResourceId(self):
        """用户资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceVip(self):
        """资源VIP。
        :rtype: str
        """
        return self._ResourceVip

    @ResourceVip.setter
    def ResourceVip(self, ResourceVip):
        self._ResourceVip = ResourceVip

    @property
    def ResourceVPort(self):
        """资源端口。
        :rtype: int
        """
        return self._ResourceVPort

    @ResourceVPort.setter
    def ResourceVPort(self, ResourceVPort):
        self._ResourceVPort = ResourceVPort

    @property
    def ResourceCreateTime(self):
        """资源被创建时间。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def ResourceUniqueVpcId(self):
        """用户资源VPC ID 字符串。
        :rtype: str
        """
        return self._ResourceUniqueVpcId

    @ResourceUniqueVpcId.setter
    def ResourceUniqueVpcId(self, ResourceUniqueVpcId):
        self._ResourceUniqueVpcId = ResourceUniqueVpcId

    @property
    def ResourceUniqueSubnetId(self):
        """用户资源Subnet ID 字符串。
        :rtype: str
        """
        return self._ResourceUniqueSubnetId

    @ResourceUniqueSubnetId.setter
    def ResourceUniqueSubnetId(self, ResourceUniqueSubnetId):
        self._ResourceUniqueSubnetId = ResourceUniqueSubnetId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ResourceVip = params.get("ResourceVip")
        self._ResourceVPort = params.get("ResourceVPort")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        self._ResourceUniqueVpcId = params.get("ResourceUniqueVpcId")
        self._ResourceUniqueSubnetId = params.get("ResourceUniqueSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDataCategoryDistributed(AbstractModel):
    """DSPA数据分类分布

    """

    def __init__(self):
        r"""
        :param _CategoryId: 数据分类ID
        :type CategoryId: int
        :param _CategoryName: 数据分类名称
        :type CategoryName: str
        :param _Count: 数据分类统计个数
        :type Count: int
        :param _CategoryFullPath: 分类路径
        :type CategoryFullPath: str
        """
        self._CategoryId = None
        self._CategoryName = None
        self._Count = None
        self._CategoryFullPath = None

    @property
    def CategoryId(self):
        """数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        """数据分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def Count(self):
        """数据分类统计个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CategoryFullPath(self):
        """分类路径
        :rtype: str
        """
        return self._CategoryFullPath

    @CategoryFullPath.setter
    def CategoryFullPath(self, CategoryFullPath):
        self._CategoryFullPath = CategoryFullPath


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._Count = params.get("Count")
        self._CategoryFullPath = params.get("CategoryFullPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDataSourceMngFilter(AbstractModel):
    """过滤内容

    """

    def __init__(self):
        r"""
        :param _Name: 过滤类型。
        :type Name: str
        :param _Values: 过滤类型的值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤类型。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """过滤类型的值。
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
        


class DspaDiscoveryCOSDataRule(AbstractModel):
    """COS敏感数据识别规则

    """

    def __init__(self):
        r"""
        :param _Operator: 只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一.
默认值为or
        :type Operator: str
        :param _Contents: 规则内容
        :type Contents: list of DspaDiscoveryDataContent
        """
        self._Operator = None
        self._Contents = None

    @property
    def Operator(self):
        """只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一.
默认值为or
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Contents(self):
        """规则内容
        :rtype: list of DspaDiscoveryDataContent
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = DspaDiscoveryDataContent()
                obj._deserialize(item)
                self._Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryCOSRules(AbstractModel):
    """分类分级任务COS识别规则

    """

    def __init__(self):
        r"""
        :param _Status: 规则状态；0 不启用, 1 启用
        :type Status: int
        :param _RegexRule: regex规则内容
        :type RegexRule: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        :param _KeywordRule: 关键词规则内容组，最大支持5个关键词。
        :type KeywordRule: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        :param _IgnoreStringRule: 忽略词规则内容组，最大支持5个忽略词。
        :type IgnoreStringRule: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        :param _MaxMatch: 最大匹配距离，默认值为100。上限为500.
        :type MaxMatch: int
        """
        self._Status = None
        self._RegexRule = None
        self._KeywordRule = None
        self._IgnoreStringRule = None
        self._MaxMatch = None

    @property
    def Status(self):
        """规则状态；0 不启用, 1 启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegexRule(self):
        """regex规则内容
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        """
        return self._RegexRule

    @RegexRule.setter
    def RegexRule(self, RegexRule):
        self._RegexRule = RegexRule

    @property
    def KeywordRule(self):
        """关键词规则内容组，最大支持5个关键词。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        """
        return self._KeywordRule

    @KeywordRule.setter
    def KeywordRule(self, KeywordRule):
        self._KeywordRule = KeywordRule

    @property
    def IgnoreStringRule(self):
        """忽略词规则内容组，最大支持5个忽略词。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSDataRule`
        """
        return self._IgnoreStringRule

    @IgnoreStringRule.setter
    def IgnoreStringRule(self, IgnoreStringRule):
        self._IgnoreStringRule = IgnoreStringRule

    @property
    def MaxMatch(self):
        """最大匹配距离，默认值为100。上限为500.
        :rtype: int
        """
        return self._MaxMatch

    @MaxMatch.setter
    def MaxMatch(self, MaxMatch):
        self._MaxMatch = MaxMatch


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("RegexRule") is not None:
            self._RegexRule = DspaDiscoveryCOSDataRule()
            self._RegexRule._deserialize(params.get("RegexRule"))
        if params.get("KeywordRule") is not None:
            self._KeywordRule = DspaDiscoveryCOSDataRule()
            self._KeywordRule._deserialize(params.get("KeywordRule"))
        if params.get("IgnoreStringRule") is not None:
            self._IgnoreStringRule = DspaDiscoveryCOSDataRule()
            self._IgnoreStringRule._deserialize(params.get("IgnoreStringRule"))
        self._MaxMatch = params.get("MaxMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryCOSTaskResultDetail(AbstractModel):
    """COS扫描任务结果详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _FileResultId: 扫描File结果详情ID
        :type FileResultId: int
        :param _BucketName: 所属桶名
        :type BucketName: str
        :param _FileName: 所属文件名
        :type FileName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _CategoryName: 敏感数据分类名称
        :type CategoryName: str
        :param _LevelId: 敏感数据分级ID
        :type LevelId: int
        :param _LevelName: 敏感数据分级名称
        :type LevelName: str
        :param _KMSEncrypted: KMS加密，true or false
        :type KMSEncrypted: bool
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _LevelRiskScore: 敏感数据分级分数
        :type LevelRiskScore: int
        :param _FileSize: 文件大小，单位为KB
        :type FileSize: int
        :param _FileType: 文件类型，如csv，txt
        :type FileType: str
        :param _SensitiveDataCount: 敏感数据出现次数
        :type SensitiveDataCount: int
        :param _CategoryFullPath: 分类树路径
        :type CategoryFullPath: list of str
        :param _CategoryArr: 分类树路径
        :type CategoryArr: list of str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _ResultId: 结果id
        :type ResultId: int
        """
        self._TaskId = None
        self._FileResultId = None
        self._BucketName = None
        self._FileName = None
        self._CategoryId = None
        self._CategoryName = None
        self._LevelId = None
        self._LevelName = None
        self._KMSEncrypted = None
        self._RuleName = None
        self._RuleId = None
        self._LevelRiskScore = None
        self._FileSize = None
        self._FileType = None
        self._SensitiveDataCount = None
        self._CategoryFullPath = None
        self._CategoryArr = None
        self._ComplianceId = None
        self._ResultId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileResultId(self):
        """扫描File结果详情ID
        :rtype: int
        """
        return self._FileResultId

    @FileResultId.setter
    def FileResultId(self, FileResultId):
        self._FileResultId = FileResultId

    @property
    def BucketName(self):
        """所属桶名
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def FileName(self):
        """所属文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        """敏感数据分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def LevelId(self):
        """敏感数据分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """敏感数据分级名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def KMSEncrypted(self):
        """KMS加密，true or false
        :rtype: bool
        """
        return self._KMSEncrypted

    @KMSEncrypted.setter
    def KMSEncrypted(self, KMSEncrypted):
        self._KMSEncrypted = KMSEncrypted

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def LevelRiskScore(self):
        """敏感数据分级分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore

    @property
    def FileSize(self):
        """文件大小，单位为KB
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileType(self):
        """文件类型，如csv，txt
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SensitiveDataCount(self):
        """敏感数据出现次数
        :rtype: int
        """
        return self._SensitiveDataCount

    @SensitiveDataCount.setter
    def SensitiveDataCount(self, SensitiveDataCount):
        self._SensitiveDataCount = SensitiveDataCount

    @property
    def CategoryFullPath(self):
        """分类树路径
        :rtype: list of str
        """
        return self._CategoryFullPath

    @CategoryFullPath.setter
    def CategoryFullPath(self, CategoryFullPath):
        self._CategoryFullPath = CategoryFullPath

    @property
    def CategoryArr(self):
        """分类树路径
        :rtype: list of str
        """
        return self._CategoryArr

    @CategoryArr.setter
    def CategoryArr(self, CategoryArr):
        self._CategoryArr = CategoryArr

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def ResultId(self):
        """结果id
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FileResultId = params.get("FileResultId")
        self._BucketName = params.get("BucketName")
        self._FileName = params.get("FileName")
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        self._KMSEncrypted = params.get("KMSEncrypted")
        self._RuleName = params.get("RuleName")
        self._RuleId = params.get("RuleId")
        self._LevelRiskScore = params.get("LevelRiskScore")
        self._FileSize = params.get("FileSize")
        self._FileType = params.get("FileType")
        self._SensitiveDataCount = params.get("SensitiveDataCount")
        self._CategoryFullPath = params.get("CategoryFullPath")
        self._CategoryArr = params.get("CategoryArr")
        self._ComplianceId = params.get("ComplianceId")
        self._ResultId = params.get("ResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryComplianceGroup(AbstractModel):
    """合规组

    """

    def __init__(self):
        r"""
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _Name: 合规组名称
        :type Name: str
        :param _Description: 合规组描述信息
        :type Description: str
        :param _ComplianceGroupType: 合规组类型；0 默认合规组，1 系统合规组（除默认合规组外）, 2 自定义合规组
        :type ComplianceGroupType: int
        :param _ComplianceGroupRules: 合规组对应的规则项
        :type ComplianceGroupRules: list of DspaDiscoveryComplianceGroupRuleInfo
        :param _LevelGroupId: 合规组对应的分级组ID
        :type LevelGroupId: int
        """
        self._ComplianceGroupId = None
        self._Name = None
        self._Description = None
        self._ComplianceGroupType = None
        self._ComplianceGroupRules = None
        self._LevelGroupId = None

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def Name(self):
        """合规组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """合规组描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ComplianceGroupType(self):
        """合规组类型；0 默认合规组，1 系统合规组（除默认合规组外）, 2 自定义合规组
        :rtype: int
        """
        return self._ComplianceGroupType

    @ComplianceGroupType.setter
    def ComplianceGroupType(self, ComplianceGroupType):
        self._ComplianceGroupType = ComplianceGroupType

    @property
    def ComplianceGroupRules(self):
        """合规组对应的规则项
        :rtype: list of DspaDiscoveryComplianceGroupRuleInfo
        """
        return self._ComplianceGroupRules

    @ComplianceGroupRules.setter
    def ComplianceGroupRules(self, ComplianceGroupRules):
        self._ComplianceGroupRules = ComplianceGroupRules

    @property
    def LevelGroupId(self):
        """合规组对应的分级组ID
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId


    def _deserialize(self, params):
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ComplianceGroupType = params.get("ComplianceGroupType")
        if params.get("ComplianceGroupRules") is not None:
            self._ComplianceGroupRules = []
            for item in params.get("ComplianceGroupRules"):
                obj = DspaDiscoveryComplianceGroupRuleInfo()
                obj._deserialize(item)
                self._ComplianceGroupRules.append(obj)
        self._LevelGroupId = params.get("LevelGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryComplianceGroupInfo(AbstractModel):
    """合规组信息

    """

    def __init__(self):
        r"""
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _Name: 合规组名称
        :type Name: str
        :param _Description: 合规组描述信息
        :type Description: str
        :param _ComplianceGroupType: 合规组类型；0 默认合规组，1 系统合规组（除默认合规组外）, 2 自定义合规组
        :type ComplianceGroupType: int
        :param _ComplianceGroupRules: 合规组对应的规则项
        :type ComplianceGroupRules: list of DspaDiscoveryComplianceGroupRule
        :param _LevelGroupId: 合规组对应的分级组ID
        :type LevelGroupId: int
        :param _Disabled: 是否禁止使用（true，禁止使用，false，可以使用）
        :type Disabled: bool
        :param _IsAlias: 是否别名
        :type IsAlias: bool
        :param _Status: 1代表模版开启，0代表模版关闭
        :type Status: int
        :param _ModifyTime: 模版最后修改时间
        :type ModifyTime: str
        """
        self._ComplianceGroupId = None
        self._Name = None
        self._Description = None
        self._ComplianceGroupType = None
        self._ComplianceGroupRules = None
        self._LevelGroupId = None
        self._Disabled = None
        self._IsAlias = None
        self._Status = None
        self._ModifyTime = None

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def Name(self):
        """合规组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """合规组描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ComplianceGroupType(self):
        """合规组类型；0 默认合规组，1 系统合规组（除默认合规组外）, 2 自定义合规组
        :rtype: int
        """
        return self._ComplianceGroupType

    @ComplianceGroupType.setter
    def ComplianceGroupType(self, ComplianceGroupType):
        self._ComplianceGroupType = ComplianceGroupType

    @property
    def ComplianceGroupRules(self):
        """合规组对应的规则项
        :rtype: list of DspaDiscoveryComplianceGroupRule
        """
        return self._ComplianceGroupRules

    @ComplianceGroupRules.setter
    def ComplianceGroupRules(self, ComplianceGroupRules):
        self._ComplianceGroupRules = ComplianceGroupRules

    @property
    def LevelGroupId(self):
        """合规组对应的分级组ID
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

    @property
    def Disabled(self):
        """是否禁止使用（true，禁止使用，false，可以使用）
        :rtype: bool
        """
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def IsAlias(self):
        """是否别名
        :rtype: bool
        """
        return self._IsAlias

    @IsAlias.setter
    def IsAlias(self, IsAlias):
        self._IsAlias = IsAlias

    @property
    def Status(self):
        """1代表模版开启，0代表模版关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        """模版最后修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ComplianceGroupType = params.get("ComplianceGroupType")
        if params.get("ComplianceGroupRules") is not None:
            self._ComplianceGroupRules = []
            for item in params.get("ComplianceGroupRules"):
                obj = DspaDiscoveryComplianceGroupRule()
                obj._deserialize(item)
                self._ComplianceGroupRules.append(obj)
        self._LevelGroupId = params.get("LevelGroupId")
        self._Disabled = params.get("Disabled")
        self._IsAlias = params.get("IsAlias")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryComplianceGroupRule(AbstractModel):
    """合规组中规则信息，用于合规组列表中规则信息展示

    """

    def __init__(self):
        r"""
        :param _RuleId: 敏感数据识别规则ID
        :type RuleId: int
        :param _RuleName: 敏感数据识别规则名称
        :type RuleName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _LevelId: 敏感数据分级ID, 目前只支持高、中、低三级
        :type LevelId: int
        :param _CategoryName: 合规组对应的分类信息
        :type CategoryName: str
        :param _LevelRiskName: 分级名称
        :type LevelRiskName: str
        """
        self._RuleId = None
        self._RuleName = None
        self._CategoryId = None
        self._LevelId = None
        self._CategoryName = None
        self._LevelRiskName = None

    @property
    def RuleId(self):
        """敏感数据识别规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """敏感数据识别规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """敏感数据分级ID, 目前只支持高、中、低三级
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def CategoryName(self):
        """合规组对应的分类信息
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def LevelRiskName(self):
        """分级名称
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        self._CategoryName = params.get("CategoryName")
        self._LevelRiskName = params.get("LevelRiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryComplianceGroupRuleInfo(AbstractModel):
    """合规组中规则信息，用于合规组列表中规则信息展示

    """

    def __init__(self):
        r"""
        :param _RuleId: 敏感数据识别规则ID
        :type RuleId: int
        :param _RuleName: 敏感数据识别规则名称
        :type RuleName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _LevelId: 敏感数据分级ID, 目前只支持高、中、低三级
        :type LevelId: int
        """
        self._RuleId = None
        self._RuleName = None
        self._CategoryId = None
        self._LevelId = None

    @property
    def RuleId(self):
        """敏感数据识别规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """敏感数据识别规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def LevelId(self):
        """敏感数据分级ID, 目前只支持高、中、低三级
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CategoryId = params.get("CategoryId")
        self._LevelId = params.get("LevelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryDataContent(AbstractModel):
    """扫描规则内容

    """

    def __init__(self):
        r"""
        :param _RuleContent: 规则内容，可以是正则规则，关键词，
忽略词扥
        :type RuleContent: str
        :param _IsIgnoreCase: 是否区分大小写
false: 不区分大小写
true:区分大小写
        :type IsIgnoreCase: bool
        """
        self._RuleContent = None
        self._IsIgnoreCase = None

    @property
    def RuleContent(self):
        """规则内容，可以是正则规则，关键词，
忽略词扥
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def IsIgnoreCase(self):
        """是否区分大小写
false: 不区分大小写
true:区分大小写
        :rtype: bool
        """
        return self._IsIgnoreCase

    @IsIgnoreCase.setter
    def IsIgnoreCase(self, IsIgnoreCase):
        self._IsIgnoreCase = IsIgnoreCase


    def _deserialize(self, params):
        self._RuleContent = params.get("RuleContent")
        self._IsIgnoreCase = params.get("IsIgnoreCase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryDataRule(AbstractModel):
    """敏感数据识别规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型；取值：
keyword 关键字, 
regex 正则
        :type RuleType: str
        :param _RuleContent: 内容
        :type RuleContent: str
        :param _ExtendParameters: 该字段是针对规则类型RuleType为keyword类型时的一个扩展属性
        :type ExtendParameters: list of DatagovRuleExtendParameter
        """
        self._RuleType = None
        self._RuleContent = None
        self._ExtendParameters = None

    @property
    def RuleType(self):
        """规则类型；取值：
keyword 关键字, 
regex 正则
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleContent(self):
        """内容
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def ExtendParameters(self):
        """该字段是针对规则类型RuleType为keyword类型时的一个扩展属性
        :rtype: list of DatagovRuleExtendParameter
        """
        return self._ExtendParameters

    @ExtendParameters.setter
    def ExtendParameters(self, ExtendParameters):
        self._ExtendParameters = ExtendParameters


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleContent = params.get("RuleContent")
        if params.get("ExtendParameters") is not None:
            self._ExtendParameters = []
            for item in params.get("ExtendParameters"):
                obj = DatagovRuleExtendParameter()
                obj._deserialize(item)
                self._ExtendParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryDataRules(AbstractModel):
    """敏感数据识别规则集

    """

    def __init__(self):
        r"""
        :param _Operator: 操作符；只能取and, or的其中一种
        :type Operator: str
        :param _Contents: 规则
        :type Contents: list of DspaDiscoveryDataRule
        """
        self._Operator = None
        self._Contents = None

    @property
    def Operator(self):
        """操作符；只能取and, or的其中一种
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Contents(self):
        """规则
        :rtype: list of DspaDiscoveryDataRule
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = DspaDiscoveryDataRule()
                obj._deserialize(item)
                self._Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryLevelDetail(AbstractModel):
    """敏感数据分级信息

    """

    def __init__(self):
        r"""
        :param _LevelGroupName: 分级组名称，唯一性约束，最多60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type LevelGroupName: str
        :param _Source: 分级组来源，0为内置，1为自定义
        :type Source: int
        :param _LevelGroupDesc: 分级组描述，最多1024字符
        :type LevelGroupDesc: str
        :param _LevelDetail: 具体分级标识详情
        :type LevelDetail: list of LevelItem
        :param _RefComplianceCnt: 引用合规组次数
        :type RefComplianceCnt: int
        :param _RefCompliance: 引用合规组
        :type RefCompliance: list of DspaDiscoveryComplianceGroup
        :param _LevelGroupId: 分级组ID
        :type LevelGroupId: int
        """
        self._LevelGroupName = None
        self._Source = None
        self._LevelGroupDesc = None
        self._LevelDetail = None
        self._RefComplianceCnt = None
        self._RefCompliance = None
        self._LevelGroupId = None

    @property
    def LevelGroupName(self):
        """分级组名称，唯一性约束，最多60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._LevelGroupName

    @LevelGroupName.setter
    def LevelGroupName(self, LevelGroupName):
        self._LevelGroupName = LevelGroupName

    @property
    def Source(self):
        """分级组来源，0为内置，1为自定义
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def LevelGroupDesc(self):
        """分级组描述，最多1024字符
        :rtype: str
        """
        return self._LevelGroupDesc

    @LevelGroupDesc.setter
    def LevelGroupDesc(self, LevelGroupDesc):
        self._LevelGroupDesc = LevelGroupDesc

    @property
    def LevelDetail(self):
        """具体分级标识详情
        :rtype: list of LevelItem
        """
        return self._LevelDetail

    @LevelDetail.setter
    def LevelDetail(self, LevelDetail):
        self._LevelDetail = LevelDetail

    @property
    def RefComplianceCnt(self):
        """引用合规组次数
        :rtype: int
        """
        return self._RefComplianceCnt

    @RefComplianceCnt.setter
    def RefComplianceCnt(self, RefComplianceCnt):
        self._RefComplianceCnt = RefComplianceCnt

    @property
    def RefCompliance(self):
        """引用合规组
        :rtype: list of DspaDiscoveryComplianceGroup
        """
        return self._RefCompliance

    @RefCompliance.setter
    def RefCompliance(self, RefCompliance):
        self._RefCompliance = RefCompliance

    @property
    def LevelGroupId(self):
        """分级组ID
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId


    def _deserialize(self, params):
        self._LevelGroupName = params.get("LevelGroupName")
        self._Source = params.get("Source")
        self._LevelGroupDesc = params.get("LevelGroupDesc")
        if params.get("LevelDetail") is not None:
            self._LevelDetail = []
            for item in params.get("LevelDetail"):
                obj = LevelItem()
                obj._deserialize(item)
                self._LevelDetail.append(obj)
        self._RefComplianceCnt = params.get("RefComplianceCnt")
        if params.get("RefCompliance") is not None:
            self._RefCompliance = []
            for item in params.get("RefCompliance"):
                obj = DspaDiscoveryComplianceGroup()
                obj._deserialize(item)
                self._RefCompliance.append(obj)
        self._LevelGroupId = params.get("LevelGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryRDBRules(AbstractModel):
    """分类分级任务RDB数据规则

    """

    def __init__(self):
        r"""
        :param _Status: 规则状态；0 不启用, 1 启用
        :type Status: int
        :param _MatchOperator: 只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :type MatchOperator: str
        :param _MetaRule: 字段名包含规则，最大支持选择9项
        :type MetaRule: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryDataRules`
        :param _ContentRule: 内容包含规则，最大支持选择9项
        :type ContentRule: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryDataRules`
        """
        self._Status = None
        self._MatchOperator = None
        self._MetaRule = None
        self._ContentRule = None

    @property
    def Status(self):
        """规则状态；0 不启用, 1 启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MatchOperator(self):
        """只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :rtype: str
        """
        return self._MatchOperator

    @MatchOperator.setter
    def MatchOperator(self, MatchOperator):
        self._MatchOperator = MatchOperator

    @property
    def MetaRule(self):
        """字段名包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryDataRules`
        """
        return self._MetaRule

    @MetaRule.setter
    def MetaRule(self, MetaRule):
        self._MetaRule = MetaRule

    @property
    def ContentRule(self):
        """内容包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryDataRules`
        """
        return self._ContentRule

    @ContentRule.setter
    def ContentRule(self, ContentRule):
        self._ContentRule = ContentRule


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MatchOperator = params.get("MatchOperator")
        if params.get("MetaRule") is not None:
            self._MetaRule = DspaDiscoveryDataRules()
            self._MetaRule._deserialize(params.get("MetaRule"))
        if params.get("ContentRule") is not None:
            self._ContentRule = DspaDiscoveryDataRules()
            self._ContentRule._deserialize(params.get("ContentRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryRuleDetail(AbstractModel):
    """敏感数据扫描任务识别规则详情

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Name: 规则名称
        :type Name: str
        :param _Description: 规则描述
        :type Description: str
        :param _Source: 规则来源，取值：0 内置, 1 自定义
        :type Source: int
        :param _RDBRules: RDB规则详情
        :type RDBRules: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryRDBRules`
        :param _COSRules: COS规则详情
        :type COSRules: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSRules`
        :param _Status: 0关闭，1开启
        :type Status: int
        """
        self._RuleId = None
        self._Name = None
        self._Description = None
        self._Source = None
        self._RDBRules = None
        self._COSRules = None
        self._Status = None

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        """规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        """规则来源，取值：0 内置, 1 自定义
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def RDBRules(self):
        """RDB规则详情
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryRDBRules`
        """
        return self._RDBRules

    @RDBRules.setter
    def RDBRules(self, RDBRules):
        self._RDBRules = RDBRules

    @property
    def COSRules(self):
        """COS规则详情
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryCOSRules`
        """
        return self._COSRules

    @COSRules.setter
    def COSRules(self, COSRules):
        self._COSRules = COSRules

    @property
    def Status(self):
        """0关闭，1开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        if params.get("RDBRules") is not None:
            self._RDBRules = DspaDiscoveryRDBRules()
            self._RDBRules._deserialize(params.get("RDBRules"))
        if params.get("COSRules") is not None:
            self._COSRules = DspaDiscoveryCOSRules()
            self._COSRules._deserialize(params.get("COSRules"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTask(AbstractModel):
    """分类分级任务相关信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Name: 任务名称
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _Period: 执行周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _Plan: 执行计划，0立即 1定时
        :type Plan: int
        :param _Enable: 任务开关；1 打开，0 关闭
        :type Enable: int
        :param _DataSourceInfo: 元数据对象信息
        :type DataSourceInfo: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDataSource`
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _Result: 任务最新的一次执行结果信息，该字段用于查询任务列表接口
        :type Result: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskResult`
        :param _TimingStartTime: 定时开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimingStartTime: str
        :param _ComplianceUpdate: 关联模板是否更新
        :type ComplianceUpdate: bool
        """
        self._TaskId = None
        self._Name = None
        self._Description = None
        self._Period = None
        self._Plan = None
        self._Enable = None
        self._DataSourceInfo = None
        self._GeneralRuleSetEnable = None
        self._Result = None
        self._TimingStartTime = None
        self._ComplianceUpdate = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Period(self):
        """执行周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Plan(self):
        """执行计划，0立即 1定时
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Enable(self):
        """任务开关；1 打开，0 关闭
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DataSourceInfo(self):
        """元数据对象信息
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDataSource`
        """
        return self._DataSourceInfo

    @DataSourceInfo.setter
    def DataSourceInfo(self, DataSourceInfo):
        self._DataSourceInfo = DataSourceInfo

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def Result(self):
        """任务最新的一次执行结果信息，该字段用于查询任务列表接口
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TimingStartTime(self):
        """定时开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def ComplianceUpdate(self):
        """关联模板是否更新
        :rtype: bool
        """
        return self._ComplianceUpdate

    @ComplianceUpdate.setter
    def ComplianceUpdate(self, ComplianceUpdate):
        self._ComplianceUpdate = ComplianceUpdate


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Period = params.get("Period")
        self._Plan = params.get("Plan")
        self._Enable = params.get("Enable")
        if params.get("DataSourceInfo") is not None:
            self._DataSourceInfo = DspaDiscoveryTaskDataSource()
            self._DataSourceInfo._deserialize(params.get("DataSourceInfo"))
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        if params.get("Result") is not None:
            self._Result = ScanTaskResult()
            self._Result._deserialize(params.get("Result"))
        self._TimingStartTime = params.get("TimingStartTime")
        self._ComplianceUpdate = params.get("ComplianceUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTaskCOSCondition(AbstractModel):
    """描述对象存储类敏感识别扫描人元数据条件。

    """

    def __init__(self):
        r"""
        :param _Bucket: 数据桶名称
        :type Bucket: str
        :param _FileTypes: 文件类型
        :type FileTypes: list of str
        :param _FileSizeLimit: 文件大小上限，单位为KB，如1000, 目前单个文件最大只支持1GB（1048576KB）
        :type FileSizeLimit: int
        """
        self._Bucket = None
        self._FileTypes = None
        self._FileSizeLimit = None

    @property
    def Bucket(self):
        """数据桶名称
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def FileTypes(self):
        """文件类型
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def FileSizeLimit(self):
        """文件大小上限，单位为KB，如1000, 目前单个文件最大只支持1GB（1048576KB）
        :rtype: int
        """
        return self._FileSizeLimit

    @FileSizeLimit.setter
    def FileSizeLimit(self, FileSizeLimit):
        self._FileSizeLimit = FileSizeLimit


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._FileTypes = params.get("FileTypes")
        self._FileSizeLimit = params.get("FileSizeLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTaskDataSource(AbstractModel):
    """扫描任务数据源信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _Condition: 用于传入的数据源的条件，可以选择多个数据库，数据库之间通过逗号分隔，如果为空，默认是全部数据库
        :type Condition: str
        :param _ProxyAddress: 代理地址
        :type ProxyAddress: list of str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        """
        self._DataSourceId = None
        self._Condition = None
        self._ProxyAddress = None
        self._DataSourceName = None
        self._ResourceRegion = None
        self._DataSourceType = None

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def Condition(self):
        """用于传入的数据源的条件，可以选择多个数据库，数据库之间通过逗号分隔，如果为空，默认是全部数据库
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ProxyAddress(self):
        """代理地址
        :rtype: list of str
        """
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._Condition = params.get("Condition")
        self._ProxyAddress = params.get("ProxyAddress")
        self._DataSourceName = params.get("DataSourceName")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTaskDbResult(AbstractModel):
    """扫描任务结果，按照数据库级别展示

    """

    def __init__(self):
        r"""
        :param _DbResultId: 扫描数据库结果ID
        :type DbResultId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ResultId: 扫描任务最新一次扫描结果ID
        :type ResultId: int
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _TotalTables: 总表数
        :type TotalTables: int
        :param _SensitiveTables: 敏感表数
        :type SensitiveTables: int
        :param _EndTime: DB扫描的结束时间，格式如：2006-01-02 15:04:05
        :type EndTime: str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _Status: DB扫描状态，0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :type Status: int
        :param _ErrorInfo: DB扫描结果错误信息
        :type ErrorInfo: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _SensitiveField: 敏感字段数
        :type SensitiveField: int
        :param _TotalField: 总的字段数
        :type TotalField: int
        """
        self._DbResultId = None
        self._TaskId = None
        self._TaskName = None
        self._ResultId = None
        self._DataSourceId = None
        self._DbName = None
        self._TotalTables = None
        self._SensitiveTables = None
        self._EndTime = None
        self._DataSourceName = None
        self._Status = None
        self._ErrorInfo = None
        self._ResourceRegion = None
        self._SensitiveField = None
        self._TotalField = None

    @property
    def DbResultId(self):
        """扫描数据库结果ID
        :rtype: int
        """
        return self._DbResultId

    @DbResultId.setter
    def DbResultId(self, DbResultId):
        self._DbResultId = DbResultId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ResultId(self):
        """扫描任务最新一次扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TotalTables(self):
        """总表数
        :rtype: int
        """
        return self._TotalTables

    @TotalTables.setter
    def TotalTables(self, TotalTables):
        self._TotalTables = TotalTables

    @property
    def SensitiveTables(self):
        """敏感表数
        :rtype: int
        """
        return self._SensitiveTables

    @SensitiveTables.setter
    def SensitiveTables(self, SensitiveTables):
        self._SensitiveTables = SensitiveTables

    @property
    def EndTime(self):
        """DB扫描的结束时间，格式如：2006-01-02 15:04:05
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def Status(self):
        """DB扫描状态，0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorInfo(self):
        """DB扫描结果错误信息
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def SensitiveField(self):
        """敏感字段数
        :rtype: int
        """
        return self._SensitiveField

    @SensitiveField.setter
    def SensitiveField(self, SensitiveField):
        self._SensitiveField = SensitiveField

    @property
    def TotalField(self):
        """总的字段数
        :rtype: int
        """
        return self._TotalField

    @TotalField.setter
    def TotalField(self, TotalField):
        self._TotalField = TotalField


    def _deserialize(self, params):
        self._DbResultId = params.get("DbResultId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._ResultId = params.get("ResultId")
        self._DataSourceId = params.get("DataSourceId")
        self._DbName = params.get("DbName")
        self._TotalTables = params.get("TotalTables")
        self._SensitiveTables = params.get("SensitiveTables")
        self._EndTime = params.get("EndTime")
        self._DataSourceName = params.get("DataSourceName")
        self._Status = params.get("Status")
        self._ErrorInfo = params.get("ErrorInfo")
        self._ResourceRegion = params.get("ResourceRegion")
        self._SensitiveField = params.get("SensitiveField")
        self._TotalField = params.get("TotalField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTaskDetail(AbstractModel):
    """敏感数据扫描任务相关信息

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _Description: 任务描述
        :type Description: str
        :param _Period: 执行周期，0单次 1每天 2每周 3每月
        :type Period: int
        :param _Plan: 执行计划，0立即 1定时
        :type Plan: int
        :param _Enable: 任务开关；1 打开，0 关闭
        :type Enable: int
        :param _DataSourceInfo: 元数据对象信息
        :type DataSourceInfo: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDataSource`
        :param _GeneralRuleSetEnable: 通用规则集开关，0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _DefaultComplianceInfo: 当创建任务时，用户打开了通用规则集开关，则该字段就会保存默认合规组信息
        :type DefaultComplianceInfo: list of ScanTaskComplianceInfo
        :param _CustomComplianceInfo: 该任务中用户选择的合规组信息列表
        :type CustomComplianceInfo: list of ScanTaskComplianceInfo
        :param _TimingStartTime: 定时开始时间
        :type TimingStartTime: str
        """
        self._Name = None
        self._Description = None
        self._Period = None
        self._Plan = None
        self._Enable = None
        self._DataSourceInfo = None
        self._GeneralRuleSetEnable = None
        self._DefaultComplianceInfo = None
        self._CustomComplianceInfo = None
        self._TimingStartTime = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Period(self):
        """执行周期，0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Plan(self):
        """执行计划，0立即 1定时
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Enable(self):
        """任务开关；1 打开，0 关闭
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DataSourceInfo(self):
        """元数据对象信息
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaDiscoveryTaskDataSource`
        """
        return self._DataSourceInfo

    @DataSourceInfo.setter
    def DataSourceInfo(self, DataSourceInfo):
        self._DataSourceInfo = DataSourceInfo

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关，0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def DefaultComplianceInfo(self):
        """当创建任务时，用户打开了通用规则集开关，则该字段就会保存默认合规组信息
        :rtype: list of ScanTaskComplianceInfo
        """
        return self._DefaultComplianceInfo

    @DefaultComplianceInfo.setter
    def DefaultComplianceInfo(self, DefaultComplianceInfo):
        self._DefaultComplianceInfo = DefaultComplianceInfo

    @property
    def CustomComplianceInfo(self):
        """该任务中用户选择的合规组信息列表
        :rtype: list of ScanTaskComplianceInfo
        """
        return self._CustomComplianceInfo

    @CustomComplianceInfo.setter
    def CustomComplianceInfo(self, CustomComplianceInfo):
        self._CustomComplianceInfo = CustomComplianceInfo

    @property
    def TimingStartTime(self):
        """定时开始时间
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Period = params.get("Period")
        self._Plan = params.get("Plan")
        self._Enable = params.get("Enable")
        if params.get("DataSourceInfo") is not None:
            self._DataSourceInfo = DspaDiscoveryTaskDataSource()
            self._DataSourceInfo._deserialize(params.get("DataSourceInfo"))
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        if params.get("DefaultComplianceInfo") is not None:
            self._DefaultComplianceInfo = []
            for item in params.get("DefaultComplianceInfo"):
                obj = ScanTaskComplianceInfo()
                obj._deserialize(item)
                self._DefaultComplianceInfo.append(obj)
        if params.get("CustomComplianceInfo") is not None:
            self._CustomComplianceInfo = []
            for item in params.get("CustomComplianceInfo"):
                obj = ScanTaskComplianceInfo()
                obj._deserialize(item)
                self._CustomComplianceInfo.append(obj)
        self._TimingStartTime = params.get("TimingStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaDiscoveryTaskResultDetail(AbstractModel):
    """扫描任务结果详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _FieldResultId: 扫描结果详情ID
        :type FieldResultId: int
        :param _TableName: 所属数据表名
        :type TableName: str
        :param _FieldName: 字段名
        :type FieldName: str
        :param _CategoryId: 敏感数据分类ID
        :type CategoryId: int
        :param _CategoryName: 敏感数据分类名称
        :type CategoryName: str
        :param _LevelId: 敏感数据分级ID
        :type LevelId: int
        :param _LevelName: 敏感数据分级名称
        :type LevelName: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _LevelRiskScore: 敏感数据分级分数
        :type LevelRiskScore: int
        :param _SafeGuard: 保护措施
        :type SafeGuard: :class:`tencentcloud.dsgc.v20190723.models.DspaSafeGuard`
        :param _CategoryFullPath: 分类路径
        :type CategoryFullPath: str
        :param _SchemaName: 模式名
        :type SchemaName: str
        """
        self._TaskId = None
        self._FieldResultId = None
        self._TableName = None
        self._FieldName = None
        self._CategoryId = None
        self._CategoryName = None
        self._LevelId = None
        self._LevelName = None
        self._RuleName = None
        self._RuleId = None
        self._LevelRiskScore = None
        self._SafeGuard = None
        self._CategoryFullPath = None
        self._SchemaName = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FieldResultId(self):
        """扫描结果详情ID
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def TableName(self):
        """所属数据表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def FieldName(self):
        """字段名
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def CategoryId(self):
        """敏感数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        """敏感数据分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def LevelId(self):
        """敏感数据分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """敏感数据分级名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def LevelRiskScore(self):
        """敏感数据分级分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore

    @property
    def SafeGuard(self):
        """保护措施
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaSafeGuard`
        """
        return self._SafeGuard

    @SafeGuard.setter
    def SafeGuard(self, SafeGuard):
        self._SafeGuard = SafeGuard

    @property
    def CategoryFullPath(self):
        """分类路径
        :rtype: str
        """
        return self._CategoryFullPath

    @CategoryFullPath.setter
    def CategoryFullPath(self, CategoryFullPath):
        self._CategoryFullPath = CategoryFullPath

    @property
    def SchemaName(self):
        """模式名
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FieldResultId = params.get("FieldResultId")
        self._TableName = params.get("TableName")
        self._FieldName = params.get("FieldName")
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        self._RuleName = params.get("RuleName")
        self._RuleId = params.get("RuleId")
        self._LevelRiskScore = params.get("LevelRiskScore")
        if params.get("SafeGuard") is not None:
            self._SafeGuard = DspaSafeGuard()
            self._SafeGuard._deserialize(params.get("SafeGuard"))
        self._CategoryFullPath = params.get("CategoryFullPath")
        self._SchemaName = params.get("SchemaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaFieldResultDataSample(AbstractModel):
    """数据样本

    """

    def __init__(self):
        r"""
        :param _DataSample: 数据样本
        :type DataSample: str
        """
        self._DataSample = None

    @property
    def DataSample(self):
        """数据样本
        :rtype: str
        """
        return self._DataSample

    @DataSample.setter
    def DataSample(self, DataSample):
        self._DataSample = DataSample


    def _deserialize(self, params):
        self._DataSample = params.get("DataSample")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaInstance(AbstractModel):
    """Dspa实例信息

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _DspaName: DSPA实例名称。
        :type DspaName: str
        :param _DspaDescription: DSPA实例描述信息。
        :type DspaDescription: str
        :param _DBAuthCount: DSPA实例已授权的数据库实例数量。
        :type DBAuthCount: int
        :param _CosBindCount: DSPA实例已绑定的cos桶数量。
        :type CosBindCount: int
        :param _InstanceVersion: DSPA实例版本。
        :type InstanceVersion: str
        :param _Status: DSPA实例状态。
        :type Status: str
        :param _ExpiredAt: 实例过期时间戳。
        :type ExpiredAt: int
        :param _AppId: 账户APPID。
        :type AppId: int
        :param _TrialVersion: 体验版本信息。
        :type TrialVersion: str
        :param _TrialEndAt: 体验版本过期时间戳。
        :type TrialEndAt: int
        :param _DbTotalQuota: DB已购配额。
        :type DbTotalQuota: int
        :param _CosTotalQuota: COS已购配额。
        :type CosTotalQuota: int
        :param _CosQuotaUnit: COS配额单位，例如:TB。
        :type CosQuotaUnit: str
        :param _RenewFlag: 0: 默认状态(用户未设置)
1: 开启自动续费
2: 明确不自动续费
        :type RenewFlag: int
        :param _Channel: 实例渠道
        :type Channel: str
        :param _InsAuthCount: 已授权的实例数量
        :type InsAuthCount: int
        :param _InsTotalQuota: 已购买的实例数量
        :type InsTotalQuota: int
        """
        self._DspaId = None
        self._DspaName = None
        self._DspaDescription = None
        self._DBAuthCount = None
        self._CosBindCount = None
        self._InstanceVersion = None
        self._Status = None
        self._ExpiredAt = None
        self._AppId = None
        self._TrialVersion = None
        self._TrialEndAt = None
        self._DbTotalQuota = None
        self._CosTotalQuota = None
        self._CosQuotaUnit = None
        self._RenewFlag = None
        self._Channel = None
        self._InsAuthCount = None
        self._InsTotalQuota = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DspaName(self):
        """DSPA实例名称。
        :rtype: str
        """
        return self._DspaName

    @DspaName.setter
    def DspaName(self, DspaName):
        self._DspaName = DspaName

    @property
    def DspaDescription(self):
        """DSPA实例描述信息。
        :rtype: str
        """
        return self._DspaDescription

    @DspaDescription.setter
    def DspaDescription(self, DspaDescription):
        self._DspaDescription = DspaDescription

    @property
    def DBAuthCount(self):
        """DSPA实例已授权的数据库实例数量。
        :rtype: int
        """
        return self._DBAuthCount

    @DBAuthCount.setter
    def DBAuthCount(self, DBAuthCount):
        self._DBAuthCount = DBAuthCount

    @property
    def CosBindCount(self):
        """DSPA实例已绑定的cos桶数量。
        :rtype: int
        """
        return self._CosBindCount

    @CosBindCount.setter
    def CosBindCount(self, CosBindCount):
        self._CosBindCount = CosBindCount

    @property
    def InstanceVersion(self):
        """DSPA实例版本。
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        """DSPA实例状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredAt(self):
        """实例过期时间戳。
        :rtype: int
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def AppId(self):
        """账户APPID。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TrialVersion(self):
        """体验版本信息。
        :rtype: str
        """
        return self._TrialVersion

    @TrialVersion.setter
    def TrialVersion(self, TrialVersion):
        self._TrialVersion = TrialVersion

    @property
    def TrialEndAt(self):
        """体验版本过期时间戳。
        :rtype: int
        """
        return self._TrialEndAt

    @TrialEndAt.setter
    def TrialEndAt(self, TrialEndAt):
        self._TrialEndAt = TrialEndAt

    @property
    def DbTotalQuota(self):
        """DB已购配额。
        :rtype: int
        """
        return self._DbTotalQuota

    @DbTotalQuota.setter
    def DbTotalQuota(self, DbTotalQuota):
        self._DbTotalQuota = DbTotalQuota

    @property
    def CosTotalQuota(self):
        """COS已购配额。
        :rtype: int
        """
        return self._CosTotalQuota

    @CosTotalQuota.setter
    def CosTotalQuota(self, CosTotalQuota):
        self._CosTotalQuota = CosTotalQuota

    @property
    def CosQuotaUnit(self):
        """COS配额单位，例如:TB。
        :rtype: str
        """
        return self._CosQuotaUnit

    @CosQuotaUnit.setter
    def CosQuotaUnit(self, CosQuotaUnit):
        self._CosQuotaUnit = CosQuotaUnit

    @property
    def RenewFlag(self):
        """0: 默认状态(用户未设置)
1: 开启自动续费
2: 明确不自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Channel(self):
        """实例渠道
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def InsAuthCount(self):
        """已授权的实例数量
        :rtype: int
        """
        return self._InsAuthCount

    @InsAuthCount.setter
    def InsAuthCount(self, InsAuthCount):
        self._InsAuthCount = InsAuthCount

    @property
    def InsTotalQuota(self):
        """已购买的实例数量
        :rtype: int
        """
        return self._InsTotalQuota

    @InsTotalQuota.setter
    def InsTotalQuota(self, InsTotalQuota):
        self._InsTotalQuota = InsTotalQuota


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DspaName = params.get("DspaName")
        self._DspaDescription = params.get("DspaDescription")
        self._DBAuthCount = params.get("DBAuthCount")
        self._CosBindCount = params.get("CosBindCount")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._ExpiredAt = params.get("ExpiredAt")
        self._AppId = params.get("AppId")
        self._TrialVersion = params.get("TrialVersion")
        self._TrialEndAt = params.get("TrialEndAt")
        self._DbTotalQuota = params.get("DbTotalQuota")
        self._CosTotalQuota = params.get("CosTotalQuota")
        self._CosQuotaUnit = params.get("CosQuotaUnit")
        self._RenewFlag = params.get("RenewFlag")
        self._Channel = params.get("Channel")
        self._InsAuthCount = params.get("InsAuthCount")
        self._InsTotalQuota = params.get("InsTotalQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaRDBDataAssetCount(AbstractModel):
    """RDB关系型数据库敏感数据资产统计

    """

    def __init__(self):
        r"""
        :param _DataAssetType: 数组资产类型，0代表关系型数据库资产，1代表对象存储COS资产
        :type DataAssetType: int
        :param _TotalDbCnt: 已扫描的数据库的个数
        :type TotalDbCnt: int
        :param _TotalTableCnt: 数据库表的个数
        :type TotalTableCnt: int
        :param _SensitiveCategoryCnt: 敏感数据类型个数
        :type SensitiveCategoryCnt: int
        :param _SensitiveFieldCnt: 敏感字段的个数
        :type SensitiveFieldCnt: int
        :param _SensitiveLevel: 敏感等级分布
        :type SensitiveLevel: list of SensitiveLevel
        :param _SensitiveDbCnt: 敏感数据库的个数
        :type SensitiveDbCnt: int
        :param _SensitiveTableCnt: 敏感数据库表的个数
        :type SensitiveTableCnt: int
        :param _TotalFieldCnt: 扫描字段的个数
        :type TotalFieldCnt: int
        :param _CategoryDistributed: 数据分类分布
        :type CategoryDistributed: list of DspaDataCategoryDistributed
        """
        self._DataAssetType = None
        self._TotalDbCnt = None
        self._TotalTableCnt = None
        self._SensitiveCategoryCnt = None
        self._SensitiveFieldCnt = None
        self._SensitiveLevel = None
        self._SensitiveDbCnt = None
        self._SensitiveTableCnt = None
        self._TotalFieldCnt = None
        self._CategoryDistributed = None

    @property
    def DataAssetType(self):
        """数组资产类型，0代表关系型数据库资产，1代表对象存储COS资产
        :rtype: int
        """
        return self._DataAssetType

    @DataAssetType.setter
    def DataAssetType(self, DataAssetType):
        self._DataAssetType = DataAssetType

    @property
    def TotalDbCnt(self):
        """已扫描的数据库的个数
        :rtype: int
        """
        return self._TotalDbCnt

    @TotalDbCnt.setter
    def TotalDbCnt(self, TotalDbCnt):
        self._TotalDbCnt = TotalDbCnt

    @property
    def TotalTableCnt(self):
        """数据库表的个数
        :rtype: int
        """
        return self._TotalTableCnt

    @TotalTableCnt.setter
    def TotalTableCnt(self, TotalTableCnt):
        self._TotalTableCnt = TotalTableCnt

    @property
    def SensitiveCategoryCnt(self):
        """敏感数据类型个数
        :rtype: int
        """
        return self._SensitiveCategoryCnt

    @SensitiveCategoryCnt.setter
    def SensitiveCategoryCnt(self, SensitiveCategoryCnt):
        self._SensitiveCategoryCnt = SensitiveCategoryCnt

    @property
    def SensitiveFieldCnt(self):
        """敏感字段的个数
        :rtype: int
        """
        return self._SensitiveFieldCnt

    @SensitiveFieldCnt.setter
    def SensitiveFieldCnt(self, SensitiveFieldCnt):
        self._SensitiveFieldCnt = SensitiveFieldCnt

    @property
    def SensitiveLevel(self):
        """敏感等级分布
        :rtype: list of SensitiveLevel
        """
        return self._SensitiveLevel

    @SensitiveLevel.setter
    def SensitiveLevel(self, SensitiveLevel):
        self._SensitiveLevel = SensitiveLevel

    @property
    def SensitiveDbCnt(self):
        """敏感数据库的个数
        :rtype: int
        """
        return self._SensitiveDbCnt

    @SensitiveDbCnt.setter
    def SensitiveDbCnt(self, SensitiveDbCnt):
        self._SensitiveDbCnt = SensitiveDbCnt

    @property
    def SensitiveTableCnt(self):
        """敏感数据库表的个数
        :rtype: int
        """
        return self._SensitiveTableCnt

    @SensitiveTableCnt.setter
    def SensitiveTableCnt(self, SensitiveTableCnt):
        self._SensitiveTableCnt = SensitiveTableCnt

    @property
    def TotalFieldCnt(self):
        """扫描字段的个数
        :rtype: int
        """
        return self._TotalFieldCnt

    @TotalFieldCnt.setter
    def TotalFieldCnt(self, TotalFieldCnt):
        self._TotalFieldCnt = TotalFieldCnt

    @property
    def CategoryDistributed(self):
        """数据分类分布
        :rtype: list of DspaDataCategoryDistributed
        """
        return self._CategoryDistributed

    @CategoryDistributed.setter
    def CategoryDistributed(self, CategoryDistributed):
        self._CategoryDistributed = CategoryDistributed


    def _deserialize(self, params):
        self._DataAssetType = params.get("DataAssetType")
        self._TotalDbCnt = params.get("TotalDbCnt")
        self._TotalTableCnt = params.get("TotalTableCnt")
        self._SensitiveCategoryCnt = params.get("SensitiveCategoryCnt")
        self._SensitiveFieldCnt = params.get("SensitiveFieldCnt")
        if params.get("SensitiveLevel") is not None:
            self._SensitiveLevel = []
            for item in params.get("SensitiveLevel"):
                obj = SensitiveLevel()
                obj._deserialize(item)
                self._SensitiveLevel.append(obj)
        self._SensitiveDbCnt = params.get("SensitiveDbCnt")
        self._SensitiveTableCnt = params.get("SensitiveTableCnt")
        self._TotalFieldCnt = params.get("TotalFieldCnt")
        if params.get("CategoryDistributed") is not None:
            self._CategoryDistributed = []
            for item in params.get("CategoryDistributed"):
                obj = DspaDataCategoryDistributed()
                obj._deserialize(item)
                self._CategoryDistributed.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaRDBDataAssetDetail(AbstractModel):
    """关系型数据库资产详情

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _DbType: 数据库类型
        :type DbType: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _TableName: 数据库表名称
        :type TableName: str
        :param _FieldName: 数据库表字段名称
        :type FieldName: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _CategoryName: 数据分类
        :type CategoryName: str
        :param _LevelRiskName: 敏感等级
        :type LevelRiskName: str
        :param _LevelRiskScore: 分级风险分数，1-10，最小值为1，最大值为10
        :type LevelRiskScore: int
        :param _TrustedScore: 可信分
        :type TrustedScore: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _FieldResultId: 字段扫描结果ID
        :type FieldResultId: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _LevelId: 分级ID
        :type LevelId: int
        :param _CategoryId: 分类ID
        :type CategoryId: int
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _SafeGuard: 保护措施
        :type SafeGuard: :class:`tencentcloud.dsgc.v20190723.models.DspaSafeGuard`
        :param _CategoryFullPath: 分类路径
        :type CategoryFullPath: str
        :param _IdentifyType: 0.系统识别，1人工打标
        :type IdentifyType: int
        :param _CheckStatus: 0未核查 1已核查
        :type CheckStatus: int
        :param _IsSensitiveData: 0非敏感，1敏感
        :type IsSensitiveData: int
        :param _SchemaName: 模式名
        :type SchemaName: str
        """
        self._DataSourceId = None
        self._DbType = None
        self._DbName = None
        self._TableName = None
        self._FieldName = None
        self._RuleName = None
        self._CategoryName = None
        self._LevelRiskName = None
        self._LevelRiskScore = None
        self._TrustedScore = None
        self._ResourceRegion = None
        self._FieldResultId = None
        self._RuleId = None
        self._LevelId = None
        self._CategoryId = None
        self._DataSourceName = None
        self._SafeGuard = None
        self._CategoryFullPath = None
        self._IdentifyType = None
        self._CheckStatus = None
        self._IsSensitiveData = None
        self._SchemaName = None

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DbType(self):
        """数据库类型
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbName(self):
        """数据库名称
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableName(self):
        """数据库表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def FieldName(self):
        """数据库表字段名称
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CategoryName(self):
        """数据分类
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def LevelRiskName(self):
        """敏感等级
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def LevelRiskScore(self):
        """分级风险分数，1-10，最小值为1，最大值为10
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore

    @property
    def TrustedScore(self):
        """可信分
        :rtype: str
        """
        return self._TrustedScore

    @TrustedScore.setter
    def TrustedScore(self, TrustedScore):
        self._TrustedScore = TrustedScore

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def FieldResultId(self):
        """字段扫描结果ID
        :rtype: str
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def LevelId(self):
        """分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def CategoryId(self):
        """分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def SafeGuard(self):
        """保护措施
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DspaSafeGuard`
        """
        return self._SafeGuard

    @SafeGuard.setter
    def SafeGuard(self, SafeGuard):
        self._SafeGuard = SafeGuard

    @property
    def CategoryFullPath(self):
        """分类路径
        :rtype: str
        """
        return self._CategoryFullPath

    @CategoryFullPath.setter
    def CategoryFullPath(self, CategoryFullPath):
        self._CategoryFullPath = CategoryFullPath

    @property
    def IdentifyType(self):
        """0.系统识别，1人工打标
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def CheckStatus(self):
        """0未核查 1已核查
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def IsSensitiveData(self):
        """0非敏感，1敏感
        :rtype: int
        """
        return self._IsSensitiveData

    @IsSensitiveData.setter
    def IsSensitiveData(self, IsSensitiveData):
        self._IsSensitiveData = IsSensitiveData

    @property
    def SchemaName(self):
        """模式名
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DbType = params.get("DbType")
        self._DbName = params.get("DbName")
        self._TableName = params.get("TableName")
        self._FieldName = params.get("FieldName")
        self._RuleName = params.get("RuleName")
        self._CategoryName = params.get("CategoryName")
        self._LevelRiskName = params.get("LevelRiskName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        self._TrustedScore = params.get("TrustedScore")
        self._ResourceRegion = params.get("ResourceRegion")
        self._FieldResultId = params.get("FieldResultId")
        self._RuleId = params.get("RuleId")
        self._LevelId = params.get("LevelId")
        self._CategoryId = params.get("CategoryId")
        self._DataSourceName = params.get("DataSourceName")
        if params.get("SafeGuard") is not None:
            self._SafeGuard = DspaSafeGuard()
            self._SafeGuard._deserialize(params.get("SafeGuard"))
        self._CategoryFullPath = params.get("CategoryFullPath")
        self._IdentifyType = params.get("IdentifyType")
        self._CheckStatus = params.get("CheckStatus")
        self._IsSensitiveData = params.get("IsSensitiveData")
        self._SchemaName = params.get("SchemaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaResourceAccount(AbstractModel):
    """资源账户信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID。
        :type ResourceId: str
        :param _UserName: 用户名。
        :type UserName: str
        :param _Password: 密码。
        :type Password: str
        """
        self._ResourceId = None
        self._UserName = None
        self._Password = None

    @property
    def ResourceId(self):
        """资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def UserName(self):
        """用户名。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """密码。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaSafeGuard(AbstractModel):
    """分类分级扫描结果字段的保护措施

    """

    def __init__(self):
        r"""
        :param _Encrypt: 加密状态，可取值如下：
UNSET 未设置
DISABLE 规则设置未启用
ENABLE 规则设置并启用
        :type Encrypt: str
        :param _Desensitization: 脱敏状态，可取值如下：
UNSET 未设置
DISABLE 规则设置未启用
ENABLE 规则设置并启用
        :type Desensitization: str
        """
        self._Encrypt = None
        self._Desensitization = None

    @property
    def Encrypt(self):
        """加密状态，可取值如下：
UNSET 未设置
DISABLE 规则设置未启用
ENABLE 规则设置并启用
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Desensitization(self):
        """脱敏状态，可取值如下：
UNSET 未设置
DISABLE 规则设置未启用
ENABLE 规则设置并启用
        :rtype: str
        """
        return self._Desensitization

    @Desensitization.setter
    def Desensitization(self, Desensitization):
        self._Desensitization = Desensitization


    def _deserialize(self, params):
        self._Encrypt = params.get("Encrypt")
        self._Desensitization = params.get("Desensitization")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaTaskResult(AbstractModel):
    """任务执行结果描述。

    """

    def __init__(self):
        r"""
        :param _Result: 任务结果。
        :type Result: str
        :param _ResultDescription: 结果描述。
        :type ResultDescription: str
        :param _ResourceId: 资源ID。
        :type ResourceId: str
        :param _MetaType: 资源类型。
        :type MetaType: str
        """
        self._Result = None
        self._ResultDescription = None
        self._ResourceId = None
        self._MetaType = None

    @property
    def Result(self):
        """任务结果。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultDescription(self):
        """结果描述。
        :rtype: str
        """
        return self._ResultDescription

    @ResultDescription.setter
    def ResultDescription(self, ResultDescription):
        self._ResultDescription = ResultDescription

    @property
    def ResourceId(self):
        """资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def MetaType(self):
        """资源类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ResultDescription = params.get("ResultDescription")
        self._ResourceId = params.get("ResourceId")
        self._MetaType = params.get("MetaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DspaUserResourceMeta(AbstractModel):
    """DSPA用户资源元信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 用户资源ID。
        :type ResourceId: str
        :param _ResourceName: 资源名称。
        :type ResourceName: str
        :param _ResourceVip: 资源VIP。
        :type ResourceVip: str
        :param _ResourceVPort: 资源端口。
        :type ResourceVPort: int
        :param _ResourceCreateTime: 资源被创建时间。
        :type ResourceCreateTime: str
        :param _ResourceUniqueVpcId: 用户资源VPC ID 字符串。
        :type ResourceUniqueVpcId: str
        :param _ResourceUniqueSubnetId: 用户资源Subnet ID 字符串。
        :type ResourceUniqueSubnetId: str
        :param _MetaType: 用户资源类型信息。
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourceSyncTime: 资源被同步时间。
        :type ResourceSyncTime: str
        :param _AuthStatus: 资源被授权状态。
        :type AuthStatus: str
        :param _BuildType: 资源创建类型，cloud-云原生资源，build-用户自建资源。
        :type BuildType: str
        :param _MasterInsId: 主实例ID。
        :type MasterInsId: str
        :param _ResourceVpcId: 用户资源VPC ID 整数。
        :type ResourceVpcId: int
        :param _ResourceSubnetId: 用户资源Subnet ID 整数。
        :type ResourceSubnetId: int
        :param _Protocol: 协议类型。
        :type Protocol: str
        :param _ResourceVersion: 资源版本号。
        :type ResourceVersion: str
        :param _ResourceAuthType: 授权方式
        :type ResourceAuthType: str
        :param _ResourceAuthAccount: 授权账号名
        :type ResourceAuthAccount: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _InstanceValue: 实例值
        :type InstanceValue: str
        :param _GovernAuthStatus: //治理授权状态（0：关闭 1：开启）
        :type GovernAuthStatus: int
        :param _AuthRange: 授权范围：all - 授权整个数据源 manual:手动指定数据源
        :type AuthRange: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._ResourceVip = None
        self._ResourceVPort = None
        self._ResourceCreateTime = None
        self._ResourceUniqueVpcId = None
        self._ResourceUniqueSubnetId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._ResourceSyncTime = None
        self._AuthStatus = None
        self._BuildType = None
        self._MasterInsId = None
        self._ResourceVpcId = None
        self._ResourceSubnetId = None
        self._Protocol = None
        self._ResourceVersion = None
        self._ResourceAuthType = None
        self._ResourceAuthAccount = None
        self._InstanceType = None
        self._InstanceValue = None
        self._GovernAuthStatus = None
        self._AuthRange = None

    @property
    def ResourceId(self):
        """用户资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceVip(self):
        """资源VIP。
        :rtype: str
        """
        return self._ResourceVip

    @ResourceVip.setter
    def ResourceVip(self, ResourceVip):
        self._ResourceVip = ResourceVip

    @property
    def ResourceVPort(self):
        """资源端口。
        :rtype: int
        """
        return self._ResourceVPort

    @ResourceVPort.setter
    def ResourceVPort(self, ResourceVPort):
        self._ResourceVPort = ResourceVPort

    @property
    def ResourceCreateTime(self):
        """资源被创建时间。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def ResourceUniqueVpcId(self):
        """用户资源VPC ID 字符串。
        :rtype: str
        """
        return self._ResourceUniqueVpcId

    @ResourceUniqueVpcId.setter
    def ResourceUniqueVpcId(self, ResourceUniqueVpcId):
        self._ResourceUniqueVpcId = ResourceUniqueVpcId

    @property
    def ResourceUniqueSubnetId(self):
        """用户资源Subnet ID 字符串。
        :rtype: str
        """
        return self._ResourceUniqueSubnetId

    @ResourceUniqueSubnetId.setter
    def ResourceUniqueSubnetId(self, ResourceUniqueSubnetId):
        self._ResourceUniqueSubnetId = ResourceUniqueSubnetId

    @property
    def MetaType(self):
        """用户资源类型信息。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceSyncTime(self):
        """资源被同步时间。
        :rtype: str
        """
        return self._ResourceSyncTime

    @ResourceSyncTime.setter
    def ResourceSyncTime(self, ResourceSyncTime):
        self._ResourceSyncTime = ResourceSyncTime

    @property
    def AuthStatus(self):
        """资源被授权状态。
        :rtype: str
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def BuildType(self):
        """资源创建类型，cloud-云原生资源，build-用户自建资源。
        :rtype: str
        """
        return self._BuildType

    @BuildType.setter
    def BuildType(self, BuildType):
        self._BuildType = BuildType

    @property
    def MasterInsId(self):
        """主实例ID。
        :rtype: str
        """
        return self._MasterInsId

    @MasterInsId.setter
    def MasterInsId(self, MasterInsId):
        self._MasterInsId = MasterInsId

    @property
    def ResourceVpcId(self):
        """用户资源VPC ID 整数。
        :rtype: int
        """
        return self._ResourceVpcId

    @ResourceVpcId.setter
    def ResourceVpcId(self, ResourceVpcId):
        self._ResourceVpcId = ResourceVpcId

    @property
    def ResourceSubnetId(self):
        """用户资源Subnet ID 整数。
        :rtype: int
        """
        return self._ResourceSubnetId

    @ResourceSubnetId.setter
    def ResourceSubnetId(self, ResourceSubnetId):
        self._ResourceSubnetId = ResourceSubnetId

    @property
    def Protocol(self):
        """协议类型。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ResourceVersion(self):
        """资源版本号。
        :rtype: str
        """
        return self._ResourceVersion

    @ResourceVersion.setter
    def ResourceVersion(self, ResourceVersion):
        self._ResourceVersion = ResourceVersion

    @property
    def ResourceAuthType(self):
        """授权方式
        :rtype: str
        """
        return self._ResourceAuthType

    @ResourceAuthType.setter
    def ResourceAuthType(self, ResourceAuthType):
        self._ResourceAuthType = ResourceAuthType

    @property
    def ResourceAuthAccount(self):
        """授权账号名
        :rtype: str
        """
        return self._ResourceAuthAccount

    @ResourceAuthAccount.setter
    def ResourceAuthAccount(self, ResourceAuthAccount):
        self._ResourceAuthAccount = ResourceAuthAccount

    @property
    def InstanceType(self):
        """实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceValue(self):
        """实例值
        :rtype: str
        """
        return self._InstanceValue

    @InstanceValue.setter
    def InstanceValue(self, InstanceValue):
        self._InstanceValue = InstanceValue

    @property
    def GovernAuthStatus(self):
        """//治理授权状态（0：关闭 1：开启）
        :rtype: int
        """
        return self._GovernAuthStatus

    @GovernAuthStatus.setter
    def GovernAuthStatus(self, GovernAuthStatus):
        self._GovernAuthStatus = GovernAuthStatus

    @property
    def AuthRange(self):
        """授权范围：all - 授权整个数据源 manual:手动指定数据源
        :rtype: str
        """
        return self._AuthRange

    @AuthRange.setter
    def AuthRange(self, AuthRange):
        self._AuthRange = AuthRange


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ResourceVip = params.get("ResourceVip")
        self._ResourceVPort = params.get("ResourceVPort")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        self._ResourceUniqueVpcId = params.get("ResourceUniqueVpcId")
        self._ResourceUniqueSubnetId = params.get("ResourceUniqueSubnetId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceSyncTime = params.get("ResourceSyncTime")
        self._AuthStatus = params.get("AuthStatus")
        self._BuildType = params.get("BuildType")
        self._MasterInsId = params.get("MasterInsId")
        self._ResourceVpcId = params.get("ResourceVpcId")
        self._ResourceSubnetId = params.get("ResourceSubnetId")
        self._Protocol = params.get("Protocol")
        self._ResourceVersion = params.get("ResourceVersion")
        self._ResourceAuthType = params.get("ResourceAuthType")
        self._ResourceAuthAccount = params.get("ResourceAuthAccount")
        self._InstanceType = params.get("InstanceType")
        self._InstanceValue = params.get("InstanceValue")
        self._GovernAuthStatus = params.get("GovernAuthStatus")
        self._AuthRange = params.get("AuthRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESAsset(AbstractModel):
    """es的资产统计结果

    """

    def __init__(self):
        r"""
        :param _IndexNums: 索引总数量
        :type IndexNums: int
        :param _SensitiveIndexNums: 敏感索引的数量
        :type SensitiveIndexNums: int
        :param _FieldNums: 字段数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感的字段数量
        :type SensitiveFieldNums: int
        """
        self._IndexNums = None
        self._SensitiveIndexNums = None
        self._FieldNums = None
        self._SensitiveFieldNums = None

    @property
    def IndexNums(self):
        """索引总数量
        :rtype: int
        """
        return self._IndexNums

    @IndexNums.setter
    def IndexNums(self, IndexNums):
        self._IndexNums = IndexNums

    @property
    def SensitiveIndexNums(self):
        """敏感索引的数量
        :rtype: int
        """
        return self._SensitiveIndexNums

    @SensitiveIndexNums.setter
    def SensitiveIndexNums(self, SensitiveIndexNums):
        self._SensitiveIndexNums = SensitiveIndexNums

    @property
    def FieldNums(self):
        """字段数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感的字段数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums


    def _deserialize(self, params):
        self._IndexNums = params.get("IndexNums")
        self._SensitiveIndexNums = params.get("SensitiveIndexNums")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESAssetDBDetail(AbstractModel):
    """es敏感资产详情列表

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _IndexName: 索引名称
        :type IndexName: str
        :param _DataType: 数据库类型
        :type DataType: str
        :param _FieldNums: 字段的数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感字段的数量
        :type SensitiveFieldNums: int
        :param _DistributionData: 敏感数据分布
        :type DistributionData: list of Note
        """
        self._DataSourceId = None
        self._IndexName = None
        self._DataType = None
        self._FieldNums = None
        self._SensitiveFieldNums = None
        self._DistributionData = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def IndexName(self):
        """索引名称
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def DataType(self):
        """数据库类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def FieldNums(self):
        """字段的数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感字段的数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums

    @property
    def DistributionData(self):
        """敏感数据分布
        :rtype: list of Note
        """
        return self._DistributionData

    @DistributionData.setter
    def DistributionData(self, DistributionData):
        self._DistributionData = DistributionData


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._IndexName = params.get("IndexName")
        self._DataType = params.get("DataType")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        if params.get("DistributionData") is not None:
            self._DistributionData = []
            for item in params.get("DistributionData"):
                obj = Note()
                obj._deserialize(item)
                self._DistributionData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESDataAssetCountDto(AbstractModel):
    """ES的概览页统计数据

    """

    def __init__(self):
        r"""
        :param _DataAssetType: es
        :type DataAssetType: int
        :param _SensitiveIndexCnt: 敏感索引个数
        :type SensitiveIndexCnt: int
        :param _TotalIndexCnt: 总的索引个数
        :type TotalIndexCnt: int
        :param _SensitiveFieldCnt: 敏感字段个数
        :type SensitiveFieldCnt: int
        :param _TotalFieldCnt: 总的字段个数
        :type TotalFieldCnt: int
        :param _SensitiveCategoryCnt: 敏感分类的个数
        :type SensitiveCategoryCnt: int
        :param _SensitiveLevel: 敏感分级的分布
        :type SensitiveLevel: list of SensitiveLevel
        :param _CategoryDistributed: 敏感分类的分布
        :type CategoryDistributed: list of DspaDataCategoryDistributed
        """
        self._DataAssetType = None
        self._SensitiveIndexCnt = None
        self._TotalIndexCnt = None
        self._SensitiveFieldCnt = None
        self._TotalFieldCnt = None
        self._SensitiveCategoryCnt = None
        self._SensitiveLevel = None
        self._CategoryDistributed = None

    @property
    def DataAssetType(self):
        """es
        :rtype: int
        """
        return self._DataAssetType

    @DataAssetType.setter
    def DataAssetType(self, DataAssetType):
        self._DataAssetType = DataAssetType

    @property
    def SensitiveIndexCnt(self):
        """敏感索引个数
        :rtype: int
        """
        return self._SensitiveIndexCnt

    @SensitiveIndexCnt.setter
    def SensitiveIndexCnt(self, SensitiveIndexCnt):
        self._SensitiveIndexCnt = SensitiveIndexCnt

    @property
    def TotalIndexCnt(self):
        """总的索引个数
        :rtype: int
        """
        return self._TotalIndexCnt

    @TotalIndexCnt.setter
    def TotalIndexCnt(self, TotalIndexCnt):
        self._TotalIndexCnt = TotalIndexCnt

    @property
    def SensitiveFieldCnt(self):
        """敏感字段个数
        :rtype: int
        """
        return self._SensitiveFieldCnt

    @SensitiveFieldCnt.setter
    def SensitiveFieldCnt(self, SensitiveFieldCnt):
        self._SensitiveFieldCnt = SensitiveFieldCnt

    @property
    def TotalFieldCnt(self):
        """总的字段个数
        :rtype: int
        """
        return self._TotalFieldCnt

    @TotalFieldCnt.setter
    def TotalFieldCnt(self, TotalFieldCnt):
        self._TotalFieldCnt = TotalFieldCnt

    @property
    def SensitiveCategoryCnt(self):
        """敏感分类的个数
        :rtype: int
        """
        return self._SensitiveCategoryCnt

    @SensitiveCategoryCnt.setter
    def SensitiveCategoryCnt(self, SensitiveCategoryCnt):
        self._SensitiveCategoryCnt = SensitiveCategoryCnt

    @property
    def SensitiveLevel(self):
        """敏感分级的分布
        :rtype: list of SensitiveLevel
        """
        return self._SensitiveLevel

    @SensitiveLevel.setter
    def SensitiveLevel(self, SensitiveLevel):
        self._SensitiveLevel = SensitiveLevel

    @property
    def CategoryDistributed(self):
        """敏感分类的分布
        :rtype: list of DspaDataCategoryDistributed
        """
        return self._CategoryDistributed

    @CategoryDistributed.setter
    def CategoryDistributed(self, CategoryDistributed):
        self._CategoryDistributed = CategoryDistributed


    def _deserialize(self, params):
        self._DataAssetType = params.get("DataAssetType")
        self._SensitiveIndexCnt = params.get("SensitiveIndexCnt")
        self._TotalIndexCnt = params.get("TotalIndexCnt")
        self._SensitiveFieldCnt = params.get("SensitiveFieldCnt")
        self._TotalFieldCnt = params.get("TotalFieldCnt")
        self._SensitiveCategoryCnt = params.get("SensitiveCategoryCnt")
        if params.get("SensitiveLevel") is not None:
            self._SensitiveLevel = []
            for item in params.get("SensitiveLevel"):
                obj = SensitiveLevel()
                obj._deserialize(item)
                self._SensitiveLevel.append(obj)
        if params.get("CategoryDistributed") is not None:
            self._CategoryDistributed = []
            for item in params.get("CategoryDistributed"):
                obj = DspaDataCategoryDistributed()
                obj._deserialize(item)
                self._CategoryDistributed.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESDataAssetDetail(AbstractModel):
    """ES的概览页资产详情

    """

    def __init__(self):
        r"""
        :param _FieldResultId: id
        :type FieldResultId: int
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _DataSourceType: 类型
        :type DataSourceType: str
        :param _ResourceRegion: 地域信息
        :type ResourceRegion: str
        :param _IndexName: 索引名称
        :type IndexName: str
        :param _FieldName: 字段名称
        :type FieldName: str
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _CategoryName: 分类名称
        :type CategoryName: str
        :param _CategoryArr: 分类路径数组
        :type CategoryArr: list of str
        :param _LevelId: 等级id
        :type LevelId: int
        :param _LevelRiskName: 分级名称
        :type LevelRiskName: str
        :param _LevelRiskScore: 分级分数
        :type LevelRiskScore: int
        :param _TrustedScore: 可信分
        :type TrustedScore: float
        :param _RuleId: 规则id
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _IdentifyType: 0系统识别，1人工打标
        :type IdentifyType: int
        :param _CheckStatus: 0未核查，1已核查
        :type CheckStatus: int
        """
        self._FieldResultId = None
        self._DataSourceId = None
        self._DataSourceName = None
        self._DataSourceType = None
        self._ResourceRegion = None
        self._IndexName = None
        self._FieldName = None
        self._CategoryId = None
        self._CategoryName = None
        self._CategoryArr = None
        self._LevelId = None
        self._LevelRiskName = None
        self._LevelRiskScore = None
        self._TrustedScore = None
        self._RuleId = None
        self._RuleName = None
        self._IdentifyType = None
        self._CheckStatus = None

    @property
    def FieldResultId(self):
        """id
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def DataSourceType(self):
        """类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def ResourceRegion(self):
        """地域信息
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def IndexName(self):
        """索引名称
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def FieldName(self):
        """字段名称
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        """分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def CategoryArr(self):
        """分类路径数组
        :rtype: list of str
        """
        return self._CategoryArr

    @CategoryArr.setter
    def CategoryArr(self, CategoryArr):
        self._CategoryArr = CategoryArr

    @property
    def LevelId(self):
        """等级id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelRiskName(self):
        """分级名称
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def LevelRiskScore(self):
        """分级分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore

    @property
    def TrustedScore(self):
        """可信分
        :rtype: float
        """
        return self._TrustedScore

    @TrustedScore.setter
    def TrustedScore(self, TrustedScore):
        self._TrustedScore = TrustedScore

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def IdentifyType(self):
        """0系统识别，1人工打标
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def CheckStatus(self):
        """0未核查，1已核查
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus


    def _deserialize(self, params):
        self._FieldResultId = params.get("FieldResultId")
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceName = params.get("DataSourceName")
        self._DataSourceType = params.get("DataSourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._IndexName = params.get("IndexName")
        self._FieldName = params.get("FieldName")
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._CategoryArr = params.get("CategoryArr")
        self._LevelId = params.get("LevelId")
        self._LevelRiskName = params.get("LevelRiskName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        self._TrustedScore = params.get("TrustedScore")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._IdentifyType = params.get("IdentifyType")
        self._CheckStatus = params.get("CheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESInstance(AbstractModel):
    """创建评估任务的ES详情

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        :param _ResourceRegion: 地域
        :type ResourceRegion: str
        :param _DiscoveryTaskId: 扫描任务ID
        :type DiscoveryTaskId: int
        :param _DiscoveryTaskInstanceID: 扫描任务实例ID
        :type DiscoveryTaskInstanceID: int
        """
        self._DataSourceId = None
        self._DataSourceType = None
        self._ResourceRegion = None
        self._DiscoveryTaskId = None
        self._DiscoveryTaskInstanceID = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def ResourceRegion(self):
        """地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DiscoveryTaskId(self):
        """扫描任务ID
        :rtype: int
        """
        return self._DiscoveryTaskId

    @DiscoveryTaskId.setter
    def DiscoveryTaskId(self, DiscoveryTaskId):
        self._DiscoveryTaskId = DiscoveryTaskId

    @property
    def DiscoveryTaskInstanceID(self):
        """扫描任务实例ID
        :rtype: int
        """
        return self._DiscoveryTaskInstanceID

    @DiscoveryTaskInstanceID.setter
    def DiscoveryTaskInstanceID(self, DiscoveryTaskInstanceID):
        self._DiscoveryTaskInstanceID = DiscoveryTaskInstanceID


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceType = params.get("DataSourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DiscoveryTaskId = params.get("DiscoveryTaskId")
        self._DiscoveryTaskInstanceID = params.get("DiscoveryTaskInstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ESTaskResultDetail(AbstractModel):
    """ES扫描任务结果详情

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _TaskId: 任务id
        :type TaskId: int
        :param _FieldName: 字段名称
        :type FieldName: str
        :param _RuleId: 规则id
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _CategoryId: 分类id
        :type CategoryId: int
        :param _CategoryName: 分类名称
        :type CategoryName: str
        :param _CategoryArr: 多级分类的路径
        :type CategoryArr: list of str
        :param _LevelId: 分级id
        :type LevelId: int
        :param _LevelName: 分级名称
        :type LevelName: str
        :param _LevelRiskScore: 分级分数
        :type LevelRiskScore: int
        """
        self._Id = None
        self._TaskId = None
        self._FieldName = None
        self._RuleId = None
        self._RuleName = None
        self._CategoryId = None
        self._CategoryName = None
        self._CategoryArr = None
        self._LevelId = None
        self._LevelName = None
        self._LevelRiskScore = None

    @property
    def Id(self):
        """id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TaskId(self):
        """任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FieldName(self):
        """字段名称
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CategoryId(self):
        """分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        """分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def CategoryArr(self):
        """多级分类的路径
        :rtype: list of str
        """
        return self._CategoryArr

    @CategoryArr.setter
    def CategoryArr(self, CategoryArr):
        self._CategoryArr = CategoryArr

    @property
    def LevelId(self):
        """分级id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """分级名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def LevelRiskScore(self):
        """分级分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TaskId = params.get("TaskId")
        self._FieldName = params.get("FieldName")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._CategoryArr = params.get("CategoryArr")
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableDSPADiscoveryRuleRequest(AbstractModel):
    """EnableDSPADiscoveryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Enable: 开关ScanRule
        :type Enable: bool
        """
        self._DspaId = None
        self._RuleId = None
        self._Enable = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Enable(self):
        """开关ScanRule
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._RuleId = params.get("RuleId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableDSPADiscoveryRuleResponse(AbstractModel):
    """EnableDSPADiscoveryRule返回参数结构体

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


class EnableTrialVersionRequest(AbstractModel):
    """EnableTrialVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _TrialVersion: 体验版本名称。
        :type TrialVersion: str
        """
        self._DspaId = None
        self._TrialVersion = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TrialVersion(self):
        """体验版本名称。
        :rtype: str
        """
        return self._TrialVersion

    @TrialVersion.setter
    def TrialVersion(self, TrialVersion):
        self._TrialVersion = TrialVersion


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TrialVersion = params.get("TrialVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTrialVersionResponse(AbstractModel):
    """EnableTrialVersion返回参数结构体

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


class ErrDescription(AbstractModel):
    """错误信息描述

    """

    def __init__(self):
        r"""
        :param _ErrCode: 错误码。
        :type ErrCode: str
        :param _ErrMessage: 具体错误信息。
        :type ErrMessage: str
        """
        self._ErrCode = None
        self._ErrMessage = None

    @property
    def ErrCode(self):
        """错误码。
        :rtype: str
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMessage(self):
        """具体错误信息。
        :rtype: str
        """
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage


    def _deserialize(self, params):
        self._ErrCode = params.get("ErrCode")
        self._ErrMessage = params.get("ErrMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetDetailDataRequest(AbstractModel):
    """ExportAssetDetailData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _ComplianceId: 合规组id
        :type ComplianceId: int
        :param _MetaDataType: 资产类型（rdb,cvm_db,cos）
        :type MetaDataType: str
        :param _Filters: 过滤数组。支持的Name：
DataSourceID 数据源ID
DbName 数据库名称
CategoryID 敏感数据分类ID
RuleID 规则ID
LevelID 敏感分级ID
ResourceRegion 资源所在地域
DataSourceType 数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
注意：每个name默认支持最多5个values。
        :type Filters: list of Filter
        :param _CasbId: casbId
        :type CasbId: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._MetaDataType = None
        self._Filters = None
        self._CasbId = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def MetaDataType(self):
        """资产类型（rdb,cvm_db,cos）
        :rtype: str
        """
        return self._MetaDataType

    @MetaDataType.setter
    def MetaDataType(self, MetaDataType):
        self._MetaDataType = MetaDataType

    @property
    def Filters(self):
        """过滤数组。支持的Name：
DataSourceID 数据源ID
DbName 数据库名称
CategoryID 敏感数据分类ID
RuleID 规则ID
LevelID 敏感分级ID
ResourceRegion 资源所在地域
DataSourceType 数据源类型，不填默认过滤非自建的所有关系型数据源类型，填selfbuilt-db只过滤自建类型
注意：每个name默认支持最多5个values。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def CasbId(self):
        """casbId
        :rtype: str
        """
        return self._CasbId

    @CasbId.setter
    def CasbId(self, CasbId):
        self._CasbId = CasbId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._MetaDataType = params.get("MetaDataType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._CasbId = params.get("CasbId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetDetailDataResponse(AbstractModel):
    """ExportAssetDetailData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportTaskId: 导出任务id
        :type ExportTaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportTaskId = None
        self._RequestId = None

    @property
    def ExportTaskId(self):
        """导出任务id
        :rtype: int
        """
        return self._ExportTaskId

    @ExportTaskId.setter
    def ExportTaskId(self, ExportTaskId):
        self._ExportTaskId = ExportTaskId

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
        self._ExportTaskId = params.get("ExportTaskId")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
        


class GetResourceConnectionStatusRequest(AbstractModel):
    """GetResourceConnectionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _MetaType: 资源类型。
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _ResourceId: 资源列表中展示的资源ID。
        :type ResourceId: str
        """
        self._DspaId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._ResourceId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MetaType(self):
        """资源类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        """资源所处地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceId(self):
        """资源列表中展示的资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourceConnectionStatusResponse(AbstractModel):
    """GetResourceConnectionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectionStatus: 连接状态，success -- 连接成功，failed -- 连接失败
        :type ConnectionStatus: str
        :param _ConnectionDesc: 连接状态的描述信息。
        :type ConnectionDesc: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConnectionStatus = None
        self._ConnectionDesc = None
        self._RequestId = None

    @property
    def ConnectionStatus(self):
        """连接状态，success -- 连接成功，failed -- 连接失败
        :rtype: str
        """
        return self._ConnectionStatus

    @ConnectionStatus.setter
    def ConnectionStatus(self, ConnectionStatus):
        self._ConnectionStatus = ConnectionStatus

    @property
    def ConnectionDesc(self):
        """连接状态的描述信息。
        :rtype: str
        """
        return self._ConnectionDesc

    @ConnectionDesc.setter
    def ConnectionDesc(self, ConnectionDesc):
        self._ConnectionDesc = ConnectionDesc

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
        self._ConnectionStatus = params.get("ConnectionStatus")
        self._ConnectionDesc = params.get("ConnectionDesc")
        self._RequestId = params.get("RequestId")


class GetTrialVersionRequest(AbstractModel):
    """GetTrialVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTrialVersionResponse(AbstractModel):
    """GetTrialVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrialVersion: 体验版本名称。
        :type TrialVersion: str
        :param _TrialEndAt: 版本体验结束时间戳。
        :type TrialEndAt: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrialVersion = None
        self._TrialEndAt = None
        self._RequestId = None

    @property
    def TrialVersion(self):
        """体验版本名称。
        :rtype: str
        """
        return self._TrialVersion

    @TrialVersion.setter
    def TrialVersion(self, TrialVersion):
        self._TrialVersion = TrialVersion

    @property
    def TrialEndAt(self):
        """版本体验结束时间戳。
        :rtype: int
        """
        return self._TrialEndAt

    @TrialEndAt.setter
    def TrialEndAt(self, TrialEndAt):
        self._TrialEndAt = TrialEndAt

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
        self._TrialVersion = params.get("TrialVersion")
        self._TrialEndAt = params.get("TrialEndAt")
        self._RequestId = params.get("RequestId")


class GetUserQuotaInfoRequest(AbstractModel):
    """GetUserQuotaInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        """
        self._DspaId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserQuotaInfoResponse(AbstractModel):
    """GetUserQuotaInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _DbTotalQuota: 用户购买的DB配额。
        :type DbTotalQuota: int
        :param _CosTotalQuota: 用户购买的COS存储量配额。
        :type CosTotalQuota: int
        :param _DbRemainQuota: 用户可用的DB配额。
        :type DbRemainQuota: int
        :param _CosRemainQuota: 用户可用的COS存储量配额。
        :type CosRemainQuota: float
        :param _CosQuotaUnit: COS存储量单位，例如TB。
        :type CosQuotaUnit: str
        :param _DBUnbindNum: db月解绑次数
        :type DBUnbindNum: int
        :param _COSUnbindNum: cos月解绑次数
        :type COSUnbindNum: int
        :param _InsTotalQuota: 用户购买的实例配额。
        :type InsTotalQuota: int
        :param _InsRemainQuota: 用户可用的实例配额。
        :type InsRemainQuota: int
        :param _Version: 用户购买的版本
        :type Version: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DspaId = None
        self._DbTotalQuota = None
        self._CosTotalQuota = None
        self._DbRemainQuota = None
        self._CosRemainQuota = None
        self._CosQuotaUnit = None
        self._DBUnbindNum = None
        self._COSUnbindNum = None
        self._InsTotalQuota = None
        self._InsRemainQuota = None
        self._Version = None
        self._RequestId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DbTotalQuota(self):
        """用户购买的DB配额。
        :rtype: int
        """
        return self._DbTotalQuota

    @DbTotalQuota.setter
    def DbTotalQuota(self, DbTotalQuota):
        self._DbTotalQuota = DbTotalQuota

    @property
    def CosTotalQuota(self):
        """用户购买的COS存储量配额。
        :rtype: int
        """
        return self._CosTotalQuota

    @CosTotalQuota.setter
    def CosTotalQuota(self, CosTotalQuota):
        self._CosTotalQuota = CosTotalQuota

    @property
    def DbRemainQuota(self):
        """用户可用的DB配额。
        :rtype: int
        """
        return self._DbRemainQuota

    @DbRemainQuota.setter
    def DbRemainQuota(self, DbRemainQuota):
        self._DbRemainQuota = DbRemainQuota

    @property
    def CosRemainQuota(self):
        """用户可用的COS存储量配额。
        :rtype: float
        """
        return self._CosRemainQuota

    @CosRemainQuota.setter
    def CosRemainQuota(self, CosRemainQuota):
        self._CosRemainQuota = CosRemainQuota

    @property
    def CosQuotaUnit(self):
        """COS存储量单位，例如TB。
        :rtype: str
        """
        return self._CosQuotaUnit

    @CosQuotaUnit.setter
    def CosQuotaUnit(self, CosQuotaUnit):
        self._CosQuotaUnit = CosQuotaUnit

    @property
    def DBUnbindNum(self):
        """db月解绑次数
        :rtype: int
        """
        return self._DBUnbindNum

    @DBUnbindNum.setter
    def DBUnbindNum(self, DBUnbindNum):
        self._DBUnbindNum = DBUnbindNum

    @property
    def COSUnbindNum(self):
        """cos月解绑次数
        :rtype: int
        """
        return self._COSUnbindNum

    @COSUnbindNum.setter
    def COSUnbindNum(self, COSUnbindNum):
        self._COSUnbindNum = COSUnbindNum

    @property
    def InsTotalQuota(self):
        """用户购买的实例配额。
        :rtype: int
        """
        return self._InsTotalQuota

    @InsTotalQuota.setter
    def InsTotalQuota(self, InsTotalQuota):
        self._InsTotalQuota = InsTotalQuota

    @property
    def InsRemainQuota(self):
        """用户可用的实例配额。
        :rtype: int
        """
        return self._InsRemainQuota

    @InsRemainQuota.setter
    def InsRemainQuota(self, InsRemainQuota):
        self._InsRemainQuota = InsRemainQuota

    @property
    def Version(self):
        """用户购买的版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        self._DspaId = params.get("DspaId")
        self._DbTotalQuota = params.get("DbTotalQuota")
        self._CosTotalQuota = params.get("CosTotalQuota")
        self._DbRemainQuota = params.get("DbRemainQuota")
        self._CosRemainQuota = params.get("CosRemainQuota")
        self._CosQuotaUnit = params.get("CosQuotaUnit")
        self._DBUnbindNum = params.get("DBUnbindNum")
        self._COSUnbindNum = params.get("COSUnbindNum")
        self._InsTotalQuota = params.get("InsTotalQuota")
        self._InsRemainQuota = params.get("InsRemainQuota")
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class HighRiskAssetsDetail(AbstractModel):
    """高风险资产详情信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _AssetsName: 资产对象名称
        :type AssetsName: str
        :param _HighRiskCount: 高风险个数
        :type HighRiskCount: int
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _TotalRiskCount: 总的风险个数
        :type TotalRiskCount: int
        :param _RiskSide: 风险面
        :type RiskSide: str
        :param _ResourceRegion: 地域
        :type ResourceRegion: str
        """
        self._InstanceId = None
        self._DataSourceType = None
        self._DataSourceName = None
        self._AssetsName = None
        self._HighRiskCount = None
        self._RiskType = None
        self._TotalRiskCount = None
        self._RiskSide = None
        self._ResourceRegion = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def AssetsName(self):
        """资产对象名称
        :rtype: str
        """
        return self._AssetsName

    @AssetsName.setter
    def AssetsName(self, AssetsName):
        self._AssetsName = AssetsName

    @property
    def HighRiskCount(self):
        """高风险个数
        :rtype: int
        """
        return self._HighRiskCount

    @HighRiskCount.setter
    def HighRiskCount(self, HighRiskCount):
        self._HighRiskCount = HighRiskCount

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def TotalRiskCount(self):
        """总的风险个数
        :rtype: int
        """
        return self._TotalRiskCount

    @TotalRiskCount.setter
    def TotalRiskCount(self, TotalRiskCount):
        self._TotalRiskCount = TotalRiskCount

    @property
    def RiskSide(self):
        """风险面
        :rtype: str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide

    @property
    def ResourceRegion(self):
        """地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DataSourceType = params.get("DataSourceType")
        self._DataSourceName = params.get("DataSourceName")
        self._AssetsName = params.get("AssetsName")
        self._HighRiskCount = params.get("HighRiskCount")
        self._RiskType = params.get("RiskType")
        self._TotalRiskCount = params.get("TotalRiskCount")
        self._RiskSide = params.get("RiskSide")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemLevel(AbstractModel):
    """某个分级单个信息

    """

    def __init__(self):
        r"""
        :param _LevelRiskName: 分级标识名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type LevelRiskName: str
        :param _LevelRiskScore: 分级标识对应的风险分数值，1-10，最小为1，最大为10
        :type LevelRiskScore: int
        """
        self._LevelRiskName = None
        self._LevelRiskScore = None

    @property
    def LevelRiskName(self):
        """分级标识名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def LevelRiskScore(self):
        """分级标识对应的风险分数值，1-10，最小为1，最大为10
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore


    def _deserialize(self, params):
        self._LevelRiskName = params.get("LevelRiskName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LevelItem(AbstractModel):
    """分级单项信息

    """

    def __init__(self):
        r"""
        :param _LevelId: 分级ID
        :type LevelId: int
        :param _LevelGroupId: 分级组ID
        :type LevelGroupId: int
        :param _LevelRiskName: 分级标识名称，支持内置分级，内置分级取值：高，中，低，也可以自定义
        :type LevelRiskName: str
        :param _LevelRiskScore: 分级风险分数，1-10，最小值为1，最大值为10
        :type LevelRiskScore: int
        """
        self._LevelId = None
        self._LevelGroupId = None
        self._LevelRiskName = None
        self._LevelRiskScore = None

    @property
    def LevelId(self):
        """分级ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelGroupId(self):
        """分级组ID
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

    @property
    def LevelRiskName(self):
        """分级标识名称，支持内置分级，内置分级取值：高，中，低，也可以自定义
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def LevelRiskScore(self):
        """分级风险分数，1-10，最小值为1，最大值为10
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore


    def _deserialize(self, params):
        self._LevelId = params.get("LevelId")
        self._LevelGroupId = params.get("LevelGroupId")
        self._LevelRiskName = params.get("LevelRiskName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDSPAClustersRequest(AbstractModel):
    """ListDSPAClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页步长，默认为100。
        :type Limit: int
        :param _Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤项。
支持的过滤项包括：DspaId、Status、Version、DspaName、Channel。
DspaId和DspaName支持模糊搜索。
Status支持的可选值：enabled、disabled。
Version支持的可选值：trial、official。
Channel支持的可选值：sp_cds_dsgc_pre（代表dsgc实例）、sp_cds_dsgc_wedata_dc（代表wedata实例）
        :type Filters: list of DspaDataSourceMngFilter
        :param _ListMode: 展示模式。

目前只有两个值的处理逻辑：

空值：需要查询每个实例的配额信息，因为是串行查询，所以速度很慢，limit最大为100

"simple"：不需要查询每个实例的配额信息，速度快，limit最大为1000
        :type ListMode: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._ListMode = None

    @property
    def Limit(self):
        """分页步长，默认为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤项。
支持的过滤项包括：DspaId、Status、Version、DspaName、Channel。
DspaId和DspaName支持模糊搜索。
Status支持的可选值：enabled、disabled。
Version支持的可选值：trial、official。
Channel支持的可选值：sp_cds_dsgc_pre（代表dsgc实例）、sp_cds_dsgc_wedata_dc（代表wedata实例）
        :rtype: list of DspaDataSourceMngFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ListMode(self):
        """展示模式。

目前只有两个值的处理逻辑：

空值：需要查询每个实例的配额信息，因为是串行查询，所以速度很慢，limit最大为100

"simple"：不需要查询每个实例的配额信息，速度快，limit最大为1000
        :rtype: str
        """
        return self._ListMode

    @ListMode.setter
    def ListMode(self, ListMode):
        self._ListMode = ListMode


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaDataSourceMngFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ListMode = params.get("ListMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDSPAClustersResponse(AbstractModel):
    """ListDSPAClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源总数。
        :type TotalCount: int
        :param _InstanceList: 资源列表。
        :type InstanceList: list of DspaInstance
        :param _DenyAll: 是否被拒绝访问所有dspa实例资源。
        :type DenyAll: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._DenyAll = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """资源列表。
        :rtype: list of DspaInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def DenyAll(self):
        """是否被拒绝访问所有dspa实例资源。
        :rtype: bool
        """
        return self._DenyAll

    @DenyAll.setter
    def DenyAll(self, DenyAll):
        self._DenyAll = DenyAll

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DspaInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._DenyAll = params.get("DenyAll")
        self._RequestId = params.get("RequestId")


class ListDSPACosMetaResourcesRequest(AbstractModel):
    """ListDSPACosMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: 实例Id
        :type DspaId: str
        :param _Filters: 过滤数组。支持的Name：
Bucket - 桶名，支持模糊匹配

ResoureRegion - 资源所处地域，需要填写完整地域名称，不支持模糊匹配。

Valid -- 资源是否有效，"1" 表示有效，"0"表示无效。
        :type Filters: list of DspaDataSourceMngFilter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为100。
        :type Limit: int
        :param _BindType: 资源绑定状态过滤，默认为全部
        :type BindType: str
        """
        self._DspaId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._BindType = None

    @property
    def DspaId(self):
        """实例Id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Filters(self):
        """过滤数组。支持的Name：
Bucket - 桶名，支持模糊匹配

ResoureRegion - 资源所处地域，需要填写完整地域名称，不支持模糊匹配。

Valid -- 资源是否有效，"1" 表示有效，"0"表示无效。
        :rtype: list of DspaDataSourceMngFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def BindType(self):
        """资源绑定状态过滤，默认为全部
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaDataSourceMngFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDSPACosMetaResourcesResponse(AbstractModel):
    """ListDSPACosMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的COS元数据数量。
        :type TotalCount: int
        :param _Items: COS元数据信息
        :type Items: list of DSPACosMetaDataInfo
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._DspaId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的COS元数据数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """COS元数据信息
        :rtype: list of DSPACosMetaDataInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DSPACosMetaDataInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._DspaId = params.get("DspaId")
        self._RequestId = params.get("RequestId")


class ListDSPAMetaResourcesRequest(AbstractModel):
    """ListDSPAMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _Filters: 过滤项。
可过滤值包括：
ResoureRegion - 资源所处地域，需要填写完整地域名称，不支持模糊匹配。

AuthStatus - authorized（已授权）、unauthorized（未授权）、deleted（资源已被删除），不支持模糊匹配，需要填写完整。

BuildType - cloud（云原生资源）、build（用户自建资源），不支持模糊匹配，需要填写完整。

MetaType - cdb（云数据Mysql）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbmysql（TDSQL-C MySQL版）、cos（对象存储）、mysql_like_proto（自建型Mysql协议类关系型数据库）、postgre_like_proto（自建型Postgre协议类关系型数据库）。

ResourceId - 资源ID，支持模糊搜索。

CvmID - 自建资源对应CvmId，如：ins-xxxxxxxx。该字段用于casb调用dsgc接口时，根据cvmId和vport确定具体的自建实例
        :type Filters: list of DspaDataSourceMngFilter
        :param _Limit: 分页步长，默认为100。
        :type Limit: int
        :param _Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param _BindType: 资源绑定状态过滤，默认为全部
        :type BindType: str
        """
        self._DspaId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._BindType = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Filters(self):
        """过滤项。
可过滤值包括：
ResoureRegion - 资源所处地域，需要填写完整地域名称，不支持模糊匹配。

AuthStatus - authorized（已授权）、unauthorized（未授权）、deleted（资源已被删除），不支持模糊匹配，需要填写完整。

BuildType - cloud（云原生资源）、build（用户自建资源），不支持模糊匹配，需要填写完整。

MetaType - cdb（云数据Mysql）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbmysql（TDSQL-C MySQL版）、cos（对象存储）、mysql_like_proto（自建型Mysql协议类关系型数据库）、postgre_like_proto（自建型Postgre协议类关系型数据库）。

ResourceId - 资源ID，支持模糊搜索。

CvmID - 自建资源对应CvmId，如：ins-xxxxxxxx。该字段用于casb调用dsgc接口时，根据cvmId和vport确定具体的自建实例
        :rtype: list of DspaDataSourceMngFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """分页步长，默认为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BindType(self):
        """资源绑定状态过滤，默认为全部
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DspaDataSourceMngFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDSPAMetaResourcesResponse(AbstractModel):
    """ListDSPAMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _Resources: 用户资源列表。
        :type Resources: list of DspaUserResourceMeta
        :param _TotalCount: 资源总量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DspaId = None
        self._Resources = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Resources(self):
        """用户资源列表。
        :rtype: list of DspaUserResourceMeta
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def TotalCount(self):
        """资源总量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._DspaId = params.get("DspaId")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = DspaUserResourceMeta()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ModifyDSPAAssessmentRiskLatestRequest(AbstractModel):
    """ModifyDSPAAssessmentRiskLatest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _Status: 风险状态（waiting:待处理，processing:处理中，finished:已处理，ignored:已忽略）
        :type Status: str
        :param _RiskLatestTableId: 最新风险项Id
        :type RiskLatestTableId: int
        :param _Note: 备注
        :type Note: str
        :param _ProcessPeople: 处置人
        :type ProcessPeople: str
        :param _BathRiskIdList: 批量处理的列表
        :type BathRiskIdList: list of int
        """
        self._DspaId = None
        self._Status = None
        self._RiskLatestTableId = None
        self._Note = None
        self._ProcessPeople = None
        self._BathRiskIdList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Status(self):
        """风险状态（waiting:待处理，processing:处理中，finished:已处理，ignored:已忽略）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskLatestTableId(self):
        warnings.warn("parameter `RiskLatestTableId` is deprecated", DeprecationWarning) 

        """最新风险项Id
        :rtype: int
        """
        return self._RiskLatestTableId

    @RiskLatestTableId.setter
    def RiskLatestTableId(self, RiskLatestTableId):
        warnings.warn("parameter `RiskLatestTableId` is deprecated", DeprecationWarning) 

        self._RiskLatestTableId = RiskLatestTableId

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ProcessPeople(self):
        """处置人
        :rtype: str
        """
        return self._ProcessPeople

    @ProcessPeople.setter
    def ProcessPeople(self, ProcessPeople):
        self._ProcessPeople = ProcessPeople

    @property
    def BathRiskIdList(self):
        """批量处理的列表
        :rtype: list of int
        """
        return self._BathRiskIdList

    @BathRiskIdList.setter
    def BathRiskIdList(self, BathRiskIdList):
        self._BathRiskIdList = BathRiskIdList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Status = params.get("Status")
        self._RiskLatestTableId = params.get("RiskLatestTableId")
        self._Note = params.get("Note")
        self._ProcessPeople = params.get("ProcessPeople")
        self._BathRiskIdList = params.get("BathRiskIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAAssessmentRiskLatestResponse(AbstractModel):
    """ModifyDSPAAssessmentRiskLatest返回参数结构体

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


class ModifyDSPAAssessmentRiskLevelRequest(AbstractModel):
    """ModifyDSPAAssessmentRiskLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _RiskLevelName: 风险等级名称
        :type RiskLevelName: str
        :param _RiskLevelDescription: 风险的描述
        :type RiskLevelDescription: str
        :param _RiskId: 风险id
        :type RiskId: int
        :param _ModifyRiskItem: 需要修改的风险列表
        :type ModifyRiskItem: list of RiskLevelMatrix
        """
        self._DspaId = None
        self._RiskLevelName = None
        self._RiskLevelDescription = None
        self._RiskId = None
        self._ModifyRiskItem = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def RiskLevelName(self):
        """风险等级名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def RiskLevelDescription(self):
        """风险的描述
        :rtype: str
        """
        return self._RiskLevelDescription

    @RiskLevelDescription.setter
    def RiskLevelDescription(self, RiskLevelDescription):
        self._RiskLevelDescription = RiskLevelDescription

    @property
    def RiskId(self):
        """风险id
        :rtype: int
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def ModifyRiskItem(self):
        """需要修改的风险列表
        :rtype: list of RiskLevelMatrix
        """
        return self._ModifyRiskItem

    @ModifyRiskItem.setter
    def ModifyRiskItem(self, ModifyRiskItem):
        self._ModifyRiskItem = ModifyRiskItem


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._RiskLevelName = params.get("RiskLevelName")
        self._RiskLevelDescription = params.get("RiskLevelDescription")
        self._RiskId = params.get("RiskId")
        if params.get("ModifyRiskItem") is not None:
            self._ModifyRiskItem = []
            for item in params.get("ModifyRiskItem"):
                obj = RiskLevelMatrix()
                obj._deserialize(item)
                self._ModifyRiskItem.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAAssessmentRiskLevelResponse(AbstractModel):
    """ModifyDSPAAssessmentRiskLevel返回参数结构体

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


class ModifyDSPAAssessmentRiskRequest(AbstractModel):
    """ModifyDSPAAssessmentRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _TaskId: 评估任务Id，格式“task-xxxxxxxx”
        :type TaskId: str
        :param _RiskId: 风险项Id，格式“risk-xxxxxxxx”
        :type RiskId: str
        :param _Status: 风险项状态。（waiting:待处理，processing:处理中，finished:已处理）
        :type Status: str
        """
        self._DspaId = None
        self._TaskId = None
        self._RiskId = None
        self._Status = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """评估任务Id，格式“task-xxxxxxxx”
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RiskId(self):
        """风险项Id，格式“risk-xxxxxxxx”
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def Status(self):
        """风险项状态。（waiting:待处理，processing:处理中，finished:已处理）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._RiskId = params.get("RiskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAAssessmentRiskResponse(AbstractModel):
    """ModifyDSPAAssessmentRisk返回参数结构体

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


class ModifyDSPAAssessmentRiskTemplateRequest(AbstractModel):
    """ModifyDSPAAssessmentRiskTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _RiskLevelId: 修改的风险等级id
        :type RiskLevelId: int
        :param _TemplateDescription: 模板的描述
        :type TemplateDescription: str
        :param _RiskIdList: 脆弱项列表
        :type RiskIdList: list of int
        """
        self._DspaId = None
        self._TemplateName = None
        self._TemplateId = None
        self._RiskLevelId = None
        self._TemplateDescription = None
        self._RiskIdList = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RiskLevelId(self):
        """修改的风险等级id
        :rtype: int
        """
        return self._RiskLevelId

    @RiskLevelId.setter
    def RiskLevelId(self, RiskLevelId):
        self._RiskLevelId = RiskLevelId

    @property
    def TemplateDescription(self):
        """模板的描述
        :rtype: str
        """
        return self._TemplateDescription

    @TemplateDescription.setter
    def TemplateDescription(self, TemplateDescription):
        self._TemplateDescription = TemplateDescription

    @property
    def RiskIdList(self):
        """脆弱项列表
        :rtype: list of int
        """
        return self._RiskIdList

    @RiskIdList.setter
    def RiskIdList(self, RiskIdList):
        self._RiskIdList = RiskIdList


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateId = params.get("TemplateId")
        self._RiskLevelId = params.get("RiskLevelId")
        self._TemplateDescription = params.get("TemplateDescription")
        self._RiskIdList = params.get("RiskIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAAssessmentRiskTemplateResponse(AbstractModel):
    """ModifyDSPAAssessmentRiskTemplate返回参数结构体

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


class ModifyDSPACOSDiscoveryTaskRequest(AbstractModel):
    """ModifyDSPACOSDiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Name: 任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _Description: 任务描述，最大长度为1024个字符
        :type Description: str
        :param _Enable: 任务开关，0 关闭，1 启用
        :type Enable: int
        :param _GeneralRuleSetEnable: 通用规则集开关；0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _ComplianceGroupIds: 合规组ID列表，最多支持添加5个
        :type ComplianceGroupIds: list of int
        :param _Plan: 执行计划； 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :type Plan: int
        :param _Period: 扫描周期；0单次 1每天 2每周 3每月
        :type Period: int
        :param _TimingStartTime: 任务定时启动时间，格式：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :type TimingStartTime: str
        :param _FileTypes: 待扫描文件类型，用逗号隔开，格式如：[".txt", ".csv", ".log", ".xml",".html", ".json"]。
        :type FileTypes: list of str
        :param _FileSizeLimit: 文件大小上限，单位为KB，如1000, 目前单个文件最大只支持100MB（102400KB）
        :type FileSizeLimit: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        """
        self._DspaId = None
        self._TaskId = None
        self._Name = None
        self._Description = None
        self._Enable = None
        self._GeneralRuleSetEnable = None
        self._ComplianceGroupIds = None
        self._Plan = None
        self._Period = None
        self._TimingStartTime = None
        self._FileTypes = None
        self._FileSizeLimit = None
        self._ResourceRegion = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enable(self):
        """任务开关，0 关闭，1 启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关；0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def ComplianceGroupIds(self):
        """合规组ID列表，最多支持添加5个
        :rtype: list of int
        """
        return self._ComplianceGroupIds

    @ComplianceGroupIds.setter
    def ComplianceGroupIds(self, ComplianceGroupIds):
        self._ComplianceGroupIds = ComplianceGroupIds

    @property
    def Plan(self):
        """执行计划； 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Period(self):
        """扫描周期；0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimingStartTime(self):
        """任务定时启动时间，格式：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def FileTypes(self):
        """待扫描文件类型，用逗号隔开，格式如：[".txt", ".csv", ".log", ".xml",".html", ".json"]。
        :rtype: list of str
        """
        return self._FileTypes

    @FileTypes.setter
    def FileTypes(self, FileTypes):
        self._FileTypes = FileTypes

    @property
    def FileSizeLimit(self):
        """文件大小上限，单位为KB，如1000, 目前单个文件最大只支持100MB（102400KB）
        :rtype: int
        """
        return self._FileSizeLimit

    @FileSizeLimit.setter
    def FileSizeLimit(self, FileSizeLimit):
        self._FileSizeLimit = FileSizeLimit

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Enable = params.get("Enable")
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        self._ComplianceGroupIds = params.get("ComplianceGroupIds")
        self._Plan = params.get("Plan")
        self._Period = params.get("Period")
        self._TimingStartTime = params.get("TimingStartTime")
        self._FileTypes = params.get("FileTypes")
        self._FileSizeLimit = params.get("FileSizeLimit")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPACOSDiscoveryTaskResponse(AbstractModel):
    """ModifyDSPACOSDiscoveryTask返回参数结构体

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


class ModifyDSPACOSTaskResultRequest(AbstractModel):
    """ModifyDSPACOSTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _FileResultId: 文件扫描结果ID
        :type FileResultId: int
        :param _IsSetNonSensitiveFile: 是否设置为非敏感文件
        :type IsSetNonSensitiveFile: bool
        :param _FileName: 文件名
        :type FileName: str
        :param _BucketName: 桶名
        :type BucketName: str
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        """
        self._DspaId = None
        self._ComplianceId = None
        self._FileResultId = None
        self._IsSetNonSensitiveFile = None
        self._FileName = None
        self._BucketName = None
        self._DataSourceId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def FileResultId(self):
        """文件扫描结果ID
        :rtype: int
        """
        return self._FileResultId

    @FileResultId.setter
    def FileResultId(self, FileResultId):
        self._FileResultId = FileResultId

    @property
    def IsSetNonSensitiveFile(self):
        """是否设置为非敏感文件
        :rtype: bool
        """
        return self._IsSetNonSensitiveFile

    @IsSetNonSensitiveFile.setter
    def IsSetNonSensitiveFile(self, IsSetNonSensitiveFile):
        self._IsSetNonSensitiveFile = IsSetNonSensitiveFile

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def BucketName(self):
        """桶名
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceId = params.get("ComplianceId")
        self._FileResultId = params.get("FileResultId")
        self._IsSetNonSensitiveFile = params.get("IsSetNonSensitiveFile")
        self._FileName = params.get("FileName")
        self._BucketName = params.get("BucketName")
        self._DataSourceId = params.get("DataSourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPACOSTaskResultResponse(AbstractModel):
    """ModifyDSPACOSTaskResult返回参数结构体

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


class ModifyDSPACategoryRelationRequest(AbstractModel):
    """ModifyDSPACategoryRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _CategoryId: 当前分类id
        :type CategoryId: int
        :param _MergedCategoryId: 合并到的分类id
        :type MergedCategoryId: int
        :param _ComplianceId: 合规组模板id
        :type ComplianceId: int
        """
        self._DspaId = None
        self._CategoryId = None
        self._MergedCategoryId = None
        self._ComplianceId = None

    @property
    def DspaId(self):
        """dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """当前分类id
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def MergedCategoryId(self):
        """合并到的分类id
        :rtype: int
        """
        return self._MergedCategoryId

    @MergedCategoryId.setter
    def MergedCategoryId(self, MergedCategoryId):
        self._MergedCategoryId = MergedCategoryId

    @property
    def ComplianceId(self):
        """合规组模板id
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._MergedCategoryId = params.get("MergedCategoryId")
        self._ComplianceId = params.get("ComplianceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPACategoryRelationResponse(AbstractModel):
    """ModifyDSPACategoryRelation返回参数结构体

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


class ModifyDSPACategoryRequest(AbstractModel):
    """ModifyDSPACategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _CategoryId: 数据分类ID
        :type CategoryId: int
        :param _Name: 敏感数据分类名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        """
        self._DspaId = None
        self._CategoryId = None
        self._Name = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def CategoryId(self):
        """数据分类ID
        :rtype: int
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Name(self):
        """敏感数据分类名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._CategoryId = params.get("CategoryId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPACategoryResponse(AbstractModel):
    """ModifyDSPACategory返回参数结构体

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


class ModifyDSPAClusterInfoRequest(AbstractModel):
    """ModifyDSPAClusterInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _DspaName: DSPA实例名。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字。
        :type DspaName: str
        :param _DspaDescription: DSPA实例描述信息。最长1024个字符。
        :type DspaDescription: str
        """
        self._DspaId = None
        self._DspaName = None
        self._DspaDescription = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DspaName(self):
        """DSPA实例名。1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字。
        :rtype: str
        """
        return self._DspaName

    @DspaName.setter
    def DspaName(self, DspaName):
        self._DspaName = DspaName

    @property
    def DspaDescription(self):
        """DSPA实例描述信息。最长1024个字符。
        :rtype: str
        """
        return self._DspaDescription

    @DspaDescription.setter
    def DspaDescription(self, DspaDescription):
        self._DspaDescription = DspaDescription


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DspaName = params.get("DspaName")
        self._DspaDescription = params.get("DspaDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAClusterInfoResponse(AbstractModel):
    """ModifyDSPAClusterInfo返回参数结构体

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


class ModifyDSPAComplianceGroupRequest(AbstractModel):
    """ModifyDSPAComplianceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _Name: 合规组名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _Description: 合规组描述，最大长度为1024个字符
        :type Description: str
        :param _ComplianceGroupRules: 合规组规则配置（参数已废弃，请传空数组）
        :type ComplianceGroupRules: list of ComplianceGroupRuleIdInfo
        :param _LevelGroupId: 分级组ID，新增参数，可选参数，默认值为1
        :type LevelGroupId: int
        :param _RuleAlias: 是否开启别名
        :type RuleAlias: bool
        """
        self._DspaId = None
        self._ComplianceGroupId = None
        self._Name = None
        self._Description = None
        self._ComplianceGroupRules = None
        self._LevelGroupId = None
        self._RuleAlias = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def Name(self):
        """合规组名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """合规组描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ComplianceGroupRules(self):
        """合规组规则配置（参数已废弃，请传空数组）
        :rtype: list of ComplianceGroupRuleIdInfo
        """
        return self._ComplianceGroupRules

    @ComplianceGroupRules.setter
    def ComplianceGroupRules(self, ComplianceGroupRules):
        self._ComplianceGroupRules = ComplianceGroupRules

    @property
    def LevelGroupId(self):
        """分级组ID，新增参数，可选参数，默认值为1
        :rtype: int
        """
        return self._LevelGroupId

    @LevelGroupId.setter
    def LevelGroupId(self, LevelGroupId):
        self._LevelGroupId = LevelGroupId

    @property
    def RuleAlias(self):
        """是否开启别名
        :rtype: bool
        """
        return self._RuleAlias

    @RuleAlias.setter
    def RuleAlias(self, RuleAlias):
        self._RuleAlias = RuleAlias


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ComplianceGroupRules") is not None:
            self._ComplianceGroupRules = []
            for item in params.get("ComplianceGroupRules"):
                obj = ComplianceGroupRuleIdInfo()
                obj._deserialize(item)
                self._ComplianceGroupRules.append(obj)
        self._LevelGroupId = params.get("LevelGroupId")
        self._RuleAlias = params.get("RuleAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAComplianceGroupResponse(AbstractModel):
    """ModifyDSPAComplianceGroup返回参数结构体

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


class ModifyDSPADiscoveryRuleRequest(AbstractModel):
    """ModifyDSPADiscoveryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _Name: 规则名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Description: 规则描述，最大长度为1024个字符
        :type Description: str
        :param _RDBRules: RDB类敏感数据识别规则
        :type RDBRules: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskRDBRules`
        :param _COSRules: COS类敏感数据识别规则
        :type COSRules: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskCOSRules`
        :param _Status: 规则状态
        :type Status: int
        """
        self._DspaId = None
        self._Name = None
        self._RuleId = None
        self._Description = None
        self._RDBRules = None
        self._COSRules = None
        self._Status = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def Name(self):
        """规则名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RuleId(self):
        """规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Description(self):
        """规则描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RDBRules(self):
        """RDB类敏感数据识别规则
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskRDBRules`
        """
        return self._RDBRules

    @RDBRules.setter
    def RDBRules(self, RDBRules):
        self._RDBRules = RDBRules

    @property
    def COSRules(self):
        """COS类敏感数据识别规则
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskCOSRules`
        """
        return self._COSRules

    @COSRules.setter
    def COSRules(self, COSRules):
        self._COSRules = COSRules

    @property
    def Status(self):
        """规则状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._Name = params.get("Name")
        self._RuleId = params.get("RuleId")
        self._Description = params.get("Description")
        if params.get("RDBRules") is not None:
            self._RDBRules = ScanTaskRDBRules()
            self._RDBRules._deserialize(params.get("RDBRules"))
        if params.get("COSRules") is not None:
            self._COSRules = ScanTaskCOSRules()
            self._COSRules._deserialize(params.get("COSRules"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPADiscoveryRuleResponse(AbstractModel):
    """ModifyDSPADiscoveryRule返回参数结构体

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


class ModifyDSPADiscoveryTaskRequest(AbstractModel):
    """ModifyDSPADiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _Name: 任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :type Name: str
        :param _Description: 任务描述，最大长度为1024个字符
        :type Description: str
        :param _Enable: 任务开关，0 关闭，1 启用
        :type Enable: int
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        :param _Condition: 用于传入的数据源的条件，目前只支持数据库，所以目前表示数据库的名称，最多添加5个数据库，之间通过逗号分隔
        :type Condition: str
        :param _GeneralRuleSetEnable: 通用规则集开关；0 关闭，1 启用
        :type GeneralRuleSetEnable: int
        :param _ComplianceGroupIds: 合规组ID列表，最多支持添加5个
        :type ComplianceGroupIds: list of int
        :param _Plan: 执行计划； 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :type Plan: int
        :param _Period: 扫描周期；0单次 1每天 2每周 3每月
        :type Period: int
        :param _TimingStartTime: 任务定时启动时间，格式：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :type TimingStartTime: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _DataSourceType: 数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :type DataSourceType: str
        """
        self._DspaId = None
        self._TaskId = None
        self._Name = None
        self._Description = None
        self._Enable = None
        self._DataSourceId = None
        self._Condition = None
        self._GeneralRuleSetEnable = None
        self._ComplianceGroupIds = None
        self._Plan = None
        self._Period = None
        self._TimingStartTime = None
        self._ResourceRegion = None
        self._DataSourceType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        """任务名称，1-60个字符，仅允许输入中文、英文字母、数字、'_'、'-'，并且开头和结尾需为中文、英文字母或者数字，Name不可重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """任务描述，最大长度为1024个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enable(self):
        """任务开关，0 关闭，1 启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DataSourceId(self):
        """数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def Condition(self):
        """用于传入的数据源的条件，目前只支持数据库，所以目前表示数据库的名称，最多添加5个数据库，之间通过逗号分隔
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def GeneralRuleSetEnable(self):
        """通用规则集开关；0 关闭，1 启用
        :rtype: int
        """
        return self._GeneralRuleSetEnable

    @GeneralRuleSetEnable.setter
    def GeneralRuleSetEnable(self, GeneralRuleSetEnable):
        self._GeneralRuleSetEnable = GeneralRuleSetEnable

    @property
    def ComplianceGroupIds(self):
        """合规组ID列表，最多支持添加5个
        :rtype: list of int
        """
        return self._ComplianceGroupIds

    @ComplianceGroupIds.setter
    def ComplianceGroupIds(self, ComplianceGroupIds):
        self._ComplianceGroupIds = ComplianceGroupIds

    @property
    def Plan(self):
        """执行计划； 0立即 1定时，选择“立即”时，扫描周期只能选择单次
        :rtype: int
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

    @property
    def Period(self):
        """扫描周期；0单次 1每天 2每周 3每月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TimingStartTime(self):
        """任务定时启动时间，格式：2006-01-02 15:04:05
当执行计划（Plan字段）为”立即“时，定时启动时间不会生效，此场景下给该字段传值不会被保存。
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DataSourceType(self):
        """数据源类型，可取值如下：
cdb 表示云数据库 MySQL,
dcdb 表示TDSQL MySQL版,
mariadb 表示云数据库 MariaDB,
postgres 表示云数据库 PostgreSQL,
cynosdbpg 表示TDSQL-C PostgreSQL版,
cynosdbmysql 表示TDSQL-C MySQL版,
selfbuilt-db 表示自建数据库
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Enable = params.get("Enable")
        self._DataSourceId = params.get("DataSourceId")
        self._Condition = params.get("Condition")
        self._GeneralRuleSetEnable = params.get("GeneralRuleSetEnable")
        self._ComplianceGroupIds = params.get("ComplianceGroupIds")
        self._Plan = params.get("Plan")
        self._Period = params.get("Period")
        self._TimingStartTime = params.get("TimingStartTime")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DataSourceType = params.get("DataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPADiscoveryTaskResponse(AbstractModel):
    """ModifyDSPADiscoveryTask返回参数结构体

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


class ModifyDSPAESTaskResultRequest(AbstractModel):
    """ModifyDSPAESTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _FieldResultId: 字段扫描结果ID
        :type FieldResultId: int
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _IsSetNonSensitiveField: 是否设置为非敏感字段
        :type IsSetNonSensitiveField: bool
        :param _DestRuleId: 调整后新的规则ID
        :type DestRuleId: int
        :param _DestCategoryId: 调整后新的分类ID
        :type DestCategoryId: int
        :param _DestLevelId: 调整后新的分级ID
        :type DestLevelId: int
        :param _SrcRuleId: 调整前的规则id（系统识别的id）
        :type SrcRuleId: int
        :param _SrcCategoryId: 调整前的规则id（系统识别的id）
        :type SrcCategoryId: int
        :param _SrcLevelId: 调整前的等级id
        :type SrcLevelId: int
        :param _IdentifyType: 0系统识别，1人工打标
        :type IdentifyType: int
        """
        self._DspaId = None
        self._FieldResultId = None
        self._ComplianceId = None
        self._IsSetNonSensitiveField = None
        self._DestRuleId = None
        self._DestCategoryId = None
        self._DestLevelId = None
        self._SrcRuleId = None
        self._SrcCategoryId = None
        self._SrcLevelId = None
        self._IdentifyType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def FieldResultId(self):
        """字段扫描结果ID
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def IsSetNonSensitiveField(self):
        """是否设置为非敏感字段
        :rtype: bool
        """
        return self._IsSetNonSensitiveField

    @IsSetNonSensitiveField.setter
    def IsSetNonSensitiveField(self, IsSetNonSensitiveField):
        self._IsSetNonSensitiveField = IsSetNonSensitiveField

    @property
    def DestRuleId(self):
        """调整后新的规则ID
        :rtype: int
        """
        return self._DestRuleId

    @DestRuleId.setter
    def DestRuleId(self, DestRuleId):
        self._DestRuleId = DestRuleId

    @property
    def DestCategoryId(self):
        """调整后新的分类ID
        :rtype: int
        """
        return self._DestCategoryId

    @DestCategoryId.setter
    def DestCategoryId(self, DestCategoryId):
        self._DestCategoryId = DestCategoryId

    @property
    def DestLevelId(self):
        """调整后新的分级ID
        :rtype: int
        """
        return self._DestLevelId

    @DestLevelId.setter
    def DestLevelId(self, DestLevelId):
        self._DestLevelId = DestLevelId

    @property
    def SrcRuleId(self):
        """调整前的规则id（系统识别的id）
        :rtype: int
        """
        return self._SrcRuleId

    @SrcRuleId.setter
    def SrcRuleId(self, SrcRuleId):
        self._SrcRuleId = SrcRuleId

    @property
    def SrcCategoryId(self):
        """调整前的规则id（系统识别的id）
        :rtype: int
        """
        return self._SrcCategoryId

    @SrcCategoryId.setter
    def SrcCategoryId(self, SrcCategoryId):
        self._SrcCategoryId = SrcCategoryId

    @property
    def SrcLevelId(self):
        """调整前的等级id
        :rtype: int
        """
        return self._SrcLevelId

    @SrcLevelId.setter
    def SrcLevelId(self, SrcLevelId):
        self._SrcLevelId = SrcLevelId

    @property
    def IdentifyType(self):
        """0系统识别，1人工打标
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._FieldResultId = params.get("FieldResultId")
        self._ComplianceId = params.get("ComplianceId")
        self._IsSetNonSensitiveField = params.get("IsSetNonSensitiveField")
        self._DestRuleId = params.get("DestRuleId")
        self._DestCategoryId = params.get("DestCategoryId")
        self._DestLevelId = params.get("DestLevelId")
        self._SrcRuleId = params.get("SrcRuleId")
        self._SrcCategoryId = params.get("SrcCategoryId")
        self._SrcLevelId = params.get("SrcLevelId")
        self._IdentifyType = params.get("IdentifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPAESTaskResultResponse(AbstractModel):
    """ModifyDSPAESTaskResult返回参数结构体

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


class ModifyDSPATaskResultRequest(AbstractModel):
    """ModifyDSPATaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _FieldResultId: 字段扫描结果ID
        :type FieldResultId: int
        :param _ComplianceId: 合规组ID
        :type ComplianceId: int
        :param _IsSetNonSensitiveField: 是否设置为非敏感字段
        :type IsSetNonSensitiveField: bool
        :param _DestRuleId: 调整后新的规则ID
        :type DestRuleId: int
        :param _DestCategoryId: 调整后新的分类ID
        :type DestCategoryId: int
        :param _DestLevelId: 调整后新的分级ID
        :type DestLevelId: int
        :param _SrcRuleId: 调整前的规则ID

        :type SrcRuleId: int
        :param _SrcCategoryId: 调整之前的分类id
        :type SrcCategoryId: int
        :param _SrcLevelId: 调整之前的分级id
        :type SrcLevelId: int
        :param _IdentifyType: 识别方式
0-系统识别，1-人工打标
        :type IdentifyType: int
        """
        self._DspaId = None
        self._FieldResultId = None
        self._ComplianceId = None
        self._IsSetNonSensitiveField = None
        self._DestRuleId = None
        self._DestCategoryId = None
        self._DestLevelId = None
        self._SrcRuleId = None
        self._SrcCategoryId = None
        self._SrcLevelId = None
        self._IdentifyType = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def FieldResultId(self):
        """字段扫描结果ID
        :rtype: int
        """
        return self._FieldResultId

    @FieldResultId.setter
    def FieldResultId(self, FieldResultId):
        self._FieldResultId = FieldResultId

    @property
    def ComplianceId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceId

    @ComplianceId.setter
    def ComplianceId(self, ComplianceId):
        self._ComplianceId = ComplianceId

    @property
    def IsSetNonSensitiveField(self):
        """是否设置为非敏感字段
        :rtype: bool
        """
        return self._IsSetNonSensitiveField

    @IsSetNonSensitiveField.setter
    def IsSetNonSensitiveField(self, IsSetNonSensitiveField):
        self._IsSetNonSensitiveField = IsSetNonSensitiveField

    @property
    def DestRuleId(self):
        """调整后新的规则ID
        :rtype: int
        """
        return self._DestRuleId

    @DestRuleId.setter
    def DestRuleId(self, DestRuleId):
        self._DestRuleId = DestRuleId

    @property
    def DestCategoryId(self):
        """调整后新的分类ID
        :rtype: int
        """
        return self._DestCategoryId

    @DestCategoryId.setter
    def DestCategoryId(self, DestCategoryId):
        self._DestCategoryId = DestCategoryId

    @property
    def DestLevelId(self):
        """调整后新的分级ID
        :rtype: int
        """
        return self._DestLevelId

    @DestLevelId.setter
    def DestLevelId(self, DestLevelId):
        self._DestLevelId = DestLevelId

    @property
    def SrcRuleId(self):
        """调整前的规则ID

        :rtype: int
        """
        return self._SrcRuleId

    @SrcRuleId.setter
    def SrcRuleId(self, SrcRuleId):
        self._SrcRuleId = SrcRuleId

    @property
    def SrcCategoryId(self):
        """调整之前的分类id
        :rtype: int
        """
        return self._SrcCategoryId

    @SrcCategoryId.setter
    def SrcCategoryId(self, SrcCategoryId):
        self._SrcCategoryId = SrcCategoryId

    @property
    def SrcLevelId(self):
        """调整之前的分级id
        :rtype: int
        """
        return self._SrcLevelId

    @SrcLevelId.setter
    def SrcLevelId(self, SrcLevelId):
        self._SrcLevelId = SrcLevelId

    @property
    def IdentifyType(self):
        """识别方式
0-系统识别，1-人工打标
        :rtype: int
        """
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._FieldResultId = params.get("FieldResultId")
        self._ComplianceId = params.get("ComplianceId")
        self._IsSetNonSensitiveField = params.get("IsSetNonSensitiveField")
        self._DestRuleId = params.get("DestRuleId")
        self._DestCategoryId = params.get("DestCategoryId")
        self._DestLevelId = params.get("DestLevelId")
        self._SrcRuleId = params.get("SrcRuleId")
        self._SrcCategoryId = params.get("SrcCategoryId")
        self._SrcLevelId = params.get("SrcLevelId")
        self._IdentifyType = params.get("IdentifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDSPATaskResultResponse(AbstractModel):
    """ModifyDSPATaskResult返回参数结构体

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


class MongoAsset(AbstractModel):
    """mongo的资产统计结果

    """

    def __init__(self):
        r"""
        :param _DbNums: DB总数量
        :type DbNums: int
        :param _SensitiveDbNums: 敏感DB数量
        :type SensitiveDbNums: int
        :param _ColNums: 集合数量
        :type ColNums: int
        :param _SensitiveColNums: 敏感集合的数量
        :type SensitiveColNums: int
        :param _FieldNums: 字段数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感的字段数量
        :type SensitiveFieldNums: int
        """
        self._DbNums = None
        self._SensitiveDbNums = None
        self._ColNums = None
        self._SensitiveColNums = None
        self._FieldNums = None
        self._SensitiveFieldNums = None

    @property
    def DbNums(self):
        """DB总数量
        :rtype: int
        """
        return self._DbNums

    @DbNums.setter
    def DbNums(self, DbNums):
        self._DbNums = DbNums

    @property
    def SensitiveDbNums(self):
        """敏感DB数量
        :rtype: int
        """
        return self._SensitiveDbNums

    @SensitiveDbNums.setter
    def SensitiveDbNums(self, SensitiveDbNums):
        self._SensitiveDbNums = SensitiveDbNums

    @property
    def ColNums(self):
        """集合数量
        :rtype: int
        """
        return self._ColNums

    @ColNums.setter
    def ColNums(self, ColNums):
        self._ColNums = ColNums

    @property
    def SensitiveColNums(self):
        """敏感集合的数量
        :rtype: int
        """
        return self._SensitiveColNums

    @SensitiveColNums.setter
    def SensitiveColNums(self, SensitiveColNums):
        self._SensitiveColNums = SensitiveColNums

    @property
    def FieldNums(self):
        """字段数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感的字段数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums


    def _deserialize(self, params):
        self._DbNums = params.get("DbNums")
        self._SensitiveDbNums = params.get("SensitiveDbNums")
        self._ColNums = params.get("ColNums")
        self._SensitiveColNums = params.get("SensitiveColNums")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MongoAssetDBDetail(AbstractModel):
    """mongo敏感资产详情列表

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DdName: 数据库名称
        :type DdName: str
        :param _DataType: 数据库类型
        :type DataType: str
        :param _ColNums: 集合的数量
        :type ColNums: int
        :param _SensitiveColNums: 敏感集合数量
        :type SensitiveColNums: int
        :param _FieldNums: 字段的数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感字段的数量
        :type SensitiveFieldNums: int
        :param _DistributionData: 敏感数据分布
        :type DistributionData: list of Note
        """
        self._DataSourceId = None
        self._DdName = None
        self._DataType = None
        self._ColNums = None
        self._SensitiveColNums = None
        self._FieldNums = None
        self._SensitiveFieldNums = None
        self._DistributionData = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DdName(self):
        """数据库名称
        :rtype: str
        """
        return self._DdName

    @DdName.setter
    def DdName(self, DdName):
        self._DdName = DdName

    @property
    def DataType(self):
        """数据库类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def ColNums(self):
        """集合的数量
        :rtype: int
        """
        return self._ColNums

    @ColNums.setter
    def ColNums(self, ColNums):
        self._ColNums = ColNums

    @property
    def SensitiveColNums(self):
        """敏感集合数量
        :rtype: int
        """
        return self._SensitiveColNums

    @SensitiveColNums.setter
    def SensitiveColNums(self, SensitiveColNums):
        self._SensitiveColNums = SensitiveColNums

    @property
    def FieldNums(self):
        """字段的数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感字段的数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums

    @property
    def DistributionData(self):
        """敏感数据分布
        :rtype: list of Note
        """
        return self._DistributionData

    @DistributionData.setter
    def DistributionData(self, DistributionData):
        self._DistributionData = DistributionData


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DdName = params.get("DdName")
        self._DataType = params.get("DataType")
        self._ColNums = params.get("ColNums")
        self._SensitiveColNums = params.get("SensitiveColNums")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        if params.get("DistributionData") is not None:
            self._DistributionData = []
            for item in params.get("DistributionData"):
                obj = Note()
                obj._deserialize(item)
                self._DistributionData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NOSQLInstance(AbstractModel):
    """NOSQL类型的数据源实例

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DataSourceType: cdb, dcdb, mariadb, postgres, cynosdbpg, cynosdbmysql, cos, mysql_like_proto, postgre_like_proto,mongodb
        :type DataSourceType: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _DiscoveryTaskId: 根据实例创建的敏感数据识别扫描任务Id
        :type DiscoveryTaskId: int
        :param _DiscoveryTaskInstanceID: 敏感数据识别任务实例id
        :type DiscoveryTaskInstanceID: int
        """
        self._DataSourceId = None
        self._DataSourceType = None
        self._ResourceRegion = None
        self._DiscoveryTaskId = None
        self._DiscoveryTaskInstanceID = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceType(self):
        """cdb, dcdb, mariadb, postgres, cynosdbpg, cynosdbmysql, cos, mysql_like_proto, postgre_like_proto,mongodb
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DiscoveryTaskId(self):
        """根据实例创建的敏感数据识别扫描任务Id
        :rtype: int
        """
        return self._DiscoveryTaskId

    @DiscoveryTaskId.setter
    def DiscoveryTaskId(self, DiscoveryTaskId):
        self._DiscoveryTaskId = DiscoveryTaskId

    @property
    def DiscoveryTaskInstanceID(self):
        """敏感数据识别任务实例id
        :rtype: int
        """
        return self._DiscoveryTaskInstanceID

    @DiscoveryTaskInstanceID.setter
    def DiscoveryTaskInstanceID(self, DiscoveryTaskInstanceID):
        self._DiscoveryTaskInstanceID = DiscoveryTaskInstanceID


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceType = params.get("DataSourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._DiscoveryTaskId = params.get("DiscoveryTaskId")
        self._DiscoveryTaskInstanceID = params.get("DiscoveryTaskInstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Note(AbstractModel):
    """数据资产报告-各种key-value的展示数据结构

    """

    def __init__(self):
        r"""
        :param _Key: 通用key，例如分类名称
        :type Key: str
        :param _Value: 通用value，例如分类个数
        :type Value: int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """通用key，例如分类名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """通用value，例如分类个数
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeRisk(AbstractModel):
    """权限风险详情

    """

    def __init__(self):
        r"""
        :param _AccountName: 账户名
        :type AccountName: list of str
        :param _TableName: 表名称
        :type TableName: str
        :param _Description: 说明
        :type Description: str
        """
        self._AccountName = None
        self._TableName = None
        self._Description = None

    @property
    def AccountName(self):
        """账户名
        :rtype: list of str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def TableName(self):
        """表名称
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Description(self):
        """说明
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._TableName = params.get("TableName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessHistory(AbstractModel):
    """处理历史

    """

    def __init__(self):
        r"""
        :param _Time: 处理时间
        :type Time: str
        :param _Status: 状态
        :type Status: int
        :param _Handler: 处理人
        :type Handler: str
        :param _Note: 备注
        :type Note: str
        """
        self._Time = None
        self._Status = None
        self._Handler = None
        self._Note = None

    @property
    def Time(self):
        """处理时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        """状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Handler(self):
        """处理人
        :rtype: str
        """
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        self._Handler = params.get("Handler")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDSPAMetaResourceDbListRequest(AbstractModel):
    """QueryDSPAMetaResourceDbList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceId: 数据库实例ID。
        :type ResourceId: str
        :param _ResourceRegion: 数据库实例所在地域。
        :type ResourceRegion: str
        :param _MetaType: 数据库实例类型。
        :type MetaType: str
        """
        self._DspaId = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._MetaType = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceId(self):
        """数据库实例ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """数据库实例所在地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def MetaType(self):
        """数据库实例类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._MetaType = params.get("MetaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDSPAMetaResourceDbListResponse(AbstractModel):
    """QueryDSPAMetaResourceDbList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DbRelationStatusItems: 数据库实例DB列表的查询结果。
        :type DbRelationStatusItems: list of DbRelationStatusItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DbRelationStatusItems = None
        self._RequestId = None

    @property
    def DbRelationStatusItems(self):
        """数据库实例DB列表的查询结果。
        :rtype: list of DbRelationStatusItem
        """
        return self._DbRelationStatusItems

    @DbRelationStatusItems.setter
    def DbRelationStatusItems(self, DbRelationStatusItems):
        self._DbRelationStatusItems = DbRelationStatusItems

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
        if params.get("DbRelationStatusItems") is not None:
            self._DbRelationStatusItems = []
            for item in params.get("DbRelationStatusItems"):
                obj = DbRelationStatusItem()
                obj._deserialize(item)
                self._DbRelationStatusItems.append(obj)
        self._RequestId = params.get("RequestId")


class QueryResourceDbBindStatusRequest(AbstractModel):
    """QueryResourceDbBindStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceId: 资源ID。
        :type ResourceId: str
        :param _ResourceRegion: 资源所在地域。
        :type ResourceRegion: str
        :param _MetaType: 资源类型。
        :type MetaType: str
        """
        self._DspaId = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._MetaType = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceId(self):
        """资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """资源所在地域。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def MetaType(self):
        """资源类型。
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._MetaType = params.get("MetaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceDbBindStatusResponse(AbstractModel):
    """QueryResourceDbBindStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindDbNums: 绑定DB数量。
        :type BindDbNums: int
        :param _UnbindDbNums: 未绑定DB数量。
        :type UnbindDbNums: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindDbNums = None
        self._UnbindDbNums = None
        self._RequestId = None

    @property
    def BindDbNums(self):
        """绑定DB数量。
        :rtype: int
        """
        return self._BindDbNums

    @BindDbNums.setter
    def BindDbNums(self, BindDbNums):
        self._BindDbNums = BindDbNums

    @property
    def UnbindDbNums(self):
        """未绑定DB数量。
        :rtype: int
        """
        return self._UnbindDbNums

    @UnbindDbNums.setter
    def UnbindDbNums(self, UnbindDbNums):
        self._UnbindDbNums = UnbindDbNums

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
        self._BindDbNums = params.get("BindDbNums")
        self._UnbindDbNums = params.get("UnbindDbNums")
        self._RequestId = params.get("RequestId")


class RDBAsset(AbstractModel):
    """rdb的资产统计结果

    """

    def __init__(self):
        r"""
        :param _DbNums: DB总数量
        :type DbNums: int
        :param _SensitiveDbNums: 敏感DB数量
        :type SensitiveDbNums: int
        :param _TableNums: 表数量
        :type TableNums: int
        :param _SensitiveTableNums: 敏感表的数量
        :type SensitiveTableNums: int
        :param _FieldNums: 字段数量
        :type FieldNums: int
        :param _SensitiveFieldNums: 敏感的字段数量
        :type SensitiveFieldNums: int
        """
        self._DbNums = None
        self._SensitiveDbNums = None
        self._TableNums = None
        self._SensitiveTableNums = None
        self._FieldNums = None
        self._SensitiveFieldNums = None

    @property
    def DbNums(self):
        """DB总数量
        :rtype: int
        """
        return self._DbNums

    @DbNums.setter
    def DbNums(self, DbNums):
        self._DbNums = DbNums

    @property
    def SensitiveDbNums(self):
        """敏感DB数量
        :rtype: int
        """
        return self._SensitiveDbNums

    @SensitiveDbNums.setter
    def SensitiveDbNums(self, SensitiveDbNums):
        self._SensitiveDbNums = SensitiveDbNums

    @property
    def TableNums(self):
        """表数量
        :rtype: int
        """
        return self._TableNums

    @TableNums.setter
    def TableNums(self, TableNums):
        self._TableNums = TableNums

    @property
    def SensitiveTableNums(self):
        """敏感表的数量
        :rtype: int
        """
        return self._SensitiveTableNums

    @SensitiveTableNums.setter
    def SensitiveTableNums(self, SensitiveTableNums):
        self._SensitiveTableNums = SensitiveTableNums

    @property
    def FieldNums(self):
        """字段数量
        :rtype: int
        """
        return self._FieldNums

    @FieldNums.setter
    def FieldNums(self, FieldNums):
        self._FieldNums = FieldNums

    @property
    def SensitiveFieldNums(self):
        """敏感的字段数量
        :rtype: int
        """
        return self._SensitiveFieldNums

    @SensitiveFieldNums.setter
    def SensitiveFieldNums(self, SensitiveFieldNums):
        self._SensitiveFieldNums = SensitiveFieldNums


    def _deserialize(self, params):
        self._DbNums = params.get("DbNums")
        self._SensitiveDbNums = params.get("SensitiveDbNums")
        self._TableNums = params.get("TableNums")
        self._SensitiveTableNums = params.get("SensitiveTableNums")
        self._FieldNums = params.get("FieldNums")
        self._SensitiveFieldNums = params.get("SensitiveFieldNums")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RDBInstance(AbstractModel):
    """RDB实例信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源Id
        :type DataSourceId: str
        :param _DataSourceType: cdb, dcdb, mariadb, postgres, cynosdbpg, cynosdbmysql, cos, mysql_like_proto, postgre_like_proto
        :type DataSourceType: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _DBs: 若未来扩展到DBName粒度，可采用
        :type DBs: list of DBStatements
        """
        self._DataSourceId = None
        self._DataSourceType = None
        self._ResourceRegion = None
        self._DBs = None

    @property
    def DataSourceId(self):
        """数据源Id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceType(self):
        """cdb, dcdb, mariadb, postgres, cynosdbpg, cynosdbmysql, cos, mysql_like_proto, postgre_like_proto
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def ResourceRegion(self):
        """资源所在地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def DBs(self):
        """若未来扩展到DBName粒度，可采用
        :rtype: list of DBStatements
        """
        return self._DBs

    @DBs.setter
    def DBs(self, DBs):
        self._DBs = DBs


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceType = params.get("DataSourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        if params.get("DBs") is not None:
            self._DBs = []
            for item in params.get("DBs"):
                obj = DBStatements()
                obj._deserialize(item)
                self._DBs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportInfo(AbstractModel):
    """报表信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务id
        :type Id: int
        :param _ReportName: 报告名称
        :type ReportName: str
        :param _ReportType: 报告类型（AssetSorting:资产梳理）
        :type ReportType: str
        :param _ReportPeriod: 报告周期（0单次 1每天 2每周 3每月）
        :type ReportPeriod: int
        :param _ReportPlan: 执行计划 （0:单次报告 1:定时报告）
        :type ReportPlan: int
        :param _ReportStatus: 报告导出状态（Success 成功, Failed 失败, InProgress 进行中）
        :type ReportStatus: str
        :param _TimingStartTime: 任务下次启动时间
        :type TimingStartTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _FinishedTime: 完成时间
        :type FinishedTime: str
        :param _SubUin: 子账号uin
        :type SubUin: str
        :param _FailedMessage: 失败信息
        :type FailedMessage: str
        :param _Enable: 是否启用（0：否 1：是）
        :type Enable: int
        :param _ComplianceName: 识别模板名称
        :type ComplianceName: str
        :param _ProgressPercent: 进度百分比
        :type ProgressPercent: int
        :param _ReportTemplateName: 报告模版名称
        :type ReportTemplateName: str
        """
        self._Id = None
        self._ReportName = None
        self._ReportType = None
        self._ReportPeriod = None
        self._ReportPlan = None
        self._ReportStatus = None
        self._TimingStartTime = None
        self._CreateTime = None
        self._FinishedTime = None
        self._SubUin = None
        self._FailedMessage = None
        self._Enable = None
        self._ComplianceName = None
        self._ProgressPercent = None
        self._ReportTemplateName = None

    @property
    def Id(self):
        """任务id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ReportName(self):
        """报告名称
        :rtype: str
        """
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def ReportType(self):
        """报告类型（AssetSorting:资产梳理）
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ReportPeriod(self):
        """报告周期（0单次 1每天 2每周 3每月）
        :rtype: int
        """
        return self._ReportPeriod

    @ReportPeriod.setter
    def ReportPeriod(self, ReportPeriod):
        self._ReportPeriod = ReportPeriod

    @property
    def ReportPlan(self):
        """执行计划 （0:单次报告 1:定时报告）
        :rtype: int
        """
        return self._ReportPlan

    @ReportPlan.setter
    def ReportPlan(self, ReportPlan):
        self._ReportPlan = ReportPlan

    @property
    def ReportStatus(self):
        """报告导出状态（Success 成功, Failed 失败, InProgress 进行中）
        :rtype: str
        """
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def TimingStartTime(self):
        """任务下次启动时间
        :rtype: str
        """
        return self._TimingStartTime

    @TimingStartTime.setter
    def TimingStartTime(self, TimingStartTime):
        self._TimingStartTime = TimingStartTime

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FinishedTime(self):
        """完成时间
        :rtype: str
        """
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def SubUin(self):
        """子账号uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def FailedMessage(self):
        """失败信息
        :rtype: str
        """
        return self._FailedMessage

    @FailedMessage.setter
    def FailedMessage(self, FailedMessage):
        self._FailedMessage = FailedMessage

    @property
    def Enable(self):
        """是否启用（0：否 1：是）
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ComplianceName(self):
        """识别模板名称
        :rtype: str
        """
        return self._ComplianceName

    @ComplianceName.setter
    def ComplianceName(self, ComplianceName):
        self._ComplianceName = ComplianceName

    @property
    def ProgressPercent(self):
        """进度百分比
        :rtype: int
        """
        return self._ProgressPercent

    @ProgressPercent.setter
    def ProgressPercent(self, ProgressPercent):
        self._ProgressPercent = ProgressPercent

    @property
    def ReportTemplateName(self):
        """报告模版名称
        :rtype: str
        """
        return self._ReportTemplateName

    @ReportTemplateName.setter
    def ReportTemplateName(self, ReportTemplateName):
        self._ReportTemplateName = ReportTemplateName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ReportName = params.get("ReportName")
        self._ReportType = params.get("ReportType")
        self._ReportPeriod = params.get("ReportPeriod")
        self._ReportPlan = params.get("ReportPlan")
        self._ReportStatus = params.get("ReportStatus")
        self._TimingStartTime = params.get("TimingStartTime")
        self._CreateTime = params.get("CreateTime")
        self._FinishedTime = params.get("FinishedTime")
        self._SubUin = params.get("SubUin")
        self._FailedMessage = params.get("FailedMessage")
        self._Enable = params.get("Enable")
        self._ComplianceName = params.get("ComplianceName")
        self._ProgressPercent = params.get("ProgressPercent")
        self._ReportTemplateName = params.get("ReportTemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDSPAAssessmentTaskRequest(AbstractModel):
    """RestartDSPAAssessmentTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例Id，格式“dspa-xxxxxxxx”
        :type DspaId: str
        :param _TaskId: 评估任务Id，格式“task-xxxxxxxx”
        :type TaskId: str
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例Id，格式“dspa-xxxxxxxx”
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """评估任务Id，格式“task-xxxxxxxx”
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDSPAAssessmentTaskResponse(AbstractModel):
    """RestartDSPAAssessmentTask返回参数结构体

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


class RiskCountInfo(AbstractModel):
    """待处理风险项数量信息

    """

    def __init__(self):
        r"""
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _Count: 该等级风险项数量
        :type Count: int
        :param _RiskLevelName: 风险等级名称
        :type RiskLevelName: str
        """
        self._RiskLevel = None
        self._Count = None
        self._RiskLevelName = None

    @property
    def RiskLevel(self):
        """风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Count(self):
        """该等级风险项数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RiskLevelName(self):
        """风险等级名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName


    def _deserialize(self, params):
        self._RiskLevel = params.get("RiskLevel")
        self._Count = params.get("Count")
        self._RiskLevelName = params.get("RiskLevelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDealedTrendItem(AbstractModel):
    """风险趋势项

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _Unhandled: 未解决数量
        :type Unhandled: int
        :param _Handled: 已解决数量
        :type Handled: int
        :param _NewDiscoveryHandled: 新发现
        :type NewDiscoveryHandled: int
        """
        self._Date = None
        self._Unhandled = None
        self._Handled = None
        self._NewDiscoveryHandled = None

    @property
    def Date(self):
        """日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Unhandled(self):
        """未解决数量
        :rtype: int
        """
        return self._Unhandled

    @Unhandled.setter
    def Unhandled(self, Unhandled):
        self._Unhandled = Unhandled

    @property
    def Handled(self):
        """已解决数量
        :rtype: int
        """
        return self._Handled

    @Handled.setter
    def Handled(self, Handled):
        self._Handled = Handled

    @property
    def NewDiscoveryHandled(self):
        """新发现
        :rtype: int
        """
        return self._NewDiscoveryHandled

    @NewDiscoveryHandled.setter
    def NewDiscoveryHandled(self, NewDiscoveryHandled):
        self._NewDiscoveryHandled = NewDiscoveryHandled


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Unhandled = params.get("Unhandled")
        self._Handled = params.get("Handled")
        self._NewDiscoveryHandled = params.get("NewDiscoveryHandled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskItem(AbstractModel):
    """风险TOP5统计项

    """

    def __init__(self):
        r"""
        :param _ItemName: 名称
        :type ItemName: str
        :param _RiskNum: 风险数量
        :type RiskNum: int
        """
        self._ItemName = None
        self._RiskNum = None

    @property
    def ItemName(self):
        """名称
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def RiskNum(self):
        """风险数量
        :rtype: int
        """
        return self._RiskNum

    @RiskNum.setter
    def RiskNum(self, RiskNum):
        self._RiskNum = RiskNum


    def _deserialize(self, params):
        self._ItemName = params.get("ItemName")
        self._RiskNum = params.get("RiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskItemInfo(AbstractModel):
    """最新的风险详情信息数据

    """

    def __init__(self):
        r"""
        :param _Id: 最新风险项id
        :type Id: int
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _DataSourceName: 数据源名称
        :type DataSourceName: str
        :param _DataSourceType: 数据源类型
        :type DataSourceType: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _RiskName: 风险项
        :type RiskName: str
        :param _RiskLevel: 风险级别
        :type RiskLevel: str
        :param _RiskDescription: 风险描述
        :type RiskDescription: str
        :param _SuggestAction: 建议措施
        :type SuggestAction: str
        :param _SecurityProduct: 安全产品（可能有多个）
        :type SecurityProduct: list of SecurityProduct
        :param _Status: 状态(waiting:待处理，processing:处理中，finished:已处理，ignored:已忽略)
        :type Status: int
        :param _ScanTime: 扫描时间
        :type ScanTime: str
        :param _LastProcessTime: 最后处置时间
        :type LastProcessTime: str
        :param _IdentifyComplianceId: 分类分级合规组Id
        :type IdentifyComplianceId: int
        :param _ItemSubType: 类型
        :type ItemSubType: str
        :param _RiskSide: 风险面
        :type RiskSide: str
        :param _APIRiskLinkURL: API安全风险链接
        :type APIRiskLinkURL: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._Id = None
        self._DataSourceId = None
        self._DataSourceName = None
        self._DataSourceType = None
        self._ResourceRegion = None
        self._AssetName = None
        self._RiskType = None
        self._RiskName = None
        self._RiskLevel = None
        self._RiskDescription = None
        self._SuggestAction = None
        self._SecurityProduct = None
        self._Status = None
        self._ScanTime = None
        self._LastProcessTime = None
        self._IdentifyComplianceId = None
        self._ItemSubType = None
        self._RiskSide = None
        self._APIRiskLinkURL = None
        self._Remark = None

    @property
    def Id(self):
        """最新风险项id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def DataSourceName(self):
        """数据源名称
        :rtype: str
        """
        return self._DataSourceName

    @DataSourceName.setter
    def DataSourceName(self, DataSourceName):
        self._DataSourceName = DataSourceName

    @property
    def DataSourceType(self):
        """数据源类型
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def ResourceRegion(self):
        """资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def AssetName(self):
        """资产名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def RiskType(self):
        """风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def RiskName(self):
        """风险项
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskLevel(self):
        """风险级别
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskDescription(self):
        """风险描述
        :rtype: str
        """
        return self._RiskDescription

    @RiskDescription.setter
    def RiskDescription(self, RiskDescription):
        self._RiskDescription = RiskDescription

    @property
    def SuggestAction(self):
        """建议措施
        :rtype: str
        """
        return self._SuggestAction

    @SuggestAction.setter
    def SuggestAction(self, SuggestAction):
        self._SuggestAction = SuggestAction

    @property
    def SecurityProduct(self):
        """安全产品（可能有多个）
        :rtype: list of SecurityProduct
        """
        return self._SecurityProduct

    @SecurityProduct.setter
    def SecurityProduct(self, SecurityProduct):
        self._SecurityProduct = SecurityProduct

    @property
    def Status(self):
        """状态(waiting:待处理，processing:处理中，finished:已处理，ignored:已忽略)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScanTime(self):
        """扫描时间
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def LastProcessTime(self):
        """最后处置时间
        :rtype: str
        """
        return self._LastProcessTime

    @LastProcessTime.setter
    def LastProcessTime(self, LastProcessTime):
        self._LastProcessTime = LastProcessTime

    @property
    def IdentifyComplianceId(self):
        """分类分级合规组Id
        :rtype: int
        """
        return self._IdentifyComplianceId

    @IdentifyComplianceId.setter
    def IdentifyComplianceId(self, IdentifyComplianceId):
        self._IdentifyComplianceId = IdentifyComplianceId

    @property
    def ItemSubType(self):
        """类型
        :rtype: str
        """
        return self._ItemSubType

    @ItemSubType.setter
    def ItemSubType(self, ItemSubType):
        self._ItemSubType = ItemSubType

    @property
    def RiskSide(self):
        """风险面
        :rtype: str
        """
        return self._RiskSide

    @RiskSide.setter
    def RiskSide(self, RiskSide):
        self._RiskSide = RiskSide

    @property
    def APIRiskLinkURL(self):
        """API安全风险链接
        :rtype: str
        """
        return self._APIRiskLinkURL

    @APIRiskLinkURL.setter
    def APIRiskLinkURL(self, APIRiskLinkURL):
        self._APIRiskLinkURL = APIRiskLinkURL

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DataSourceId = params.get("DataSourceId")
        self._DataSourceName = params.get("DataSourceName")
        self._DataSourceType = params.get("DataSourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._AssetName = params.get("AssetName")
        self._RiskType = params.get("RiskType")
        self._RiskName = params.get("RiskName")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskDescription = params.get("RiskDescription")
        self._SuggestAction = params.get("SuggestAction")
        if params.get("SecurityProduct") is not None:
            self._SecurityProduct = []
            for item in params.get("SecurityProduct"):
                obj = SecurityProduct()
                obj._deserialize(item)
                self._SecurityProduct.append(obj)
        self._Status = params.get("Status")
        self._ScanTime = params.get("ScanTime")
        self._LastProcessTime = params.get("LastProcessTime")
        self._IdentifyComplianceId = params.get("IdentifyComplianceId")
        self._ItemSubType = params.get("ItemSubType")
        self._RiskSide = params.get("RiskSide")
        self._APIRiskLinkURL = params.get("APIRiskLinkURL")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskLevelMatrix(AbstractModel):
    """风险级别详情的矩阵

    """

    def __init__(self):
        r"""
        :param _Id: 存储id
        :type Id: int
        :param _SensitiveLevelId: 分类分级levelID
        :type SensitiveLevelId: int
        :param _SensitiveLevelName: 分类分级名称
        :type SensitiveLevelName: str
        :param _VulnerabilityLevel: 漏洞级别
        :type VulnerabilityLevel: str
        :param _RiskLevel: 风险级别
        :type RiskLevel: str
        """
        self._Id = None
        self._SensitiveLevelId = None
        self._SensitiveLevelName = None
        self._VulnerabilityLevel = None
        self._RiskLevel = None

    @property
    def Id(self):
        """存储id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SensitiveLevelId(self):
        """分类分级levelID
        :rtype: int
        """
        return self._SensitiveLevelId

    @SensitiveLevelId.setter
    def SensitiveLevelId(self, SensitiveLevelId):
        self._SensitiveLevelId = SensitiveLevelId

    @property
    def SensitiveLevelName(self):
        """分类分级名称
        :rtype: str
        """
        return self._SensitiveLevelName

    @SensitiveLevelName.setter
    def SensitiveLevelName(self, SensitiveLevelName):
        self._SensitiveLevelName = SensitiveLevelName

    @property
    def VulnerabilityLevel(self):
        """漏洞级别
        :rtype: str
        """
        return self._VulnerabilityLevel

    @VulnerabilityLevel.setter
    def VulnerabilityLevel(self, VulnerabilityLevel):
        self._VulnerabilityLevel = VulnerabilityLevel

    @property
    def RiskLevel(self):
        """风险级别
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SensitiveLevelId = params.get("SensitiveLevelId")
        self._SensitiveLevelName = params.get("SensitiveLevelName")
        self._VulnerabilityLevel = params.get("VulnerabilityLevel")
        self._RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskLevelRisk(AbstractModel):
    """风险等级列表

    """

    def __init__(self):
        r"""
        :param _Id: 风险id
        :type Id: int
        :param _RiskLevelName: 风险等级列表
        :type RiskLevelName: str
        :param _RiskLevelDescription: 风险级别描述
        :type RiskLevelDescription: str
        :param _IdentifyComplianceName: 引用的分类分级模板
        :type IdentifyComplianceName: str
        :param _Type: 类型，区分自定义还是系统内置
        :type Type: str
        """
        self._Id = None
        self._RiskLevelName = None
        self._RiskLevelDescription = None
        self._IdentifyComplianceName = None
        self._Type = None

    @property
    def Id(self):
        """风险id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RiskLevelName(self):
        """风险等级列表
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def RiskLevelDescription(self):
        """风险级别描述
        :rtype: str
        """
        return self._RiskLevelDescription

    @RiskLevelDescription.setter
    def RiskLevelDescription(self, RiskLevelDescription):
        self._RiskLevelDescription = RiskLevelDescription

    @property
    def IdentifyComplianceName(self):
        """引用的分类分级模板
        :rtype: str
        """
        return self._IdentifyComplianceName

    @IdentifyComplianceName.setter
    def IdentifyComplianceName(self, IdentifyComplianceName):
        self._IdentifyComplianceName = IdentifyComplianceName

    @property
    def Type(self):
        """类型，区分自定义还是系统内置
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RiskLevelName = params.get("RiskLevelName")
        self._RiskLevelDescription = params.get("RiskLevelDescription")
        self._IdentifyComplianceName = params.get("IdentifyComplianceName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskLevelTrendItem(AbstractModel):
    """风险级别趋势项

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _High: 高风险数量
        :type High: int
        :param _Medium: 中风险数量
        :type Medium: int
        :param _Low: 低风险数量
        :type Low: int
        :param _Total: 总数
        :type Total: int
        """
        self._Date = None
        self._High = None
        self._Medium = None
        self._Low = None
        self._Total = None

    @property
    def Date(self):
        """日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def High(self):
        """高风险数量
        :rtype: int
        """
        return self._High

    @High.setter
    def High(self, High):
        self._High = High

    @property
    def Medium(self):
        """中风险数量
        :rtype: int
        """
        return self._Medium

    @Medium.setter
    def Medium(self, Medium):
        self._Medium = Medium

    @property
    def Low(self):
        """低风险数量
        :rtype: int
        """
        return self._Low

    @Low.setter
    def Low(self, Low):
        self._Low = Low

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._High = params.get("High")
        self._Medium = params.get("Medium")
        self._Low = params.get("Low")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskMatrixLevel(AbstractModel):
    """用于生成默认的风险级别矩阵

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Id: 就是id
        :type Id: int
        :param _Score: 分数
        :type Score: float
        """
        self._Name = None
        self._Id = None
        self._Score = None

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
    def Id(self):
        """就是id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Score(self):
        """分数
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskSideDistributed(AbstractModel):
    """风险面的分布

    """

    def __init__(self):
        r"""
        :param _AssessmentRiskSide: 风险面
        :type AssessmentRiskSide: :class:`tencentcloud.dsgc.v20190723.models.Note`
        :param _AssessmentRisk: 风险类型
        :type AssessmentRisk: list of Note
        """
        self._AssessmentRiskSide = None
        self._AssessmentRisk = None

    @property
    def AssessmentRiskSide(self):
        """风险面
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.Note`
        """
        return self._AssessmentRiskSide

    @AssessmentRiskSide.setter
    def AssessmentRiskSide(self, AssessmentRiskSide):
        self._AssessmentRiskSide = AssessmentRiskSide

    @property
    def AssessmentRisk(self):
        """风险类型
        :rtype: list of Note
        """
        return self._AssessmentRisk

    @AssessmentRisk.setter
    def AssessmentRisk(self, AssessmentRisk):
        self._AssessmentRisk = AssessmentRisk


    def _deserialize(self, params):
        if params.get("AssessmentRiskSide") is not None:
            self._AssessmentRiskSide = Note()
            self._AssessmentRiskSide._deserialize(params.get("AssessmentRiskSide"))
        if params.get("AssessmentRisk") is not None:
            self._AssessmentRisk = []
            for item in params.get("AssessmentRisk"):
                obj = Note()
                obj._deserialize(item)
                self._AssessmentRisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDistribution(AbstractModel):
    """数据资产报告-rdb的敏感数据规则分布

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则id
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _LevelId: 分级id
        :type LevelId: int
        :param _LevelName: 分级名称
        :type LevelName: str
        :param _RuleCnt: 规则数量
        :type RuleCnt: int
        """
        self._RuleId = None
        self._RuleName = None
        self._LevelId = None
        self._LevelName = None
        self._RuleCnt = None

    @property
    def RuleId(self):
        """规则id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def LevelId(self):
        """分级id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """分级名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def RuleCnt(self):
        """规则数量
        :rtype: int
        """
        return self._RuleCnt

    @RuleCnt.setter
    def RuleCnt(self, RuleCnt):
        self._RuleCnt = RuleCnt


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        self._RuleCnt = params.get("RuleCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleEffectItem(AbstractModel):
    """分类分级规则数量

    """

    def __init__(self):
        r"""
        :param _Name: 规则描述
        :type Name: str
        :param _Value: 规则值
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """规则描述
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """规则值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskCOSRules(AbstractModel):
    """敏感识别任务COS识别规则

    """

    def __init__(self):
        r"""
        :param _RegexRule: regex规则内容
        :type RegexRule: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        :param _Status: 规则状态；0 不启用, 1 启用
        :type Status: int
        :param _KeywordRule: 关键词规则内容组，最大支持5个关键词。
        :type KeywordRule: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        :param _IgnoreStringRule: 忽略词规则内容组，最大支持5个忽略词。
        :type IgnoreStringRule: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        :param _MaxMatch: 最大匹配距离，默认值为100。上限为500.
        :type MaxMatch: int
        """
        self._RegexRule = None
        self._Status = None
        self._KeywordRule = None
        self._IgnoreStringRule = None
        self._MaxMatch = None

    @property
    def RegexRule(self):
        """regex规则内容
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        """
        return self._RegexRule

    @RegexRule.setter
    def RegexRule(self, RegexRule):
        self._RegexRule = RegexRule

    @property
    def Status(self):
        """规则状态；0 不启用, 1 启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def KeywordRule(self):
        """关键词规则内容组，最大支持5个关键词。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        """
        return self._KeywordRule

    @KeywordRule.setter
    def KeywordRule(self, KeywordRule):
        self._KeywordRule = KeywordRule

    @property
    def IgnoreStringRule(self):
        """忽略词规则内容组，最大支持5个忽略词。
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.COSDataRule`
        """
        return self._IgnoreStringRule

    @IgnoreStringRule.setter
    def IgnoreStringRule(self, IgnoreStringRule):
        self._IgnoreStringRule = IgnoreStringRule

    @property
    def MaxMatch(self):
        """最大匹配距离，默认值为100。上限为500.
        :rtype: int
        """
        return self._MaxMatch

    @MaxMatch.setter
    def MaxMatch(self, MaxMatch):
        self._MaxMatch = MaxMatch


    def _deserialize(self, params):
        if params.get("RegexRule") is not None:
            self._RegexRule = COSDataRule()
            self._RegexRule._deserialize(params.get("RegexRule"))
        self._Status = params.get("Status")
        if params.get("KeywordRule") is not None:
            self._KeywordRule = COSDataRule()
            self._KeywordRule._deserialize(params.get("KeywordRule"))
        if params.get("IgnoreStringRule") is not None:
            self._IgnoreStringRule = COSDataRule()
            self._IgnoreStringRule._deserialize(params.get("IgnoreStringRule"))
        self._MaxMatch = params.get("MaxMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskComplianceInfo(AbstractModel):
    """扫描任务选择的合规组信息

    """

    def __init__(self):
        r"""
        :param _ComplianceGroupId: 合规组ID
        :type ComplianceGroupId: int
        :param _ComplianceGroupName: 合规组名称
        :type ComplianceGroupName: str
        """
        self._ComplianceGroupId = None
        self._ComplianceGroupName = None

    @property
    def ComplianceGroupId(self):
        """合规组ID
        :rtype: int
        """
        return self._ComplianceGroupId

    @ComplianceGroupId.setter
    def ComplianceGroupId(self, ComplianceGroupId):
        self._ComplianceGroupId = ComplianceGroupId

    @property
    def ComplianceGroupName(self):
        """合规组名称
        :rtype: str
        """
        return self._ComplianceGroupName

    @ComplianceGroupName.setter
    def ComplianceGroupName(self, ComplianceGroupName):
        self._ComplianceGroupName = ComplianceGroupName


    def _deserialize(self, params):
        self._ComplianceGroupId = params.get("ComplianceGroupId")
        self._ComplianceGroupName = params.get("ComplianceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskRDBRules(AbstractModel):
    """敏感识别任务RDB数据规则

    """

    def __init__(self):
        r"""
        :param _Status: 规则状态；0 不启用, 1 启用
        :type Status: int
        :param _MatchOperator: 只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :type MatchOperator: str
        :param _MetaRule: 字段名包含规则，最大支持选择9项
        :type MetaRule: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        :param _ContentRule: 内容包含规则，最大支持选择9项
        :type ContentRule: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        """
        self._Status = None
        self._MatchOperator = None
        self._MetaRule = None
        self._ContentRule = None

    @property
    def Status(self):
        """规则状态；0 不启用, 1 启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MatchOperator(self):
        """只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :rtype: str
        """
        return self._MatchOperator

    @MatchOperator.setter
    def MatchOperator(self, MatchOperator):
        self._MatchOperator = MatchOperator

    @property
    def MetaRule(self):
        """字段名包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        """
        return self._MetaRule

    @MetaRule.setter
    def MetaRule(self, MetaRule):
        self._MetaRule = MetaRule

    @property
    def ContentRule(self):
        """内容包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        """
        return self._ContentRule

    @ContentRule.setter
    def ContentRule(self, ContentRule):
        self._ContentRule = ContentRule


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MatchOperator = params.get("MatchOperator")
        if params.get("MetaRule") is not None:
            self._MetaRule = DataRules()
            self._MetaRule._deserialize(params.get("MetaRule"))
        if params.get("ContentRule") is not None:
            self._ContentRule = DataRules()
            self._ContentRule._deserialize(params.get("ContentRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskResult(AbstractModel):
    """扫描任务结果信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务最新一次运行结果ID
        :type Id: int
        :param _EndTime: 任务扫描结束的时间，格式如：2021-12-12 12:12:12
        :type EndTime: str
        :param _Status: 任务状态，-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :type Status: int
        :param _Result: 扫描任务结果展示，如果扫描失败，则显示失败原因
        :type Result: str
        :param _ResultDescription: 结果描述
        :type ResultDescription: str
        :param _Suggestion: 结果建议
        :type Suggestion: str
        :param _Progress: 扫描进度
        :type Progress: float
        """
        self._Id = None
        self._EndTime = None
        self._Status = None
        self._Result = None
        self._ResultDescription = None
        self._Suggestion = None
        self._Progress = None

    @property
    def Id(self):
        """任务最新一次运行结果ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def EndTime(self):
        """任务扫描结束的时间，格式如：2021-12-12 12:12:12
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """任务状态，-1待触发 0待扫描 1扫描中 2扫描终止 3扫描成功 4扫描失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        """扫描任务结果展示，如果扫描失败，则显示失败原因
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultDescription(self):
        """结果描述
        :rtype: str
        """
        return self._ResultDescription

    @ResultDescription.setter
    def ResultDescription(self, ResultDescription):
        self._ResultDescription = ResultDescription

    @property
    def Suggestion(self):
        """结果建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Progress(self):
        """扫描进度
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._ResultDescription = params.get("ResultDescription")
        self._Suggestion = params.get("Suggestion")
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityProduct(AbstractModel):
    """建议使用的安全产品

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ReferUrl: 产品链接
        :type ReferUrl: str
        """
        self._ProductName = None
        self._ReferUrl = None

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ReferUrl(self):
        """产品链接
        :rtype: str
        """
        return self._ReferUrl

    @ReferUrl.setter
    def ReferUrl(self, ReferUrl):
        self._ReferUrl = ReferUrl


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._ReferUrl = params.get("ReferUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SensitiveLevel(AbstractModel):
    """敏感等级分布

    """

    def __init__(self):
        r"""
        :param _LevelId: 分级标识ID
        :type LevelId: int
        :param _LevelCnt: 分级标识统计
        :type LevelCnt: int
        :param _LevelRiskName: 分级标识名称
        :type LevelRiskName: str
        :param _LevelRiskScore: 分级标识分数
        :type LevelRiskScore: int
        """
        self._LevelId = None
        self._LevelCnt = None
        self._LevelRiskName = None
        self._LevelRiskScore = None

    @property
    def LevelId(self):
        """分级标识ID
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelCnt(self):
        """分级标识统计
        :rtype: int
        """
        return self._LevelCnt

    @LevelCnt.setter
    def LevelCnt(self, LevelCnt):
        self._LevelCnt = LevelCnt

    @property
    def LevelRiskName(self):
        """分级标识名称
        :rtype: str
        """
        return self._LevelRiskName

    @LevelRiskName.setter
    def LevelRiskName(self, LevelRiskName):
        self._LevelRiskName = LevelRiskName

    @property
    def LevelRiskScore(self):
        """分级标识分数
        :rtype: int
        """
        return self._LevelRiskScore

    @LevelRiskScore.setter
    def LevelRiskScore(self, LevelRiskScore):
        self._LevelRiskScore = LevelRiskScore


    def _deserialize(self, params):
        self._LevelId = params.get("LevelId")
        self._LevelCnt = params.get("LevelCnt")
        self._LevelRiskName = params.get("LevelRiskName")
        self._LevelRiskScore = params.get("LevelRiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartDSPADiscoveryTaskRequest(AbstractModel):
    """StartDSPADiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartDSPADiscoveryTaskResponse(AbstractModel):
    """StartDSPADiscoveryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultId: 任务扫描结果ID
        :type ResultId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultId = None
        self._RequestId = None

    @property
    def ResultId(self):
        """任务扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

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
        self._ResultId = params.get("ResultId")
        self._RequestId = params.get("RequestId")


class StopDSPADiscoveryTaskRequest(AbstractModel):
    """StopDSPADiscoveryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._DspaId = None
        self._TaskId = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDSPADiscoveryTaskResponse(AbstractModel):
    """StopDSPADiscoveryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultId: 任务扫描结果ID
        :type ResultId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultId = None
        self._RequestId = None

    @property
    def ResultId(self):
        """任务扫描结果ID
        :rtype: int
        """
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

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
        self._ResultId = params.get("ResultId")
        self._RequestId = params.get("RequestId")


class SuggestRiskLevelMatrix(AbstractModel):
    """生成的建议的风险等级矩阵

    """

    def __init__(self):
        r"""
        :param _RiskLevelMatrix: 矩阵
        :type RiskLevelMatrix: list of SuggestRiskLevelMatrixItem
        """
        self._RiskLevelMatrix = None

    @property
    def RiskLevelMatrix(self):
        """矩阵
        :rtype: list of SuggestRiskLevelMatrixItem
        """
        return self._RiskLevelMatrix

    @RiskLevelMatrix.setter
    def RiskLevelMatrix(self, RiskLevelMatrix):
        self._RiskLevelMatrix = RiskLevelMatrix


    def _deserialize(self, params):
        if params.get("RiskLevelMatrix") is not None:
            self._RiskLevelMatrix = []
            for item in params.get("RiskLevelMatrix"):
                obj = SuggestRiskLevelMatrixItem()
                obj._deserialize(item)
                self._RiskLevelMatrix.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuggestRiskLevelMatrixItem(AbstractModel):
    """建议生成的二位矩阵的第二层

    """

    def __init__(self):
        r"""
        :param _SensitiveLevel: 分类分级等级
        :type SensitiveLevel: :class:`tencentcloud.dsgc.v20190723.models.RiskMatrixLevel`
        :param _VulnerabilityLevel: 脆弱项等级
        :type VulnerabilityLevel: :class:`tencentcloud.dsgc.v20190723.models.RiskMatrixLevel`
        :param _RiskName: 风险名
        :type RiskName: str
        :param _RiskScore: 分数
        :type RiskScore: float
        """
        self._SensitiveLevel = None
        self._VulnerabilityLevel = None
        self._RiskName = None
        self._RiskScore = None

    @property
    def SensitiveLevel(self):
        """分类分级等级
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.RiskMatrixLevel`
        """
        return self._SensitiveLevel

    @SensitiveLevel.setter
    def SensitiveLevel(self, SensitiveLevel):
        self._SensitiveLevel = SensitiveLevel

    @property
    def VulnerabilityLevel(self):
        """脆弱项等级
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.RiskMatrixLevel`
        """
        return self._VulnerabilityLevel

    @VulnerabilityLevel.setter
    def VulnerabilityLevel(self, VulnerabilityLevel):
        self._VulnerabilityLevel = VulnerabilityLevel

    @property
    def RiskName(self):
        """风险名
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskScore(self):
        """分数
        :rtype: float
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore


    def _deserialize(self, params):
        if params.get("SensitiveLevel") is not None:
            self._SensitiveLevel = RiskMatrixLevel()
            self._SensitiveLevel._deserialize(params.get("SensitiveLevel"))
        if params.get("VulnerabilityLevel") is not None:
            self._VulnerabilityLevel = RiskMatrixLevel()
            self._VulnerabilityLevel._deserialize(params.get("VulnerabilityLevel"))
        self._RiskName = params.get("RiskName")
        self._RiskScore = params.get("RiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """评估模板的详情数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

    @property
    def TemplateId(self):
        """模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopAsset(AbstractModel):
    """数据资产报告-涉敏top的资产

    """

    def __init__(self):
        r"""
        :param _LevelName: 分级名称
        :type LevelName: str
        :param _TopStat: top数据信息
        :type TopStat: list of TopAssetStat
        """
        self._LevelName = None
        self._TopStat = None

    @property
    def LevelName(self):
        """分级名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def TopStat(self):
        """top数据信息
        :rtype: list of TopAssetStat
        """
        return self._TopStat

    @TopStat.setter
    def TopStat(self, TopStat):
        self._TopStat = TopStat


    def _deserialize(self, params):
        self._LevelName = params.get("LevelName")
        if params.get("TopStat") is not None:
            self._TopStat = []
            for item in params.get("TopStat"):
                obj = TopAssetStat()
                obj._deserialize(item)
                self._TopStat.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopAssetStat(AbstractModel):
    """设敏top资产的信息

    """

    def __init__(self):
        r"""
        :param _DataSourceId: 数据源id
        :type DataSourceId: str
        :param _SubData: db_name
        :type SubData: str
        :param _SensitiveCnt: 敏感个数
        :type SensitiveCnt: int
        """
        self._DataSourceId = None
        self._SubData = None
        self._SensitiveCnt = None

    @property
    def DataSourceId(self):
        """数据源id
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def SubData(self):
        """db_name
        :rtype: str
        """
        return self._SubData

    @SubData.setter
    def SubData(self, SubData):
        self._SubData = SubData

    @property
    def SensitiveCnt(self):
        """敏感个数
        :rtype: int
        """
        return self._SensitiveCnt

    @SensitiveCnt.setter
    def SensitiveCnt(self, SensitiveCnt):
        self._SensitiveCnt = SensitiveCnt


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._SubData = params.get("SubData")
        self._SensitiveCnt = params.get("SensitiveCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDSPASelfBuildResourceRequest(AbstractModel):
    """UpdateDSPASelfBuildResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceId: 云资源名称，如果是通过CVM访问则填写CVM的资源ID，如果是通过LB访问则填写LB的资源ID。
        :type ResourceId: str
        :param _ResourceVPort: 资源绑定的端口，为0则表示不更新。
        :type ResourceVPort: int
        :param _UserName: 账户名，为空则表示不更新。
UserName和Password必须同时填写或同时为空。
        :type UserName: str
        :param _Password: 账户密码，为空则表示不更新。
UserName和Password必须同时填写或同时为空。
        :type Password: str
        :param _AuthRange: 授权范围：all 授权全部  manual：手动指定
        :type AuthRange: str
        :param _ResourceName: 自建数据资产的名称，支持修改
        :type ResourceName: str
        """
        self._DspaId = None
        self._ResourceId = None
        self._ResourceVPort = None
        self._UserName = None
        self._Password = None
        self._AuthRange = None
        self._ResourceName = None

    @property
    def DspaId(self):
        """DSPA实例ID。
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceId(self):
        """云资源名称，如果是通过CVM访问则填写CVM的资源ID，如果是通过LB访问则填写LB的资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceVPort(self):
        """资源绑定的端口，为0则表示不更新。
        :rtype: int
        """
        return self._ResourceVPort

    @ResourceVPort.setter
    def ResourceVPort(self, ResourceVPort):
        self._ResourceVPort = ResourceVPort

    @property
    def UserName(self):
        """账户名，为空则表示不更新。
UserName和Password必须同时填写或同时为空。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """账户密码，为空则表示不更新。
UserName和Password必须同时填写或同时为空。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AuthRange(self):
        """授权范围：all 授权全部  manual：手动指定
        :rtype: str
        """
        return self._AuthRange

    @AuthRange.setter
    def AuthRange(self, AuthRange):
        self._AuthRange = AuthRange

    @property
    def ResourceName(self):
        """自建数据资产的名称，支持修改
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceVPort = params.get("ResourceVPort")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._AuthRange = params.get("AuthRange")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDSPASelfBuildResourceResponse(AbstractModel):
    """UpdateDSPASelfBuildResource返回参数结构体

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


class VerifyDSPACOSRuleRequest(AbstractModel):
    """VerifyDSPACOSRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _COSRules: 待验证COS规则
        :type COSRules: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskCOSRules`
        :param _Data: 待验证数据
        :type Data: str
        """
        self._DspaId = None
        self._COSRules = None
        self._Data = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def COSRules(self):
        """待验证COS规则
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ScanTaskCOSRules`
        """
        return self._COSRules

    @COSRules.setter
    def COSRules(self, COSRules):
        self._COSRules = COSRules

    @property
    def Data(self):
        """待验证数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        if params.get("COSRules") is not None:
            self._COSRules = ScanTaskCOSRules()
            self._COSRules._deserialize(params.get("COSRules"))
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyDSPACOSRuleResponse(AbstractModel):
    """VerifyDSPACOSRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验证结果
Success 验证成功
Failed 验证失败
        :type VerifyResult: str
        :param _DetailInfo: 验证结果详情
        :type DetailInfo: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyResult = None
        self._DetailInfo = None
        self._RequestId = None

    @property
    def VerifyResult(self):
        """验证结果
Success 验证成功
Failed 验证失败
        :rtype: str
        """
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def DetailInfo(self):
        """验证结果详情
        :rtype: str
        """
        return self._DetailInfo

    @DetailInfo.setter
    def DetailInfo(self, DetailInfo):
        self._DetailInfo = DetailInfo

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
        self._VerifyResult = params.get("VerifyResult")
        self._DetailInfo = params.get("DetailInfo")
        self._RequestId = params.get("RequestId")


class VerifyDSPADiscoveryRuleRequest(AbstractModel):
    """VerifyDSPADiscoveryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID
        :type DspaId: str
        :param _MatchOperator: 只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :type MatchOperator: str
        :param _MetaRule: 字段名包含规则，最大支持选择9项
        :type MetaRule: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        :param _ContentRule: 内容包含规则，最大支持选择9项
        :type ContentRule: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        :param _VerifyMeta: 验证规则字段名，最大长度为1024个字符
        :type VerifyMeta: str
        :param _VerifyContent: 验证规则数据内容，最大长度为1024个字符
        :type VerifyContent: str
        """
        self._DspaId = None
        self._MatchOperator = None
        self._MetaRule = None
        self._ContentRule = None
        self._VerifyMeta = None
        self._VerifyContent = None

    @property
    def DspaId(self):
        """DSPA实例ID
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MatchOperator(self):
        """只能取and 、or两个值其中之一，and：字段和内容同时满足，or：字段和内容满足其一
        :rtype: str
        """
        return self._MatchOperator

    @MatchOperator.setter
    def MatchOperator(self, MatchOperator):
        self._MatchOperator = MatchOperator

    @property
    def MetaRule(self):
        """字段名包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        """
        return self._MetaRule

    @MetaRule.setter
    def MetaRule(self, MetaRule):
        self._MetaRule = MetaRule

    @property
    def ContentRule(self):
        """内容包含规则，最大支持选择9项
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DataRules`
        """
        return self._ContentRule

    @ContentRule.setter
    def ContentRule(self, ContentRule):
        self._ContentRule = ContentRule

    @property
    def VerifyMeta(self):
        """验证规则字段名，最大长度为1024个字符
        :rtype: str
        """
        return self._VerifyMeta

    @VerifyMeta.setter
    def VerifyMeta(self, VerifyMeta):
        self._VerifyMeta = VerifyMeta

    @property
    def VerifyContent(self):
        """验证规则数据内容，最大长度为1024个字符
        :rtype: str
        """
        return self._VerifyContent

    @VerifyContent.setter
    def VerifyContent(self, VerifyContent):
        self._VerifyContent = VerifyContent


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MatchOperator = params.get("MatchOperator")
        if params.get("MetaRule") is not None:
            self._MetaRule = DataRules()
            self._MetaRule._deserialize(params.get("MetaRule"))
        if params.get("ContentRule") is not None:
            self._ContentRule = DataRules()
            self._ContentRule._deserialize(params.get("ContentRule"))
        self._VerifyMeta = params.get("VerifyMeta")
        self._VerifyContent = params.get("VerifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyDSPADiscoveryRuleResponse(AbstractModel):
    """VerifyDSPADiscoveryRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验证结果
Success 验证成功
Failed 验证失败
        :type VerifyResult: str
        :param _DetailInfo: 验证结果详情
        :type DetailInfo: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyResult = None
        self._DetailInfo = None
        self._RequestId = None

    @property
    def VerifyResult(self):
        """验证结果
Success 验证成功
Failed 验证失败
        :rtype: str
        """
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def DetailInfo(self):
        """验证结果详情
        :rtype: str
        """
        return self._DetailInfo

    @DetailInfo.setter
    def DetailInfo(self, DetailInfo):
        self._DetailInfo = DetailInfo

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
        self._VerifyResult = params.get("VerifyResult")
        self._DetailInfo = params.get("DetailInfo")
        self._RequestId = params.get("RequestId")