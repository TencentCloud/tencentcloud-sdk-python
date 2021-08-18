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
from tencentcloud.cwp.v20180228 import models


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.tencentcloudapi.com'
    _service = 'cwp'


    def CloseProVersion(self, request):
        """本接口 (CloseProVersion) 用于关闭专业版。

        :param request: Request instance for CloseProVersion.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CloseProVersionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CloseProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseProVersionResponse()
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


    def CreateBaselineStrategy(self, request):
        """根据策略信息创建基线策略

        :param request: Request instance for CreateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBaselineStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBaselineStrategyResponse()
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


    def CreateProtectServer(self, request):
        """添加房展防护服务器

        :param request: Request instance for CreateProtectServer.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProtectServer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProtectServerResponse()
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


    def CreateScanMalwareSetting(self, request):
        """该接口可以对入侵检测-文件查杀扫描检测

        :param request: Request instance for CreateScanMalwareSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScanMalwareSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScanMalwareSettingResponse()
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


    def CreateSearchLog(self, request):
        """添加历史搜索记录

        :param request: Request instance for CreateSearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSearchLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSearchLogResponse()
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


    def CreateSearchTemplate(self, request):
        """添加检索模板

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSearchTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSearchTemplateResponse()
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


    def DeleteAttackLogs(self, request):
        """删除网络攻击日志

        :param request: Request instance for DeleteAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAttackLogsResponse()
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


    def DeleteBashEvents(self, request):
        """根据Ids删除高危命令事件

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBashEventsResponse()
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


    def DeleteBashRules(self, request):
        """删除高危命令规则

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBashRulesResponse()
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


    def DeleteBruteAttacks(self, request):
        """本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBruteAttacksResponse()
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


    def DeleteLoginWhiteList(self, request):
        """本接口用于删除异地登录白名单规则。

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoginWhiteListResponse()
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


    def DeleteMachine(self, request):
        """本接口（DeleteMachine）用于卸载云镜客户端。

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMachineResponse()
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


    def DeleteMachineTag(self, request):
        """删除服务器关联的标签

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMachineTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMachineTagResponse()
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


    def DeleteMaliciousRequests(self, request):
        """本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMaliciousRequests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMaliciousRequestsResponse()
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


    def DeleteMalwares(self, request):
        """本接口 (DeleteMalwares) 用于删除木马记录。

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMalwaresResponse()
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


    def DeleteNonlocalLoginPlaces(self, request):
        """本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNonlocalLoginPlacesResponse()
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


    def DeletePrivilegeEvents(self, request):
        """根据Ids删除本地提权

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivilegeEventsResponse()
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


    def DeletePrivilegeRules(self, request):
        """删除本地提权规则

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivilegeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivilegeRulesResponse()
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


    def DeleteReverseShellEvents(self, request):
        """根据Ids删除反弹Shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellEventsResponse()
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


    def DeleteReverseShellRules(self, request):
        """删除反弹Shell规则

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReverseShellRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellRulesResponse()
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


    def DeleteSearchTemplate(self, request):
        """删除检索模板

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSearchTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSearchTemplateResponse()
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


    def DeleteTags(self, request):
        """删除标签

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTagsResponse()
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


    def DeleteWebPageEventLog(self, request):
        """网站防篡改-删除事件记录

        :param request: Request instance for DeleteWebPageEventLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWebPageEventLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWebPageEventLogResponse()
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


    def DescribeAccountStatistics(self, request):
        """本接口 (DescribeAccountStatistics) 用于获取帐号统计列表数据。

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountStatisticsResponse()
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


    def DescribeAccounts(self, request):
        """该接口已废弃

        本接口 (DescribeAccounts) 用于获取帐号列表数据。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeAssetInfo(self, request):
        """获取资产数量： 主机数、账号数、端口数、进程数、软件数、数据库数、Web应用数、Web框架数、Web服务数、Web站点数

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetInfoResponse()
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


    def DescribeAssetRecentMachineInfo(self, request):
        """获取主机最近趋势情况

        :param request: Request instance for DescribeAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetRecentMachineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetRecentMachineInfoResponse()
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


    def DescribeAttackLogInfo(self, request):
        """网络攻击日志详情

        :param request: Request instance for DescribeAttackLogInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttackLogInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttackLogInfoResponse()
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


    def DescribeAttackLogs(self, request):
        """按分页形式展示网络攻击日志列表

        :param request: Request instance for DescribeAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttackLogsResponse()
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


    def DescribeAttackVulTypeList(self, request):
        """获取网络攻击威胁类型列表

        :param request: Request instance for DescribeAttackVulTypeList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttackVulTypeList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttackVulTypeListResponse()
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


    def DescribeBashEvents(self, request):
        """获取高危命令列表

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBashEventsResponse()
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


    def DescribeBashRules(self, request):
        """获取高危命令规则列表

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBashRulesResponse()
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


    def DescribeBruteAttackList(self, request):
        """获取密码破解列表

        :param request: Request instance for DescribeBruteAttackList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBruteAttackList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBruteAttackListResponse()
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


    def DescribeComponentStatistics(self, request):
        """本接口 (DescribeComponentStatistics) 用于获取组件统计列表数据。

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComponentStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComponentStatisticsResponse()
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


    def DescribeESAggregations(self, request):
        """获取ES字段聚合结果

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeESAggregations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeESAggregationsResponse()
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


    def DescribeESHits(self, request):
        """获取ES查询文档列表

        :param request: Request instance for DescribeESHits.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeESHitsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeESHitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeESHits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeESHitsResponse()
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


    def DescribeExportMachines(self, request):
        """本接口 (DescribeExportMachines) 用于导出区域主机列表。

        :param request: Request instance for DescribeExportMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeExportMachines", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExportMachinesResponse()
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


    def DescribeGeneralStat(self, request):
        """获取主机安全相关统计

        :param request: Request instance for DescribeGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGeneralStat", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGeneralStatResponse()
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


    def DescribeHistoryAccounts(self, request):
        """本接口 (DescribeHistoryAccounts) 用于获取帐号变更历史列表数据。

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryAccountsResponse()
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


    def DescribeHistoryService(self, request):
        """查询日志检索服务信息

        :param request: Request instance for DescribeHistoryService.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryServiceResponse()
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


    def DescribeImportMachineInfo(self, request):
        """查询批量导入机器信息

        :param request: Request instance for DescribeImportMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImportMachineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImportMachineInfoResponse()
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


    def DescribeIndexList(self, request):
        """获取索引列表

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIndexList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIndexListResponse()
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


    def DescribeLogStorageStatistic(self, request):
        """获取日志检索容量使用统计

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogStorageStatistic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogStorageStatisticResponse()
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


    def DescribeLoginWhiteList(self, request):
        """获取异地登录白名单列表

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoginWhiteListResponse()
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


    def DescribeMachineInfo(self, request):
        """本接口（DescribeMachineInfo）用于获取机器详细信息。

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineInfoResponse()
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


    def DescribeMachineList(self, request):
        """本接口 (DescribeMachineList) 用于网页防篡改获取区域主机列表。

        :param request: Request instance for DescribeMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineListResponse()
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


    def DescribeMachineOsList(self, request):
        """查询可筛选操作系统列表.

        :param request: Request instance for DescribeMachineOsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineOsList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineOsListResponse()
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


    def DescribeMachineRegions(self, request):
        """获取机器地域列表

        :param request: Request instance for DescribeMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineRegionsResponse()
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


    def DescribeMachines(self, request):
        """本接口 (DescribeMachines) 用于获取区域主机列表。

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachines", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachinesResponse()
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


    def DescribeMalwareInfo(self, request):
        """查看恶意文件详情

        :param request: Request instance for DescribeMalwareInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMalwareInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMalwareInfoResponse()
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


    def DescribeMalwareTimingScanSetting(self, request):
        """查询定时扫描配置

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMalwareTimingScanSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMalwareTimingScanSettingResponse()
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


    def DescribeOpenPortStatistics(self, request):
        """本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOpenPortStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOpenPortStatisticsResponse()
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


    def DescribeOverviewStatistics(self, request):
        """本接口用于（DescribeOverviewStatistics）获取概览统计数据。

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOverviewStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOverviewStatisticsResponse()
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


    def DescribePrivilegeEvents(self, request):
        """获取本地提权事件列表

        :param request: Request instance for DescribePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivilegeEventsResponse()
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


    def DescribePrivilegeRules(self, request):
        """获取本地提权规则列表

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivilegeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivilegeRulesResponse()
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


    def DescribeProVersionInfo(self, request):
        """本接口 (DescribeProVersionInfo) 用于获取专业版信息。

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProVersionInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProVersionInfoResponse()
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


    def DescribeProcessStatistics(self, request):
        """本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProcessStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProcessStatisticsResponse()
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


    def DescribeReverseShellEvents(self, request):
        """获取反弹Shell列表

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsResponse()
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


    def DescribeReverseShellRules(self, request):
        """获取反弹Shell规则列表

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellRulesResponse()
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


    def DescribeRiskDnsList(self, request):
        """入侵检测，获取恶意请求列表

        :param request: Request instance for DescribeRiskDnsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskDnsList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskDnsListResponse()
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


    def DescribeScanMalwareSchedule(self, request):
        """查询木马扫描进度

        :param request: Request instance for DescribeScanMalwareSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanMalwareSchedule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanMalwareScheduleResponse()
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


    def DescribeScanTaskDetails(self, request):
        """DescribeScanTaskDetails 查询扫描任务详情 , 可以查询扫描进度信息/异常;

        :param request: Request instance for DescribeScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanTaskDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanTaskDetailsResponse()
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


    def DescribeScanVulSetting(self, request):
        """查询定期检测的配置

        :param request: Request instance for DescribeScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanVulSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanVulSettingResponse()
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


    def DescribeSearchExportList(self, request):
        """导出ES查询文档列表

        :param request: Request instance for DescribeSearchExportList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchExportListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchExportListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSearchExportList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchExportListResponse()
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


    def DescribeSearchLogs(self, request):
        """获取历史搜索记录

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSearchLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchLogsResponse()
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


    def DescribeSearchTemplates(self, request):
        """获取快速检索列表

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSearchTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchTemplatesResponse()
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


    def DescribeSecurityDynamics(self, request):
        """本接口 (DescribeSecurityDynamics) 用于获取安全事件消息数据。

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityDynamics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityDynamicsResponse()
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


    def DescribeSecurityEventsCnt(self, request):
        """获取安全概览相关事件统计数据接口

        :param request: Request instance for DescribeSecurityEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityEventsCnt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityEventsCntResponse()
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


    def DescribeSecurityTrends(self, request):
        """本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityTrends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityTrendsResponse()
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


    def DescribeTagMachines(self, request):
        """获取指定标签关联的服务器信息

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagMachines", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagMachinesResponse()
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


    def DescribeTags(self, request):
        """获取所有主机标签

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsResponse()
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


    def DescribeUsualLoginPlaces(self, request):
        """此接口（DescribeUsualLoginPlaces）用于查询常用登录地。

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsualLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsualLoginPlacesResponse()
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


    def DescribeWebPageGeneralize(self, request):
        """查询网站防篡改概览信息

        :param request: Request instance for DescribeWebPageGeneralize.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWebPageGeneralize", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebPageGeneralizeResponse()
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


    def EditBashRules(self, request):
        """新增或修改高危命令规则

        :param request: Request instance for EditBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditBashRulesResponse()
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


    def EditTags(self, request):
        """新增或编辑标签

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditTagsResponse()
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


    def ExportAssetCoreModuleList(self, request):
        """导出资产管理内核模块列表

        :param request: Request instance for ExportAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportAssetCoreModuleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportAssetCoreModuleListResponse()
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


    def ExportAttackLogs(self, request):
        """导出网络攻击日志

        :param request: Request instance for ExportAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportAttackLogsResponse()
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


    def ExportBashEvents(self, request):
        """导出高危命令事件

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportBashEventsResponse()
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


    def ExportBruteAttacks(self, request):
        """本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportBruteAttacksResponse()
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


    def ExportMaliciousRequests(self, request):
        """本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportMaliciousRequests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportMaliciousRequestsResponse()
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


    def ExportMalwares(self, request):
        """本接口 (ExportMalwares) 用于导出木马记录CSV文件。

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportMalwaresResponse()
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


    def ExportNonlocalLoginPlaces(self, request):
        """本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportNonlocalLoginPlacesResponse()
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


    def ExportPrivilegeEvents(self, request):
        """导出本地提权事件

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportPrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportPrivilegeEventsResponse()
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


    def ExportReverseShellEvents(self, request):
        """导出反弹Shell事件

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportReverseShellEventsResponse()
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


    def ExportTasks(self, request):
        """用于异步导出数据量大的日志文件

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportTasksResponse()
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


    def ExportVulDetectionExcel(self, request):
        """导出本次漏洞检测Excel

        :param request: Request instance for ExportVulDetectionExcel.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVulDetectionExcel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVulDetectionExcelResponse()
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


    def ExportVulDetectionReport(self, request):
        """导出漏洞检测报告。

        :param request: Request instance for ExportVulDetectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVulDetectionReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVulDetectionReportResponse()
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


    def IgnoreImpactedHosts(self, request):
        """本接口 (IgnoreImpactedHosts) 用于忽略漏洞。

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IgnoreImpactedHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IgnoreImpactedHostsResponse()
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


    def InquiryPriceOpenProVersionPrepaid(self, request):
        """本接口 (InquiryPriceOpenProVersionPrepaid) 用于开通专业版询价(预付费)。

        :param request: Request instance for InquiryPriceOpenProVersionPrepaid.
        :type request: :class:`tencentcloud.cwp.v20180228.models.InquiryPriceOpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.InquiryPriceOpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceOpenProVersionPrepaid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceOpenProVersionPrepaidResponse()
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


    def ModifyAutoOpenProVersionConfig(self, request):
        """本接口 (ModifyAutoOpenProVersionConfig) 用于设置新增主机自动开通专业版配置。

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoOpenProVersionConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoOpenProVersionConfigResponse()
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


    def ModifyMalwareTimingScanSettings(self, request):
        """定时扫描设置

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMalwareTimingScanSettings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMalwareTimingScanSettingsResponse()
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


    def ModifyProVersionRenewFlag(self, request):
        """本接口 (ModifyProVersionRenewFlag) 用于修改专业版包年包月续费标识。

        :param request: Request instance for ModifyProVersionRenewFlag.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyProVersionRenewFlagRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyProVersionRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProVersionRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProVersionRenewFlagResponse()
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


    def ModifyWarningSetting(self, request):
        """修改告警设置

        :param request: Request instance for ModifyWarningSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWarningSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWarningSettingResponse()
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


    def ModifyWebPageProtectSetting(self, request):
        """网站防篡改-修改网站防护设置

        :param request: Request instance for ModifyWebPageProtectSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWebPageProtectSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWebPageProtectSettingResponse()
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


    def OpenProVersion(self, request):
        """本接口 (OpenProVersion) 用于开通专业版。

        :param request: Request instance for OpenProVersion.
        :type request: :class:`tencentcloud.cwp.v20180228.models.OpenProVersionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.OpenProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProVersionResponse()
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


    def OpenProVersionPrepaid(self, request):
        """本接口 (OpenProVersionPrepaid) 用于开通专业版(包年包月)。

        :param request: Request instance for OpenProVersionPrepaid.
        :type request: :class:`tencentcloud.cwp.v20180228.models.OpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.OpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProVersionPrepaid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProVersionPrepaidResponse()
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


    def RecoverMalwares(self, request):
        """本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverMalwaresResponse()
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


    def RenewProVersion(self, request):
        """本接口 (RenewProVersion) 用于续费专业版(包年包月)。

        :param request: Request instance for RenewProVersion.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RenewProVersionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RenewProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewProVersionResponse()
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


    def RescanImpactedHost(self, request):
        """该接口已废弃

        本接口 (RescanImpactedHost) 用于漏洞重新检测。

        :param request: Request instance for RescanImpactedHost.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RescanImpactedHostRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RescanImpactedHostResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RescanImpactedHost", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RescanImpactedHostResponse()
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


    def ScanAsset(self, request):
        """资产指纹启动扫描

        :param request: Request instance for ScanAsset.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanAssetRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanAssetResponse()
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


    def ScanVul(self, request):
        """一键检测

        :param request: Request instance for ScanVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanVul", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanVulResponse()
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


    def ScanVulAgain(self, request):
        """漏洞管理-重新检测接口

        :param request: Request instance for ScanVulAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanVulAgain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanVulAgainResponse()
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


    def ScanVulSetting(self, request):
        """定期扫描漏洞设置

        :param request: Request instance for ScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanVulSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanVulSettingResponse()
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


    def SeparateMalwares(self, request):
        """本接口（SeparateMalwares）用于隔离木马。

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SeparateMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SeparateMalwaresResponse()
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


    def SetBashEventsStatus(self, request):
        """设置高危命令事件状态

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetBashEventsStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetBashEventsStatusResponse()
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


    def SwitchBashRules(self, request):
        """切换高危命令规则状态

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchBashRulesResponse()
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


    def SyncAssetScan(self, request):
        """同步资产扫描信息

        :param request: Request instance for SyncAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncAssetScan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncAssetScanResponse()
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


    def TrustMalwares(self, request):
        """本接口(TrustMalwares)将被识别木马文件设为信任。

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrustMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrustMalwaresResponse()
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


    def UntrustMalwares(self, request):
        """本接口（UntrustMalwares）用于取消信任木马文件。

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UntrustMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UntrustMalwaresResponse()
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


    def UpdateBaselineStrategy(self, request):
        """根据基线策略id更新策略信息

        :param request: Request instance for UpdateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateBaselineStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateBaselineStrategyResponse()
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