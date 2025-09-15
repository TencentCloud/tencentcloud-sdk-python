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


class DescribeSdkAppidRequest(AbstractModel):
    r"""DescribeSdkAppid请求参数结构体

    """


class DescribeSdkAppidResponse(AbstractModel):
    r"""DescribeSdkAppid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppids: 表示 appid 对应的 SdkAppid 的数据
        :type SdkAppids: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SdkAppids = None
        self._RequestId = None

    @property
    def SdkAppids(self):
        r"""表示 appid 对应的 SdkAppid 的数据
        :rtype: list of int
        """
        return self._SdkAppids

    @SdkAppids.setter
    def SdkAppids(self, SdkAppids):
        self._SdkAppids = SdkAppids

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppids = params.get("SdkAppids")
        self._RequestId = params.get("RequestId")