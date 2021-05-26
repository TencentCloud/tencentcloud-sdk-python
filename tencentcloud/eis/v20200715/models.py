# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        :param ConnectorName: 连接器名称
        :type ConnectorName: str
        :param ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEisConnectorConfigResponse(AbstractModel):
    """DescribeEisConnectorConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ConnectorParameter: 连接器配置参数描述（json结构），示例如下：
{
    "attributes":{
        "description":"测试",
        "displayName":"test",
        "name":"test",
        "version":"1.0.0"
    },
    "properties":[
        {
            "displayName":"日期",
            "name":"prop1",
            "required":"true",
            "type":"date"
        }
    ],
    "operations":{
        "get-info":[
            {
                "displayName":"para1",
                "name":"para1",
                "required":"true",
                "type":"int"
            },
            {
                "displayName":"para2",
                "name":"para2",
                "required":"true",
                "type":"float"
            },
            {
                "displayName":"para3",
                "name":"para3",
                "required":"true",
                "type":"string"
            },
            {
                "displayName":"para4",
                "name":"para4",
                "required":"true",
                "type":"decimal"
            },
            {
                "displayName":"para5",
                "name":"para5",
                "required":"true",
                "type":"bool"
            },
            {
                "displayName":"para6",
                "name":"para6",
                "required":"true",
                "type":"date"
            },
            {
                "displayName":"para7",
                "name":"para7",
                "required":"true",
                "type":"time"
            },
            {
                "displayName":"para8",
                "name":"para8",
                "required":"true",
                "type":"datetime"
            },
            {
                "displayName":"para9",
                "name":"para9",
                "required":"true",
                "type":"struct",
                "children":[
                    {
                        "displayName":"date",
                        "name":"date",
                        "required":"true",
                        "type":"date"
                    },
                    {
                        "displayName":"time",
                        "name":"time",
                        "required":"true",
                        "type":"time"
                    },
                    {
                        "displayName":"datetime",
                        "name":"datetime",
                        "required":"true",
                        "type":"datetime"
                    }
                ]
            },
            {
                "displayName":"para10",
                "name":"para10",
                "required":"true",
                "type":"list",
                "children":[
                    {
                        "displayName":"value",
                        "name":"value",
                        "required":"true",
                        "type":"string"
                    }
                ]
            },
            {
                "displayName":"para11",
                "name":"para11",
                "required":"true",
                "type":"dict",
                "children":[
                    {
                        "displayName":"key",
                        "name":"key",
                        "required":"true",
                        "type":"string"
                    },
                    {
                        "displayName":"value",
                        "name":"value",
                        "required":"true",
                        "type":"string"
                    }
                ]
            },
            {
                "displayName":"para12",
                "name":"para12",
                "required":"true",
                "type":"enum",
                "children":[
                    {
                        "displayName":"PC",
                        "name":"1"
                    },
                    {
                        "displayName":"Mac",
                        "name":"2"
                    }
                ]
            }
        ]
    }
}
        :type ConnectorParameter: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConnectorParameter = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConnectorParameter = params.get("ConnectorParameter")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EisConnectionOperation(AbstractModel):
    """连接器操作

    """

    def __init__(self):
        """
        :param OperationName: 连接器操作名称
        :type OperationName: str
        :param DisplayName: 连接器展示名称
        :type DisplayName: str
        :param IsTrigger: 操作是否为触发器
        :type IsTrigger: bool
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EisConnectorSummary(AbstractModel):
    """连接器概要信息

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称
        :type ConnectorName: str
        :param DisplayName: 连接器展示名称
        :type DisplayName: str
        :param Company: 连接器对应企业
        :type Company: str
        :param Product: 连接器对应产品
        :type Product: str
        :param ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        :param CreateTime: 连接器创建时间
        :type CreateTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListEisConnectorOperationsRequest(AbstractModel):
    """ListEisConnectorOperations请求参数结构体

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称
        :type ConnectorName: str
        :param ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListEisConnectorOperationsResponse(AbstractModel):
    """ListEisConnectorOperations返回参数结构体

    """

    def __init__(self):
        """
        :param Operations: 连接器列表
        :type Operations: list of EisConnectionOperation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListEisConnectorsRequest(AbstractModel):
    """ListEisConnectors请求参数结构体

    """

    def __init__(self):
        """
        :param ConnectorName: 连接器名称,非必输，如输入则按照输入值模糊匹配
        :type ConnectorName: str
        :param Offset: 分页参数,数据偏移量
        :type Offset: int
        :param Limit: 分页参数,每页显示的条数
        :type Limit: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListEisConnectorsResponse(AbstractModel):
    """ListEisConnectors返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 连接器总数
        :type TotalCount: int
        :param Connectors: 连接器列表
        :type Connectors: list of EisConnectorSummary
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        