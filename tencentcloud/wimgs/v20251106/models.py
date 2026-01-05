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


class SearchByTextRequest(AbstractModel):
    r"""SearchByText请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 查询词
        :type Query: str
        """
        self._Query = None

    @property
    def Query(self):
        r"""查询词
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchByTextResponse(AbstractModel):
    r"""SearchByText返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 原始查询词
        :type Query: str
        :param _Images: 搜索结果图片列表，格式为json字符串。

- thumbnailUrl：缩略图地址。
- thumbnailWidth：缩略图宽度。
- thumbnailHeight：缩略图高度。
- origPicUrl：原图地址。
-  origPicWidth：原图宽度。
- siteUrl：站点地址，原图来源网页URL。
- siteName：站点名称。
- title：标题，原图标题或原图来源网页标题。
- date：内容发布时间。
        :type Images: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Query = None
        self._Images = None
        self._RequestId = None

    @property
    def Query(self):
        r"""原始查询词
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Images(self):
        r"""搜索结果图片列表，格式为json字符串。

- thumbnailUrl：缩略图地址。
- thumbnailWidth：缩略图宽度。
- thumbnailHeight：缩略图高度。
- origPicUrl：原图地址。
-  origPicWidth：原图宽度。
- siteUrl：站点地址，原图来源网页URL。
- siteName：站点名称。
- title：标题，原图标题或原图来源网页标题。
- date：内容发布时间。
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

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
        self._Images = params.get("Images")
        self._RequestId = params.get("RequestId")