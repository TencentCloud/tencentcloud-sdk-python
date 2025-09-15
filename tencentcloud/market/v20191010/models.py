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


class FlowProductRemindRequest(AbstractModel):
    r"""FlowProductRemind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderUin: 服务商uin
        :type ProviderUin: str
        :param _SignId: 服务商实例ID
        :type SignId: str
        :param _ResourceId: 云市场实例ID
        :type ResourceId: str
        :param _TotalFlow: 实例总流量
        :type TotalFlow: str
        :param _LeftFlow: 剩余流量
        :type LeftFlow: str
        :param _FlowUnit: 流量单位
        :type FlowUnit: str
        """
        self._ProviderUin = None
        self._SignId = None
        self._ResourceId = None
        self._TotalFlow = None
        self._LeftFlow = None
        self._FlowUnit = None

    @property
    def ProviderUin(self):
        r"""服务商uin
        :rtype: str
        """
        return self._ProviderUin

    @ProviderUin.setter
    def ProviderUin(self, ProviderUin):
        self._ProviderUin = ProviderUin

    @property
    def SignId(self):
        r"""服务商实例ID
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def ResourceId(self):
        r"""云市场实例ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TotalFlow(self):
        r"""实例总流量
        :rtype: str
        """
        return self._TotalFlow

    @TotalFlow.setter
    def TotalFlow(self, TotalFlow):
        self._TotalFlow = TotalFlow

    @property
    def LeftFlow(self):
        r"""剩余流量
        :rtype: str
        """
        return self._LeftFlow

    @LeftFlow.setter
    def LeftFlow(self, LeftFlow):
        self._LeftFlow = LeftFlow

    @property
    def FlowUnit(self):
        r"""流量单位
        :rtype: str
        """
        return self._FlowUnit

    @FlowUnit.setter
    def FlowUnit(self, FlowUnit):
        self._FlowUnit = FlowUnit


    def _deserialize(self, params):
        self._ProviderUin = params.get("ProviderUin")
        self._SignId = params.get("SignId")
        self._ResourceId = params.get("ResourceId")
        self._TotalFlow = params.get("TotalFlow")
        self._LeftFlow = params.get("LeftFlow")
        self._FlowUnit = params.get("FlowUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowProductRemindResponse(AbstractModel):
    r"""FlowProductRemind返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 是否成功
        :type Success: str
        :param _FlowId: 流水号
        :type FlowId: str
        :param _Info: 消息
        :type Info: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._FlowId = None
        self._Info = None
        self._RequestId = None

    @property
    def Success(self):
        r"""是否成功
        :rtype: str
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def FlowId(self):
        r"""流水号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Info(self):
        r"""消息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Success = params.get("Success")
        self._FlowId = params.get("FlowId")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class GetUsagePlanUsageAmountRequest(AbstractModel):
    r"""GetUsagePlanUsageAmount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 用于查询实例的Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""用于查询实例的Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUsagePlanUsageAmountResponse(AbstractModel):
    r"""GetUsagePlanUsageAmount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxRequestNum: 最大调用量
        :type MaxRequestNum: int
        :param _InUseRequestNum: 已经调用量
        :type InUseRequestNum: int
        :param _RemainingRequestNum: 剩余调用量
        :type RemainingRequestNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaxRequestNum = None
        self._InUseRequestNum = None
        self._RemainingRequestNum = None
        self._RequestId = None

    @property
    def MaxRequestNum(self):
        r"""最大调用量
        :rtype: int
        """
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def InUseRequestNum(self):
        r"""已经调用量
        :rtype: int
        """
        return self._InUseRequestNum

    @InUseRequestNum.setter
    def InUseRequestNum(self, InUseRequestNum):
        self._InUseRequestNum = InUseRequestNum

    @property
    def RemainingRequestNum(self):
        r"""剩余调用量
        :rtype: int
        """
        return self._RemainingRequestNum

    @RemainingRequestNum.setter
    def RemainingRequestNum(self, RemainingRequestNum):
        self._RemainingRequestNum = RemainingRequestNum

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
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._InUseRequestNum = params.get("InUseRequestNum")
        self._RemainingRequestNum = params.get("RemainingRequestNum")
        self._RequestId = params.get("RequestId")