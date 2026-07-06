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
from tencentcloud.fwm.v20250611 import models


class FwmClient(AbstractClient):
    _apiVersion = '2025-06-11'
    _endpoint = 'fwm.tencentcloudapi.com'
    _service = 'fwm'


    def CancelIgnorePolicyRisk(self, request):
        r"""取消忽略策略风险

        :param request: Request instance for CancelIgnorePolicyRisk.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CancelIgnorePolicyRiskRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CancelIgnorePolicyRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelIgnorePolicyRisk", params, headers=headers)
            response = json.loads(body)
            model = models.CancelIgnorePolicyRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAnalyzePolicyTask(self, request):
        r"""创建策略风险分析任务

        :param request: Request instance for CreateAnalyzePolicyTask.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateAnalyzePolicyTaskRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateAnalyzePolicyTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAnalyzePolicyTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAnalyzePolicyTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeAclRule(self, request):
        r"""向已有的互联网边界ACL规则组中添加规则。需要先创建规则组，然后通过此接口添加规则。

        :param request: Request instance for CreateEdgeAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateEdgeAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateEdgeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeAclRuleGroup(self, request):
        r"""创建互联网边界ACL规则组，支持同时创建多条规则。Product 必须为 cfw_edge_acl。规则支持 IP、域名、参数模板、实例、标签等多种源/目标类型。

        :param request: Request instance for CreateEdgeAclRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateEdgeAclRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateEdgeAclRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeAclRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeAclRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatAclRule(self, request):
        r"""在已有规则组中添加NAT ACL规则

        :param request: Request instance for CreateNatAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateNatAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateNatAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatAclRuleGroup(self, request):
        r"""创建NAT ACL规则组（NAT边界防火墙规则组管理）

        :param request: Request instance for CreateNatAclRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateNatAclRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateNatAclRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatAclRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatAclRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupRule(self, request):
        r"""规则组编辑时添加规则（规则组管理）

        :param request: Request instance for CreateSecurityGroupRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupRuleGroup(self, request):
        r"""创建规则组（规则组管理）

        :param request: Request instance for CreateSecurityGroupRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateSecurityGroupRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateSecurityGroupRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStrategy(self, request):
        r"""创建策略

        :param request: Request instance for CreateStrategy.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateStrategyRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcAclRule(self, request):
        r"""在已有规则组中添加VPC ACL规则

        :param request: Request instance for CreateVpcAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateVpcAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateVpcAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcAclRuleGroup(self, request):
        r"""创建VPC ACL规则组（VPC间防火墙规则组管理）

        :param request: Request instance for CreateVpcAclRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.CreateVpcAclRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.CreateVpcAclRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcAclRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcAclRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeAclRule(self, request):
        r"""批量删除互联网边界ACL规则。支持一次删除多条规则。

        :param request: Request instance for DeleteEdgeAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteEdgeAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteEdgeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatAclRule(self, request):
        r"""删除NAT ACL规则

        :param request: Request instance for DeleteNatAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteNatAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteNatAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRuleGroup(self, request):
        r"""删除规则组

        :param request: Request instance for DeleteRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupRule(self, request):
        r"""删除规则（规则组管理）

        :param request: Request instance for DeleteSecurityGroupRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStrategy(self, request):
        r"""删除策略

        :param request: Request instance for DeleteStrategy.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteStrategyRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcAclRule(self, request):
        r"""删除VPC ACL规则

        :param request: Request instance for DeleteVpcAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DeleteVpcAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DeleteVpcAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeAclRules(self, request):
        r"""查询指定规则组下的互联网边界ACL规则列表。支持分页和多种过滤条件。

        :param request: Request instance for DescribeEdgeAclRules.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeEdgeAclRulesRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeEdgeAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatAclRules(self, request):
        r"""查询NAT ACL规则列表

        :param request: Request instance for DescribeNatAclRules.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeNatAclRulesRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeNatAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganMembers(self, request):
        r"""查询集团下所有纳管成员账号列表，支持分页、排序和多条件筛选，仅管理员可调用

        :param request: Request instance for DescribeOrganMembers.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeOrganMembersRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeOrganMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganSummary(self, request):
        r"""获取集团概览信息，包括集团名称、管理员信息、成员数量等

        :param request: Request instance for DescribeOrganSummary.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeOrganSummaryRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeOrganSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicyRiskAccountProductStats(self, request):
        r"""查询账号+产品维度风险统计，按账号分组返回各产品的体检策略数、待整改风险数、整改率、最近体检时间等信息，支持按账号名称/ID搜索以及仅看待整改、仅超时未体检筛选

        :param request: Request instance for DescribePolicyRiskAccountProductStats.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribePolicyRiskAccountProductStatsRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribePolicyRiskAccountProductStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyRiskAccountProductStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyRiskAccountProductStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskAnalysisDetails(self, request):
        r"""获取实时分析风险详情

        :param request: Request instance for DescribeRiskAnalysisDetails.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskAnalysisDetailsRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskAnalysisDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskAnalysisDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskAnalysisDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCategoryStats(self, request):
        r"""查询策略体检风险分类统计数据,包含各类风险的规则数量、处置状态、整改率等信息

        :param request: Request instance for DescribeRiskCategoryStats.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskCategoryStatsRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskCategoryStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCategoryStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCategoryStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskList(self, request):
        r"""查询用户所有规则的策略问题

        :param request: Request instance for DescribeRiskList.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskListRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupRule(self, request):
        r"""查询规则详情（规则组管理）

        :param request: Request instance for DescribeSecurityGroupRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupRules(self, request):
        r"""查询规则组中规则列表接口

        :param request: Request instance for DescribeSecurityGroupRules.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeSecurityGroupRulesRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeSecurityGroupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategies(self, request):
        r"""查询策略列表

        :param request: Request instance for DescribeStrategies.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategiesRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategy(self, request):
        r"""查询策略详情

        :param request: Request instance for DescribeStrategy.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyAccounts(self, request):
        r"""查看防火墙管理规则下发账号列表

        :param request: Request instance for DescribeStrategyAccounts.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyAccountsRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyDispatchStatus(self, request):
        r"""查询策略下发状态

        :param request: Request instance for DescribeStrategyDispatchStatus.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyDispatchStatusRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeStrategyDispatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyDispatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyDispatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAclRules(self, request):
        r"""查询VPC ACL规则列表

        :param request: Request instance for DescribeVpcAclRules.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DescribeVpcAclRulesRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DescribeVpcAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DispatchStrategy(self, request):
        r"""下发策略

        :param request: Request instance for DispatchStrategy.
        :type request: :class:`tencentcloud.fwm.v20250611.models.DispatchStrategyRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.DispatchStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DispatchStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DispatchStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnorePolicyRisk(self, request):
        r"""忽略策略问题

        :param request: Request instance for IgnorePolicyRisk.
        :type request: :class:`tencentcloud.fwm.v20250611.models.IgnorePolicyRiskRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.IgnorePolicyRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnorePolicyRisk", params, headers=headers)
            response = json.loads(body)
            model = models.IgnorePolicyRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeAclRule(self, request):
        r"""修改互联网边界ACL规则。Rule 参数中必须包含 RuleId 用于指定要修改的规则。

        :param request: Request instance for ModifyEdgeAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyEdgeAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyEdgeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeAclRuleSequence(self, request):
        r"""批量调整互联网边界ACL规则的执行顺序。Sequences 参数必须包含所有受影响的规则序号映射关系。

        :param request: Request instance for ModifyEdgeAclRuleSequence.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyEdgeAclRuleSequenceRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyEdgeAclRuleSequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeAclRuleSequence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeAclRuleSequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatAclRule(self, request):
        r"""修改NAT ACL规则

        :param request: Request instance for ModifyNatAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyNatAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyNatAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatAclRuleSequence(self, request):
        r"""调整NAT ACL规则优先级顺序

        :param request: Request instance for ModifyNatAclRuleSequence.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyNatAclRuleSequenceRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyNatAclRuleSequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatAclRuleSequence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatAclRuleSequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleGroup(self, request):
        r"""修改规则组信息（规则组管理）

        :param request: Request instance for ModifyRuleGroup.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyRuleGroupRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupRule(self, request):
        r"""修改规则（规则组管理）

        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifySecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifySecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStrategy(self, request):
        r"""修改策略信息

        :param request: Request instance for ModifyStrategy.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyStrategyRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStrategySequence(self, request):
        r"""快速排序修改策略优先级

        :param request: Request instance for ModifyStrategySequence.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyStrategySequenceRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyStrategySequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStrategySequence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStrategySequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAclRule(self, request):
        r"""修改VPC ACL规则

        :param request: Request instance for ModifyVpcAclRule.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyVpcAclRuleRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyVpcAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAclRuleSequence(self, request):
        r"""调整VPC ACL规则优先级顺序

        :param request: Request instance for ModifyVpcAclRuleSequence.
        :type request: :class:`tencentcloud.fwm.v20250611.models.ModifyVpcAclRuleSequenceRequest`
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ModifyVpcAclRuleSequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAclRuleSequence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAclRuleSequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))