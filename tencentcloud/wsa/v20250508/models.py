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
        :param _Mode: <p>返回结果类型，不传默认为0。（<strong>仅标准版、尊享版支持该参数</strong>）</p><p>枚举值：</p><ul><li>0： 公开网页信源结果（自然结果）</li><li>1： 优质权威垂直信源结果（VR 卡）</li><li>2： 混合结果（自然结果+VR卡）</li></ul>
        :type Mode: int
        :param _Site: <p>指定网址搜索/过滤。（<strong>仅标准版、尊享版、旗舰版支持该参数</strong>）</p><ul><li>指定网址搜索：需要查询某个特定网址的内容时，传入&quot;Site=qq.com&quot;，实现只搜索qq.com的结果；每次搜索仅支持指定一个域名。</li><li>指定网址过滤：需要排除某个特定网址的内容时，传入&quot;Site=exclude:qq.com|sohu.com&quot;，实现过滤qq.com和sohu.com的结果；每次搜索最多支持过滤五个域名。</li></ul><p>注意： 该参数与mode参数共同使用时，仅对公开网页信源结果（自然结果）生效，对优质权威垂直信源结果（VR卡）不生效。</p>
        :type Site: str
        :param _Cnt: <p>控制返回结果条数，可取值：cnt=10/20/30/40/50。（<strong>仅尊享版、旗舰版支持该参数</strong>）</p><p>枚举值：</p><ul><li>10： 返回10条结果</li><li>20： 返回20条结果</li><li>30： 返回30条结果</li><li>40： 返回40条结果</li><li>50： 返回50条结果</li></ul>
        :type Cnt: int
        :param _Industry: <p>垂直领域搜索。（<strong>仅尊享版、旗舰版支持该参数</strong>）</p><p>枚举值：</p><ul><li>gov： 政府</li><li>news： 新闻</li><li>acad： 学术</li><li>finance： 财经</li></ul>
        :type Industry: str
        :param _Freshness: <p>搜索时效范围（<strong>仅标准版、尊享版、旗舰版支持该参数</strong>）</p><ul><li><p>d[N]：最近N天，N取值1-30整数。</p></li><li><p>m[N]：最近N月，N取值1-12整数。</p></li><li><p>y[N]：最近N年，N取值1-5整数。</p></li></ul><p>示例说明：</p><ul><li><p>d1/m1/y1：当天/当月/当年。<br>例如，2026.6.15分别传参d1/m1/y1进行搜索，则搜索结果的时间范围分别为“2026.6.15”/“2026.6”/“2026”，以此类推。</p></li><li><p>d/m/y：N值为空时，默认N=1，即等效入参d1/m1/y1。</p></li><li><p>未传参时，默认不生效。</p></li><li><p>d、m、y不支持组合使用。</p></li></ul><p>枚举值：</p><ul><li>d7： 最近七天</li><li>m3： 最近三月</li><li>y2： 最近两年</li><li>d： 当天</li><li>m： 当月</li><li>y： 当年</li></ul>
        :type Freshness: str
        :param _Deeplinks: <p>返回附件子链信息（<strong>仅旗舰版支持该参数</strong>）</p><p>附件子链信息包括&quot;子链标题&quot;和&quot;子链URL&quot;，单个doc最多返回10条子链信息。</p><ul><li>true：返回</li><li>false：不返回</li><li>未传参时默认不返回</li></ul>
        :type Deeplinks: bool
        """
        self._Query = None
        self._Mode = None
        self._Site = None
        self._Cnt = None
        self._Industry = None
        self._Freshness = None
        self._Deeplinks = None

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
        r"""<p>返回结果类型，不传默认为0。（<strong>仅标准版、尊享版支持该参数</strong>）</p><p>枚举值：</p><ul><li>0： 公开网页信源结果（自然结果）</li><li>1： 优质权威垂直信源结果（VR 卡）</li><li>2： 混合结果（自然结果+VR卡）</li></ul>
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Site(self):
        r"""<p>指定网址搜索/过滤。（<strong>仅标准版、尊享版、旗舰版支持该参数</strong>）</p><ul><li>指定网址搜索：需要查询某个特定网址的内容时，传入&quot;Site=qq.com&quot;，实现只搜索qq.com的结果；每次搜索仅支持指定一个域名。</li><li>指定网址过滤：需要排除某个特定网址的内容时，传入&quot;Site=exclude:qq.com|sohu.com&quot;，实现过滤qq.com和sohu.com的结果；每次搜索最多支持过滤五个域名。</li></ul><p>注意： 该参数与mode参数共同使用时，仅对公开网页信源结果（自然结果）生效，对优质权威垂直信源结果（VR卡）不生效。</p>
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def Cnt(self):
        r"""<p>控制返回结果条数，可取值：cnt=10/20/30/40/50。（<strong>仅尊享版、旗舰版支持该参数</strong>）</p><p>枚举值：</p><ul><li>10： 返回10条结果</li><li>20： 返回20条结果</li><li>30： 返回30条结果</li><li>40： 返回40条结果</li><li>50： 返回50条结果</li></ul>
        :rtype: int
        """
        return self._Cnt

    @Cnt.setter
    def Cnt(self, Cnt):
        self._Cnt = Cnt

    @property
    def Industry(self):
        r"""<p>垂直领域搜索。（<strong>仅尊享版、旗舰版支持该参数</strong>）</p><p>枚举值：</p><ul><li>gov： 政府</li><li>news： 新闻</li><li>acad： 学术</li><li>finance： 财经</li></ul>
        :rtype: str
        """
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def Freshness(self):
        r"""<p>搜索时效范围（<strong>仅标准版、尊享版、旗舰版支持该参数</strong>）</p><ul><li><p>d[N]：最近N天，N取值1-30整数。</p></li><li><p>m[N]：最近N月，N取值1-12整数。</p></li><li><p>y[N]：最近N年，N取值1-5整数。</p></li></ul><p>示例说明：</p><ul><li><p>d1/m1/y1：当天/当月/当年。<br>例如，2026.6.15分别传参d1/m1/y1进行搜索，则搜索结果的时间范围分别为“2026.6.15”/“2026.6”/“2026”，以此类推。</p></li><li><p>d/m/y：N值为空时，默认N=1，即等效入参d1/m1/y1。</p></li><li><p>未传参时，默认不生效。</p></li><li><p>d、m、y不支持组合使用。</p></li></ul><p>枚举值：</p><ul><li>d7： 最近七天</li><li>m3： 最近三月</li><li>y2： 最近两年</li><li>d： 当天</li><li>m： 当月</li><li>y： 当年</li></ul>
        :rtype: str
        """
        return self._Freshness

    @Freshness.setter
    def Freshness(self, Freshness):
        self._Freshness = Freshness

    @property
    def Deeplinks(self):
        r"""<p>返回附件子链信息（<strong>仅旗舰版支持该参数</strong>）</p><p>附件子链信息包括&quot;子链标题&quot;和&quot;子链URL&quot;，单个doc最多返回10条子链信息。</p><ul><li>true：返回</li><li>false：不返回</li><li>未传参时默认不返回</li></ul>
        :rtype: bool
        """
        return self._Deeplinks

    @Deeplinks.setter
    def Deeplinks(self, Deeplinks):
        self._Deeplinks = Deeplinks


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Mode = params.get("Mode")
        self._Site = params.get("Site")
        self._Cnt = params.get("Cnt")
        self._Industry = params.get("Industry")
        self._Freshness = params.get("Freshness")
        self._Deeplinks = params.get("Deeplinks")
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
        :param _Pages: <p>搜索结果页面详情，格式为json字符串。</p><ul><li><p>title：结果标题</p></li><li><p>date：内容发布时间</p></li><li><p>url：内容发布源url</p></li><li><p>passage：标准摘要</p></li><li><p>content：动态摘要（<strong>仅尊享版、旗舰版返回该字段</strong>）</p></li><li><p>site：网站名称，部分不知名站点结果可能为空</p></li><li><p>score：相关性得分，取值0～1，越靠近1表示越相关</p></li><li><p>authority_level：权威度得分，取值0～5，数值越大表示越权威（<strong>仅旗舰版返回该字段</strong>）</p></li><li><p>pics：图片列表，单个doc返回0～10条（<strong>仅标准版、尊享版、旗舰版返回该字段</strong>）</p><ul><li>caption：图片描述</li><li>origin_url：源图url地</li></ul></li><li><p>favicon：网站图标链接，部分不知名站点结果可能为空</p></li><li><p>deeplinks：附件子链信息，单个doc最多返回10条子链信息。（<strong>仅旗舰版返回该字段，通过Deeplinks入参控制</strong>）</p><ul><li>title：子链标题</li><li>url：子链地址</li></ul></li></ul>
        :type Pages: list of str
        :param _Version: <p>用户版本：standard/premium/lite/flagship（标准/尊享/轻量/旗舰）</p>
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
        r"""<p>搜索结果页面详情，格式为json字符串。</p><ul><li><p>title：结果标题</p></li><li><p>date：内容发布时间</p></li><li><p>url：内容发布源url</p></li><li><p>passage：标准摘要</p></li><li><p>content：动态摘要（<strong>仅尊享版、旗舰版返回该字段</strong>）</p></li><li><p>site：网站名称，部分不知名站点结果可能为空</p></li><li><p>score：相关性得分，取值0～1，越靠近1表示越相关</p></li><li><p>authority_level：权威度得分，取值0～5，数值越大表示越权威（<strong>仅旗舰版返回该字段</strong>）</p></li><li><p>pics：图片列表，单个doc返回0～10条（<strong>仅标准版、尊享版、旗舰版返回该字段</strong>）</p><ul><li>caption：图片描述</li><li>origin_url：源图url地</li></ul></li><li><p>favicon：网站图标链接，部分不知名站点结果可能为空</p></li><li><p>deeplinks：附件子链信息，单个doc最多返回10条子链信息。（<strong>仅旗舰版返回该字段，通过Deeplinks入参控制</strong>）</p><ul><li>title：子链标题</li><li>url：子链地址</li></ul></li></ul>
        :rtype: list of str
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Version(self):
        r"""<p>用户版本：standard/premium/lite/flagship（标准/尊享/轻量/旗舰）</p>
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