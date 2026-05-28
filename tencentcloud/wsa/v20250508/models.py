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
    r"""SearchPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: <p>搜索词</p>
        :type Query: str
        :param _Mode: <p>返回结果类型，0-自然检索结果(默认)，1-多模态VR结果，2-混合结果（多模态VR结果+自然检索结果）</p>
        :type Mode: int
        :param _Site: <p>指定域名站内搜索（用于过滤自然检索结果）<br>注意： mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :type Site: str
        :param _FromTime: <p>起始时间（用于过滤自然检索结果），精确到秒时间戳格式<br>注意： mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :type FromTime: int
        :param _ToTime: <p>结束时间（用于过滤自然检索结果），精确到秒时间戳格式<br>注意：mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :type ToTime: int
        :param _Cnt: <p>cnt=10/20/30/40/50，最多可支持返回50条搜索结果，<strong>仅限尊享版使用</strong></p>
        :type Cnt: int
        :param _Industry: <p>Industry=gov/news/acad/finance，对应党政机关、权威媒体、学术（英文）、金融，<strong>仅限尊享版使用</strong></p>
        :type Industry: str
        """
        self._Query = None
        self._Mode = None
        self._Site = None
        self._FromTime = None
        self._ToTime = None
        self._Cnt = None
        self._Industry = None

    @property
    def Query(self):
        r"""<p>搜索词</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Mode(self):
        r"""<p>返回结果类型，0-自然检索结果(默认)，1-多模态VR结果，2-混合结果（多模态VR结果+自然检索结果）</p>
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Site(self):
        r"""<p>指定域名站内搜索（用于过滤自然检索结果）<br>注意： mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def FromTime(self):
        r"""<p>起始时间（用于过滤自然检索结果），精确到秒时间戳格式<br>注意： mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :rtype: int
        """
        return self._FromTime

    @FromTime.setter
    def FromTime(self, FromTime):
        self._FromTime = FromTime

    @property
    def ToTime(self):
        r"""<p>结束时间（用于过滤自然检索结果），精确到秒时间戳格式<br>注意：mode=1模式下，参数无效；mode=0模式下，对所有结果生效；mode=2模式下，对输出的自然结果生效</p>
        :rtype: int
        """
        return self._ToTime

    @ToTime.setter
    def ToTime(self, ToTime):
        self._ToTime = ToTime

    @property
    def Cnt(self):
        r"""<p>cnt=10/20/30/40/50，最多可支持返回50条搜索结果，<strong>仅限尊享版使用</strong></p>
        :rtype: int
        """
        return self._Cnt

    @Cnt.setter
    def Cnt(self, Cnt):
        self._Cnt = Cnt

    @property
    def Industry(self):
        r"""<p>Industry=gov/news/acad/finance，对应党政机关、权威媒体、学术（英文）、金融，<strong>仅限尊享版使用</strong></p>
        :rtype: str
        """
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Mode = params.get("Mode")
        self._Site = params.get("Site")
        self._FromTime = params.get("FromTime")
        self._ToTime = params.get("ToTime")
        self._Cnt = params.get("Cnt")
        self._Industry = params.get("Industry")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchProResponse(AbstractModel):
    r"""SearchPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: <p>原始查询语</p>
        :type Query: str
        :param _Pages: <p>搜索结果页面详情，格式为json字符串。<br>title：结果标题<br>date：内容发布时间<br>url：内容发布源url<br>passage：标准摘要<br>content：动态摘要 （尊享版字段）<br>site：网站名称，部分不知名站点结果可能为空<br>score：相关性得分，取值0～1，越靠近1表示越相关<br>images：图片列表<br>favicon：网站图标链接，部分不知名站点结果可能为空</p>
        :type Pages: list of str
        :param _Version: <p>用户版本：standard/premium/lite/flagship</p>
        :type Version: str
        :param _Msg: <p>提示信息</p>
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Query = None
        self._Pages = None
        self._Version = None
        self._Msg = None
        self._RequestId = None

    @property
    def Query(self):
        r"""<p>原始查询语</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Pages(self):
        r"""<p>搜索结果页面详情，格式为json字符串。<br>title：结果标题<br>date：内容发布时间<br>url：内容发布源url<br>passage：标准摘要<br>content：动态摘要 （尊享版字段）<br>site：网站名称，部分不知名站点结果可能为空<br>score：相关性得分，取值0～1，越靠近1表示越相关<br>images：图片列表<br>favicon：网站图标链接，部分不知名站点结果可能为空</p>
        :rtype: list of str
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Version(self):
        r"""<p>用户版本：standard/premium/lite/flagship</p>
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Msg(self):
        r"""<p>提示信息</p>
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Query = params.get("Query")
        self._Pages = params.get("Pages")
        self._Version = params.get("Version")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")