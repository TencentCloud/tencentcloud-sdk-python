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
        


class CreateStructureTaskInfo(AbstractModel):
    """创建结构化任务子任务信息

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型
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


class CreateStructureTaskTestRequest(AbstractModel):
    """CreateStructureTaskTest请求参数结构体

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
        


class CreateStructureTaskTestResponse(AbstractModel):
    """CreateStructureTaskTest返回参数结构体

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
                obj = StructureResultObject()
                obj._deserialize(item)
                self.Results.append(obj)
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


class DescribeStructureTaskResultTestRequest(AbstractModel):
    """DescribeStructureTaskResultTest请求参数结构体

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
        


class DescribeStructureTaskResultTestResponse(AbstractModel):
    """DescribeStructureTaskResultTest返回参数结构体

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


class ResultObject(AbstractModel):
    """用于返回结构化任务结果

    """

    def __init__(self):
        r"""
        :param Quality: 图片质量分
        :type Quality: float
        :param StructureResult: 由结构化算法结构化json转换的字符串，具体协议参见算法结构化结果协议
        :type StructureResult: str
        """
        self.Quality = None
        self.StructureResult = None


    def _deserialize(self, params):
        self.Quality = params.get("Quality")
        self.StructureResult = params.get("StructureResult")
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
        :param TaskType: 任务类型
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
        


class StructureResultObject(AbstractModel):
    """结构化结果

    """

    def __init__(self):
        r"""
        :param Code: 0表示正常返回
        :type Code: int
        :param TaskType: 报告类型
        :type TaskType: str
        :param StructureResult: 结构化结果
        :type StructureResult: str
        """
        self.Code = None
        self.TaskType = None
        self.StructureResult = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.TaskType = params.get("TaskType")
        self.StructureResult = params.get("StructureResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        