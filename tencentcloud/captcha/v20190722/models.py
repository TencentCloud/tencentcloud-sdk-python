# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class DescribeCaptchaResultRequest(AbstractModel):
    """DescribeCaptchaResult请求参数结构体

    """

    def __init__(self):
        """
        :param CaptchaType: 验证码类型，9：滑块验证码
        :type CaptchaType: int
        :param Ticket: 验证码返回给用户的票据
        :type Ticket: str
        :param UserIp: 用户操作来源的外网 IP
        :type UserIp: str
        :param Randstr: 验证票据需要的随机字符串
        :type Randstr: str
        :param CaptchaAppId: 验证码应用ID
        :type CaptchaAppId: int
        :param AppSecretKey: 用于服务器端校验验证码票据的验证密钥，请妥善保密，请勿泄露给第三方
        :type AppSecretKey: str
        :param BusinessId: 业务 ID，网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据
        :type BusinessId: int
        :param SceneId: 场景 ID，网站或应用的业务下有多个场景使用此服务，通过此 ID 区分统计数据
        :type SceneId: int
        :param MacAddress: mac 地址或设备唯一标识
        :type MacAddress: str
        :param Imei: 手机设备号
        :type Imei: str
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.Randstr = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.Randstr = params.get("Randstr")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult返回参数结构体

    """

    def __init__(self):
        """
        :param CaptchaCode: 1:验证成功，0:验证失败，100:AppSecretKey参数校验错误
        :type CaptchaCode: int
        :param CaptchaMsg: 状态描述及验证错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param EvilLevel: [0,100]，恶意等级
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLevel: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.EvilLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.EvilLevel = params.get("EvilLevel")
        self.RequestId = params.get("RequestId")