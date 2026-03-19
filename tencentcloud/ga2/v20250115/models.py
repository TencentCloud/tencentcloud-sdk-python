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