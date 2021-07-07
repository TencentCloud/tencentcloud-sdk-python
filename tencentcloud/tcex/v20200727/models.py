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
        """
        :param AlgoId: 算法ID
        :type AlgoId: str
        :param AlgoName: 算法名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgoName: str
        :param Result: 算法返回的结果。
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
        :param Error: 算法调用错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        :param AlgoType: 算法类型：
1：OCR算法
2：文本分类算法
3：情感分析算法
4：合同要素抽取算法
5、实体识别算法
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgoType: int
        """
        self.AlgoId = None
        self.AlgoName = None
        self.Result = None
        self.Error = None
        self.AlgoType = None


    def _deserialize(self, params):
        self.AlgoId = params.get("AlgoId")
        self.AlgoName = params.get("AlgoName")
        self.Result = params.get("Result")
        self.Error = params.get("Error")
        self.AlgoType = params.get("AlgoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationResultRequest(AbstractModel):
    """DescribeInvocationResult请求参数结构体

    """

    def __init__(self):
        """
        :param InvokeId: 调用id，为调用InvokeService接口返回的RequestId
        :type InvokeId: str
        """
        self.InvokeId = None


    def _deserialize(self, params):
        self.InvokeId = params.get("InvokeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationResultResponse(AbstractModel):
    """DescribeInvocationResult返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 服务的调用结果
        :type Results: list of AlgorithmResult
        :param Status: 0:获取结果失败
1：结果还没有生成，继续轮询
2：获取结果成功
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = AlgorithmResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class InvokeServiceRequest(AbstractModel):
    """InvokeService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待调用的服务ID。
        :type ServiceId: str
        :param ServiceStatus: 要调用服务的状态：0表示调试版本，1表示上线版本
        :type ServiceStatus: int
        :param FileUrl: 用于测试的文档的URL。
        :type FileUrl: str
        :param Input: 用于测试的文本，当此值不为空时，调用内容以此参数的值为准。
        :type Input: str
        """
        self.ServiceId = None
        self.ServiceStatus = None
        self.FileUrl = None
        self.Input = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceStatus = params.get("ServiceStatus")
        self.FileUrl = params.get("FileUrl")
        self.Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeServiceResponse(AbstractModel):
    """InvokeService返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")