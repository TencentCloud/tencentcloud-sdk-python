# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AppAssociatedUserGroupIds(AbstractModel):
    r"""用户组删除时关联的应用信息

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组id
        :type UserGroupId: str
        :param _ApplicationId: 应用id
        :type ApplicationId: str
        :param _ApplicationName: 应用名称
        :type ApplicationName: str
        """
        self._UserGroupId = None
        self._ApplicationId = None
        self._ApplicationName = None

    @property
    def UserGroupId(self):
        r"""用户组id
        :rtype: str
        """
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def ApplicationId(self):
        r"""应用id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        r"""应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiImportUserJobRequest(AbstractModel):
    r"""CreateApiImportUserJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _DataFlowUserCreateList: 导入的用户数据
        :type DataFlowUserCreateList: list of ImportUser
        """
        self._UserStoreId = None
        self._DataFlowUserCreateList = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def DataFlowUserCreateList(self):
        r"""导入的用户数据
        :rtype: list of ImportUser
        """
        return self._DataFlowUserCreateList

    @DataFlowUserCreateList.setter
    def DataFlowUserCreateList(self, DataFlowUserCreateList):
        self._DataFlowUserCreateList = DataFlowUserCreateList


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("DataFlowUserCreateList") is not None:
            self._DataFlowUserCreateList = []
            for item in params.get("DataFlowUserCreateList"):
                obj = ImportUser()
                obj._deserialize(item)
                self._DataFlowUserCreateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiImportUserJobResponse(AbstractModel):
    r"""CreateApiImportUserJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 数据流任务
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        r"""数据流任务
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateFileExportUserJobRequest(AbstractModel):
    r"""CreateFileExportUserJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Format: 导出的数据类型

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
        :type Format: str
        :param _Filters: Key可选值为condition、userGroupId

<li> **condition** </li>	Values = 查询条件，用户ID，用户名称，手机或邮箱
<li> **userGroupId** </li>	Values = 用户组ID
        :type Filters: list of Filter
        :param _ExportPropertyMaps: 导出用户包含的属性和映射名称，为空时包含所有的属性
        :type ExportPropertyMaps: list of ExportPropertyMap
        """
        self._UserStoreId = None
        self._Format = None
        self._Filters = None
        self._ExportPropertyMaps = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Format(self):
        r"""导出的数据类型

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Filters(self):
        r"""Key可选值为condition、userGroupId

