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


class AddUserToUserGroupRequest(AbstractModel):
    """AddUserToUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserIds: 加入用户组的用户ID列表。
        :type UserIds: list of str
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self.UserIds = None
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToUserGroupResponse(AbstractModel):
    """AddUserToUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ApplicationAuthorizationInfo(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        """
        :param ApplicationAccounts: 用户在被授权应用下对应的账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param ApplicationId: 应用ID，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param InheritedForm: 展示用户所在的用户组、机构节点拥有该应用的访问权限的ID信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        """
        self.ApplicationAccounts = None
        self.ApplicationId = None
        self.InheritedForm = None


    def _deserialize(self, params):
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("InheritedForm") is not None:
            self.InheritedForm = InheritedForm()
            self.InheritedForm._deserialize(params.get("InheritedForm"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgNodeRequest(AbstractModel):
    """CreateOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param DisplayName: 机构节点名称，长度限制：64个字符。
        :type DisplayName: str
        :param ParentOrgNodeId: 父机构节点ID，如果为空则默认创建在机构根节点下。
        :type ParentOrgNodeId: str
        :param Description: 机构节点描述。
        :type Description: str
        :param CustomizedOrgNodeId: 用户自定义可选填的机构节点对外ID，如果非空则校验此ID的唯一性。
        :type CustomizedOrgNodeId: str
        """
        self.DisplayName = None
        self.ParentOrgNodeId = None
        self.Description = None
        self.CustomizedOrgNodeId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.Description = params.get("Description")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgNodeResponse(AbstractModel):
    """CreateOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrgNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param DisplayName: 昵称，长度限制：64个字符。 DisplayName是唯一的。
        :type DisplayName: str
        :param Description: 用户备注，长度限制：512个字符。
        :type Description: str
        """
        self.DisplayName = None
        self.Description = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserGroupResponse(AbstractModel):
    """CreateUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名，长度限制：64个字符。
        :type UserName: str
        :param Password: 用户密码， 需要符合密码策略的配置。
        :type Password: str
        :param DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
        :type DisplayName: str
        :param Description: 用户备注，长度限制：512个字符。
        :type Description: str
        :param UserGroupIds: 用户所属用户组ID列表。
        :type UserGroupIds: list of str
        :param Phone: 用户手机号。
        :type Phone: str
        :param OrgNodeId: 用户所属组织机构唯一ID。如果为空，默认为在根节点下创建用户。
        :type OrgNodeId: str
        :param ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
        :type ExpirationTime: str
        :param Email: 用户邮箱。
        :type Email: str
        :param PwdNeedReset: 密码是否需要重置，为空默认为false不需要重置密码。
        :type PwdNeedReset: bool
        """
        self.UserName = None
        self.Password = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.Phone = None
        self.OrgNodeId = None
        self.ExpirationTime = None
        self.Email = None
        self.PwdNeedReset = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.Phone = params.get("Phone")
        self.OrgNodeId = params.get("OrgNodeId")
        self.ExpirationTime = params.get("ExpirationTime")
        self.Email = params.get("Email")
        self.PwdNeedReset = params.get("PwdNeedReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        """
        :param UserId: 返回的新创建的用户ID，是该用户的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class DecribePublicKeyRequest(AbstractModel):
    """DecribePublicKey请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecribePublicKeyResponse(AbstractModel):
    """DecribePublicKey返回参数结构体

    """

    def __init__(self):
        """
        :param PublicKey: jwt验证签名所用的公钥信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param KeyId: jwt的密钥id。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param ApplicationId: 应用ID，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PublicKey = None
        self.KeyId = None
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
        self.KeyId = params.get("KeyId")
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class DeleteOrgNodeRequest(AbstractModel):
    """DeleteOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
        :type OrgNodeId: str
        """
        self.OrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrgNodeResponse(AbstractModel):
    """DeleteOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserGroupRequest(AbstractModel):
    """DeleteUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupResponse(AbstractModel):
    """DeleteUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名，长度限制：32个字符。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserName: str
        :param UserId: 用户 id。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserId: str
        """
        self.UserName = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用id，是应用的全局唯一标识，与ClientId参数不能同时为空。
        :type ApplicationId: str
        :param ClientId: 客户端id，与ApplicationId参数不能同时为空。
        :type ClientId: str
        """
        self.ApplicationId = None
        self.ClientId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 密钥id。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param DisplayName: 应用展示名称，长度限制：64个字符。 默认与应用名字相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param LastModifiedDate: 应用最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param ClientId: 客户端id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param ApplicationType: 应用类型，即创建应用时所选择的应用模版类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param CreatedDate: 应用创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param ApplicationId: 应用id，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param TokenExpired: 令牌有效时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenExpired: int
        :param ClientSecret: 客户端secret。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientSecret: str
        :param PublicKey: 公钥信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param AuthorizeUrl: 授权地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizeUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.DisplayName = None
        self.LastModifiedDate = None
        self.ClientId = None
        self.ApplicationType = None
        self.CreatedDate = None
        self.ApplicationId = None
        self.TokenExpired = None
        self.ClientSecret = None
        self.PublicKey = None
        self.AuthorizeUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.ClientId = params.get("ClientId")
        self.ApplicationType = params.get("ApplicationType")
        self.CreatedDate = params.get("CreatedDate")
        self.ApplicationId = params.get("ApplicationId")
        self.TokenExpired = params.get("TokenExpired")
        self.ClientSecret = params.get("ClientSecret")
        self.PublicKey = params.get("PublicKey")
        self.AuthorizeUrl = params.get("AuthorizeUrl")
        self.RequestId = params.get("RequestId")


class DescribeOrgNodeRequest(AbstractModel):
    """DescribeOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点信息。
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: 是否读取其子节点信息。当读取层数为空或0时，默认仅读取当前机构节点信息。当读取层数为1时，读取本机构节点以及其第一层子节点信息。
        :type IncludeOrgNodeChildInfo: bool
        """
        self.OrgNodeId = None
        self.IncludeOrgNodeChildInfo = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgNodeResponse(AbstractModel):
    """DescribeOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param DisplayName: 机构节点展示名称，长度限制：64个字符。 默认与机构名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param LastModifiedDate: 机构节点最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param CustomizedOrgNodeId: 机构节点外部ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizedOrgNodeId: str
        :param ParentOrgNodeId: 当前机构节点的父节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentOrgNodeId: str
        :param OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param CreatedDate: 机构节点创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param OrgNodeChildInfo: 当前机构节点下的子节点列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeChildInfo: list of OrgNodeChildInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DisplayName = None
        self.LastModifiedDate = None
        self.CustomizedOrgNodeId = None
        self.ParentOrgNodeId = None
        self.OrgNodeId = None
        self.DataSource = None
        self.CreatedDate = None
        self.OrgNodeChildInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.CreatedDate = params.get("CreatedDate")
        if params.get("OrgNodeChildInfo") is not None:
            self.OrgNodeChildInfo = []
            for item in params.get("OrgNodeChildInfo"):
                obj = OrgNodeChildInfo()
                obj._deserialize(item)
                self.OrgNodeChildInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserGroupRequest(AbstractModel):
    """DescribeUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResponse(AbstractModel):
    """DescribeUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param DisplayName: 昵称，长度限制：64个字符。 DisplayName不唯一。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param Description: 用户备注，长度限制：512个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DisplayName = None
        self.Description = None
        self.UserGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupId = params.get("UserGroupId")
        self.RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名，长度限制：64个字符。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserName: str
        :param UserId: 用户 id，长度限制：64个字符。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserId: str
        """
        self.UserName = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param Status: 用户状态，取值 NORMAL （正常）、FREEZE （已冻结）、LOCKED （已锁定）或 NOT_ENABLED （未启用）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param DisplayName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param Description: 用户备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param UserGroupIds: 用户所属用户组 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param UserId: 用户 id，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param Email: 用户邮箱。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param Phone: 用户手机号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param OrgNodeId: 用户所属组织机构 Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param DataSource: 数据来源
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationTime: str
        :param ActivationTime: 用户激活时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivationTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserName = None
        self.Status = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.UserId = None
        self.Email = None
        self.Phone = None
        self.OrgNodeId = None
        self.DataSource = None
        self.ExpirationTime = None
        self.ActivationTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Status = params.get("Status")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.ExpirationTime = params.get("ExpirationTime")
        self.ActivationTime = params.get("ActivationTime")
        self.RequestId = params.get("RequestId")


class InheritedForm(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        """
        :param UserGroupIds: 用户所在的用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param OrgNodeIds: 用户所在的机构节点ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeIds: list of str
        """
        self.UserGroupIds = None
        self.OrgNodeIds = None


    def _deserialize(self, params):
        self.UserGroupIds = params.get("UserGroupIds")
        self.OrgNodeIds = params.get("OrgNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToOrgNodeRequest(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点 Id 。
        :type OrgNodeId: str
        """
        self.OrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToOrgNodeResponse(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param ApplicationIds: 机构节点拥有访问权限的应用 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserGroupRequest(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组 Id 。
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserGroupResponse(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param ApplicationIds: 用户组拥有访问权限的应用 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserRequest(AbstractModel):
    """ListAuthorizedApplicationsToUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户 ID。
        :type UserId: str
        :param IncludeInheritedAuthorizations: 查询范围是否包括用户关联的用户组、组织机构的应用访问权限。默认为不查询 。传0表示不查询该范围，传1表示应用查询该范围。
        :type IncludeInheritedAuthorizations: bool
        """
        self.UserId = None
        self.IncludeInheritedAuthorizations = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserResponse(AbstractModel):
    """ListAuthorizedApplicationsToUser返回参数结构体

    """

    def __init__(self):
        """
        :param ApplicationAuthorizationInfo: 用户拥有访问权限的应用信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAuthorizationInfo: list of ApplicationAuthorizationInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationAuthorizationInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationAuthorizationInfo") is not None:
            self.ApplicationAuthorizationInfo = []
            for item in params.get("ApplicationAuthorizationInfo"):
                obj = ApplicationAuthorizationInfo()
                obj._deserialize(item)
                self.ApplicationAuthorizationInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUserGroupsOfUserRequest(AbstractModel):
    """ListUserGroupsOfUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID，是用户的全局唯一标识。
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsOfUserResponse(AbstractModel):
    """ListUserGroupsOfUser返回参数结构体

    """

    def __init__(self):
        """
        :param UserGroupIds: 用户所属的用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param UserId: 用户ID，是用户的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserGroupIds = None
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class ListUsersInOrgNodeRequest(AbstractModel):
    """ListUsersInOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点下用户信息。
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: 限制读取子节点信息层数。当读取层数为空或0时，默认仅读取当前机构节点信息。当读取层数为1时，读取本机构节点以及其第一层子节点信息。
        :type IncludeOrgNodeChildInfo: bool
        """
        self.OrgNodeId = None
        self.IncludeOrgNodeChildInfo = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInOrgNodeResponse(AbstractModel):
    """ListUsersInOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeChildUserInfo: 机构子节点下的用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeChildUserInfo: list of OrgNodeChildUserInfo
        :param OrgNodeId: 机构ID，是机构节点全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param UserInfo: 用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param TotalUserNum: 当前机构节点下的用户总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUserNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrgNodeChildUserInfo = None
        self.OrgNodeId = None
        self.UserInfo = None
        self.TotalUserNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OrgNodeChildUserInfo") is not None:
            self.OrgNodeChildUserInfo = []
            for item in params.get("OrgNodeChildUserInfo"):
                obj = OrgNodeChildUserInfo()
                obj._deserialize(item)
                self.OrgNodeChildUserInfo.append(obj)
        self.OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalUserNum = params.get("TotalUserNum")
        self.RequestId = params.get("RequestId")


class ListUsersInUserGroupRequest(AbstractModel):
    """ListUsersInUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupResponse(AbstractModel):
    """ListUsersInUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param UserInfo: 返回的用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param TotalNum: 返回的用户信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserGroupId = None
        self.UserInfo = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ModifyUserInfoRequest(AbstractModel):
    """ModifyUserInfo请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名，长度限制：32个字符。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserName: str
        :param DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
        :type DisplayName: str
        :param Description: 用户备注，长度限制：512个字符。
        :type Description: str
        :param UserGroupIds: 用户所属用户组ID列表。
        :type UserGroupIds: list of str
        :param UserId: 用户 id。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserId: str
        :param Phone: 用户手机号。
        :type Phone: str
        :param ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
        :type ExpirationTime: str
        :param Password: 用户密码， 需要符合密码策略的配置。
        :type Password: str
        :param Email: 用户邮箱。
        :type Email: str
        :param PwdNeedReset: 密码是否需要重置，为空默认为false不需要重置密码。
        :type PwdNeedReset: bool
        """
        self.UserName = None
        self.DisplayName = None
        self.Description = None
        self.UserGroupIds = None
        self.UserId = None
        self.Phone = None
        self.ExpirationTime = None
        self.Password = None
        self.Email = None
        self.PwdNeedReset = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.UserGroupIds = params.get("UserGroupIds")
        self.UserId = params.get("UserId")
        self.Phone = params.get("Phone")
        self.ExpirationTime = params.get("ExpirationTime")
        self.Password = params.get("Password")
        self.Email = params.get("Email")
        self.PwdNeedReset = params.get("PwdNeedReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserInfoResponse(AbstractModel):
    """ModifyUserInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgNodeChildInfo(AbstractModel):
    """当前机构节点下的子节点列表

    """

    def __init__(self):
        """
        :param DisplayName: 机构节点展示名称，长度限制：64个字符。 默认与机构名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param LastModifiedDate: 机构节点最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param CustomizedOrgNodeId: 用户自定义可选填的机构节点对外ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizedOrgNodeId: str
        :param ParentOrgNodeId: 当前机构节点的父节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentOrgNodeId: str
        :param OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param CreatedDate: 机构节点创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        """
        self.DisplayName = None
        self.LastModifiedDate = None
        self.CustomizedOrgNodeId = None
        self.ParentOrgNodeId = None
        self.OrgNodeId = None
        self.DataSource = None
        self.CreatedDate = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self.ParentOrgNodeId = params.get("ParentOrgNodeId")
        self.OrgNodeId = params.get("OrgNodeId")
        self.DataSource = params.get("DataSource")
        self.CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNodeChildUserInfo(AbstractModel):
    """机构子节点下的用户信息列表

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构ID，是机构节点全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param UserInfo: 用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param TotalUserNum: 当前机构节点下的用户总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUserNum: int
        """
        self.OrgNodeId = None
        self.UserInfo = None
        self.TotalUserNum = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.TotalUserNum = params.get("TotalUserNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromUserGroupRequest(AbstractModel):
    """RemoveUserFromUserGroup请求参数结构体

    """

    def __init__(self):
        """
        :param UserIds: 要加入用户组的用户ID列表。
        :type UserIds: list of str
        :param UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self.UserIds = None
        self.UserGroupId = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromUserGroupResponse(AbstractModel):
    """RemoveUserFromUserGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrgNodeRequest(AbstractModel):
    """UpdateOrgNode请求参数结构体

    """

    def __init__(self):
        """
        :param OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
        :type OrgNodeId: str
        :param DisplayName: 机构节点名称，长度限制：64个字符。
        :type DisplayName: str
        :param Description: 机构节点描述。
        :type Description: str
        :param CustomizedOrgNodeId: 用户自定义可选填的机构节点对外ID，如果非空则校验此ID的唯一性。
        :type CustomizedOrgNodeId: str
        """
        self.OrgNodeId = None
        self.DisplayName = None
        self.Description = None
        self.CustomizedOrgNodeId = None


    def _deserialize(self, params):
        self.OrgNodeId = params.get("OrgNodeId")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeResponse(AbstractModel):
    """UpdateOrgNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    """用户信息列表。

    """

    def __init__(self):
        """
        :param UserId: 用户ID，是用户全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        """
        self.UserId = None
        self.DisplayName = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.DisplayName = params.get("DisplayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        