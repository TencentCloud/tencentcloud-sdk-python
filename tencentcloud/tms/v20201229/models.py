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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DetailResults(AbstractModel):
    """文本返回的详细结果

    """

    def __init__(self):
        """
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Keywords: 该标签下命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param Score: 该标签模型命中的分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param LibType: 仅当Label为Custom自定义关键词时有效，表示自定义关键词库类型，1:黑白库，2：自定义库
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param LibId: 仅当Label为Custom自定义关键词时有效，表示自定义库id
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 仅当Labe为Custom自定义关键词时有效，表示自定义库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        """
        self.Label = None
        self.Suggestion = None
        self.Keywords = None
        self.Score = None
        self.LibType = None
        self.LibId = None
        self.LibName = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        self.LibType = params.get("LibType")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Device(AbstractModel):
    """设备信息

    """

    def __init__(self):
        """
        :param IP: 用户IP
        :type IP: str
        :param Mac: Mac地址
        :type Mac: str
        :param TokenId: 设备指纹Token
        :type TokenId: str
        :param DeviceId: 设备指纹ID
        :type DeviceId: str
        :param IMEI: 设备序列号
        :type IMEI: str
        :param IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
        :type IDFV: str
        """
        self.IP = None
        self.Mac = None
        self.TokenId = None
        self.DeviceId = None
        self.IMEI = None
        self.IDFA = None
        self.IDFV = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Mac = params.get("Mac")
        self.TokenId = params.get("TokenId")
        self.DeviceId = params.get("DeviceId")
        self.IMEI = params.get("IMEI")
        self.IDFA = params.get("IDFA")
        self.IDFV = params.get("IDFV")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RiskDetails(AbstractModel):
    """账号风险检测结果

    """

    def __init__(self):
        """
        :param Label: 风险类别，RiskAccount，RiskIP, RiskIMEI
        :type Label: str
        :param Level: 风险等级，1:疑似，2：恶意
        :type Level: int
        """
        self.Label = None
        self.Level = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。
        :type Content: str
        :param BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略。 -- 该字段暂未开放。
        :type BizType: str
        :param DataId: 数据ID，英文字母、下划线、-组成，不超过64个字符
        :type DataId: str
        :param User: 账号相关信息字段，填入后可识别违规风险账号。
        :type User: :class:`tencentcloud.tms.v20201229.models.User`
        :param Device: 设备相关信息字段，填入后可识别违规风险设备。
        :type Device: :class:`tencentcloud.tms.v20201229.models.Device`
        """
        self.Content = None
        self.BizType = None
        self.DataId = None
        self.User = None
        self.Device = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        """
        :param BizType: 您在入参时所填入的Biztype参数。 -- 该字段暂未开放。
        :type BizType: str
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param Keywords: 文本命中的关键词信息，用于提示您文本违规的具体原因，可能会返回多个命中的关键词。（如：加我微信）
如返回值为空，Score不为空，即识别结果（Label）是来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param Score: 机器判断当前分类的置信度，取值范围：0.00~100.00。分数越高，表示越有可能属于当前分类。
（如：色情 99.99，则该样本属于色情的置信度非常高。）
        :type Score: int
        :param DetailResults: 接口识别样本后返回的详细结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailResults: list of DetailResults
        :param RiskDetails: 接口识别样本中存在违规账号风险的检测结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDetails: list of RiskDetails
        :param Extra: 扩展字段，用于特定信息返回，不同客户/Biztype下返回信息不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param DataId: 请求参数中的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BizType = None
        self.Label = None
        self.Suggestion = None
        self.Keywords = None
        self.Score = None
        self.DetailResults = None
        self.RiskDetails = None
        self.Extra = None
        self.DataId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        if params.get("DetailResults") is not None:
            self.DetailResults = []
            for item in params.get("DetailResults"):
                obj = DetailResults()
                obj._deserialize(item)
                self.DetailResults.append(obj)
        if params.get("RiskDetails") is not None:
            self.RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self.RiskDetails.append(obj)
        self.Extra = params.get("Extra")
        self.DataId = params.get("DataId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class User(AbstractModel):
    """用户相关信息

    """

    def __init__(self):
        """
        :param UserId: 用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param Nickname: 用户昵称
        :type Nickname: str
        :param AccountType: 账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: int
        :param Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param Age: 年龄 默认0 未知
        :type Age: int
        :param Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param Phone: 手机号
        :type Phone: str
        """
        self.UserId = None
        self.Nickname = None
        self.AccountType = None
        self.Gender = None
        self.Age = None
        self.Level = None
        self.Phone = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Nickname = params.get("Nickname")
        self.AccountType = params.get("AccountType")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Level = params.get("Level")
        self.Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        