<li> **condition** </li>	Values = 查询条件，用户ID，用户名称，手机或邮箱
<li> **userGroupId** </li>	Values = 用户组ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ExportPropertyMaps(self):
        r"""导出用户包含的属性和映射名称，为空时包含所有的属性
        :rtype: list of ExportPropertyMap
        """
        return self._ExportPropertyMaps

    @ExportPropertyMaps.setter
    def ExportPropertyMaps(self, ExportPropertyMaps):
        self._ExportPropertyMaps = ExportPropertyMaps


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._Format = params.get("Format")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("ExportPropertyMaps") is not None:
            self._ExportPropertyMaps = []
            for item in params.get("ExportPropertyMaps"):
                obj = ExportPropertyMap()
                obj._deserialize(item)
                self._ExportPropertyMaps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileExportUserJobResponse(AbstractModel):
    r"""CreateFileExportUserJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 数据流任务
        :type Job: :class:`tencentcloud.ciam.v20220331.models.Job`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        r"""数据流任务
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    r"""CreateUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayName: 用户组名称
        :type DisplayName: str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Description: 用户组描述
        :type Description: str
        """
        self._DisplayName = None
        self._UserStoreId = None
        self._Description = None

    @property
    def DisplayName(self):
        r"""用户组名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Description(self):
        r"""用户组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._UserStoreId = params.get("UserStoreId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserGroupResponse(AbstractModel):
    r"""CreateUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID
        :type UserGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupId = None
        self._RequestId = None

    @property
    def UserGroupId(self):
        r"""用户组ID
        :rtype: str
        """
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    r"""CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _PhoneNumber: 手机号码
        :type PhoneNumber: str
        :param _Email: 邮箱
        :type Email: str
        :param _Password: 密码
        :type Password: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _Address: 地址
        :type Address: str
        :param _UserGroup: 用户组ID
        :type UserGroup: list of str
        :param _Birthdate: 生日
        :type Birthdate: int
        :param _CustomizationAttributes: 自定义属性
        :type CustomizationAttributes: list of MemberMap
        :param _IndexedAttribute1: 索引字段1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: 索引字段2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: 索引字段3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: 索引字段4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: 索引字段5
        :type IndexedAttribute5: str
        """
        self._UserStoreId = None
        self._PhoneNumber = None
        self._Email = None
        self._Password = None
        self._UserName = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._Birthdate = None
        self._CustomizationAttributes = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PhoneNumber(self):
        r"""手机号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        r"""邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Password(self):
        r"""密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        r"""地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        r"""用户组ID
        :rtype: list of str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Birthdate(self):
        r"""生日
        :rtype: int
        """
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def CustomizationAttributes(self):
        r"""自定义属性
        :rtype: list of MemberMap
        """
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def IndexedAttribute1(self):
        r"""索引字段1
        :rtype: str
        """
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        r"""索引字段2
        :rtype: str
        """
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        r"""索引字段3
        :rtype: str
        """
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        r"""索引字段4
        :rtype: str
        """
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        r"""索引字段5
        :rtype: str
        """
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    r"""CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _User: 创建的用户信息
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""创建的用户信息
        :rtype: :class:`tencentcloud.ciam.v20220331.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class CreateUserStoreRequest(AbstractModel):
    r"""CreateUserStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserPoolName: 用户池名字
        :type UserPoolName: str
        :param _UserPoolDesc: 用户池描述
        :type UserPoolDesc: str
        :param _UserPoolLogo: 用户池logo
        :type UserPoolLogo: str
        """
        self._UserPoolName = None
        self._UserPoolDesc = None
        self._UserPoolLogo = None

    @property
    def UserPoolName(self):
        r"""用户池名字
        :rtype: str
        """
        return self._UserPoolName

    @UserPoolName.setter
    def UserPoolName(self, UserPoolName):
        self._UserPoolName = UserPoolName

    @property
    def UserPoolDesc(self):
        r"""用户池描述
        :rtype: str
        """
        return self._UserPoolDesc

    @UserPoolDesc.setter
    def UserPoolDesc(self, UserPoolDesc):
        self._UserPoolDesc = UserPoolDesc

    @property
    def UserPoolLogo(self):
        r"""用户池logo
        :rtype: str
        """
        return self._UserPoolLogo

    @UserPoolLogo.setter
    def UserPoolLogo(self, UserPoolLogo):
        self._UserPoolLogo = UserPoolLogo


    def _deserialize(self, params):
        self._UserPoolName = params.get("UserPoolName")
        self._UserPoolDesc = params.get("UserPoolDesc")
        self._UserPoolLogo = params.get("UserPoolLogo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserStoreResponse(AbstractModel):
    r"""CreateUserStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserStoreId = None
        self._RequestId = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._RequestId = params.get("RequestId")


class DeleteUserGroupsRequest(AbstractModel):
    r"""DeleteUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupIds: 用户组ID数组
        :type UserGroupIds: list of str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        """
        self._UserGroupIds = None
        self._UserStoreId = None

    @property
    def UserGroupIds(self):
        r"""用户组ID数组
        :rtype: list of str
        """
        return self._UserGroupIds

    @UserGroupIds.setter
    def UserGroupIds(self, UserGroupIds):
        self._UserGroupIds = UserGroupIds

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId


    def _deserialize(self, params):
        self._UserGroupIds = params.get("UserGroupIds")
        self._UserStoreId = params.get("UserStoreId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupsResponse(AbstractModel):
    r"""DeleteUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupDeletedInfo: 删除的用户组关联的应用信息
        :type UserGroupDeletedInfo: :class:`tencentcloud.ciam.v20220331.models.UserGroupDeleteResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserGroupDeletedInfo = None
        self._RequestId = None

    @property
    def UserGroupDeletedInfo(self):
        r"""删除的用户组关联的应用信息
        :rtype: :class:`tencentcloud.ciam.v20220331.models.UserGroupDeleteResp`
        """
        return self._UserGroupDeletedInfo

    @UserGroupDeletedInfo.setter
    def UserGroupDeletedInfo(self, UserGroupDeletedInfo):
        self._UserGroupDeletedInfo = UserGroupDeletedInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserGroupDeletedInfo") is not None:
            self._UserGroupDeletedInfo = UserGroupDeleteResp()
            self._UserGroupDeletedInfo._deserialize(params.get("UserGroupDeletedInfo"))
        self._RequestId = params.get("RequestId")


class DeleteUserStoreRequest(AbstractModel):
    r"""DeleteUserStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserPoolId: 用户池ID
        :type UserPoolId: str
        """
        self._UserPoolId = None

    @property
    def UserPoolId(self):
        r"""用户池ID
        :rtype: str
        """
        return self._UserPoolId

    @UserPoolId.setter
    def UserPoolId(self, UserPoolId):
        self._UserPoolId = UserPoolId


    def _deserialize(self, params):
        self._UserPoolId = params.get("UserPoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserStoreResponse(AbstractModel):
    r"""DeleteUserStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    r"""DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _UserIds: 用户ID数组
        :type UserIds: list of str
        """
        self._UserStoreId = None
        self._UserIds = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserIds(self):
        r"""用户ID数组
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    r"""DeleteUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeUserByIdRequest(AbstractModel):
    r"""DescribeUserById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _Original: 返回信息是否为原文

<li> **false** </li>	默认，返回信息为脱敏信息
<li> **true** </li>	返回用户信息原文
        :type Original: bool
        """
        self._UserStoreId = None
        self._UserId = None
        self._Original = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Original(self):
        r"""返回信息是否为原文

<li> **false** </li>	默认，返回信息为脱敏信息
<li> **true** </li>	返回用户信息原文
        :rtype: bool
        """
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserByIdResponse(AbstractModel):
    r"""DescribeUserById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _User: 用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ciam.v20220331.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    r"""DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Pageable: 分页数据
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Filters: 查询条件，根据propertycode和propertykey
        :type Filters: list of QueryUserFilter
        :param _Original: 是否返回明文
        :type Original: bool
        :param _Sort: 排序设置
        :type Sort: :class:`tencentcloud.ciam.v20220331.models.Sort`
        """
        self._UserStoreId = None
        self._Pageable = None
        self._Filters = None
        self._Original = None
        self._Sort = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        r"""分页数据
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Filters(self):
        r"""查询条件，根据propertycode和propertykey
        :rtype: list of QueryUserFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Original(self):
        r"""是否返回明文
        :rtype: bool
        """
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original

    @property
    def Sort(self):
        r"""排序设置
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryUserFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Original = params.get("Original")
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    r"""DescribeUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Pageable: 分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: 用户列表
        :type Content: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        r"""分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        r"""用户列表
        :rtype: list of User
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class ErrorDetails(AbstractModel):
    r"""失败详情

    """

    def __init__(self):
        r"""
        :param _UserId: 用户信息
        :type UserId: str
        :param _Error: 失败原因
        :type Error: str
        """
        self._UserId = None
        self._Error = None

    @property
    def UserId(self):
        r"""用户信息
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Error(self):
        r"""失败原因
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportPropertyMap(AbstractModel):
    r"""导出属性映射

    """

    def __init__(self):
        r"""
        :param _UserPropertyCode: 用户属性code
        :type UserPropertyCode: str
        :param _ColumnName: 用户属性映射名称
        :type ColumnName: str
        """
        self._UserPropertyCode = None
        self._ColumnName = None

    @property
    def UserPropertyCode(self):
        r"""用户属性code
        :rtype: str
        """
        return self._UserPropertyCode

    @UserPropertyCode.setter
    def UserPropertyCode(self, UserPropertyCode):
        self._UserPropertyCode = UserPropertyCode

    @property
    def ColumnName(self):
        r"""用户属性映射名称
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._UserPropertyCode = params.get("UserPropertyCode")
        self._ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedUsers(AbstractModel):
    r"""失败的用户

    """

    def __init__(self):
        r"""
        :param _FailedUserIdentification: 失败用户标识
        :type FailedUserIdentification: str
        :param _FailedReason: 导入的用户失败原因
        :type FailedReason: str
        """
        self._FailedUserIdentification = None
        self._FailedReason = None

    @property
    def FailedUserIdentification(self):
        r"""失败用户标识
        :rtype: str
        """
        return self._FailedUserIdentification

    @FailedUserIdentification.setter
    def FailedUserIdentification(self, FailedUserIdentification):
        self._FailedUserIdentification = FailedUserIdentification

    @property
    def FailedReason(self):
        r"""导入的用户失败原因
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason


    def _deserialize(self, params):
        self._FailedUserIdentification = params.get("FailedUserIdentification")
        self._FailedReason = params.get("FailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""查询条件

    """

    def __init__(self):
        r"""
        :param _Key: key值
        :type Key: str
        :param _Values: value值
        :type Values: list of str
        :param _Logic: 逻辑值
        :type Logic: bool
        """
        self._Key = None
        self._Values = None
        self._Logic = None

    @property
    def Key(self):
        r"""key值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""value值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Logic(self):
        r"""逻辑值
        :rtype: bool
        """
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportUser(AbstractModel):
    r"""导入用户信息
    1、UserName，PhoneNumber ，Email ，WechatOpenId ，WechatUnionId ，AlipayUserId ，QqOpenId ，QqUnionId ，WeComUserId 九个属性中，导入时必须包含其中一个属性并遵守初始化自定义属性的正则表达式规则。UserName，PhoneNumber，Email的正则表达式在控制台的自定义属性中可以查询到。
    2、对于密码的导入，导入的密码支持明文导入，MD5密文导入，SHA1密文导入，BCRYPT密文导入 ，这个需要在PasswordEncryptTypeEnum 字段中指定。
    3、IdentityVerified，IdentityVerificationMethod 支持导入，
    IdentityVerified 为true，IdentityVerificationMethod必传；
    IdentityVerificationMethod 为nameAndIdCard，Name,ResidentIdentityCard必传
    IdentityVerificationMethod 为nameIdCardAndPhone，Name,PhoneNumber,ResidentIdentityCard必传;

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _PhoneNumber: 手机号
        :type PhoneNumber: str
        :param _Email: 邮箱
        :type Email: str
        :param _ResidentIdentityCard: 身份证号
        :type ResidentIdentityCard: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _Address: 地址
        :type Address: str
        :param _UserGroup: 用户组ID
        :type UserGroup: list of str
        :param _QqOpenId: QQ qqOpenId
        :type QqOpenId: str
        :param _QqUnionId: QQ qqUnionId
        :type QqUnionId: str
        :param _WechatOpenId: 微信wechatOpenId
        :type WechatOpenId: str
        :param _WechatUnionId: 微信wechatUnionId
        :type WechatUnionId: str
        :param _AlipayUserId: 支付宝alipayUserId
        :type AlipayUserId: str
        :param _WeComUserId: 企业微信weComUserId
        :type WeComUserId: str
        :param _Description: 描述
        :type Description: str
        :param _Birthdate: 生日
        :type Birthdate: str
        :param _Name: 姓名
        :type Name: str
        :param _Locale: 坐标
        :type Locale: str
        :param _Gender: 性别（MALE;FEMALE;UNKNOWN）
        :type Gender: str
        :param _IdentityVerificationMethod: 实名核验方式
        :type IdentityVerificationMethod: str
        :param _IdentityVerified: 是否已实名核验
        :type IdentityVerified: bool
        :param _Job: 工作
        :type Job: str
        :param _Nationality: 国家
        :type Nationality: str
        :param _Zone: 时区
        :type Zone: str
        :param _Password: 密码密文
        :type Password: str
        :param _CustomizationAttributes: 自定义属性
        :type CustomizationAttributes: list of MemberMap
        :param _Salt: 密码盐
        :type Salt: :class:`tencentcloud.ciam.v20220331.models.Salt`
        :param _PasswordEncryptTypeEnum: 密码加密方式（SHA1;BCRYPT）
        :type PasswordEncryptTypeEnum: str
        :param _IndexedAttribute1: 索引字段1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: 索引字段2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: 索引字段3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: 索引字段4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: 索引字段5
        :type IndexedAttribute5: str
        """
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._ResidentIdentityCard = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._QqOpenId = None
        self._QqUnionId = None
        self._WechatOpenId = None
        self._WechatUnionId = None
        self._AlipayUserId = None
        self._WeComUserId = None
        self._Description = None
        self._Birthdate = None
        self._Name = None
        self._Locale = None
        self._Gender = None
        self._IdentityVerificationMethod = None
        self._IdentityVerified = None
        self._Job = None
        self._Nationality = None
        self._Zone = None
        self._Password = None
        self._CustomizationAttributes = None
        self._Salt = None
        self._PasswordEncryptTypeEnum = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        r"""手机号
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        r"""邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ResidentIdentityCard(self):
        r"""身份证号
        :rtype: str
        """
        return self._ResidentIdentityCard

    @ResidentIdentityCard.setter
    def ResidentIdentityCard(self, ResidentIdentityCard):
        self._ResidentIdentityCard = ResidentIdentityCard

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        r"""地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        r"""用户组ID
        :rtype: list of str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def QqOpenId(self):
        r"""QQ qqOpenId
        :rtype: str
        """
        return self._QqOpenId

    @QqOpenId.setter
    def QqOpenId(self, QqOpenId):
        self._QqOpenId = QqOpenId

    @property
    def QqUnionId(self):
        r"""QQ qqUnionId
        :rtype: str
        """
        return self._QqUnionId

    @QqUnionId.setter
    def QqUnionId(self, QqUnionId):
        self._QqUnionId = QqUnionId

    @property
    def WechatOpenId(self):
        r"""微信wechatOpenId
        :rtype: str
        """
        return self._WechatOpenId

    @WechatOpenId.setter
    def WechatOpenId(self, WechatOpenId):
        self._WechatOpenId = WechatOpenId

    @property
    def WechatUnionId(self):
        r"""微信wechatUnionId
        :rtype: str
        """
        return self._WechatUnionId

    @WechatUnionId.setter
    def WechatUnionId(self, WechatUnionId):
        self._WechatUnionId = WechatUnionId

    @property
    def AlipayUserId(self):
        r"""支付宝alipayUserId
        :rtype: str
        """
        return self._AlipayUserId

    @AlipayUserId.setter
    def AlipayUserId(self, AlipayUserId):
        self._AlipayUserId = AlipayUserId

    @property
    def WeComUserId(self):
        r"""企业微信weComUserId
        :rtype: str
        """
        return self._WeComUserId

    @WeComUserId.setter
    def WeComUserId(self, WeComUserId):
        self._WeComUserId = WeComUserId

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Birthdate(self):
        r"""生日
        :rtype: str
        """
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def Name(self):
        r"""姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Locale(self):
        r"""坐标
        :rtype: str
        """
        return self._Locale

    @Locale.setter
    def Locale(self, Locale):
        self._Locale = Locale

    @property
    def Gender(self):
        r"""性别（MALE;FEMALE;UNKNOWN）
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def IdentityVerificationMethod(self):
        r"""实名核验方式
        :rtype: str
        """
        return self._IdentityVerificationMethod

    @IdentityVerificationMethod.setter
    def IdentityVerificationMethod(self, IdentityVerificationMethod):
        self._IdentityVerificationMethod = IdentityVerificationMethod

    @property
    def IdentityVerified(self):
        r"""是否已实名核验
        :rtype: bool
        """
        return self._IdentityVerified

    @IdentityVerified.setter
    def IdentityVerified(self, IdentityVerified):
        self._IdentityVerified = IdentityVerified

    @property
    def Job(self):
        r"""工作
        :rtype: str
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def Nationality(self):
        r"""国家
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Zone(self):
        r"""时区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Password(self):
        r"""密码密文
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CustomizationAttributes(self):
        r"""自定义属性
        :rtype: list of MemberMap
        """
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def Salt(self):
        r"""密码盐
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Salt`
        """
        return self._Salt

    @Salt.setter
    def Salt(self, Salt):
        self._Salt = Salt

    @property
    def PasswordEncryptTypeEnum(self):
        r"""密码加密方式（SHA1;BCRYPT）
        :rtype: str
        """
        return self._PasswordEncryptTypeEnum

    @PasswordEncryptTypeEnum.setter
    def PasswordEncryptTypeEnum(self, PasswordEncryptTypeEnum):
        self._PasswordEncryptTypeEnum = PasswordEncryptTypeEnum

    @property
    def IndexedAttribute1(self):
        r"""索引字段1
        :rtype: str
        """
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        r"""索引字段2
        :rtype: str
        """
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        r"""索引字段3
        :rtype: str
        """
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        r"""索引字段4
        :rtype: str
        """
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        r"""索引字段5
        :rtype: str
        """
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._ResidentIdentityCard = params.get("ResidentIdentityCard")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._QqOpenId = params.get("QqOpenId")
        self._QqUnionId = params.get("QqUnionId")
        self._WechatOpenId = params.get("WechatOpenId")
        self._WechatUnionId = params.get("WechatUnionId")
        self._AlipayUserId = params.get("AlipayUserId")
        self._WeComUserId = params.get("WeComUserId")
        self._Description = params.get("Description")
        self._Birthdate = params.get("Birthdate")
        self._Name = params.get("Name")
        self._Locale = params.get("Locale")
        self._Gender = params.get("Gender")
        self._IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self._IdentityVerified = params.get("IdentityVerified")
        self._Job = params.get("Job")
        self._Nationality = params.get("Nationality")
        self._Zone = params.get("Zone")
        self._Password = params.get("Password")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        if params.get("Salt") is not None:
            self._Salt = Salt()
            self._Salt._deserialize(params.get("Salt"))
        self._PasswordEncryptTypeEnum = params.get("PasswordEncryptTypeEnum")
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    r"""任务详情

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: str
        :param _Status: 任务状态

<li> **PENDING** </li>  待执行
<li> **PROCESSING** </li>  执行中
<li> **COMPLETED** </li>  完成
<li> **FAILED** </li>  失败
        :type Status: str
        :param _Type: 任务类型

<li> **IMPORT_USER** </li>  用户导入
<li> **EXPORT_USER** </li>  用户导出
        :type Type: str
        :param _CreatedDate: 任务创建时间
        :type CreatedDate: int
        :param _Format: 任务的数据类型

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _Location: 任务结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _ErrorDetails: 失败详情
        :type ErrorDetails: list of ErrorDetails
        :param _FailedUsers: 失败的用户
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedUsers: list of FailedUsers
        """
        self._Id = None
        self._Status = None
        self._Type = None
        self._CreatedDate = None
        self._Format = None
        self._Location = None
        self._ErrorDetails = None
        self._FailedUsers = None

    @property
    def Id(self):
        r"""任务ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        r"""任务状态

<li> **PENDING** </li>  待执行
<li> **PROCESSING** </li>  执行中
<li> **COMPLETED** </li>  完成
<li> **FAILED** </li>  失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""任务类型

<li> **IMPORT_USER** </li>  用户导入
<li> **EXPORT_USER** </li>  用户导出
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatedDate(self):
        r"""任务创建时间
        :rtype: int
        """
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Format(self):
        r"""任务的数据类型

<li> **NDJSON** </li>  New-line Delimited JSON
<li> **CSV** </li>  Comma-Separated Values
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Location(self):
        r"""任务结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def ErrorDetails(self):
        r"""失败详情
        :rtype: list of ErrorDetails
        """
        return self._ErrorDetails

    @ErrorDetails.setter
    def ErrorDetails(self, ErrorDetails):
        self._ErrorDetails = ErrorDetails

    @property
    def FailedUsers(self):
        r"""失败的用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FailedUsers
        """
        return self._FailedUsers

    @FailedUsers.setter
    def FailedUsers(self, FailedUsers):
        self._FailedUsers = FailedUsers


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreatedDate = params.get("CreatedDate")
        self._Format = params.get("Format")
        self._Location = params.get("Location")
        if params.get("ErrorDetails") is not None:
            self._ErrorDetails = []
            for item in params.get("ErrorDetails"):
                obj = ErrorDetails()
                obj._deserialize(item)
                self._ErrorDetails.append(obj)
        if params.get("FailedUsers") is not None:
            self._FailedUsers = []
            for item in params.get("FailedUsers"):
                obj = FailedUsers()
                obj._deserialize(item)
                self._FailedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountRequest(AbstractModel):
    r"""LinkAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _PrimaryUserId: 主用户ID
        :type PrimaryUserId: str
        :param _SecondaryUserId: 从用户ID
        :type SecondaryUserId: str
        :param _UserLinkedOnAttribute: 融合属性

<li> **PHONENUMBER** </li>	  手机号码
<li> **EMAIL** </li>  邮箱
        :type UserLinkedOnAttribute: str
        """
        self._UserStoreId = None
        self._PrimaryUserId = None
        self._SecondaryUserId = None
        self._UserLinkedOnAttribute = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PrimaryUserId(self):
        r"""主用户ID
        :rtype: str
        """
        return self._PrimaryUserId

    @PrimaryUserId.setter
    def PrimaryUserId(self, PrimaryUserId):
        self._PrimaryUserId = PrimaryUserId

    @property
    def SecondaryUserId(self):
        r"""从用户ID
        :rtype: str
        """
        return self._SecondaryUserId

    @SecondaryUserId.setter
    def SecondaryUserId(self, SecondaryUserId):
        self._SecondaryUserId = SecondaryUserId

    @property
    def UserLinkedOnAttribute(self):
        r"""融合属性

<li> **PHONENUMBER** </li>	  手机号码
<li> **EMAIL** </li>  邮箱
        :rtype: str
        """
        return self._UserLinkedOnAttribute

    @UserLinkedOnAttribute.setter
    def UserLinkedOnAttribute(self, UserLinkedOnAttribute):
        self._UserLinkedOnAttribute = UserLinkedOnAttribute


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PrimaryUserId = params.get("PrimaryUserId")
        self._SecondaryUserId = params.get("SecondaryUserId")
        self._UserLinkedOnAttribute = params.get("UserLinkedOnAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountResponse(AbstractModel):
    r"""LinkAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ListJobsRequest(AbstractModel):
    r"""ListJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _JobIds: 任务ID列表，为空时返回全部任务
        :type JobIds: list of str
        """
        self._UserStoreId = None
        self._JobIds = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def JobIds(self):
        r"""任务ID列表，为空时返回全部任务
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJobsResponse(AbstractModel):
    r"""ListJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobSet: 任务列表
        :type JobSet: list of Job
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobSet = None
        self._RequestId = None

    @property
    def JobSet(self):
        r"""任务列表
        :rtype: list of Job
        """
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = Job()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._RequestId = params.get("RequestId")


class ListLogMessageByConditionRequest(AbstractModel):
    r"""ListLogMessageByCondition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户池ID
        :type UserStoreId: str
        :param _Pageable: 分页数据
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _StartTime: 开始时间，时间戳精确到毫秒
        :type StartTime: int
        :param _Filters: Key可选值为events

<li> **events** </li>	Values为["SIGNUP", "USER_UPDATE", "USER_DELETE", "USER_CREATE", "ACCOUNT_LINKING"] 中的一个或多个
        :type Filters: list of Filter
        """
        self._UserStoreId = None
        self._Pageable = None
        self._StartTime = None
        self._Filters = None

    @property
    def UserStoreId(self):
        r"""用户池ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        r"""分页数据
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def StartTime(self):
        r"""开始时间，时间戳精确到毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Filters(self):
        r"""Key可选值为events

<li> **events** </li>	Values为["SIGNUP", "USER_UPDATE", "USER_DELETE", "USER_CREATE", "ACCOUNT_LINKING"] 中的一个或多个
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        self._StartTime = params.get("StartTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLogMessageByConditionResponse(AbstractModel):
    r"""ListLogMessageByCondition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Pageable: 分页对象
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: 日志列表
        :type Content: list of LogMessage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        r"""分页对象
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        r"""日志列表
        :rtype: list of LogMessage
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = LogMessage()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserByPropertyRequest(AbstractModel):
    r"""ListUserByProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _PropertyCode: 查询的属性

<li> **phoneNumber** </li>	  手机号码
<li> **email** </li>  邮箱
        :type PropertyCode: str
        :param _PropertyValue: 属性值
        :type PropertyValue: str
        :param _Original: 返回信息是否为原文
        :type Original: bool
        """
        self._UserStoreId = None
        self._PropertyCode = None
        self._PropertyValue = None
        self._Original = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def PropertyCode(self):
        r"""查询的属性

<li> **phoneNumber** </li>	  手机号码
<li> **email** </li>  邮箱
        :rtype: str
        """
        return self._PropertyCode

    @PropertyCode.setter
    def PropertyCode(self, PropertyCode):
        self._PropertyCode = PropertyCode

    @property
    def PropertyValue(self):
        r"""属性值
        :rtype: str
        """
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue

    @property
    def Original(self):
        r"""返回信息是否为原文
        :rtype: bool
        """
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._PropertyCode = params.get("PropertyCode")
        self._PropertyValue = params.get("PropertyValue")
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserByPropertyResponse(AbstractModel):
    r"""ListUserByProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 用户列表
        :type Users: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        r"""用户列表
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserGroupsRequest(AbstractModel):
    r"""ListUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Pageable: 分页数据
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Filters: Key可选值为condition

<li> **condition** </li>	Values = 查询条件，用户组ID或用户组名称
        :type Filters: list of Filter
        """
        self._UserStoreId = None
        self._Pageable = None
        self._Filters = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        r"""分页数据
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Filters(self):
        r"""Key可选值为condition

<li> **condition** </li>	Values = 查询条件，用户组ID或用户组名称
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserGroupsResponse(AbstractModel):
    r"""ListUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 用户组列表
        :type Content: list of UserGroup
        :param _Total: 总条数
        :type Total: int
        :param _Pageable: 分页
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._Total = None
        self._Pageable = None
        self._RequestId = None

    @property
    def Content(self):
        r"""用户组列表
        :rtype: list of UserGroup
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Total(self):
        r"""总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        r"""分页
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = UserGroup()
                obj._deserialize(item)
                self._Content.append(obj)
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        self._RequestId = params.get("RequestId")


class ListUserRequest(AbstractModel):
    r"""ListUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Pageable: 分页数据
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Filters: Key可选值为condition、userGroupId

<li> **condition** </li>	Values = 查询条件，用户ID，用户名称，手机或邮箱
<li> **userGroupId** </li>	Values = 用户组ID
        :type Filters: list of Filter
        :param _Original: 返回信息是否为原文
        :type Original: bool
        """
        self._UserStoreId = None
        self._Pageable = None
        self._Filters = None
        self._Original = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Pageable(self):
        r"""分页数据
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Filters(self):
        r"""Key可选值为condition、userGroupId

<li> **condition** </li>	Values = 查询条件，用户ID，用户名称，手机或邮箱
<li> **userGroupId** </li>	Values = 用户组ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Original(self):
        r"""返回信息是否为原文
        :rtype: bool
        """
        return self._Original

    @Original.setter
    def Original(self, Original):
        self._Original = Original


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Original = params.get("Original")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserResponse(AbstractModel):
    r"""ListUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Pageable: 分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param _Content: 用户列表
        :type Content: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Pageable = None
        self._Content = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Pageable(self):
        r"""分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        """
        return self._Pageable

    @Pageable.setter
    def Pageable(self, Pageable):
        self._Pageable = Pageable

    @property
    def Content(self):
        r"""用户列表
        :rtype: list of User
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Pageable") is not None:
            self._Pageable = Pageable()
            self._Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserStoreRequest(AbstractModel):
    r"""ListUserStore请求参数结构体

    """


class ListUserStoreResponse(AbstractModel):
    r"""ListUserStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreSet: 用户目录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserStoreSet: list of UserStore
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserStoreSet = None
        self._RequestId = None

    @property
    def UserStoreSet(self):
        r"""用户目录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UserStore
        """
        return self._UserStoreSet

    @UserStoreSet.setter
    def UserStoreSet(self, UserStoreSet):
        self._UserStoreSet = UserStoreSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserStoreSet") is not None:
            self._UserStoreSet = []
            for item in params.get("UserStoreSet"):
                obj = UserStore()
                obj._deserialize(item)
                self._UserStoreSet.append(obj)
        self._RequestId = params.get("RequestId")


class LogMessage(AbstractModel):
    r"""日志详情

    """

    def __init__(self):
        r"""
        :param _LogId: 日志标识
        :type LogId: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UserStoreId: 用户池ID
        :type UserStoreId: str
        :param _EventCode: 事件编码
        :type EventCode: str
        :param _EventDate: 事件发生时间戳，单位：毫秒
        :type EventDate: int
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Participant: 事件参与者

<li> **TENANT** </li>  租户
<li> **USER** </li>  用户
        :type Participant: str
        :param _ApplicationClientId: 应用clientId
        :type ApplicationClientId: str
        :param _ApplicationName: 应用名称
        :type ApplicationName: str
        :param _AuthSourceId: 认证源ID
        :type AuthSourceId: str
        :param _AuthSourceName: 认证源名称
        :type AuthSourceName: str
        :param _AuthSourceType: 认证源类型
        :type AuthSourceType: str
        :param _AuthSourceCategory: 认证源类别
        :type AuthSourceCategory: str
        :param _Ip: IP地址
        :type Ip: str
        :param _UserAgent: 用户代理
        :type UserAgent: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _Detail: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        :param _ActionResult: 日志结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionResult: str
        """
        self._LogId = None
        self._TenantId = None
        self._UserStoreId = None
        self._EventCode = None
        self._EventDate = None
        self._Description = None
        self._Participant = None
        self._ApplicationClientId = None
        self._ApplicationName = None
        self._AuthSourceId = None
        self._AuthSourceName = None
        self._AuthSourceType = None
        self._AuthSourceCategory = None
        self._Ip = None
        self._UserAgent = None
        self._UserId = None
        self._Detail = None
        self._ActionResult = None

    @property
    def LogId(self):
        r"""日志标识
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TenantId(self):
        r"""租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserStoreId(self):
        r"""用户池ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def EventCode(self):
        r"""事件编码
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventDate(self):
        r"""事件发生时间戳，单位：毫秒
        :rtype: int
        """
        return self._EventDate

    @EventDate.setter
    def EventDate(self, EventDate):
        self._EventDate = EventDate

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Participant(self):
        r"""事件参与者

<li> **TENANT** </li>  租户
<li> **USER** </li>  用户
        :rtype: str
        """
        return self._Participant

    @Participant.setter
    def Participant(self, Participant):
        self._Participant = Participant

    @property
    def ApplicationClientId(self):
        r"""应用clientId
        :rtype: str
        """
        return self._ApplicationClientId

    @ApplicationClientId.setter
    def ApplicationClientId(self, ApplicationClientId):
        self._ApplicationClientId = ApplicationClientId

    @property
    def ApplicationName(self):
        r"""应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def AuthSourceId(self):
        r"""认证源ID
        :rtype: str
        """
        return self._AuthSourceId

    @AuthSourceId.setter
    def AuthSourceId(self, AuthSourceId):
        self._AuthSourceId = AuthSourceId

    @property
    def AuthSourceName(self):
        r"""认证源名称
        :rtype: str
        """
        return self._AuthSourceName

    @AuthSourceName.setter
    def AuthSourceName(self, AuthSourceName):
        self._AuthSourceName = AuthSourceName

    @property
    def AuthSourceType(self):
        r"""认证源类型
        :rtype: str
        """
        return self._AuthSourceType

    @AuthSourceType.setter
    def AuthSourceType(self, AuthSourceType):
        self._AuthSourceType = AuthSourceType

    @property
    def AuthSourceCategory(self):
        r"""认证源类别
        :rtype: str
        """
        return self._AuthSourceCategory

    @AuthSourceCategory.setter
    def AuthSourceCategory(self, AuthSourceCategory):
        self._AuthSourceCategory = AuthSourceCategory

    @property
    def Ip(self):
        r"""IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def UserAgent(self):
        r"""用户代理
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Detail(self):
        r"""详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ActionResult(self):
        r"""日志结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActionResult

    @ActionResult.setter
    def ActionResult(self, ActionResult):
        self._ActionResult = ActionResult


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._TenantId = params.get("TenantId")
        self._UserStoreId = params.get("UserStoreId")
        self._EventCode = params.get("EventCode")
        self._EventDate = params.get("EventDate")
        self._Description = params.get("Description")
        self._Participant = params.get("Participant")
        self._ApplicationClientId = params.get("ApplicationClientId")
        self._ApplicationName = params.get("ApplicationName")
        self._AuthSourceId = params.get("AuthSourceId")
        self._AuthSourceName = params.get("AuthSourceName")
        self._AuthSourceType = params.get("AuthSourceType")
        self._AuthSourceCategory = params.get("AuthSourceCategory")
        self._Ip = params.get("Ip")
        self._UserAgent = params.get("UserAgent")
        self._UserId = params.get("UserId")
        self._Detail = params.get("Detail")
        self._ActionResult = params.get("ActionResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberMap(AbstractModel):
    r"""Map数据类型

    """

    def __init__(self):
        r"""
        :param _Name: 健
        :type Name: str
        :param _Value: 值
        :type Value: str
        :param _Type: 类型
        :type Type: str
        """
        self._Name = None
        self._Value = None
        self._Type = None

    @property
    def Name(self):
        r"""健
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pageable(AbstractModel):
    r"""分页对象

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _PageNumber: 当前页码
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        r"""每页数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryUserFilter(AbstractModel):
    r"""查询用户信息条件

    """

    def __init__(self):
        r"""
        :param _PropertyKey: 属性key
        :type PropertyKey: str
        :param _PropertyValue: 属性value
        :type PropertyValue: str
        :param _Logic: 逻辑值，等于true，不等于false
        :type Logic: bool
        :param _OperateLogic: 操作逻辑符（支持> < = >= <=  != between）
        :type OperateLogic: str
        """
        self._PropertyKey = None
        self._PropertyValue = None
        self._Logic = None
        self._OperateLogic = None

    @property
    def PropertyKey(self):
        r"""属性key
        :rtype: str
        """
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def PropertyValue(self):
        r"""属性value
        :rtype: str
        """
        return self._PropertyValue

    @PropertyValue.setter
    def PropertyValue(self, PropertyValue):
        self._PropertyValue = PropertyValue

    @property
    def Logic(self):
        r"""逻辑值，等于true，不等于false
        :rtype: bool
        """
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic

    @property
    def OperateLogic(self):
        r"""操作逻辑符（支持> < = >= <=  != between）
        :rtype: str
        """
        return self._OperateLogic

    @OperateLogic.setter
    def OperateLogic(self, OperateLogic):
        self._OperateLogic = OperateLogic


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._PropertyValue = params.get("PropertyValue")
        self._Logic = params.get("Logic")
        self._OperateLogic = params.get("OperateLogic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    r"""ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        """
        self._UserId = None
        self._UserStoreId = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserStoreId = params.get("UserStoreId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    r"""ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 重置后的用户密码
        :type Password: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Password = None
        self._RequestId = None

    @property
    def Password(self):
        r"""重置后的用户密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._RequestId = params.get("RequestId")


class Salt(AbstractModel):
    r"""密码盐

    """

    def __init__(self):
        r"""
        :param _SaltValue: 盐值
        :type SaltValue: str
        :param _SaltLocation: 盐值位置
        :type SaltLocation: :class:`tencentcloud.ciam.v20220331.models.SaltLocation`
        """
        self._SaltValue = None
        self._SaltLocation = None

    @property
    def SaltValue(self):
        r"""盐值
        :rtype: str
        """
        return self._SaltValue

    @SaltValue.setter
    def SaltValue(self, SaltValue):
        self._SaltValue = SaltValue

    @property
    def SaltLocation(self):
        r"""盐值位置
        :rtype: :class:`tencentcloud.ciam.v20220331.models.SaltLocation`
        """
        return self._SaltLocation

    @SaltLocation.setter
    def SaltLocation(self, SaltLocation):
        self._SaltLocation = SaltLocation


    def _deserialize(self, params):
        self._SaltValue = params.get("SaltValue")
        if params.get("SaltLocation") is not None:
            self._SaltLocation = SaltLocation()
            self._SaltLocation._deserialize(params.get("SaltLocation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocation(AbstractModel):
    r"""盐位

    """

    def __init__(self):
        r"""
        :param _SaltLocationTypeEnum: 密码加盐的类型（HEAD，TAIL，OTHER）
        :type SaltLocationTypeEnum: str
        :param _SaltLocationRule: 加盐规则
        :type SaltLocationRule: :class:`tencentcloud.ciam.v20220331.models.SaltLocationRule`
        """
        self._SaltLocationTypeEnum = None
        self._SaltLocationRule = None

    @property
    def SaltLocationTypeEnum(self):
        r"""密码加盐的类型（HEAD，TAIL，OTHER）
        :rtype: str
        """
        return self._SaltLocationTypeEnum

    @SaltLocationTypeEnum.setter
    def SaltLocationTypeEnum(self, SaltLocationTypeEnum):
        self._SaltLocationTypeEnum = SaltLocationTypeEnum

    @property
    def SaltLocationRule(self):
        r"""加盐规则
        :rtype: :class:`tencentcloud.ciam.v20220331.models.SaltLocationRule`
        """
        return self._SaltLocationRule

    @SaltLocationRule.setter
    def SaltLocationRule(self, SaltLocationRule):
        self._SaltLocationRule = SaltLocationRule


    def _deserialize(self, params):
        self._SaltLocationTypeEnum = params.get("SaltLocationTypeEnum")
        if params.get("SaltLocationRule") is not None:
            self._SaltLocationRule = SaltLocationRule()
            self._SaltLocationRule._deserialize(params.get("SaltLocationRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaltLocationRule(AbstractModel):
    r"""盐位规则

    """

    def __init__(self):
        r"""
        :param _Regex: 表达式
        :type Regex: str
        """
        self._Regex = None

    @property
    def Regex(self):
        r"""表达式
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordRequest(AbstractModel):
    r"""SetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _Password: 密码
        :type Password: str
        """
        self._UserStoreId = None
        self._UserId = None
        self._Password = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Password(self):
        r"""密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordResponse(AbstractModel):
    r"""SetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Sort(AbstractModel):
    r"""查询用户排序

    """

    def __init__(self):
        r"""
        :param _PropertyKey: 排序字段的key，参考自定义属性
        :type PropertyKey: str
        :param _Order: 升序或者降序，ASC/DESC
        :type Order: str
        """
        self._PropertyKey = None
        self._Order = None

    @property
    def PropertyKey(self):
        r"""排序字段的key，参考自定义属性
        :rtype: str
        """
        return self._PropertyKey

    @PropertyKey.setter
    def PropertyKey(self, PropertyKey):
        self._PropertyKey = PropertyKey

    @property
    def Order(self):
        r"""升序或者降序，ASC/DESC
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._PropertyKey = params.get("PropertyKey")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserGroupRequest(AbstractModel):
    r"""UpdateUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID
        :type UserGroupId: str
        :param _DisplayName: 用户组名称
        :type DisplayName: str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _Description: 用户组描述
        :type Description: str
        """
        self._UserGroupId = None
        self._DisplayName = None
        self._UserStoreId = None
        self._Description = None

    @property
    def UserGroupId(self):
        r"""用户组ID
        :rtype: str
        """
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def DisplayName(self):
        r"""用户组名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Description(self):
        r"""用户组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._DisplayName = params.get("DisplayName")
        self._UserStoreId = params.get("UserStoreId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserGroupResponse(AbstractModel):
    r"""UpdateUserGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    r"""UpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _PhoneNumber: 手机号码
        :type PhoneNumber: str
        :param _Email: 邮箱
        :type Email: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _Address: 地址
        :type Address: str
        :param _UserGroup: 用户组
        :type UserGroup: list of str
        :param _Birthdate: 生日
        :type Birthdate: int
        :param _CustomizationAttributes: 自定义属性
        :type CustomizationAttributes: list of MemberMap
        :param _IndexedAttribute1: 索引字段1
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: 索引字段2
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: 索引字段3
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: 索引字段4
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: 索引字段5
        :type IndexedAttribute5: str
        """
        self._UserId = None
        self._UserStoreId = None
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._Nickname = None
        self._Address = None
        self._UserGroup = None
        self._Birthdate = None
        self._CustomizationAttributes = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserName(self):
        r"""用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        r"""手机号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        r"""邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Nickname(self):
        r"""昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        r"""地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UserGroup(self):
        r"""用户组
        :rtype: list of str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Birthdate(self):
        r"""生日
        :rtype: int
        """
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def CustomizationAttributes(self):
        r"""自定义属性
        :rtype: list of MemberMap
        """
        return self._CustomizationAttributes

    @CustomizationAttributes.setter
    def CustomizationAttributes(self, CustomizationAttributes):
        self._CustomizationAttributes = CustomizationAttributes

    @property
    def IndexedAttribute1(self):
        r"""索引字段1
        :rtype: str
        """
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        r"""索引字段2
        :rtype: str
        """
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        r"""索引字段3
        :rtype: str
        """
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        r"""索引字段4
        :rtype: str
        """
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        r"""索引字段5
        :rtype: str
        """
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserStoreId = params.get("UserStoreId")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._UserGroup = params.get("UserGroup")
        self._Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self._CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomizationAttributes.append(obj)
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    r"""UpdateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _User: 更新之后的用户信息
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""更新之后的用户信息
        :rtype: :class:`tencentcloud.ciam.v20220331.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class UpdateUserStatusRequest(AbstractModel):
    r"""UpdateUserStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _Status: 用户状态

<li> **NORMAL** </li>	  正常
<li> **LOCK** </li>  锁定
<li> **FREEZE** </li>	  冻结
        :type Status: str
        """
        self._UserStoreId = None
        self._UserId = None
        self._Status = None

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Status(self):
        r"""用户状态

<li> **NORMAL** </li>	  正常
<li> **LOCK** </li>  锁定
<li> **FREEZE** </li>	  冻结
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._UserStoreId = params.get("UserStoreId")
        self._UserId = params.get("UserId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStatusResponse(AbstractModel):
    r"""UpdateUserStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateUserStoreRequest(AbstractModel):
    r"""UpdateUserStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserPoolId: 用户池ID
        :type UserPoolId: str
        :param _UserPoolName: 用户池名字
        :type UserPoolName: str
        :param _UserPoolDesc: 用户池描述
        :type UserPoolDesc: str
        :param _UserPoolLogo: 用户池logo
        :type UserPoolLogo: str
        """
        self._UserPoolId = None
        self._UserPoolName = None
        self._UserPoolDesc = None
        self._UserPoolLogo = None

    @property
    def UserPoolId(self):
        r"""用户池ID
        :rtype: str
        """
        return self._UserPoolId

    @UserPoolId.setter
    def UserPoolId(self, UserPoolId):
        self._UserPoolId = UserPoolId

    @property
    def UserPoolName(self):
        r"""用户池名字
        :rtype: str
        """
        return self._UserPoolName

    @UserPoolName.setter
    def UserPoolName(self, UserPoolName):
        self._UserPoolName = UserPoolName

    @property
    def UserPoolDesc(self):
        r"""用户池描述
        :rtype: str
        """
        return self._UserPoolDesc

    @UserPoolDesc.setter
    def UserPoolDesc(self, UserPoolDesc):
        self._UserPoolDesc = UserPoolDesc

    @property
    def UserPoolLogo(self):
        r"""用户池logo
        :rtype: str
        """
        return self._UserPoolLogo

    @UserPoolLogo.setter
    def UserPoolLogo(self, UserPoolLogo):
        self._UserPoolLogo = UserPoolLogo


    def _deserialize(self, params):
        self._UserPoolId = params.get("UserPoolId")
        self._UserPoolName = params.get("UserPoolName")
        self._UserPoolDesc = params.get("UserPoolDesc")
        self._UserPoolLogo = params.get("UserPoolLogo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStoreResponse(AbstractModel):
    r"""UpdateUserStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _PhoneNumber: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _LastSignOn: 上次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSignOn: int
        :param _CreatedDate: 创建时间
        :type CreatedDate: int
        :param _Status: 状态
        :type Status: str
        :param _UserDataSourceEnum: 用户来源
        :type UserDataSourceEnum: str
        :param _Nickname: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nickname: str
        :param _Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _Birthdate: 生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthdate: int
        :param _UserGroups: 用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroups: list of str
        :param _LastModifiedDate: 上次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: int
        :param _CustomAttributes: 自定义属性
        :type CustomAttributes: list of MemberMap
        :param _ResidentIdentityCard: 身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type ResidentIdentityCard: str
        :param _QqOpenId: QQ的OpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type QqOpenId: str
        :param _QqUnionId: QQ的UnionId
注意：此字段可能返回 null，表示取不到有效值。
        :type QqUnionId: str
        :param _WechatOpenId: 微信的WechatOpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatOpenId: str
        :param _WechatUnionId: 微信的WechatUnionId
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatUnionId: str
        :param _AlipayUserId: 支付宝的AlipayUserId
注意：此字段可能返回 null，表示取不到有效值。
        :type AlipayUserId: str
        :param _WeComUserId: 企业微信的WeComUserId
注意：此字段可能返回 null，表示取不到有效值。
        :type WeComUserId: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Locale: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Locale: str
        :param _Gender: 性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: str
        :param _IdentityVerificationMethod: 实名核验方式
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityVerificationMethod: str
        :param _IdentityVerified: 是否已经实名核验
        :type IdentityVerified: bool
        :param _Job: 工作
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: str
        :param _Nationality: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param _Primary: 是否主账号（进行过账号融合后，主账号为true，从账号为false）
        :type Primary: bool
        :param _Zone: 时区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _AlreadyFirstLogin: 是否已经首次登录
        :type AlreadyFirstLogin: bool
        :param _TenantId: 租户id
        :type TenantId: str
        :param _UserStoreId: 用户目录id
        :type UserStoreId: str
        :param _Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _LockType: 锁定类型（分为管理员锁定，和登录策略锁定）
注意：此字段可能返回 null，表示取不到有效值。
        :type LockType: str
        :param _LockTime: 锁定时间点
注意：此字段可能返回 null，表示取不到有效值。
        :type LockTime: int
        :param _IndexedAttribute1: 索引字段1
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexedAttribute1: str
        :param _IndexedAttribute2: 索引字段2
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexedAttribute2: str
        :param _IndexedAttribute3: 索引字段3
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexedAttribute3: str
        :param _IndexedAttribute4: 索引字段4
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexedAttribute4: str
        :param _IndexedAttribute5: 索引字段5
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexedAttribute5: str
        """
        self._UserId = None
        self._UserName = None
        self._PhoneNumber = None
        self._Email = None
        self._LastSignOn = None
        self._CreatedDate = None
        self._Status = None
        self._UserDataSourceEnum = None
        self._Nickname = None
        self._Address = None
        self._Birthdate = None
        self._UserGroups = None
        self._LastModifiedDate = None
        self._CustomAttributes = None
        self._ResidentIdentityCard = None
        self._QqOpenId = None
        self._QqUnionId = None
        self._WechatOpenId = None
        self._WechatUnionId = None
        self._AlipayUserId = None
        self._WeComUserId = None
        self._Description = None
        self._Name = None
        self._Locale = None
        self._Gender = None
        self._IdentityVerificationMethod = None
        self._IdentityVerified = None
        self._Job = None
        self._Nationality = None
        self._Primary = None
        self._Zone = None
        self._AlreadyFirstLogin = None
        self._TenantId = None
        self._UserStoreId = None
        self._Version = None
        self._LockType = None
        self._LockTime = None
        self._IndexedAttribute1 = None
        self._IndexedAttribute2 = None
        self._IndexedAttribute3 = None
        self._IndexedAttribute4 = None
        self._IndexedAttribute5 = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        r"""手机号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        r"""邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastSignOn(self):
        r"""上次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastSignOn

    @LastSignOn.setter
    def LastSignOn(self, LastSignOn):
        self._LastSignOn = LastSignOn

    @property
    def CreatedDate(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserDataSourceEnum(self):
        r"""用户来源
        :rtype: str
        """
        return self._UserDataSourceEnum

    @UserDataSourceEnum.setter
    def UserDataSourceEnum(self, UserDataSourceEnum):
        self._UserDataSourceEnum = UserDataSourceEnum

    @property
    def Nickname(self):
        r"""昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Address(self):
        r"""地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthdate(self):
        r"""生日
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Birthdate

    @Birthdate.setter
    def Birthdate(self, Birthdate):
        self._Birthdate = Birthdate

    @property
    def UserGroups(self):
        r"""用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._UserGroups

    @UserGroups.setter
    def UserGroups(self, UserGroups):
        self._UserGroups = UserGroups

    @property
    def LastModifiedDate(self):
        r"""上次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastModifiedDate

    @LastModifiedDate.setter
    def LastModifiedDate(self, LastModifiedDate):
        self._LastModifiedDate = LastModifiedDate

    @property
    def CustomAttributes(self):
        r"""自定义属性
        :rtype: list of MemberMap
        """
        return self._CustomAttributes

    @CustomAttributes.setter
    def CustomAttributes(self, CustomAttributes):
        self._CustomAttributes = CustomAttributes

    @property
    def ResidentIdentityCard(self):
        r"""身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResidentIdentityCard

    @ResidentIdentityCard.setter
    def ResidentIdentityCard(self, ResidentIdentityCard):
        self._ResidentIdentityCard = ResidentIdentityCard

    @property
    def QqOpenId(self):
        r"""QQ的OpenId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QqOpenId

    @QqOpenId.setter
    def QqOpenId(self, QqOpenId):
        self._QqOpenId = QqOpenId

    @property
    def QqUnionId(self):
        r"""QQ的UnionId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QqUnionId

    @QqUnionId.setter
    def QqUnionId(self, QqUnionId):
        self._QqUnionId = QqUnionId

    @property
    def WechatOpenId(self):
        r"""微信的WechatOpenId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WechatOpenId

    @WechatOpenId.setter
    def WechatOpenId(self, WechatOpenId):
        self._WechatOpenId = WechatOpenId

    @property
    def WechatUnionId(self):
        r"""微信的WechatUnionId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WechatUnionId

    @WechatUnionId.setter
    def WechatUnionId(self, WechatUnionId):
        self._WechatUnionId = WechatUnionId

    @property
    def AlipayUserId(self):
        r"""支付宝的AlipayUserId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlipayUserId

    @AlipayUserId.setter
    def AlipayUserId(self, AlipayUserId):
        self._AlipayUserId = AlipayUserId

    @property
    def WeComUserId(self):
        r"""企业微信的WeComUserId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WeComUserId

    @WeComUserId.setter
    def WeComUserId(self, WeComUserId):
        self._WeComUserId = WeComUserId

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""姓名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Locale(self):
        r"""坐标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Locale

    @Locale.setter
    def Locale(self, Locale):
        self._Locale = Locale

    @property
    def Gender(self):
        r"""性别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def IdentityVerificationMethod(self):
        r"""实名核验方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdentityVerificationMethod

    @IdentityVerificationMethod.setter
    def IdentityVerificationMethod(self, IdentityVerificationMethod):
        self._IdentityVerificationMethod = IdentityVerificationMethod

    @property
    def IdentityVerified(self):
        r"""是否已经实名核验
        :rtype: bool
        """
        return self._IdentityVerified

    @IdentityVerified.setter
    def IdentityVerified(self, IdentityVerified):
        self._IdentityVerified = IdentityVerified

    @property
    def Job(self):
        r"""工作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def Nationality(self):
        r"""国家
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Primary(self):
        r"""是否主账号（进行过账号融合后，主账号为true，从账号为false）
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def Zone(self):
        r"""时区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AlreadyFirstLogin(self):
        r"""是否已经首次登录
        :rtype: bool
        """
        return self._AlreadyFirstLogin

    @AlreadyFirstLogin.setter
    def AlreadyFirstLogin(self, AlreadyFirstLogin):
        self._AlreadyFirstLogin = AlreadyFirstLogin

    @property
    def TenantId(self):
        r"""租户id
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserStoreId(self):
        r"""用户目录id
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def Version(self):
        r"""版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LockType(self):
        r"""锁定类型（分为管理员锁定，和登录策略锁定）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LockType

    @LockType.setter
    def LockType(self, LockType):
        self._LockType = LockType

    @property
    def LockTime(self):
        r"""锁定时间点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def IndexedAttribute1(self):
        r"""索引字段1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexedAttribute1

    @IndexedAttribute1.setter
    def IndexedAttribute1(self, IndexedAttribute1):
        self._IndexedAttribute1 = IndexedAttribute1

    @property
    def IndexedAttribute2(self):
        r"""索引字段2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexedAttribute2

    @IndexedAttribute2.setter
    def IndexedAttribute2(self, IndexedAttribute2):
        self._IndexedAttribute2 = IndexedAttribute2

    @property
    def IndexedAttribute3(self):
        r"""索引字段3
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexedAttribute3

    @IndexedAttribute3.setter
    def IndexedAttribute3(self, IndexedAttribute3):
        self._IndexedAttribute3 = IndexedAttribute3

    @property
    def IndexedAttribute4(self):
        r"""索引字段4
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexedAttribute4

    @IndexedAttribute4.setter
    def IndexedAttribute4(self, IndexedAttribute4):
        self._IndexedAttribute4 = IndexedAttribute4

    @property
    def IndexedAttribute5(self):
        r"""索引字段5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexedAttribute5

    @IndexedAttribute5.setter
    def IndexedAttribute5(self, IndexedAttribute5):
        self._IndexedAttribute5 = IndexedAttribute5


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._LastSignOn = params.get("LastSignOn")
        self._CreatedDate = params.get("CreatedDate")
        self._Status = params.get("Status")
        self._UserDataSourceEnum = params.get("UserDataSourceEnum")
        self._Nickname = params.get("Nickname")
        self._Address = params.get("Address")
        self._Birthdate = params.get("Birthdate")
        self._UserGroups = params.get("UserGroups")
        self._LastModifiedDate = params.get("LastModifiedDate")
        if params.get("CustomAttributes") is not None:
            self._CustomAttributes = []
            for item in params.get("CustomAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self._CustomAttributes.append(obj)
        self._ResidentIdentityCard = params.get("ResidentIdentityCard")
        self._QqOpenId = params.get("QqOpenId")
        self._QqUnionId = params.get("QqUnionId")
        self._WechatOpenId = params.get("WechatOpenId")
        self._WechatUnionId = params.get("WechatUnionId")
        self._AlipayUserId = params.get("AlipayUserId")
        self._WeComUserId = params.get("WeComUserId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Locale = params.get("Locale")
        self._Gender = params.get("Gender")
        self._IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self._IdentityVerified = params.get("IdentityVerified")
        self._Job = params.get("Job")
        self._Nationality = params.get("Nationality")
        self._Primary = params.get("Primary")
        self._Zone = params.get("Zone")
        self._AlreadyFirstLogin = params.get("AlreadyFirstLogin")
        self._TenantId = params.get("TenantId")
        self._UserStoreId = params.get("UserStoreId")
        self._Version = params.get("Version")
        self._LockType = params.get("LockType")
        self._LockTime = params.get("LockTime")
        self._IndexedAttribute1 = params.get("IndexedAttribute1")
        self._IndexedAttribute2 = params.get("IndexedAttribute2")
        self._IndexedAttribute3 = params.get("IndexedAttribute3")
        self._IndexedAttribute4 = params.get("IndexedAttribute4")
        self._IndexedAttribute5 = params.get("IndexedAttribute5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroup(AbstractModel):
    r"""用户组

    """

    def __init__(self):
        r"""
        :param _UserGroupId: 用户组ID
        :type UserGroupId: str
        :param _DisplayName: 用户组名称
        :type DisplayName: str
        :param _Description: 用户组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _CreatedDate: 创建时间
        :type CreatedDate: int
        :param _LastModifyDate: 最近更新时间
        :type LastModifyDate: int
        """
        self._UserGroupId = None
        self._DisplayName = None
        self._Description = None
        self._UserStoreId = None
        self._TenantId = None
        self._CreatedDate = None
        self._LastModifyDate = None

    @property
    def UserGroupId(self):
        r"""用户组ID
        :rtype: str
        """
        return self._UserGroupId

    @UserGroupId.setter
    def UserGroupId(self, UserGroupId):
        self._UserGroupId = UserGroupId

    @property
    def DisplayName(self):
        r"""用户组名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""用户组描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UserStoreId(self):
        r"""用户目录ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def TenantId(self):
        r"""租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def CreatedDate(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def LastModifyDate(self):
        r"""最近更新时间
        :rtype: int
        """
        return self._LastModifyDate

    @LastModifyDate.setter
    def LastModifyDate(self, LastModifyDate):
        self._LastModifyDate = LastModifyDate


    def _deserialize(self, params):
        self._UserGroupId = params.get("UserGroupId")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._UserStoreId = params.get("UserStoreId")
        self._TenantId = params.get("TenantId")
        self._CreatedDate = params.get("CreatedDate")
        self._LastModifyDate = params.get("LastModifyDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserGroupDeleteResp(AbstractModel):
    r"""删除用户组信息时返回的详情

    """

    def __init__(self):
        r"""
        :param _ErrorMessage: 错误详情
        :type ErrorMessage: str
        :param _AppAssociatedUserGroupIds: 用户组关联的应用信息
        :type AppAssociatedUserGroupIds: list of AppAssociatedUserGroupIds
        """
        self._ErrorMessage = None
        self._AppAssociatedUserGroupIds = None

    @property
    def ErrorMessage(self):
        r"""错误详情
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def AppAssociatedUserGroupIds(self):
        r"""用户组关联的应用信息
        :rtype: list of AppAssociatedUserGroupIds
        """
        return self._AppAssociatedUserGroupIds

    @AppAssociatedUserGroupIds.setter
    def AppAssociatedUserGroupIds(self, AppAssociatedUserGroupIds):
        self._AppAssociatedUserGroupIds = AppAssociatedUserGroupIds


    def _deserialize(self, params):
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("AppAssociatedUserGroupIds") is not None:
            self._AppAssociatedUserGroupIds = []
            for item in params.get("AppAssociatedUserGroupIds"):
                obj = AppAssociatedUserGroupIds()
                obj._deserialize(item)
                self._AppAssociatedUserGroupIds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserStore(AbstractModel):
    r"""用户池

    """

    def __init__(self):
        r"""
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UserStoreLogo: 用户池logo
注意：此字段可能返回 null，表示取不到有效值。
        :type UserStoreLogo: str
        :param _UserStoreDesc: 用户池描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UserStoreDesc: str
        :param _UserStoreName: 用户池名称
        :type UserStoreName: str
        :param _UserNum: 用户数量
        :type UserNum: int
        :param _UserStoreId: 用户池ID
        :type UserStoreId: str
        :param _AppNum: 应用数量
        :type AppNum: int
        :param _LastStatus: 上次切换的用户池
        :type LastStatus: bool
        :param _DefaultStatus: 默认用户池
        :type DefaultStatus: bool
        :param _CreateDate: 创建时间
        :type CreateDate: int
        :param _LastStatusTime: 上次切换时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastStatusTime: int
        :param _UserStoreProtocolHost: 用户目录域名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserStoreProtocolHost: str
        """
        self._TenantId = None
        self._UserStoreLogo = None
        self._UserStoreDesc = None
        self._UserStoreName = None
        self._UserNum = None
        self._UserStoreId = None
        self._AppNum = None
        self._LastStatus = None
        self._DefaultStatus = None
        self._CreateDate = None
        self._LastStatusTime = None
        self._UserStoreProtocolHost = None

    @property
    def TenantId(self):
        r"""租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserStoreLogo(self):
        r"""用户池logo
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserStoreLogo

    @UserStoreLogo.setter
    def UserStoreLogo(self, UserStoreLogo):
        self._UserStoreLogo = UserStoreLogo

    @property
    def UserStoreDesc(self):
        r"""用户池描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserStoreDesc

    @UserStoreDesc.setter
    def UserStoreDesc(self, UserStoreDesc):
        self._UserStoreDesc = UserStoreDesc

    @property
    def UserStoreName(self):
        r"""用户池名称
        :rtype: str
        """
        return self._UserStoreName

    @UserStoreName.setter
    def UserStoreName(self, UserStoreName):
        self._UserStoreName = UserStoreName

    @property
    def UserNum(self):
        r"""用户数量
        :rtype: int
        """
        return self._UserNum

    @UserNum.setter
    def UserNum(self, UserNum):
        self._UserNum = UserNum

    @property
    def UserStoreId(self):
        r"""用户池ID
        :rtype: str
        """
        return self._UserStoreId

    @UserStoreId.setter
    def UserStoreId(self, UserStoreId):
        self._UserStoreId = UserStoreId

    @property
    def AppNum(self):
        r"""应用数量
        :rtype: int
        """
        return self._AppNum

    @AppNum.setter
    def AppNum(self, AppNum):
        self._AppNum = AppNum

    @property
    def LastStatus(self):
        r"""上次切换的用户池
        :rtype: bool
        """
        return self._LastStatus

    @LastStatus.setter
    def LastStatus(self, LastStatus):
        self._LastStatus = LastStatus

    @property
    def DefaultStatus(self):
        r"""默认用户池
        :rtype: bool
        """
        return self._DefaultStatus

    @DefaultStatus.setter
    def DefaultStatus(self, DefaultStatus):
        self._DefaultStatus = DefaultStatus

    @property
    def CreateDate(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def LastStatusTime(self):
        r"""上次切换时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastStatusTime

    @LastStatusTime.setter
    def LastStatusTime(self, LastStatusTime):
        self._LastStatusTime = LastStatusTime

    @property
    def UserStoreProtocolHost(self):
        r"""用户目录域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserStoreProtocolHost

    @UserStoreProtocolHost.setter
    def UserStoreProtocolHost(self, UserStoreProtocolHost):
        self._UserStoreProtocolHost = UserStoreProtocolHost


    def _deserialize(self, params):
        self._TenantId = params.get("TenantId")
        self._UserStoreLogo = params.get("UserStoreLogo")
        self._UserStoreDesc = params.get("UserStoreDesc")
        self._UserStoreName = params.get("UserStoreName")
        self._UserNum = params.get("UserNum")
        self._UserStoreId = params.get("UserStoreId")
        self._AppNum = params.get("AppNum")
        self._LastStatus = params.get("LastStatus")
        self._DefaultStatus = params.get("DefaultStatus")
        self._CreateDate = params.get("CreateDate")
        self._LastStatusTime = params.get("LastStatusTime")
        self._UserStoreProtocolHost = params.get("UserStoreProtocolHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        