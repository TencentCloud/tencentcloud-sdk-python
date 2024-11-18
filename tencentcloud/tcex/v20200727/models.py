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


class AlgorithmResult(AbstractModel):
    """每个算法的返回结果

    """

    def __init__(self):
        r"""
        :param _AlgoId: 算法ID
        :type AlgoId: str
        :param _AlgoName: 算法名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgoName: str
        :param _Result: 算法返回的结果。
- 当算法类型为“OCR（1）”时，结果为文本字符串
- 当算法类型为“文本分类（2）”时，结果字符串为json对象数组：
  Class：分类结果
  Confidence：置信度
- 算法类型为“情感分析（3）”时，结果字符串为json对象：
  Positive：正面情感概率
  Negative：负面情感概率
  Neutral：中性情感概率
- 当算法类型为“合同要素抽取（4）”时，结果字符串为json对象数组：
  NodeName：一级要素名称
  ItemName：二级要素名称
  Content：要素文本内容
- 当算法类型为“实体识别（5）”时，结果字符串为json对象数组：
  - Entity：实体类型
  - Content：实体文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _Error: 算法调用错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        :param _AlgoType: 算法类型：
1：OCR算法
2：文本分类算法
3：情感分析算法
4：合同要素抽取算法
5、实体识别算法
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgoType: int
        """
        self._AlgoId = None
        self._AlgoName = None
        self._Result = None
        self._Error = None
        self._AlgoType = None

    @property
    def AlgoId(self):
        """算法ID
        :rtype: str
        """
        return self._AlgoId

    @AlgoId.setter
    def AlgoId(self, AlgoId):
        self._AlgoId = AlgoId

    @property
    def AlgoName(self):
        """算法名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlgoName

    @AlgoName.setter
    def AlgoName(self, AlgoName):
        self._AlgoName = AlgoName

    @property
    def Result(self):
        """算法返回的结果。
- 当算法类型为“OCR（1）”时，结果为文本字符串
- 当算法类型为“文本分类（2）”时，结果字符串为json对象数组：
  Class：分类结果
  Confidence：置信度
- 算法类型为“情感分析（3）”时，结果字符串为json对象：
  Positive：正面情感概率
  Negative：负面情感概率
  Neutral：中性情感概率
- 当算法类型为“合同要素抽取（4）”时，结果字符串为json对象数组：
  NodeName：一级要素名称
  ItemName：二级要素名称
  Content：要素文本内容
- 当算法类型为“实体识别（5）”时，结果字符串为json对象数组：
  - Entity：实体类型
  - Content：实体文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Error(self):
        """算法调用错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def AlgoType(self):
        """算法类型：
1：OCR算法
2：文本分类算法
3：情感分析算法
4：合同要素抽取算法
5、实体识别算法
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AlgoType

    @AlgoType.setter
    def AlgoType(self, AlgoType):
        self._AlgoType = AlgoType


    def _deserialize(self, params):
        self._AlgoId = params.get("AlgoId")
        self._AlgoName = params.get("AlgoName")
        self._Result = params.get("Result")
        self._Error = params.get("Error")
        self._AlgoType = params.get("AlgoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationResultRequest(AbstractModel):
    """DescribeInvocationResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokeId: 调用id，为调用InvokeService接口返回的RequestId
        :type InvokeId: str
        """
        self._InvokeId = None

    @property
    def InvokeId(self):
        """调用id，为调用InvokeService接口返回的RequestId
        :rtype: str
        """
        return self._InvokeId

    @InvokeId.setter
    def InvokeId(self, InvokeId):
        self._InvokeId = InvokeId


    def _deserialize(self, params):
        self._InvokeId = params.get("InvokeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationResultResponse(AbstractModel):
    """DescribeInvocationResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 服务的调用结果
        :type Results: list of AlgorithmResult
        :param _Status: 0:获取结果失败
1：结果还没有生成，继续轮询
2：获取结果成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._Status = None
        self._RequestId = None

    @property
    def Results(self):
        """服务的调用结果
        :rtype: list of AlgorithmResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Status(self):
        """0:获取结果失败
1：结果还没有生成，继续轮询
2：获取结果成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = AlgorithmResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class InvokeServiceRequest(AbstractModel):
    """InvokeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待调用的服务ID。
        :type ServiceId: str
        :param _ServiceStatus: 要调用服务的状态：0表示调试版本，1表示上线版本
        :type ServiceStatus: int
        :param _FileUrl: 用于测试的文档的URL。
        :type FileUrl: str
        :param _Input: 用于测试的文本，当此值不为空时，调用内容以此参数的值为准。
        :type Input: str
        """
        self._ServiceId = None
        self._ServiceStatus = None
        self._FileUrl = None
        self._Input = None

    @property
    def ServiceId(self):
        """待调用的服务ID。
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceStatus(self):
        """要调用服务的状态：0表示调试版本，1表示上线版本
        :rtype: int
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def FileUrl(self):
        """用于测试的文档的URL。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def Input(self):
        """用于测试的文本，当此值不为空时，调用内容以此参数的值为准。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceStatus = params.get("ServiceStatus")
        self._FileUrl = params.get("FileUrl")
        self._Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeServiceResponse(AbstractModel):
    """InvokeService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")