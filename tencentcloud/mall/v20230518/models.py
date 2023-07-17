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
        :param _PageNumber: PageNumber
        :type PageNumber: int
        :param _PageSize: PageSize
        :type PageSize: int
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDrawResourceListResponse(AbstractModel):
    """DescribeDrawResourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回数据条数
        :type TotalCount: int
        :param _ResourceDrawList: 返回数据内容
        :type ResourceDrawList: list of ResourceDrawListType
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceDrawList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceDrawList(self):
        return self._ResourceDrawList

    @ResourceDrawList.setter
    def ResourceDrawList(self, ResourceDrawList):
        self._ResourceDrawList = ResourceDrawList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResourceDrawList") is not None:
            self._ResourceDrawList = []
            for item in params.get("ResourceDrawList"):
                obj = ResourceDrawListType()
                obj._deserialize(item)
                self._ResourceDrawList.append(obj)
        self._RequestId = params.get("RequestId")


class ResourceDrawListType(AbstractModel):
    """输出用户的资源数据

    """

    def __init__(self):
        r"""
        :param _Id: 记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _FlowId: 资源记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _IndexId: 本订单资源序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexId: str
        :param _Uin: 客户的Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _BigDealId: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param _SmallOrderId: 小订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type SmallOrderId: str
        :param _ResourceNewStartTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceNewStartTime: str
        :param _ResourceNewEndTime: 资源到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceNewEndTime: str
        :param _ResourceStatus: 资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: int
        :param _Status: 本记录状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ResourceType: 项目类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: int
        """
        self._Id = None
        self._FlowId = None
        self._ResourceId = None
        self._IndexId = None
        self._Uin = None
        self._BigDealId = None
        self._SmallOrderId = None
        self._ResourceNewStartTime = None
        self._ResourceNewEndTime = None
        self._ResourceStatus = None
        self._Status = None
        self._ResourceType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def IndexId(self):
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def SmallOrderId(self):
        return self._SmallOrderId

    @SmallOrderId.setter
    def SmallOrderId(self, SmallOrderId):
        self._SmallOrderId = SmallOrderId

    @property
    def ResourceNewStartTime(self):
        return self._ResourceNewStartTime

    @ResourceNewStartTime.setter
    def ResourceNewStartTime(self, ResourceNewStartTime):
        self._ResourceNewStartTime = ResourceNewStartTime

    @property
    def ResourceNewEndTime(self):
        return self._ResourceNewEndTime

    @ResourceNewEndTime.setter
    def ResourceNewEndTime(self, ResourceNewEndTime):
        self._ResourceNewEndTime = ResourceNewEndTime

    @property
    def ResourceStatus(self):
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._FlowId = params.get("FlowId")
        self._ResourceId = params.get("ResourceId")
        self._IndexId = params.get("IndexId")
        self._Uin = params.get("Uin")
        self._BigDealId = params.get("BigDealId")
        self._SmallOrderId = params.get("SmallOrderId")
        self._ResourceNewStartTime = params.get("ResourceNewStartTime")
        self._ResourceNewEndTime = params.get("ResourceNewEndTime")
        self._ResourceStatus = params.get("ResourceStatus")
        self._Status = params.get("Status")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        