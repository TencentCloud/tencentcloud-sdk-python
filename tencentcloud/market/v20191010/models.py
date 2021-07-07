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


class FlowProductRemindRequest(AbstractModel):
    """FlowProductRemind请求参数结构体

    """

    def __init__(self):
        """
        :param ProviderUin: 服务商uin
        :type ProviderUin: str
        :param SignId: 服务商实例ID
        :type SignId: str
        :param ResourceId: 云市场实例ID
        :type ResourceId: str
        :param TotalFlow: 实例总流量
        :type TotalFlow: str
        :param LeftFlow: 剩余流量
        :type LeftFlow: str
        :param FlowUnit: 流量单位
        :type FlowUnit: str
        """
        self.ProviderUin = None
        self.SignId = None
        self.ResourceId = None
        self.TotalFlow = None
        self.LeftFlow = None
        self.FlowUnit = None


    def _deserialize(self, params):
        self.ProviderUin = params.get("ProviderUin")
        self.SignId = params.get("SignId")
        self.ResourceId = params.get("ResourceId")
        self.TotalFlow = params.get("TotalFlow")
        self.LeftFlow = params.get("LeftFlow")
        self.FlowUnit = params.get("FlowUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowProductRemindResponse(AbstractModel):
    """FlowProductRemind返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 是否成功
        :type Success: str
        :param FlowId: 流水号
        :type FlowId: str
        :param Info: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.FlowId = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Success = params.get("Success")
        self.FlowId = params.get("FlowId")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class GetUsagePlanUsageAmountRequest(AbstractModel):
    """GetUsagePlanUsageAmount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 用于查询实例的Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUsagePlanUsageAmountResponse(AbstractModel):
    """GetUsagePlanUsageAmount返回参数结构体

    """

    def __init__(self):
        """
        :param MaxRequestNum: 最大调用量
        :type MaxRequestNum: int
        :param InUseRequestNum: 已经调用量
        :type InUseRequestNum: int
        :param RemainingRequestNum: 剩余调用量
        :type RemainingRequestNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxRequestNum = None
        self.InUseRequestNum = None
        self.RemainingRequestNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.RemainingRequestNum = params.get("RemainingRequestNum")
        self.RequestId = params.get("RequestId")