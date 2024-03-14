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


class AttrItem(AbstractModel):
    """通用属性

    Type 的枚举值
    text:文本类型, longtext:长文本类型, banner:单图片类型, image:多图片类型, video:视频类型, mp:小程序类型

    具体组合如下
    - Type: "text" 文本类型, 对应值 Value: "文本字符串"
    - Type: "longtext" 长文本类型, 对应值 Value: "长文本字符串, 支持换行\n"
    - Type: "banner" 单图片类型, 对应图片地址 Value: "https://sample.cdn.com/xxx.jpg"
    - Type: "image" 多图片类型, 对应图片地址 Values: ["https://sample.cdn.com/1.jpg", "https://sample.cdn.com/2.jpg"]
    - Type: "video" 视频类型, 对应视频地址 Value: "https://sample.cdn.com/xxx.mp4"
    - Type: "mp" 小程序类型, 对应配置 Values: ["WXAPPID", "WXAPP_PATH", "跳转说明"]

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Value: 字段值
        :type Value: str
        :param _Type: 字段类型
text:文本类型, 
longtext:长文本类型, banner:单图片类型, image:多图片类型,
video:视频类型,
mp:小程序类型
        :type Type: str
        :param _ReadOnly: 只读
        :type ReadOnly: bool
        :param _Hidden: 扫码展示
        :type Hidden: bool
        :param _Values: 多个值
        :type Values: list of str
        :param _Key: 类型标识
        :type Key: str
        :param _Ext: 扩展字段
        :type Ext: str
        """
        self._Name = None
        self._Value = None
        self._Type = None
        self._ReadOnly = None
        self._Hidden = None
        self._Values = None
        self._Key = None
        self._Ext = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Hidden(self):
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._ReadOnly = params.get("ReadOnly")
        self._Hidden = params.get("Hidden")
        self._Values = params.get("Values")
        self._Key = params.get("Key")
        self._Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizedTransferRequest(AbstractModel):
    """AuthorizedTransfer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务加密入参。
        :type BusinessSecurityData: :class:`tencentcloud.trp.v20210515.models.InputEncryptData`
        """
        self._BusinessSecurityData = None

    @property
    def BusinessSecurityData(self):
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = InputEncryptData()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizedTransferResponse(AbstractModel):
    """AuthorizedTransfer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参。
        :type Data: :class:`tencentcloud.trp.v20210515.models.OutputAuthorizedTransfer`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
            self._Data = OutputAuthorizedTransfer()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ChainData(AbstractModel):
    """上链数据

    """

    def __init__(self):
        r"""
        :param _BlockHash: 区块hash
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockHash: str
        :param _BlockHeight: 区块高度
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockHeight: str
        :param _BlockTime: 区块时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockTime: str
        """
        self._BlockHash = None
        self._BlockHeight = None
        self._BlockTime = None

    @property
    def BlockHash(self):
        return self._BlockHash

    @BlockHash.setter
    def BlockHash(self, BlockHash):
        self._BlockHash = BlockHash

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime


    def _deserialize(self, params):
        self._BlockHash = params.get("BlockHash")
        self._BlockHeight = params.get("BlockHeight")
        self._BlockTime = params.get("BlockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeBatch(AbstractModel):
    """批次

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次号
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _BatchCode: 批次编码(未使用)
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchCode: str
        :param _CodeCnt: 码数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeCnt: int
        :param _MerchantId: 所属商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _BatchType: 批次类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchType: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _MpTpl: 微信模板
