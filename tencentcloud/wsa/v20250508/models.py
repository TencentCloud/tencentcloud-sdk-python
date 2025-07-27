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


class SearchProRequest(AbstractModel):
    """SearchPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 搜索词
        :type Query: str
        :param _Mode: 返回结果类型，0-自然检索结果(默认)，1-垂类VR结果，2-混合结果（垂类VR结果+自然检索结果）
        :type Mode: int
        :param _Site: 指定域名站内搜索（用于过滤自然检索结果）  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :type Site: str
        :param _FromTime: 起始时间（用于过滤自然检索结果），精确到秒时间戳格式  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :type FromTime: int
        :param _ToTime: 结束时间（用于过滤自然检索结果），精确到秒时间戳格式  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :type ToTime: int
        """
        self._Query = None
        self._Mode = None
        self._Site = None
        self._FromTime = None
        self._ToTime = None

    @property
    def Query(self):
        """搜索词
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Mode(self):
        """返回结果类型，0-自然检索结果(默认)，1-垂类VR结果，2-混合结果（垂类VR结果+自然检索结果）
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Site(self):
        """指定域名站内搜索（用于过滤自然检索结果）  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def FromTime(self):
        """起始时间（用于过滤自然检索结果），精确到秒时间戳格式  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :rtype: int
        """
        return self._FromTime

    @FromTime.setter
    def FromTime(self, FromTime):
        self._FromTime = FromTime

    @property
    def ToTime(self):
        """结束时间（用于过滤自然检索结果），精确到秒时间戳格式  注意：  mode=1模式下，参数无效 mode=0模式下对所有结果生效 mode=2模式下对输出的自然结果生效
        :rtype: int
        """
        return self._ToTime

    @ToTime.setter
    def ToTime(self, ToTime):
        self._ToTime = ToTime


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Mode = params.get("Mode")
        self._Site = params.get("Site")
        self._FromTime = params.get("FromTime")
        self._ToTime = params.get("ToTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchProResponse(AbstractModel):
    """SearchPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 原始查询语
        :type Query: str
        :param _Pages: 搜索结果页面
        :type Pages: list of str
        :param _Msg: 提示信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Query = None
        self._Pages = None
        self._Msg = None
        self._RequestId = None

    @property
    def Query(self):
        """原始查询语
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Pages(self):
        """搜索结果页面
        :rtype: list of str
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Msg(self):
        """提示信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Pages = params.get("Pages")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")