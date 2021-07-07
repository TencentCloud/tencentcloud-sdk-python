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
        """
        :param ShortStructAccuracy: 短文准确率
        :type ShortStructAccuracy: str
        :param ShortStructRecall: 短文召回率
        :type ShortStructRecall: str
        :param LongStructAccuracy: 长文结构化准确率
        :type LongStructAccuracy: str
        :param LongStructRecall: 长文结构化召回率
        :type LongStructRecall: str
        :param LongContentAccuracy: 长文提取准确率
        :type LongContentAccuracy: str
        :param LongContentRecall: 长文提取召回率
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
        


class CreateStructureTaskRequest(AbstractModel):
    """CreateStructureTask请求参数结构体

    """

    def __init__(self):
        """
        :param PolicyId: 保单号
        :type PolicyId: str
        :param CustomerId: 客户号
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param TaskType: 文件类型，目前只支持体检报告类型，对应的值为：HealthReport
        :type TaskType: str
        :param Year: 报告年份
        :type Year: str
        :param FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        """
        self.PolicyId = None
        self.CustomerId = None
        self.CustomerName = None
        self.TaskType = None
        self.Year = None
        self.FileList = None
        self.InsuranceTypes = None
        self.ImageList = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.CustomerId = params.get("CustomerId")
        self.CustomerName = params.get("CustomerName")
        self.TaskType = params.get("TaskType")
        self.Year = params.get("Year")
        self.FileList = params.get("FileList")
        self.InsuranceTypes = params.get("InsuranceTypes")
        self.ImageList = params.get("ImageList")
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
        """
        :param TaskId: 本次结构化任务的ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeStructCompareDataRequest(AbstractModel):
    """DescribeStructCompareData请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 结构化任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        """
        :param PolicyId: 保单号
        :type PolicyId: str
        :param TaskId: 结构化任务ID
        :type TaskId: str
        :param CustomerId: 客户号
        :type CustomerId: str
        :param CustomerName: 客户姓名
        :type CustomerName: str
        :param ReviewTime: 复核时间
        :type ReviewTime: str
        :param MachineResult: 算法识别结果
        :type MachineResult: str
        :param ManualResult: 人工复核结果
        :type ManualResult: str
        :param Metrics: 结构化对比指标数据
        :type Metrics: :class:`tencentcloud.cii.v20201210.models.CompareMetricsData`
        :param NewItems: 新增项
        :type NewItems: str
        :param ModifyItems: 修改项
        :type ModifyItems: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.TaskId = None
        self.CustomerId = None
        self.CustomerName = None
        self.ReviewTime = None
        self.MachineResult = None
        self.ManualResult = None
        self.Metrics = None
        self.NewItems = None
        self.ModifyItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.TaskId = params.get("TaskId")
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
        self.RequestId = params.get("RequestId")


class DescribeStructureTaskResultRequest(AbstractModel):
    """DescribeStructureTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 结构化任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        """
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
        """
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
        