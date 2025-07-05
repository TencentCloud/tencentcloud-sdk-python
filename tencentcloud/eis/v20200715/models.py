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


class DescribeEisConnectorConfigRequest(AbstractModel):
    """DescribeEisConnectorConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectorName: 连接器名称
        :type ConnectorName: str
        :param _ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        """
        self._ConnectorName = None
        self._ConnectorVersion = None

    @property
    def ConnectorName(self):
        """连接器名称
        :rtype: str
        """
        return self._ConnectorName

    @ConnectorName.setter
    def ConnectorName(self, ConnectorName):
        self._ConnectorName = ConnectorName

    @property
    def ConnectorVersion(self):
        """连接器版本
        :rtype: str
        """
        return self._ConnectorVersion

    @ConnectorVersion.setter
    def ConnectorVersion(self, ConnectorVersion):
        self._ConnectorVersion = ConnectorVersion


    def _deserialize(self, params):
        self._ConnectorName = params.get("ConnectorName")
        self._ConnectorVersion = params.get("ConnectorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEisConnectorConfigResponse(AbstractModel):
    """DescribeEisConnectorConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectorParameter: 连接器配置参数描述（json结构），示例如下：
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
}
        :type ConnectorParameter: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConnectorParameter = None
        self._RequestId = None

    @property
    def ConnectorParameter(self):
        """连接器配置参数描述（json结构），示例如下：
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
}
        :rtype: str
        """
        return self._ConnectorParameter

    @ConnectorParameter.setter
    def ConnectorParameter(self, ConnectorParameter):
        self._ConnectorParameter = ConnectorParameter

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
        self._ConnectorParameter = params.get("ConnectorParameter")
        self._RequestId = params.get("RequestId")


class EisConnectionOperation(AbstractModel):
    """连接器操作

    """

    def __init__(self):
        r"""
        :param _OperationName: 连接器操作名称
        :type OperationName: str
        :param _DisplayName: 连接器展示名称
        :type DisplayName: str
        :param _IsTrigger: 操作是否为触发器
        :type IsTrigger: bool
        """
        self._OperationName = None
        self._DisplayName = None
        self._IsTrigger = None

    @property
    def OperationName(self):
        """连接器操作名称
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def DisplayName(self):
        """连接器展示名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def IsTrigger(self):
        """操作是否为触发器
        :rtype: bool
        """
        return self._IsTrigger

    @IsTrigger.setter
    def IsTrigger(self, IsTrigger):
        self._IsTrigger = IsTrigger


    def _deserialize(self, params):
        self._OperationName = params.get("OperationName")
        self._DisplayName = params.get("DisplayName")
        self._IsTrigger = params.get("IsTrigger")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EisConnectorSummary(AbstractModel):
    """连接器概要信息

    """

    def __init__(self):
        r"""
        :param _ConnectorName: 连接器名称
        :type ConnectorName: str
        :param _DisplayName: 连接器展示名称
        :type DisplayName: str
        :param _Company: 连接器对应企业
        :type Company: str
        :param _Product: 连接器对应产品
        :type Product: str
        :param _ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        :param _CreateTime: 连接器创建时间
        :type CreateTime: int
        """
        self._ConnectorName = None
        self._DisplayName = None
        self._Company = None
        self._Product = None
        self._ConnectorVersion = None
        self._CreateTime = None

    @property
    def ConnectorName(self):
        """连接器名称
        :rtype: str
        """
        return self._ConnectorName

    @ConnectorName.setter
    def ConnectorName(self, ConnectorName):
        self._ConnectorName = ConnectorName

    @property
    def DisplayName(self):
        """连接器展示名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Company(self):
        """连接器对应企业
        :rtype: str
        """
        return self._Company

    @Company.setter
    def Company(self, Company):
        self._Company = Company

    @property
    def Product(self):
        """连接器对应产品
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ConnectorVersion(self):
        """连接器版本
        :rtype: str
        """
        return self._ConnectorVersion

    @ConnectorVersion.setter
    def ConnectorVersion(self, ConnectorVersion):
        self._ConnectorVersion = ConnectorVersion

    @property
    def CreateTime(self):
        """连接器创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ConnectorName = params.get("ConnectorName")
        self._DisplayName = params.get("DisplayName")
        self._Company = params.get("Company")
        self._Product = params.get("Product")
        self._ConnectorVersion = params.get("ConnectorVersion")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorOperationsRequest(AbstractModel):
    """ListEisConnectorOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectorName: 连接器名称
        :type ConnectorName: str
        :param _ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        """
        self._ConnectorName = None
        self._ConnectorVersion = None

    @property
    def ConnectorName(self):
        """连接器名称
        :rtype: str
        """
        return self._ConnectorName

    @ConnectorName.setter
    def ConnectorName(self, ConnectorName):
        self._ConnectorName = ConnectorName

    @property
    def ConnectorVersion(self):
        """连接器版本
        :rtype: str
        """
        return self._ConnectorVersion

    @ConnectorVersion.setter
    def ConnectorVersion(self, ConnectorVersion):
        self._ConnectorVersion = ConnectorVersion


    def _deserialize(self, params):
        self._ConnectorName = params.get("ConnectorName")
        self._ConnectorVersion = params.get("ConnectorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorOperationsResponse(AbstractModel):
    """ListEisConnectorOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Operations: 连接器列表
        :type Operations: list of EisConnectionOperation
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Operations = None
        self._RequestId = None

    @property
    def Operations(self):
        """连接器列表
        :rtype: list of EisConnectionOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = EisConnectionOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class ListEisConnectorsRequest(AbstractModel):
    """ListEisConnectors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectorName: 连接器名称,非必输，如输入则按照输入值模糊匹配
        :type ConnectorName: str
        :param _Offset: 分页参数,数据偏移量
        :type Offset: int
        :param _Limit: 分页参数,每页显示的条数
        :type Limit: int
        """
        self._ConnectorName = None
        self._Offset = None
        self._Limit = None

    @property
    def ConnectorName(self):
        """连接器名称,非必输，如输入则按照输入值模糊匹配
        :rtype: str
        """
        return self._ConnectorName

    @ConnectorName.setter
    def ConnectorName(self, ConnectorName):
        self._ConnectorName = ConnectorName

    @property
    def Offset(self):
        """分页参数,数据偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数,每页显示的条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ConnectorName = params.get("ConnectorName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEisConnectorsResponse(AbstractModel):
    """ListEisConnectors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 连接器总数
        :type TotalCount: int
        :param _Connectors: 连接器列表
        :type Connectors: list of EisConnectorSummary
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Connectors = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """连接器总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Connectors(self):
        """连接器列表
        :rtype: list of EisConnectorSummary
        """
        return self._Connectors

    @Connectors.setter
    def Connectors(self, Connectors):
        self._Connectors = Connectors

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Connectors") is not None:
            self._Connectors = []
            for item in params.get("Connectors"):
                obj = EisConnectorSummary()
                obj._deserialize(item)
                self._Connectors.append(obj)
        self._RequestId = params.get("RequestId")