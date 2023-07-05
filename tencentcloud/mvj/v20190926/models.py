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


class Data(AbstractModel):
    """返回结构

    """

    def __init__(self):
        r"""
        :param _PostTime: 操作时间戳，单位秒
        :type PostTime: int
        :param _Uid: 用户ID 
accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
        :type Uid: str
        :param _UserIp: 操作来源的外网IP
        :type UserIp: str
        :param _ValueScore: 0~100：营销价值评分，分值越高，价值越大
[0,50]低价值
[50,70]价值一般
[70,100]高价值
        :type ValueScore: int
        """
        self._PostTime = None
        self._Uid = None
        self._UserIp = None
        self._ValueScore = None

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def ValueScore(self):
        return self._ValueScore

    @ValueScore.setter
    def ValueScore(self, ValueScore):
        self._ValueScore = ValueScore


    def _deserialize(self, params):
        self._PostTime = params.get("PostTime")
        self._Uid = params.get("Uid")
        self._UserIp = params.get("UserIp")
        self._ValueScore = params.get("ValueScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingValueJudgementRequest(AbstractModel):
    """MarketingValueJudgement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 手机账号类型填写4
        :type AccountType: int
        :param _Uid: 填写手机号码，如15317537488
        :type Uid: str
        :param _UserIp: 用户请求时的客户端外网IP
        :type UserIp: str
        :param _PostTime: 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）
        :type PostTime: int
        :param _Imei: 用户设备号imei/idfa(建议填写)
        :type Imei: str
        :param _Referer: 活动链接(建议填写)
        :type Referer: str
        """
        self._AccountType = None
        self._Uid = None
        self._UserIp = None
        self._PostTime = None
        self._Imei = None
        self._Referer = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Uid = params.get("Uid")
        self._UserIp = params.get("UserIp")
        self._PostTime = params.get("PostTime")
        self._Imei = params.get("Imei")
        self._Referer = params.get("Referer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingValueJudgementResponse(AbstractModel):
    """MarketingValueJudgement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.mvj.v20190926.models.Data`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = Data()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")