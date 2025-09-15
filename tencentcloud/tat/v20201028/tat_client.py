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
from tencentcloud.tat.v20201028 import models


class TatClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'tat.tencentcloudapi.com'
    _service = 'tat'


    def CancelInvocation(self, request):
        r"""取消一台或多台实例执行的命令

        * 如果命令还未下发到agent，任务状态处于PENDING、DELIVERING、DELIVER_DELAYED，取消后任务状态是CANCELLED
        * 如果命令已下发到agent，任务状态处于RUNNING， 取消后任务状态是TERMINATED

        :param request: Request instance for CancelInvocation.
        :type request: :class:`tencentcloud.tat.v20201028.models.CancelInvocationRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CancelInvocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelInvocation", params, headers=headers)
            response = json.loads(body)
            model = models.CancelInvocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCommand(self, request):
        r"""此接口用于创建命令。

        :param request: Request instance for CreateCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommand", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInvoker(self, request):
        r"""此接口用于创建执行器。

        :param request: Request instance for CreateInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInvoker", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInvokerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRegisterCode(self, request):
        r"""接口用于创建注册码。

        :param request: Request instance for CreateRegisterCode.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateRegisterCodeRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateRegisterCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRegisterCode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRegisterCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCommand(self, request):
        r"""此接口用于删除命令。
        如果命令与执行器关联，则无法被删除。

        :param request: Request instance for DeleteCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCommands(self, request):
        r"""批量删除命令接口

        :param request: Request instance for DeleteCommands.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteCommandsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCommands", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCommandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInvoker(self, request):
        r"""此接口用于删除执行器。

        :param request: Request instance for DeleteInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInvoker", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInvokerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRegisterCodes(self, request):
        r"""此接口用于批量删除注册码。

        :param request: Request instance for DeleteRegisterCodes.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteRegisterCodesRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteRegisterCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRegisterCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRegisterCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRegisterInstance(self, request):
        r"""接口用于删除托管实例。

        :param request: Request instance for DeleteRegisterInstance.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteRegisterInstanceRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteRegisterInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRegisterInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRegisterInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutomationAgentStatus(self, request):
        r"""此接口用于查询自动化助手客户端的状态。

        :param request: Request instance for DescribeAutomationAgentStatus.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutomationAgentStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutomationAgentStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCommands(self, request):
        r"""此接口用于查询命令详情。

        :param request: Request instance for DescribeCommands.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommands", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCommandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationTasks(self, request):
        r"""此接口用于查询执行任务详情。

        :param request: Request instance for DescribeInvocationTasks.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocations(self, request):
        r"""此接口用于查询执行活动详情。

        :param request: Request instance for DescribeInvocations.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvokerRecords(self, request):
        r"""此接口用于查询执行器的执行记录。

        :param request: Request instance for DescribeInvokerRecords.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvokerRecordsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvokerRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvokerRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvokerRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvokers(self, request):
        r"""此接口用于查询执行器信息。

        :param request: Request instance for DescribeInvokers.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvokersRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvokersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvokers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvokersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotas(self, request):
        r"""此接口用于获取配额信息

        :param request: Request instance for DescribeQuotas.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeQuotasRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        r"""此接口用于查询 TAT 产品后台地域列表。
        RegionState 为 AVAILABLE，代表该地域的 TAT 后台服务已经可用；未返回，代表该地域的 TAT 后台服务尚不可用。

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegisterCodes(self, request):
        r"""接口用于查询注册码信息。

        :param request: Request instance for DescribeRegisterCodes.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeRegisterCodesRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeRegisterCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegisterCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegisterCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegisterInstances(self, request):
        r"""接口用于查询被托管的实例信息。

        :param request: Request instance for DescribeRegisterInstances.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeRegisterInstancesRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeRegisterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegisterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegisterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenes(self, request):
        r"""此接口用于查询场景详情。

        :param request: Request instance for DescribeScenes.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeScenesRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableInvoker(self, request):
        r"""此接口用于停止执行器。

        :param request: Request instance for DisableInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.DisableInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DisableInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableInvoker", params, headers=headers)
            response = json.loads(body)
            model = models.DisableInvokerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRegisterCodes(self, request):
        r"""此接口用于批量禁用注册码。

        :param request: Request instance for DisableRegisterCodes.
        :type request: :class:`tencentcloud.tat.v20201028.models.DisableRegisterCodesRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DisableRegisterCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRegisterCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRegisterCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableInvoker(self, request):
        r"""此接口用于启用执行器。

        :param request: Request instance for EnableInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.EnableInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.EnableInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableInvoker", params, headers=headers)
            response = json.loads(body)
            model = models.EnableInvokerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeCommand(self, request):
        r"""在指定的实例上触发命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

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
            headers = request.headers
            body = self.call("InvokeCommand", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCommand(self, request):
        r"""此接口用于修改命令。

        :param request: Request instance for ModifyCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCommand", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInvoker(self, request):
        r"""此接口用于修改执行器。

        :param request: Request instance for ModifyInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInvoker", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInvokerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRegisterInstance(self, request):
        r"""接口用于修改托管实例信息。

        :param request: Request instance for ModifyRegisterInstance.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyRegisterInstanceRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyRegisterInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRegisterInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRegisterInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewReplacedCommandContent(self, request):
        r"""此接口用于预览自定义参数替换后的命令内容。不会触发真实执行。

        :param request: Request instance for PreviewReplacedCommandContent.
        :type request: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewReplacedCommandContent", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewReplacedCommandContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunCommand(self, request):
        r"""执行命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

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
            headers = request.headers
            body = self.call("RunCommand", params, headers=headers)
            response = json.loads(body)
            model = models.RunCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))