# Release 3.1.215

## 腾讯云智能体开发平台(adp) 版本：2026-05-20

### 第 43 次发布

发布时间：2026-11-26 01:03:47

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [ConnectorKnowledgeScope](https://cloud.tencent.com/document/api/1759/132545#ConnectorKnowledgeScope)
* [ConnectorResource](https://cloud.tencent.com/document/api/1759/132545#ConnectorResource)
* [ConnectorResourceRef](https://cloud.tencent.com/document/api/1759/132545#ConnectorResourceRef)

修改数据结构：

* [AgentPluginConfig](https://cloud.tencent.com/document/api/1759/132545#AgentPluginConfig)

	* 新增成员：KnowledgeScope

* [DocParseConfig](https://cloud.tencent.com/document/api/1759/132545#DocParseConfig)

	* 新增成员：ParseStrategy


### 第 42 次发布

发布时间：2026-11-25 01:03:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAppTrigger](https://cloud.tencent.com/document/api/1759/135012)

	* 新增入参：AgentId

* [ModifyAppTrigger](https://cloud.tencent.com/document/api/1759/134999)

	* 新增出参：Credential


新增数据结构：

* [AppTriggerGongfengWebhookConfig](https://cloud.tencent.com/document/api/1759/132545#AppTriggerGongfengWebhookConfig)
* [AppTriggerTAPDWebhookConfig](https://cloud.tencent.com/document/api/1759/132545#AppTriggerTAPDWebhookConfig)
* [AppTriggerWebhookConfigExt](https://cloud.tencent.com/document/api/1759/132545#AppTriggerWebhookConfigExt)
* [AppTriggerWebhookCredential](https://cloud.tencent.com/document/api/1759/132545#AppTriggerWebhookCredential)
* [FileSplitModel](https://cloud.tencent.com/document/api/1759/132545#FileSplitModel)
* [HeaderExtractModel](https://cloud.tencent.com/document/api/1759/132545#HeaderExtractModel)

修改数据结构：

* [AppModelConfig](https://cloud.tencent.com/document/api/1759/132545#AppModelConfig)

	* 新增成员：FileSplitModel, HeaderExtractModel

* [AppTrigger](https://cloud.tencent.com/document/api/1759/132545#AppTrigger)

	* 新增成员：AgentId

* [AppTriggerSummary](https://cloud.tencent.com/document/api/1759/132545#AppTriggerSummary)

	* 新增成员：WebhookProvider

* [AppTriggerWebhookConfig](https://cloud.tencent.com/document/api/1759/132545#AppTriggerWebhookConfig)

	* 新增成员：WebhookConfigExt, WebhookProvider

* [Variable](https://cloud.tencent.com/document/api/1759/132545#Variable)

	* 新增成员：ValueScope


### 第 41 次发布

发布时间：2026-11-24 11:04:59

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreatePromptTemplate](https://cloud.tencent.com/document/api/1759/141304)
* [CreatePromptTemplateLabel](https://cloud.tencent.com/document/api/1759/141303)
* [DeletePromptTemplate](https://cloud.tencent.com/document/api/1759/141302)
* [DeletePromptTemplateLabel](https://cloud.tencent.com/document/api/1759/141301)
* [DescribePromptTemplate](https://cloud.tencent.com/document/api/1759/141300)
* [DescribePromptTemplateCategoryList](https://cloud.tencent.com/document/api/1759/141299)
* [DescribePromptTemplateLabelList](https://cloud.tencent.com/document/api/1759/141298)
* [DescribePromptTemplateSummaryList](https://cloud.tencent.com/document/api/1759/141297)
* [FavoritePromptTemplate](https://cloud.tencent.com/document/api/1759/141296)
* [ModifyPromptTemplate](https://cloud.tencent.com/document/api/1759/141295)
* [UnfavoritePromptTemplate](https://cloud.tencent.com/document/api/1759/141294)

新增数据结构：

* [Audit](https://cloud.tencent.com/document/api/1759/132545#Audit)
* [PromptTemplate](https://cloud.tencent.com/document/api/1759/132545#PromptTemplate)
* [PromptTemplateCategory](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateCategory)
* [PromptTemplateCategoryGroup](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateCategoryGroup)
* [PromptTemplateLabel](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateLabel)
* [PromptTemplateProfile](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateProfile)
* [PromptTemplateSpec](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateSpec)
* [PromptTemplateSummary](https://cloud.tencent.com/document/api/1759/132545#PromptTemplateSummary)



## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 41 次发布

发布时间：2026-11-26 01:05:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreatePreCacheImageTask](https://cloud.tencent.com/document/api/1814/127508)

	* 新增入参：IdleTTL

* [DescribePreCacheImageTask](https://cloud.tencent.com/document/api/1814/127507)

	* 新增出参：IdleTTL, ExpireTime


### 第 40 次发布

发布时间：2026-11-20 19:48:37

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreatePreCacheImageCleanupPolicy](https://cloud.tencent.com/document/api/1814/141176)
* [DeletePreCacheImageCleanupPolicy](https://cloud.tencent.com/document/api/1814/141175)
* [DescribePreCacheImageCleanupPolicyList](https://cloud.tencent.com/document/api/1814/141174)
* [UpdatePreCacheImageCleanupPolicy](https://cloud.tencent.com/document/api/1814/141173)

修改接口：

* [StartSandboxInstance](https://cloud.tencent.com/document/api/1814/124816)

	* 新增入参：StorageMounts


新增数据结构：

* [PreCacheImageCleanupPolicy](https://cloud.tencent.com/document/api/1814/124823#PreCacheImageCleanupPolicy)



## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 17 次发布

发布时间：2026-11-26 01:09:20

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAgentCredential](https://cloud.tencent.com/document/api/1627/129675)

	* 新增入参：InstanceID, Name, Type, Content

	* 新增出参：Data

* [DeleteAgentCredential](https://cloud.tencent.com/document/api/1627/129674)

	* 新增入参：InstanceID, ID

	* 新增出参：Data

* [DescribeAgentCredential](https://cloud.tencent.com/document/api/1627/129673)

	* 新增入参：InstanceID, ID

	* 新增出参：Data

* [DescribeAgentCredentials](https://cloud.tencent.com/document/api/1627/129672)

	* 新增入参：Limit, InstanceID, NotIDs, Status, Offset, Keyword, IDs, Type, Sort

	* 新增出参：Data

* [ModifyAgentCredential](https://cloud.tencent.com/document/api/1627/129671)

	* 新增入参：InstanceID, ID, Name, Type, Content

	* 新增出参：Data


新增数据结构：

* [DescribeAgentCredentialsResp](https://cloud.tencent.com/document/api/1627/129635#DescribeAgentCredentialsResp)
* [DescribeAgentCredentialsSortDTO](https://cloud.tencent.com/document/api/1627/129635#DescribeAgentCredentialsSortDTO)

修改数据结构：

* [McpSecurityRulesVO](https://cloud.tencent.com/document/api/1627/129635#McpSecurityRulesVO)

	* <font color="#dd0000">**修改成员**：</font>ID, Type, Name, Description, RiskLevel, VersionNumber, Status, Act, SupportActs, BodyType, IconType

* [PromptModerateConfigDTO](https://cloud.tencent.com/document/api/1627/129635#PromptModerateConfigDTO)

	* 新增成员：CheckTargets

* [ServiceVO](https://cloud.tencent.com/document/api/1627/129635#ServiceVO)

	* 新增成员：ServiceSecurityRules, ServiceSecurityRulesVO

* [TmsConfigDTO](https://cloud.tencent.com/document/api/1627/129635#TmsConfigDTO)

	* 新增成员：CheckTargets




## 应用性能监控(apm) 版本：2021-06-22

### 第 75 次发布

发布时间：2026-11-24 01:07:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateApmPrometheusRule](https://cloud.tencent.com/document/api/1463/125082)

	* 新增入参：AssociationId

* [DescribeApmPrometheusRule](https://cloud.tencent.com/document/api/1463/125078)

	* 新增入参：AssociationId

* [ModifyApmPrometheusRule](https://cloud.tencent.com/document/api/1463/125075)

	* 新增入参：AssociationId


修改数据结构：

* [ApmPrometheusRules](https://cloud.tencent.com/document/api/1463/64927#ApmPrometheusRules)

	* 新增成员：AssociationId




## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 42 次发布

发布时间：2026-11-25 01:10:41

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ApproveTicket](https://cloud.tencent.com/document/api/1025/141317)
* [DescribeTickets](https://cloud.tencent.com/document/api/1025/141316)

新增数据结构：

* [Ticket](https://cloud.tencent.com/document/api/1025/74416#Ticket)

### 第 41 次发布

发布时间：2026-11-24 01:10:03

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CheckLDAPConnection](https://cloud.tencent.com/document/api/1025/120145)

	* 新增入参：ResourceId

* [DescribeLDAPUnitSet](https://cloud.tencent.com/document/api/1025/120144)

	* 新增入参：ResourceId

* [ModifyLDAPSetting](https://cloud.tencent.com/document/api/1025/120143)

	* 新增入参：ResourceId


修改数据结构：

* [LoginSetting](https://cloud.tencent.com/document/api/1025/74416#LoginSetting)

	* 新增成员：EnableDeviceFingerprintVerify




## 应用云渲染(car) 版本：2022-01-10

### 第 12 次发布

发布时间：2026-11-24 01:13:41

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateMCPToken](https://cloud.tencent.com/document/api/1547/141104)

	* 新增入参：ExpireSeconds, TokenName, UserId

	* 新增出参：TokenId, Token

* [DescribeMCPTokens](https://cloud.tencent.com/document/api/1547/141103)

	* 新增入参：Offset, Limit, Filters

	* 新增出参：Tokens, TotalCount

* [RenewMCPToken](https://cloud.tencent.com/document/api/1547/141102)

	* 新增入参：TokenId, ExpireSeconds


新增数据结构：

* [Filter](https://cloud.tencent.com/document/api/1547/141275#Filter)
* [MCPTokenInfo](https://cloud.tencent.com/document/api/1547/141275#MCPTokenInfo)



## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 69 次发布

发布时间：2026-11-23 01:19:09

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstanceNew](https://cloud.tencent.com/document/api/1387/102611)

	* 新增入参：CacheDiskType

* [DeleteWorkloadGroup](https://cloud.tencent.com/document/api/1387/109439)

	* 新增入参：ComputeGroup

* [DescribeWorkloadGroup](https://cloud.tencent.com/document/api/1387/109437)

	* 新增出参：NeedPodRebuild

* [ModifyWorkloadGroupStatus](https://cloud.tencent.com/document/api/1387/109430)

	* 新增入参：RestartType


修改数据结构：

* [WorkloadGroupConfig](https://cloud.tencent.com/document/api/1387/102385#WorkloadGroupConfig)

	* 新增成员：ComputeGroup




## 腾讯云数据仓库TCHouse-P(cdwpg) 版本：2020-12-30

### 第 18 次发布

发布时间：2026-11-25 01:19:18

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstanceState](https://cloud.tencent.com/document/api/878/100160)

	* 新增出参：RecoveryState


修改数据结构：

* [InstanceStateItem](https://cloud.tencent.com/document/api/878/98895#InstanceStateItem)

	* 新增成员：RecoveryState




## 专属可用区(cdz) 版本：2022-11-23

### 第 4 次发布

发布时间：2026-11-25 01:19:33

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeUserAvailableCloudDedicatedZones](https://cloud.tencent.com/document/api/1629/141318)

新增数据结构：

* [CloudDedicatedZone](https://cloud.tencent.com/document/api/1629/108683#CloudDedicatedZone)



## 云原生智能网关(cngw) 版本：2023-04-18

### 第 16 次发布

发布时间：2026-11-23 01:28:00

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAIGWLLMModelAPIIPRestriction](https://cloud.tencent.com/document/api/1826/141190)
* [ModifyAIGWLLMModelAPIIPRestriction](https://cloud.tencent.com/document/api/1826/141189)

新增数据结构：

* [AIGWLLMIPRestrictionResult](https://cloud.tencent.com/document/api/1826/133161#AIGWLLMIPRestrictionResult)



## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 205 次发布

发布时间：2026-11-26 01:43:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateProxy](https://cloud.tencent.com/document/api/1003/94134)

	* 新增入参：ProxyVersion

* [DescribeSupportProxyVersion](https://cloud.tencent.com/document/api/1003/94260)

	* 新增入参：Zone, DbVersion, CynosVersion, StorageVersion

	* <font color="#dd0000">**修改入参**：</font>ClusterId

* [IsolateCluster](https://cloud.tencent.com/document/api/1003/48082)

	* 新增入参：ImmediateRecycleRo

* [IsolateInstance](https://cloud.tencent.com/document/api/1003/48081)

	* 新增入参：ImmediateRecycleRo


修改数据结构：

* [ProxyConfig](https://cloud.tencent.com/document/api/1003/48097#ProxyConfig)

	* 新增成员：ProxyVersion

* [UserHostPrivilege](https://cloud.tencent.com/document/api/1003/48097#UserHostPrivilege)

	* 新增成员：PrivilegeList




## 数据安全治理中心(dsgc) 版本：2019-07-23

### 第 36 次发布

发布时间：2026-11-24 02:00:41

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDSPACategories](https://cloud.tencent.com/document/api/1087/97224)

	* 新增入参：Filters, Keyword




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 162 次发布

发布时间：2026-11-23 01:54:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSLInstance](https://cloud.tencent.com/document/api/589/110872)

	* 新增入参：EnablePublicIP, SecurityGroupIds, TerminateProtection




## Elasticsearch Service(es) 版本：2025-01-01



## Elasticsearch Service(es) 版本：2018-04-16

### 第 114 次发布

发布时间：2026-11-24 02:10:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstance](https://cloud.tencent.com/document/api/845/30633)

	* 新增入参：EnableLvm


修改数据结构：

* [InstanceInfo](https://cloud.tencent.com/document/api/845/30634#InstanceInfo)

	* 新增成员：LvmStatus, LvmSwitchFlowId




## 人脸核身(faceid) 版本：2018-03-01

### 第 94 次发布

发布时间：2026-11-26 02:06:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetAttackDetail](https://cloud.tencent.com/document/api/1007/141365)

新增数据结构：

* [AttackRegion](https://cloud.tencent.com/document/api/1007/41958#AttackRegion)
* [Point](https://cloud.tencent.com/document/api/1007/41958#Point)



## 全球加速(ga2) 版本：2025-01-15

### 第 16 次发布

发布时间：2026-11-25 01:54:36

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AcceleratorAreas](https://cloud.tencent.com/document/api/1817/130045#AcceleratorAreas)

	* 新增成员：AccelerateRegionName




## 云游戏(gs) 版本：2019-11-18

### 第 70 次发布

发布时间：2026-11-25 01:56:30

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AndroidInstance](https://cloud.tencent.com/document/api/1162/40743#AndroidInstance)

	* 新增成员：DPI, FPS




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 50 次发布

发布时间：2026-11-24 02:29:00

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDeviceSecurityInfo](https://cloud.tencent.com/document/api/1092/138821)

	* 新增入参：DomainInstanceId




## 密钥管理系统(kms) 版本：2019-01-18

### 第 33 次发布

发布时间：2026-11-26 02:22:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ExclusiveHSM](https://cloud.tencent.com/document/api/573/34431#ExclusiveHSM)

	* 新增成员：CmkUserCount, CmkLimit




## 云直播CSS(live) 版本：2018-08-01

### 第 195 次发布

发布时间：2026-11-24 02:47:53

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [StartLiveSubtitle](https://cloud.tencent.com/document/api/267/141278)
* [StopLiveSubtitle](https://cloud.tencent.com/document/api/267/141277)



## Web 与 Agent 开发部署平台 Makers(makers) 版本：2026-11-13

### 第 3 次发布

发布时间：2026-11-26 02:27:52

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BlockProject](https://cloud.tencent.com/document/api/1847/141366)

### 第 2 次发布

发布时间：2026-11-25 02:10:39

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Project](https://cloud.tencent.com/document/api/1847/141002#Project)

	* 新增成员：BuildMachine




## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 172 次发布

发布时间：2026-11-25 02:13:06

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddSubnetToManagedCluster](https://cloud.tencent.com/document/api/248/141319)



## 媒体处理(mps) 版本：2019-06-12

### 第 261 次发布

发布时间：2026-11-26 02:33:42

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AigcAudioReferenceAudioInfo](https://cloud.tencent.com/document/api/862/37615#AigcAudioReferenceAudioInfo)

	* 新增成员：ReferenceType


### 第 260 次发布

发布时间：2026-11-23 02:19:37

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [VoiceInfo](https://cloud.tencent.com/document/api/862/37615#VoiceInfo)

	* 新增成员：CreatedAt, UpdatedAt




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 37 次发布

发布时间：2026-11-23 02:21:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAuthorizationPolicy](https://cloud.tencent.com/document/api/1778/111079)

	* 新增入参：ResourceItems

* [ModifyAuthorizationPolicy](https://cloud.tencent.com/document/api/1778/111072)

	* 新增入参：ResourceItems


修改数据结构：

* [AuthorizationPolicyItem](https://cloud.tencent.com/document/api/1778/111031#AuthorizationPolicyItem)

	* 新增成员：ResourceItems




## 文字识别(ocr) 版本：2018-11-19

### 第 283 次发布

发布时间：2026-11-23 02:23:38

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ResultList](https://cloud.tencent.com/document/api/866/33527#ResultList)

	* 新增成员：Confidence




## 集团账号管理(organization) 版本：2021-03-31

### 第 64 次发布

发布时间：2026-11-25 02:20:18

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeOrganization](https://cloud.tencent.com/document/api/850/67059)

	* 新增出参：MemberPermissionOptions, DefaultPayType


新增数据结构：

* [MemberPermissionOption](https://cloud.tencent.com/document/api/850/67060#MemberPermissionOption)



## 集团账号管理(organization) 版本：2018-12-25



## 风险识别 RCE(rce) 版本：2026-01-30

### 第 10 次发布

发布时间：2026-11-24 03:19:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AssessRisk](https://cloud.tencent.com/document/api/1343/135880)

	* <font color="#dd0000">**修改入参**：</font>EventDetail

* [ReportEvent](https://cloud.tencent.com/document/api/1343/135879)

	* <font color="#dd0000">**修改入参**：</font>EventDetail


修改数据结构：

* [AddFriendEvent](https://cloud.tencent.com/document/api/1343/134560#AddFriendEvent)

	* 新增成员：Cust

* [ChatEvent](https://cloud.tencent.com/document/api/1343/134560#ChatEvent)

	* 新增成员：Cust

* [ModifyGuildEvent](https://cloud.tencent.com/document/api/1343/134560#ModifyGuildEvent)

	* 新增成员：Cust

* [ModifyRoleEvent](https://cloud.tencent.com/document/api/1343/134560#ModifyRoleEvent)

	* 新增成员：Cust




## 风险识别 RCE(rce) 版本：2025-04-25



## 风险识别 RCE(rce) 版本：2020-11-03



## 前端性能监控(rum) 版本：2021-06-22

### 第 57 次发布

发布时间：2026-11-23 02:30:01

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* DescribeRumLogExportV2
* DescribeRumLogExportsV2

修改接口：

* [DescribeRumLogDetailsV2](https://cloud.tencent.com/document/api/1464/131625)

	* 新增入参：Offset, Context

	* 新增出参：Context, ListOver


修改数据结构：

* [Whitelist](https://cloud.tencent.com/document/api/1464/61476#Whitelist)

	* 新增成员：CreateDatetime




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 182 次发布

发布时间：2026-11-25 02:31:33

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreatePlatformEnv](https://cloud.tencent.com/document/api/876/138302)

	* 新增入参：PGConfig


新增数据结构：

* [PGConfig](https://cloud.tencent.com/document/api/876/34822#PGConfig)

### 第 181 次发布

发布时间：2026-11-24 03:35:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetFunction](https://cloud.tencent.com/document/api/876/137948)

	* 新增出参：Environment, ClsLogsetId, ClsTopicId, EipConfig

* [ModifyPGInstanceSpec](https://cloud.tencent.com/document/api/876/137349)

	* 新增入参：CpuCores


新增数据结构：

* [EipOutConfig](https://cloud.tencent.com/document/api/876/34822#EipOutConfig)
* [EnvironmentOut](https://cloud.tencent.com/document/api/876/34822#EnvironmentOut)



## 云托管 CloudBase Run(tcbr) 版本：2022-02-17

### 第 34 次发布

发布时间：2026-11-25 02:32:40

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeStableIP](https://cloud.tencent.com/document/api/1243/141320)

### 第 33 次发布

发布时间：2026-11-24 03:38:03

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeStableIPTask](https://cloud.tencent.com/document/api/1243/141279)



## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 175 次发布

发布时间：2026-11-25 02:38:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyOriginACL](https://cloud.tencent.com/document/api/1552/120405)

	* 新增入参：L7EnableMode, L4EnableMode


修改数据结构：

* [OriginACLInfo](https://cloud.tencent.com/document/api/1552/80721#OriginACLInfo)

	* 新增成员：L7EnableMode, L4EnableMode

* [WebSecurity](https://cloud.tencent.com/document/api/1552/80721#WebSecurity)

	* <font color="#dd0000">**修改成员**：</font>HostPolicy, Templates


### 第 174 次发布

发布时间：2026-11-24 03:50:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateCustomGroup](https://cloud.tencent.com/document/api/1552/141285)
* [DeleteCustomGroup](https://cloud.tencent.com/document/api/1552/141284)
* [DescribeCustomGroup](https://cloud.tencent.com/document/api/1552/141283)
* [DescribeCustomGroupReferences](https://cloud.tencent.com/document/api/1552/141282)
* [DescribeCustomGroups](https://cloud.tencent.com/document/api/1552/141281)
* [ModifyCustomGroup](https://cloud.tencent.com/document/api/1552/141280)

新增数据结构：

* [CustomGroup](https://cloud.tencent.com/document/api/1552/80721#CustomGroup)
* [CustomGroupItem](https://cloud.tencent.com/document/api/1552/80721#CustomGroupItem)
* [CustomGroupReference](https://cloud.tencent.com/document/api/1552/80721#CustomGroupReference)



## 边缘安全加速平台(teo) 版本：2022-01-06



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 149 次发布

发布时间：2026-11-25 02:41:23

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyTrainingTaskSchedulingPolicy](https://cloud.tencent.com/document/api/851/141321)

新增数据结构：

* [SchedulePolicy](https://cloud.tencent.com/document/api/851/75051#SchedulePolicy)



## TI-ONE 训练平台(tione) 版本：2019-10-22



## 容器服务(tke) 版本：2022-05-01

### 第 34 次发布

发布时间：2026-11-23 02:49:21

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [RegistryConfig](https://cloud.tencent.com/document/api/457/103206#RegistryConfig)
* [RegistryMirror](https://cloud.tencent.com/document/api/457/103206#RegistryMirror)

修改数据结构：

* [CreateNativeNodePoolParam](https://cloud.tencent.com/document/api/457/103206#CreateNativeNodePoolParam)

	* 新增成员：Registry

* [UpdateNativeNodePoolParam](https://cloud.tencent.com/document/api/457/103206#UpdateNativeNodePoolParam)

	* 新增成员：Registry




## 容器服务(tke) 版本：2018-05-25

### 第 242 次发布

发布时间：2026-11-26 03:09:30

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClusterExternalConfig](https://cloud.tencent.com/document/api/457/31866#ClusterExternalConfig)

	* 新增成员：ProxyCLBMode




## TokenHub(tokenhub) 版本：2026-03-22

### 第 29 次发布

发布时间：2026-11-25 02:45:06

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTokenPlanApiKeys](https://cloud.tencent.com/document/api/1823/132278)

	* 新增入参：IpWhitelist, OverageEnabled

* [ModifyTokenPlanApiKey](https://cloud.tencent.com/document/api/1823/132273)

	* 新增入参：IpWhitelist


修改数据结构：

* [EndpointDetail](https://cloud.tencent.com/document/api/1823/132279#EndpointDetail)

	* 新增成员：WorkspaceId, OriginEndpointId, NightDiscountEnabled

* [ModelEndpointView](https://cloud.tencent.com/document/api/1823/132279#ModelEndpointView)

	* 新增成员：ModelChargeUnit, ModelImage, OfflineAt, DiscontinuedAt, NightDiscountEnabled

* [TokenPlanApiKeyListItem](https://cloud.tencent.com/document/api/1823/132279#TokenPlanApiKeyListItem)

	* 新增成员：IpWhitelist, OverageEnabled




## 实时音视频(trtc) 版本：2019-07-22

### 第 161 次发布

发布时间：2026-11-26 03:15:24

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AsyncTextToSpeech](https://cloud.tencent.com/document/api/647/130582)

	* 新增入参：TextSegments

	* 新增出参：CurrentTaskCount, MaxTaskCount

* [DescribeAsyncTextToSpeech](https://cloud.tencent.com/document/api/647/130581)

	* 新增出参：SegmentResults


新增数据结构：

* [AsyncTTSSegmentResult](https://cloud.tencent.com/document/api/647/44055#AsyncTTSSegmentResult)
* [AsyncTTSTextSegment](https://cloud.tencent.com/document/api/647/44055#AsyncTTSTextSegment)

### 第 160 次发布

发布时间：2026-11-25 02:47:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeFinanceCloudRoomUsage](https://cloud.tencent.com/document/api/647/141145)

	* 新增出参：Data


### 第 159 次发布

发布时间：2026-11-23 02:51:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [VoiceClone](https://cloud.tencent.com/document/api/647/122473)

	* 新增入参：PreviewText

	* 新增出参：PreviewUrl




## TSF-Polaris&ZK&网关(tse) 版本：2020-12-07

### 第 120 次发布

发布时间：2026-11-26 03:16:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeCloudNativeAPIGateways](https://cloud.tencent.com/document/api/1364/96752)

	* 新增入参：EnableRegionFilter


### 第 119 次发布

发布时间：2026-11-25 02:48:10

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeCloudNativeAPIGatewayRoutes](https://cloud.tencent.com/document/api/1364/94842)

	* 新增入参：ServiceId


修改数据结构：

* [LimitRule](https://cloud.tencent.com/document/api/1364/54942#LimitRule)

	* 新增成员：Enabled




## 云点播(vod) 版本：2024-07-18



## 云点播(vod) 版本：2018-07-17

### 第 298 次发布

发布时间：2026-11-23 02:56:24

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AigcVideoTaskOutput](https://cloud.tencent.com/document/api/266/31773#AigcVideoTaskOutput)

	* 新增成员：TotalInputVideoDuration




## 私有网络(vpc) 版本：2017-03-12

### 第 316 次发布

发布时间：2026-11-24 04:23:32

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SecurityGroup](https://cloud.tencent.com/document/api/215/15824#SecurityGroup)

	* 新增成员：ServiceManaged




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06

### 第 29 次发布

发布时间：2026-11-25 03:03:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTriggerWorkflow](https://cloud.tencent.com/document/api/1267/127267)

	* 新增入参：WorkflowLabels

* [ListCodeFolderContents](https://cloud.tencent.com/document/api/1267/123602)

	* 新增入参：SubmitStatusFilter

* [UpdateTriggerWorkflow](https://cloud.tencent.com/document/api/1267/127241)

	* 新增入参：WorkflowLabels


新增数据结构：

* [TriggerTableUpdateRecord](https://cloud.tencent.com/document/api/1267/123643#TriggerTableUpdateRecord)
* [WorkflowLabel](https://cloud.tencent.com/document/api/1267/123643#WorkflowLabel)

修改数据结构：

* [TriggerTaskRunBrief](https://cloud.tencent.com/document/api/1267/123643#TriggerTaskRunBrief)

	* 新增成员：TriggerTableUpdateRecords

* [TriggerWorkflowDetail](https://cloud.tencent.com/document/api/1267/123643#TriggerWorkflowDetail)

	* 新增成员：WorkflowLabels

* [TriggerWorkflowRunBrief](https://cloud.tencent.com/document/api/1267/123643#TriggerWorkflowRunBrief)

	* 新增成员：TriggerTableUpdateRecords, WorkflowLabels

* [UpdateTriggerWorkflowPartially](https://cloud.tencent.com/document/api/1267/123643#UpdateTriggerWorkflowPartially)

	* 新增成员：WorkflowLabels

* [WorkflowTriggerConfig](https://cloud.tencent.com/document/api/1267/123643#WorkflowTriggerConfig)

	* 新增成员：TableQualifiers, TriggerPolicy




## 数据开发治理平台 WeData(wedata) 版本：2021-08-20

### 第 210 次发布

发布时间：2026-11-25 03:00:18

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [WorkflowLabel](https://cloud.tencent.com/document/api/1267/76336#WorkflowLabel)

修改数据结构：

* [WorkflowDsDTO](https://cloud.tencent.com/document/api/1267/76336#WorkflowDsDTO)

	* 新增成员：WorkflowLabels


### 第 209 次发布

发布时间：2026-11-23 03:04:33

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [LogDiagnosisRules](https://cloud.tencent.com/document/api/1267/76336#LogDiagnosisRules)

修改数据结构：

* [InstanceLogInfoOpsDto](https://cloud.tencent.com/document/api/1267/76336#InstanceLogInfoOpsDto)

	* 新增成员：LogDiagnosisRules




## WorkBuddy Enterprise(workbuddyenterprise) 版本：2026-07-09

### 第 10 次发布

发布时间：2026-11-24 04:45:22

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAgentSession](https://cloud.tencent.com/document/api/1831/138630)

	* 新增入参：MetricEntry

* [DeleteSessionArtifactList](https://cloud.tencent.com/document/api/1831/140523)

	* 新增入参：SessionId, ArtifactIds

	* 新增出参：DeletedCount

* [DescribeSessionArtifactDownloadUrl](https://cloud.tencent.com/document/api/1831/140522)

	* 新增入参：ArtifactId, ExpiredSeconds

	* 新增出参：DownloadUrl, ExpiredTime, FileName, FileSizeBytes, FileSha256

* [DescribeSessionArtifactList](https://cloud.tencent.com/document/api/1831/140521)

	* 新增入参：SessionId, Offset, Limit, Filters

	* 新增出参：TotalCount, ArtifactSet


新增数据结构：

* [SessionArtifactDetail](https://cloud.tencent.com/document/api/1831/138580#SessionArtifactDetail)



## 元宝搜索(wsa) 版本：2025-05-08

### 第 7 次发布

发布时间：2026-11-23 03:09:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [SearchPro](https://cloud.tencent.com/document/api/1806/121811)

	* 新增入参：Switch




