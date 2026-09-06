# Release 3.1.170

## 负载均衡(clb) 版本：2018-03-17

### 第 163 次发布

发布时间：2026-09-07 01:31:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModel](https://cloud.tencent.com/document/api/214/133679)

	* 新增入参：Capability, EndpointPath

* [CreateModelRouter](https://cloud.tencent.com/document/api/214/133217)

	* 新增入参：EmbeddingConfig

* [DescribeModelAssociations](https://cloud.tencent.com/document/api/214/133659)

	* 新增入参：Capability

* [ModifyModelAliasAttributes](https://cloud.tencent.com/document/api/214/133671)

	* 新增入参：Capability

* [ModifyModelAttributes](https://cloud.tencent.com/document/api/214/133670)

	* 新增入参：ApiBase, EndpointPath

* [ModifyModelRouterAttributes](https://cloud.tencent.com/document/api/214/133203)

	* 新增入参：Capability, EmbeddingConfig

* [TestServiceProviderConnection](https://cloud.tencent.com/document/api/214/133665)

	* 新增入参：Capability


新增数据结构：

* [EmbeddingConfig](https://cloud.tencent.com/document/api/214/30694#EmbeddingConfig)

修改数据结构：

* [ModelAlias](https://cloud.tencent.com/document/api/214/30694#ModelAlias)

	* 新增成员：Capability

* [ModelAssociation](https://cloud.tencent.com/document/api/214/30694#ModelAssociation)

	* 新增成员：Capability

* [ModelKeyInfoItem](https://cloud.tencent.com/document/api/214/30694#ModelKeyInfoItem)

	* 新增成员：Capability, EndpointPath

* [ModelRouterDetail](https://cloud.tencent.com/document/api/214/30694#ModelRouterDetail)

	* 新增成员：EmbeddingConfig




## 日志服务(cls) 版本：2020-10-16

### 第 177 次发布

发布时间：2026-09-07 01:33:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetAlarmLog](https://cloud.tencent.com/document/api/614/56460)

	* 新增入参：QueryString

	* <font color="#dd0000">**修改入参**：</font>Query




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 193 次发布

发布时间：2026-09-07 01:44:22

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [TransferStoragePrepayToPostpay](https://cloud.tencent.com/document/api/1003/135369)

	* 新增入参：ClusterId

	* 新增出参：BigDealIds, DealNames, ResourceIds, ClusterIds




## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 15 次发布

发布时间：2026-09-07 01:48:19

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDBCustomDisasterRecoverGroup](https://cloud.tencent.com/document/api/1322/137569)
* [DeleteDBCustomDisasterRecoverGroups](https://cloud.tencent.com/document/api/1322/137568)
* [DeleteDBCustomNodesDisasterRecoverGroup](https://cloud.tencent.com/document/api/1322/137567)
* [DescribeDBCustomDisasterRecoverGroupQuota](https://cloud.tencent.com/document/api/1322/137566)
* [DescribeDBCustomDisasterRecoverGroups](https://cloud.tencent.com/document/api/1322/137565)
* [ModifyDBCustomDisasterRecoverGroupAttribute](https://cloud.tencent.com/document/api/1322/137564)
* [ModifyDBCustomDisasterRecoverGroupTags](https://cloud.tencent.com/document/api/1322/137563)
* [ModifyDBCustomNodesDisasterRecoverGroup](https://cloud.tencent.com/document/api/1322/137562)

修改接口：

* [CreateDBCustomNodes](https://cloud.tencent.com/document/api/1322/132929)

	* 新增入参：DisasterRecoverGroupIds


新增数据结构：

* [DisasterRecoverGroup](https://cloud.tencent.com/document/api/1322/74754#DisasterRecoverGroup)

修改数据结构：

* [DBCustomNode](https://cloud.tencent.com/document/api/1322/74754#DBCustomNode)

	* 新增成员：DisasterRecoverGroupId




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 156 次发布

发布时间：2026-09-07 02:00:12

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [NodeHardwareInfo](https://cloud.tencent.com/document/api/589/33981#NodeHardwareInfo)

	* 新增成员：NodeGroupId, NodeGroupName




## 物联网智能视频服务（行业版）(iotvideoindustry) 版本：2020-12-01

### 第 21 次发布

发布时间：2026-09-07 02:17:50

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [RecordTaskItem](https://cloud.tencent.com/document/api/1361/53754#RecordTaskItem)

	* 新增成员：InitID, ExpectDeleteTime, RecordTimeLen, FileSize




## 媒体处理(mps) 版本：2019-06-12

### 第 245 次发布

发布时间：2026-09-07 02:30:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CloneViral](https://cloud.tencent.com/document/api/862/135033)

	* 新增入参：Output

* [DescribeAigcTaskStatus](https://cloud.tencent.com/document/api/862/134738)

	* 新增出参：TaskInfo, Stage

* [DescribeCloneViralTask](https://cloud.tencent.com/document/api/862/135032)

	* 新增出参：RequestBody


新增数据结构：

* [CloneViralCosInfo](https://cloud.tencent.com/document/api/862/37615#CloneViralCosInfo)
* [CloneViralOutputOption](https://cloud.tencent.com/document/api/862/37615#CloneViralOutputOption)
* [DocToVideoBackgroundInfo](https://cloud.tencent.com/document/api/862/37615#DocToVideoBackgroundInfo)
* [DocToVideoWatermarkInfo](https://cloud.tencent.com/document/api/862/37615#DocToVideoWatermarkInfo)

修改数据结构：

* [AigcTaskListItem](https://cloud.tencent.com/document/api/862/37615#AigcTaskListItem)

	* 新增成员：TaskInfo, Stage

* [DocToVideoInput](https://cloud.tencent.com/document/api/862/37615#DocToVideoInput)

	* 新增成员：PPTXFidelity, Mode, Background, Watermark, EnableCaption

* [QueryTaskFilter](https://cloud.tencent.com/document/api/862/37615#QueryTaskFilter)

	* 新增成员：ExecuteMode, VideoType, ModelTier




## 文字识别(ocr) 版本：2018-11-19

### 第 265 次发布

发布时间：2026-09-07 02:35:19

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [RedLetterInvoiceItem](https://cloud.tencent.com/document/api/866/33527#RedLetterInvoiceItem)

修改数据结构：

* [ElectronicTrainTicket](https://cloud.tencent.com/document/api/866/33527#ElectronicTrainTicket)

	* 新增成员：Type, AirConditionerFeature, TicketType, OriginalTaxRate, FullElectronicNumber

* [PassInvoiceInfo](https://cloud.tencent.com/document/api/866/33527#PassInvoiceInfo)

	* 新增成员：CarType, PlateNumber

* [UsedVehicleInvoiceInfo](https://cloud.tencent.com/document/api/866/33527#UsedVehicleInvoiceInfo)

	* 新增成员：VehicleTotalPriceCN, InvoiceRiskLevel, CarType, PlateModel, AbandonerName, AbandonDate, IssuerType, IssuerTaxCode, CustomCode, TaxClassifyCode, ZeroTaxRateMark

* [VatInvoice](https://cloud.tencent.com/document/api/866/33527#VatInvoice)

	* 新增成员：RegionCode, ReviewerName, IssuerName, PayeeName, MachineCode, TaxControlCode, AmountWithTaxCN, TaxRate, SpecialTicketCode, RedLetterInvoices, FullElectronicType, OfdUrl, PdfUrl, OriginalCode, OriginalNumber

* [VatInvoiceItem](https://cloud.tencent.com/document/api/866/33527#VatInvoiceItem)

	* 新增成员：OriginalTaxRate, OriginalTaxAmount, ZeroTaxRateMark, TaxIncludedUnitPrice, TaxIncludedAmount

	* <font color="#dd0000">**修改成员**：</font>VehicleType, VehicleBrand, DeparturePlace, ArrivalPlace, TransportItemsName, ConstructionPlace, ConstructionName




## TDSQL(tdmysql) 版本：2021-11-22

### 第 16 次发布

发布时间：2026-09-07 02:56:15

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDBCharsets](https://cloud.tencent.com/document/api/1376/137573)
* [DescribeFlowTypes](https://cloud.tencent.com/document/api/1376/137574)
* [DescribeInstanceDataReservedSpace](https://cloud.tencent.com/document/api/1376/137572)
* [ModifyInstanceDataReservedSpace](https://cloud.tencent.com/document/api/1376/137571)
* [ResetDbaAdminPrivileges](https://cloud.tencent.com/document/api/1376/137570)

新增数据结构：

* [FlowType](https://cloud.tencent.com/document/api/1376/128305#FlowType)



## 云点播(vod) 版本：2024-07-18



## 云点播(vod) 版本：2018-07-17

### 第 286 次发布

发布时间：2026-09-07 03:13:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateKnowledgeBase](https://cloud.tencent.com/document/api/266/135377)

	* 新增出参：KnowledgeBaseId

* [DescribeKnowledgeBases](https://cloud.tencent.com/document/api/266/135375)

	* 新增出参：TotalCount, KnowledgeBaseSet


新增数据结构：

* [KnowledgeBaseInfo](https://cloud.tencent.com/document/api/266/31773#KnowledgeBaseInfo)



## 私有网络(vpc) 版本：2017-03-12

### 第 310 次发布

发布时间：2026-09-07 03:17:08

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyGatewayFlowQos](https://cloud.tencent.com/document/api/215/43268)

	* 新增入参：Direction




