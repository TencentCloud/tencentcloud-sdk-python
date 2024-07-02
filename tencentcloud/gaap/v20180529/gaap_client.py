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
from tencentcloud.gaap.v20180529 import models


class GaapClient(AbstractClient):
    _apiVersion = '2018-05-29'
    _endpoint = 'gaap.tencentcloudapi.com'
    _service = 'gaap'


    def AddRealServers(self, request):
        """添加源站(服务器)信息，支持IP或域名

        :param request: Request instance for AddRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.AddRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.AddRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.AddRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BanAndRecoverProxy(self, request):
        """本接口（BanAndRecoverProxy）用于联通封禁解封GAAP跨境通道实例，支持按照客户UIN维度下发请求。被封禁的实例带宽上限将会被限制到0Mbps，无法正常处理客户端和源站之间的请求。

        :param request: Request instance for BanAndRecoverProxy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.BanAndRecoverProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.BanAndRecoverProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BanAndRecoverProxy", params, headers=headers)
            response = json.loads(body)
            model = models.BanAndRecoverProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindListenerRealServers(self, request):
        """本接口（BindListenerRealServers）用于TCP/UDP监听器绑定解绑源站。
        注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。例如：原来绑定的源站为A，B，C，本次调用的选择绑定的源站为C，D，E，那么调用后所绑定的源站为C，D，E。

        :param request: Request instance for BindListenerRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.BindListenerRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.BindListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindListenerRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.BindListenerRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindRuleRealServers(self, request):
        """该接口用于7层监听器的转发规则绑定源站。注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。

        :param request: Request instance for BindRuleRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.BindRuleRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.BindRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindRuleRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.BindRuleRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckProxyCreate(self, request):
        """本接口(CheckProxyCreate)用于查询能否创建指定配置的加速通道。

        :param request: Request instance for CheckProxyCreate.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CheckProxyCreateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CheckProxyCreateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckProxyCreate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckProxyCreateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseProxies(self, request):
        """本接口（CloseProxies）用于关闭通道。通道关闭后，不再产生流量，但每天仍然收取通道基础配置费用。

        :param request: Request instance for CloseProxies.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CloseProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CloseProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProxies", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseProxyGroup(self, request):
        """本接口（CloseProxyGroup）用于关闭通道组。通道组关闭后，不再产生流量，但每天仍然收取通道基础配置费用。

        :param request: Request instance for CloseProxyGroup.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CloseProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CloseProxyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProxyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProxyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseSecurityPolicy(self, request):
        """关闭安全策略

        :param request: Request instance for CloseSecurityPolicy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CloseSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CloseSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CloseSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificate(self, request):
        """本接口（CreateCertificate）用于创建Gaap相关证书和配置文件，包括基础认证配置文件，客户端CA证书，服务器SSL证书，Gaap SSL证书以及源站CA证书。

        :param request: Request instance for CreateCertificate.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomHeader(self, request):
        """本接口（CreateCustomHeader）用于创建HTTP/HTTPS监听器的自定义header，客户端请求通过访问该监听器时，会将监听器中配置的header信息发送到源站。

        :param request: Request instance for CreateCustomHeader.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateCustomHeaderRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateCustomHeaderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomHeader", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomHeaderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomain(self, request):
        """本接口（CreateDomain）用于创建HTTP/HTTPS监听器的访问域名，客户端请求通过访问该域名来请求后端业务。
        该接口仅支持version3.0的通道。

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainErrorPageInfo(self, request):
        """定制域名指定错误码的错误响应

        :param request: Request instance for CreateDomainErrorPageInfo.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateDomainErrorPageInfoRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainErrorPageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainErrorPageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFirstLinkSession(self, request):
        """本接口（CreateFirstLinkSession）用于创建接入段加速会话，创建有可能成功，也可能失败，需要通过返回码来进行判断。

        :param request: Request instance for CreateFirstLinkSession.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateFirstLinkSessionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateFirstLinkSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFirstLinkSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFirstLinkSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalDomain(self, request):
        """用来创建统一域名

        :param request: Request instance for CreateGlobalDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateGlobalDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalDomainDns(self, request):
        """创建域名解析记录

        :param request: Request instance for CreateGlobalDomainDns.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateGlobalDomainDnsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateGlobalDomainDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalDomainDns", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalDomainDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHTTPListener(self, request):
        """该接口（CreateHTTPListener）用于在通道实例下创建HTTP协议类型的监听器。

        :param request: Request instance for CreateHTTPListener.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPListenerRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHTTPListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHTTPListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHTTPSListener(self, request):
        """该接口（CreateHTTPSListener）用于在通道实例下创建HTTPS协议类型的监听器。

        :param request: Request instance for CreateHTTPSListener.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPSListenerRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPSListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHTTPSListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHTTPSListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxy(self, request):
        """本接口（CreateProxy）用于创建/复制一个指定配置的加速通道。当复制通道时，需要设置新通道的基本配置参数，并设置ClonedProxyId来指定被复制的通道。

        :param request: Request instance for CreateProxy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxyGroup(self, request):
        """本接口（CreateProxyGroup）用于创建通道组。

        :param request: Request instance for CreateProxyGroup.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxyGroupDomain(self, request):
        """本接口（CreateProxyGroupDomain）用于创建通道组域名，并开启域名解析。

        :param request: Request instance for CreateProxyGroupDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxyGroupDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyGroupDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """该接口（CreateRule）用于创建HTTP/HTTPS监听器转发规则。

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateRuleResponse`

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


    def CreateSecurityPolicy(self, request):
        """创建安全策略

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityRules(self, request):
        """添加安全策略规则

        :param request: Request instance for CreateSecurityRules.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTCPListeners(self, request):
        """该接口（CreateTCPListeners）用于批量创建单通道或者通道组的TCP协议类型的监听器。

        :param request: Request instance for CreateTCPListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateTCPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateTCPListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTCPListeners", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTCPListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUDPListeners(self, request):
        """该接口（CreateUDPListeners）用于批量创建单通道或者通道组的UDP协议类型的监听器。

        :param request: Request instance for CreateUDPListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateUDPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateUDPListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUDPListeners", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUDPListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCertificate(self, request):
        """本接口（DeleteCertificate）用于删除证书。

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomain(self, request):
        """本接口（DeleteDomain）仅适用于7层监听器，用于删除该监听器下对应域名及域名下的所有规则，所有已绑定源站的规则将自动解绑。

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainErrorPageInfo(self, request):
        """删除域名的定制错误

        :param request: Request instance for DeleteDomainErrorPageInfo.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainErrorPageInfoRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainErrorPageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainErrorPageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFirstLinkSession(self, request):
        """本接口（DeleteFirstLinkSession）用于删除接入段加速会话，删除加速会话后会停止加速。

        :param request: Request instance for DeleteFirstLinkSession.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteFirstLinkSessionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteFirstLinkSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirstLinkSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirstLinkSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalDomain(self, request):
        """删除统一域名

        :param request: Request instance for DeleteGlobalDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteGlobalDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalDomainDns(self, request):
        """删除域名的某条解析记录

        :param request: Request instance for DeleteGlobalDomainDns.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteGlobalDomainDnsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteGlobalDomainDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalDomainDns", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalDomainDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListeners(self, request):
        """该接口（DeleteListeners）用于批量删除通道或通道组的监听器，包括4/7层监听器。

        :param request: Request instance for DeleteListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProxyGroup(self, request):
        """本接口（DeleteProxyGroup）用于删除通道组。

        :param request: Request instance for DeleteProxyGroup.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteProxyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProxyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProxyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """该接口（DeleteRule）用于删除HTTP/HTTPS监听器的转发规则。

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteRuleResponse`

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


    def DeleteSecurityPolicy(self, request):
        """删除安全策略

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityRules(self, request):
        """删除安全策略规则

        :param request: Request instance for DeleteSecurityRules.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessRegions(self, request):
        """本接口（DescribeAccessRegions）用于查询加速区域，即客户端接入区域。

        :param request: Request instance for DescribeAccessRegions.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessRegionsByDestRegion(self, request):
        """本接口（DescribeAccessRegionsByDestRegion）根据源站区域查询可用的加速区域列表。

        :param request: Request instance for DescribeAccessRegionsByDestRegion.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessRegionsByDestRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessRegionsByDestRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthSignature(self, request):
        """为了防止在下单、询价、后付费开通等过程中确保来源合法以及订单参数没有被篡改过，各个业务方使用下单、询价等场景需调用计费签名接口获取签名，获取签名的请求需带上签名以验证身份，本接口可以获取计费签名。

        :param request: Request instance for DescribeAuthSignature.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeAuthSignatureRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeAuthSignatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthSignature", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthSignatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlackHeader(self, request):
        """本接口（DescribeBlackHeader）用于查询禁用的自定义header 名称

        :param request: Request instance for DescribeBlackHeader.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeBlackHeaderRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeBlackHeaderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlackHeader", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlackHeaderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateDetail(self, request):
        """本接口（DescribeCertificateDetail）用于查询证书详情，包括证书ID，证书名字，证书类型，证书内容以及密钥等信息。

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificateDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificates(self, request):
        """本接口（DescribeCertificates）用来查询可以使用的证书列表。

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificatesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCountryAreaMapping(self, request):
        """本接口（DescribeCountryAreaMapping）用于获取国家地区编码映射表。

        :param request: Request instance for DescribeCountryAreaMapping.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCountryAreaMappingRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCountryAreaMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCountryAreaMapping", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCountryAreaMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderProxies(self, request):
        """本接口（DescribeCrossBorderProxies）用于查询跨境通道实例列表。

        :param request: Request instance for DescribeCrossBorderProxies.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCrossBorderProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCrossBorderProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomHeader(self, request):
        """本接口（DescribeCustomHeader）用于自定义header列表

        :param request: Request instance for DescribeCustomHeader.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCustomHeaderRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCustomHeaderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomHeader", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomHeaderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDestRegions(self, request):
        """本接口（DescribeDestRegions）用于查询源站区域，即源站服务器所在区域。

        :param request: Request instance for DescribeDestRegions.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeDestRegionsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeDestRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDestRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDestRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainErrorPageInfo(self, request):
        """查询目前定制域名的错误响应

        :param request: Request instance for DescribeDomainErrorPageInfo.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainErrorPageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainErrorPageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainErrorPageInfoByIds(self, request):
        """根据定制错误ID查询错误响应

        :param request: Request instance for DescribeDomainErrorPageInfoByIds.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoByIdsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoByIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainErrorPageInfoByIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainErrorPageInfoByIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirstLinkSession(self, request):
        """本接口（DescribeFirstLinkSession）用于查询接入段加速会话状态，包括会话状态，生效时长，加速套餐等信息。

        :param request: Request instance for DescribeFirstLinkSession.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeFirstLinkSessionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeFirstLinkSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirstLinkSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirstLinkSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalDomainDns(self, request):
        """查询域名解析列表

        :param request: Request instance for DescribeGlobalDomainDns.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGlobalDomainDnsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGlobalDomainDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalDomainDns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalDomainDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalDomains(self, request):
        """查询域名列表

        :param request: Request instance for DescribeGlobalDomains.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGlobalDomainsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGlobalDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupAndStatisticsProxy(self, request):
        """该接口为内部接口，用于查询可以获取统计数据的通道组和通道信息

        :param request: Request instance for DescribeGroupAndStatisticsProxy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupAndStatisticsProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupAndStatisticsProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupDomainConfig(self, request):
        """本接口（DescribeGroupDomainConfig）用于获取通道组域名解析配置详情。

        :param request: Request instance for DescribeGroupDomainConfig.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupDomainConfigRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHTTPListeners(self, request):
        """该接口（DescribeHTTPListeners）用来查询HTTP监听器信息。

        :param request: Request instance for DescribeHTTPListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHTTPListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHTTPListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHTTPSListeners(self, request):
        """本接口（DescribeHTTPSListeners）用来查询HTTPS监听器信息。

        :param request: Request instance for DescribeHTTPSListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPSListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPSListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHTTPSListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHTTPSListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerRealServers(self, request):
        """该接口（DescribeListenerRealServers）用于查询TCP/UDP监听器源站列表，包括该监听器已经绑定的源站列表以及可以绑定的源站列表。

        :param request: Request instance for DescribeListenerRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300秒, 3600秒和86400秒的细粒度，取值为细粒度范围内最大值。

        :param request: Request instance for DescribeListenerStatistics.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxies(self, request):
        """本接口（DescribeProxies）用于查询通道实例列表。

        :param request: Request instance for DescribeProxies.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxiesStatus(self, request):
        """本接口（DescribeProxiesStatus）用于查询通道状态列表。

        :param request: Request instance for DescribeProxiesStatus.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesStatusRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxiesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxiesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyAndStatisticsListeners(self, request):
        """该接口为内部接口，用于查询可以获取统计数据的通道和监听器信息

        :param request: Request instance for DescribeProxyAndStatisticsListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyAndStatisticsListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyAndStatisticsListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyDetail(self, request):
        """本接口（DescribeProxyDetail）用于查询通道详情。

        :param request: Request instance for DescribeProxyDetail.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyGroupDetails(self, request):
        """本接口（DescribeProxyGroupDetails）用于查询通道组详情。

        :param request: Request instance for DescribeProxyGroupDetails.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyGroupDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyGroupDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyGroupList(self, request):
        """本接口（DescribeProxyGroupList）用于拉取通道组列表及各通道组基本信息。

        :param request: Request instance for DescribeProxyGroupList.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupListRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyGroupStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。

        :param request: Request instance for DescribeProxyGroupStatistics.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyGroupStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyGroupStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发，丢包和时延数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。

        :param request: Request instance for DescribeProxyStatistics.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealServerStatistics(self, request):
        """该接口（DescribeRealServerStatistics）用于查询源站健康检查结果的统计数据。源站状态展示位为1：正常或者0：异常。查询的源站需要在监听器或者规则上进行了绑定，查询时需指定绑定的监听器或者规则ID。该接口支持1分钟细粒度的源站状态统计数据展示。

        :param request: Request instance for DescribeRealServerStatistics.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServerStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServerStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealServerStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealServerStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealServers(self, request):
        """本接口（DescribeRealServers）用于查询源站信息，可以根据项目名查询所有的源站信息，此外支持指定IP或者域名的源站模糊查询。

        :param request: Request instance for DescribeRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealServersStatus(self, request):
        """本接口（DescribeRealServersStatus）用于查询源站是否已被规则或者监听器绑定

        :param request: Request instance for DescribeRealServersStatus.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersStatusRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealServersStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealServersStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegionAndPrice(self, request):
        """该接口（DescribeRegionAndPrice）用于获取源站区域和带宽梯度价格

        :param request: Request instance for DescribeRegionAndPrice.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRegionAndPriceRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRegionAndPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegionAndPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionAndPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcesByTag(self, request):
        """本接口（DescribeResourcesByTag）用于根据标签来查询对应的资源信息，包括通道，通道组和源站。

        :param request: Request instance for DescribeResourcesByTag.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeResourcesByTagRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeResourcesByTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByTag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleRealServers(self, request):
        """本接口（DescribeRuleRealServers）用于查询转发规则相关的源站信息， 包括该规则可绑定的源站信息和已绑定的源站信息。

        :param request: Request instance for DescribeRuleRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRuleRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """本接口（DescribeRules）用于查询监听器下的所有规则信息，包括规则域名，路径以及该规则下所绑定的源站列表。当通道版本为3.0时，该接口会返回该域名对应的高级认证配置信息。

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesResponse`

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


    def DescribeRulesByRuleIds(self, request):
        """本接口（DescribeRulesByRuleIds）用于根据规则ID拉取规则信息列表。支持一个或者多个规则信息的拉取。一次最多支持10个规则信息的拉取。

        :param request: Request instance for DescribeRulesByRuleIds.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesByRuleIdsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesByRuleIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesByRuleIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesByRuleIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyDetail(self, request):
        """获取安全策略详情

        :param request: Request instance for DescribeSecurityPolicyDetail.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityRules(self, request):
        """本接口（DescribeSecurityRules）用于根据安全规则ID查询安全规则详情列表。支持一个或多个安全规则的查询。一次最多支持20个安全规则的查询。

        :param request: Request instance for DescribeSecurityRules.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTCPListeners(self, request):
        """该接口（DescribeTCPListeners）用于查询单通道或者通道组下的TCP监听器信息。

        :param request: Request instance for DescribeTCPListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeTCPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeTCPListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTCPListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTCPListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUDPListeners(self, request):
        """该接口（DescribeUDPListeners）用于查询单通道或者通道组下的UDP监听器信息

        :param request: Request instance for DescribeUDPListeners.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeUDPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeUDPListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUDPListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUDPListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyProxies(self, request):
        """本接口（DestroyProxies）用于销毁。通道销毁后，不再产生任何费用。

        :param request: Request instance for DestroyProxies.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DestroyProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DestroyProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableGlobalDomain(self, request):
        """暂停域名解析

        :param request: Request instance for DisableGlobalDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.DisableGlobalDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DisableGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DisableGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableGlobalDomain(self, request):
        """开启域名解析

        :param request: Request instance for EnableGlobalDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.EnableGlobalDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.EnableGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.EnableGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateProxy(self, request):
        """本接口（InquiryPriceCreateProxy）用于创建加速通道询价。

        :param request: Request instance for InquiryPriceCreateProxy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.InquiryPriceCreateProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.InquiryPriceCreateProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateProxy", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificate(self, request):
        """本接口（ModifyCertificate）用于修改监听器下的域名对应的证书。该接口仅适用于version3.0的通道。

        :param request: Request instance for ModifyCertificate.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateAttributes(self, request):
        """本接口（ModifyCertificateAttributes）用于修改证书，包括证书名字以及证书内容。

        :param request: Request instance for ModifyCertificateAttributes.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateAttributesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomain(self, request):
        """本接口（ModifyDomain）用于监听器下的域名。当通道版本为3.0时，支持对该域名所对应的证书修改。

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalDomainAttribute(self, request):
        """修改域名属性

        :param request: Request instance for ModifyGlobalDomainAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyGlobalDomainAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyGlobalDomainAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalDomainAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalDomainAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalDomainDns(self, request):
        """修改域名解析记录

        :param request: Request instance for ModifyGlobalDomainDns.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyGlobalDomainDnsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyGlobalDomainDnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalDomainDns", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalDomainDnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroupDomainConfig(self, request):
        """本接口（ModifyGroupDomainConfig）用于配置通道组就近接入域名。

        :param request: Request instance for ModifyGroupDomainConfig.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyGroupDomainConfigRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroupDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHTTPListenerAttribute(self, request):
        """该接口（ModifyHTTPListenerAttribute）用于修改通道的HTTP监听器配置信息，目前仅支持修改监听器的名称。
        注意：通道组通道暂时不支持HTTP/HTTPS监听器。

        :param request: Request instance for ModifyHTTPListenerAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHTTPListenerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHTTPListenerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHTTPSListenerAttribute(self, request):
        """该接口（ModifyHTTPSListenerAttribute）用于修改HTTPS监听器配置，当前不支持通道组和v1版本通道。

        :param request: Request instance for ModifyHTTPSListenerAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHTTPSListenerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHTTPSListenerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxiesAttribute(self, request):
        """本接口（ModifyProxiesAttribute）用于修改实例的属性（目前只支持修改通道的名称）。

        :param request: Request instance for ModifyProxiesAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxiesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxiesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxiesProject(self, request):
        """本接口（ModifyProxiesProject）用于修改通道所属项目。

        :param request: Request instance for ModifyProxiesProject.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesProjectRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxiesProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxiesProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxyConfiguration(self, request):
        """本接口（ModifyProxyConfiguration）用于修改通道的配置。根据当前业务的容量需求，扩容或缩容相关通道的配置。仅支持Scalarable为1的通道,Scalarable可通过接口DescribeProxies获取。

        :param request: Request instance for ModifyProxyConfiguration.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyConfigurationRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxyGroupAttribute(self, request):
        """本接口（ModifyProxyGroupAttribute）用于修改通道组属性，目前仅支持修改通道组名称。

        :param request: Request instance for ModifyProxyGroupAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyGroupAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRealServerName(self, request):
        """本接口（ModifyRealServerName）用于修改源站的名称

        :param request: Request instance for ModifyRealServerName.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyRealServerNameRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyRealServerNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRealServerName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRealServerNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleAttribute(self, request):
        """本接口（ModifyRuleAttribute）用于修改转发规则的信息，包括健康检查的配置以及转发策略。

        :param request: Request instance for ModifyRuleAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyRuleAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyRuleAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityRule(self, request):
        """修改安全策略规则名

        :param request: Request instance for ModifySecurityRule.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifySecurityRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifySecurityRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTCPListenerAttribute(self, request):
        """本接口（ModifyTCPListenerAttribute）用于修改通道实例下TCP监听器配置，包括健康检查的配置，调度策略。

        :param request: Request instance for ModifyTCPListenerAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyTCPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyTCPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTCPListenerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTCPListenerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUDPListenerAttribute(self, request):
        """本接口（ModifyUDPListenerAttribute）用于修改通道实例下UDP监听器配置，包括监听器名称和调度策略的修改。

        :param request: Request instance for ModifyUDPListenerAttribute.
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyUDPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyUDPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUDPListenerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUDPListenerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenProxies(self, request):
        """该接口（OpenProxies）用于开启一条或者多条通道。

        :param request: Request instance for OpenProxies.
        :type request: :class:`tencentcloud.gaap.v20180529.models.OpenProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.OpenProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenProxies", params, headers=headers)
            response = json.loads(body)
            model = models.OpenProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenProxyGroup(self, request):
        """该接口（OpenProxyGroup）用于开启一条通道组中的所有通道

        :param request: Request instance for OpenProxyGroup.
        :type request: :class:`tencentcloud.gaap.v20180529.models.OpenProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.OpenProxyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenProxyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.OpenProxyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenSecurityPolicy(self, request):
        """开启安全策略

        :param request: Request instance for OpenSecurityPolicy.
        :type request: :class:`tencentcloud.gaap.v20180529.models.OpenSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.OpenSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.OpenSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveRealServers(self, request):
        """删除已添加的源站(服务器)IP或域名

        :param request: Request instance for RemoveRealServers.
        :type request: :class:`tencentcloud.gaap.v20180529.models.RemoveRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RemoveRealServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveRealServers", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveRealServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAuthentication(self, request):
        """本接口（SetAuthentication）用于通道的高级认证配置，包括认证方式选择，以及各种认证方式对应的证书选择。仅支持Version3.0的通道。

        :param request: Request instance for SetAuthentication.
        :type request: :class:`tencentcloud.gaap.v20180529.models.SetAuthenticationRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.SetAuthenticationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAuthentication", params, headers=headers)
            response = json.loads(body)
            model = models.SetAuthenticationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTlsVersion(self, request):
        """设置监听器TLS配置

        :param request: Request instance for SetTlsVersion.
        :type request: :class:`tencentcloud.gaap.v20180529.models.SetTlsVersionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.SetTlsVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTlsVersion", params, headers=headers)
            response = json.loads(body)
            model = models.SetTlsVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))