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


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList请求参数结构体

    """


class DescribeApplicationListResponse(AbstractModel):
    """DescribeApplicationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeEdgeApplicationTokenRequest(AbstractModel):
    """DescribeEdgeApplicationToken请求参数结构体

    """


class DescribeEdgeApplicationTokenResponse(AbstractModel):
    """DescribeEdgeApplicationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeInterfaceListRequest(AbstractModel):
    """DescribeInterfaceList请求参数结构体

    """


class DescribeInterfaceListResponse(AbstractModel):
    """DescribeInterfaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeWorkspaceListRequest(AbstractModel):
    """DescribeWorkspaceList请求参数结构体

    """


class DescribeWorkspaceListResponse(AbstractModel):
    """DescribeWorkspaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeWorkspaceUserListRequest(AbstractModel):
    """DescribeWorkspaceUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        """
        self._Offset = None
        self._Limit = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceUserListResponse(AbstractModel):
    """DescribeWorkspaceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoTeamUserResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = SsoTeamUserResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class SsoTeamUser(AbstractModel):
    """部门用户

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RealName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param _UserType: 用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _TenantId: 所属租户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Phone: 电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Status: 用户状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: int
        :param _DepartmentId: 部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        :param _LinkFilter: 是否关联权限
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkFilter: int
        """
        self._UserId = None
        self._RealName = None
        self._UserType = None
        self._TenantId = None
        self._Email = None
        self._Phone = None
        self._Status = None
        self._CreateAt = None
        self._DepartmentId = None
        self._DepartmentName = None
        self._LinkFilter = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def LinkFilter(self):
        return self._LinkFilter

    @LinkFilter.setter
    def LinkFilter(self, LinkFilter):
        self._LinkFilter = LinkFilter


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RealName = params.get("RealName")
        self._UserType = params.get("UserType")
        self._TenantId = params.get("TenantId")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        self._LinkFilter = params.get("LinkFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoTeamUserResult(AbstractModel):
    """空间用户结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Users: 部门用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of SsoTeamUser
        """
        self._Total = None
        self._Users = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = SsoTeamUser()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        