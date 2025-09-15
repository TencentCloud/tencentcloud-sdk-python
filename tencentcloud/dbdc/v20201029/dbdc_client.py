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
from tencentcloud.dbdc.v20201029 import models


class DbdcClient(AbstractClient):
    _apiVersion = '2020-10-29'
    _endpoint = 'dbdc.tencentcloudapi.com'
    _service = 'dbdc'


    def DescribeDBInstances(self, request):
        r"""本接口用于查询独享集群内的DB实例列表

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostList(self, request):
        r"""本接口用于查询主机列表

        :param request: Request instance for DescribeHostList.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeHostListRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetail(self, request):
        r"""本接口用于查询独享集群详情

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""本接口用于查询独享集群实例列表

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""根据不同地域不同用户，获取集群列表信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceName(self, request):
        r"""本接口用于修改集群名称

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.dbdc.v20201029.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))