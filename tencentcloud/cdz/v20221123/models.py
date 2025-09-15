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


class CloudDedicatedZoneHostsInfo(AbstractModel):
    r"""CDZ的母机和子机的对应关系

    """

    def __init__(self):
        r"""
        :param _HostUuid: Host的唯一标识uuid
        :type HostUuid: str
        :param _InstancesInfo: 实例名称数组
        :type InstancesInfo: list of str
        """
        self._HostUuid = None
        self._InstancesInfo = None

    @property
    def HostUuid(self):
        r"""Host的唯一标识uuid
        :rtype: str
        """
        return self._HostUuid

    @HostUuid.setter
    def HostUuid(self, HostUuid):
        self._HostUuid = HostUuid

    @property
    def InstancesInfo(self):
        r"""实例名称数组
        :rtype: list of str
        """
        return self._InstancesInfo

    @InstancesInfo.setter
    def InstancesInfo(self, InstancesInfo):
        self._InstancesInfo = InstancesInfo


    def _deserialize(self, params):
        self._HostUuid = params.get("HostUuid")
        self._InstancesInfo = params.get("InstancesInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudDedicatedZoneResourceStatisticsInfo(AbstractModel):
    r"""专属可用区资源统计项数据详情，对应一个具体的垂直产品的资源统计项。

    """

    def __init__(self):
        r"""
        :param _Item: 资源统计项名称
        :type Item: str
        :param _Unit: 资源统计项单位
        :type Unit: str
        :param _Total: 资源总量
        :type Total: str
        :param _Usage: 已用资源
        :type Usage: str
        :param _UsageRate: 已用资源占比
        :type UsageRate: str
        :param _Remain: 剩余资源
        :type Remain: str
        :param _RemainRate: 剩余资源占比
        :type RemainRate: str
        :param _ThisMondayUsageRate: 本周一零点资源使用率
        :type ThisMondayUsageRate: str
        :param _ThisMondayUsageGrowthRate: 本周资源增长比例
        :type ThisMondayUsageGrowthRate: str
        :param _LastMondayUsageGrowthRate: 上周资源增长比例
        :type LastMondayUsageGrowthRate: str
        """
        self._Item = None
        self._Unit = None
        self._Total = None
        self._Usage = None
        self._UsageRate = None
        self._Remain = None
        self._RemainRate = None
        self._ThisMondayUsageRate = None
        self._ThisMondayUsageGrowthRate = None
        self._LastMondayUsageGrowthRate = None

    @property
    def Item(self):
        r"""资源统计项名称
        :rtype: str
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Unit(self):
        r"""资源统计项单位
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Total(self):
        r"""资源总量
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Usage(self):
        r"""已用资源
        :rtype: str
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def UsageRate(self):
        r"""已用资源占比
        :rtype: str
        """
        return self._UsageRate

    @UsageRate.setter
    def UsageRate(self, UsageRate):
        self._UsageRate = UsageRate

    @property
    def Remain(self):
        r"""剩余资源
        :rtype: str
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def RemainRate(self):
        r"""剩余资源占比
        :rtype: str
        """
        return self._RemainRate

    @RemainRate.setter
    def RemainRate(self, RemainRate):
        self._RemainRate = RemainRate

    @property
    def ThisMondayUsageRate(self):
        r"""本周一零点资源使用率
        :rtype: str
        """
        return self._ThisMondayUsageRate

    @ThisMondayUsageRate.setter
    def ThisMondayUsageRate(self, ThisMondayUsageRate):
        self._ThisMondayUsageRate = ThisMondayUsageRate

    @property
    def ThisMondayUsageGrowthRate(self):
        r"""本周资源增长比例
        :rtype: str
        """
        return self._ThisMondayUsageGrowthRate

    @ThisMondayUsageGrowthRate.setter
    def ThisMondayUsageGrowthRate(self, ThisMondayUsageGrowthRate):
        self._ThisMondayUsageGrowthRate = ThisMondayUsageGrowthRate

    @property
    def LastMondayUsageGrowthRate(self):
        r"""上周资源增长比例
        :rtype: str
        """
        return self._LastMondayUsageGrowthRate

    @LastMondayUsageGrowthRate.setter
    def LastMondayUsageGrowthRate(self, LastMondayUsageGrowthRate):
        self._LastMondayUsageGrowthRate = LastMondayUsageGrowthRate


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._Unit = params.get("Unit")
        self._Total = params.get("Total")
        self._Usage = params.get("Usage")
        self._UsageRate = params.get("UsageRate")
        self._Remain = params.get("Remain")
        self._RemainRate = params.get("RemainRate")
        self._ThisMondayUsageRate = params.get("ThisMondayUsageRate")
        self._ThisMondayUsageGrowthRate = params.get("ThisMondayUsageGrowthRate")
        self._LastMondayUsageGrowthRate = params.get("LastMondayUsageGrowthRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudDedicatedZoneResourceSummaryInfo(AbstractModel):
    r"""专属可用区资源水位数据详情，对应一个具体的垂直产品。

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _SubProductName: 子产品名称
        :type SubProductName: str
        :param _Statistics: 资源统计详情
        :type Statistics: list of CloudDedicatedZoneResourceStatisticsInfo
        """
        self._ProductName = None
        self._SubProductName = None
        self._Statistics = None

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def SubProductName(self):
        r"""子产品名称
        :rtype: str
        """
        return self._SubProductName

    @SubProductName.setter
    def SubProductName(self, SubProductName):
        self._SubProductName = SubProductName

    @property
    def Statistics(self):
        r"""资源统计详情
        :rtype: list of CloudDedicatedZoneResourceStatisticsInfo
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._SubProductName = params.get("SubProductName")
        if params.get("Statistics") is not None:
            self._Statistics = []
            for item in params.get("Statistics"):
                obj = CloudDedicatedZoneResourceStatisticsInfo()
                obj._deserialize(item)
                self._Statistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudDedicatedZoneHostsRequest(AbstractModel):
    r"""DescribeCloudDedicatedZoneHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudDedicatedZoneID: 专属可用区ID 
        :type CloudDedicatedZoneID: str
        :param _HostUuids: 一个或多个Host面的CVM实例信息。最大支持查询100台Host。
        :type HostUuids: list of str
        :param _InstanceIds: 查询一个实例或者多个实例所在的Host上面的CVM实例信息。最大支持查询100台实例。
        :type InstanceIds: list of str
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。该参数仅与CloudDedicatedZoneID有关，传递了HostUuids和InstanceIds则会失效。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。该参数仅与CloudDedicatedZoneID有关，传递了HostUuids和InstanceIds则会失效。
        :type Limit: int
        """
        self._CloudDedicatedZoneID = None
        self._HostUuids = None
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def CloudDedicatedZoneID(self):
        r"""专属可用区ID 
        :rtype: str
        """
        return self._CloudDedicatedZoneID

    @CloudDedicatedZoneID.setter
    def CloudDedicatedZoneID(self, CloudDedicatedZoneID):
        self._CloudDedicatedZoneID = CloudDedicatedZoneID

    @property
    def HostUuids(self):
        r"""一个或多个Host面的CVM实例信息。最大支持查询100台Host。
        :rtype: list of str
        """
        return self._HostUuids

    @HostUuids.setter
    def HostUuids(self, HostUuids):
        self._HostUuids = HostUuids

    @property
    def InstanceIds(self):
        r"""查询一个实例或者多个实例所在的Host上面的CVM实例信息。最大支持查询100台实例。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        r"""偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。该参数仅与CloudDedicatedZoneID有关，传递了HostUuids和InstanceIds则会失效。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。该参数仅与CloudDedicatedZoneID有关，传递了HostUuids和InstanceIds则会失效。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CloudDedicatedZoneID = params.get("CloudDedicatedZoneID")
        self._HostUuids = params.get("HostUuids")
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudDedicatedZoneHostsResponse(AbstractModel):
    r"""DescribeCloudDedicatedZoneHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudDedicatedZoneHostsInfoSet: 返回Host和Host上部署的实例信息之间的关系
        :type CloudDedicatedZoneHostsInfoSet: list of CloudDedicatedZoneHostsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CloudDedicatedZoneHostsInfoSet = None
        self._RequestId = None

    @property
    def CloudDedicatedZoneHostsInfoSet(self):
        r"""返回Host和Host上部署的实例信息之间的关系
        :rtype: list of CloudDedicatedZoneHostsInfo
        """
        return self._CloudDedicatedZoneHostsInfoSet

    @CloudDedicatedZoneHostsInfoSet.setter
    def CloudDedicatedZoneHostsInfoSet(self, CloudDedicatedZoneHostsInfoSet):
        self._CloudDedicatedZoneHostsInfoSet = CloudDedicatedZoneHostsInfoSet

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
        if params.get("CloudDedicatedZoneHostsInfoSet") is not None:
            self._CloudDedicatedZoneHostsInfoSet = []
            for item in params.get("CloudDedicatedZoneHostsInfoSet"):
                obj = CloudDedicatedZoneHostsInfo()
                obj._deserialize(item)
                self._CloudDedicatedZoneHostsInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudDedicatedZoneResourceSummaryRequest(AbstractModel):
    r"""DescribeCloudDedicatedZoneResourceSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CdzId: 专属可用区唯一标识
        :type CdzId: str
        """
        self._CdzId = None

    @property
    def CdzId(self):
        r"""专属可用区唯一标识
        :rtype: str
        """
        return self._CdzId

    @CdzId.setter
    def CdzId(self, CdzId):
        self._CdzId = CdzId


    def _deserialize(self, params):
        self._CdzId = params.get("CdzId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudDedicatedZoneResourceSummaryResponse(AbstractModel):
    r"""DescribeCloudDedicatedZoneResourceSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSummarySet: 资源水位详情
        :type ResourceSummarySet: list of CloudDedicatedZoneResourceSummaryInfo
        :param _ExtraInfo: 资源水位扩展信息
        :type ExtraInfo: :class:`tencentcloud.cdz.v20221123.models.ExtraInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSummarySet = None
        self._ExtraInfo = None
        self._RequestId = None

    @property
    def ResourceSummarySet(self):
        r"""资源水位详情
        :rtype: list of CloudDedicatedZoneResourceSummaryInfo
        """
        return self._ResourceSummarySet

    @ResourceSummarySet.setter
    def ResourceSummarySet(self, ResourceSummarySet):
        self._ResourceSummarySet = ResourceSummarySet

    @property
    def ExtraInfo(self):
        r"""资源水位扩展信息
        :rtype: :class:`tencentcloud.cdz.v20221123.models.ExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

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
        if params.get("ResourceSummarySet") is not None:
            self._ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = CloudDedicatedZoneResourceSummaryInfo()
                obj._deserialize(item)
                self._ResourceSummarySet.append(obj)
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._RequestId = params.get("RequestId")


class ExtraInfo(AbstractModel):
    r"""专属可用区资源水位数据扩展信息，包含可用区当地时间等数据。

    """

    def __init__(self):
        r"""
        :param _ThisMondayLocalDate: 专属可用区当地时间本周一日期
        :type ThisMondayLocalDate: str
        :param _LastMondayLocalDate: 专属可用区当地时间上周一日期
        :type LastMondayLocalDate: str
        """
        self._ThisMondayLocalDate = None
        self._LastMondayLocalDate = None

    @property
    def ThisMondayLocalDate(self):
        r"""专属可用区当地时间本周一日期
        :rtype: str
        """
        return self._ThisMondayLocalDate

    @ThisMondayLocalDate.setter
    def ThisMondayLocalDate(self, ThisMondayLocalDate):
        self._ThisMondayLocalDate = ThisMondayLocalDate

    @property
    def LastMondayLocalDate(self):
        r"""专属可用区当地时间上周一日期
        :rtype: str
        """
        return self._LastMondayLocalDate

    @LastMondayLocalDate.setter
    def LastMondayLocalDate(self, LastMondayLocalDate):
        self._LastMondayLocalDate = LastMondayLocalDate


    def _deserialize(self, params):
        self._ThisMondayLocalDate = params.get("ThisMondayLocalDate")
        self._LastMondayLocalDate = params.get("LastMondayLocalDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        