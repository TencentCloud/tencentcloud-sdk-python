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


class Acct(AbstractModel):
    """账户信息

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctProperty: STRING(10)，见证子账户的属性（可重复。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctProperty: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctName: STRING(150)，见证子账户的名称（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param AcctAvailBal: STRING(20)，见证子账户可用余额（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctAvailBal: str
        :param CashAmt: STRING(20)，见证子账户可提现金额（可重复。开户日期或修改日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type CashAmt: str
        :param MaintenanceDate: STRING(8)，维护日期
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.TranNetMemberCode = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")


class ApplyWithdrawalRequest(AbstractModel):
    """ApplyWithdrawal请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctName: str
        :param CurrencyType: 币种 RMB
        :type CurrencyType: str
        :param CurrencyUnit: 单位，1：元，2：角，3：分
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
        :type CurrencyAmt: str
        :param TranWebName: 交易网名称
        :type TranWebName: str
        :param IdType: 会员证件类型
        :type IdType: str
        :param IdCode: 会员证件号码
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type IdCode: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.TranWebName = None
        self.IdType = None
        self.IdCode = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.TranWebName = params.get("TranWebName")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class ApplyWithdrawalResponse(AbstractModel):
    """ApplyWithdrawal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindAcctRequest(AbstractModel):
    """BindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1 – 小额转账验证
2 – 短信验证
每个结算账户每天只能使用一次小额转账验证
        :type BindType: int
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctName: str
        :param SettleAcctType: 1 – 本行账户
2 – 他行账户
        :type SettleAcctType: int
        :param IdType: 证件类型，见《证件类型》表
        :type IdType: str
        :param IdCode: 证件号码
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type IdCode: str
        :param AcctBranchName: 开户行名称
        :type AcctBranchName: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Mobile: str
        :param CnapsBranchId: 超级网银行号和大小额行号
二选一
        :type CnapsBranchId: str
        :param EiconBankBranchId: 超级网银行号和大小额行号
二选一
        :type EiconBankBranchId: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.SettleAcctType = None
        self.IdType = None
        self.IdCode = None
        self.AcctBranchName = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.SettleAcctType = params.get("SettleAcctType")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.AcctBranchName = params.get("AcctBranchName")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")


class BindAcctResponse(AbstractModel):
    """BindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRelateAccReUnionPayRequest(AbstractModel):
    """BindRelateAccReUnionPay请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）
        :type MemberAcctNo: str
        :param MessageCheckCode: STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）
        :type MessageCheckCode: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.MessageCheckCode = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.MessageCheckCode = params.get("MessageCheckCode")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAccReUnionPayResponse(AbstractModel):
    """BindRelateAccReUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class BindRelateAcctSmallAmountRequest(AbstractModel):
    """BindRelateAcctSmallAmount请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAcctSmallAmountResponse(AbstractModel):
    """BindRelateAcctSmallAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域（来账鉴权的方式下，此字段的值为客户需往监管账户转入的金额。在同名子账户绑定的场景下，若返回""VERIFIED""则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class BindRelateAcctUnionPayRequest(AbstractModel):
    """BindRelateAcctUnionPay请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.MrchCode = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAcctUnionPayResponse(AbstractModel):
    """BindRelateAcctUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param ReservedMsg: STRING(1027)，保留域（在同名子账户绑定的场景下，若返回"VERIFIED"则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAcctRequest(AbstractModel):
    """CheckAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1：小额鉴权
2：短信校验鉴权
        :type BindType: int
        :param SettleAcctNo: 结算账户账号
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CheckCode: 短信验证码
BindType==2必填
        :type CheckCode: str
        :param CurrencyType: 币种 RMB
BindType==1必填
        :type CurrencyType: str
        :param CurrencyUnit: 单位
1：元，2：角，3：分
BindType==1必填
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
BindType==1必填
        :type CurrencyAmt: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CheckCode = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CheckCode = params.get("CheckCode")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")


class CheckAcctResponse(AbstractModel):
    """CheckAcct返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: 前置流水号，请保存
        :type FrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAmountRequest(AbstractModel):
    """CheckAmount请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param TakeCashAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）
        :type TakeCashAcctNo: str
        :param AuthAmt: STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）
        :type AuthAmt: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param ReservedMsg: STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.TakeCashAcctNo = None
        self.AuthAmt = None
        self.Ccy = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.AuthAmt = params.get("AuthAmt")
        self.Ccy = params.get("Ccy")
        self.ReservedMsg = params.get("ReservedMsg")


