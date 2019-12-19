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


    def CreateJob(self, request):
        """创建任务

        :param request: Request instance for CreateJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateJobResponse()
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


    def CreateRuntime(self, request):
        """创建运行环境

        :param request: Request instance for CreateRuntime.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateRuntimeRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateRuntimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRuntime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuntimeResponse()
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


    def CreateService(self, request):
        """创建服务

        :param request: Request instance for CreateService.
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

        :param request: Request instance for CreateServiceConfig.
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


    def DeleteJob(self, request):
        """删除任务

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteJobResponse()
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


    def DeleteRuntime(self, request):
        """删除运行环境

        :param request: Request instance for DeleteRuntime.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteRuntimeRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteRuntimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRuntime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuntimeResponse()
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

        :param request: Request instance for DeleteService.
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

        :param request: Request instance for DeleteServiceConfig.
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


    def DescribeInstances(self, request):
        """获取节点列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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

        :param request: Request instance for DescribeRuntimes.
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

        :param request: Request instance for DescribeServiceConfigs.
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

        :param request: Request instance for DescribeServices.
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


    def ExposeService(self, request):
        """暴露服务

        :param request: Request instance for ExposeService.
        :type request: :class:`tencentcloud.tiems.v20190416.models.ExposeServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ExposeServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExposeService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExposeServiceResponse()
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


    def UpdateJob(self, request):
        """更新任务

        :param request: Request instance for UpdateJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.UpdateJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.UpdateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateJobResponse()
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

        :param request: Request instance for UpdateService.
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