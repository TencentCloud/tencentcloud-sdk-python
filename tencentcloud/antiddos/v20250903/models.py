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


class DDoSBlockRecord(AbstractModel):
    r"""封堵记录

    """

    def __init__(self):
        r"""
        :param _Resource: <p>被封堵的资源，公网 IP，示例如下：</p><ul><li> 公网 IP：117.175.94.231。</li></ul>
        :type Resource: str
        :param _BlockTime: <p>被封堵的时间。</p>
        :type BlockTime: str
        :param _Status: <p>封堵解封状态。</p><p>枚举值：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :type Status: str
        """
        self._Resource = None
        self._BlockTime = None
        self._Status = None

    @property
    def Resource(self):
        r"""<p>被封堵的资源，公网 IP，示例如下：</p><ul><li> 公网 IP：117.175.94.231。</li></ul>
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def BlockTime(self):
        r"""<p>被封堵的时间。</p>
        :rtype: str
        """
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def Status(self):
        r"""<p>封堵解封状态。</p><p>枚举值：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._BlockTime = params.get("BlockTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUnblockQuota(AbstractModel):
    r"""当前账号剩余解封配额信息。购买高防产品的用户默认解封配额为三个资源，系统将在每天零点（UTC+8）时区重置解封配额数，当天未使用的解封配额数不会累计到次日；DDoS 高防包（轻量版）解封配额数为每月三个资源，每月重置。

    """

    def __init__(self):
        r"""
        :param _TotalQuota: <p>解封次数配额总数。</p>
        :type TotalQuota: int
        :param _UsedQuota: <p>已使用的配额总数。</p>
        :type UsedQuota: int
        :param _QuotaStartTime: <p>配额生效的起始时间。</p>
        :type QuotaStartTime: str
        :param _QuotaEndTime: <p>配额生效的结束时间。</p>
        :type QuotaEndTime: str
        """
        self._TotalQuota = None
        self._UsedQuota = None
        self._QuotaStartTime = None
        self._QuotaEndTime = None

    @property
    def TotalQuota(self):
        r"""<p>解封次数配额总数。</p>
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def UsedQuota(self):
        r"""<p>已使用的配额总数。</p>
        :rtype: int
        """
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def QuotaStartTime(self):
        r"""<p>配额生效的起始时间。</p>
        :rtype: str
        """
        return self._QuotaStartTime

    @QuotaStartTime.setter
    def QuotaStartTime(self, QuotaStartTime):
        self._QuotaStartTime = QuotaStartTime

    @property
    def QuotaEndTime(self):
        r"""<p>配额生效的结束时间。</p>
        :rtype: str
        """
        return self._QuotaEndTime

    @QuotaEndTime.setter
    def QuotaEndTime(self, QuotaEndTime):
        self._QuotaEndTime = QuotaEndTime


    def _deserialize(self, params):
        self._TotalQuota = params.get("TotalQuota")
        self._UsedQuota = params.get("UsedQuota")
        self._QuotaStartTime = params.get("QuotaStartTime")
        self._QuotaEndTime = params.get("QuotaEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockRecordsRequest(AbstractModel):
    r"""DescribeDDoSBlockRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: <p>查询的起始时间。最高支持近一年的数据查询。</p><p>参数格式：2026-02-04T11:30:00+08:00。</p>
        :type StartTime: str
        :param _EndTime: <p>查询的结束时间。查询时间范围（EndTime - StartTime）需小于等于 31 天。</p><p>参数格式：2026-03-04T11:30:00+08:00。</p>
        :type EndTime: str
        :param _Filters: <p>过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 appid 下所有被封堵过的资源列表。详细的过滤条件如下：</p><ul><li> Resource：可按照被封堵的 IP 或者被封堵的资源六段式进行过滤；</li><li> Status：可按照被封堵的资源状态进行过滤。</li></ul><p>当 Filters.Name 取值为 Status 时，Filters.Values 取值有：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :type Filters: list of Filter
        :param _Limit: <p>分页查询限制数，最大值为 100。</p><p>默认值：20</p>
        :type Limit: int
        :param _Offset: <p>分页查询偏移量。</p><p>默认值：0</p>
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        r"""<p>查询的起始时间。最高支持近一年的数据查询。</p><p>参数格式：2026-02-04T11:30:00+08:00。</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>查询的结束时间。查询时间范围（EndTime - StartTime）需小于等于 31 天。</p><p>参数格式：2026-03-04T11:30:00+08:00。</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 appid 下所有被封堵过的资源列表。详细的过滤条件如下：</p><ul><li> Resource：可按照被封堵的 IP 或者被封堵的资源六段式进行过滤；</li><li> Status：可按照被封堵的资源状态进行过滤。</li></ul><p>当 Filters.Name 取值为 Status 时，Filters.Values 取值有：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""<p>分页查询限制数，最大值为 100。</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>分页查询偏移量。</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockRecordsResponse(AbstractModel):
    r"""DescribeDDoSBlockRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>封堵解封记录总数。</p>
        :type TotalCount: int
        :param _BlockRecords: <p>封堵解封记录。</p>
        :type BlockRecords: list of DDoSBlockRecord
        :param _UnblockQuotaInfo: <p>解封次数配额信息。</p>
        :type UnblockQuotaInfo: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlockRecords = None
        self._UnblockQuotaInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>封堵解封记录总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlockRecords(self):
        r"""<p>封堵解封记录。</p>
        :rtype: list of DDoSBlockRecord
        """
        return self._BlockRecords

    @BlockRecords.setter
    def BlockRecords(self, BlockRecords):
        self._BlockRecords = BlockRecords

    @property
    def UnblockQuotaInfo(self):
        r"""<p>解封次数配额信息。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        """
        return self._UnblockQuotaInfo

    @UnblockQuotaInfo.setter
    def UnblockQuotaInfo(self, UnblockQuotaInfo):
        self._UnblockQuotaInfo = UnblockQuotaInfo

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
        self._TotalCount = params.get("TotalCount")
        if params.get("BlockRecords") is not None:
            self._BlockRecords = []
            for item in params.get("BlockRecords"):
                obj = DDoSBlockRecord()
                obj._deserialize(item)
                self._BlockRecords.append(obj)
        if params.get("UnblockQuotaInfo") is not None:
            self._UnblockQuotaInfo = DDoSUnblockQuota()
            self._UnblockQuotaInfo._deserialize(params.get("UnblockQuotaInfo"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤 ID、名称、状态等。 若存在多个 Filter 时，Filter 间的关系为逻辑与（AND）关系。 若同一个 Filter 存在多个 Values，同一 Filter 下 Values 间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: <p>需要过滤的字段；具体可选择值请查看对应的引用接口。</p>
        :type Name: str
        :param _Values: <p>字段的过滤值。</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>需要过滤的字段；具体可选择值请查看对应的引用接口。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>字段的过滤值。</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesRequest(AbstractModel):
    r"""UnblockResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: <p>申请解封的资源列表。支持按照公网 IP 解封；可通过 DescribeDDoSBlockRecords 接口获取被封堵的资源详情。参数示例如下：</p><ul><li>公网 IP：117.175.94.230。</li></ul><p>入参限制：列表长度最大限制 10。</p>
        :type Resources: list of str
        """
        self._Resources = None

    @property
    def Resources(self):
        r"""<p>申请解封的资源列表。支持按照公网 IP 解封；可通过 DescribeDDoSBlockRecords 接口获取被封堵的资源详情。参数示例如下：</p><ul><li>公网 IP：117.175.94.230。</li></ul><p>入参限制：列表长度最大限制 10。</p>
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesResponse(AbstractModel):
    r"""UnblockResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")