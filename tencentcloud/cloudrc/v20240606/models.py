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


class DescribeResourceRequest(AbstractModel):
    r"""DescribeResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: <p>资源类型</p>
        :type ResourceType: str
        :param _RegionCode: <p>地域编码</p>
        :type RegionCode: str
        :param _ResourceId: <p>资源ID</p>
        :type ResourceId: str
        :param _ViewId: <p>视图ID</p>
        :type ViewId: str
        """
        self._ResourceType = None
        self._RegionCode = None
        self._ResourceId = None
        self._ViewId = None

    @property
    def ResourceType(self):
        r"""<p>资源类型</p>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def RegionCode(self):
        r"""<p>地域编码</p>
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def ResourceId(self):
        r"""<p>资源ID</p>
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ViewId(self):
        r"""<p>视图ID</p>
        :rtype: str
        """
        return self._ViewId

    @ViewId.setter
    def ViewId(self, ViewId):
        self._ViewId = ViewId


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._RegionCode = params.get("RegionCode")
        self._ResourceId = params.get("ResourceId")
        self._ViewId = params.get("ViewId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceResponse(AbstractModel):
    r"""DescribeResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: <p>资源ID</p>
        :type ResourceId: str
        :param _ResourceAlias: <p>资源别名</p>
        :type ResourceAlias: str
        :param _Uin: <p>uin</p>
        :type Uin: int
        :param _ResourceType: <p>资源类型</p>
        :type ResourceType: str
        :param _RegionCode: <p>地域编码</p>
        :type RegionCode: str
        :param _ZoneCode: <p>可用区编码</p>
        :type ZoneCode: str
        :param _PayMode: <p>付费类型</p>
        :type PayMode: str
        :param _CreateTime: <p>资源创建时间</p>
        :type CreateTime: str
        :param _ExpireTime: <p>资源过期时间</p>
        :type ExpireTime: str
        :param _PrivateIpAddress: <p>内网IP</p>
        :type PrivateIpAddress: list of str
        :param _PublicIpAddress: <p>外网IP</p>
        :type PublicIpAddress: list of str
        :param _Properties: <p>资源属性</p>
        :type Properties: str
        :param _Tags: <p>标签信息</p>
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._ResourceAlias = None
        self._Uin = None
        self._ResourceType = None
        self._RegionCode = None
        self._ZoneCode = None
        self._PayMode = None
        self._CreateTime = None
        self._ExpireTime = None
        self._PrivateIpAddress = None
        self._PublicIpAddress = None
        self._Properties = None
        self._Tags = None
        self._RequestId = None

    @property
    def ResourceId(self):
        r"""<p>资源ID</p>
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceAlias(self):
        r"""<p>资源别名</p>
        :rtype: str
        """
        return self._ResourceAlias

    @ResourceAlias.setter
    def ResourceAlias(self, ResourceAlias):
        self._ResourceAlias = ResourceAlias

    @property
    def Uin(self):
        r"""<p>uin</p>
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ResourceType(self):
        r"""<p>资源类型</p>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def RegionCode(self):
        r"""<p>地域编码</p>
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def ZoneCode(self):
        r"""<p>可用区编码</p>
        :rtype: str
        """
        return self._ZoneCode

    @ZoneCode.setter
    def ZoneCode(self, ZoneCode):
        self._ZoneCode = ZoneCode

    @property
    def PayMode(self):
        r"""<p>付费类型</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        r"""<p>资源创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""<p>资源过期时间</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PrivateIpAddress(self):
        r"""<p>内网IP</p>
        :rtype: list of str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def PublicIpAddress(self):
        r"""<p>外网IP</p>
        :rtype: list of str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def Properties(self):
        r"""<p>资源属性</p>
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Tags(self):
        r"""<p>标签信息</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceAlias = params.get("ResourceAlias")
        self._Uin = params.get("Uin")
        self._ResourceType = params.get("ResourceType")
        self._RegionCode = params.get("RegionCode")
        self._ZoneCode = params.get("ZoneCode")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._Properties = params.get("Properties")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class ExtendedFilter(AbstractModel):
    r"""过滤器

    """

    def __init__(self):
        r"""
        :param _Key: <p>过滤条件键</p><p>枚举值：</p><ul><li>ResourceType： 资源类型</li><li>ResourceId： 资源ID</li><li>ResourceAlias： 资源名称</li><li>PayMode： 计费模式</li><li>RegionCode： 地域编码</li><li>ZoneCode： 可用区编码</li><li>PublicIpAddress： 外网IP</li><li>PrivateIpAddress： 内网IP</li><li>VpcId： VPC ID</li><li>SubnetId： 子网ID</li><li>Tag： 标签</li></ul>
        :type Key: str
        :param _Values: <p>过滤条件值</p>
        :type Values: list of str
        :param _MatchType: <p>匹配方式</p><p>枚举值：</p><ul><li>Equals： 等于</li><li>NotEquals： 不等于</li><li>Contains： 包含</li><li>NotContains： 不包含</li><li>Exists： 存在</li><li>NotExists： 不存在</li></ul>
        :type MatchType: str
        """
        self._Key = None
        self._Values = None
        self._MatchType = None

    @property
    def Key(self):
        r"""<p>过滤条件键</p><p>枚举值：</p><ul><li>ResourceType： 资源类型</li><li>ResourceId： 资源ID</li><li>ResourceAlias： 资源名称</li><li>PayMode： 计费模式</li><li>RegionCode： 地域编码</li><li>ZoneCode： 可用区编码</li><li>PublicIpAddress： 外网IP</li><li>PrivateIpAddress： 内网IP</li><li>VpcId： VPC ID</li><li>SubnetId： 子网ID</li><li>Tag： 标签</li></ul>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""<p>过滤条件值</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def MatchType(self):
        r"""<p>匹配方式</p><p>枚举值：</p><ul><li>Equals： 等于</li><li>NotEquals： 不等于</li><li>Contains： 包含</li><li>NotContains： 不包含</li><li>Exists： 存在</li><li>NotExists： 不存在</li></ul>
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._MatchType = params.get("MatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceSummary(AbstractModel):
    r"""资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: <p>资源ID</p>
        :type ResourceId: str
        :param _ResourceAlias: <p>资源别名</p>
        :type ResourceAlias: str
        :param _Uin: <p>uin</p>
        :type Uin: int
        :param _ResourceType: <p>资源类型</p>
        :type ResourceType: str
        :param _RegionCode: <p>地域编码</p>
        :type RegionCode: str
        :param _ZoneCode: <p>可用区编码</p>
        :type ZoneCode: str
        :param _PayMode: <p>付费类型，包括后付费(0)、预付费(1)、预留实例(2)</p>
        :type PayMode: str
        :param _CreateTime: <p>资源创建时间</p>
        :type CreateTime: str
        :param _ExpireTime: <p>资源过期时间</p>
        :type ExpireTime: str
        :param _PrivateIpAddress: <p>内网IP</p>
        :type PrivateIpAddress: list of str
        :param _PublicIpAddress: <p>外网IP</p>
        :type PublicIpAddress: list of str
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        """
        self._ResourceId = None
        self._ResourceAlias = None
        self._Uin = None
        self._ResourceType = None
        self._RegionCode = None
        self._ZoneCode = None
        self._PayMode = None
        self._CreateTime = None
        self._ExpireTime = None
        self._PrivateIpAddress = None
        self._PublicIpAddress = None
        self._Tags = None

    @property
    def ResourceId(self):
        r"""<p>资源ID</p>
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceAlias(self):
        r"""<p>资源别名</p>
        :rtype: str
        """
        return self._ResourceAlias

    @ResourceAlias.setter
    def ResourceAlias(self, ResourceAlias):
        self._ResourceAlias = ResourceAlias

    @property
    def Uin(self):
        r"""<p>uin</p>
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ResourceType(self):
        r"""<p>资源类型</p>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def RegionCode(self):
        r"""<p>地域编码</p>
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def ZoneCode(self):
        r"""<p>可用区编码</p>
        :rtype: str
        """
        return self._ZoneCode

    @ZoneCode.setter
    def ZoneCode(self, ZoneCode):
        self._ZoneCode = ZoneCode

    @property
    def PayMode(self):
        r"""<p>付费类型，包括后付费(0)、预付费(1)、预留实例(2)</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        r"""<p>资源创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""<p>资源过期时间</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PrivateIpAddress(self):
        r"""<p>内网IP</p>
        :rtype: list of str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def PublicIpAddress(self):
        r"""<p>外网IP</p>
        :rtype: list of str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceAlias = params.get("ResourceAlias")
        self._Uin = params.get("Uin")
        self._ResourceType = params.get("ResourceType")
        self._RegionCode = params.get("RegionCode")
        self._ZoneCode = params.get("ZoneCode")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._PublicIpAddress = params.get("PublicIpAddress")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResourcesRequest(AbstractModel):
    r"""SearchResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ViewId: <p>视图ID</p>
        :type ViewId: str
        :param _MaxResults: <p>每页返回的最大记录数</p>
        :type MaxResults: int
        :param _NextToken: <p>分页Token，首次查询不传</p>
        :type NextToken: str
        :param _Filters: <p>过滤条件列表</p>
        :type Filters: list of ExtendedFilter
        :param _SortBy: <p>排序条件</p><p>枚举值：</p><ul><li>CreateTime： 表示按资源创建时间排序</li><li>ExpireTime： 表示按资源到期时间排序</li><li>IpAddress： 表示按资源IP地址排序</li></ul>
        :type SortBy: str
        :param _SortOrder: <p>排序顺序</p><p>枚举值：</p><ul><li>Asc： 升序</li><li>Desc： 降序</li></ul><p>默认值：Asc</p>
        :type SortOrder: str
        """
        self._ViewId = None
        self._MaxResults = None
        self._NextToken = None
        self._Filters = None
        self._SortBy = None
        self._SortOrder = None

    @property
    def ViewId(self):
        r"""<p>视图ID</p>
        :rtype: str
        """
        return self._ViewId

    @ViewId.setter
    def ViewId(self, ViewId):
        self._ViewId = ViewId

    @property
    def MaxResults(self):
        r"""<p>每页返回的最大记录数</p>
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>分页Token，首次查询不传</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Filters(self):
        r"""<p>过滤条件列表</p>
        :rtype: list of ExtendedFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        r"""<p>排序条件</p><p>枚举值：</p><ul><li>CreateTime： 表示按资源创建时间排序</li><li>ExpireTime： 表示按资源到期时间排序</li><li>IpAddress： 表示按资源IP地址排序</li></ul>
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def SortOrder(self):
        r"""<p>排序顺序</p><p>枚举值：</p><ul><li>Asc： 升序</li><li>Desc： 降序</li></ul><p>默认值：Asc</p>
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._ViewId = params.get("ViewId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ExtendedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResourcesResponse(AbstractModel):
    r"""SearchResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: <p>下一页Token，为空时表示无更多数据</p>
        :type NextToken: str
        :param _Resources: <p>资源列表</p>
        :type Resources: list of ResourceSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._Resources = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""<p>下一页Token，为空时表示无更多数据</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Resources(self):
        r"""<p>资源列表</p>
        :rtype: list of ResourceSummary
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceSummary()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        