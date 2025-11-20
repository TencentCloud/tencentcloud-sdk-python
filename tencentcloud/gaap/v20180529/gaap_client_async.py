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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.gaap.v20180529 import models
from typing import Dict


class GaapClient(AbstractClient):
    _apiVersion = '2018-05-29'
    _endpoint = 'gaap.tencentcloudapi.com'
    _service = 'gaap'

    async def AddRealServers(
            self,
            request: models.AddRealServersRequest,
            opts: Dict = None,
    ) -> models.AddRealServersResponse:
        """
        添加源站(服务器)信息，支持IP或域名
        """
        
        kwargs = {}
        kwargs["action"] = "AddRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BanAndRecoverProxy(
            self,
            request: models.BanAndRecoverProxyRequest,
            opts: Dict = None,
    ) -> models.BanAndRecoverProxyResponse:
        """
        本接口（BanAndRecoverProxy）用于联通封禁解封GAAP跨境通道实例，支持按照客户UIN维度下发请求。被封禁的实例带宽上限将会被限制到0Mbps，无法正常处理客户端和源站之间的请求。
        """
        
        kwargs = {}
        kwargs["action"] = "BanAndRecoverProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BanAndRecoverProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindListenerRealServers(
            self,
            request: models.BindListenerRealServersRequest,
            opts: Dict = None,
    ) -> models.BindListenerRealServersResponse:
        """
        本接口（BindListenerRealServers）用于TCP/UDP监听器绑定解绑源站。
        注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。例如：原来绑定的源站为A，B，C，本次调用的选择绑定的源站为C，D，E，那么调用后所绑定的源站为C，D，E。
        """
        
        kwargs = {}
        kwargs["action"] = "BindListenerRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindListenerRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRuleRealServers(
            self,
            request: models.BindRuleRealServersRequest,
            opts: Dict = None,
    ) -> models.BindRuleRealServersResponse:
        """
        该接口用于7层监听器的转发规则绑定源站。注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。
        """
        
        kwargs = {}
        kwargs["action"] = "BindRuleRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRuleRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckProxyCreate(
            self,
            request: models.CheckProxyCreateRequest,
            opts: Dict = None,
    ) -> models.CheckProxyCreateResponse:
        """
        本接口(CheckProxyCreate)用于查询能否创建指定配置的加速通道。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckProxyCreate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckProxyCreateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxies(
            self,
            request: models.CloseProxiesRequest,
            opts: Dict = None,
    ) -> models.CloseProxiesResponse:
        """
        本接口（CloseProxies）用于关闭通道。通道关闭后，不再产生流量，但每天仍然收取通道基础配置费用。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxyGroup(
            self,
            request: models.CloseProxyGroupRequest,
            opts: Dict = None,
    ) -> models.CloseProxyGroupResponse:
        """
        本接口（CloseProxyGroup）用于关闭通道组。通道组关闭后，不再产生流量，但每天仍然收取通道基础配置费用。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSecurityPolicy(
            self,
            request: models.CloseSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CloseSecurityPolicyResponse:
        """
        关闭安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificate(
            self,
            request: models.CreateCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateResponse:
        """
        本接口（CreateCertificate）用于创建Gaap相关证书和配置文件，包括基础认证配置文件，客户端CA证书，服务器SSL证书，Gaap SSL证书以及源站CA证书。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomHeader(
            self,
            request: models.CreateCustomHeaderRequest,
            opts: Dict = None,
    ) -> models.CreateCustomHeaderResponse:
        """
        本接口（CreateCustomHeader）用于创建HTTP/HTTPS监听器的自定义header，客户端请求通过访问该监听器时，会将监听器中配置的header信息发送到源站。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        本接口（CreateDomain）用于创建HTTP/HTTPS监听器的访问域名，客户端请求通过访问该域名来请求后端业务。
        该接口仅支持version3.0的通道。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainErrorPageInfo(
            self,
            request: models.CreateDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.CreateDomainErrorPageInfoResponse:
        """
        定制域名指定错误码的错误响应
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalDomain(
            self,
            request: models.CreateGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalDomainResponse:
        """
        用来创建统一域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalDomainDns(
            self,
            request: models.CreateGlobalDomainDnsRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalDomainDnsResponse:
        """
        创建域名解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalDomainDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalDomainDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHTTPListener(
            self,
            request: models.CreateHTTPListenerRequest,
            opts: Dict = None,
    ) -> models.CreateHTTPListenerResponse:
        """
        该接口（CreateHTTPListener）用于在通道实例下创建HTTP协议类型的监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHTTPListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHTTPListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHTTPSListener(
            self,
            request: models.CreateHTTPSListenerRequest,
            opts: Dict = None,
    ) -> models.CreateHTTPSListenerResponse:
        """
        该接口（CreateHTTPSListener）用于在通道实例下创建HTTPS协议类型的监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHTTPSListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHTTPSListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxy(
            self,
            request: models.CreateProxyRequest,
            opts: Dict = None,
    ) -> models.CreateProxyResponse:
        """
        本接口（CreateProxy）用于创建/复制一个指定配置的加速通道。当复制通道时，需要设置新通道的基本配置参数，并设置ClonedProxyId来指定被复制的通道。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyGroup(
            self,
            request: models.CreateProxyGroupRequest,
            opts: Dict = None,
    ) -> models.CreateProxyGroupResponse:
        """
        本接口（CreateProxyGroup）用于创建通道组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyGroupDomain(
            self,
            request: models.CreateProxyGroupDomainRequest,
            opts: Dict = None,
    ) -> models.CreateProxyGroupDomainResponse:
        """
        本接口（CreateProxyGroupDomain）用于创建通道组域名，并开启域名解析。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyGroupDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyGroupDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        该接口（CreateRule）用于创建HTTP/HTTPS监听器转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        创建安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityRules(
            self,
            request: models.CreateSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityRulesResponse:
        """
        添加安全策略规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTCPListeners(
            self,
            request: models.CreateTCPListenersRequest,
            opts: Dict = None,
    ) -> models.CreateTCPListenersResponse:
        """
        该接口（CreateTCPListeners）用于批量创建单通道或者通道组的TCP协议类型的监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTCPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTCPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUDPListeners(
            self,
            request: models.CreateUDPListenersRequest,
            opts: Dict = None,
    ) -> models.CreateUDPListenersResponse:
        """
        该接口（CreateUDPListeners）用于批量创建单通道或者通道组的UDP协议类型的监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUDPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUDPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCertificate(
            self,
            request: models.DeleteCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCertificateResponse:
        """
        本接口（DeleteCertificate）用于删除证书。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        本接口（DeleteDomain）仅适用于7层监听器，用于删除该监听器下对应域名及域名下的所有规则，所有已绑定源站的规则将自动解绑。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainErrorPageInfo(
            self,
            request: models.DeleteDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainErrorPageInfoResponse:
        """
        删除域名的定制错误
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalDomain(
            self,
            request: models.DeleteGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalDomainResponse:
        """
        删除统一域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalDomainDns(
            self,
            request: models.DeleteGlobalDomainDnsRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalDomainDnsResponse:
        """
        删除域名的某条解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalDomainDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalDomainDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListeners(
            self,
            request: models.DeleteListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteListenersResponse:
        """
        该接口（DeleteListeners）用于批量删除通道或通道组的监听器，包括4/7层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProxyGroup(
            self,
            request: models.DeleteProxyGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteProxyGroupResponse:
        """
        本接口（DeleteProxyGroup）用于删除通道组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        该接口（DeleteRule）用于删除HTTP/HTTPS监听器的转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        删除安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityRules(
            self,
            request: models.DeleteSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityRulesResponse:
        """
        删除安全策略规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRegions(
            self,
            request: models.DescribeAccessRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRegionsResponse:
        """
        本接口（DescribeAccessRegions）用于查询加速区域，即客户端接入区域。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRegionsByDestRegion(
            self,
            request: models.DescribeAccessRegionsByDestRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRegionsByDestRegionResponse:
        """
        本接口（DescribeAccessRegionsByDestRegion）根据源站区域查询可用的加速区域列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRegionsByDestRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRegionsByDestRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthSignature(
            self,
            request: models.DescribeAuthSignatureRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthSignatureResponse:
        """
        为了防止在下单、询价、后付费开通等过程中确保来源合法以及订单参数没有被篡改过，各个业务方使用下单、询价等场景需调用计费签名接口获取签名，获取签名的请求需带上签名以验证身份，本接口可以获取计费签名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthSignature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthSignatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlackHeader(
            self,
            request: models.DescribeBlackHeaderRequest,
            opts: Dict = None,
    ) -> models.DescribeBlackHeaderResponse:
        """
        本接口（DescribeBlackHeader）用于查询禁用的自定义header 名称
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlackHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlackHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateDetail(
            self,
            request: models.DescribeCertificateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateDetailResponse:
        """
        本接口（DescribeCertificateDetail）用于查询证书详情，包括证书ID，证书名字，证书类型，证书内容以及密钥等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificates(
            self,
            request: models.DescribeCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificatesResponse:
        """
        本接口（DescribeCertificates）用来查询可以使用的证书列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCountryAreaMapping(
            self,
            request: models.DescribeCountryAreaMappingRequest,
            opts: Dict = None,
    ) -> models.DescribeCountryAreaMappingResponse:
        """
        本接口（DescribeCountryAreaMapping）用于获取国家地区编码映射表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCountryAreaMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCountryAreaMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderProxies(
            self,
            request: models.DescribeCrossBorderProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderProxiesResponse:
        """
        本接口（DescribeCrossBorderProxies）用于查询跨境通道实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomHeader(
            self,
            request: models.DescribeCustomHeaderRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomHeaderResponse:
        """
        本接口（DescribeCustomHeader）用于自定义header列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDestRegions(
            self,
            request: models.DescribeDestRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDestRegionsResponse:
        """
        本接口（DescribeDestRegions）用于查询源站区域，即源站服务器所在区域。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDestRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDestRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainErrorPageInfo(
            self,
            request: models.DescribeDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainErrorPageInfoResponse:
        """
        查询指定域名的错误响应
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainErrorPageInfoByIds(
            self,
            request: models.DescribeDomainErrorPageInfoByIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainErrorPageInfoByIdsResponse:
        """
        根据定制错误ID查询错误响应
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainErrorPageInfoByIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainErrorPageInfoByIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalDomainDns(
            self,
            request: models.DescribeGlobalDomainDnsRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalDomainDnsResponse:
        """
        查询域名解析列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalDomainDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalDomainDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalDomains(
            self,
            request: models.DescribeGlobalDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalDomainsResponse:
        """
        查询域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupAndStatisticsProxy(
            self,
            request: models.DescribeGroupAndStatisticsProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupAndStatisticsProxyResponse:
        """
        该接口为内部接口，用于查询可以获取统计数据的通道组和通道信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupAndStatisticsProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupAndStatisticsProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupDomainConfig(
            self,
            request: models.DescribeGroupDomainConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupDomainConfigResponse:
        """
        本接口（DescribeGroupDomainConfig）用于获取通道组域名解析配置详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHTTPListeners(
            self,
            request: models.DescribeHTTPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeHTTPListenersResponse:
        """
        该接口（DescribeHTTPListeners）用来查询HTTP监听器信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHTTPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHTTPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHTTPSListeners(
            self,
            request: models.DescribeHTTPSListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeHTTPSListenersResponse:
        """
        本接口（DescribeHTTPSListeners）用来查询HTTPS监听器信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHTTPSListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHTTPSListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerRealServers(
            self,
            request: models.DescribeListenerRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerRealServersResponse:
        """
        该接口（DescribeListenerRealServers）用于查询TCP/UDP监听器源站列表，包括该监听器已经绑定的源站列表以及可以绑定的源站列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerStatistics(
            self,
            request: models.DescribeListenerStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerStatisticsResponse:
        """
        该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300秒, 3600秒和86400秒的细粒度，取值为细粒度范围内最大值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxies(
            self,
            request: models.DescribeProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesResponse:
        """
        本接口（DescribeProxies）用于查询通道实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxiesStatus(
            self,
            request: models.DescribeProxiesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesStatusResponse:
        """
        本接口（DescribeProxiesStatus）用于查询通道状态列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxiesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyAndStatisticsListeners(
            self,
            request: models.DescribeProxyAndStatisticsListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyAndStatisticsListenersResponse:
        """
        该接口为内部接口，用于查询可以获取统计数据的通道和监听器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyAndStatisticsListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyAndStatisticsListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyDetail(
            self,
            request: models.DescribeProxyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyDetailResponse:
        """
        本接口（DescribeProxyDetail）用于查询通道详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupDetails(
            self,
            request: models.DescribeProxyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupDetailsResponse:
        """
        本接口（DescribeProxyGroupDetails）用于查询通道组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupList(
            self,
            request: models.DescribeProxyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupListResponse:
        """
        本接口（DescribeProxyGroupList）用于拉取通道组列表及各通道组基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupStatistics(
            self,
            request: models.DescribeProxyGroupStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupStatisticsResponse:
        """
        该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyStatistics(
            self,
            request: models.DescribeProxyStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyStatisticsResponse:
        """
        该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发，丢包和时延数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServerStatistics(
            self,
            request: models.DescribeRealServerStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServerStatisticsResponse:
        """
        该接口（DescribeRealServerStatistics）用于查询源站健康检查结果的统计数据。源站状态展示位为1：正常或者0：异常。查询的源站需要在监听器或者规则上进行了绑定，查询时需指定绑定的监听器或者规则ID。该接口支持1分钟细粒度的源站状态统计数据展示。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServerStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServerStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServers(
            self,
            request: models.DescribeRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServersResponse:
        """
        本接口（DescribeRealServers）用于查询源站信息，可以根据项目名查询所有的源站信息，此外支持指定IP或者域名的源站模糊查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServersStatus(
            self,
            request: models.DescribeRealServersStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServersStatusResponse:
        """
        本接口（DescribeRealServersStatus）用于查询源站是否已被规则或者监听器绑定
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServersStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServersStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegionAndPrice(
            self,
            request: models.DescribeRegionAndPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionAndPriceResponse:
        """
        该接口（DescribeRegionAndPrice）用于获取源站区域和带宽梯度价格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegionAndPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionAndPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTag(
            self,
            request: models.DescribeResourcesByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagResponse:
        """
        本接口（DescribeResourcesByTag）用于根据标签来查询对应的资源信息，包括通道，通道组和源站。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleRealServers(
            self,
            request: models.DescribeRuleRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleRealServersResponse:
        """
        本接口（DescribeRuleRealServers）用于查询转发规则相关的源站信息， 包括该规则可绑定的源站信息和已绑定的源站信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        本接口（DescribeRules）用于查询监听器下的所有规则信息，包括规则域名，路径以及该规则下所绑定的源站列表。当通道版本为3.0时，该接口会返回该域名对应的高级认证配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesByRuleIds(
            self,
            request: models.DescribeRulesByRuleIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesByRuleIdsResponse:
        """
        本接口（DescribeRulesByRuleIds）用于根据规则ID拉取规则信息列表。支持一个或者多个规则信息的拉取。一次最多支持10个规则信息的拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesByRuleIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesByRuleIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyDetail(
            self,
            request: models.DescribeSecurityPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyDetailResponse:
        """
        获取安全策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityRules(
            self,
            request: models.DescribeSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityRulesResponse:
        """
        本接口（DescribeSecurityRules）用于根据安全规则ID查询安全规则详情列表。支持一个或多个安全规则的查询。一次最多支持20个安全规则的查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTCPListeners(
            self,
            request: models.DescribeTCPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeTCPListenersResponse:
        """
        该接口（DescribeTCPListeners）用于查询单通道或者通道组下的TCP监听器信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTCPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTCPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        查询异步任务执行状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUDPListeners(
            self,
            request: models.DescribeUDPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeUDPListenersResponse:
        """
        该接口（DescribeUDPListeners）用于查询单通道或者通道组下的UDP监听器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUDPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUDPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyProxies(
            self,
            request: models.DestroyProxiesRequest,
            opts: Dict = None,
    ) -> models.DestroyProxiesResponse:
        """
        本接口（DestroyProxies）用于销毁。通道销毁后，不再产生任何费用。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableGlobalDomain(
            self,
            request: models.DisableGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.DisableGlobalDomainResponse:
        """
        暂停域名解析
        """
        
        kwargs = {}
        kwargs["action"] = "DisableGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGlobalDomain(
            self,
            request: models.EnableGlobalDomainRequest,
            opts: Dict = None,
    ) -> models.EnableGlobalDomainResponse:
        """
        开启域名解析
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGlobalDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGlobalDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateProxy(
            self,
            request: models.InquiryPriceCreateProxyRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateProxyResponse:
        """
        本接口（InquiryPriceCreateProxy）用于创建加速通道询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificate(
            self,
            request: models.ModifyCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateResponse:
        """
        本接口（ModifyCertificate）用于修改监听器下的域名对应的证书。该接口仅适用于version3.0的通道。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateAttributes(
            self,
            request: models.ModifyCertificateAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateAttributesResponse:
        """
        本接口（ModifyCertificateAttributes）用于修改证书，包括证书名字以及证书内容。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomain(
            self,
            request: models.ModifyDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainResponse:
        """
        本接口（ModifyDomain）用于监听器下的域名。当通道版本为3.0时，支持对该域名所对应的证书修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalDomainAttribute(
            self,
            request: models.ModifyGlobalDomainAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalDomainAttributeResponse:
        """
        修改域名属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalDomainAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalDomainAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalDomainDns(
            self,
            request: models.ModifyGlobalDomainDnsRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalDomainDnsResponse:
        """
        修改域名解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalDomainDns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalDomainDnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroupDomainConfig(
            self,
            request: models.ModifyGroupDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupDomainConfigResponse:
        """
        本接口（ModifyGroupDomainConfig）用于配置通道组就近接入域名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroupDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHTTPListenerAttribute(
            self,
            request: models.ModifyHTTPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHTTPListenerAttributeResponse:
        """
        该接口（ModifyHTTPListenerAttribute）用于修改通道的HTTP监听器配置信息，目前仅支持修改监听器的名称。
        注意：通道组通道暂时不支持HTTP/HTTPS监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHTTPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHTTPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHTTPSListenerAttribute(
            self,
            request: models.ModifyHTTPSListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHTTPSListenerAttributeResponse:
        """
        该接口（ModifyHTTPSListenerAttribute）用于修改HTTPS监听器配置，当前不支持通道组和v1版本通道。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHTTPSListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHTTPSListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxiesAttribute(
            self,
            request: models.ModifyProxiesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyProxiesAttributeResponse:
        """
        本接口（ModifyProxiesAttribute）用于修改实例的属性（目前只支持修改通道的名称）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxiesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxiesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxiesProject(
            self,
            request: models.ModifyProxiesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProxiesProjectResponse:
        """
        本接口（ModifyProxiesProject）用于修改通道所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxiesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxiesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyConfiguration(
            self,
            request: models.ModifyProxyConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyConfigurationResponse:
        """
        本接口（ModifyProxyConfiguration）用于修改通道的配置。根据当前业务的容量需求，扩容或缩容相关通道的配置。仅支持Scalarable为1的通道,Scalarable可通过接口DescribeProxies获取。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyGroupAttribute(
            self,
            request: models.ModifyProxyGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyGroupAttributeResponse:
        """
        本接口（ModifyProxyGroupAttribute）用于修改通道组属性，目前仅支持修改通道组名称与项目ID。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealServerName(
            self,
            request: models.ModifyRealServerNameRequest,
            opts: Dict = None,
    ) -> models.ModifyRealServerNameResponse:
        """
        本接口（ModifyRealServerName）用于修改源站的名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRealServerName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRealServerNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleAttribute(
            self,
            request: models.ModifyRuleAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleAttributeResponse:
        """
        本接口（ModifyRuleAttribute）用于修改转发规则的信息，包括健康检查的配置以及转发策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityRule(
            self,
            request: models.ModifySecurityRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityRuleResponse:
        """
        修改安全策略规则名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTCPListenerAttribute(
            self,
            request: models.ModifyTCPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTCPListenerAttributeResponse:
        """
        本接口（ModifyTCPListenerAttribute）用于修改通道实例下TCP监听器配置，包括健康检查的配置，调度策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTCPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTCPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUDPListenerAttribute(
            self,
            request: models.ModifyUDPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyUDPListenerAttributeResponse:
        """
        本接口（ModifyUDPListenerAttribute）用于修改通道实例下UDP监听器配置，包括监听器名称和调度策略的修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUDPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUDPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProxies(
            self,
            request: models.OpenProxiesRequest,
            opts: Dict = None,
    ) -> models.OpenProxiesResponse:
        """
        该接口（OpenProxies）用于开启一条或者多条通道。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProxyGroup(
            self,
            request: models.OpenProxyGroupRequest,
            opts: Dict = None,
    ) -> models.OpenProxyGroupResponse:
        """
        该接口（OpenProxyGroup）用于开启一条通道组中的所有通道
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSecurityPolicy(
            self,
            request: models.OpenSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.OpenSecurityPolicyResponse:
        """
        开启安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveRealServers(
            self,
            request: models.RemoveRealServersRequest,
            opts: Dict = None,
    ) -> models.RemoveRealServersResponse:
        """
        删除已添加的源站(服务器)IP或域名
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAuthentication(
            self,
            request: models.SetAuthenticationRequest,
            opts: Dict = None,
    ) -> models.SetAuthenticationResponse:
        """
        本接口（SetAuthentication）用于通道的高级认证配置，包括认证方式选择，以及各种认证方式对应的证书选择。仅支持Version3.0的通道。
        """
        
        kwargs = {}
        kwargs["action"] = "SetAuthentication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAuthenticationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTlsVersion(
            self,
            request: models.SetTlsVersionRequest,
            opts: Dict = None,
    ) -> models.SetTlsVersionResponse:
        """
        设置监听器TLS配置
        """
        
        kwargs = {}
        kwargs["action"] = "SetTlsVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTlsVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)