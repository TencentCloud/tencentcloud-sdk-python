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


class ComplexRule(AbstractModel):
    """自动划分规则数据

    """

    def __init__(self):
        r"""
        :param _SimpleRules: 简单规则表达式
        :type SimpleRules: list of SimpleRule
        :param _Relation: 表达式间逻辑关系
        :type Relation: str
        """
        self._SimpleRules = None
        self._Relation = None

    @property
    def SimpleRules(self):
        """简单规则表达式
        :rtype: list of SimpleRule
        """
        return self._SimpleRules

    @SimpleRules.setter
    def SimpleRules(self, SimpleRules):
        self._SimpleRules = SimpleRules

    @property
    def Relation(self):
        """表达式间逻辑关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("SimpleRules") is not None:
            self._SimpleRules = []
            for item in params.get("SimpleRules"):
                obj = SimpleRule()
                obj._deserialize(item)
                self._SimpleRules.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Condition(AbstractModel):
    """这是一个多接口的公共数据结构，用于接口根据条件进行过滤和分页。具体支持哪些过滤条件，参考具体使用该结构的接口字段描述

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
        :type Filters: list of Filter
        :param _FilterGroups: FilterGroups 条件过滤组
        :type FilterGroups: list of FilterGroup
        :param _Sort: Sort 排序字段
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageSize: PageSize 每页获取数(只支持32位)
        :type PageSize: int
        :param _PageNum: PageNum 获取第几页(只支持32位)
        :type PageNum: int
        """
        self._Filters = None
        self._FilterGroups = None
        self._Sort = None
        self._PageSize = None
        self._PageNum = None

    @property
    def Filters(self):
        """Filters 条件过滤
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterGroups(self):
        """FilterGroups 条件过滤组
        :rtype: list of FilterGroup
        """
        return self._FilterGroups

    @FilterGroups.setter
    def FilterGroups(self, FilterGroups):
        self._FilterGroups = FilterGroups

    @property
    def Sort(self):
        """Sort 排序字段
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageSize(self):
        """PageSize 每页获取数(只支持32位)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """PageNum 获取第几页(只支持32位)
        :rtype: int
        """
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
        


