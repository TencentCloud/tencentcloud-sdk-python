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
        :param _ProjectId: 分享项目id，必选
        :type ProjectId: int
        :param _PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param _BIToken: 需要申请延期的Token
        :type BIToken: str
        :param _ExtraParam: 备用字段
        :type ExtraParam: str
        :param _Scope: panel,看板；page，页面
        :type Scope: str
        """
        self._ProjectId = None
        self._PageId = None
        self._BIToken = None
        self._ExtraParam = None
        self._Scope = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def BIToken(self):
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._BIToken = params.get("BIToken")
        self._ExtraParam = params.get("ExtraParam")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyEmbedIntervalResponse(AbstractModel):
    """ApplyEmbedInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Extra: 额外参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedTokenInfo`
        :param _Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = ApplyEmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ApplyEmbedTokenInfo(AbstractModel):
    """申请Token延期

    """

    def __init__(self):
        r"""
        :param _Result: 申请结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenRequest(AbstractModel):
    """CreateEmbedToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 分享项目id
        :type ProjectId: int
        :param _PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param _Scope: page表示嵌出页面，panel表嵌出整个看板
        :type Scope: str
        :param _ExpireTime: 过期时间。 单位：分钟 最大值：240。即，4小时 默认值：240
        :type ExpireTime: str
        :param _ExtraParam: 备用字段
        :type ExtraParam: str
        :param _UserCorpId: 使用者企业Id(仅用于多用户)
        :type UserCorpId: str
        :param _UserId: 使用者Id(仅用于多用户)
        :type UserId: str
        """
        self._ProjectId = None
        self._PageId = None
        self._Scope = None
        self._ExpireTime = None
        self._ExtraParam = None
        self._UserCorpId = None
        self._UserId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UserCorpId(self):
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._ExtraParam = params.get("ExtraParam")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenResponse(AbstractModel):
    """CreateEmbedToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.EmbedTokenInfo`
        :param _Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = EmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class EmbedTokenInfo(AbstractModel):
    """报表嵌出数据结构-强鉴权

    """

    def __init__(self):
        r"""
        :param _Id: 信息标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _BIToken: 令牌
注意：此字段可能返回 null，表示取不到有效值。
        :type BIToken: str
        :param _ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _PageId: 页面Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: str
        :param _ExtraParam: 备用
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParam: str
        :param _Scope: 嵌出类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: str
        :param _ExpireTime: 过期时间，分钟为单位，最大240
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _UserCorpId: 使用者企业Id(仅用于多用户)
注意：此字段可能返回 null，表示取不到有效值。
        :type UserCorpId: str
        :param _UserId: 使用者Id(仅用于多用户)
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        """
        self._Id = None
        self._BIToken = None
        self._ProjectId = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._PageId = None
        self._ExtraParam = None
        self._Scope = None
        self._ExpireTime = None
        self._UserCorpId = None
        self._UserId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BIToken(self):
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserCorpId(self):
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BIToken = params.get("BIToken")
        self._ProjectId = params.get("ProjectId")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._PageId = params.get("PageId")
        self._ExtraParam = params.get("ExtraParam")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        