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


class AccessKey(AbstractModel):
    """访问密钥列表

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 访问密钥标识
        :type AccessKeyId: str
        :param _Status: 密钥状态，激活（Active）或未激活（Inactive）
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Description: 密钥描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._AccessKeyId = None
        self._Status = None
        self._CreateTime = None
        self._Description = None

    @property
    def AccessKeyId(self):
        """访问密钥标识
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def Status(self):
        """密钥状态，激活（Active）或未激活（Inactive）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        """密钥描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyDetail(AbstractModel):
    """访问密钥

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 访问密钥标识
        :type AccessKeyId: str
        :param _SecretAccessKey: 访问密钥（密钥仅创建时可见，请妥善保存）
        :type SecretAccessKey: str
        :param _Status: 密钥状态，激活（Active）或未激活（Inactive）
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._AccessKeyId = None
        self._SecretAccessKey = None
        self._Status = None
        self._CreateTime = None
        self._Description = None

    @property
    def AccessKeyId(self):
        """访问密钥标识
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        """访问密钥（密钥仅创建时可见，请妥善保存）
        :rtype: str
        """
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey

    @property
    def Status(self):
        """密钥状态，激活（Active）或未激活（Inactive）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        """描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretAccessKey = params.get("SecretAccessKey")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserRequest(AbstractModel):
    """AddUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 子用户用户名
        :type Name: str
        :param _Remark: 子用户备注
        :type Remark: str
        :param _ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param _UseApi: 是否生成子用户密钥。传0不生成子用户密钥，传1生成子用户密钥。
        :type UseApi: int
        :param _Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :type Password: str
        :param _NeedResetPassword: 子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :type NeedResetPassword: int
        :param _PhoneNum: 手机号
        :type PhoneNum: str
        :param _CountryCode: 区号
        :type CountryCode: str
        :param _Email: 邮箱
        :type Email: str
        """
        self._Name = None
        self._Remark = None
        self._ConsoleLogin = None
        self._UseApi = None
        self._Password = None
        self._NeedResetPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """子用户备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        """子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def UseApi(self):
        """是否生成子用户密钥。传0不生成子用户密钥，传1生成子用户密钥。
        :rtype: int
        """
        return self._UseApi

    @UseApi.setter
    def UseApi(self, UseApi):
        self._UseApi = UseApi

    @property
    def Password(self):
        """子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NeedResetPassword(self):
        """子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :rtype: int
        """
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword

    @property
    def PhoneNum(self):
        """手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """区号
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._UseApi = params.get("UseApi")
        self._Password = params.get("Password")
        self._NeedResetPassword = params.get("NeedResetPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserResponse(AbstractModel):
    """AddUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 子用户 UIN
        :type Uin: int
        :param _Name: 子用户用户名
        :type Name: str
        :param _Password: 如果输入参数组合为自动生成随机密码，则返回生成的密码
        :type Password: str
        :param _SecretId: 子用户密钥 ID
        :type SecretId: str
        :param _SecretKey: 子用户密钥 Key
        :type SecretKey: str
        :param _Uid: 子用户 UID
        :type Uid: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._Name = None
        self._Password = None
        self._SecretId = None
        self._SecretKey = None
        self._Uid = None
        self._RequestId = None

    @property
    def Uin(self):
        """子用户 UIN
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """如果输入参数组合为自动生成随机密码，则返回生成的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SecretId(self):
        """子用户密钥 ID
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        """子用户密钥 Key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Uid(self):
        """子用户 UID
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

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
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Uid = params.get("Uid")
        self._RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 添加的子用户 UIN/UID 和用户组 ID 关联关系
        :type Info: list of GroupIdOfUidInfo
        """
        self._Info = None

    @property
    def Info(self):
        """添加的子用户 UIN/UID 和用户组 ID 关联关系
        :rtype: list of GroupIdOfUidInfo
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup返回参数结构体

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


class AttachEntityOfPolicy(AbstractModel):
    """策略关联的实体信息

    """

    def __init__(self):
        r"""
        :param _Id: 实体ID
        :type Id: str
        :param _Name: 实体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Uin: 实体Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param _RelatedType: 关联类型。1 用户关联 ； 2 用户组关联 3 角色关联
        :type RelatedType: int
        :param _AttachmentTime: 策略关联时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachmentTime: str
        """
        self._Id = None
        self._Name = None
        self._Uin = None
        self._RelatedType = None
        self._AttachmentTime = None

    @property
    def Id(self):
        """实体ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """实体名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uin(self):
        """实体Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RelatedType(self):
        """关联类型。1 用户关联 ； 2 用户组关联 3 角色关联
        :rtype: int
        """
        return self._RelatedType

    @RelatedType.setter
    def RelatedType(self, RelatedType):
        self._RelatedType = RelatedType

    @property
    def AttachmentTime(self):
        """策略关联时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttachmentTime

    @AttachmentTime.setter
    def AttachmentTime(self, AttachmentTime):
        self._AttachmentTime = AttachmentTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Uin = params.get("Uin")
        self._RelatedType = params.get("RelatedType")
        self._AttachmentTime = params.get("AttachmentTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略 id
        :type PolicyId: int
        :param _AttachGroupId: 用户组 id
        :type AttachGroupId: int
        """
        self._PolicyId = None
        self._AttachGroupId = None

    @property
    def PolicyId(self):
        """策略 id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachGroupId(self):
        """用户组 id
        :rtype: int
        """
        return self._AttachGroupId

    @AttachGroupId.setter
    def AttachGroupId(self, AttachGroupId):
        self._AttachGroupId = AttachGroupId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachGroupId = params.get("AttachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy返回参数结构体

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


class AttachPolicyInfo(AbstractModel):
    """关联策略信息

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略id
        :type PolicyId: int
        :param _PolicyName: 策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _CreateMode: 创建来源，1 通过控制台创建, 2 通过策略语法创建
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param _PolicyType: 取值为User和QCS。User代表自定义策略，QCS代表系统策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _Remark: 策略备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _OperateOwnerUin: 策略关联操作者主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateOwnerUin: str
        :param _OperateUin: 策略关联操作者ID，如果UinType为0表示子账号Uin，如果UinType为1表示角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param _OperateUinType: 取值为0和1。OperateUinType为0表示OperateUin字段是子账号Uin。如果OperateUinType为1表示OperateUin字段是角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUinType: int
        :param _Deactived: 是否已下线，1代表已下线，0代表未下线
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param _DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._CreateMode = None
        self._PolicyType = None
        self._Remark = None
        self._OperateOwnerUin = None
        self._OperateUin = None
        self._OperateUinType = None
        self._Deactived = None
        self._DeactivedDetail = None

    @property
    def PolicyId(self):
        """策略id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def CreateMode(self):
        """创建来源，1 通过控制台创建, 2 通过策略语法创建
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def PolicyType(self):
        """取值为User和QCS。User代表自定义策略，QCS代表系统策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Remark(self):
        """策略备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def OperateOwnerUin(self):
        """策略关联操作者主账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperateOwnerUin

    @OperateOwnerUin.setter
    def OperateOwnerUin(self, OperateOwnerUin):
        self._OperateOwnerUin = OperateOwnerUin

    @property
    def OperateUin(self):
        """策略关联操作者ID，如果UinType为0表示子账号Uin，如果UinType为1表示角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def OperateUinType(self):
        """取值为0和1。OperateUinType为0表示OperateUin字段是子账号Uin。如果OperateUinType为1表示OperateUin字段是角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OperateUinType

    @OperateUinType.setter
    def OperateUinType(self, OperateUinType):
        self._OperateUinType = OperateUinType

    @property
    def Deactived(self):
        """是否已下线，1代表已下线，0代表未下线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        """已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._CreateMode = params.get("CreateMode")
        self._PolicyType = params.get("PolicyType")
        self._Remark = params.get("Remark")
        self._OperateOwnerUin = params.get("OperateOwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._OperateUinType = params.get("OperateUinType")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID，入参PolicyId与PolicyName二选一
        :type PolicyId: int
        :param _AttachRoleId: 角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type AttachRoleId: str
        :param _AttachRoleName: 角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type AttachRoleName: str
        :param _PolicyName: 策略名，入参PolicyId与PolicyName二选一
        :type PolicyName: str
        """
        self._PolicyId = None
        self._AttachRoleId = None
        self._AttachRoleName = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        """策略ID，入参PolicyId与PolicyName二选一
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachRoleId(self):
        """角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :rtype: str
        """
        return self._AttachRoleId

    @AttachRoleId.setter
    def AttachRoleId(self, AttachRoleId):
        self._AttachRoleId = AttachRoleId

    @property
    def AttachRoleName(self):
        """角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :rtype: str
        """
        return self._AttachRoleName

    @AttachRoleName.setter
    def AttachRoleName(self, AttachRoleName):
        self._AttachRoleName = AttachRoleName

    @property
    def PolicyName(self):
        """策略名，入参PolicyId与PolicyName二选一
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachRoleId = params.get("AttachRoleId")
        self._AttachRoleName = params.get("AttachRoleName")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy返回参数结构体

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


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略 id
        :type PolicyId: int
        :param _AttachUin: 子账号 uin
        :type AttachUin: int
        """
        self._PolicyId = None
        self._AttachUin = None

    @property
    def PolicyId(self):
        """策略 id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachUin(self):
        """子账号 uin
        :rtype: int
        """
        return self._AttachUin

    @AttachUin.setter
    def AttachUin(self, AttachUin):
        self._AttachUin = AttachUin


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachUin = params.get("AttachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回参数结构体

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


class AttachedPolicyOfRole(AbstractModel):
    """角色关联的策略信息

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _AddTime: 绑定时间
        :type AddTime: str
        :param _PolicyType: 策略类型，User表示自定义策略，QCS表示预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _CreateMode: 策略创建方式，1表示按产品功能或项目权限创建，其他表示按策略语法创建
        :type CreateMode: int
        :param _Deactived: 是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param _DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param _Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._PolicyType = None
        self._CreateMode = None
        self._Deactived = None
        self._DeactivedDetail = None
        self._Description = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        """绑定时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def PolicyType(self):
        """策略类型，User表示自定义策略，QCS表示预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def CreateMode(self):
        """策略创建方式，1表示按产品功能或项目权限创建，其他表示按策略语法创建
        :rtype: int
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Deactived(self):
        """是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        """已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail

    @property
    def Description(self):
        """策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._PolicyType = params.get("PolicyType")
        self._CreateMode = params.get("CreateMode")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicy(AbstractModel):
    """用户关联的策略详情

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _PolicyName: 策略名
        :type PolicyName: str
        :param _Description: 策略描述
        :type Description: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _StrategyType: 策略类型(1表示自定义策略，2表示预设策略)
        :type StrategyType: str
        :param _CreateMode: 创建模式(1表示按产品或项目权限创建的策略，其他表示策略语法创建的策略)
        :type CreateMode: str
        :param _Groups: 随组关联信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of AttachedUserPolicyGroupInfo
        :param _Deactived: 是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param _DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Description = None
        self._AddTime = None
        self._StrategyType = None
        self._CreateMode = None
        self._Groups = None
        self._Deactived = None
        self._DeactivedDetail = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        """策略描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        """创建时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def StrategyType(self):
        """策略类型(1表示自定义策略，2表示预设策略)
        :rtype: str
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def CreateMode(self):
        """创建模式(1表示按产品或项目权限创建的策略，其他表示策略语法创建的策略)
        :rtype: str
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Groups(self):
        """随组关联信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttachedUserPolicyGroupInfo
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Deactived(self):
        """是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        """已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._StrategyType = params.get("StrategyType")
        self._CreateMode = params.get("CreateMode")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = AttachedUserPolicyGroupInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicyGroupInfo(AbstractModel):
    """用户关联策略(随组关联)信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: int
        :param _GroupName: 分组名称
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthToken(AbstractModel):
    """认证凭据Token

    """

    def __init__(self):
        r"""
        :param _Token: 认证Token
        :type Token: str
        :param _CurrentTime: 服务器时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentTime: int
        :param _NextRotationTime: 毫秒时间戳，根据轮转周期准确计算得到
注意：此字段可能返回 null，表示取不到有效值。
        :type NextRotationTime: int
        :param _LastRotationTimeCost: 毫秒，如果轮转失败则为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :type LastRotationTimeCost: int
        :param _RotationStatus: 成功：success
失败：failed
注意：此字段可能返回 null，表示取不到有效值。
        :type RotationStatus: str
        :param _RotationMessage: 成功：success
失败：失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RotationMessage: str
        """
        self._Token = None
        self._CurrentTime = None
        self._NextRotationTime = None
        self._LastRotationTimeCost = None
        self._RotationStatus = None
        self._RotationMessage = None

    @property
    def Token(self):
        """认证Token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def CurrentTime(self):
        """服务器时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def NextRotationTime(self):
        """毫秒时间戳，根据轮转周期准确计算得到
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NextRotationTime

    @NextRotationTime.setter
    def NextRotationTime(self, NextRotationTime):
        self._NextRotationTime = NextRotationTime

    @property
    def LastRotationTimeCost(self):
        """毫秒，如果轮转失败则为 -1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastRotationTimeCost

    @LastRotationTimeCost.setter
    def LastRotationTimeCost(self, LastRotationTimeCost):
        self._LastRotationTimeCost = LastRotationTimeCost

    @property
    def RotationStatus(self):
        """成功：success
失败：failed
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RotationStatus

    @RotationStatus.setter
    def RotationStatus(self, RotationStatus):
        self._RotationStatus = RotationStatus

    @property
    def RotationMessage(self):
        """成功：success
失败：失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RotationMessage

    @RotationMessage.setter
    def RotationMessage(self, RotationMessage):
        self._RotationMessage = RotationMessage


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._CurrentTime = params.get("CurrentTime")
        self._NextRotationTime = params.get("NextRotationTime")
        self._LastRotationTimeCost = params.get("LastRotationTimeCost")
        self._RotationStatus = params.get("RotationStatus")
        self._RotationMessage = params.get("RotationMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildDataFlowAuthTokenRequest(AbstractModel):
    """BuildDataFlowAuthToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _ResourceAccount: 资源用户名
        :type ResourceAccount: str
        """
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceAccount = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceAccount(self):
        """资源用户名
        :rtype: str
        """
        return self._ResourceAccount

    @ResourceAccount.setter
    def ResourceAccount(self, ResourceAccount):
        self._ResourceAccount = ResourceAccount


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceAccount = params.get("ResourceAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildDataFlowAuthTokenResponse(AbstractModel):
    """BuildDataFlowAuthToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 认证凭据AuthToken信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Credentials: :class:`tencentcloud.cam.v20190116.models.AuthToken`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._RequestId = None

    @property
    def Credentials(self):
        """认证凭据AuthToken信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cam.v20190116.models.AuthToken`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

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
        if params.get("Credentials") is not None:
            self._Credentials = AuthToken()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MFAToken: 自定义多因子验证Token
        :type MFAToken: str
        """
        self._MFAToken = None

    @property
    def MFAToken(self):
        """自定义多因子验证Token
        :rtype: str
        """
        return self._MFAToken

    @MFAToken.setter
    def MFAToken(self, MFAToken):
        self._MFAToken = MFAToken


    def _deserialize(self, params):
        self._MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken返回参数结构体

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


class CreateAccessKeyRequest(AbstractModel):
    """CreateAccessKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 指定用户Uin，不填默认为当前用户创建访问密钥
        :type TargetUin: int
        :param _Description: 密钥描述，长度在1到1024之间，可包含大小写字符，数字以及特殊字符：=,.@:/-。 正则为：[\w+=,.@:/-]*。
        :type Description: str
        """
        self._TargetUin = None
        self._Description = None

    @property
    def TargetUin(self):
        """指定用户Uin，不填默认为当前用户创建访问密钥
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def Description(self):
        """密钥描述，长度在1到1024之间，可包含大小写字符，数字以及特殊字符：=,.@:/-。 正则为：[\w+=,.@:/-]*。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyResponse(AbstractModel):
    """CreateAccessKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKey: 访问密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: :class:`tencentcloud.cam.v20190116.models.AccessKeyDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessKey = None
        self._RequestId = None

    @property
    def AccessKey(self):
        """访问密钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cam.v20190116.models.AccessKeyDetail`
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

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
        if params.get("AccessKey") is not None:
            self._AccessKey = AccessKeyDetail()
            self._AccessKey._deserialize(params.get("AccessKey"))
        self._RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 用户组名
        :type GroupName: str
        :param _Remark: 用户组描述
        :type Remark: str
        """
        self._GroupName = None
        self._Remark = None

    @property
    def GroupName(self):
        """用户组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        """用户组描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateMessageReceiverRequest(AbstractModel):
    """CreateMessageReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 消息接收人的用户名
        :type Name: str
        :param _CountryCode: 手机号国际区号，国内为86
        :type CountryCode: str
        :param _PhoneNumber: 手机号码, 例如：132****2492
        :type PhoneNumber: str
        :param _Email: 邮箱，例如：57*****@qq.com
        :type Email: str
        :param _Remark: 消息接收人的备注，选填
        :type Remark: str
        """
        self._Name = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._Email = None
        self._Remark = None

    @property
    def Name(self):
        """消息接收人的用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CountryCode(self):
        """手机号国际区号，国内为86
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        """手机号码, 例如：132****2492
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Email(self):
        """邮箱，例如：57*****@qq.com
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Remark(self):
        """消息接收人的备注，选填
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Email = params.get("Email")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMessageReceiverResponse(AbstractModel):
    """CreateMessageReceiver返回参数结构体

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


class CreateOIDCConfigRequest(AbstractModel):
    """CreateOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL
        :type IdentityUrl: str
        :param _ClientId: 客户端ID
        :type ClientId: list of str
        :param _Name: 名称
        :type Name: str
        :param _IdentityKey: 签名公钥，需要base64
        :type IdentityKey: str
        :param _Description: 描述
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._Name = None
        self._IdentityKey = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID
        :rtype: list of str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdentityKey(self):
        """签名公钥，需要base64
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._Name = params.get("Name")
        self._IdentityKey = params.get("IdentityKey")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOIDCConfigResponse(AbstractModel):
    """CreateOIDCConfig返回参数结构体

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


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyName: 策略名称。长度为1~128个字符，可包含英文字母、数字和+=,.@-_。
        :type PolicyName: str
        :param _PolicyDocument: 策略文档
        :type PolicyDocument: str
        :param _Description: 策略描述
        :type Description: str
        """
        self._PolicyName = None
        self._PolicyDocument = None
        self._Description = None

    @property
    def PolicyName(self):
        """策略名称。长度为1~128个字符，可包含英文字母、数字和+=,.@-_。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyDocument(self):
        """策略文档
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        """策略描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._PolicyName = params.get("PolicyName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 新增策略ID
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """新增策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _PolicyDocument: 策略文本信息
        :type PolicyDocument: str
        :param _SetAsDefault: 是否设置为当前策略的版本
        :type SetAsDefault: bool
        """
        self._PolicyId = None
        self._PolicyDocument = None
        self._SetAsDefault = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyDocument(self):
        """策略文本信息
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def SetAsDefault(self):
        """是否设置为当前策略的版本
        :rtype: bool
        """
        return self._SetAsDefault

    @SetAsDefault.setter
    def SetAsDefault(self, SetAsDefault):
        self._SetAsDefault = SetAsDefault


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyDocument = params.get("PolicyDocument")
        self._SetAsDefault = params.get("SetAsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionId = None
        self._RequestId = None

    @property
    def VersionId(self):
        """策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

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
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称。长度为1~128个字符，可包含英文字母、数字和+=,.@-_。
        :type RoleName: str
        :param _PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param _Description: 角色描述
        :type Description: str
        :param _ConsoleLogin: 是否允许登录 1 为允许 0 为不允许
        :type ConsoleLogin: int
        :param _SessionDuration: 申请角色临时密钥的最长有效期限制(范围：0~43200)
        :type SessionDuration: int
        :param _Tags: 角色绑定标签
        :type Tags: list of RoleTags
        """
        self._RoleName = None
        self._PolicyDocument = None
        self._Description = None
        self._ConsoleLogin = None
        self._SessionDuration = None
        self._Tags = None

    @property
    def RoleName(self):
        """角色名称。长度为1~128个字符，可包含英文字母、数字和+=,.@-_。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyDocument(self):
        """策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        """角色描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConsoleLogin(self):
        """是否允许登录 1 为允许 0 为不允许
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def SessionDuration(self):
        """申请角色临时密钥的最长有效期限制(范围：0~43200)
        :rtype: int
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def Tags(self):
        """角色绑定标签
        :rtype: list of RoleTags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._SessionDuration = params.get("SessionDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        """角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

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
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        :param _Description: SAML身份提供商描述
        :type Description: str
        :param _SAMLMetadataDocument: SAML身份提供商Base64编码的元数据文档
        :type SAMLMetadataDocument: str
        """
        self._Name = None
        self._Description = None
        self._SAMLMetadataDocument = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """SAML身份提供商描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SAMLMetadataDocument(self):
        """SAML身份提供商Base64编码的元数据文档
        :rtype: str
        """
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderArn: SAML身份提供商资源描述符
        :type ProviderArn: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProviderArn = None
        self._RequestId = None

    @property
    def ProviderArn(self):
        """SAML身份提供商资源描述符
        :rtype: str
        """
        return self._ProviderArn

    @ProviderArn.setter
    def ProviderArn(self, ProviderArn):
        self._ProviderArn = ProviderArn

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
        self._ProviderArn = params.get("ProviderArn")
        self._RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QCSServiceName: 填写此角色的腾讯云服务载体，具体可查询文档（角色载体）字段
https://cloud.tencent.com/document/product/598/85165
        :type QCSServiceName: list of str
        :param _CustomSuffix: 自定义后缀，根据您提供的字符串，与服务提供的前缀组合在一起以形成完整的角色名称。
        :type CustomSuffix: str
        :param _Description: 角色说明。
        :type Description: str
        :param _Tags: 角色绑定标签。
        :type Tags: list of RoleTags
        """
        self._QCSServiceName = None
        self._CustomSuffix = None
        self._Description = None
        self._Tags = None

    @property
    def QCSServiceName(self):
        """填写此角色的腾讯云服务载体，具体可查询文档（角色载体）字段
https://cloud.tencent.com/document/product/598/85165
        :rtype: list of str
        """
        return self._QCSServiceName

    @QCSServiceName.setter
    def QCSServiceName(self, QCSServiceName):
        self._QCSServiceName = QCSServiceName

    @property
    def CustomSuffix(self):
        """自定义后缀，根据您提供的字符串，与服务提供的前缀组合在一起以形成完整的角色名称。
        :rtype: str
        """
        return self._CustomSuffix

    @CustomSuffix.setter
    def CustomSuffix(self, CustomSuffix):
        self._CustomSuffix = CustomSuffix

    @property
    def Description(self):
        """角色说明。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """角色绑定标签。
        :rtype: list of RoleTags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._QCSServiceName = params.get("QCSServiceName")
        self._CustomSuffix = params.get("CustomSuffix")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID
        :type RoleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        """角色ID
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

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
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class CreateUserOIDCConfigRequest(AbstractModel):
    """CreateUserOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL。OpenID Connect身份提供商标识。
对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :type IdentityUrl: str
        :param _ClientId: 客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :type ClientId: str
        :param _AuthorizationEndpoint: 授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :type AuthorizationEndpoint: str
        :param _ResponseType: 授权请求Response type，固定值id_token
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :type MappingFiled: str
        :param _IdentityKey: 签名公钥，需要base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :type IdentityKey: str
        :param _Scope: 授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :type Scope: list of str
        :param _Description: 描述信息。由用户自行定义。
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL。OpenID Connect身份提供商标识。
对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """授权请求Response type，固定值id_token
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """签名公钥，需要base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """描述信息。由用户自行定义。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserOIDCConfigResponse(AbstractModel):
    """CreateUserOIDCConfig返回参数结构体

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


class CreateUserSAMLConfigRequest(AbstractModel):
    """CreateUserSAMLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SAMLMetadataDocument: SAML元数据文档，需要base64 encode
        :type SAMLMetadataDocument: str
        :param _AuxiliaryDomain: 辅助域名
        :type AuxiliaryDomain: str
        """
        self._SAMLMetadataDocument = None
        self._AuxiliaryDomain = None

    @property
    def SAMLMetadataDocument(self):
        """SAML元数据文档，需要base64 encode
        :rtype: str
        """
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument

    @property
    def AuxiliaryDomain(self):
        """辅助域名
        :rtype: str
        """
        return self._AuxiliaryDomain

    @AuxiliaryDomain.setter
    def AuxiliaryDomain(self, AuxiliaryDomain):
        self._AuxiliaryDomain = AuxiliaryDomain


    def _deserialize(self, params):
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        self._AuxiliaryDomain = params.get("AuxiliaryDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSAMLConfigResponse(AbstractModel):
    """CreateUserSAMLConfig返回参数结构体

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


class DeleteAccessKeyRequest(AbstractModel):
    """DeleteAccessKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 指定需要删除的AccessKeyId
        :type AccessKeyId: str
        :param _TargetUin: 指定用户Uin，不填默认为当前用户删除访问密钥
        :type TargetUin: int
        """
        self._AccessKeyId = None
        self._TargetUin = None

    @property
    def AccessKeyId(self):
        """指定需要删除的AccessKeyId
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def TargetUin(self):
        """指定用户Uin，不填默认为当前用户删除访问密钥
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessKeyResponse(AbstractModel):
    """DeleteAccessKey返回参数结构体

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


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

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


class DeleteMessageReceiverRequest(AbstractModel):
    """DeleteMessageReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 消息接受者的名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """消息接受者的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMessageReceiverResponse(AbstractModel):
    """DeleteMessageReceiver返回参数结构体

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


class DeleteOIDCConfigRequest(AbstractModel):
    """DeleteOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: OIDC身份提供商名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """OIDC身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOIDCConfigResponse(AbstractModel):
    """DeleteOIDCConfig返回参数结构体

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


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 数组，数组成员是策略 id，支持批量删除策略
        :type PolicyId: list of int non-negative
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        """数组，数组成员是策略 id，支持批量删除策略
        :rtype: list of int non-negative
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy返回参数结构体

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


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _VersionId: 策略版本号
        :type VersionId: list of int non-negative
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        """策略版本号
        :rtype: list of int non-negative
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion返回参数结构体

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


class DeleteRolePermissionsBoundaryRequest(AbstractModel):
    """DeleteRolePermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID（与角色名至少填一个）
        :type RoleId: str
        :param _RoleName: 角色名（与角色ID至少填一个）
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        """角色ID（与角色名至少填一个）
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名（与角色ID至少填一个）
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolePermissionsBoundaryResponse(AbstractModel):
    """DeleteRolePermissionsBoundary返回参数结构体

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


class DeleteRoleRequest(AbstractModel):
    """DeleteRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param _RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        """角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    """DeleteRole返回参数结构体

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


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider返回参数结构体

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


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 要删除的服务相关角色的名称。
        :type RoleName: str
        """
        self._RoleName = None

    @property
    def RoleName(self):
        """要删除的服务相关角色的名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeletionTaskId: 删除任务ID，可用于检查删除服务相关角色状态。
        :type DeletionTaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeletionTaskId = None
        self._RequestId = None

    @property
    def DeletionTaskId(self):
        """删除任务ID，可用于检查删除服务相关角色状态。
        :rtype: str
        """
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId

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
        self._DeletionTaskId = params.get("DeletionTaskId")
        self._RequestId = params.get("RequestId")


class DeleteUserPermissionsBoundaryRequest(AbstractModel):
    """DeleteUserPermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 子账号Uin
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        """子账号Uin
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserPermissionsBoundaryResponse(AbstractModel):
    """DeleteUserPermissionsBoundary返回参数结构体

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
        :param _Name: 子用户用户名
        :type Name: str
        :param _Force: 是否强制删除该子用户，默认入参为0。0：若该用户存在未删除API密钥，则不删除用户；1：若该用户存在未删除API密钥，则先删除密钥后删除用户。删除密钥需要您拥有cam:DeleteApiKey权限，您将可以删除该用户下启用或禁用状态的所有密钥，无权限则删除密钥和用户失败
        :type Force: int
        """
        self._Name = None
        self._Force = None

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Force(self):
        """是否强制删除该子用户，默认入参为0。0：若该用户存在未删除API密钥，则不删除用户；1：若该用户存在未删除API密钥，则先删除密钥后删除用户。删除密钥需要您拥有cam:DeleteApiKey权限，您将可以删除该用户下启用或禁用状态的所有密钥，无权限则删除密钥和用户失败
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Force = params.get("Force")
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


class DescribeOIDCConfigRequest(AbstractModel):
    """DescribeOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOIDCConfigResponse(AbstractModel):
    """DescribeOIDCConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderType: 身份提供商类型 11角色身份提供商
        :type ProviderType: int
        :param _IdentityUrl: 身份提供商URL
        :type IdentityUrl: str
        :param _IdentityKey: 签名公钥
        :type IdentityKey: str
        :param _ClientId: 客户端id
        :type ClientId: list of str
        :param _Status: 状态：0:未设置，11:已开启，2:已禁用
        :type Status: int
        :param _Description: 描述
        :type Description: str
        :param _Name: 名称
        :type Name: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._Description = None
        self._Name = None
        self._RequestId = None

    @property
    def ProviderType(self):
        """身份提供商类型 11角色身份提供商
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        """身份提供商URL
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        """签名公钥
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        """客户端id
        :rtype: list of str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Status(self):
        """状态：0:未设置，11:已开启，2:已禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._ProviderType = params.get("ProviderType")
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Page: 页码，从1开始
        :type Page: int
        :param _Rp: 每页行数，不能大于200
        :type Rp: int
        :param _Tags: 标签筛选
        :type Tags: list of RoleTags
        """
        self._Page = None
        self._Rp = None
        self._Tags = None

    @property
    def Page(self):
        """页码，从1开始
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页行数，不能大于200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Tags(self):
        """标签筛选
        :rtype: list of RoleTags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 角色详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of RoleInfo
        :param _TotalNum: 角色总数
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def List(self):
        """角色详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RoleInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalNum(self):
        """角色总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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
                obj = RoleInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeSafeAuthFlagCollRequest(AbstractModel):
    """DescribeSafeAuthFlagColl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubUin: 子账号
        :type SubUin: int
        """
        self._SubUin = None

    @property
    def SubUin(self):
        """子账号
        :rtype: int
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeAuthFlagCollResponse(AbstractModel):
    """DescribeSafeAuthFlagColl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param _PromptTrust: 是否提示信任设备1 ：提示 0: 不提示
注意：此字段可能返回 null，表示取不到有效值。
        :type PromptTrust: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginFlag = None
        self._ActionFlag = None
        self._OffsiteFlag = None
        self._PromptTrust = None
        self._RequestId = None

    @property
    def LoginFlag(self):
        """登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        """敏感操作保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def OffsiteFlag(self):
        """异地登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        """
        return self._OffsiteFlag

    @OffsiteFlag.setter
    def OffsiteFlag(self, OffsiteFlag):
        self._OffsiteFlag = OffsiteFlag

    @property
    def PromptTrust(self):
        """是否提示信任设备1 ：提示 0: 不提示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PromptTrust

    @PromptTrust.setter
    def PromptTrust(self, PromptTrust):
        self._PromptTrust = PromptTrust

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
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionFlag()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionFlag()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self._OffsiteFlag = OffsiteFlag()
            self._OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self._PromptTrust = params.get("PromptTrust")
        self._RequestId = params.get("RequestId")


class DescribeSafeAuthFlagIntlRequest(AbstractModel):
    """DescribeSafeAuthFlagIntl请求参数结构体

    """


class DescribeSafeAuthFlagIntlResponse(AbstractModel):
    """DescribeSafeAuthFlagIntl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param _ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param _OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginFlag = None
        self._ActionFlag = None
        self._OffsiteFlag = None
        self._RequestId = None

    @property
    def LoginFlag(self):
        """登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        """敏感操作保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def OffsiteFlag(self):
        """异地登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        """
        return self._OffsiteFlag

    @OffsiteFlag.setter
    def OffsiteFlag(self, OffsiteFlag):
        self._OffsiteFlag = OffsiteFlag

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
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionFlagIntl()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionFlagIntl()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self._OffsiteFlag = OffsiteFlag()
            self._OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self._RequestId = params.get("RequestId")


class DescribeSafeAuthFlagRequest(AbstractModel):
    """DescribeSafeAuthFlag请求参数结构体

    """


class DescribeSafeAuthFlagResponse(AbstractModel):
    """DescribeSafeAuthFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param _PromptTrust: 是否提示信任设备：1: 提示  0: 不提示
        :type PromptTrust: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginFlag = None
        self._ActionFlag = None
        self._OffsiteFlag = None
        self._PromptTrust = None
        self._RequestId = None

    @property
    def LoginFlag(self):
        """登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        """敏感操作保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def OffsiteFlag(self):
        """异地登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        """
        return self._OffsiteFlag

    @OffsiteFlag.setter
    def OffsiteFlag(self, OffsiteFlag):
        self._OffsiteFlag = OffsiteFlag

    @property
    def PromptTrust(self):
        """是否提示信任设备：1: 提示  0: 不提示
        :rtype: int
        """
        return self._PromptTrust

    @PromptTrust.setter
    def PromptTrust(self, PromptTrust):
        self._PromptTrust = PromptTrust

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
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionFlag()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionFlag()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self._OffsiteFlag = OffsiteFlag()
            self._OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self._PromptTrust = params.get("PromptTrust")
        self._RequestId = params.get("RequestId")


class DescribeSubAccountsRequest(AbstractModel):
    """DescribeSubAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FilterSubAccountUin: 子用户UIN列表，最多支持50个UIN
        :type FilterSubAccountUin: list of int non-negative
        """
        self._FilterSubAccountUin = None

    @property
    def FilterSubAccountUin(self):
        """子用户UIN列表，最多支持50个UIN
        :rtype: list of int non-negative
        """
        return self._FilterSubAccountUin

    @FilterSubAccountUin.setter
    def FilterSubAccountUin(self, FilterSubAccountUin):
        self._FilterSubAccountUin = FilterSubAccountUin


    def _deserialize(self, params):
        self._FilterSubAccountUin = params.get("FilterSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAccountsResponse(AbstractModel):
    """DescribeSubAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAccounts: 子用户列表
        :type SubAccounts: list of SubAccountUser
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubAccounts = None
        self._RequestId = None

    @property
    def SubAccounts(self):
        """子用户列表
        :rtype: list of SubAccountUser
        """
        return self._SubAccounts

    @SubAccounts.setter
    def SubAccounts(self, SubAccounts):
        self._SubAccounts = SubAccounts

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
        if params.get("SubAccounts") is not None:
            self._SubAccounts = []
            for item in params.get("SubAccounts"):
                obj = SubAccountUser()
                obj._deserialize(item)
                self._SubAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserOIDCConfigRequest(AbstractModel):
    """DescribeUserOIDCConfig请求参数结构体

    """


class DescribeUserOIDCConfigResponse(AbstractModel):
    """DescribeUserOIDCConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderType: 身份提供商类型。 12：用户OIDC身份提供商
        :type ProviderType: int
        :param _IdentityUrl: 身份提供商URL
        :type IdentityUrl: str
        :param _IdentityKey: 签名公钥
        :type IdentityKey: str
        :param _ClientId: 客户端id
        :type ClientId: str
        :param _Status: 状态：0:未设置，11:已开启，2:已禁用
        :type Status: int
        :param _AuthorizationEndpoint: 授权请求Endpoint
        :type AuthorizationEndpoint: str
        :param _Scope: 授权请求Scope
        :type Scope: list of str
        :param _ResponseType: 授权请求Response type
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称
        :type MappingFiled: str
        :param _Description: 描述
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._AuthorizationEndpoint = None
        self._Scope = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Description = None
        self._RequestId = None

    @property
    def ProviderType(self):
        """身份提供商类型。 12：用户OIDC身份提供商
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        """身份提供商URL
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        """签名公钥
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        """客户端id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Status(self):
        """状态：0:未设置，11:已开启，2:已禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def Scope(self):
        """授权请求Scope
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ResponseType(self):
        """授权请求Response type
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
        self._ProviderType = params.get("ProviderType")
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Status = params.get("Status")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._Scope = params.get("Scope")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeUserSAMLConfigRequest(AbstractModel):
    """DescribeUserSAMLConfig请求参数结构体

    """


class DescribeUserSAMLConfigResponse(AbstractModel):
    """DescribeUserSAMLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SAMLMetadata: SAML元数据文档
        :type SAMLMetadata: str
        :param _Status: 状态：0:未设置，11:已开启，2:已禁用
        :type Status: int
        :param _AuxiliaryDomain: 辅助域名
        :type AuxiliaryDomain: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SAMLMetadata = None
        self._Status = None
        self._AuxiliaryDomain = None
        self._RequestId = None

    @property
    def SAMLMetadata(self):
        """SAML元数据文档
        :rtype: str
        """
        return self._SAMLMetadata

    @SAMLMetadata.setter
    def SAMLMetadata(self, SAMLMetadata):
        self._SAMLMetadata = SAMLMetadata

    @property
    def Status(self):
        """状态：0:未设置，11:已开启，2:已禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AuxiliaryDomain(self):
        """辅助域名
        :rtype: str
        """
        return self._AuxiliaryDomain

    @AuxiliaryDomain.setter
    def AuxiliaryDomain(self, AuxiliaryDomain):
        self._AuxiliaryDomain = AuxiliaryDomain

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
        self._SAMLMetadata = params.get("SAMLMetadata")
        self._Status = params.get("Status")
        self._AuxiliaryDomain = params.get("AuxiliaryDomain")
        self._RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略 id
        :type PolicyId: int
        :param _DetachGroupId: 用户组 id
        :type DetachGroupId: int
        """
        self._PolicyId = None
        self._DetachGroupId = None

    @property
    def PolicyId(self):
        """策略 id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachGroupId(self):
        """用户组 id
        :rtype: int
        """
        return self._DetachGroupId

    @DetachGroupId.setter
    def DetachGroupId(self, DetachGroupId):
        self._DetachGroupId = DetachGroupId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachGroupId = params.get("DetachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy返回参数结构体

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


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID，入参PolicyId与PolicyName二选一
        :type PolicyId: int
        :param _DetachRoleId: 角色ID，用于指定角色，入参 DetachRoleId 与 DetachRoleName 二选一
        :type DetachRoleId: str
        :param _DetachRoleName: 角色名称，用于指定角色，入参 DetachRoleId 与 DetachRoleName 二选一
        :type DetachRoleName: str
        :param _PolicyName: 策略名，入参PolicyId与PolicyName二选一
        :type PolicyName: str
        """
        self._PolicyId = None
        self._DetachRoleId = None
        self._DetachRoleName = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        """策略ID，入参PolicyId与PolicyName二选一
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachRoleId(self):
        """角色ID，用于指定角色，入参 DetachRoleId 与 DetachRoleName 二选一
        :rtype: str
        """
        return self._DetachRoleId

    @DetachRoleId.setter
    def DetachRoleId(self, DetachRoleId):
        self._DetachRoleId = DetachRoleId

    @property
    def DetachRoleName(self):
        """角色名称，用于指定角色，入参 DetachRoleId 与 DetachRoleName 二选一
        :rtype: str
        """
        return self._DetachRoleName

    @DetachRoleName.setter
    def DetachRoleName(self, DetachRoleName):
        self._DetachRoleName = DetachRoleName

    @property
    def PolicyName(self):
        """策略名，入参PolicyId与PolicyName二选一
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachRoleId = params.get("DetachRoleId")
        self._DetachRoleName = params.get("DetachRoleName")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy返回参数结构体

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


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略 id
        :type PolicyId: int
        :param _DetachUin: 子账号 uin
        :type DetachUin: int
        """
        self._PolicyId = None
        self._DetachUin = None

    @property
    def PolicyId(self):
        """策略 id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachUin(self):
        """子账号 uin
        :rtype: int
        """
        return self._DetachUin

    @DetachUin.setter
    def DetachUin(self, DetachUin):
        self._DetachUin = DetachUin


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachUin = params.get("DetachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回参数结构体

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


class DisableUserSSORequest(AbstractModel):
    """DisableUserSSO请求参数结构体

    """


class DisableUserSSOResponse(AbstractModel):
    """DisableUserSSO返回参数结构体

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


class GetAccountSummaryRequest(AbstractModel):
    """GetAccountSummary请求参数结构体

    """


class GetAccountSummaryResponse(AbstractModel):
    """GetAccountSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Policies: 策略数
        :type Policies: int
        :param _Roles: 角色数
        :type Roles: int
        :param _Idps: 身份提供商数
        :type Idps: int
        :param _User: 子账户数
        :type User: int
        :param _Group: 分组数
        :type Group: int
        :param _Member: 分组用户总数
        :type Member: int
        :param _IdentityProviders: 身份提供商数。
        :type IdentityProviders: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Policies = None
        self._Roles = None
        self._Idps = None
        self._User = None
        self._Group = None
        self._Member = None
        self._IdentityProviders = None
        self._RequestId = None

    @property
    def Policies(self):
        """策略数
        :rtype: int
        """
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies

    @property
    def Roles(self):
        """角色数
        :rtype: int
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def Idps(self):
        warnings.warn("parameter `Idps` is deprecated", DeprecationWarning) 

        """身份提供商数
        :rtype: int
        """
        return self._Idps

    @Idps.setter
    def Idps(self, Idps):
        warnings.warn("parameter `Idps` is deprecated", DeprecationWarning) 

        self._Idps = Idps

    @property
    def User(self):
        """子账户数
        :rtype: int
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Group(self):
        """分组数
        :rtype: int
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Member(self):
        """分组用户总数
        :rtype: int
        """
        return self._Member

    @Member.setter
    def Member(self, Member):
        self._Member = Member

    @property
    def IdentityProviders(self):
        """身份提供商数。
        :rtype: int
        """
        return self._IdentityProviders

    @IdentityProviders.setter
    def IdentityProviders(self, IdentityProviders):
        self._IdentityProviders = IdentityProviders

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
        self._Policies = params.get("Policies")
        self._Roles = params.get("Roles")
        self._Idps = params.get("Idps")
        self._User = params.get("User")
        self._Group = params.get("Group")
        self._Member = params.get("Member")
        self._IdentityProviders = params.get("IdentityProviders")
        self._RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MFAToken: 自定义多因子验证Token，针对用户自定义的安全校验方式而生成的，以供查询用户安全校验时使用。
        :type MFAToken: str
        """
        self._MFAToken = None

    @property
    def MFAToken(self):
        """自定义多因子验证Token，针对用户自定义的安全校验方式而生成的，以供查询用户安全校验时使用。
        :rtype: str
        """
        return self._MFAToken

    @MFAToken.setter
    def MFAToken(self, MFAToken):
        self._MFAToken = MFAToken


    def _deserialize(self, params):
        self._MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 自定义多因子验证Token对应的账号Id
        :type Uin: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        """自定义多因子验证Token对应的账号Id
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    """GetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        :param _GroupName: 用户组名称
        :type GroupName: str
        :param _GroupNum: 用户组成员数量
        :type GroupNum: int
        :param _Remark: 用户组描述
        :type Remark: str
        :param _CreateTime: 用户组创建时间
        :type CreateTime: str
        :param _UserInfo: 用户组成员信息
        :type UserInfo: list of GroupMemberInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupNum = None
        self._Remark = None
        self._CreateTime = None
        self._UserInfo = None
        self._RequestId = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """用户组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNum(self):
        """用户组成员数量
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def Remark(self):
        """用户组描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """用户组创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserInfo(self):
        """用户组成员信息
        :rtype: list of GroupMemberInfo
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

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
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupNum = params.get("GroupNum")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id。
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        """策略Id。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyResponse(AbstractModel):
    """GetPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _Description: 策略描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Type: 1 表示自定义策略，2 表示预设策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _AddTime: 策略创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _UpdateTime: 策略最近更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _PolicyDocument: 策略文档。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param _PresetAlias: 备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetAlias: str
        :param _IsServiceLinkedRolePolicy: 是否是服务相关策略，0代表不是服务相关策略，1代表是服务相关策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsServiceLinkedRolePolicy: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyName = None
        self._Description = None
        self._Type = None
        self._AddTime = None
        self._UpdateTime = None
        self._PolicyDocument = None
        self._PresetAlias = None
        self._IsServiceLinkedRolePolicy = None
        self._RequestId = None

    @property
    def PolicyName(self):
        """策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        """策略描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        """1 表示自定义策略，2 表示预设策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AddTime(self):
        """策略创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def UpdateTime(self):
        """策略最近更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PolicyDocument(self):
        """策略文档。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def PresetAlias(self):
        """备注。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PresetAlias

    @PresetAlias.setter
    def PresetAlias(self, PresetAlias):
        self._PresetAlias = PresetAlias

    @property
    def IsServiceLinkedRolePolicy(self):
        """是否是服务相关策略，0代表不是服务相关策略，1代表是服务相关策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsServiceLinkedRolePolicy

    @IsServiceLinkedRolePolicy.setter
    def IsServiceLinkedRolePolicy(self, IsServiceLinkedRolePolicy):
        self._IsServiceLinkedRolePolicy = IsServiceLinkedRolePolicy

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
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._AddTime = params.get("AddTime")
        self._UpdateTime = params.get("UpdateTime")
        self._PolicyDocument = params.get("PolicyDocument")
        self._PresetAlias = params.get("PresetAlias")
        self._IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self._RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _VersionId: 策略版本号，可由ListPolicyVersions获取
        :type VersionId: int
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        """策略版本号，可由ListPolicyVersions获取
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyVersion: 策略版本详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyVersion: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyVersion = None
        self._RequestId = None

    @property
    def PolicyVersion(self):
        """策略版本详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`
        """
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

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
        if params.get("PolicyVersion") is not None:
            self._PolicyVersion = PolicyVersionDetail()
            self._PolicyVersion._deserialize(params.get("PolicyVersion"))
        self._RequestId = params.get("RequestId")


class GetRolePermissionBoundaryRequest(AbstractModel):
    """GetRolePermissionBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID
        :type RoleId: str
        """
        self._RoleId = None

    @property
    def RoleId(self):
        """角色ID
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRolePermissionBoundaryResponse(AbstractModel):
    """GetRolePermissionBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _PolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _PolicyDocument: 策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param _PolicyType: 策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: int
        :param _CreateMode: 创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._PolicyDocument = None
        self._PolicyType = None
        self._CreateMode = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyDocument(self):
        """策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def PolicyType(self):
        """策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def CreateMode(self):
        """创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

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
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._PolicyType = params.get("PolicyType")
        self._CreateMode = params.get("CreateMode")
        self._RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色 ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param _RoleName: 角色名，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        """角色 ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleResponse(AbstractModel):
    """GetRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleInfo: 角色详情
        :type RoleInfo: :class:`tencentcloud.cam.v20190116.models.RoleInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleInfo = None
        self._RequestId = None

    @property
    def RoleInfo(self):
        """角色详情
        :rtype: :class:`tencentcloud.cam.v20190116.models.RoleInfo`
        """
        return self._RoleInfo

    @RoleInfo.setter
    def RoleInfo(self, RoleInfo):
        self._RoleInfo = RoleInfo

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
        if params.get("RoleInfo") is not None:
            self._RoleInfo = RoleInfo()
            self._RoleInfo._deserialize(params.get("RoleInfo"))
        self._RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        :param _Description: SAML身份提供商描述
        :type Description: str
        :param _CreateTime: SAML身份提供商创建时间
        :type CreateTime: str
        :param _ModifyTime: SAML身份提供商上次修改时间
        :type ModifyTime: str
        :param _SAMLMetadata: SAML身份提供商元数据文档
        :type SAMLMetadata: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._ModifyTime = None
        self._SAMLMetadata = None
        self._RequestId = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """SAML身份提供商描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """SAML身份提供商创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """SAML身份提供商上次修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def SAMLMetadata(self):
        """SAML身份提供商元数据文档
        :rtype: str
        """
        return self._SAMLMetadata

    @SAMLMetadata.setter
    def SAMLMetadata(self, SAMLMetadata):
        self._SAMLMetadata = SAMLMetadata

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
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._SAMLMetadata = params.get("SAMLMetadata")
        self._RequestId = params.get("RequestId")


class GetSecurityLastUsedRequest(AbstractModel):
    """GetSecurityLastUsed请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretIdList: 查询密钥ID列表。最多支持10个。
        :type SecretIdList: list of str
        """
        self._SecretIdList = None

    @property
    def SecretIdList(self):
        """查询密钥ID列表。最多支持10个。
        :rtype: list of str
        """
        return self._SecretIdList

    @SecretIdList.setter
    def SecretIdList(self, SecretIdList):
        self._SecretIdList = SecretIdList


    def _deserialize(self, params):
        self._SecretIdList = params.get("SecretIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecurityLastUsedResponse(AbstractModel):
    """GetSecurityLastUsed返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretIdLastUsedRows: 密钥ID最近访问列表
        :type SecretIdLastUsedRows: list of SecretIdLastUsed
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretIdLastUsedRows = None
        self._RequestId = None

    @property
    def SecretIdLastUsedRows(self):
        """密钥ID最近访问列表
        :rtype: list of SecretIdLastUsed
        """
        return self._SecretIdLastUsedRows

    @SecretIdLastUsedRows.setter
    def SecretIdLastUsedRows(self, SecretIdLastUsedRows):
        self._SecretIdLastUsedRows = SecretIdLastUsedRows

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
        if params.get("SecretIdLastUsedRows") is not None:
            self._SecretIdLastUsedRows = []
            for item in params.get("SecretIdLastUsedRows"):
                obj = SecretIdLastUsed()
                obj._deserialize(item)
                self._SecretIdLastUsedRows.append(obj)
        self._RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeletionTaskId: 删除任务ID
        :type DeletionTaskId: str
        """
        self._DeletionTaskId = None

    @property
    def DeletionTaskId(self):
        """删除任务ID
        :rtype: str
        """
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId


    def _deserialize(self, params):
        self._DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态：NOT_STARTED，IN_PROGRESS，SUCCEEDED，FAILED
        :type Status: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _ServiceType: 服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _ServiceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Reason = None
        self._ServiceType = None
        self._ServiceName = None
        self._RequestId = None

    @property
    def Status(self):
        """状态：NOT_STARTED，IN_PROGRESS，SUCCEEDED，FAILED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        """失败原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ServiceType(self):
        """服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceName(self):
        """服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

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
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._ServiceType = params.get("ServiceType")
        self._ServiceName = params.get("ServiceName")
        self._RequestId = params.get("RequestId")


class GetUserAppIdRequest(AbstractModel):
    """GetUserAppId请求参数结构体

    """


class GetUserAppIdResponse(AbstractModel):
    """GetUserAppId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 当前账号Uin
        :type Uin: str
        :param _OwnerUin: 当前账号OwnerUin
        :type OwnerUin: str
        :param _AppId: 当前账号AppId
        :type AppId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._OwnerUin = None
        self._AppId = None
        self._RequestId = None

    @property
    def Uin(self):
        """当前账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def OwnerUin(self):
        """当前账号OwnerUin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def AppId(self):
        """当前账号AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
        self._Uin = params.get("Uin")
        self._OwnerUin = params.get("OwnerUin")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class GetUserPermissionBoundaryRequest(AbstractModel):
    """GetUserPermissionBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 子账号Uin
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        """子账号Uin
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserPermissionBoundaryResponse(AbstractModel):
    """GetUserPermissionBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _PolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _PolicyDocument: 策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param _PolicyType: 策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: int
        :param _CreateMode: 创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._PolicyDocument = None
        self._PolicyType = None
        self._CreateMode = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyDocument(self):
        """策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def PolicyType(self):
        """策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def CreateMode(self):
        """创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

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
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._PolicyType = params.get("PolicyType")
        self._CreateMode = params.get("CreateMode")
        self._RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 子用户用户名
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    """GetUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 子用户用户 UIN
        :type Uin: int
        :param _Name: 子用户用户名
        :type Name: str
        :param _Uid: 子用户 UID
        :type Uid: int
        :param _Remark: 子用户备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _ConsoleLogin: 子用户能否登录控制台 0-无法登录控制台，1-可以登录控制台
        :type ConsoleLogin: int
        :param _PhoneNum: 手机号
        :type PhoneNum: str
        :param _CountryCode: 区号
        :type CountryCode: str
        :param _Email: 邮箱
        :type Email: str
        :param _RecentlyLoginIP: 最近一次登录ip
注意：此字段可能返回 null，表示取不到有效值。
        :type RecentlyLoginIP: str
        :param _RecentlyLoginTime: 最近一次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RecentlyLoginTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._ConsoleLogin = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None
        self._RecentlyLoginIP = None
        self._RecentlyLoginTime = None
        self._RequestId = None

    @property
    def Uin(self):
        """子用户用户 UIN
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        """子用户 UID
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        """子用户备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        """子用户能否登录控制台 0-无法登录控制台，1-可以登录控制台
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def PhoneNum(self):
        """手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """区号
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def RecentlyLoginIP(self):
        """最近一次登录ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecentlyLoginIP

    @RecentlyLoginIP.setter
    def RecentlyLoginIP(self, RecentlyLoginIP):
        self._RecentlyLoginIP = RecentlyLoginIP

    @property
    def RecentlyLoginTime(self):
        """最近一次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecentlyLoginTime

    @RecentlyLoginTime.setter
    def RecentlyLoginTime(self, RecentlyLoginTime):
        self._RecentlyLoginTime = RecentlyLoginTime

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
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        self._RecentlyLoginIP = params.get("RecentlyLoginIP")
        self._RecentlyLoginTime = params.get("RecentlyLoginTime")
        self._RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """子用户和用户组关联信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        :param _Uid: 子用户 UID
        :type Uid: int
        :param _Uin: 子用户 Uin，Uid和Uin至少有一个必填
        :type Uin: int
        """
        self._GroupId = None
        self._Uid = None
        self._Uin = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Uid(self):
        """子用户 UID
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Uin(self):
        """子用户 Uin，Uid和Uin至少有一个必填
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Uid = params.get("Uid")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """用户组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID。
        :type GroupId: int
        :param _GroupName: 用户组名称。
        :type GroupName: str
        :param _CreateTime: 用户组创建时间。
        :type CreateTime: str
        :param _Remark: 用户组描述。
        :type Remark: str
        """
        self._GroupId = None
        self._GroupName = None
        self._CreateTime = None
        self._Remark = None

    @property
    def GroupId(self):
        """用户组 ID。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """用户组名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def CreateTime(self):
        """用户组创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        """用户组描述。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMemberInfo(AbstractModel):
    """用户组用户信息

    """

    def __init__(self):
        r"""
        :param _Uid: 子用户 Uid。
        :type Uid: int
        :param _Uin: 子用户 Uin。
        :type Uin: int
        :param _Name: 子用户名称。
        :type Name: str
        :param _PhoneNum: 手机号。
        :type PhoneNum: str
        :param _CountryCode: 手机区域代码。
        :type CountryCode: str
        :param _PhoneFlag: 是否已验证手机。0-未验证  1-验证
        :type PhoneFlag: int
        :param _Email: 邮箱地址。
        :type Email: str
        :param _EmailFlag: 是否已验证邮箱。0-未验证  1-验证
        :type EmailFlag: int
        :param _UserType: 用户类型。1-全局协作者 2-项目协作者 3-消息接收者
        :type UserType: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _IsReceiverOwner: 是否为主消息接收人。0-否 1-是
        :type IsReceiverOwner: int
        :param _Remark: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Uid = None
        self._Uin = None
        self._Name = None
        self._PhoneNum = None
        self._CountryCode = None
        self._PhoneFlag = None
        self._Email = None
        self._EmailFlag = None
        self._UserType = None
        self._CreateTime = None
        self._IsReceiverOwner = None
        self._Remark = None

    @property
    def Uid(self):
        """子用户 Uid。
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Uin(self):
        """子用户 Uin。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PhoneNum(self):
        """手机号。
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """手机区域代码。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneFlag(self):
        """是否已验证手机。0-未验证  1-验证
        :rtype: int
        """
        return self._PhoneFlag

    @PhoneFlag.setter
    def PhoneFlag(self, PhoneFlag):
        self._PhoneFlag = PhoneFlag

    @property
    def Email(self):
        """邮箱地址。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def EmailFlag(self):
        """是否已验证邮箱。0-未验证  1-验证
        :rtype: int
        """
        return self._EmailFlag

    @EmailFlag.setter
    def EmailFlag(self, EmailFlag):
        self._EmailFlag = EmailFlag

    @property
    def UserType(self):
        """用户类型。1-全局协作者 2-项目协作者 3-消息接收者
        :rtype: int
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsReceiverOwner(self):
        """是否为主消息接收人。0-否 1-是
        :rtype: int
        """
        return self._IsReceiverOwner

    @IsReceiverOwner.setter
    def IsReceiverOwner(self, IsReceiverOwner):
        self._IsReceiverOwner = IsReceiverOwner

    @property
    def Remark(self):
        """昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._PhoneFlag = params.get("PhoneFlag")
        self._Email = params.get("Email")
        self._EmailFlag = params.get("EmailFlag")
        self._UserType = params.get("UserType")
        self._CreateTime = params.get("CreateTime")
        self._IsReceiverOwner = params.get("IsReceiverOwner")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 指定用户Uin，不填默认列出当前用户访问密钥
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        """指定用户Uin，不填默认列出当前用户访问密钥
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysResponse(AbstractModel):
    """ListAccessKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeys: 访问密钥列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeys: list of AccessKey
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessKeys = None
        self._RequestId = None

    @property
    def AccessKeys(self):
        """访问密钥列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccessKey
        """
        return self._AccessKeys

    @AccessKeys.setter
    def AccessKeys(self, AccessKeys):
        self._AccessKeys = AccessKeys

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
        if params.get("AccessKeys") is not None:
            self._AccessKeys = []
            for item in params.get("AccessKeys"):
                obj = AccessKey()
                obj._deserialize(item)
                self._AccessKeys.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 用户组ID
        :type TargetGroupId: int
        :param _Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param _Rp: 每页大小，默认值是 20
        :type Rp: int
        :param _Keyword: 搜索关键字
        :type Keyword: str
        """
        self._TargetGroupId = None
        self._Page = None
        self._Rp = None
        self._Keyword = None

    @property
    def TargetGroupId(self):
        """用户组ID
        :rtype: int
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Page(self):
        """页码，默认值是 1，从 1 开始
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页大小，默认值是 20
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Keyword(self):
        """搜索关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 策略总数。取值范围大于等于0。
        :type TotalNum: int
        :param _List: 策略列表
        :type List: list of AttachPolicyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """策略总数。取值范围大于等于0。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        """策略列表
        :rtype: list of AttachPolicyInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Page: 页码，从 1 开始
        :type Page: int
        :param _Rp: 每页行数，不能大于200
        :type Rp: int
        :param _RoleId: 角色 ID。用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param _RoleName: 角色名。用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        :param _PolicyType: 按策略类型过滤，User表示仅查询自定义策略，QCS表示仅查询预设策略
        :type PolicyType: str
        :param _Keyword: 搜索关键字
        :type Keyword: str
        """
        self._Page = None
        self._Rp = None
        self._RoleId = None
        self._RoleName = None
        self._PolicyType = None
        self._Keyword = None

    @property
    def Page(self):
        """页码，从 1 开始
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页行数，不能大于200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def RoleId(self):
        """角色 ID。用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名。用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyType(self):
        """按策略类型过滤，User表示仅查询自定义策略，QCS表示仅查询预设策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Keyword(self):
        """搜索关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._PolicyType = params.get("PolicyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 角色关联的策略列表
        :type List: list of AttachedPolicyOfRole
        :param _TotalNum: 角色关联的策略总数
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def List(self):
        """角色关联的策略列表
        :rtype: list of AttachedPolicyOfRole
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalNum(self):
        """角色关联的策略总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListAttachedUserAllPoliciesRequest(AbstractModel):
    """ListAttachedUserAllPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 目标用户Uin
        :type TargetUin: int
        :param _Rp: 每页数量，必须大于 0 且小于等于 200。
        :type Rp: int
        :param _Page: 页码，从 1开始，不能大于 200。
        :type Page: int
        :param _AttachType: 关联类型。0:返回直接关联和随组关联策略，1:只返回直接关联策略，2:只返回随组关联策略。
        :type AttachType: int
        :param _StrategyType: 策略类型。1表示自定义策略，2表示预设策略。
        :type StrategyType: int
        :param _Keyword: 搜索关键字
        :type Keyword: str
        """
        self._TargetUin = None
        self._Rp = None
        self._Page = None
        self._AttachType = None
        self._StrategyType = None
        self._Keyword = None

    @property
    def TargetUin(self):
        """目标用户Uin
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def Rp(self):
        """每页数量，必须大于 0 且小于等于 200。
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        """页码，从 1开始，不能大于 200。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def AttachType(self):
        """关联类型。0:返回直接关联和随组关联策略，1:只返回直接关联策略，2:只返回随组关联策略。
        :rtype: int
        """
        return self._AttachType

    @AttachType.setter
    def AttachType(self, AttachType):
        self._AttachType = AttachType

    @property
    def StrategyType(self):
        """策略类型。1表示自定义策略，2表示预设策略。
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def Keyword(self):
        """搜索关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._AttachType = params.get("AttachType")
        self._StrategyType = params.get("StrategyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserAllPoliciesResponse(AbstractModel):
    """ListAttachedUserAllPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyList: 策略列表数据。
        :type PolicyList: list of AttachedUserPolicy
        :param _TotalNum: 策略总数。
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyList = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def PolicyList(self):
        """策略列表数据。
        :rtype: list of AttachedUserPolicy
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList

    @property
    def TotalNum(self):
        """策略总数。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = AttachedUserPolicy()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 子账号 uin
        :type TargetUin: int
        :param _Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param _Rp: 每页大小，默认值是 20
        :type Rp: int
        """
        self._TargetUin = None
        self._Page = None
        self._Rp = None

    @property
    def TargetUin(self):
        """子账号 uin
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def Page(self):
        """页码，默认值是 1，从 1 开始
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页大小，默认值是 20
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 策略总数
        :type TotalNum: int
        :param _List: 策略列表
        :type List: list of AttachPolicyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """策略总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        """策略列表
        :rtype: list of AttachPolicyInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页的条数，默认是20条。
        :type Limit: int
        :param _Offset: 分页的起始值，默认从0开始。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """分页的条数，默认是20条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页的起始值，默认从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 总数
        :type TotalNum: int
        :param _Data: 协作者信息
        :type Data: list of SubAccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def Data(self):
        """协作者信息
        :rtype: list of SubAccountInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略 id
        :type PolicyId: int
        :param _Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param _Rp: 每页大小，默认值是 20
        :type Rp: int
        :param _EntityFilter: 可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示获取所有实体类型，'User' 表示只获取子账号，'Group' 表示只获取用户组，'Role' 表示只获取角色，默认取 'All'
        :type EntityFilter: str
        """
        self._PolicyId = None
        self._Page = None
        self._Rp = None
        self._EntityFilter = None

    @property
    def PolicyId(self):
        """策略 id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Page(self):
        """页码，默认值是 1，从 1 开始
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页大小，默认值是 20
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def EntityFilter(self):
        """可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示获取所有实体类型，'User' 表示只获取子账号，'Group' 表示只获取用户组，'Role' 表示只获取角色，默认取 'All'
        :rtype: str
        """
        return self._EntityFilter

    @EntityFilter.setter
    def EntityFilter(self, EntityFilter):
        self._EntityFilter = EntityFilter


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._EntityFilter = params.get("EntityFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 实体总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param _List: 实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of AttachEntityOfPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """实体总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        """实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttachEntityOfPolicy
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListGrantServiceAccessActionNode(AbstractModel):
    """ListGrantServiceAccessAction节点

    """

    def __init__(self):
        r"""
        :param _Name: 接口名
        :type Name: str
        :param _Description: 接口描述
        :type Description: str
        """
        self._Name = None
        self._Description = None

    @property
    def Name(self):
        """接口名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """接口描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessNode(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的List节点

    """

    def __init__(self):
        r"""
        :param _Service: 服务
        :type Service: :class:`tencentcloud.cam.v20190116.models.ListGrantServiceAccessService`
        :param _Action: 接口信息
        :type Action: list of ListGrantServiceAccessActionNode
        :param _Policy: 授权的策略
        :type Policy: list of ListGrantServiceAccessPolicy
        """
        self._Service = None
        self._Action = None
        self._Policy = None

    @property
    def Service(self):
        """服务
        :rtype: :class:`tencentcloud.cam.v20190116.models.ListGrantServiceAccessService`
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Action(self):
        """接口信息
        :rtype: list of ListGrantServiceAccessActionNode
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Policy(self):
        """授权的策略
        :rtype: list of ListGrantServiceAccessPolicy
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = ListGrantServiceAccessService()
            self._Service._deserialize(params.get("Service"))
        if params.get("Action") is not None:
            self._Action = []
            for item in params.get("Action"):
                obj = ListGrantServiceAccessActionNode()
                obj._deserialize(item)
                self._Action.append(obj)
        if params.get("Policy") is not None:
            self._Policy = []
            for item in params.get("Policy"):
                obj = ListGrantServiceAccessPolicy()
                obj._deserialize(item)
                self._Policy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessPolicy(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的Policy节点

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _PolicyName: 策略名
        :type PolicyName: str
        :param _PolicyType: 策略类型: Custom自定义策略，Presetting预设策略
        :type PolicyType: str
        :param _PolicyDescription: 策略描述
        :type PolicyDescription: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._PolicyType = None
        self._PolicyDescription = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyType(self):
        """策略类型: Custom自定义策略，Presetting预设策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyDescription(self):
        """策略描述
        :rtype: str
        """
        return self._PolicyDescription

    @PolicyDescription.setter
    def PolicyDescription(self, PolicyDescription):
        self._PolicyDescription = PolicyDescription


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyType = params.get("PolicyType")
        self._PolicyDescription = params.get("PolicyDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessService(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的Service节点

    """

    def __init__(self):
        r"""
        :param _ServiceType: 服务
        :type ServiceType: str
        :param _ServiceName: 服务名
        :type ServiceName: str
        """
        self._ServiceType = None
        self._ServiceName = None

    @property
    def ServiceType(self):
        """服务
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceName(self):
        """服务名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uid: 子用户 UID，入参Uid和SubUin二选一
        :type Uid: int
        :param _Rp: 每页数量。默认为20。
        :type Rp: int
        :param _Page: 页码。默认为1。
        :type Page: int
        :param _SubUin: 子账号UIN，入参Uid和SubUin二选一
        :type SubUin: int
        """
        self._Uid = None
        self._Rp = None
        self._Page = None
        self._SubUin = None

    @property
    def Uid(self):
        """子用户 UID，入参Uid和SubUin二选一
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Rp(self):
        """每页数量。默认为20。
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        """页码。默认为1。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def SubUin(self):
        """子账号UIN，入参Uid和SubUin二选一
        :rtype: int
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 子用户加入的用户组总数
        :type TotalNum: int
        :param _GroupInfo: 用户组信息
        :type GroupInfo: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._GroupInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """子用户加入的用户组总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def GroupInfo(self):
        """用户组信息
        :rtype: list of GroupInfo
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

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
        self._TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Page: 页码。默认为1。
        :type Page: int
        :param _Rp: 每页数量。默认为20。
        :type Rp: int
        :param _Keyword: 按用户组名称匹配。
        :type Keyword: str
        """
        self._Page = None
        self._Rp = None
        self._Keyword = None

    @property
    def Page(self):
        """页码。默认为1。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页数量。默认为20。
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Keyword(self):
        """按用户组名称匹配。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    """ListGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 用户组总数。
        :type TotalNum: int
        :param _GroupInfo: 用户组数组信息。
        :type GroupInfo: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._GroupInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """用户组总数。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def GroupInfo(self):
        """用户组数组信息。
        :rtype: list of GroupInfo
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

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
        self._TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListPoliciesGrantingServiceAccessRequest(AbstractModel):
    """ListPoliciesGrantingServiceAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 子账号uin，与RoleId、GroupId三选一必传
        :type TargetUin: int
        :param _RoleId: 角色ID，与TargetUin、GroupId三选一必传
        :type RoleId: int
        :param _GroupId: 用户组ID，与TargetUin、RoleId三选一必传
        :type GroupId: int
        :param _ServiceType: 服务名，查看服务授权接口详情时需传该字段
        :type ServiceType: str
        """
        self._TargetUin = None
        self._RoleId = None
        self._GroupId = None
        self._ServiceType = None

    @property
    def TargetUin(self):
        """子账号uin，与RoleId、GroupId三选一必传
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def RoleId(self):
        """角色ID，与TargetUin、GroupId三选一必传
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def GroupId(self):
        """用户组ID，与TargetUin、RoleId三选一必传
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ServiceType(self):
        """服务名，查看服务授权接口详情时需传该字段
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._RoleId = params.get("RoleId")
        self._GroupId = params.get("GroupId")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesGrantingServiceAccessResponse(AbstractModel):
    """ListPoliciesGrantingServiceAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表
        :type List: list of ListGrantServiceAccessNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """列表
        :rtype: list of ListGrantServiceAccessNode
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
                obj = ListGrantServiceAccessNode()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rp: 每页数量，默认值是 20，必须大于 0 且小于或等于 200
        :type Rp: int
        :param _Page: 页码，默认值是 1，从 1开始，不能大于 200
        :type Page: int
        :param _Scope: 可取值 'All'、'QCS' 和 'Local'，'All' 获取所有策略，'QCS' 只获取预设策略，'Local' 只获取自定义策略，默认取 'All'
        :type Scope: str
        :param _Keyword: 按策略名匹配
        :type Keyword: str
        """
        self._Rp = None
        self._Page = None
        self._Scope = None
        self._Keyword = None

    @property
    def Rp(self):
        """每页数量，默认值是 20，必须大于 0 且小于或等于 200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        """页码，默认值是 1，从 1开始，不能大于 200
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Scope(self):
        """可取值 'All'、'QCS' 和 'Local'，'All' 获取所有策略，'QCS' 只获取预设策略，'Local' 只获取自定义策略，默认取 'All'
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Keyword(self):
        """按策略名匹配
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._Scope = params.get("Scope")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    """ListPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 策略总数
        :type TotalNum: int
        :param _List: 策略数组，数组每个成员包括 policyId、policyName、addTime、type、description、 createMode 字段。其中： 
policyId：策略 id 
policyName：策略名
addTime：策略创建时间
type：1 表示自定义策略，2 表示预设策略 
description：策略描述 
createMode：1 表示按业务权限创建的策略，其他值表示可以查看策略语法和通过策略语法更新策略
Attachments: 关联的用户数
ServiceType: 策略关联的产品
IsAttached: 当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
        :type List: list of StrategyInfo
        :param _ServiceTypeList: 保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTypeList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._ServiceTypeList = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """策略总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        """策略数组，数组每个成员包括 policyId、policyName、addTime、type、description、 createMode 字段。其中： 
policyId：策略 id 
policyName：策略名
addTime：策略创建时间
type：1 表示自定义策略，2 表示预设策略 
description：策略描述 
createMode：1 表示按业务权限创建的策略，其他值表示可以查看策略语法和通过策略语法更新策略
Attachments: 关联的用户数
ServiceType: 策略关联的产品
IsAttached: 当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
        :rtype: list of StrategyInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def ServiceTypeList(self):
        """保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ServiceTypeList

    @ServiceTypeList.setter
    def ServiceTypeList(self, ServiceTypeList):
        self._ServiceTypeList = ServiceTypeList

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._ServiceTypeList = params.get("ServiceTypeList")
        self._RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Versions: 策略版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of PolicyVersionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Versions = None
        self._RequestId = None

    @property
    def Versions(self):
        """策略版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PolicyVersionItem
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

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
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class ListReceiverRequest(AbstractModel):
    """ListReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页限制数目
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReceiverResponse(AbstractModel):
    """ListReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _Receivers: 联系人列表
        :type Receivers: list of Receiver
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Receivers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Receivers(self):
        """联系人列表
        :rtype: list of Receiver
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Receivers") is not None:
            self._Receivers = []
            for item in params.get("Receivers"):
                obj = Receiver()
                obj._deserialize(item)
                self._Receivers.append(obj)
        self._RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders请求参数结构体

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: SAML身份提供商总数
        :type TotalCount: int
        :param _SAMLProviderSet: SAML身份提供商列表
        :type SAMLProviderSet: list of SAMLProviderInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SAMLProviderSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """SAML身份提供商总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SAMLProviderSet(self):
        """SAML身份提供商列表
        :rtype: list of SAMLProviderInfo
        """
        return self._SAMLProviderSet

    @SAMLProviderSet.setter
    def SAMLProviderSet(self, SAMLProviderSet):
        self._SAMLProviderSet = SAMLProviderSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self._SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self._SAMLProviderSet.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID。
        :type GroupId: int
        :param _Page: 页码。默认为1。
        :type Page: int
        :param _Rp: 每页数量。默认为20。
        :type Rp: int
        """
        self._GroupId = None
        self._Page = None
        self._Rp = None

    @property
    def GroupId(self):
        """用户组 ID。
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Page(self):
        """页码。默认为1。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        """每页数量。默认为20。
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 用户组关联的用户总数。
        :type TotalNum: int
        :param _UserInfo: 子用户信息。
        :type UserInfo: list of GroupMemberInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._UserInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """用户组关联的用户总数。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def UserInfo(self):
        """子用户信息。
        :rtype: list of GroupMemberInfo
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

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
        self._TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers请求参数结构体

    """


class ListUsersResponse(AbstractModel):
    """ListUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 子用户信息
        :type Data: list of SubAccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """子用户信息
        :rtype: list of SubAccountInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListWeChatWorkSubAccountsRequest(AbstractModel):
    """ListWeChatWorkSubAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWeChatWorkSubAccountsResponse(AbstractModel):
    """ListWeChatWorkSubAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 企业微信子用户列表。
        :type Data: list of WeChatWorkSubAccount
        :param _TotalCount: 总数目。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """企业微信子用户列表。
        :rtype: list of WeChatWorkSubAccount
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """总数目。
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WeChatWorkSubAccount()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class LoginActionFlag(AbstractModel):
    """登录和敏感操作flag（校验方式是单选）

    """

    def __init__(self):
        r"""
        :param _Phone: 0: 非安全手机校验 1: 安全手机校验。
        :type Phone: int
        :param _Token: 0: 非硬token校验 1: 硬token校验。
        :type Token: int
        :param _Stoken: 0: 非软token校验 1: 软token校验
        :type Stoken: int
        :param _Wechat: 0: 非微信校验 1: 微信校验
        :type Wechat: int
        :param _Custom: 0: 非自定义校验 1: 自定义校验
        :type Custom: int
        :param _Mail: 0: 非邮箱校验 1: 邮箱校验
        :type Mail: int
        :param _U2FToken: 0: 非u2f硬件token 1: u2f硬件token
注意：此字段可能返回 null，表示取不到有效值。
        :type U2FToken: int
        """
        self._Phone = None
        self._Token = None
        self._Stoken = None
        self._Wechat = None
        self._Custom = None
        self._Mail = None
        self._U2FToken = None

    @property
    def Phone(self):
        """0: 非安全手机校验 1: 安全手机校验。
        :rtype: int
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Token(self):
        """0: 非硬token校验 1: 硬token校验。
        :rtype: int
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Stoken(self):
        """0: 非软token校验 1: 软token校验
        :rtype: int
        """
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        """0: 非微信校验 1: 微信校验
        :rtype: int
        """
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def Custom(self):
        """0: 非自定义校验 1: 自定义校验
        :rtype: int
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Mail(self):
        """0: 非邮箱校验 1: 邮箱校验
        :rtype: int
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def U2FToken(self):
        """0: 非u2f硬件token 1: u2f硬件token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._U2FToken

    @U2FToken.setter
    def U2FToken(self, U2FToken):
        self._U2FToken = U2FToken


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Token = params.get("Token")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        self._Custom = params.get("Custom")
        self._Mail = params.get("Mail")
        self._U2FToken = params.get("U2FToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionFlagIntl(AbstractModel):
    """登录和敏感操作flag

    """

    def __init__(self):
        r"""
        :param _Phone: 手机
        :type Phone: int
        :param _Token: 硬token
        :type Token: int
        :param _Stoken: 软token
        :type Stoken: int
        :param _Wechat: 微信
        :type Wechat: int
        :param _Custom: 自定义
        :type Custom: int
        :param _Mail: 邮件
        :type Mail: int
        :param _U2FToken: u2f硬件token
注意：此字段可能返回 null，表示取不到有效值。
        :type U2FToken: int
        """
        self._Phone = None
        self._Token = None
        self._Stoken = None
        self._Wechat = None
        self._Custom = None
        self._Mail = None
        self._U2FToken = None

    @property
    def Phone(self):
        """手机
        :rtype: int
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Token(self):
        """硬token
        :rtype: int
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Stoken(self):
        """软token
        :rtype: int
        """
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        """微信
        :rtype: int
        """
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def Custom(self):
        """自定义
        :rtype: int
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Mail(self):
        """邮件
        :rtype: int
        """
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def U2FToken(self):
        """u2f硬件token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._U2FToken

    @U2FToken.setter
    def U2FToken(self, U2FToken):
        self._U2FToken = U2FToken


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Token = params.get("Token")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        self._Custom = params.get("Custom")
        self._Mail = params.get("Mail")
        self._U2FToken = params.get("U2FToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionMfaFlag(AbstractModel):
    """登录和敏感操作flag

    """

    def __init__(self):
        r"""
        :param _Phone: 是否设置手机号为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :type Phone: int
        :param _Stoken: 是否设置软token为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :type Stoken: int
        :param _Wechat: 是否设置微信为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :type Wechat: int
        """
        self._Phone = None
        self._Stoken = None
        self._Wechat = None

    @property
    def Phone(self):
        """是否设置手机号为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :rtype: int
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Stoken(self):
        """是否设置软token为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :rtype: int
        """
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        """是否设置微信为登录和敏感操作安全校验方式， 1: 设置，0: 不设置
        :rtype: int
        """
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsiteFlag(AbstractModel):
    """异地登录设置

    """

    def __init__(self):
        r"""
        :param _VerifyFlag: 验证标识
        :type VerifyFlag: int
        :param _NotifyPhone: 手机通知
        :type NotifyPhone: int
        :param _NotifyEmail: 邮箱通知
        :type NotifyEmail: int
        :param _NotifyWechat: 微信通知
        :type NotifyWechat: int
        :param _Tips: 提示
        :type Tips: int
        """
        self._VerifyFlag = None
        self._NotifyPhone = None
        self._NotifyEmail = None
        self._NotifyWechat = None
        self._Tips = None

    @property
    def VerifyFlag(self):
        """验证标识
        :rtype: int
        """
        return self._VerifyFlag

    @VerifyFlag.setter
    def VerifyFlag(self, VerifyFlag):
        self._VerifyFlag = VerifyFlag

    @property
    def NotifyPhone(self):
        """手机通知
        :rtype: int
        """
        return self._NotifyPhone

    @NotifyPhone.setter
    def NotifyPhone(self, NotifyPhone):
        self._NotifyPhone = NotifyPhone

    @property
    def NotifyEmail(self):
        """邮箱通知
        :rtype: int
        """
        return self._NotifyEmail

    @NotifyEmail.setter
    def NotifyEmail(self, NotifyEmail):
        self._NotifyEmail = NotifyEmail

    @property
    def NotifyWechat(self):
        """微信通知
        :rtype: int
        """
        return self._NotifyWechat

    @NotifyWechat.setter
    def NotifyWechat(self, NotifyWechat):
        self._NotifyWechat = NotifyWechat

    @property
    def Tips(self):
        """提示
        :rtype: int
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._VerifyFlag = params.get("VerifyFlag")
        self._NotifyPhone = params.get("NotifyPhone")
        self._NotifyEmail = params.get("NotifyEmail")
        self._NotifyWechat = params.get("NotifyWechat")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionDetail(AbstractModel):
    """策略版本详情

    """

    def __init__(self):
        r"""
        :param _VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _CreateDate: 策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        :param _Document: 策略语法文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Document: str
        """
        self._VersionId = None
        self._CreateDate = None
        self._IsDefaultVersion = None
        self._Document = None

    @property
    def VersionId(self):
        """策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateDate(self):
        """策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def IsDefaultVersion(self):
        """是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion

    @property
    def Document(self):
        """策略语法文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateDate = params.get("CreateDate")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        self._Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionItem(AbstractModel):
    """策略版本列表元素结构

    """

    def __init__(self):
        r"""
        :param _VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _CreateDate: 策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        """
        self._VersionId = None
        self._CreateDate = None
        self._IsDefaultVersion = None

    @property
    def VersionId(self):
        """策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateDate(self):
        """策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def IsDefaultVersion(self):
        """是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateDate = params.get("CreateDate")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryRequest(AbstractModel):
    """PutRolePermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _RoleId: 角色ID（与角色名至少填一个）
        :type RoleId: str
        :param _RoleName: 角色名（与角色ID至少填一个）
        :type RoleName: str
        """
        self._PolicyId = None
        self._RoleId = None
        self._RoleName = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RoleId(self):
        """角色ID（与角色名至少填一个）
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名（与角色ID至少填一个）
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryResponse(AbstractModel):
    """PutRolePermissionsBoundary返回参数结构体

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


class PutUserPermissionsBoundaryRequest(AbstractModel):
    """PutUserPermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 子账号Uin
        :type TargetUin: int
        :param _PolicyId: 策略ID
        :type PolicyId: int
        """
        self._TargetUin = None
        self._PolicyId = None

    @property
    def TargetUin(self):
        """子账号Uin
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutUserPermissionsBoundaryResponse(AbstractModel):
    """PutUserPermissionsBoundary返回参数结构体

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


class Receiver(AbstractModel):
    """消息接收人信息

    """

    def __init__(self):
        r"""
        :param _Uid: id
        :type Uid: int
        :param _Name: 名字
        :type Name: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _PhoneNumber: 手机号码
        :type PhoneNumber: str
        :param _PhoneFlag: 手机号码是否验证
        :type PhoneFlag: int
        :param _Email: 邮箱
        :type Email: str
        :param _EmailFlag: 邮箱是否验证
        :type EmailFlag: int
        :param _IsReceiverOwner: 是否主联系人
        :type IsReceiverOwner: int
        :param _WechatFlag: 是否允许微信接收通知
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatFlag: int
        :param _Uin: 账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        """
        self._Uid = None
        self._Name = None
        self._Remark = None
        self._PhoneNumber = None
        self._PhoneFlag = None
        self._Email = None
        self._EmailFlag = None
        self._IsReceiverOwner = None
        self._WechatFlag = None
        self._Uin = None

    @property
    def Uid(self):
        """id
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Name(self):
        """名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PhoneNumber(self):
        """手机号码
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def PhoneFlag(self):
        """手机号码是否验证
        :rtype: int
        """
        return self._PhoneFlag

    @PhoneFlag.setter
    def PhoneFlag(self, PhoneFlag):
        self._PhoneFlag = PhoneFlag

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def EmailFlag(self):
        """邮箱是否验证
        :rtype: int
        """
        return self._EmailFlag

    @EmailFlag.setter
    def EmailFlag(self, EmailFlag):
        self._EmailFlag = EmailFlag

    @property
    def IsReceiverOwner(self):
        """是否主联系人
        :rtype: int
        """
        return self._IsReceiverOwner

    @IsReceiverOwner.setter
    def IsReceiverOwner(self, IsReceiverOwner):
        self._IsReceiverOwner = IsReceiverOwner

    @property
    def WechatFlag(self):
        """是否允许微信接收通知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WechatFlag

    @WechatFlag.setter
    def WechatFlag(self, WechatFlag):
        self._WechatFlag = WechatFlag

    @property
    def Uin(self):
        """账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._PhoneNumber = params.get("PhoneNumber")
        self._PhoneFlag = params.get("PhoneFlag")
        self._Email = params.get("Email")
        self._EmailFlag = params.get("EmailFlag")
        self._IsReceiverOwner = params.get("IsReceiverOwner")
        self._WechatFlag = params.get("WechatFlag")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 要删除的用户 UIN/UID和用户组 ID对应数组
        :type Info: list of GroupIdOfUidInfo
        """
        self._Info = None

    @property
    def Info(self):
        """要删除的用户 UIN/UID和用户组 ID对应数组
        :rtype: list of GroupIdOfUidInfo
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup返回参数结构体

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


class RoleInfo(AbstractModel):
    """角色详细信息

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID
        :type RoleId: str
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _PolicyDocument: 角色的策略文档
        :type PolicyDocument: str
        :param _Description: 角色描述
        :type Description: str
        :param _AddTime: 角色的创建时间
        :type AddTime: str
        :param _UpdateTime: 角色的最近一次时间
        :type UpdateTime: str
        :param _ConsoleLogin: 角色是否允许登录
        :type ConsoleLogin: int
        :param _RoleType: 角色类型，取user、system或service_linked
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleType: str
        :param _SessionDuration: 有效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionDuration: int
        :param _DeletionTaskId: 服务相关角色删除TaskId
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionTaskId: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of RoleTags
        :param _RoleArn: 角色RoleArn信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleArn: str
        """
        self._RoleId = None
        self._RoleName = None
        self._PolicyDocument = None
        self._Description = None
        self._AddTime = None
        self._UpdateTime = None
        self._ConsoleLogin = None
        self._RoleType = None
        self._SessionDuration = None
        self._DeletionTaskId = None
        self._Tags = None
        self._RoleArn = None

    @property
    def RoleId(self):
        """角色ID
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyDocument(self):
        """角色的策略文档
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        """角色描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        """角色的创建时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def UpdateTime(self):
        """角色的最近一次时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ConsoleLogin(self):
        """角色是否允许登录
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def RoleType(self):
        """角色类型，取user、system或service_linked
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def SessionDuration(self):
        """有效时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def DeletionTaskId(self):
        """服务相关角色删除TaskId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RoleTags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RoleArn(self):
        """角色RoleArn信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._RoleType = params.get("RoleType")
        self._SessionDuration = params.get("SessionDuration")
        self._DeletionTaskId = params.get("DeletionTaskId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RoleArn = params.get("RoleArn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleTags(AbstractModel):
    """角色标签类型

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
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
        


class SAMLProviderInfo(AbstractModel):
    """SAML身份提供商

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        :param _Description: SAML身份提供商描述
        :type Description: str
        :param _CreateTime: SAML身份提供商创建时间
        :type CreateTime: str
        :param _ModifyTime: SAML身份提供商上次修改时间
        :type ModifyTime: str
        """
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """SAML身份提供商描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        """SAML身份提供商创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """SAML身份提供商上次修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretIdLastUsed(AbstractModel):
    """密钥最后使用时间

    """

    def __init__(self):
        r"""
        :param _SecretId: 密钥ID
        :type SecretId: str
        :param _LastUsedDate: 最后访问日期(有1天延迟)
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUsedDate: str
        :param _LastSecretUsedDate: 最后密钥访问日期
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSecretUsedDate: int
        """
        self._SecretId = None
        self._LastUsedDate = None
        self._LastSecretUsedDate = None

    @property
    def SecretId(self):
        """密钥ID
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def LastUsedDate(self):
        """最后访问日期(有1天延迟)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUsedDate

    @LastUsedDate.setter
    def LastUsedDate(self, LastUsedDate):
        self._LastUsedDate = LastUsedDate

    @property
    def LastSecretUsedDate(self):
        """最后密钥访问日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastSecretUsedDate

    @LastSecretUsedDate.setter
    def LastSecretUsedDate(self, LastSecretUsedDate):
        self._LastSecretUsedDate = LastSecretUsedDate


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._LastUsedDate = params.get("LastUsedDate")
        self._LastSecretUsedDate = params.get("LastSecretUsedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _VersionId: 策略版本号，可由ListPolicyVersions获取
        :type VersionId: int
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        """策略版本号，可由ListPolicyVersions获取
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion返回参数结构体

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


class SetMfaFlagRequest(AbstractModel):
    """SetMfaFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OpUin: 设置用户的uin
        :type OpUin: int
        :param _LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        :param _ActionFlag: 操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        self._OpUin = None
        self._LoginFlag = None
        self._ActionFlag = None

    @property
    def OpUin(self):
        """设置用户的uin
        :rtype: int
        """
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def LoginFlag(self):
        """登录保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        """操作保护设置
        :rtype: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag


    def _deserialize(self, params):
        self._OpUin = params.get("OpUin")
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionMfaFlag()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionMfaFlag()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMfaFlagResponse(AbstractModel):
    """SetMfaFlag返回参数结构体

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


class StrategyInfo(AbstractModel):
    """策略信息

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _PolicyName: 策略名称。
        :type PolicyName: str
        :param _AddTime: 策略创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _Type: 策略类型。1 表示自定义策略，2 表示预设策略。
        :type Type: int
        :param _Description: 策略描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateMode: 创建来源，1 通过控制台创建, 2 通过策略语法创建。
        :type CreateMode: int
        :param _Attachments: 关联的用户数
        :type Attachments: int
        :param _ServiceType: 策略关联的产品
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _IsAttached: 当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAttached: int
        :param _Deactived: 是否已下线
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param _DeactivedDetail: 已下线产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param _IsServiceLinkedPolicy: 是否是服务相关角色策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsServiceLinkedPolicy: int
        :param _AttachEntityCount: 关联策略实体数
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachEntityCount: int
        :param _AttachEntityBoundaryCount: 关联权限边界实体数
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachEntityBoundaryCount: int
        :param _UpdateTime: 最后编辑时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._Type = None
        self._Description = None
        self._CreateMode = None
        self._Attachments = None
        self._ServiceType = None
        self._IsAttached = None
        self._Deactived = None
        self._DeactivedDetail = None
        self._IsServiceLinkedPolicy = None
        self._AttachEntityCount = None
        self._AttachEntityBoundaryCount = None
        self._UpdateTime = None

    @property
    def PolicyId(self):
        """策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名称。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        """策略创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Type(self):
        """策略类型。1 表示自定义策略，2 表示预设策略。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        """策略描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateMode(self):
        """创建来源，1 通过控制台创建, 2 通过策略语法创建。
        :rtype: int
        """
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Attachments(self):
        """关联的用户数
        :rtype: int
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def ServiceType(self):
        """策略关联的产品
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def IsAttached(self):
        """当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsAttached

    @IsAttached.setter
    def IsAttached(self, IsAttached):
        self._IsAttached = IsAttached

    @property
    def Deactived(self):
        """是否已下线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        """已下线产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail

    @property
    def IsServiceLinkedPolicy(self):
        """是否是服务相关角色策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsServiceLinkedPolicy

    @IsServiceLinkedPolicy.setter
    def IsServiceLinkedPolicy(self, IsServiceLinkedPolicy):
        self._IsServiceLinkedPolicy = IsServiceLinkedPolicy

    @property
    def AttachEntityCount(self):
        """关联策略实体数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AttachEntityCount

    @AttachEntityCount.setter
    def AttachEntityCount(self, AttachEntityCount):
        self._AttachEntityCount = AttachEntityCount

    @property
    def AttachEntityBoundaryCount(self):
        """关联权限边界实体数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AttachEntityBoundaryCount

    @AttachEntityBoundaryCount.setter
    def AttachEntityBoundaryCount(self, AttachEntityBoundaryCount):
        self._AttachEntityBoundaryCount = AttachEntityBoundaryCount

    @property
    def UpdateTime(self):
        """最后编辑时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._CreateMode = params.get("CreateMode")
        self._Attachments = params.get("Attachments")
        self._ServiceType = params.get("ServiceType")
        self._IsAttached = params.get("IsAttached")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        self._IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")
        self._AttachEntityCount = params.get("AttachEntityCount")
        self._AttachEntityBoundaryCount = params.get("AttachEntityBoundaryCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountInfo(AbstractModel):
    """子用户信息

    """

    def __init__(self):
        r"""
        :param _Uin: 子用户用户 ID
        :type Uin: int
        :param _Name: 子用户用户名
        :type Name: str
        :param _Uid: 子用户 UID
        :type Uid: int
        :param _Remark: 子用户备注
        :type Remark: str
        :param _ConsoleLogin: 子用户能否登录控制台
        :type ConsoleLogin: int
        :param _PhoneNum: 手机号
        :type PhoneNum: str
        :param _CountryCode: 区号
        :type CountryCode: str
        :param _Email: 邮箱
        :type Email: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._ConsoleLogin = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None
        self._CreateTime = None
        self._NickName = None

    @property
    def Uin(self):
        """子用户用户 ID
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        """子用户 UID
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        """子用户备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        """子用户能否登录控制台
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def PhoneNum(self):
        """手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """区号
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NickName(self):
        """昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        self._CreateTime = params.get("CreateTime")
        self._NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountUser(AbstractModel):
    """子用户信息

    """

    def __init__(self):
        r"""
        :param _Uin: 子用户用户 ID
        :type Uin: int
        :param _Name: 子用户用户名
        :type Name: str
        :param _Uid: 子用户 UID，UID是用户作为消息接收人时的唯一标识，和 UIN 一样可以唯一标识一个用户，可通过接口https://cloud.tencent.com/document/api/598/53486 获取
        :type Uid: int
        :param _Remark: 子用户备注
        :type Remark: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UserType: 用户类型(2:子用户;3:企业微信子用户;4:协作者;5:消息接收人)
        :type UserType: int
        :param _LastLoginIp: 最近登录IP
        :type LastLoginIp: str
        :param _LastLoginTime: 最近登录时间，回参为空，即为未登录过控制台
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLoginTime: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._CreateTime = None
        self._UserType = None
        self._LastLoginIp = None
        self._LastLoginTime = None

    @property
    def Uin(self):
        """子用户用户 ID
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        """子用户 UID，UID是用户作为消息接收人时的唯一标识，和 UIN 一样可以唯一标识一个用户，可通过接口https://cloud.tencent.com/document/api/598/53486 获取
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        """子用户备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserType(self):
        """用户类型(2:子用户;3:企业微信子用户;4:协作者;5:消息接收人)
        :rtype: int
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def LastLoginIp(self):
        """最近登录IP
        :rtype: str
        """
        return self._LastLoginIp

    @LastLoginIp.setter
    def LastLoginIp(self, LastLoginIp):
        self._LastLoginIp = LastLoginIp

    @property
    def LastLoginTime(self):
        """最近登录时间，回参为空，即为未登录过控制台
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UserType = params.get("UserType")
        self._LastLoginIp = params.get("LastLoginIp")
        self._LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleRequest(AbstractModel):
    """TagRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: 标签
        :type Tags: list of RoleTags
        :param _RoleName: 角色名，与角色ID至少输入一个
        :type RoleName: str
        :param _RoleId: 角色ID，与角色名至少输入一个
        :type RoleId: str
        """
        self._Tags = None
        self._RoleName = None
        self._RoleId = None

    @property
    def Tags(self):
        """标签
        :rtype: list of RoleTags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RoleName(self):
        """角色名，与角色ID至少输入一个
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        """角色ID，与角色名至少输入一个
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleResponse(AbstractModel):
    """TagRole返回参数结构体

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


class UntagRoleRequest(AbstractModel):
    """UntagRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKeys: 标签键
        :type TagKeys: list of str
        :param _RoleName: 角色名，与角色ID至少输入一个
        :type RoleName: str
        :param _RoleId: 角色ID，与角色名至少输入一个
        :type RoleId: str
        """
        self._TagKeys = None
        self._RoleName = None
        self._RoleId = None

    @property
    def TagKeys(self):
        """标签键
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RoleName(self):
        """角色名，与角色ID至少输入一个
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        """角色ID，与角色名至少输入一个
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntagRoleResponse(AbstractModel):
    """UntagRole返回参数结构体

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


class UpdateAccessKeyRequest(AbstractModel):
    """UpdateAccessKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 指定需要更新的AccessKeyId
        :type AccessKeyId: str
        :param _Status: 密钥状态，激活（Active）或未激活（Inactive）
        :type Status: str
        :param _TargetUin: 指定用户Uin，不填默认为当前用户更新访问密钥
        :type TargetUin: int
        """
        self._AccessKeyId = None
        self._Status = None
        self._TargetUin = None

    @property
    def AccessKeyId(self):
        """指定需要更新的AccessKeyId
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def Status(self):
        """密钥状态，激活（Active）或未激活（Inactive）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetUin(self):
        """指定用户Uin，不填默认为当前用户更新访问密钥
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._Status = params.get("Status")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyResponse(AbstractModel):
    """UpdateAccessKey返回参数结构体

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


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param _RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param _RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self._PolicyDocument = None
        self._RoleId = None
        self._RoleName = None

    @property
    def PolicyDocument(self):
        """策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def RoleId(self):
        """角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._PolicyDocument = params.get("PolicyDocument")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy返回参数结构体

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


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 用户组 ID
        :type GroupId: int
        :param _GroupName: 用户组名
        :type GroupName: str
        :param _Remark: 用户组描述
        :type Remark: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Remark = None

    @property
    def GroupId(self):
        """用户组 ID
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """用户组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        """用户组描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup返回参数结构体

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


class UpdateOIDCConfigRequest(AbstractModel):
    """UpdateOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL
        :type IdentityUrl: str
        :param _ClientId: 客户端ID
        :type ClientId: list of str
        :param _Name: 名称
        :type Name: str
        :param _IdentityKey: 签名公钥，需要base64
        :type IdentityKey: str
        :param _Description: 描述
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._Name = None
        self._IdentityKey = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID
        :rtype: list of str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdentityKey(self):
        """签名公钥，需要base64
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._Name = params.get("Name")
        self._IdentityKey = params.get("IdentityKey")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOIDCConfigResponse(AbstractModel):
    """UpdateOIDCConfig返回参数结构体

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


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID，与PolicyName二选一必填
        :type PolicyId: int
        :param _PolicyName: 策略名，与PolicyId二选一必填
        :type PolicyName: str
        :param _Description: 策略描述
        :type Description: str
        :param _PolicyDocument: 策略文档
        :type PolicyDocument: str
        :param _Alias: 预设策略备注
        :type Alias: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Description = None
        self._PolicyDocument = None
        self._Alias = None

    @property
    def PolicyId(self):
        """策略ID，与PolicyName二选一必填
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        """策略名，与PolicyId二选一必填
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        """策略描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PolicyDocument(self):
        """策略文档
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Alias(self):
        """预设策略备注
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略id，入参是PolicyName时，才会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """策略id，入参是PolicyName时，才会返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsoleLogin: 是否可登录，可登录：1，不可登录：0
        :type ConsoleLogin: int
        :param _RoleId: 角色ID，入参 RoleId 与 RoleName 二选一
        :type RoleId: int
        :param _RoleName: 角色名，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self._ConsoleLogin = None
        self._RoleId = None
        self._RoleName = None

    @property
    def ConsoleLogin(self):
        """是否可登录，可登录：1，不可登录：0
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def RoleId(self):
        """角色ID，入参 RoleId 与 RoleName 二选一
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin返回参数结构体

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


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Description: 角色描述
        :type Description: str
        :param _RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param _RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self._Description = None
        self._RoleId = None
        self._RoleName = None

    @property
    def Description(self):
        """角色描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoleId(self):
        """角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        """角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription返回参数结构体

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


class UpdateRoleSessionDurationRequest(AbstractModel):
    """UpdateRoleSessionDuration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionDuration: 时长(秒)
        :type SessionDuration: int
        :param _RoleName: 角色名(与角色ID必填一个)
        :type RoleName: str
        :param _RoleId: 角色ID(与角色名必填一个)
        :type RoleId: int
        """
        self._SessionDuration = None
        self._RoleName = None
        self._RoleId = None

    @property
    def SessionDuration(self):
        """时长(秒)
        :rtype: int
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def RoleName(self):
        """角色名(与角色ID必填一个)
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        """角色ID(与角色名必填一个)
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        self._SessionDuration = params.get("SessionDuration")
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleSessionDurationResponse(AbstractModel):
    """UpdateRoleSessionDuration返回参数结构体

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


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: SAML身份提供商名称
        :type Name: str
        :param _Description: SAML身份提供商描述
        :type Description: str
        :param _SAMLMetadataDocument: SAML身份提供商Base64编码的元数据文档
        :type SAMLMetadataDocument: str
        """
        self._Name = None
        self._Description = None
        self._SAMLMetadataDocument = None

    @property
    def Name(self):
        """SAML身份提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """SAML身份提供商描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SAMLMetadataDocument(self):
        """SAML身份提供商Base64编码的元数据文档
        :rtype: str
        """
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider返回参数结构体

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


class UpdateUserOIDCConfigRequest(AbstractModel):
    """UpdateUserOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL。OpenID Connect身份提供商标识。
对应企业IdP提供的Openid-configuration中"issuer"字段的值，该URL必须以https开头，符合标准URL格式，不允许带有query参数（以?标识）、fragment片段（以#标识）和登录信息（以@标识）。
        :type IdentityUrl: str
        :param _ClientId: 客户端ID，在OpenID Connect身份提供商注册的客户端ID，允许英文字母、数字、特殊字符.-_:/，不能以特殊字符.-_:/开头，单个客户端ID最大64个字符。
        :type ClientId: str
        :param _AuthorizationEndpoint: 授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值，该URL必须以https开头，符合标准URL格式，不允许带有query参数（以?标识）、fragment片段（以#标识）和登录信息（以@标识）。
        :type AuthorizationEndpoint: str
        :param _ResponseType: 授权请求Response type，有code，id_token，固定值id_token。
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode。授权请求返回模式，有form_post和fragment两种可选模式，推荐选择form_post模式。
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段,仅支持英文字母、数字、汉字、符号@、＆_[]-的组合，1-255个中文或英文字符
        :type MappingFiled: str
        :param _IdentityKey: RSA签名公钥，JWKS格式，需要进行base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :type IdentityKey: str
        :param _Scope: 授权请求Scope。有openid; email;profile三种。代表授权请求信息范围openid表示请求访问用户的身份信息，email表示请求访问用户的电子邮件地址，profile表示请求访问用户的基本信息。默认必选openid。
        :type Scope: list of str
        :param _Description: 描述，长度为1~255个英文或中文字符，默认值为空。
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL。OpenID Connect身份提供商标识。
对应企业IdP提供的Openid-configuration中"issuer"字段的值，该URL必须以https开头，符合标准URL格式，不允许带有query参数（以?标识）、fragment片段（以#标识）和登录信息（以@标识）。
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID，在OpenID Connect身份提供商注册的客户端ID，允许英文字母、数字、特殊字符.-_:/，不能以特殊字符.-_:/开头，单个客户端ID最大64个字符。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值，该URL必须以https开头，符合标准URL格式，不允许带有query参数（以?标识）、fragment片段（以#标识）和登录信息（以@标识）。
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """授权请求Response type，有code，id_token，固定值id_token。
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode。授权请求返回模式，有form_post和fragment两种可选模式，推荐选择form_post模式。
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段,仅支持英文字母、数字、汉字、符号@、＆_[]-的组合，1-255个中文或英文字符
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """RSA签名公钥，JWKS格式，需要进行base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """授权请求Scope。有openid; email;profile三种。代表授权请求信息范围openid表示请求访问用户的身份信息，email表示请求访问用户的电子邮件地址，profile表示请求访问用户的基本信息。默认必选openid。
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """描述，长度为1~255个英文或中文字符，默认值为空。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserOIDCConfigResponse(AbstractModel):
    """UpdateUserOIDCConfig返回参数结构体

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


class UpdateUserRequest(AbstractModel):
    """UpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 子用户用户名
        :type Name: str
        :param _Remark: 子用户备注
        :type Remark: str
        :param _ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param _Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :type Password: str
        :param _NeedResetPassword: 子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :type NeedResetPassword: int
        :param _PhoneNum: 手机号
        :type PhoneNum: str
        :param _CountryCode: 区号
        :type CountryCode: str
        :param _Email: 邮箱
        :type Email: str
        """
        self._Name = None
        self._Remark = None
        self._ConsoleLogin = None
        self._Password = None
        self._NeedResetPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """子用户备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        """子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def Password(self):
        """子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NeedResetPassword(self):
        """子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :rtype: int
        """
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword

    @property
    def PhoneNum(self):
        """手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """区号
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._Password = params.get("Password")
        self._NeedResetPassword = params.get("NeedResetPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser返回参数结构体

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


class UpdateUserSAMLConfigRequest(AbstractModel):
    """UpdateUserSAMLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operate: 修改的操作类型:enable:启用,disable:禁用,updateSAML:修改元数据文档
        :type Operate: str
        :param _SAMLMetadataDocument: 元数据文档，需要base64 encode，仅当Operate为updateSAML时需要此参数
        :type SAMLMetadataDocument: str
        :param _AuxiliaryDomain: 辅助域名
        :type AuxiliaryDomain: str
        """
        self._Operate = None
        self._SAMLMetadataDocument = None
        self._AuxiliaryDomain = None

    @property
    def Operate(self):
        """修改的操作类型:enable:启用,disable:禁用,updateSAML:修改元数据文档
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def SAMLMetadataDocument(self):
        """元数据文档，需要base64 encode，仅当Operate为updateSAML时需要此参数
        :rtype: str
        """
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument

    @property
    def AuxiliaryDomain(self):
        """辅助域名
        :rtype: str
        """
        return self._AuxiliaryDomain

    @AuxiliaryDomain.setter
    def AuxiliaryDomain(self, AuxiliaryDomain):
        self._AuxiliaryDomain = AuxiliaryDomain


    def _deserialize(self, params):
        self._Operate = params.get("Operate")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        self._AuxiliaryDomain = params.get("AuxiliaryDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserSAMLConfigResponse(AbstractModel):
    """UpdateUserSAMLConfig返回参数结构体

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


class WeChatWorkSubAccount(AbstractModel):
    """企业微信子用户

    """

    def __init__(self):
        r"""
        :param _Uin: 子用户用户 ID
        :type Uin: int
        :param _Name: 子用户用户名
        :type Name: str
        :param _Uid: 子用户 UID
        :type Uid: int
        :param _Remark: 备注
        :type Remark: str
        :param _ConsoleLogin: 子用户能否登录控制台
        :type ConsoleLogin: int
        :param _PhoneNum: 手机号
        :type PhoneNum: str
        :param _CountryCode: 区号
        :type CountryCode: str
        :param _Email: 邮箱
        :type Email: str
        :param _WeChatWorkUserId: 企业微信UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type WeChatWorkUserId: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._ConsoleLogin = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None
        self._WeChatWorkUserId = None
        self._CreateTime = None

    @property
    def Uin(self):
        """子用户用户 ID
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        """子用户用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        """子用户 UID
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

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
    def ConsoleLogin(self):
        """子用户能否登录控制台
        :rtype: int
        """
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def PhoneNum(self):
        """手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        """区号
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def WeChatWorkUserId(self):
        """企业微信UserId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WeChatWorkUserId

    @WeChatWorkUserId.setter
    def WeChatWorkUserId(self, WeChatWorkUserId):
        self._WeChatWorkUserId = WeChatWorkUserId

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        self._WeChatWorkUserId = params.get("WeChatWorkUserId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        