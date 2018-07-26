# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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
from tencentcloud.scf.v20180416 import models


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.tencentcloudapi.com'


    def CreateFunction(self, request):
        """该接口根据传入参数创建新的函数。

        :param request: 调用CreateFunction所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTrigger(self, request):
        """该接口根据参数输入设置新的触发方式。

        :param request: 调用CreateTrigger所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFunction(self, request):
        """该接口根据传入参数删除函数。

        :param request: 调用DeleteFunction所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTrigger(self, request):
        """该接口根据参数传入删除已有的触发方式。

        :param request: 调用DeleteTrigger所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetFunction(self, request):
        """该接口获取某个函数的详细信息，包括名称、代码、处理方法、关联触发器和超时时间等字段。

        :param request: 调用GetFunction所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetFunctionLogs(self, request):
        """该接口根据设置的日志查询条件返回函数日志。

        :param request: 调用GetFunctionLogs所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Invoke(self, request):
        """该接口用于运行函数。

        :param request: 调用Invoke所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Invoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListFunctions(self, request):
        """该接口根据传入的查询参数返回相关函数信息。

        :param request: 调用ListFunctions所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListFunctionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListFunctions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListFunctionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateFunctionCode(self, request):
        """该接口根据传入参数更新函数代码。

        :param request: 调用UpdateFunctionCode所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateFunctionConfiguration(self, request):
        """该接口根据传入参数更新函数配置。

        :param request: 调用UpdateFunctionConfiguration所需参数的结构体。
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)