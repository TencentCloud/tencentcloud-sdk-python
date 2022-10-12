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
from tencentcloud.tse.v20201207 import models


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.tencentcloudapi.com'
    _service = 'tse'


    def CreateEngine(self, request):
        """创建引擎实例

        :param request: Request instance for CreateEngine.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateEngineRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEngine", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEngineResponse()
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


    def DeleteEngine(self, request):
        """删除引擎实例

        :param request: Request instance for DeleteEngine.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteEngineRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEngine", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEngineResponse()
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


    def DescribeCloudNativeAPIGatewayNodes(self, request):
        """获取云原生网关节点列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayNodes.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayNodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudNativeAPIGatewayNodesResponse()
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


    def DescribeNacosReplicas(self, request):
        """查询Nacos类型引擎实例副本信息

        :param request: Request instance for DescribeNacosReplicas.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNacosReplicasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNacosReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNacosReplicas", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNacosReplicasResponse()
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


    def DescribeNacosServerInterfaces(self, request):
        """查询nacos服务接口列表

        :param request: Request instance for DescribeNacosServerInterfaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNacosServerInterfacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNacosServerInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNacosServerInterfaces", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNacosServerInterfacesResponse()
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


    def DescribeSREInstanceAccessAddress(self, request):
        """查询引擎实例访问地址

        :param request: Request instance for DescribeSREInstanceAccessAddress.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstanceAccessAddressRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstanceAccessAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSREInstanceAccessAddress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSREInstanceAccessAddressResponse()
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


    def DescribeSREInstances(self, request):
        """用于查询引擎实例列表

        :param request: Request instance for DescribeSREInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSREInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSREInstancesResponse()
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


    def DescribeZookeeperReplicas(self, request):
        """查询Zookeeper类型注册引擎实例副本信息

        :param request: Request instance for DescribeZookeeperReplicas.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperReplicasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZookeeperReplicas", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZookeeperReplicasResponse()
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


    def DescribeZookeeperServerInterfaces(self, request):
        """查询zookeeper服务接口列表

        :param request: Request instance for DescribeZookeeperServerInterfaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperServerInterfacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperServerInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZookeeperServerInterfaces", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZookeeperServerInterfacesResponse()
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


    def UpdateEngineInternetAccess(self, request):
        """修改引擎公网访问配置

        :param request: Request instance for UpdateEngineInternetAccess.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateEngineInternetAccessRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateEngineInternetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEngineInternetAccess", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEngineInternetAccessResponse()
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