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


class AgentShell(AbstractModel):
    """agent安装脚本串

    """

    def __init__(self):
        """
        :param Token: 鉴权token
注意：此字段可能返回 null，表示取不到有效值。\n        :type Token: str\n        :param EtlIp: 数据接收Ip
注意：此字段可能返回 null，表示取不到有效值。\n        :type EtlIp: str\n        :param EtlPort: 数据接收port
注意：此字段可能返回 null，表示取不到有效值。\n        :type EtlPort: str\n        :param ByHandAccess: 手动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。\n        :type ByHandAccess: str\n        :param ByShellAccess: 自动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。\n        :type ByShellAccess: str\n        :param SkyWalkingPort: SkyWalking数据接收port
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkyWalkingPort: str\n        :param ZipkinPort: Zipkin数据接收port
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZipkinPort: str\n        :param JaegerPort: Jaeger数据接收port
注意：此字段可能返回 null，表示取不到有效值。\n        :type JaegerPort: str\n        """
        self.Token = None
        self.EtlIp = None
        self.EtlPort = None
        self.ByHandAccess = None
        self.ByShellAccess = None
        self.SkyWalkingPort = None
        self.ZipkinPort = None
        self.JaegerPort = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.EtlIp = params.get("EtlIp")
        self.EtlPort = params.get("EtlPort")
        self.ByHandAccess = params.get("ByHandAccess")
        self.ByShellAccess = params.get("ByShellAccess")
        self.SkyWalkingPort = params.get("SkyWalkingPort")
        self.ZipkinPort = params.get("ZipkinPort")
        self.JaegerPort = params.get("JaegerPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentShellRequest(AbstractModel):
    """DescribeAgentShell请求参数结构体

    """


class DescribeAgentShellResponse(AbstractModel):
    """DescribeAgentShell返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 接入信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsw.v20200924.models.AgentShell`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AgentShell()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")