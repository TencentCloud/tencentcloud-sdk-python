# Release 3.1.212

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



## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 162 次发布

发布时间：2026-11-23 01:54:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSLInstance](https://cloud.tencent.com/document/api/589/110872)

	* 新增入参：EnablePublicIP, SecurityGroupIds, TerminateProtection




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




## 元宝搜索(wsa) 版本：2025-05-08

### 第 7 次发布

发布时间：2026-11-23 03:09:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [SearchPro](https://cloud.tencent.com/document/api/1806/121811)

	* 新增入参：Switch




