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
from tencentcloud.yunjing.v20180228 import models


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.tencentcloudapi.com'
    _service = 'yunjing'


    def AddLoginWhiteList(self, request):
        r"""本接口（AddLoginWhiteList）用于添加白名单规则

        :param request: Request instance for AddLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.AddLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddMachineTag(self, request):
        r"""增加机器关联标签

        :param request: Request instance for AddMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.AddMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseProVersion(self, request):
        r"""本接口 (CloseProVersion) 用于关闭专业版。

        :param request: Request instance for CloseProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineStrategy(self, request):
        r"""根据策略信息创建基线策略

        :param request: Request instance for CreateBaselineStrategy.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOpenPortTask(self, request):
        r"""本接口 (CreateOpenPortTask) 用于创建实时获取端口任务。

        :param request: Request instance for CreateOpenPortTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenPortTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenPortTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProcessTask(self, request):
        r"""本接口 (CreateProcessTask) 用于创建实时拉取进程任务。

        :param request: Request instance for CreateProcessTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcessTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcessTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUsualLoginPlaces(self, request):
        r"""此接口（CreateUsualLoginPlaces）用于添加常用登录地。

        :param request: Request instance for CreateUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAttackLogs(self, request):
        r"""删除网络攻击日志

        :param request: Request instance for DeleteAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashEvents(self, request):
        r"""根据Ids删除高危命令事件

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashRules(self, request):
        r"""删除高危命令规则

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBruteAttacks(self, request):
        r"""本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginWhiteList(self, request):
        r"""删除白名单规则

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachine(self, request):
        r"""本接口（DeleteMachine）用于卸载云镜客户端。

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineTag(self, request):
        r"""删除服务器关联的标签

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequests(self, request):
        r"""本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwares(self, request):
        r"""本接口 (DeleteMalwares) 用于删除木马记录。

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNonlocalLoginPlaces(self, request):
        r"""本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeEvents(self, request):
        r"""根据Ids删除本地提权

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeRules(self, request):
        r"""删除本地提权规则

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellEvents(self, request):
        r"""根据Ids删除反弹Shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellRules(self, request):
        r"""删除反弹Shell规则

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTags(self, request):
        r"""删除标签

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsualLoginPlaces(self, request):
        r"""本接口（DeleteUsualLoginPlaces）用于删除常用登录地。

        :param request: Request instance for DeleteUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountStatistics(self, request):
        r"""本接口 (DescribeAccountStatistics) 用于获取帐号统计列表数据。

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        r"""本接口 (DescribeAccounts) 用于获取帐号列表数据。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentVuls(self, request):
        r"""本接口 (DescribeAgentVuls) 用于获取单台主机的漏洞列表。

        :param request: Request instance for DescribeAgentVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmAttribute(self, request):
        r"""本接口 (DescribeAlarmAttribute) 用于获取告警设置。

        :param request: Request instance for DescribeAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackLogInfo(self, request):
        r"""网络攻击日志详情

        :param request: Request instance for DescribeAttackLogInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackLogInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackLogInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackLogs(self, request):
        r"""按分页形式展示网络攻击日志列表

        :param request: Request instance for DescribeAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEvents(self, request):
        r"""获取高危命令列表

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashRules(self, request):
        r"""获取高危命令规则列表

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttacks(self, request):
        r"""本接口{DescribeBruteAttacks}用于获取暴力破解事件列表。

        :param request: Request instance for DescribeBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComponentInfo(self, request):
        r"""本接口 (DescribeComponentInfo) 用于获取组件信息数据。

        :param request: Request instance for DescribeComponentInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComponentStatistics(self, request):
        r"""本接口 (DescribeComponentStatistics) 用于获取组件统计列表数据。

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComponents(self, request):
        r"""本接口 (DescribeComponents) 用于获取组件列表数据。

        :param request: Request instance for DescribeComponents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryAccounts(self, request):
        r"""本接口 (DescribeHistoryAccounts) 用于获取帐号变更历史列表数据。

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImpactedHosts(self, request):
        r"""本接口 (DescribeImpactedHosts) 用于获取漏洞受影响机器列表。

        :param request: Request instance for DescribeImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteList(self, request):
        r"""获取异地登录白名单列表

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineInfo(self, request):
        r"""本接口（DescribeMachineInfo）用于获取机器详细信息。

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        r"""本接口 (DescribeMachines) 用于获取区域主机列表。

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaliciousRequests(self, request):
        r"""本接口 (DescribeMaliciousRequests) 用于获取恶意请求数据。

        :param request: Request instance for DescribeMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwares(self, request):
        r"""本接口（DescribeMalwares）用于获取木马事件列表。

        :param request: Request instance for DescribeMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNonlocalLoginPlaces(self, request):
        r"""本接口(DescribeNonlocalLoginPlaces)用于获取异地登录事件。

        :param request: Request instance for DescribeNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPortStatistics(self, request):
        r"""本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPortTaskStatus(self, request):
        r"""本接口 (DescribeOpenPortTaskStatus) 用于获取实时拉取端口任务状态。

        :param request: Request instance for DescribeOpenPortTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPorts(self, request):
        r"""本接口 (DescribeOpenPorts) 用于获取端口列表数据。

        :param request: Request instance for DescribeOpenPorts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewStatistics(self, request):
        r"""本接口用于（DescribeOverviewStatistics）获取概览统计数据。

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEvents(self, request):
        r"""获取本地提权事件列表

        :param request: Request instance for DescribePrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeRules(self, request):
        r"""获取本地提权规则列表

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionInfo(self, request):
        r"""本接口 (DescribeProVersionInfo) 用于获取专业版信息。

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessStatistics(self, request):
        r"""本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessTaskStatus(self, request):
        r"""本接口 (DescribeProcessTaskStatus) 用于获取实时拉取进程任务状态。

        :param request: Request instance for DescribeProcessTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcesses(self, request):
        r"""本接口 (DescribeProcesses) 用于获取进程列表数据。

        :param request: Request instance for DescribeProcesses.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcesses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEvents(self, request):
        r"""获取反弹Shell列表

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellRules(self, request):
        r"""获取反弹Shell规则列表

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityDynamics(self, request):
        r"""本接口 (DescribeSecurityDynamics) 用于获取安全事件消息数据。

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityDynamics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityDynamicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTrends(self, request):
        r"""本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagMachines(self, request):
        r"""获取指定标签关联的服务器信息

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        r"""获取所有主机标签

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsualLoginPlaces(self, request):
        r"""此接口（DescribeUsualLoginPlaces）用于查询常用登录地。

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulInfo(self, request):
        r"""本接口 (DescribeVulInfo) 用于获取漏洞详情。

        :param request: Request instance for DescribeVulInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanResult(self, request):
        r"""本接口 (DescribeVulScanResult) 用于获取漏洞检测结果。

        :param request: Request instance for DescribeVulScanResult.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVuls(self, request):
        r"""本接口 (DescribeVuls) 用于获取漏洞列表数据。

        :param request: Request instance for DescribeVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReportBruteAttacks(self, request):
        r"""本接口 (DescribeWeeklyReportBruteAttacks) 用于获取专业周报密码破解数据。

        :param request: Request instance for DescribeWeeklyReportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReportInfo(self, request):
        r"""本接口 (DescribeWeeklyReportInfo) 用于获取专业周报详情数据。

        :param request: Request instance for DescribeWeeklyReportInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReportMalwares(self, request):
        r"""本接口 (DescribeWeeklyReportMalwares) 用于获取专业周报木马数据。

        :param request: Request instance for DescribeWeeklyReportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReportNonlocalLoginPlaces(self, request):
        r"""本接口 (DescribeWeeklyReportNonlocalLoginPlaces) 用于获取专业周报异地登录数据。

        :param request: Request instance for DescribeWeeklyReportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReportVuls(self, request):
        r"""本接口 (DescribeWeeklyReportVuls) 用于专业版周报漏洞数据。

        :param request: Request instance for DescribeWeeklyReportVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReportVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeeklyReports(self, request):
        r"""本接口 (DescribeWeeklyReports) 用于获取周报列表数据。

        :param request: Request instance for DescribeWeeklyReports.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeeklyReports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeeklyReportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditBashRule(self, request):
        r"""新增或修改高危命令规则

        :param request: Request instance for EditBashRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditBashRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditBashRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditBashRule", params, headers=headers)
            response = json.loads(body)
            model = models.EditBashRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditPrivilegeRule(self, request):
        r"""新增或修改本地提权规则

        :param request: Request instance for EditPrivilegeRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditPrivilegeRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditPrivilegeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditPrivilegeRule", params, headers=headers)
            response = json.loads(body)
            model = models.EditPrivilegeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditReverseShellRule(self, request):
        r"""编辑反弹Shell规则

        :param request: Request instance for EditReverseShellRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditReverseShellRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditReverseShellRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditReverseShellRule", params, headers=headers)
            response = json.loads(body)
            model = models.EditReverseShellRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditTags(self, request):
        r"""新增或编辑标签

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditTags", params, headers=headers)
            response = json.loads(body)
            model = models.EditTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttackLogs(self, request):
        r"""导出网络攻击日志

        :param request: Request instance for ExportAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEvents(self, request):
        r"""导出高危命令事件

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBruteAttacks(self, request):
        r"""本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMaliciousRequests(self, request):
        r"""本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMalwares(self, request):
        r"""本接口 (ExportMalwares) 用于导出木马记录CSV文件。

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportNonlocalLoginPlaces(self, request):
        r"""本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.ExportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportPrivilegeEvents(self, request):
        r"""导出本地提权事件

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportPrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportPrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportReverseShellEvents(self, request):
        r"""导出反弹Shell事件

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreImpactedHosts(self, request):
        r"""本接口 (IgnoreImpactedHosts) 用于忽略漏洞。

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceOpenProVersionPrepaid(self, request):
        r"""本接口 (InquiryPriceOpenProVersionPrepaid) 用于开通专业版询价(预付费)。

        :param request: Request instance for InquiryPriceOpenProVersionPrepaid.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceOpenProVersionPrepaid", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceOpenProVersionPrepaidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MisAlarmNonlocalLoginPlaces(self, request):
        r"""本接口{MisAlarmNonlocalLoginPlaces}将设置当前地点为常用登录地。

        :param request: Request instance for MisAlarmNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MisAlarmNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.MisAlarmNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmAttribute(self, request):
        r"""本接口（ModifyAlarmAttribute）用于修改告警设置。

        :param request: Request instance for ModifyAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoOpenProVersionConfig(self, request):
        r"""本接口 (ModifyAutoOpenProVersionConfig) 用于设置新增主机自动开通专业版配置。

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoOpenProVersionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoOpenProVersionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteList(self, request):
        r"""编辑白名单规则

        :param request: Request instance for ModifyLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProVersionRenewFlag(self, request):
        r"""本接口 (ModifyProVersionRenewFlag) 用于修改专业版包年包月续费标识。

        :param request: Request instance for ModifyProVersionRenewFlag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProVersionRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProVersionRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenProVersion(self, request):
        r"""本接口 (OpenProVersion) 用于开通专业版。

        :param request: Request instance for OpenProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenProVersion", params, headers=headers)
            response = json.loads(body)
            model = models.OpenProVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenProVersionPrepaid(self, request):
        r"""本接口 (OpenProVersionPrepaid) 用于开通专业版(包年包月)。

        :param request: Request instance for OpenProVersionPrepaid.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenProVersionPrepaid", params, headers=headers)
            response = json.loads(body)
            model = models.OpenProVersionPrepaidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMalwares(self, request):
        r"""本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewProVersion(self, request):
        r"""本接口 (RenewProVersion) 用于续费专业版(包年包月)。

        :param request: Request instance for RenewProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RenewProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RenewProVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewProVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RenewProVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RescanImpactedHost(self, request):
        r"""本接口 (RescanImpactedHost) 用于漏洞重新检测。

        :param request: Request instance for RescanImpactedHost.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RescanImpactedHost", params, headers=headers)
            response = json.loads(body)
            model = models.RescanImpactedHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SeparateMalwares(self, request):
        r"""本接口（SeparateMalwares）用于隔离木马。

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SeparateMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.SeparateMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBashEventsStatus(self, request):
        r"""设置高危命令事件状态

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBashEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetBashEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchBashRules(self, request):
        r"""切换高危命令规则状态

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrustMaliciousRequest(self, request):
        r"""本接口 (TrustMaliciousRequest) 用于恶意请求添加信任。

        :param request: Request instance for TrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMaliciousRequest", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMaliciousRequestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrustMalwares(self, request):
        r"""本接口(TrustMalwares)将被识别木马文件设为信任。

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UntrustMaliciousRequest(self, request):
        r"""本接口 (UntrustMaliciousRequest) 用于取消信任恶意请求。

        :param request: Request instance for UntrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMaliciousRequest", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMaliciousRequestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UntrustMalwares(self, request):
        r"""本接口（UntrustMalwares）用于取消信任木马文件。

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))