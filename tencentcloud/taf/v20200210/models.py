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


class ManagePortraitRiskInput(AbstractModel):
    r"""业务入参

    """

    def __init__(self):
        r"""
        :param _PostTime: 请求时间戳秒
        :type PostTime: int
        :param _UserIp: 用户公网ip（仅支持IPv4）
        :type UserIp: str
        :param _Channel: 渠道号
        :type Channel: int
        """
        self._PostTime = None
        self._UserIp = None
        self._Channel = None

    @property
    def PostTime(self):
        r"""请求时间戳秒
        :rtype: int
        """
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

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
        self._PostTime = params.get("PostTime")
        self._UserIp = params.get("UserIp")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskOutput(AbstractModel):
    r"""业务出参

    """

    def __init__(self):
        r"""
        :param _Code: 返回码（0，成功，其他失败）
        :type Code: int
        :param _Message: 返回码对应的信息
        :type Message: str
        :param _Value: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskValueOutput`
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        r"""返回码（0，成功，其他失败）
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""返回码对应的信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        r"""结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskValueOutput`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = ManagePortraitRiskValueOutput()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskRequest(AbstractModel):
    r"""ManagePortraitRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskInput`
        """
        self._BusinessSecurityData = None

    @property
    def BusinessSecurityData(self):
        r"""业务入参
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskInput`
        """
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = ManagePortraitRiskInput()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagePortraitRiskResponse(AbstractModel):
    r"""ManagePortraitRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskOutput`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.taf.v20200210.models.ManagePortraitRiskOutput`
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
            self._Data = ManagePortraitRiskOutput()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ManagePortraitRiskValueOutput(AbstractModel):
    r"""业务出参

    """

    def __init__(self):
        r"""
        :param _UserIp: 对应的IP
        :type UserIp: str
        :param _Level: 返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :type Level: int
        """
        self._UserIp = None
        self._Level = None

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
    def Level(self):
        r"""返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        