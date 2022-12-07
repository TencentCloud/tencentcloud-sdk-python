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


class ChainData(AbstractModel):
    """上链数据

    """

    def __init__(self):
        r"""
        :param BlockHash: 区块hash
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockHash: str
        :param BlockHeight: 区块高度
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockHeight: str
        :param BlockTime: 区块时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockTime: str
        """
        self.BlockHash = None
        self.BlockHeight = None
        self.BlockTime = None


    def _deserialize(self, params):
        self.BlockHash = params.get("BlockHash")
        self.BlockHeight = params.get("BlockHeight")
        self.BlockTime = params.get("BlockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeBatch(AbstractModel):
    """批次

    """

    def __init__(self):
        r"""
        :param BatchId: 批次号
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param BatchCode: 批次编码(未使用)
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchCode: str
        :param CodeCnt: 码数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeCnt: int
        :param MerchantId: 所属商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param BatchType: 批次类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchType: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param MpTpl: 微信模板
注意：此字段可能返回 null，表示取不到有效值。
        :type MpTpl: str
        :param Status: 批次状态 0: 未激活 1: 已激活 -1: 已冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param MerchantName: 所属商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param Ext: 未使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        :param TplName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TplName: str
        :param Job: 调度任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.trp.v20210515.models.Job`
        """
        self.BatchId = None
        self.CorpId = None
        self.BatchCode = None
        self.CodeCnt = None
        self.MerchantId = None
        self.ProductId = None
        self.BatchType = None
        self.Remark = None
        self.MpTpl = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MerchantName = None
        self.ProductName = None
        self.Ext = None
        self.TplName = None
        self.Job = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.CorpId = params.get("CorpId")
        self.BatchCode = params.get("BatchCode")
        self.CodeCnt = params.get("CodeCnt")
        self.MerchantId = params.get("MerchantId")
        self.ProductId = params.get("ProductId")
        self.BatchType = params.get("BatchType")
        self.Remark = params.get("Remark")
        self.MpTpl = params.get("MpTpl")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MerchantName = params.get("MerchantName")
        self.ProductName = params.get("ProductName")
        if params.get("Ext") is not None:
            self.Ext = Ext()
            self.Ext._deserialize(params.get("Ext"))
        self.TplName = params.get("TplName")
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeItem(AbstractModel):
    """码类型

    """

    def __init__(self):
        r"""
        :param Code: 无
        :type Code: str
        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePack(AbstractModel):
    """码包类型

    """

    def __init__(self):
        r"""
        :param PackId: 码id
注意：此字段可能返回 null，表示取不到有效值。
        :type PackId: str
        :param CorpId: 企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param MerchantId: 商户id
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Status: 制码状态 init: 初始化, pending: 执行中, done: 完成, error: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Log: 执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param CreateUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUser: str
        :param Amount: 码数
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: int
        :param CodeLength: 码长度
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeLength: int
        :param CodeType: 码类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param Cipher: 是否暗码
注意：此字段可能返回 null，表示取不到有效值。
        :type Cipher: int
        :param TextUrl: [弃用] 文字码地址，通过另一个接口查
注意：此字段可能返回 null，表示取不到有效值。
        :type TextUrl: str
        :param PackUrl: [弃用] 二维码地址，通过另一个接口查
注意：此字段可能返回 null，表示取不到有效值。
        :type PackUrl: str
        :param MerchantName: 商户名
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param RuleType: 码规则类型 0: 默认, 1: 自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: int
        :param CustomId: 自定义码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param PackType: 码包类型 0: 普通码包 1: 层级码包
注意：此字段可能返回 null，表示取不到有效值。
        :type PackType: int
        :param PackLevel: 生码层级
注意：此字段可能返回 null，表示取不到有效值。
        :type PackLevel: int
        :param PackSpec: 层级码配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PackSpec: list of PackSpec
        """
        self.PackId = None
        self.CorpId = None
        self.MerchantId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.Log = None
        self.CreateUser = None
        self.Amount = None
        self.CodeLength = None
        self.CodeType = None
        self.Cipher = None
        self.TextUrl = None
        self.PackUrl = None
        self.MerchantName = None
        self.RuleType = None
        self.CustomId = None
        self.PackType = None
        self.PackLevel = None
        self.PackSpec = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.CorpId = params.get("CorpId")
        self.MerchantId = params.get("MerchantId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Log = params.get("Log")
        self.CreateUser = params.get("CreateUser")
        self.Amount = params.get("Amount")
        self.CodeLength = params.get("CodeLength")
        self.CodeType = params.get("CodeType")
        self.Cipher = params.get("Cipher")
        self.TextUrl = params.get("TextUrl")
        self.PackUrl = params.get("PackUrl")
        self.MerchantName = params.get("MerchantName")
        self.RuleType = params.get("RuleType")
        self.CustomId = params.get("CustomId")
        self.PackType = params.get("PackType")
        self.PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self.PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self.PackSpec.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePart(AbstractModel):
    """码段配置

    """

    def __init__(self):
        r"""
        :param Name: 码段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 码段类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Value: 码段内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Length: 码段长度
        :type Length: int
        :param Ext: 扩展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self.Name = None
        self.Type = None
        self.Value = None
        self.Length = None
        self.Ext = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Length = params.get("Length")
        self.Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorpQuota(AbstractModel):
    """渠道商的子企业额度使用情况

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param CorpName: 企业名称
        :type CorpName: str
        :param Quota: 额度
        :type Quota: :class:`tencentcloud.trp.v20210515.models.Quota`
        :param UsageQuota: 额度使用量
        :type UsageQuota: :class:`tencentcloud.trp.v20210515.models.UsageQuota`
        """
        self.CorpId = None
        self.CorpName = None
        self.Quota = None
        self.UsageQuota = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.CorpName = params.get("CorpName")
        if params.get("Quota") is not None:
            self.Quota = Quota()
            self.Quota._deserialize(params.get("Quota"))
        if params.get("UsageQuota") is not None:
            self.UsageQuota = UsageQuota()
            self.UsageQuota._deserialize(params.get("UsageQuota"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeBatchRequest(AbstractModel):
    """CreateCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param BatchType: 批次类型 0:溯源 1:营销
        :type BatchType: int
        :param BatchId: 批次ID，系统自动生成
        :type BatchId: str
        :param Remark: 备注
        :type Remark: str
        :param MpTpl: 模版ID，或者活动ID
        :type MpTpl: str
        :param CloneId: 克隆批次ID，同时会复制溯源信息
        :type CloneId: str
        """
        self.CorpId = None
        self.MerchantId = None
        self.ProductId = None
        self.BatchType = None
        self.BatchId = None
        self.Remark = None
        self.MpTpl = None
        self.CloneId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.MerchantId = params.get("MerchantId")
        self.ProductId = params.get("ProductId")
        self.BatchType = params.get("BatchType")
        self.BatchId = params.get("BatchId")
        self.Remark = params.get("Remark")
        self.MpTpl = params.get("MpTpl")
        self.CloneId = params.get("CloneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeBatchResponse(AbstractModel):
    """CreateCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class CreateCodePackRequest(AbstractModel):
    """CreateCodePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param CodeLength: 码长度
        :type CodeLength: int
        :param CodeType: 码类型 alphabet 字母, number 数字, mixin 混合
        :type CodeType: str
        :param Amount: 生码数量 普通码包时必填
        :type Amount: int
        :param CorpId: 企业ID
        :type CorpId: int
        :param PackType: 码包类型 0: 普通码包 1: 层级码包
        :type PackType: int
        :param PackLevel: 码包层级
        :type PackLevel: int
        :param PackSpec: 码包规格
        :type PackSpec: list of PackSpec
        :param BatchId: 批次ID，如果传了生码后会同时绑定批次，并激活码
        :type BatchId: str
        """
        self.MerchantId = None
        self.CodeLength = None
        self.CodeType = None
        self.Amount = None
        self.CorpId = None
        self.PackType = None
        self.PackLevel = None
        self.PackSpec = None
        self.BatchId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.CodeLength = params.get("CodeLength")
        self.CodeType = params.get("CodeType")
        self.Amount = params.get("Amount")
        self.CorpId = params.get("CorpId")
        self.PackType = params.get("PackType")
        self.PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self.PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self.PackSpec.append(obj)
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodePackResponse(AbstractModel):
    """CreateCodePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param PackId: 码包ID
        :type PackId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.RequestId = params.get("RequestId")


class CreateCorporationOrderRequest(AbstractModel):
    """CreateCorporationOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpName: 企业名称
        :type CorpName: str
        :param Owner: 所有者ID
        :type Owner: str
        :param CodeQuota: 溯源码额度
        :type CodeQuota: int
        :param ExpireTime: 额度过期时间
        :type ExpireTime: str
        :param Amount: 金额
        :type Amount: int
        :param CorpId: 企业ID
        :type CorpId: int
        :param ContactPerson: 联系人
        :type ContactPerson: str
        :param ContactNumber: 联系电话
        :type ContactNumber: str
        :param Remark: 备注
        :type Remark: str
        """
        self.CorpName = None
        self.Owner = None
        self.CodeQuota = None
        self.ExpireTime = None
        self.Amount = None
        self.CorpId = None
        self.ContactPerson = None
        self.ContactNumber = None
        self.Remark = None


    def _deserialize(self, params):
        self.CorpName = params.get("CorpName")
        self.Owner = params.get("Owner")
        self.CodeQuota = params.get("CodeQuota")
        self.ExpireTime = params.get("ExpireTime")
        self.Amount = params.get("Amount")
        self.CorpId = params.get("CorpId")
        self.ContactPerson = params.get("ContactPerson")
        self.ContactNumber = params.get("ContactNumber")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorporationOrderResponse(AbstractModel):
    """CreateCorporationOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CorpId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.RequestId = params.get("RequestId")


class CreateCustomPackRequest(AbstractModel):
    """CreateCustomPack请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param Amount: 生码数量, 普通码包时必填
        :type Amount: int
        :param CorpId: 企业ID
        :type CorpId: int
        :param PackType: 码包类型 0: 普通码包 1: 层级码包
        :type PackType: int
        :param PackLevel: 码包层级
        :type PackLevel: int
        :param PackSpec: 层级码包规则
        :type PackSpec: list of PackSpec
        :param CustomId: 码规则ID,  和CodeParts二选一必填
        :type CustomId: str
        :param CodeParts: 码段配置，和CustomId二选一必填
        :type CodeParts: list of CodePart
        :param BatchId: 批次ID，如果传了生码后会同时绑定批次，并激活码
        :type BatchId: str
        """
        self.MerchantId = None
        self.Amount = None
        self.CorpId = None
        self.PackType = None
        self.PackLevel = None
        self.PackSpec = None
        self.CustomId = None
        self.CodeParts = None
        self.BatchId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.Amount = params.get("Amount")
        self.CorpId = params.get("CorpId")
        self.PackType = params.get("PackType")
        self.PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self.PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self.PackSpec.append(obj)
        self.CustomId = params.get("CustomId")
        if params.get("CodeParts") is not None:
            self.CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self.CodeParts.append(obj)
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomPackResponse(AbstractModel):
    """CreateCustomPack返回参数结构体

    """

    def __init__(self):
        r"""
        :param PackId: 码包ID
        :type PackId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.RequestId = params.get("RequestId")


class CreateCustomRuleRequest(AbstractModel):
    """CreateCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 规则名称
        :type Name: str
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param CodeLength: 码长度
        :type CodeLength: int
        :param CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.Name = None
        self.MerchantId = None
        self.CodeLength = None
        self.CodeParts = None
        self.CorpId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MerchantId = params.get("MerchantId")
        self.CodeLength = params.get("CodeLength")
        if params.get("CodeParts") is not None:
            self.CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self.CodeParts.append(obj)
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomRuleResponse(AbstractModel):
    """CreateCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.RequestId = params.get("RequestId")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 商户名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param CodeType: 码包来源 0:自建, 1:第三发
        :type CodeType: int
        :param CodeUrl: 码包前缀地址 第三方码包时必填
        :type CodeUrl: str
        """
        self.Name = None
        self.Remark = None
        self.CorpId = None
        self.CodeType = None
        self.CodeUrl = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.CorpId = params.get("CorpId")
        self.CodeType = params.get("CodeType")
        self.CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 商品名称
        :type Name: str
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param Remark: 备注
        :type Remark: str
        :param MerchantName: 商户名称
        :type MerchantName: str
        :param Specification: 商品规格
        :type Specification: str
        :param Logo: 商品图片
        :type Logo: list of str
        :param CorpId: 企业ID
        :type CorpId: int
        :param Ext: 预留字段
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        """
        self.Name = None
        self.MerchantId = None
        self.Remark = None
        self.MerchantName = None
        self.Specification = None
        self.Logo = None
        self.CorpId = None
        self.Ext = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MerchantId = params.get("MerchantId")
        self.Remark = params.get("Remark")
        self.MerchantName = params.get("MerchantName")
        self.Specification = params.get("Specification")
        self.Logo = params.get("Logo")
        self.CorpId = params.get("CorpId")
        if params.get("Ext") is not None:
            self.Ext = Ext()
            self.Ext._deserialize(params.get("Ext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class CreateTraceChainRequest(AbstractModel):
    """CreateTraceChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param TraceId: 溯源ID
        :type TraceId: str
        """
        self.CorpId = None
        self.TraceId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceChainResponse(AbstractModel):
    """CreateTraceChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
        :type TraceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.RequestId = params.get("RequestId")


class CreateTraceCodesAsyncRequest(AbstractModel):
    """CreateTraceCodesAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        :param FileKey: 上传文件Key，仅支持 csv 或者 zip 类型
        :type FileKey: str
        """
        self.CorpId = None
        self.BatchId = None
        self.FileKey = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        self.FileKey = params.get("FileKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceCodesAsyncResponse(AbstractModel):
    """CreateTraceCodesAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class CreateTraceCodesRequest(AbstractModel):
    """CreateTraceCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param Codes: 码
        :type Codes: list of CodeItem
        """
        self.BatchId = None
        self.CorpId = None
        self.Codes = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.CorpId = params.get("CorpId")
        if params.get("Codes") is not None:
            self.Codes = []
            for item in params.get("Codes"):
                obj = CodeItem()
                obj._deserialize(item)
                self.Codes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceCodesResponse(AbstractModel):
    """CreateTraceCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param ActiveCnt: 导入成功码数量
        :type ActiveCnt: int
        :param CodeCnt: 批次码数量
        :type CodeCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.ActiveCnt = None
        self.CodeCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.ActiveCnt = params.get("ActiveCnt")
        self.CodeCnt = params.get("CodeCnt")
        self.RequestId = params.get("RequestId")


class CreateTraceDataRequest(AbstractModel):
    """CreateTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param Phase: 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
        :type Phase: int
        :param PhaseName: 溯源阶段名称
        :type PhaseName: str
        :param ChainStatus: [无效] 上链状态
        :type ChainStatus: int
        :param Type: [无效] 码类型 0: 批次, 1: 码, 2: 生产任务, 3: 物流信息
        :type Type: int
        :param TraceId: [无效] 溯源ID
        :type TraceId: str
        :param TraceItems: 溯源信息
        :type TraceItems: list of TraceItem
        :param Status: 溯源状态 0: 无效, 1: 有效
        :type Status: int
        :param PhaseData: 环节数据
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        """
        self.CorpId = None
        self.BatchId = None
        self.TaskId = None
        self.Phase = None
        self.PhaseName = None
        self.ChainStatus = None
        self.Type = None
        self.TraceId = None
        self.TraceItems = None
        self.Status = None
        self.PhaseData = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        self.Phase = params.get("Phase")
        self.PhaseName = params.get("PhaseName")
        self.ChainStatus = params.get("ChainStatus")
        self.Type = params.get("Type")
        self.TraceId = params.get("TraceId")
        if params.get("TraceItems") is not None:
            self.TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self.TraceItems.append(obj)
        self.Status = params.get("Status")
        if params.get("PhaseData") is not None:
            self.PhaseData = PhaseData()
            self.PhaseData._deserialize(params.get("PhaseData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceDataResponse(AbstractModel):
    """CreateTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
        :type TraceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.RequestId = params.get("RequestId")


class CustomRule(AbstractModel):
    """码规则

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
        :type CustomId: str
        :param Name: 码规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param MerchantId: 商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param CodeLength: 码ID长度
        :type CodeLength: int
        :param Status: 规则状态
        :type Status: int
        :param CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.CustomId = None
        self.Name = None
        self.CorpId = None
        self.MerchantId = None
        self.CodeLength = None
        self.Status = None
        self.CodeParts = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.Name = params.get("Name")
        self.CorpId = params.get("CorpId")
        self.MerchantId = params.get("MerchantId")
        self.CodeLength = params.get("CodeLength")
        self.Status = params.get("Status")
        if params.get("CodeParts") is not None:
            self.CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self.CodeParts.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeBatchRequest(AbstractModel):
    """DeleteCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        """
        self.CorpId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeBatchResponse(AbstractModel):
    """DeleteCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class DeleteMerchantRequest(AbstractModel):
    """DeleteMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
        :type MerchantId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.MerchantId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMerchantResponse(AbstractModel):
    """DeleteMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 商品ID
        :type ProductId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.ProductId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class DeleteTraceDataRequest(AbstractModel):
    """DeleteTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
        :type TraceId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.TraceId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTraceDataResponse(AbstractModel):
    """DeleteTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源id
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.RequestId = params.get("RequestId")


class DescribeCodeBatchByIdRequest(AbstractModel):
    """DescribeCodeBatchById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        """
        self.CorpId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeBatchByIdResponse(AbstractModel):
    """DescribeCodeBatchById返回参数结构体

    """

    def __init__(self):
        r"""
        :param CodeBatch: 批次
        :type CodeBatch: :class:`tencentcloud.trp.v20210515.models.CodeBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CodeBatch") is not None:
            self.CodeBatch = CodeBatch()
            self.CodeBatch._deserialize(params.get("CodeBatch"))
        self.RequestId = params.get("RequestId")


class DescribeCodeBatchsRequest(AbstractModel):
    """DescribeCodeBatchs请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 查询商户ID
        :type MerchantId: str
        :param ProductId: 查询商品ID
        :type ProductId: str
        :param Keyword: 查询关键字
        :type Keyword: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param BatchType: 批次类型 0:溯源 1:营销
        :type BatchType: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.MerchantId = None
        self.ProductId = None
        self.Keyword = None
        self.PageSize = None
        self.PageNumber = None
        self.BatchType = None
        self.CorpId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.ProductId = params.get("ProductId")
        self.Keyword = params.get("Keyword")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.BatchType = params.get("BatchType")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeBatchsResponse(AbstractModel):
    """DescribeCodeBatchs返回参数结构体

    """

    def __init__(self):
        r"""
        :param CodeBatchs: 批次列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeBatchs: list of CodeBatch
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeBatchs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CodeBatchs") is not None:
            self.CodeBatchs = []
            for item in params.get("CodeBatchs"):
                obj = CodeBatch()
                obj._deserialize(item)
                self.CodeBatchs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCodePackStatusRequest(AbstractModel):
    """DescribeCodePackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackId: 码包ID
        :type PackId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.PackId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePackStatusResponse(AbstractModel):
    """DescribeCodePackStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 码包状态 init: 初始化, pending: 执行中, done: 完成, error: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeCodePackUrlRequest(AbstractModel):
    """DescribeCodePackUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackId: 码包ID
        :type PackId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.PackId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePackUrlResponse(AbstractModel):
    """DescribeCodePackUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 文字码包地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param ImgUrl: 图片码包地址，可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ImgUrl: str
        :param FileKey: 文字码包Key，用于上传导入
注意：此字段可能返回 null，表示取不到有效值。
        :type FileKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.ImgUrl = None
        self.FileKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.ImgUrl = params.get("ImgUrl")
        self.FileKey = params.get("FileKey")
        self.RequestId = params.get("RequestId")


class DescribeCodePacksRequest(AbstractModel):
    """DescribeCodePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 每页数量
        :type PageSize: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param Keyword: 查询关键字
        :type Keyword: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.PageSize = None
        self.PageNumber = None
        self.Keyword = None
        self.CorpId = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.Keyword = params.get("Keyword")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePacksResponse(AbstractModel):
    """DescribeCodePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param CodePacks: 码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePacks: list of CodePack
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodePacks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CodePacks") is not None:
            self.CodePacks = []
            for item in params.get("CodePacks"):
                obj = CodePack()
                obj._deserialize(item)
                self.CodePacks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCodesByPackRequest(AbstractModel):
    """DescribeCodesByPack请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackId: 码包ID
        :type PackId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.PackId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.PackId = params.get("PackId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodesByPackResponse(AbstractModel):
    """DescribeCodesByPack返回参数结构体

    """

    def __init__(self):
        r"""
        :param Codes: 码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Codes: list of CodeItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Codes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Codes") is not None:
            self.Codes = []
            for item in params.get("Codes"):
                obj = CodeItem()
                obj._deserialize(item)
                self.Codes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCorpQuotasRequest(AbstractModel):
    """DescribeCorpQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 渠道商ID，不要传
        :type AgentId: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param PageSize: 每页数量
        :type PageSize: int
        :param Keyword: 搜索企业ID
        :type Keyword: str
        """
        self.AgentId = None
        self.PageNumber = None
        self.PageSize = None
        self.Keyword = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCorpQuotasResponse(AbstractModel):
    """DescribeCorpQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param CorpQuotas: 子企业额度使用情况
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpQuotas: list of CorpQuota
        :param Total: 记录总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CorpQuotas = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CorpQuotas") is not None:
            self.CorpQuotas = []
            for item in params.get("CorpQuotas"):
                obj = CorpQuota()
                obj._deserialize(item)
                self.CorpQuotas.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCustomRuleByIdRequest(AbstractModel):
    """DescribeCustomRuleById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
        :type CustomId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.CustomId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRuleByIdResponse(AbstractModel):
    """DescribeCustomRuleById返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomRule: 码规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRule: :class:`tencentcloud.trp.v20210515.models.CustomRule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomRule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomRule") is not None:
            self.CustomRule = CustomRule()
            self.CustomRule._deserialize(params.get("CustomRule"))
        self.RequestId = params.get("RequestId")


class DescribeCustomRulesRequest(AbstractModel):
    """DescribeCustomRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Keyword: 搜索关键字
        :type Keyword: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param CorpId: 企业ID
        :type CorpId: int
        :param Status: 码规则状态 0:未生效 1:已生效 -1:已失效
        :type Status: int
        :param MerchantId: 商户ID
        :type MerchantId: str
        """
        self.Keyword = None
        self.PageSize = None
        self.PageNumber = None
        self.CorpId = None
        self.Status = None
        self.MerchantId = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.CorpId = params.get("CorpId")
        self.Status = params.get("Status")
        self.MerchantId = params.get("MerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRulesResponse(AbstractModel):
    """DescribeCustomRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomRules: 码规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRules: list of CustomRule
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomRules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomRules") is not None:
            self.CustomRules = []
            for item in params.get("CustomRules"):
                obj = CustomRule()
                obj._deserialize(item)
                self.CustomRules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeJobFileUrlRequest(AbstractModel):
    """DescribeJobFileUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 调度ID
        :type JobId: int
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.JobId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobFileUrlResponse(AbstractModel):
    """DescribeJobFileUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 码包地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class DescribeMerchantByIdRequest(AbstractModel):
    """DescribeMerchantById请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
        :type MerchantId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.MerchantId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMerchantByIdResponse(AbstractModel):
    """DescribeMerchantById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Merchant: 商户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Merchant: :class:`tencentcloud.trp.v20210515.models.Merchant`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Merchant = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Merchant") is not None:
            self.Merchant = Merchant()
            self.Merchant._deserialize(params.get("Merchant"))
        self.RequestId = params.get("RequestId")


class DescribeMerchantsRequest(AbstractModel):
    """DescribeMerchants请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 搜索商户名称
        :type Name: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param CorpId: 企业ID
        :type CorpId: int
        :param CodeType: 码来源类型 0:自建, 1:第三方
        :type CodeType: int
        """
        self.Name = None
        self.PageSize = None
        self.PageNumber = None
        self.CorpId = None
        self.CodeType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.CorpId = params.get("CorpId")
        self.CodeType = params.get("CodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMerchantsResponse(AbstractModel):
    """DescribeMerchants返回参数结构体

    """

    def __init__(self):
        r"""
        :param Merchants: 商户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Merchants: list of Merchant
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Merchants = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Merchants") is not None:
            self.Merchants = []
            for item in params.get("Merchants"):
                obj = Merchant()
                obj._deserialize(item)
                self.Merchants.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProductByIdRequest(AbstractModel):
    """DescribeProductById请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 商品ID
        :type ProductId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.ProductId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductByIdResponse(AbstractModel):
    """DescribeProductById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: :class:`tencentcloud.trp.v20210515.models.Product`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 商品名称
        :type Name: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param MerchantId: 商品ID
        :type MerchantId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.Name = None
        self.PageSize = None
        self.PageNumber = None
        self.MerchantId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.MerchantId = params.get("MerchantId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 商品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Products: list of Product
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self.Products.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTmpTokenRequest(AbstractModel):
    """DescribeTmpToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.CorpId = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTmpTokenResponse(AbstractModel):
    """DescribeTmpToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Token: 临时token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class DescribeTraceCodeByIdRequest(AbstractModel):
    """DescribeTraceCodeById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param Code: 二维码
        :type Code: str
        """
        self.CorpId = None
        self.Code = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceCodeByIdResponse(AbstractModel):
    """DescribeTraceCodeById返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceCode: 无
        :type TraceCode: :class:`tencentcloud.trp.v20210515.models.TraceCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TraceCode") is not None:
            self.TraceCode = TraceCode()
            self.TraceCode._deserialize(params.get("TraceCode"))
        self.RequestId = params.get("RequestId")


class DescribeTraceCodesRequest(AbstractModel):
    """DescribeTraceCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Keyword: 搜索关键字 码标识，或者批次ID
        :type Keyword: str
        :param PageNumber: 条数
        :type PageNumber: int
        :param PageSize: 页码
        :type PageSize: int
        :param BatchId: 批次ID，弃用
        :type BatchId: str
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.Keyword = None
        self.PageNumber = None
        self.PageSize = None
        self.BatchId = None
        self.CorpId = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.BatchId = params.get("BatchId")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceCodesResponse(AbstractModel):
    """DescribeTraceCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceCodes: 标识列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceCodes: list of TraceCode
        :param TotalCount: 条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceCodes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TraceCodes") is not None:
            self.TraceCodes = []
            for item in params.get("TraceCodes"):
                obj = TraceCode()
                obj._deserialize(item)
                self.TraceCodes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTraceDataListRequest(AbstractModel):
    """DescribeTraceDataList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        :param TaskId: 任务ID 用于外部溯源
        :type TaskId: str
        :param PageNumber: 页数
        :type PageNumber: int
        :param Code: 二维码
        :type Code: str
        :param Phase: 溯源阶段 0:商品 1:通用 2:内部溯源 3:外部溯源
        :type Phase: int
        :param PageSize: 数量
        :type PageSize: int
        """
        self.CorpId = None
        self.BatchId = None
        self.TaskId = None
        self.PageNumber = None
        self.Code = None
        self.Phase = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        self.PageNumber = params.get("PageNumber")
        self.Code = params.get("Code")
        self.Phase = params.get("Phase")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceDataListResponse(AbstractModel):
    """DescribeTraceDataList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 数量
        :type TotalCount: int
        :param TraceDataList: 无
        :type TraceDataList: list of TraceData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TraceDataList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TraceDataList") is not None:
            self.TraceDataList = []
            for item in params.get("TraceDataList"):
                obj = TraceData()
                obj._deserialize(item)
                self.TraceDataList.append(obj)
        self.RequestId = params.get("RequestId")


class Ext(AbstractModel):
    """预留字段

    """


class Job(AbstractModel):
    """通用调度任务

    """

    def __init__(self):
        r"""
        :param JobId: 调度ID
        :type JobId: int
        :param Status: 执行状态 init:初始化, pending: 执行中, done: 执行成功, error: 执行失败
        :type Status: str
        """
        self.JobId = None
        self.Status = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Merchant(AbstractModel):
    """商户信息

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
        :type MerchantId: str
        :param CorpId: 企业id
        :type CorpId: int
        :param Name: 商户名称
        :type Name: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CodeRule: 商户码规则
        :type CodeRule: str
        :param CodeType: 码来源类型 0: 安心平台 1: 第三方码
        :type CodeType: int
        :param CodeUrl: 第三方码域名前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeUrl: str
        """
        self.MerchantId = None
        self.CorpId = None
        self.Name = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CodeRule = None
        self.CodeType = None
        self.CodeUrl = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.CorpId = params.get("CorpId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CodeRule = params.get("CodeRule")
        self.CodeType = params.get("CodeType")
        self.CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCodeBatchRequest(AbstractModel):
    """ModifyCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param Status: 状态 0: 未激活 1: 已激活 -1: 已冻结
        :type Status: int
        :param MpTpl: 模版ID，或者活动ID
        :type MpTpl: str
        :param MerchantId: 商户ID
        :type MerchantId: str
        :param ProductId: 商品ID
        :type ProductId: str
        :param Remark: 备注
        :type Remark: str
        """
        self.BatchId = None
        self.CorpId = None
        self.Status = None
        self.MpTpl = None
        self.MerchantId = None
        self.ProductId = None
        self.Remark = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.CorpId = params.get("CorpId")
        self.Status = params.get("Status")
        self.MpTpl = params.get("MpTpl")
        self.MerchantId = params.get("MerchantId")
        self.ProductId = params.get("ProductId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCodeBatchResponse(AbstractModel):
    """ModifyCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
        :type BatchId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class ModifyCustomRuleRequest(AbstractModel):
    """ModifyCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
        :type CustomId: str
        :param Name: 规则名称
        :type Name: str
        :param CodeLength: 码长度
        :type CodeLength: int
        :param CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.CustomId = None
        self.Name = None
        self.CodeLength = None
        self.CodeParts = None
        self.CorpId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.Name = params.get("Name")
        self.CodeLength = params.get("CodeLength")
        if params.get("CodeParts") is not None:
            self.CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self.CodeParts.append(obj)
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleResponse(AbstractModel):
    """ModifyCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.RequestId = params.get("RequestId")


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
        :type CustomId: str
        :param Status: 码规则状态 0:未生效 1:已生效 -1:已失效
        :type Status: int
        :param CorpId: 企业ID
        :type CorpId: int
        """
        self.CustomId = None
        self.Status = None
        self.CorpId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.Status = params.get("Status")
        self.CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleStatusResponse(AbstractModel):
    """ModifyCustomRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.RequestId = params.get("RequestId")


class ModifyMerchantRequest(AbstractModel):
    """ModifyMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 商户名称
        :type Name: str
        :param MerchantId: 商户标识码
        :type MerchantId: str
        :param Remark: 备注
        :type Remark: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param CodeType: 码包来源 0:自建, 1:第三码包，暂不支持修改
        :type CodeType: int
        :param CodeUrl: 码包前缀地址 第三方码包时必填
        :type CodeUrl: str
        """
        self.Name = None
        self.MerchantId = None
        self.Remark = None
        self.CorpId = None
        self.CodeType = None
        self.CodeUrl = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MerchantId = params.get("MerchantId")
        self.Remark = params.get("Remark")
        self.CorpId = params.get("CorpId")
        self.CodeType = params.get("CodeType")
        self.CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMerchantResponse(AbstractModel):
    """ModifyMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 商品名称
        :type Name: str
        :param ProductId: 商品ID
        :type ProductId: str
        :param Remark: 备注
        :type Remark: str
        :param Specification: 商品规格
        :type Specification: str
        :param Logo: 商品图片
        :type Logo: list of str
        :param CorpId: 企业ID
        :type CorpId: int
        :param Ext: 预留字段
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        """
        self.Name = None
        self.ProductId = None
        self.Remark = None
        self.Specification = None
        self.Logo = None
        self.CorpId = None
        self.Ext = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ProductId = params.get("ProductId")
        self.Remark = params.get("Remark")
        self.Specification = params.get("Specification")
        self.Logo = params.get("Logo")
        self.CorpId = params.get("CorpId")
        if params.get("Ext") is not None:
            self.Ext = Ext()
            self.Ext._deserialize(params.get("Ext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class ModifyTraceCodeRequest(AbstractModel):
    """ModifyTraceCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Code: 二维码
        :type Code: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param Status: 状态 0: 冻结 1: 激活
        :type Status: int
        """
        self.Code = None
        self.CorpId = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CorpId = params.get("CorpId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceCodeResponse(AbstractModel):
    """ModifyTraceCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTraceDataRanksRequest(AbstractModel):
    """ModifyTraceDataRanks请求参数结构体

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
        :type CorpId: int
        :param BatchId: 批次ID
        :type BatchId: str
        :param TaskId: 生产任务ID
        :type TaskId: str
        :param TraceIds: 溯源ID
        :type TraceIds: list of str
        """
        self.CorpId = None
        self.BatchId = None
        self.TaskId = None
        self.TraceIds = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        self.TraceIds = params.get("TraceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceDataRanksResponse(AbstractModel):
    """ModifyTraceDataRanks返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class ModifyTraceDataRequest(AbstractModel):
    """ModifyTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
        :type TraceId: str
        :param BatchId: 批次ID
        :type BatchId: str
        :param TaskId: 生产溯源任务ID
        :type TaskId: str
        :param TraceItems: 溯源信息
        :type TraceItems: list of TraceItem
        :param PhaseName: 溯源阶段名称
        :type PhaseName: str
        :param Type: [无效] 类型
        :type Type: int
        :param Code: [无效] 溯源码
        :type Code: str
        :param Rank: [无效] 排序
        :type Rank: int
        :param Phase: [无效] 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
        :type Phase: int
        :param TraceTime: [无效] 溯源时间
        :type TraceTime: str
        :param CreateTime: [无效] 创建时间
        :type CreateTime: str
        :param ChainStatus: [无效] 上链状态
        :type ChainStatus: int
        :param ChainTime: [无效] 上链时间
        :type ChainTime: str
        :param ChainData: [无效] 上链数据
        :type ChainData: :class:`tencentcloud.trp.v20210515.models.ChainData`
        :param CorpId: 企业ID
        :type CorpId: int
        :param Status: 溯源状态 0: 无效, 1: 有效
        :type Status: int
        :param PhaseData: 环节数据
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        """
        self.TraceId = None
        self.BatchId = None
        self.TaskId = None
        self.TraceItems = None
        self.PhaseName = None
        self.Type = None
        self.Code = None
        self.Rank = None
        self.Phase = None
        self.TraceTime = None
        self.CreateTime = None
        self.ChainStatus = None
        self.ChainTime = None
        self.ChainData = None
        self.CorpId = None
        self.Status = None
        self.PhaseData = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        if params.get("TraceItems") is not None:
            self.TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self.TraceItems.append(obj)
        self.PhaseName = params.get("PhaseName")
        self.Type = params.get("Type")
        self.Code = params.get("Code")
        self.Rank = params.get("Rank")
        self.Phase = params.get("Phase")
        self.TraceTime = params.get("TraceTime")
        self.CreateTime = params.get("CreateTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ChainTime = params.get("ChainTime")
        if params.get("ChainData") is not None:
            self.ChainData = ChainData()
            self.ChainData._deserialize(params.get("ChainData"))
        self.CorpId = params.get("CorpId")
        self.Status = params.get("Status")
        if params.get("PhaseData") is not None:
            self.PhaseData = PhaseData()
            self.PhaseData._deserialize(params.get("PhaseData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceDataResponse(AbstractModel):
    """ModifyTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
        :type TraceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.RequestId = params.get("RequestId")


class PackSpec(AbstractModel):
    """层级码配置

    """

    def __init__(self):
        r"""
        :param Level: 层级
        :type Level: int
        :param Rate: 比例
        :type Rate: int
        :param Amount: 数量
        :type Amount: int
        :param CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param CodeParts: 码段配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeParts: list of CodePart
        """
        self.Level = None
        self.Rate = None
        self.Amount = None
        self.CustomId = None
        self.CodeParts = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.Rate = params.get("Rate")
        self.Amount = params.get("Amount")
        self.CustomId = params.get("CustomId")
        if params.get("CodeParts") is not None:
            self.CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self.CodeParts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhaseData(AbstractModel):
    """环节数据

    """

    def __init__(self):
        r"""
        :param HeadEnabled: 启用头
        :type HeadEnabled: bool
        :param HeadTitle: 标题
        :type HeadTitle: str
        :param Key: 标识符
        :type Key: str
        :param AppId: 小程序AppId
        :type AppId: str
        :param AppPath: 小程序AppPath
        :type AppPath: str
        :param AppName: 小程序名称AppName
        :type AppName: str
        """
        self.HeadEnabled = None
        self.HeadTitle = None
        self.Key = None
        self.AppId = None
        self.AppPath = None
        self.AppName = None


    def _deserialize(self, params):
        self.HeadEnabled = params.get("HeadEnabled")
        self.HeadTitle = params.get("HeadTitle")
        self.Key = params.get("Key")
        self.AppId = params.get("AppId")
        self.AppPath = params.get("AppPath")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    """商品信息

    """

    def __init__(self):
        r"""
        :param ProductId: 商品id
        :type ProductId: str
        :param CorpId: 企业id
        :type CorpId: int
        :param MerchantId: 商户标识码
        :type MerchantId: str
        :param ProductCode: 商品编号
        :type ProductCode: str
        :param Name: 商品名称
        :type Name: str
        :param Specification: 商品规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Logo: 商品图片
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: list of str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        :param Ext: 预留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        :param MerchantName: 商户名称
        :type MerchantName: str
        """
        self.ProductId = None
        self.CorpId = None
        self.MerchantId = None
        self.ProductCode = None
        self.Name = None
        self.Specification = None
        self.Remark = None
        self.Logo = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Ext = None
        self.MerchantName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.CorpId = params.get("CorpId")
        self.MerchantId = params.get("MerchantId")
        self.ProductCode = params.get("ProductCode")
        self.Name = params.get("Name")
        self.Specification = params.get("Specification")
        self.Remark = params.get("Remark")
        self.Logo = params.get("Logo")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Ext") is not None:
            self.Ext = Ext()
            self.Ext._deserialize(params.get("Ext"))
        self.MerchantName = params.get("MerchantName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """企业配额信息

    """

    def __init__(self):
        r"""
        :param StartTime: 服务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 服务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param QuotaId: 配额ID
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaId: int
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param Services: 开通服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of str
        :param FactoryQuota: 工厂配额
注意：此字段可能返回 null，表示取不到有效值。
        :type FactoryQuota: int
        :param ItemQuota: 产品配额
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemQuota: int
        :param TrackQuota: 溯源码配额
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackQuota: int
        :param SaleQuota: 销售码配额
注意：此字段可能返回 null，表示取不到有效值。
        :type SaleQuota: int
        :param ChainQuota: 上链配额
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainQuota: int
        :param RiskQuota: 风控配额
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskQuota: int
        :param TrackType: 溯源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackType: int
        :param Version: 开通版本 basic standard enterprise
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QuotaId = None
        self.CorpId = None
        self.Services = None
        self.FactoryQuota = None
        self.ItemQuota = None
        self.TrackQuota = None
        self.SaleQuota = None
        self.ChainQuota = None
        self.RiskQuota = None
        self.TrackType = None
        self.Version = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QuotaId = params.get("QuotaId")
        self.CorpId = params.get("CorpId")
        self.Services = params.get("Services")
        self.FactoryQuota = params.get("FactoryQuota")
        self.ItemQuota = params.get("ItemQuota")
        self.TrackQuota = params.get("TrackQuota")
        self.SaleQuota = params.get("SaleQuota")
        self.ChainQuota = params.get("ChainQuota")
        self.RiskQuota = params.get("RiskQuota")
        self.TrackType = params.get("TrackType")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceCode(AbstractModel):
    """溯源码

    """

    def __init__(self):
        r"""
        :param Code: 二维码
        :type Code: str
        :param CorpId: 企业ID
        :type CorpId: int
        :param PackId: 码包ID
        :type PackId: str
        :param BatchId: 批次ID
        :type BatchId: str
        :param MerchantId: 所属商户ID
        :type MerchantId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param Status: 码状态 0: 冻结 1: 激活
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        :param MerchantName: 商户名称
        :type MerchantName: str
        :param ProductName: 产品名称
        :type ProductName: str
        """
        self.Code = None
        self.CorpId = None
        self.PackId = None
        self.BatchId = None
        self.MerchantId = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MerchantName = None
        self.ProductName = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CorpId = params.get("CorpId")
        self.PackId = params.get("PackId")
        self.BatchId = params.get("BatchId")
        self.MerchantId = params.get("MerchantId")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MerchantName = params.get("MerchantName")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceData(AbstractModel):
    """溯源数据

    """

    def __init__(self):
        r"""
        :param TraceId: 溯源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param Type: 码类型 0: 批次, 1: 码, 2: 生产任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Code: 码值，跟码类型一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Rank: 排序，在Phase相同情况下，值越小排名靠前
注意：此字段可能返回 null，表示取不到有效值。
        :type Rank: int
        :param Phase: 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
注意：此字段可能返回 null，表示取不到有效值。
        :type Phase: int
        :param PhaseName: 溯源环节名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PhaseName: str
        :param TraceTime: 溯源时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceTime: str
        :param TraceItems: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceItems: list of TraceItem
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ChainStatus: 上链状态 0: 未上链 1: 上链中 2: 已上链 -1: 异常
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainStatus: int
        :param ChainTime: 上链时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainTime: str
        :param ChainData: 上链数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainData: :class:`tencentcloud.trp.v20210515.models.ChainData`
        :param PhaseData: 溯源阶段配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        :param Status: 溯源阶段状态 0: 无效, 1: 有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.TraceId = None
        self.CorpId = None
        self.Type = None
        self.Code = None
        self.Rank = None
        self.Phase = None
        self.PhaseName = None
        self.TraceTime = None
        self.TraceItems = None
        self.CreateTime = None
        self.ChainStatus = None
        self.ChainTime = None
        self.ChainData = None
        self.PhaseData = None
        self.Status = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.CorpId = params.get("CorpId")
        self.Type = params.get("Type")
        self.Code = params.get("Code")
        self.Rank = params.get("Rank")
        self.Phase = params.get("Phase")
        self.PhaseName = params.get("PhaseName")
        self.TraceTime = params.get("TraceTime")
        if params.get("TraceItems") is not None:
            self.TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self.TraceItems.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ChainTime = params.get("ChainTime")
        if params.get("ChainData") is not None:
            self.ChainData = ChainData()
            self.ChainData._deserialize(params.get("ChainData"))
        if params.get("PhaseData") is not None:
            self.PhaseData = PhaseData()
            self.PhaseData._deserialize(params.get("PhaseData"))
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceItem(AbstractModel):
    """溯源数据项
    Type的枚举值
    text:文本类型, longtext:长文本类型, banner:单图片类型, image:多图片类型, video:视频类型, mp:小程序类型
    具体组合如下
    Type: "text" 文本类型, 对应值 Value: "文本字符串"
    Type: "longtext" 长文本类型, 对应值 Value: "长文本字符串, 支持换行\n"
    Type: "banner" 单图片类型, 对应图片地址 Value: "https://sample.cdn.com/xxx.jpg"
    Type: "image" 多图片类型, 对应图片地址 Values: ["https://sample.cdn.com/1.jpg", "https://sample.cdn.com/2.jpg"]
    Type: "video" 视频类型, 对应视频地址 Value: "https://sample.cdn.com/xxx.mp4"
    Type: "mp" 小程序类型, 对应配置 Values: ["WXAPPID", "WXAPP_PATH", "跳转说明"]

    """

    def __init__(self):
        r"""
        :param Name: 字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 字段值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Type: 类型 text:文本类型, longtext:长文本类型, banner:单图片类型, image:多图片类型, video:视频类型, mp:小程序类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ReadOnly: 只读
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: bool
        :param Hidden: 扫码展示
注意：此字段可能返回 null，表示取不到有效值。
        :type Hidden: bool
        :param Values: 多个值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param Key: 类型标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Ext: 扩展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self.Name = None
        self.Value = None
        self.Type = None
        self.ReadOnly = None
        self.Hidden = None
        self.Values = None
        self.Key = None
        self.Ext = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.ReadOnly = params.get("ReadOnly")
        self.Hidden = params.get("Hidden")
        self.Values = params.get("Values")
        self.Key = params.get("Key")
        self.Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageQuota(AbstractModel):
    """付费信息使用量

    """

    def __init__(self):
        r"""
        :param CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param FactoryCnt: 商户配额
注意：此字段可能返回 null，表示取不到有效值。
        :type FactoryCnt: int
        :param ItemCnt: 商品数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemCnt: int
        :param TrackCnt: 溯源码量
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackCnt: int
        :param SaleCnt: 营销码额度
注意：此字段可能返回 null，表示取不到有效值。
        :type SaleCnt: int
        :param ChainCnt: 区块链上链次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainCnt: int
        :param RiskCnt: 营销风控次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCnt: int
        :param UpdateTime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.CorpId = None
        self.FactoryCnt = None
        self.ItemCnt = None
        self.TrackCnt = None
        self.SaleCnt = None
        self.ChainCnt = None
        self.RiskCnt = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.CorpId = params.get("CorpId")
        self.FactoryCnt = params.get("FactoryCnt")
        self.ItemCnt = params.get("ItemCnt")
        self.TrackCnt = params.get("TrackCnt")
        self.SaleCnt = params.get("SaleCnt")
        self.ChainCnt = params.get("ChainCnt")
        self.RiskCnt = params.get("RiskCnt")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        