class CheckAmountResponse(AbstractModel):
    """CheckAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ClearItem(AbstractModel):
    """银行在途清算结果信息

    """

    def __init__(self):
        """
        :param Date: STRING(8)，日期（格式: 20190101）
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param SubAcctType: STRING(40)，子账号类型（子帐号类型。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号; 7: 在途; 8: 理财购买子帐号; 9: 理财赎回子帐号; 10: 平台子拥有结算子帐号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctType: str
        :param ReconcileStatus: STRING(3)，对账状态（0: 成功; 1: 失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileStatus: str
        :param ReconcileReturnMsg: STRING(300)，对账返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileReturnMsg: str
        :param ClearingStatus: STRING(20)，清算状态（0: 成功; 1: 失败; 2: 异常; 3: 待处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingStatus: str
        :param ClearingReturnMsg: STRING(2)，清算返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingReturnMsg: str
        :param TotalAmt: STRING(300)，待清算总金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmt: str
        """
        self.Date = None
        self.SubAcctType = None
        self.ReconcileStatus = None
        self.ReconcileReturnMsg = None
        self.ClearingStatus = None
        self.ClearingReturnMsg = None
        self.TotalAmt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.SubAcctType = params.get("SubAcctType")
        self.ReconcileStatus = params.get("ReconcileStatus")
        self.ReconcileReturnMsg = params.get("ReconcileReturnMsg")
        self.ClearingStatus = params.get("ClearingStatus")
        self.ClearingReturnMsg = params.get("ClearingReturnMsg")
        self.TotalAmt = params.get("TotalAmt")


class CloseOrderRequest(AbstractModel):
    """CloseOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppid
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")


class CloseOrderResponse(AbstractModel):
    """CloseOrder返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAcctRequest(AbstractModel):
    """CreateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param Address: 子商户地址
        :type Address: str
        :param Contact: 子商户联系人
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Contact: str
        :param Mobile: 联系人手机号
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Email: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.SubMchName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubMchType = None
        self.ShortName = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.SubMchName = params.get("SubMchName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")


class CreateAcctResponse(AbstractModel):
    """CreateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubAcctNo: 平安银行生成的子商户账户
        :type SubAcctNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubAcctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.RequestId = params.get("RequestId")


class CreateCustAcctIdRequest(AbstractModel):
    """CreateCustAcctId请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionFlag: STRING(2)，功能标志（1: 开户; 3: 销户）
        :type FunctionFlag: str
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号（即收单资金归集入账的账号）
        :type FundSummaryAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）
        :type TranNetMemberCode: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）
        :type MemberProperty: str
        :param Mobile: STRING(30)，手机号码
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SelfBusiness: String(2)，是否为自营业务（0位非自营，1为自营）
        :type SelfBusiness: bool
        :param ContactName: String(64)，联系人
        :type ContactName: str
        :param SubAcctName: String(64)，子账户名称
        :type SubAcctName: str
        :param SubAcctShortName: String(64)，子账户简称
        :type SubAcctShortName: str
        :param SubAcctType: String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）
        :type SubAcctType: int
        :param UserNickname: STRING(150)，用户昵称
        :type UserNickname: str
        :param Email: STRING(150)，邮箱
        :type Email: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.FunctionFlag = None
        self.FundSummaryAcctNo = None
        self.TranNetMemberCode = None
        self.MemberProperty = None
        self.Mobile = None
        self.MrchCode = None
        self.SelfBusiness = None
        self.ContactName = None
        self.SubAcctName = None
        self.SubAcctShortName = None
        self.SubAcctType = None
        self.UserNickname = None
        self.Email = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.FunctionFlag = params.get("FunctionFlag")
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberProperty = params.get("MemberProperty")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.SelfBusiness = params.get("SelfBusiness")
        self.ContactName = params.get("ContactName")
        self.SubAcctName = params.get("SubAcctName")
        self.SubAcctShortName = params.get("SubAcctShortName")
        self.SubAcctType = params.get("SubAcctType")
        self.UserNickname = params.get("UserNickname")
        self.Email = params.get("Email")
        self.ReservedMsg = params.get("ReservedMsg")


class CreateCustAcctIdResponse(AbstractModel):
    """CreateCustAcctId返回参数结构体

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（平台需要记录下来，后续所有接口交互都会用到）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域（需要开通智能收款，此处返回智能收款账号，正常情况下返回空）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class DownloadBillRequest(AbstractModel):
    """DownloadBill请求参数结构体

    """

    def __init__(self):
        """
        :param StateDate: 请求下载对账单日期
        :type StateDate: str
        :param MidasAppId: 聚鑫分配的MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的SecretId
        :type MidasSecretId: str
        :param MidasSignature: 使用聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.StateDate = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.StateDate = params.get("StateDate")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class DownloadBillResponse(AbstractModel):
    """DownloadBill返回参数结构体

    """

    def __init__(self):
        """
        :param FileName: 账单文件名
        :type FileName: str
        :param FileMD5: 账单文件的MD5值
        :type FileMD5: str
        :param DownloadUrl: 账单文件的真实下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.FileMD5 = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileMD5 = params.get("FileMD5")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class FileItem(AbstractModel):
    """对账文件信息

    """

    def __init__(self):
        """
        :param FileName: STRING(256)，文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param RandomPassword: STRING(120)，随机密码
