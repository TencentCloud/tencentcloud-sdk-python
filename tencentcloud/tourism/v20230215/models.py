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


class DescribeDrawResourceListRequest(AbstractModel):
    """DescribeDrawResourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: PageNumber
        :type PageNumber: int
        :param PageSize: PageSize
        :type PageSize: int
        """
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDrawResourceListResponse(AbstractModel):
    """DescribeDrawResourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回数据条数
        :type TotalCount: int
        :param ResourceDrawList: 返回数据数组
        :type ResourceDrawList: list of ResourceDrawListType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceDrawList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceDrawList") is not None:
            self.ResourceDrawList = []
            for item in params.get("ResourceDrawList"):
                obj = ResourceDrawListType()
                obj._deserialize(item)
                self.ResourceDrawList.append(obj)
        self.RequestId = params.get("RequestId")


class ResourceDrawListType(AbstractModel):
    """输出用户的资源数据

    """

    def __init__(self):
        r"""
        :param Id: 记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param FlowId: 资源记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param IndexId: 本订单资源序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexId: str
        :param Uin: 客户的uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param SmallOrderId: 小订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type SmallOrderId: str
        :param ResourceNewStartTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceNewStartTime: str
        :param ResourceNewEndTime: 资源到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceNewEndTime: str
        :param ResourceStatus: 资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        :param Status: 本记录状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ResourceType: 项目类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: int
        """
        self.Id = None
        self.FlowId = None
        self.ResourceId = None
        self.IndexId = None
        self.Uin = None
        self.BigDealId = None
        self.SmallOrderId = None
        self.ResourceNewStartTime = None
        self.ResourceNewEndTime = None
        self.ResourceStatus = None
        self.Status = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.FlowId = params.get("FlowId")
        self.ResourceId = params.get("ResourceId")
        self.IndexId = params.get("IndexId")
        self.Uin = params.get("Uin")
        self.BigDealId = params.get("BigDealId")
        self.SmallOrderId = params.get("SmallOrderId")
        self.ResourceNewStartTime = params.get("ResourceNewStartTime")
        self.ResourceNewEndTime = params.get("ResourceNewEndTime")
        self.ResourceStatus = params.get("ResourceStatus")
        self.Status = params.get("Status")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        