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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AgentShell(AbstractModel):
    r"""agent安装脚本串

    """

    def __init__(self):
        r"""
        :param _Token: 鉴权token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _EtlIp: 数据接收Ip
注意：此字段可能返回 null，表示取不到有效值。
        :type EtlIp: str
        :param _EtlPort: 数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :type EtlPort: str
        :param _ByHandAccess: 手动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。
        :type ByHandAccess: str
        :param _ByShellAccess: 自动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。
        :type ByShellAccess: str
        :param _SkyWalkingPort: SkyWalking数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :type SkyWalkingPort: str
        :param _ZipkinPort: Zipkin数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :type ZipkinPort: str
        :param _JaegerPort: Jaeger数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :type JaegerPort: str
        """
        self._Token = None
        self._EtlIp = None
        self._EtlPort = None
        self._ByHandAccess = None
        self._ByShellAccess = None
        self._SkyWalkingPort = None
        self._ZipkinPort = None
        self._JaegerPort = None

    @property
    def Token(self):
        r"""鉴权token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def EtlIp(self):
        r"""数据接收Ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EtlIp

    @EtlIp.setter
    def EtlIp(self, EtlIp):
        self._EtlIp = EtlIp

    @property
    def EtlPort(self):
        r"""数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EtlPort

    @EtlPort.setter
    def EtlPort(self, EtlPort):
        self._EtlPort = EtlPort

    @property
    def ByHandAccess(self):
        r"""手动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ByHandAccess

    @ByHandAccess.setter
    def ByHandAccess(self, ByHandAccess):
        self._ByHandAccess = ByHandAccess

    @property
    def ByShellAccess(self):
        r"""自动接入脚本串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ByShellAccess

    @ByShellAccess.setter
    def ByShellAccess(self, ByShellAccess):
        self._ByShellAccess = ByShellAccess

    @property
    def SkyWalkingPort(self):
        r"""SkyWalking数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkyWalkingPort

    @SkyWalkingPort.setter
    def SkyWalkingPort(self, SkyWalkingPort):
        self._SkyWalkingPort = SkyWalkingPort

    @property
    def ZipkinPort(self):
        r"""Zipkin数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZipkinPort

    @ZipkinPort.setter
    def ZipkinPort(self, ZipkinPort):
        self._ZipkinPort = ZipkinPort

    @property
    def JaegerPort(self):
        r"""Jaeger数据接收port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JaegerPort

    @JaegerPort.setter
    def JaegerPort(self, JaegerPort):
        self._JaegerPort = JaegerPort


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._EtlIp = params.get("EtlIp")
        self._EtlPort = params.get("EtlPort")
        self._ByHandAccess = params.get("ByHandAccess")
        self._ByShellAccess = params.get("ByShellAccess")
        self._SkyWalkingPort = params.get("SkyWalkingPort")
        self._ZipkinPort = params.get("ZipkinPort")
        self._JaegerPort = params.get("JaegerPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentShellRequest(AbstractModel):
    r"""DescribeAgentShell请求参数结构体

    """


class DescribeAgentShellResponse(AbstractModel):
    r"""DescribeAgentShell返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 接入信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsw.v20200924.models.AgentShell`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""接入信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tsw.v20200924.models.AgentShell`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AgentShell()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")