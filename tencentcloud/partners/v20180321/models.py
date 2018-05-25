# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class AgentBillElem(AbstractModel):
    """业务信息定义

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID
        :type Uin: str
        :param OrderId: 订单号，仅对预付费账单有意义
        :type OrderId: str
        :param ClientUin: 代客账号ID
        :type ClientUin: str
        :param ClientRemark: 代客备注名称
        :type ClientRemark: str
        :param PayTime: 支付时间
        :type PayTime: str
        :param GoodsType: 云产品名称
        :type GoodsType: str
        :param PayMode: 预付费/后付费
        :type PayMode: str
        :param SettleMonth: 支付月份
        :type SettleMonth: str
        :param Amt: 支付金额，单位分
        :type Amt: int
        :param PayerMode: agentpay：代付；selfpay：自付
        :type PayerMode: str
        """
        self.Uin = None
        self.OrderId = None
        self.ClientUin = None
        self.ClientRemark = None
        self.PayTime = None
        self.GoodsType = None
        self.PayMode = None
        self.SettleMonth = None
        self.Amt = None
        self.PayerMode = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.OrderId = params.get("OrderId")
        self.ClientUin = params.get("ClientUin")
        self.ClientRemark = params.get("ClientRemark")
        self.PayTime = params.get("PayTime")
        self.GoodsType = params.get("GoodsType")
        self.PayMode = params.get("PayMode")
        self.SettleMonth = params.get("SettleMonth")
        self.Amt = params.get("Amt")
        self.PayerMode = params.get("PayerMode")


class AgentClientElem(AbstractModel):
    """描述代客信息

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID
        :type Uin: str
        :param ClientUin: 代客账号ID
        :type ClientUin: str
        :param ApplyTime: 代客申请时间戳
        :type ApplyTime: int
        :param ClientFlag: 代客类型，可能值为a/b
        :type ClientFlag: str
        :param Mail: 代客邮箱，打码显示
        :type Mail: str
        :param Phone: 代客手机，打码显示
        :type Phone: str
        :param HasOverdueBill: 0表示不欠费，1表示欠费
        :type HasOverdueBill: int
        """
        self.Uin = None
        self.ClientUin = None
        self.ApplyTime = None
        self.ClientFlag = None
        self.Mail = None
        self.Phone = None
        self.HasOverdueBill = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.ApplyTime = params.get("ApplyTime")
        self.ClientFlag = params.get("ClientFlag")
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.HasOverdueBill = params.get("HasOverdueBill")


class AuditApplyClientRequest(AbstractModel):
    """AuditApplyClient请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 待审核客户账号ID
        :type ClientUin: str
        :param AuditResult: 审核结果，可能的取值：accept/reject
        :type AuditResult: str
        :param Note: 申请理由，B类客户审核通过时必须填写申请理由
        :type Note: str
        """
        self.ClientUin = None
        self.AuditResult = None
        self.Note = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.Note = params.get("Note")


