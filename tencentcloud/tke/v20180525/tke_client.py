# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.tke.v20180525 import models


class TkeClient(AbstractClient):
    _apiVersion = '2018-05-25'
    _endpoint = 'tke.tencentcloudapi.com'


    def AddExistedInstances(self, request):
        """添加已经存在的实例到集群

        :param request: 调用AddExistedInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddExistedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddExistedInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteClusterInstances(self, request):
        """删除集群中的实例

        :param request: 调用DeleteClusterInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterInstances(self, request):
        """查询集群下节点实例信息

        :param request: 调用DescribeClusterInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusters(self, request):
        """查询集群列表

        :param request: 调用DescribeClusters所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)