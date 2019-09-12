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


    def CreateCluster(self, request):
        """创建集群

        :param request: 调用CreateCluster所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateClusterAsGroup(self, request):
        """为已经存在的集群创建伸缩组

        :param request: 调用CreateClusterAsGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterAsGroupRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterAsGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterAsGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterAsGroupResponse()
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


    def CreateClusterInstances(self, request):
        """扩展(新建)集群节点

        :param request: 调用CreateClusterInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterInstancesResponse()
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


    def CreateClusterRoute(self, request):
        """创建集群路由

        :param request: 调用CreateClusterRoute所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterRouteResponse()
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


    def CreateClusterRouteTable(self, request):
        """创建集群路由表

        :param request: 调用CreateClusterRouteTable所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterRouteTableResponse()
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


    def DeleteCluster(self, request):
        """删除集群(YUNAPI V3版本)

        :param request: 调用DeleteCluster所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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


    def DeleteClusterAsGroups(self, request):
        """删除集群伸缩组

        :param request: 调用DeleteClusterAsGroups所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterAsGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterAsGroupsResponse()
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


    def DeleteClusterRoute(self, request):
        """删除集群路由

        :param request: 调用DeleteClusterRoute所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterRouteResponse()
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


    def DeleteClusterRouteTable(self, request):
        """删除集群路由表

        :param request: 调用DeleteClusterRouteTable所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterRouteTableResponse()
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


    def DescribeClusterRouteTables(self, request):
        """查询集群路由表

        :param request: 调用DescribeClusterRouteTables所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterRouteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterRouteTablesResponse()
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


    def DescribeClusterRoutes(self, request):
        """查询集群路由

        :param request: 调用DescribeClusterRoutes所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterRoutesResponse()
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


    def DescribeClusterSecurity(self, request):
        """集群的密钥信息

        :param request: 调用DescribeClusterSecurity所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterSecurity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterSecurityResponse()
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


    def DescribeExistedInstances(self, request):
        """查询已经存在的节点，判断是否可以加入集群

        :param request: 调用DescribeExistedInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeExistedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExistedInstancesResponse()
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


    def DescribeRouteTableConflicts(self, request):
        """查询路由表冲突列表

        :param request: 调用DescribeRouteTableConflicts所需参数的结构体。
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteTableConflicts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteTableConflictsResponse()
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