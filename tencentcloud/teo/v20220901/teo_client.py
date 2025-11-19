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
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def ApplyFreeCertificate(self, request):
        r"""申请免费证书时，如果您需要通过使用 DNS 委派验证或者文件验证进行申请，您可以调用该接口来进行发起证书申请并根据申请方式来获取对应的验证内容。调用接口的顺序如下：
        第一步：调用 ApplyFreeCertificate，指定申请免费证书的校验方式，获取验证内容；
        第二步：为相应域名按照验证内容配置；
        第三步：调用CheckFreeCertificateVerification 验证，验证通过后即完成免费证书申请；
        第四步：调用ModifyHostsCertificate，下发域名证书为使用 EdgeOne 免费证书配置。

        申请方式的介绍可参考文档：[免费证书申请说明](https://cloud.tencent.com/document/product/1552/90437)
        说明：
        - 仅 CNAME 接入模式可调用该接口来指定免费证书申请方式。NS/DNSPod 托管接入模式都是使用自动验证来申请免费证书，无需调用该接口。
        - 如果您需要切换免费证书验证方式，您可以重新调用本接口通过修改 VerificationMethod 字段来进行变更。
        - 同个域名只能申请一本免费证书，在调用本接口后，后台会触发申请免费证书相关任务，您需要在2 天内，完成域名验证信息的相关配置，然后完成证书验证。

        :param request: Request instance for ApplyFreeCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ApplyFreeCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ApplyFreeCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFreeCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFreeCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSecurityTemplateToEntity(self, request):
        r"""操作安全策略模板，支持将域名绑定或换绑到指定的策略模板，或者从指定的策略模板解绑。

        :param request: Request instance for BindSecurityTemplateToEntity.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindSecurityTemplateToEntityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindSecurityTemplateToEntityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSecurityTemplateToEntity", params, headers=headers)
            response = json.loads(body)
            model = models.BindSecurityTemplateToEntityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSharedCNAME(self, request):
        r"""用于加速域名绑定或解绑共享 CNAME，该功能白名单内测中。

        :param request: Request instance for BindSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.BindSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindZoneToPlan(self, request):
        r"""将未绑定套餐的站点绑定到已有套餐

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            model = models.BindZoneToPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCnameStatus(self, request):
        r"""校验域名 CNAME 状态

        :param request: Request instance for CheckCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCnameStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCnameStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFreeCertificateVerification(self, request):
        r"""该接口用于验证免费证书并获取免费证书申请结果。如果验证通过，可通过该接口查询到对应域名申请的免费证书信息，如果申请失败，该接口将返回对应的验证失败信息。
        在触发[申请免费证书接口](https://cloud.tencent.com/document/product/1552/90437)后，您可以通过本接口检查免费证书申请结果。在免费证书申请成功后， 还需要通过[配置域名证书](https://cloud.tencent.com/document/product/1552/80764)接口配置，才能将免费证书部署至加速域上。

        :param request: Request instance for CheckFreeCertificateVerification.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckFreeCertificateVerificationRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckFreeCertificateVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFreeCertificateVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFreeCertificateVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmMultiPathGatewayOriginACL(self, request):
        r"""本接口用于多通道安全加速网关回源 IP 网段发生变更时，确认已将最新回源 IP 网段更新至源站防火墙。

        :param request: Request instance for ConfirmMultiPathGatewayOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.ConfirmMultiPathGatewayOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ConfirmMultiPathGatewayOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmMultiPathGatewayOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmMultiPathGatewayOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmOriginACLUpdate(self, request):
        r"""本接口用于回源 IP 网段发生变更时，确认已将最新回源 IP 网段更新至源站防火墙。确认已更新至最新的回源 IP 网段后，相关变更通知将会停止推送。

        :param request: Request instance for ConfirmOriginACLUpdate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ConfirmOriginACLUpdateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ConfirmOriginACLUpdateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmOriginACLUpdate", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmOriginACLUpdateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccelerationDomain(self, request):
        r"""在创建完站点之后，您可以通过本接口创建加速域名。

        CNAME 模式接入时，若您未完成站点归属权校验，本接口将为您返回域名归属权验证信息，您可以单独对域名进行归属权验证，详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

        :param request: Request instance for CreateAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAliasDomain(self, request):
        r"""创建别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxy(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版 [创建四层代理实例](https://cloud.tencent.com/document/product/1552/103417) 。

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxyRule(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [创建四层代理转发规则
        ](https://cloud.tencent.com/document/product/1552/103416) 。

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCLSIndex(self, request):
        r"""针对指定实时日志投递任务（task-id），在对应的腾讯云 CLS 日志主题中创建投递日志字段对应的键值索引。如果您在腾讯云 CLS 已经创建索引，本接口将采用合并的方式追加索引。

        :param request: Request instance for CreateCLSIndex.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCLSIndexRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCLSIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigGroupVersion(self, request):
        r"""在版本管理模式下，用于创建指定配置组的新版本。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for CreateConfigGroupVersion.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateConfigGroupVersionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateConfigGroupVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigGroupVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigGroupVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContentIdentifier(self, request):
        r"""创建内容标识符，可以设置描述、标签等信息，同时需要绑定企业版套餐用于统计计费数据；一个内容标识符只能绑定一个计费套餐，一个计费套餐可以绑定多个内容标识符。该功能仅限白名单开放。

        :param request: Request instance for CreateContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomizeErrorPage(self, request):
        r"""创建自定义错误页面。

        :param request: Request instance for CreateCustomizeErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCustomizeErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCustomizeErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomizeErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomizeErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDnsRecord(self, request):
        r"""在创建完站点后，并且站点为 NS 模式接入时，您可以通过本接口创建 DNS 记录。

        :param request: Request instance for CreateDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDnsRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDnsRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunction(self, request):
        r"""创建并部署边缘函数至 EdgeOne 的边缘节点。

        :param request: Request instance for CreateFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunctionRule(self, request):
        r"""创建边缘函数的触发规则。支持通过自定义过滤条件来决定是否需要执行函数，当需要执行函数时，提供了多种选择目标函数的方式，包括：直接指定，基于客户端归属地区选择和基于权重选择。

        :param request: Request instance for CreateFunctionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunctionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJustInTimeTranscodeTemplate(self, request):
        r"""即时转码已经提供了预置转码模板，满足大部分的需求。如果有个性化的转码需求，可以通过本接口创建自定义的转码模板，最多可创建100个自定义转码模板。
        为了确保即时转码效果的一致性，避免因 EO 缓存或 M3U8 分片处理过程中的模板变更导致视频输出异常，模板在创建后不可进行修改。
        即时转码详细能力了解：[EdgeOne视频即时处理功能介绍](https://cloud.tencent.com/document/product/1552/111927)。

        :param request: Request instance for CreateJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL4Proxy(self, request):
        r"""用于创建四层代理实例。

        :param request: Request instance for CreateL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL4ProxyRules(self, request):
        r"""用于创建四层代理实例规则，支持单条或者批量创建。

        :param request: Request instance for CreateL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL7AccRules(self, request):
        r"""本接口用于在[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中创建规则，支持批量创建。

        :param request: Request instance for CreateL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        r"""创建负载均衡实例。详情请参考 [快速创建负载均衡实例](https://cloud.tencent.com/document/product/1552/104223)。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGateway(self, request):
        r"""通过本接口创建多通道安全加速网关，包括云上网关（腾讯云创建和管理的网关）和自有网关（用户部署的私有网关），需要通过接口 DescribeMultiPathGateway，查询状态为 online 即创建成功。

        :param request: Request instance for CreateMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGatewayLine(self, request):
        r"""通过本接口创建接入多通道安全加速网关的线路。包括 EdgeOne 四层代理线路、自定义线路。

        :param request: Request instance for CreateMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGatewaySecretKey(self, request):
        r"""通过本接口创建接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关。每个站点下只有一个密钥，可用于接入该站点下的所有网关，可通过接口 DescribeMultiPathGatewaySecretKey 查询。

        :param request: Request instance for CreateMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOriginGroup(self, request):
        r"""创建源站组，以源站组的方式管理业务源站。此处配置的源站组可于**添加加速域名**和**四层代理**等功能中引用。

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlan(self, request):
        r"""若您需要使用 Edgeone 产品，您需要通过此接口创建计费套餐。
        > 创建套餐后，您需要通过 [CreateZone](https://cloud.tencent.com/document/product/1552/80719) 完成创建站点，绑定套餐的流程，Edgeone 才能正常提供服务。

        :param request: Request instance for CreatePlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlanForZone(self, request):
        r"""为未购买套餐的站点购买套餐

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanForZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrefetchTask(self, request):
        r"""创建预热任务

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrefetchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePurgeTask(self, request):
        r"""当源站资源更新，但节点缓存 TTL 未过期时，用户仍会访问到旧的资源，此时可以通过该接口实现节点资源更新。触发更新的方法有以下两种：<li>直接删除：不做任何校验，直接删除节点缓存，用户请求时触发回源拉取；</li><li>标记过期：将节点资源置为过期，用户请求时触发回源校验，即发送带有 If-None-Match 和 If-Modified-Since 头部的 HTTP 条件请求。若源站响应 200，则节点会回源拉取新的资源并更新缓存；若源站响应 304，则节点不会更新缓存；</li>

        清除缓存任务详情请查看[清除缓存](https://cloud.tencent.com/document/product/1552/70759)。

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePurgeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRealtimeLogDeliveryTask(self, request):
        r"""本接口用于创建实时日志投递任务。本接口有如下限制：
        - 当数据投递类型（LogType）为站点加速日志（七层访问日志）、四层代理日志、边缘函数运行日志时，同一个实体（七层域名、四层代理实例、边缘函数实例）在同种数据投递类型（LogType）和数据投递区域（Area）的组合下，只能被添加到如下实时日志投递任务类型（TaskType）组合中：
            - 一个推送至腾讯云  CLS 的任务，加上另一个推送至自定义 HTTP(S) 地址的任务；
            - 一个推送至腾讯云  CLS 的任务，加上另一个推送至 AWS S3 兼容对象存储的任务；
        - 当数据投递类型（LogType）为速率限制和 CC 攻击防护日志、托管规则日志、自定义规则日志、Bot 管理日志时，同一个实体在同种数据投递类型（LogType）和数据投递区域（Area）的组合下，只能被添加到一个实时日志投递任务中。
        - 当实时日志投递任务类型（TaskType）为 EdgeOne 日志分析（log_analysis）时，只支持数据投递类型（LogType）为站点加速日志（domain）；在同一站点（ZoneId）和数据投递区域（Area）的组合下，只能添加一个推送至 EdgeOne 日志分析的实时日志投递任务；。

        建议先通过 [DescribeRealtimeLogDeliveryTasks](https://cloud.tencent.com/document/product/1552/104110)  接口根据实体查询实时日志投递任务列表，检查实体是否已经被添加到另一实时日志投递任务中。

        :param request: Request instance for CreateRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        r"""本接口为旧版本创建规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本创建七层加速规则接口详情请参考 [CreateL7AccRules](https://cloud.tencent.com/document/product/1552/115822)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

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


    def CreateSecurityAPIResource(self, request):
        r"""用于创建 API 资源。

        :param request: Request instance for CreateSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityAPIService(self, request):
        r"""用于创建 API 服务。

        :param request: Request instance for CreateSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityClientAttester(self, request):
        r"""创建客户端认证选项。

        :param request: Request instance for CreateSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityIPGroup(self, request):
        r"""创建安全 IP 组

        :param request: Request instance for CreateSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityJSInjectionRule(self, request):
        r"""创建 JavaScript 注入规则。

        :param request: Request instance for CreateSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSharedCNAME(self, request):
        r"""用于创建共享 CNAME，该功能白名单内测中。

        :param request: Request instance for CreateSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebSecurityTemplate(self, request):
        r"""创建安全策略配置模板

        :param request: Request instance for CreateWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateZone(self, request):
        r"""EdgeOne 为您提供 CNAME、NS 和无域名接入三种接入方式，您需要先通过此接口完成站点创建。CNAME 和 NS 接入站点的场景可参考 [从零开始快速接入 EdgeOne](https://cloud.tencent.com/document/product/1552/87601); 无域名接入的场景可参考 [快速启用四层代理服务](https://cloud.tencent.com/document/product/1552/96051)。

        > 建议您在账号下已存在套餐时调用本接口创建站点，请在入参时传入 PlanId ，直接将站点绑定至该套餐；不传入 PlanId 时，创建出来的站点会处于未激活状态，无法正常服务，您需要通过 [BindZoneToPlan](https://cloud.tencent.com/document/product/1552/83042) 完成套餐绑定之后，站点才可正常提供服务 。若您当前没有可绑定的套餐时，请前往控制台购买套餐完成站点创建。

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerationDomains(self, request):
        r"""批量删除加速域名

        :param request: Request instance for DeleteAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAliasDomain(self, request):
        r"""删除别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxy(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [删除四层代理实例
        ](https://cloud.tencent.com/document/product/1552/103415) 。

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxyRule(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [删除四层代理转发规则](https://cloud.tencent.com/document/product/1552/103414) 。

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContentIdentifier(self, request):
        r"""删除指定的内容标识符。该功能仅白名单开放。

        :param request: Request instance for DeleteContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomErrorPage(self, request):
        r"""删除自定义错误页面。

        :param request: Request instance for DeleteCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDnsRecords(self, request):
        r"""您可以用本接口批量删除 DNS 记录。

        :param request: Request instance for DeleteDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunction(self, request):
        r"""删除边缘函数，删除后函数无法恢复，关联的触发规则会一并删除。

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunctionRules(self, request):
        r"""删除边缘函数触发规则。

        :param request: Request instance for DeleteFunctionRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunctionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJustInTimeTranscodeTemplates(self, request):
        r"""根据站点 id 下唯一的模板标识，删除相应的即时转码模板。

        :param request: Request instance for DeleteJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL4Proxy(self, request):
        r"""用于删除四层代理实例。

        :param request: Request instance for DeleteL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL4ProxyRules(self, request):
        r"""用于删除四层代理转发规则，支持单条或者批量操作。

        :param request: Request instance for DeleteL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL7AccRules(self, request):
        r"""本接口用于删除[规则引擎](https://cloud.tencent.com/document/product/1552/70901)的规则，支持批量删除。

        :param request: Request instance for DeleteL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancer(self, request):
        r"""删除负载均衡实例，若负载均衡示例被其他服务（例如：四层代理等）引用的时候，示例无法被删除，需要先解除引用关系。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultiPathGateway(self, request):
        r"""通过本接口删除多通道安全加速网关，包括自有网关和云上网关。

        :param request: Request instance for DeleteMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultiPathGatewayLine(self, request):
        r"""通过本接口删除接入多通道安全加速网关的线路，仅自定义线路支持删除。

        :param request: Request instance for DeleteMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOriginGroup(self, request):
        r"""删除源站组，若源站组仍然被服务（例如：四层代理，域名服务，负载均衡，规则引起）引用，将不允许删除。

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRealtimeLogDeliveryTask(self, request):
        r"""通过本接口删除实时日志投递任务。

        :param request: Request instance for DeleteRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        r"""本接口为旧版本删除规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本删除七层加速规则接口详情请参考 [DeleteL7AccRules](https://cloud.tencent.com/document/product/1552/115821)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityAPIResource(self, request):
        r"""用于删除 API 资源。

        :param request: Request instance for DeleteSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityAPIService(self, request):
        r"""用于删除 API 服务。

        :param request: Request instance for DeleteSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityClientAttester(self, request):
        r"""删除客户端认证选项。

        :param request: Request instance for DeleteSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityIPGroup(self, request):
        r"""删除指定 IP 组，如果有规则引用了 IP 组情况，则不允许删除。

        :param request: Request instance for DeleteSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityJSInjectionRule(self, request):
        r"""删除 JavaScript 注入规则。

        :param request: Request instance for DeleteSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSharedCNAME(self, request):
        r"""用于删除共享 CNAME，该功能白名单内测中。

        :param request: Request instance for DeleteSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebSecurityTemplate(self, request):
        r"""删除安全策略配置模板

        :param request: Request instance for DeleteWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteZone(self, request):
        r"""删除站点。

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployConfigGroupVersion(self, request):
        r"""在版本管理模式下，用于版本发布，可通过 EnvId 将版本发布至测试环境或生产环境。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for DeployConfigGroupVersion.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeployConfigGroupVersionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeployConfigGroupVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployConfigGroupVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeployConfigGroupVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerationDomains(self, request):
        r"""您可以通过本接口查看站点下的域名信息，包括加速域名、源站以及域名状态等信息。您可以查看站点下全部域名的信息，也可以指定过滤条件查询对应的域名信息。

        :param request: Request instance for DescribeAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAliasDomains(self, request):
        r"""查询别称域名信息列表。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAliasDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProxies(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，新版接口中将四层代理实例列表的查询和四层转发规则的查询拆分成两个接口，详情请参考 [查询四层代理实例列表](https://cloud.tencent.com/document/product/1552/103413) 和 [查询四层代理转发规则列表](https://cloud.tencent.com/document/product/1552/103412)。

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailablePlans(self, request):
        r"""查询当前账户可用套餐信息列表

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailablePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingData(self, request):
        r"""通过本接口查询计费数据。

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBillingDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigGroupVersionDetail(self, request):
        r"""在版本管理模式下，用于获取版本的详细信息，包括版本 ID、描述、状态、创建时间、所属配置组信息以及版本配置文件的内容。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for DescribeConfigGroupVersionDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigGroupVersionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigGroupVersionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigGroupVersions(self, request):
        r"""在版本管理模式下，用于查询指定配置组的版本列表。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for DescribeConfigGroupVersions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigGroupVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigGroupVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentIdentifiers(self, request):
        r"""批量查询内容标识符，可以根据 ID、描述、状态或者标签过滤。按照状态查询被删除的内容标识符仅保留三个月。该功能仅白名单开放。

        :param request: Request instance for DescribeContentIdentifiers.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentIdentifiersRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentIdentifiersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentIdentifiers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentIdentifiersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentQuota(self, request):
        r"""查询内容管理接口配额

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomErrorPages(self, request):
        r"""查询自定义错误页列表。

        :param request: Request instance for DescribeCustomErrorPages.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeCustomErrorPagesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeCustomErrorPagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomErrorPages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomErrorPagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackData(self, request):
        r"""本接口（DescribeDDoSAttackData）用于查询DDoS攻击时序数据。

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackEvent(self, request):
        r"""本接口（DescribeDDoSAttackEvent）用于查询DDoS攻击事件列表。

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackTopData(self, request):
        r"""本接口（DescribeDDoSAttackTopData）用于查询DDoS攻击Top数据。

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSProtection(self, request):
        r"""获取站点的独立 DDoS 防护信息。

        :param request: Request instance for DescribeDDoSProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultCertificates(self, request):
        r"""查询默认证书列表

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployHistory(self, request):
        r"""在版本管理模式下，用于查询生产/测试环境的版本发布历史。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for DescribeDeployHistory.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDeployHistoryRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDeployHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeployHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDnsRecords(self, request):
        r"""您可以用过本接口查看站点下的 DNS 记录信息，包括 DNS 记录名、记录类型以及记录内容等信息，支持指定过滤条件查询对应的 DNS 记录信息。

        :param request: Request instance for DescribeDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        r"""在版本管理模式下，用于查询环境信息，可获取环境 ID、类型、当前生效版本等。版本管理功能内测中，当前仅白名单开放。

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionRules(self, request):
        r"""查询边缘函数触发规则列表，支持按照规则 ID、函数 ID、规则描述等条件进行过滤。

        :param request: Request instance for DescribeFunctionRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionRuntimeEnvironment(self, request):
        r"""查询边缘函数运行环境，包括环境变量。

        :param request: Request instance for DescribeFunctionRuntimeEnvironment.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRuntimeEnvironmentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRuntimeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionRuntimeEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionRuntimeEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctions(self, request):
        r"""查询边缘函数列表，支持函数 ID、函数名称、描述等条件的过滤。

        :param request: Request instance for DescribeFunctions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostsSetting(self, request):
        r"""本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，可通过 [DescribeL7AccSetting](https://cloud.tencent.com/document/product/1552/115819) 和 [DescribeL7AccRules](https://cloud.tencent.com/document/product/1552/115820) 来获取域名的详细配置。

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPRegion(self, request):
        r"""该接口可用于查询 IP 是否为 EdgeOne IP。

        :param request: Request instance for DescribeIPRegion.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIPRegionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIPRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentifications(self, request):
        r"""查询站点的验证信息。

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentificationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJustInTimeTranscodeTemplates(self, request):
        r"""根据即时转码模板名字、模板类型或唯一标识，获取即时转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及预置模板。

        :param request: Request instance for DescribeJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL4Proxy(self, request):
        r"""用于查询四层代理实例列表。

        :param request: Request instance for DescribeL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL4ProxyRules(self, request):
        r"""查询四层代理实例下的转发规则列表。

        :param request: Request instance for DescribeL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL7AccRules(self, request):
        r"""本接口用于查询[规则引擎](https://cloud.tencent.com/document/product/1552/70901)的规则列表。

        :param request: Request instance for DescribeL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL7AccSetting(self, request):
        r"""本接口用于查询[站点加速](https://cloud.tencent.com/document/product/1552/96193)全局配置。

        :param request: Request instance for DescribeL7AccSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7AccSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL7AccSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerList(self, request):
        r"""查询负载均衡实例列表。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。

        :param request: Request instance for DescribeLoadBalancerList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancerListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGateway(self, request):
        r"""通过本接口查询多通道安全加速网关详情。如名称、网关 ID、IP、端口、类型等。

        :param request: Request instance for DescribeMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayLine(self, request):
        r"""通过本接口查询接入多通道安全加速网关的线路。包括直连、EdgeOne 四层代理线路、自定义线路。

        :param request: Request instance for DescribeMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayOriginACL(self, request):
        r"""本接口用于查询多通道安全加速网关实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。若 MultiPathGatewayNextOriginACL 字段有返回值，则需要将最新的回源 IP 网段同步到源站防火墙配置中。

        :param request: Request instance for DescribeMultiPathGatewayOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayRegions(self, request):
        r"""通过本接口查询用户创建的多通道安全加速网关（云上网关）的可用地域列表。

        :param request: Request instance for DescribeMultiPathGatewayRegions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewaySecretKey(self, request):
        r"""通过本接口查询接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关。

        :param request: Request instance for DescribeMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGateways(self, request):
        r"""通过本接口查询用户创建的多通道安全加速网关列表。支持翻页。

        :param request: Request instance for DescribeMultiPathGateways.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaysRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginACL(self, request):
        r"""本接口用于查询站点下的七层加速域名/四层代理实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。如果您想通过自动化脚本定期获取回源 IP 网段的最新版本，可以较低频率（建议每三天一次）轮询本接口，若 NextOriginACL 字段有返回值，则将最新的回源 IP 网段同步到源站防火墙配置中。

        :param request: Request instance for DescribeOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroup(self, request):
        r"""获取源站组列表

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroupHealthStatus(self, request):
        r"""查询负载均衡实例下源站组健康状态。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。

        :param request: Request instance for DescribeOriginGroupHealthStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupHealthStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroupHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginProtection(self, request):
        r"""本接口为旧版本查询源站防护接口，EdgeOne 于 2025 年 6 月 27 日已对源站防护相关接口全面升级，新版本查询源站防护接口详情请参考 [DescribeOriginACL](https://cloud.tencent.com/document/product/1552/120408)。

        <p style="color: red;">注意：自 2025 年 6 月 27 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版源站防护接口。</p>

        :param request: Request instance for DescribeOriginProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewL7Data(self, request):
        r"""本接口（DescribeOverviewL7Data）用于查询七层监控类时序流量数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80648">DescribeTimingL7AnalysisData</a> 接口。

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewL7DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlans(self, request):
        r"""查询套餐信息列表，支持分页。

        :param request: Request instance for DescribePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrefetchTasks(self, request):
        r"""DescribePrefetchTasks 用于查询预热任务提交历史记录及执行进度，通过 CreatePrefetchTasks 接口提交的任务可通过此接口进行查询。

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrefetchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        r"""DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 CreatePurgeTasks 接口提交的任务均可通过此接口进行查询。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealtimeLogDeliveryTasks(self, request):
        r"""通过本接口查询实时日志投递任务列表。

        :param request: Request instance for DescribeRealtimeLogDeliveryTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRealtimeLogDeliveryTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRealtimeLogDeliveryTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealtimeLogDeliveryTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealtimeLogDeliveryTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        r"""本接口为旧版本查询规则引擎规则接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本查询七层加速规则接口详情请参考  [DescribeL7AccRules](https://cloud.tencent.com/document/product/1552/115820)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

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


    def DescribeRulesSetting(self, request):
        r"""本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [RuleEngineAction](https://cloud.tencent.com/document/product/1552/80721#RuleEngineAction)。

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAPIResource(self, request):
        r"""查询站点下的 API 资源。

        :param request: Request instance for DescribeSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAPIService(self, request):
        r"""查询站点下的 API 服务。

        :param request: Request instance for DescribeSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityClientAttester(self, request):
        r"""查询客户端认证选项配置。

        :param request: Request instance for DescribeSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroup(self, request):
        r"""查询安全 IP 组的配置信息，包括安全 IP 组的 ID、名称和内容。本接口的查询结果中，每个 IP 组最多只返回 2000 个 IP / 网段。如果存在超过 2000 个 IP / 网段的超大 IP 组，请调用 DescribeSecurityIPGroupContent 进行分页查询。

        :param request: Request instance for DescribeSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroupContent(self, request):
        r"""该接口用于分页查询指定 IP 组中的 IP 地址列表。当 IP 组中的 IP 地址数量超过 2000 个时，可以使用此接口进行分页查询，以获取完整的 IP 地址列表。

        :param request: Request instance for DescribeSecurityIPGroupContent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupContentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroupContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroupInfo(self, request):
        r"""接口已废弃，将于 2024 年 6 月 30 日停止服务。请使用 [查询安全 IP 组
        ](https://cloud.tencent.com/document/product/1552/105866) 接口。

        查询 IP 组的配置信息，包括 IP 组名称、 IP 组内容、 IP 组归属站点。

        :param request: Request instance for DescribeSecurityIPGroupInfo.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupInfoRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityJSInjectionRule(self, request):
        r"""查询 JavaScript 注入规则。

        :param request: Request instance for DescribeSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicy(self, request):
        r"""查询安全防护配置详情。

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTemplateBindings(self, request):
        r"""查询指定策略模板的绑定关系列表。

        :param request: Request instance for DescribeSecurityTemplateBindings.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTemplateBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTemplateBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL4Data(self, request):
        r"""本接口（DescribeTimingL4Data）用于查询四层时序流量数据列表。

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL4DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7AnalysisData(self, request):
        r"""本接口用于查询七层域名业务的时序数据。
        注意：
        1. 本接口查询数据有 10 分钟左右延迟，建议拉取当前时间 10 分钟以前的数据。
        2. 本接口默认返回防护后的流量请求数据，用户可在 `Filters.mitigatedByWebSecurity` 中自定义查询已防护缓释的数据。

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7CacheData(self, request):
        r"""本接口用于查询七层缓存分析时序类流量数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80648">DescribeTimingL7AnalysisData</a> 接口。

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7OriginPullData(self, request):
        r"""本接口用以查询七层域名业务的回源时序数据。

        :param request: Request instance for DescribeTimingL7OriginPullData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7OriginPullDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7OriginPullDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7OriginPullData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7OriginPullDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7AnalysisData(self, request):
        r"""本接口用于查询七层域名业务按照指定维度的 topN 数据。
        注意：
        1. 本接口查询数据有 10 分钟左右延迟，建议拉取当前时间 10 分钟以前的数据。
        2. 本接口默认返回防护后的流量请求数据，用户可在 `Filters.mitigatedByWebSecurity` 中自定义查询已防护缓释的数据。

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7CacheData(self, request):
        r"""本接口用于查询七层缓存分析 topN 数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80646"> DescribeTopL7AnalysisData</a> 接口。

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebSecurityTemplate(self, request):
        r"""查询安全策略配置模板详情

        :param request: Request instance for DescribeWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebSecurityTemplates(self, request):
        r"""查询安全策略配置模板列表

        :param request: Request instance for DescribeWebSecurityTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebSecurityTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebSecurityTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneConfigImportResult(self, request):
        r"""查询站点配置项导入结果接口，本接口用于站点配置导入接口（ImportZoneConfig）的结果查询。该功能仅支持标准版或企业版套餐的站点使用。

        :param request: Request instance for DescribeZoneConfigImportResult.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneConfigImportResultRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneConfigImportResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneConfigImportResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneConfigImportResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneSetting(self, request):
        r"""本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [DescribeL7AccSetting](https://cloud.tencent.com/document/product/1552/115819)。

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""该接口用于查询您有权限的站点信息。可根据不同查询条件筛选站点。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPlan(self, request):
        r"""当您需要停止 Edgeone 套餐的计费，可以通过该接口销毁计费套餐。
        > 销毁计费套餐需要满足以下条件：
            1.套餐已过期（企业版套餐除外）；
            2.套餐下所有站点均已关闭或删除。

        > 站点状态可以通过 [查询站点列表](https://cloud.tencent.com/document/product/1552/80713) 接口进行查询
        停用站点可以通过 [切换站点状态](https://cloud.tencent.com/document/product/1552/80707) 接口将站点切换至关闭状态
        删除站点可以通过 [删除站点](https://cloud.tencent.com/document/product/1552/80717) 接口将站点删除

        :param request: Request instance for DestroyPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.DestroyPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DestroyPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableOriginACL(self, request):
        r"""本接口用于关闭站点的源站防护功能。停用后，相关资源不再仅使用「源站防护」提供的回源 IP 网段请求您的源站，同时停止发送回源 IP 网段更新通知。

        :param request: Request instance for DisableOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DisableOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DisableOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DisableOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL4Logs(self, request):
        r"""本接口（DownloadL4Logs）用于下载四层离线日志。

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL4LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL7Logs(self, request):
        r"""本接口（DownloadL7Logs）下载七层离线日志。

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL7LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableOriginACL(self, request):
        r"""本接口用于站点首次开启源站防护，启用后 EdgeOne 将会使用特定的回源 IP 网段为七层加速域名/四层代理实例回源。单次支持提交的七层加速域名的数量最大为 200，四层代理实例的数量最大为 100，支持七层加速域名/四层代理实例混合提交，总实例个数最大为 200。如需要启用超过 200 个资源，可先通过指定资源的方式以最大数量启用，剩余资源通过 ModifyOriginACL 接口启用。后续新增七层加速域名/四层代理实例均请通过 ModifyOriginACL 接口配置。

        注意：
        - 调用本接口视为同意 [源站防护启用特别约定](https://cloud.tencent.com/document/product/1552/120141)；
        - 回源 IP 网段会不定期变更，EdgeOne 将在回源 IP 网段变更前 14 天、前 7 天、前 3 天和前 1 天分别通过站内信、短信、邮件等一种或多种方式发起通知，为了能正常收到回源 IP 网段的变更通知，请务必确保您在 [腾讯云消息中心控制台](https://console.cloud.tencent.com/message)内，已勾选边缘安全加速平台 EO 的产品服务相关消息通知，并配置正确的消息接收人。配置方式请参考 [消息订阅管理](https://cloud.tencent.com/document/product/567/43476)。

        :param request: Request instance for EnableOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.EnableOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EnableOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.EnableOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportZoneConfig(self, request):
        r"""导出站点配置接口，本接口支持用户根据需要的配置项进行配置导出，导出的配置用于导入站点配置接口（ImportZoneConfig）进行配置导入。该功能仅支持标准版和企业版套餐站点使用。

        :param request: Request instance for ExportZoneConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ExportZoneConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ExportZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ExportZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleFunctionRuntimeEnvironment(self, request):
        r"""操作边缘函数运行环境，支持环境变量的相关设置。
        设置环境变量后，可在函数代码中使用，具体参考 [边缘函数引入环境变量](https://cloud.tencent.com/document/product/1552/109151#0151fd9a-8b0e-407b-ae37-54553a60ded6)。

        :param request: Request instance for HandleFunctionRuntimeEnvironment.
        :type request: :class:`tencentcloud.teo.v20220901.models.HandleFunctionRuntimeEnvironmentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.HandleFunctionRuntimeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleFunctionRuntimeEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.HandleFunctionRuntimeEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdentifyZone(self, request):
        r"""用于验证站点所有权。

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.IdentifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportZoneConfig(self, request):
        r"""导入站点配置接口，本接口支持站点配置文件的快速导入，发起导入后接口会返回对应的任务 ID（TaskId），用户需通过查询站点配置导入结果接口（DescribeZoneConfigImportResult）获取本次导入任务执行的结果。该功能仅支持标准版和企业版套餐站点使用。

        :param request: Request instance for ImportZoneConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ImportZoneConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ImportZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ImportZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IncreasePlanQuota(self, request):
        r"""当您的套餐绑定的站点数，或配置的 Web 防护 - 自定义规则 - 精准匹配策略的规则数，或 Web 防护 - 速率限制 - 精准速率限制模块的规则数达到套餐允许的配额上限，可以通过该接口增购对应配额。
        > 该接口该仅支持企业版套餐。

        :param request: Request instance for IncreasePlanQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.IncreasePlanQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IncreasePlanQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IncreasePlanQuota", params, headers=headers)
            response = json.loads(body)
            model = models.IncreasePlanQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomain(self, request):
        r"""修改加速域名信息

        :param request: Request instance for ModifyAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomainStatuses(self, request):
        r"""批量修改加速域名状态

        :param request: Request instance for ModifyAccelerationDomainStatuses.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomainStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomain(self, request):
        r"""修改别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomainStatus(self, request):
        r"""修改别称域名状态。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxy(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理实例
        ](https://cloud.tencent.com/document/product/1552/103411) 。

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRule(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理转发规则
        ](https://cloud.tencent.com/document/product/1552/103410) 。

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRuleStatus(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理转发规则状态
        ](https://cloud.tencent.com/document/product/1552/103409) 。

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyStatus(self, request):
        r"""本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理实例状态](https://cloud.tencent.com/document/product/1552/103408) 。

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContentIdentifier(self, request):
        r"""修改内容标识符，仅支持修改描述。该功能仅白名单开放。

        :param request: Request instance for ModifyContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomErrorPage(self, request):
        r"""修改自定义错误页面。

        :param request: Request instance for ModifyCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSProtection(self, request):
        r"""修改站点的独立 DDoS 防护。

        :param request: Request instance for ModifyDDoSProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnsRecords(self, request):
        r"""您可以通过本接口批量修改 DNS 记录。

        :param request: Request instance for ModifyDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnsRecordsStatus(self, request):
        r"""您可以通过本接口批量修改 DNS 记录的状态，批量对记录进行开启和停用。

        :param request: Request instance for ModifyDnsRecordsStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecordsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnsRecordsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunction(self, request):
        r"""修改边缘函数，支持修改函数的内容及描述信息，修改且重新部署后，函数立刻生效。

        :param request: Request instance for ModifyFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionRule(self, request):
        r"""修改边缘函数触发规则，支持修改规则条件、执行函数以及描述信息。您可以先通过 DescribeFunctionRules 接口来获取需要修改的规则的 RuleId，然后传入修改后的规则内容，原规则内容会被覆盖式更新。

        :param request: Request instance for ModifyFunctionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionRulePriority(self, request):
        r"""修改边缘函数触发规则的优先级。

        :param request: Request instance for ModifyFunctionRulePriority.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionRulePriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionRulePriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostsCertificate(self, request):
        r"""完成域名创建之后，您可以为域名配置自有证书，也可以使用 EdgeOne 为您提供的 [免费证书](https://cloud.tencent.com/document/product/1552/90437)。
        如果您需要配置自有证书，请先将证书上传至 [SSL证书控制台](https://console.cloud.tencent.com/certoverview)，然后在本接口中传入对应的证书 ID。详情参考 [部署自有证书至 EdgeOne 域名
        ](https://cloud.tencent.com/document/product/1552/88874)。

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostsCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4Proxy(self, request):
        r"""用于修改四层代理实例的配置。

        :param request: Request instance for ModifyL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyRules(self, request):
        r"""用于修改四层代理转发规则，支持单条或者批量修改。

        :param request: Request instance for ModifyL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyRulesStatus(self, request):
        r"""用于启用/停用四层代理转发规则状态，支持单条或者批量操作。

        :param request: Request instance for ModifyL4ProxyRulesStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyRulesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyRulesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyStatus(self, request):
        r"""用于启用/停用四层代理实例。

        :param request: Request instance for ModifyL4ProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccRule(self, request):
        r"""本接口用于修改[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中的规则，单次仅支持修改单条规则。

        :param request: Request instance for ModifyL7AccRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccRulePriority(self, request):
        r"""本接口用于修改[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中规则列表的优先级，本接口需要传入站点 ID 下完整的规则 ID 列表，规则 ID 列表可以通过[查询七层加速规则](https://cloud.tencent.com/document/product/1552/115820)接口获取，最终优先级顺序将调整成规则 ID 列表的顺序，从前往后执行。

        :param request: Request instance for ModifyL7AccRulePriority.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccRulePriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccRulePriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccSetting(self, request):
        r"""本接口用于修改[站点加速](https://cloud.tencent.com/document/product/1552/96193)全局配置。

        :param request: Request instance for ModifyL7AccSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancer(self, request):
        r"""修改负载均衡实例配置。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。

        :param request: Request instance for ModifyLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGateway(self, request):
        r"""通过本接口修改多通道安全加速网关信息，如名称、网关 ID、IP、端口等。

        :param request: Request instance for ModifyMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewayLine(self, request):
        r"""通过本接口修改接入多通道安全加速网关的线路，包括 EdgeOne 四层代理线路、自定义线路。

        :param request: Request instance for ModifyMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewaySecretKey(self, request):
        r"""通过本接口修改接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关，修改后原密钥失效。

        :param request: Request instance for ModifyMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewayStatus(self, request):
        r"""更新多通道安全网关状态。

        :param request: Request instance for ModifyMultiPathGatewayStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewayStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginACL(self, request):
        r"""本接口用于对七层加速域名/四层代理实例启用/关闭特定回源 IP 网段回源。单次支持提交的七层加速域名的数量最大为 200，四层代理实例的数量最大为 100，支持七层加速域名/四层代理实例混合提交，总实例个数最大为 200。如需变更超过 200 个实例，请通过本接口分批提交。

        :param request: Request instance for ModifyOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginGroup(self, request):
        r"""修改源站组配置，新提交的源站记录将会覆盖原有源站组中的源站记录。

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPlan(self, request):
        r"""修改套餐配置。目前仅支持修改预付费套餐的自动续费开关。

        :param request: Request instance for ModifyPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRealtimeLogDeliveryTask(self, request):
        r"""通过本接口修改实时日志投递任务配置。本接口有如下限制：<li>不支持修改实时日志投递任务目的地类型（TaskType）；</li><li>不支持修改数据投递类型（LogType）</li><li>不支持修改数据投递区域（Area）</li><li>当原实时日志投递任务的目的地为腾讯云 CLS 时，不支持修改目的地详细配置，如日志集、日志主题。</li>

        :param request: Request instance for ModifyRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        r"""本接口为旧版本修改规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本修改七层加速规则接口详情请参考 [ModifyL7AccRule](https://cloud.tencent.com/document/product/1552/115818)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

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


    def ModifySecurityAPIResource(self, request):
        r"""该接口用于修改 API 资源。

        :param request: Request instance for ModifySecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityAPIService(self, request):
        r"""该接口用于修改 API 服务。

        :param request: Request instance for ModifySecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityClientAttester(self, request):
        r"""修改客户端认证选项。

        :param request: Request instance for ModifySecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityIPGroup(self, request):
        r"""修改安全 IP 组。

        :param request: Request instance for ModifySecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityJSInjectionRule(self, request):
        r"""修改 JavaScript 注入规则。

        :param request: Request instance for ModifySecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        r"""修改Web&Bot安全配置。

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebSecurityTemplate(self, request):
        r"""修改安全策略配置模板

        :param request: Request instance for ModifyWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZone(self, request):
        r"""修改站点信息。

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneSetting(self, request):
        r"""本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [ModifyL7AccSetting](https://cloud.tencent.com/document/product/1552/115817)。

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneStatus(self, request):
        r"""用于开启，关闭站点。

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshMultiPathGatewaySecretKey(self, request):
        r"""通过本接口刷新多通道安全加速网关的密钥。客户基于接入密钥签名接入多通道安全加速网关。每个站点下只有一个密钥，可用于接入该站点下的所有网关，刷新密钥后，原始密钥会失效。

        :param request: Request instance for RefreshMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.RefreshMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.RefreshMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewPlan(self, request):
        r"""当您的套餐需要延长有效期，可以通过该接口进行续费。套餐续费仅支持个人版，基础版，标准版套餐。
        > 费用详情可参考 [套餐费用](https://cloud.tencent.com/document/product/1552/94158)

        :param request: Request instance for RenewPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.RenewPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.RenewPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewPlan", params, headers=headers)
            response = json.loads(body)
            model = models.RenewPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradePlan(self, request):
        r"""当您需要使用高等级套餐才拥有的功能，可以通过本接口升级套餐，仅支持个人版，基础版套餐进行升级。
        > 不同类型 Edgeone 计费套餐区别参考 [Edgeone计费套餐选型对比](https://cloud.tencent.com/document/product/1552/94165)
        计费套餐升级规则以及资费详情参考 [Edgeone计费套餐升配说明](https://cloud.tencent.com/document/product/1552/95291)
        如果需要将套餐升级至企业版，请 [联系我们](https://cloud.tencent.com/online-service)

        :param request: Request instance for UpgradePlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.UpgradePlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.UpgradePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradePlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyOwnership(self, request):
        r"""在 CNAME 接入模式下，您需要对站点或者域名的归属权进行验证，可以通过本接口触发验证。若站点通过归属权验证后，后续添加域名无需再验证。详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

        在 NS 接入模式下，您也可以通过本接口来查询 NS 服务器是否切换成功，详情参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452)。

        :param request: Request instance for VerifyOwnership.
        :type request: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyOwnership", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyOwnershipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))