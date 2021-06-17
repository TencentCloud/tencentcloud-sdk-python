# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class GetCateTreeRequest(AbstractModel):
    """GetCateTree请求参数结构体

    """

    def __init__(self):
        """
        :param CateId: 分类ID
        :type CateId: int
        """
        self.CateId = None


    def _deserialize(self, params):
        self.CateId = params.get("CateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetCateTreeResponse(AbstractModel):
    """GetCateTree返回参数结构体

    """

    def __init__(self):
        """
        :param CateId: 分类ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateId: int
        :param Name: 分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CateId = None
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CateId = params.get("CateId")
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        