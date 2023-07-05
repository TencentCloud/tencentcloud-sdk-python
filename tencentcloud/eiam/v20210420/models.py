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


class AccountGroupInfo(AbstractModel):
    """查询账号组信息列表。

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID。
        :type AccountGroupId: str
        :param _GroupName: 账号组名。
        :type GroupName: str
        :param _Description: 备注。
        :type Description: str
        :param _CreatedDate: 创建时间。
        :type CreatedDate: str
        """
        self._AccountGroupId = None
        self._GroupName = None
        self._Description = None
        self._CreatedDate = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroupSearchCriteria(AbstractModel):
    """账号组查询参数

    """

    def __init__(self):
        r"""
        :param _Keyword: 关键字
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupRequest(AbstractModel):
    """AddAccountToAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _AccountIds: 加入账号组的账号ID列表。
        :type AccountIds: list of str
        """
        self._AccountGroupId = None
        self._AccountIds = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAccountToAccountGroupResponse(AbstractModel):
    """AddAccountToAccountGroup返回参数结构体

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


class AddUserToUserGroupRequest(AbstractModel):
    """AddUserToUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: 加入用户组的用户ID列表。
        :type UserIds: list of str
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self._UserIds = None
        self._UserGroupId = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToUserGroupResponse(AbstractModel):
    """AddUserToUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedItems: 未成功加入用户组的用户ID列表信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedItems = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._RequestId = params.get("RequestId")


