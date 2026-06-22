# Release 3.1.120

## 批量计算(batch) 版本：2017-03-12

### 第 64 次发布

发布时间：2026-06-23 01:10:46

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SystemDisk](https://cloud.tencent.com/document/api/599/15912#SystemDisk)

	* 新增成员：Encrypt, KmsKeyId




## 云联络中心(ccc) 版本：2020-02-10

### 第 130 次发布

发布时间：2026-06-23 01:13:28

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AISpeakEvent](https://cloud.tencent.com/document/api/679/47715#AISpeakEvent)

	* 新增成员：TraverseReason




## 云服务器(cvm) 版本：2017-03-12

### 第 164 次发布

发布时间：2026-06-23 01:21:17

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [SystemDisk](https://cloud.tencent.com/document/api/213/15753#SystemDisk)

	* 新增成员：Encrypt, KmsKeyId




## 凭据管理系统(ssm) 版本：2019-09-23

### 第 16 次发布

发布时间：2026-06-23 01:50:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSecret](https://cloud.tencent.com/document/api/1140/40526)

	* 新增出参：CreateUinString, TargetUinString


修改数据结构：

* [SecretMetadata](https://cloud.tencent.com/document/api/1140/40530#SecretMetadata)

	* 新增成员：CreateUinString, TargetUinString




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 177 次发布

发布时间：2026-06-23 01:54:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeRocketMQMsg](https://cloud.tencent.com/document/api/1179/91055)

	* 新增入参：QueryDelayMessage

* [ModifyRocketMQInstance](https://cloud.tencent.com/document/api/1179/108862)

	* 新增入参：AclEnabled


修改数据结构：

* [RocketMQClusterInfo](https://cloud.tencent.com/document/api/1179/46089#RocketMQClusterInfo)

	* 新增成员：AutoCreateConsumeGroupEnabled




## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 148 次发布

发布时间：2026-06-23 01:55:40

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [AdvancedOriginRoutingParameters](https://cloud.tencent.com/document/api/1552/80721#AdvancedOriginRoutingParameters)

修改数据结构：

* [RuleEngineAction](https://cloud.tencent.com/document/api/1552/80721#RuleEngineAction)

	* 新增成员：AdvancedOriginRoutingParameters




## 边缘安全加速平台(teo) 版本：2022-01-06



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 122 次发布

发布时间：2026-06-23 01:57:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBillingResourceGroupAttachedWorkspaces](https://cloud.tencent.com/document/api/851/130953)

	* 新增入参：ResourceGroupId


新增数据结构：

* [RepairTaskInfo](https://cloud.tencent.com/document/api/851/75051#RepairTaskInfo)

修改数据结构：

* [Instance](https://cloud.tencent.com/document/api/851/75051#Instance)

	* 新增成员：AvailableResource, InstanceIP, InstanceName, CvmInstanceType, AutoRenew, Isolated, RepairTaskInfo, ZoneName




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 消息队列 RabbitMQ Serverless 版(trabbit) 版本：2023-04-18

### 第 8 次发布

发布时间：2026-06-23 01:59:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRabbitMQServerlessBinding](https://cloud.tencent.com/document/api/1495/116150)

	* 新增入参：Arguments


新增数据结构：

* [RabbitMQServerlessKeyValuePair](https://cloud.tencent.com/document/api/1495/116155#RabbitMQServerlessKeyValuePair)

修改数据结构：

* [RabbitMQBindingListInfo](https://cloud.tencent.com/document/api/1495/116155#RabbitMQBindingListInfo)

	* 新增成员：Arguments




## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 53 次发布

发布时间：2026-06-23 01:59:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateConsumerGroup](https://cloud.tencent.com/document/api/1493/97943)

	* 新增入参：LiteTopic

* [CreateTopic](https://cloud.tencent.com/document/api/1493/97947)

	* 新增入参：AutoExpireDelete, AutoExpireTime

	* <font color="#dd0000">**修改入参**：</font>QueueNum

* [DescribeConsumerGroup](https://cloud.tencent.com/document/api/1493/97941)

	* 新增出参：ConsumeModel, LiteTopic

* [DescribeMessage](https://cloud.tencent.com/document/api/1493/114594)

	* 新增出参：LiteTopic

* [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593)

	* 新增入参：LiteTopic

* [DescribeMessageTrace](https://cloud.tencent.com/document/api/1493/114302)

	* 新增出参：LiteTopic

* [DescribeTopic](https://cloud.tencent.com/document/api/1493/97945)

	* 新增出参：AutoExpireDelete, AutoExpireTime

* [ModifyTopic](https://cloud.tencent.com/document/api/1493/97944)

	* 新增入参：AutoExpireDelete, AutoExpireTime

* [SendMessage](https://cloud.tencent.com/document/api/1493/126164)

	* 新增入参：LiteTopic




## 私有网络(vpc) 版本：2017-03-12

### 第 304 次发布

发布时间：2026-06-23 02:04:30

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [CcnPolicyBasedRoutingRule](https://cloud.tencent.com/document/api/215/15824#CcnPolicyBasedRoutingRule)

	* 新增成员：DestinationInstanceType, DestinationInstanceId




