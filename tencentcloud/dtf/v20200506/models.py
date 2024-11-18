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
        :param _GroupId: 事务分组ID
        :type GroupId: str
        :param _TransactionBeginFrom: 事务开始时间查询起始时间戳，UTC，精确到毫秒
        :type TransactionBeginFrom: int
        :param _TransactionBeginTo: 事务开始时间查询截止时间戳，UTC，精确到毫秒
        :type TransactionBeginTo: int
        :param _SearchError: 仅查询异常状态的事务，true：仅查询异常，false或不传入：查询所有
        :type SearchError: bool
        :param _TransactionId: 主事务ID，不传入时查询全量，高优先级
        :type TransactionId: int
        :param _TransactionIdList: 主事务ID列表，不传入时查询全量，低优先级
        :type TransactionIdList: list of int
        :param _Limit: 每页数量
        :type Limit: int
        :param _Offset: 起始偏移量
        :type Offset: int
        """
        self._GroupId = None
        self._TransactionBeginFrom = None
        self._TransactionBeginTo = None
        self._SearchError = None
        self._TransactionId = None
        self._TransactionIdList = None
        self._Limit = None
        self._Offset = None

    @property
    def GroupId(self):
        """事务分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TransactionBeginFrom(self):
        """事务开始时间查询起始时间戳，UTC，精确到毫秒
        :rtype: int
        """
        return self._TransactionBeginFrom

    @TransactionBeginFrom.setter
    def TransactionBeginFrom(self, TransactionBeginFrom):
        self._TransactionBeginFrom = TransactionBeginFrom

    @property
    def TransactionBeginTo(self):
        """事务开始时间查询截止时间戳，UTC，精确到毫秒
        :rtype: int
        """
        return self._TransactionBeginTo

    @TransactionBeginTo.setter
    def TransactionBeginTo(self, TransactionBeginTo):
        self._TransactionBeginTo = TransactionBeginTo

    @property
    def SearchError(self):
        """仅查询异常状态的事务，true：仅查询异常，false或不传入：查询所有
        :rtype: bool
        """
        return self._SearchError

    @SearchError.setter
    def SearchError(self, SearchError):
        self._SearchError = SearchError

    @property
    def TransactionId(self):
        """主事务ID，不传入时查询全量，高优先级
        :rtype: int
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionIdList(self):
        """主事务ID列表，不传入时查询全量，低优先级
        :rtype: list of int
        """
        return self._TransactionIdList

    @TransactionIdList.setter
    def TransactionIdList(self, TransactionIdList):
        self._TransactionIdList = TransactionIdList

    @property
    def Limit(self):
        """每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """起始偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._TransactionBeginFrom = params.get("TransactionBeginFrom")
        self._TransactionBeginTo = params.get("TransactionBeginTo")
        self._SearchError = params.get("SearchError")
        self._TransactionId = params.get("TransactionId")
        self._TransactionIdList = params.get("TransactionIdList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransactionsResponse(AbstractModel):
    """DescribeTransactions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 主事务分页列表
        :type Result: :class:`tencentcloud.dtf.v20200506.models.PagedTransaction`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """主事务分页列表
        :rtype: :class:`tencentcloud.dtf.v20200506.models.PagedTransaction`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = PagedTransaction()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class PagedTransaction(AbstractModel):
    """分页主事务

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数，特定在该接口中总是会返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Content: 主事务分组列表
        :type Content: list of Transaction
        """
        self._TotalCount = None
        self._Content = None

    @property
    def TotalCount(self):
        """总条数，特定在该接口中总是会返回null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        """主事务分组列表
        :rtype: list of Transaction
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = Transaction()
                obj._deserialize(item)
                self._Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transaction(AbstractModel):
    """主事务

    """

    def __init__(self):
        r"""
        :param _TransactionId: 主事务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionId: int
        :param _TransactionBegin: 主事务开始时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionBegin: int
        :param _TransactionEnd: 主事务结束时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionEnd: int
        :param _TransactionCommit: 主事务提交时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionCommit: int
        :param _TransactionRollback: 主事务回滚时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionRollback: int
        :param _TransactionError: 主事务异常停止时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionError: int
        :param _Timeout: 主事务超时时长，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _Status: 主事务状态：0:Trying, 1:Confirming, 2: Confirmed, 3:Canceling, 4: Canceled
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _EndFlag: 主事务结束标识：0:运行中, 1: 已结束
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: int
        :param _TimeoutFlag: 主事务超时标识：0:运行中, 1: 已超时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutFlag: int
        :param _Comment: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _GroupId: 事务分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _Server: 主事务来源服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param _BranchQuantity: 分支事务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type BranchQuantity: int
        :param _RetryFlag: 重试标识：true：可以重试；false：不可重试
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryFlag: bool
        """
        self._TransactionId = None
        self._TransactionBegin = None
        self._TransactionEnd = None
        self._TransactionCommit = None
        self._TransactionRollback = None
        self._TransactionError = None
        self._Timeout = None
        self._Status = None
        self._EndFlag = None
        self._TimeoutFlag = None
        self._Comment = None
        self._GroupId = None
        self._Server = None
        self._BranchQuantity = None
        self._RetryFlag = None

    @property
    def TransactionId(self):
        """主事务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionBegin(self):
        """主事务开始时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionBegin

    @TransactionBegin.setter
    def TransactionBegin(self, TransactionBegin):
        self._TransactionBegin = TransactionBegin

    @property
    def TransactionEnd(self):
        """主事务结束时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionEnd

    @TransactionEnd.setter
    def TransactionEnd(self, TransactionEnd):
        self._TransactionEnd = TransactionEnd

    @property
    def TransactionCommit(self):
        """主事务提交时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionCommit

    @TransactionCommit.setter
    def TransactionCommit(self, TransactionCommit):
        self._TransactionCommit = TransactionCommit

    @property
    def TransactionRollback(self):
        """主事务回滚时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionRollback

    @TransactionRollback.setter
    def TransactionRollback(self, TransactionRollback):
        self._TransactionRollback = TransactionRollback

    @property
    def TransactionError(self):
        """主事务异常停止时间戳，UTC，精确到毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TransactionError

    @TransactionError.setter
    def TransactionError(self, TransactionError):
        self._TransactionError = TransactionError

    @property
    def Timeout(self):
        """主事务超时时长，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Status(self):
        """主事务状态：0:Trying, 1:Confirming, 2: Confirmed, 3:Canceling, 4: Canceled
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndFlag(self):
        """主事务结束标识：0:运行中, 1: 已结束
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EndFlag

    @EndFlag.setter
    def EndFlag(self, EndFlag):
        self._EndFlag = EndFlag

    @property
    def TimeoutFlag(self):
        """主事务超时标识：0:运行中, 1: 已超时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeoutFlag

    @TimeoutFlag.setter
    def TimeoutFlag(self, TimeoutFlag):
        self._TimeoutFlag = TimeoutFlag

    @property
    def Comment(self):
        """异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def GroupId(self):
        """事务分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Server(self):
        """主事务来源服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def BranchQuantity(self):
        """分支事务数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BranchQuantity

    @BranchQuantity.setter
    def BranchQuantity(self, BranchQuantity):
        self._BranchQuantity = BranchQuantity

    @property
    def RetryFlag(self):
        """重试标识：true：可以重试；false：不可重试
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RetryFlag

    @RetryFlag.setter
    def RetryFlag(self, RetryFlag):
        self._RetryFlag = RetryFlag


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._TransactionBegin = params.get("TransactionBegin")
        self._TransactionEnd = params.get("TransactionEnd")
        self._TransactionCommit = params.get("TransactionCommit")
        self._TransactionRollback = params.get("TransactionRollback")
        self._TransactionError = params.get("TransactionError")
        self._Timeout = params.get("Timeout")
        self._Status = params.get("Status")
        self._EndFlag = params.get("EndFlag")
        self._TimeoutFlag = params.get("TimeoutFlag")
        self._Comment = params.get("Comment")
        self._GroupId = params.get("GroupId")
        self._Server = params.get("Server")
        self._BranchQuantity = params.get("BranchQuantity")
        self._RetryFlag = params.get("RetryFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        