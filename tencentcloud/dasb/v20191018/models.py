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


class Acl(AbstractModel):
    """访问权限

    """

    def __init__(self):
        r"""
        :param Id: 访问权限ID
        :type Id: int
        :param Name: 访问权限名称
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板文本（目前含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板文本（目前含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制（预留参数，暂未启用）
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制（预留参数，暂未启用）
        :type MaxFileDownSize: int
        :param AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param UserSet: 关联的用户列表
        :type UserSet: list of User
        :param UserGroupSet: 关联的用户组列表
        :type UserGroupSet: list of Group
        :param DeviceSet: 关联的资产列表
        :type DeviceSet: list of Device
        :param DeviceGroupSet: 关联的资产组列表
        :type DeviceGroupSet: list of Group
        :param AccountSet: 关联的账号列表
        :type AccountSet: list of str
        :param CmdTemplateSet: 关联的高危命令模板列表
        :type CmdTemplateSet: list of CmdTemplate
        :param AllowDiskFileUp: 是否开启 RDP 磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param AllowDiskFileDown: 是否开启 RDP 磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param AllowShellFileUp: 是否开启 rz sz 文件上传
        :type AllowShellFileUp: bool
        :param AllowShellFileDown: 是否开启 rz sz 文件下载
        :type AllowShellFileDown: bool
        :param AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param Status: 访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :type Status: int
        :param Department: 所属部门的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.dasb.v20191018.models.Department`
        """
        self.Id = None
        self.Name = None
        self.AllowDiskRedirect = None
        self.AllowClipFileUp = None
        self.AllowClipFileDown = None
        self.AllowClipTextUp = None
        self.AllowClipTextDown = None
        self.AllowFileUp = None
        self.MaxFileUpSize = None
        self.AllowFileDown = None
        self.MaxFileDownSize = None
        self.AllowAnyAccount = None
        self.UserSet = None
        self.UserGroupSet = None
        self.DeviceSet = None
        self.DeviceGroupSet = None
        self.AccountSet = None
        self.CmdTemplateSet = None
        self.AllowDiskFileUp = None
        self.AllowDiskFileDown = None
        self.AllowShellFileUp = None
        self.AllowShellFileDown = None
        self.AllowFileDel = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.Status = None
        self.Department = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.AllowDiskRedirect = params.get("AllowDiskRedirect")
        self.AllowClipFileUp = params.get("AllowClipFileUp")
        self.AllowClipFileDown = params.get("AllowClipFileDown")
        self.AllowClipTextUp = params.get("AllowClipTextUp")
        self.AllowClipTextDown = params.get("AllowClipTextDown")
        self.AllowFileUp = params.get("AllowFileUp")
        self.MaxFileUpSize = params.get("MaxFileUpSize")
        self.AllowFileDown = params.get("AllowFileDown")
        self.MaxFileDownSize = params.get("MaxFileDownSize")
        self.AllowAnyAccount = params.get("AllowAnyAccount")
        if params.get("UserSet") is not None:
            self.UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self.UserSet.append(obj)
        if params.get("UserGroupSet") is not None:
            self.UserGroupSet = []
            for item in params.get("UserGroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.UserGroupSet.append(obj)
        if params.get("DeviceSet") is not None:
            self.DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self.DeviceSet.append(obj)
        if params.get("DeviceGroupSet") is not None:
            self.DeviceGroupSet = []
            for item in params.get("DeviceGroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.DeviceGroupSet.append(obj)
        self.AccountSet = params.get("AccountSet")
        if params.get("CmdTemplateSet") is not None:
            self.CmdTemplateSet = []
            for item in params.get("CmdTemplateSet"):
                obj = CmdTemplate()
                obj._deserialize(item)
                self.CmdTemplateSet.append(obj)
        self.AllowDiskFileUp = params.get("AllowDiskFileUp")
        self.AllowDiskFileDown = params.get("AllowDiskFileDown")
        self.AllowShellFileUp = params.get("AllowShellFileUp")
        self.AllowShellFileDown = params.get("AllowShellFileDown")
        self.AllowFileDel = params.get("AllowFileDel")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        self.Status = params.get("Status")
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceGroupMembersRequest(AbstractModel):
    """AddDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 资产组ID
        :type Id: int
        :param MemberIdSet: 需要添加到资产组的资产ID集合
        :type MemberIdSet: list of int non-negative
        """
        self.Id = None
        self.MemberIdSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceGroupMembersResponse(AbstractModel):
    """AddDeviceGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddUserGroupMembersRequest(AbstractModel):
    """AddUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 用户组ID
        :type Id: int
        :param MemberIdSet: 成员用户ID集合
        :type MemberIdSet: list of int non-negative
        """
        self.Id = None
        self.MemberIdSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserGroupMembersResponse(AbstractModel):
    """AddUserGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindDeviceResourceRequest(AbstractModel):
    """BindDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceIdSet: 资产ID集合
        :type DeviceIdSet: list of int non-negative
        :param ResourceId: 堡垒机服务ID
        :type ResourceId: str
        """
        self.DeviceIdSet = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.DeviceIdSet = params.get("DeviceIdSet")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceResourceResponse(AbstractModel):
    """BindDeviceResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CmdTemplate(AbstractModel):
    """高危命令模板

    """

    def __init__(self):
        r"""
        :param Id: 高危命令模板ID
        :type Id: int
        :param Name: 高危命令模板名称
        :type Name: str
        :param CmdList: 命令列表，命令之间用换行符（"\n"）分隔
        :type CmdList: str
        """
        self.Id = None
        self.Name = None
        self.CmdList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.CmdList = params.get("CmdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRequest(AbstractModel):
    """CreateAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 权限名称，最大32字符，不能包含空白字符
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板文本（含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板文本（含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启 SFTP 文件上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制（预留参数，目前暂未使用）
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启 SFTP 文件下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制（预留参数，目前暂未使用）
        :type MaxFileDownSize: int
        :param UserIdSet: 关联的用户ID集合
        :type UserIdSet: list of int non-negative
        :param UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param DeviceIdSet: 关联的资产ID集合
        :type DeviceIdSet: list of int non-negative
        :param DeviceGroupIdSet: 关联的资产组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param AccountSet: 关联的账号
        :type AccountSet: list of str
        :param CmdTemplateIdSet: 关联的高危命令模板ID
        :type CmdTemplateIdSet: list of int non-negative
        :param AllowDiskFileUp: 是否开启rdp磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param AllowDiskFileDown: 是否开启rdp磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param AllowShellFileUp: 是否开启rz sz文件上传
        :type AllowShellFileUp: bool
        :param AllowShellFileDown: 是否开启rz sz文件下载
        :type AllowShellFileDown: bool
        :param AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param DepartmentId: 访问权限所属部门的ID
        :type DepartmentId: str
        """
        self.Name = None
        self.AllowDiskRedirect = None
        self.AllowAnyAccount = None
        self.AllowClipFileUp = None
        self.AllowClipFileDown = None
        self.AllowClipTextUp = None
        self.AllowClipTextDown = None
        self.AllowFileUp = None
        self.MaxFileUpSize = None
        self.AllowFileDown = None
        self.MaxFileDownSize = None
        self.UserIdSet = None
        self.UserGroupIdSet = None
        self.DeviceIdSet = None
        self.DeviceGroupIdSet = None
        self.AccountSet = None
        self.CmdTemplateIdSet = None
        self.AllowDiskFileUp = None
        self.AllowDiskFileDown = None
        self.AllowShellFileUp = None
        self.AllowShellFileDown = None
        self.AllowFileDel = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AllowDiskRedirect = params.get("AllowDiskRedirect")
        self.AllowAnyAccount = params.get("AllowAnyAccount")
        self.AllowClipFileUp = params.get("AllowClipFileUp")
        self.AllowClipFileDown = params.get("AllowClipFileDown")
        self.AllowClipTextUp = params.get("AllowClipTextUp")
        self.AllowClipTextDown = params.get("AllowClipTextDown")
        self.AllowFileUp = params.get("AllowFileUp")
        self.MaxFileUpSize = params.get("MaxFileUpSize")
        self.AllowFileDown = params.get("AllowFileDown")
        self.MaxFileDownSize = params.get("MaxFileDownSize")
        self.UserIdSet = params.get("UserIdSet")
        self.UserGroupIdSet = params.get("UserGroupIdSet")
        self.DeviceIdSet = params.get("DeviceIdSet")
        self.DeviceGroupIdSet = params.get("DeviceGroupIdSet")
        self.AccountSet = params.get("AccountSet")
        self.CmdTemplateIdSet = params.get("CmdTemplateIdSet")
        self.AllowDiskFileUp = params.get("AllowDiskFileUp")
        self.AllowDiskFileDown = params.get("AllowDiskFileDown")
        self.AllowShellFileUp = params.get("AllowShellFileUp")
        self.AllowShellFileDown = params.get("AllowShellFileDown")
        self.AllowFileDel = params.get("AllowFileDel")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    """CreateAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 新建成功的访问权限ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateDeviceGroupRequest(AbstractModel):
    """CreateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 资产组名，最大长度32字符
        :type Name: str
        :param DepartmentId: 资产组所属部门ID，如：1.2.3
        :type DepartmentId: str
        """
        self.Name = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceGroupResponse(AbstractModel):
    """CreateDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 新建成功的资产组ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 用户组名，最大长度32字符
        :type Name: str
        :param DepartmentId: 用户组所属部门的ID，如：1.2.3
        :type DepartmentId: str
        """
        self.Name = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DepartmentId = params.get("DepartmentId")
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
        :param Id: 新建成功的用户组ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserName: 用户名, 3-20个字符, 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :type UserName: str
        :param RealName: 用户姓名，最大长度20个字符，不能包含空白字符
        :type RealName: str
        :param Phone: 大陆手机号直接填写，如果是其他国家、地区号码， 按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param ValidateTo: 用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param AuthType: 认证方式，0 - 本地， 1 - LDAP， 2 - OAuth 不传则默认为0
        :type AuthType: int
        :param ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param DepartmentId: 所属部门ID，如：“1.2.3”
        :type DepartmentId: str
        """
        self.UserName = None
        self.RealName = None
        self.Phone = None
        self.Email = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.GroupIdSet = None
        self.AuthType = None
        self.ValidateTime = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        self.GroupIdSet = params.get("GroupIdSet")
        self.AuthType = params.get("AuthType")
        self.ValidateTime = params.get("ValidateTime")
        self.DepartmentId = params.get("DepartmentId")
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
        :param Id: 新建用户的ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DeleteAclsRequest(AbstractModel):
    """DeleteAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的权限ID集合
        :type IdSet: list of int non-negative
        """
        self.IdSet = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclsResponse(AbstractModel):
    """DeleteAcls返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceGroupMembersRequest(AbstractModel):
    """DeleteDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 资产组ID
        :type Id: int
        :param MemberIdSet: 需要删除的资产ID集合
        :type MemberIdSet: list of int non-negative
        """
        self.Id = None
        self.MemberIdSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupMembersResponse(AbstractModel):
    """DeleteDeviceGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceGroupsRequest(AbstractModel):
    """DeleteDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的资产组ID集合
        :type IdSet: list of int non-negative
        """
        self.IdSet = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupsResponse(AbstractModel):
    """DeleteDeviceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserGroupMembersRequest(AbstractModel):
    """DeleteUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 用户组ID
        :type Id: int
        :param MemberIdSet: 需删除的成员用户ID集合
        :type MemberIdSet: list of int non-negative
        """
        self.Id = None
        self.MemberIdSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupMembersResponse(AbstractModel):
    """DeleteUserGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserGroupsRequest(AbstractModel):
    """DeleteUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的用户组ID集合
        :type IdSet: list of int non-negative
        """
        self.IdSet = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupsResponse(AbstractModel):
    """DeleteUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的用户ID集合
        :type IdSet: list of int non-negative
        """
        self.IdSet = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
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


class Department(AbstractModel):
    """部门信息

    """

    def __init__(self):
        r"""
        :param Id: 部门ID
        :type Id: str
        :param Name: 部门名称，1 - 256个字符
        :type Name: str
        :param Managers: 部门管理员账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Managers: list of str
        """
        self.Id = None
        self.Name = None
        self.Managers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Managers = params.get("Managers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAclsRequest(AbstractModel):
    """DescribeAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 访问权限ID集合
        :type IdSet: list of int non-negative
        :param Name: 访问权限名称，模糊查询，最长64字符
        :type Name: str
        :param Offset: 分页偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20，最大500
        :type Limit: int
        :param Exact: 是否根据Name进行精确查询，默认值false
        :type Exact: bool
        :param AuthorizedUserIdSet: 有访问权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param AuthorizedDeviceIdSet: 有访问权限的资产ID集合
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param Status: 访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :type Status: int
        :param DepartmentId: 部门ID，用于过滤属于某个部门的访问权限
        :type DepartmentId: str
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.Exact = None
        self.AuthorizedUserIdSet = None
        self.AuthorizedDeviceIdSet = None
        self.Status = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Exact = params.get("Exact")
        self.AuthorizedUserIdSet = params.get("AuthorizedUserIdSet")
        self.AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self.Status = params.get("Status")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAclsResponse(AbstractModel):
    """DescribeAcls返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 访问权限总数
        :type TotalCount: int
        :param AclSet: 访问权限列表
        :type AclSet: list of Acl
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AclSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AclSet") is not None:
            self.AclSet = []
            for item in params.get("AclSet"):
                obj = Acl()
                obj._deserialize(item)
                self.AclSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDasbImageIdsRequest(AbstractModel):
    """DescribeDasbImageIds请求参数结构体

    """


class DescribeDasbImageIdsResponse(AbstractModel):
    """DescribeDasbImageIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaseImageId: 基础镜像ID
        :type BaseImageId: str
        :param AiImageId: AI镜像ID
        :type AiImageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaseImageId = None
        self.AiImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BaseImageId = params.get("BaseImageId")
        self.AiImageId = params.get("AiImageId")
        self.RequestId = params.get("RequestId")


class DescribeDeviceGroupMembersRequest(AbstractModel):
    """DescribeDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 资产组ID
        :type Id: int
        :param Bound: true - 查询已在该资产组的资产，false - 查询未在该资产组的资产
        :type Bound: bool
        :param Name: 资产名或资产IP，模糊查询
        :type Name: str
        :param Offset: 分页偏移位置
        :type Offset: int
        :param Limit: 每页条目数，默认20, 最大500
        :type Limit: int
        :param Kind: 资产类型，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :type Kind: int
        :param DepartmentId: 所属部门ID
        :type DepartmentId: str
        """
        self.Id = None
        self.Bound = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.Kind = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Bound = params.get("Bound")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Kind = params.get("Kind")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupMembersResponse(AbstractModel):
    """DescribeDeviceGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 资产组成员总数
        :type TotalCount: int
        :param DeviceSet: 资产组成员列表
        :type DeviceSet: list of Device
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceSet") is not None:
            self.DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self.DeviceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceGroupsRequest(AbstractModel):
    """DescribeDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 资产组ID集合
        :type IdSet: list of int non-negative
        :param Name: 资产组名，最长64个字符，模糊查询
        :type Name: str
        :param Offset: 分页偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，缺省20，最大500
        :type Limit: int
        :param DepartmentId: 部门ID，用于过滤属于某个部门的资产组
        :type DepartmentId: str
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupsResponse(AbstractModel):
    """DescribeDeviceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 资产组总数
        :type TotalCount: int
        :param GroupSet: 资产组列表
        :type GroupSet: list of Group
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 资产ID集合
        :type IdSet: list of int non-negative
        :param Name: 资产名或资产IP，模糊查询
        :type Name: str
        :param Ip: 暂未使用
        :type Ip: str
        :param ApCodeSet: 地域码集合
        :type ApCodeSet: list of str
        :param Kind: 操作系统类型, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type Kind: int
        :param Offset: 分页，偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        :param AuthorizedUserIdSet: 有该资产访问权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param ResourceIdSet: 过滤条件，资产绑定的堡垒机服务ID集合
        :type ResourceIdSet: list of str
        :param KindSet: 可提供按照多种类型过滤, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type KindSet: list of int non-negative
        :param DepartmentId: 过滤条件，可按照部门ID进行过滤
        :type DepartmentId: str
        """
        self.IdSet = None
        self.Name = None
        self.Ip = None
        self.ApCodeSet = None
        self.Kind = None
        self.Offset = None
        self.Limit = None
        self.AuthorizedUserIdSet = None
        self.ResourceIdSet = None
        self.KindSet = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Ip = params.get("Ip")
        self.ApCodeSet = params.get("ApCodeSet")
        self.Kind = params.get("Kind")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AuthorizedUserIdSet = params.get("AuthorizedUserIdSet")
        self.ResourceIdSet = params.get("ResourceIdSet")
        self.KindSet = params.get("KindSet")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 资产总数
        :type TotalCount: int
        :param DeviceSet: 资产信息列表
        :type DeviceSet: list of Device
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceSet") is not None:
            self.DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self.DeviceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApCode: 地域码, 如: ap-guangzhou
        :type ApCode: str
        :param VpcId: 按照堡垒机开通的 VPC 实例ID查询
        :type VpcId: str
        :param ResourceIds: 资源ID集合，当传入ID集合时忽略 ApCode 和 VpcId
        :type ResourceIds: list of str
        """
        self.ApCode = None
        self.VpcId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.ApCode = params.get("ApCode")
        self.VpcId = params.get("VpcId")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesResponse(AbstractModel):
    """DescribeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceSet: 堡垒机资源列表
        :type ResourceSet: list of Resource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserGroupMembersRequest(AbstractModel):
    """DescribeUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 用户组ID
        :type Id: int
        :param Bound: true - 查询已添加到该用户组的用户，false - 查询未添加到该用户组的用户
        :type Bound: bool
        :param Name: 用户名或用户姓名，最长64个字符，模糊查询
        :type Name: str
        :param Offset: 分页偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20, 最大500
        :type Limit: int
        :param DepartmentId: 所属部门ID
        :type DepartmentId: str
        """
        self.Id = None
        self.Bound = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Bound = params.get("Bound")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupMembersResponse(AbstractModel):
    """DescribeUserGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 用户组成员总数
        :type TotalCount: int
        :param UserSet: 用户组成员列表
        :type UserSet: list of User
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self.UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self.UserSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserGroupsRequest(AbstractModel):
    """DescribeUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 用户组ID集合
        :type IdSet: list of int non-negative
        :param Name: 用户组名，模糊查询,长度：0-64字符
        :type Name: str
        :param Offset: 分页偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，缺省20，最大500
        :type Limit: int
        :param DepartmentId: 部门ID，用于过滤属于某个部门的用户组
        :type DepartmentId: str
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupsResponse(AbstractModel):
    """DescribeUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 用户组总数
        :type TotalCount: int
        :param GroupSet: 用户组列表
        :type GroupSet: list of Group
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 如果IdSet不为空，则忽略其他参数
        :type IdSet: list of int non-negative
        :param Name: 模糊查询，IdSet、UserName、Phone为空时才生效，对用户名和姓名进行模糊查询
        :type Name: str
        :param Offset: 分页，偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20, 最大500
        :type Limit: int
        :param UserName: 精确查询，IdSet为空时才生效
        :type UserName: str
        :param Phone: 精确查询，IdSet、UserName为空时才生效。
大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param AuthorizedDeviceIdSet: 查询具有指定资产ID访问权限的用户
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param AuthTypeSet: 认证方式，0 - 本地, 1 - LDAP, 2 - OAuth, 不传为全部
        :type AuthTypeSet: list of int non-negative
        :param DepartmentId: 部门ID，用于过滤属于某个部门的用户
        :type DepartmentId: str
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.UserName = None
        self.Phone = None
        self.AuthorizedDeviceIdSet = None
        self.AuthTypeSet = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self.AuthTypeSet = params.get("AuthTypeSet")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 用户总数
        :type TotalCount: int
        :param UserSet: 用户列表
        :type UserSet: list of User
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self.UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self.UserSet.append(obj)
        self.RequestId = params.get("RequestId")


class Device(AbstractModel):
    """资产信息

    """

    def __init__(self):
        r"""
        :param Id: 资产ID
        :type Id: int
        :param InstanceId: 实例ID，对应CVM、CDB等实例ID
        :type InstanceId: str
        :param Name: 资产名
        :type Name: str
        :param PublicIp: 公网IP
        :type PublicIp: str
        :param PrivateIp: 内网IP
        :type PrivateIp: str
        :param ApCode: 地域编码
        :type ApCode: str
        :param OsName: 操作系统名称
        :type OsName: str
        :param Kind: 资产类型 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type Kind: int
        :param Port: 管理端口
        :type Port: int
        :param GroupSet: 所属资产组列表
        :type GroupSet: list of Group
        :param AccountCount: 资产绑定的账号数
        :type AccountCount: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Resource: 堡垒机服务信息，注意没有绑定服务时为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.dasb.v20191018.models.Resource`
        :param Department: 资产所属部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.dasb.v20191018.models.Department`
        """
        self.Id = None
        self.InstanceId = None
        self.Name = None
        self.PublicIp = None
        self.PrivateIp = None
        self.ApCode = None
        self.OsName = None
        self.Kind = None
        self.Port = None
        self.GroupSet = None
        self.AccountCount = None
        self.VpcId = None
        self.SubnetId = None
        self.Resource = None
        self.Department = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.ApCode = params.get("ApCode")
        self.OsName = params.get("OsName")
        self.Kind = params.get("Kind")
        self.Port = params.get("Port")
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.AccountCount = params.get("AccountCount")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("Resource") is not None:
            self.Resource = Resource()
            self.Resource._deserialize(params.get("Resource"))
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Group(AbstractModel):
    """组信息，用于用户组、主机组

    """

    def __init__(self):
        r"""
        :param Id: 组ID
        :type Id: int
        :param Name: 组名称
        :type Name: str
        :param Department: 所属部门信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.dasb.v20191018.models.Department`
        """
        self.Id = None
        self.Name = None
        self.Department = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRequest(AbstractModel):
    """ModifyAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 访问权限名称，最大32字符，不能包含空白字符
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param Id: 访问权限ID
        :type Id: int
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板文本（含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板文本（含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制（预留参数，目前暂未使用）
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制（预留参数，目前暂未使用）
        :type MaxFileDownSize: int
        :param UserIdSet: 关联的用户ID
        :type UserIdSet: list of int non-negative
        :param UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param DeviceIdSet: 关联的资产ID
        :type DeviceIdSet: list of int non-negative
        :param DeviceGroupIdSet: 关联的资产组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param AccountSet: 关联的账号
        :type AccountSet: list of str
        :param CmdTemplateIdSet: 关联的高危命令模板ID
        :type CmdTemplateIdSet: list of int non-negative
        :param AllowDiskFileUp: 是否开启 RDP 磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param AllowDiskFileDown: 是否开启 RDP 磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param AllowShellFileUp: 是否开启rz sz文件上传
        :type AllowShellFileUp: bool
        :param AllowShellFileDown: 是否开启rz sz文件下载
        :type AllowShellFileDown: bool
        :param AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param DepartmentId: 权限所属部门的ID，如：1.2.3
        :type DepartmentId: str
        """
        self.Name = None
        self.AllowDiskRedirect = None
        self.AllowAnyAccount = None
        self.Id = None
        self.AllowClipFileUp = None
        self.AllowClipFileDown = None
        self.AllowClipTextUp = None
        self.AllowClipTextDown = None
        self.AllowFileUp = None
        self.MaxFileUpSize = None
        self.AllowFileDown = None
        self.MaxFileDownSize = None
        self.UserIdSet = None
        self.UserGroupIdSet = None
        self.DeviceIdSet = None
        self.DeviceGroupIdSet = None
        self.AccountSet = None
        self.CmdTemplateIdSet = None
        self.AllowDiskFileUp = None
        self.AllowDiskFileDown = None
        self.AllowShellFileUp = None
        self.AllowShellFileDown = None
        self.AllowFileDel = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AllowDiskRedirect = params.get("AllowDiskRedirect")
        self.AllowAnyAccount = params.get("AllowAnyAccount")
        self.Id = params.get("Id")
        self.AllowClipFileUp = params.get("AllowClipFileUp")
        self.AllowClipFileDown = params.get("AllowClipFileDown")
        self.AllowClipTextUp = params.get("AllowClipTextUp")
        self.AllowClipTextDown = params.get("AllowClipTextDown")
        self.AllowFileUp = params.get("AllowFileUp")
        self.MaxFileUpSize = params.get("MaxFileUpSize")
        self.AllowFileDown = params.get("AllowFileDown")
        self.MaxFileDownSize = params.get("MaxFileDownSize")
        self.UserIdSet = params.get("UserIdSet")
        self.UserGroupIdSet = params.get("UserGroupIdSet")
        self.DeviceIdSet = params.get("DeviceIdSet")
        self.DeviceGroupIdSet = params.get("DeviceGroupIdSet")
        self.AccountSet = params.get("AccountSet")
        self.CmdTemplateIdSet = params.get("CmdTemplateIdSet")
        self.AllowDiskFileUp = params.get("AllowDiskFileUp")
        self.AllowDiskFileDown = params.get("AllowDiskFileDown")
        self.AllowShellFileUp = params.get("AllowShellFileUp")
        self.AllowShellFileDown = params.get("AllowShellFileDown")
        self.AllowFileDel = params.get("AllowFileDel")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclResponse(AbstractModel):
    """ModifyAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 用户ID
        :type Id: int
        :param RealName: 用户姓名，最大长度20个字符，不能包含空格
        :type RealName: str
        :param Phone: 大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param ValidateTo: 用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param AuthType: 认证方式，0 - 本地，1 - LDAP，2 - OAuth 不传则默认为0
        :type AuthType: int
        :param ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param DepartmentId: 用户所属部门的ID，如1.2.3
        :type DepartmentId: str
        """
        self.Id = None
        self.RealName = None
        self.Phone = None
        self.Email = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.GroupIdSet = None
        self.AuthType = None
        self.ValidateTime = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RealName = params.get("RealName")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        self.GroupIdSet = params.get("GroupIdSet")
        self.AuthType = params.get("AuthType")
        self.ValidateTime = params.get("ValidateTime")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """堡垒机服务信息

    """

    def __init__(self):
        r"""
        :param ResourceId: 服务实例ID，如bh-saas-s3ed4r5e
        :type ResourceId: str
        :param ApCode: 地域编码
        :type ApCode: str
        :param SvArgs: 服务实例规格信息
        :type SvArgs: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param Nodes: 服务规格对应的资产数
        :type Nodes: int
        :param RenewFlag: 自动续费标记，0 - 表示默认状态，1 - 表示自动续费，2 - 表示明确不自动续费
        :type RenewFlag: int
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param Status: 资源状态，0 - 未初始化，1 - 正常，2 - 隔离，3 - 销毁，4 - 初始化失败，5 - 初始化中
        :type Status: int
        :param ResourceName: 服务实例名，如T-Sec-堡垒机（SaaS型）
        :type ResourceName: str
        :param Pid: 定价模型ID
        :type Pid: int
        :param CreateTime: 资源创建时间
        :type CreateTime: str
        :param ProductCode: 商品码, p_cds_dasb
        :type ProductCode: str
        :param SubProductCode: 子商品码, sp_cds_dasb_bh_saas
        :type SubProductCode: str
        :param Zone: 可用区
        :type Zone: str
        :param Expired: 是否过期，true-过期，false-未过期
        :type Expired: bool
        :param Deployed: 是否开通，true-开通，false-未开通
        :type Deployed: bool
        :param VpcName: 开通服务的 VPC 名称
        :type VpcName: str
        :param VpcCidrBlock: 开通服务的 VPC 对应的网段
        :type VpcCidrBlock: str
        :param SubnetId: 开通服务的子网ID
        :type SubnetId: str
        :param SubnetName: 开通服务的子网名称
        :type SubnetName: str
        :param CidrBlock: 开通服务的子网网段
        :type CidrBlock: str
        :param PublicIpSet: 外部IP
        :type PublicIpSet: list of str
        :param PrivateIpSet: 内部IP
        :type PrivateIpSet: list of str
        :param ModuleSet: 服务开通的高级功能列表，如:[DB]
        :type ModuleSet: list of str
        :param UsedNodes: 已使用的授权点数
        :type UsedNodes: int
        :param ExtendPoints: 扩展点数
        :type ExtendPoints: int
        :param PackageBandwidth: 带宽扩展包个数(4M)
        :type PackageBandwidth: int
        :param PackageNode: 授权点数扩展包个数(50点)
        :type PackageNode: int
        """
        self.ResourceId = None
        self.ApCode = None
        self.SvArgs = None
        self.VpcId = None
        self.Nodes = None
        self.RenewFlag = None
        self.ExpireTime = None
        self.Status = None
        self.ResourceName = None
        self.Pid = None
        self.CreateTime = None
        self.ProductCode = None
        self.SubProductCode = None
        self.Zone = None
        self.Expired = None
        self.Deployed = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.PublicIpSet = None
        self.PrivateIpSet = None
        self.ModuleSet = None
        self.UsedNodes = None
        self.ExtendPoints = None
        self.PackageBandwidth = None
        self.PackageNode = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ApCode = params.get("ApCode")
        self.SvArgs = params.get("SvArgs")
        self.VpcId = params.get("VpcId")
        self.Nodes = params.get("Nodes")
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        self.ResourceName = params.get("ResourceName")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ProductCode = params.get("ProductCode")
        self.SubProductCode = params.get("SubProductCode")
        self.Zone = params.get("Zone")
        self.Expired = params.get("Expired")
        self.Deployed = params.get("Deployed")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.PublicIpSet = params.get("PublicIpSet")
        self.PrivateIpSet = params.get("PrivateIpSet")
        self.ModuleSet = params.get("ModuleSet")
        self.UsedNodes = params.get("UsedNodes")
        self.ExtendPoints = params.get("ExtendPoints")
        self.PackageBandwidth = params.get("PackageBandwidth")
        self.PackageNode = params.get("PackageNode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserName: 用户名, 3-20个字符 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :type UserName: str
        :param RealName: 用户姓名， 最大20个字符，不能包含空白字符
        :type RealName: str
        :param Phone: 手机号码， 大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param Id: 用户ID
        :type Id: int
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param ValidateTo: 用户失效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param GroupSet: 所属用户组列表
        :type GroupSet: list of Group
        :param AuthType: 认证方式，0 - 本地，1 - LDAP，2 - OAuth
        :type AuthType: int
        :param ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param Department: 用户所属部门（用于出参）
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.dasb.v20191018.models.Department`
        :param DepartmentId: 用户所属部门（用于入参）
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        """
        self.UserName = None
        self.RealName = None
        self.Phone = None
        self.Id = None
        self.Email = None
        self.ValidateFrom = None
        self.ValidateTo = None
        self.GroupSet = None
        self.AuthType = None
        self.ValidateTime = None
        self.Department = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.Phone = params.get("Phone")
        self.Id = params.get("Id")
        self.Email = params.get("Email")
        self.ValidateFrom = params.get("ValidateFrom")
        self.ValidateTo = params.get("ValidateTo")
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.AuthType = params.get("AuthType")
        self.ValidateTime = params.get("ValidateTime")
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        