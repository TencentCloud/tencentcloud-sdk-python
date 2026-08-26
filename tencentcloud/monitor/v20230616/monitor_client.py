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
from tencentcloud.monitor.v20230616 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'


    def CancelAIWorkbenchChat(self, request):
        r"""取消对话执行

        :param request: Request instance for CancelAIWorkbenchChat.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CancelAIWorkbenchChatRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CancelAIWorkbenchChatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAIWorkbenchChat", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAIWorkbenchChatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIWorkbenchAgent(self, request):
        r"""创建 Agent

        :param request: Request instance for CreateAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIWorkbenchTask(self, request):
        r"""创建任务

        :param request: Request instance for CreateAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CreateAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNoticeContentTmpl(self, request):
        r"""创建自定义通知内容模板

        :param request: Request instance for CreateNoticeContentTmpl.
        :type request: :class:`tencentcloud.monitor.v20230616.models.CreateNoticeContentTmplRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.CreateNoticeContentTmplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNoticeContentTmpl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNoticeContentTmplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIWorkbenchAgent(self, request):
        r"""删除 Agent

        :param request: Request instance for DeleteAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIWorkbenchTask(self, request):
        r"""删除任务

        :param request: Request instance for DeleteAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DeleteAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNoticeContentTmpls(self, request):
        r"""删除通知内容模板

        :param request: Request instance for DeleteNoticeContentTmpls.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DeleteNoticeContentTmplsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DeleteNoticeContentTmplsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNoticeContentTmpls", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNoticeContentTmplsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchAgent(self, request):
        r"""查询 Agent 详情

        :param request: Request instance for DescribeAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchArtifact(self, request):
        r"""查询制品详情

        :param request: Request instance for DescribeAIWorkbenchArtifact.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchArtifactRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchArtifactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchArtifact", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchArtifactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchExecution(self, request):
        r"""查询执行详情

        :param request: Request instance for DescribeAIWorkbenchExecution.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchExecutionRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchExecution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSREDigitalTwinTaskList(self, request):
        r"""查询AI工作台SRE数字分身任务列表

        :param request: Request instance for DescribeAIWorkbenchSREDigitalTwinTaskList.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinTaskListRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSREDigitalTwinTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSREDigitalTwinWorkLogDetail(self, request):
        r"""查询AI工作台SRE数字分身工作日志详细信息

        :param request: Request instance for DescribeAIWorkbenchSREDigitalTwinWorkLogDetail.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSREDigitalTwinWorkLogDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSREDigitalTwinWorkLogList(self, request):
        r"""查询AI工作台SRE数字分身任务工作日志列表

        :param request: Request instance for DescribeAIWorkbenchSREDigitalTwinWorkLogList.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinWorkLogListRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSREDigitalTwinWorkLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSession(self, request):
        r"""查询会话详情

        :param request: Request instance for DescribeAIWorkbenchSession.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSessionRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIWorkbenchSkill(self, request):
        r"""查询技能详情

        :param request: Request instance for DescribeAIWorkbenchSkill.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSkillRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAIWorkbenchSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIWorkbenchSkill", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIWorkbenchSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmNotifyHistories(self, request):
        r"""按需查询告警的通知历史

        :param request: Request instance for DescribeAlarmNotifyHistories.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeAlarmNotifyHistoriesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeAlarmNotifyHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotifyHistories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNotifyHistoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNoticeContentTmpl(self, request):
        r"""根据查询条件获取自定义通知内容模板，若所有查询条件空，则获取账号下所有模板

        :param request: Request instance for DescribeNoticeContentTmpl.
        :type request: :class:`tencentcloud.monitor.v20230616.models.DescribeNoticeContentTmplRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DescribeNoticeContentTmplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNoticeContentTmpl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNoticeContentTmplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAIWorkbenchArtifactDownloadURL(self, request):
        r"""获取AI工作台制品的下载地址

        :param request: Request instance for GetAIWorkbenchArtifactDownloadURL.
        :type request: :class:`tencentcloud.monitor.v20230616.models.GetAIWorkbenchArtifactDownloadURLRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.GetAIWorkbenchArtifactDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAIWorkbenchArtifactDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.GetAIWorkbenchArtifactDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchAgents(self, request):
        r"""查询 Agent 列表

        :param request: Request instance for ListAIWorkbenchAgents.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchAgentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchAgents", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchAgentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchArtifacts(self, request):
        r"""查询产物列表

        :param request: Request instance for ListAIWorkbenchArtifacts.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchArtifactsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchArtifactsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchArtifacts", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchArtifactsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchExecutions(self, request):
        r"""查询执行列表

        :param request: Request instance for ListAIWorkbenchExecutions.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchExecutionsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchMCPs(self, request):
        r"""查询 MCP 列表

        :param request: Request instance for ListAIWorkbenchMCPs.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMCPsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMCPsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchMCPs", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchMCPsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchMessages(self, request):
        r"""查询消息列表

        :param request: Request instance for ListAIWorkbenchMessages.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMessagesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchMessages", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchResourceInstances(self, request):
        r"""列出资源实例

        :param request: Request instance for ListAIWorkbenchResourceInstances.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchResourceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchResourceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchResourceMaps(self, request):
        r"""查询资源地图列表

        :param request: Request instance for ListAIWorkbenchResourceMaps.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceMapsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchResourceMapsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchResourceMaps", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchResourceMapsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchSessions(self, request):
        r"""查询会话列表

        :param request: Request instance for ListAIWorkbenchSessions.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSessionsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchSessions", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchSkills(self, request):
        r"""查询技能列表

        :param request: Request instance for ListAIWorkbenchSkills.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSkillsRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchSkillsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchSkills", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchSkillsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAIWorkbenchTasks(self, request):
        r"""查询任务列表

        :param request: Request instance for ListAIWorkbenchTasks.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchTasksRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ListAIWorkbenchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAIWorkbenchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListAIWorkbenchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNoticeContentTmpl(self, request):
        r"""修改通知内容模板

        :param request: Request instance for ModifyNoticeContentTmpl.
        :type request: :class:`tencentcloud.monitor.v20230616.models.ModifyNoticeContentTmplRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.ModifyNoticeContentTmplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNoticeContentTmpl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNoticeContentTmplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerAIWorkbenchSREDigitalTwinTask(self, request):
        r"""触发数字分身任务请求

        :param request: Request instance for TriggerAIWorkbenchSREDigitalTwinTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchSREDigitalTwinTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchSREDigitalTwinTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerAIWorkbenchSREDigitalTwinTask", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerAIWorkbenchSREDigitalTwinTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerAIWorkbenchTask(self, request):
        r"""手动触发任务

        :param request: Request instance for TriggerAIWorkbenchTask.
        :type request: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchTaskRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TriggerAIWorkbenchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerAIWorkbenchTask", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerAIWorkbenchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAIWorkbenchAgent(self, request):
        r"""更新 Agent

        :param request: Request instance for UpdateAIWorkbenchAgent.
        :type request: :class:`tencentcloud.monitor.v20230616.models.UpdateAIWorkbenchAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20230616.models.UpdateAIWorkbenchAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIWorkbenchAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIWorkbenchAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))