class CreateDeviceVirtualGroupRequest(AbstractModel):
    """CreateDeviceVirtualGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceVirtualGroupName: 必填，终端自定义分组名
        :type DeviceVirtualGroupName: str
        :param _Description: 详情
        :type Description: str
        :param _OsType: 必填，系统类型（0: win，1：linux，2: mac，3: win_srv，4：android，5：ios ）(只支持32位)
        :type OsType: int
        :param _TimeType: 必填，分组类型（0:手动分组；非0为自动划分分组；具体枚举值为：1:自动每小时划分分组、2:自动每天划分分组、3:自定义时间划分分组）(只支持32位)
        :type TimeType: int
        :param _AutoMinute: 选填，TimeType=3时的自动划分时间，其他情况为0（单位min）(只支持32位)
        :type AutoMinute: int
        :param _AutoRules: 选填，手动分组不填，自动划分分组的划分规则数据
        :type AutoRules: :class:`tencentcloud.ioa.v20220601.models.ComplexRule`
        """
        self._DeviceVirtualGroupName = None
        self._Description = None
        self._OsType = None
        self._TimeType = None
        self._AutoMinute = None
        self._AutoRules = None

    @property
    def DeviceVirtualGroupName(self):
        """必填，终端自定义分组名
        :rtype: str
        """
        return self._DeviceVirtualGroupName

    @DeviceVirtualGroupName.setter
    def DeviceVirtualGroupName(self, DeviceVirtualGroupName):
        self._DeviceVirtualGroupName = DeviceVirtualGroupName

    @property
    def Description(self):
        """详情
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OsType(self):
        """必填，系统类型（0: win，1：linux，2: mac，3: win_srv，4：android，5：ios ）(只支持32位)
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def TimeType(self):
        """必填，分组类型（0:手动分组；非0为自动划分分组；具体枚举值为：1:自动每小时划分分组、2:自动每天划分分组、3:自定义时间划分分组）(只支持32位)
        :rtype: int
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def AutoMinute(self):
        """选填，TimeType=3时的自动划分时间，其他情况为0（单位min）(只支持32位)
        :rtype: int
        """
        return self._AutoMinute

    @AutoMinute.setter
    def AutoMinute(self, AutoMinute):
        self._AutoMinute = AutoMinute

    @property
    def AutoRules(self):
        """选填，手动分组不填，自动划分分组的划分规则数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.ComplexRule`
        """
        return self._AutoRules

    @AutoRules.setter
    def AutoRules(self, AutoRules):
        self._AutoRules = AutoRules


    def _deserialize(self, params):
        self._DeviceVirtualGroupName = params.get("DeviceVirtualGroupName")
        self._Description = params.get("Description")
        self._OsType = params.get("OsType")
        self._TimeType = params.get("TimeType")
        self._AutoMinute = params.get("AutoMinute")
        if params.get("AutoRules") is not None:
            self._AutoRules = ComplexRule()
            self._AutoRules._deserialize(params.get("AutoRules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceVirtualGroupResponse(AbstractModel):
    """CreateDeviceVirtualGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应返回的data
        :type Data: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRspData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """响应返回的data
        :rtype: :class:`tencentcloud.ioa.v20220601.models.CreateDeviceVirtualGroupRspData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateDeviceVirtualGroupRspData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDeviceVirtualGroupRspData(AbstractModel):
    """响应返回的data

    """

    def __init__(self):
        r"""
        :param _Id: 返回的自定义分组id
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """返回的自定义分组id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsData(AbstractModel):
    """账号分组信息

    """

    def __init__(self):
        r"""
        :param _NamePath: 账号分组名全路径，点分格式
        :type NamePath: str
        :param _IdPathArr: 账号分组ID全路径，数组格式
        :type IdPathArr: list of int
        :param _ExtraInfo: 扩展信息
        :type ExtraInfo: str
        :param _Utime: 最后更新时间
        :type Utime: str
        :param _ParentId: 父分组ID
        :type ParentId: int
        :param _OrgId: 源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type OrgId: str
        :param _Name: 分组名称
        :type Name: str
        :param _Id: 分组ID
        :type Id: int
        :param _Description: 分组描述
        :type Description: str
        :param _Source: 同步数据源
        :type Source: int
        :param _IdPath: 账号分组ID全路径，点分格式
        :type IdPath: str
        :param _Itime: 创建时间
        :type Itime: str
        :param _ParentOrgId: 父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type ParentOrgId: str
        :param _ImportType: 导入类型
        :type ImportType: str
        :param _MiniIamId: miniIAM id
        :type MiniIamId: str
        :param _UserTotal: 该分组下含子组的所有用户总数
        :type UserTotal: int
        :param _IsLeaf: 是否叶子节点
        :type IsLeaf: bool
        :param _ReadOnly: 是否该账户的直接权限
        :type ReadOnly: bool
        :param _LatestSyncResult: 最新一次同步任务的结果
        :type LatestSyncResult: str
        :param _LatestSyncTime: 最新一次同步任务的结束时间
        :type LatestSyncTime: str
        """
        self._NamePath = None
        self._IdPathArr = None
        self._ExtraInfo = None
        self._Utime = None
        self._ParentId = None
        self._OrgId = None
        self._Name = None
        self._Id = None
        self._Description = None
        self._Source = None
        self._IdPath = None
        self._Itime = None
        self._ParentOrgId = None
        self._ImportType = None
        self._MiniIamId = None
        self._UserTotal = None
        self._IsLeaf = None
        self._ReadOnly = None
        self._LatestSyncResult = None
        self._LatestSyncTime = None

    @property
    def NamePath(self):
        """账号分组名全路径，点分格式
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def IdPathArr(self):
        """账号分组ID全路径，数组格式
        :rtype: list of int
        """
        return self._IdPathArr

    @IdPathArr.setter
    def IdPathArr(self, IdPathArr):
        self._IdPathArr = IdPathArr

    @property
    def ExtraInfo(self):
        """扩展信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Utime(self):
        """最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ParentId(self):
        """父分组ID
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def OrgId(self):
        """源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Name(self):
        """分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        """分组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        """分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        """同步数据源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def IdPath(self):
        """账号分组ID全路径，点分格式
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def Itime(self):
        """创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ParentOrgId(self):
        """父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._ParentOrgId

    @ParentOrgId.setter
    def ParentOrgId(self, ParentOrgId):
        self._ParentOrgId = ParentOrgId

    @property
    def ImportType(self):
        """导入类型
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def MiniIamId(self):
        """miniIAM id
        :rtype: str
        """
        return self._MiniIamId

    @MiniIamId.setter
    def MiniIamId(self, MiniIamId):
        self._MiniIamId = MiniIamId

    @property
    def UserTotal(self):
        """该分组下含子组的所有用户总数
        :rtype: int
        """
        return self._UserTotal

    @UserTotal.setter
    def UserTotal(self, UserTotal):
        self._UserTotal = UserTotal

    @property
    def IsLeaf(self):
        """是否叶子节点
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def ReadOnly(self):
        """是否该账户的直接权限
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def LatestSyncResult(self):
        """最新一次同步任务的结果
        :rtype: str
        """
        return self._LatestSyncResult

    @LatestSyncResult.setter
    def LatestSyncResult(self, LatestSyncResult):
        self._LatestSyncResult = LatestSyncResult

    @property
    def LatestSyncTime(self):
        """最新一次同步任务的结束时间
        :rtype: str
        """
        return self._LatestSyncTime

    @LatestSyncTime.setter
    def LatestSyncTime(self, LatestSyncTime):
        self._LatestSyncTime = LatestSyncTime


    def _deserialize(self, params):
        self._NamePath = params.get("NamePath")
        self._IdPathArr = params.get("IdPathArr")
        self._ExtraInfo = params.get("ExtraInfo")
        self._Utime = params.get("Utime")
        self._ParentId = params.get("ParentId")
        self._OrgId = params.get("OrgId")
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._IdPath = params.get("IdPath")
        self._Itime = params.get("Itime")
        self._ParentOrgId = params.get("ParentOrgId")
        self._ImportType = params.get("ImportType")
        self._MiniIamId = params.get("MiniIamId")
        self._UserTotal = params.get("UserTotal")
        self._IsLeaf = params.get("IsLeaf")
        self._ReadOnly = params.get("ReadOnly")
        self._LatestSyncResult = params.get("LatestSyncResult")
        self._LatestSyncTime = params.get("LatestSyncTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsPageResp(AbstractModel):
    """账户分组详情响应数据

    """

    def __init__(self):
        r"""
        :param _Items: 账户分响应对象集合
        :type Items: list of DescribeAccountGroupsData
        :param _Page: 分页公共对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        self._Items = None
        self._Page = None

    @property
    def Items(self):
        """账户分响应对象集合
        :rtype: list of DescribeAccountGroupsData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Page(self):
        """分页公共对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeAccountGroupsData()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsRequest(AbstractModel):
    """DescribeAccountGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Deepin: 搜索范围：0-仅当前分组的直接子组，1-当前分组的所有子组。默认为0。
        :type Deepin: int
        :param _Condition: 查询条件

过滤参数
1、Name，string类型，按分组名过滤
是否必填：否
操作符: like

排序条件
1、Itime，string类型，按分组创建时间排序
是否必填：否
2、Utime，string类型，按分组更新时间排序
是否必填：否
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _ParentId: 父分组ID，获取该分组下的子组信息。默认查询全网根分组下子组信息。
        :type ParentId: int
        """
        self._Deepin = None
        self._Condition = None
        self._ParentId = None

    @property
    def Deepin(self):
        """搜索范围：0-仅当前分组的直接子组，1-当前分组的所有子组。默认为0。
        :rtype: int
        """
        return self._Deepin

    @Deepin.setter
    def Deepin(self, Deepin):
        self._Deepin = Deepin

    @property
    def Condition(self):
        """查询条件

过滤参数
1、Name，string类型，按分组名过滤
是否必填：否
操作符: like

排序条件
1、Itime，string类型，按分组创建时间排序
是否必填：否
2、Utime，string类型，按分组更新时间排序
是否必填：否
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def ParentId(self):
        """父分组ID，获取该分组下的子组信息。默认查询全网根分组下子组信息。
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Deepin = params.get("Deepin")
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsResponse(AbstractModel):
    """DescribeAccountGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号分组详情响应数据
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsPageResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """账号分组详情响应数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeAccountGroupsPageResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeAccountGroupsPageResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDevicesPageRsp(AbstractModel):
    """分页的data数据

    """

    def __init__(self):
        r"""
        :param _Paging: 数据分页信息
        :type Paging: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 业务响应数据
        :type Items: list of DeviceDetail
        """
        self._Paging = None
        self._Items = None

    @property
    def Paging(self):
        """数据分页信息
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

    @property
    def Items(self):
        """业务响应数据
        :rtype: list of DeviceDetail
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceDetail()
                obj._deserialize(item)
                self._Items.append(obj)
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
        :param _Condition: 过滤条件参数（字段含义请参考接口返回值）

- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序
- Name, 类型String，支持操作：【eq，like，ilike】，支持排序
- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序
- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序
- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序
- Tags，类型String，支持操作：【eq，like，ilike】，支持排序
- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序
- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序
- Version，类型String，支持操作：【eq，like，ilike】，支持排序
- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- HostName，类型String，支持操作：【eq，like，ilike】，支持排序
- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序
- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序
- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**
- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**
- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序
- Os，类型String，支持操作：【eq，like，ilike】，支持排序
- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**
- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序
- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序
- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序
- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序
- Memory，类型String，支持操作：【eq，like，ilike】，支持排序
- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序
- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序
- AccountName，类型String，支持操作：【like.ilike】，支持排序
- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序
- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序
- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序





分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _GroupId: 【和GroupIds必须有一个填写】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：
id-名称-操作系统
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


SaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :type GroupId: int
        :param _OsType: 【必填】操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :type OsType: int
        :param _OnlineStatus: 在线状态 （2表示在线，0或者1表示离线）
        :type OnlineStatus: int
        :param _Filters: 过滤条件--兼容旧接口,参数同Condition
        :type Filters: list of Filter
        :param _Sort: 排序字段--兼容旧接口,参数同Condition
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageNum: 获取第几页--兼容旧接口,参数同Condition
        :type PageNum: int
        :param _PageSize: 每页获取数--兼容旧接口,参数同Condition
        :type PageSize: int
        :param _Status: 授权状态： 4基础授权 5高级授权
        :type Status: int
        :param _GroupIds: 【和GroupId必须有一个填写】设备分组id列表（需要和OsType匹配）

        :type GroupIds: list of int
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
        self._GroupIds = None

    @property
    def Condition(self):
        """过滤条件参数（字段含义请参考接口返回值）

- Mid, 类型String，支持操作：【eq，like，ilike】，支持排序
- Name, 类型String，支持操作：【eq，like，ilike】，支持排序
- Itime, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserName, 类型String，支持操作：【eq，like，ilike】，支持排序
- MacAddr, 类型String，支持操作：【eq，like，ilike】，支持排序
- UserId, 类型String，支持操作：【eq，like，ilike】，支持排序
- Ip, 类型String，支持操作：【eq，like，ilike】，支持排序
- Tags，类型String，支持操作：【eq，like，ilike】，支持排序
- LocalIpList，类型String，支持操作：【eq，like，ilike】，支持排序
- SerialNum，类型String，支持操作：【eq，like，ilike】，支持排序
- Version，类型String，支持操作：【eq，like，ilike】，支持排序
- StrVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- RtpStatus，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- HostName，类型String，支持操作：【eq，like，ilike】，支持排序
- IoaUserName，类型String，支持操作：【eq，like，ilike】，支持排序
- GroupName，类型String，支持操作：【eq，like，ilike】，支持排序
- CriticalVulListCount，**类型Int**，支持操作：【eq】，**不支持排序**
- RiskCount，**类型Int**，支持操作：【eq】，**不支持排序**
- VulVersion，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- Virusver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- SysRepver，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- BaseBoardSn，类型String，支持操作：【eq，like，ilike】，支持排序
- Os，类型String，支持操作：【eq，like，ilike】，支持排序
- ConnActiveTime，类型String，支持操作：【eq，like，ilike】，**不支持排序**
- FirewallStatus，**类型Int**，支持操作：【eq】，**不支持排序**
- ProfileName，类型String，支持操作：【eq，like，ilike】，支持排序
- DomainName，类型String，支持操作：【eq，like，ilike】，支持排序
- SysRepVersion，类型String，支持操作：【eq，like，ilike】，支持排序
- VirusVer，类型String，支持操作：【eq，like，ilike】，支持排序
- Cpu，类型String，支持操作：【eq，like，ilike】，支持排序
- Memory，类型String，支持操作：【eq，like，ilike】，支持排序
- HardDiskSize，类型String，支持操作：【eq，like，ilike】，支持排序
- HardwareChangeCount，**类型Int**，支持操作：【eq】，支持排序
- AccountName，类型String，支持操作：【like.ilike】，支持排序
- AccountGroupName，类型String，支持操作：【like.ilike】，支持排序
- ScreenRecordingPermission，**类型Int**，支持操作：【eq】，支持排序
- DiskAccessPermission，**类型Int**，支持操作：【eq】，支持排序





分页参数
- PageNum 从1开始，小于等于0时使用默认参数
- PageSize 最大值5000，最好不超过100
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def GroupId(self):
        """【和GroupIds必须有一个填写】设备分组id（需要和OsType匹配），下面是私有化场景下默认id：
id-名称-操作系统
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