注意：此字段可能返回 null，表示取不到有效值。
        :type RandomPassword: str
        :param FilePath: STRING(512)，文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param DrawCode: STRING(64)，提取码
注意：此字段可能返回 null，表示取不到有效值。
        :type DrawCode: str
        """
        self.FileName = None
        self.RandomPassword = None
        self.FilePath = None
        self.DrawCode = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RandomPassword = params.get("RandomPassword")
        self.FilePath = params.get("FilePath")
        self.DrawCode = params.get("DrawCode")


class ModifyMntMbrBindRelateAcctBankCodeRequest(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberBindAcctNo: STRING(50)，会员绑定账号
        :type MemberBindAcctNo: str
        :param AcctOpenBranchName: STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，超级网银行号
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberBindAcctNo = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberBindAcctNo = params.get("MemberBindAcctNo")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class ModifyMntMbrBindRelateAcctBankCodeResponse(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBalanceRequest(AbstractModel):
    """QueryBalance请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param QueryFlag: 2：普通会员子账号
3：功能子账号
        :type QueryFlag: str
        :param PageOffset: 起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后
        :type PageOffset: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.QueryFlag = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.QueryFlag = params.get("QueryFlag")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryBalanceResponse(AbstractModel):
    """QueryBalance返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查询结果记录数
        :type ResultCount: str
        :param StartRecordOffset: 起始记录号
        :type StartRecordOffset: str
        :param EndFlag: 结束标志
        :type EndFlag: str
        :param TotalCount: 符合业务查询条件的记录总数
        :type TotalCount: str
        :param QueryItems: 查询结果项
        :type QueryItems: list of QueryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCount = None
        self.StartRecordOffset = None
        self.EndFlag = None
        self.TotalCount = None
        self.QueryItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.StartRecordOffset = params.get("StartRecordOffset")
        self.EndFlag = params.get("EndFlag")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryItems") is not None:
            self.QueryItems = []
            for item in params.get("QueryItems"):
                obj = QueryItem()
                obj._deserialize(item)
                self.QueryItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryBankClearRequest(AbstractModel):
    """QueryBankClear请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 全部; 2: 指定时间段）
        :type FunctionFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankClearResponse(AbstractModel):
    """QueryBankClear返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数, 一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of ClearItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = ClearItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankTransactionDetailsRequest(AbstractModel):
    """QueryBankTransactionDetails请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankTransactionDetailsResponse(AbstractModel):
    """QueryBankTransactionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransactionItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankWithdrawCashDetailsRequest(AbstractModel):
    """QueryBankWithdrawCashDetails请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（2: 提现; 3: 清分）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param BeginDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type BeginDate: str
        :param EndDate: STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.BeginDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankWithdrawCashDetailsResponse(AbstractModel):
    """QueryBankWithdrawCashDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0:否; 1:是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of WithdrawItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = WithdrawItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryCommonTransferRechargeRequest(AbstractModel):
    """QueryCommonTransferRecharge请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1为查询当日数据，0查询历史数据）
        :type FunctionFlag: str
        :param StartDate: STRING(8)，开始日期（格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（格式：20190101）
        :type EndDate: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.StartDate = None
        self.EndDate = None
        self.PageNum = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PageNum = params.get("PageNum")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCommonTransferRechargeResponse(AbstractModel):
    """QueryCommonTransferRecharge返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransferItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransferItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryCustAcctIdBalanceRequest(AbstractModel):
    """QueryCustAcctIdBalance请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCustAcctIdBalanceResponse(AbstractModel):
    """QueryCustAcctIdBalance返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param AcctArray: 账户信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctArray: list of Acct
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.AcctArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("AcctArray") is not None:
            self.AcctArray = []
            for item in params.get("AcctArray"):
                obj = Acct()
                obj._deserialize(item)
                self.AcctArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryItem(AbstractModel):
    """聚鑫商户余额查询输出项

    """

    def __init__(self):
        """
        :param SubAcctNo: 子商户账户
        :type SubAcctNo: str
        :param SubAcctProperty: 子账户属性 
1：普通会员子账号 
2：挂账子账号 
3：手续费子账号 
4：利息子账号
5：平台担保子账号
        :type SubAcctProperty: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubAcctName: 子账户名称
        :type SubAcctName: str
        :param AcctAvailBal: 账户可用余额
        :type AcctAvailBal: str
        :param CashAmt: 可提现金额
        :type CashAmt: str
        :param MaintenanceDate: 维护日期 开户日期或修改日期
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.SubMchId = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")


