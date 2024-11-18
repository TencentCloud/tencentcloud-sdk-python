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


class AddSubStructureTasksRequest(AbstractModel):
    """AddSubStructureTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 主任务id
        :type MainTaskId: str
        :param _TaskInfos: 子任务信息数组
        :type TaskInfos: list of CreateStructureTaskInfo
        """
        self._MainTaskId = None
        self._TaskInfos = None

    @property
    def MainTaskId(self):
        """主任务id
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def TaskInfos(self):
        """子任务信息数组
        :rtype: list of CreateStructureTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateStructureTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSubStructureTasksResponse(AbstractModel):
    """AddSubStructureTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubTaskIds: 增量子任务id数组
        :type SubTaskIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubTaskIds = None
        self._RequestId = None

    @property
    def SubTaskIds(self):
        """增量子任务id数组
        :rtype: list of str
        """
        return self._SubTaskIds

    @SubTaskIds.setter
    def SubTaskIds(self, SubTaskIds):
        self._SubTaskIds = SubTaskIds

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubTaskIds = params.get("SubTaskIds")
        self._RequestId = params.get("RequestId")


class ClassifiedReports(AbstractModel):
    """报告分类结果

    """

    def __init__(self):
        r"""
        :param _ReportType: 报告类型
        :type ReportType: str
        :param _FileList: 文件列表
        :type FileList: list of str
        """
        self._ReportType = None
        self._FileList = None

    @property
    def ReportType(self):
        """报告类型
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def FileList(self):
        """文件列表
        :rtype: list of str
        """
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList


    def _deserialize(self, params):
        self._ReportType = params.get("ReportType")
        self._FileList = params.get("FileList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyInfo(AbstractModel):
    """报告分类信息

    """

    def __init__(self):
        r"""
        :param _FirstClass: 一级分类
        :type FirstClass: str
        :param _SecondClass: 二级分类
        :type SecondClass: str
        :param _ThirdClass: 三级分类
        :type ThirdClass: str
        :param _FirstClassId: 一级分类序号
        :type FirstClassId: int
        :param _SecondClassId: 二级分类序号
        :type SecondClassId: int
        :param _ThirdClassId: 三级分类序号
        :type ThirdClassId: int
        """
        self._FirstClass = None
        self._SecondClass = None
        self._ThirdClass = None
        self._FirstClassId = None
        self._SecondClassId = None
        self._ThirdClassId = None

    @property
    def FirstClass(self):
        """一级分类
        :rtype: str
        """
        return self._FirstClass

    @FirstClass.setter
    def FirstClass(self, FirstClass):
        self._FirstClass = FirstClass

    @property
    def SecondClass(self):
        """二级分类
        :rtype: str
        """
        return self._SecondClass

    @SecondClass.setter
    def SecondClass(self, SecondClass):
        self._SecondClass = SecondClass

    @property
    def ThirdClass(self):
        """三级分类
        :rtype: str
        """
        return self._ThirdClass

    @ThirdClass.setter
    def ThirdClass(self, ThirdClass):
        self._ThirdClass = ThirdClass

    @property
    def FirstClassId(self):
        """一级分类序号
        :rtype: int
        """
        return self._FirstClassId

    @FirstClassId.setter
    def FirstClassId(self, FirstClassId):
        self._FirstClassId = FirstClassId

    @property
    def SecondClassId(self):
        """二级分类序号
        :rtype: int
        """
        return self._SecondClassId

    @SecondClassId.setter
    def SecondClassId(self, SecondClassId):
        self._SecondClassId = SecondClassId

    @property
    def ThirdClassId(self):
        """三级分类序号
        :rtype: int
        """
        return self._ThirdClassId

    @ThirdClassId.setter
    def ThirdClassId(self, ThirdClassId):
        self._ThirdClassId = ThirdClassId


    def _deserialize(self, params):
        self._FirstClass = params.get("FirstClass")
        self._SecondClass = params.get("SecondClass")
        self._ThirdClass = params.get("ThirdClass")
        self._FirstClassId = params.get("FirstClassId")
        self._SecondClassId = params.get("SecondClassId")
        self._ThirdClassId = params.get("ThirdClassId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareMetricsData(AbstractModel):
    """结构化对比指标（准确率/召回率）数据

    """

    def __init__(self):
        r"""
        :param _ShortStructAccuracy: 短文准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortStructAccuracy: str
        :param _ShortStructRecall: 短文召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortStructRecall: str
        :param _LongStructAccuracy: 长文结构化准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongStructAccuracy: str
        :param _LongStructRecall: 长文结构化召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongStructRecall: str
        :param _LongContentAccuracy: 长文提取准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongContentAccuracy: str
        :param _LongContentRecall: 长文提取召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongContentRecall: str
        """
        self._ShortStructAccuracy = None
        self._ShortStructRecall = None
        self._LongStructAccuracy = None
        self._LongStructRecall = None
        self._LongContentAccuracy = None
        self._LongContentRecall = None

    @property
    def ShortStructAccuracy(self):
        """短文准确率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShortStructAccuracy

    @ShortStructAccuracy.setter
    def ShortStructAccuracy(self, ShortStructAccuracy):
        self._ShortStructAccuracy = ShortStructAccuracy

    @property
    def ShortStructRecall(self):
        """短文召回率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShortStructRecall

    @ShortStructRecall.setter
    def ShortStructRecall(self, ShortStructRecall):
        self._ShortStructRecall = ShortStructRecall

    @property
    def LongStructAccuracy(self):
        """长文结构化准确率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LongStructAccuracy

    @LongStructAccuracy.setter
    def LongStructAccuracy(self, LongStructAccuracy):
        self._LongStructAccuracy = LongStructAccuracy

    @property
    def LongStructRecall(self):
        """长文结构化召回率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LongStructRecall

    @LongStructRecall.setter
    def LongStructRecall(self, LongStructRecall):
        self._LongStructRecall = LongStructRecall

    @property
    def LongContentAccuracy(self):
        """长文提取准确率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LongContentAccuracy

    @LongContentAccuracy.setter
    def LongContentAccuracy(self, LongContentAccuracy):
        self._LongContentAccuracy = LongContentAccuracy

    @property
    def LongContentRecall(self):
        """长文提取召回率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LongContentRecall

    @LongContentRecall.setter
    def LongContentRecall(self, LongContentRecall):
        self._LongContentRecall = LongContentRecall


    def _deserialize(self, params):
        self._ShortStructAccuracy = params.get("ShortStructAccuracy")
        self._ShortStructRecall = params.get("ShortStructRecall")
        self._LongStructAccuracy = params.get("LongStructAccuracy")
        self._LongStructRecall = params.get("LongStructRecall")
        self._LongContentAccuracy = params.get("LongContentAccuracy")
        self._LongContentRecall = params.get("LongContentRecall")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskInfo(AbstractModel):
    """创建自动分类的结构化任务子任务信息

    """

    def __init__(self):
        r"""
        :param _FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param _CustomerId: 客户号
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        """
        self._FileList = None
        self._CustomerId = None
        self._CustomerName = None
        self._ImageList = None

    @property
    def FileList(self):
        """报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :rtype: list of str
        """
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList

    @property
    def CustomerId(self):
        """客户号
        :rtype: str
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """客户姓名
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def ImageList(self):
        """报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :rtype: list of str
        """
        return self._ImageList

    @ImageList.setter
    def ImageList(self, ImageList):
        self._ImageList = ImageList


    def _deserialize(self, params):
        self._FileList = params.get("FileList")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._ImageList = params.get("ImageList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskRequest(AbstractModel):
    """CreateAutoClassifyStructureTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param _TaskInfos: 创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :type TaskInfos: list of CreateAutoClassifyStructureTaskInfo
        :param _PolicyId: 保单号
        :type PolicyId: str
        :param _TriggerType: 核保触发方式
Auto 自动
Manual 手动
        :type TriggerType: str
        :param _InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param _CallbackUrl: 回调地址，接收Post请求传送结果
        :type CallbackUrl: str
        """
        self._ServiceType = None
        self._TaskInfos = None
        self._PolicyId = None
        self._TriggerType = None
        self._InsuranceTypes = None
        self._CallbackUrl = None

    @property
    def ServiceType(self):
        """服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def TaskInfos(self):
        """创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :rtype: list of CreateAutoClassifyStructureTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def PolicyId(self):
        """保单号
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def TriggerType(self):
        """核保触发方式
Auto 自动
Manual 手动
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def InsuranceTypes(self):
        """险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :rtype: list of str
        """
        return self._InsuranceTypes

    @InsuranceTypes.setter
    def InsuranceTypes(self, InsuranceTypes):
        self._InsuranceTypes = InsuranceTypes

    @property
    def CallbackUrl(self):
        """回调地址，接收Post请求传送结果
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateAutoClassifyStructureTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._TriggerType = params.get("TriggerType")
        self._InsuranceTypes = params.get("InsuranceTypes")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskResponse(AbstractModel):
    """CreateAutoClassifyStructureTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 创建的主任务号，用于查询结果
        :type MainTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MainTaskId = None
        self._RequestId = None

    @property
    def MainTaskId(self):
        """创建的主任务号，用于查询结果
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._RequestId = params.get("RequestId")


class CreateStructureTaskInfo(AbstractModel):
    """创建结构化任务子任务信息

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param _FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param _CustomerId: 客户号
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        :param _Year: 报告年份
        :type Year: str
        """
        self._TaskType = None
        self._FileList = None
        self._CustomerId = None
        self._CustomerName = None
        self._ImageList = None
        self._Year = None

    @property
    def TaskType(self):
        """任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def FileList(self):
        """报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :rtype: list of str
        """
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList

    @property
    def CustomerId(self):
        """客户号
        :rtype: str
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """客户姓名
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def ImageList(self):
        """报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :rtype: list of str
        """
        return self._ImageList

    @ImageList.setter
    def ImageList(self, ImageList):
        self._ImageList = ImageList

    @property
    def Year(self):
        """报告年份
        :rtype: str
        """
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._FileList = params.get("FileList")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._ImageList = params.get("ImageList")
        self._Year = params.get("Year")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStructureTaskRequest(AbstractModel):
    """CreateStructureTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param _TaskInfos: 创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :type TaskInfos: list of CreateStructureTaskInfo
        :param _PolicyId: 保单号
        :type PolicyId: str
        :param _TriggerType: 核保触发方式
Auto 自动
Manual 手动
        :type TriggerType: str
        :param _InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param _CallbackUrl: 回调地址，接收Post请求传送结果
        :type CallbackUrl: str
        """
        self._ServiceType = None
        self._TaskInfos = None
        self._PolicyId = None
        self._TriggerType = None
        self._InsuranceTypes = None
        self._CallbackUrl = None

    @property
    def ServiceType(self):
        """服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def TaskInfos(self):
        """创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :rtype: list of CreateStructureTaskInfo
        """
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def PolicyId(self):
        """保单号
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def TriggerType(self):
        """核保触发方式
Auto 自动
Manual 手动
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def InsuranceTypes(self):
        """险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :rtype: list of str
        """
        return self._InsuranceTypes

    @InsuranceTypes.setter
    def InsuranceTypes(self, InsuranceTypes):
        self._InsuranceTypes = InsuranceTypes

    @property
    def CallbackUrl(self):
        """回调地址，接收Post请求传送结果
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateStructureTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._TriggerType = params.get("TriggerType")
        self._InsuranceTypes = params.get("InsuranceTypes")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStructureTaskResponse(AbstractModel):
    """CreateStructureTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 创建的主任务号，用于查询结果
        :type MainTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MainTaskId = None
        self._RequestId = None

    @property
    def MainTaskId(self):
        """创建的主任务号，用于查询结果
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._RequestId = params.get("RequestId")


class CreateUnderwriteTaskByIdRequest(AbstractModel):
    """CreateUnderwriteTaskById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskIds: 主任务ID数组，
        :type MainTaskIds: list of str
        :param _CallbackUrl: 回调地址，可不传（提供轮询机制）。
        :type CallbackUrl: str
        """
        self._MainTaskIds = None
        self._CallbackUrl = None

    @property
    def MainTaskIds(self):
        """主任务ID数组，
        :rtype: list of str
        """
        return self._MainTaskIds

    @MainTaskIds.setter
    def MainTaskIds(self, MainTaskIds):
        self._MainTaskIds = MainTaskIds

    @property
    def CallbackUrl(self):
        """回调地址，可不传（提供轮询机制）。
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._MainTaskIds = params.get("MainTaskIds")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnderwriteTaskByIdResponse(AbstractModel):
    """CreateUnderwriteTaskById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnderwriteTaskIds: 核保任务ID数据
        :type UnderwriteTaskIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnderwriteTaskIds = None
        self._RequestId = None

    @property
    def UnderwriteTaskIds(self):
        """核保任务ID数据
        :rtype: list of str
        """
        return self._UnderwriteTaskIds

    @UnderwriteTaskIds.setter
    def UnderwriteTaskIds(self, UnderwriteTaskIds):
        self._UnderwriteTaskIds = UnderwriteTaskIds

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UnderwriteTaskIds = params.get("UnderwriteTaskIds")
        self._RequestId = params.get("RequestId")


class DescribeMachineUnderwriteRequest(AbstractModel):
    """DescribeMachineUnderwrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        """
        self._UnderwriteTaskId = None

    @property
    def UnderwriteTaskId(self):
        """核保任务ID
        :rtype: str
        """
        return self._UnderwriteTaskId

    @UnderwriteTaskId.setter
    def UnderwriteTaskId(self, UnderwriteTaskId):
        self._UnderwriteTaskId = UnderwriteTaskId


    def _deserialize(self, params):
        self._UnderwriteTaskId = params.get("UnderwriteTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineUnderwriteResponse(AbstractModel):
    """DescribeMachineUnderwrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 腾讯云主账号ID
        :type Uin: str
        :param _SubAccountUin: 操作人子账户ID
        :type SubAccountUin: str
        :param _PolicyId: 保单ID
        :type PolicyId: str
        :param _MainTaskId: 主任务ID
        :type MainTaskId: str
        :param _UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        :param _Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param _UnderwriteResults: 机器核保结果
        :type UnderwriteResults: list of MachineUnderwriteOutput
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._SubAccountUin = None
        self._PolicyId = None
        self._MainTaskId = None
        self._UnderwriteTaskId = None
        self._Status = None
        self._UnderwriteResults = None
        self._RequestId = None

    @property
    def Uin(self):
        """腾讯云主账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        """操作人子账户ID
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def PolicyId(self):
        """保单ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def MainTaskId(self):
        """主任务ID
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def UnderwriteTaskId(self):
        """核保任务ID
        :rtype: str
        """
        return self._UnderwriteTaskId

    @UnderwriteTaskId.setter
    def UnderwriteTaskId(self, UnderwriteTaskId):
        self._UnderwriteTaskId = UnderwriteTaskId

    @property
    def Status(self):
        """结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnderwriteResults(self):
        """机器核保结果
        :rtype: list of MachineUnderwriteOutput
        """
        return self._UnderwriteResults

    @UnderwriteResults.setter
    def UnderwriteResults(self, UnderwriteResults):
        self._UnderwriteResults = UnderwriteResults

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._PolicyId = params.get("PolicyId")
        self._MainTaskId = params.get("MainTaskId")
        self._UnderwriteTaskId = params.get("UnderwriteTaskId")
        self._Status = params.get("Status")
        if params.get("UnderwriteResults") is not None:
            self._UnderwriteResults = []
            for item in params.get("UnderwriteResults"):
                obj = MachineUnderwriteOutput()
                obj._deserialize(item)
                self._UnderwriteResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQualityScoreRequest(AbstractModel):
    """DescribeQualityScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _File: 文件二进制数据
        :type File: binary
        """
        self._File = None

    @property
    def File(self):
        """文件二进制数据
        :rtype: binary
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File


    def _deserialize(self, params):
        self._File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityScoreResponse(AbstractModel):
    """DescribeQualityScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QualityScore: 质量分
        :type QualityScore: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QualityScore = None
        self._RequestId = None

    @property
    def QualityScore(self):
        """质量分
        :rtype: float
        """
        return self._QualityScore

    @QualityScore.setter
    def QualityScore(self, QualityScore):
        self._QualityScore = QualityScore

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QualityScore = params.get("QualityScore")
        self._RequestId = params.get("RequestId")


class DescribeReportClassifyRequest(AbstractModel):
    """DescribeReportClassify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param _FileList: 文件地址数组
        :type FileList: list of str
        """
        self._ServiceType = None
        self._FileList = None

    @property
    def ServiceType(self):
        """服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def FileList(self):
        """文件地址数组
        :rtype: list of str
        """
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._FileList = params.get("FileList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportClassifyResponse(AbstractModel):
    """DescribeReportClassify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Reports: 报告分类结果
        :type Reports: list of ClassifiedReports
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Reports = None
        self._RequestId = None

    @property
    def Reports(self):
        """报告分类结果
        :rtype: list of ClassifiedReports
        """
        return self._Reports

    @Reports.setter
    def Reports(self, Reports):
        self._Reports = Reports

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Reports") is not None:
            self._Reports = []
            for item in params.get("Reports"):
                obj = ClassifiedReports()
                obj._deserialize(item)
                self._Reports.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStructCompareDataRequest(AbstractModel):
    """DescribeStructCompareData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 主任务号
        :type MainTaskId: str
        :param _SubTaskId: 子任务号
        :type SubTaskId: str
        """
        self._MainTaskId = None
        self._SubTaskId = None

    @property
    def MainTaskId(self):
        """主任务号
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def SubTaskId(self):
        """子任务号
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._SubTaskId = params.get("SubTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructCompareDataResponse(AbstractModel):
    """DescribeStructCompareData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 保单号
        :type PolicyId: str
        :param _MainTaskId: 主任务号
        :type MainTaskId: str
        :param _CustomerId: 客户号
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerId: str
        :param _CustomerName: 客户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerName: str
        :param _ReviewTime: 复核时间
        :type ReviewTime: str
        :param _MachineResult: 算法识别结果
        :type MachineResult: str
        :param _ManualResult: 人工复核结果
        :type ManualResult: str
        :param _Metrics: 结构化对比指标数据
        :type Metrics: :class:`tencentcloud.cii.v20210408.models.CompareMetricsData`
        :param _NewItems: 新增项
        :type NewItems: str
        :param _ModifyItems: 修改项
        :type ModifyItems: str
        :param _SubTaskId: 子任务号
        :type SubTaskId: str
        :param _AllTasks: 所有的子任务
        :type AllTasks: list of ReviewDataTaskInfo
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._MainTaskId = None
        self._CustomerId = None
        self._CustomerName = None
        self._ReviewTime = None
        self._MachineResult = None
        self._ManualResult = None
        self._Metrics = None
        self._NewItems = None
        self._ModifyItems = None
        self._SubTaskId = None
        self._AllTasks = None
        self._TaskType = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """保单号
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def MainTaskId(self):
        """主任务号
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def CustomerId(self):
        """客户号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """客户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def ReviewTime(self):
        """复核时间
        :rtype: str
        """
        return self._ReviewTime

    @ReviewTime.setter
    def ReviewTime(self, ReviewTime):
        self._ReviewTime = ReviewTime

    @property
    def MachineResult(self):
        """算法识别结果
        :rtype: str
        """
        return self._MachineResult

    @MachineResult.setter
    def MachineResult(self, MachineResult):
        self._MachineResult = MachineResult

    @property
    def ManualResult(self):
        """人工复核结果
        :rtype: str
        """
        return self._ManualResult

    @ManualResult.setter
    def ManualResult(self, ManualResult):
        self._ManualResult = ManualResult

    @property
    def Metrics(self):
        """结构化对比指标数据
        :rtype: :class:`tencentcloud.cii.v20210408.models.CompareMetricsData`
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def NewItems(self):
        """新增项
        :rtype: str
        """
        return self._NewItems

    @NewItems.setter
    def NewItems(self, NewItems):
        self._NewItems = NewItems

    @property
    def ModifyItems(self):
        """修改项
        :rtype: str
        """
        return self._ModifyItems

    @ModifyItems.setter
    def ModifyItems(self, ModifyItems):
        self._ModifyItems = ModifyItems

    @property
    def SubTaskId(self):
        """子任务号
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def AllTasks(self):
        """所有的子任务
        :rtype: list of ReviewDataTaskInfo
        """
        return self._AllTasks

    @AllTasks.setter
    def AllTasks(self, AllTasks):
        self._AllTasks = AllTasks

    @property
    def TaskType(self):
        """任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._MainTaskId = params.get("MainTaskId")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._ReviewTime = params.get("ReviewTime")
        self._MachineResult = params.get("MachineResult")
        self._ManualResult = params.get("ManualResult")
        if params.get("Metrics") is not None:
            self._Metrics = CompareMetricsData()
            self._Metrics._deserialize(params.get("Metrics"))
        self._NewItems = params.get("NewItems")
        self._ModifyItems = params.get("ModifyItems")
        self._SubTaskId = params.get("SubTaskId")
        if params.get("AllTasks") is not None:
            self._AllTasks = []
            for item in params.get("AllTasks"):
                obj = ReviewDataTaskInfo()
                obj._deserialize(item)
                self._AllTasks.append(obj)
        self._TaskType = params.get("TaskType")
        self._RequestId = params.get("RequestId")


class DescribeStructureDifferenceRequest(AbstractModel):
    """DescribeStructureDifference请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 主任务号
        :type MainTaskId: str
        :param _SubTaskId: 子任务号
        :type SubTaskId: str
        """
        self._MainTaskId = None
        self._SubTaskId = None

    @property
    def MainTaskId(self):
        """主任务号
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def SubTaskId(self):
        """子任务号
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._SubTaskId = params.get("SubTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureDifferenceResponse(AbstractModel):
    """DescribeStructureDifference返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 主任务号
        :type MainTaskId: str
        :param _Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Results: 差异的结果数组
        :type Results: list of PerStructDifference
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MainTaskId = None
        self._Status = None
        self._Results = None
        self._RequestId = None

    @property
    def MainTaskId(self):
        """主任务号
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def Status(self):
        """结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Results(self):
        """差异的结果数组
        :rtype: list of PerStructDifference
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._Status = params.get("Status")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = PerStructDifference()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStructureResultRequest(AbstractModel):
    """DescribeStructureResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 创建任务时返回的主任务ID
        :type MainTaskId: str
        """
        self._MainTaskId = None

    @property
    def MainTaskId(self):
        """创建任务时返回的主任务ID
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureResultResponse(AbstractModel):
    """DescribeStructureResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param _Results: 结构化结果
        :type Results: list of StructureResultObject
        :param _MainTaskId: 主任务ID
        :type MainTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Results = None
        self._MainTaskId = None
        self._RequestId = None

    @property
    def Status(self):
        """结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Results(self):
        """结构化结果
        :rtype: list of StructureResultObject
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def MainTaskId(self):
        """主任务ID
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = StructureResultObject()
                obj._deserialize(item)
                self._Results.append(obj)
        self._MainTaskId = params.get("MainTaskId")
        self._RequestId = params.get("RequestId")


class DescribeStructureTaskResultRequest(AbstractModel):
    """DescribeStructureTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 结构化任务ID
        :type MainTaskId: str
        """
        self._MainTaskId = None

    @property
    def MainTaskId(self):
        """结构化任务ID
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureTaskResultResponse(AbstractModel):
    """DescribeStructureTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param _Results: 结构化识别结果数组，每个数组元素对应一个图片的结构化结果，顺序和输入参数的ImageList或FileList对应。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of ResultObject
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Results = None
        self._RequestId = None

    @property
    def Status(self):
        """结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Results(self):
        """结构化识别结果数组，每个数组元素对应一个图片的结构化结果，顺序和输入参数的ImageList或FileList对应。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResultObject
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ResultObject()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUnderwriteTaskRequest(AbstractModel):
    """DescribeUnderwriteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnderwriteTaskId: 任务ID
        :type UnderwriteTaskId: str
        """
        self._UnderwriteTaskId = None

    @property
    def UnderwriteTaskId(self):
        """任务ID
        :rtype: str
        """
        return self._UnderwriteTaskId

    @UnderwriteTaskId.setter
    def UnderwriteTaskId(self, UnderwriteTaskId):
        self._UnderwriteTaskId = UnderwriteTaskId


    def _deserialize(self, params):
        self._UnderwriteTaskId = params.get("UnderwriteTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnderwriteTaskResponse(AbstractModel):
    """DescribeUnderwriteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 腾讯云主账号ID
        :type Uin: str
        :param _SubAccountUin: 操作人子账户ID
        :type SubAccountUin: str
        :param _PolicyId: 保单ID
        :type PolicyId: str
        :param _MainTaskId: 主任务ID
        :type MainTaskId: str
        :param _UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        :param _Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param _UnderwriteResults: 核保结果
        :type UnderwriteResults: list of UnderwriteOutput
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._SubAccountUin = None
        self._PolicyId = None
        self._MainTaskId = None
        self._UnderwriteTaskId = None
        self._Status = None
        self._UnderwriteResults = None
        self._RequestId = None

    @property
    def Uin(self):
        """腾讯云主账号ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        """操作人子账户ID
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def PolicyId(self):
        """保单ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def MainTaskId(self):
        """主任务ID
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def UnderwriteTaskId(self):
        """核保任务ID
        :rtype: str
        """
        return self._UnderwriteTaskId

    @UnderwriteTaskId.setter
    def UnderwriteTaskId(self, UnderwriteTaskId):
        self._UnderwriteTaskId = UnderwriteTaskId

    @property
    def Status(self):
        """结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnderwriteResults(self):
        """核保结果
        :rtype: list of UnderwriteOutput
        """
        return self._UnderwriteResults

    @UnderwriteResults.setter
    def UnderwriteResults(self, UnderwriteResults):
        self._UnderwriteResults = UnderwriteResults

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._PolicyId = params.get("PolicyId")
        self._MainTaskId = params.get("MainTaskId")
        self._UnderwriteTaskId = params.get("UnderwriteTaskId")
        self._Status = params.get("Status")
        if params.get("UnderwriteResults") is not None:
            self._UnderwriteResults = []
            for item in params.get("UnderwriteResults"):
                obj = UnderwriteOutput()
                obj._deserialize(item)
                self._UnderwriteResults.append(obj)
        self._RequestId = params.get("RequestId")


class InsuranceResult(AbstractModel):
    """包含险种的各个核保结论

    """

    def __init__(self):
        r"""
        :param _InsuranceType: 险种:CriticalDiseaseInsurance(重疾险);LifeInsurance(寿险);AccidentInsurance(意外险);MedicalInsurance(医疗险)
        :type InsuranceType: str
        :param _Result: 对应险种的机器核保结果
        :type Result: list of MachinePredict
        """
        self._InsuranceType = None
        self._Result = None

    @property
    def InsuranceType(self):
        """险种:CriticalDiseaseInsurance(重疾险);LifeInsurance(寿险);AccidentInsurance(意外险);MedicalInsurance(医疗险)
        :rtype: str
        """
        return self._InsuranceType

    @InsuranceType.setter
    def InsuranceType(self, InsuranceType):
        self._InsuranceType = InsuranceType

    @property
    def Result(self):
        """对应险种的机器核保结果
        :rtype: list of MachinePredict
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._InsuranceType = params.get("InsuranceType")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = MachinePredict()
                obj._deserialize(item)
                self._Result.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Location(AbstractModel):
    """位置信息

    """

    def __init__(self):
        r"""
        :param _Points: 位置信息
        :type Points: list of Point
        """
        self._Points = None

    @property
    def Points(self):
        """位置信息
        :rtype: list of Point
        """
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = Point()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachinePredict(AbstractModel):
    """机器核保预测结果

    """

    def __init__(self):
        r"""
        :param _Title: 核保引擎名称
        :type Title: str
        :param _Conclusion: 核保结论：加费、承保、拒保、延期、除外、加费+除外
        :type Conclusion: str
        :param _Explanation: AI决策树解释
        :type Explanation: list of UnderwriteItem
        :param _Disease: 疾病指标
        :type Disease: list of UnderwriteItem
        :param _Laboratory: 检查异常
        :type Laboratory: list of UnderwriteItem
        """
        self._Title = None
        self._Conclusion = None
        self._Explanation = None
        self._Disease = None
        self._Laboratory = None

    @property
    def Title(self):
        """核保引擎名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Conclusion(self):
        """核保结论：加费、承保、拒保、延期、除外、加费+除外
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def Explanation(self):
        """AI决策树解释
        :rtype: list of UnderwriteItem
        """
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation

    @property
    def Disease(self):
        """疾病指标
        :rtype: list of UnderwriteItem
        """
        return self._Disease

    @Disease.setter
    def Disease(self, Disease):
        self._Disease = Disease

    @property
    def Laboratory(self):
        """检查异常
        :rtype: list of UnderwriteItem
        """
        return self._Laboratory

    @Laboratory.setter
    def Laboratory(self, Laboratory):
        self._Laboratory = Laboratory


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Conclusion = params.get("Conclusion")
        if params.get("Explanation") is not None:
            self._Explanation = []
            for item in params.get("Explanation"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self._Explanation.append(obj)
        if params.get("Disease") is not None:
            self._Disease = []
            for item in params.get("Disease"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self._Disease.append(obj)
        if params.get("Laboratory") is not None:
            self._Laboratory = []
            for item in params.get("Laboratory"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self._Laboratory.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineUnderwriteOutput(AbstractModel):
    """机器核保输出

    """

    def __init__(self):
        r"""
        :param _CustomerId: 客户号
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _Results: 各个险种的结果
        :type Results: list of InsuranceResult
        """
        self._CustomerId = None
        self._CustomerName = None
        self._Results = None

    @property
    def CustomerId(self):
        """客户号
        :rtype: str
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """客户姓名
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def Results(self):
        """各个险种的结果
        :rtype: list of InsuranceResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = InsuranceResult()
                obj._deserialize(item)
                self._Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrRecognise(AbstractModel):
    """Ocr识别结果

    """

    def __init__(self):
        r"""
        :param _OriginalField: 原文字段
        :type OriginalField: str
        :param _Value: 识别结果
        :type Value: str
        :param _Confidence: 置信度
        :type Confidence: float
        :param _Location: 位置信息
        :type Location: :class:`tencentcloud.cii.v20210408.models.Location`
        :param _Field: 字段名
        :type Field: str
        """
        self._OriginalField = None
        self._Value = None
        self._Confidence = None
        self._Location = None
        self._Field = None

    @property
    def OriginalField(self):
        """原文字段
        :rtype: str
        """
        return self._OriginalField

    @OriginalField.setter
    def OriginalField(self, OriginalField):
        self._OriginalField = OriginalField

    @property
    def Value(self):
        """识别结果
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Confidence(self):
        """置信度
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Location(self):
        """位置信息
        :rtype: :class:`tencentcloud.cii.v20210408.models.Location`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Field(self):
        """字段名
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field


    def _deserialize(self, params):
        self._OriginalField = params.get("OriginalField")
        self._Value = params.get("Value")
        self._Confidence = params.get("Confidence")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._Field = params.get("Field")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PerStructDifference(AbstractModel):
    """复核差异接口的每一份报告的差异结果

    """

    def __init__(self):
        r"""
        :param _SubTaskId: 子任务ID
        :type SubTaskId: str
        :param _TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param _ModifyItems: 修改的项
        :type ModifyItems: list of StructureModifyItem
        :param _NewItems: 新增的项
        :type NewItems: list of StructureOneItem
        :param _RemoveItems: 删除的项
        :type RemoveItems: list of StructureOneItem
        """
        self._SubTaskId = None
        self._TaskType = None
        self._ModifyItems = None
        self._NewItems = None
        self._RemoveItems = None

    @property
    def SubTaskId(self):
        """子任务ID
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def TaskType(self):
        """任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ModifyItems(self):
        """修改的项
        :rtype: list of StructureModifyItem
        """
        return self._ModifyItems

    @ModifyItems.setter
    def ModifyItems(self, ModifyItems):
        self._ModifyItems = ModifyItems

    @property
    def NewItems(self):
        """新增的项
        :rtype: list of StructureOneItem
        """
        return self._NewItems

    @NewItems.setter
    def NewItems(self, NewItems):
        self._NewItems = NewItems

    @property
    def RemoveItems(self):
        """删除的项
        :rtype: list of StructureOneItem
        """
        return self._RemoveItems

    @RemoveItems.setter
    def RemoveItems(self, RemoveItems):
        self._RemoveItems = RemoveItems


    def _deserialize(self, params):
        self._SubTaskId = params.get("SubTaskId")
        self._TaskType = params.get("TaskType")
        if params.get("ModifyItems") is not None:
            self._ModifyItems = []
            for item in params.get("ModifyItems"):
                obj = StructureModifyItem()
                obj._deserialize(item)
                self._ModifyItems.append(obj)
        if params.get("NewItems") is not None:
            self._NewItems = []
            for item in params.get("NewItems"):
                obj = StructureOneItem()
                obj._deserialize(item)
                self._NewItems.append(obj)
        if params.get("RemoveItems") is not None:
            self._RemoveItems = []
            for item in params.get("RemoveItems"):
                obj = StructureOneItem()
                obj._deserialize(item)
                self._RemoveItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """点信息

    """

    def __init__(self):
        r"""
        :param _XCoordinate: x坐标
        :type XCoordinate: int
        :param _YCoordinate: y坐标
        :type YCoordinate: int
        :param _Page: 页码
        :type Page: int
        """
        self._XCoordinate = None
        self._YCoordinate = None
        self._Page = None

    @property
    def XCoordinate(self):
        """x坐标
        :rtype: int
        """
        return self._XCoordinate

    @XCoordinate.setter
    def XCoordinate(self, XCoordinate):
        self._XCoordinate = XCoordinate

    @property
    def YCoordinate(self):
        """y坐标
        :rtype: int
        """
        return self._YCoordinate

    @YCoordinate.setter
    def YCoordinate(self, YCoordinate):
        self._YCoordinate = YCoordinate

    @property
    def Page(self):
        """页码
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._XCoordinate = params.get("XCoordinate")
        self._YCoordinate = params.get("YCoordinate")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultObject(AbstractModel):
    """用于返回结构化任务结果

    """

    def __init__(self):
        r"""
        :param _Quality: 图片质量分
        :type Quality: float
        :param _StructureResult: 由结构化算法结构化json转换的字符串，具体协议参见算法结构化结果协议
        :type StructureResult: str
        :param _ReportType: 报告分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: list of ClassifyInfo
        """
        self._Quality = None
        self._StructureResult = None
        self._ReportType = None

    @property
    def Quality(self):
        """图片质量分
        :rtype: float
        """
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality

    @property
    def StructureResult(self):
        """由结构化算法结构化json转换的字符串，具体协议参见算法结构化结果协议
        :rtype: str
        """
        return self._StructureResult

    @StructureResult.setter
    def StructureResult(self, StructureResult):
        self._StructureResult = StructureResult

    @property
    def ReportType(self):
        """报告分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClassifyInfo
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        self._Quality = params.get("Quality")
        self._StructureResult = params.get("StructureResult")
        if params.get("ReportType") is not None:
            self._ReportType = []
            for item in params.get("ReportType"):
                obj = ClassifyInfo()
                obj._deserialize(item)
                self._ReportType.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReviewDataTaskInfo(AbstractModel):
    """人工复核数据的子任务信息

    """

    def __init__(self):
        r"""
        :param _MainTaskId: 主任务号
        :type MainTaskId: str
        :param _SubTaskId: 子任务号
        :type SubTaskId: str
        :param _TaskName: 任务名
        :type TaskName: str
        :param _TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        """
        self._MainTaskId = None
        self._SubTaskId = None
        self._TaskName = None
        self._TaskType = None

    @property
    def MainTaskId(self):
        """主任务号
        :rtype: str
        """
        return self._MainTaskId

    @MainTaskId.setter
    def MainTaskId(self, MainTaskId):
        self._MainTaskId = MainTaskId

    @property
    def SubTaskId(self):
        """子任务号
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def TaskName(self):
        """任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        """任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._MainTaskId = params.get("MainTaskId")
        self._SubTaskId = params.get("SubTaskId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureModifyItem(AbstractModel):
    """结构化复核差异接口的修改的项

    """

    def __init__(self):
        r"""
        :param _Path: 修改的字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Machine: 机器结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Machine: str
        :param _Manual: 人工结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Manual: str
        """
        self._Path = None
        self._Machine = None
        self._Manual = None

    @property
    def Path(self):
        """修改的字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Machine(self):
        """机器结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def Manual(self):
        """人工结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Manual

    @Manual.setter
    def Manual(self, Manual):
        self._Manual = Manual


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Machine = params.get("Machine")
        self._Manual = params.get("Manual")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureOneItem(AbstractModel):
    """复核差异接口的新增或者删除的项

    """

    def __init__(self):
        r"""
        :param _Path: 新字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Value: 字段的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Path = None
        self._Value = None

    @property
    def Path(self):
        """新字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Value(self):
        """字段的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureResultObject(AbstractModel):
    """结构化结果

    """

    def __init__(self):
        r"""
        :param _Code: 0表示正常返回；1代表结果未生成；2代表任务执行失败
        :type Code: int
        :param _TaskType: 报告类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param _StructureResult: 结构化结果
        :type StructureResult: str
        :param _SubTaskId: 子任务ID
        :type SubTaskId: str
        :param _TaskFiles: 任务文件列表
        :type TaskFiles: list of str
        :param _ResultFields: 结构化字段结果数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultFields: list of OcrRecognise
        """
        self._Code = None
        self._TaskType = None
        self._StructureResult = None
        self._SubTaskId = None
        self._TaskFiles = None
        self._ResultFields = None

    @property
    def Code(self):
        """0表示正常返回；1代表结果未生成；2代表任务执行失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def TaskType(self):
        """报告类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def StructureResult(self):
        """结构化结果
        :rtype: str
        """
        return self._StructureResult

    @StructureResult.setter
    def StructureResult(self, StructureResult):
        self._StructureResult = StructureResult

    @property
    def SubTaskId(self):
        """子任务ID
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def TaskFiles(self):
        """任务文件列表
        :rtype: list of str
        """
        return self._TaskFiles

    @TaskFiles.setter
    def TaskFiles(self, TaskFiles):
        self._TaskFiles = TaskFiles

    @property
    def ResultFields(self):
        """结构化字段结果数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OcrRecognise
        """
        return self._ResultFields

    @ResultFields.setter
    def ResultFields(self, ResultFields):
        self._ResultFields = ResultFields


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._TaskType = params.get("TaskType")
        self._StructureResult = params.get("StructureResult")
        self._SubTaskId = params.get("SubTaskId")
        self._TaskFiles = params.get("TaskFiles")
        if params.get("ResultFields") is not None:
            self._ResultFields = []
            for item in params.get("ResultFields"):
                obj = OcrRecognise()
                obj._deserialize(item)
                self._ResultFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteConclusion(AbstractModel):
    """核保结论 机器结论和人工结论统一数据结构

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Conclusion: 结论
        :type Conclusion: str
        :param _Explanation: 解释
        :type Explanation: str
        """
        self._Type = None
        self._Conclusion = None
        self._Explanation = None

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
    def Conclusion(self):
        """结论
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def Explanation(self):
        """解释
        :rtype: str
        """
        return self._Explanation

    @Explanation.setter
    def Explanation(self, Explanation):
        self._Explanation = Explanation


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Conclusion = params.get("Conclusion")
        self._Explanation = params.get("Explanation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteItem(AbstractModel):
    """机器核保结论子项

    """

    def __init__(self):
        r"""
        :param _Name: 字段名
        :type Name: str
        :param _Result: 结果
        :type Result: str
        :param _Value: 风险值或者说明
        :type Value: str
        :param _Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        :param _ReportDate: 报告时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportDate: list of str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _InspectProject: 检查项目
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectProject: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _OriginName: 原名
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginName: str
        :param _YinYang: 阴阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type YinYang: str
        """
        self._Name = None
        self._Result = None
        self._Value = None
        self._Range = None
        self._ReportDate = None
        self._FileType = None
        self._InspectProject = None
        self._Unit = None
        self._OriginName = None
        self._YinYang = None

    @property
    def Name(self):
        """字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        """结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Value(self):
        """风险值或者说明
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Range(self):
        """参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def ReportDate(self):
        """报告时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ReportDate

    @ReportDate.setter
    def ReportDate(self, ReportDate):
        self._ReportDate = ReportDate

    @property
    def FileType(self):
        """文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def InspectProject(self):
        """检查项目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InspectProject

    @InspectProject.setter
    def InspectProject(self, InspectProject):
        self._InspectProject = InspectProject

    @property
    def Unit(self):
        """单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def OriginName(self):
        """原名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginName

    @OriginName.setter
    def OriginName(self, OriginName):
        self._OriginName = OriginName

    @property
    def YinYang(self):
        """阴阳性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._YinYang

    @YinYang.setter
    def YinYang(self, YinYang):
        self._YinYang = YinYang


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._Value = params.get("Value")
        self._Range = params.get("Range")
        self._ReportDate = params.get("ReportDate")
        self._FileType = params.get("FileType")
        self._InspectProject = params.get("InspectProject")
        self._Unit = params.get("Unit")
        self._OriginName = params.get("OriginName")
        self._YinYang = params.get("YinYang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteOutput(AbstractModel):
    """核保结果输出

    """

    def __init__(self):
        r"""
        :param _CustomerId: 客户ID
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _Results: 结果
        :type Results: list of InsuranceResult
        :param _ReviewTime: 复核时间
        :type ReviewTime: str
        :param _ManualDetail: 人工复核结果
        :type ManualDetail: list of UnderwriteConclusion
        """
        self._CustomerId = None
        self._CustomerName = None
        self._Results = None
        self._ReviewTime = None
        self._ManualDetail = None

    @property
    def CustomerId(self):
        """客户ID
        :rtype: str
        """
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def CustomerName(self):
        """客户姓名
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def Results(self):
        """结果
        :rtype: list of InsuranceResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ReviewTime(self):
        """复核时间
        :rtype: str
        """
        return self._ReviewTime

    @ReviewTime.setter
    def ReviewTime(self, ReviewTime):
        self._ReviewTime = ReviewTime

    @property
    def ManualDetail(self):
        """人工复核结果
        :rtype: list of UnderwriteConclusion
        """
        return self._ManualDetail

    @ManualDetail.setter
    def ManualDetail(self, ManualDetail):
        self._ManualDetail = ManualDetail


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = InsuranceResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._ReviewTime = params.get("ReviewTime")
        if params.get("ManualDetail") is not None:
            self._ManualDetail = []
            for item in params.get("ManualDetail"):
                obj = UnderwriteConclusion()
                obj._deserialize(item)
                self._ManualDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadMedicalFileRequest(AbstractModel):
    """UploadMedicalFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _File: 文件的字节内容。File与FileURL有一个不为空即可，若FileURL参数也存在，会只取File的内容。
        :type File: binary
        :param _FileURL: 文件的URL地址。File与FileURL不能同时为空，若File参数也存在，会只取File的内容。
        :type FileURL: str
        """
        self._File = None
        self._FileURL = None

    @property
    def File(self):
        """文件的字节内容。File与FileURL有一个不为空即可，若FileURL参数也存在，会只取File的内容。
        :rtype: binary
        """
        return self._File

    @File.setter
    def File(self, File):
        self._File = File

    @property
    def FileURL(self):
        """文件的URL地址。File与FileURL不能同时为空，若File参数也存在，会只取File的内容。
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL


    def _deserialize(self, params):
        self._File = params.get("File")
        self._FileURL = params.get("FileURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadMedicalFileResponse(AbstractModel):
    """UploadMedicalFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileKey: 文件存储的key，可以用来创建结构化任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileKey = None
        self._RequestId = None

    @property
    def FileKey(self):
        """文件存储的key，可以用来创建结构化任务。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileKey = params.get("FileKey")
        self._RequestId = params.get("RequestId")