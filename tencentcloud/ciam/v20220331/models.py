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


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param PhoneNumber: 手机号码
        :type PhoneNumber: str
        :param Email: 邮箱
        :type Email: str
        :param Password: 密码
        :type Password: str
        :param UserName: 用户名
        :type UserName: str
        :param Nickname: 昵称
        :type Nickname: str
        :param Address: 地址
        :type Address: str
        :param UserGroup: 用户组ID
        :type UserGroup: list of str
        :param Birthdate: 生日
        :type Birthdate: int
        :param CustomizationAttributes: 自定义属性
        :type CustomizationAttributes: list of MemberMap
        """
        self.UserStoreId = None
        self.PhoneNumber = None
        self.Email = None
        self.Password = None
        self.UserName = None
        self.Nickname = None
        self.Address = None
        self.UserGroup = None
        self.Birthdate = None
        self.CustomizationAttributes = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.UserGroup = params.get("UserGroup")
        self.Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self.CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomizationAttributes.append(obj)
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
        :param User: 创建的用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param UserIds: 用户ID数组
        :type UserIds: list of str
        """
        self.UserStoreId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    """DeleteUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeUserByIdRequest(AbstractModel):
    """DescribeUserById请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param UserId: 用户ID
        :type UserId: str
        """
        self.UserStoreId = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserByIdResponse(AbstractModel):
    """DescribeUserById返回参数结构体

    """

    def __init__(self):
        r"""
        :param User: 用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询条件

    """

    def __init__(self):
        r"""
        :param Key: key值
        :type Key: str
        :param Values: value值
        :type Values: list of str
        :param Logic: 逻辑值
        :type Logic: bool
        """
        self.Key = None
        self.Values = None
        self.Logic = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        self.Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountRequest(AbstractModel):
    """LinkAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param PrimaryUserId: 主用户ID
        :type PrimaryUserId: str
        :param SecondaryUserId: 从用户ID
        :type SecondaryUserId: str
        :param UserLinkedOnAttribute: 融合属性(PHONENUMBER,EMAIL)
        :type UserLinkedOnAttribute: str
        """
        self.UserStoreId = None
        self.PrimaryUserId = None
        self.SecondaryUserId = None
        self.UserLinkedOnAttribute = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PrimaryUserId = params.get("PrimaryUserId")
        self.SecondaryUserId = params.get("SecondaryUserId")
        self.UserLinkedOnAttribute = params.get("UserLinkedOnAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkAccountResponse(AbstractModel):
    """LinkAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ListUserByPropertyRequest(AbstractModel):
    """ListUserByProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param PropertyCode: 查询的属性（支持phoneNumber，email）
        :type PropertyCode: str
        :param PropertyValue: 属性值
        :type PropertyValue: str
        """
        self.UserStoreId = None
        self.PropertyCode = None
        self.PropertyValue = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.PropertyCode = params.get("PropertyCode")
        self.PropertyValue = params.get("PropertyValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserByPropertyResponse(AbstractModel):
    """ListUserByProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param Users: 用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of User
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class ListUserRequest(AbstractModel):
    """ListUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param Pageable: 分页数据
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param Filters: Key可选值为condition、userGroupId

<li> **condition** </li>	Values = 查询条件，用户ID，用户名称，手机或邮箱
<li> **userGroupId** </li>	Values = 用户组ID
        :type Filters: list of Filter
        """
        self.UserStoreId = None
        self.Pageable = None
        self.Filters = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserResponse(AbstractModel):
    """ListUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Pageable: 分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Pageable: :class:`tencentcloud.ciam.v20220331.models.Pageable`
        :param Content: 用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of User
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Pageable = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Pageable") is not None:
            self.Pageable = Pageable()
            self.Pageable._deserialize(params.get("Pageable"))
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = User()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class MemberMap(AbstractModel):
    """Map数据类型

    """

    def __init__(self):
        r"""
        :param Name: 健
        :type Name: str
        :param Value: 值
        :type Value: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Name = None
        self.Value = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pageable(AbstractModel):
    """分页对象

    """

    def __init__(self):
        r"""
        :param PageSize: 每页数量
        :type PageSize: int
        :param PageNumber: 当前页码
        :type PageNumber: int
        """
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        """
        self.UserId = None
        self.UserStoreId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserStoreId = params.get("UserStoreId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param Password: 重置后的用户密码
        :type Password: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Password = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.RequestId = params.get("RequestId")


class SetPasswordRequest(AbstractModel):
    """SetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param UserId: 用户ID
        :type UserId: str
        :param Password: 密码
        :type Password: str
        """
        self.UserStoreId = None
        self.UserId = None
        self.Password = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordResponse(AbstractModel):
    """SetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param UserName: 用户名称
        :type UserName: str
        :param PhoneNumber: 手机号码
        :type PhoneNumber: str
        :param Email: 邮箱
        :type Email: str
        :param Nickname: 昵称
        :type Nickname: str
        :param Address: 地址
        :type Address: str
        :param UserGroup: 用户组
        :type UserGroup: list of str
        :param Birthdate: 生日
        :type Birthdate: int
        :param CustomizationAttributes: 自定义属性
        :type CustomizationAttributes: list of MemberMap
        """
        self.UserId = None
        self.UserStoreId = None
        self.UserName = None
        self.PhoneNumber = None
        self.Email = None
        self.Nickname = None
        self.Address = None
        self.UserGroup = None
        self.Birthdate = None
        self.CustomizationAttributes = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserStoreId = params.get("UserStoreId")
        self.UserName = params.get("UserName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.UserGroup = params.get("UserGroup")
        self.Birthdate = params.get("Birthdate")
        if params.get("CustomizationAttributes") is not None:
            self.CustomizationAttributes = []
            for item in params.get("CustomizationAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomizationAttributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param User: 更新之后的用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type User: :class:`tencentcloud.ciam.v20220331.models.User`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class UpdateUserStatusRequest(AbstractModel):
    """UpdateUserStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserStoreId: 用户目录ID
        :type UserStoreId: str
        :param UserId: 用户ID
        :type UserId: str
        :param Status: NORMAL（正常）,LOCK（锁定）,FREEZE（冻结）,请传英文大写字母
        :type Status: str
        """
        self.UserStoreId = None
        self.UserId = None
        self.Status = None


    def _deserialize(self, params):
        self.UserStoreId = params.get("UserStoreId")
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStatusResponse(AbstractModel):
    """UpdateUserStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class User(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param PhoneNumber: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param LastSignOn: 上次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSignOn: int
        :param CreatedDate: 创建时间
        :type CreatedDate: int
        :param Status: 状态
        :type Status: str
        :param UserDataSourceEnum: 用户来源
        :type UserDataSourceEnum: str
        :param Nickname: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nickname: str
        :param Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Birthdate: 生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthdate: int
        :param UserGroups: 用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroups: list of str
        :param LastModifiedDate: 上次修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifiedDate: int
        :param CustomAttributes: 自定义属性
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomAttributes: list of MemberMap
        :param ResidentIdentityCard: 身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type ResidentIdentityCard: str
        :param QqOpenId: QQ的OpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type QqOpenId: str
        :param QqUnionId: QQ的UnionId
注意：此字段可能返回 null，表示取不到有效值。
        :type QqUnionId: str
        :param WechatOpenId: 微信的WechatOpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatOpenId: str
        :param WechatUnionId: 微信的WechatUnionId
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatUnionId: str
        :param AlipayUserId: 支付宝的AlipayUserId
注意：此字段可能返回 null，表示取不到有效值。
        :type AlipayUserId: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Locale: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Locale: str
        :param Gender: 性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: str
        :param IdentityVerificationMethod: 实名核验方式
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityVerificationMethod: str
        :param IdentityVerified: 是否已经实名核验
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityVerified: bool
        :param Job: 工作
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: str
        :param Nationality: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param Primary: 是否主账号（进行过账号融合后，主账号为true，从账号为false）
注意：此字段可能返回 null，表示取不到有效值。
        :type Primary: bool
        :param Zone: 时区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param AlreadyFirstLogin: 是否已经首次登录
注意：此字段可能返回 null，表示取不到有效值。
        :type AlreadyFirstLogin: bool
        :param TenantId: 租户id
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param UserStoreId: 用户目录id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserStoreId: str
        :param Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param LockType: 锁定类型（分为管理员锁定，和登录策略锁定）
注意：此字段可能返回 null，表示取不到有效值。
        :type LockType: str
        :param LockTime: 锁定时间点
注意：此字段可能返回 null，表示取不到有效值。
        :type LockTime: int
        """
        self.UserId = None
        self.UserName = None
        self.PhoneNumber = None
        self.Email = None
        self.LastSignOn = None
        self.CreatedDate = None
        self.Status = None
        self.UserDataSourceEnum = None
        self.Nickname = None
        self.Address = None
        self.Birthdate = None
        self.UserGroups = None
        self.LastModifiedDate = None
        self.CustomAttributes = None
        self.ResidentIdentityCard = None
        self.QqOpenId = None
        self.QqUnionId = None
        self.WechatOpenId = None
        self.WechatUnionId = None
        self.AlipayUserId = None
        self.Description = None
        self.Name = None
        self.Locale = None
        self.Gender = None
        self.IdentityVerificationMethod = None
        self.IdentityVerified = None
        self.Job = None
        self.Nationality = None
        self.Primary = None
        self.Zone = None
        self.AlreadyFirstLogin = None
        self.TenantId = None
        self.UserStoreId = None
        self.Version = None
        self.LockType = None
        self.LockTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Email = params.get("Email")
        self.LastSignOn = params.get("LastSignOn")
        self.CreatedDate = params.get("CreatedDate")
        self.Status = params.get("Status")
        self.UserDataSourceEnum = params.get("UserDataSourceEnum")
        self.Nickname = params.get("Nickname")
        self.Address = params.get("Address")
        self.Birthdate = params.get("Birthdate")
        self.UserGroups = params.get("UserGroups")
        self.LastModifiedDate = params.get("LastModifiedDate")
        if params.get("CustomAttributes") is not None:
            self.CustomAttributes = []
            for item in params.get("CustomAttributes"):
                obj = MemberMap()
                obj._deserialize(item)
                self.CustomAttributes.append(obj)
        self.ResidentIdentityCard = params.get("ResidentIdentityCard")
        self.QqOpenId = params.get("QqOpenId")
        self.QqUnionId = params.get("QqUnionId")
        self.WechatOpenId = params.get("WechatOpenId")
        self.WechatUnionId = params.get("WechatUnionId")
        self.AlipayUserId = params.get("AlipayUserId")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Locale = params.get("Locale")
        self.Gender = params.get("Gender")
        self.IdentityVerificationMethod = params.get("IdentityVerificationMethod")
        self.IdentityVerified = params.get("IdentityVerified")
        self.Job = params.get("Job")
        self.Nationality = params.get("Nationality")
        self.Primary = params.get("Primary")
        self.Zone = params.get("Zone")
        self.AlreadyFirstLogin = params.get("AlreadyFirstLogin")
        self.TenantId = params.get("TenantId")
        self.UserStoreId = params.get("UserStoreId")
        self.Version = params.get("Version")
        self.LockType = params.get("LockType")
        self.LockTime = params.get("LockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        