class QueryMemberBindRequest(AbstractModel):
    """QueryMemberBind请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）
        :type QueryFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryMemberBindResponse(AbstractModel):
    """QueryMemberBind返回参数结构体

    """

    def __init__(self):
        """
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TranItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TranItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class QueryMemberTransactionRequest(AbstractModel):
    """QueryMemberTransaction请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）
        :type FunctionFlag: str
        :param OutSubAcctNo: STRING(50)，转出方的见证子账户的账号（付款方）
        :type OutSubAcctNo: str
        :param OutMemberCode: STRING(32)，转出方的交易网会员代码
        :type OutMemberCode: str
        :param OutSubAcctName: STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type OutSubAcctName: str
        :param InSubAcctNo: STRING(50)，转入方的见证子账户的账号（收款方）
        :type InSubAcctNo: str
        :param InMemberCode: STRING(32)，转入方的交易网会员代码
        :type InMemberCode: str
        :param InSubAcctName: STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type InSubAcctName: str
        :param TranAmt: STRING(20)，交易金额
        :type TranAmt: str
        :param TranFee: STRING(20)，交易费用（平台收取交易费用）
        :type TranFee: str
        :param TranType: STRING(20)，交易类型（01: 普通交易）
        :type TranType: str
        :param Ccy: STRING(3)，币种（默认: RMB）
        :type Ccy: str
        :param OrderNo: STRING(50)，订单号（功能标志为1,2,3时必输）
        :type OrderNo: str
        :param OrderContent: STRING(500)，订单内容
        :type OrderContent: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名（若需短信验证码则此项必输）
        :type WebSign: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.OutSubAcctNo = None
        self.OutMemberCode = None
        self.OutSubAcctName = None
        self.InSubAcctNo = None
        self.InMemberCode = None
        self.InSubAcctName = None
        self.TranAmt = None
        self.TranFee = None
        self.TranType = None
        self.Ccy = None
        self.OrderNo = None
        self.OrderContent = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.OutMemberCode = params.get("OutMemberCode")
        self.OutSubAcctName = params.get("OutSubAcctName")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.InMemberCode = params.get("InMemberCode")
        self.InSubAcctName = params.get("InSubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.TranFee = params.get("TranFee")
        self.TranType = params.get("TranType")
        self.Ccy = params.get("Ccy")
        self.OrderNo = params.get("OrderNo")
        self.OrderContent = params.get("OrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")


class QueryMemberTransactionResponse(AbstractModel):
    """QueryMemberTransaction返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryOrderOutOrderList(AbstractModel):
    """查询订单接口的出参，订单列表

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param Amt: 支付金额，单位：分
        :type Amt: int
        :param UserId: 用户Id
        :type UserId: str
        :param CashAmt: 现金支付金额
        :type CashAmt: str
        :param Metadata: 发货标识，由业务在调用聚鑫下单 接口的时候下发
        :type Metadata: str
        :param PayTime: 支付时间unix时间戳
        :type PayTime: str
        :param CouponAmt: 抵扣券金额
        :type CouponAmt: str
        :param OrderTime: 下单时间unix时间戳
        :type OrderTime: str
        :param ProductId: 物品id
        :type ProductId: str
        :param SceneInfo: 高速场景信息
        :type SceneInfo: str
        :param OrderState: 当前订单的订单状态 
0：初始状态，获取聚鑫交易订单成功；  
1：拉起聚鑫支付页面成功，用户未 支付；
2：用户支付成功，正在发货；
3：用户支付成功，发货失败；
4：用户支付成功，发货成功；
5：聚鑫支付页面正在失效中；
6：聚鑫支付页面已经失效；
        :type OrderState: str
        :param Channel: 支付渠道：wechat：微信支付;
qqwallet：QQ钱包;
bank：网银
        :type Channel: str
        :param RefundFlag: 是否曾退款
        :type RefundFlag: str
        :param OutTradeNo: 务支付订单号
        :type OutTradeNo: str
        :param ProductName: 商品名称
        :type ProductName: str
        :param CallBackTime: 支付回调时间，unix时间戳
        :type CallBackTime: str
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param AcctSubAppId: 微校场景账户Id
        :type AcctSubAppId: str
        :param TransactionId: 调用下单接口获取的聚鑫交易订单
        :type TransactionId: str
        :param ChannelOrderId: 聚鑫内部渠道订单号
        :type ChannelOrderId: str
        :param SubOrderList: 调用下单接口传进来的 SubOutTradeNoList
        :type SubOrderList: list of QueryOrderOutSubOrderList
        :param ChannelExternalOrderId: 支付机构订单号
        :type ChannelExternalOrderId: str
        """
        self.MidasAppId = None
        self.Amt = None
        self.UserId = None
        self.CashAmt = None
        self.Metadata = None
        self.PayTime = None
        self.CouponAmt = None
        self.OrderTime = None
        self.ProductId = None
        self.SceneInfo = None
        self.OrderState = None
        self.Channel = None
        self.RefundFlag = None
        self.OutTradeNo = None
        self.ProductName = None
        self.CallBackTime = None
        self.CurrencyType = None
        self.AcctSubAppId = None
        self.TransactionId = None
        self.ChannelOrderId = None
        self.SubOrderList = None
        self.ChannelExternalOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.Amt = params.get("Amt")
        self.UserId = params.get("UserId")
        self.CashAmt = params.get("CashAmt")
        self.Metadata = params.get("Metadata")
        self.PayTime = params.get("PayTime")
        self.CouponAmt = params.get("CouponAmt")
        self.OrderTime = params.get("OrderTime")
        self.ProductId = params.get("ProductId")
        self.SceneInfo = params.get("SceneInfo")
        self.OrderState = params.get("OrderState")
        self.Channel = params.get("Channel")
        self.RefundFlag = params.get("RefundFlag")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductName = params.get("ProductName")
        self.CallBackTime = params.get("CallBackTime")
        self.CurrencyType = params.get("CurrencyType")
        self.AcctSubAppId = params.get("AcctSubAppId")
        self.TransactionId = params.get("TransactionId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = QueryOrderOutSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")


class QueryOrderOutSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        """
        :param Amt: 子订单支付金额
        :type Amt: int
        :param SubMchIncome: 子订单结算应收金额，单位：分
        :type SubMchIncome: int
        :param Metadata: 发货标识，由业务在调用Midas下单接口的时候下发。
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SettleCheck: 核销状态，1表示核销，0表示未核销
        :type SettleCheck: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        """
        self.Amt = None
        self.SubMchIncome = None
        self.Metadata = None
        self.OriginalAmt = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SettleCheck = None
        self.SubAppId = None
        self.SubOutTradeNo = None


    def _deserialize(self, params):
        self.Amt = params.get("Amt")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SettleCheck = params.get("SettleCheck")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")


class QueryOrderRequest(AbstractModel):
    """QueryOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主 MidasAppId
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param Type: type=by_order根据订单号 查订单；
type=by_user根据用户id 查订单 。
        :type Type: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Count: 每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填
        :type Count: int
        :param Offset: 记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填
        :type Offset: int
        :param StartTime: 查询开始时间，Unix时间戳。Type=by_order时必填
        :type StartTime: str
        :param EndTime: 查询结束时间，Unix时间戳。Type=by_order时必填
        :type EndTime: str
        :param OutTradeNo: 业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type TransactionId: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Type = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Count = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None
        self.OutTradeNo = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Count = params.get("Count")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")


class QueryOrderResponse(AbstractModel):
    """QueryOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 返回订单数
        :type TotalNum: int
        :param OrderList: 查询结果的订单列表
        :type OrderList: list of QueryOrderOutOrderList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.OrderList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("OrderList") is not None:
            self.OrderList = []
            for item in params.get("OrderList"):
                obj = QueryOrderOutOrderList()
                obj._deserialize(item)
                self.OrderList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryReconciliationDocumentRequest(AbstractModel):
    """QueryReconciliationDocument请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param FileType: STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）
        :type FileType: str
        :param FileDate: STRING(8)，文件日期（格式：20190101）
        :type FileDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FileType = None
        self.FileDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FileType = params.get("FileType")
        self.FileDate = params.get("FileDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryReconciliationDocumentResponse(AbstractModel):
    """QueryReconciliationDocument返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of FileItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = FileItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryRefundRequest(AbstractModel):
    """QueryRefund请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合。
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppid
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryRefundResponse(AbstractModel):
    """QueryRefund返回参数结构体

    """

    def __init__(self):
        """
        :param State: 退款状态码，退款提交成功后返回  1：退款中；  2：退款成功；  3：退款失败。
        :type State: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class QuerySingleTransactionStatusRequest(AbstractModel):
    """QuerySingleTransactionStatus请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）
        :type FunctionFlag: str
        :param TranNetSeqNo: STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）
        :type TranNetSeqNo: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号（未启用）
        :type SubAcctNo: str
        :param TranDate: STRING(8)，交易日期（未启用）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetSeqNo = None
        self.SubAcctNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetSeqNo = params.get("TranNetSeqNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySingleTransactionStatusResponse(AbstractModel):
    """QuerySingleTransactionStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param BookingFlag: STRING(2)，记账标志（记账标志。1: 登记挂账; 2: 支付; 3: 提现; 4: 清分; 5: 下单预支付; 6: 确认并付款; 7: 退款; 8: 支付到平台; N: 其他）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功; 1: 失败; 2: 待确认; 5: 待处理; 6: 处理中。0和1是终态，2、5、6是中间态，其中2是特指提现后待确认提现是否成功，5是银行收到交易等待处理，6是交易正在处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param InSubAcctNo: STRING(50)，转入子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param FailMsg: STRING(300)，失败信息（当提现失败时，返回交易失败原因）
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMsg: str
        :param OldTranFrontSeqNo: STRING(50)，原前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OldTranFrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.FailMsg = None
        self.OldTranFrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.FailMsg = params.get("FailMsg")
        self.OldTranFrontSeqNo = params.get("OldTranFrontSeqNo")
        self.RequestId = params.get("RequestId")