class AppAccountInfo(AbstractModel):
    """查询账号信息列表。

    """

    def __init__(self):
        r"""
        :param _AccountId: 账号ID。
        :type AccountId: str
        :param _AccountName: 账号名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _UserList: 用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of LinkUserInfo
        :param _Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreatedDate: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        """
        self._AccountId = None
        self._AccountName = None
        self._UserList = None
        self._Description = None
        self._CreatedDate = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._AccountName = params.get("AccountName")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = LinkUserInfo()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAccountSearchCriteria(AbstractModel):
    """账号查询参数

    """

    def __init__(self):
        r"""
        :param _Keyword: 关键字
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationAuthorizationInfo(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        r"""
        :param _ApplicationAccounts: 用户在被授权应用下对应的账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param _ApplicationId: 应用ID，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _InheritedForm: 展示用户所在的用户组、机构节点拥有该应用的访问权限的ID信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param _ApplicationName: 应用名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param _CreatedDate: 应用创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        """
        self._ApplicationAccounts = None
        self._ApplicationId = None
        self._InheritedForm = None
        self._ApplicationName = None
        self._CreatedDate = None

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def InheritedForm(self):
        return self._InheritedForm

    @InheritedForm.setter
    def InheritedForm(self, InheritedForm):
        self._InheritedForm = InheritedForm

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("InheritedForm") is not None:
            self._InheritedForm = InheritedForm()
            self._InheritedForm._deserialize(params.get("InheritedForm"))
        self._ApplicationName = params.get("ApplicationName")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInfoSearchCriteria(AbstractModel):
    """应用属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _Keyword: 应用匹配搜索关键字，匹配范围包括：应用名称、应用ID。
        :type Keyword: str
        :param _ApplicationType: 应用类型。ApplicationType的取值范围有：OAUTH2、JWT、CAS、SAML2、FORM、OIDC、APIGW。
        :type ApplicationType: str
        """
        self._Keyword = None
        self._ApplicationType = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._ApplicationType = params.get("ApplicationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInformation(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        :param _DisplayName: 应用展示名称，长度限制：64个字符。 默认与应用名字相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _CreatedDate: 应用创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param _LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param _AppStatus: 应用状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: bool
        :param _Icon: 应用图标。
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param _ApplicationType: 应用类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param _ClientId: 客户端id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        """
        self._ApplicationId = None
        self._DisplayName = None
        self._CreatedDate = None
        self._LastModifiedDate = None
        self._AppStatus = None
        self._Icon = None
        self._ApplicationType = None
        self._ClientId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._DisplayName = params.get("DisplayName")
        self._CreatedDate = params.get("CreatedDate")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._AppStatus = params.get("AppStatus")
        self._Icon = params.get("Icon")
        self._ApplicationType = params.get("ApplicationType")
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfo(AbstractModel):
    """返回的授权关系信息。

    """

    def __init__(self):
        r"""
        :param _AppId: 应用唯一ID。
        :type AppId: str
        :param _AppName: 应用名称。
        :type AppName: str
        :param _EntityName: 类型名称。
        :type EntityName: str
        :param _EntityId: 类型唯一ID。
        :type EntityId: str
        :param _LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
        :type LastModifiedDate: str
        :param _AuthorizationId: 授权类型唯一ID。
        :type AuthorizationId: str
        """
        self._AppId = None
        self._AppName = None
        self._EntityName = None
        self._EntityId = None
        self._LastModifiedDate = None
        self._AuthorizationId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def EntityName(self):
        return self._EntityName

    @EntityName.setter
    def EntityName(self, EntityName):
        self._EntityName = EntityName

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def AuthorizationId(self):
        return self._AuthorizationId

    @AuthorizationId.setter
    def AuthorizationId(self, AuthorizationId):
        self._AuthorizationId = AuthorizationId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._EntityName = params.get("EntityName")
        self._EntityId = params.get("EntityId")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._AuthorizationId = params.get("AuthorizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfoSearchCriteria(AbstractModel):
    """用户属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _Keyword: 名称匹配搜索，当查询类型为用户时，匹配范围包括：用户名称、应用名称；当查询类型为用户组时，匹配范围包括：用户组名称、应用名称；当查询类型为组织机构时，匹配范围包括：组织机构名称、应用名称。
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationResourceEntityInfo(AbstractModel):
    """授权资源详情

    """

    def __init__(self):
        r"""
        :param _ResourceId: 授权关系的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceType: 资源授权类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Resource: 授权的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Resource = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Resource = params.get("Resource")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationUserResouceInfo(AbstractModel):
    """返回符合条件的用户数据列表

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Resource: 授权资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _InheritedForm: 继承关系
注意：此字段可能返回 null，表示取不到有效值。
        :type InheritedForm: :class:`tencentcloud.eiam.v20210420.models.InheritedForm`
        :param _ApplicationAccounts: 应用账户
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param _ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Resource = None
        self._InheritedForm = None
        self._ApplicationAccounts = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def InheritedForm(self):
        return self._InheritedForm

    @InheritedForm.setter
    def InheritedForm(self, InheritedForm):
        self._InheritedForm = InheritedForm

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Resource = params.get("Resource")
        if params.get("InheritedForm") is not None:
            self._InheritedForm = InheritedForm()
            self._InheritedForm._deserialize(params.get("InheritedForm"))
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupRequest(AbstractModel):
    """CreateAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _GroupName: 账号组名。
        :type GroupName: str
        :param _Description: 描述。
        :type Description: str
        """
        self._ApplicationId = None
        self._GroupName = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountGroupResponse(AbstractModel):
    """CreateAccountGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountGroupId = None
        self._RequestId = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._RequestId = params.get("RequestId")


class CreateAppAccountRequest(AbstractModel):
    """CreateAppAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _AccountName: 账号名称
        :type AccountName: str
        :param _Password: 账号密码
        :type Password: str
        :param _Description: 描述
        :type Description: str
        """
        self._ApplicationId = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppAccountResponse(AbstractModel):
    """CreateAppAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountId: 账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountId = None
        self._RequestId = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._RequestId = params.get("RequestId")


class CreateOrgNodeRequest(AbstractModel):
    """CreateOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: 机构节点名称，长度限制：64个字符。
        :type DisplayName: str
        :param _ParentOrgNodeId: 父机构节点ID，如果为空则默认创建在机构根节点下。
        :type ParentOrgNodeId: str
        :param _Description: 机构节点描述。
        :type Description: str
        :param _CustomizedOrgNodeId: 机构代码。如果为空，则默认生成机构代码。如果为非空，则校验机构代码的唯一性。
        :type CustomizedOrgNodeId: str
        """
        self._DisplayName = None
        self._ParentOrgNodeId = None
        self._Description = None
        self._CustomizedOrgNodeId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._Description = params.get("Description")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgNodeResponse(AbstractModel):
    """CreateOrgNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgNodeId = None
        self._RequestId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: 用户组昵称，长度限制：64个字符。 DisplayName是唯一的。
        :type DisplayName: str
        :param _Description: 用户组备注，长度限制：512个字符。
        :type Description: str
        """
        self._DisplayName = None
        self._Description = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserGroupResponse(AbstractModel):
    """CreateUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupId = None
        self._RequestId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：64个字符。
        :type UserName: str
        :param _Password: 用户密码， 需要符合密码策略的配置。
        :type Password: str
        :param _DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
        :type DisplayName: str
        :param _Description: 用户备注，长度限制：512个字符。
        :type Description: str
        :param _UserGroupIds: 用户所属用户组ID列表。
        :type UserGroupIds: list of str
        :param _Phone: 用户手机号。例如：+86-1xxxxxxxxxx。
        :type Phone: str
        :param _OrgNodeId: 用户所属的主组织机构唯一ID。如果为空，默认为在根节点下创建用户。
        :type OrgNodeId: str
        :param _ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
        :type ExpirationTime: str
        :param _Email: 用户邮箱。
        :type Email: str
        :param _PwdNeedReset: 密码是否需要重置，为空默认为false不需要重置密码。
        :type PwdNeedReset: bool
        :param _SecondaryOrgNodeIdList: 用户所属的次要组织机构ID列表。
        :type SecondaryOrgNodeIdList: list of str
        """
        self._UserName = None
        self._Password = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._Phone = None
        self._OrgNodeId = None
        self._ExpirationTime = None
        self._Email = None
        self._PwdNeedReset = None
        self._SecondaryOrgNodeIdList = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._Phone = params.get("Phone")
        self._OrgNodeId = params.get("OrgNodeId")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Email = params.get("Email")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 返回的新创建的用户ID，是该用户的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class DeleteAccountGroupRequest(AbstractModel):
    """DeleteAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupIdList: 账号组ID数组。
        :type AccountGroupIdList: list of str
        """
        self._AccountGroupIdList = None

    @property
    def AccountGroupIdList(self):
        return self._AccountGroupIdList

    @AccountGroupIdList.setter
    def AccountGroupIdList(self, AccountGroupIdList):
        self._AccountGroupIdList = AccountGroupIdList


    def _deserialize(self, params):
        self._AccountGroupIdList = params.get("AccountGroupIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountGroupResponse(AbstractModel):
    """DeleteAccountGroup返回参数结构体

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


class DeleteAppAccountRequest(AbstractModel):
    """DeleteAppAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountIdList: 账号ID数组。
        :type AccountIdList: list of str
        """
        self._AccountIdList = None

    @property
    def AccountIdList(self):
        return self._AccountIdList

    @AccountIdList.setter
    def AccountIdList(self, AccountIdList):
        self._AccountIdList = AccountIdList


    def _deserialize(self, params):
        self._AccountIdList = params.get("AccountIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppAccountResponse(AbstractModel):
    """DeleteAppAccount返回参数结构体

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


class DeleteOrgNodeRequest(AbstractModel):
    """DeleteOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
        :type OrgNodeId: str
        """
        self._OrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrgNodeResponse(AbstractModel):
    """DeleteOrgNode返回参数结构体

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


class DeleteUserGroupRequest(AbstractModel):
    """DeleteUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupResponse(AbstractModel):
    """DeleteUserGroup返回参数结构体

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


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：32个字符。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserName: str
        :param _UserId: 用户 id。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

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


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteIdList: 被删除用户的ID列表。DeleteIdList 和 DeleteNameList 需至少一个不为空；都不为空时优先使用 DeleteNameList。
        :type DeleteIdList: list of str
        :param _DeleteNameList: 被删除用户的名称列表。DeleteIdList 和 DeleteNameList 需至少一个不为空；都不为空时优先使用 DeleteNameList。
        :type DeleteNameList: list of str
        """
        self._DeleteIdList = None
        self._DeleteNameList = None

    @property
    def DeleteIdList(self):
        return self._DeleteIdList

    @DeleteIdList.setter
    def DeleteIdList(self, DeleteIdList):
        self._DeleteIdList = DeleteIdList

    @property
    def DeleteNameList(self):
        return self._DeleteNameList

    @DeleteNameList.setter
    def DeleteNameList(self, DeleteNameList):
        self._DeleteNameList = DeleteNameList


    def _deserialize(self, params):
        self._DeleteIdList = params.get("DeleteIdList")
        self._DeleteNameList = params.get("DeleteNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    """DeleteUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedItems: 未被成功删除的用户信息。当业务参数为DeleteIdList时，本字段将返回未成功删除的用户ID列表。当业务参数为DeleteNameList时，本字段将返回未成功删除的用户名称列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedItems = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._RequestId = params.get("RequestId")


class DescribeAccountGroupRequest(AbstractModel):
    """DescribeAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（*）结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._ApplicationId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AccountGroupSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupResponse(AbstractModel):
    """DescribeAccountGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回查询的总记录数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApplicationId: 应用ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _AccountGroupList: 返回符合条件的数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupList: list of AccountGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationId = None
        self._AccountGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AccountGroupList(self):
        return self._AccountGroupList

    @AccountGroupList.setter
    def AccountGroupList(self, AccountGroupList):
        self._AccountGroupList = AccountGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("AccountGroupList") is not None:
            self._AccountGroupList = []
            for item in params.get("AccountGroupList"):
                obj = AccountGroupInfo()
                obj._deserialize(item)
                self._AccountGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAppAccountRequest(AbstractModel):
    """DescribeAppAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（*）结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AppAccountSearchCriteria`
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._ApplicationId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AppAccountSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppAccountResponse(AbstractModel):
    """DescribeAppAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回查询的总记录数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApplicationId: 应用ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _AppAccountList: 返回符合条件的数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppAccountList: list of AppAccountInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationId = None
        self._AppAccountList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppAccountList(self):
        return self._AppAccountList

    @AppAccountList.setter
    def AppAccountList(self, AppAccountList):
        self._AppAccountList = AppAccountList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._ApplicationId = params.get("ApplicationId")
        if params.get("AppAccountList") is not None:
            self._AppAccountList = []
            for item in params.get("AppAccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self._AppAccountList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用id，是应用的全局唯一标识，与ClientId参数不能同时为空。
        :type ApplicationId: str
        :param _ClientId: 客户端id，与ApplicationId参数不能同时为空。
        :type ClientId: str
        """
        self._ApplicationId = None
        self._ClientId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥id。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param _DisplayName: 应用展示名称，长度限制：64个字符。 默认与应用名字相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _LastModifiedDate: 应用最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param _ClientId: 客户端id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _ApplicationType: 应用类型，即创建应用时所选择的应用模板类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param _CreatedDate: 应用创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param _ApplicationId: 应用id，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _TokenExpired: 令牌有效时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenExpired: int
        :param _ClientSecret: 客户端secret。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientSecret: str
        :param _PublicKey: 公钥信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param _AuthorizeUrl: 授权地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizeUrl: str
        :param _IconUrl: 应用图标图片访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param _SecureLevel: 安全等级。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecureLevel: str
        :param _AppStatus: 应用状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: bool
        :param _Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._DisplayName = None
        self._LastModifiedDate = None
        self._ClientId = None
        self._ApplicationType = None
        self._CreatedDate = None
        self._ApplicationId = None
        self._TokenExpired = None
        self._ClientSecret = None
        self._PublicKey = None
        self._AuthorizeUrl = None
        self._IconUrl = None
        self._SecureLevel = None
        self._AppStatus = None
        self._Description = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def TokenExpired(self):
        return self._TokenExpired

    @TokenExpired.setter
    def TokenExpired(self, TokenExpired):
        self._TokenExpired = TokenExpired

    @property
    def ClientSecret(self):
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def AuthorizeUrl(self):
        return self._AuthorizeUrl

    @AuthorizeUrl.setter
    def AuthorizeUrl(self, AuthorizeUrl):
        self._AuthorizeUrl = AuthorizeUrl

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._ClientId = params.get("ClientId")
        self._ApplicationType = params.get("ApplicationType")
        self._CreatedDate = params.get("CreatedDate")
        self._ApplicationId = params.get("ApplicationId")
        self._TokenExpired = params.get("TokenExpired")
        self._ClientSecret = params.get("ClientSecret")
        self._PublicKey = params.get("PublicKey")
        self._AuthorizeUrl = params.get("AuthorizeUrl")
        self._IconUrl = params.get("IconUrl")
        self._SecureLevel = params.get("SecureLevel")
        self._AppStatus = params.get("AppStatus")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeOrgNodeRequest(AbstractModel):
    """DescribeOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点信息。
        :type OrgNodeId: str
        :param _IncludeOrgNodeChildInfo: 是否读取其子节点信息。当其为空或false时，默认仅读取当前机构节点信息。当其为true时，读取本机构节点以及其第一层子节点信息。
        :type IncludeOrgNodeChildInfo: bool
        """
        self._OrgNodeId = None
        self._IncludeOrgNodeChildInfo = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def IncludeOrgNodeChildInfo(self):
        return self._IncludeOrgNodeChildInfo

    @IncludeOrgNodeChildInfo.setter
    def IncludeOrgNodeChildInfo(self, IncludeOrgNodeChildInfo):
        self._IncludeOrgNodeChildInfo = IncludeOrgNodeChildInfo


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgNodeResponse(AbstractModel):
    """DescribeOrgNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: 机构节点展示名称，长度限制：64个字符。 默认与机构名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _LastModifiedDate: 机构节点最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param _CustomizedOrgNodeId: 机构节点外部ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizedOrgNodeId: str
        :param _ParentOrgNodeId: 当前机构节点的父节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentOrgNodeId: str
        :param _OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _CreatedDate: 机构节点创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param _OrgNodeChildInfo: 当前机构节点下的子节点列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeChildInfo: list of OrgNodeChildInfo
        :param _Description: 机构节点描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DisplayName = None
        self._LastModifiedDate = None
        self._CustomizedOrgNodeId = None
        self._ParentOrgNodeId = None
        self._OrgNodeId = None
        self._DataSource = None
        self._CreatedDate = None
        self._OrgNodeChildInfo = None
        self._Description = None
        self._RequestId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def OrgNodeChildInfo(self):
        return self._OrgNodeChildInfo

    @OrgNodeChildInfo.setter
    def OrgNodeChildInfo(self, OrgNodeChildInfo):
        self._OrgNodeChildInfo = OrgNodeChildInfo

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._CreatedDate = params.get("CreatedDate")
        if params.get("OrgNodeChildInfo") is not None:
            self._OrgNodeChildInfo = []
            for item in params.get("OrgNodeChildInfo"):
                obj = OrgNodeChildInfo()
                obj._deserialize(item)
                self._OrgNodeChildInfo.append(obj)
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeOrgResourcesAuthorizationRequest(AbstractModel):
    """DescribeOrgResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _OrgNodeId: 机构ID
        :type OrgNodeId: str
        """
        self._ApplicationId = None
        self._OrgNodeId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrgResourcesAuthorizationResponse(AbstractModel):
    """DescribeOrgResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _OrgNodeId: 授权机构ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _OrgNodeName: 机构名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeName: str
        :param _OrgNodePath: 机构目录
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodePath: str
        :param _AuthorizationOrgResourceList: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationOrgResourceList: list of AuthorizationResourceEntityInfo
        :param _TotalCount: 资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._OrgNodeId = None
        self._OrgNodeName = None
        self._OrgNodePath = None
        self._AuthorizationOrgResourceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def OrgNodeName(self):
        return self._OrgNodeName

    @OrgNodeName.setter
    def OrgNodeName(self, OrgNodeName):
        self._OrgNodeName = OrgNodeName

    @property
    def OrgNodePath(self):
        return self._OrgNodePath

    @OrgNodePath.setter
    def OrgNodePath(self, OrgNodePath):
        self._OrgNodePath = OrgNodePath

    @property
    def AuthorizationOrgResourceList(self):
        return self._AuthorizationOrgResourceList

    @AuthorizationOrgResourceList.setter
    def AuthorizationOrgResourceList(self, AuthorizationOrgResourceList):
        self._AuthorizationOrgResourceList = AuthorizationOrgResourceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._OrgNodeId = params.get("OrgNodeId")
        self._OrgNodeName = params.get("OrgNodeName")
        self._OrgNodePath = params.get("OrgNodePath")
        if params.get("AuthorizationOrgResourceList") is not None:
            self._AuthorizationOrgResourceList = []
            for item in params.get("AuthorizationOrgResourceList"):
                obj = AuthorizationResourceEntityInfo()
                obj._deserialize(item)
                self._AuthorizationOrgResourceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePublicKeyRequest(AbstractModel):
    """DescribePublicKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicKeyResponse(AbstractModel):
    """DescribePublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PublicKey: jwt验证签名所用的公钥信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param _KeyId: jwt的密钥id。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param _ApplicationId: 应用ID，是应用的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PublicKey = None
        self._KeyId = None
        self._ApplicationId = None
        self._RequestId = None

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._KeyId = params.get("KeyId")
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class DescribeUserGroupRequest(AbstractModel):
    """DescribeUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserGroupResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _UserGroupId: 用户组ID
        :type UserGroupId: str
        """
        self._ApplicationId = None
        self._UserGroupId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserGroupResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param _UserGroupId: 用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param _UserGroupName: 用户组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupName: str
        :param _AuthorizationUserGroupResourceList: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationUserGroupResourceList: list of AuthorizationResourceEntityInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._UserGroupId = None
        self._UserGroupName = None
        self._AuthorizationUserGroupResourceList = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def UserGroupName(self):
        return self._UserGroupName

    @UserGroupName.setter
    def UserGroupName(self, UserGroupName):
        self._UserGroupName = UserGroupName

    @property
    def AuthorizationUserGroupResourceList(self):
        return self._AuthorizationUserGroupResourceList

    @AuthorizationUserGroupResourceList.setter
    def AuthorizationUserGroupResourceList(self, AuthorizationUserGroupResourceList):
        self._AuthorizationUserGroupResourceList = AuthorizationUserGroupResourceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._UserGroupId = params.get("UserGroupId")
        self._UserGroupName = params.get("UserGroupName")
        if params.get("AuthorizationUserGroupResourceList") is not None:
            self._AuthorizationUserGroupResourceList = []
            for item in params.get("AuthorizationUserGroupResourceList"):
                obj = AuthorizationResourceEntityInfo()
                obj._deserialize(item)
                self._AuthorizationUserGroupResourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserGroupResponse(AbstractModel):
    """DescribeUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: 用户组昵称，长度限制：64个字符。 DisplayName不唯一。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _Description: 用户组备注，长度限制：512个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DisplayName = None
        self._Description = None
        self._UserGroupId = None
        self._RequestId = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupId = params.get("UserGroupId")
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：64个字符。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserName: str
        :param _UserId: 用户 id，长度限制：64个字符。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Status: 用户状态，取值 NORMAL （正常）、FREEZE （已冻结）、LOCKED （已锁定）或 NOT_ENABLED （未启用）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _DisplayName: 昵称。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _Description: 用户备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _UserGroupIds: 用户所属用户组 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param _UserId: 用户 id，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Email: 用户邮箱。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Phone: 用户手机号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _OrgNodeId: 用户所属的主组织机构唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationTime: str
        :param _ActivationTime: 用户激活时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivationTime: str
        :param _PwdNeedReset: 当前用户的密码是否需要重置，该字段为false表示不需要重置密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PwdNeedReset: bool
        :param _SecondaryOrgNodeIdList: 用户所属的次要组织机构ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryOrgNodeIdList: list of str
        :param _AdminFlag: 是否管理员标志，0为否、1为是。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminFlag: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserName = None
        self._Status = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._UserId = None
        self._Email = None
        self._Phone = None
        self._OrgNodeId = None
        self._DataSource = None
        self._ExpirationTime = None
        self._ActivationTime = None
        self._PwdNeedReset = None
        self._SecondaryOrgNodeIdList = None
        self._AdminFlag = None
        self._RequestId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def ActivationTime(self):
        return self._ActivationTime

    @ActivationTime.setter
    def ActivationTime(self, ActivationTime):
        self._ActivationTime = ActivationTime

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList

    @property
    def AdminFlag(self):
        return self._AdminFlag

    @AdminFlag.setter
    def AdminFlag(self, AdminFlag):
        self._AdminFlag = AdminFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Status = params.get("Status")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._ExpirationTime = params.get("ExpirationTime")
        self._ActivationTime = params.get("ActivationTime")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        self._AdminFlag = params.get("AdminFlag")
        self._RequestId = params.get("RequestId")


class DescribeUserResourcesAuthorizationRequest(AbstractModel):
    """DescribeUserResourcesAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。
        :type ApplicationId: str
        :param _UserId: 用户ID。UserName 和 UserId 需至少一个不为空；都不为空时优先使用 UserName。
        :type UserId: str
        :param _UserName: 用户名。UserName 和 UserId 需至少一个不为空；都不为空时优先使用 UserName。
        :type UserName: str
        :param _IncludeInheritedAuthorizations: 查询范围是否包括用户关联的用户组、组织机构的应用访问权限。默认为不查询 ，传false表示不查询该范围，传true查询该范围。
        :type IncludeInheritedAuthorizations: bool
        """
        self._ApplicationId = None
        self._UserId = None
        self._UserName = None
        self._IncludeInheritedAuthorizations = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def IncludeInheritedAuthorizations(self):
        return self._IncludeInheritedAuthorizations

    @IncludeInheritedAuthorizations.setter
    def IncludeInheritedAuthorizations(self, IncludeInheritedAuthorizations):
        self._IncludeInheritedAuthorizations = IncludeInheritedAuthorizations


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResourcesAuthorizationResponse(AbstractModel):
    """DescribeUserResourcesAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用的唯一ID。
        :type ApplicationId: str
        :param _ApplicationAccounts: 应用账户。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAccounts: list of str
        :param _UserId: 授权用户的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _UserName: 授权的用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _AuthorizationUserResourceList: 返回的资源列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationUserResourceList: list of AuthorizationUserResouceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._ApplicationAccounts = None
        self._UserId = None
        self._UserName = None
        self._AuthorizationUserResourceList = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationAccounts(self):
        return self._ApplicationAccounts

    @ApplicationAccounts.setter
    def ApplicationAccounts(self, ApplicationAccounts):
        self._ApplicationAccounts = ApplicationAccounts

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AuthorizationUserResourceList(self):
        return self._AuthorizationUserResourceList

    @AuthorizationUserResourceList.setter
    def AuthorizationUserResourceList(self, AuthorizationUserResourceList):
        self._AuthorizationUserResourceList = AuthorizationUserResourceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationAccounts = params.get("ApplicationAccounts")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        if params.get("AuthorizationUserResourceList") is not None:
            self._AuthorizationUserResourceList = []
            for item in params.get("AuthorizationUserResourceList"):
                obj = AuthorizationUserResouceInfo()
                obj._deserialize(item)
                self._AuthorizationUserResourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserThirdPartyAccountInfoRequest(AbstractModel):
    """DescribeUserThirdPartyAccountInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserName: str
        :param _UserId: 用户 ID。 Username 和 UserId 需至少一个不为空；都不为空时优先使用 Username。
        :type UserId: str
        """
        self._UserName = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserThirdPartyAccountInfoResponse(AbstractModel):
    """DescribeUserThirdPartyAccountInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 id。
        :type UserId: str
        :param _UserName: 用户名。
        :type UserName: str
        :param _ThirdPartyAccounts: 三方账号的绑定情况。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdPartyAccounts: list of ThirdPartyAccountInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._UserName = None
        self._ThirdPartyAccounts = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ThirdPartyAccounts(self):
        return self._ThirdPartyAccounts

    @ThirdPartyAccounts.setter
    def ThirdPartyAccounts(self, ThirdPartyAccounts):
        self._ThirdPartyAccounts = ThirdPartyAccounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        if params.get("ThirdPartyAccounts") is not None:
            self._ThirdPartyAccounts = []
            for item in params.get("ThirdPartyAccounts"):
                obj = ThirdPartyAccountInfo()
                obj._deserialize(item)
                self._ThirdPartyAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class InheritedForm(AbstractModel):
    """应用信息列表。

    """

    def __init__(self):
        r"""
        :param _UserGroupIds: 用户所在的用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param _OrgNodeIds: 用户所在的机构节点ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeIds: list of str
        """
        self._UserGroupIds = None
        self._OrgNodeIds = None

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def OrgNodeIds(self):
        return self._OrgNodeIds

    @OrgNodeIds.setter
    def OrgNodeIds(self, OrgNodeIds):
        self._OrgNodeIds = OrgNodeIds


    def _deserialize(self, params):
        self._UserGroupIds = params.get("UserGroupIds")
        self._OrgNodeIds = params.get("OrgNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkUserInfo(AbstractModel):
    """账号关联的用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID，是用户全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _UserName: 用户名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._UserId = None
        self._UserName = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupRequest(AbstractModel):
    """ListAccountInAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID。
        :type AccountGroupId: str
        :param _SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AccountGroupSearchCriteria`
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._AccountGroupId = None
        self._SearchCondition = None
        self._Offset = None
        self._Limit = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

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


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AccountGroupSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountInAccountGroupResponse(AbstractModel):
    """ListAccountInAccountGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountList: 查询返回的相关账号列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountList: list of AppAccountInfo
        :param _TotalCount: 返回查询账号的总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _AccountGroupId: 账号组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountList = None
        self._TotalCount = None
        self._AccountGroupId = None
        self._RequestId = None

    @property
    def AccountList(self):
        return self._AccountList

    @AccountList.setter
    def AccountList(self, AccountList):
        self._AccountList = AccountList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountList") is not None:
            self._AccountList = []
            for item in params.get("AccountList"):
                obj = AppAccountInfo()
                obj._deserialize(item)
                self._AccountList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AccountGroupId = params.get("AccountGroupId")
        self._RequestId = params.get("RequestId")


class ListApplicationAuthorizationsRequest(AbstractModel):
    """ListApplicationAuthorizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EntityType: 查询类型，包含用户（User）、用户组（UserGroup）、组织机构（OrgNode）。
        :type EntityType: str
        :param _SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.AuthorizationInfoSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：上次修改时间（lastModifiedDate）。如果该字段为空，则默认按照应用名称正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Offset: int
        :param _Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        """
        self._EntityType = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def EntityType(self):
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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


    def _deserialize(self, params):
        self._EntityType = params.get("EntityType")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = AuthorizationInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationAuthorizationsResponse(AbstractModel):
    """ListApplicationAuthorizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthorizationInfoList: 返回的应用授权信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationInfoList: list of AuthorizationInfo
        :param _TotalCount: 返回的应用信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthorizationInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AuthorizationInfoList(self):
        return self._AuthorizationInfoList

    @AuthorizationInfoList.setter
    def AuthorizationInfoList(self, AuthorizationInfoList):
        self._AuthorizationInfoList = AuthorizationInfoList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthorizationInfoList") is not None:
            self._AuthorizationInfoList = []
            for item in params.get("AuthorizationInfoList"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self._AuthorizationInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListApplicationsRequest(AbstractModel):
    """ListApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchCondition: 模糊匹配搜索条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。模糊匹配搜索功能与精准匹配查询不会同时生效，如果SearchCondition与ApplicationIdList均不为空，则默认以ApplicationIdList进行精准查询。如果SearchCondition字段与ApplicationIdList字段均为空，则默认返回全部的应用信息。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ApplicationInfoSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：应用名字（DisplayName）、创建时间（CreatedDate）、上次修改时间（LastModifiedDate）。如果该字段为空，则默认按照应用名字正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 排序条件集合。可排序的属性支持：应用名字（DisplayName）、创建时间（CreatedDate）、上次修改时间（LastModifiedDate）。如果该字段为空，则默认按照应用名字正向排序。
        :type Offset: int
        :param _Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        :param _ApplicationIdList: 应用ID列表，通过应用ID列表精准匹配对应的应用信息。模糊匹配搜索功能与精准匹配查询不会同时生效，如果SearchCondition与ApplicationIdList均不为空，则默认以ApplicationIdList进行精准查询。如果SearchCondition字段与ApplicationIdList字段均为空，则默认返回全部的应用信息。
        :type ApplicationIdList: list of str
        """
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._ApplicationIdList = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
    def ApplicationIdList(self):
        return self._ApplicationIdList

    @ApplicationIdList.setter
    def ApplicationIdList(self, ApplicationIdList):
        self._ApplicationIdList = ApplicationIdList


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self._SearchCondition = ApplicationInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationIdList = params.get("ApplicationIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListApplicationsResponse(AbstractModel):
    """ListApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的应用信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApplicationInfoList: 返回的应用信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationInfoList: list of ApplicationInformation
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationInfoList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationInfoList(self):
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInformation()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToOrgNodeRequest(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点 Id 。
        :type OrgNodeId: str
        """
        self._OrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToOrgNodeResponse(AbstractModel):
    """ListAuthorizedApplicationsToOrgNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: 机构节点拥有访问权限的应用 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserGroupRequest(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组 Id 。
        :type UserGroupId: str
        """
        self._UserGroupId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserGroupResponse(AbstractModel):
    """ListAuthorizedApplicationsToUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: 用户组拥有访问权限的应用 id 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationIds = None
        self._RequestId = None

    @property
    def ApplicationIds(self):
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        self._RequestId = params.get("RequestId")


class ListAuthorizedApplicationsToUserRequest(AbstractModel):
    """ListAuthorizedApplicationsToUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _IncludeInheritedAuthorizations: 查询范围是否包括用户关联的用户组、组织机构的应用访问权限。默认为不查询 。传false表示不查询该范围，传true表示应用查询该范围。
        :type IncludeInheritedAuthorizations: bool
        """
        self._UserId = None
        self._IncludeInheritedAuthorizations = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IncludeInheritedAuthorizations(self):
        return self._IncludeInheritedAuthorizations

    @IncludeInheritedAuthorizations.setter
    def IncludeInheritedAuthorizations(self, IncludeInheritedAuthorizations):
        self._IncludeInheritedAuthorizations = IncludeInheritedAuthorizations


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._IncludeInheritedAuthorizations = params.get("IncludeInheritedAuthorizations")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAuthorizedApplicationsToUserResponse(AbstractModel):
    """ListAuthorizedApplicationsToUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationAuthorizationInfo: 用户拥有访问权限的应用信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationAuthorizationInfo: list of ApplicationAuthorizationInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationAuthorizationInfo = None
        self._RequestId = None

    @property
    def ApplicationAuthorizationInfo(self):
        return self._ApplicationAuthorizationInfo

    @ApplicationAuthorizationInfo.setter
    def ApplicationAuthorizationInfo(self, ApplicationAuthorizationInfo):
        self._ApplicationAuthorizationInfo = ApplicationAuthorizationInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationAuthorizationInfo") is not None:
            self._ApplicationAuthorizationInfo = []
            for item in params.get("ApplicationAuthorizationInfo"):
                obj = ApplicationAuthorizationInfo()
                obj._deserialize(item)
                self._ApplicationAuthorizationInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserGroupsOfUserRequest(AbstractModel):
    """ListUserGroupsOfUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID，是用户的全局唯一标识。
        :type UserId: str
        :param _SearchCondition: 模糊查询条件，支持匹配用户组名称（DisplayName）。如果该字段为空，则默认展示该用户所有的用户组。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInformationSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：用户组名称（DisplayName）、用户组ID（UserGroupId）、创建时间（CreatedDate）。如果该字段为空，则默认按照用户组名称正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量，默认为0。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户组。
        :type Offset: int
        :param _Limit: 分页读取数量，默认为50，最大值为100。 Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户组。
        :type Limit: int
        """
        self._UserId = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserGroupInformationSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsOfUserResponse(AbstractModel):
    """ListUserGroupsOfUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupIds: 用户所属的用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupIds: list of str
        :param _UserId: 用户ID，是用户的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _UserGroupInfoList: 用户所属的用户组信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupInfoList: list of UserGroupInfo
        :param _TotalCount: 返回的用户组信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupIds = None
        self._UserId = None
        self._UserGroupInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserGroupInfoList(self):
        return self._UserGroupInfoList

    @UserGroupInfoList.setter
    def UserGroupInfoList(self, UserGroupInfoList):
        self._UserGroupInfoList = UserGroupInfoList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        if params.get("UserGroupInfoList") is not None:
            self._UserGroupInfoList = []
            for item in params.get("UserGroupInfoList"):
                obj = UserGroupInfo()
                obj._deserialize(item)
                self._UserGroupInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListUserGroupsRequest(AbstractModel):
    """ListUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchCondition: 查询条件，支持多搜索条件组合、多数据范围匹配的搜索。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（""）表示全匹配、以星号（* ) 结尾表示字段部分匹配。如果该字段为空，则默认查全量表。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserGroupInfoSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：用户组名称（DisplayName）、用户组ID（UserGroupId）、上次更新时间（LastModifiedDate）。如果该字段为空，则默认按照用户组名称正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Offset: int
        :param _Limit: 分页读取数量。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询。
        :type Limit: int
        """
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserGroupInfoSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsResponse(AbstractModel):
    """ListUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupList: 返回的用户组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupList: list of UserGroupInformation
        :param _TotalCount: 返回的用户组信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserGroupList(self):
        return self._UserGroupList

    @UserGroupList.setter
    def UserGroupList(self, UserGroupList):
        self._UserGroupList = UserGroupList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserGroupList") is not None:
            self._UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserGroupInformation()
                obj._deserialize(item)
                self._UserGroupList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListUsersInOrgNodeRequest(AbstractModel):
    """ListUsersInOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点ID，是机构节点全局唯一标识，长度限制：64个字符。如果为空默认读取机构根节点下用户信息。
        :type OrgNodeId: str
        :param _IncludeOrgNodeChildInfo: 是否读取其子节点信息。当其为空或false时，默认仅读取当前机构节点信息。当其为true时，读取本机构节点以及其第一层子节点信息。
        :type IncludeOrgNodeChildInfo: bool
        :param _SearchCondition: 用户属性搜索条件，可查询条件包括：用户名、手机号码，邮箱、用户锁定状态、用户冻结状态、创建时间、上次修改时间，支持多种属性组合作为查询条件。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（*）结尾表示字段部分匹配、中括号以逗号分隔（[Min，Max]）表示闭区间查询、大括号以逗号分隔（{Min，Max}）表示开区间查询，中括号与大括号可以配合使用（例如：{Min，Max]表示最小值开区间，最大值闭区间查询）。范围匹配支持使用星号（例如{20,*]表示查询范围为大于20的所有数据）。范围查询同时支持时间段查询，支持的属性包括创建时间 （CreationTime）、上次修改时间（LastUpdateTime），查询的时间格式遵循 ISO 8601 标准，例如：2021-01-13T09:44:07.182+0000。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.ListUsersInOrgNodeSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：用户名字（UserName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、创建时间 （CreatedDate）、上次更新时间（LastModifiedDate）。如果不指定，则默认按照用户昵称（DisplayName）正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量，默认为0。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户。
        :type Offset: int
        :param _Limit: 分页读取数量，默认为50，最大值为100。 Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户。
        :type Limit: int
        """
        self._OrgNodeId = None
        self._IncludeOrgNodeChildInfo = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def IncludeOrgNodeChildInfo(self):
        return self._IncludeOrgNodeChildInfo

    @IncludeOrgNodeChildInfo.setter
    def IncludeOrgNodeChildInfo(self, IncludeOrgNodeChildInfo):
        self._IncludeOrgNodeChildInfo = IncludeOrgNodeChildInfo

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._IncludeOrgNodeChildInfo = params.get("IncludeOrgNodeChildInfo")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = ListUsersInOrgNodeSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInOrgNodeResponse(AbstractModel):
    """ListUsersInOrgNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeChildUserInfo: 机构子节点下的用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeChildUserInfo: list of OrgNodeChildUserInfo
        :param _OrgNodeId: 机构ID，是机构节点全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _UserInfo: 用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param _TotalUserNum: 当前机构节点下的用户总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUserNum: int
        :param _OrgNodeIdPath: 组织机构ID路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeIdPath: str
        :param _OrgNodeNamePath: 组织机构名称路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeNamePath: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgNodeChildUserInfo = None
        self._OrgNodeId = None
        self._UserInfo = None
        self._TotalUserNum = None
        self._OrgNodeIdPath = None
        self._OrgNodeNamePath = None
        self._RequestId = None

    @property
    def OrgNodeChildUserInfo(self):
        return self._OrgNodeChildUserInfo

    @OrgNodeChildUserInfo.setter
    def OrgNodeChildUserInfo(self, OrgNodeChildUserInfo):
        self._OrgNodeChildUserInfo = OrgNodeChildUserInfo

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalUserNum(self):
        return self._TotalUserNum

    @TotalUserNum.setter
    def TotalUserNum(self, TotalUserNum):
        self._TotalUserNum = TotalUserNum

    @property
    def OrgNodeIdPath(self):
        return self._OrgNodeIdPath

    @OrgNodeIdPath.setter
    def OrgNodeIdPath(self, OrgNodeIdPath):
        self._OrgNodeIdPath = OrgNodeIdPath

    @property
    def OrgNodeNamePath(self):
        return self._OrgNodeNamePath

    @OrgNodeNamePath.setter
    def OrgNodeNamePath(self, OrgNodeNamePath):
        self._OrgNodeNamePath = OrgNodeNamePath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OrgNodeChildUserInfo") is not None:
            self._OrgNodeChildUserInfo = []
            for item in params.get("OrgNodeChildUserInfo"):
                obj = OrgNodeChildUserInfo()
                obj._deserialize(item)
                self._OrgNodeChildUserInfo.append(obj)
        self._OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalUserNum = params.get("TotalUserNum")
        self._OrgNodeIdPath = params.get("OrgNodeIdPath")
        self._OrgNodeNamePath = params.get("OrgNodeNamePath")
        self._RequestId = params.get("RequestId")


class ListUsersInOrgNodeSearchCriteria(AbstractModel):
    """展示机构下用户的属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：64个字符。
        :type UserName: str
        :param _Phone: 用户手机号。
        :type Phone: str
        :param _Email: 用户邮箱。
        :type Email: str
        :param _Status: 用户状态，取值 NORMAL （正常）、FREEZE （已冻结）、LOCKED （已锁定）或 NOT_ENABLED （未启用）。
        :type Status: str
        :param _CreationTime: 用户创建时间，遵循 ISO 8601 标准。
        :type CreationTime: str
        :param _LastUpdateTime: 用户上次更新时间。
        :type LastUpdateTime: str
        :param _Keyword: 名称匹配搜索，匹配范围包括：用户名称、用户手机号。
        :type Keyword: str
        """
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._CreationTime = None
        self._LastUpdateTime = None
        self._Keyword = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._CreationTime = params.get("CreationTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupRequest(AbstractModel):
    """ListUsersInUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        :param _SearchCondition: 用户属性搜索条件，可查询条件包括：用户名、手机号码，邮箱、用户锁定状态、用户冻结状态、创建时间、上次修改时间，支持多种属性组合作为查询条件。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（）结尾表示字段部分匹配、中括号以逗号分隔（[Min，Max]）表示闭区间查询、大括号以逗号分隔（{Min，Max}）表示开区间查询，中括号与大括号可以配合使用（例如：{Min，Max]表示最小值开区间，最大值闭区间查询）。范围匹配支持使用星号（例如{20,]表示查询范围为大于20的所有数据）。范围查询同时支持时间段查询，支持的属性包括创建时间 （CreationTime）、上次修改时间（LastUpdateTime），查询的时间格式遵循 ISO 8601 标准，例如：2021-01-13T09:44:07.182+0000。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param _Sort: 排序条件集合。可排序的属性支持：用户名字（UserName）、用户昵称（DisplayName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、创建时间 （CreatedDate）、上次更新时间（LastModifiedDate）。如果不指定，则默认按照用户昵称（DisplayName）正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量，默认为0。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户。
        :type Offset: int
        :param _Limit: 分页读取数量，默认为50，最大值为100。 Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多50个用户。
        :type Limit: int
        """
        self._UserGroupId = None
        self._SearchCondition = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersInUserGroupResponse(AbstractModel):
    """ListUsersInUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param _UserInfo: 返回的用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param _TotalNum: 返回的用户信息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupId = None
        self._UserInfo = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchCondition: 用户属性搜索条件，可查询条件包括：用户名、手机号码，邮箱、用户锁定状态、用户冻结状态、创建时间、上次修改时间，支持多种属性组合作为查询条件。同时支持查询信息内容全匹配、部分匹配、范围匹配等多种查询方式，具体查询方式为：双引号（“”）表示全匹配、以星号（*）结尾表示字段部分匹配、中括号以逗号分隔（[Min，Max]）表示闭区间查询、大括号以逗号分隔（{Min，Max}）表示开区间查询，中括号与大括号可以配合使用（例如：{Min，Max]表示最小值开区间，最大值闭区间查询）。范围匹配支持使用星号（例如{20,*]表示查询范围为大于20的所有数据）。范围查询同时支持时间段查询，支持的属性包括创建时间 （CreationTime）、上次修改时间（LastUpdateTime），查询的时间格式遵循 ISO 8601 标准，例如：2021-01-13T09:44:07.182+0000。
        :type SearchCondition: :class:`tencentcloud.eiam.v20210420.models.UserSearchCriteria`
        :param _ExpectedFields: 指定期望返回的用户属性，默认返回所有用户内置属性。内置用户属性包括：用户UUID（UserId）、用户昵称（DisplayName）、用户名字（UserName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、用户组（SubjectGroups）机构路径（OrgPath）、备注（Description）、创建时间 （CreationTime）、上次修改时间（LastUpdateTime）、上次登录时间（LastLoginTime）。
        :type ExpectedFields: list of str
        :param _Sort: 排序条件集合。可排序的属性支持：用户名字（UserName）、用户昵称（DisplayName）、手机号（Phone）、邮箱（Email）、用户状态（Status）、创建时间 （CreationTime）、上次修改时间（LastUpdateTime）、上次登录时间（LastLoginTime）。如果不指定，则默认按照用户昵称（DisplayName）正向排序。
        :type Sort: :class:`tencentcloud.eiam.v20210420.models.SortCondition`
        :param _Offset: 分页偏移量，默认为0。Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多1000个用户。
        :type Offset: int
        :param _Limit: 分页读取数量，默认为50，最大值为100。 Offset 和 Limit 两个字段需配合使用，即其中一个指定了，另一个必须指定。 如果不指定以上参数，则表示不进行分页查询，即只返回最多1000个用户。
        :type Limit: int
        :param _IncludeTotal: 是否查看搜索结果的总数，默认该选项为false不查看。
        :type IncludeTotal: bool
        """
        self._SearchCondition = None
        self._ExpectedFields = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._IncludeTotal = None

    @property
    def SearchCondition(self):
        return self._SearchCondition

    @SearchCondition.setter
    def SearchCondition(self, SearchCondition):
        self._SearchCondition = SearchCondition

    @property
    def ExpectedFields(self):
        return self._ExpectedFields

    @ExpectedFields.setter
    def ExpectedFields(self, ExpectedFields):
        self._ExpectedFields = ExpectedFields

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

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
    def IncludeTotal(self):
        return self._IncludeTotal

    @IncludeTotal.setter
    def IncludeTotal(self, IncludeTotal):
        self._IncludeTotal = IncludeTotal


    def _deserialize(self, params):
        if params.get("SearchCondition") is not None:
            self._SearchCondition = UserSearchCriteria()
            self._SearchCondition._deserialize(params.get("SearchCondition"))
        self._ExpectedFields = params.get("ExpectedFields")
        if params.get("Sort") is not None:
            self._Sort = SortCondition()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IncludeTotal = params.get("IncludeTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersResponse(AbstractModel):
    """ListUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserList: 查询返回的相关用户列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param _TotalCount: 返回查询用户的总数量，仅当入参IncludeTotal等于true时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ModifyAccountGroupRequest(AbstractModel):
    """ModifyAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID。
        :type AccountGroupId: str
        :param _GroupName: 账号组名。未传入该参数时，表示不进行修改。
        :type GroupName: str
        :param _Description: 描述，未传入该参数时，表示不进行修改。
        :type Description: str
        """
        self._AccountGroupId = None
        self._GroupName = None
        self._Description = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountGroupResponse(AbstractModel):
    """ModifyAccountGroup返回参数结构体

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


class ModifyAppAccountRequest(AbstractModel):
    """ModifyAppAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountId: 账号ID。
        :type AccountId: str
        :param _AccountName: 账号名称。未传入该参数时，表示不进行修改。
        :type AccountName: str
        :param _Password: 账号密码。未传入该参数时，表示不进行修改。
        :type Password: str
        :param _Description: 描述，未传入该参数时，表示不进行修改。
        :type Description: str
        """
        self._AccountId = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppAccountResponse(AbstractModel):
    """ModifyAppAccount返回参数结构体

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


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID，是应用的全局唯一标识。
        :type ApplicationId: str
        :param _SecureLevel: 安全级别。
        :type SecureLevel: str
        :param _DisplayName: 应用展示名称，长度限制：32个字符。 默认与应用名字相同。
        :type DisplayName: str
        :param _AppStatus: 应用状态，true表示启用，false表示禁用。
        :type AppStatus: bool
        :param _IconUrl: 应用图标图片访问地址。
        :type IconUrl: str
        :param _Description: 描述。长度不超过128。
        :type Description: str
        """
        self._ApplicationId = None
        self._SecureLevel = None
        self._DisplayName = None
        self._AppStatus = None
        self._IconUrl = None
        self._Description = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SecureLevel(self):
        return self._SecureLevel

    @SecureLevel.setter
    def SecureLevel(self, SecureLevel):
        self._SecureLevel = SecureLevel

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SecureLevel = params.get("SecureLevel")
        self._DisplayName = params.get("DisplayName")
        self._AppStatus = params.get("AppStatus")
        self._IconUrl = params.get("IconUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication返回参数结构体

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


class ModifyUserInfoRequest(AbstractModel):
    """ModifyUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：32个字符。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserName: str
        :param _DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
        :type DisplayName: str
        :param _Description: 用户备注，长度限制：512个字符。
        :type Description: str
        :param _UserGroupIds: 用户所属用户组ID列表。
        :type UserGroupIds: list of str
        :param _UserId: 用户 id。 Username 和 UserId 需选择一个作为搜索条件；如两个条件同时使用则默认使用Username作为搜索条件。
        :type UserId: str
        :param _Phone: 用户手机号。
        :type Phone: str
        :param _ExpirationTime: 用户过期时间，遵循 ISO 8601 标准。
        :type ExpirationTime: str
        :param _Password: 用户密码， 需要符合密码策略的配置。
        :type Password: str
        :param _Email: 用户邮箱。
        :type Email: str
        :param _PwdNeedReset: 密码是否需要重置，为空默认为false不需要重置密码。
        :type PwdNeedReset: bool
        :param _OrgNodeId: 用户所属的主组织机构唯一ID。如果为空，默认为在根节点下创建用户。
        :type OrgNodeId: str
        :param _SecondaryOrgNodeIdList: 用户所属的次要组织机构ID列表。
        :type SecondaryOrgNodeIdList: list of str
        """
        self._UserName = None
        self._DisplayName = None
        self._Description = None
        self._UserGroupIds = None
        self._UserId = None
        self._Phone = None
        self._ExpirationTime = None
        self._Password = None
        self._Email = None
        self._PwdNeedReset = None
        self._OrgNodeId = None
        self._SecondaryOrgNodeIdList = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserGroupIds(self):
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def ExpirationTime(self):
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PwdNeedReset(self):
        return self._PwdNeedReset

    @PwdNeedReset.setter
    def PwdNeedReset(self, PwdNeedReset):
        self._PwdNeedReset = PwdNeedReset

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def SecondaryOrgNodeIdList(self):
        return self._SecondaryOrgNodeIdList

    @SecondaryOrgNodeIdList.setter
    def SecondaryOrgNodeIdList(self, SecondaryOrgNodeIdList):
        self._SecondaryOrgNodeIdList = SecondaryOrgNodeIdList


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserId = params.get("UserId")
        self._Phone = params.get("Phone")
        self._ExpirationTime = params.get("ExpirationTime")
        self._Password = params.get("Password")
        self._Email = params.get("Email")
        self._PwdNeedReset = params.get("PwdNeedReset")
        self._OrgNodeId = params.get("OrgNodeId")
        self._SecondaryOrgNodeIdList = params.get("SecondaryOrgNodeIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserInfoResponse(AbstractModel):
    """ModifyUserInfo返回参数结构体

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


class OrgNodeChildInfo(AbstractModel):
    """当前机构节点下的子节点列表

    """

    def __init__(self):
        r"""
        :param _DisplayName: 机构节点展示名称，长度限制：64个字符。 默认与机构名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _LastModifiedDate: 机构节点最后修改时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        :param _CustomizedOrgNodeId: 用户自定义可选填的机构节点对外ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizedOrgNodeId: str
        :param _ParentOrgNodeId: 当前机构节点的父节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentOrgNodeId: str
        :param _OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _CreatedDate: 机构节点创建时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        :param _Description: 机构节点描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._DisplayName = None
        self._LastModifiedDate = None
        self._CustomizedOrgNodeId = None
        self._ParentOrgNodeId = None
        self._OrgNodeId = None
        self._DataSource = None
        self._CreatedDate = None
        self._Description = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId

    @property
    def ParentOrgNodeId(self):
        return self._ParentOrgNodeId

    @ParentOrgNodeId.setter
    def ParentOrgNodeId(self, ParentOrgNodeId):
        self._ParentOrgNodeId = ParentOrgNodeId

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        self._ParentOrgNodeId = params.get("ParentOrgNodeId")
        self._OrgNodeId = params.get("OrgNodeId")
        self._DataSource = params.get("DataSource")
        self._CreatedDate = params.get("CreatedDate")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNodeChildUserInfo(AbstractModel):
    """机构子节点下的用户信息列表

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构ID，是机构节点全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeId: str
        :param _UserInfo: 用户信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: list of UserInfo
        :param _TotalUserNum: 当前机构节点下的用户总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUserNum: int
        :param _OrgNodeIdPath: 组织机构ID路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeIdPath: str
        :param _OrgNodeNamePath: 组织机构名称路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgNodeNamePath: str
        """
        self._OrgNodeId = None
        self._UserInfo = None
        self._TotalUserNum = None
        self._OrgNodeIdPath = None
        self._OrgNodeNamePath = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def TotalUserNum(self):
        return self._TotalUserNum

    @TotalUserNum.setter
    def TotalUserNum(self, TotalUserNum):
        self._TotalUserNum = TotalUserNum

    @property
    def OrgNodeIdPath(self):
        return self._OrgNodeIdPath

    @OrgNodeIdPath.setter
    def OrgNodeIdPath(self, OrgNodeIdPath):
        self._OrgNodeIdPath = OrgNodeIdPath

    @property
    def OrgNodeNamePath(self):
        return self._OrgNodeNamePath

    @OrgNodeNamePath.setter
    def OrgNodeNamePath(self, OrgNodeNamePath):
        self._OrgNodeNamePath = OrgNodeNamePath


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._TotalUserNum = params.get("TotalUserNum")
        self._OrgNodeIdPath = params.get("OrgNodeIdPath")
        self._OrgNodeNamePath = params.get("OrgNodeNamePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupRequest(AbstractModel):
    """RemoveAccountFromAccountGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _AccountIds: 需要移除账号ID列表。
        :type AccountIds: list of str
        """
        self._AccountGroupId = None
        self._AccountIds = None

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountIds = params.get("AccountIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAccountFromAccountGroupResponse(AbstractModel):
    """RemoveAccountFromAccountGroup返回参数结构体

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


class RemoveUserFromUserGroupRequest(AbstractModel):
    """RemoveUserFromUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: 要加入用户组的用户ID列表。
        :type UserIds: list of str
        :param _UserGroupId: 用户组ID，是用户组的全局唯一标识。
        :type UserGroupId: str
        """
        self._UserIds = None
        self._UserGroupId = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._UserGroupId = params.get("UserGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromUserGroupResponse(AbstractModel):
    """RemoveUserFromUserGroup返回参数结构体

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


class SortCondition(AbstractModel):
    """排序条件。

    """

    def __init__(self):
        r"""
        :param _SortKey: 排序属性。
        :type SortKey: str
        :param _SortOrder: 排序顺序，ASC为正向排序，DESC为反向排序。
        :type SortOrder: str
        """
        self._SortKey = None
        self._SortOrder = None

    @property
    def SortKey(self):
        return self._SortKey

    @SortKey.setter
    def SortKey(self, SortKey):
        self._SortKey = SortKey

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._SortKey = params.get("SortKey")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThirdPartyAccountInfo(AbstractModel):
    """三方账号信息。

    """

    def __init__(self):
        r"""
        :param _AccountCode: 第三方账号代码。"2"代表企业微信。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountCode: str
        :param _AccountName: 账号对应的用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        """
        self._AccountCode = None
        self._AccountName = None

    @property
    def AccountCode(self):
        return self._AccountCode

    @AccountCode.setter
    def AccountCode(self, AccountCode):
        self._AccountCode = AccountCode

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._AccountCode = params.get("AccountCode")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeRequest(AbstractModel):
    """UpdateOrgNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgNodeId: 机构节点ID，是机构节点的全局唯一标识。
        :type OrgNodeId: str
        :param _DisplayName: 机构节点名称，长度限制：64个字符。
        :type DisplayName: str
        :param _Description: 机构节点描述。
        :type Description: str
        :param _CustomizedOrgNodeId: 机构代码。如果非空则校验此ID的唯一性。
        :type CustomizedOrgNodeId: str
        """
        self._OrgNodeId = None
        self._DisplayName = None
        self._Description = None
        self._CustomizedOrgNodeId = None

    @property
    def OrgNodeId(self):
        return self._OrgNodeId

    @OrgNodeId.setter
    def OrgNodeId(self, OrgNodeId):
        self._OrgNodeId = OrgNodeId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CustomizedOrgNodeId(self):
        return self._CustomizedOrgNodeId

    @CustomizedOrgNodeId.setter
    def CustomizedOrgNodeId(self, CustomizedOrgNodeId):
        self._CustomizedOrgNodeId = CustomizedOrgNodeId


    def _deserialize(self, params):
        self._OrgNodeId = params.get("OrgNodeId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._CustomizedOrgNodeId = params.get("CustomizedOrgNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrgNodeResponse(AbstractModel):
    """UpdateOrgNode返回参数结构体

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


class UserGroupInfo(AbstractModel):
    """返回的用户组列表。

    """

    def __init__(self):
        r"""
        :param _DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _UserGroupId: 用户组ID，是用户组全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroupId: str
        :param _Description: 用户组备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreatedDate: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedDate: str
        """
        self._DisplayName = None
        self._UserGroupId = None
        self._Description = None
        self._CreatedDate = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._UserGroupId = params.get("UserGroupId")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInfoSearchCriteria(AbstractModel):
    """用户组属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _Keyword: 名称匹配搜索，匹配范围包括：用户组名称、用户组ID。
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformation(AbstractModel):
    """返回的用户组列表。

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID。
        :type UserGroupId: str
        :param _UserGroupName: 用户组名称。
        :type UserGroupName: str
        :param _LastModifiedDate: 上次更新时间，符合 ISO8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: str
        """
        self._UserGroupId = None
        self._UserGroupName = None
        self._LastModifiedDate = None

    @property
    def UserGroupId(self):
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def UserGroupName(self):
        return self._UserGroupName

    @UserGroupName.setter
    def UserGroupName(self, UserGroupName):
        self._UserGroupName = UserGroupName

    @property
    def LastModifiedDate(self):
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._UserGroupName = params.get("UserGroupName")
        self._LastModifiedDate = params.get("LastModifiedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupInformationSearchCriteria(AbstractModel):
    """获取用户所在的用户组列表功能中用户组属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _Keyword: 名称匹配搜索，匹配范围包括：用户组名称。
        :type Keyword: str
        """
        self._Keyword = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息列表。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID，是用户全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _UserName: 用户名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Phone: 用户手机号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Email: 邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Status: 用户状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _DataSource: 数据来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        """
        self._UserId = None
        self._DisplayName = None
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._DataSource = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._DisplayName = params.get("DisplayName")
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._DataSource = params.get("DataSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInformation(AbstractModel):
    """用户信息列表。

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：32个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Status: 用户状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _DisplayName: 昵称，长度限制：64个字符。 默认与用户名相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _Description: 用户备注，长度限制：512个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _LastUpdateTime: 用户上次更新时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _CreationTime: 用户创建时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param _OrgPath: 用户所属主组织机构的路径ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPath: str
        :param _Phone: 带国家号的用户手机号，例如+86-00000000000。
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _SubjectGroups: 用户所属用户组ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectGroups: list of str
        :param _Email: 用户邮箱。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _LastLoginTime: 用户上次登录时间，遵循 ISO 8601 标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLoginTime: str
        :param _UserId: 用户ID，是用户全局唯一标识，长度限制：64个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        """
        self._UserName = None
        self._Status = None
        self._DisplayName = None
        self._Description = None
        self._LastUpdateTime = None
        self._CreationTime = None
        self._OrgPath = None
        self._Phone = None
        self._SubjectGroups = None
        self._Email = None
        self._LastLoginTime = None
        self._UserId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def OrgPath(self):
        return self._OrgPath

    @OrgPath.setter
    def OrgPath(self, OrgPath):
        self._OrgPath = OrgPath

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def SubjectGroups(self):
        return self._SubjectGroups

    @SubjectGroups.setter
    def SubjectGroups(self, SubjectGroups):
        self._SubjectGroups = SubjectGroups

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastLoginTime(self):
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Status = params.get("Status")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._CreationTime = params.get("CreationTime")
        self._OrgPath = params.get("OrgPath")
        self._Phone = params.get("Phone")
        self._SubjectGroups = params.get("SubjectGroups")
        self._Email = params.get("Email")
        self._LastLoginTime = params.get("LastLoginTime")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSearchCriteria(AbstractModel):
    """用户属性搜索条件。

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，长度限制：64个字符。
        :type UserName: str
        :param _Phone: 用户手机号。
        :type Phone: str
        :param _Email: 用户邮箱。
        :type Email: str
        :param _Status: 用户状态，取值 NORMAL （正常）、FREEZE （已冻结）、LOCKED （已锁定）或 NOT_ENABLED （未启用）。
        :type Status: str
        :param _CreationTime: 用户创建时间，遵循 ISO 8601 标准。
        :type CreationTime: str
        :param _LastUpdateTime: 用户上次更新时间区间。
        :type LastUpdateTime: str
        :param _Keyword: 名称匹配搜索，匹配范围包括：用户名称、用户ID。
        :type Keyword: str
        """
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._Status = None
        self._CreationTime = None
        self._LastUpdateTime = None
        self._Keyword = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._CreationTime = params.get("CreationTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        