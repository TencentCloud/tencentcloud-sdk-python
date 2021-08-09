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


class DescribeSdkAppidRequest(AbstractModel):
    """DescribeSdkAppid请求参数结构体

    """


class DescribeSdkAppidResponse(AbstractModel):
    """DescribeSdkAppid返回参数结构体

    """

    def __init__(self):
        """
        :param SdkAppids: 表示 appid 对应的 SdkAppid 的数据\n        :type SdkAppids: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SdkAppids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppids = params.get("SdkAppids")
        self.RequestId = params.get("RequestId")