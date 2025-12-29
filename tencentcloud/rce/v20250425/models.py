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


class ManageIPPortraitRiskInput(AbstractModel):
    r"""业务入参

    """

    def __init__(self):
        r"""
        :param _UserIp: 用户公网ip（仅支持IPv4）
        :type UserIp: str
        :param _Channel: 渠道号
        :type Channel: int
        """
        self._UserIp = None
        self._Channel = None

    @property
    def UserIp(self):
        r"""用户公网ip（仅支持IPv4）
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Channel(self):
        r"""渠道号
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskOutput(AbstractModel):
    r"""IP画像出参

    """

    def __init__(self):
        r"""
        :param _Code: 返回码
        :type Code: int
        :param _Message: 返回消息
        :type Message: str
        :param _Value: 结果
        :type Value: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskValueOutput`
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        r"""返回码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""返回消息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        r"""结果
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskValueOutput`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = ManageIPPortraitRiskValueOutput()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskRequest(AbstractModel):
    r"""ManageIPPortraitRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PostTime: 请求秒级时间戳
        :type PostTime: int
        :param _BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskInput`
        """
        self._PostTime = None
        self._BusinessSecurityData = None

    @property
    def PostTime(self):
        r"""请求秒级时间戳
        :rtype: int
        """
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def BusinessSecurityData(self):
        r"""业务入参
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskInput`
        """
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        self._PostTime = params.get("PostTime")
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = ManageIPPortraitRiskInput()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskResponse(AbstractModel):
    r"""ManageIPPortraitRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 出参
        :type Data: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskOutput`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""出参
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskOutput`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ManageIPPortraitRiskOutput()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ManageIPPortraitRiskValueOutput(AbstractModel):
    r"""业务出参

    """

    def __init__(self):
        r"""
        :param _UserIp: 对应的IP
        :type UserIp: str
        :param _RiskScore: 返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :type RiskScore: int
        :param _RiskType: 风险类型
        :type RiskType: list of int
        """
        self._UserIp = None
        self._RiskScore = None
        self._RiskType = None

    @property
    def UserIp(self):
        r"""对应的IP
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def RiskScore(self):
        r"""返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :rtype: int
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskType(self):
        r"""风险类型
        :rtype: list of int
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._RiskScore = params.get("RiskScore")
        self._RiskType = params.get("RiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        