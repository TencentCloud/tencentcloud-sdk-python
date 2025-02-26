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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.lowcode.v20210108 import models


class LowcodeClient(AbstractClient):
    _apiVersion = '2021-01-08'
    _endpoint = 'lowcode.tencentcloudapi.com'
    _service = 'lowcode'


    def CreateKnowledgeSet(self, request):
        """创建知识库

        :param request: Request instance for CreateKnowledgeSet.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.CreateKnowledgeSetRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.CreateKnowledgeSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKnowledgeSet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKnowledgeSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKnowledgeDocumentSet(self, request):
        """删除知识库下文档

        :param request: Request instance for DeleteKnowledgeDocumentSet.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeDocumentSetRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeDocumentSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKnowledgeDocumentSet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKnowledgeDocumentSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKnowledgeSet(self, request):
        """删除知识库

        :param request: Request instance for DeleteKnowledgeSet.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeSetRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKnowledgeSet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKnowledgeSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceList(self, request):
        """获取数据源详情列表

        :param request: Request instance for DescribeDataSourceList.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeDataSourceListRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeDataSourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeDocumentSetDetail(self, request):
        """获取知识库下文档详情

        :param request: Request instance for DescribeKnowledgeDocumentSetDetail.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetDetailRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeDocumentSetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeDocumentSetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeDocumentSetList(self, request):
        """查询知识库下文件集合

        :param request: Request instance for DescribeKnowledgeDocumentSetList.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetListRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeDocumentSetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeDocumentSetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeSetList(self, request):
        """查询知识库

        :param request: Request instance for DescribeKnowledgeSetList.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeSetListRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeSetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeSetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeSetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchDocList(self, request):
        """知识库文档搜索接口

        :param request: Request instance for SearchDocList.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.SearchDocListRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.SearchDocListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchDocList", params, headers=headers)
            response = json.loads(body)
            model = models.SearchDocListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateKnowledgeSet(self, request):
        """更新知识库

        :param request: Request instance for UpdateKnowledgeSet.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.UpdateKnowledgeSetRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.UpdateKnowledgeSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateKnowledgeSet", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateKnowledgeSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadKnowledgeDocumentSet(self, request):
        """更新知识库

        :param request: Request instance for UploadKnowledgeDocumentSet.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.UploadKnowledgeDocumentSetRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.UploadKnowledgeDocumentSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadKnowledgeDocumentSet", params, headers=headers)
            response = json.loads(body)
            model = models.UploadKnowledgeDocumentSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))