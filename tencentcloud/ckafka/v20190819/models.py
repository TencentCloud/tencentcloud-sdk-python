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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Acl(AbstractModel):
    """ACL对象实体

    """

    def __init__(self):
        r"""
        :param ResourceType: Acl资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）当前只有TOPIC，
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
注意：此字段可能返回 null，表示取不到有效值。
        :type Principal: str
        :param Host: 默认为*，表示任何host都可以访问，当前ckafka不支持host为*，但是后面开源kafka的产品化会直接支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Operation: Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)
        :type Operation: int
        :param PermissionType: 权限类型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)
        :type PermissionType: int
        """
        self.ResourceType = None
        self.ResourceName = None
        self.Principal = None
        self.Host = None
        self.Operation = None
        self.PermissionType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Principal = params.get("Principal")
        self.Host = params.get("Host")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclResponse(AbstractModel):
    """ACL返回结果集

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的总数据条数
        :type TotalCount: int
        :param AclList: ACL列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AclList: list of Acl
        """
        self.TotalCount = None
        self.AclList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self.AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self.AclList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRule(AbstractModel):
    """AclRule列表接口出参

    """

    def __init__(self):
        r"""
        :param RuleName: Acl规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param PatternType: 匹配类型，目前只支持前缀匹配，枚举值列表：PREFIXED
注意：此字段可能返回 null，表示取不到有效值。
        :type PatternType: str
        :param Pattern: 表示前缀匹配的前缀的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Pattern: str
        :param ResourceType: Acl资源类型,目前只支持Topic,枚举值列表：Topic
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param AclList: 该规则所包含的ACL信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AclList: str
        :param CreateTimeStamp: 规则所创建的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTimeStamp: str
        :param IsApplied: 预设ACL规则是否应用到新增的topic中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsApplied: int
        :param UpdateTimeStamp: 规则更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTimeStamp: str
        :param Comment: 规则的备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param TopicName: 其中一个显示的对应的TopicName
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param TopicCount: 应用该ACL规则的Topic数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicCount: int
        :param PatternTypeTitle: patternType的中文显示
注意：此字段可能返回 null，表示取不到有效值。
        :type PatternTypeTitle: str
        """
        self.RuleName = None
        self.InstanceId = None
        self.PatternType = None
        self.Pattern = None
        self.ResourceType = None
        self.AclList = None
        self.CreateTimeStamp = None
        self.IsApplied = None
        self.UpdateTimeStamp = None
        self.Comment = None
        self.TopicName = None
        self.TopicCount = None
        self.PatternTypeTitle = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.InstanceId = params.get("InstanceId")
        self.PatternType = params.get("PatternType")
        self.Pattern = params.get("Pattern")
        self.ResourceType = params.get("ResourceType")
        self.AclList = params.get("AclList")
        self.CreateTimeStamp = params.get("CreateTimeStamp")
        self.IsApplied = params.get("IsApplied")
        self.UpdateTimeStamp = params.get("UpdateTimeStamp")
        self.Comment = params.get("Comment")
        self.TopicName = params.get("TopicName")
        self.TopicCount = params.get("TopicCount")
        self.PatternTypeTitle = params.get("PatternTypeTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRuleInfo(AbstractModel):
    """表示ACL 规则的四元组信息

    """

    def __init__(self):
        r"""
        :param Operation: Acl操作方式，枚举值(所有操作: All, 读：Read，写：Write)
        :type Operation: str
        :param PermissionType: 权限类型，(Deny，Allow)
        :type PermissionType: str
        :param Host: 默认为*，表示任何host都可以访问，当前ckafka不支持host为*和ip网段
        :type Host: str
        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入格式需要带【User:】前缀。例如用户A，传入为User:A。
        :type Principal: str
        """
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIdResponse(AbstractModel):
    """AppId的查询结果

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合要求的所有AppId数量
        :type TotalCount: int
        :param AppIdList: 符合要求的App Id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of int
        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Assignment(AbstractModel):
    """存储着分配给该消费者的 partition 信息

    """

    def __init__(self):
        r"""
        :param Version: assingment版本信息
        :type Version: int
        :param Topics: topic信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of GroupInfoTopics
        """
        self.Version = None
        self.Topics = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self.Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeTokenRequest(AbstractModel):
    """AuthorizeToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param User: 用户
        :type User: str
        :param Tokens: token串
        :type Tokens: str
        """
        self.InstanceId = None
        self.User = None
        self.Tokens = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Tokens = params.get("Tokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeTokenResponse(AbstractModel):
    """AuthorizeToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 0 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BatchContent(AbstractModel):
    """批量发送消息内容

    """

    def __init__(self):
        r"""
        :param Body: 发送的消息体
        :type Body: str
        :param Key: 发送消息的键名
        :type Key: str
        """
        self.Body = None
        self.Key = None


    def _deserialize(self, params):
        self.Body = params.get("Body")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclRequest(AbstractModel):
    """BatchCreateAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(2:TOPIC）
        :type ResourceType: int
        :param ResourceNames: 资源列表数组
        :type ResourceNames: list of str
        :param RuleList: 设置的ACL规则列表
        :type RuleList: list of AclRuleInfo
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceNames = None
        self.RuleList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceNames = params.get("ResourceNames")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = AclRuleInfo()
                obj._deserialize(item)
                self.RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclResponse(AbstractModel):
    """BatchCreateAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 状态码
        :type Result: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BatchModifyGroupOffsetsRequest(AbstractModel):
    """BatchModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 消费分组名称
        :type GroupName: str
        :param InstanceId: 实例名称
        :type InstanceId: str
        :param Partitions: partition信息
        :type Partitions: list of Partitions
        :param TopicName: 指定topic，默认所有topic
        :type TopicName: list of str
        """
        self.GroupName = None
        self.InstanceId = None
        self.Partitions = None
        self.TopicName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.InstanceId = params.get("InstanceId")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = Partitions()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyGroupOffsetsResponse(AbstractModel):
    """BatchModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class BatchModifyTopicAttributesRequest(AbstractModel):
    """BatchModifyTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Topic: 主题属性列表
        :type Topic: list of BatchModifyTopicInfo
        """
        self.InstanceId = None
        self.Topic = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Topic") is not None:
            self.Topic = []
            for item in params.get("Topic"):
                obj = BatchModifyTopicInfo()
                obj._deserialize(item)
                self.Topic.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicAttributesResponse(AbstractModel):
    """BatchModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: list of BatchModifyTopicResultDTO
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = BatchModifyTopicResultDTO()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class BatchModifyTopicInfo(AbstractModel):
    """批量修改topic参数

    """

    def __init__(self):
        r"""
        :param TopicName: topic名称
        :type TopicName: str
        :param PartitionNum: 分区数
        :type PartitionNum: int
        :param Note: 备注
        :type Note: str
        :param ReplicaNum: 副本数
        :type ReplicaNum: int
        :param CleanUpPolicy: 消息删除策略，可以选择delete 或者compact
        :type CleanUpPolicy: str
        :param MinInsyncReplicas: 当producer设置request.required.acks为-1时，min.insync.replicas指定replicas的最小数目
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 是否允许非ISR的副本成为Leader
        :type UncleanLeaderElectionEnable: bool
        :param RetentionMs: topic维度的消息保留时间（毫秒）范围1 分钟到90 天
        :type RetentionMs: int
        :param RetentionBytes: topic维度的消息保留大小，范围1 MB到1024 GB
        :type RetentionBytes: int
        :param SegmentMs: Segment分片滚动的时长（毫秒），范围1 到90 天
        :type SegmentMs: int
        :param MaxMessageBytes: 批次的消息大小，范围1 KB到12 MB
        :type MaxMessageBytes: int
        """
        self.TopicName = None
        self.PartitionNum = None
        self.Note = None
        self.ReplicaNum = None
        self.CleanUpPolicy = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.RetentionBytes = None
        self.SegmentMs = None
        self.MaxMessageBytes = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        self.Note = params.get("Note")
        self.ReplicaNum = params.get("ReplicaNum")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.RetentionBytes = params.get("RetentionBytes")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicResultDTO(AbstractModel):
    """批量修改topic属性结果

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param TopicName: topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param ReturnCode: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: str
        :param Message: 状态消息
        :type Message: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.ReturnCode = None
        self.Message = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.ReturnCode = params.get("ReturnCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorizationTokenRequest(AbstractModel):
    """CancelAuthorizationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param User: 用户
        :type User: str
        :param Tokens: token串
        :type Tokens: str
        """
        self.InstanceId = None
        self.User = None
        self.Tokens = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Tokens = params.get("Tokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorizationTokenResponse(AbstractModel):
    """CancelAuthorizationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 0 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CdcClusterResponse(AbstractModel):
    """创建CDC 标准版共享集群出参

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCdcClusterRequest(AbstractModel):
    """CheckCdcCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCdcClusterResponse(AbstractModel):
    """CheckCdcCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果状态Success
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    """集群信息实体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: int
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param MaxDiskSize: 集群最大磁盘 单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSize: int
        :param MaxBandWidth: 集群最大带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBandWidth: int
        :param AvailableDiskSize: 集群当前可用磁盘  单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableDiskSize: int
        :param AvailableBandWidth: 集群当前可用带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableBandWidth: int
        :param ZoneId: 集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.MaxDiskSize = None
        self.MaxBandWidth = None
        self.AvailableDiskSize = None
        self.AvailableBandWidth = None
        self.ZoneId = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.AvailableDiskSize = params.get("AvailableDiskSize")
        self.AvailableBandWidth = params.get("AvailableBandWidth")
        self.ZoneId = params.get("ZoneId")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """高级配置对象

    """

    def __init__(self):
        r"""
        :param Retention: 消息保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param MinInsyncReplicas: 最小同步复制数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinInsyncReplicas: int
        :param CleanUpPolicy: 日志清理模式，默认 delete。
delete：日志按保存时间删除；compact：日志按 key 压缩；compact, delete：日志按 key 压缩且会保存时间删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type CleanUpPolicy: str
        :param SegmentMs: Segment 分片滚动的时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentMs: int
        :param UncleanLeaderElectionEnable: 0表示 false。 1表示 true。
注意：此字段可能返回 null，表示取不到有效值。
        :type UncleanLeaderElectionEnable: int
        :param SegmentBytes: Segment 分片滚动的字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentBytes: int
        :param MaxMessageBytes: 最大消息字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageBytes: int
        :param RetentionBytes: 消息保留文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionBytes: int
        """
        self.Retention = None
        self.MinInsyncReplicas = None
        self.CleanUpPolicy = None
        self.SegmentMs = None
        self.UncleanLeaderElectionEnable = None
        self.SegmentBytes = None
        self.MaxMessageBytes = None
        self.RetentionBytes = None


    def _deserialize(self, params):
        self.Retention = params.get("Retention")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.SegmentMs = params.get("SegmentMs")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.SegmentBytes = params.get("SegmentBytes")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.RetentionBytes = params.get("RetentionBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    """用户组实体

    """

    def __init__(self):
        r"""
        :param ConsumerGroupName: 用户组名称
        :type ConsumerGroupName: str
        :param SubscribedInfo: 订阅信息实体
        :type SubscribedInfo: list of SubscribedInfo
        """
        self.ConsumerGroupName = None
        self.SubscribedInfo = None


    def _deserialize(self, params):
        self.ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self.SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self.SubscribedInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupResponse(AbstractModel):
    """消费组返回结果实体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的消费组数量
        :type TotalCount: int
        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of ConsumerGroupTopic
        :param GroupList: 消费分组List
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of ConsumerGroup
        :param TotalPartition: 所有分区数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPartition: int
        :param PartitionListForMonitor: 监控的分区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionListForMonitor: list of Partition
        :param TotalTopic: 主题总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTopic: int
        :param TopicListForMonitor: 监控的主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param GroupListForMonitor: 监控的组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupListForMonitor: list of Group
        """
        self.TotalCount = None
        self.TopicList = None
        self.GroupList = None
        self.TotalPartition = None
        self.PartitionListForMonitor = None
        self.TotalTopic = None
        self.TopicListForMonitor = None
        self.GroupListForMonitor = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self.PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self.PartitionListForMonitor.append(obj)
        self.TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self.TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self.GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self.GroupListForMonitor.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupTopic(AbstractModel):
    """消费组主题对象

    """

    def __init__(self):
        r"""
        :param TopicId: 主题ID
        :type TopicId: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerRecord(AbstractModel):
    """消息记录

    """

    def __init__(self):
        r"""
        :param Topic: 主题名
        :type Topic: str
        :param Partition: 分区id
        :type Partition: int
        :param Offset: 位点
        :type Offset: int
        :param Key: 消息key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 消息value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Timestamp: 消息时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        """
        self.Topic = None
        self.Partition = None
        self.Offset = None
        self.Key = None
        self.Value = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRequest(AbstractModel):
    """CreateAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入时需要加 User: 前缀,如用户A则传入User:A。
        :type Principal: str
        :param ResourceNameList: 资源名称列表,Json字符串格式。ResourceName和resourceNameList只能指定其中一个。
        :type ResourceNameList: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.Operation = None
        self.PermissionType = None
        self.ResourceName = None
        self.Host = None
        self.Principal = None
        self.ResourceNameList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.ResourceName = params.get("ResourceName")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")
        self.ResourceNameList = params.get("ResourceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    """CreateAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateCdcClusterRequest(AbstractModel):
    """CreateCdcCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param CdcId: cdc的id
        :type CdcId: str
        :param CdcVpcId: vpcId,一个地域只有唯一一个vpcid用于CDC
        :type CdcVpcId: str
        :param CdcSubnetId: 每个CDC集群有唯一一个子网ID
        :type CdcSubnetId: str
        :param ZoneId: 所在可用区ID
        :type ZoneId: int
        :param Bandwidth: cdc集群的总带宽
        :type Bandwidth: int
        :param DiskSize: cdc集群的总磁盘
        :type DiskSize: int
        :param DiskType: 数据盘类型
        :type DiskType: str
        :param SystemDiskType: 系统盘类型
        :type SystemDiskType: str
        """
        self.CdcId = None
        self.CdcVpcId = None
        self.CdcSubnetId = None
        self.ZoneId = None
        self.Bandwidth = None
        self.DiskSize = None
        self.DiskType = None
        self.SystemDiskType = None


    def _deserialize(self, params):
        self.CdcId = params.get("CdcId")
        self.CdcVpcId = params.get("CdcVpcId")
        self.CdcSubnetId = params.get("CdcSubnetId")
        self.ZoneId = params.get("ZoneId")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.SystemDiskType = params.get("SystemDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdcClusterResponse(AbstractModel):
    """CreateCdcCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 无
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CdcClusterResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CdcClusterResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param GroupName: group名称
        :type GroupName: str
        :param TopicName: topic名称，TopicName、TopicNameList 需要显示指定一个存在的topic名称
        :type TopicName: str
        :param TopicNameList: topic名称数组
        :type TopicNameList: list of str
        """
        self.InstanceId = None
        self.GroupName = None
        self.TopicName = None
        self.TopicNameList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupName = params.get("GroupName")
        self.TopicName = params.get("TopicName")
        self.TopicNameList = params.get("TopicNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 创建group描述
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInstancePreData(AbstractModel):
    """创建预付费接口返回的Data

    """

    def __init__(self):
        r"""
        :param FlowId: CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param DealNames: 订单号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreRequest(AbstractModel):
    """CreateInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param ZoneId: 可用区
        :type ZoneId: int
        :param Period: 预付费购买时长，例如 "1m",就是一个月
        :type Period: str
        :param InstanceType: 实例规格说明 专业版实例[所有规格]填写1.
标准版实例 ([入门型]填写1，[标准型]填写2，[进阶型]填写3，[容量型]填写4，[高阶型1]填写5，[高阶性2]填写6,[高阶型3]填写7,[高阶型4]填写8，[独占型]填写9。
        :type InstanceType: int
        :param VpcId: vpcId，不填默认基础网络
        :type VpcId: str
        :param SubnetId: 子网id，vpc网络需要传该参数，基础网络可以不传
        :type SubnetId: str
        :param MsgRetentionTime: 可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id
        :type ClusterId: int
        :param RenewFlag: 预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type RenewFlag: int
        :param KafkaVersion: CKafka版本号[0.10.2、1.1.1、2.4.1], 默认是1.1.1
        :type KafkaVersion: str
        :param SpecificationsType: 实例类型: [标准版实例]填写 standard(默认), [专业版实例]填写 profession
        :type SpecificationsType: str
        :param DiskSize: 磁盘大小,专业版不填写默认最小磁盘,填写后根据磁盘带宽分区数弹性计算
        :type DiskSize: int
        :param BandWidth: 带宽,专业版不填写默认最小带宽,填写后根据磁盘带宽分区数弹性计算
        :type BandWidth: int
        :param Partition: 分区大小,专业版不填写默认最小分区数,填写后根据磁盘带宽分区数弹性计算
        :type Partition: int
        :param Tags: 标签
        :type Tags: list of Tag
        :param DiskType: 磁盘类型（ssd填写CLOUD_SSD，sata填写CLOUD_BASIC）
        :type DiskType: str
        :param MultiZoneFlag: 跨可用区，zoneIds必填
        :type MultiZoneFlag: bool
        :param ZoneIds: 可用区列表
        :type ZoneIds: list of int
        """
        self.InstanceName = None
        self.ZoneId = None
        self.Period = None
        self.InstanceType = None
        self.VpcId = None
        self.SubnetId = None
        self.MsgRetentionTime = None
        self.ClusterId = None
        self.RenewFlag = None
        self.KafkaVersion = None
        self.SpecificationsType = None
        self.DiskSize = None
        self.BandWidth = None
        self.Partition = None
        self.Tags = None
        self.DiskType = None
        self.MultiZoneFlag = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.ZoneId = params.get("ZoneId")
        self.Period = params.get("Period")
        self.InstanceType = params.get("InstanceType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.ClusterId = params.get("ClusterId")
        self.RenewFlag = params.get("RenewFlag")
        self.KafkaVersion = params.get("KafkaVersion")
        self.SpecificationsType = params.get("SpecificationsType")
        self.DiskSize = params.get("DiskSize")
        self.BandWidth = params.get("BandWidth")
        self.Partition = params.get("Partition")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DiskType = params.get("DiskType")
        self.MultiZoneFlag = params.get("MultiZoneFlag")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResp(AbstractModel):
    """创建预付费实例返回结构

    """

    def __init__(self):
        r"""
        :param ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param Data: 操作型返回的Data数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        :param DeleteRouteTimestamp: 删除是时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteRouteTimestamp: str
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None
        self.DeleteRouteTimestamp = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = CreateInstancePreData()
            self.Data._deserialize(params.get("Data"))
        self.DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResponse(AbstractModel):
    """CreateInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInstancePreResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreatePartitionRequest(AbstractModel):
    """CreatePartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param PartitionNum: 主题分区个数
        :type PartitionNum: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionResponse(AbstractModel):
    """CreatePartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateRouteRequest(AbstractModel):
    """CreateRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一id
        :type InstanceId: str
        :param VipType: 路由网络类型(3:vpc路由;4:标准版支撑路由;7:专业版支撑路由)
        :type VipType: int
        :param VpcId: vpc网络Id
        :type VpcId: str
        :param SubnetId: vpc子网id
        :type SubnetId: str
        :param AccessType: 访问类型
        :type AccessType: int
        :param AuthFlag: 是否需要权限管理
        :type AuthFlag: int
        :param CallerAppid: 调用方appId
        :type CallerAppid: int
        :param PublicNetwork: 公网带宽
        :type PublicNetwork: int
        :param Ip: vip地址
        :type Ip: str
        """
        self.InstanceId = None
        self.VipType = None
        self.VpcId = None
        self.SubnetId = None
        self.AccessType = None
        self.AuthFlag = None
        self.CallerAppid = None
        self.PublicNetwork = None
        self.Ip = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VipType = params.get("VipType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AccessType = params.get("AccessType")
        self.AuthFlag = params.get("AuthFlag")
        self.CallerAppid = params.get("CallerAppid")
        self.PublicNetwork = params.get("PublicNetwork")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteResponse(AbstractModel):
    """CreateRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTokenRequest(AbstractModel):
    """CreateToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param User: 用户名
        :type User: str
        """
        self.InstanceId = None
        self.User = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenResponse(AbstractModel):
    """CreateToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: token串
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称，是一个不超过 128 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type TopicName: str
        :param PartitionNum: Partition个数，大于0
        :type PartitionNum: int
        :param ReplicaNum: 副本个数，不能多于 broker 数，最大为3
        :type ReplicaNum: int
        :param EnableWhiteList: ip白名单开关, 1:打开  0:关闭，默认不打开
        :type EnableWhiteList: int
        :param IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选
        :type IpWhiteList: list of str
        :param CleanUpPolicy: 清理日志策略，日志清理模式，默认为"delete"。"delete"：日志按保存时间删除，"compact"：日志按 key 压缩，"compact, delete"：日志按 key 压缩且会按保存时间删除。
        :type CleanUpPolicy: str
        :param Note: 主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type Note: str
        :param MinInsyncReplicas: 默认为1
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 可选参数。消息保留时间，单位ms，当前最小值为60000ms
        :type RetentionMs: int
        :param SegmentMs: Segment分片滚动的时长，单位ms，当前最小为3600000ms
        :type SegmentMs: int
        :param MaxMessageBytes: 主题消息最大值，单位为 Byte，最小值1024Byte(即1KB)，最大值为8388608Byte（即8MB）。
        :type MaxMessageBytes: int
        :param EnableAclRule: 预设ACL规则, 1:打开  0:关闭，默认不打开
        :type EnableAclRule: int
        :param AclRuleName: 预设ACL规则的名称
        :type AclRuleName: str
        :param RetentionBytes: 可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :type RetentionBytes: int
        :param Tags: 标签列表
        :type Tags: list of Tag
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.CleanUpPolicy = None
        self.Note = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None
        self.MaxMessageBytes = None
        self.EnableAclRule = None
        self.AclRuleName = None
        self.RetentionBytes = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.Note = params.get("Note")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.EnableAclRule = params.get("EnableAclRule")
        self.AclRuleName = params.get("AclRuleName")
        self.RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    """创建主题返回

    """

    def __init__(self):
        r"""
        :param TopicId: 主题Id
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回创建结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateTopicResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        :param Password: 用户密码
        :type Password: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRequest(AbstractModel):
    """DeleteAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param Principal: 用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclResponse(AbstractModel):
    """DeleteAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRuleRequest(AbstractModel):
    """DeleteAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param RuleName: acl规则名称
        :type RuleName: str
        """
        self.InstanceId = None
        self.RuleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRuleResponse(AbstractModel):
    """DeleteAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回被删除的规则的ID
        :type Result: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Group: 消费分组
        :type Group: str
        """
        self.InstanceId = None
        self.Group = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteInstancePreRequest(AbstractModel):
    """DeleteInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstancePreResponse(AbstractModel):
    """DeleteInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInstancePreResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteRouteRequest(AbstractModel):
    """DeleteRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一id
        :type InstanceId: str
        :param RouteId: 路由id
        :type RouteId: int
        :param CallerAppid: 调用方appId
        :type CallerAppid: int
        :param DeleteRouteTime: 删除路由时间
        :type DeleteRouteTime: str
        """
        self.InstanceId = None
        self.RouteId = None
        self.CallerAppid = None
        self.DeleteRouteTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RouteId = params.get("RouteId")
        self.CallerAppid = params.get("CallerAppid")
        self.DeleteRouteTime = params.get("DeleteRouteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteResponse(AbstractModel):
    """DeleteRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteRouteTriggerTimeRequest(AbstractModel):
    """DeleteRouteTriggerTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param DelayTime: 修改时间
        :type DelayTime: str
        """
        self.DelayTime = None


    def _deserialize(self, params):
        self.DelayTime = params.get("DelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTriggerTimeResponse(AbstractModel):
    """DeleteRouteTriggerTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ckafka 实例Id
        :type InstanceId: str
        :param TopicName: ckafka 主题名称
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 个数限制
        :type Limit: int
        :param SearchWord: 关键字匹配
        :type SearchWord: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeACLResponse(AbstractModel):
    """DescribeACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的ACL结果集对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AclResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 本次查询用户数目最大数量限制，最大值为50，默认50
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的符合要求的App Id列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AppIdResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeCkafkaZoneRequest(AbstractModel):
    """DescribeCkafkaZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param CdcId: cdc专业集群业务参数
        :type CdcId: str
        """
        self.CdcId = None


    def _deserialize(self, params):
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkafkaZoneResponse(AbstractModel):
    """DescribeCkafkaZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询结果复杂对象实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ZoneResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ckafka实例id。
        :type InstanceId: str
        :param GroupName: 可选，用户需要查询的group名称。
        :type GroupName: str
        :param TopicName: 可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。
        :type TopicName: str
        :param Limit: 本次返回个数限制
        :type Limit: int
        :param Offset: 偏移位置
        :type Offset: int
        """
        self.InstanceId = None
        self.GroupName = None
        self.TopicName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupName = params.get("GroupName")
        self.TopicName = params.get("TopicName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的消费分组信息
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerGroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """DescribeGroup返回实体

    """

    def __init__(self):
        r"""
        :param Group: groupId
        :type Group: str
        :param Protocol: 该 group 使用的协议。
        :type Protocol: str
        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: （过滤条件）按照实例 ID 过滤。
        :type InstanceId: str
        :param GroupList: Kafka 消费分组，Consumer-group，这里是数组形式，格式：GroupList.0=xxx&GroupList.1=yyy。
        :type GroupList: list of str
        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of GroupInfoResponse
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: （过滤条件）按照实例 ID 过滤
        :type InstanceId: str
        :param Group: Kafka 消费分组
        :type Group: str
        :param Topics: group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息
        :type Topics: list of str
        :param SearchWord: 模糊匹配 topicName
        :type SearchWord: str
        :param Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        """
        self.InstanceId = None
        self.Group = None
        self.Topics = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Topics = params.get("Topics")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupOffsetResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 最大返回数量
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果集列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 实例属性返回结果对象。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认10，最大值20。
        :type Limit: int
        :param TagKey: 匹配标签key值。
        :type TagKey: str
        :param Filters: 过滤器。filter.Name 支持('Ip', 'VpcId', 'SubNetId', 'InstanceType','InstanceId') ,filter.Values最多传递10个值.
        :type Filters: list of Filter
        :param InstanceIds: 已经废弃， 使用InstanceIdList
        :type InstanceIds: str
        :param InstanceIdList: 按照实例ID过滤
        :type InstanceIdList: list of str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None
        self.Filters = None
        self.InstanceIds = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的实例详情结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认10，最大值100
        :type Limit: int
        :param TagKey: 已废弃。匹配标签key值。
        :type TagKey: str
        :param VpcId: 私有网络Id
        :type VpcId: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None
        self.VpcId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    """DescribeRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回最大结果数
        :type Limit: int
        :param Business: 业务字段，可忽略
        :type Business: str
        :param CdcId: cdc专有集群业务字段，可忽略
        :type CdcId: str
        """
        self.Offset = None
        self.Limit = None
        self.Business = None
        self.CdcId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Business = params.get("Business")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回地域枚举结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of Region
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的路由信息结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = RouteResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照topicName过滤，支持模糊查询
        :type SearchWord: str
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认 10，最大值20，取值要大于0
        :type Limit: int
        :param AclRuleName: Acl预设策略名称
        :type AclRuleName: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.AclRuleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AclRuleName = params.get("AclRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的主题详情实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param SearchWord: 过滤条件，按照 topicName 过滤，支持模糊查询
        :type SearchWord: str
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为50
        :type Limit: int
        :param AclRuleName: Acl预设策略名称
        :type AclRuleName: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.AclRuleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AclRuleName = params.get("AclRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicSubscribeGroupRequest(AbstractModel):
    """DescribeTopicSubscribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param Offset: 分页时的起始位置
        :type Offset: int
        :param Limit: 分页时的个数
        :type Limit: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSubscribeGroupResponse(AbstractModel):
    """DescribeTopicSubscribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicSubscribeGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicSyncReplicaRequest(AbstractModel):
    """DescribeTopicSyncReplica请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认10，最大值20。
        :type Limit: int
        :param OutOfSyncReplicaOnly: 仅筛选未同步副本
        :type OutOfSyncReplicaOnly: bool
        """
        self.InstanceId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.OutOfSyncReplicaOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OutOfSyncReplicaOnly = params.get("OutOfSyncReplicaOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSyncReplicaResponse(AbstractModel):
    """DescribeTopicSyncReplica返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回topic 副本详情
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicInSyncReplicaResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param SearchWord: 按照名称过滤
        :type SearchWord: str
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 本次返回个数
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UserResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DynamicDiskConfig(AbstractModel):
    """动态硬盘扩容配置

    """

    def __init__(self):
        r"""
        :param Enable: 动态硬盘扩容配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param StepForwardPercentage: 每次磁盘动态扩容大小百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type StepForwardPercentage: int
        :param DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发硬盘自动扩容事件
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskQuotaPercentage: int
        :param MaxDiskSpace: 最大扩容硬盘大小，以 GB 为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSpace: int
        """
        self.Enable = None
        self.StepForwardPercentage = None
        self.DiskQuotaPercentage = None
        self.MaxDiskSpace = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.MaxDiskSpace = params.get("MaxDiskSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicRetentionTime(AbstractModel):
    """动态消息保留时间配置

    """

    def __init__(self):
        r"""
        :param Enable: 动态消息保留时间配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发消息保留时间变更事件
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskQuotaPercentage: int
        :param StepForwardPercentage: 每次向前调整消息保留时间百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type StepForwardPercentage: int
        :param BottomRetention: 保底时长，单位分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type BottomRetention: int
        """
        self.Enable = None
        self.DiskQuotaPercentage = None
        self.StepForwardPercentage = None
        self.BottomRetention = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.BottomRetention = params.get("BottomRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetRequest(AbstractModel):
    """FetchMessageByOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Topic: 主题名
        :type Topic: str
        :param Partition: 分区id
        :type Partition: int
        :param Offset: 位点信息，必填
        :type Offset: int
        """
        self.InstanceId = None
        self.Topic = None
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Topic = params.get("Topic")
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetResponse(AbstractModel):
    """FetchMessageByOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerRecord()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤器
    >描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Group(AbstractModel):
    """组实体

    """

    def __init__(self):
        r"""
        :param GroupName: 组名称
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoMember(AbstractModel):
    """consumer信息

    """

    def __init__(self):
        r"""
        :param MemberId: coordinator 为消费分组中的消费者生成的唯一 ID
        :type MemberId: str
        :param ClientId: 客户消费者 SDK 自己设置的 client.id 信息
        :type ClientId: str
        :param ClientHost: 一般存储客户的 IP 地址
        :type ClientHost: str
        :param Assignment: 存储着分配给该消费者的 partition 信息
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self.MemberId = None
        self.ClientId = None
        self.ClientHost = None
        self.Assignment = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.ClientId = params.get("ClientId")
        self.ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self.Assignment = Assignment()
            self.Assignment._deserialize(params.get("Assignment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoResponse(AbstractModel):
    """GroupInfo返回数据的实体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 错误码，正常为0
        :type ErrorCode: str
        :param State: group 状态描述（常见的为 Empty、Stable、Dead 三种状态）：
Dead：消费分组不存在
Empty：消费分组，当前没有任何消费者订阅
PreparingRebalance：消费分组处于 rebalance 状态
CompletingRebalance：消费分组处于 rebalance 状态
Stable：消费分组中各个消费者已经加入，处于稳定状态
        :type State: str
        :param ProtocolType: 消费分组选择的协议类型正常的消费者一般为 consumer 但有些系统采用了自己的协议如 kafka-connect 用的就是 connect。只有标准的 consumer 协议，本接口才知道具体的分配方式的格式，才能解析到具体的 partition 的分配情况
        :type ProtocolType: str
        :param Protocol: 消费者 partition 分配算法常见的有如下几种(Kafka 消费者 SDK 默认的选择项为 range)：range、 roundrobin、 sticky
        :type Protocol: str
        :param Members: 仅当 state 为 Stable 且 protocol_type 为 consumer 时， 该数组才包含信息
        :type Members: list of GroupInfoMember
        :param Group: Kafka 消费分组
        :type Group: str
        """
        self.ErrorCode = None
        self.State = None
        self.ProtocolType = None
        self.Protocol = None
        self.Members = None
        self.Group = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.State = params.get("State")
        self.ProtocolType = params.get("ProtocolType")
        self.Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoTopics(AbstractModel):
    """GroupInfo内部topic对象

    """

    def __init__(self):
        r"""
        :param Topic: 分配的 topic 名称
        :type Topic: str
        :param Partitions: 分配的 partition 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of int
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetPartition(AbstractModel):
    """组偏移量分区对象

    """

    def __init__(self):
        r"""
        :param Partition: topic 的 partitionId
        :type Partition: int
        :param Offset: consumer 提交的 offset 位置
        :type Offset: int
        :param Metadata: 支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: str
        :param ErrorCode: 错误码
        :type ErrorCode: int
        :param LogEndOffset: 当前 partition 最新的 offset
        :type LogEndOffset: int
        :param Lag: 未消费的消息个数
        :type Lag: int
        """
        self.Partition = None
        self.Offset = None
        self.Metadata = None
        self.ErrorCode = None
        self.LogEndOffset = None
        self.Lag = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Metadata = params.get("Metadata")
        self.ErrorCode = params.get("ErrorCode")
        self.LogEndOffset = params.get("LogEndOffset")
        self.Lag = params.get("Lag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetResponse(AbstractModel):
    """消费组偏移量返回结果

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合调节的总结果数
        :type TotalCount: int
        :param TopicList: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of GroupOffsetTopic
        """
        self.TotalCount = None
        self.TopicList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetTopic(AbstractModel):
    """消费分组主题对象

    """

    def __init__(self):
        r"""
        :param Topic: 主题名称
        :type Topic: str
        :param Partitions: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of GroupOffsetPartition
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResponse(AbstractModel):
    """DescribeGroup的返回

    """

    def __init__(self):
        r"""
        :param TotalCount: 计数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param GroupList: GroupList
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribeGroup
        """
        self.TotalCount = None
        self.GroupList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例对象

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中 ， 5 隔离中，-1 创建失败
        :type Status: int
        :param IfCommunity: 是否开源实例。开源：true，不开源：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IfCommunity: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAttributesResponse(AbstractModel):
    """实例属性返回结果对象

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param VipList: 接入点 VIP 列表信息
        :type VipList: list of VipEntity
        :param Vip: 虚拟IP
        :type Vip: str
        :param Vport: 虚拟端口
        :type Vport: str
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中
        :type Status: int
        :param Bandwidth: 实例带宽，单位：Mbps
        :type Bandwidth: int
        :param DiskSize: 实例的存储大小，单位：GB
        :type DiskSize: int
        :param ZoneId: 可用区
        :type ZoneId: int
        :param VpcId: VPC 的 ID，为空表示是基础网络
        :type VpcId: str
        :param SubnetId: 子网 ID， 为空表示基础网络
        :type SubnetId: str
        :param Healthy: 实例健康状态， 1：健康，2：告警，3：异常
        :type Healthy: int
        :param HealthyMessage: 实例健康信息，当前会展示磁盘利用率，最大长度为256
        :type HealthyMessage: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param MsgRetentionTime: 消息保存时间,单位为分钟
        :type MsgRetentionTime: int
        :param Config: 自动创建 Topic 配置， 若该字段为空，则表示未开启自动创建
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param RemainderPartitions: 剩余创建分区数
        :type RemainderPartitions: int
        :param RemainderTopics: 剩余创建主题数
        :type RemainderTopics: int
        :param CreatedPartitions: 当前创建分区数
        :type CreatedPartitions: int
        :param CreatedTopics: 当前创建主题数
        :type CreatedTopics: int
        :param Tags: 标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param MaxGroupNum: 最大分组数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxGroupNum: int
        :param Cvm: 售卖类型,0:标准版,1:专业版
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param InstanceType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Features: 表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param RetentionTimeConfig: 动态消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param MaxConnection: 最大连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConnection: int
        :param PublicNetwork: 公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: int
        :param DeleteRouteTimestamp: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteRouteTimestamp: str
        :param RemainingPartitions: 剩余创建分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingPartitions: int
        :param RemainingTopics: 剩余创建主题数
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingTopics: int
        :param DynamicDiskConfig: 动态硬盘扩容策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VipList = None
        self.Vip = None
        self.Vport = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.MsgRetentionTime = None
        self.Config = None
        self.RemainderPartitions = None
        self.RemainderTopics = None
        self.CreatedPartitions = None
        self.CreatedTopics = None
        self.Tags = None
        self.ExpireTime = None
        self.ZoneIds = None
        self.Version = None
        self.MaxGroupNum = None
        self.Cvm = None
        self.InstanceType = None
        self.Features = None
        self.RetentionTimeConfig = None
        self.MaxConnection = None
        self.PublicNetwork = None
        self.DeleteRouteTimestamp = None
        self.RemainingPartitions = None
        self.RemainingTopics = None
        self.DynamicDiskConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self.Config = InstanceConfigDO()
            self.Config._deserialize(params.get("Config"))
        self.RemainderPartitions = params.get("RemainderPartitions")
        self.RemainderTopics = params.get("RemainderTopics")
        self.CreatedPartitions = params.get("CreatedPartitions")
        self.CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ExpireTime = params.get("ExpireTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Version = params.get("Version")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.Features = params.get("Features")
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = DynamicRetentionTime()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self.MaxConnection = params.get("MaxConnection")
        self.PublicNetwork = params.get("PublicNetwork")
        self.DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        self.RemainingPartitions = params.get("RemainingPartitions")
        self.RemainingTopics = params.get("RemainingTopics")
        if params.get("DynamicDiskConfig") is not None:
            self.DynamicDiskConfig = DynamicDiskConfig()
            self.DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigDO(AbstractModel):
    """实例配置实体

    """

    def __init__(self):
        r"""
        :param AutoCreateTopicsEnable: 是否自动创建主题
        :type AutoCreateTopicsEnable: bool
        :param DefaultNumPartitions: 分区数
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 默认的复制Factor
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Vip: 访问实例的vip 信息
        :type Vip: str
        :param Vport: 访问实例的端口信息
        :type Vport: str
        :param VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中：5隔离中， -1 创建失败
        :type Status: int
        :param Bandwidth: 实例带宽，单位Mbps
        :type Bandwidth: int
        :param DiskSize: 实例的存储大小，单位GB
        :type DiskSize: int
        :param ZoneId: 可用区域ID
        :type ZoneId: int
        :param VpcId: vpcId，如果为空，说明是基础网络
        :type VpcId: str
        :param SubnetId: 子网id
        :type SubnetId: str
        :param RenewFlag: 实例是否续费，int  枚举值：1表示自动续费，2表示明确不自动续费
        :type RenewFlag: int
        :param Healthy: 实例状态 int：1表示健康，2表示告警，3 表示实例状态异常
        :type Healthy: int
        :param HealthyMessage: 实例状态信息
        :type HealthyMessage: str
        :param CreateTime: 实例创建时间时间
        :type CreateTime: int
        :param ExpireTime: 实例过期时间
        :type ExpireTime: int
        :param IsInternal: 是否为内部客户。值为1 表示内部客户
        :type IsInternal: int
        :param TopicNum: Topic个数
        :type TopicNum: int
        :param Tags: 标识tag
        :type Tags: list of Tag
        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Cvm: ckafka售卖类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param InstanceType: ckafka实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param MaxTopicNumber: 当前规格最大Topic数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTopicNumber: int
        :param MaxPartitionNumber: 当前规格最大Partition数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPartitionNumber: int
        :param RebalanceTime: 计划升级配置时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RebalanceTime: str
        :param PartitionNumber: 实例当前partition数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNumber: int
        :param PublicNetworkChargeType: 公网带宽类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkChargeType: str
        :param PublicNetwork: 公网带宽值
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: int
        :param ClusterType: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.VipList = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.RenewFlag = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsInternal = None
        self.TopicNum = None
        self.Tags = None
        self.Version = None
        self.ZoneIds = None
        self.Cvm = None
        self.InstanceType = None
        self.DiskType = None
        self.MaxTopicNumber = None
        self.MaxPartitionNumber = None
        self.RebalanceTime = None
        self.PartitionNumber = None
        self.PublicNetworkChargeType = None
        self.PublicNetwork = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RenewFlag = params.get("RenewFlag")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsInternal = params.get("IsInternal")
        self.TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Version = params.get("Version")
        self.ZoneIds = params.get("ZoneIds")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.DiskType = params.get("DiskType")
        self.MaxTopicNumber = params.get("MaxTopicNumber")
        self.MaxPartitionNumber = params.get("MaxPartitionNumber")
        self.RebalanceTime = params.get("RebalanceTime")
        self.PartitionNumber = params.get("PartitionNumber")
        self.PublicNetworkChargeType = params.get("PublicNetworkChargeType")
        self.PublicNetwork = params.get("PublicNetwork")
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetailResponse(AbstractModel):
    """实例详情返回结果

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例总数
        :type TotalCount: int
        :param InstanceList: 符合条件的实例详情列表
        :type InstanceList: list of InstanceDetail
        """
        self.TotalCount = None
        self.InstanceList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceQuotaConfigResp(AbstractModel):
    """实例 / topic 维度限流策略

    """

    def __init__(self):
        r"""
        :param QuotaProducerByteRate: 生产限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaProducerByteRate: int
        :param QuotaConsumerByteRate: 消费限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaConsumerByteRate: int
        """
        self.QuotaProducerByteRate = None
        self.QuotaConsumerByteRate = None


    def _deserialize(self, params):
        self.QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self.QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceResponse(AbstractModel):
    """聚合的实例状态返回结果

    """

    def __init__(self):
        r"""
        :param InstanceList: 符合条件的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of Instance
        :param TotalCount: 符合条件的结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.InstanceList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JgwOperateResponse(AbstractModel):
    """操作型结果返回值

    """

    def __init__(self):
        r"""
        :param ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param Data: 操作型返回的Data数据,可能有flowId等
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: kafka实例id
        :type InstanceId: str
        :param Group: kafka 消费分组
        :type Group: str
        :param Strategy: 重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置
        :type Strategy: int
        :param Topics: 表示需要重置的topics， 不填表示全部
        :type Topics: list of str
        :param Shift: 当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest
        :type Shift: int
        :param ShiftTimestamp: 单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。
        :type ShiftTimestamp: int
        :param Offset: 需要重新设置的offset位置。当strategy为2，必须包含该字段。
        :type Offset: int
        :param Partitions: 需要重新设置的partition的列表，如果没有指定Topics参数。则重置全部topics的对应的Partition列表里的partition。指定Topics时则重置指定的topic列表的对应的Partitions列表的partition。
        :type Partitions: list of int
        """
        self.InstanceId = None
        self.Group = None
        self.Strategy = None
        self.Topics = None
        self.Shift = None
        self.ShiftTimestamp = None
        self.Offset = None
        self.Partitions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Strategy = params.get("Strategy")
        self.Topics = params.get("Topics")
        self.Shift = params.get("Shift")
        self.ShiftTimestamp = params.get("ShiftTimestamp")
        self.Offset = params.get("Offset")
        self.Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """修改实例属性的配置对象

    """

    def __init__(self):
        r"""
        :param AutoCreateTopicEnable: 自动创建 true 表示开启，false 表示不开启
        :type AutoCreateTopicEnable: bool
        :param DefaultNumPartitions: 可选，如果auto.create.topic.enable设置为true没有设置该值时，默认设置为3
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 如歌auto.create.topic.enable设置为true没有指定该值时默认设置为2
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param MsgRetentionTime: 实例日志的最长保留时间，单位分钟，最大30天，0代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param Config: 实例配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param DynamicRetentionConfig: 动态消息保留策略配置
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param RebalanceTime: 修改升配置rebalance时间
        :type RebalanceTime: int
        :param PublicNetwork: 时间戳
        :type PublicNetwork: int
        :param DynamicDiskConfig: 动态硬盘扩容策略配置
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        self.InstanceId = None
        self.MsgRetentionTime = None
        self.InstanceName = None
        self.Config = None
        self.DynamicRetentionConfig = None
        self.RebalanceTime = None
        self.PublicNetwork = None
        self.DynamicDiskConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self.Config = ModifyInstanceAttributesConfig()
            self.Config._deserialize(params.get("Config"))
        if params.get("DynamicRetentionConfig") is not None:
            self.DynamicRetentionConfig = DynamicRetentionTime()
            self.DynamicRetentionConfig._deserialize(params.get("DynamicRetentionConfig"))
        self.RebalanceTime = params.get("RebalanceTime")
        self.PublicNetwork = params.get("PublicNetwork")
        if params.get("DynamicDiskConfig") is not None:
            self.DynamicDiskConfig = DynamicDiskConfig()
            self.DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyInstancePreRequest(AbstractModel):
    """ModifyInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例名称
        :type InstanceId: str
        :param DiskSize: 预计磁盘，根据磁盘步长，规格向上调整。
        :type DiskSize: int
        :param BandWidth: 预计带宽，根据带宽步长，规格向上调整。
        :type BandWidth: int
        :param Partition: 预计分区，根据带宽步长，规格向上调整。
        :type Partition: int
        """
        self.InstanceId = None
        self.DiskSize = None
        self.BandWidth = None
        self.Partition = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DiskSize = params.get("DiskSize")
        self.BandWidth = params.get("BandWidth")
        self.Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePreResponse(AbstractModel):
    """ModifyInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 变更预付费实例配置返回结构
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInstancePreResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        :param Password: 用户当前密码
        :type Password: str
        :param PasswordNew: 用户新密码
        :type PasswordNew: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param Note: 主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :type Note: str
        :param EnableWhiteList: IP 白名单开关，1：打开；0：关闭。
        :type EnableWhiteList: int
        :param MinInsyncReplicas: 默认为1。
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 默认为 0，0：false；1：true。
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 消息保留时间，单位：ms，当前最小值为60000ms。
        :type RetentionMs: int
        :param SegmentMs: Segment 分片滚动的时长，单位：ms，当前最小为86400000ms。
        :type SegmentMs: int
        :param MaxMessageBytes: 主题消息最大值，单位为 Byte，最大值为12582912Byte（即12MB）。
        :type MaxMessageBytes: int
        :param CleanUpPolicy: 消息删除策略，可以选择delete 或者compact
        :type CleanUpPolicy: str
        :param IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选
        :type IpWhiteList: list of str
        :param EnableAclRule: 预设ACL规则, 1:打开  0:关闭，默认不打开
        :type EnableAclRule: int
        :param AclRuleName: 预设ACL规则的名称
        :type AclRuleName: str
        :param RetentionBytes: 可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :type RetentionBytes: int
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param QuotaProducerByteRate: 生产限流，单位 MB/s
        :type QuotaProducerByteRate: int
        :param QuotaConsumerByteRate: 消费限流，单位 MB/s
        :type QuotaConsumerByteRate: int
        :param ReplicaNum: 调整topic副本数
        :type ReplicaNum: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.Note = None
        self.EnableWhiteList = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None
        self.MaxMessageBytes = None
        self.CleanUpPolicy = None
        self.IpWhiteList = None
        self.EnableAclRule = None
        self.AclRuleName = None
        self.RetentionBytes = None
        self.Tags = None
        self.QuotaProducerByteRate = None
        self.QuotaConsumerByteRate = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.IpWhiteList = params.get("IpWhiteList")
        self.EnableAclRule = params.get("EnableAclRule")
        self.AclRuleName = params.get("AclRuleName")
        self.RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self.QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        self.ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    """操作类型返回的Data结构

    """

    def __init__(self):
        r"""
        :param FlowId: FlowId11
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """分区实体

    """

    def __init__(self):
        r"""
        :param PartitionId: 分区ID
        :type PartitionId: int
        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionOffset(AbstractModel):
    """分区和位移

    """

    def __init__(self):
        r"""
        :param Partition: Partition,例如"0"或"1"
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: str
        :param Offset: Offset,例如100
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partitions(AbstractModel):
    """partition信息

    """

    def __init__(self):
        r"""
        :param Partition: 分区
        :type Partition: int
        :param Offset: partition 消费位移
        :type Offset: int
        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """消息价格实体

    """

    def __init__(self):
        r"""
        :param RealTotalCost: 折扣价
        :type RealTotalCost: float
        :param TotalCost: 原价
        :type TotalCost: float
        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """地域实体对象

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID
        :type RegionId: int
        :param RegionName: 地域名称
        :type RegionName: str
        :param AreaName: 区域名称
        :type AreaName: str
        :param RegionCode: 地域代码
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCode: str
        :param RegionCodeV3: 地域代码（V3版本）
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCodeV3: str
        :param Support: NONE:默认值不支持任何特殊机型\nCVM:支持CVM类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Support: str
        :param Ipv6: 是否支持ipv6, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: int
        :param MultiZone: 是否支持跨可用区, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiZone: int
        """
        self.RegionId = None
        self.RegionName = None
        self.AreaName = None
        self.RegionCode = None
        self.RegionCodeV3 = None
        self.Support = None
        self.Ipv6 = None
        self.MultiZone = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.AreaName = params.get("AreaName")
        self.RegionCode = params.get("RegionCode")
        self.RegionCodeV3 = params.get("RegionCodeV3")
        self.Support = params.get("Support")
        self.Ipv6 = params.get("Ipv6")
        self.MultiZone = params.get("MultiZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """路由实体对象

    """

    def __init__(self):
        r"""
        :param AccessType: 实例接入方式
0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
        :type AccessType: int
        :param RouteId: 路由ID
        :type RouteId: int
        :param VipType: vip网络类型（1:外网TGW  2:基础网络 3:VPC网络 4:支撑网络(idc 环境) 5:SSL外网访问方式访问 6:黑石环境vpc 7:支撑网络(cvm 环境）
        :type VipType: int
        :param VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainPort: 域名port
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainPort: int
        :param DeleteTimestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteTimestamp: str
        """
        self.AccessType = None
        self.RouteId = None
        self.VipType = None
        self.VipList = None
        self.Domain = None
        self.DomainPort = None
        self.DeleteTimestamp = None


    def _deserialize(self, params):
        self.AccessType = params.get("AccessType")
        self.RouteId = params.get("RouteId")
        self.VipType = params.get("VipType")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Domain = params.get("Domain")
        self.DomainPort = params.get("DomainPort")
        self.DeleteTimestamp = params.get("DeleteTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    """路由信息返回对象

    """

    def __init__(self):
        r"""
        :param Routers: 路由信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Routers: list of Route
        """
        self.Routers = None


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self.Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self.Routers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleInfo(AbstractModel):
    """标准版销售信息

    """

    def __init__(self):
        r"""
        :param Flag: 手动设置的flag标志
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: bool
        :param Version: ckakfa版本号(1.1.1/2.4.2/0.10.2)
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param Platform: 专业版、标准版标志
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param SoldOut: 售罄标志：true售罄
注意：此字段可能返回 null，表示取不到有效值。
        :type SoldOut: bool
        """
        self.Flag = None
        self.Version = None
        self.Platform = None
        self.SoldOut = None


    def _deserialize(self, params):
        self.Flag = params.get("Flag")
        self.Version = params.get("Version")
        self.Platform = params.get("Platform")
        self.SoldOut = params.get("SoldOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param DataHubId: DataHub接入ID
        :type DataHubId: str
        :param Message: 发送消息内容(单次请求最多500条)
        :type Message: list of BatchContent
        """
        self.DataHubId = None
        self.Message = None


    def _deserialize(self, params):
        self.DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self.Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self.Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param MessageId: 消息ID列表
        :type MessageId: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")


class SubscribedInfo(AbstractModel):
    """订阅信息实体

    """

    def __init__(self):
        r"""
        :param TopicName: 订阅的主题名
        :type TopicName: str
        :param Partition: 订阅的分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: list of int
        :param PartitionOffset: 分区offset信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionOffset: list of PartitionOffset
        :param TopicId: 订阅的主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self.TopicName = None
        self.Partition = None
        self.PartitionOffset = None
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self.PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self.PartitionOffset.append(obj)
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """实例详情中的标签对象

    """

    def __init__(self):
        r"""
        :param TagKey: 标签的key
        :type TagKey: str
        :param TagValue: 标签的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic(AbstractModel):
    """返回的topic对象

    """

    def __init__(self):
        r"""
        :param TopicId: 主题的ID
        :type TopicId: str
        :param TopicName: 主题的名称
        :type TopicName: str
        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAttributesResponse(AbstractModel):
    """主题属性返回结果实体

    """

    def __init__(self):
        r"""
        :param TopicId: 主题 ID
        :type TopicId: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param Note: 主题备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param PartitionNum: 分区个数
        :type PartitionNum: int
        :param EnableWhiteList: IP 白名单开关，1：打开； 0：关闭
        :type EnableWhiteList: int
        :param IpWhiteList: IP 白名单列表
        :type IpWhiteList: list of str
        :param Config: topic 配置数组
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param Partitions: 分区详情
        :type Partitions: list of TopicPartitionDO
        :param EnableAclRule: ACL预设策略开关，1：打开； 0：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableAclRule: int
        :param AclRuleList: 预设策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AclRuleList: list of AclRule
        :param QuotaConfig: topic 限流策略
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaConfig: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        """
        self.TopicId = None
        self.CreateTime = None
        self.Note = None
        self.PartitionNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.Config = None
        self.Partitions = None
        self.EnableAclRule = None
        self.AclRuleList = None
        self.QuotaConfig = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Note = params.get("Note")
        self.PartitionNum = params.get("PartitionNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.EnableAclRule = params.get("EnableAclRule")
        if params.get("AclRuleList") is not None:
            self.AclRuleList = []
            for item in params.get("AclRuleList"):
                obj = AclRule()
                obj._deserialize(item)
                self.AclRuleList.append(obj)
        if params.get("QuotaConfig") is not None:
            self.QuotaConfig = InstanceQuotaConfigResp()
            self.QuotaConfig._deserialize(params.get("QuotaConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetail(AbstractModel):
    """主题详情

    """

    def __init__(self):
        r"""
        :param TopicName: 主题名称
        :type TopicName: str
        :param TopicId: 主题ID
        :type TopicId: str
        :param PartitionNum: 分区数
        :type PartitionNum: int
        :param ReplicaNum: 副本数
        :type ReplicaNum: int
        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param EnableWhiteList: 是否开启ip鉴权白名单，true表示开启，false表示不开启
        :type EnableWhiteList: bool
        :param IpWhiteListCount: ip白名单中ip个数
        :type IpWhiteListCount: int
        :param ForwardCosBucket: 数据备份cos bucket: 转存到cos 的bucket地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardCosBucket: str
        :param ForwardStatus: 数据备份cos 状态： 1 不开启数据备份，0 开启数据备份
        :type ForwardStatus: int
        :param ForwardInterval: 数据备份到cos的周期频率
        :type ForwardInterval: int
        :param Config: 高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param RetentionTimeConfig: 消息保留时间配置(用于动态配置变更记录)
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        :param Status: 0:正常，1：已删除，2：删除中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.TopicName = None
        self.TopicId = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.Note = None
        self.CreateTime = None
        self.EnableWhiteList = None
        self.IpWhiteListCount = None
        self.ForwardCosBucket = None
        self.ForwardStatus = None
        self.ForwardInterval = None
        self.Config = None
        self.RetentionTimeConfig = None
        self.Status = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.Note = params.get("Note")
        self.CreateTime = params.get("CreateTime")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteListCount = params.get("IpWhiteListCount")
        self.ForwardCosBucket = params.get("ForwardCosBucket")
        self.ForwardStatus = params.get("ForwardStatus")
        self.ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = TopicRetentionTimeConfigRsp()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetailResponse(AbstractModel):
    """主题详情返回实体

    """

    def __init__(self):
        r"""
        :param TopicList: 返回的主题详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of TopicDetail
        :param TotalCount: 符合条件的所有主题详情数量
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaInfo(AbstractModel):
    """topic副本及详细信息

    """

    def __init__(self):
        r"""
        :param Partition: 分区名称
        :type Partition: str
        :param Leader: Leader Id
        :type Leader: int
        :param Replica: 副本集
        :type Replica: str
        :param InSyncReplica: ISR
        :type InSyncReplica: str
        :param BeginOffset: 起始Offset
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginOffset: int
        :param EndOffset: 末端Offset
注意：此字段可能返回 null，表示取不到有效值。
        :type EndOffset: int
        :param MessageCount: 消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageCount: int
        :param OutOfSyncReplica: 未同步副本集
注意：此字段可能返回 null，表示取不到有效值。
        :type OutOfSyncReplica: str
        """
        self.Partition = None
        self.Leader = None
        self.Replica = None
        self.InSyncReplica = None
        self.BeginOffset = None
        self.EndOffset = None
        self.MessageCount = None
        self.OutOfSyncReplica = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Leader = params.get("Leader")
        self.Replica = params.get("Replica")
        self.InSyncReplica = params.get("InSyncReplica")
        self.BeginOffset = params.get("BeginOffset")
        self.EndOffset = params.get("EndOffset")
        self.MessageCount = params.get("MessageCount")
        self.OutOfSyncReplica = params.get("OutOfSyncReplica")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaResult(AbstractModel):
    """Topic 副本及详情数据集合

    """

    def __init__(self):
        r"""
        :param TopicInSyncReplicaList: Topic详情及副本合集
        :type TopicInSyncReplicaList: list of TopicInSyncReplicaInfo
        :param TotalCount: 总计个数
        :type TotalCount: int
        """
        self.TopicInSyncReplicaList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicInSyncReplicaList") is not None:
            self.TopicInSyncReplicaList = []
            for item in params.get("TopicInSyncReplicaList"):
                obj = TopicInSyncReplicaInfo()
                obj._deserialize(item)
                self.TopicInSyncReplicaList.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicPartitionDO(AbstractModel):
    """分区详情

    """

    def __init__(self):
        r"""
        :param Partition: Partition ID
        :type Partition: int
        :param LeaderStatus: Leader 运行状态
        :type LeaderStatus: int
        :param IsrNum: ISR 个数
        :type IsrNum: int
        :param ReplicaNum: 副本个数
        :type ReplicaNum: int
        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicResult(AbstractModel):
    """统一返回的TopicResponse

    """

    def __init__(self):
        r"""
        :param TopicList: 返回的主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of Topic
        :param TotalCount: 符合条件的 topic 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Topic消息保留时间配置返回信息

    """

    def __init__(self):
        r"""
        :param Expect: 期望值，即用户配置的Topic消息保留时间(单位分钟)
注意：此字段可能返回 null，表示取不到有效值。
        :type Expect: int
        :param Current: 当前值，即当前生效值(可能存在动态调整，单位分钟)
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        :param ModTimeStamp: 最近变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTimeStamp: int
        """
        self.Expect = None
        self.Current = None
        self.ModTimeStamp = None


    def _deserialize(self, params):
        self.Expect = params.get("Expect")
        self.Current = params.get("Current")
        self.ModTimeStamp = params.get("ModTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSubscribeGroup(AbstractModel):
    """DescribeTopicSubscribeGroup接口出参

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param StatusCountInfo: 消费分组状态数量信息
        :type StatusCountInfo: str
        :param GroupsInfo: 消费分组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupsInfo: list of GroupInfoResponse
        :param Status: 此次请求是否异步的状态。实例里分组较少的会直接返回结果,Status为1。当分组较多时,会异步更新缓存，Status为0时不会返回分组信息，直至Status为1更新完毕返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.TotalCount = None
        self.StatusCountInfo = None
        self.GroupsInfo = None
        self.Status = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.StatusCountInfo = params.get("StatusCountInfo")
        if params.get("GroupsInfo") is not None:
            self.GroupsInfo = []
            for item in params.get("GroupsInfo"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self.GroupsInfo.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户实体

    """

    def __init__(self):
        r"""
        :param UserId: 用户id
        :type UserId: int
        :param Name: 用户名称
        :type Name: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最后更新时间
        :type UpdateTime: str
        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResponse(AbstractModel):
    """用户返回实体

    """

    def __init__(self):
        r"""
        :param Users: 符合条件的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of User
        :param TotalCount: 符合条件的总用户数
        :type TotalCount: int
        """
        self.Users = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipEntity(AbstractModel):
    """虚拟IP实体

    """

    def __init__(self):
        r"""
        :param Vip: 虚拟IP
        :type Vip: str
        :param Vport: 虚拟端口
        :type Vport: str
        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """zone信息实体

    """

    def __init__(self):
        r"""
        :param ZoneId: zone的id
        :type ZoneId: str
        :param IsInternalApp: 是否内部APP
        :type IsInternalApp: int
        :param AppId: app id
        :type AppId: int
        :param Flag: 标识
        :type Flag: bool
        :param ZoneName: zone名称
        :type ZoneName: str
        :param ZoneStatus: zone状态
        :type ZoneStatus: int
        :param Exflag: 额外标识
        :type Exflag: str
        :param SoldOut: json对象，key为机型，value true为售罄，false为未售罄
        :type SoldOut: str
        :param SalesInfo: 标准版售罄信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SalesInfo: list of SaleInfo
        """
        self.ZoneId = None
        self.IsInternalApp = None
        self.AppId = None
        self.Flag = None
        self.ZoneName = None
        self.ZoneStatus = None
        self.Exflag = None
        self.SoldOut = None
        self.SalesInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.IsInternalApp = params.get("IsInternalApp")
        self.AppId = params.get("AppId")
        self.Flag = params.get("Flag")
        self.ZoneName = params.get("ZoneName")
        self.ZoneStatus = params.get("ZoneStatus")
        self.Exflag = params.get("Exflag")
        self.SoldOut = params.get("SoldOut")
        if params.get("SalesInfo") is not None:
            self.SalesInfo = []
            for item in params.get("SalesInfo"):
                obj = SaleInfo()
                obj._deserialize(item)
                self.SalesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    """查询kafka的zone信息返回的实体

    """

    def __init__(self):
        r"""
        :param ZoneList: zone列表
        :type ZoneList: list of ZoneInfo
        :param MaxBuyInstanceNum: 最大购买实例个数
        :type MaxBuyInstanceNum: int
        :param MaxBandwidth: 最大购买带宽 单位Mb/s
        :type MaxBandwidth: int
        :param UnitPrice: 后付费单位价格
        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param MessagePrice: 后付费消息单价
        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param ClusterInfo: 用户独占集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterInfo: list of ClusterInfo
        :param Standard: 购买标准版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        :param StandardS2: 购买标准版S2配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardS2: str
        :param Profession: 购买专业版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param Physical: 购买物理独占版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Physical: str
        :param PublicNetwork: 公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: str
        :param PublicNetworkLimit: 公网带宽配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkLimit: str
        """
        self.ZoneList = None
        self.MaxBuyInstanceNum = None
        self.MaxBandwidth = None
        self.UnitPrice = None
        self.MessagePrice = None
        self.ClusterInfo = None
        self.Standard = None
        self.StandardS2 = None
        self.Profession = None
        self.Physical = None
        self.PublicNetwork = None
        self.PublicNetworkLimit = None


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        self.MaxBuyInstanceNum = params.get("MaxBuyInstanceNum")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("UnitPrice") is not None:
            self.UnitPrice = Price()
            self.UnitPrice._deserialize(params.get("UnitPrice"))
        if params.get("MessagePrice") is not None:
            self.MessagePrice = Price()
            self.MessagePrice._deserialize(params.get("MessagePrice"))
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = []
            for item in params.get("ClusterInfo"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.ClusterInfo.append(obj)
        self.Standard = params.get("Standard")
        self.StandardS2 = params.get("StandardS2")
        self.Profession = params.get("Profession")
        self.Physical = params.get("Physical")
        self.PublicNetwork = params.get("PublicNetwork")
        self.PublicNetworkLimit = params.get("PublicNetworkLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        