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
from tencentcloud.teo.v20220106 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-01-06'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def CheckCertificate(self, request):
        """校验证书

        :param request: Request instance for CheckCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.CheckCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CheckCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckCertificateResponse()
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


    def CreateApplicationProxy(self, request):
        """创建应用代理

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationProxyResponse()
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


    def CreateApplicationProxyRule(self, request):
        """创建应用代理规则

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationProxyRuleResponse()
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


    def CreateApplicationProxyRules(self, request):
        """批量创建应用代理规则

        :param request: Request instance for CreateApplicationProxyRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateApplicationProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationProxyRulesResponse()
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


    def CreateCustomErrorPage(self, request):
        """创建自定义规则的自定义页

        :param request: Request instance for CreateCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomErrorPageResponse()
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


    def CreateDnsRecord(self, request):
        """创建 DNS 记录

        :param request: Request instance for CreateDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDnsRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDnsRecordResponse()
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


    def CreateLoadBalancing(self, request):
        """创建负载均衡

        :param request: Request instance for CreateLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancing", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancingResponse()
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


    def CreateOriginGroup(self, request):
        """源站组创建

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOriginGroupResponse()
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


    def CreatePlanForZone(self, request):
        """为未购买套餐的站点购买套餐

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePlanForZoneResponse()
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


    def CreatePrefetchTask(self, request):
        """创建预热任务

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrefetchTaskResponse()
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


    def CreatePurgeTask(self, request):
        """创建清除缓存任务

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePurgeTaskResponse()
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


    def CreateRule(self, request):
        """规则引擎创建规则。

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def CreateZone(self, request):
        """用于用户接入新的站点

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateZoneResponse()
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


    def DeleteApplicationProxy(self, request):
        """删除应用代理

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationProxyResponse()
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


    def DeleteApplicationProxyRule(self, request):
        """删除应用代理规则

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationProxyRuleResponse()
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


    def DeleteDnsRecords(self, request):
        """批量删除 DNS 记录

        :param request: Request instance for DeleteDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDnsRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDnsRecordsResponse()
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


    def DeleteLoadBalancing(self, request):
        """删除负载均衡

        :param request: Request instance for DeleteLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancing", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancingResponse()
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


    def DeleteOriginGroup(self, request):
        """源站组删除

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOriginGroupResponse()
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


    def DeleteRules(self, request):
        """批量删除规则引擎规则。

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRulesResponse()
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


    def DeleteZone(self, request):
        """删除站点

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteZoneResponse()
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


    def DescribeApplicationProxy(self, request):
        """获取应用代理列表

        :param request: Request instance for DescribeApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationProxyResponse()
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


    def DescribeApplicationProxyDetail(self, request):
        """获取应用代理详细信息

        :param request: Request instance for DescribeApplicationProxyDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeApplicationProxyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationProxyDetailResponse()
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


    def DescribeAvailablePlans(self, request):
        """查询当前账户可用套餐信息列表

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailablePlansResponse()
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


    def DescribeBotLog(self, request):
        """查询Bot攻击日志

        :param request: Request instance for DescribeBotLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeBotLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeBotLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotLogResponse()
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


    def DescribeBotManagedRules(self, request):
        """分页查询Bot托管规则

        :param request: Request instance for DescribeBotManagedRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeBotManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeBotManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotManagedRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotManagedRulesResponse()
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


    def DescribeCnameStatus(self, request):
        """查询域名 CNAME 状态

        :param request: Request instance for DescribeCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCnameStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCnameStatusResponse()
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


    def DescribeDDoSPolicy(self, request):
        """查询DDoS防护配置详情

        :param request: Request instance for DescribeDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSPolicyResponse()
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


    def DescribeDDosAttackData(self, request):
        """查询DDos攻击时序数据

        :param request: Request instance for DescribeDDosAttackData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosAttackDataResponse()
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


    def DescribeDDosAttackEvent(self, request):
        """查询DDos攻击事件

        :param request: Request instance for DescribeDDosAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosAttackEventResponse()
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


    def DescribeDDosAttackEventDetail(self, request):
        """查询DDos攻击事件详情

        :param request: Request instance for DescribeDDosAttackEventDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackEventDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosAttackEventDetailResponse()
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


    def DescribeDDosAttackSourceEvent(self, request):
        """查询DDos攻击源信息

        :param request: Request instance for DescribeDDosAttackSourceEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackSourceEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackSourceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackSourceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosAttackSourceEventResponse()
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


    def DescribeDDosAttackTopData(self, request):
        """查询DDos攻击Top数据

        :param request: Request instance for DescribeDDosAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosAttackTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosAttackTopDataResponse()
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


    def DescribeDDosMajorAttackEvent(self, request):
        """查询DDos主攻击事件

        :param request: Request instance for DescribeDDosMajorAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDDosMajorAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDDosMajorAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDosMajorAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDosMajorAttackEventResponse()
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


    def DescribeDefaultCertificates(self, request):
        """查询默认证书列表

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultCertificatesResponse()
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


    def DescribeDnsData(self, request):
        """获取DNS请求数统计曲线

        :param request: Request instance for DescribeDnsData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnsDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnsDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDnsDataResponse()
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


    def DescribeDnsRecords(self, request):
        """查询 DNS 记录列表，支持搜索、分页、排序、过滤。

        :param request: Request instance for DescribeDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDnsRecordsResponse()
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


    def DescribeDnssec(self, request):
        """用于查询 DNSSEC 相关信息

        :param request: Request instance for DescribeDnssec.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnssec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDnssecResponse()
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


    def DescribeHostsCertificate(self, request):
        """查询域名证书列表，支持搜索、分页、排序、过滤。

        :param request: Request instance for DescribeHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsCertificateResponse()
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


    def DescribeHostsSetting(self, request):
        """用于查询域名配置信息

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsSettingResponse()
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


    def DescribeIdentification(self, request):
        """查询验证结果

        :param request: Request instance for DescribeIdentification.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeIdentificationRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeIdentificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdentificationResponse()
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


    def DescribeLoadBalancing(self, request):
        """获取负载均衡列表

        :param request: Request instance for DescribeLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancing", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancingResponse()
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


    def DescribeLoadBalancingDetail(self, request):
        """获取负载均衡详细信息

        :param request: Request instance for DescribeLoadBalancingDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeLoadBalancingDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancingDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancingDetailResponse()
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


    def DescribeOriginGroup(self, request):
        """获取源站组信息列表

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginGroupResponse()
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


    def DescribeOriginGroupDetail(self, request):
        """获取源站组详细信息

        :param request: Request instance for DescribeOriginGroupDetail.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOriginGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroupDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginGroupDetailResponse()
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


    def DescribeOverviewL7Data(self, request):
        """本接口（DescribeOverviewL7Data）用于查询七层监控类时序流量数据。

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOverviewL7DataResponse()
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


    def DescribePrefetchTasks(self, request):
        """查询预热任务状态

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrefetchTasksResponse()
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


    def DescribePurgeTasks(self, request):
        """查询清除缓存历史记录

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
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


    def DescribeRules(self, request):
        """查询规则引擎规则。

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesResponse()
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


    def DescribeRulesSetting(self, request):
        """返回规则引擎可应用匹配请求的设置列表及其详细建议配置信息

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesSettingResponse()
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


    def DescribeSecurityPolicy(self, request):
        """查询安全防护配置详情

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyResponse()
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


    def DescribeSecurityPolicyList(self, request):
        """查询全部安全实例

        :param request: Request instance for DescribeSecurityPolicyList.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyListRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyListResponse()
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


    def DescribeSecurityPolicyManagedRules(self, request):
        """分页查询门神规则

        :param request: Request instance for DescribeSecurityPolicyManagedRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyManagedRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyManagedRulesResponse()
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


    def DescribeSecurityPolicyManagedRulesId(self, request):
        """规则id查询门神规则详情

        :param request: Request instance for DescribeSecurityPolicyManagedRulesId.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesIdRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyManagedRulesIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyManagedRulesId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyManagedRulesIdResponse()
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


    def DescribeSecurityPolicyRegions(self, request):
        """查询所有地域信息

        :param request: Request instance for DescribeSecurityPolicyRegions.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPolicyRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyRegions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyRegionsResponse()
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


    def DescribeSecurityPortraitRules(self, request):
        """查询Bot用户画像规则

        :param request: Request instance for DescribeSecurityPortraitRules.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPortraitRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeSecurityPortraitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPortraitRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPortraitRulesResponse()
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


    def DescribeTimingL4Data(self, request):
        """四层时序流量数据查询

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL4DataResponse()
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


    def DescribeTimingL7AnalysisData(self, request):
        """查询七层数据分析类时序流量数据

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL7AnalysisDataResponse()
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


    def DescribeTimingL7CacheData(self, request):
        """七层查询缓存分析时序类流量数据

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL7CacheDataResponse()
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


    def DescribeTopL7AnalysisData(self, request):
        """查询top类流量数据

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopL7AnalysisDataResponse()
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


    def DescribeTopL7CacheData(self, request):
        """七层查询缓存分析top类流量数据

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopL7CacheDataResponse()
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


    def DescribeWebManagedRulesAttackEvents(self, request):
        """查询Web托管攻击事件

        :param request: Request instance for DescribeWebManagedRulesAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesAttackEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesAttackEventsResponse()
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


    def DescribeWebManagedRulesData(self, request):
        """查询waf攻击时序数据

        :param request: Request instance for DescribeWebManagedRulesData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesDataResponse()
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


    def DescribeWebManagedRulesLog(self, request):
        """查询waf攻击日志

        :param request: Request instance for DescribeWebManagedRulesLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesLogResponse()
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


    def DescribeWebManagedRulesTopData(self, request):
        """查询waf攻击top数据

        :param request: Request instance for DescribeWebManagedRulesTopData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebManagedRulesTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesTopDataResponse()
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


    def DescribeWebProtectionAttackEvents(self, request):
        """查询web防护攻击事件

        :param request: Request instance for DescribeWebProtectionAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionAttackEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionAttackEventsResponse()
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


    def DescribeWebProtectionData(self, request):
        """查询CC防护时序数据

        :param request: Request instance for DescribeWebProtectionData.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionDataResponse()
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


    def DescribeWebProtectionLog(self, request):
        """查询CC防护日志

        :param request: Request instance for DescribeWebProtectionLog.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeWebProtectionLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionLogResponse()
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


    def DescribeZoneDDoSPolicy(self, request):
        """查询所有DDoS防护分区

        :param request: Request instance for DescribeZoneDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneDDoSPolicyResponse()
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


    def DescribeZoneDetails(self, request):
        """根据站点 ID 查询站点的详细信息

        :param request: Request instance for DescribeZoneDetails.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDetailsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneDetails", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneDetailsResponse()
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


    def DescribeZoneSetting(self, request):
        """用于查询站点的所有配置信息。

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneSettingResponse()
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


    def DescribeZones(self, request):
        """用户查询用户站点信息列表，支持分页

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220106.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def DownloadL7Logs(self, request):
        """查询七层离线日志

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220106.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadL7LogsResponse()
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


    def IdentifyZone(self, request):
        """用于验证站点所有权

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdentifyZoneResponse()
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


    def ImportDnsRecords(self, request):
        """导入 DNS 记录

        :param request: Request instance for ImportDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.ImportDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ImportDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportDnsRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportDnsRecordsResponse()
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


    def ModifyApplicationProxy(self, request):
        """修改应用代理

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyResponse()
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


    def ModifyApplicationProxyRule(self, request):
        """修改应用代理规则

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyRuleResponse()
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


    def ModifyApplicationProxyRuleStatus(self, request):
        """修改应用代理规则的状态

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyRuleStatusResponse()
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


    def ModifyApplicationProxyStatus(self, request):
        """修改应用代理的状态

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyStatusResponse()
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


    def ModifyDDoSPolicy(self, request):
        """修改DDoS防护分区配置

        :param request: Request instance for ModifyDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyResponse()
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


    def ModifyDDoSPolicyHost(self, request):
        """域名DDoS高可用开关

        :param request: Request instance for ModifyDDoSPolicyHost.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyHostRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDDoSPolicyHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicyHost", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyHostResponse()
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


    def ModifyDefaultCertificate(self, request):
        """修改默认证书状态

        :param request: Request instance for ModifyDefaultCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDefaultCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDefaultCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDefaultCertificateResponse()
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


    def ModifyDnsRecord(self, request):
        """修改 DNS 记录

        :param request: Request instance for ModifyDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDnsRecordResponse()
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


    def ModifyDnssec(self, request):
        """修改 DNSSEC 状态

        :param request: Request instance for ModifyDnssec.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnssec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDnssecResponse()
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


    def ModifyHostsCertificate(self, request):
        """用于修改域名证书

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHostsCertificateResponse()
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


    def ModifyLoadBalancing(self, request):
        """修改负载均衡

        :param request: Request instance for ModifyLoadBalancing.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancing", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancingResponse()
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


    def ModifyLoadBalancingStatus(self, request):
        """修改负载均衡状态

        :param request: Request instance for ModifyLoadBalancingStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyLoadBalancingStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancingStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancingStatusResponse()
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


    def ModifyOriginGroup(self, request):
        """源站组修改

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyOriginGroupResponse()
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


    def ModifyRule(self, request):
        """修改规则引擎规则。

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleResponse()
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


    def ModifyRulePriority(self, request):
        """修改规则引擎规则优先级

        :param request: Request instance for ModifyRulePriority.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRulePriority", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRulePriorityResponse()
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


    def ModifySecurityPolicy(self, request):
        """修改Web&Bot安全配置

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityPolicyResponse()
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


    def ModifyZone(self, request):
        """用该站点信息

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneResponse()
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


    def ModifyZoneCnameSpeedUp(self, request):
        """开启，关闭 CNAME 加速

        :param request: Request instance for ModifyZoneCnameSpeedUp.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneCnameSpeedUpRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneCnameSpeedUpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneCnameSpeedUp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneCnameSpeedUpResponse()
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


    def ModifyZoneSetting(self, request):
        """用于修改站点配置

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneSettingResponse()
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


    def ModifyZoneStatus(self, request):
        """用于开启，关闭站点

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220106.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneStatusResponse()
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


    def ReclaimZone(self, request):
        """站点被其他用户接入后，验证了站点所有权之后，可以找回该站点

        :param request: Request instance for ReclaimZone.
        :type request: :class:`tencentcloud.teo.v20220106.models.ReclaimZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ReclaimZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReclaimZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReclaimZoneResponse()
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


    def ScanDnsRecords(self, request):
        """扫描站点历史解析记录

        :param request: Request instance for ScanDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220106.models.ScanDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220106.models.ScanDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanDnsRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanDnsRecordsResponse()
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