注意：此字段可能返回 null，表示取不到有效值。
        :type MpTpl: str
        :param _Status: 批次状态 0: 未激活 1: 已激活 -1: 已冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _MerchantName: 所属商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _Ext: 未使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        :param _TplName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TplName: str
        :param _Job: 调度任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.trp.v20210515.models.Job`
        :param _ProductionDate: 生产日期
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductionDate: str
        :param _ValidDate: 有效期
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidDate: str
        :param _Attrs: 扩展属性
        :type Attrs: list of AttrItem
        """
        self._BatchId = None
        self._CorpId = None
        self._BatchCode = None
        self._CodeCnt = None
        self._MerchantId = None
        self._ProductId = None
        self._BatchType = None
        self._Remark = None
        self._MpTpl = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MerchantName = None
        self._ProductName = None
        self._Ext = None
        self._TplName = None
        self._Job = None
        self._ProductionDate = None
        self._ValidDate = None
        self._Attrs = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchCode(self):
        return self._BatchCode

    @BatchCode.setter
    def BatchCode(self, BatchCode):
        self._BatchCode = BatchCode

    @property
    def CodeCnt(self):
        return self._CodeCnt

    @CodeCnt.setter
    def CodeCnt(self, CodeCnt):
        self._CodeCnt = CodeCnt

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchType(self):
        return self._BatchType

    @BatchType.setter
    def BatchType(self, BatchType):
        self._BatchType = BatchType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MpTpl(self):
        return self._MpTpl

    @MpTpl.setter
    def MpTpl(self, MpTpl):
        self._MpTpl = MpTpl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Ext(self):
        warnings.warn("parameter `Ext` is deprecated", DeprecationWarning) 

        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        warnings.warn("parameter `Ext` is deprecated", DeprecationWarning) 

        self._Ext = Ext

    @property
    def TplName(self):
        return self._TplName

    @TplName.setter
    def TplName(self, TplName):
        self._TplName = TplName

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def ProductionDate(self):
        return self._ProductionDate

    @ProductionDate.setter
    def ProductionDate(self, ProductionDate):
        self._ProductionDate = ProductionDate

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Attrs(self):
        return self._Attrs

    @Attrs.setter
    def Attrs(self, Attrs):
        self._Attrs = Attrs


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CorpId = params.get("CorpId")
        self._BatchCode = params.get("BatchCode")
        self._CodeCnt = params.get("CodeCnt")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._BatchType = params.get("BatchType")
        self._Remark = params.get("Remark")
        self._MpTpl = params.get("MpTpl")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MerchantName = params.get("MerchantName")
        self._ProductName = params.get("ProductName")
        if params.get("Ext") is not None:
            self._Ext = Ext()
            self._Ext._deserialize(params.get("Ext"))
        self._TplName = params.get("TplName")
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._ProductionDate = params.get("ProductionDate")
        self._ValidDate = params.get("ValidDate")
        if params.get("Attrs") is not None:
            self._Attrs = []
            for item in params.get("Attrs"):
                obj = AttrItem()
                obj._deserialize(item)
                self._Attrs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeItem(AbstractModel):
    """码类型

    """

    def __init__(self):
        r"""
        :param _Code: 无
        :type Code: str
        """
        self._Code = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePack(AbstractModel):
    """码包类型

    """

    def __init__(self):
        r"""
        :param _PackId: 码id
注意：此字段可能返回 null，表示取不到有效值。
        :type PackId: str
        :param _CorpId: 企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _MerchantId: 商户id
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Status: 制码状态 init: 初始化, pending: 执行中, done: 完成, error: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Log: 执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param _CreateUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUser: str
        :param _Amount: 码数
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: int
        :param _CodeLength: 防伪码长度
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeLength: int
        :param _CodeType: 码类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param _Cipher: 是否暗码
注意：此字段可能返回 null，表示取不到有效值。
        :type Cipher: int
        :param _TextUrl: [弃用] 文字码地址，通过另一个接口查
注意：此字段可能返回 null，表示取不到有效值。
        :type TextUrl: str
        :param _PackUrl: [弃用] 二维码地址，通过另一个接口查
注意：此字段可能返回 null，表示取不到有效值。
        :type PackUrl: str
        :param _MerchantName: 商户名
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param _RuleType: 码规则类型 0: 默认, 1: 自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: int
        :param _CustomId: 自定义码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param _PackType: 码包类型 0: 普通码包 1: 层级码包
注意：此字段可能返回 null，表示取不到有效值。
        :type PackType: int
        :param _PackLevel: 生码层级
注意：此字段可能返回 null，表示取不到有效值。
        :type PackLevel: int
        :param _PackSpec: 层级码配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PackSpec: list of PackSpec
        :param _ProductName: 商品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _ProductSpecification: 商品规格
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductSpecification: str
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _RelateType: 码关系是否预关联
0:否, 1:是
        :type RelateType: int
        """
        self._PackId = None
        self._CorpId = None
        self._MerchantId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._Log = None
        self._CreateUser = None
        self._Amount = None
        self._CodeLength = None
        self._CodeType = None
        self._Cipher = None
        self._TextUrl = None
        self._PackUrl = None
        self._MerchantName = None
        self._RuleType = None
        self._CustomId = None
        self._PackType = None
        self._PackLevel = None
        self._PackSpec = None
        self._ProductName = None
        self._ProductSpecification = None
        self._ProductId = None
        self._RelateType = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def CreateUser(self):
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def CodeLength(self):
        return self._CodeLength

    @CodeLength.setter
    def CodeLength(self, CodeLength):
        self._CodeLength = CodeLength

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def Cipher(self):
        return self._Cipher

    @Cipher.setter
    def Cipher(self, Cipher):
        self._Cipher = Cipher

    @property
    def TextUrl(self):
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def PackUrl(self):
        return self._PackUrl

    @PackUrl.setter
    def PackUrl(self, PackUrl):
        self._PackUrl = PackUrl

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def PackType(self):
        return self._PackType

    @PackType.setter
    def PackType(self, PackType):
        self._PackType = PackType

    @property
    def PackLevel(self):
        return self._PackLevel

    @PackLevel.setter
    def PackLevel(self, PackLevel):
        self._PackLevel = PackLevel

    @property
    def PackSpec(self):
        return self._PackSpec

    @PackSpec.setter
    def PackSpec(self, PackSpec):
        self._PackSpec = PackSpec

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductSpecification(self):
        return self._ProductSpecification

    @ProductSpecification.setter
    def ProductSpecification(self, ProductSpecification):
        self._ProductSpecification = ProductSpecification

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RelateType(self):
        return self._RelateType

    @RelateType.setter
    def RelateType(self, RelateType):
        self._RelateType = RelateType


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Log = params.get("Log")
        self._CreateUser = params.get("CreateUser")
        self._Amount = params.get("Amount")
        self._CodeLength = params.get("CodeLength")
        self._CodeType = params.get("CodeType")
        self._Cipher = params.get("Cipher")
        self._TextUrl = params.get("TextUrl")
        self._PackUrl = params.get("PackUrl")
        self._MerchantName = params.get("MerchantName")
        self._RuleType = params.get("RuleType")
        self._CustomId = params.get("CustomId")
        self._PackType = params.get("PackType")
        self._PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self._PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self._PackSpec.append(obj)
        self._ProductName = params.get("ProductName")
        self._ProductSpecification = params.get("ProductSpecification")
        self._ProductId = params.get("ProductId")
        self._RelateType = params.get("RelateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePart(AbstractModel):
    """码段配置

    """

    def __init__(self):
        r"""
        :param _Name: 码段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 码段类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Value: 码段内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Length: 码段长度
        :type Length: int
        :param _Ext: 扩展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self._Name = None
        self._Type = None
        self._Value = None
        self._Length = None
        self._Ext = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._Length = params.get("Length")
        self._Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorpQuota(AbstractModel):
    """渠道商的子企业额度使用情况

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _CorpName: 企业名称
        :type CorpName: str
        :param _Quota: 额度
        :type Quota: :class:`tencentcloud.trp.v20210515.models.Quota`
        :param _UsageQuota: 额度使用量
        :type UsageQuota: :class:`tencentcloud.trp.v20210515.models.UsageQuota`
        """
        self._CorpId = None
        self._CorpName = None
        self._Quota = None
        self._UsageQuota = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def CorpName(self):
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def UsageQuota(self):
        return self._UsageQuota

    @UsageQuota.setter
    def UsageQuota(self, UsageQuota):
        self._UsageQuota = UsageQuota


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._CorpName = params.get("CorpName")
        if params.get("Quota") is not None:
            self._Quota = Quota()
            self._Quota._deserialize(params.get("Quota"))
        if params.get("UsageQuota") is not None:
            self._UsageQuota = UsageQuota()
            self._UsageQuota._deserialize(params.get("UsageQuota"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeBatchRequest(AbstractModel):
    """CreateCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BatchType: 批次类型 0:溯源 1:营销
        :type BatchType: int
        :param _BatchId: 批次ID，留空时系统自动生成
        :type BatchId: str
        :param _Remark: 备注
        :type Remark: str
        :param _MpTpl: 模板ID，或者活动ID
        :type MpTpl: str
        :param _CloneId: 克隆批次ID，同时会复制溯源信息
        :type CloneId: str
        :param _BatchCode: 批次编号，业务字段不判断唯一性
        :type BatchCode: str
        :param _ValidDate: 有效期
        :type ValidDate: str
        :param _ProductionDate: 生产日期
        :type ProductionDate: str
        """
        self._CorpId = None
        self._MerchantId = None
        self._ProductId = None
        self._BatchType = None
        self._BatchId = None
        self._Remark = None
        self._MpTpl = None
        self._CloneId = None
        self._BatchCode = None
        self._ValidDate = None
        self._ProductionDate = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchType(self):
        return self._BatchType

    @BatchType.setter
    def BatchType(self, BatchType):
        self._BatchType = BatchType

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MpTpl(self):
        return self._MpTpl

    @MpTpl.setter
    def MpTpl(self, MpTpl):
        self._MpTpl = MpTpl

    @property
    def CloneId(self):
        return self._CloneId

    @CloneId.setter
    def CloneId(self, CloneId):
        self._CloneId = CloneId

    @property
    def BatchCode(self):
        return self._BatchCode

    @BatchCode.setter
    def BatchCode(self, BatchCode):
        self._BatchCode = BatchCode

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def ProductionDate(self):
        return self._ProductionDate

    @ProductionDate.setter
    def ProductionDate(self, ProductionDate):
        self._ProductionDate = ProductionDate


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._BatchType = params.get("BatchType")
        self._BatchId = params.get("BatchId")
        self._Remark = params.get("Remark")
        self._MpTpl = params.get("MpTpl")
        self._CloneId = params.get("CloneId")
        self._BatchCode = params.get("BatchCode")
        self._ValidDate = params.get("ValidDate")
        self._ProductionDate = params.get("ProductionDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeBatchResponse(AbstractModel):
    """CreateCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class CreateCodePackRequest(AbstractModel):
    """CreateCodePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _CodeLength: 码长度
        :type CodeLength: int
        :param _CodeType: 码类型 alphabet 字母, number 数字, mixin 混合
        :type CodeType: str
        :param _Amount: 生码数量 普通码包时必填
        :type Amount: int
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _PackType: 码包类型 0: 普通码包 1: 层级码包
        :type PackType: int
        :param _PackLevel: 码包层级
        :type PackLevel: int
        :param _PackSpec: 码包规格
        :type PackSpec: list of PackSpec
        :param _BatchId: 批次ID，如果传了生码后会同时绑定批次，并激活码
        :type BatchId: str
        :param _SerialType: 是否有流水码 0:无 1:有
        :type SerialType: int
        :param _ProductId: 关联产品ID
        :type ProductId: str
        :param _RelateType: 层级码时是否提前生成关联关系，默认为 1
        :type RelateType: int
        """
        self._MerchantId = None
        self._CodeLength = None
        self._CodeType = None
        self._Amount = None
        self._CorpId = None
        self._PackType = None
        self._PackLevel = None
        self._PackSpec = None
        self._BatchId = None
        self._SerialType = None
        self._ProductId = None
        self._RelateType = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CodeLength(self):
        return self._CodeLength

    @CodeLength.setter
    def CodeLength(self, CodeLength):
        self._CodeLength = CodeLength

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PackType(self):
        return self._PackType

    @PackType.setter
    def PackType(self, PackType):
        self._PackType = PackType

    @property
    def PackLevel(self):
        return self._PackLevel

    @PackLevel.setter
    def PackLevel(self, PackLevel):
        self._PackLevel = PackLevel

    @property
    def PackSpec(self):
        return self._PackSpec

    @PackSpec.setter
    def PackSpec(self, PackSpec):
        self._PackSpec = PackSpec

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def SerialType(self):
        return self._SerialType

    @SerialType.setter
    def SerialType(self, SerialType):
        self._SerialType = SerialType

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RelateType(self):
        return self._RelateType

    @RelateType.setter
    def RelateType(self, RelateType):
        self._RelateType = RelateType


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._CodeLength = params.get("CodeLength")
        self._CodeType = params.get("CodeType")
        self._Amount = params.get("Amount")
        self._CorpId = params.get("CorpId")
        self._PackType = params.get("PackType")
        self._PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self._PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self._PackSpec.append(obj)
        self._BatchId = params.get("BatchId")
        self._SerialType = params.get("SerialType")
        self._ProductId = params.get("ProductId")
        self._RelateType = params.get("RelateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodePackResponse(AbstractModel):
    """CreateCodePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackId: 码包ID
        :type PackId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackId = None
        self._RequestId = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._RequestId = params.get("RequestId")


class CreateCorporationOrderRequest(AbstractModel):
    """CreateCorporationOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpName: 企业名称
        :type CorpName: str
        :param _Owner: 所有者ID
        :type Owner: str
        :param _CodeQuota: 溯源码额度
        :type CodeQuota: int
        :param _ExpireTime: 额度过期时间
        :type ExpireTime: str
        :param _Amount: 金额
        :type Amount: int
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _ContactPerson: 联系人
        :type ContactPerson: str
        :param _ContactNumber: 联系电话
        :type ContactNumber: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._CorpName = None
        self._Owner = None
        self._CodeQuota = None
        self._ExpireTime = None
        self._Amount = None
        self._CorpId = None
        self._ContactPerson = None
        self._ContactNumber = None
        self._Remark = None

    @property
    def CorpName(self):
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def CodeQuota(self):
        return self._CodeQuota

    @CodeQuota.setter
    def CodeQuota(self, CodeQuota):
        self._CodeQuota = CodeQuota

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def ContactPerson(self):
        return self._ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self._ContactPerson = ContactPerson

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._CorpName = params.get("CorpName")
        self._Owner = params.get("Owner")
        self._CodeQuota = params.get("CodeQuota")
        self._ExpireTime = params.get("ExpireTime")
        self._Amount = params.get("Amount")
        self._CorpId = params.get("CorpId")
        self._ContactPerson = params.get("ContactPerson")
        self._ContactNumber = params.get("ContactNumber")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorporationOrderResponse(AbstractModel):
    """CreateCorporationOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorpId = None
        self._RequestId = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._RequestId = params.get("RequestId")


class CreateCustomPackRequest(AbstractModel):
    """CreateCustomPack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _Amount: 生码数量, 普通码包时必填
        :type Amount: int
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _PackType: 码包类型 0: 普通码包 1: 层级码包
        :type PackType: int
        :param _PackLevel: 码包层级
        :type PackLevel: int
        :param _PackSpec: 层级码包规则
        :type PackSpec: list of PackSpec
        :param _CustomId: 码规则ID,  和CodeParts二选一必填
        :type CustomId: str
        :param _CodeParts: 码段配置，和CustomId二选一必填
        :type CodeParts: list of CodePart
        :param _BatchId: 批次ID，如果传了生码后会同时绑定批次，并激活码
        :type BatchId: str
        :param _SerialType: 是否有流水码 0:无 1:有
        :type SerialType: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _RelateType: 是否预生成码关系
0: 否, 1:是
默认为1，仅对层级码有效
        :type RelateType: int
        """
        self._MerchantId = None
        self._Amount = None
        self._CorpId = None
        self._PackType = None
        self._PackLevel = None
        self._PackSpec = None
        self._CustomId = None
        self._CodeParts = None
        self._BatchId = None
        self._SerialType = None
        self._ProductId = None
        self._RelateType = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PackType(self):
        return self._PackType

    @PackType.setter
    def PackType(self, PackType):
        self._PackType = PackType

    @property
    def PackLevel(self):
        return self._PackLevel

    @PackLevel.setter
    def PackLevel(self, PackLevel):
        self._PackLevel = PackLevel

    @property
    def PackSpec(self):
        return self._PackSpec

    @PackSpec.setter
    def PackSpec(self, PackSpec):
        self._PackSpec = PackSpec

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def CodeParts(self):
        return self._CodeParts

    @CodeParts.setter
    def CodeParts(self, CodeParts):
        self._CodeParts = CodeParts

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def SerialType(self):
        return self._SerialType

    @SerialType.setter
    def SerialType(self, SerialType):
        self._SerialType = SerialType

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RelateType(self):
        return self._RelateType

    @RelateType.setter
    def RelateType(self, RelateType):
        self._RelateType = RelateType


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._Amount = params.get("Amount")
        self._CorpId = params.get("CorpId")
        self._PackType = params.get("PackType")
        self._PackLevel = params.get("PackLevel")
        if params.get("PackSpec") is not None:
            self._PackSpec = []
            for item in params.get("PackSpec"):
                obj = PackSpec()
                obj._deserialize(item)
                self._PackSpec.append(obj)
        self._CustomId = params.get("CustomId")
        if params.get("CodeParts") is not None:
            self._CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self._CodeParts.append(obj)
        self._BatchId = params.get("BatchId")
        self._SerialType = params.get("SerialType")
        self._ProductId = params.get("ProductId")
        self._RelateType = params.get("RelateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomPackResponse(AbstractModel):
    """CreateCustomPack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackId: 码包ID
        :type PackId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackId = None
        self._RequestId = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._RequestId = params.get("RequestId")


class CreateCustomRuleRequest(AbstractModel):
    """CreateCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _CodeLength: 码长度
        :type CodeLength: int
        :param _CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._Name = None
        self._MerchantId = None
        self._CodeLength = None
        self._CodeParts = None
        self._CorpId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CodeLength(self):
        return self._CodeLength

    @CodeLength.setter
    def CodeLength(self, CodeLength):
        self._CodeLength = CodeLength

    @property
    def CodeParts(self):
        return self._CodeParts

    @CodeParts.setter
    def CodeParts(self, CodeParts):
        self._CodeParts = CodeParts

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MerchantId = params.get("MerchantId")
        self._CodeLength = params.get("CodeLength")
        if params.get("CodeParts") is not None:
            self._CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self._CodeParts.append(obj)
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomRuleResponse(AbstractModel):
    """CreateCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomId = None
        self._RequestId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._RequestId = params.get("RequestId")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 商户名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _CodeType: 码包来源 0:自建, 1:第三发
        :type CodeType: int
        :param _CodeUrl: 码包前缀地址 第三方码包时必填
        :type CodeUrl: str
        """
        self._Name = None
        self._Remark = None
        self._CorpId = None
        self._CodeType = None
        self._CodeUrl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CodeUrl(self):
        return self._CodeUrl

    @CodeUrl.setter
    def CodeUrl(self, CodeUrl):
        self._CodeUrl = CodeUrl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._CorpId = params.get("CorpId")
        self._CodeType = params.get("CodeType")
        self._CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MerchantId = None
        self._RequestId = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 商品名称
        :type Name: str
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _Remark: 备注
        :type Remark: str
        :param _MerchantName: 商户名称
        :type MerchantName: str
        :param _Specification: 商品规格
        :type Specification: str
        :param _Logo: 商品图片
        :type Logo: list of str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Ext: 预留字段
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        """
        self._Name = None
        self._MerchantId = None
        self._Remark = None
        self._MerchantName = None
        self._Specification = None
        self._Logo = None
        self._CorpId = None
        self._Ext = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MerchantId = params.get("MerchantId")
        self._Remark = params.get("Remark")
        self._MerchantName = params.get("MerchantName")
        self._Specification = params.get("Specification")
        self._Logo = params.get("Logo")
        self._CorpId = params.get("CorpId")
        if params.get("Ext") is not None:
            self._Ext = Ext()
            self._Ext._deserialize(params.get("Ext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._RequestId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RequestId = params.get("RequestId")


class CreateTraceChainRequest(AbstractModel):
    """CreateTraceChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _TraceId: 溯源ID
        :type TraceId: str
        """
        self._CorpId = None
        self._TraceId = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceChainResponse(AbstractModel):
    """CreateTraceChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._RequestId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class CreateTraceCodesAsyncRequest(AbstractModel):
    """CreateTraceCodesAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _FileKey: 上传文件Key，仅支持 csv 或者 zip 类型
        :type FileKey: str
        """
        self._CorpId = None
        self._BatchId = None
        self._FileKey = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def FileKey(self):
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        self._FileKey = params.get("FileKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceCodesAsyncResponse(AbstractModel):
    """CreateTraceCodesAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class CreateTraceCodesRequest(AbstractModel):
    """CreateTraceCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Codes: 码
        :type Codes: list of CodeItem
        :param _CodeType: 码绑定激活策略，默认  0
0: 传什么码就激活什么码
1: 层级码 + 层级子码
        :type CodeType: int
        :param _CheckType: 错误检查类型，默认 0
0: 没有新导入码时正常返回
1: 没有新导入码时报错，并返回没有导入成功的原因
        :type CheckType: int
        """
        self._BatchId = None
        self._CorpId = None
        self._Codes = None
        self._CodeType = None
        self._CheckType = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Codes(self):
        return self._Codes

    @Codes.setter
    def Codes(self, Codes):
        self._Codes = Codes

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CheckType(self):
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CorpId = params.get("CorpId")
        if params.get("Codes") is not None:
            self._Codes = []
            for item in params.get("Codes"):
                obj = CodeItem()
                obj._deserialize(item)
                self._Codes.append(obj)
        self._CodeType = params.get("CodeType")
        self._CheckType = params.get("CheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceCodesResponse(AbstractModel):
    """CreateTraceCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _ActiveCnt: 导入成功码数量
        :type ActiveCnt: int
        :param _CodeCnt: 批次码数量
        :type CodeCnt: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._ActiveCnt = None
        self._CodeCnt = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def ActiveCnt(self):
        return self._ActiveCnt

    @ActiveCnt.setter
    def ActiveCnt(self, ActiveCnt):
        self._ActiveCnt = ActiveCnt

    @property
    def CodeCnt(self):
        return self._CodeCnt

    @CodeCnt.setter
    def CodeCnt(self, CodeCnt):
        self._CodeCnt = CodeCnt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._ActiveCnt = params.get("ActiveCnt")
        self._CodeCnt = params.get("CodeCnt")
        self._RequestId = params.get("RequestId")


class CreateTraceDataRequest(AbstractModel):
    """CreateTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Phase: 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
        :type Phase: int
        :param _PhaseName: 溯源阶段名称
        :type PhaseName: str
        :param _ChainStatus: [无效] 上链状态
        :type ChainStatus: int
        :param _Type: [无效] 码类型 0: 批次, 1: 码, 2: 生产任务, 3: 物流信息
        :type Type: int
        :param _TraceId: [无效] 溯源ID
        :type TraceId: str
        :param _TraceItems: 溯源信息
        :type TraceItems: list of TraceItem
        :param _Status: 溯源状态 0: 无效, 1: 有效
        :type Status: int
        :param _PhaseData: 环节数据
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        """
        self._CorpId = None
        self._BatchId = None
        self._TaskId = None
        self._Phase = None
        self._PhaseName = None
        self._ChainStatus = None
        self._Type = None
        self._TraceId = None
        self._TraceItems = None
        self._Status = None
        self._PhaseData = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def PhaseName(self):
        return self._PhaseName

    @PhaseName.setter
    def PhaseName(self, PhaseName):
        self._PhaseName = PhaseName

    @property
    def ChainStatus(self):
        return self._ChainStatus

    @ChainStatus.setter
    def ChainStatus(self, ChainStatus):
        self._ChainStatus = ChainStatus

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def TraceItems(self):
        return self._TraceItems

    @TraceItems.setter
    def TraceItems(self, TraceItems):
        self._TraceItems = TraceItems

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PhaseData(self):
        return self._PhaseData

    @PhaseData.setter
    def PhaseData(self, PhaseData):
        self._PhaseData = PhaseData


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        self._Phase = params.get("Phase")
        self._PhaseName = params.get("PhaseName")
        self._ChainStatus = params.get("ChainStatus")
        self._Type = params.get("Type")
        self._TraceId = params.get("TraceId")
        if params.get("TraceItems") is not None:
            self._TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self._TraceItems.append(obj)
        self._Status = params.get("Status")
        if params.get("PhaseData") is not None:
            self._PhaseData = PhaseData()
            self._PhaseData._deserialize(params.get("PhaseData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceDataResponse(AbstractModel):
    """CreateTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._RequestId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class CustomRule(AbstractModel):
    """码规则

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
        :type CustomId: str
        :param _Name: 码规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _MerchantId: 商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _CodeLength: 码ID长度
        :type CodeLength: int
        :param _Status: 规则状态
        :type Status: int
        :param _CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._CustomId = None
        self._Name = None
        self._CorpId = None
        self._MerchantId = None
        self._CodeLength = None
        self._Status = None
        self._CodeParts = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CodeLength(self):
        return self._CodeLength

    @CodeLength.setter
    def CodeLength(self, CodeLength):
        self._CodeLength = CodeLength

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CodeParts(self):
        return self._CodeParts

    @CodeParts.setter
    def CodeParts(self, CodeParts):
        self._CodeParts = CodeParts

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._Name = params.get("Name")
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._CodeLength = params.get("CodeLength")
        self._Status = params.get("Status")
        if params.get("CodeParts") is not None:
            self._CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self._CodeParts.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeBatchRequest(AbstractModel):
    """DeleteCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        """
        self._CorpId = None
        self._BatchId = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeBatchResponse(AbstractModel):
    """DeleteCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class DeleteMerchantRequest(AbstractModel):
    """DeleteMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
        :type MerchantId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._MerchantId = None
        self._CorpId = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMerchantResponse(AbstractModel):
    """DeleteMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MerchantId = None
        self._RequestId = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 商品ID
        :type ProductId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._ProductId = None
        self._CorpId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._RequestId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RequestId = params.get("RequestId")


class DeleteTraceDataRequest(AbstractModel):
    """DeleteTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._TraceId = None
        self._CorpId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTraceDataResponse(AbstractModel):
    """DeleteTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源id
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._RequestId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class DescribeAgentCorpsRequest(AbstractModel):
    """DescribeAgentCorps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _AgentId: 渠道ID
        :type AgentId: int
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._PageSize = None
        self._PageNumber = None
        self._AgentId = None
        self._CorpId = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._AgentId = params.get("AgentId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentCorpsResponse(AbstractModel):
    """DescribeAgentCorps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCodeBatchByIdRequest(AbstractModel):
    """DescribeCodeBatchById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        """
        self._CorpId = None
        self._BatchId = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeBatchByIdResponse(AbstractModel):
    """DescribeCodeBatchById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeBatch: 批次
        :type CodeBatch: :class:`tencentcloud.trp.v20210515.models.CodeBatch`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeBatch = None
        self._RequestId = None

    @property
    def CodeBatch(self):
        return self._CodeBatch

    @CodeBatch.setter
    def CodeBatch(self, CodeBatch):
        self._CodeBatch = CodeBatch

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CodeBatch") is not None:
            self._CodeBatch = CodeBatch()
            self._CodeBatch._deserialize(params.get("CodeBatch"))
        self._RequestId = params.get("RequestId")


class DescribeCodeBatchesRequest(AbstractModel):
    """DescribeCodeBatches请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 查询商户ID
        :type MerchantId: str
        :param _ProductId: 查询商品ID
        :type ProductId: str
        :param _Keyword: 查询关键字
        :type Keyword: str
        :param _PageSize: 条数
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _BatchType: 批次类型 0:溯源 1:营销
        :type BatchType: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Status: 批次状态
        :type Status: int
        """
        self._MerchantId = None
        self._ProductId = None
        self._Keyword = None
        self._PageSize = None
        self._PageNumber = None
        self._BatchType = None
        self._CorpId = None
        self._Status = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def BatchType(self):
        return self._BatchType

    @BatchType.setter
    def BatchType(self, BatchType):
        self._BatchType = BatchType

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._Keyword = params.get("Keyword")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._BatchType = params.get("BatchType")
        self._CorpId = params.get("CorpId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeBatchesResponse(AbstractModel):
    """DescribeCodeBatches返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeBatches: 批次列表
        :type CodeBatches: list of CodeBatch
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeBatches = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CodeBatches(self):
        return self._CodeBatches

    @CodeBatches.setter
    def CodeBatches(self, CodeBatches):
        self._CodeBatches = CodeBatches

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CodeBatches") is not None:
            self._CodeBatches = []
            for item in params.get("CodeBatches"):
                obj = CodeBatch()
                obj._deserialize(item)
                self._CodeBatches.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCodeBatchsRequest(AbstractModel):
    """DescribeCodeBatchs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 查询商户ID
        :type MerchantId: str
        :param _ProductId: 查询商品ID
        :type ProductId: str
        :param _Keyword: 查询关键字
        :type Keyword: str
        :param _PageSize: 条数
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _BatchType: 批次类型 0:溯源 1:营销
        :type BatchType: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Status: 批次状态
        :type Status: int
        """
        self._MerchantId = None
        self._ProductId = None
        self._Keyword = None
        self._PageSize = None
        self._PageNumber = None
        self._BatchType = None
        self._CorpId = None
        self._Status = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def BatchType(self):
        return self._BatchType

    @BatchType.setter
    def BatchType(self, BatchType):
        self._BatchType = BatchType

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._Keyword = params.get("Keyword")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._BatchType = params.get("BatchType")
        self._CorpId = params.get("CorpId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodeBatchsResponse(AbstractModel):
    """DescribeCodeBatchs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeBatchs: 批次列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeBatchs: list of CodeBatch
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeBatchs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CodeBatchs(self):
        return self._CodeBatchs

    @CodeBatchs.setter
    def CodeBatchs(self, CodeBatchs):
        self._CodeBatchs = CodeBatchs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CodeBatchs") is not None:
            self._CodeBatchs = []
            for item in params.get("CodeBatchs"):
                obj = CodeBatch()
                obj._deserialize(item)
                self._CodeBatchs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCodePackStatusRequest(AbstractModel):
    """DescribeCodePackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackId: 码包ID
        :type PackId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._PackId = None
        self._CorpId = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePackStatusResponse(AbstractModel):
    """DescribeCodePackStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 码包状态 init: 初始化, pending: 执行中, done: 完成, error: 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeCodePackUrlRequest(AbstractModel):
    """DescribeCodePackUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackId: 码包ID
        :type PackId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._PackId = None
        self._CorpId = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePackUrlResponse(AbstractModel):
    """DescribeCodePackUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 文字码包地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _ImgUrl: 图片码包地址，可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ImgUrl: str
        :param _FileKey: 文字码包Key，用于上传导入
注意：此字段可能返回 null，表示取不到有效值。
        :type FileKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._ImgUrl = None
        self._FileKey = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ImgUrl(self):
        return self._ImgUrl

    @ImgUrl.setter
    def ImgUrl(self, ImgUrl):
        self._ImgUrl = ImgUrl

    @property
    def FileKey(self):
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ImgUrl = params.get("ImgUrl")
        self._FileKey = params.get("FileKey")
        self._RequestId = params.get("RequestId")


class DescribeCodePacksRequest(AbstractModel):
    """DescribeCodePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _Keyword: 查询关键字
        :type Keyword: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _SerialType: 是否有流水码 0:无 1:有
        :type SerialType: int
        :param _ResType: 资源类型 batch:批次, order_in 入库, order_out: 出入
        :type ResType: str
        :param _ResId: 资源ID ResType是 batch 时对应是批次ID, 是 order_in, order_out时，则是订单ID
        :type ResId: str
        """
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None
        self._CorpId = None
        self._SerialType = None
        self._ResType = None
        self._ResId = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def SerialType(self):
        return self._SerialType

    @SerialType.setter
    def SerialType(self, SerialType):
        self._SerialType = SerialType

    @property
    def ResType(self):
        return self._ResType

    @ResType.setter
    def ResType(self, ResType):
        self._ResType = ResType

    @property
    def ResId(self):
        return self._ResId

    @ResId.setter
    def ResId(self, ResId):
        self._ResId = ResId


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        self._CorpId = params.get("CorpId")
        self._SerialType = params.get("SerialType")
        self._ResType = params.get("ResType")
        self._ResId = params.get("ResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodePacksResponse(AbstractModel):
    """DescribeCodePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodePacks: 码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePacks: list of CodePack
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodePacks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CodePacks(self):
        return self._CodePacks

    @CodePacks.setter
    def CodePacks(self, CodePacks):
        self._CodePacks = CodePacks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CodePacks") is not None:
            self._CodePacks = []
            for item in params.get("CodePacks"):
                obj = CodePack()
                obj._deserialize(item)
                self._CodePacks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCodesByPackRequest(AbstractModel):
    """DescribeCodesByPack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackId: 码包ID
        :type PackId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._PackId = None
        self._CorpId = None

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._PackId = params.get("PackId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCodesByPackResponse(AbstractModel):
    """DescribeCodesByPack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Codes: 码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Codes: list of CodeItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Codes = None
        self._RequestId = None

    @property
    def Codes(self):
        return self._Codes

    @Codes.setter
    def Codes(self, Codes):
        self._Codes = Codes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Codes") is not None:
            self._Codes = []
            for item in params.get("Codes"):
                obj = CodeItem()
                obj._deserialize(item)
                self._Codes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCorpQuotasRequest(AbstractModel):
    """DescribeCorpQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: 渠道商ID，不要传
        :type AgentId: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Keyword: 搜索企业ID
        :type Keyword: str
        """
        self._AgentId = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCorpQuotasResponse(AbstractModel):
    """DescribeCorpQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpQuotas: 子企业额度使用情况
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpQuotas: list of CorpQuota
        :param _Total: 记录总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorpQuotas = None
        self._Total = None
        self._RequestId = None

    @property
    def CorpQuotas(self):
        return self._CorpQuotas

    @CorpQuotas.setter
    def CorpQuotas(self, CorpQuotas):
        self._CorpQuotas = CorpQuotas

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CorpQuotas") is not None:
            self._CorpQuotas = []
            for item in params.get("CorpQuotas"):
                obj = CorpQuota()
                obj._deserialize(item)
                self._CorpQuotas.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCustomRuleByIdRequest(AbstractModel):
    """DescribeCustomRuleById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
        :type CustomId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._CustomId = None
        self._CorpId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRuleByIdResponse(AbstractModel):
    """DescribeCustomRuleById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomRule: 码规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRule: :class:`tencentcloud.trp.v20210515.models.CustomRule`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomRule = None
        self._RequestId = None

    @property
    def CustomRule(self):
        return self._CustomRule

    @CustomRule.setter
    def CustomRule(self, CustomRule):
        self._CustomRule = CustomRule

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomRule") is not None:
            self._CustomRule = CustomRule()
            self._CustomRule._deserialize(params.get("CustomRule"))
        self._RequestId = params.get("RequestId")


class DescribeCustomRulesRequest(AbstractModel):
    """DescribeCustomRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Keyword: 搜索关键字
        :type Keyword: str
        :param _PageSize: 条数
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Status: 码规则状态 0:未生效 1:已生效 -1:已失效
        :type Status: int
        :param _MerchantId: 商户ID
        :type MerchantId: str
        """
        self._Keyword = None
        self._PageSize = None
        self._PageNumber = None
        self._CorpId = None
        self._Status = None
        self._MerchantId = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._CorpId = params.get("CorpId")
        self._Status = params.get("Status")
        self._MerchantId = params.get("MerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRulesResponse(AbstractModel):
    """DescribeCustomRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomRules: 码规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRules: list of CustomRule
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomRules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CustomRules(self):
        return self._CustomRules

    @CustomRules.setter
    def CustomRules(self, CustomRules):
        self._CustomRules = CustomRules

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomRules") is not None:
            self._CustomRules = []
            for item in params.get("CustomRules"):
                obj = CustomRule()
                obj._deserialize(item)
                self._CustomRules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeJobFileUrlRequest(AbstractModel):
    """DescribeJobFileUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 调度ID
        :type JobId: int
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._JobId = None
        self._CorpId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobFileUrlResponse(AbstractModel):
    """DescribeJobFileUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 码包地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class DescribeMerchantByIdRequest(AbstractModel):
    """DescribeMerchantById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
        :type MerchantId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._MerchantId = None
        self._CorpId = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMerchantByIdResponse(AbstractModel):
    """DescribeMerchantById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Merchant: 商户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Merchant: :class:`tencentcloud.trp.v20210515.models.Merchant`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Merchant = None
        self._RequestId = None

    @property
    def Merchant(self):
        return self._Merchant

    @Merchant.setter
    def Merchant(self, Merchant):
        self._Merchant = Merchant

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Merchant") is not None:
            self._Merchant = Merchant()
            self._Merchant._deserialize(params.get("Merchant"))
        self._RequestId = params.get("RequestId")


class DescribeMerchantsRequest(AbstractModel):
    """DescribeMerchants请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 搜索商户名称
        :type Name: str
        :param _PageSize: 条数
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _CodeType: 码来源类型 0:自建, 1:第三方
        :type CodeType: int
        """
        self._Name = None
        self._PageSize = None
        self._PageNumber = None
        self._CorpId = None
        self._CodeType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._CorpId = params.get("CorpId")
        self._CodeType = params.get("CodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMerchantsResponse(AbstractModel):
    """DescribeMerchants返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Merchants: 商户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Merchants: list of Merchant
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Merchants = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Merchants(self):
        return self._Merchants

    @Merchants.setter
    def Merchants(self, Merchants):
        self._Merchants = Merchants

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Merchants") is not None:
            self._Merchants = []
            for item in params.get("Merchants"):
                obj = Merchant()
                obj._deserialize(item)
                self._Merchants.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePlanQRCodeScanRecordsRequest(AbstractModel):
    """DescribePlanQRCodeScanRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页大小
        :type PageSize: int
        """
        self._StartTime = None
        self._EndTime = None
        self._PageNo = None
        self._PageSize = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlanQRCodeScanRecordsResponse(AbstractModel):
    """DescribePlanQRCodeScanRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回码
        :type Ret: int
        :param _Total: 总数
        :type Total: int
        :param _Data: 数据
        :type Data: list of PlanQRCodeRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Ret = params.get("Ret")
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PlanQRCodeRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePlanQRCodesRequest(AbstractModel):
    """DescribePlanQRCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页大小
        :type PageSize: int
        """
        self._PlanId = None
        self._StartTime = None
        self._EndTime = None
        self._PageNo = None
        self._PageSize = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlanQRCodesResponse(AbstractModel):
    """DescribePlanQRCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回码
        :type Ret: int
        :param _Total: 总数
        :type Total: int
        :param _Data: 数据
        :type Data: list of PlanQRCode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Ret = params.get("Ret")
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PlanQRCode()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductByIdRequest(AbstractModel):
    """DescribeProductById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 商品ID
        :type ProductId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._ProductId = None
        self._CorpId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductByIdResponse(AbstractModel):
    """DescribeProductById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 商品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: :class:`tencentcloud.trp.v20210515.models.Product`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = Product()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 商品名称
        :type Name: str
        :param _PageSize: 条数
        :type PageSize: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _MerchantId: 商品ID
        :type MerchantId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _CertState: 认证状态
        :type CertState: int
        """
        self._Name = None
        self._PageSize = None
        self._PageNumber = None
        self._MerchantId = None
        self._CorpId = None
        self._CertState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._MerchantId = params.get("MerchantId")
        self._CorpId = params.get("CorpId")
        self._CertState = params.get("CertState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 商品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Products: list of Product
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self._Products.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRawScanLogsRequest(AbstractModel):
    """DescribeRawScanLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID, 默认为当前企业
如果有渠道权限，可以传 0 会查渠道下所有的企业
        :type CorpId: int
        :param _PageSize: 分页数量，默认为 20，最大为 1000
        :type PageSize: int
        :param _PageNumber: 当前分页，默认为 1
        :type PageNumber: int
        :param _AfterLogId: 从哪个日志后查询
即: LogId > $AfterLogId
        :type AfterLogId: int
        :param _StartTime: 开始时间 >= StartTime
        :type StartTime: str
        :param _EndTime: 结束时间 < EndTime
        :type EndTime: str
        """
        self._CorpId = None
        self._PageSize = None
        self._PageNumber = None
        self._AfterLogId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def AfterLogId(self):
        return self._AfterLogId

    @AfterLogId.setter
    def AfterLogId(self, AfterLogId):
        self._AfterLogId = AfterLogId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._AfterLogId = params.get("AfterLogId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRawScanLogsResponse(AbstractModel):
    """DescribeRawScanLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScanLogs: 原始扫码日志
        :type ScanLogs: list of RawScanLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScanLogs = None
        self._RequestId = None

    @property
    def ScanLogs(self):
        return self._ScanLogs

    @ScanLogs.setter
    def ScanLogs(self, ScanLogs):
        self._ScanLogs = ScanLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ScanLogs") is not None:
            self._ScanLogs = []
            for item in params.get("ScanLogs"):
                obj = RawScanLog()
                obj._deserialize(item)
                self._ScanLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanLogsRequest(AbstractModel):
    """DescribeScanLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _PageSize: 分页数量
        :type PageSize: int
        :param _PageNumber: 当前分页
        :type PageNumber: int
        :param _Code: 安心码
        :type Code: str
        :param _Openid: 小程序用户ID
        :type Openid: str
        """
        self._CorpId = None
        self._PageSize = None
        self._PageNumber = None
        self._Code = None
        self._Openid = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Code = params.get("Code")
        self._Openid = params.get("Openid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanLogsResponse(AbstractModel):
    """DescribeScanLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 【弃用】
        :type Products: list of ScanLog
        :param _TotalCount: 条数
        :type TotalCount: int
        :param _ScanLogs: 扫描记录
        :type ScanLogs: list of ScanLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._TotalCount = None
        self._ScanLogs = None
        self._RequestId = None

    @property
    def Products(self):
        warnings.warn("parameter `Products` is deprecated", DeprecationWarning) 

        return self._Products

    @Products.setter
    def Products(self, Products):
        warnings.warn("parameter `Products` is deprecated", DeprecationWarning) 

        self._Products = Products

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ScanLogs(self):
        return self._ScanLogs

    @ScanLogs.setter
    def ScanLogs(self, ScanLogs):
        self._ScanLogs = ScanLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ScanLog()
                obj._deserialize(item)
                self._Products.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("ScanLogs") is not None:
            self._ScanLogs = []
            for item in params.get("ScanLogs"):
                obj = ScanLog()
                obj._deserialize(item)
                self._ScanLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanStatsRequest(AbstractModel):
    """DescribeScanStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _PageSize: 分页数量
        :type PageSize: int
        :param _PageNumber: 当前分页
        :type PageNumber: int
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _Code: 安心码
        :type Code: str
        """
        self._CorpId = None
        self._PageSize = None
        self._PageNumber = None
        self._MerchantId = None
        self._ProductId = None
        self._BatchId = None
        self._Code = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._BatchId = params.get("BatchId")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanStatsResponse(AbstractModel):
    """DescribeScanStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScanStats: 统计记录
        :type ScanStats: list of ScanStat
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScanStats = None
        self._RequestId = None

    @property
    def ScanStats(self):
        return self._ScanStats

    @ScanStats.setter
    def ScanStats(self, ScanStats):
        self._ScanStats = ScanStats

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ScanStats") is not None:
            self._ScanStats = []
            for item in params.get("ScanStats"):
                obj = ScanStat()
                obj._deserialize(item)
                self._ScanStats.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTmpTokenRequest(AbstractModel):
    """DescribeTmpToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._CorpId = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTmpTokenResponse(AbstractModel):
    """DescribeTmpToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: 临时token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._RequestId = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class DescribeTraceCodeByIdRequest(AbstractModel):
    """DescribeTraceCodeById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Code: 二维码
        :type Code: str
        """
        self._CorpId = None
        self._Code = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceCodeByIdResponse(AbstractModel):
    """DescribeTraceCodeById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceCode: 无
        :type TraceCode: :class:`tencentcloud.trp.v20210515.models.TraceCode`
        :param _CodePath: 码路径，如level是2，则为 [1级, 2级]
        :type CodePath: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceCode = None
        self._CodePath = None
        self._RequestId = None

    @property
    def TraceCode(self):
        return self._TraceCode

    @TraceCode.setter
    def TraceCode(self, TraceCode):
        self._TraceCode = TraceCode

    @property
    def CodePath(self):
        return self._CodePath

    @CodePath.setter
    def CodePath(self, CodePath):
        self._CodePath = CodePath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TraceCode") is not None:
            self._TraceCode = TraceCode()
            self._TraceCode._deserialize(params.get("TraceCode"))
        self._CodePath = params.get("CodePath")
        self._RequestId = params.get("RequestId")


class DescribeTraceCodesRequest(AbstractModel):
    """DescribeTraceCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Keyword: 搜索关键字 码标识，或者批次ID
        :type Keyword: str
        :param _PageNumber: 条数
        :type PageNumber: int
        :param _PageSize: 页码
        :type PageSize: int
        :param _BatchId: 批次ID，弃用
        :type BatchId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._Keyword = None
        self._PageNumber = None
        self._PageSize = None
        self._BatchId = None
        self._CorpId = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._BatchId = params.get("BatchId")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceCodesResponse(AbstractModel):
    """DescribeTraceCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceCodes: 标识列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceCodes: list of TraceCode
        :param _TotalCount: 条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceCodes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TraceCodes(self):
        return self._TraceCodes

    @TraceCodes.setter
    def TraceCodes(self, TraceCodes):
        self._TraceCodes = TraceCodes

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TraceCodes") is not None:
            self._TraceCodes = []
            for item in params.get("TraceCodes"):
                obj = TraceCode()
                obj._deserialize(item)
                self._TraceCodes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTraceDataByIdRequest(AbstractModel):
    """DescribeTraceDataById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 溯源ID
        :type Id: str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._Id = None
        self._CorpId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceDataByIdResponse(AbstractModel):
    """DescribeTraceDataById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceData: 无
        :type TraceData: :class:`tencentcloud.trp.v20210515.models.TraceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceData = None
        self._RequestId = None

    @property
    def TraceData(self):
        return self._TraceData

    @TraceData.setter
    def TraceData(self, TraceData):
        self._TraceData = TraceData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TraceData") is not None:
            self._TraceData = TraceData()
            self._TraceData._deserialize(params.get("TraceData"))
        self._RequestId = params.get("RequestId")


