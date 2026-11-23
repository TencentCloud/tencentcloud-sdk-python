# Release 3.1.213

## Agent 沙箱服务(ags) 版本：2025-09-20

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




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 50 次发布

发布时间：2026-11-24 02:29:00

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDeviceSecurityInfo](https://cloud.tencent.com/document/api/1092/138821)

	* 新增入参：DomainInstanceId




## 云直播CSS(live) 版本：2018-08-01

### 第 195 次发布

发布时间：2026-11-24 02:47:53

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [StartLiveSubtitle](https://cloud.tencent.com/document/api/267/141278)
* [StopLiveSubtitle](https://cloud.tencent.com/document/api/267/141277)



## 媒体处理(mps) 版本：2019-06-12

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

### 第 33 次发布

发布时间：2026-11-24 03:38:03

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeStableIPTask](https://cloud.tencent.com/document/api/1243/141279)



## 边缘安全加速平台(teo) 版本：2022-09-01

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



## 实时音视频(trtc) 版本：2019-07-22

### 第 159 次发布

发布时间：2026-11-23 02:51:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [VoiceClone](https://cloud.tencent.com/document/api/647/122473)

	* 新增入参：PreviewText

	* 新增出参：PreviewUrl




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



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20

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




