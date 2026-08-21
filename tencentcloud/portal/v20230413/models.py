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


class SearchDocumentItem(AbstractModel):
    r"""搜索文档结果

    """

    def __init__(self):
        r"""
        :param _Url: <p>文档URL</p>
        :type Url: str
        :param _Title: <p>文档标题</p>
        :type Title: str
        :param _ProductName: <p>产品名称</p>
        :type ProductName: str
        :param _Snippet: <p>文档片段</p>
        :type Snippet: str
        """
        self._Url = None
        self._Title = None
        self._ProductName = None
        self._Snippet = None

    @property
    def Url(self):
        r"""<p>文档URL</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Title(self):
        r"""<p>文档标题</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ProductName(self):
        r"""<p>产品名称</p>
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Snippet(self):
        r"""<p>文档片段</p>
        :rtype: str
        """
        return self._Snippet

    @Snippet.setter
    def Snippet(self, Snippet):
        self._Snippet = Snippet


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Title = params.get("Title")
        self._ProductName = params.get("ProductName")
        self._Snippet = params.get("Snippet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDocumentsRequest(AbstractModel):
    r"""SearchDocuments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: <p>搜索关键词</p>
        :type Query: str
        :param _Page: <p>页码</p><p>取值范围：[1, 99]</p>
        :type Page: int
        :param _PageSize: <p>每页条数</p><p>取值范围：[1, 20]</p>
        :type PageSize: int
        :param _ProductName: <p>产品名称</p>
        :type ProductName: str
        """
        self._Query = None
        self._Page = None
        self._PageSize = None
        self._ProductName = None

    @property
    def Query(self):
        r"""<p>搜索关键词</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Page(self):
        r"""<p>页码</p><p>取值范围：[1, 99]</p>
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""<p>每页条数</p><p>取值范围：[1, 20]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProductName(self):
        r"""<p>产品名称</p>
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDocumentsResponse(AbstractModel):
    r"""SearchDocuments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: <p>总数</p>
        :type Total: int
        :param _Documents: <p>文档列表</p>
        :type Documents: list of SearchDocumentItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Documents = None
        self._RequestId = None

    @property
    def Total(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        r"""<p>文档列表</p>
        :rtype: list of SearchDocumentItem
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

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
        self._Total = params.get("Total")
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = SearchDocumentItem()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")