class QuerySmallAmountTransferRequest(AbstractModel):
    """QuerySmallAmountTransfer请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param OldTranSeqNo: STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）
        :type OldTranSeqNo: str
        :param TranDate: STRING(8)，交易日期（格式：20190101）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.OldTranSeqNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.OldTranSeqNo = params.get("OldTranSeqNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySmallAmountTransferResponse(AbstractModel):
    """QuerySmallAmountTransfer返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReturnStatus: STRING(10)，返回状态（0: 成功; 1: 失败; 2: 待确认）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnStatus: str
        :param ReturnMsg: STRING(512)，返回信息（失败返回具体信息）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReturnStatus = None
        self.ReturnMsg = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReturnStatus = params.get("ReturnStatus")
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RechargeMemberThirdPayRequest(AbstractModel):
    """RechargeMemberThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会代码
        :type TranNetMemberCode: str
        :param MemberFillAmt: STRING(20)，会员充值金额
        :type MemberFillAmt: str
        :param Commission: STRING(20)，手续费金额
        :type Commission: str
        :param Ccy: STRING(3)，币种
        :type Ccy: str
        :param PayChannelType: STRING(20)，支付渠道类型
        :type PayChannelType: str
        :param PayChannelAssignMerNo: STRING(50)，支付渠道所分配的商户号
        :type PayChannelAssignMerNo: str
        :param PayChannelTranSeqNo: STRING(52)，支付渠道交易流水号
        :type PayChannelTranSeqNo: str
        :param EjzbOrderNo: STRING(52)，电商见证宝订单号
        :type EjzbOrderNo: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param EjzbOrderContent: STRING(500)，电商见证宝订单内容
        :type EjzbOrderContent: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.TranNetMemberCode = None
        self.MemberFillAmt = None
        self.Commission = None
        self.Ccy = None
        self.PayChannelType = None
        self.PayChannelAssignMerNo = None
        self.PayChannelTranSeqNo = None
        self.EjzbOrderNo = None
        self.MrchCode = None
        self.EjzbOrderContent = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberFillAmt = params.get("MemberFillAmt")
        self.Commission = params.get("Commission")
        self.Ccy = params.get("Ccy")
        self.PayChannelType = params.get("PayChannelType")
        self.PayChannelAssignMerNo = params.get("PayChannelAssignMerNo")
        self.PayChannelTranSeqNo = params.get("PayChannelTranSeqNo")
        self.EjzbOrderNo = params.get("EjzbOrderNo")
        self.MrchCode = params.get("MrchCode")
        self.EjzbOrderContent = params.get("EjzbOrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RechargeMemberThirdPayResponse(AbstractModel):
    """RechargeMemberThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param MemberSubAcctPreAvailBal: STRING(20)，会员子账户交易前可用余额
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberSubAcctPreAvailBal: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.MemberSubAcctPreAvailBal = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.MemberSubAcctPreAvailBal = params.get("MemberSubAcctPreAvailBal")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RefundOutSubOrderRefundList(AbstractModel):
    """退款子订单列表

    """

    def __init__(self):
        """
        :param PlatformRefundAmt: 平台应退金额
        :type PlatformRefundAmt: int
        :param RefundAmt: 子订单退款金额
        :type RefundAmt: int
        :param SubMchRefundAmt: 商家应退金额
        :type SubMchRefundAmt: int
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param SubRefundId: 子退款单号，调用方需要保证 全局唯一性
        :type SubRefundId: str
        """
        self.PlatformRefundAmt = None
        self.RefundAmt = None
        self.SubMchRefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None


    def _deserialize(self, params):
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.RefundAmt = params.get("RefundAmt")
        self.SubMchRefundAmt = params.get("SubMchRefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")


