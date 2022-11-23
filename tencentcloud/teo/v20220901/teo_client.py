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
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def BindZoneToPlan(self, request):
        """将未绑定套餐的站点绑定到已有套餐

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindZoneToPlanResponse()
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


    def CheckCertificate(self, request):
        """校验证书

        :param request: Request instance for CheckCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCertificateResponse`

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


    def CreateAliasDomain(self, request):
        """创建别称域名。

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAliasDomainResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

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


    def CreateCredential(self, request):
        """用于创建COS回源私有凭证

        :param request: Request instance for CreateCredential.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCredentialRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCredential", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCredentialResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCustomErrorPageResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordResponse`

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


    def CreateIpTableList(self, request):
        """创建IP黑白名单列表

        :param request: Request instance for CreateIpTableList.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateIpTableListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateIpTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIpTableList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIpTableListResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancingResponse`

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


    def CreateLogSet(self, request):
        """本接口（CreateClsLog）用于创建CLS日志集。

        :param request: Request instance for CreateLogSet.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLogSetRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogSet", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogSetResponse()
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


    def CreateLogTopicTask(self, request):
        """本接口（CreateLogTopicTask）用于创建日志推送任务。

        :param request: Request instance for CreateLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogTopicTaskResponse()
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
        """创建源站组

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

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


    def CreateReplayTask(self, request):
        """创建刷新/预热重放任务

        :param request: Request instance for CreateReplayTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateReplayTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateReplayTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplayTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReplayTaskResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

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


    def CreateSecurityDropPage(self, request):
        """创建自定义拦截页面。

        :param request: Request instance for CreateSecurityDropPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityDropPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityDropPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityDropPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityDropPageResponse()
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


    def CreateSpeedTesting(self, request):
        """对用户指定的域名进行一次站点拨测

        :param request: Request instance for CreateSpeedTesting.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSpeedTestingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSpeedTestingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpeedTesting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSpeedTestingResponse()
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
        """用于用户接入新的站点。

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

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


    def DeleteAliasDomain(self, request):
        """删除别称域名。

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAliasDomainResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancingResponse`

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


    def DeleteLogTopicTask(self, request):
        """本接口（DeleteLogTopicTask）用于删除日志推送任务。

        :param request: Request instance for DeleteLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLogTopicTaskResponse()
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
        """删除源站组

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

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
        """删除站点。

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

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


    def DescribeAddableEntityList(self, request):
        """本接口（DescribeAddableEntityList）用于查询剩余可添加的日志推送实体列表。

        :param request: Request instance for DescribeAddableEntityList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAddableEntityListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAddableEntityListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddableEntityList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddableEntityListResponse()
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


    def DescribeAliasDomains(self, request):
        """查询别称域名信息列表。

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAliasDomainsResponse()
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


    def DescribeApplicationProxies(self, request):
        """查询应用代理列表。

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationProxiesResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

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


    def DescribeBotClientIpList(self, request):
        """本接口（DescribeBotClientIpList）用于查询Bot攻击客户端Ip信息列表。

        :param request: Request instance for DescribeBotClientIpList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotClientIpListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotClientIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotClientIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotClientIpListResponse()
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


    def DescribeBotData(self, request):
        """本接口（DescribeBotData）查询Bot攻击时序数据。

        :param request: Request instance for DescribeBotData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotDataResponse()
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


    def DescribeBotHitRuleDetail(self, request):
        """本接口（DescribeBotHitRuleDetail）用于查询Bot攻击命中规则详情信息。

        :param request: Request instance for DescribeBotHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotHitRuleDetailResponse()
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
        """本接口（DescribeBotLog）用于查询Bot攻击日志。

        :param request: Request instance for DescribeBotLog.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotLogResponse`

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
        """查询Bot托管规则

        :param request: Request instance for DescribeBotManagedRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotManagedRulesResponse`

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


    def DescribeBotTopData(self, request):
        """本接口（DescribeBotTopData）查询Bot攻击TopN数据。

        :param request: Request instance for DescribeBotTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotTopDataResponse()
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


    def DescribeClientRuleList(self, request):
        """本接口（DescribeClientRuleList）用于查询封禁客户端信息列表。

        :param request: Request instance for DescribeClientRuleList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeClientRuleListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeClientRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientRuleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientRuleListResponse()
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


    def DescribeContentQuota(self, request):
        """查询内容管理接口配额

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContentQuotaResponse()
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


    def DescribeDDoSAttackData(self, request):
        """本接口（DescribeDDoSAttackData）用于查询DDoS攻击时序数据。

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackDataResponse()
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


    def DescribeDDoSAttackEvent(self, request):
        """本接口（DescribeDDoSAttackEvent）用于查询DDoS攻击事件列表。

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackEventResponse()
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


    def DescribeDDoSAttackEventDetail(self, request):
        """本接口（DescribeDDoSAttackEventDetail）用于查询DDoS攻击事件详情。

        :param request: Request instance for DescribeDDoSAttackEventDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEventDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackEventDetailResponse()
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


    def DescribeDDoSAttackSourceEvent(self, request):
        """本接口（DescribeDDoSAttackSourceEvent）用于查询DDoS攻击源信息列表。

        :param request: Request instance for DescribeDDoSAttackSourceEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackSourceEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackSourceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackSourceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackSourceEventResponse()
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


    def DescribeDDoSAttackTopData(self, request):
        """本接口（DescribeDDoSAttackTopData）用于查询DDoS攻击Top数据。

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackTopDataResponse()
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


    def DescribeDDoSBlockList(self, request):
        """本接口（DescribeDDoSBlockList）用于查询DDoS封禁解封列表。

        :param request: Request instance for DescribeDDoSBlockList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSBlockListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSBlockListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSBlockList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSBlockListResponse()
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


    def DescribeDDoSMajorAttackEvent(self, request):
        """本接口（DescribeDDoSMajorAttackEvent）用于查询DDoS主攻击事件列表。

        :param request: Request instance for DescribeDDoSMajorAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSMajorAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSMajorAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSMajorAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSMajorAttackEventResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSPolicyResponse`

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


    def DescribeDefaultCertificates(self, request):
        """查询默认证书列表

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnsDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnsDataResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnssecResponse`

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


    def DescribeHostsSetting(self, request):
        """用于查询域名配置信息

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

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


    def DescribeIdentifications(self, request):
        """查询站点的验证信息。

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdentificationsResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancingResponse`

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


    def DescribeLogSets(self, request):
        """本接口（DescribeLogSets）用于获取日志集列表。

        :param request: Request instance for DescribeLogSets.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogSetsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogSetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogSets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogSetsResponse()
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


    def DescribeLogTopicTaskDetail(self, request):
        """本接口（DescribeLogTopicTaskDetail）用于获取日志推送任务详细信息。

        :param request: Request instance for DescribeLogTopicTaskDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTaskDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTopicTaskDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogTopicTaskDetailResponse()
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


    def DescribeLogTopicTasks(self, request):
        """本接口（DescribeLogTopicTasks）用于获取日志推送任务列表。

        :param request: Request instance for DescribeLogTopicTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTopicTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogTopicTasksResponse()
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
        """获取源站组列表

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

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


    def DescribeOverviewL7Data(self, request):
        """本接口（DescribeOverviewL7Data）用于查询七层监控类时序流量数据。

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

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


    def DescribeRateLimitIntelligenceRule(self, request):
        """查询速率限制智能客户端过滤学习出来的规则

        :param request: Request instance for DescribeRateLimitIntelligenceRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRateLimitIntelligenceRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRateLimitIntelligenceRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRateLimitIntelligenceRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRateLimitIntelligenceRuleResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

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


    def DescribeSecurityGroupManagedRules(self, request):
        """获取托管规则组

        :param request: Request instance for DescribeSecurityGroupManagedRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityGroupManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityGroupManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupManagedRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupManagedRulesResponse()
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
        """查询安全防护配置详情。请求参数中ZoneId+Entity或TemplateId至少填一项。

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyListResponse`

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


    def DescribeSecurityPolicyRegions(self, request):
        """查询所有地域信息

        :param request: Request instance for DescribeSecurityPolicyRegions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRegionsResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPortraitRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPortraitRulesResponse`

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


    def DescribeSecurityRuleId(self, request):
        """查询安全规则详情

        :param request: Request instance for DescribeSecurityRuleId.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityRuleIdRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityRuleIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityRuleId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityRuleIdResponse()
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


    def DescribeSingleL7AnalysisData(self, request):
        """本接口（DescribeSingleL7AnalysisData）用于查询七层数据分析类单值流量数据列表。

        :param request: Request instance for DescribeSingleL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSingleL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSingleL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSingleL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSingleL7AnalysisDataResponse()
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


    def DescribeSpeedTestingDetails(self, request):
        """用于查询拨测分地区数据

        :param request: Request instance for DescribeSpeedTestingDetails.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingDetailsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingDetails", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingDetailsResponse()
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


    def DescribeSpeedTestingMetricData(self, request):
        """查询站点拨测结果

        :param request: Request instance for DescribeSpeedTestingMetricData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingMetricDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingMetricData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingMetricDataResponse()
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


    def DescribeSpeedTestingQuota(self, request):
        """查询站点拨测配额

        :param request: Request instance for DescribeSpeedTestingQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingQuotaResponse()
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
        """本接口（DescribeTimingL4Data）用于查询四层时序流量数据列表。

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

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
        """本接口（DescribeTimingL7AnalysisData）查询七层数据分析类时序数据。

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

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
        """本接口（DescribeTimingL7CacheData）用于查询七层缓存分析时序类流量数据。

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

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
        """本接口（DescribeTopL7AnalysisData）用于查询七层流量前topN的数据。

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

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
        """本接口（DescribeTopL7CacheData）用于查询七层缓存分析topN流量数据。

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

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


    def DescribeWebManagedRulesData(self, request):
        """本接口（DescribeWebManagedRulesData）用于查询WAF攻击的时序数据。

        :param request: Request instance for DescribeWebManagedRulesData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesDataResponse`

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


    def DescribeWebManagedRulesHitRuleDetail(self, request):
        """本接口（DescribeWebManagedRulesHitRuleDetail）用于查询WAF攻击命中规则详情。

        :param request: Request instance for DescribeWebManagedRulesHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesHitRuleDetailResponse()
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
        """本接口（DescribeWebManagedRulesLog）用于查询Web攻击日志。

        :param request: Request instance for DescribeWebManagedRulesLog.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesLogResponse`

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


    def DescribeWebProtectionAttackEvents(self, request):
        """本接口（DescribeWebProtectionAttackEvents）用于查询CC相关攻击事件列表。

        :param request: Request instance for DescribeWebProtectionAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionAttackEventsResponse`

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


    def DescribeWebProtectionClientIpList(self, request):
        """本接口（DescribeWebProtectionClientIpList）用于查询CC防护客户端（攻击源）IP信息。

        :param request: Request instance for DescribeWebProtectionClientIpList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionClientIpListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionClientIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionClientIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionClientIpListResponse()
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
        """本接口（DescribeWebProtectionData）用于查询CC防护时序数据。

        :param request: Request instance for DescribeWebProtectionData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionDataResponse`

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


    def DescribeWebProtectionHitRuleDetail(self, request):
        """本接口（DescribeWebProtectionHitRuleDetail）用于查询CC防护命中规则详情列表。

        :param request: Request instance for DescribeWebProtectionHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionHitRuleDetailResponse()
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


    def DescribeWebProtectionTopData(self, request):
        """本接口（DescribeWebProtectionTopData）用于查询CC防护的Top数据。

        :param request: Request instance for DescribeWebProtectionTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionTopDataResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneDDoSPolicyResponse`

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


    def DescribeZoneSetting(self, request):
        """用于查询站点的所有配置信息。

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

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
        """用户查询用户站点信息列表，支持分页。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

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


    def DownloadL4Logs(self, request):
        """本接口（DownloadL4Logs）用于下载四层离线日志。

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadL4LogsResponse()
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
        """本接口（DownloadL7Logs）下载七层离线日志。

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

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
        """用于验证站点所有权。

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

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


    def ModifyAlarmConfig(self, request):
        """本接口（ModifyAlarmConfig）用于修改用户告警配置。

        :param request: Request instance for ModifyAlarmConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmConfigResponse()
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


    def ModifyAlarmDefaultThreshold(self, request):
        """此接口（ModifyAlarmDefaultThreshold）用于修改告警默认阈值。

        :param request: Request instance for ModifyAlarmDefaultThreshold.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmDefaultThresholdRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmDefaultThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmDefaultThreshold", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmDefaultThresholdResponse()
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


    def ModifyAliasDomain(self, request):
        """修改别称域名。

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAliasDomainResponse()
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


    def ModifyAliasDomainStatus(self, request):
        """修改别称域名状态。

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAliasDomainStatusResponse()
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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyHostRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyHostResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDefaultCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDefaultCertificateResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordResponse`

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
        """设置站点DNSSEC状态

        :param request: Request instance for ModifyDnssec.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnssecResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancingResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancingStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancingStatusResponse`

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


    def ModifyLogTopicTask(self, request):
        """本接口（ModifyLogTopicTask）用于修改日志推送任务信息。

        :param request: Request instance for ModifyLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogTopicTaskResponse()
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
        """修改源站组

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRulePriorityResponse`

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
        """修改Web&Bot安全配置。

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

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


    def ModifySecurityWafGroupPolicy(self, request):
        """修改安全配置托管规则

        :param request: Request instance for ModifySecurityWafGroupPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityWafGroupPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityWafGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityWafGroupPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityWafGroupPolicyResponse()
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
        """修改站点信息。

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

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
        """开启，关闭 CNAME 加速。

        :param request: Request instance for ModifyZoneCnameSpeedUp.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCnameSpeedUpRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCnameSpeedUpResponse`

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
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

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
        """用于开启，关闭站点。

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

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


    def ReclaimAliasDomain(self, request):
        """当客户取回站定的同时会取回此站点下关联的别称域名，此时入参为ZoneId；当客户接入站点发现已被别称域名接入时通过验证之后可取回域名，此时入参为ZoneName。

        :param request: Request instance for ReclaimAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ReclaimAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ReclaimAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReclaimAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReclaimAliasDomainResponse()
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
        """站点被其他用户接入后，验证了站点所有权之后，可以找回该站点。

        :param request: Request instance for ReclaimZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ReclaimZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ReclaimZoneResponse`

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


    def SwitchLogTopicTask(self, request):
        """本接口（SwitchLogTopicTask）用于开启/关闭推送任务。

        :param request: Request instance for SwitchLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.SwitchLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.SwitchLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchLogTopicTaskResponse()
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