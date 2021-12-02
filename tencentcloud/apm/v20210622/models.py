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


class ApmAgentInfo(AbstractModel):
    """apm Agent信息

    """

    def __init__(self):
        r"""
        :param AgentDownloadURL: Agent下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentDownloadURL: str
        :param CollectorURL: Collector上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorURL: str
        :param Token: Token信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param PublicCollectorURL: 外网上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicCollectorURL: str
        :param InnerCollectorURL: 自研VPC上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerCollectorURL: str
        :param PrivateLinkCollectorURL: 内网上报地址(Private Link上报地址)
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateLinkCollectorURL: str
        """
        self.AgentDownloadURL = None
        self.CollectorURL = None
        self.Token = None
        self.PublicCollectorURL = None
        self.InnerCollectorURL = None
        self.PrivateLinkCollectorURL = None


    def _deserialize(self, params):
        self.AgentDownloadURL = params.get("AgentDownloadURL")
        self.CollectorURL = params.get("CollectorURL")
        self.Token = params.get("Token")
        self.PublicCollectorURL = params.get("PublicCollectorURL")
        self.InnerCollectorURL = params.get("InnerCollectorURL")
        self.PrivateLinkCollectorURL = params.get("PrivateLinkCollectorURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmInstanceDetail(AbstractModel):
    """apm实例信息

    """

    def __init__(self):
        r"""
        :param AmountOfUsedStorage: 存储使用量(MB)
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountOfUsedStorage: float
        :param Name: 实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Tags: 实例所属tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param CreateUin: 创建人Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param ServiceCount: 该实例已上报的服务数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param CountOfReportSpanPerDay: 日均上报Span数
注意：此字段可能返回 null，表示取不到有效值。
        :type CountOfReportSpanPerDay: int
        :param AppId: AppId信息
        :type AppId: int
        :param TraceDuration: Trace数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceDuration: int
        :param Description: 实例描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Region: 实例所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SpanDailyCounters: 实例上报额度
注意：此字段可能返回 null，表示取不到有效值。
        :type SpanDailyCounters: int
        :param BillingInstance: 实例是否开通计费
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInstance: int
        :param ErrRateThreshold: 错误率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrRateThreshold: int
        :param SampleRate: 采样率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: int
        :param ErrorSample: 是否开启错误采样 0  关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorSample: int
        :param SlowRequestSavedThreshold: 慢调用保存阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowRequestSavedThreshold: int
        """
        self.AmountOfUsedStorage = None
        self.Name = None
        self.Tags = None
        self.InstanceId = None
        self.CreateUin = None
        self.ServiceCount = None
        self.CountOfReportSpanPerDay = None
        self.AppId = None
        self.TraceDuration = None
        self.Description = None
        self.Status = None
        self.Region = None
        self.SpanDailyCounters = None
        self.BillingInstance = None
        self.ErrRateThreshold = None
        self.SampleRate = None
        self.ErrorSample = None
        self.SlowRequestSavedThreshold = None


    def _deserialize(self, params):
        self.AmountOfUsedStorage = params.get("AmountOfUsedStorage")
        self.Name = params.get("Name")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.CreateUin = params.get("CreateUin")
        self.ServiceCount = params.get("ServiceCount")
        self.CountOfReportSpanPerDay = params.get("CountOfReportSpanPerDay")
        self.AppId = params.get("AppId")
        self.TraceDuration = params.get("TraceDuration")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.SpanDailyCounters = params.get("SpanDailyCounters")
        self.BillingInstance = params.get("BillingInstance")
        self.ErrRateThreshold = params.get("ErrRateThreshold")
        self.SampleRate = params.get("SampleRate")
        self.ErrorSample = params.get("ErrorSample")
        self.SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmTag(AbstractModel):
    """维度（标签）对象

    """

    def __init__(self):
        r"""
        :param Key: 维度Key(列名，标签Key)
        :type Key: str
        :param Value: 维度值（标签值）
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmInstanceRequest(AbstractModel):
    """CreateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 实例名
        :type Name: str
        :param Description: 实例描述信息
        :type Description: str
        :param TraceDuration: Trace数据保存时长
        :type TraceDuration: int
        :param Tags: 标签列表
        :type Tags: list of ApmTag
        :param SpanDailyCounters: 实例上报额度值
        :type SpanDailyCounters: int
        """
        self.Name = None
        self.Description = None
        self.TraceDuration = None
        self.Tags = None
        self.SpanDailyCounters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.TraceDuration = params.get("TraceDuration")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SpanDailyCounters = params.get("SpanDailyCounters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmInstanceResponse(AbstractModel):
    """CreateApmInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeApmAgentRequest(AbstractModel):
    """DescribeApmAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AgentType: 接入方式
        :type AgentType: str
        :param NetworkMode: 环境
        :type NetworkMode: str
        :param LanguageEnvironment: 语言
        :type LanguageEnvironment: str
        """
        self.InstanceId = None
        self.AgentType = None
        self.NetworkMode = None
        self.LanguageEnvironment = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentType = params.get("AgentType")
        self.NetworkMode = params.get("NetworkMode")
        self.LanguageEnvironment = params.get("LanguageEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAgentResponse(AbstractModel):
    """DescribeApmAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApmAgent: Agent信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmAgent: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApmAgent = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApmAgent") is not None:
            self.ApmAgent = ApmAgentInfo()
            self.ApmAgent._deserialize(params.get("ApmAgent"))
        self.RequestId = params.get("RequestId")


class DescribeApmInstancesRequest(AbstractModel):
    """DescribeApmInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: Tag列表
        :type Tags: list of ApmTag
        :param InstanceName: 搜索实例名
        :type InstanceName: str
        :param InstanceIds: 过滤实例ID
        :type InstanceIds: list of str
        """
        self.Tags = None
        self.InstanceName = None
        self.InstanceIds = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceName = params.get("InstanceName")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmInstancesResponse(AbstractModel):
    """DescribeApmInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: apm实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of ApmInstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")