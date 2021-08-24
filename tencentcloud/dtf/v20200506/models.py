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


class DescribeTransactionsRequest(AbstractModel):
    """DescribeTransactions请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 事务分组ID
        :type GroupId: str
        :param TransactionBeginFrom: 事务开始时间查询起始时间戳，UTC，精确到毫秒
        :type TransactionBeginFrom: int
        :param TransactionBeginTo: 事务开始时间查询截止时间戳，UTC，精确到毫秒
        :type TransactionBeginTo: int
        :param SearchError: 仅查询异常状态的事务，true：仅查询异常，false或不传入：查询所有
        :type SearchError: bool
        :param TransactionId: 主事务ID，不传入时查询全量，高优先级
        :type TransactionId: int
        :param TransactionIdList: 主事务ID列表，不传入时查询全量，低优先级
        :type TransactionIdList: list of int
        :param Limit: 每页数量
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        """
        self.GroupId = None
        self.TransactionBeginFrom = None
        self.TransactionBeginTo = None
        self.SearchError = None
        self.TransactionId = None
        self.TransactionIdList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.TransactionBeginFrom = params.get("TransactionBeginFrom")
        self.TransactionBeginTo = params.get("TransactionBeginTo")
        self.SearchError = params.get("SearchError")
        self.TransactionId = params.get("TransactionId")
        self.TransactionIdList = params.get("TransactionIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransactionsResponse(AbstractModel):
    """DescribeTransactions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 主事务分页列表
        :type Result: :class:`tencentcloud.dtf.v20200506.models.PagedTransaction`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PagedTransaction()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class PagedTransaction(AbstractModel):
    """分页主事务

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数，特定在该接口中总是会返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 主事务分组列表
        :type Content: list of Transaction
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Transaction()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transaction(AbstractModel):
    """主事务

    """

    def __init__(self):
        r"""
        :param TransactionId: 主事务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionId: int
        :param TransactionBegin: 主事务开始时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionBegin: int
        :param TransactionEnd: 主事务结束时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionEnd: int
        :param TransactionCommit: 主事务提交时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionCommit: int
        :param TransactionRollback: 主事务回滚时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionRollback: int
        :param TransactionError: 主事务异常停止时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionError: int
        :param Timeout: 主事务超时时长，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param Status: 主事务状态：0:Trying, 1:Confirming, 2: Confirmed, 3:Canceling, 4: Canceled
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param EndFlag: 主事务结束标识：0:运行中, 1: 已结束
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: int
        :param TimeoutFlag: 主事务超时标识：0:运行中, 1: 已超时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutFlag: int
        :param Comment: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param GroupId: 事务分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param Server: 主事务来源服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param BranchQuantity: 分支事务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BranchQuantity: int
        :param RetryFlag: 重试标识：true：可以重试；false：不可重试
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryFlag: bool
        """
        self.TransactionId = None
        self.TransactionBegin = None
        self.TransactionEnd = None
        self.TransactionCommit = None
        self.TransactionRollback = None
        self.TransactionError = None
        self.Timeout = None
        self.Status = None
        self.EndFlag = None
        self.TimeoutFlag = None
        self.Comment = None
        self.GroupId = None
        self.Server = None
        self.BranchQuantity = None
        self.RetryFlag = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.TransactionBegin = params.get("TransactionBegin")
        self.TransactionEnd = params.get("TransactionEnd")
        self.TransactionCommit = params.get("TransactionCommit")
        self.TransactionRollback = params.get("TransactionRollback")
        self.TransactionError = params.get("TransactionError")
        self.Timeout = params.get("Timeout")
        self.Status = params.get("Status")
        self.EndFlag = params.get("EndFlag")
        self.TimeoutFlag = params.get("TimeoutFlag")
        self.Comment = params.get("Comment")
        self.GroupId = params.get("GroupId")
        self.Server = params.get("Server")
        self.BranchQuantity = params.get("BranchQuantity")
        self.RetryFlag = params.get("RetryFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        