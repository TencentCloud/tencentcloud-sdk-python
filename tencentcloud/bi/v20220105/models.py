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


class ApplyEmbedIntervalRequest(AbstractModel):
    """ApplyEmbedInterval请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 分享项目id，必选
        :type ProjectId: int
        :param PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param BIToken: 需要申请延期的Token
        :type BIToken: str
        :param ExtraParam: 备用字段
        :type ExtraParam: str
        :param Scope: panel,看板；page，页面
        :type Scope: str
        """
        self.ProjectId = None
        self.PageId = None
        self.BIToken = None
        self.ExtraParam = None
        self.Scope = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageId = params.get("PageId")
        self.BIToken = params.get("BIToken")
        self.ExtraParam = params.get("ExtraParam")
        self.Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyEmbedIntervalResponse(AbstractModel):
    """ApplyEmbedInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param Extra: 额外参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param Data: 结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedTokenInfo`
        :param Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Extra = None
        self.Data = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Extra = params.get("Extra")
        if params.get("Data") is not None:
            self.Data = ApplyEmbedTokenInfo()
            self.Data._deserialize(params.get("Data"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class ApplyEmbedTokenInfo(AbstractModel):
    """申请Token延期

    """

    def __init__(self):
        r"""
        :param Result: 申请结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        """
        self.Result = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenRequest(AbstractModel):
    """CreateEmbedToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 分享项目id，必选
        :type ProjectId: int
        :param PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param Scope: page表示嵌出页面，panel表嵌出整个看板
        :type Scope: str
        :param ExpireTime: 过期时间。 单位：分钟 最大值：240。即，4小时 默认值：240
        :type ExpireTime: str
        :param ExtraParam: 备用字段
        :type ExtraParam: str
        """
        self.ProjectId = None
        self.PageId = None
        self.Scope = None
        self.ExpireTime = None
        self.ExtraParam = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageId = params.get("PageId")
        self.Scope = params.get("Scope")
        self.ExpireTime = params.get("ExpireTime")
        self.ExtraParam = params.get("ExtraParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenResponse(AbstractModel):
    """CreateEmbedToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.EmbedTokenInfo`
        :param Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Extra = None
        self.Data = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Extra = params.get("Extra")
        if params.get("Data") is not None:
            self.Data = EmbedTokenInfo()
            self.Data._deserialize(params.get("Data"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class EmbedTokenInfo(AbstractModel):
    """报表嵌出数据结构-强鉴权

    """

    def __init__(self):
        r"""
        :param Id: 信息标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param BIToken: 令牌
注意：此字段可能返回 null，表示取不到有效值。
        :type BIToken: str
        :param ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param PageId: 页面Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: str
        :param ExtraParam: 备用
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParam: str
        :param Scope: 嵌出类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: str
        :param ExpireTime: 过期时间，分钟为单位，最大240
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        """
        self.Id = None
        self.BIToken = None
        self.ProjectId = None
        self.CreatedUser = None
        self.CreatedAt = None
        self.UpdatedUser = None
        self.UpdatedAt = None
        self.PageId = None
        self.ExtraParam = None
        self.Scope = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.BIToken = params.get("BIToken")
        self.ProjectId = params.get("ProjectId")
        self.CreatedUser = params.get("CreatedUser")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedUser = params.get("UpdatedUser")
        self.UpdatedAt = params.get("UpdatedAt")
        self.PageId = params.get("PageId")
        self.ExtraParam = params.get("ExtraParam")
        self.Scope = params.get("Scope")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        