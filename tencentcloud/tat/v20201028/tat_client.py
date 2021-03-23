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
from tencentcloud.tat.v20201028 import models


class TatClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'tat.tencentcloudapi.com'
    _service = 'tat'


    def CreateCommand(self, request):
        """此接口用于创建命令。

        :param request: Request instance for CreateCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateCommandResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCommand", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCommandResponse()
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


    def DeleteCommand(self, request):
        """此接口用于删除命令。

        :param request: Request instance for DeleteCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteCommandResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCommand", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCommandResponse()
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


    def DescribeAutomationAgentStatus(self, request):
        """此接口用于查询自动化助手客户端的状态。

        :param request: Request instance for DescribeAutomationAgentStatus.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutomationAgentStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutomationAgentStatusResponse()
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


    def DescribeCommands(self, request):
        """此接口用于查询命令详情。

        :param request: Request instance for DescribeCommands.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCommands", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCommandsResponse()
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


    def DescribeInvocationTasks(self, request):
        """此接口用于查询执行任务详情。

        :param request: Request instance for DescribeInvocationTasks.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInvocationTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvocationTasksResponse()
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


    def DescribeInvocations(self, request):
        """此接口用于查询执行活动详情。

        :param request: Request instance for DescribeInvocations.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInvocations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvocationsResponse()
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


    def DescribeRegions(self, request):
        """此接口用于查询地域列表

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def InvokeCommand(self, request):
        """在指定的实例上触发命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

        * 如果指定实例未安装 agent，或 agent 不在线，返回失败
        * 如果命令类型与 agent 运行环境不符，返回失败
        * 指定的实例需要处于 VPC 网络
        * 指定的实例需要处于 RUNNING 状态
        * 不可同时指定 CVM 和 Lighthouse

        :param request: Request instance for InvokeCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.InvokeCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.InvokeCommandResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InvokeCommand", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeCommandResponse()
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


    def ModifyCommand(self, request):
        """此接口用于修改命令。

        :param request: Request instance for ModifyCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyCommandResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCommand", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCommandResponse()
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


    def PreviewReplacedCommandContent(self, request):
        """此接口用于预览自定义参数替换后的命令内容。不会触发真实执行。

        :param request: Request instance for PreviewReplacedCommandContent.
        :type request: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PreviewReplacedCommandContent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PreviewReplacedCommandContentResponse()
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


    def RunCommand(self, request):
        """执行命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

        * 如果指定实例未安装 agent，或 agent 不在线，返回失败
        * 如果命令类型与 agent 运行环境不符，返回失败
        * 指定的实例需要处于 VPC 网络
        * 指定的实例需要处于 `RUNNING` 状态
        * 不可同时指定 CVM 和 Lighthouse

        :param request: Request instance for RunCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.RunCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.RunCommandResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunCommand", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunCommandResponse()
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