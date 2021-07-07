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
from tencentcloud.cat.v20180409 import models


class CatClient(AbstractClient):
    _apiVersion = '2018-04-09'
    _endpoint = 'cat.tencentcloudapi.com'
    _service = 'cat'


    def BindAlarmPolicy(self, request):
        """绑定拨测任务和告警策略组

        :param request: Request instance for BindAlarmPolicy.
        :type request: :class:`tencentcloud.cat.v20180409.models.BindAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.BindAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAlarmPolicyResponse()
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


    def CreateAgentGroup(self, request):
        """添加拨测分组

        :param request: Request instance for CreateAgentGroup.
        :type request: :class:`tencentcloud.cat.v20180409.models.CreateAgentGroupRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.CreateAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAgentGroupResponse()
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


    def CreateTaskEx(self, request):
        """创建拨测任务(扩展)

        :param request: Request instance for CreateTaskEx.
        :type request: :class:`tencentcloud.cat.v20180409.models.CreateTaskExRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.CreateTaskExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskExResponse()
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


    def DeleteAgentGroup(self, request):
        """删除拨测分组

        :param request: Request instance for DeleteAgentGroup.
        :type request: :class:`tencentcloud.cat.v20180409.models.DeleteAgentGroupRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DeleteAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAgentGroupResponse()
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


    def DeleteTasks(self, request):
        """删除多个拨测任务

        :param request: Request instance for DeleteTasks.
        :type request: :class:`tencentcloud.cat.v20180409.models.DeleteTasksRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DeleteTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTasksResponse()
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


    def DescribeAgentGroups(self, request):
        """查询拨测分组列表

        :param request: Request instance for DescribeAgentGroups.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeAgentGroupsRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeAgentGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentGroupsResponse()
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


    def DescribeAgents(self, request):
        """查询本用户可选的拨测点列表

        :param request: Request instance for DescribeAgents.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeAgentsRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeAgentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentsResponse()
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


    def DescribeAlarmTopic(self, request):
        """查询用户的告警主题列表

        :param request: Request instance for DescribeAlarmTopic.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmTopicRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmTopicResponse()
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


    def DescribeAlarms(self, request):
        """查询拨测告警列表

        :param request: Request instance for DescribeAlarms.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmsRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmsResponse()
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


    def DescribeAlarmsByTask(self, request):
        """按任务查询拨测告警列表

        :param request: Request instance for DescribeAlarmsByTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmsByTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeAlarmsByTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmsByTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmsByTaskResponse()
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


    def DescribeCatLogs(self, request):
        """查询拨测流水

        :param request: Request instance for DescribeCatLogs.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeCatLogsRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeCatLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCatLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCatLogsResponse()
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


    def DescribeTaskDetail(self, request):
        """查询拨测任务信息

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasksByType(self, request):
        """按类型查询拨测任务列表

        :param request: Request instance for DescribeTasksByType.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeTasksByTypeRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeTasksByTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasksByType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksByTypeResponse()
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


    def DescribeUserLimit(self, request):
        """获取用户可用资源限制

        :param request: Request instance for DescribeUserLimit.
        :type request: :class:`tencentcloud.cat.v20180409.models.DescribeUserLimitRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.DescribeUserLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserLimitResponse()
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


    def GetAvailRatioHistory(self, request):
        """获取指定时刻的可用率地图信息

        :param request: Request instance for GetAvailRatioHistory.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetAvailRatioHistoryRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetAvailRatioHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAvailRatioHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAvailRatioHistoryResponse()
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


    def GetDailyAvailRatio(self, request):
        """获取一天的整体可用率信息

        :param request: Request instance for GetDailyAvailRatio.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetDailyAvailRatioRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetDailyAvailRatioResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDailyAvailRatio", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDailyAvailRatioResponse()
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


    def GetRealAvailRatio(self, request):
        """获取实时可用率信息

        :param request: Request instance for GetRealAvailRatio.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetRealAvailRatioRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetRealAvailRatioResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRealAvailRatio", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRealAvailRatioResponse()
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


    def GetRespTimeTrendEx(self, request):
        """查询拨测任务的走势数据

        :param request: Request instance for GetRespTimeTrendEx.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetRespTimeTrendExRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetRespTimeTrendExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRespTimeTrendEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRespTimeTrendExResponse()
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


    def GetResultSummary(self, request):
        """获取任务列表的实时数据

        :param request: Request instance for GetResultSummary.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetResultSummaryRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetResultSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetResultSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetResultSummaryResponse()
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


    def GetReturnCodeHistory(self, request):
        """查询拨测任务的历史返回码信息

        :param request: Request instance for GetReturnCodeHistory.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetReturnCodeHistoryRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetReturnCodeHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetReturnCodeHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetReturnCodeHistoryResponse()
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


    def GetReturnCodeInfo(self, request):
        """查询拨测任务的返回码统计信息

        :param request: Request instance for GetReturnCodeInfo.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetReturnCodeInfoRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetReturnCodeInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetReturnCodeInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetReturnCodeInfoResponse()
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


    def GetTaskTotalNumber(self, request):
        """获取AppId下的拨测任务总数

        :param request: Request instance for GetTaskTotalNumber.
        :type request: :class:`tencentcloud.cat.v20180409.models.GetTaskTotalNumberRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.GetTaskTotalNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTaskTotalNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTaskTotalNumberResponse()
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


    def ModifyAgentGroup(self, request):
        """修改拨测分组

        :param request: Request instance for ModifyAgentGroup.
        :type request: :class:`tencentcloud.cat.v20180409.models.ModifyAgentGroupRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.ModifyAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAgentGroupResponse()
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


    def ModifyTaskEx(self, request):
        """修改拨测任务(扩展)

        :param request: Request instance for ModifyTaskEx.
        :type request: :class:`tencentcloud.cat.v20180409.models.ModifyTaskExRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.ModifyTaskExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTaskEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskExResponse()
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


    def PauseTask(self, request):
        """暂停拨测任务

        :param request: Request instance for PauseTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.PauseTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.PauseTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PauseTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PauseTaskResponse()
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


    def RunTask(self, request):
        """运行拨测任务

        :param request: Request instance for RunTask.
        :type request: :class:`tencentcloud.cat.v20180409.models.RunTaskRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.RunTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunTaskResponse()
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


    def VerifyResult(self, request):
        """验证拨测任务，结果验证查询（验证成功的，才建议创建拨测任务）

        :param request: Request instance for VerifyResult.
        :type request: :class:`tencentcloud.cat.v20180409.models.VerifyResultRequest`
        :rtype: :class:`tencentcloud.cat.v20180409.models.VerifyResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyResultResponse()
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