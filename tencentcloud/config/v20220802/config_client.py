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
from tencentcloud.config.v20220802 import models


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.tencentcloudapi.com'
    _service = 'config'


    def AddAggregateCompliancePack(self, request):
        r"""账号组新建合规包

        :param request: Request instance for AddAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.AddAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.AddAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAggregateConfigRule(self, request):
        r"""账号组新建规则

        :param request: Request instance for AddAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.AddAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCompliancePack(self, request):
        r"""新建合规包

        :param request: Request instance for AddCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.AddCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.AddCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddConfigRule(self, request):
        r"""新建 规则

        :param request: Request instance for AddConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.AddConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.AddConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAggregateConfigRule(self, request):
        r"""账号组关闭规则

        :param request: Request instance for CloseAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseConfigRecorder(self, request):
        r"""资源监控管理-关闭监控

        :param request: Request instance for CloseConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.CloseConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseConfigRule(self, request):
        r"""关闭规则

        :param request: Request instance for CloseConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.CloseConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CloseConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.CloseConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAggregator(self, request):
        r"""新建账号组

        :param request: Request instance for CreateAggregator.
        :type request: :class:`tencentcloud.config.v20220802.models.CreateAggregatorRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CreateAggregatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAggregator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAggregatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRemediation(self, request):
        r"""新增规则修正设置

        :param request: Request instance for CreateRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.CreateRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.CreateRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAggregateCompliancePack(self, request):
        r"""账号组删除合规包

        :param request: Request instance for DeleteAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAggregateConfigRule(self, request):
        r"""账号组删除规则

        :param request: Request instance for DeleteAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompliancePack(self, request):
        r"""删除合规包

        :param request: Request instance for DeleteCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigRule(self, request):
        r"""删除规则

        :param request: Request instance for DeleteConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRemediations(self, request):
        r"""删除规则修正设置

        :param request: Request instance for DeleteRemediations.
        :type request: :class:`tencentcloud.config.v20220802.models.DeleteRemediationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DeleteRemediationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRemediations", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRemediationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateCompliancePack(self, request):
        r"""账号组合规包详情

        :param request: Request instance for DescribeAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateConfigDeliver(self, request):
        r"""账号组获取投递设置详情

        :param request: Request instance for DescribeAggregateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateConfigRule(self, request):
        r"""账号组获取规则详情

        :param request: Request instance for DescribeAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregateDiscoveredResource(self, request):
        r"""账号组资源详情

        :param request: Request instance for DescribeAggregateDiscoveredResource.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregateDiscoveredResourceRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregateDiscoveredResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregateDiscoveredResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregateDiscoveredResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAggregator(self, request):
        r"""账号组详情

        :param request: Request instance for DescribeAggregator.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeAggregatorRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeAggregatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAggregator", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAggregatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompliancePack(self, request):
        r"""合规包详情

        :param request: Request instance for DescribeCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigDeliver(self, request):
        r"""获取投递设置详情

        :param request: Request instance for DescribeConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigRecorder(self, request):
        r"""获取监控详情

        :param request: Request instance for DescribeConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigRule(self, request):
        r"""获取规则详情

        :param request: Request instance for DescribeConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiscoveredResource(self, request):
        r"""资源详情

        :param request: Request instance for DescribeDiscoveredResource.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeDiscoveredResourceRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeDiscoveredResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiscoveredResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiscoveredResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemCompliancePack(self, request):
        r"""获取系统合规包详情

        :param request: Request instance for DescribeSystemCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeSystemCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeSystemCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemRule(self, request):
        r"""预设规则详情

        :param request: Request instance for DescribeSystemRule.
        :type request: :class:`tencentcloud.config.v20220802.models.DescribeSystemRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DescribeSystemRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachAggregateConfigRuleToCompliancePack(self, request):
        r"""账号组合规包移除规则

        :param request: Request instance for DetachAggregateConfigRuleToCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DetachAggregateConfigRuleToCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DetachAggregateConfigRuleToCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachAggregateConfigRuleToCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DetachAggregateConfigRuleToCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachConfigRuleToCompliancePack(self, request):
        r"""合规包移除规则

        :param request: Request instance for DetachConfigRuleToCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.DetachConfigRuleToCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.DetachConfigRuleToCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachConfigRuleToCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.DetachConfigRuleToCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateCompliancePacks(self, request):
        r"""账号组获取合规包列表

        :param request: Request instance for ListAggregateCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateConfigRuleEvaluationResults(self, request):
        r"""账号组获取评估结果--规则维度（某个规则下资源的评估结果列表）

        :param request: Request instance for ListAggregateConfigRuleEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRuleEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRuleEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRuleEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateConfigRules(self, request):
        r"""账号组获取规则列表

        :param request: Request instance for ListAggregateConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregateDiscoveredResources(self, request):
        r"""账号组获取资源列表

        :param request: Request instance for ListAggregateDiscoveredResources.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregateDiscoveredResourcesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregateDiscoveredResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregateDiscoveredResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregateDiscoveredResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAggregators(self, request):
        r"""账号组列表

        :param request: Request instance for ListAggregators.
        :type request: :class:`tencentcloud.config.v20220802.models.ListAggregatorsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListAggregatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAggregators", params, headers=headers)
            response = json.loads(body)
            model = models.ListAggregatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCompliancePacks(self, request):
        r"""获取合规包列表

        :param request: Request instance for ListCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRuleEvaluationResults(self, request):
        r"""获取评估结果--规则维度（某个规则下资源的评估结果列表）

        :param request: Request instance for ListConfigRuleEvaluationResults.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRuleEvaluationResultsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRuleEvaluationResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRuleEvaluationResults", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRuleEvaluationResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConfigRules(self, request):
        r"""获取规则列表

        :param request: Request instance for ListConfigRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListConfigRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListConfigRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConfigRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListConfigRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDiscoveredResources(self, request):
        r"""获取资源列表

        :param request: Request instance for ListDiscoveredResources.
        :type request: :class:`tencentcloud.config.v20220802.models.ListDiscoveredResourcesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListDiscoveredResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDiscoveredResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListDiscoveredResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRemediationExecutions(self, request):
        r"""修正记录

        :param request: Request instance for ListRemediationExecutions.
        :type request: :class:`tencentcloud.config.v20220802.models.ListRemediationExecutionsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListRemediationExecutionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRemediationExecutions", params, headers=headers)
            response = json.loads(body)
            model = models.ListRemediationExecutionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRemediations(self, request):
        r"""修正设置列表

        :param request: Request instance for ListRemediations.
        :type request: :class:`tencentcloud.config.v20220802.models.ListRemediationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListRemediationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRemediations", params, headers=headers)
            response = json.loads(body)
            model = models.ListRemediationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceTypes(self, request):
        r"""获取资源类型列表

        :param request: Request instance for ListResourceTypes.
        :type request: :class:`tencentcloud.config.v20220802.models.ListResourceTypesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListResourceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSystemCompliancePacks(self, request):
        r"""获取系统合规包列表

        :param request: Request instance for ListSystemCompliancePacks.
        :type request: :class:`tencentcloud.config.v20220802.models.ListSystemCompliancePacksRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListSystemCompliancePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSystemCompliancePacks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSystemCompliancePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSystemRules(self, request):
        r"""获取预设规则列表

        :param request: Request instance for ListSystemRules.
        :type request: :class:`tencentcloud.config.v20220802.models.ListSystemRulesRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.ListSystemRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSystemRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListSystemRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAggregateConfigRule(self, request):
        r"""账号组开启规则

        :param request: Request instance for OpenAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenConfigRecorder(self, request):
        r"""资源监控管理-开启监控

        :param request: Request instance for OpenConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.OpenConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenConfigRule(self, request):
        r"""开启规则

        :param request: Request instance for OpenConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.OpenConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.OpenConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.OpenConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutEvaluations(self, request):
        r"""上报自定义规则评估结果

        :param request: Request instance for PutEvaluations.
        :type request: :class:`tencentcloud.config.v20220802.models.PutEvaluationsRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.PutEvaluationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutEvaluations", params, headers=headers)
            response = json.loads(body)
            model = models.PutEvaluationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAggregateConfigRuleEvaluation(self, request):
        r"""账号组触发评估

        :param request: Request instance for StartAggregateConfigRuleEvaluation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartAggregateConfigRuleEvaluationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartAggregateConfigRuleEvaluationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAggregateConfigRuleEvaluation", params, headers=headers)
            response = json.loads(body)
            model = models.StartAggregateConfigRuleEvaluationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartConfigRuleEvaluation(self, request):
        r"""触发评估

        :param request: Request instance for StartConfigRuleEvaluation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartConfigRuleEvaluationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartConfigRuleEvaluationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartConfigRuleEvaluation", params, headers=headers)
            response = json.loads(body)
            model = models.StartConfigRuleEvaluationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRemediation(self, request):
        r"""手动执行规则修复

        :param request: Request instance for StartRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.StartRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.StartRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.StartRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateCompliancePack(self, request):
        r"""账号组编辑合规包

        :param request: Request instance for UpdateAggregateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateCompliancePackStatus(self, request):
        r"""账号组开启、关闭合规包

        :param request: Request instance for UpdateAggregateCompliancePackStatus.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackStatusRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateCompliancePackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateCompliancePackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateCompliancePackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateConfigDeliver(self, request):
        r"""账号组编辑投递设置

        :param request: Request instance for UpdateAggregateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAggregateConfigRule(self, request):
        r"""账号组编辑规则

        :param request: Request instance for UpdateAggregateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateAggregateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAggregateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAggregateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCompliancePack(self, request):
        r"""编辑合规包

        :param request: Request instance for UpdateCompliancePack.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCompliancePack", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCompliancePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCompliancePackStatus(self, request):
        r"""开启、关闭合规包

        :param request: Request instance for UpdateCompliancePackStatus.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackStatusRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateCompliancePackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCompliancePackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCompliancePackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigDeliver(self, request):
        r"""编辑投递设置

        :param request: Request instance for UpdateConfigDeliver.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigDeliverRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigRecorder(self, request):
        r"""编辑监控范围

        :param request: Request instance for UpdateConfigRecorder.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigRecorderRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigRecorderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigRecorder", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigRecorderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigRule(self, request):
        r"""编辑规则

        :param request: Request instance for UpdateConfigRule.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateConfigRuleRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateConfigRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRemediation(self, request):
        r"""新增告警监控规则

        :param request: Request instance for UpdateRemediation.
        :type request: :class:`tencentcloud.config.v20220802.models.UpdateRemediationRequest`
        :rtype: :class:`tencentcloud.config.v20220802.models.UpdateRemediationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRemediation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRemediationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))