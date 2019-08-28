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
from tencentcloud.tiems.v20190416 import models


class TiemsClient(AbstractClient):
    _apiVersion = '2019-04-16'
    _endpoint = 'tiems.tencentcloudapi.com'


    def CreateService(self, request):
        """创建服务

        :param request: 调用CreateService所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceResponse()
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


    def CreateServiceConfig(self, request):
        """创建服务配置

        :param request: 调用CreateServiceConfig所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateServiceConfigRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateServiceConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceConfigResponse()
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


    def DeleteService(self, request):
        """删除服务

        :param request: 调用DeleteService所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceResponse()
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


    def DeleteServiceConfig(self, request):
        """删除服务配置

        :param request: 调用DeleteServiceConfig所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceConfigRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceConfigResponse()
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


    def DescribeRuntimes(self, request):
        """描述服务运行环境

        :param request: 调用DescribeRuntimes所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeRuntimesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeRuntimesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuntimes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuntimesResponse()
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


    def DescribeServiceConfigs(self, request):
        """描述服务配置

        :param request: 调用DescribeServiceConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeServiceConfigsRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeServiceConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceConfigsResponse()
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


    def DescribeServices(self, request):
        """描述服务

        :param request: 调用DescribeServices所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeServicesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeServicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServicesResponse()
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


    def UpdateService(self, request):
        """更新服务

        :param request: 调用UpdateService所需参数的结构体。
        :type request: :class:`tencentcloud.tiems.v20190416.models.UpdateServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.UpdateServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateServiceResponse()
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