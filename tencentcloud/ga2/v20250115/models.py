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


class CreateGlobalAcceleratorRequest(AbstractModel):
    r"""CreateGlobalAccelerator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _InstanceChargeType: <p>计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。当前仅支持后付费。</p>
        :type InstanceChargeType: str
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _CrossBorderType: <p>跨境类型；HighQuality：精品BGP-IP跨境；Unicom：联通专线跨境。</p>
        :type CrossBorderType: str
        :param _CrossBorderPromiseFlag: <p>此Flag代表签署跨境服务承诺书。当使用跨境服务时候，此字段必传。True：代表签署。</p>
        :type CrossBorderPromiseFlag: bool
        :param _Tags: <p>标签信息</p>
        :type Tags: list of Tag
        """
        self._Name = None
        self._InstanceChargeType = None
        self._Description = None
        self._CrossBorderType = None
        self._CrossBorderPromiseFlag = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceChargeType(self):
        r"""<p>计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。当前仅支持后付费。</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CrossBorderType(self):
        r"""<p>跨境类型；HighQuality：精品BGP-IP跨境；Unicom：联通专线跨境。</p>
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def CrossBorderPromiseFlag(self):
        r"""<p>此Flag代表签署跨境服务承诺书。当使用跨境服务时候，此字段必传。True：代表签署。</p>
        :rtype: bool
        """
        return self._CrossBorderPromiseFlag

    @CrossBorderPromiseFlag.setter
    def CrossBorderPromiseFlag(self, CrossBorderPromiseFlag):
        self._CrossBorderPromiseFlag = CrossBorderPromiseFlag

    @property
    def Tags(self):
        r"""<p>标签信息</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Description = params.get("Description")
        self._CrossBorderType = params.get("CrossBorderType")
        self._CrossBorderPromiseFlag = params.get("CrossBorderPromiseFlag")
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
        


class CreateGlobalAcceleratorResponse(AbstractModel):
    r"""CreateGlobalAccelerator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID。</p>
        :type TaskId: str
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._GlobalAcceleratorId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

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
        self._TaskId = params.get("TaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._RequestId = params.get("RequestId")


class DescribeCrossBorderSettlementRequest(AbstractModel):
    r"""DescribeCrossBorderSettlement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _AccelerateRegion: 加速地域。
        :type AccelerateRegion: str
        :param _EndpointGroupRegion: 终端节点组地域。
        :type EndpointGroupRegion: str
        :param _SettlementMonth: 账单年月时间。
        :type SettlementMonth: int
        """
        self._GlobalAcceleratorId = None
        self._AccelerateRegion = None
        self._EndpointGroupRegion = None
        self._SettlementMonth = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AccelerateRegion(self):
        r"""加速地域。
        :rtype: str
        """
        return self._AccelerateRegion

    @AccelerateRegion.setter
    def AccelerateRegion(self, AccelerateRegion):
        self._AccelerateRegion = AccelerateRegion

    @property
    def EndpointGroupRegion(self):
        r"""终端节点组地域。
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def SettlementMonth(self):
        r"""账单年月时间。
        :rtype: int
        """
        return self._SettlementMonth

    @SettlementMonth.setter
    def SettlementMonth(self, SettlementMonth):
        self._SettlementMonth = SettlementMonth


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._AccelerateRegion = params.get("AccelerateRegion")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        self._SettlementMonth = params.get("SettlementMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBorderSettlementResponse(AbstractModel):
    r"""DescribeCrossBorderSettlement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Traffic: 流量用量，单位是GB；精度为保留小数点6位。
        :type Traffic: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Traffic = None
        self._RequestId = None

    @property
    def Traffic(self):
        r"""流量用量，单位是GB；精度为保留小数点6位。
        :rtype: float
        """
        return self._Traffic

    @Traffic.setter
    def Traffic(self, Traffic):
        self._Traffic = Traffic

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
        self._Traffic = params.get("Traffic")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        