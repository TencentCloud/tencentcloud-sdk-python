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
        """
        :param GroupId: 事务分组ID\n        :type GroupId: str\n        :param TransactionBeginFrom: 事务开始时间查询起始时间戳，UTC，精确到毫秒\n        :type TransactionBeginFrom: int\n        :param TransactionBeginTo: 事务开始时间查询截止时间戳，UTC，精确到毫秒\n        :type TransactionBeginTo: int\n        :param SearchError: 仅查询异常状态的事务，true：仅查询异常，false或不传入：查询所有\n        :type SearchError: bool\n        :param TransactionId: 主事务ID，不传入时查询全量，高优先级\n        :type TransactionId: int\n        :param TransactionIdList: 主事务ID列表，不传入时查询全量，低优先级\n        :type TransactionIdList: list of int\n        :param Limit: 每页数量\n        :type Limit: int\n        :param Offset: 起始偏移量\n        :type Offset: int\n        """
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
        """
        :param Result: 主事务分页列表\n        :type Result: :class:`tencentcloud.dtf.v20200506.models.PagedTransaction`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TotalCount: 总条数，特定在该接口中总是会返回null
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 主事务分组列表\n        :type Content: list of Transaction\n        """
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
        """
        :param TransactionId: 主事务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionId: int\n        :param TransactionBegin: 主事务开始时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionBegin: int\n        :param TransactionEnd: 主事务结束时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionEnd: int\n        :param TransactionCommit: 主事务提交时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionCommit: int\n        :param TransactionRollback: 主事务回滚时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionRollback: int\n        :param TransactionError: 主事务异常停止时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionError: int\n        :param Timeout: 主事务超时时长，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timeout: int\n        :param Status: 主事务状态：0:Trying, 1:Confirming, 2: Confirmed, 3:Canceling, 4: Canceled
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param EndFlag: 主事务结束标识：0:运行中, 1: 已结束
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: int\n        :param TimeoutFlag: 主事务超时标识：0:运行中, 1: 已超时
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeoutFlag: int\n        :param Comment: 异常信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Comment: str\n        :param GroupId: 事务分组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param Server: 主事务来源服务标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type Server: str\n        :param BranchQuantity: 分支事务数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type BranchQuantity: int\n        :param RetryFlag: 重试标识：true：可以重试；false：不可重试
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetryFlag: bool\n        """
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
        