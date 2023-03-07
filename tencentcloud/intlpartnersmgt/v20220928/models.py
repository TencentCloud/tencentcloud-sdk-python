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


class AllocateCustomerCreditRequest(AbstractModel):
    """AllocateCustomerCredit请求参数结构体

    """

    def __init__(self):
        r"""
        :param AddedCredit: 分配客户信用的具体值
        :type AddedCredit: float
        :param ClientUin: 客户uin
        :type ClientUin: int
        """
        self.AddedCredit = None
        self.ClientUin = None


    def _deserialize(self, params):
        self.AddedCredit = params.get("AddedCredit")
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCustomerCreditResponse(AbstractModel):
    """AllocateCustomerCredit返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCredit: 更新后的信用总额
        :type TotalCredit: float
        :param RemainingCredit: 更新后的信用余额
        :type RemainingCredit: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCredit = None
        self.RemainingCredit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCredit = params.get("TotalCredit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.RequestId = params.get("RequestId")


class CountryCodeItem(AbstractModel):
    """获取国家码接口的一个元素类型

    """

    def __init__(self):
        r"""
        :param EnName: 国家英文名
        :type EnName: str
        :param Name: 国家中文名
        :type Name: str
        :param IOS2: ISO2标准国家/地区代码
        :type IOS2: str
        :param IOS3: ISO3标准国家/地区代码
        :type IOS3: str
        :param Code: 电话代码
        :type Code: str
        """
        self.EnName = None
        self.Name = None
        self.IOS2 = None
        self.IOS3 = None
        self.Code = None


    def _deserialize(self, params):
        self.EnName = params.get("EnName")
        self.Name = params.get("Name")
        self.IOS2 = params.get("IOS2")
        self.IOS3 = params.get("IOS3")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccountType: 新建客户的账户类型标识。本接口取值为：personal或company
        :type AccountType: str
        :param Mail: 注册邮件地址。需要调用方保证邮件地址的有效性和正确性。
需要满足邮件的格式。如：account@qq.com
        :type Mail: str
        :param Password: 账户密码。
长度限制：[8,20]。
需同时包含数字、字母以及特殊符号（!@#$%^&*()等非空格）
        :type Password: str
        :param ConfirmPassword: 二次确认密码。必须和Password值相同
        :type ConfirmPassword: str
        :param PhoneNum: 客户手机号码。需要调用方保证手机号码的有效性和正确性。
长度限制：[1,32]。支持全球手机号。如18888888888
        :type PhoneNum: str
        :param CountryCode: 客户的国家/地区代码。取值参考获取国家/地区码接口GetCountryCodes。如852
        :type CountryCode: str
        :param Area: 客户的IOS2标准国家/地区代码。参考获取国家/地区码接口GetCountryCodes。需要与CountryCode值对应。如HK
        :type Area: str
        :param Extended: 拓展字段，默认为空
        :type Extended: str
        """
        self.AccountType = None
        self.Mail = None
        self.Password = None
        self.ConfirmPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Area = None
        self.Extended = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Mail = params.get("Mail")
        self.Password = params.get("Password")
        self.ConfirmPassword = params.get("ConfirmPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Area = params.get("Area")
        self.Extended = params.get("Extended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 账号的uin
        :type Uin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetCountryCodesRequest(AbstractModel):
    """GetCountryCodes请求参数结构体

    """


class GetCountryCodesResponse(AbstractModel):
    """GetCountryCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 国家地区代码列表
        :type Data: list of CountryCodeItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CountryCodeItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCreditAllocationHistoryData(AbstractModel):
    """查询子客授信历史记录返回信息

    """

    def __init__(self):
        r"""
        :param AllocatedTime: 分配时间
        :type AllocatedTime: str
        :param Operator: 操作员
        :type Operator: str
        :param Credit: 分配的信用值
        :type Credit: float
        :param AllocatedCredit: 分配的总金额
        :type AllocatedCredit: float
        """
        self.AllocatedTime = None
        self.Operator = None
        self.Credit = None
        self.AllocatedCredit = None


    def _deserialize(self, params):
        self.AllocatedTime = params.get("AllocatedTime")
        self.Operator = params.get("Operator")
        self.Credit = params.get("Credit")
        self.AllocatedCredit = params.get("AllocatedCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryRequest(AbstractModel):
    """QueryCreditAllocationHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClientUin: 客户uin
        :type ClientUin: int
        :param Page: 翻页参数，所在页数
        :type Page: int
        :param PageSize: 翻页参数，每页数据量
        :type PageSize: int
        """
        self.ClientUin = None
        self.Page = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.Page = params.get("Page")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryResponse(AbstractModel):
    """QueryCreditAllocationHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 历史信息总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param History: 历史信息详细列表数据
注意：此字段可能返回 null，表示取不到有效值。
        :type History: list of QueryCreditAllocationHistoryData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.History = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = QueryCreditAllocationHistoryData()
                obj._deserialize(item)
                self.History.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCreditByUinListRequest(AbstractModel):
    """QueryCreditByUinList请求参数结构体

    """

    def __init__(self):
        r"""
        :param UinList: 用户列表
        :type UinList: list of int non-negative
        """
        self.UinList = None


    def _deserialize(self, params):
        self.UinList = params.get("UinList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditByUinListResponse(AbstractModel):
    """QueryCreditByUinList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 用户信息列表
        :type Data: list of QueryDirectCustomersCreditData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCustomersCreditData(AbstractModel):
    """查询客户信用额度出参复杂类型

    """

    def __init__(self):
        r"""
        :param Name: 名字
        :type Name: str
        :param Type: 类型
        :type Type: str
        :param Mobile: 电话
        :type Mobile: str
        :param Email: 邮箱
        :type Email: str
        :param Arrears: 欠费标记
        :type Arrears: str
        :param AssociationTime: 绑定时间
        :type AssociationTime: str
        :param RecentExpiry: 最近到期时间
        :type RecentExpiry: str
        :param ClientUin: 子客uin
        :type ClientUin: int
        :param Credit: 子客授信额度
        :type Credit: float
        :param RemainingCredit: 子客剩余额度
        :type RemainingCredit: float
        :param IdentifyType: 0：未实名 1: 个人实名 2：企业实名
        :type IdentifyType: int
        :param Remark: 客户备注
        :type Remark: str
        :param Force: 强制状态
        :type Force: int
        """
        self.Name = None
        self.Type = None
        self.Mobile = None
        self.Email = None
        self.Arrears = None
        self.AssociationTime = None
        self.RecentExpiry = None
        self.ClientUin = None
        self.Credit = None
        self.RemainingCredit = None
        self.IdentifyType = None
        self.Remark = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.Arrears = params.get("Arrears")
        self.AssociationTime = params.get("AssociationTime")
        self.RecentExpiry = params.get("RecentExpiry")
        self.ClientUin = params.get("ClientUin")
        self.Credit = params.get("Credit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.IdentifyType = params.get("IdentifyType")
        self.Remark = params.get("Remark")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditRequest(AbstractModel):
    """QueryCustomersCredit请求参数结构体

    """

    def __init__(self):
        r"""
        :param FilterType: 搜索条件类型，只能是：ClientUin|Name|Remark|Email四选一
        :type FilterType: str
        :param Filter: 查询条件值
        :type Filter: str
        :param Page: 分页参数：当前页数，从1开始
        :type Page: int
        :param PageSize: 分页参数：每页条数
        :type PageSize: int
        :param Order: 排序参数，根据AssociationTime按照空或者desc：逆序，asc：顺序的方式进行排序
        :type Order: str
        """
        self.FilterType = None
        self.Filter = None
        self.Page = None
        self.PageSize = None
        self.Order = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Filter = params.get("Filter")
        self.Page = params.get("Page")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditResponse(AbstractModel):
    """QueryCustomersCredit返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 查询客户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of QueryCustomersCreditData
        :param Total: 客户数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryCustomersCreditData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class QueryDirectCustomersCreditData(AbstractModel):
    """直接子客信用信息

    """

    def __init__(self):
        r"""
        :param Uin: 用户Uin
        :type Uin: int
        :param TotalCredit: 总信用值
        :type TotalCredit: float
        :param RemainingCredit: 剩余信用值
        :type RemainingCredit: float
        """
        self.Uin = None
        self.TotalCredit = None
        self.RemainingCredit = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.TotalCredit = params.get("TotalCredit")
        self.RemainingCredit = params.get("RemainingCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDirectCustomersCreditRequest(AbstractModel):
    """QueryDirectCustomersCredit请求参数结构体

    """


class QueryDirectCustomersCreditResponse(AbstractModel):
    """QueryDirectCustomersCredit返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 直接子客信息列表
        :type Data: list of QueryDirectCustomersCreditData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryDirectCustomersCreditData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryPartnerCreditRequest(AbstractModel):
    """QueryPartnerCredit请求参数结构体

    """


class QueryPartnerCreditResponse(AbstractModel):
    """QueryPartnerCredit返回参数结构体

    """

    def __init__(self):
        r"""
        :param AllocatedCredit: 已分配额度
        :type AllocatedCredit: float
        :param TotalCredit: 额度总数
        :type TotalCredit: float
        :param RemainingCredit: 剩余额度
        :type RemainingCredit: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllocatedCredit = None
        self.TotalCredit = None
        self.RemainingCredit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllocatedCredit = params.get("AllocatedCredit")
        self.TotalCredit = params.get("TotalCredit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.RequestId = params.get("RequestId")


class QueryVoucherAmountByUinItem(AbstractModel):
    """子客代金券额度

    """

    def __init__(self):
        r"""
        :param ClientUin: 子客uin
        :type ClientUin: int
        :param TotalAmount: 代金券额度
        :type TotalAmount: float
        :param RemainAmount: 代金券余额
        :type RemainAmount: float
        """
        self.ClientUin = None
        self.TotalAmount = None
        self.RemainAmount = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.TotalAmount = params.get("TotalAmount")
        self.RemainAmount = params.get("RemainAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherAmountByUinRequest(AbstractModel):
    """QueryVoucherAmountByUin请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClientUins: 子客uin列表
        :type ClientUins: list of int non-negative
        """
        self.ClientUins = None


    def _deserialize(self, params):
        self.ClientUins = params.get("ClientUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherAmountByUinResponse(AbstractModel):
    """QueryVoucherAmountByUin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 子客代金券额度数据
        :type Data: list of QueryVoucherAmountByUinItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryVoucherAmountByUinItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryVoucherListByUinItem(AbstractModel):
    """单个客户代金券数据

    """

    def __init__(self):
        r"""
        :param ClientUin: 子客uin
        :type ClientUin: int
        :param TotalCount: 券总数量
        :type TotalCount: int
        :param Data: 券详情
        :type Data: list of QueryVoucherListByUinVoucherItem
        """
        self.ClientUin = None
        self.TotalCount = None
        self.Data = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryVoucherListByUinVoucherItem()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherListByUinRequest(AbstractModel):
    """QueryVoucherListByUin请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClientUins: 子客uin列表
        :type ClientUins: list of int non-negative
        :param Status: 状态，不传时默认查询所有状态。Unused,Used,Expired
        :type Status: str
        """
        self.ClientUins = None
        self.Status = None


    def _deserialize(self, params):
        self.ClientUins = params.get("ClientUins")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherListByUinResponse(AbstractModel):
    """QueryVoucherListByUin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 子客代金券数据
        :type Data: list of QueryVoucherListByUinItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryVoucherListByUinItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryVoucherListByUinVoucherItem(AbstractModel):
    """子客代金券数据

    """

    def __init__(self):
        r"""
        :param VoucherId: 券号
        :type VoucherId: str
        :param VoucherStatus: 状态
        :type VoucherStatus: str
        :param TotalAmount: 面额
        :type TotalAmount: float
        :param RemainAmount: 余额
        :type RemainAmount: float
        """
        self.VoucherId = None
        self.VoucherStatus = None
        self.TotalAmount = None
        self.RemainAmount = None


    def _deserialize(self, params):
        self.VoucherId = params.get("VoucherId")
        self.VoucherStatus = params.get("VoucherStatus")
        self.TotalAmount = params.get("TotalAmount")
        self.RemainAmount = params.get("RemainAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVoucherPoolRequest(AbstractModel):
    """QueryVoucherPool请求参数结构体

    """


class QueryVoucherPoolResponse(AbstractModel):
    """QueryVoucherPool返回参数结构体

    """

    def __init__(self):
        r"""
        :param AgentName: 经销商姓名
        :type AgentName: str
        :param AccountType: 经销商角色类型：1:经销商 2:总经销商 3:二级经销商
        :type AccountType: int
        :param TotalQuota: 总额度
        :type TotalQuota: float
        :param RemainingQuota: 剩余额度
        :type RemainingQuota: float
        :param IssuedNum: 已发放的代金券数量
        :type IssuedNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AgentName = None
        self.AccountType = None
        self.TotalQuota = None
        self.RemainingQuota = None
        self.IssuedNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AgentName = params.get("AgentName")
        self.AccountType = params.get("AccountType")
        self.TotalQuota = params.get("TotalQuota")
        self.RemainingQuota = params.get("RemainingQuota")
        self.IssuedNum = params.get("IssuedNum")
        self.RequestId = params.get("RequestId")