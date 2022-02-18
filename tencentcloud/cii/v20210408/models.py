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
        :param MainTaskId: 主任务id
        :type MainTaskId: str
        :param TaskInfos: 子任务信息数组
        :type TaskInfos: list of CreateStructureTaskInfo
        """
        self.MainTaskId = None
        self.TaskInfos = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateStructureTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSubStructureTasksResponse(AbstractModel):
    """AddSubStructureTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubTaskIds: 增量子任务id数组
        :type SubTaskIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubTaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubTaskIds = params.get("SubTaskIds")
        self.RequestId = params.get("RequestId")


class ClassifiedReports(AbstractModel):
    """报告分类结果

    """

    def __init__(self):
        r"""
        :param ReportType: 报告类型
        :type ReportType: str
        :param FileList: 文件列表
        :type FileList: list of str
        """
        self.ReportType = None
        self.FileList = None


    def _deserialize(self, params):
        self.ReportType = params.get("ReportType")
        self.FileList = params.get("FileList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyInfo(AbstractModel):
    """报告分类信息

    """

    def __init__(self):
        r"""
        :param FirstClass: 一级分类
        :type FirstClass: str
        :param SecondClass: 二级分类
        :type SecondClass: str
        :param ThirdClass: 三级分类
        :type ThirdClass: str
        :param FirstClassId: 一级分类序号
        :type FirstClassId: int
        :param SecondClassId: 二级分类序号
        :type SecondClassId: int
        :param ThirdClassId: 三级分类序号
        :type ThirdClassId: int
        """
        self.FirstClass = None
        self.SecondClass = None
        self.ThirdClass = None
        self.FirstClassId = None
        self.SecondClassId = None
        self.ThirdClassId = None


    def _deserialize(self, params):
        self.FirstClass = params.get("FirstClass")
        self.SecondClass = params.get("SecondClass")
        self.ThirdClass = params.get("ThirdClass")
        self.FirstClassId = params.get("FirstClassId")
        self.SecondClassId = params.get("SecondClassId")
        self.ThirdClassId = params.get("ThirdClassId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareMetricsData(AbstractModel):
    """结构化对比指标（准确率/召回率）数据

    """

    def __init__(self):
        r"""
        :param ShortStructAccuracy: 短文准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortStructAccuracy: str
        :param ShortStructRecall: 短文召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortStructRecall: str
        :param LongStructAccuracy: 长文结构化准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongStructAccuracy: str
        :param LongStructRecall: 长文结构化召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongStructRecall: str
        :param LongContentAccuracy: 长文提取准确率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongContentAccuracy: str
        :param LongContentRecall: 长文提取召回率
注意：此字段可能返回 null，表示取不到有效值。
        :type LongContentRecall: str
        """
        self.ShortStructAccuracy = None
        self.ShortStructRecall = None
        self.LongStructAccuracy = None
        self.LongStructRecall = None
        self.LongContentAccuracy = None
        self.LongContentRecall = None


    def _deserialize(self, params):
        self.ShortStructAccuracy = params.get("ShortStructAccuracy")
        self.ShortStructRecall = params.get("ShortStructRecall")
        self.LongStructAccuracy = params.get("LongStructAccuracy")
        self.LongStructRecall = params.get("LongStructRecall")
        self.LongContentAccuracy = params.get("LongContentAccuracy")
        self.LongContentRecall = params.get("LongContentRecall")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskInfo(AbstractModel):
    """创建自动分类的结构化任务子任务信息

    """

    def __init__(self):
        r"""
        :param FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param CustomerId: 客户号
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        """
        self.FileList = None
        self.CustomerId = None
        self.CustomerName = None
        self.ImageList = None


    def _deserialize(self, params):
        self.FileList = params.get("FileList")
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        self.ImageList = params.get("ImageList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskRequest(AbstractModel):
    """CreateAutoClassifyStructureTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param TaskInfos: 创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :type TaskInfos: list of CreateAutoClassifyStructureTaskInfo
        :param PolicyId: 保单号
        :type PolicyId: str
        :param TriggerType: 核保触发方式
Auto 自动
Manual 手动
        :type TriggerType: str
        :param InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param CallbackUrl: 回调地址，接收Post请求传送结果
        :type CallbackUrl: str
        """
        self.ServiceType = None
        self.TaskInfos = None
        self.PolicyId = None
        self.TriggerType = None
        self.InsuranceTypes = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateAutoClassifyStructureTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.TriggerType = params.get("TriggerType")
        self.InsuranceTypes = params.get("InsuranceTypes")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoClassifyStructureTaskResponse(AbstractModel):
    """CreateAutoClassifyStructureTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 创建的主任务号，用于查询结果
        :type MainTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MainTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.RequestId = params.get("RequestId")


class CreateStructureTaskInfo(AbstractModel):
    """创建结构化任务子任务信息

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param CustomerId: 客户号
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        :param Year: 报告年份
        :type Year: str
        """
        self.TaskType = None
        self.FileList = None
        self.CustomerId = None
        self.CustomerName = None
        self.ImageList = None
        self.Year = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.FileList = params.get("FileList")
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        self.ImageList = params.get("ImageList")
        self.Year = params.get("Year")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStructureTaskRequest(AbstractModel):
    """CreateStructureTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param TaskInfos: 创建任务时可以上传多个报告，后台生成多个识别子任务，子任务的详细信息
        :type TaskInfos: list of CreateStructureTaskInfo
        :param PolicyId: 保单号
        :type PolicyId: str
        :param TriggerType: 核保触发方式
Auto 自动
Manual 手动
        :type TriggerType: str
        :param InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param CallbackUrl: 回调地址，接收Post请求传送结果
        :type CallbackUrl: str
        """
        self.ServiceType = None
        self.TaskInfos = None
        self.PolicyId = None
        self.TriggerType = None
        self.InsuranceTypes = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = CreateStructureTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.TriggerType = params.get("TriggerType")
        self.InsuranceTypes = params.get("InsuranceTypes")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStructureTaskResponse(AbstractModel):
    """CreateStructureTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 创建的主任务号，用于查询结果
        :type MainTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MainTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.RequestId = params.get("RequestId")


class CreateUnderwriteTaskByIdRequest(AbstractModel):
    """CreateUnderwriteTaskById请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskIds: 主任务ID数组，
        :type MainTaskIds: list of str
        :param CallbackUrl: 回调地址，可不传（提供轮询机制）。
        :type CallbackUrl: str
        """
        self.MainTaskIds = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.MainTaskIds = params.get("MainTaskIds")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnderwriteTaskByIdResponse(AbstractModel):
    """CreateUnderwriteTaskById返回参数结构体

    """

    def __init__(self):
        r"""
        :param UnderwriteTaskIds: 核保任务ID数据
        :type UnderwriteTaskIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UnderwriteTaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnderwriteTaskIds = params.get("UnderwriteTaskIds")
        self.RequestId = params.get("RequestId")


class DescribeMachineUnderwriteRequest(AbstractModel):
    """DescribeMachineUnderwrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        """
        self.UnderwriteTaskId = None


    def _deserialize(self, params):
        self.UnderwriteTaskId = params.get("UnderwriteTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineUnderwriteResponse(AbstractModel):
    """DescribeMachineUnderwrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 腾讯云主账号ID
        :type Uin: str
        :param SubAccountUin: 操作人子账户ID
        :type SubAccountUin: str
        :param PolicyId: 保单ID
        :type PolicyId: str
        :param MainTaskId: 主任务ID
        :type MainTaskId: str
        :param UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        :param Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param UnderwriteResults: 机器核保结果
        :type UnderwriteResults: list of MachineUnderwriteOutput
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.SubAccountUin = None
        self.PolicyId = None
        self.MainTaskId = None
        self.UnderwriteTaskId = None
        self.Status = None
        self.UnderwriteResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        self.PolicyId = params.get("PolicyId")
        self.MainTaskId = params.get("MainTaskId")
        self.UnderwriteTaskId = params.get("UnderwriteTaskId")
        self.Status = params.get("Status")
        if params.get("UnderwriteResults") is not None:
            self.UnderwriteResults = []
            for item in params.get("UnderwriteResults"):
                obj = MachineUnderwriteOutput()
                obj._deserialize(item)
                self.UnderwriteResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQualityScoreRequest(AbstractModel):
    """DescribeQualityScore请求参数结构体

    """

    def __init__(self):
        r"""
        :param File: 文件二进制数据
        :type File: binary
        """
        self.File = None


    def _deserialize(self, params):
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityScoreResponse(AbstractModel):
    """DescribeQualityScore返回参数结构体

    """

    def __init__(self):
        r"""
        :param QualityScore: 质量分
        :type QualityScore: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QualityScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QualityScore = params.get("QualityScore")
        self.RequestId = params.get("RequestId")


class DescribeReportClassifyRequest(AbstractModel):
    """DescribeReportClassify请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceType: 服务类型
Structured 仅结构化
Underwrite 结构化+核保
        :type ServiceType: str
        :param FileList: 文件地址数组
        :type FileList: list of str
        """
        self.ServiceType = None
        self.FileList = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.FileList = params.get("FileList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportClassifyResponse(AbstractModel):
    """DescribeReportClassify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Reports: 报告分类结果
        :type Reports: list of ClassifiedReports
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Reports = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Reports") is not None:
            self.Reports = []
            for item in params.get("Reports"):
                obj = ClassifiedReports()
                obj._deserialize(item)
                self.Reports.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStructCompareDataRequest(AbstractModel):
    """DescribeStructCompareData请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 主任务号
        :type MainTaskId: str
        :param SubTaskId: 子任务号
        :type SubTaskId: str
        """
        self.MainTaskId = None
        self.SubTaskId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.SubTaskId = params.get("SubTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructCompareDataResponse(AbstractModel):
    """DescribeStructCompareData返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 保单号
        :type PolicyId: str
        :param MainTaskId: 主任务号
        :type MainTaskId: str
        :param CustomerId: 客户号
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerId: str
        :param CustomerName: 客户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerName: str
        :param ReviewTime: 复核时间
        :type ReviewTime: str
        :param MachineResult: 算法识别结果
        :type MachineResult: str
        :param ManualResult: 人工复核结果
        :type ManualResult: str
        :param Metrics: 结构化对比指标数据
        :type Metrics: :class:`tencentcloud.cii.v20210408.models.CompareMetricsData`
        :param NewItems: 新增项
        :type NewItems: str
        :param ModifyItems: 修改项
        :type ModifyItems: str
        :param SubTaskId: 子任务号
        :type SubTaskId: str
        :param AllTasks: 所有的子任务
        :type AllTasks: list of ReviewDataTaskInfo
        :param TaskType: 任务类型
        :type TaskType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.MainTaskId = None
        self.CustomerId = None
        self.CustomerName = None
        self.ReviewTime = None
        self.MachineResult = None
        self.ManualResult = None
        self.Metrics = None
        self.NewItems = None
        self.ModifyItems = None
        self.SubTaskId = None
        self.AllTasks = None
        self.TaskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.MainTaskId = params.get("MainTaskId")
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        self.ReviewTime = params.get("ReviewTime")
        self.MachineResult = params.get("MachineResult")
        self.ManualResult = params.get("ManualResult")
        if params.get("Metrics") is not None:
            self.Metrics = CompareMetricsData()
            self.Metrics._deserialize(params.get("Metrics"))
        self.NewItems = params.get("NewItems")
        self.ModifyItems = params.get("ModifyItems")
        self.SubTaskId = params.get("SubTaskId")
        if params.get("AllTasks") is not None:
            self.AllTasks = []
            for item in params.get("AllTasks"):
                obj = ReviewDataTaskInfo()
                obj._deserialize(item)
                self.AllTasks.append(obj)
        self.TaskType = params.get("TaskType")
        self.RequestId = params.get("RequestId")


class DescribeStructureDifferenceRequest(AbstractModel):
    """DescribeStructureDifference请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 主任务号
        :type MainTaskId: str
        :param SubTaskId: 子任务号
        :type SubTaskId: str
        """
        self.MainTaskId = None
        self.SubTaskId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.SubTaskId = params.get("SubTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureDifferenceResponse(AbstractModel):
    """DescribeStructureDifference返回参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 主任务号
        :type MainTaskId: str
        :param Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Results: 差异的结果数组
        :type Results: list of PerStructDifference
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MainTaskId = None
        self.Status = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.Status = params.get("Status")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = PerStructDifference()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStructureResultRequest(AbstractModel):
    """DescribeStructureResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 创建任务时返回的主任务ID
        :type MainTaskId: str
        """
        self.MainTaskId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureResultResponse(AbstractModel):
    """DescribeStructureResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param Results: 结构化结果
        :type Results: list of StructureResultObject
        :param MainTaskId: 主任务ID
        :type MainTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Results = None
        self.MainTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = StructureResultObject()
                obj._deserialize(item)
                self.Results.append(obj)
        self.MainTaskId = params.get("MainTaskId")
        self.RequestId = params.get("RequestId")


class DescribeStructureTaskResultRequest(AbstractModel):
    """DescribeStructureTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainTaskId: 结构化任务ID
        :type MainTaskId: str
        """
        self.MainTaskId = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStructureTaskResultResponse(AbstractModel):
    """DescribeStructureTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param Results: 结构化识别结果数组，每个数组元素对应一个图片的结构化结果，顺序和输入参数的ImageList或FileList对应。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of ResultObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ResultObject()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUnderwriteTaskRequest(AbstractModel):
    """DescribeUnderwriteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param UnderwriteTaskId: 任务ID
        :type UnderwriteTaskId: str
        """
        self.UnderwriteTaskId = None


    def _deserialize(self, params):
        self.UnderwriteTaskId = params.get("UnderwriteTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnderwriteTaskResponse(AbstractModel):
    """DescribeUnderwriteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 腾讯云主账号ID
        :type Uin: str
        :param SubAccountUin: 操作人子账户ID
        :type SubAccountUin: str
        :param PolicyId: 保单ID
        :type PolicyId: str
        :param MainTaskId: 主任务ID
        :type MainTaskId: str
        :param UnderwriteTaskId: 核保任务ID
        :type UnderwriteTaskId: str
        :param Status: 结果状态：
0：返回成功
1：结果未生成
2：结果生成失败
        :type Status: int
        :param UnderwriteResults: 核保结果
        :type UnderwriteResults: list of UnderwriteOutput
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.SubAccountUin = None
        self.PolicyId = None
        self.MainTaskId = None
        self.UnderwriteTaskId = None
        self.Status = None
        self.UnderwriteResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        self.PolicyId = params.get("PolicyId")
        self.MainTaskId = params.get("MainTaskId")
        self.UnderwriteTaskId = params.get("UnderwriteTaskId")
        self.Status = params.get("Status")
        if params.get("UnderwriteResults") is not None:
            self.UnderwriteResults = []
            for item in params.get("UnderwriteResults"):
                obj = UnderwriteOutput()
                obj._deserialize(item)
                self.UnderwriteResults.append(obj)
        self.RequestId = params.get("RequestId")


class InsuranceResult(AbstractModel):
    """包含险种的各个核保结论

    """

    def __init__(self):
        r"""
        :param InsuranceType: 险种:CriticalDiseaseInsurance(重疾险);LifeInsurance(寿险);AccidentInsurance(意外险);MedicalInsurance(医疗险)
        :type InsuranceType: str
        :param Result: 对应险种的机器核保结果
        :type Result: list of MachinePredict
        """
        self.InsuranceType = None
        self.Result = None


    def _deserialize(self, params):
        self.InsuranceType = params.get("InsuranceType")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MachinePredict()
                obj._deserialize(item)
                self.Result.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachinePredict(AbstractModel):
    """机器核保预测结果

    """

    def __init__(self):
        r"""
        :param Title: 核保引擎名称
        :type Title: str
        :param Conclusion: 核保结论：加费、承保、拒保、延期、除外、加费+除外
        :type Conclusion: str
        :param Explanation: AI决策树解释
        :type Explanation: list of UnderwriteItem
        :param Disease: 疾病指标
        :type Disease: list of UnderwriteItem
        :param Laboratory: 检查异常
        :type Laboratory: list of UnderwriteItem
        """
        self.Title = None
        self.Conclusion = None
        self.Explanation = None
        self.Disease = None
        self.Laboratory = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Conclusion = params.get("Conclusion")
        if params.get("Explanation") is not None:
            self.Explanation = []
            for item in params.get("Explanation"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self.Explanation.append(obj)
        if params.get("Disease") is not None:
            self.Disease = []
            for item in params.get("Disease"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self.Disease.append(obj)
        if params.get("Laboratory") is not None:
            self.Laboratory = []
            for item in params.get("Laboratory"):
                obj = UnderwriteItem()
                obj._deserialize(item)
                self.Laboratory.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineUnderwriteOutput(AbstractModel):
    """机器核保输出

    """

    def __init__(self):
        r"""
        :param CustomerId: 客户号
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param Results: 各个险种的结果
        :type Results: list of InsuranceResult
        """
        self.CustomerId = None
        self.CustomerName = None
        self.Results = None


    def _deserialize(self, params):
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = InsuranceResult()
                obj._deserialize(item)
                self.Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PerStructDifference(AbstractModel):
    """复核差异接口的每一份报告的差异结果

    """

    def __init__(self):
        r"""
        :param SubTaskId: 子任务ID
        :type SubTaskId: str
        :param TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param ModifyItems: 修改的项
        :type ModifyItems: list of StructureModifyItem
        :param NewItems: 新增的项
        :type NewItems: list of StructureOneItem
        :param RemoveItems: 删除的项
        :type RemoveItems: list of StructureOneItem
        """
        self.SubTaskId = None
        self.TaskType = None
        self.ModifyItems = None
        self.NewItems = None
        self.RemoveItems = None


    def _deserialize(self, params):
        self.SubTaskId = params.get("SubTaskId")
        self.TaskType = params.get("TaskType")
        if params.get("ModifyItems") is not None:
            self.ModifyItems = []
            for item in params.get("ModifyItems"):
                obj = StructureModifyItem()
                obj._deserialize(item)
                self.ModifyItems.append(obj)
        if params.get("NewItems") is not None:
            self.NewItems = []
            for item in params.get("NewItems"):
                obj = StructureOneItem()
                obj._deserialize(item)
                self.NewItems.append(obj)
        if params.get("RemoveItems") is not None:
            self.RemoveItems = []
            for item in params.get("RemoveItems"):
                obj = StructureOneItem()
                obj._deserialize(item)
                self.RemoveItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultObject(AbstractModel):
    """用于返回结构化任务结果

    """

    def __init__(self):
        r"""
        :param Quality: 图片质量分
        :type Quality: float
        :param StructureResult: 由结构化算法结构化json转换的字符串，具体协议参见算法结构化结果协议
        :type StructureResult: str
        :param ReportType: 报告分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: list of ClassifyInfo
        """
        self.Quality = None
        self.StructureResult = None
        self.ReportType = None


    def _deserialize(self, params):
        self.Quality = params.get("Quality")
        self.StructureResult = params.get("StructureResult")
        if params.get("ReportType") is not None:
            self.ReportType = []
            for item in params.get("ReportType"):
                obj = ClassifyInfo()
                obj._deserialize(item)
                self.ReportType.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReviewDataTaskInfo(AbstractModel):
    """人工复核数据的子任务信息

    """

    def __init__(self):
        r"""
        :param MainTaskId: 主任务号
        :type MainTaskId: str
        :param SubTaskId: 子任务号
        :type SubTaskId: str
        :param TaskName: 任务名
        :type TaskName: str
        :param TaskType: 任务类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        """
        self.MainTaskId = None
        self.SubTaskId = None
        self.TaskName = None
        self.TaskType = None


    def _deserialize(self, params):
        self.MainTaskId = params.get("MainTaskId")
        self.SubTaskId = params.get("SubTaskId")
        self.TaskName = params.get("TaskName")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureModifyItem(AbstractModel):
    """结构化复核差异接口的修改的项

    """

    def __init__(self):
        r"""
        :param Path: 修改的字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Machine: 机器结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Machine: str
        :param Manual: 人工结果的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Manual: str
        """
        self.Path = None
        self.Machine = None
        self.Manual = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Machine = params.get("Machine")
        self.Manual = params.get("Manual")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureOneItem(AbstractModel):
    """复核差异接口的新增或者删除的项

    """

    def __init__(self):
        r"""
        :param Path: 新字段的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Value: 字段的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Path = None
        self.Value = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StructureResultObject(AbstractModel):
    """结构化结果

    """

    def __init__(self):
        r"""
        :param Code: 0表示正常返回；1代表结果未生成；2代表任务执行失败
        :type Code: int
        :param TaskType: 报告类型:HealthReport(体检报告); BUltraReport(B超报告);MedCheckReport(检查报告);LaboratoryReport(检验报告); PathologyReport(病理报告);AdmissionReport(入院记录);DischargeReport(出院记录); DischargeSummary(出院小结);DiagnosisReport(诊断证明); MedicalRecordFront(病案首页);OperationReport(手术记录);OutpatientMedicalRecord(门诊病历)
        :type TaskType: str
        :param StructureResult: 结构化结果
        :type StructureResult: str
        :param SubTaskId: 子任务ID
        :type SubTaskId: str
        :param TaskFiles: 任务文件列表
        :type TaskFiles: list of str
        """
        self.Code = None
        self.TaskType = None
        self.StructureResult = None
        self.SubTaskId = None
        self.TaskFiles = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.TaskType = params.get("TaskType")
        self.StructureResult = params.get("StructureResult")
        self.SubTaskId = params.get("SubTaskId")
        self.TaskFiles = params.get("TaskFiles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteConclusion(AbstractModel):
    """核保结论 机器结论和人工结论统一数据结构

    """

    def __init__(self):
        r"""
        :param Type: 类型
        :type Type: str
        :param Conclusion: 结论
        :type Conclusion: str
        :param Explanation: 解释
        :type Explanation: str
        """
        self.Type = None
        self.Conclusion = None
        self.Explanation = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Conclusion = params.get("Conclusion")
        self.Explanation = params.get("Explanation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteItem(AbstractModel):
    """机器核保结论子项

    """

    def __init__(self):
        r"""
        :param Name: 字段名
        :type Name: str
        :param Result: 结果
        :type Result: str
        :param Value: 风险值或者说明
        :type Value: str
        :param Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        :param ReportDate: 报告时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportDate: list of str
        :param FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param InspectProject: 检查项目
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectProject: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param OriginName: 原名
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginName: str
        :param YinYang: 阴阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type YinYang: str
        """
        self.Name = None
        self.Result = None
        self.Value = None
        self.Range = None
        self.ReportDate = None
        self.FileType = None
        self.InspectProject = None
        self.Unit = None
        self.OriginName = None
        self.YinYang = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.Value = params.get("Value")
        self.Range = params.get("Range")
        self.ReportDate = params.get("ReportDate")
        self.FileType = params.get("FileType")
        self.InspectProject = params.get("InspectProject")
        self.Unit = params.get("Unit")
        self.OriginName = params.get("OriginName")
        self.YinYang = params.get("YinYang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnderwriteOutput(AbstractModel):
    """核保结果输出

    """

    def __init__(self):
        r"""
        :param CustomerId: 客户ID
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param Results: 结果
        :type Results: list of InsuranceResult
        :param ReviewTime: 复核时间
        :type ReviewTime: str
        :param ManualDetail: 人工复核结果
        :type ManualDetail: list of UnderwriteConclusion
        """
        self.CustomerId = None
        self.CustomerName = None
        self.Results = None
        self.ReviewTime = None
        self.ManualDetail = None


    def _deserialize(self, params):
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = InsuranceResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.ReviewTime = params.get("ReviewTime")
        if params.get("ManualDetail") is not None:
            self.ManualDetail = []
            for item in params.get("ManualDetail"):
                obj = UnderwriteConclusion()
                obj._deserialize(item)
                self.ManualDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadMedicalFileRequest(AbstractModel):
    """UploadMedicalFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param File: 文件的字节内容。File与FileURL有一个不为空即可，若FileURL参数也存在，会只取File的内容。
        :type File: binary
        :param FileURL: 文件的URL地址。File与FileURL不能同时为空，若File参数也存在，会只取File的内容。
        :type FileURL: str
        """
        self.File = None
        self.FileURL = None


    def _deserialize(self, params):
        self.File = params.get("File")
        self.FileURL = params.get("FileURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadMedicalFileResponse(AbstractModel):
    """UploadMedicalFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileKey: 文件存储的key，可以用来创建结构化任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileKey = params.get("FileKey")
        self.RequestId = params.get("RequestId")