class DescribeTraceDataListRequest(AbstractModel):
    """DescribeTraceDataList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _TaskId: 任务ID 用于外部溯源
        :type TaskId: str
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _Code: 二维码
        :type Code: str
        :param _Phase: 溯源阶段 0:商品 1:通用 2:内部溯源 3:外部溯源
        :type Phase: int
        :param _PageSize: 数量
        :type PageSize: int
        """
        self._CorpId = None
        self._BatchId = None
        self._TaskId = None
        self._PageNumber = None
        self._Code = None
        self._Phase = None
        self._PageSize = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._Code = params.get("Code")
        self._Phase = params.get("Phase")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceDataListResponse(AbstractModel):
    """DescribeTraceDataList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _TraceDataList: 无
        :type TraceDataList: list of TraceData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TraceDataList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TraceDataList(self):
        return self._TraceDataList

    @TraceDataList.setter
    def TraceDataList(self, TraceDataList):
        self._TraceDataList = TraceDataList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TraceDataList") is not None:
            self._TraceDataList = []
            for item in params.get("TraceDataList"):
                obj = TraceData()
                obj._deserialize(item)
                self._TraceDataList.append(obj)
        self._RequestId = params.get("RequestId")


class EffectFeedbackRequest(AbstractModel):
    """EffectFeedback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务加密入参。
        :type BusinessSecurityData: :class:`tencentcloud.trp.v20210515.models.InputEncryptData`
        """
        self._BusinessSecurityData = None

    @property
    def BusinessSecurityData(self):
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = InputEncryptData()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EffectFeedbackResponse(AbstractModel):
    """EffectFeedback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参。
        :type Data: :class:`tencentcloud.trp.v20210515.models.OutputAuthorizedTransfer`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
            self._Data = OutputAuthorizedTransfer()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Ext(AbstractModel):
    """预留字段

    """

    def __init__(self):
        r"""
        :param _Value: 字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Value = None

    @property
    def Value(self):
        warnings.warn("parameter `Value` is deprecated", DeprecationWarning) 

        return self._Value

    @Value.setter
    def Value(self, Value):
        warnings.warn("parameter `Value` is deprecated", DeprecationWarning) 

        self._Value = Value


    def _deserialize(self, params):
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputEncryptData(AbstractModel):
    """业务加密入参

    """

    def __init__(self):
        r"""
        :param _EncryptMethod: 加密方式，0：AES加密；

        :type EncryptMethod: int
        :param _EncryptMode: 加密算法中的块处理模式，1：CBC模式； 目前只支持CBC模式
        :type EncryptMode: int
        :param _PaddingType: 填充模式，0：ZeroPadding；1：PKCS5Padding；2：
