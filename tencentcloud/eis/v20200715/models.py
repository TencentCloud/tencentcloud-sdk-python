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


class DescribeEisConnectorConfigRequest(AbstractModel):
    """DescribeEisConnectorConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称\n        :type ConnectorName: str\n        :param ConnectorVersion: 连接器版本\n        :type ConnectorVersion: str\n        """
        self.ConnectorName = None
        self.ConnectorVersion = None


    def _deserialize(self, params):
        self.ConnectorName = params.get("ConnectorName")
        self.ConnectorVersion = params.get("ConnectorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEisConnectorConfigResponse(AbstractModel):
    """DescribeEisConnectorConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ConnectorParameter: 连接器配置参数描述（json结构），示例如下：
{
    "attributes":{
        "description":"测试", // 连接器的描述
        "displayName":"测试", // 连接器的展示名
        "name":"test", // 连接器的名称
        "version":"1.0.0" // 连接器的版本号
    },
    "properties":[
        {
            "attributes":{
                "displayName":"企业ID", // 参数的展示名
                "name":"para1", // 参数名
                "required":"true", // 是否必填
                "type":"int" // 参数的类型
            }
        },
        {
            "attributes":{
                "displayName":"成员管理密钥",
                "name":"para2",
                "required":"true",
                "type":"float"
            }
        },
        {
            "attributes":{
                "displayName":"应用管理密钥",
                "name":"para3",
                "required":"true",
                "type":"string"
            }
        },
        {
            "attributes":{
                "displayName":"企业ID",
                "name":"para4",
                "required":"true",
                "type":"decimal"
            }
        },
        {
            "attributes":{
                "displayName":"成员管理密钥",
                "name":"para5",
                "required":"true",
                "type":"bool"
            }
        },
        {
            "attributes":{
                "displayName":"应用管理密钥",
                "name":"para6",
                "required":"true",
                "type":"date"
            }
        },
        {
            "attributes":{
                "displayName":"企业ID",
                "name":"para7",
                "required":"true",
                "type":"time"
            }
        },
        {
            "attributes":{
                "displayName":"成员管理密钥",
                "name":"para8",
                "required":"true",
                "type":"datetime"
            }
        },
        {
            "attributes":{
                "displayName":"应用管理密钥",
                "name":"para9",
                "required":"true",
                "type":"map"
            },
            "children":[
                {
                    "attributes":{
                        "displayName":"key",
                        "name":"key",
                        "required":"true",
                        "type":"string"
                    }
                },
                {
                    "attributes":{
                        "displayName":"value",
                        "name":"value",
                        "required":"true",
                        "type":"any"
                    }
                }
            ]
        },
        {
            "attributes":{
                "displayName":"企业ID",
                "name":"para10",
                "required":"true",
                "type":"list" // list，list里元素的类型是结构体，children里是结构体的描述
            },
            "children":[
                {
                    "attributes":{
                        "displayName":"field1",
                        "name":"field1",
                        "required":"true",
                        "type":"string"
                    }
                },
                {
                    "attributes":{
                        "displayName":"field2",
                        "name":"field2",
                        "required":"true",
                        "type":"any"
                    }
                }
            ]
        },
        {
            "attributes":{
                "displayName":"成员管理密钥",
                "name":"para11",
                "required":"true",
                "type":"struct"
            },
            "children":[
                {
                    "attributes":{
                        "displayName":"field1", // 结构体属性的展示名
                        "name":"field1", // 结构体属性的名称
                        "required":"true", // 是否必填
                        "type":"string" // 属性的类型
                    }
                },
                {
                    "attributes":{
                        "displayName":"field2",
                        "name":"field2",
                        "required":"true",
                        "type":"any"
                    }
                }
            ]
        },
        {
            "attributes":{
                "displayName":"应用管理密钥",
                "name":"para12",
                "required":"true",
                "type":"enum"
            },
            "children":[
                {
                    "attributes":{
                        "displayName":"PC", // 枚举值的展示名
                        "name":"PC" // 枚举值的名称
                    }
                },
                {
                    "attributes":{
                        "displayName":"MAC",
                        "name":"MAC"
                    }
                }
            ]
        }
    ]
}\n        :type ConnectorParameter: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ConnectorParameter = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConnectorParameter = params.get("ConnectorParameter")
        self.RequestId = params.get("RequestId")


class EisConnectionOperation(AbstractModel):
    """连接器操作

    """

    def __init__(self):
        """
        :param OperationName: 连接器操作名称\n        :type OperationName: str\n        :param DisplayName: 连接器展示名称\n        :type DisplayName: str\n        :param IsTrigger: 操作是否为触发器\n        :type IsTrigger: bool\n        """
        self.OperationName = None
        self.DisplayName = None
        self.IsTrigger = None


    def _deserialize(self, params):
        self.OperationName = params.get("OperationName")
        self.DisplayName = params.get("DisplayName")
        self.IsTrigger = params.get("IsTrigger")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EisConnectorSummary(AbstractModel):
    """连接器概要信息

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称\n        :type ConnectorName: str\n        :param DisplayName: 连接器展示名称\n        :type DisplayName: str\n        :param Company: 连接器对应企业\n        :type Company: str\n        :param Product: 连接器对应产品\n        :type Product: str\n        :param ConnectorVersion: 连接器版本\n        :type ConnectorVersion: str\n        :param CreateTime: 连接器创建时间\n        :type CreateTime: int\n        """
        self.ConnectorName = None
        self.DisplayName = None
        self.Company = None
        self.Product = None
        self.ConnectorVersion = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ConnectorName = params.get("ConnectorName")
        self.DisplayName = params.get("DisplayName")
        self.Company = params.get("Company")
        self.Product = params.get("Product")
        self.ConnectorVersion = params.get("ConnectorVersion")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorOperationsRequest(AbstractModel):
    """ListEisConnectorOperations请求参数结构体

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称\n        :type ConnectorName: str\n        :param ConnectorVersion: 连接器版本\n        :type ConnectorVersion: str\n        """
        self.ConnectorName = None
        self.ConnectorVersion = None


    def _deserialize(self, params):
        self.ConnectorName = params.get("ConnectorName")
        self.ConnectorVersion = params.get("ConnectorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorOperationsResponse(AbstractModel):
    """ListEisConnectorOperations返回参数结构体

    """

    def __init__(self):
        """
        :param Operations: 连接器列表\n        :type Operations: list of EisConnectionOperation\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = EisConnectionOperation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class ListEisConnectorsRequest(AbstractModel):
    """ListEisConnectors请求参数结构体

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称,非必输，如输入则按照输入值模糊匹配\n        :type ConnectorName: str\n        :param Offset: 分页参数,数据偏移量\n        :type Offset: int\n        :param Limit: 分页参数,每页显示的条数\n        :type Limit: int\n        """
        self.ConnectorName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ConnectorName = params.get("ConnectorName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorsResponse(AbstractModel):
    """ListEisConnectors返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 连接器总数\n        :type TotalCount: int\n        :param Connectors: 连接器列表\n        :type Connectors: list of EisConnectorSummary\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Connectors = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Connectors") is not None:
            self.Connectors = []
            for item in params.get("Connectors"):
                obj = EisConnectorSummary()
                obj._deserialize(item)
                self.Connectors.append(obj)
        self.RequestId = params.get("RequestId")