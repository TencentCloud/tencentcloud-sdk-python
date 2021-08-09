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
        """
        :param PostTime: 操作时间戳，单位秒\n        :type PostTime: int\n        :param Uid: 用户ID 
accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId\n        :type Uid: str\n        :param UserIp: 操作来源的外网IP\n        :type UserIp: str\n        :param ValueScore: 0~100：营销价值评分，分值越高，价值越大
[0,50]低价值
[50,70]价值一般
[70,100]高价值\n        :type ValueScore: int\n        """
        self.PostTime = None
        self.Uid = None
        self.UserIp = None
        self.ValueScore = None


    def _deserialize(self, params):
        self.PostTime = params.get("PostTime")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.ValueScore = params.get("ValueScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingValueJudgementRequest(AbstractModel):
    """MarketingValueJudgement请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 手机账号类型填写4\n        :type AccountType: int\n        :param Uid: 填写手机号码，如15317537488\n        :type Uid: str\n        :param UserIp: 用户请求时的客户端外网IP\n        :type UserIp: str\n        :param PostTime: 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）\n        :type PostTime: int\n        :param Imei: 用户设备号imei/idfa(建议填写)\n        :type Imei: str\n        :param Referer: 活动链接(建议填写)\n        :type Referer: str\n        """
        self.AccountType = None
        self.Uid = None
        self.UserIp = None
        self.PostTime = None
        self.Imei = None
        self.Referer = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.Imei = params.get("Imei")
        self.Referer = params.get("Referer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingValueJudgementResponse(AbstractModel):
    """MarketingValueJudgement返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回数据\n        :type Data: :class:`tencentcloud.mvj.v20190926.models.Data`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Data()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")