PKCS7Padding。
        :type PaddingType: int
        :param _EncryptData: 加密数据，将AuthorizedData结构体数组（数组最大长度不超过20）序列化成JSON字符串，对得到的字符串加密并填充到该字段。
        :type EncryptData: str
        :param _IsAuthorized: 用户是否授权，本接口取值：1，已授权。

        :type IsAuthorized: int
        """
        self._EncryptMethod = None
        self._EncryptMode = None
        self._PaddingType = None
        self._EncryptData = None
        self._IsAuthorized = None

    @property
    def EncryptMethod(self):
        return self._EncryptMethod

    @EncryptMethod.setter
    def EncryptMethod(self, EncryptMethod):
        self._EncryptMethod = EncryptMethod

    @property
    def EncryptMode(self):
        return self._EncryptMode

    @EncryptMode.setter
    def EncryptMode(self, EncryptMode):
        self._EncryptMode = EncryptMode

    @property
    def PaddingType(self):
        return self._PaddingType

    @PaddingType.setter
    def PaddingType(self, PaddingType):
        self._PaddingType = PaddingType

    @property
    def EncryptData(self):
        return self._EncryptData

    @EncryptData.setter
    def EncryptData(self, EncryptData):
        self._EncryptData = EncryptData

    @property
    def IsAuthorized(self):
        return self._IsAuthorized

    @IsAuthorized.setter
    def IsAuthorized(self, IsAuthorized):
        self._IsAuthorized = IsAuthorized


    def _deserialize(self, params):
        self._EncryptMethod = params.get("EncryptMethod")
        self._EncryptMode = params.get("EncryptMode")
        self._PaddingType = params.get("PaddingType")
        self._EncryptData = params.get("EncryptData")
        self._IsAuthorized = params.get("IsAuthorized")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """通用调度任务

    """

    def __init__(self):
        r"""
        :param _JobId: 调度ID
        :type JobId: int
        :param _Status: 执行状态 init:初始化, pending: 执行中, done: 执行成功, error: 执行失败
        :type Status: str
        """
        self._JobId = None
        self._Status = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Merchant(AbstractModel):
    """商户信息

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
        :type MerchantId: str
        :param _CorpId: 企业id
        :type CorpId: int
        :param _Name: 商户名称
        :type Name: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CodeRule: 商户码规则
        :type CodeRule: str
        :param _CodeType: 码来源类型 0: 安心平台 1: 第三方码
        :type CodeType: int
        :param _CodeUrl: 第三方码域名前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeUrl: str
        """
        self._MerchantId = None
        self._CorpId = None
        self._Name = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CodeRule = None
        self._CodeType = None
        self._CodeUrl = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CodeRule(self):
        return self._CodeRule

    @CodeRule.setter
    def CodeRule(self, CodeRule):
        self._CodeRule = CodeRule

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CodeUrl(self):
        return self._CodeUrl

    @CodeUrl.setter
    def CodeUrl(self, CodeUrl):
        self._CodeUrl = CodeUrl


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._CorpId = params.get("CorpId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CodeRule = params.get("CodeRule")
        self._CodeType = params.get("CodeType")
        self._CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCodeBatchRequest(AbstractModel):
    """ModifyCodeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Status: 状态 0: 未激活 1: 已激活 -1: 已冻结
        :type Status: int
        :param _MpTpl: 模板ID，或者活动ID
        :type MpTpl: str
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _ProductId: 商品ID
        :type ProductId: str
        :param _Remark: 备注
        :type Remark: str
        :param _BatchCode: 批次编码，业务字段不判断唯一性
        :type BatchCode: str
        :param _ValidDate: 有效期
        :type ValidDate: str
        :param _ProductionDate: 生产日期
        :type ProductionDate: str
        """
        self._BatchId = None
        self._CorpId = None
        self._Status = None
        self._MpTpl = None
        self._MerchantId = None
        self._ProductId = None
        self._Remark = None
        self._BatchCode = None
        self._ValidDate = None
        self._ProductionDate = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MpTpl(self):
        return self._MpTpl

    @MpTpl.setter
    def MpTpl(self, MpTpl):
        self._MpTpl = MpTpl

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def BatchCode(self):
        return self._BatchCode

    @BatchCode.setter
    def BatchCode(self, BatchCode):
        self._BatchCode = BatchCode

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def ProductionDate(self):
        return self._ProductionDate

    @ProductionDate.setter
    def ProductionDate(self, ProductionDate):
        self._ProductionDate = ProductionDate


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._CorpId = params.get("CorpId")
        self._Status = params.get("Status")
        self._MpTpl = params.get("MpTpl")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._Remark = params.get("Remark")
        self._BatchCode = params.get("BatchCode")
        self._ValidDate = params.get("ValidDate")
        self._ProductionDate = params.get("ProductionDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCodeBatchResponse(AbstractModel):
    """ModifyCodeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class ModifyCustomRuleRequest(AbstractModel):
    """ModifyCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
        :type CustomId: str
        :param _Name: 规则名称
        :type Name: str
        :param _CodeLength: 码长度
        :type CodeLength: int
        :param _CodeParts: 码段配置
        :type CodeParts: list of CodePart
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._CustomId = None
        self._Name = None
        self._CodeLength = None
        self._CodeParts = None
        self._CorpId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CodeLength(self):
        return self._CodeLength

    @CodeLength.setter
    def CodeLength(self, CodeLength):
        self._CodeLength = CodeLength

    @property
    def CodeParts(self):
        return self._CodeParts

    @CodeParts.setter
    def CodeParts(self, CodeParts):
        self._CodeParts = CodeParts

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._Name = params.get("Name")
        self._CodeLength = params.get("CodeLength")
        if params.get("CodeParts") is not None:
            self._CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self._CodeParts.append(obj)
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleResponse(AbstractModel):
    """ModifyCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomId = None
        self._RequestId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._RequestId = params.get("RequestId")


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
        :type CustomId: str
        :param _Status: 码规则状态 0:未生效 1:已生效 -1:已失效
        :type Status: int
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._CustomId = None
        self._Status = None
        self._CorpId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._Status = params.get("Status")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleStatusResponse(AbstractModel):
    """ModifyCustomRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomId = None
        self._RequestId = None

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._RequestId = params.get("RequestId")


class ModifyMerchantRequest(AbstractModel):
    """ModifyMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 商户名称
        :type Name: str
        :param _MerchantId: 商户标识码
        :type MerchantId: str
        :param _Remark: 备注
        :type Remark: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _CodeType: 码包来源 0:自建, 1:第三码包，暂不支持修改
        :type CodeType: int
        :param _CodeUrl: 码包前缀地址 第三方码包时必填
        :type CodeUrl: str
        """
        self._Name = None
        self._MerchantId = None
        self._Remark = None
        self._CorpId = None
        self._CodeType = None
        self._CodeUrl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CodeUrl(self):
        return self._CodeUrl

    @CodeUrl.setter
    def CodeUrl(self, CodeUrl):
        self._CodeUrl = CodeUrl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MerchantId = params.get("MerchantId")
        self._Remark = params.get("Remark")
        self._CorpId = params.get("CorpId")
        self._CodeType = params.get("CodeType")
        self._CodeUrl = params.get("CodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMerchantResponse(AbstractModel):
    """ModifyMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MerchantId = None
        self._RequestId = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 商品名称
        :type Name: str
        :param _ProductId: 商品ID
        :type ProductId: str
        :param _Remark: 备注
        :type Remark: str
        :param _Specification: 商品规格
        :type Specification: str
        :param _Logo: 商品图片
        :type Logo: list of str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Ext: 预留字段
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        """
        self._Name = None
        self._ProductId = None
        self._Remark = None
        self._Specification = None
        self._Logo = None
        self._CorpId = None
        self._Ext = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ProductId = params.get("ProductId")
        self._Remark = params.get("Remark")
        self._Specification = params.get("Specification")
        self._Logo = params.get("Logo")
        self._CorpId = params.get("CorpId")
        if params.get("Ext") is not None:
            self._Ext = Ext()
            self._Ext._deserialize(params.get("Ext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductId = None
        self._RequestId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RequestId = params.get("RequestId")


class ModifyTraceCodeRequest(AbstractModel):
    """ModifyTraceCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 二维码
        :type Code: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Status: 状态 0: 冻结 1: 激活
        :type Status: int
        """
        self._Code = None
        self._CorpId = None
        self._Status = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CorpId = params.get("CorpId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceCodeResponse(AbstractModel):
    """ModifyTraceCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTraceCodeUnlinkRequest(AbstractModel):
    """ModifyTraceCodeUnlink请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _Codes: 溯源码列表
        :type Codes: list of str
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._BatchId = None
        self._Codes = None
        self._CorpId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Codes(self):
        return self._Codes

    @Codes.setter
    def Codes(self, Codes):
        self._Codes = Codes

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._Codes = params.get("Codes")
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceCodeUnlinkResponse(AbstractModel):
    """ModifyTraceCodeUnlink返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnlinkCnt: 成功解绑溯源码的数量
        :type UnlinkCnt: int
        :param _CodeCnt: 当前批次的码数量
        :type CodeCnt: int
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnlinkCnt = None
        self._CodeCnt = None
        self._BatchId = None
        self._RequestId = None

    @property
    def UnlinkCnt(self):
        return self._UnlinkCnt

    @UnlinkCnt.setter
    def UnlinkCnt(self, UnlinkCnt):
        self._UnlinkCnt = UnlinkCnt

    @property
    def CodeCnt(self):
        return self._CodeCnt

    @CodeCnt.setter
    def CodeCnt(self, CodeCnt):
        self._CodeCnt = CodeCnt

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UnlinkCnt = params.get("UnlinkCnt")
        self._CodeCnt = params.get("CodeCnt")
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class ModifyTraceDataRanksRequest(AbstractModel):
    """ModifyTraceDataRanks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _TaskId: 生产任务ID
        :type TaskId: str
        :param _TraceIds: 溯源ID
        :type TraceIds: list of str
        """
        self._CorpId = None
        self._BatchId = None
        self._TaskId = None
        self._TraceIds = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TraceIds(self):
        return self._TraceIds

    @TraceIds.setter
    def TraceIds(self, TraceIds):
        self._TraceIds = TraceIds


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        self._TraceIds = params.get("TraceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceDataRanksResponse(AbstractModel):
    """ModifyTraceDataRanks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class ModifyTraceDataRequest(AbstractModel):
    """ModifyTraceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _TaskId: 生产溯源任务ID
        :type TaskId: str
        :param _TraceItems: 溯源信息
        :type TraceItems: list of TraceItem
        :param _PhaseName: 溯源阶段名称
        :type PhaseName: str
        :param _PhaseData: 环节数据
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        :param _Status: 溯源状态 0: 无效, 1: 有效
        :type Status: int
        :param _Rank: 排序
        :type Rank: int
        :param _Type: [无效] 类型
        :type Type: int
        :param _Code: [无效] 溯源码
        :type Code: str
        :param _Phase: [无效] 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
        :type Phase: int
        :param _TraceTime: [无效] 溯源时间
        :type TraceTime: str
        :param _CreateTime: [无效] 创建时间
        :type CreateTime: str
        :param _ChainStatus: [无效] 上链状态
        :type ChainStatus: int
        :param _ChainTime: [无效] 上链时间
        :type ChainTime: str
        :param _ChainData: [无效] 上链数据
        :type ChainData: :class:`tencentcloud.trp.v20210515.models.ChainData`
        :param _CorpId: 企业ID
        :type CorpId: int
        """
        self._TraceId = None
        self._BatchId = None
        self._TaskId = None
        self._TraceItems = None
        self._PhaseName = None
        self._PhaseData = None
        self._Status = None
        self._Rank = None
        self._Type = None
        self._Code = None
        self._Phase = None
        self._TraceTime = None
        self._CreateTime = None
        self._ChainStatus = None
        self._ChainTime = None
        self._ChainData = None
        self._CorpId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TraceItems(self):
        return self._TraceItems

    @TraceItems.setter
    def TraceItems(self, TraceItems):
        self._TraceItems = TraceItems

    @property
    def PhaseName(self):
        return self._PhaseName

    @PhaseName.setter
    def PhaseName(self, PhaseName):
        self._PhaseName = PhaseName

    @property
    def PhaseData(self):
        return self._PhaseData

    @PhaseData.setter
    def PhaseData(self, PhaseData):
        self._PhaseData = PhaseData

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rank(self):
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def TraceTime(self):
        return self._TraceTime

    @TraceTime.setter
    def TraceTime(self, TraceTime):
        self._TraceTime = TraceTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChainStatus(self):
        return self._ChainStatus

    @ChainStatus.setter
    def ChainStatus(self, ChainStatus):
        self._ChainStatus = ChainStatus

    @property
    def ChainTime(self):
        return self._ChainTime

    @ChainTime.setter
    def ChainTime(self, ChainTime):
        self._ChainTime = ChainTime

    @property
    def ChainData(self):
        return self._ChainData

    @ChainData.setter
    def ChainData(self, ChainData):
        self._ChainData = ChainData

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        if params.get("TraceItems") is not None:
            self._TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self._TraceItems.append(obj)
        self._PhaseName = params.get("PhaseName")
        if params.get("PhaseData") is not None:
            self._PhaseData = PhaseData()
            self._PhaseData._deserialize(params.get("PhaseData"))
        self._Status = params.get("Status")
        self._Rank = params.get("Rank")
        self._Type = params.get("Type")
        self._Code = params.get("Code")
        self._Phase = params.get("Phase")
        self._TraceTime = params.get("TraceTime")
        self._CreateTime = params.get("CreateTime")
        self._ChainStatus = params.get("ChainStatus")
        self._ChainTime = params.get("ChainTime")
        if params.get("ChainData") is not None:
            self._ChainData = ChainData()
            self._ChainData._deserialize(params.get("ChainData"))
        self._CorpId = params.get("CorpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTraceDataResponse(AbstractModel):
    """ModifyTraceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._RequestId = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._RequestId = params.get("RequestId")


class OutputAuthorizedTransfer(AbstractModel):
    """业务出参

    """

    def __init__(self):
        r"""
        :param _Code: 推送状态，0表示成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Message: 错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Value: 错误信息描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackSpec(AbstractModel):
    """层级码配置

    """

    def __init__(self):
        r"""
        :param _Level: 层级
        :type Level: int
        :param _Rate: 比例
        :type Rate: int
        :param _Amount: 数量
        :type Amount: int
        :param _CustomId: 码规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomId: str
        :param _CodeParts: 码段配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeParts: list of CodePart
        """
        self._Level = None
        self._Rate = None
        self._Amount = None
        self._CustomId = None
        self._CodeParts = None

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def CustomId(self):
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def CodeParts(self):
        return self._CodeParts

    @CodeParts.setter
    def CodeParts(self, CodeParts):
        self._CodeParts = CodeParts


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Rate = params.get("Rate")
        self._Amount = params.get("Amount")
        self._CustomId = params.get("CustomId")
        if params.get("CodeParts") is not None:
            self._CodeParts = []
            for item in params.get("CodeParts"):
                obj = CodePart()
                obj._deserialize(item)
                self._CodeParts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhaseData(AbstractModel):
    """环节数据

    """

    def __init__(self):
        r"""
        :param _HeadEnabled: 启用头
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadEnabled: bool
        :param _HeadTitle: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadTitle: str
        :param _Key: 标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _AppId: 小程序AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _AppPath: 小程序AppPath
注意：此字段可能返回 null，表示取不到有效值。
        :type AppPath: str
        :param _AppName: 小程序名称AppName
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        """
        self._HeadEnabled = None
        self._HeadTitle = None
        self._Key = None
        self._AppId = None
        self._AppPath = None
        self._AppName = None

    @property
    def HeadEnabled(self):
        return self._HeadEnabled

    @HeadEnabled.setter
    def HeadEnabled(self, HeadEnabled):
        self._HeadEnabled = HeadEnabled

    @property
    def HeadTitle(self):
        return self._HeadTitle

    @HeadTitle.setter
    def HeadTitle(self, HeadTitle):
        self._HeadTitle = HeadTitle

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppPath(self):
        return self._AppPath

    @AppPath.setter
    def AppPath(self, AppPath):
        self._AppPath = AppPath

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._HeadEnabled = params.get("HeadEnabled")
        self._HeadTitle = params.get("HeadTitle")
        self._Key = params.get("Key")
        self._AppId = params.get("AppId")
        self._AppPath = params.get("AppPath")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanQRCode(AbstractModel):
    """安心计划二维码

    """

    def __init__(self):
        r"""
        :param _Url: 二维码
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Status: 状态，0:未激活 1:已激活 2:已冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Url = None
        self._Status = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanQRCodeRecord(AbstractModel):
    """安心计划二维码扫码记录

    """

    def __init__(self):
        r"""
        :param _Url: 二维码
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _OpenId: OpenID
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _ScanTime: 扫码时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTime: str
        :param _Ip: IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Country: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        """
        self._Url = None
        self._OpenId = None
        self._ScanTime = None
        self._Ip = None
        self._Country = None
        self._Province = None
        self._City = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def ScanTime(self):
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._OpenId = params.get("OpenId")
        self._ScanTime = params.get("ScanTime")
        self._Ip = params.get("Ip")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    """商品信息

    """

    def __init__(self):
        r"""
        :param _MerchantId: 商户标识码
        :type MerchantId: str
        :param _Name: 商品名称
        :type Name: str
        :param _ProductId: 商品id
        :type ProductId: str
        :param _CorpId: 企业id
        :type CorpId: int
        :param _ProductCode: 商品编号
        :type ProductCode: str
        :param _Specification: 商品规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Logo: 商品图片
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: list of str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _Ext: 预留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: :class:`tencentcloud.trp.v20210515.models.Ext`
        :param _MerchantName: 商户名称
        :type MerchantName: str
        :param _CertState: 认证状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        """
        self._MerchantId = None
        self._Name = None
        self._ProductId = None
        self._CorpId = None
        self._ProductCode = None
        self._Specification = None
        self._Remark = None
        self._Logo = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Ext = None
        self._MerchantName = None
        self._CertState = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._Name = params.get("Name")
        self._ProductId = params.get("ProductId")
        self._CorpId = params.get("CorpId")
        self._ProductCode = params.get("ProductCode")
        self._Specification = params.get("Specification")
        self._Remark = params.get("Remark")
        self._Logo = params.get("Logo")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Ext") is not None:
            self._Ext = Ext()
            self._Ext._deserialize(params.get("Ext"))
        self._MerchantName = params.get("MerchantName")
        self._CertState = params.get("CertState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """企业配额信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 服务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 服务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _QuotaId: 配额ID
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaId: int
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _Services: 开通服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of str
        :param _FactoryQuota: 商户配额
注意：此字段可能返回 null，表示取不到有效值。
        :type FactoryQuota: int
        :param _ItemQuota: 商品配额
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemQuota: int
        :param _TrackQuota: 溯源码配额
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackQuota: int
        :param _SaleQuota: 销售码配额
注意：此字段可能返回 null，表示取不到有效值。
        :type SaleQuota: int
        :param _ChainQuota: 上链配额
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainQuota: int
        :param _RiskQuota: 风控配额
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskQuota: int
        :param _AigcTextQuota: AI文字数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AigcTextQuota: int
        :param _AigcImageQuota: AI图片数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AigcImageQuota: int
        :param _TrackType: 溯源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackType: int
        :param _Version: 开通版本 lite:轻量版, basic:基础版, standard:标准版
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _ProductCertify: 是否开启企业认证
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCertify: int
        """
        self._StartTime = None
        self._EndTime = None
        self._QuotaId = None
        self._CorpId = None
        self._Services = None
        self._FactoryQuota = None
        self._ItemQuota = None
        self._TrackQuota = None
        self._SaleQuota = None
        self._ChainQuota = None
        self._RiskQuota = None
        self._AigcTextQuota = None
        self._AigcImageQuota = None
        self._TrackType = None
        self._Version = None
        self._ProductCertify = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QuotaId(self):
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def FactoryQuota(self):
        return self._FactoryQuota

    @FactoryQuota.setter
    def FactoryQuota(self, FactoryQuota):
        self._FactoryQuota = FactoryQuota

    @property
    def ItemQuota(self):
        return self._ItemQuota

    @ItemQuota.setter
    def ItemQuota(self, ItemQuota):
        self._ItemQuota = ItemQuota

    @property
    def TrackQuota(self):
        return self._TrackQuota

    @TrackQuota.setter
    def TrackQuota(self, TrackQuota):
        self._TrackQuota = TrackQuota

    @property
    def SaleQuota(self):
        return self._SaleQuota

    @SaleQuota.setter
    def SaleQuota(self, SaleQuota):
        self._SaleQuota = SaleQuota

    @property
    def ChainQuota(self):
        return self._ChainQuota

    @ChainQuota.setter
    def ChainQuota(self, ChainQuota):
        self._ChainQuota = ChainQuota

    @property
    def RiskQuota(self):
        return self._RiskQuota

    @RiskQuota.setter
    def RiskQuota(self, RiskQuota):
        self._RiskQuota = RiskQuota

    @property
    def AigcTextQuota(self):
        return self._AigcTextQuota

    @AigcTextQuota.setter
    def AigcTextQuota(self, AigcTextQuota):
        self._AigcTextQuota = AigcTextQuota

    @property
    def AigcImageQuota(self):
        return self._AigcImageQuota

    @AigcImageQuota.setter
    def AigcImageQuota(self, AigcImageQuota):
        self._AigcImageQuota = AigcImageQuota

    @property
    def TrackType(self):
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProductCertify(self):
        return self._ProductCertify

    @ProductCertify.setter
    def ProductCertify(self, ProductCertify):
        self._ProductCertify = ProductCertify


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QuotaId = params.get("QuotaId")
        self._CorpId = params.get("CorpId")
        self._Services = params.get("Services")
        self._FactoryQuota = params.get("FactoryQuota")
        self._ItemQuota = params.get("ItemQuota")
        self._TrackQuota = params.get("TrackQuota")
        self._SaleQuota = params.get("SaleQuota")
        self._ChainQuota = params.get("ChainQuota")
        self._RiskQuota = params.get("RiskQuota")
        self._AigcTextQuota = params.get("AigcTextQuota")
        self._AigcImageQuota = params.get("AigcImageQuota")
        self._TrackType = params.get("TrackType")
        self._Version = params.get("Version")
        self._ProductCertify = params.get("ProductCertify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawScanLog(AbstractModel):
    """原始扫码日志

    """

    def __init__(self):
        r"""
        :param _LogId: 日志ID
        :type LogId: int
        :param _Openid: 微信小程序openid
注意：此字段可能返回 null，表示取不到有效值。
        :type Openid: str
        :param _CreateTime: 扫码时间
        :type CreateTime: str
        :param _Code: 溯源码
        :type Code: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _MerchantId: 商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _City: 地市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _District: 区/县
注意：此字段可能返回 null，表示取不到有效值。
        :type District: str
        """
        self._LogId = None
        self._Openid = None
        self._CreateTime = None
        self._Code = None
        self._CorpId = None
        self._MerchantId = None
        self._ProductId = None
        self._BatchId = None
        self._Province = None
        self._City = None
        self._District = None

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._Openid = params.get("Openid")
        self._CreateTime = params.get("CreateTime")
        self._Code = params.get("Code")
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._BatchId = params.get("BatchId")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._District = params.get("District")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportBatchCallbackStatusRequest(AbstractModel):
    """ReportBatchCallbackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务加密入参。
        :type BusinessSecurityData: :class:`tencentcloud.trp.v20210515.models.InputEncryptData`
        """
        self._BusinessSecurityData = None

    @property
    def BusinessSecurityData(self):
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = InputEncryptData()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportBatchCallbackStatusResponse(AbstractModel):
    """ReportBatchCallbackStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参。
        :type Data: :class:`tencentcloud.trp.v20210515.models.OutputAuthorizedTransfer`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
            self._Data = OutputAuthorizedTransfer()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ScanLog(AbstractModel):
    """扫码明细

    """

    def __init__(self):
        r"""
        :param _LogId: 行ID
        :type LogId: int
        :param _Openid: 微信openid
注意：此字段可能返回 null，表示取不到有效值。
        :type Openid: str
        :param _Nickname: 微信昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nickname: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Code: 码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _MerchantId: 商户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantId: str
        :param _ProductId: 商品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Country: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _District: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: str
        :param _Unionid: 微信 unionid
注意：此字段可能返回 null，表示取不到有效值。
        :type Unionid: str
        :param _First: 首次扫码 0:否, 1:是
注意：此字段可能返回 null，表示取不到有效值。
        :type First: int
        :param _BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param _Type: 扫码类型 0:无效扫码 1: 小程序扫码 2: 商家扫码
        :type Type: int
        :param _MerchantName: 商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        """
        self._LogId = None
        self._Openid = None
        self._Nickname = None
        self._CreateTime = None
        self._Code = None
        self._CorpId = None
        self._MerchantId = None
        self._ProductId = None
        self._Ip = None
        self._Country = None
        self._Province = None
        self._City = None
        self._District = None
        self._Unionid = None
        self._First = None
        self._BatchId = None
        self._Type = None
        self._MerchantName = None
        self._ProductName = None

    @property
    def LogId(self):
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Unionid(self):
        return self._Unionid

    @Unionid.setter
    def Unionid(self, Unionid):
        self._Unionid = Unionid

    @property
    def First(self):
        return self._First

    @First.setter
    def First(self, First):
        self._First = First

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._Openid = params.get("Openid")
        self._Nickname = params.get("Nickname")
        self._CreateTime = params.get("CreateTime")
        self._Code = params.get("Code")
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._Ip = params.get("Ip")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Unionid = params.get("Unionid")
        self._First = params.get("First")
        self._BatchId = params.get("BatchId")
        self._Type = params.get("Type")
        self._MerchantName = params.get("MerchantName")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanStat(AbstractModel):
    """扫码统计

    """

    def __init__(self):
        r"""
        :param _Code: 安心码
        :type Code: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _MerchantId: 商户ID
        :type MerchantId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _Pv: 扫码次数
        :type Pv: int
        :param _Uv: 扫码人数
        :type Uv: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _MerchantName: 商户名称
        :type MerchantName: str
        :param _ProductName: 产品名称
        :type ProductName: str
        """
        self._Code = None
        self._CorpId = None
        self._MerchantId = None
        self._ProductId = None
        self._BatchId = None
        self._Pv = None
        self._Uv = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MerchantName = None
        self._ProductName = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def Pv(self):
        return self._Pv

    @Pv.setter
    def Pv(self, Pv):
        self._Pv = Pv

    @property
    def Uv(self):
        return self._Uv

    @Uv.setter
    def Uv(self, Uv):
        self._Uv = Uv

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CorpId = params.get("CorpId")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._BatchId = params.get("BatchId")
        self._Pv = params.get("Pv")
        self._Uv = params.get("Uv")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MerchantName = params.get("MerchantName")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceCode(AbstractModel):
    """溯源码

    """

    def __init__(self):
        r"""
        :param _Code: 二维码
        :type Code: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _PackId: 码包ID
        :type PackId: str
        :param _BatchId: 批次ID
        :type BatchId: str
        :param _MerchantId: 所属商户ID
        :type MerchantId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Status: 码状态 0: 冻结 1: 激活
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _MerchantName: 商户名称
        :type MerchantName: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _AgentId: 渠道商ID
        :type AgentId: int
        :param _Level: 码层级 0: 最小级, 1: 一级, 2: 二级
        :type Level: int
        """
        self._Code = None
        self._CorpId = None
        self._PackId = None
        self._BatchId = None
        self._MerchantId = None
        self._ProductId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MerchantName = None
        self._ProductName = None
        self._AgentId = None
        self._Level = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def PackId(self):
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MerchantName(self):
        return self._MerchantName

    @MerchantName.setter
    def MerchantName(self, MerchantName):
        self._MerchantName = MerchantName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CorpId = params.get("CorpId")
        self._PackId = params.get("PackId")
        self._BatchId = params.get("BatchId")
        self._MerchantId = params.get("MerchantId")
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MerchantName = params.get("MerchantName")
        self._ProductName = params.get("ProductName")
        self._AgentId = params.get("AgentId")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceData(AbstractModel):
    """溯源数据

    """

    def __init__(self):
        r"""
        :param _TraceId: 溯源ID
        :type TraceId: str
        :param _CorpId: 企业ID
        :type CorpId: int
        :param _Type: 码类型 0: 批次, 1: 码, 2: 生产任务
        :type Type: int
        :param _Code: 码值，跟码类型一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Rank: 排序，在Phase相同情况下，值越小排名靠前
        :type Rank: int
        :param _Phase: 溯源阶段 0:商品 1:通用 2:生产溯源 3:销售溯源
        :type Phase: int
        :param _PhaseName: 溯源环节名称
        :type PhaseName: str
        :param _TraceTime: 溯源时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ChainStatus: 上链状态 0: 未上链 1: 上链中 2: 已上链 -1: 异常
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainStatus: int
        :param _ChainTime: 上链时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainTime: str
        :param _ChainData: 上链数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainData: :class:`tencentcloud.trp.v20210515.models.ChainData`
        :param _PhaseData: 溯源阶段配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PhaseData: :class:`tencentcloud.trp.v20210515.models.PhaseData`
        :param _Status: 溯源阶段状态 0: 无效, 1: 有效
        :type Status: int
        :param _TraceItems: 无
        :type TraceItems: list of TraceItem
        """
        self._TraceId = None
        self._CorpId = None
        self._Type = None
        self._Code = None
        self._Rank = None
        self._Phase = None
        self._PhaseName = None
        self._TraceTime = None
        self._CreateTime = None
        self._ChainStatus = None
        self._ChainTime = None
        self._ChainData = None
        self._PhaseData = None
        self._Status = None
        self._TraceItems = None

    @property
    def TraceId(self):
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Rank(self):
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def PhaseName(self):
        return self._PhaseName

    @PhaseName.setter
    def PhaseName(self, PhaseName):
        self._PhaseName = PhaseName

    @property
    def TraceTime(self):
        return self._TraceTime

    @TraceTime.setter
    def TraceTime(self, TraceTime):
        self._TraceTime = TraceTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChainStatus(self):
        return self._ChainStatus

    @ChainStatus.setter
    def ChainStatus(self, ChainStatus):
        self._ChainStatus = ChainStatus

    @property
    def ChainTime(self):
        return self._ChainTime

    @ChainTime.setter
    def ChainTime(self, ChainTime):
        self._ChainTime = ChainTime

    @property
    def ChainData(self):
        return self._ChainData

    @ChainData.setter
    def ChainData(self, ChainData):
        self._ChainData = ChainData

    @property
    def PhaseData(self):
        return self._PhaseData

    @PhaseData.setter
    def PhaseData(self, PhaseData):
        self._PhaseData = PhaseData

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TraceItems(self):
        return self._TraceItems

    @TraceItems.setter
    def TraceItems(self, TraceItems):
        self._TraceItems = TraceItems


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._CorpId = params.get("CorpId")
        self._Type = params.get("Type")
        self._Code = params.get("Code")
        self._Rank = params.get("Rank")
        self._Phase = params.get("Phase")
        self._PhaseName = params.get("PhaseName")
        self._TraceTime = params.get("TraceTime")
        self._CreateTime = params.get("CreateTime")
        self._ChainStatus = params.get("ChainStatus")
        self._ChainTime = params.get("ChainTime")
        if params.get("ChainData") is not None:
            self._ChainData = ChainData()
            self._ChainData._deserialize(params.get("ChainData"))
        if params.get("PhaseData") is not None:
            self._PhaseData = PhaseData()
            self._PhaseData._deserialize(params.get("PhaseData"))
        self._Status = params.get("Status")
        if params.get("TraceItems") is not None:
            self._TraceItems = []
            for item in params.get("TraceItems"):
                obj = TraceItem()
                obj._deserialize(item)
                self._TraceItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceItem(AbstractModel):
    """溯源数据项 Type 的枚举值

    text:文本类型, longtext:长文本类型, banner:单图片类型, image:多图片类型, video:视频类型, mp:小程序类型

    具体组合如下
    - Type: "text" 文本类型, 对应值 Value: "文本字符串"
    - Type: "longtext" 长文本类型, 对应值 Value: "长文本字符串, 支持换行\n"
    - Type: "banner" 单图片类型, 对应图片地址 Value: "https://sample.cdn.com/xxx.jpg"
    - Type: "image" 多图片类型, 对应图片地址 Values: ["https://sample.cdn.com/1.jpg", "https://sample.cdn.com/2.jpg"]
    - Type: "video" 视频类型, 对应视频地址 Value: "https://sample.cdn.com/xxx.mp4"
    - Type: "mp" 小程序类型, 对应配置 Values: ["WXAPPID", "WXAPP_PATH", "跳转说明"]

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Value: 字段值
        :type Value: str
        :param _Type: 字段类型
text:文本类型, 
longtext:长文本类型, banner:单图片类型, image:多图片类型,
video:视频类型,
mp:小程序类型
        :type Type: str
        :param _Values: 多个值
        :type Values: list of str
        :param _ReadOnly: 只读
        :type ReadOnly: bool
        :param _Hidden: 扫码展示
        :type Hidden: bool
        :param _Key: 类型标识
        :type Key: str
        :param _Ext: 扩展字段
        :type Ext: str
        :param _Attrs: 额外属性
        :type Attrs: list of TraceItem
        :param _List: 子页面，只读
        :type List: list of TraceData
        """
        self._Name = None
        self._Value = None
        self._Type = None
        self._Values = None
        self._ReadOnly = None
        self._Hidden = None
        self._Key = None
        self._Ext = None
        self._Attrs = None
        self._List = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Hidden(self):
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext

    @property
    def Attrs(self):
        return self._Attrs

    @Attrs.setter
    def Attrs(self, Attrs):
        self._Attrs = Attrs

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        self._ReadOnly = params.get("ReadOnly")
        self._Hidden = params.get("Hidden")
        self._Key = params.get("Key")
        self._Ext = params.get("Ext")
        if params.get("Attrs") is not None:
            self._Attrs = []
            for item in params.get("Attrs"):
                obj = TraceItem()
                obj._deserialize(item)
                self._Attrs.append(obj)
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TraceData()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageQuota(AbstractModel):
    """付费信息使用量

    """

    def __init__(self):
        r"""
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: int
        :param _FactoryCnt: 商户配额
注意：此字段可能返回 null，表示取不到有效值。
        :type FactoryCnt: int
        :param _ItemCnt: 商品数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemCnt: int
        :param _TrackCnt: 溯源码量
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackCnt: int
        :param _SaleCnt: 营销码额度
注意：此字段可能返回 null，表示取不到有效值。
        :type SaleCnt: int
        :param _ChainCnt: 区块链上链次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChainCnt: int
        :param _RiskCnt: 营销风控次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCnt: int
        :param _UpdateTime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._CorpId = None
        self._FactoryCnt = None
        self._ItemCnt = None
        self._TrackCnt = None
        self._SaleCnt = None
        self._ChainCnt = None
        self._RiskCnt = None
        self._UpdateTime = None

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def FactoryCnt(self):
        return self._FactoryCnt

    @FactoryCnt.setter
    def FactoryCnt(self, FactoryCnt):
        self._FactoryCnt = FactoryCnt

    @property
    def ItemCnt(self):
        return self._ItemCnt

    @ItemCnt.setter
    def ItemCnt(self, ItemCnt):
        self._ItemCnt = ItemCnt

    @property
    def TrackCnt(self):
        return self._TrackCnt

    @TrackCnt.setter
    def TrackCnt(self, TrackCnt):
        self._TrackCnt = TrackCnt

    @property
    def SaleCnt(self):
        return self._SaleCnt

    @SaleCnt.setter
    def SaleCnt(self, SaleCnt):
        self._SaleCnt = SaleCnt

    @property
    def ChainCnt(self):
        return self._ChainCnt

    @ChainCnt.setter
    def ChainCnt(self, ChainCnt):
        self._ChainCnt = ChainCnt

    @property
    def RiskCnt(self):
        return self._RiskCnt

    @RiskCnt.setter
    def RiskCnt(self, RiskCnt):
        self._RiskCnt = RiskCnt

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._CorpId = params.get("CorpId")
        self._FactoryCnt = params.get("FactoryCnt")
        self._ItemCnt = params.get("ItemCnt")
        self._TrackCnt = params.get("TrackCnt")
        self._SaleCnt = params.get("SaleCnt")
        self._ChainCnt = params.get("ChainCnt")
        self._RiskCnt = params.get("RiskCnt")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        