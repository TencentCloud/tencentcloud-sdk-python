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


class Condition(AbstractModel):
    """- [ ] 过滤条件<br>

    <li>Name - String - 是否必填：否 - 操作符: ilike  - 排序支持：否- 根据分组名称进行查询。</li>
    分页参数<br>
    <li>PageNum 从1开始，小于等于0时使用默认参数。</li>
    <li>PageSize 最大值5000，最好不超过100。</li>

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of Filter
        :param _FilterGroups: FilterGroups 条件过滤组
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterGroups: list of FilterGroup
        :param _Sort: Sort 排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageSize: PageSize 每页获取数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNum: PageNum 获取第几页(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        """
        self._Filters = None
        self._FilterGroups = None
        self._Sort = None
        self._PageSize = None
        self._PageNum = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterGroups(self):
        return self._FilterGroups

    @FilterGroups.setter
    def FilterGroups(self, FilterGroups):
        self._FilterGroups = FilterGroups

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("FilterGroups") is not None:
            self._FilterGroups = []
            for item in params.get("FilterGroups"):
                obj = FilterGroup()
                obj._deserialize(item)
                self._FilterGroups.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesPageRsp(AbstractModel):
    """分页的data数据

    """

    def __init__(self):
        r"""
        :param _Paging: 数据分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Paging: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Paging = None

    @property
    def Paging(self):
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging


    def _deserialize(self, params):
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 过滤条件<br>
<li>Ip - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照Ip进行过滤。</li>
<li>MacAddr - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照mac地址进行过滤。</li>
<li>IoaUserName - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照ioa用户名进行过滤。</li>
分页参数<br>
<li>PageNum 从1开始，小于等于0时使用默认参数。</li>
<li>PageSize 最大值5000，最好不超过100。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _GroupId: 私有化默认分组id-名称-操作系统
1	全网终端	Win
2	未分组终端	Win
30000000	服务器	Win
40000101	全网终端	Linux
40000102	未分组终端	Linux
40000103	服务器	Linux
40000201	全网终端	macOS
40000202	未分组终端	macOS
40000203	服务器	macOS
40000401	全网终端	Android
40000402	未分组终端	Android
40000501	全网终端	iOS
40000502	未分组终端	iOS
        :type GroupId: int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，3: win_srv，4：android，5：ios   默认值0）
        :type OsType: int
        :param _OnlineStatus: 在线状态 2 在线 0，1 离线
        :type OnlineStatus: int
        :param _Filters: 过滤条件--兼容旧接口,参数同Condition
        :type Filters: list of Filter
        :param _Sort: 排序字段--兼容旧接口,参数同Condition
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageNum: 获取第几页--兼容旧接口,参数同Condition(只支持32位)
        :type PageNum: int
        :param _PageSize: 每页获取数--兼容旧接口,参数同Condition(只支持32位)
        :type PageSize: int
        :param _Status: 授权状态 4未授权 5已授权
        :type Status: int
        """
        self._Condition = None
        self._GroupId = None
        self._OsType = None
        self._OnlineStatus = None
        self._Filters = None
        self._Sort = None
        self._PageNum = None
        self._PageSize = None
        self._Status = None

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OnlineStatus(self):
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._OnlineStatus = params.get("OnlineStatus")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的data数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeDevicesPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filters 条件过滤

    """

    def __init__(self):
        r"""
        :param _Field: 过滤字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _Operator: 过滤方式 eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Values: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Field = None
        self._Operator = None
        self._Values = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Operator = params.get("Operator")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterGroup(AbstractModel):
    """FilterGroups 条件过滤组

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """数据分页信息

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页条数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNum: 页码(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        :param _PageCount: 总页数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageCount: int
        :param _Total: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._PageSize = None
        self._PageNum = None
        self._PageCount = None
        self._Total = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._PageCount = params.get("PageCount")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """Sort 排序字段

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _Order: 排序方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        