class RefundRequest(AbstractModel):
    """Refund请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户Id，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppid
        :type MidasAppId: str
        :param TotalRefundAmt: 退款金额，单位：分。备 注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额做为退款金额
        :type TotalRefundAmt: int
        :param SubOrderRefundList: 支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算 出来总和。
        :type SubOrderRefundList: list of RefundOutSubOrderRefundList
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param MchRefundAmt: 结算应收金额，单位：分
        :type MchRefundAmt: int
        :param TransactionId: 调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        :param PlatformRefundAmt: 平台应收金额，单位：分
        :type PlatformRefundAmt: int
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.TotalRefundAmt = None
        self.SubOrderRefundList = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.MchRefundAmt = None
        self.TransactionId = None
        self.PlatformRefundAmt = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        if params.get("SubOrderRefundList") is not None:
            self.SubOrderRefundList = []
            for item in params.get("SubOrderRefundList"):
                obj = RefundOutSubOrderRefundList()
                obj._deserialize(item)
                self.SubOrderRefundList.append(obj)
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MchRefundAmt = params.get("MchRefundAmt")
        self.TransactionId = params.get("TransactionId")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")


class RefundResponse(AbstractModel):
    """Refund返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterBillSupportWithdrawRequest(AbstractModel):
    """RegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OrderNo: STRING(50)，订单号
        :type OrderNo: str
        :param SuspendAmt: STRING(20)，挂账金额（包含交易费用）
        :type SuspendAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.TranNetMemberCode = None
        self.OrderNo = None
        self.SuspendAmt = None
        self.TranFee = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OrderNo = params.get("OrderNo")
        self.SuspendAmt = params.get("SuspendAmt")
        self.TranFee = params.get("TranFee")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RegisterBillSupportWithdrawResponse(AbstractModel):
    """RegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param CnsmrSeqNo: String(22)，交易流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.FrontSeqNo = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevRegisterBillSupportWithdrawRequest(AbstractModel):
    """RevRegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OldOrderNo = params.get("OldOrderNo")
        self.CancelAmt = params.get("CancelAmt")
        self.TranFee = params.get("TranFee")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RevRegisterBillSupportWithdrawResponse(AbstractModel):
    """RevRegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ReviseMbrPropertyRequest(AbstractModel):
    """ReviseMbrProperty请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）
        :type MemberProperty: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberProperty = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberProperty = params.get("MemberProperty")
        self.ReservedMsg = params.get("ReservedMsg")


class ReviseMbrPropertyResponse(AbstractModel):
    """ReviseMbrProperty返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevokeMemberRechargeThirdPayRequest(AbstractModel):
    """RevokeMemberRechargeThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param OldFillFrontSeqNo: STRING(52)，原充值的前置流水号
        :type OldFillFrontSeqNo: str
        :param OldFillPayChannelType: STRING(20)，原充值的支付渠道类型
        :type OldFillPayChannelType: str
        :param OldPayChannelTranSeqNo: STRING(52)，原充值的支付渠道交易流水号
        :type OldPayChannelTranSeqNo: str
        :param OldFillEjzbOrderNo: STRING(52)，原充值的电商见证宝订单号
        :type OldFillEjzbOrderNo: str
        :param ApplyCancelMemberAmt: STRING(20)，申请撤销的会员金额
        :type ApplyCancelMemberAmt: str
        :param ApplyCancelCommission: STRING(20)，申请撤销的手续费金额
        :type ApplyCancelCommission: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.OldFillFrontSeqNo = None
        self.OldFillPayChannelType = None
        self.OldPayChannelTranSeqNo = None
        self.OldFillEjzbOrderNo = None
        self.ApplyCancelMemberAmt = None
        self.ApplyCancelCommission = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.OldFillFrontSeqNo = params.get("OldFillFrontSeqNo")
        self.OldFillPayChannelType = params.get("OldFillPayChannelType")
        self.OldPayChannelTranSeqNo = params.get("OldPayChannelTranSeqNo")
        self.OldFillEjzbOrderNo = params.get("OldFillEjzbOrderNo")
        self.ApplyCancelMemberAmt = params.get("ApplyCancelMemberAmt")
        self.ApplyCancelCommission = params.get("ApplyCancelCommission")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RevokeMemberRechargeThirdPayResponse(AbstractModel):
    """RevokeMemberRechargeThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class TranItem(AbstractModel):
    """交易信息

    """

    def __init__(self):
        """
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号
注意：此字段可能返回 null，表示取不到有效值。
        :type FundSummaryAcctNo: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员绑定账户的账号（提现的银行卡）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员绑定账户的本他行类型（1: 本行; 2: 他行）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员绑定账户的开户行名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，会员绑定账户的开户行的联行号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员绑定账户的开户行的超级网银行号
注意：此字段可能返回 null，表示取不到有效值。
        :type EiconBankBranchId: str
        :param Mobile: STRING(30)，会员的手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.FundSummaryAcctNo = None
        self.SubAcctNo = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.Mobile = None


    def _deserialize(self, params):
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.Mobile = params.get("Mobile")


class TransactionItem(AbstractModel):
    """交易明细信息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，记账标志（1: 转出; 2: 转入）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param BookingType: STRING(20)，记账类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingType: str
        :param InSubAcctNo: STRING(50)，转入见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param Remark: STRING(300)，备注（返回交易订单号）
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.BookingType = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.BookingType = params.get("BookingType")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.Remark = params.get("Remark")


