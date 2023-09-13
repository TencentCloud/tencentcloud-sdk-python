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
from tencentcloud.weilingwith.v20230427 import models


class WeilingwithClient(AbstractClient):
    _apiVersion = '2023-04-27'
    _endpoint = 'weilingwith.tencentcloudapi.com'
    _service = 'weilingwith'


    def DescribeApplicationList(self, request):
        """查询指定空间关联的应用列表

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeApplicationToken(self, request):
        """查询边缘应用凭证

        :param request: Request instance for DescribeEdgeApplicationToken.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEdgeApplicationTokenRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEdgeApplicationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeApplicationToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeApplicationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInterfaceList(self, request):
        """查询接口列表

        :param request: Request instance for DescribeInterfaceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeInterfaceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeInterfaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInterfaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInterfaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceList(self, request):
        """获取租户下的空间列表

        :param request: Request instance for DescribeWorkspaceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceUserList(self, request):
        """查询项目空间人员列表

        :param request: Request instance for DescribeWorkspaceUserList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceUserListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))