SaaS需要调用分组接口DescribeDeviceChildGroups获取对应分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        """【必填】操作系统类型（0: win，1：linux，2: mac，4：android，5：ios   默认值0），需要和GroupId或者GroupIds匹配
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OnlineStatus(self):
        """在线状态 （2表示在线，0或者1表示离线）
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Filters(self):
        """过滤条件--兼容旧接口,参数同Condition
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        """排序字段--兼容旧接口,参数同Condition
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageNum(self):
        """获取第几页--兼容旧接口,参数同Condition
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """每页获取数--兼容旧接口,参数同Condition
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        """授权状态： 4基础授权 5高级授权
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupIds(self):
        """【和GroupId必须有一个填写】设备分组id列表（需要和OsType匹配）

        :rtype: list of int
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


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
        self._GroupIds = params.get("GroupIds")
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
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """分页的data数据
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeDevicesPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLocalAccountAccountGroupsData(AbstractModel):
    """所属组

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 组Id(只支持32位)
        :type AccountGroupId: int
        """
        self._AccountGroupId = None

    @property
    def AccountGroupId(self):
        """组Id(只支持32位)
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsData(AbstractModel):
    """获取账号列表响应的单个对象

    """

    def __init__(self):
        r"""
        :param _Id: uid，数据库中唯一
        :type Id: int
        :param _UserId: 账号，登录账号
        :type UserId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _AccountId: 账号id，同Id字段
        :type AccountId: int
        :param _GroupId: 账号所在的分组id
        :type GroupId: int
        :param _GroupName: 账号所在的分组名称
        :type GroupName: str
        :param _NamePath: 账号所在的分组名称路径，用英文.分割
        :type NamePath: str
        :param _Source: 账号来源,0表示本地账号(只支持32位)
        :type Source: int
        :param _Status: 账号状态,0禁用，1启用(只支持32位)
        :type Status: int
        :param _Itime: 账号的创建时间
        :type Itime: str
        :param _Utime: 账号的最后更新时间
        :type Utime: str
        :param _ExtraInfo: 账号的扩展信息，包含邮箱、手机号、身份证、职位等信息
        :type ExtraInfo: str
        :param _RiskLevel: 用户风险等级，枚举：none, low, middle, high
        :type RiskLevel: str
        :param _AccountGroups: 所属组
        :type AccountGroups: list of DescribeLocalAccountAccountGroupsData
        :param _MobileBindNum: 绑定手机端设备数
        :type MobileBindNum: int
        :param _PcBindNum: 绑定Pc端设备数
        :type PcBindNum: int
        :param _OnlineStatus: 账号在线状态 1：在线 2：离线
        :type OnlineStatus: int
        :param _ActiveStatus: 账号活跃状态 1：活跃 2：非活跃
        :type ActiveStatus: int
        :param _LoginTime: 账号登录时间
        :type LoginTime: str
        :param _LogoutTime: 账号登出时间
        :type LogoutTime: str
        """
        self._Id = None
        self._UserId = None
        self._UserName = None
        self._AccountId = None
        self._GroupId = None
        self._GroupName = None
        self._NamePath = None
        self._Source = None
        self._Status = None
        self._Itime = None
        self._Utime = None
        self._ExtraInfo = None
        self._RiskLevel = None
        self._AccountGroups = None
        self._MobileBindNum = None
        self._PcBindNum = None
        self._OnlineStatus = None
        self._ActiveStatus = None
        self._LoginTime = None
        self._LogoutTime = None

    @property
    def Id(self):
        """uid，数据库中唯一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserId(self):
        """账号，登录账号
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AccountId(self):
        """账号id，同Id字段
        :rtype: int
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def GroupId(self):
        """账号所在的分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """账号所在的分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def NamePath(self):
        """账号所在的分组名称路径，用英文.分割
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def Source(self):
        """账号来源,0表示本地账号(只支持32位)
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Status(self):
        """账号状态,0禁用，1启用(只支持32位)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Itime(self):
        """账号的创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def Utime(self):
        """账号的最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ExtraInfo(self):
        """账号的扩展信息，包含邮箱、手机号、身份证、职位等信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def RiskLevel(self):
        """用户风险等级，枚举：none, low, middle, high
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def AccountGroups(self):
        """所属组
        :rtype: list of DescribeLocalAccountAccountGroupsData
        """
        return self._AccountGroups

    @AccountGroups.setter
    def AccountGroups(self, AccountGroups):
        self._AccountGroups = AccountGroups

    @property
    def MobileBindNum(self):
        """绑定手机端设备数
        :rtype: int
        """
        return self._MobileBindNum

    @MobileBindNum.setter
    def MobileBindNum(self, MobileBindNum):
        self._MobileBindNum = MobileBindNum

    @property
    def PcBindNum(self):
        """绑定Pc端设备数
        :rtype: int
        """
        return self._PcBindNum

    @PcBindNum.setter
    def PcBindNum(self, PcBindNum):
        self._PcBindNum = PcBindNum

    @property
    def OnlineStatus(self):
        """账号在线状态 1：在线 2：离线
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def ActiveStatus(self):
        """账号活跃状态 1：活跃 2：非活跃
        :rtype: int
        """
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def LoginTime(self):
        """账号登录时间
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def LogoutTime(self):
        """账号登出时间
        :rtype: str
        """
        return self._LogoutTime

    @LogoutTime.setter
    def LogoutTime(self, LogoutTime):
        self._LogoutTime = LogoutTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._AccountId = params.get("AccountId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._NamePath = params.get("NamePath")
        self._Source = params.get("Source")
        self._Status = params.get("Status")
        self._Itime = params.get("Itime")
        self._Utime = params.get("Utime")
        self._ExtraInfo = params.get("ExtraInfo")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("AccountGroups") is not None:
            self._AccountGroups = []
            for item in params.get("AccountGroups"):
                obj = DescribeLocalAccountAccountGroupsData()
                obj._deserialize(item)
                self._AccountGroups.append(obj)
        self._MobileBindNum = params.get("MobileBindNum")
        self._PcBindNum = params.get("PcBindNum")
        self._OnlineStatus = params.get("OnlineStatus")
        self._ActiveStatus = params.get("ActiveStatus")
        self._LoginTime = params.get("LoginTime")
        self._LogoutTime = params.get("LogoutTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsPage(AbstractModel):
    """获取账号列表响应的分页对象

    """

    def __init__(self):
        r"""
        :param _Page: 公共分页对象
        :type Page: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 获取账号列表响应的单个对象
        :type Items: list of DescribeLocalAccountsData
        """
        self._Page = None
        self._Items = None

    @property
    def Page(self):
        """公共分页对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Paging`
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Items(self):
        """获取账号列表响应的单个对象
        :rtype: list of DescribeLocalAccountsData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Page") is not None:
            self._Page = Paging()
            self._Page._deserialize(params.get("Page"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeLocalAccountsData()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsRequest(AbstractModel):
    """DescribeLocalAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 查询条件：过滤或排序
1、UserName，string类型，姓名
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
2、UserId，string类型，账户
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
3、Phone，string类型，手机号
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _AccountGroupId: 获取账号的分组ID，不传默认获取全网根账号组
        :type AccountGroupId: int
        :param _ShowFlag: 是否仅展示当前目录下用户 1： 递归显示 2：仅显示当前目录下用户
        :type ShowFlag: int
        """
        self._Condition = None
        self._AccountGroupId = None
        self._ShowFlag = None

    @property
    def Condition(self):
        """查询条件：过滤或排序
1、UserName，string类型，姓名
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
2、UserId，string类型，账户
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
3、Phone，string类型，手机号
是否必填：否
过滤支持：是，支持eq、like、ilike
排序支持：否
        :rtype: :class:`tencentcloud.ioa.v20220601.models.Condition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def AccountGroupId(self):
        """获取账号的分组ID，不传默认获取全网根账号组
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ShowFlag(self):
        """是否仅展示当前目录下用户 1： 递归显示 2：仅显示当前目录下用户
        :rtype: int
        """
        return self._ShowFlag

    @ShowFlag.setter
    def ShowFlag(self, ShowFlag):
        self._ShowFlag = ShowFlag


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._AccountGroupId = params.get("AccountGroupId")
        self._ShowFlag = params.get("ShowFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalAccountsResponse(AbstractModel):
    """DescribeLocalAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 获取账号列表响应的分页对象
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """获取账号列表响应的分页对象
        :rtype: :class:`tencentcloud.ioa.v20220601.models.DescribeLocalAccountsPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeLocalAccountsPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRootAccountGroupRequest(AbstractModel):
    """DescribeRootAccountGroup请求参数结构体

    """


class DescribeRootAccountGroupResponse(AbstractModel):
    """DescribeRootAccountGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号根分组响应详情
        :type Data: :class:`tencentcloud.ioa.v20220601.models.GetAccountGroupData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """账号根分组响应详情
        :rtype: :class:`tencentcloud.ioa.v20220601.models.GetAccountGroupData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = GetAccountGroupData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeviceDetail(AbstractModel):
    """业务响应数据

    """

    def __init__(self):
        r"""
        :param _Id: 设备ID
        :type Id: int
        :param _Mid: 设备唯一标识码，在ioa中每个设备有唯一标识码
        :type Mid: str
        :param _Name: 终端名（设备名）
        :type Name: str
        :param _GroupId: 设备所在分组ID
        :type GroupId: int
        :param _OsType: OS平台，0：Windows 、1： Linux、 2：macOS 、4： Android、 5: iOS。默认是0
        :type OsType: int
        :param _Ip: 设备IP地址（出口IP）
        :type Ip: str
        :param _OnlineStatus: 在线状态，2：在线、0或者1:离线
        :type OnlineStatus: int
        :param _Version: 客户端版本号-大整数
        :type Version: str
        :param _StrVersion: 客户端版本号-点分字符串
        :type StrVersion: str
        :param _Itime: 首次在线时间
        :type Itime: str
        :param _ConnActiveTime: 最后一次在线时间
        :type ConnActiveTime: str
        :param _Locked: 设备是否加锁 ，1：锁定 0或者2：未锁定。
        :type Locked: int
        :param _LocalIpList: 设备本地IP列表, 包括IP
        :type LocalIpList: str
        :param _HostId: 宿主机id（需要宿主机也安装iOA才能显示）
        :type HostId: int
        :param _GroupName: 设备所属分组名
        :type GroupName: str
        :param _GroupNamePath: 设备所属分组路径
        :type GroupNamePath: str
        :param _CriticalVulListCount: 未修复高危漏洞数(只支持32位)
        :type CriticalVulListCount: int
        :param _ComputerName: 设备名，和Name相同
        :type ComputerName: str
        :param _DomainName: 登录域名
        :type DomainName: str
        :param _MacAddr: MAC地址
        :type MacAddr: str
        :param _VulCount: 漏洞数
        :type VulCount: int
        :param _RiskCount: 病毒风险数
        :type RiskCount: int
        :param _VirusVer: 病毒库版本
        :type VirusVer: str
        :param _VulVersion: 漏洞库版本
        :type VulVersion: str
        :param _SysRepVersion: 系统修复引擎版本
        :type SysRepVersion: str
        :param _VulCriticalList: 高危补丁列表
        :type VulCriticalList: list of str
        :param _Tags: 标签
        :type Tags: str
        :param _UserName: 终端用户名
        :type UserName: str
        :param _FirewallStatus: 防火墙状态，不等于0表示开启
        :type FirewallStatus: int
        :param _SerialNum: SN序列号
        :type SerialNum: str
        :param _DeviceStrategyVer: 设备管控策略版本
        :type DeviceStrategyVer: str
        :param _NGNStrategyVer: NGN策略版本
        :type NGNStrategyVer: str
        :param _IOAUserName: 最近登录账户的账号
        :type IOAUserName: str
        :param _DeviceNewStrategyVer: 设备管控新策略
        :type DeviceNewStrategyVer: str
        :param _NGNNewStrategyVer: NGN策略新版本
        :type NGNNewStrategyVer: str
        :param _HostName: 宿主机名称（需要宿主机也安装iOA才能显示）
        :type HostName: str
        :param _BaseBoardSn: 主板序列号
        :type BaseBoardSn: str
        :param _AccountUsers: 绑定账户名称
        :type AccountUsers: str
        :param _IdentityStrategyVer: 身份策略版本
        :type IdentityStrategyVer: str
        :param _IdentityNewStrategyVer: 身份策略新版本
        :type IdentityNewStrategyVer: str
        :param _AccountGroupName: 最近登录账号部门
        :type AccountGroupName: str
        :param _AccountName: 最近登录账户的姓名
        :type AccountName: str
        :param _AccountGroupId: 账号组id
        :type AccountGroupId: int
        """
        self._Id = None
        self._Mid = None
        self._Name = None
        self._GroupId = None
        self._OsType = None
        self._Ip = None
        self._OnlineStatus = None
        self._Version = None
        self._StrVersion = None
        self._Itime = None
        self._ConnActiveTime = None
        self._Locked = None
        self._LocalIpList = None
        self._HostId = None
        self._GroupName = None
        self._GroupNamePath = None
        self._CriticalVulListCount = None
        self._ComputerName = None
        self._DomainName = None
        self._MacAddr = None
        self._VulCount = None
        self._RiskCount = None
        self._VirusVer = None
        self._VulVersion = None
        self._SysRepVersion = None
        self._VulCriticalList = None
        self._Tags = None
        self._UserName = None
        self._FirewallStatus = None
        self._SerialNum = None
        self._DeviceStrategyVer = None
        self._NGNStrategyVer = None
        self._IOAUserName = None
        self._DeviceNewStrategyVer = None
        self._NGNNewStrategyVer = None
        self._HostName = None
        self._BaseBoardSn = None
        self._AccountUsers = None
        self._IdentityStrategyVer = None
        self._IdentityNewStrategyVer = None
        self._AccountGroupName = None
        self._AccountName = None
        self._AccountGroupId = None

    @property
    def Id(self):
        """设备ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Mid(self):
        """设备唯一标识码，在ioa中每个设备有唯一标识码
        :rtype: str
        """
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Name(self):
        """终端名（设备名）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupId(self):
        """设备所在分组ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        """OS平台，0：Windows 、1： Linux、 2：macOS 、4： Android、 5: iOS。默认是0
        :rtype: int
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Ip(self):
        """设备IP地址（出口IP）
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def OnlineStatus(self):
        """在线状态，2：在线、0或者1:离线
        :rtype: int
        """
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Version(self):
        """客户端版本号-大整数
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def StrVersion(self):
        """客户端版本号-点分字符串
        :rtype: str
        """
        return self._StrVersion

    @StrVersion.setter
    def StrVersion(self, StrVersion):
        self._StrVersion = StrVersion

    @property
    def Itime(self):
        """首次在线时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ConnActiveTime(self):
        """最后一次在线时间
        :rtype: str
        """
        return self._ConnActiveTime

    @ConnActiveTime.setter
    def ConnActiveTime(self, ConnActiveTime):
        self._ConnActiveTime = ConnActiveTime

    @property
    def Locked(self):
        """设备是否加锁 ，1：锁定 0或者2：未锁定。
        :rtype: int
        """
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def LocalIpList(self):
        """设备本地IP列表, 包括IP
        :rtype: str
        """
        return self._LocalIpList

    @LocalIpList.setter
    def LocalIpList(self, LocalIpList):
        self._LocalIpList = LocalIpList

    @property
    def HostId(self):
        """宿主机id（需要宿主机也安装iOA才能显示）
        :rtype: int
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def GroupName(self):
        """设备所属分组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNamePath(self):
        """设备所属分组路径
        :rtype: str
        """
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def CriticalVulListCount(self):
        """未修复高危漏洞数(只支持32位)
        :rtype: int
        """
        return self._CriticalVulListCount

    @CriticalVulListCount.setter
    def CriticalVulListCount(self, CriticalVulListCount):
        self._CriticalVulListCount = CriticalVulListCount

    @property
    def ComputerName(self):
        """设备名，和Name相同
        :rtype: str
        """
        return self._ComputerName

    @ComputerName.setter
    def ComputerName(self, ComputerName):
        self._ComputerName = ComputerName

    @property
    def DomainName(self):
        """登录域名
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def MacAddr(self):
        """MAC地址
        :rtype: str
        """
        return self._MacAddr

    @MacAddr.setter
    def MacAddr(self, MacAddr):
        self._MacAddr = MacAddr

    @property
    def VulCount(self):
        """漏洞数
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def RiskCount(self):
        """病毒风险数
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def VirusVer(self):
        """病毒库版本
        :rtype: str
        """
        return self._VirusVer

    @VirusVer.setter
    def VirusVer(self, VirusVer):
        self._VirusVer = VirusVer

    @property
    def VulVersion(self):
        """漏洞库版本
        :rtype: str
        """
        return self._VulVersion

    @VulVersion.setter
    def VulVersion(self, VulVersion):
        self._VulVersion = VulVersion

    @property
    def SysRepVersion(self):
        """系统修复引擎版本
        :rtype: str
        """
        return self._SysRepVersion

    @SysRepVersion.setter
    def SysRepVersion(self, SysRepVersion):
        self._SysRepVersion = SysRepVersion

    @property
    def VulCriticalList(self):
        """高危补丁列表
        :rtype: list of str
        """
        return self._VulCriticalList

    @VulCriticalList.setter
    def VulCriticalList(self, VulCriticalList):
        self._VulCriticalList = VulCriticalList

    @property
    def Tags(self):
        """标签
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UserName(self):
        """终端用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def FirewallStatus(self):
        """防火墙状态，不等于0表示开启
        :rtype: int
        """
        return self._FirewallStatus

    @FirewallStatus.setter
    def FirewallStatus(self, FirewallStatus):
        self._FirewallStatus = FirewallStatus

    @property
    def SerialNum(self):
        """SN序列号
        :rtype: str
        """
        return self._SerialNum

    @SerialNum.setter
    def SerialNum(self, SerialNum):
        self._SerialNum = SerialNum

    @property
    def DeviceStrategyVer(self):
        """设备管控策略版本
        :rtype: str
        """
        return self._DeviceStrategyVer

    @DeviceStrategyVer.setter
    def DeviceStrategyVer(self, DeviceStrategyVer):
        self._DeviceStrategyVer = DeviceStrategyVer

    @property
    def NGNStrategyVer(self):
        """NGN策略版本
        :rtype: str
        """
        return self._NGNStrategyVer

    @NGNStrategyVer.setter
    def NGNStrategyVer(self, NGNStrategyVer):
        self._NGNStrategyVer = NGNStrategyVer

    @property
    def IOAUserName(self):
        """最近登录账户的账号
        :rtype: str
        """
        return self._IOAUserName

    @IOAUserName.setter
    def IOAUserName(self, IOAUserName):
        self._IOAUserName = IOAUserName

    @property
    def DeviceNewStrategyVer(self):
        """设备管控新策略
        :rtype: str
        """
        return self._DeviceNewStrategyVer

    @DeviceNewStrategyVer.setter
    def DeviceNewStrategyVer(self, DeviceNewStrategyVer):
        self._DeviceNewStrategyVer = DeviceNewStrategyVer

    @property
    def NGNNewStrategyVer(self):
        """NGN策略新版本
        :rtype: str
        """
        return self._NGNNewStrategyVer

    @NGNNewStrategyVer.setter
    def NGNNewStrategyVer(self, NGNNewStrategyVer):
        self._NGNNewStrategyVer = NGNNewStrategyVer

    @property
    def HostName(self):
        """宿主机名称（需要宿主机也安装iOA才能显示）
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def BaseBoardSn(self):
        """主板序列号
        :rtype: str
        """
        return self._BaseBoardSn

    @BaseBoardSn.setter
    def BaseBoardSn(self, BaseBoardSn):
        self._BaseBoardSn = BaseBoardSn

    @property
    def AccountUsers(self):
        """绑定账户名称
        :rtype: str
        """
        return self._AccountUsers

    @AccountUsers.setter
    def AccountUsers(self, AccountUsers):
        self._AccountUsers = AccountUsers

    @property
    def IdentityStrategyVer(self):
        """身份策略版本
        :rtype: str
        """
        return self._IdentityStrategyVer

    @IdentityStrategyVer.setter
    def IdentityStrategyVer(self, IdentityStrategyVer):
        self._IdentityStrategyVer = IdentityStrategyVer

    @property
    def IdentityNewStrategyVer(self):
        """身份策略新版本
        :rtype: str
        """
        return self._IdentityNewStrategyVer

    @IdentityNewStrategyVer.setter
    def IdentityNewStrategyVer(self, IdentityNewStrategyVer):
        self._IdentityNewStrategyVer = IdentityNewStrategyVer

    @property
    def AccountGroupName(self):
        """最近登录账号部门
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def AccountName(self):
        """最近登录账户的姓名
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountGroupId(self):
        """账号组id
        :rtype: int
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Mid = params.get("Mid")
        self._Name = params.get("Name")
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._Ip = params.get("Ip")
        self._OnlineStatus = params.get("OnlineStatus")
        self._Version = params.get("Version")
        self._StrVersion = params.get("StrVersion")
        self._Itime = params.get("Itime")
        self._ConnActiveTime = params.get("ConnActiveTime")
        self._Locked = params.get("Locked")
        self._LocalIpList = params.get("LocalIpList")
        self._HostId = params.get("HostId")
        self._GroupName = params.get("GroupName")
        self._GroupNamePath = params.get("GroupNamePath")
        self._CriticalVulListCount = params.get("CriticalVulListCount")
        self._ComputerName = params.get("ComputerName")
        self._DomainName = params.get("DomainName")
        self._MacAddr = params.get("MacAddr")
        self._VulCount = params.get("VulCount")
        self._RiskCount = params.get("RiskCount")
        self._VirusVer = params.get("VirusVer")
        self._VulVersion = params.get("VulVersion")
        self._SysRepVersion = params.get("SysRepVersion")
        self._VulCriticalList = params.get("VulCriticalList")
        self._Tags = params.get("Tags")
        self._UserName = params.get("UserName")
        self._FirewallStatus = params.get("FirewallStatus")
        self._SerialNum = params.get("SerialNum")
        self._DeviceStrategyVer = params.get("DeviceStrategyVer")
        self._NGNStrategyVer = params.get("NGNStrategyVer")
        self._IOAUserName = params.get("IOAUserName")
        self._DeviceNewStrategyVer = params.get("DeviceNewStrategyVer")
        self._NGNNewStrategyVer = params.get("NGNNewStrategyVer")
        self._HostName = params.get("HostName")
        self._BaseBoardSn = params.get("BaseBoardSn")
        self._AccountUsers = params.get("AccountUsers")
        self._IdentityStrategyVer = params.get("IdentityStrategyVer")
        self._IdentityNewStrategyVer = params.get("IdentityNewStrategyVer")
        self._AccountGroupName = params.get("AccountGroupName")
        self._AccountName = params.get("AccountName")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filters 条件过滤

    """

    def __init__(self):
        r"""
        :param _Field: 过滤字段
        :type Field: str
        :param _Operator: 过滤方式： eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于。具体支持哪些过滤方式，结合具体接口字段描述来定
        :type Operator: str
        :param _Values: 过滤条件
        :type Values: list of str
        """
        self._Field = None
        self._Operator = None
        self._Values = None

    @property
    def Field(self):
        """过滤字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Operator(self):
        """过滤方式： eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于。具体支持哪些过滤方式，结合具体接口字段描述来定
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Values(self):
        """过滤条件
        :rtype: list of str
        """
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
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Filters 条件过滤
        :rtype: list of Filter
        """
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
        


class GetAccountGroupData(AbstractModel):
    """账号分组详情响应数据

    """

    def __init__(self):
        r"""
        :param _NamePath: 分组名称全路径，点分格式
        :type NamePath: str
        :param _IdPathArr: 分组ID全路径，数组格式
        :type IdPathArr: list of int
        :param _ExtraInfo: 分组扩展信息
        :type ExtraInfo: str
        :param _Utime: 最后更新时间
        :type Utime: str
        :param _ParentId: 当前分组的父分组ID
        :type ParentId: int
        :param _OrgId: 源账号组ID，该字段仅适用于第三方同步的组织架构，通过OrgId-Id构成源组织架构分组ID-现组织架构分组ID映射关系
        :type OrgId: str
        :param _Name: 分组名称
        :type Name: str
        :param _Id: 分组ID
        :type Id: int
        :param _Description: 分组描述
        :type Description: str
        :param _Source: 分组导入源(只支持32位)
        :type Source: int
        :param _IdPath: 分组ID全路径，点分格式
        :type IdPath: str
        :param _Itime: 创建时间
        :type Itime: str
        :param _ParentOrgId: 父源账号组ID，该字段仅适用于第三方同步的组织架构
        :type ParentOrgId: str
        :param _Import: 导入信息,json格式
        :type Import: str
        :param _ImportEnable: 是否开启导入架构
        :type ImportEnable: bool
        :param _ImportType: 导入类型
        :type ImportType: str
        :param _MiniIamId: miniIAMId，MiniIAM源才有
        :type MiniIamId: str
        """
        self._NamePath = None
        self._IdPathArr = None
        self._ExtraInfo = None
        self._Utime = None
        self._ParentId = None
        self._OrgId = None
        self._Name = None
        self._Id = None
        self._Description = None
        self._Source = None
        self._IdPath = None
        self._Itime = None
        self._ParentOrgId = None
        self._Import = None
        self._ImportEnable = None
        self._ImportType = None
        self._MiniIamId = None

    @property
    def NamePath(self):
        """分组名称全路径，点分格式
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def IdPathArr(self):
        """分组ID全路径，数组格式
        :rtype: list of int
        """
        return self._IdPathArr

    @IdPathArr.setter
    def IdPathArr(self, IdPathArr):
        self._IdPathArr = IdPathArr

    @property
    def ExtraInfo(self):
        """分组扩展信息
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Utime(self):
        """最后更新时间
        :rtype: str
        """
        return self._Utime

    @Utime.setter
    def Utime(self, Utime):
        self._Utime = Utime

    @property
    def ParentId(self):
        """当前分组的父分组ID
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def OrgId(self):
        """源账号组ID，该字段仅适用于第三方同步的组织架构，通过OrgId-Id构成源组织架构分组ID-现组织架构分组ID映射关系
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Name(self):
        """分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        """分组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        """分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        """分组导入源(只支持32位)
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def IdPath(self):
        """分组ID全路径，点分格式
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def Itime(self):
        """创建时间
        :rtype: str
        """
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ParentOrgId(self):
        """父源账号组ID，该字段仅适用于第三方同步的组织架构
        :rtype: str
        """
        return self._ParentOrgId

    @ParentOrgId.setter
    def ParentOrgId(self, ParentOrgId):
        self._ParentOrgId = ParentOrgId

    @property
    def Import(self):
        """导入信息,json格式
        :rtype: str
        """
        return self._Import

    @Import.setter
    def Import(self, Import):
        self._Import = Import

    @property
    def ImportEnable(self):
        """是否开启导入架构
        :rtype: bool
        """
        return self._ImportEnable

    @ImportEnable.setter
    def ImportEnable(self, ImportEnable):
        self._ImportEnable = ImportEnable

    @property
    def ImportType(self):
        """导入类型
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def MiniIamId(self):
        """miniIAMId，MiniIAM源才有
        :rtype: str
        """
        return self._MiniIamId

    @MiniIamId.setter
    def MiniIamId(self, MiniIamId):
        self._MiniIamId = MiniIamId


    def _deserialize(self, params):
        self._NamePath = params.get("NamePath")
        self._IdPathArr = params.get("IdPathArr")
        self._ExtraInfo = params.get("ExtraInfo")
        self._Utime = params.get("Utime")
        self._ParentId = params.get("ParentId")
        self._OrgId = params.get("OrgId")
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._IdPath = params.get("IdPath")
        self._Itime = params.get("Itime")
        self._ParentOrgId = params.get("ParentOrgId")
        self._Import = params.get("Import")
        self._ImportEnable = params.get("ImportEnable")
        self._ImportType = params.get("ImportType")
        self._MiniIamId = params.get("MiniIamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """页码

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageCount: 总页数
        :type PageCount: int
        :param _Total: 记录总数
        :type Total: int
        """
        self._PageSize = None
        self._PageNum = None
        self._PageCount = None
        self._Total = None

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """页码
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageCount(self):
        """总页数
        :rtype: int
        """
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def Total(self):
        """记录总数
        :rtype: int
        """
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
        


class RuleExpression(AbstractModel):
    """规则表达式

    """

    def __init__(self):
        r"""
        :param _Items: 规则元数据
        :type Items: list of RuleItem
        :param _Relation: 关系
        :type Relation: str
        """
        self._Items = None
        self._Relation = None

    @property
    def Items(self):
        """规则元数据
        :rtype: list of RuleItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Relation(self):
        """关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RuleItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """规则元数据

    """

    def __init__(self):
        r"""
        :param _Key: 字段名称
        :type Key: str
        :param _Operate: 操作关系（等于、不等于、包含、不包含）
        :type Operate: str
        :param _Value: 内容
        :type Value: str
        :param _Values: 内容，v2多值版本使用
        :type Values: list of str
        """
        self._Key = None
        self._Operate = None
        self._Value = None
        self._Values = None

    @property
    def Key(self):
        """字段名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operate(self):
        """操作关系（等于、不等于、包含、不包含）
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def Value(self):
        """内容
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Values(self):
        """内容，v2多值版本使用
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operate = params.get("Operate")
        self._Value = params.get("Value")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleRule(AbstractModel):
    """简单规则表达式

    """

    def __init__(self):
        r"""
        :param _Expressions: 规则表达式
        :type Expressions: list of RuleExpression
        :param _Relation: 表达式间逻辑关系
        :type Relation: str
        """
        self._Expressions = None
        self._Relation = None

    @property
    def Expressions(self):
        """规则表达式
        :rtype: list of RuleExpression
        """
        return self._Expressions

    @Expressions.setter
    def Expressions(self, Expressions):
        self._Expressions = Expressions

    @property
    def Relation(self):
        """表达式间逻辑关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("Expressions") is not None:
            self._Expressions = []
            for item in params.get("Expressions"):
                obj = RuleExpression()
                obj._deserialize(item)
                self._Expressions.append(obj)
        self._Relation = params.get("Relation")
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
        :type Field: str
        :param _Order: 排序方式
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        """排序字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        """排序方式
        :rtype: str
        """
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
        