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


class CreateLibraryRequest(AbstractModel):
    """CreateLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 媒体库名称，最多 50 个字符
        :type Name: str
        :param _Remark: 备注，最多 250 个字符
        :type Remark: str
        :param _BucketName: 存储桶全名，新建后不可更改。当前版本不再支持指定存储桶。
        :type BucketName: str
        :param _BucketRegion: 存储桶所在地域，新建后不可更改。当前版本不再支持指定存储桶所在地域。
        :type BucketRegion: str
        :param _LibraryExtension: 媒体库配置项，部分参数新建后不可更改
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        self._Name = None
        self._Remark = None
        self._BucketName = None
        self._BucketRegion = None
        self._LibraryExtension = None

    @property
    def Name(self):
        """媒体库名称，最多 50 个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """备注，最多 250 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def BucketName(self):
        """存储桶全名，新建后不可更改。当前版本不再支持指定存储桶。
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        """存储桶所在地域，新建后不可更改。当前版本不再支持指定存储桶所在地域。
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def LibraryExtension(self):
        """媒体库配置项，部分参数新建后不可更改
        :rtype: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        return self._LibraryExtension

    @LibraryExtension.setter
    def LibraryExtension(self, LibraryExtension):
        self._LibraryExtension = LibraryExtension


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        if params.get("LibraryExtension") is not None:
            self._LibraryExtension = LibraryExtension()
            self._LibraryExtension._deserialize(params.get("LibraryExtension"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLibraryResponse(AbstractModel):
    """CreateLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID
        :type LibraryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._RequestId = params.get("RequestId")


class CreateUserLifecycleRequest(AbstractModel):
    """CreateUserLifecycle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID。
        :type LibraryId: str
        :param _Filter: 用于唯一查找用户的过滤器。
        :type Filter: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        :param _IsolateTime: 隔离时间，当时间超过该时间点后，指定用户将无法登录，但他的账号信息、文件资源会被保留，可以通过再次调用本接口更新隔离时间，恢复登录。如不指定，则代表不设置隔离时间，且当前用户已经设置的隔离时间会被删除。
        :type IsolateTime: str
        :param _DestroyTime: 销毁时间，当时间超过该时间点后，指定用户的资源将被销毁且无法通过再次调用此接口更新时间。如果同时指定了 IsolateTime 则不能早于 IsolateTime 指定的时间。如不指定，则代表不设置销毁时间，且当前用户已经设置的销毁时间会被删除。
        :type DestroyTime: str
        """
        self._LibraryId = None
        self._Filter = None
        self._IsolateTime = None
        self._DestroyTime = None

    @property
    def LibraryId(self):
        """媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Filter(self):
        """用于唯一查找用户的过滤器。
        :rtype: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def IsolateTime(self):
        """隔离时间，当时间超过该时间点后，指定用户将无法登录，但他的账号信息、文件资源会被保留，可以通过再次调用本接口更新隔离时间，恢复登录。如不指定，则代表不设置隔离时间，且当前用户已经设置的隔离时间会被删除。
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def DestroyTime(self):
        """销毁时间，当时间超过该时间点后，指定用户的资源将被销毁且无法通过再次调用此接口更新时间。如果同时指定了 IsolateTime 则不能早于 IsolateTime 指定的时间。如不指定，则代表不设置销毁时间，且当前用户已经设置的销毁时间会被删除。
        :rtype: str
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        if params.get("Filter") is not None:
            self._Filter = UserFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._IsolateTime = params.get("IsolateTime")
        self._DestroyTime = params.get("DestroyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserLifecycleResponse(AbstractModel):
    """CreateUserLifecycle返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _IsolateTime: 设置的隔离时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _DestroyTime: 设置的销毁时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._IsolateTime = None
        self._DestroyTime = None
        self._RequestId = None

    @property
    def UserId(self):
        """用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsolateTime(self):
        """设置的隔离时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def DestroyTime(self):
        """设置的销毁时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._IsolateTime = params.get("IsolateTime")
        self._DestroyTime = params.get("DestroyTime")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID。
        :type LibraryId: str
        :param _Role: 用户角色，当只支持 user。
        :type Role: str
        :param _Enabled: 是否启用。
        :type Enabled: bool
        :param _CountryCode: 手机号国家码，不传默认为 null，此时无法使用该登录方式进行登录。
        :type CountryCode: str
        :param _PhoneNumber: 手机号码，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有手机号重复则报错。CountryCode 和 PhoneNumber 必须同时传入或同时不传入。
        :type PhoneNumber: str
        :param _Email: 邮箱，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有邮箱重复则报错。
        :type Email: str
        :param _AccountName: 账号，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 50 个字符。
        :type AccountName: str
        :param _AccountPassword: 密码的 base64 形式，不传默认为 null，此时无法使用该登录方式进行登录。AccountName 和 AccountPassword 必须同时传入或同时不传入。
        :type AccountPassword: str
        :param _AccountUserId: 第三方账号 ID，用于关联第三方账号体系，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有第三方账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 200 个字符。
        :type AccountUserId: str
        :param _Comment: 备注。不超过 255 个字符。
        :type Comment: str
        :param _Nickname: 昵称。不超过 100 个字符。
        :type Nickname: str
        :param _Avatar: 用户头像地址。不超过 255 个字符。
        :type Avatar: str
        :param _Customize: 自定义信息。不超过 255 个字符。
        :type Customize: str
        """
        self._LibraryId = None
        self._Role = None
        self._Enabled = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._Email = None
        self._AccountName = None
        self._AccountPassword = None
        self._AccountUserId = None
        self._Comment = None
        self._Nickname = None
        self._Avatar = None
        self._Customize = None

    @property
    def LibraryId(self):
        """媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Role(self):
        """用户角色，当只支持 user。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Enabled(self):
        """是否启用。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CountryCode(self):
        """手机号国家码，不传默认为 null，此时无法使用该登录方式进行登录。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        """手机号码，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有手机号重复则报错。CountryCode 和 PhoneNumber 必须同时传入或同时不传入。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        """邮箱，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有邮箱重复则报错。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AccountName(self):
        """账号，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 50 个字符。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        """密码的 base64 形式，不传默认为 null，此时无法使用该登录方式进行登录。AccountName 和 AccountPassword 必须同时传入或同时不传入。
        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def AccountUserId(self):
        """第三方账号 ID，用于关联第三方账号体系，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有第三方账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 200 个字符。
        :rtype: str
        """
        return self._AccountUserId

    @AccountUserId.setter
    def AccountUserId(self, AccountUserId):
        self._AccountUserId = AccountUserId

    @property
    def Comment(self):
        """备注。不超过 255 个字符。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Nickname(self):
        """昵称。不超过 100 个字符。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        """用户头像地址。不超过 255 个字符。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Customize(self):
        """自定义信息。不超过 255 个字符。
        :rtype: str
        """
        return self._Customize

    @Customize.setter
    def Customize(self, Customize):
        self._Customize = Customize


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._Role = params.get("Role")
        self._Enabled = params.get("Enabled")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._AccountUserId = params.get("AccountUserId")
        self._Comment = params.get("Comment")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        self._Customize = params.get("Customize")
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
        :param _LibraryId: 用户所在的媒体库 ID。
        :type LibraryId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _CreationTime: 用户创建时间。
        :type CreationTime: str
        :param _Role: 用户角色.
        :type Role: str
        :param _Enabled: 是否启用。
        :type Enabled: bool
        :param _CountryCode: 手机号国家码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryCode: str
        :param _PhoneNumber: 手机号码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _Email: 邮箱，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _AccountName: 账号，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _AccountUserId: 第三方账号 ID，用于关联第三方账号体系，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUserId: str
        :param _Comment: 备注。
        :type Comment: str
        :param _Nickname: 昵称。
        :type Nickname: str
        :param _Avatar: 用户头像地址。
        :type Avatar: str
        :param _Customize: 自定义信息。
        :type Customize: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._UserId = None
        self._CreationTime = None
        self._Role = None
        self._Enabled = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._Email = None
        self._AccountName = None
        self._AccountUserId = None
        self._Comment = None
        self._Nickname = None
        self._Avatar = None
        self._Customize = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """用户所在的媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def UserId(self):
        """用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CreationTime(self):
        """用户创建时间。
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Role(self):
        """用户角色.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Enabled(self):
        """是否启用。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CountryCode(self):
        """手机号国家码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        """手机号码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        """邮箱，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AccountName(self):
        """账号，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountUserId(self):
        """第三方账号 ID，用于关联第三方账号体系，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUserId

    @AccountUserId.setter
    def AccountUserId(self, AccountUserId):
        self._AccountUserId = AccountUserId

    @property
    def Comment(self):
        """备注。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Nickname(self):
        """昵称。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        """用户头像地址。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Customize(self):
        """自定义信息。
        :rtype: str
        """
        return self._Customize

    @Customize.setter
    def Customize(self, Customize):
        self._Customize = Customize

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._UserId = params.get("UserId")
        self._CreationTime = params.get("CreationTime")
        self._Role = params.get("Role")
        self._Enabled = params.get("Enabled")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._AccountName = params.get("AccountName")
        self._AccountUserId = params.get("AccountUserId")
        self._Comment = params.get("Comment")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        self._Customize = params.get("Customize")
        self._RequestId = params.get("RequestId")


class DeleteLibraryRequest(AbstractModel):
    """DeleteLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID
        :type LibraryId: str
        """
        self._LibraryId = None

    @property
    def LibraryId(self):
        """媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibraryResponse(AbstractModel):
    """DeleteLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        :param _LibraryId: 媒体库 ID。
        :type LibraryId: str
        :param _Filters: 用于唯一查找用户的过滤器数组，数组之间为 **或** 的关系，即满足任意一个过滤器的用户，都将被删除，单次传入的过滤器最多为 100 个。
        :type Filters: list of UserFilter
        """
        self._LibraryId = None
        self._Filters = None

    @property
    def LibraryId(self):
        """媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Filters(self):
        """用于唯一查找用户的过滤器数组，数组之间为 **或** 的关系，即满足任意一个过滤器的用户，都将被删除，单次传入的过滤器最多为 100 个。
        :rtype: list of UserFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = UserFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeLibrariesRequest(AbstractModel):
    """DescribeLibraries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryIds: 按照一个或者多个媒体库 ID 查询，每次请求的上限为 100 个。
        :type LibraryIds: list of str
        :param _PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param _PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        """
        self._LibraryIds = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def LibraryIds(self):
        """按照一个或者多个媒体库 ID 查询，每次请求的上限为 100 个。
        :rtype: list of str
        """
        return self._LibraryIds

    @LibraryIds.setter
    def LibraryIds(self, LibraryIds):
        self._LibraryIds = LibraryIds

    @property
    def PageNumber(self):
        """页码，整型，配合 PageSize 使用，默认值为 1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._LibraryIds = params.get("LibraryIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibrariesResponse(AbstractModel):
    """DescribeLibraries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 媒体库列表
        :type List: list of Library
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        """媒体库列表
        :rtype: list of Library
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Library()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLibrarySecretRequest(AbstractModel):
    """DescribeLibrarySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID
        :type LibraryId: str
        """
        self._LibraryId = None

    @property
    def LibraryId(self):
        """媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibrarySecretResponse(AbstractModel):
    """DescribeLibrarySecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 查询的媒体库 ID
        :type LibraryId: str
        :param _LibrarySecret: 查询到的媒体库密钥
        :type LibrarySecret: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._LibrarySecret = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """查询的媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def LibrarySecret(self):
        """查询到的媒体库密钥
        :rtype: str
        """
        return self._LibrarySecret

    @LibrarySecret.setter
    def LibrarySecret(self, LibrarySecret):
        self._LibrarySecret = LibrarySecret

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._LibrarySecret = params.get("LibrarySecret")
        self._RequestId = params.get("RequestId")


class DescribeOfficialInstancesRequest(AbstractModel):
    """DescribeOfficialInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SuperAdminAccount: 是否查询实例绑定的超级管理员账号，默认值为 false。
        :type SuperAdminAccount: bool
        :param _InstanceIds: 按照一个或者多个实例 ID 查询，每次请求的上限为 100 个。
        :type InstanceIds: list of str
        :param _PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param _PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        :param _OrderBy: 对指定列进行排序
        :type OrderBy: str
        :param _OrderByType: 排序方式
        :type OrderByType: str
        :param _AutoRenew: 续费管理筛选类型
        :type AutoRenew: int
        :param _BindPhone: 超级管理管理员账号是否绑定了手机号
        :type BindPhone: bool
        """
        self._SuperAdminAccount = None
        self._InstanceIds = None
        self._PageNumber = None
        self._PageSize = None
        self._OrderBy = None
        self._OrderByType = None
        self._AutoRenew = None
        self._BindPhone = None

    @property
    def SuperAdminAccount(self):
        """是否查询实例绑定的超级管理员账号，默认值为 false。
        :rtype: bool
        """
        return self._SuperAdminAccount

    @SuperAdminAccount.setter
    def SuperAdminAccount(self, SuperAdminAccount):
        self._SuperAdminAccount = SuperAdminAccount

    @property
    def InstanceIds(self):
        """按照一个或者多个实例 ID 查询，每次请求的上限为 100 个。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def PageNumber(self):
        """页码，整型，配合 PageSize 使用，默认值为 1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrderBy(self):
        """对指定列进行排序
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序方式
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def AutoRenew(self):
        """续费管理筛选类型
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def BindPhone(self):
        """超级管理管理员账号是否绑定了手机号
        :rtype: bool
        """
        return self._BindPhone

    @BindPhone.setter
    def BindPhone(self, BindPhone):
        self._BindPhone = BindPhone


    def _deserialize(self, params):
        self._SuperAdminAccount = params.get("SuperAdminAccount")
        self._InstanceIds = params.get("InstanceIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._AutoRenew = params.get("AutoRenew")
        self._BindPhone = params.get("BindPhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfficialInstancesResponse(AbstractModel):
    """DescribeOfficialInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 实例列表
        :type List: list of Instance
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        """实例列表
        :rtype: list of Instance
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Instance()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOfficialOverviewRequest(AbstractModel):
    """DescribeOfficialOverview请求参数结构体

    """


class DescribeOfficialOverviewResponse(AbstractModel):
    """DescribeOfficialOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Quantity: 云盘实例数量
        :type Quantity: int
        :param _Storage: 已经使用的总存储量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Storage: str
        :param _UserCount: 已经分配和使用的总用户数
        :type UserCount: int
        :param _InternetTraffic: 本月外网下行流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type InternetTraffic: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Quantity = None
        self._Storage = None
        self._UserCount = None
        self._InternetTraffic = None
        self._RequestId = None

    @property
    def Quantity(self):
        """云盘实例数量
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Storage(self):
        """已经使用的总存储量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def UserCount(self):
        """已经分配和使用的总用户数
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def InternetTraffic(self):
        """本月外网下行流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._InternetTraffic

    @InternetTraffic.setter
    def InternetTraffic(self, InternetTraffic):
        self._InternetTraffic = InternetTraffic

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Quantity = params.get("Quantity")
        self._Storage = params.get("Storage")
        self._UserCount = params.get("UserCount")
        self._InternetTraffic = params.get("InternetTraffic")
        self._RequestId = params.get("RequestId")


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 按照一个或者多个资源 ID 查询，每次请求的上限为 100 个。
        :type ResourceIds: list of str
        :param _PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param _PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        :param _OrderBy: 对指定列进行排序
        :type OrderBy: str
        :param _OrderByType: 排序方式
        :type OrderByType: str
        :param _Type: 来源类型筛选
        :type Type: int
        """
        self._ResourceIds = None
        self._PageNumber = None
        self._PageSize = None
        self._OrderBy = None
        self._OrderByType = None
        self._Type = None

    @property
    def ResourceIds(self):
        """按照一个或者多个资源 ID 查询，每次请求的上限为 100 个。
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def PageNumber(self):
        """页码，整型，配合 PageSize 使用，默认值为 1。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrderBy(self):
        """对指定列进行排序
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序方式
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Type(self):
        """来源类型筛选
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 流量包列表
        :type List: list of TrafficPackage
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        """流量包列表
        :rtype: list of TrafficPackage
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserLifecycleRequest(AbstractModel):
    """DescribeUserLifecycle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID。
        :type LibraryId: str
        :param _Filter: 用于唯一查找用户的过滤器。
        :type Filter: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        """
        self._LibraryId = None
        self._Filter = None

    @property
    def LibraryId(self):
        """媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Filter(self):
        """用于唯一查找用户的过滤器。
        :rtype: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        if params.get("Filter") is not None:
            self._Filter = UserFilter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserLifecycleResponse(AbstractModel):
    """DescribeUserLifecycle返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _IsolateTime: 设置的隔离时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _DestroyTime: 设置的销毁时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._IsolateTime = None
        self._DestroyTime = None
        self._RequestId = None

    @property
    def UserId(self):
        """用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsolateTime(self):
        """设置的隔离时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def DestroyTime(self):
        """设置的销毁时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._IsolateTime = params.get("IsolateTime")
        self._DestroyTime = params.get("DestroyTime")
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """官方云盘实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Domain: 专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _EffectiveTime: 生效时间
        :type EffectiveTime: str
        :param _ExpireTime: 过期时间。如果为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _UserLimit: 用户数量。如果为按量计费或不限制用户数量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserLimit: int
        :param _StorageLimit: 存储容量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: str
        :param _StorageLimitGB: 存储容量，单位为 GB。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimitGB: int
        :param _Isolated: 是否过期隔离
        :type Isolated: bool
        :param _AutoRenew: 续费标识。0：手动续费；1：自动续费；2：到期不续。
        :type AutoRenew: int
        :param _SuperAdminAccount: 超级管理员账号，如果未选择查询实例绑定的超级管理员账号或当前实例未绑定超级管理员账号，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuperAdminAccount: str
        :param _Bucket: 自选桶模式下，展示存储桶使用
        :type Bucket: str
        :param _LogBucket: 自选桶模式下，展示日志桶使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBucket: str
        """
        self._InstanceId = None
        self._Domain = None
        self._EffectiveTime = None
        self._ExpireTime = None
        self._UserLimit = None
        self._StorageLimit = None
        self._StorageLimitGB = None
        self._Isolated = None
        self._AutoRenew = None
        self._SuperAdminAccount = None
        self._Bucket = None
        self._LogBucket = None

    @property
    def InstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Domain(self):
        """专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def EffectiveTime(self):
        """生效时间
        :rtype: str
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def ExpireTime(self):
        """过期时间。如果为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserLimit(self):
        """用户数量。如果为按量计费或不限制用户数量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UserLimit

    @UserLimit.setter
    def UserLimit(self, UserLimit):
        self._UserLimit = UserLimit

    @property
    def StorageLimit(self):
        """存储容量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def StorageLimitGB(self):
        """存储容量，单位为 GB。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageLimitGB

    @StorageLimitGB.setter
    def StorageLimitGB(self, StorageLimitGB):
        self._StorageLimitGB = StorageLimitGB

    @property
    def Isolated(self):
        """是否过期隔离
        :rtype: bool
        """
        return self._Isolated

    @Isolated.setter
    def Isolated(self, Isolated):
        self._Isolated = Isolated

    @property
    def AutoRenew(self):
        """续费标识。0：手动续费；1：自动续费；2：到期不续。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SuperAdminAccount(self):
        """超级管理员账号，如果未选择查询实例绑定的超级管理员账号或当前实例未绑定超级管理员账号，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SuperAdminAccount

    @SuperAdminAccount.setter
    def SuperAdminAccount(self, SuperAdminAccount):
        self._SuperAdminAccount = SuperAdminAccount

    @property
    def Bucket(self):
        """自选桶模式下，展示存储桶使用
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def LogBucket(self):
        """自选桶模式下，展示日志桶使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogBucket

    @LogBucket.setter
    def LogBucket(self, LogBucket):
        self._LogBucket = LogBucket


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Domain = params.get("Domain")
        self._EffectiveTime = params.get("EffectiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._UserLimit = params.get("UserLimit")
        self._StorageLimit = params.get("StorageLimit")
        self._StorageLimitGB = params.get("StorageLimitGB")
        self._Isolated = params.get("Isolated")
        self._AutoRenew = params.get("AutoRenew")
        self._SuperAdminAccount = params.get("SuperAdminAccount")
        self._Bucket = params.get("Bucket")
        self._LogBucket = params.get("LogBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Library(AbstractModel):
    """PaaS 服务媒体库信息

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID
        :type LibraryId: str
        :param _Name: 媒体库友好名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _BucketName: 媒体库绑定的 COS 存储桶
        :type BucketName: str
        :param _BucketRegion: 媒体库绑定的 COS 存储桶所在的地域
        :type BucketRegion: str
        :param _CreationTime: 媒体库创建时间
        :type CreationTime: str
        :param _LibraryExtension: 媒体库配置项
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        :param _Size: 媒体库用量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Size: str
        :param _DirNum: 媒体库目录数，由于数字类型精度限制，该字段为 String 类型。
        :type DirNum: str
        :param _FileNum: 媒体库文件数，由于数字类型精度限制，该字段为 String 类型。
        :type FileNum: str
        """
        self._LibraryId = None
        self._Name = None
        self._Remark = None
        self._BucketName = None
        self._BucketRegion = None
        self._CreationTime = None
        self._LibraryExtension = None
        self._Size = None
        self._DirNum = None
        self._FileNum = None

    @property
    def LibraryId(self):
        """媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Name(self):
        """媒体库友好名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def BucketName(self):
        """媒体库绑定的 COS 存储桶
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketRegion(self):
        """媒体库绑定的 COS 存储桶所在的地域
        :rtype: str
        """
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def CreationTime(self):
        """媒体库创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LibraryExtension(self):
        """媒体库配置项
        :rtype: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        return self._LibraryExtension

    @LibraryExtension.setter
    def LibraryExtension(self, LibraryExtension):
        self._LibraryExtension = LibraryExtension

    @property
    def Size(self):
        """媒体库用量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def DirNum(self):
        """媒体库目录数，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._DirNum

    @DirNum.setter
    def DirNum(self, DirNum):
        self._DirNum = DirNum

    @property
    def FileNum(self):
        """媒体库文件数，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._FileNum

    @FileNum.setter
    def FileNum(self, FileNum):
        self._FileNum = FileNum


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._BucketName = params.get("BucketName")
        self._BucketRegion = params.get("BucketRegion")
        self._CreationTime = params.get("CreationTime")
        if params.get("LibraryExtension") is not None:
            self._LibraryExtension = LibraryExtension()
            self._LibraryExtension._deserialize(params.get("LibraryExtension"))
        self._Size = params.get("Size")
        self._DirNum = params.get("DirNum")
        self._FileNum = params.get("FileNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibraryExtension(AbstractModel):
    """媒体库配置项

    """

    def __init__(self):
        r"""
        :param _IsFileLibrary: true 为文件类型媒体库，可存储任何类型文件；false 为媒体类型媒体库，仅可存储照片和视频类型文件。默认为 false。在媒体库创建后不能修改。
        :type IsFileLibrary: bool
        :param _IsMultiSpace: true 为多租户空间媒体库，可创建多个租户空间；false 为单租户空间媒体库，不能创建租户空间，仅可使用默认的单一租户空间。默认为 false。在媒体库创建后不能修改。
        :type IsMultiSpace: bool
        :param _CosStorageClass: 保存至 COS 对象存储的文件的存储类型，仅支持 STANDARD、STANDARD_IA、INTELLIGENT_TIERING、MAZ_STANDARD、MAZ_STANDARD_IA 和 MAZ_INTELLIGENT_TIERING，默认为 STANDARD，当使用多 AZ 存储桶时将自动使用 MAZ_ 开头的用于多 AZ 的存储类型，否则自动使用非 MAZ_ 开头的用于非多 AZ 的存储类型。当指定智能分层存储 INTELLIGENT_TIERING 或 MAZ_INTELLIGENT_TIERING 时，需要事先为存储桶开启智能分层存储，否则将返回失败。在媒体库创建后不能修改。
        :type CosStorageClass: str
        :param _UseRecycleBin: 是否开启回收站功能。默认为 false。
        :type UseRecycleBin: bool
        :param _AutoRemoveRecycledDays: 当开启回收站时，自动删除回收站项目的天数，不能超过 1095（3 年），指定为 0 则不自动删除，默认为 0。当未开启回收站时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRemoveRecycledDays: int
        :param _EnableSearch: 是否启用文件路径搜索功能。默认为 false。
        :type EnableSearch: bool
        :param _DenyOnQuotaLessThanUsage: 设置媒体库或租户空间配额且配额小于已使用存储量时，是否拒绝设置请求。默认为 false。
        :type DenyOnQuotaLessThanUsage: bool
        :param _EnableFileHistory: 是否开启历史版本。默认为 false。
        :type EnableFileHistory: bool
        :param _FileHistoryCount: 当开启历史版本时，指定单个文件保留的历史版本的数量上限，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileHistoryCount: int
        :param _FileHistoryExpireDay: 当开启历史版本时，指定历史版本保留的最长天数，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileHistoryExpireDay: int
        :param _MaxDirFileNameLength: 目录或文件名的最长长度，不能超过 255，默认为 255。修改该参数不会影响存量目录或文件名，即如果将该字段的值改小，已经存在的长度超过目标值的目录或文件名不会发生变化。
        :type MaxDirFileNameLength: int
        :param _IsPublicRead: 是否开启公有读，开启后读操作无需使用访问令牌，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublicRead: bool
        :param _IsMultiAlbum: 媒体类型媒体库是否开启多相簿，开启后可创建一级目录（即相簿）且媒体文件只能保存在各相簿中，否则不能创建相簿且媒体文件只能保存在根目录。默认为 false。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。在媒体库创建后不能修改。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiAlbum: bool
        :param _AllowPhoto: 媒体类型媒体库是否允许上传照片，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowPhoto: bool
        :param _AllowPhotoExtName: 当媒体类型媒体库允许上传照片时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowPhotoExtName: list of str
        :param _AllowVideo: 媒体类型媒体库是否允许上传视频，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowVideo: bool
        :param _AllowVideoExtName: 当媒体类型媒体库允许上传视频时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowVideoExtName: list of str
        :param _AllowFileExtName: 指定文件类型媒体库允许的文件扩展名，默认为空数组，此时允许上传所有类型文件。仅单租户空间文件类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowFileExtName: list of str
        :param _RecognizeSensitiveContent: 照片上传时是否进行敏感内容鉴定，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognizeSensitiveContent: bool
        """
        self._IsFileLibrary = None
        self._IsMultiSpace = None
        self._CosStorageClass = None
        self._UseRecycleBin = None
        self._AutoRemoveRecycledDays = None
        self._EnableSearch = None
        self._DenyOnQuotaLessThanUsage = None
        self._EnableFileHistory = None
        self._FileHistoryCount = None
        self._FileHistoryExpireDay = None
        self._MaxDirFileNameLength = None
        self._IsPublicRead = None
        self._IsMultiAlbum = None
        self._AllowPhoto = None
        self._AllowPhotoExtName = None
        self._AllowVideo = None
        self._AllowVideoExtName = None
        self._AllowFileExtName = None
        self._RecognizeSensitiveContent = None

    @property
    def IsFileLibrary(self):
        """true 为文件类型媒体库，可存储任何类型文件；false 为媒体类型媒体库，仅可存储照片和视频类型文件。默认为 false。在媒体库创建后不能修改。
        :rtype: bool
        """
        return self._IsFileLibrary

    @IsFileLibrary.setter
    def IsFileLibrary(self, IsFileLibrary):
        self._IsFileLibrary = IsFileLibrary

    @property
    def IsMultiSpace(self):
        """true 为多租户空间媒体库，可创建多个租户空间；false 为单租户空间媒体库，不能创建租户空间，仅可使用默认的单一租户空间。默认为 false。在媒体库创建后不能修改。
        :rtype: bool
        """
        return self._IsMultiSpace

    @IsMultiSpace.setter
    def IsMultiSpace(self, IsMultiSpace):
        self._IsMultiSpace = IsMultiSpace

    @property
    def CosStorageClass(self):
        """保存至 COS 对象存储的文件的存储类型，仅支持 STANDARD、STANDARD_IA、INTELLIGENT_TIERING、MAZ_STANDARD、MAZ_STANDARD_IA 和 MAZ_INTELLIGENT_TIERING，默认为 STANDARD，当使用多 AZ 存储桶时将自动使用 MAZ_ 开头的用于多 AZ 的存储类型，否则自动使用非 MAZ_ 开头的用于非多 AZ 的存储类型。当指定智能分层存储 INTELLIGENT_TIERING 或 MAZ_INTELLIGENT_TIERING 时，需要事先为存储桶开启智能分层存储，否则将返回失败。在媒体库创建后不能修改。
        :rtype: str
        """
        return self._CosStorageClass

    @CosStorageClass.setter
    def CosStorageClass(self, CosStorageClass):
        self._CosStorageClass = CosStorageClass

    @property
    def UseRecycleBin(self):
        """是否开启回收站功能。默认为 false。
        :rtype: bool
        """
        return self._UseRecycleBin

    @UseRecycleBin.setter
    def UseRecycleBin(self, UseRecycleBin):
        self._UseRecycleBin = UseRecycleBin

    @property
    def AutoRemoveRecycledDays(self):
        """当开启回收站时，自动删除回收站项目的天数，不能超过 1095（3 年），指定为 0 则不自动删除，默认为 0。当未开启回收站时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRemoveRecycledDays

    @AutoRemoveRecycledDays.setter
    def AutoRemoveRecycledDays(self, AutoRemoveRecycledDays):
        self._AutoRemoveRecycledDays = AutoRemoveRecycledDays

    @property
    def EnableSearch(self):
        """是否启用文件路径搜索功能。默认为 false。
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def DenyOnQuotaLessThanUsage(self):
        """设置媒体库或租户空间配额且配额小于已使用存储量时，是否拒绝设置请求。默认为 false。
        :rtype: bool
        """
        return self._DenyOnQuotaLessThanUsage

    @DenyOnQuotaLessThanUsage.setter
    def DenyOnQuotaLessThanUsage(self, DenyOnQuotaLessThanUsage):
        self._DenyOnQuotaLessThanUsage = DenyOnQuotaLessThanUsage

    @property
    def EnableFileHistory(self):
        """是否开启历史版本。默认为 false。
        :rtype: bool
        """
        return self._EnableFileHistory

    @EnableFileHistory.setter
    def EnableFileHistory(self, EnableFileHistory):
        self._EnableFileHistory = EnableFileHistory

    @property
    def FileHistoryCount(self):
        """当开启历史版本时，指定单个文件保留的历史版本的数量上限，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileHistoryCount

    @FileHistoryCount.setter
    def FileHistoryCount(self, FileHistoryCount):
        self._FileHistoryCount = FileHistoryCount

    @property
    def FileHistoryExpireDay(self):
        """当开启历史版本时，指定历史版本保留的最长天数，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileHistoryExpireDay

    @FileHistoryExpireDay.setter
    def FileHistoryExpireDay(self, FileHistoryExpireDay):
        self._FileHistoryExpireDay = FileHistoryExpireDay

    @property
    def MaxDirFileNameLength(self):
        """目录或文件名的最长长度，不能超过 255，默认为 255。修改该参数不会影响存量目录或文件名，即如果将该字段的值改小，已经存在的长度超过目标值的目录或文件名不会发生变化。
        :rtype: int
        """
        return self._MaxDirFileNameLength

    @MaxDirFileNameLength.setter
    def MaxDirFileNameLength(self, MaxDirFileNameLength):
        self._MaxDirFileNameLength = MaxDirFileNameLength

    @property
    def IsPublicRead(self):
        """是否开启公有读，开启后读操作无需使用访问令牌，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsPublicRead

    @IsPublicRead.setter
    def IsPublicRead(self, IsPublicRead):
        self._IsPublicRead = IsPublicRead

    @property
    def IsMultiAlbum(self):
        """媒体类型媒体库是否开启多相簿，开启后可创建一级目录（即相簿）且媒体文件只能保存在各相簿中，否则不能创建相簿且媒体文件只能保存在根目录。默认为 false。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。在媒体库创建后不能修改。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsMultiAlbum

    @IsMultiAlbum.setter
    def IsMultiAlbum(self, IsMultiAlbum):
        self._IsMultiAlbum = IsMultiAlbum

    @property
    def AllowPhoto(self):
        """媒体类型媒体库是否允许上传照片，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AllowPhoto

    @AllowPhoto.setter
    def AllowPhoto(self, AllowPhoto):
        self._AllowPhoto = AllowPhoto

    @property
    def AllowPhotoExtName(self):
        """当媒体类型媒体库允许上传照片时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AllowPhotoExtName

    @AllowPhotoExtName.setter
    def AllowPhotoExtName(self, AllowPhotoExtName):
        self._AllowPhotoExtName = AllowPhotoExtName

    @property
    def AllowVideo(self):
        """媒体类型媒体库是否允许上传视频，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AllowVideo

    @AllowVideo.setter
    def AllowVideo(self, AllowVideo):
        self._AllowVideo = AllowVideo

    @property
    def AllowVideoExtName(self):
        """当媒体类型媒体库允许上传视频时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AllowVideoExtName

    @AllowVideoExtName.setter
    def AllowVideoExtName(self, AllowVideoExtName):
        self._AllowVideoExtName = AllowVideoExtName

    @property
    def AllowFileExtName(self):
        """指定文件类型媒体库允许的文件扩展名，默认为空数组，此时允许上传所有类型文件。仅单租户空间文件类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AllowFileExtName

    @AllowFileExtName.setter
    def AllowFileExtName(self, AllowFileExtName):
        self._AllowFileExtName = AllowFileExtName

    @property
    def RecognizeSensitiveContent(self):
        """照片上传时是否进行敏感内容鉴定，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RecognizeSensitiveContent

    @RecognizeSensitiveContent.setter
    def RecognizeSensitiveContent(self, RecognizeSensitiveContent):
        self._RecognizeSensitiveContent = RecognizeSensitiveContent


    def _deserialize(self, params):
        self._IsFileLibrary = params.get("IsFileLibrary")
        self._IsMultiSpace = params.get("IsMultiSpace")
        self._CosStorageClass = params.get("CosStorageClass")
        self._UseRecycleBin = params.get("UseRecycleBin")
        self._AutoRemoveRecycledDays = params.get("AutoRemoveRecycledDays")
        self._EnableSearch = params.get("EnableSearch")
        self._DenyOnQuotaLessThanUsage = params.get("DenyOnQuotaLessThanUsage")
        self._EnableFileHistory = params.get("EnableFileHistory")
        self._FileHistoryCount = params.get("FileHistoryCount")
        self._FileHistoryExpireDay = params.get("FileHistoryExpireDay")
        self._MaxDirFileNameLength = params.get("MaxDirFileNameLength")
        self._IsPublicRead = params.get("IsPublicRead")
        self._IsMultiAlbum = params.get("IsMultiAlbum")
        self._AllowPhoto = params.get("AllowPhoto")
        self._AllowPhotoExtName = params.get("AllowPhotoExtName")
        self._AllowVideo = params.get("AllowVideo")
        self._AllowVideoExtName = params.get("AllowVideoExtName")
        self._AllowFileExtName = params.get("AllowFileExtName")
        self._RecognizeSensitiveContent = params.get("RecognizeSensitiveContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryRequest(AbstractModel):
    """ModifyLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID
        :type LibraryId: str
        :param _Name: 媒体库名称，最多 50 个字符。如不传则不修改。
        :type Name: str
        :param _Remark: 备注，最多 250 个字符。如不传则不修改。
        :type Remark: str
        :param _LibraryExtension: 媒体库配置项，部分参数在新建后不可更改，且仅修改传入的参数。如不传该参数则不修改任何配置项。
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        self._LibraryId = None
        self._Name = None
        self._Remark = None
        self._LibraryExtension = None

    @property
    def LibraryId(self):
        """媒体库 ID
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Name(self):
        """媒体库名称，最多 50 个字符。如不传则不修改。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """备注，最多 250 个字符。如不传则不修改。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def LibraryExtension(self):
        """媒体库配置项，部分参数在新建后不可更改，且仅修改传入的参数。如不传该参数则不修改任何配置项。
        :rtype: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        return self._LibraryExtension

    @LibraryExtension.setter
    def LibraryExtension(self, LibraryExtension):
        self._LibraryExtension = LibraryExtension


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        if params.get("LibraryExtension") is not None:
            self._LibraryExtension = LibraryExtension()
            self._LibraryExtension._deserialize(params.get("LibraryExtension"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryResponse(AbstractModel):
    """ModifyLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 媒体库 ID。
        :type LibraryId: str
        :param _Filter: 用于唯一查找用户的过滤器。
        :type Filter: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        :param _Role: 用户角色，当只支持 user。
        :type Role: str
        :param _Enabled: 是否启用。
        :type Enabled: bool
        :param _CountryCode: 手机号国家码，不传默认为 null，此时无法使用该登录方式进行登录。
        :type CountryCode: str
        :param _PhoneNumber: 手机号码，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有手机号重复则报错。CountryCode 和 PhoneNumber 必须同时传入或同时不传入。
        :type PhoneNumber: str
        :param _Email: 邮箱，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有邮箱重复则报错。
        :type Email: str
        :param _AccountName: 账号，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 50 个字符。
        :type AccountName: str
        :param _AccountPassword: 密码的 base64 形式，不传默认为 null，此时无法使用该登录方式进行登录。AccountName 和 AccountPassword 必须同时传入或同时不传入。
        :type AccountPassword: str
        :param _AccountUserId: 第三方账号 ID，用于关联第三方账号体系，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有第三方账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 200 个字符。
        :type AccountUserId: str
        :param _Comment: 备注。不超过 255 个字符。
        :type Comment: str
        :param _Nickname: 昵称。不超过 100 个字符。
        :type Nickname: str
        :param _Avatar: 用户头像地址。不超过 255 个字符。
        :type Avatar: str
        :param _Customize: 自定义信息。不超过 255 个字符。
        :type Customize: str
        """
        self._LibraryId = None
        self._Filter = None
        self._Role = None
        self._Enabled = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._Email = None
        self._AccountName = None
        self._AccountPassword = None
        self._AccountUserId = None
        self._Comment = None
        self._Nickname = None
        self._Avatar = None
        self._Customize = None

    @property
    def LibraryId(self):
        """媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def Filter(self):
        """用于唯一查找用户的过滤器。
        :rtype: :class:`tencentcloud.smh.v20210712.models.UserFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Role(self):
        """用户角色，当只支持 user。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Enabled(self):
        """是否启用。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CountryCode(self):
        """手机号国家码，不传默认为 null，此时无法使用该登录方式进行登录。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        """手机号码，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有手机号重复则报错。CountryCode 和 PhoneNumber 必须同时传入或同时不传入。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        """邮箱，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有邮箱重复则报错。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AccountName(self):
        """账号，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 50 个字符。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        """密码的 base64 形式，不传默认为 null，此时无法使用该登录方式进行登录。AccountName 和 AccountPassword 必须同时传入或同时不传入。
        :rtype: str
        """
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def AccountUserId(self):
        """第三方账号 ID，用于关联第三方账号体系，不传默认为 null，此时无法使用该登录方式进行登录。如果与同一媒体库内已有第三方账号重复则报错。只能使用大小写字母、数字、中划线、下划线、小数点，长度不超过 200 个字符。
        :rtype: str
        """
        return self._AccountUserId

    @AccountUserId.setter
    def AccountUserId(self, AccountUserId):
        self._AccountUserId = AccountUserId

    @property
    def Comment(self):
        """备注。不超过 255 个字符。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Nickname(self):
        """昵称。不超过 100 个字符。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        """用户头像地址。不超过 255 个字符。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Customize(self):
        """自定义信息。不超过 255 个字符。
        :rtype: str
        """
        return self._Customize

    @Customize.setter
    def Customize(self, Customize):
        self._Customize = Customize


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        if params.get("Filter") is not None:
            self._Filter = UserFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Role = params.get("Role")
        self._Enabled = params.get("Enabled")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._AccountUserId = params.get("AccountUserId")
        self._Comment = params.get("Comment")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        self._Customize = params.get("Customize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LibraryId: 用户所在的媒体库 ID。
        :type LibraryId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _CreationTime: 用户创建时间。
        :type CreationTime: str
        :param _Role: 用户角色.
        :type Role: str
        :param _Enabled: 是否启用。
        :type Enabled: bool
        :param _CountryCode: 手机号国家码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryCode: str
        :param _PhoneNumber: 手机号码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _Email: 邮箱，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _AccountName: 账号，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _AccountUserId: 第三方账号 ID，用于关联第三方账号体系，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUserId: str
        :param _Comment: 备注。
        :type Comment: str
        :param _Nickname: 昵称。
        :type Nickname: str
        :param _Avatar: 用户头像地址。
        :type Avatar: str
        :param _Customize: 自定义信息。
        :type Customize: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LibraryId = None
        self._UserId = None
        self._CreationTime = None
        self._Role = None
        self._Enabled = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._Email = None
        self._AccountName = None
        self._AccountUserId = None
        self._Comment = None
        self._Nickname = None
        self._Avatar = None
        self._Customize = None
        self._RequestId = None

    @property
    def LibraryId(self):
        """用户所在的媒体库 ID。
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def UserId(self):
        """用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CreationTime(self):
        """用户创建时间。
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Role(self):
        """用户角色.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Enabled(self):
        """是否启用。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CountryCode(self):
        """手机号国家码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        """手机号码，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        """邮箱，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AccountName(self):
        """账号，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountUserId(self):
        """第三方账号 ID，用于关联第三方账号体系，如未指定则为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountUserId

    @AccountUserId.setter
    def AccountUserId(self, AccountUserId):
        self._AccountUserId = AccountUserId

    @property
    def Comment(self):
        """备注。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Nickname(self):
        """昵称。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        """用户头像地址。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Customize(self):
        """自定义信息。
        :rtype: str
        """
        return self._Customize

    @Customize.setter
    def Customize(self, Customize):
        self._Customize = Customize

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._UserId = params.get("UserId")
        self._CreationTime = params.get("CreationTime")
        self._Role = params.get("Role")
        self._Enabled = params.get("Enabled")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._AccountName = params.get("AccountName")
        self._AccountUserId = params.get("AccountUserId")
        self._Comment = params.get("Comment")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        self._Customize = params.get("Customize")
        self._RequestId = params.get("RequestId")


class SendSmsCodeRequest(AbstractModel):
    """SendSmsCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Purpose: 验证码目的，当前支持换绑超级管理员账号， BindSuperAdmin；体验版企业升级，ChannelUpdateVerify等
        :type Purpose: str
        :param _PhoneNumber: 将作为超级管理员账号的手机号码
        :type PhoneNumber: str
        :param _InstanceId: 官方云盘实例 ID
        :type InstanceId: str
        :param _CountryCode: 将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :type CountryCode: str
        """
        self._Purpose = None
        self._PhoneNumber = None
        self._InstanceId = None
        self._CountryCode = None

    @property
    def Purpose(self):
        """验证码目的，当前支持换绑超级管理员账号， BindSuperAdmin；体验版企业升级，ChannelUpdateVerify等
        :rtype: str
        """
        return self._Purpose

    @Purpose.setter
    def Purpose(self, Purpose):
        self._Purpose = Purpose

    @property
    def PhoneNumber(self):
        """将作为超级管理员账号的手机号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def InstanceId(self):
        """官方云盘实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CountryCode(self):
        """将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode


    def _deserialize(self, params):
        self._Purpose = params.get("Purpose")
        self._PhoneNumber = params.get("PhoneNumber")
        self._InstanceId = params.get("InstanceId")
        self._CountryCode = params.get("CountryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsCodeResponse(AbstractModel):
    """SendSmsCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TrafficPackage(AbstractModel):
    """流量资源包信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 流量资源包所抵扣的实例 ID
        :type InstanceId: str
        :param _Domain: 专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Type: 流量资源包来源类型，0 为付费购买，1 为赠送。
        :type Type: int
        :param _Size: 总流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Size: str
        :param _SizeGB: 总流量，单位为 GB
        :type SizeGB: int
        :param _Remain: 剩余流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Remain: str
        :param _Used: 已使用流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Used: str
        :param _UsedPercentage: 已使用百分比，由于数字类型精度限制，该字段为 String 类型。
        :type UsedPercentage: str
        :param _EffectiveTime: 生效时间，即流量资源包的订购时间
        :type EffectiveTime: str
        :param _ExpireTime: 过期时间，即所抵扣的实例的过期时间。如果流量资源包所抵扣的实例为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        """
        self._InstanceId = None
        self._Domain = None
        self._Type = None
        self._Size = None
        self._SizeGB = None
        self._Remain = None
        self._Used = None
        self._UsedPercentage = None
        self._EffectiveTime = None
        self._ExpireTime = None

    @property
    def InstanceId(self):
        """流量资源包所抵扣的实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Domain(self):
        """专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Type(self):
        """流量资源包来源类型，0 为付费购买，1 为赠送。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        """总流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SizeGB(self):
        """总流量，单位为 GB
        :rtype: int
        """
        return self._SizeGB

    @SizeGB.setter
    def SizeGB(self, SizeGB):
        self._SizeGB = SizeGB

    @property
    def Remain(self):
        """剩余流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Used(self):
        """已使用流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def UsedPercentage(self):
        """已使用百分比，由于数字类型精度限制，该字段为 String 类型。
        :rtype: str
        """
        return self._UsedPercentage

    @UsedPercentage.setter
    def UsedPercentage(self, UsedPercentage):
        self._UsedPercentage = UsedPercentage

    @property
    def EffectiveTime(self):
        """生效时间，即流量资源包的订购时间
        :rtype: str
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def ExpireTime(self):
        """过期时间，即所抵扣的实例的过期时间。如果流量资源包所抵扣的实例为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Domain = params.get("Domain")
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._SizeGB = params.get("SizeGB")
        self._Remain = params.get("Remain")
        self._Used = params.get("Used")
        self._UsedPercentage = params.get("UsedPercentage")
        self._EffectiveTime = params.get("EffectiveTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserFilter(AbstractModel):
    """用于唯一查找用户的过滤器。

    """

    def __init__(self):
        r"""
        :param _Key: 过滤类型，当前支持：UserId、PhoneNumber、Email、AccountName、AccountUserId。
        :type Key: str
        :param _Value: 过滤值，只支持完全匹配，不支持模糊搜索。针对不同的 Key，Value 的取值如下：
UserId: user12345678abcde
PhoneNumber: +86-13800000000（格式为：{CountryCode}-{PhoneNumber}）
Email: admin@mail.foobar.com
AccountName: account_name
AccountUserId: x53mYVqykfPqTCqekbNwwa4aXk4
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """过滤类型，当前支持：UserId、PhoneNumber、Email、AccountName、AccountUserId。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """过滤值，只支持完全匹配，不支持模糊搜索。针对不同的 Key，Value 的取值如下：
UserId: user12345678abcde
PhoneNumber: +86-13800000000（格式为：{CountryCode}-{PhoneNumber}）
Email: admin@mail.foobar.com
AccountName: account_name
AccountUserId: x53mYVqykfPqTCqekbNwwa4aXk4
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySmsCodeRequest(AbstractModel):
    """VerifySmsCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Purpose: 验证码目的，当前支持换绑超级管理员账号，BindSuperAdmin；体验版企业升级验证ChannelUpdateVerify，等
        :type Purpose: str
        :param _PhoneNumber: 将作为超级管理员账号的手机号码
        :type PhoneNumber: str
        :param _Code: 短信验证码
        :type Code: str
        :param _InstanceId: 官方云盘实例 ID
        :type InstanceId: str
        :param _CountryCode: 将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :type CountryCode: str
        """
        self._Purpose = None
        self._PhoneNumber = None
        self._Code = None
        self._InstanceId = None
        self._CountryCode = None

    @property
    def Purpose(self):
        """验证码目的，当前支持换绑超级管理员账号，BindSuperAdmin；体验版企业升级验证ChannelUpdateVerify，等
        :rtype: str
        """
        return self._Purpose

    @Purpose.setter
    def Purpose(self, Purpose):
        self._Purpose = Purpose

    @property
    def PhoneNumber(self):
        """将作为超级管理员账号的手机号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Code(self):
        """短信验证码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def InstanceId(self):
        """官方云盘实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CountryCode(self):
        """将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode


    def _deserialize(self, params):
        self._Purpose = params.get("Purpose")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Code = params.get("Code")
        self._InstanceId = params.get("InstanceId")
        self._CountryCode = params.get("CountryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySmsCodeResponse(AbstractModel):
    """VerifySmsCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")