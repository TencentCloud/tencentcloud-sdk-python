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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.lowcode.v20210108 import models


class LowcodeClient(AbstractClient):
    _apiVersion = '2021-01-08'
    _endpoint = 'lowcode.tencentcloudapi.com'
    _service = 'lowcode'


    def CheckDeployApp(self, request):
        r"""检查应用发布状态

        :param request: Request instance for CheckDeployApp.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.CheckDeployAppRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.CheckDeployAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDeployApp", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDeployAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKnowledgeSet(self, request):
        r"""创建知识库

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


    def DeleteAppBindWxApp(self, request):
        r"""删除应用绑定小程序

        :param request: Request instance for DeleteAppBindWxApp.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DeleteAppBindWxAppRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeleteAppBindWxAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppBindWxApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppBindWxAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKnowledgeDocumentSet(self, request):
        r"""删除知识库下文档

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
        r"""删除知识库

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


    def DeployApp(self, request):
        r"""发布应用

        :param request: Request instance for DeployApp.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DeployAppRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeployAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeployAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApps(self, request):
        r"""分页获取当前用户的应用列表

        :param request: Request instance for DescribeApps.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeAppsRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceList(self, request):
        r"""获取数据源详情列表

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
        r"""获取知识库下文档详情

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
        r"""查询知识库下文件集合

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
        r"""查询知识库

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


    def DescribeRelatedUsers(self, request):
        r"""获取角色关联的用户列表

        :param request: Request instance for DescribeRelatedUsers.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeRelatedUsersRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeRelatedUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelatedUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceRoleList(self, request):
        r"""查询资源关联的角色列表

        :param request: Request instance for DescribeResourceRoleList.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.DescribeResourceRoleListRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeResourceRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutWxAppIdToWeApp(self, request):
        r"""接口提供应用绑定微信ID功能。

        :param request: Request instance for PutWxAppIdToWeApp.
        :type request: :class:`tencentcloud.lowcode.v20210108.models.PutWxAppIdToWeAppRequest`
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.PutWxAppIdToWeAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutWxAppIdToWeApp", params, headers=headers)
            response = json.loads(body)
            model = models.PutWxAppIdToWeAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchDocList(self, request):
        r"""知识库文档搜索接口

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
        r"""更新知识库

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
        r"""更新知识库

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