class TransferItem(AbstractModel):
    """转账充值明细信息

    """

    def __init__(self):
        """
        :param InAcctType: STRING(10)，入账类型（02: 会员充值; 03: 资金挂账）
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctType: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranAmt: STRING(20)，入金金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param InAcctNo: STRING(50)，入金账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctNo: str
        :param InAcctName: STRING(150)，入金账户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctName: str
        :param Ccy: STRING(3)，币种
注意：此字段可能返回 null，表示取不到有效值。
        :type Ccy: str
        :param AccountingDate: STRING(8)，会计日期（即银行主机记账日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountingDate: str
        :param BankName: STRING(150)，银行名称（付款账户银行名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankName: str
        :param Remark: STRING(300)，转账备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        """
        self.InAcctType = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.TranAmt = None
        self.InAcctNo = None
        self.InAcctName = None
        self.Ccy = None
        self.AccountingDate = None
        self.BankName = None
        self.Remark = None
        self.FrontSeqNo = None


    def _deserialize(self, params):
        self.InAcctType = params.get("InAcctType")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranAmt = params.get("TranAmt")
        self.InAcctNo = params.get("InAcctNo")
        self.InAcctName = params.get("InAcctName")
        self.Ccy = params.get("Ccy")
        self.AccountingDate = params.get("AccountingDate")
        self.BankName = params.get("BankName")
        self.Remark = params.get("Remark")
        self.FrontSeqNo = params.get("FrontSeqNo")


class UnBindAcctRequest(AbstractModel):
    """UnBindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class UnBindAcctResponse(AbstractModel):
    """UnBindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindRelateAcctRequest(AbstractModel):
    """UnbindRelateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 解绑）
        :type FunctionFlag: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，待解绑的提现账户的账号（提现账号）
        :type MemberAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class UnbindRelateAcctResponse(AbstractModel):
    """UnbindRelateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class UnifiedOrderInSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        """
        :param SubMchIncome: 子订单结算应收金额，单位： 分
        :type SubMchIncome: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param Amt: 子订单支付金额
        :type Amt: int
        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.Metadata = None
        self.OriginalAmt = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")


class UnifiedOrderRequest(AbstractModel):
    """UnifiedOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppid
        :type MidasAppId: str
        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutTradeNo: str
        :param ProductDetail: 商品详情，需要URL编码
        :type ProductDetail: str
        :param ProductId: 商品id，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type ProductId: str
        :param ProductName: 商品名称，需要URL编码
        :type ProductName: str
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RealChannel: 银行真实渠道.如:bank_ccb
        :type RealChannel: str
        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用Id、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
        :type SubOrderList: list of UnifiedOrderInSubOrderList
        :param OriginalAmt: 原始金额
        :type OriginalAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CallbackUrl: Web端回调地址
        :type CallbackUrl: str
        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容
        :type Metadata: str
        :param Quantity: 购买数量，不传默认为1
        :type Quantity: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param TotalMchIncome: 结算应收金额，单位：分
        :type TotalMchIncome: int
        :param TotalPlatformIncome: 平台应收金额，单位：分
        :type TotalPlatformIncome: int
        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid
        :type WxOpenId: str
        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一
        :type WxSubOpenId: str
        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.SubOrderList = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = UnifiedOrderInSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")


class UnifiedOrderResponse(AbstractModel):
    """UnifiedOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param OutTradeNo: 应用支付订单号
        :type OutTradeNo: str
        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）
        :type PayInfo: str
        :param TransactionId: 聚鑫的交易订单
        :type TransactionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.RequestId = params.get("RequestId")


class WithdrawCashMembershipRequest(AbstractModel):
    """WithdrawCashMembership请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranWebName: STRING(150)，交易网名称（市场名称）
        :type TranWebName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
        :type MemberName: str
        :param TakeCashAcctNo: STRING(50)，提现账号（银行卡）
        :type TakeCashAcctNo: str
        :param OutAmtAcctName: STRING(150)，出金账户名称（银行卡户名）
        :type OutAmtAcctName: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param CashAmt: STRING(20)，可提现金额
        :type CashAmt: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名
        :type WebSign: str
        """
        self.MrchCode = None
        self.TranWebName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.TakeCashAcctNo = None
        self.OutAmtAcctName = None
        self.Ccy = None
        self.CashAmt = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranWebName = params.get("TranWebName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.OutAmtAcctName = params.get("OutAmtAcctName")
        self.Ccy = params.get("Ccy")
        self.CashAmt = params.get("CashAmt")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")


class WithdrawCashMembershipResponse(AbstractModel):
    """WithdrawCashMembership返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param TransferFee: STRING(20)，转账手续费（固定返回0.00）
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFee: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.TransferFee = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.TransferFee = params.get("TransferFee")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class WithdrawItem(AbstractModel):
    """清分提现明细信息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，记账标志（01: 提现; 02: 清分 ）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param BookingMsg: STRING(200)，记账说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingMsg: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctName: STRING(150)，见证子账户的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param Commission: STRING(20)，手续费
注意：此字段可能返回 null，表示取不到有效值。
        :type Commission: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param Remark: STRING(300)，备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.BookingMsg = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.SubAcctName = None
        self.TranAmt = None
        self.Commission = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.BookingMsg = params.get("BookingMsg")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctName = params.get("SubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.Commission = params.get("Commission")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.Remark = params.get("Remark")