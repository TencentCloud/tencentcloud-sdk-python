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
        :param _ShortStructAccuracy: 短文准确率
        :type ShortStructAccuracy: str
        :param _ShortStructRecall: 短文召回率
        :type ShortStructRecall: str
        :param _LongStructAccuracy: 长文结构化准确率
        :type LongStructAccuracy: str
        :param _LongStructRecall: 长文结构化召回率
        :type LongStructRecall: str
        :param _LongContentAccuracy: 长文提取准确率
        :type LongContentAccuracy: str
        :param _LongContentRecall: 长文提取召回率
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
        :rtype: str
        """
        return self._ShortStructAccuracy

    @ShortStructAccuracy.setter
    def ShortStructAccuracy(self, ShortStructAccuracy):
        self._ShortStructAccuracy = ShortStructAccuracy

    @property
    def ShortStructRecall(self):
        """短文召回率
        :rtype: str
        """
        return self._ShortStructRecall

    @ShortStructRecall.setter
    def ShortStructRecall(self, ShortStructRecall):
        self._ShortStructRecall = ShortStructRecall

    @property
    def LongStructAccuracy(self):
        """长文结构化准确率
        :rtype: str
        """
        return self._LongStructAccuracy

    @LongStructAccuracy.setter
    def LongStructAccuracy(self, LongStructAccuracy):
        self._LongStructAccuracy = LongStructAccuracy

    @property
    def LongStructRecall(self):
        """长文结构化召回率
        :rtype: str
        """
        return self._LongStructRecall

    @LongStructRecall.setter
    def LongStructRecall(self, LongStructRecall):
        self._LongStructRecall = LongStructRecall

    @property
    def LongContentAccuracy(self):
        """长文提取准确率
        :rtype: str
        """
        return self._LongContentAccuracy

    @LongContentAccuracy.setter
    def LongContentAccuracy(self, LongContentAccuracy):
        self._LongContentAccuracy = LongContentAccuracy

    @property
    def LongContentRecall(self):
        """长文提取召回率
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
        


class CreateStructureTaskRequest(AbstractModel):
    """CreateStructureTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 保单号
        :type PolicyId: str
        :param _CustomerId: 客户号
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _TaskType: 文件类型，目前只支持体检报告类型，对应的值为：HealthReport
        :type TaskType: str
        :param _Year: 报告年份
        :type Year: str
        :param _FileList: 报告文件上传的地址列表，需按顺序排列。如果使用ImageList参数，置为空数组即可
        :type FileList: list of str
        :param _InsuranceTypes: 险种，如果是体检报告类型，此参数是必填，类型说明如下：
CriticalDiseaseInsurance:重疾险
LifeInsurance：寿险
AccidentInsurance：意外险
        :type InsuranceTypes: list of str
        :param _ImageList: 报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :type ImageList: list of str
        """
        self._PolicyId = None
        self._CustomerId = None
        self._CustomerName = None
        self._TaskType = None
        self._Year = None
        self._FileList = None
        self._InsuranceTypes = None
        self._ImageList = None

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
    def TaskType(self):
        """文件类型，目前只支持体检报告类型，对应的值为：HealthReport
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Year(self):
        """报告年份
        :rtype: str
        """
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year

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
    def ImageList(self):
        """报告上传的图片内容数组，图片内容采用base64编码，需按顺序排列
        :rtype: list of str
        """
        return self._ImageList

    @ImageList.setter
    def ImageList(self, ImageList):
        self._ImageList = ImageList


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._CustomerId = params.get("CustomerId")
        self._CustomerName = params.get("CustomerName")
        self._TaskType = params.get("TaskType")
        self._Year = params.get("Year")
        self._FileList = params.get("FileList")
        self._InsuranceTypes = params.get("InsuranceTypes")
        self._ImageList = params.get("ImageList")
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
        :param _TaskId: 本次结构化任务的ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """本次结构化任务的ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeStructCompareDataRequest(AbstractModel):
    """DescribeStructCompareData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 结构化任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """结构化任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        :param _TaskId: 结构化任务ID
        :type TaskId: str
        :param _CustomerId: 客户号
        :type CustomerId: str
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _ReviewTime: 复核时间
        :type ReviewTime: str
        :param _MachineResult: 算法识别结果
        :type MachineResult: str
        :param _ManualResult: 人工复核结果
        :type ManualResult: str
        :param _Metrics: 结构化对比指标数据
        :type Metrics: :class:`tencentcloud.cii.v20201210.models.CompareMetricsData`
        :param _NewItems: 新增项
        :type NewItems: str
        :param _ModifyItems: 修改项
        :type ModifyItems: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._TaskId = None
        self._CustomerId = None
        self._CustomerName = None
        self._ReviewTime = None
        self._MachineResult = None
        self._ManualResult = None
        self._Metrics = None
        self._NewItems = None
        self._ModifyItems = None
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
    def TaskId(self):
        """结构化任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        :rtype: :class:`tencentcloud.cii.v20201210.models.CompareMetricsData`
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
        self._TaskId = params.get("TaskId")
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
        self._RequestId = params.get("RequestId")


class DescribeStructureTaskResultRequest(AbstractModel):
    """DescribeStructureTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 结构化任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """结构化任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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


class ResultObject(AbstractModel):
    """用于返回结构化任务结果

    """

    def __init__(self):
        r"""
        :param _Quality: 图片质量分
        :type Quality: float
        :param _StructureResult: 由结构化算法结构化json转换的字符串，具体协议参见算法结构化结果协议
        :type StructureResult: str
        """
        self._Quality = None
        self._StructureResult = None

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


    def _deserialize(self, params):
        self._Quality = params.get("Quality")
        self._StructureResult = params.get("StructureResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        