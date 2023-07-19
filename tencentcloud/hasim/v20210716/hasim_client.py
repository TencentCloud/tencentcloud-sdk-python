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
from tencentcloud.hasim.v20210716 import models


class HasimClient(AbstractClient):
    _apiVersion = '2021-07-16'
    _endpoint = 'hasim.tencentcloudapi.com'
    _service = 'hasim'


    def CreateRule(self, request):
        """创建自动化规则

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.hasim.v20210716.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTactic(self, request):
        """创建云兔切换策略

        :param request: Request instance for CreateTactic.
        :type request: :class:`tencentcloud.hasim.v20210716.models.CreateTacticRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.CreateTacticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTactic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTacticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTag(self, request):
        """创建标签

        :param request: Request instance for CreateTag.
        :type request: :class:`tencentcloud.hasim.v20210716.models.CreateTagRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.CreateTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """删除自动化规则

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTactic(self, request):
        """删除策略

        :param request: Request instance for DeleteTactic.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DeleteTacticRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DeleteTacticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTactic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTacticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTag(self, request):
        """删除标签

        :param request: Request instance for DeleteTag.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DeleteTagRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DeleteTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLink(self, request):
        """查询云兔连接详细信息

        :param request: Request instance for DescribeLink.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeLinkRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeLinkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLink", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLinkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLinks(self, request):
        """查询云兔连接列表

        :param request: Request instance for DescribeLinks.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeLinksRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeLinksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLinks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLinksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """查询订单列表

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRule(self, request):
        """查询自动化规则

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """查询自动化规则列表

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTactic(self, request):
        """查询云兔切换策略信息

        :param request: Request instance for DescribeTactic.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeTacticRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeTacticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTactic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTacticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTactics(self, request):
        """查询云兔切换策略列表

        :param request: Request instance for DescribeTactics.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeTacticsRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeTacticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTactics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTacticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        """查询标签列表

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.hasim.v20210716.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.DescribeTagsResponse`

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


    def ModifyLinkAdvancedLog(self, request):
        """编辑云兔高级日志状态

        :param request: Request instance for ModifyLinkAdvancedLog.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkAdvancedLogRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkAdvancedLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLinkAdvancedLog", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLinkAdvancedLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLinkTactic(self, request):
        """编辑云兔策略

        :param request: Request instance for ModifyLinkTactic.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkTacticRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkTacticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLinkTactic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLinkTacticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLinkTele(self, request):
        """修改云兔运营商

        :param request: Request instance for ModifyLinkTele.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkTeleRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyLinkTeleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLinkTele", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLinkTeleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """编辑自动化规则

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleStatus(self, request):
        """编辑自动化规则状态

        :param request: Request instance for ModifyRuleStatus.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyRuleStatusRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTactic(self, request):
        """修改云兔切换策略

        :param request: Request instance for ModifyTactic.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyTacticRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyTacticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTactic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTacticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTag(self, request):
        """编辑标签

        :param request: Request instance for ModifyTag.
        :type request: :class:`tencentcloud.hasim.v20210716.models.ModifyTagRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.ModifyTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewLinkInfo(self, request):
        """刷新云兔连接信息同步

        :param request: Request instance for RenewLinkInfo.
        :type request: :class:`tencentcloud.hasim.v20210716.models.RenewLinkInfoRequest`
        :rtype: :class:`tencentcloud.hasim.v20210716.models.RenewLinkInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewLinkInfo", params, headers=headers)
            response = json.loads(body)
            model = models.RenewLinkInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))