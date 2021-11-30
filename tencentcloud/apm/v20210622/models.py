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