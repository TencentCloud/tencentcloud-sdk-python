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
from tencentcloud.tdai.v20250717 import models


class TdaiClient(AbstractClient):
    _apiVersion = '2025-07-17'
    _endpoint = 'tdai.tencentcloudapi.com'
    _service = 'tdai'


    def ContinueAgentWork(self, request):
        r"""本接口（ContinueAgentWork）用于重启智能体实例的值守任务，通常在用户需要重启时使用。

        :param request: Request instance for ContinueAgentWork.
        :type request: :class:`tencentcloud.tdai.v20250717.models.ContinueAgentWorkRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ContinueAgentWorkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueAgentWork", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueAgentWorkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentInstance(self, request):
        r"""本接口（CreateAgentInstance）用于创建一个智能体实例，通常在用户购买一个智能体实例时使用。

        :param request: Request instance for CreateAgentInstance.
        :type request: :class:`tencentcloud.tdai.v20250717.models.CreateAgentInstanceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.CreateAgentInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChatCompletion(self, request):
        r"""用于创建一次会话的SSE接口

        :param request: Request instance for CreateChatCompletion.
        :type request: :class:`tencentcloud.tdai.v20250717.models.CreateChatCompletionRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.CreateChatCompletionResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("CreateChatCompletion", params, models.CreateChatCompletionResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMemoryPlusSpace(self, request):
        r"""本接口（CreateMemoryPlusSpace）用于创建正式版 Memory 实例。

        :param request: Request instance for CreateMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.CreateMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.CreateMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDutyTaskDetail(self, request):
        r"""查询智能体值守任务详情

        :param request: Request instance for DescribeAgentDutyTaskDetail.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentDutyTaskDetailRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentDutyTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDutyTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDutyTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDutyTasks(self, request):
        r"""查询智能体值守任务列表

        :param request: Request instance for DescribeAgentDutyTasks.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentDutyTasksRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentDutyTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDutyTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDutyTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstance(self, request):
        r"""本接口（DescribeAgentInstance）用于查询智能体实例详情，通常在用户查询所购买的所有智能体实例详情时使用。

        :param request: Request instance for DescribeAgentInstance.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentInstanceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstances(self, request):
        r"""本接口（DescribeAgentInstances）用于查询智能体实例列表，通常在用户查询所购买的所有智能体列表。

        :param request: Request instance for DescribeAgentInstances.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentInstancesRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgents(self, request):
        r"""本接口（DescribeAgents）用于查询智能体列表，通常在用户查询所购买的所有智能体列表。

        :param request: Request instance for DescribeAgents.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentsRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChatDetail(self, request):
        r"""本接口（DescribeChatDetail）用于查询对话详情，通常在用户查询会话的历史记录时使用。

        :param request: Request instance for DescribeChatDetail.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeChatDetailRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeChatDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChatDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChatDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChats(self, request):
        r"""本接口（DescribeChats）用于查询对话列表，通常在用户查询会话列表时使用。

        :param request: Request instance for DescribeChats.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeChatsRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeChatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMemoryPlusRecord(self, request):
        r"""本接口（DescribeMemoryPlusRecord）用于查询 Memory 实例的记忆数据。

        :param request: Request instance for DescribeMemoryPlusRecord.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusRecordRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMemoryPlusRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMemoryPlusRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMemoryPlusSpace(self, request):
        r"""本接口（DescribeMemoryPlusSpace）用于查询 Memory 正式版实例详情。

        :param request: Request instance for DescribeMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMemoryPlusSpaces(self, request):
        r"""本接口（DescribeMemoryPlusSpaces）用于查询 Memory正式版实例列表。

        :param request: Request instance for DescribeMemoryPlusSpaces.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusSpacesRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeMemoryPlusSpacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMemoryPlusSpaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMemoryPlusSpacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportUrl(self, request):
        r"""智能体报告地址生成并下载

        :param request: Request instance for DescribeReportUrl.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeReportUrlRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeReportUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceAccessKey(self, request):
        r"""本接口（DescribeServiceAccessKey）用于查询服务访问密钥。

        :param request: Request instance for DescribeServiceAccessKey.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DescribeServiceAccessKeyRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DescribeServiceAccessKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceAccessKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceAccessKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyMemoryPlusSpace(self, request):
        r"""本接口（DestroyMemoryPlusSpace）用于从回收站彻底销毁 Memory 实例。

        :param request: Request instance for DestroyMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.DestroyMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.DestroyMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateAgentInstance(self, request):
        r"""本接口（IsolateAgentInstance）用于隔离智能体实例，通常在用户需要隔离智能体实例时使用。

        :param request: Request instance for IsolateAgentInstance.
        :type request: :class:`tencentcloud.tdai.v20250717.models.IsolateAgentInstanceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.IsolateAgentInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateAgentInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateAgentInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateMemoryPlusSpace(self, request):
        r"""本接口（IsolateMemoryPlusSpace）用于将正式版 Memory 实例放入回收站隔离。

        :param request: Request instance for IsolateMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.IsolateMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.IsolateMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentInstanceParameters(self, request):
        r"""本接口（ModifyAgentInstanceParameters）用于修改智能体实例的参数列表，通常在用户需要配置智能体实例时使用。

        :param request: Request instance for ModifyAgentInstanceParameters.
        :type request: :class:`tencentcloud.tdai.v20250717.models.ModifyAgentInstanceParametersRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ModifyAgentInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentInstanceParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentInstanceParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyChatTitle(self, request):
        r"""本接口（ModifyChatTitle）用于修改会话标题，通常在用户修改会话标题时使用。

        :param request: Request instance for ModifyChatTitle.
        :type request: :class:`tencentcloud.tdai.v20250717.models.ModifyChatTitleRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ModifyChatTitleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyChatTitle", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyChatTitleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMemoryPlusSpace(self, request):
        r"""本接口（ModifyMemoryPlusSpace）用于修改正式版 Memory 实例，可修改实例名称与描述。

        :param request: Request instance for ModifyMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.ModifyMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.ModifyMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseAgentWork(self, request):
        r"""本接口（PauseAgentWork）用于暂停智能体实例的值守任务，通常在用户需要暂停时使用。

        :param request: Request instance for PauseAgentWork.
        :type request: :class:`tencentcloud.tdai.v20250717.models.PauseAgentWorkRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.PauseAgentWorkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseAgentWork", params, headers=headers)
            response = json.loads(body)
            model = models.PauseAgentWorkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverAgentInstance(self, request):
        r"""本接口（RecoverAgentInstance）用于解隔离智能体实例，通常在用户需要解隔离智能体实例时使用。

        :param request: Request instance for RecoverAgentInstance.
        :type request: :class:`tencentcloud.tdai.v20250717.models.RecoverAgentInstanceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.RecoverAgentInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverAgentInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverAgentInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMemoryPlusSpace(self, request):
        r"""本接口（RecoverMemoryPlusSpace）用于从回收站恢复 Memory 实例。

        :param request: Request instance for RecoverMemoryPlusSpace.
        :type request: :class:`tencentcloud.tdai.v20250717.models.RecoverMemoryPlusSpaceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.RecoverMemoryPlusSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMemoryPlusSpace", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMemoryPlusSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveChat(self, request):
        r"""本接口（RemoveChat）用于删除会话，通常在用户删除会话时使用。

        :param request: Request instance for RemoveChat.
        :type request: :class:`tencentcloud.tdai.v20250717.models.RemoveChatRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.RemoveChatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveChat", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveChatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAgentTask(self, request):
        r"""该接口用于启动一个智能体的任务

        :param request: Request instance for StartAgentTask.
        :type request: :class:`tencentcloud.tdai.v20250717.models.StartAgentTaskRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.StartAgentTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAgentTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartAgentTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateAgentInstance(self, request):
        r"""本接口（TerminateAgentInstance）用于下线智能体实例，通常在用户需要下线智能体实例时使用。

        :param request: Request instance for TerminateAgentInstance.
        :type request: :class:`tencentcloud.tdai.v20250717.models.TerminateAgentInstanceRequest`
        :rtype: :class:`tencentcloud.tdai.v20250717.models.TerminateAgentInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateAgentInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateAgentInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))