class AuditApplyClientResponse(AbstractModel):
    """AuditApplyClient返回参数结构体

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID
        :type Uin: str
        :param ClientUin: 客户账号ID
        :type ClientUin: str
        :param AuditResult: 审核结果，包括accept/reject/qcloudaudit（腾讯云审核）
        :type AuditResult: str
        :param AgentTime: 关联时间对应的时间戳
        :type AgentTime: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.ClientUin = None
        self.AuditResult = None
        self.AgentTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.AgentTime = params.get("AgentTime")
        self.RequestId = params.get("RequestId")


class DescribeAgentBillsRequest(AbstractModel):
    """DescribeAgentBills请求参数结构体

    """

    def __init__(self):
        """
        :param SettleMonth: 支付月份，如2018-02
        :type SettleMonth: str
        :param ClientUin: 客户账号ID
        :type ClientUin: str
        :param PayMode: 支付方式，prepay/postpay
        :type PayMode: str
        :param OrderId: 预付费订单号
        :type OrderId: str
        :param ClientRemark: 客户备注名称
        :type ClientRemark: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
        self.SettleMonth = None
        self.ClientUin = None
        self.PayMode = None
        self.OrderId = None
        self.ClientRemark = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SettleMonth = params.get("SettleMonth")
        self.ClientUin = params.get("ClientUin")
        self.PayMode = params.get("PayMode")
        self.OrderId = params.get("OrderId")
        self.ClientRemark = params.get("ClientRemark")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAgentBillsResponse(AbstractModel):
    """DescribeAgentBills返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件列表总数量
        :type TotalCount: int
        :param AgentBillSet: 业务明细列表
        :type AgentBillSet: list of AgentBillElem
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AgentBillSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentBillSet") is not None:
            self.AgentBillSet = []
            for item in params.get("AgentBillSet"):
                obj = AgentBillElem()
                obj._deserialize(item)
                self.AgentBillSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentClientsRequest(AbstractModel):
    """DescribeAgentClients请求参数结构体

    """

    def __init__(self):
        """
        :param ClientUin: 客户账号ID
        :type ClientUin: str
        :param ClientName: 客户名称。由于涉及隐私，名称打码显示，故名称仅支持打码后的模糊搜索
        :type ClientName: str
        :param ClientFlag: 客户类型，a/b，类型定义参考代理商相关政策文档
        :type ClientFlag: str
        :param OrderDirection: ASC/DESC， 不区分大小写，按申请时间排序
        :type OrderDirection: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
        self.ClientUin = None
        self.ClientName = None
        self.ClientFlag = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.ClientName = params.get("ClientName")
        self.ClientFlag = params.get("ClientFlag")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAgentClientsResponse(AbstractModel):
    """DescribeAgentClients返回参数结构体

    """

    def __init__(self):
        """
        :param AgentClientSet: 代客列表
        :type AgentClientSet: list of AgentClientElem
        :param TotalCount: 符合条件的代客总数
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AgentClientSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentClientSet") is not None:
            self.AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentClientElem()
                obj._deserialize(item)
                self.AgentClientSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRebateInfosRequest(AbstractModel):
    """DescribeRebateInfos请求参数结构体

    """

    def __init__(self):
        """
        :param RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
        self.RebateMonth = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RebateMonth = params.get("RebateMonth")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRebateInfosResponse(AbstractModel):
    """DescribeRebateInfos返回参数结构体

    """

    def __init__(self):
        """
        :param RebateInfoSet: 返佣信息列表
        :type RebateInfoSet: list of RebateInfoElem
        :param TotalCount: 符合查询条件返佣信息数目
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RebateInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RebateInfoSet") is not None:
            self.RebateInfoSet = []
            for item in params.get("RebateInfoSet"):
                obj = RebateInfoElem()
                obj._deserialize(item)
                self.RebateInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ModifyClientRemarkRequest(AbstractModel):
    """ModifyClientRemark请求参数结构体

    """

    def __init__(self):
        """
        :param ClientRemark: 客户备注名称
        :type ClientRemark: str
        :param ClientUin: 客户账号ID
        :type ClientUin: str
        """
        self.ClientRemark = None
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientRemark = params.get("ClientRemark")
        self.ClientUin = params.get("ClientUin")


class ModifyClientRemarkResponse(AbstractModel):
    """ModifyClientRemark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RebateInfoElem(AbstractModel):
    """返佣信息定义

    """

    def __init__(self):
        """
        :param Uin: 代理商账号ID
        :type Uin: str
        :param RebateMonth: 返佣月份，如2018-02
        :type RebateMonth: str
        :param Amt: 返佣金额，单位分
        :type Amt: int
        :param MonthSales: 月度业绩，单位分
        :type MonthSales: int
        :param QuarterSales: 季度业绩，单位分
        :type QuarterSales: int
        :param ExceptionFlag: NORMAL(正常)/HAS_OVERDUE_BILL(欠费)/NO_CONTRACT(缺合同)
        :type ExceptionFlag: str
        """
        self.Uin = None
        self.RebateMonth = None
        self.Amt = None
        self.MonthSales = None
        self.QuarterSales = None
        self.ExceptionFlag = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RebateMonth = params.get("RebateMonth")
        self.Amt = params.get("Amt")
        self.MonthSales = params.get("MonthSales")
        self.QuarterSales = params.get("QuarterSales")
        self.ExceptionFlag = params.get("ExceptionFlag")