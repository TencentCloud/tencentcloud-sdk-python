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
        r"""
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
        r"""
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
        r"""
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
        


class ApplicationInfoSearchCriteria(AbstractModel):
    """应用属性搜索条件。

    """

    def __init__(self):
        r"""
        :param Keyword: 应用匹配搜索关键字，匹配范围包括：应用名称、应用ID。
        :type Keyword: str
        :param ApplicationType: 应用类型。ApplicationType的取值范围有：OAUTH2、JWT、CAS、SAML2、FORM、OIDC、APIGW。
        :type ApplicationType: str
        """
        self.Keyword = None
        self.ApplicationType = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInformation(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        :param DisplayName: 应用展示名称，长度限制：64个字符。 默认与应用名字相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param CreatedDate: 应用创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param AppStatus: 应用状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: bool
        :param Icon: 应用图标。
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param ApplicationType: 应用类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ClientId: 客户端id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        """
        self.ApplicationId = None
        self.DisplayName = None
        self.CreatedDate = None
        self.LastModifiedDate = None
        self.AppStatus = None
        self.Icon = None
        self.ApplicationType = None
        self.ClientId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.DisplayName = params.get("DisplayName")
        self.CreatedDate = params.get("CreatedDate")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.AppStatus = params.get("AppStatus")
        self.Icon = params.get("Icon")
        self.ApplicationType = params.get("ApplicationType")
        self.ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfo(AbstractModel):
    """返回的授权关系信息。

    """

    def __init__(self):
        r"""
        :param AppId: 应用唯一ID。
        :type AppId: str
        :param AppName: 应用名称。
        :type AppName: str
        :param EntityName: 类型名称。
        :type EntityName: str
        :param EntityId: 类型唯一ID。
        :type EntityId: str
        :param LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
        :type LastModifiedDate: str
        :param AuthorizationId: 授权类型唯一ID。
        :type AuthorizationId: str
        """
        self.AppId = None
        self.AppName = None
        self.EntityName = None
        self.EntityId = None
        self.LastModifiedDate = None
        self.AuthorizationId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.AppName = params.get("AppName")
        self.EntityName = params.get("EntityName")
        self.EntityId = params.get("EntityId")
        self.LastModifiedDate = params.get("LastModifiedDate")
        self.AuthorizationId = params.get("AuthorizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfoSearchCriteria(AbstractModel):
    """用户属性搜索条件。

    """

    def __init__(self):
        r"""
        :param Keyword: 名称匹配搜索，当查询类型为用户时，匹配范围包括：用户名称、应用名称；当查询类型为用户组时，匹配范围包括：用户组名称、应用名称；当查询类型为组织机构时，匹配范围包括：组织机构名称、应用名称。
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationResouceEntityInfo(AbstractModel):
    """授权资源详情

    """

    def __init__(self):
        r"""
        :param ResourceId: 授权关系的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ResourceType: 资源授权类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Resource: 授权的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        """
        self.ResourceId = None
        self.ResourceType = None
        self.Resource = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.Resource = params.get("Resource")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationUserResouceInfo(AbstractModel):
    """返回符合条件的用户数据列表

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Resource: 授权资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param InheritedForm: 继承关系
注意：此字段可能返回 null，表示取不到有效值。
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param ApplicationAccounts: 应用账户
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        """
        self.ResourceId = None
        self.ResourceType = None
        self.Resource = None
        self.InheritedForm = None
        self.ApplicationAccounts = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.Resource = params.get("Resource")
        if params.get("InheritedForm") is not None:
            self.InheritedForm = InheritedForm()
            self.InheritedForm._deserialize(params.get("InheritedForm"))
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.ResourceName = params.get("ResourceName")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param Phone: 用户手机号。例如：+86-1xxxxxxxxxx。
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
        r"""
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


class DeleteOrgNodeRequest(AbstractModel):
    """DeleteOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param IconUrl: 应用图标图片访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param SecureLevel: 安全等级。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecureLevel: str
        :param AppStatus: 应用状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: bool
        :param Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
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
        self.IconUrl = None
        self.SecureLevel = None
        self.AppStatus = None
        self.Description = None
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
        self.IconUrl = params.get("IconUrl")
        self.SecureLevel = params.get("SecureLevel")
        self.AppStatus = params.get("AppStatus")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeOrgNodeRequest(AbstractModel):
    """DescribeOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点信息。
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: 是否读取其子节点信息。当其为空或false时，默认仅读取当前机构节点信息。当其为true时，读取本机构节点以及其第一层子节点信息。
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
        r"""
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


class DescribeOrgResourcesAuthorizationRequest(AbstractModel):
    """DescribeOrgResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param OrgNodeId: 机构ID
        :type OrgNodeId: str
        """
        self.ApplicationId = None
        self.OrgNodeId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgResourcesAuthorizationResponse(AbstractModel):
    """DescribeOrgResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param OrgNodeId: 授权机构ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param OrgNodeName: 机构名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeName: str
        :param OrgNodePath: 机构目录
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodePath: str
        :param AuthorizationOrgResourceList: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationOrgResourceList: list of AuthorizationResouceEntityInfo
        :param TotalCount: 资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.OrgNodeId = None
        self.OrgNodeName = None
        self.OrgNodePath = None
        self.AuthorizationOrgResourceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.OrgNodeId = params.get("OrgNodeId")
        self.OrgNodeName = params.get("OrgNodeName")
        self.OrgNodePath = params.get("OrgNodePath")
        if params.get("AuthorizationOrgResourceList") is not None:
            self.AuthorizationOrgResourceList = []
            for item in params.get("AuthorizationOrgResourceList"):
                obj = AuthorizationResouceEntityInfo()
                obj._deserialize(item)
                self.AuthorizationOrgResourceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePublicKeyRequest(AbstractModel):
    """DescribePublicKey请求参数结构体

    """

    def __init__(self):
        r"""
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
        


class DescribePublicKeyResponse(AbstractModel):
    """DescribePublicKey返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeUserGroupRequest(AbstractModel):
    """DescribeUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
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
        


class DescribeUserGroupResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserGroupResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param UserGroupId: 用户组ID
        :type UserGroupId: str
        """
        self.ApplicationId = None
        self.UserGroupId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserGroupResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param UserGroupId: 用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param UserGroupName: 用户组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupName: str
        :param AuthorizationUserGroupResourceList: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationUserGroupResourceList: list of AuthorizationResouceEntityInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.UserGroupId = None
        self.UserGroupName = None
        self.AuthorizationUserGroupResourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserGroupId = params.get("UserGroupId")
        self.UserGroupName = params.get("UserGroupName")
        if params.get("AuthorizationUserGroupResourceList") is not None:
            self.AuthorizationUserGroupResourceList = []
            for item in params.get("AuthorizationUserGroupResourceList"):
                obj = AuthorizationResouceEntityInfo()
                obj._deserialize(item)
                self.AuthorizationUserGroupResourceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserGroupResponse(AbstractModel):
    """DescribeUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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


class DescribeUserResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID。
        :type ApplicationId: str
        :param UserId: 用户ID。UserName 和 UserId 需至少一个不为空；都不为空时优先使用 UserName。
        :type UserId: str
        :param UserName: 用户名。UserName 和 UserId 需至少一个不为空；都不为空时优先使用 UserName。
        :type UserName: str
        :param IncludeInheritedAuthorizations: 查询范围是否包括用户关联的用户组、组织机构的应用访问权限。默认为不查询 ，传false表示不查询该范围，传true查询该范围。
        :type IncludeInheritedAuthorizations: bool
        """
        self.ApplicationId = None
        self.UserId = None
        self.UserName = None
        self.IncludeInheritedAuthorizations = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用的唯一ID。
        :type ApplicationId: str
        :param ApplicationAccounts: 应用账户。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param UserId: 授权用户的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param UserName: 授权的用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param AuthorizationUserResourceList: 返回的资源列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationUserResourceList: list of AuthorizationUserResouceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.ApplicationAccounts = None
        self.UserId = None
        self.UserName = None
        self.AuthorizationUserResourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationAccounts = params.get("ApplicationAccounts")
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        if params.get("AuthorizationUserResourceList") is not None:
            self.AuthorizationUserResourceList = []
            for item in params.get("AuthorizationUserResourceList"):
                obj = AuthorizationUserResouceInfo()
                obj._deserialize(item)
                self.AuthorizationUserResourceList.append(obj)
        self.RequestId = params.get("RequestId")


class InheritedForm(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        r"""
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
        


class ListApplicationAuthorizationsRequest(AbstractModel):
    """ListApplicationAuthorizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param EntityType: 查询类型，包含用户（User）、用户组（UserGroup）、组织机构（OrgNode）。
        :type EntityType: str
        :param SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AuthorizationInfoSearchCriteria`
        :param Sort: 排序条件集合。可排序的属性支持：上次修改时间（lastModifiedDate）。如果该字段为空，则默认按照应用名称正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: 分页偏移量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Offset: int
        :param Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        """
        self.EntityType = None
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EntityType = params.get("EntityType")
        if params.get("SearchCondition") is not None:
            self.SearchCondition = AuthorizationInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationAuthorizationsResponse(AbstractModel):
    """ListApplicationAuthorizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuthorizationInfoList: 返回的应用授权信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationInfoList: list of AuthorizationInfo
        :param TotalCount: 返回的应用信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthorizationInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuthorizationInfoList") is not None:
            self.AuthorizationInfoList = []
            for item in params.get("AuthorizationInfoList"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self.AuthorizationInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListApplicationsRequest(AbstractModel):
    """ListApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ApplicationInfoSearchCriteria`
        :param Sort: 排序条件集合。可排序的属性支持：应用名字（displayName）、创建时间（createdDate）、上次修改时间（lastModifiedDate）。如果该字段为空，则默认按照应用名字正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: 分页偏移量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Offset: int
        :param Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        """
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = ApplicationInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationsResponse(AbstractModel):
    """ListApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的应用信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApplicationInfoList: 返回的应用信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationInfoList: list of ApplicationInformation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApplicationInfoList") is not None:
            self.ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInformation()
                obj._deserialize(item)
                self.ApplicationInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToOrgNodeRequest(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param UserId: 用户 ID。
        :type UserId: str
        :param IncludeInheritedAuthorizations: 查询范围是否包括用户关联的用户组、组织机构的应用访问权限。默认为不查询 。传false表示不查询该范围，传true表示应用查询该范围。
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
        r"""
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
        r"""
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
        r"""
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


class ListUserGroupsRequest(AbstractModel):
    """ListUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInfoSearchCriteria`
        :param Sort: 排序条件集合。可排序的属性支持：用户组名称（DisplayName）、用户组ID（UserGroupId）、上次更新时间（LastModifiedDate）。如果该字段为空，则默认按照用户组名称正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: 分页偏移量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Offset: int
        :param Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        """
        self.SearchCondition = None
        self.Sort = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserGroupInfoSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsResponse(AbstractModel):
    """ListUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserGroupList: 返回的用户组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupList: list of UserGroupInformation
        :param TotalCount: 返回的用户组信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserGroupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserGroupList") is not None:
            self.UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserGroupInformation()
                obj._deserialize(item)
                self.UserGroupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListUsersInOrgNodeRequest(AbstractModel):
    """ListUsersInOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点下用户信息。
        :type OrgNodeId: str
        :param IncludeOrgNodeChildInfo: 是否读取其子节点信息。当其为空或false时，默认仅读取当前机构节点信息。当其为true时，读取本机构节点以及其第一层子节点信息。
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
        r"""
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
        r"""
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
        r"""
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


class ListUsersRequest(AbstractModel):
    """ListUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchCondition: 用户属性搜索条件，可查询条件包括：用户名、手机号码，邮箱、用户锁定状态、用户冻结状态、创建时间、上次修改时间，支持多种属性组合作为查询条件。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（*）结尾表示字段部分匹配、中括号以逗号分隔（[Min，Max]）表示闭区间查询、大括号以逗号分隔（{Min，Max}）表示开区间查询，中括号与大括号可以配合使用（例如：{Min，Max]表示最小值开区间，最大值闭区间查询）。范围匹配支持使用星号（例如{20,*]表示查询范围为大于20的所有数据）。范围查询同时支持时间段查询，支持的属性包括创建时间 （CreationTime）、上次修改时间（LastUpdateTime），查询的时间格式遵循 ISO 8601 标准，例如：2021-01-13T09:44:07.182+0000。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param ExpectedFields: 指定期望返回的用户属性，默认返回所有用户内置属性。内置用户属性包括：用户UUID（UserId）、用户昵称（DisplayName）、用户名字（UserName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、用户组（SubjectGroups）机构路径（OrgPath）、备注（Description）、创建时间 （CreationTime）、上次修改时间（LastUpdateTime）、上次登录时间（LastLoginTime）。
        :type ExpectedFields: list of str
        :param Sort: 排序条件集合。可排序的属性支持：用户名字（UserName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、创建时间 （CreationTime）、上次修改时间（LastUpdateTime）、上次登录时间（LastLoginTime）。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param Offset: 分页偏移量，默认为0。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多1000个用户。
        :type Offset: int
        :param Limit: 分页读取数量，默认为50，最大值为100。 Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多1000个用户。
        :type Limit: int
        :param IncludeTotal: 是否查看搜索结果的总数，默认该选项为false不查看。
        :type IncludeTotal: bool
        """
        self.SearchCondition = None
        self.ExpectedFields = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.IncludeTotal = None


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self.SearchCondition = UserSearchCriteria()
            self.SearchCondition._deserialize(params.get("SearchCondition"))
        self.ExpectedFields = params.get("ExpectedFields")
        if params.get("Sort") is not None:
            self.Sort = SortCondition()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IncludeTotal = params.get("IncludeTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersResponse(AbstractModel):
    """ListUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserList: 查询返回的相关用户列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param TotalCount: 返回查询用户的总数量，仅当入参IncludeTotal等于true时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        :param SecureLevel: 安全级别。
        :type SecureLevel: str
        :param DisplayName: 应用展示名称，长度限制：32个字符。 默认与应用名字相同。
        :type DisplayName: str
        :param AppStatus: 应用状态，true表示启用，false表示禁用。
        :type AppStatus: bool
        :param IconUrl: 应用图标图片访问地址。
        :type IconUrl: str
        :param Description: 描述。长度不超过128。
        :type Description: str
        """
        self.ApplicationId = None
        self.SecureLevel = None
        self.DisplayName = None
        self.AppStatus = None
        self.IconUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SecureLevel = params.get("SecureLevel")
        self.DisplayName = params.get("DisplayName")
        self.AppStatus = params.get("AppStatus")
        self.IconUrl = params.get("IconUrl")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserInfoRequest(AbstractModel):
    """ModifyUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SortCondition(AbstractModel):
    """排序条件。

    """

    def __init__(self):
        r"""
        :param SortKey: 排序属性。
        :type SortKey: str
        :param SortOrder: 排序顺序，ASC为正向排序，DESC为反向排序。
        :type SortOrder: str
        """
        self.SortKey = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.SortKey = params.get("SortKey")
        self.SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeRequest(AbstractModel):
    """UpdateOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserGroupInfoSearchCriteria(AbstractModel):
    """用户组属性搜索条件。

    """

    def __init__(self):
        r"""
        :param Keyword: 名称匹配搜索，匹配范围包括：用户组名称、用户组ID。
        :type Keyword: str
        """
        self.Keyword = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformation(AbstractModel):
    """返回的用户组列表。

    """

    def __init__(self):
        r"""
        :param UserGroupId: 用户组ID。
        :type UserGroupId: str
        :param UserGroupName: 用户组名称。
        :type UserGroupName: str
        :param LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        """
        self.UserGroupId = None
        self.UserGroupName = None
        self.LastModifiedDate = None


    def _deserialize(self, params):
        self.UserGroupId = params.get("UserGroupId")
        self.UserGroupName = params.get("UserGroupName")
        self.LastModifiedDate = params.get("LastModifiedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息列表。

    """

    def __init__(self):
        r"""
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
        


class UserInformation(AbstractModel):
    """用户信息列表。

    """

    def __init__(self):
        r"""
        :param UserName: 用户名，长度限制：32个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param Status: 用户状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param Description: 用户备注，长度限制：512个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param LastUpdateTime: 用户上次更新时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param CreationTime: 用户创建时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param OrgPath: 用户所属组织机构路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPath: str
        :param Phone: 带国家号的用户手机号，例如+86-00000000000。
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param SubjectGroups: 用户所属用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectGroups: list of str
        :param Email: 用户邮箱。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param LastLoginTime: 用户上次登录时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLoginTime: str
        :param UserId: 用户ID，是用户全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        """
        self.UserName = None
        self.Status = None
        self.DisplayName = None
        self.Description = None
        self.LastUpdateTime = None
        self.CreationTime = None
        self.OrgPath = None
        self.Phone = None
        self.SubjectGroups = None
        self.Email = None
        self.LastLoginTime = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Status = params.get("Status")
        self.DisplayName = params.get("DisplayName")
        self.Description = params.get("Description")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.CreationTime = params.get("CreationTime")
        self.OrgPath = params.get("OrgPath")
        self.Phone = params.get("Phone")
        self.SubjectGroups = params.get("SubjectGroups")
        self.Email = params.get("Email")
        self.LastLoginTime = params.get("LastLoginTime")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSearchCriteria(AbstractModel):
    """用户属性搜索条件。

    """

    def __init__(self):
        r"""
        :param UserName: 用户名，长度限制：64个字符。
        :type UserName: str
        :param Phone: 用户手机号。
        :type Phone: str
        :param Email: 用户邮箱。
        :type Email: str
        :param Status: 用户状态，取值 NORMAL （正常）、FREEZE （已冻结）、LOCKED （已锁定）或 NOT_ENABLED （未启用）。
        :type Status: str
        :param CreationTime: 用户创建时间，遵循 ISO 8601 标准。
        :type CreationTime: str
        :param LastUpdateTime: 用户上次更新时间区间。
        :type LastUpdateTime: str
        :param Keyword: 名称匹配搜索，匹配范围包括：用户名称、用户ID。
        :type Keyword: str
        """
        self.UserName = None
        self.Phone = None
        self.Email = None
        self.Status = None
        self.CreationTime = None
        self.LastUpdateTime = None
        self.Keyword = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        self.CreationTime = params.get("CreationTime")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        