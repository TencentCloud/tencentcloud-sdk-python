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
from tencentcloud.teo.v20220901 import models
from typing import Dict


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'

    async def ApplyFreeCertificate(
            self,
            request: models.ApplyFreeCertificateRequest,
            opts: Dict = None,
    ) -> models.ApplyFreeCertificateResponse:
        """
        申请免费证书时，如果您需要通过使用 DNS 委派验证或者文件验证进行申请，您可以调用该接口来进行发起证书申请并根据申请方式来获取对应的验证内容。调用接口的顺序如下：
        第一步：调用 ApplyFreeCertificate，指定申请免费证书的校验方式，获取验证内容；
        第二步：为相应域名按照验证内容配置；
        第三步：调用CheckFreeCertificateVerification 验证，验证通过后即完成免费证书申请；
        第四步：调用ModifyHostsCertificate，下发域名证书为使用 EdgeOne 免费证书配置。

        申请方式的介绍可参考文档：[免费证书申请说明](https://cloud.tencent.com/document/product/1552/90437)
        说明：
        - 仅 CNAME 接入模式可调用该接口来指定免费证书申请方式。NS/DNSPod 托管接入模式都是使用自动验证来申请免费证书，无需调用该接口。
        - 如果您需要切换免费证书验证方式，您可以重新调用本接口通过修改 VerificationMethod 字段来进行变更。
        - 同个域名只能申请一本免费证书，在调用本接口后，后台会触发申请免费证书相关任务，您需要在2 天内，完成域名验证信息的相关配置，然后完成证书验证。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyFreeCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyFreeCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSecurityTemplateToEntity(
            self,
            request: models.BindSecurityTemplateToEntityRequest,
            opts: Dict = None,
    ) -> models.BindSecurityTemplateToEntityResponse:
        """
        操作安全策略模板，支持将域名绑定或换绑到指定的策略模板，或者从指定的策略模板解绑。
        """
        
        kwargs = {}
        kwargs["action"] = "BindSecurityTemplateToEntity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSecurityTemplateToEntityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSharedCNAME(
            self,
            request: models.BindSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.BindSharedCNAMEResponse:
        """
        用于加速域名绑定或解绑共享 CNAME，该功能白名单内测中。
        """
        
        kwargs = {}
        kwargs["action"] = "BindSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindZoneToPlan(
            self,
            request: models.BindZoneToPlanRequest,
            opts: Dict = None,
    ) -> models.BindZoneToPlanResponse:
        """
        将未绑定套餐的站点绑定到已有套餐
        """
        
        kwargs = {}
        kwargs["action"] = "BindZoneToPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindZoneToPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCnameStatus(
            self,
            request: models.CheckCnameStatusRequest,
            opts: Dict = None,
    ) -> models.CheckCnameStatusResponse:
        """
        校验域名 CNAME 状态
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCnameStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCnameStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFreeCertificateVerification(
            self,
            request: models.CheckFreeCertificateVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckFreeCertificateVerificationResponse:
        """
        该接口用于验证免费证书并获取免费证书申请结果。如果验证通过，可通过该接口查询到对应域名申请的免费证书信息，如果申请失败，该接口将返回对应的验证失败信息。
        在触发[申请免费证书接口](https://cloud.tencent.com/document/product/1552/90437)后，您可以通过本接口检查免费证书申请结果。在免费证书申请成功后， 还需要通过[配置域名证书](https://cloud.tencent.com/document/product/1552/80764)接口配置，才能将免费证书部署至加速域上。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFreeCertificateVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFreeCertificateVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmMultiPathGatewayOriginACL(
            self,
            request: models.ConfirmMultiPathGatewayOriginACLRequest,
            opts: Dict = None,
    ) -> models.ConfirmMultiPathGatewayOriginACLResponse:
        """
        本接口用于多通道安全加速网关回源 IP 网段发生变更时，确认已将最新回源 IP 网段更新至源站防火墙。
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmMultiPathGatewayOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmMultiPathGatewayOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmOriginACLUpdate(
            self,
            request: models.ConfirmOriginACLUpdateRequest,
            opts: Dict = None,
    ) -> models.ConfirmOriginACLUpdateResponse:
        """
        本接口用于回源 IP 网段发生变更时，确认已将最新回源 IP 网段更新至源站防火墙。确认已更新至最新的回源 IP 网段后，相关变更通知将会停止推送。
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmOriginACLUpdate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmOriginACLUpdateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccelerationDomain(
            self,
            request: models.CreateAccelerationDomainRequest,
            opts: Dict = None,
    ) -> models.CreateAccelerationDomainResponse:
        """
        在创建完站点之后，您可以通过本接口创建加速域名。

        CNAME 模式接入时，若您未完成站点归属权校验，本接口将为您返回域名归属权验证信息，您可以单独对域名进行归属权验证，详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccelerationDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccelerationDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAliasDomain(
            self,
            request: models.CreateAliasDomainRequest,
            opts: Dict = None,
    ) -> models.CreateAliasDomainResponse:
        """
        创建别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxy(
            self,
            request: models.CreateApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版 [创建四层代理实例](https://cloud.tencent.com/document/product/1552/103417) 。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxyRule(
            self,
            request: models.CreateApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyRuleResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [创建四层代理转发规则
        ](https://cloud.tencent.com/document/product/1552/103416) 。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSIndex(
            self,
            request: models.CreateCLSIndexRequest,
            opts: Dict = None,
    ) -> models.CreateCLSIndexResponse:
        """
        针对指定实时日志投递任务（task-id），在对应的腾讯云 CLS 日志主题中创建投递日志字段对应的键值索引。如果您在腾讯云 CLS 已经创建索引，本接口将采用合并的方式追加索引。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigGroupVersion(
            self,
            request: models.CreateConfigGroupVersionRequest,
            opts: Dict = None,
    ) -> models.CreateConfigGroupVersionResponse:
        """
        在版本管理模式下，用于创建指定配置组的新版本。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigGroupVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigGroupVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContentIdentifier(
            self,
            request: models.CreateContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.CreateContentIdentifierResponse:
        """
        创建内容标识符，可以设置描述、标签等信息，同时需要绑定企业版套餐用于统计计费数据；一个内容标识符只能绑定一个计费套餐，一个计费套餐可以绑定多个内容标识符。该功能仅限白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomizeErrorPage(
            self,
            request: models.CreateCustomizeErrorPageRequest,
            opts: Dict = None,
    ) -> models.CreateCustomizeErrorPageResponse:
        """
        创建自定义错误页面。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomizeErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomizeErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDnsRecord(
            self,
            request: models.CreateDnsRecordRequest,
            opts: Dict = None,
    ) -> models.CreateDnsRecordResponse:
        """
        在创建完站点后，并且站点为 NS 模式接入时，您可以通过本接口创建 DNS 记录。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDnsRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDnsRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunction(
            self,
            request: models.CreateFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionResponse:
        """
        创建并部署边缘函数至 EdgeOne 的边缘节点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunctionRule(
            self,
            request: models.CreateFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionRuleResponse:
        """
        创建边缘函数的触发规则。支持通过自定义过滤条件来决定是否需要执行函数，当需要执行函数时，提供了多种选择目标函数的方式，包括：直接指定，基于客户端归属地区选择和基于权重选择。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunctionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJustInTimeTranscodeTemplate(
            self,
            request: models.CreateJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateJustInTimeTranscodeTemplateResponse:
        """
        即时转码已经提供了预置转码模板，满足大部分的需求。如果有个性化的转码需求，可以通过本接口创建自定义的转码模板，最多可创建100个自定义转码模板。
        为了确保即时转码效果的一致性，避免因 EO 缓存或 M3U8 分片处理过程中的模板变更导致视频输出异常，模板在创建后不可进行修改。
        即时转码详细能力了解：[EdgeOne视频即时处理功能介绍](https://cloud.tencent.com/document/product/1552/111927)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4Proxy(
            self,
            request: models.CreateL4ProxyRequest,
            opts: Dict = None,
    ) -> models.CreateL4ProxyResponse:
        """
        用于创建四层代理实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4ProxyRules(
            self,
            request: models.CreateL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.CreateL4ProxyRulesResponse:
        """
        用于创建四层代理实例规则，支持单条或者批量创建。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7AccRules(
            self,
            request: models.CreateL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.CreateL7AccRulesResponse:
        """
        本接口用于在[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中创建规则，支持批量创建。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        创建负载均衡实例。详情请参考 [快速创建负载均衡实例](https://cloud.tencent.com/document/product/1552/104223)。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGateway(
            self,
            request: models.CreateMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewayResponse:
        """
        通过本接口创建多通道安全加速网关，包括云上网关（腾讯云创建和管理的网关）和自有网关（用户部署的私有网关），需要通过接口 DescribeMultiPathGateway，查询状态为 online 即创建成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGatewayLine(
            self,
            request: models.CreateMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewayLineResponse:
        """
        通过本接口创建接入多通道安全加速网关的线路。包括 EdgeOne 四层代理线路、自定义线路。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGatewaySecretKey(
            self,
            request: models.CreateMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewaySecretKeyResponse:
        """
        通过本接口创建接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关。每个站点下只有一个密钥，可用于接入该站点下的所有网关，可通过接口 DescribeMultiPathGatewaySecretKey 查询。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOriginGroup(
            self,
            request: models.CreateOriginGroupRequest,
            opts: Dict = None,
    ) -> models.CreateOriginGroupResponse:
        """
        创建源站组，以源站组的方式管理业务源站。此处配置的源站组可于**添加加速域名**和**四层代理**等功能中引用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlan(
            self,
            request: models.CreatePlanRequest,
            opts: Dict = None,
    ) -> models.CreatePlanResponse:
        """
        若您需要使用 Edgeone 产品，您需要通过此接口创建计费套餐。
        > 创建套餐后，您需要通过 [CreateZone](https://cloud.tencent.com/document/product/1552/80719) 完成创建站点，绑定套餐的流程，Edgeone 才能正常提供服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlanForZone(
            self,
            request: models.CreatePlanForZoneRequest,
            opts: Dict = None,
    ) -> models.CreatePlanForZoneResponse:
        """
        为未购买套餐的站点购买套餐
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlanForZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePlanForZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrefetchTask(
            self,
            request: models.CreatePrefetchTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePrefetchTaskResponse:
        """
        创建预热任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrefetchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrefetchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePurgeTask(
            self,
            request: models.CreatePurgeTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePurgeTaskResponse:
        """
        当源站资源更新，但节点缓存 TTL 未过期时，用户仍会访问到旧的资源，此时可以通过该接口实现节点资源更新。触发更新的方法有以下两种：<li>直接删除：不做任何校验，直接删除节点缓存，用户请求时触发回源拉取；</li><li>标记过期：将节点资源置为过期，用户请求时触发回源校验，即发送带有 If-None-Match 和 If-Modified-Since 头部的 HTTP 条件请求。若源站响应 200，则节点会回源拉取新的资源并更新缓存；若源站响应 304，则节点不会更新缓存；</li>

        清除缓存任务详情请查看[清除缓存](https://cloud.tencent.com/document/product/1552/70759)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePurgeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePurgeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRealtimeLogDeliveryTask(
            self,
            request: models.CreateRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRealtimeLogDeliveryTaskResponse:
        """
        本接口用于创建实时日志投递任务。本接口有如下限制：
        - 当数据投递类型（LogType）为站点加速日志（七层访问日志）、四层代理日志、边缘函数运行日志时，同一个实体（七层域名、四层代理实例、边缘函数实例）在同种数据投递类型（LogType）和数据投递区域（Area）的组合下，只能被添加到如下实时日志投递任务类型（TaskType）组合中：
            - 一个推送至腾讯云  CLS 的任务，加上另一个推送至自定义 HTTP(S) 地址的任务；
            - 一个推送至腾讯云  CLS 的任务，加上另一个推送至 AWS S3 兼容对象存储的任务；
        - 当数据投递类型（LogType）为速率限制和 CC 攻击防护日志、托管规则日志、自定义规则日志、Bot 管理日志时，同一个实体在同种数据投递类型（LogType）和数据投递区域（Area）的组合下，只能被添加到一个实时日志投递任务中。
        - 当实时日志投递任务类型（TaskType）为 EdgeOne 日志分析（log_analysis）时，只支持数据投递类型（LogType）为站点加速日志（domain）；在同一站点（ZoneId）和数据投递区域（Area）的组合下，只能添加一个推送至 EdgeOne 日志分析的实时日志投递任务；。

        建议先通过 [DescribeRealtimeLogDeliveryTasks](https://cloud.tencent.com/document/product/1552/104110)  接口根据实体查询实时日志投递任务列表，检查实体是否已经被添加到另一实时日志投递任务中。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        本接口为旧版本创建规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本创建七层加速规则接口详情请参考 [CreateL7AccRules](https://cloud.tencent.com/document/product/1552/115822)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAPIResource(
            self,
            request: models.CreateSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAPIResourceResponse:
        """
        用于创建 API 资源。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAPIService(
            self,
            request: models.CreateSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAPIServiceResponse:
        """
        用于创建 API 服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityClientAttester(
            self,
            request: models.CreateSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityClientAttesterResponse:
        """
        创建客户端认证选项。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityIPGroup(
            self,
            request: models.CreateSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityIPGroupResponse:
        """
        创建安全 IP 组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityJSInjectionRule(
            self,
            request: models.CreateSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityJSInjectionRuleResponse:
        """
        创建 JavaScript 注入规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSharedCNAME(
            self,
            request: models.CreateSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.CreateSharedCNAMEResponse:
        """
        用于创建共享 CNAME，该功能白名单内测中。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebSecurityTemplate(
            self,
            request: models.CreateWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateWebSecurityTemplateResponse:
        """
        创建安全策略配置模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateZone(
            self,
            request: models.CreateZoneRequest,
            opts: Dict = None,
    ) -> models.CreateZoneResponse:
        """
        EdgeOne 为您提供 CNAME、NS 和无域名接入三种接入方式，您需要先通过此接口完成站点创建。CNAME 和 NS 接入站点的场景可参考 [从零开始快速接入 EdgeOne](https://cloud.tencent.com/document/product/1552/87601); 无域名接入的场景可参考 [快速启用四层代理服务](https://cloud.tencent.com/document/product/1552/96051)。

        > 建议您在账号下已存在套餐时调用本接口创建站点，请在入参时传入 PlanId ，直接将站点绑定至该套餐；不传入 PlanId 时，创建出来的站点会处于未激活状态，无法正常服务，您需要通过 [BindZoneToPlan](https://cloud.tencent.com/document/product/1552/83042) 完成套餐绑定之后，站点才可正常提供服务 。若您当前没有可绑定的套餐时，请前往控制台购买套餐完成站点创建。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccelerationDomains(
            self,
            request: models.DeleteAccelerationDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccelerationDomainsResponse:
        """
        批量删除加速域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccelerationDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccelerationDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAliasDomain(
            self,
            request: models.DeleteAliasDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteAliasDomainResponse:
        """
        删除别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxy(
            self,
            request: models.DeleteApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [删除四层代理实例
        ](https://cloud.tencent.com/document/product/1552/103415) 。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxyRule(
            self,
            request: models.DeleteApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyRuleResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [删除四层代理转发规则](https://cloud.tencent.com/document/product/1552/103414) 。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContentIdentifier(
            self,
            request: models.DeleteContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.DeleteContentIdentifierResponse:
        """
        删除指定的内容标识符。该功能仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomErrorPage(
            self,
            request: models.DeleteCustomErrorPageRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomErrorPageResponse:
        """
        删除自定义错误页面。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDnsRecords(
            self,
            request: models.DeleteDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteDnsRecordsResponse:
        """
        您可以用本接口批量删除 DNS 记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunction(
            self,
            request: models.DeleteFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionResponse:
        """
        删除边缘函数，删除后函数无法恢复，关联的触发规则会一并删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunctionRules(
            self,
            request: models.DeleteFunctionRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionRulesResponse:
        """
        删除边缘函数触发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunctionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJustInTimeTranscodeTemplates(
            self,
            request: models.DeleteJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteJustInTimeTranscodeTemplatesResponse:
        """
        根据站点 id 下唯一的模板标识，删除相应的即时转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4Proxy(
            self,
            request: models.DeleteL4ProxyRequest,
            opts: Dict = None,
    ) -> models.DeleteL4ProxyResponse:
        """
        用于删除四层代理实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4ProxyRules(
            self,
            request: models.DeleteL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL4ProxyRulesResponse:
        """
        用于删除四层代理转发规则，支持单条或者批量操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7AccRules(
            self,
            request: models.DeleteL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL7AccRulesResponse:
        """
        本接口用于删除[规则引擎](https://cloud.tencent.com/document/product/1552/70901)的规则，支持批量删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        删除负载均衡实例，若负载均衡示例被其他服务（例如：四层代理等）引用的时候，示例无法被删除，需要先解除引用关系。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultiPathGateway(
            self,
            request: models.DeleteMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteMultiPathGatewayResponse:
        """
        通过本接口删除多通道安全加速网关，包括自有网关和云上网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultiPathGatewayLine(
            self,
            request: models.DeleteMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.DeleteMultiPathGatewayLineResponse:
        """
        通过本接口删除接入多通道安全加速网关的线路，仅自定义线路支持删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOriginGroup(
            self,
            request: models.DeleteOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteOriginGroupResponse:
        """
        删除源站组，若源站组仍然被服务（例如：四层代理，域名服务，负载均衡，规则引起）引用，将不允许删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRealtimeLogDeliveryTask(
            self,
            request: models.DeleteRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRealtimeLogDeliveryTaskResponse:
        """
        通过本接口删除实时日志投递任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRules(
            self,
            request: models.DeleteRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRulesResponse:
        """
        本接口为旧版本删除规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本删除七层加速规则接口详情请参考 [DeleteL7AccRules](https://cloud.tencent.com/document/product/1552/115821)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAPIResource(
            self,
            request: models.DeleteSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAPIResourceResponse:
        """
        用于删除 API 资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAPIService(
            self,
            request: models.DeleteSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAPIServiceResponse:
        """
        用于删除 API 服务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityClientAttester(
            self,
            request: models.DeleteSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityClientAttesterResponse:
        """
        删除客户端认证选项。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityIPGroup(
            self,
            request: models.DeleteSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityIPGroupResponse:
        """
        删除指定 IP 组，如果有规则引用了 IP 组情况，则不允许删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityJSInjectionRule(
            self,
            request: models.DeleteSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityJSInjectionRuleResponse:
        """
        删除 JavaScript 注入规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSharedCNAME(
            self,
            request: models.DeleteSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.DeleteSharedCNAMEResponse:
        """
        用于删除共享 CNAME，该功能白名单内测中。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebSecurityTemplate(
            self,
            request: models.DeleteWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteWebSecurityTemplateResponse:
        """
        删除安全策略配置模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteZone(
            self,
            request: models.DeleteZoneRequest,
            opts: Dict = None,
    ) -> models.DeleteZoneResponse:
        """
        删除站点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployConfigGroupVersion(
            self,
            request: models.DeployConfigGroupVersionRequest,
            opts: Dict = None,
    ) -> models.DeployConfigGroupVersionResponse:
        """
        在版本管理模式下，用于版本发布，可通过 EnvId 将版本发布至测试环境或生产环境。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DeployConfigGroupVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployConfigGroupVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerationDomains(
            self,
            request: models.DescribeAccelerationDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerationDomainsResponse:
        """
        您可以通过本接口查看站点下的域名信息，包括加速域名、源站以及域名状态等信息。您可以查看站点下全部域名的信息，也可以指定过滤条件查询对应的域名信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerationDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerationDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAliasDomains(
            self,
            request: models.DescribeAliasDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeAliasDomainsResponse:
        """
        查询别称域名信息列表。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAliasDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAliasDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProxies(
            self,
            request: models.DescribeApplicationProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProxiesResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，新版接口中将四层代理实例列表的查询和四层转发规则的查询拆分成两个接口，详情请参考 [查询四层代理实例列表](https://cloud.tencent.com/document/product/1552/103413) 和 [查询四层代理转发规则列表](https://cloud.tencent.com/document/product/1552/103412)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailablePlans(
            self,
            request: models.DescribeAvailablePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailablePlansResponse:
        """
        查询当前账户可用套餐信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailablePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailablePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingData(
            self,
            request: models.DescribeBillingDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingDataResponse:
        """
        通过本接口查询计费数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigGroupVersionDetail(
            self,
            request: models.DescribeConfigGroupVersionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigGroupVersionDetailResponse:
        """
        在版本管理模式下，用于获取版本的详细信息，包括版本 ID、描述、状态、创建时间、所属配置组信息以及版本配置文件的内容。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigGroupVersionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigGroupVersionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigGroupVersions(
            self,
            request: models.DescribeConfigGroupVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigGroupVersionsResponse:
        """
        在版本管理模式下，用于查询指定配置组的版本列表。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigGroupVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigGroupVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentIdentifiers(
            self,
            request: models.DescribeContentIdentifiersRequest,
            opts: Dict = None,
    ) -> models.DescribeContentIdentifiersResponse:
        """
        批量查询内容标识符，可以根据 ID、描述、状态或者标签过滤。按照状态查询被删除的内容标识符仅保留三个月。该功能仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentIdentifiers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentIdentifiersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentQuota(
            self,
            request: models.DescribeContentQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeContentQuotaResponse:
        """
        查询内容管理接口配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomErrorPages(
            self,
            request: models.DescribeCustomErrorPagesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomErrorPagesResponse:
        """
        查询自定义错误页列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomErrorPages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomErrorPagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackData(
            self,
            request: models.DescribeDDoSAttackDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackDataResponse:
        """
        本接口（DescribeDDoSAttackData）用于查询DDoS攻击时序数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackEvent(
            self,
            request: models.DescribeDDoSAttackEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackEventResponse:
        """
        本接口（DescribeDDoSAttackEvent）用于查询DDoS攻击事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackTopData(
            self,
            request: models.DescribeDDoSAttackTopDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackTopDataResponse:
        """
        本接口（DescribeDDoSAttackTopData）用于查询DDoS攻击Top数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSProtection(
            self,
            request: models.DescribeDDoSProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSProtectionResponse:
        """
        获取站点的独立 DDoS 防护信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultCertificates(
            self,
            request: models.DescribeDefaultCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultCertificatesResponse:
        """
        查询默认证书列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployHistory(
            self,
            request: models.DescribeDeployHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeployHistoryResponse:
        """
        在版本管理模式下，用于查询生产/测试环境的版本发布历史。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeployHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnsRecords(
            self,
            request: models.DescribeDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDnsRecordsResponse:
        """
        您可以用过本接口查看站点下的 DNS 记录信息，包括 DNS 记录名、记录类型以及记录内容等信息，支持指定过滤条件查询对应的 DNS 记录信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        在版本管理模式下，用于查询环境信息，可获取环境 ID、类型、当前生效版本等。版本管理功能内测中，当前仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionRules(
            self,
            request: models.DescribeFunctionRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionRulesResponse:
        """
        查询边缘函数触发规则列表，支持按照规则 ID、函数 ID、规则描述等条件进行过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionRuntimeEnvironment(
            self,
            request: models.DescribeFunctionRuntimeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionRuntimeEnvironmentResponse:
        """
        查询边缘函数运行环境，包括环境变量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionRuntimeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionRuntimeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctions(
            self,
            request: models.DescribeFunctionsRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionsResponse:
        """
        查询边缘函数列表，支持函数 ID、函数名称、描述等条件的过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostsSetting(
            self,
            request: models.DescribeHostsSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsSettingResponse:
        """
        本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，可通过 [DescribeL7AccSetting](https://cloud.tencent.com/document/product/1552/115819) 和 [DescribeL7AccRules](https://cloud.tencent.com/document/product/1552/115820) 来获取域名的详细配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPRegion(
            self,
            request: models.DescribeIPRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeIPRegionResponse:
        """
        该接口可用于查询 IP 是否为 EdgeOne IP。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdentifications(
            self,
            request: models.DescribeIdentificationsRequest,
            opts: Dict = None,
    ) -> models.DescribeIdentificationsResponse:
        """
        查询站点的验证信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentifications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentificationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJustInTimeTranscodeTemplates(
            self,
            request: models.DescribeJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeJustInTimeTranscodeTemplatesResponse:
        """
        根据即时转码模板名字、模板类型或唯一标识，获取即时转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及预置模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4Proxy(
            self,
            request: models.DescribeL4ProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ProxyResponse:
        """
        用于查询四层代理实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4ProxyRules(
            self,
            request: models.DescribeL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ProxyRulesResponse:
        """
        查询四层代理实例下的转发规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7AccRules(
            self,
            request: models.DescribeL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeL7AccRulesResponse:
        """
        本接口用于查询[规则引擎](https://cloud.tencent.com/document/product/1552/70901)的规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7AccSetting(
            self,
            request: models.DescribeL7AccSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeL7AccSettingResponse:
        """
        本接口用于查询[站点加速](https://cloud.tencent.com/document/product/1552/96193)全局配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7AccSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7AccSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerList(
            self,
            request: models.DescribeLoadBalancerListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerListResponse:
        """
        查询负载均衡实例列表。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGateway(
            self,
            request: models.DescribeMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayResponse:
        """
        通过本接口查询多通道安全加速网关详情。如名称、网关 ID、IP、端口、类型等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayLine(
            self,
            request: models.DescribeMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayLineResponse:
        """
        通过本接口查询接入多通道安全加速网关的线路。包括直连、EdgeOne 四层代理线路、自定义线路。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayOriginACL(
            self,
            request: models.DescribeMultiPathGatewayOriginACLRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayOriginACLResponse:
        """
        本接口用于查询多通道安全加速网关实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。若 MultiPathGatewayNextOriginACL 字段有返回值，则需要将最新的回源 IP 网段同步到源站防火墙配置中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayRegions(
            self,
            request: models.DescribeMultiPathGatewayRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayRegionsResponse:
        """
        通过本接口查询用户创建的多通道安全加速网关（云上网关）的可用地域列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewaySecretKey(
            self,
            request: models.DescribeMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewaySecretKeyResponse:
        """
        通过本接口查询接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGateways(
            self,
            request: models.DescribeMultiPathGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewaysResponse:
        """
        通过本接口查询用户创建的多通道安全加速网关列表。支持翻页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginACL(
            self,
            request: models.DescribeOriginACLRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginACLResponse:
        """
        本接口用于查询站点下的七层加速域名/四层代理实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。如果您想通过自动化脚本定期获取回源 IP 网段的最新版本，可以较低频率（建议每三天一次）轮询本接口，若 NextOriginACL 字段有返回值，则将最新的回源 IP 网段同步到源站防火墙配置中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroup(
            self,
            request: models.DescribeOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupResponse:
        """
        获取源站组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroupHealthStatus(
            self,
            request: models.DescribeOriginGroupHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupHealthStatusResponse:
        """
        查询负载均衡实例下源站组健康状态。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroupHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginProtection(
            self,
            request: models.DescribeOriginProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginProtectionResponse:
        """
        本接口为旧版本查询源站防护接口，EdgeOne 于 2025 年 6 月 27 日已对源站防护相关接口全面升级，新版本查询源站防护接口详情请参考 [DescribeOriginACL](https://cloud.tencent.com/document/product/1552/120408)。

        <p style="color: red;">注意：自 2025 年 6 月 27 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版源站防护接口。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewL7Data(
            self,
            request: models.DescribeOverviewL7DataRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewL7DataResponse:
        """
        本接口（DescribeOverviewL7Data）用于查询七层监控类时序流量数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80648">DescribeTimingL7AnalysisData</a> 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewL7Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewL7DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlans(
            self,
            request: models.DescribePlansRequest,
            opts: Dict = None,
    ) -> models.DescribePlansResponse:
        """
        查询套餐信息列表，支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchOriginLimit(
            self,
            request: models.DescribePrefetchOriginLimitRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchOriginLimitResponse:
        """
        本接口用于查询回源限速限制，该功能白名单内测中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchOriginLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchOriginLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchTasks(
            self,
            request: models.DescribePrefetchTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchTasksResponse:
        """
        DescribePrefetchTasks 用于查询预热任务提交历史记录及执行进度，通过 CreatePrefetchTasks 接口提交的任务可通过此接口进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 CreatePurgeTasks 接口提交的任务均可通过此接口进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealtimeLogDeliveryTasks(
            self,
            request: models.DescribeRealtimeLogDeliveryTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRealtimeLogDeliveryTasksResponse:
        """
        通过本接口查询实时日志投递任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealtimeLogDeliveryTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealtimeLogDeliveryTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        本接口为旧版本查询规则引擎规则接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本查询七层加速规则接口详情请参考  [DescribeL7AccRules](https://cloud.tencent.com/document/product/1552/115820)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesSetting(
            self,
            request: models.DescribeRulesSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesSettingResponse:
        """
        本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [RuleEngineAction](https://cloud.tencent.com/document/product/1552/80721#RuleEngineAction)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAPIResource(
            self,
            request: models.DescribeSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAPIResourceResponse:
        """
        查询站点下的 API 资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAPIService(
            self,
            request: models.DescribeSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAPIServiceResponse:
        """
        查询站点下的 API 服务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityClientAttester(
            self,
            request: models.DescribeSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityClientAttesterResponse:
        """
        查询客户端认证选项配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroup(
            self,
            request: models.DescribeSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupResponse:
        """
        查询安全 IP 组的配置信息，包括安全 IP 组的 ID、名称和内容。本接口的查询结果中，每个 IP 组最多只返回 2000 个 IP / 网段。如果存在超过 2000 个 IP / 网段的超大 IP 组，请调用 DescribeSecurityIPGroupContent 进行分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroupContent(
            self,
            request: models.DescribeSecurityIPGroupContentRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupContentResponse:
        """
        该接口用于分页查询指定 IP 组中的 IP 地址列表。当 IP 组中的 IP 地址数量超过 2000 个时，可以使用此接口进行分页查询，以获取完整的 IP 地址列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroupContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroupInfo(
            self,
            request: models.DescribeSecurityIPGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupInfoResponse:
        """
        接口已废弃，将于 2024 年 6 月 30 日停止服务。请使用 [查询安全 IP 组
        ](https://cloud.tencent.com/document/product/1552/105866) 接口。

        查询 IP 组的配置信息，包括 IP 组名称、 IP 组内容、 IP 组归属站点。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityJSInjectionRule(
            self,
            request: models.DescribeSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityJSInjectionRuleResponse:
        """
        查询 JavaScript 注入规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicy(
            self,
            request: models.DescribeSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyResponse:
        """
        查询安全防护配置详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTemplateBindings(
            self,
            request: models.DescribeSecurityTemplateBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTemplateBindingsResponse:
        """
        查询指定策略模板的绑定关系列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTemplateBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTemplateBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL4Data(
            self,
            request: models.DescribeTimingL4DataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL4DataResponse:
        """
        本接口（DescribeTimingL4Data）用于查询四层时序流量数据列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL4Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL4DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7AnalysisData(
            self,
            request: models.DescribeTimingL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7AnalysisDataResponse:
        """
        本接口用于查询七层域名业务的时序数据。
        注意：
        1. 本接口查询数据有 10 分钟左右延迟，建议拉取当前时间 10 分钟以前的数据。
        2. 本接口默认返回防护后的流量请求数据，用户可在 `Filters.mitigatedByWebSecurity` 中自定义查询已防护缓释的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7CacheData(
            self,
            request: models.DescribeTimingL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7CacheDataResponse:
        """
        本接口用于查询七层缓存分析时序类流量数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80648">DescribeTimingL7AnalysisData</a> 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7OriginPullData(
            self,
            request: models.DescribeTimingL7OriginPullDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7OriginPullDataResponse:
        """
        本接口用以查询七层域名业务的回源时序数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7OriginPullData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7OriginPullDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7AnalysisData(
            self,
            request: models.DescribeTopL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7AnalysisDataResponse:
        """
        本接口用于查询七层域名业务按照指定维度的 topN 数据。
        注意：
        1. 本接口查询数据有 10 分钟左右延迟，建议拉取当前时间 10 分钟以前的数据。
        2. 本接口默认返回防护后的流量请求数据，用户可在 `Filters.mitigatedByWebSecurity` 中自定义查询已防护缓释的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7CacheData(
            self,
            request: models.DescribeTopL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7CacheDataResponse:
        """
        本接口用于查询七层缓存分析 topN 数据。此接口待废弃，请使用 <a href="https://cloud.tencent.com/document/product/1552/80646"> DescribeTopL7AnalysisData</a> 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebSecurityTemplate(
            self,
            request: models.DescribeWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeWebSecurityTemplateResponse:
        """
        查询安全策略配置模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebSecurityTemplates(
            self,
            request: models.DescribeWebSecurityTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeWebSecurityTemplatesResponse:
        """
        查询安全策略配置模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebSecurityTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebSecurityTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneConfigImportResult(
            self,
            request: models.DescribeZoneConfigImportResultRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneConfigImportResultResponse:
        """
        查询站点配置项导入结果接口，本接口用于站点配置导入接口（ImportZoneConfig）的结果查询。该功能仅支持标准版或企业版套餐的站点使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneConfigImportResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneConfigImportResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneSetting(
            self,
            request: models.DescribeZoneSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneSettingResponse:
        """
        本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [DescribeL7AccSetting](https://cloud.tencent.com/document/product/1552/115819)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        该接口用于查询您有权限的站点信息。可根据不同查询条件筛选站点。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPlan(
            self,
            request: models.DestroyPlanRequest,
            opts: Dict = None,
    ) -> models.DestroyPlanResponse:
        """
        当您需要停止 Edgeone 套餐的计费，可以通过该接口销毁计费套餐。
        > 销毁计费套餐需要满足以下条件：
            1.套餐已过期（企业版套餐除外）；
            2.套餐下所有站点均已关闭或删除。

        > 站点状态可以通过 [查询站点列表](https://cloud.tencent.com/document/product/1552/80713) 接口进行查询
        停用站点可以通过 [切换站点状态](https://cloud.tencent.com/document/product/1552/80707) 接口将站点切换至关闭状态
        删除站点可以通过 [删除站点](https://cloud.tencent.com/document/product/1552/80717) 接口将站点删除
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableOriginACL(
            self,
            request: models.DisableOriginACLRequest,
            opts: Dict = None,
    ) -> models.DisableOriginACLResponse:
        """
        本接口用于关闭站点的源站防护功能。停用后，相关资源不再仅使用「源站防护」提供的回源 IP 网段请求您的源站，同时停止发送回源 IP 网段更新通知。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadL4Logs(
            self,
            request: models.DownloadL4LogsRequest,
            opts: Dict = None,
    ) -> models.DownloadL4LogsResponse:
        """
        本接口（DownloadL4Logs）用于下载四层离线日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL4Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL4LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadL7Logs(
            self,
            request: models.DownloadL7LogsRequest,
            opts: Dict = None,
    ) -> models.DownloadL7LogsResponse:
        """
        本接口（DownloadL7Logs）下载七层离线日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL7Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL7LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableOriginACL(
            self,
            request: models.EnableOriginACLRequest,
            opts: Dict = None,
    ) -> models.EnableOriginACLResponse:
        """
        本接口用于站点首次开启源站防护，启用后 EdgeOne 将会使用特定的回源 IP 网段为七层加速域名/四层代理实例回源。单次支持提交的七层加速域名的数量最大为 200，四层代理实例的数量最大为 100，支持七层加速域名/四层代理实例混合提交，总实例个数最大为 200。如需要启用超过 200 个资源，可先通过指定资源的方式以最大数量启用，剩余资源通过 ModifyOriginACL 接口启用。后续新增七层加速域名/四层代理实例均请通过 ModifyOriginACL 接口配置。

        注意：
        - 调用本接口视为同意 [源站防护启用特别约定](https://cloud.tencent.com/document/product/1552/120141)；
        - 回源 IP 网段会不定期变更，EdgeOne 将在回源 IP 网段变更前 14 天、前 7 天、前 3 天和前 1 天分别通过站内信、短信、邮件等一种或多种方式发起通知，为了能正常收到回源 IP 网段的变更通知，请务必确保您在 [腾讯云消息中心控制台](https://console.cloud.tencent.com/message)内，已勾选边缘安全加速平台 EO 的产品服务相关消息通知，并配置正确的消息接收人。配置方式请参考 [消息订阅管理](https://cloud.tencent.com/document/product/567/43476)。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportZoneConfig(
            self,
            request: models.ExportZoneConfigRequest,
            opts: Dict = None,
    ) -> models.ExportZoneConfigResponse:
        """
        导出站点配置接口，本接口支持用户根据需要的配置项进行配置导出，导出的配置用于导入站点配置接口（ImportZoneConfig）进行配置导入。该功能仅支持标准版和企业版套餐站点使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleFunctionRuntimeEnvironment(
            self,
            request: models.HandleFunctionRuntimeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.HandleFunctionRuntimeEnvironmentResponse:
        """
        操作边缘函数运行环境，支持环境变量的相关设置。
        设置环境变量后，可在函数代码中使用，具体参考 [边缘函数引入环境变量](https://cloud.tencent.com/document/product/1552/109151#0151fd9a-8b0e-407b-ae37-54553a60ded6)。
        """
        
        kwargs = {}
        kwargs["action"] = "HandleFunctionRuntimeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleFunctionRuntimeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdentifyZone(
            self,
            request: models.IdentifyZoneRequest,
            opts: Dict = None,
    ) -> models.IdentifyZoneResponse:
        """
        用于验证站点所有权。
        """
        
        kwargs = {}
        kwargs["action"] = "IdentifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdentifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportZoneConfig(
            self,
            request: models.ImportZoneConfigRequest,
            opts: Dict = None,
    ) -> models.ImportZoneConfigResponse:
        """
        导入站点配置接口，本接口支持站点配置文件的快速导入，发起导入后接口会返回对应的任务 ID（TaskId），用户需通过查询站点配置导入结果接口（DescribeZoneConfigImportResult）获取本次导入任务执行的结果。该功能仅支持标准版和企业版套餐站点使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IncreasePlanQuota(
            self,
            request: models.IncreasePlanQuotaRequest,
            opts: Dict = None,
    ) -> models.IncreasePlanQuotaResponse:
        """
        当您的套餐绑定的站点数，或配置的 Web 防护 - 自定义规则 - 精准匹配策略的规则数，或 Web 防护 - 速率限制 - 精准速率限制模块的规则数达到套餐允许的配额上限，可以通过该接口增购对应配额。
        > 该接口该仅支持企业版套餐。
        """
        
        kwargs = {}
        kwargs["action"] = "IncreasePlanQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IncreasePlanQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerationDomain(
            self,
            request: models.ModifyAccelerationDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerationDomainResponse:
        """
        修改加速域名信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerationDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerationDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerationDomainStatuses(
            self,
            request: models.ModifyAccelerationDomainStatusesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerationDomainStatusesResponse:
        """
        批量修改加速域名状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerationDomainStatuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerationDomainStatusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAliasDomain(
            self,
            request: models.ModifyAliasDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyAliasDomainResponse:
        """
        修改别称域名。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAliasDomainStatus(
            self,
            request: models.ModifyAliasDomainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAliasDomainStatusResponse:
        """
        修改别称域名状态。
        该功能仅企业版套餐支持，并且该功能当前仍在内测中，如需使用，请[联系我们](https://cloud.tencent.com/online-service?from=connect-us)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAliasDomainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAliasDomainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxy(
            self,
            request: models.ModifyApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理实例
        ](https://cloud.tencent.com/document/product/1552/103411) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRule(
            self,
            request: models.ModifyApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理转发规则
        ](https://cloud.tencent.com/document/product/1552/103410) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRuleStatus(
            self,
            request: models.ModifyApplicationProxyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleStatusResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理转发规则状态
        ](https://cloud.tencent.com/document/product/1552/103409) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyStatus(
            self,
            request: models.ModifyApplicationProxyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyStatusResponse:
        """
        本接口为旧版，如需调用请尽快迁移至新版，详情请参考 [修改四层代理实例状态](https://cloud.tencent.com/document/product/1552/103408) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContentIdentifier(
            self,
            request: models.ModifyContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.ModifyContentIdentifierResponse:
        """
        修改内容标识符，仅支持修改描述。该功能仅白名单开放。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomErrorPage(
            self,
            request: models.ModifyCustomErrorPageRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomErrorPageResponse:
        """
        修改自定义错误页面。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSProtection(
            self,
            request: models.ModifyDDoSProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSProtectionResponse:
        """
        修改站点的独立 DDoS 防护。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnsRecords(
            self,
            request: models.ModifyDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.ModifyDnsRecordsResponse:
        """
        您可以通过本接口批量修改 DNS 记录。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnsRecordsStatus(
            self,
            request: models.ModifyDnsRecordsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDnsRecordsStatusResponse:
        """
        您可以通过本接口批量修改 DNS 记录的状态，批量对记录进行开启和停用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecordsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunction(
            self,
            request: models.ModifyFunctionRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionResponse:
        """
        修改边缘函数，支持修改函数的内容及描述信息，修改且重新部署后，函数立刻生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionRule(
            self,
            request: models.ModifyFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionRuleResponse:
        """
        修改边缘函数触发规则，支持修改规则条件、执行函数以及描述信息。您可以先通过 DescribeFunctionRules 接口来获取需要修改的规则的 RuleId，然后传入修改后的规则内容，原规则内容会被覆盖式更新。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionRulePriority(
            self,
            request: models.ModifyFunctionRulePriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionRulePriorityResponse:
        """
        修改边缘函数触发规则的优先级。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostsCertificate(
            self,
            request: models.ModifyHostsCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyHostsCertificateResponse:
        """
        完成域名创建之后，您可以为域名配置自有证书，也可以使用 EdgeOne 为您提供的 [免费证书](https://cloud.tencent.com/document/product/1552/90437)。
        如果您需要配置自有证书，请先将证书上传至 [SSL证书控制台](https://console.cloud.tencent.com/certoverview)，然后在本接口中传入对应的证书 ID。详情参考 [部署自有证书至 EdgeOne 域名
        ](https://cloud.tencent.com/document/product/1552/88874)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostsCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostsCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Proxy(
            self,
            request: models.ModifyL4ProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyResponse:
        """
        用于修改四层代理实例的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyRules(
            self,
            request: models.ModifyL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyRulesResponse:
        """
        用于修改四层代理转发规则，支持单条或者批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyRulesStatus(
            self,
            request: models.ModifyL4ProxyRulesStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyRulesStatusResponse:
        """
        用于启用/停用四层代理转发规则状态，支持单条或者批量操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyRulesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyRulesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyStatus(
            self,
            request: models.ModifyL4ProxyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyStatusResponse:
        """
        用于启用/停用四层代理实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccRule(
            self,
            request: models.ModifyL7AccRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccRuleResponse:
        """
        本接口用于修改[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中的规则，单次仅支持修改单条规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccRulePriority(
            self,
            request: models.ModifyL7AccRulePriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccRulePriorityResponse:
        """
        本接口用于修改[规则引擎](https://cloud.tencent.com/document/product/1552/70901)中规则列表的优先级，本接口需要传入站点 ID 下完整的规则 ID 列表，规则 ID 列表可以通过[查询七层加速规则](https://cloud.tencent.com/document/product/1552/115820)接口获取，最终优先级顺序将调整成规则 ID 列表的顺序，从前往后执行。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccSetting(
            self,
            request: models.ModifyL7AccSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccSettingResponse:
        """
        本接口用于修改[站点加速](https://cloud.tencent.com/document/product/1552/96193)全局配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancer(
            self,
            request: models.ModifyLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerResponse:
        """
        修改负载均衡实例配置。负载均衡功能内测中，如您需要使用请 [联系我们](https://cloud.tencent.com/online-service)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGateway(
            self,
            request: models.ModifyMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayResponse:
        """
        通过本接口修改多通道安全加速网关信息，如名称、网关 ID、IP、端口等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewayLine(
            self,
            request: models.ModifyMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayLineResponse:
        """
        通过本接口修改接入多通道安全加速网关的线路，包括 EdgeOne 四层代理线路、自定义线路。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewaySecretKey(
            self,
            request: models.ModifyMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewaySecretKeyResponse:
        """
        通过本接口修改接入多通道安全加速网关的密钥，客户基于接入密钥签名接入多通道安全加速网关，修改后原密钥失效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewayStatus(
            self,
            request: models.ModifyMultiPathGatewayStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayStatusResponse:
        """
        更新多通道安全网关状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewayStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOriginACL(
            self,
            request: models.ModifyOriginACLRequest,
            opts: Dict = None,
    ) -> models.ModifyOriginACLResponse:
        """
        本接口用于对七层加速域名/四层代理实例启用/关闭特定回源 IP 网段回源。单次支持提交的七层加速域名的数量最大为 200，四层代理实例的数量最大为 100，支持七层加速域名/四层代理实例混合提交，总实例个数最大为 200。如需变更超过 200 个实例，请通过本接口分批提交。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOriginGroup(
            self,
            request: models.ModifyOriginGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyOriginGroupResponse:
        """
        修改源站组配置，新提交的源站记录将会覆盖原有源站组中的源站记录。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPlan(
            self,
            request: models.ModifyPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyPlanResponse:
        """
        修改套餐配置。目前仅支持修改预付费套餐的自动续费开关。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrefetchOriginLimit(
            self,
            request: models.ModifyPrefetchOriginLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyPrefetchOriginLimitResponse:
        """
        本接口用于配置回源限速限制，该功能白名单内测中。
        可通过此接口创建、修改与删除预热回源限速限制，每个账号最多支持 100 条限制。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrefetchOriginLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrefetchOriginLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealtimeLogDeliveryTask(
            self,
            request: models.ModifyRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRealtimeLogDeliveryTaskResponse:
        """
        通过本接口修改实时日志投递任务配置。本接口有如下限制：<li>不支持修改实时日志投递任务目的地类型（TaskType）；</li><li>不支持修改数据投递类型（LogType）</li><li>不支持修改数据投递区域（Area）</li><li>当原实时日志投递任务的目的地为腾讯云 CLS 时，不支持修改目的地详细配置，如日志集、日志主题。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        本接口为旧版本修改规则引擎接口，EdgeOne 于 2025 年 1 月 21 日已对规则引擎相关接口全面升级，新版本修改七层加速规则接口详情请参考 [ModifyL7AccRule](https://cloud.tencent.com/document/product/1552/115818)。
        <p style="color: red;">注意：自 2025 年 1 月 21 日起，旧版接口停止更新迭代，后续新增功能将仅在新版接口中提供，旧版接口支持的原有能力将不受影响。为避免在使用旧版接口时出现数据字段冲突，建议您尽早迁移到新版规则引擎接口。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityAPIResource(
            self,
            request: models.ModifySecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityAPIResourceResponse:
        """
        该接口用于修改 API 资源。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityAPIService(
            self,
            request: models.ModifySecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityAPIServiceResponse:
        """
        该接口用于修改 API 服务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityClientAttester(
            self,
            request: models.ModifySecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityClientAttesterResponse:
        """
        修改客户端认证选项。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityIPGroup(
            self,
            request: models.ModifySecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityIPGroupResponse:
        """
        修改安全 IP 组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityJSInjectionRule(
            self,
            request: models.ModifySecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityJSInjectionRuleResponse:
        """
        修改 JavaScript 注入规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicy(
            self,
            request: models.ModifySecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyResponse:
        """
        修改Web&Bot安全配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebSecurityTemplate(
            self,
            request: models.ModifyWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyWebSecurityTemplateResponse:
        """
        修改安全策略配置模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZone(
            self,
            request: models.ModifyZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneResponse:
        """
        修改站点信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneSetting(
            self,
            request: models.ModifyZoneSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneSettingResponse:
        """
        本接口为旧版，EdgeOne 已对规则引擎相关接口全面升级，详情请参考 [ModifyL7AccSetting](https://cloud.tencent.com/document/product/1552/115817)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneStatus(
            self,
            request: models.ModifyZoneStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneStatusResponse:
        """
        用于开启，关闭站点。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshMultiPathGatewaySecretKey(
            self,
            request: models.RefreshMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.RefreshMultiPathGatewaySecretKeyResponse:
        """
        通过本接口刷新多通道安全加速网关的密钥。客户基于接入密钥签名接入多通道安全加速网关。每个站点下只有一个密钥，可用于接入该站点下的所有网关，刷新密钥后，原始密钥会失效。
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewPlan(
            self,
            request: models.RenewPlanRequest,
            opts: Dict = None,
    ) -> models.RenewPlanResponse:
        """
        当您的套餐需要延长有效期，可以通过该接口进行续费。套餐续费仅支持个人版，基础版，标准版套餐。
        > 费用详情可参考 [套餐费用](https://cloud.tencent.com/document/product/1552/94158)
        """
        
        kwargs = {}
        kwargs["action"] = "RenewPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradePlan(
            self,
            request: models.UpgradePlanRequest,
            opts: Dict = None,
    ) -> models.UpgradePlanResponse:
        """
        当您需要使用高等级套餐才拥有的功能，可以通过本接口升级套餐，仅支持个人版，基础版套餐进行升级。
        > 不同类型 Edgeone 计费套餐区别参考 [Edgeone计费套餐选型对比](https://cloud.tencent.com/document/product/1552/94165)
        计费套餐升级规则以及资费详情参考 [Edgeone计费套餐升配说明](https://cloud.tencent.com/document/product/1552/95291)
        如果需要将套餐升级至企业版，请 [联系我们](https://cloud.tencent.com/online-service)
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyOwnership(
            self,
            request: models.VerifyOwnershipRequest,
            opts: Dict = None,
    ) -> models.VerifyOwnershipResponse:
        """
        在 CNAME 接入模式下，您需要对站点或者域名的归属权进行验证，可以通过本接口触发验证。若站点通过归属权验证后，后续添加域名无需再验证。详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

        在 NS 接入模式下，您也可以通过本接口来查询 NS 服务器是否切换成功，详情参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452)。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyOwnership"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyOwnershipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)