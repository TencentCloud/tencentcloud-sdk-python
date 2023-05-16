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


class AssetSyncStatus(AbstractModel):
    """资产同步状态

    """

    def __init__(self):
        r"""
        :param LastTime: 上一次同步完成的时间
        :type LastTime: str
        :param LastStatus: 上一次同步的结果。 0 - 从未进行, 1 - 成功， 2 - 失败
        :type LastStatus: int
        :param InProcess: 同步任务是否正在进行中
        :type InProcess: bool
        """
        self.LastTime = None
        self.LastStatus = None
        self.InProcess = None


    def _deserialize(self, params):
        self.LastTime = params.get("LastTime")
        self.LastStatus = params.get("LastStatus")
        self.InProcess = params.get("InProcess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogResult(AbstractModel):
    """审计日志

    """

    def __init__(self):
        r"""
        :param Sid: 被审计会话的Sid
        :type Sid: str
        :param Uin: 审计者的编号
        :type Uin: str
        :param Time: 审计动作发生的时间
        :type Time: str
        :param ClientIp: 审计者的Ip
        :type ClientIp: str
        :param Operation: 审计动作类型，1--回放、2--中断、3--监控
        :type Operation: int
        :param InstanceId: 被审计主机的Id
        :type InstanceId: str
        :param DeviceName: 被审计主机的主机名
        :type DeviceName: str
        :param Protocol: 被审计会话所属的类型，如字符会话
        :type Protocol: str
        :param PrivateIp: 被审计主机的内部Ip
        :type PrivateIp: str
        :param PublicIp: 被审计主机的外部Ip
        :type PublicIp: str
        :param SubAccountUin: 审计者的子账号
        :type SubAccountUin: str
        """
        self.Sid = None
        self.Uin = None
        self.Time = None
        self.ClientIp = None
        self.Operation = None
        self.InstanceId = None
        self.DeviceName = None
        self.Protocol = None
        self.PrivateIp = None
        self.PublicIp = None
        self.SubAccountUin = None


    def _deserialize(self, params):
        self.Sid = params.get("Sid")
        self.Uin = params.get("Uin")
        self.Time = params.get("Time")
        self.ClientIp = params.get("ClientIp")
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.Protocol = params.get("Protocol")
        self.PrivateIp = params.get("PrivateIp")
        self.PublicIp = params.get("PublicIp")
        self.SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPasswordRequest(AbstractModel):
    """BindDeviceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 主机账号ID
        :type Id: int
        :param Password: 主机账号密码
        :type Password: str
        """
        self.Id = None
        self.Password = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPasswordResponse(AbstractModel):
    """BindDeviceAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindDeviceAccountPrivateKeyRequest(AbstractModel):
    """BindDeviceAccountPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 主机账号ID
        :type Id: int
        :param PrivateKey: 主机账号私钥，最新长度128字节，最大长度8192字节
        :type PrivateKey: str
        :param PrivateKeyPassword: 主机账号私钥口令，最大长度256字节
        :type PrivateKeyPassword: str
        """
        self.Id = None
        self.PrivateKey = None
        self.PrivateKeyPassword = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PrivateKey = params.get("PrivateKey")
        self.PrivateKeyPassword = params.get("PrivateKeyPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPrivateKeyResponse(AbstractModel):
    """BindDeviceAccountPrivateKey返回参数结构体

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
        


class Command(AbstractModel):
    """命令集合

    """

    def __init__(self):
        r"""
        :param Cmd: 命令
        :type Cmd: str
        :param Time: 命令输入的时间
        :type Time: str
        :param TimeOffset: 命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :type TimeOffset: int
        :param Action: 命令执行情况，1--允许，2--拒绝，3--确认
        :type Action: int
        :param Sid: 会话id
注意：此字段可能返回 null，表示取不到有效值。
        :type Sid: str
        :param UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param Account: 设备account
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param InstanceId: 设备ip
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param FromIp: source ip
注意：此字段可能返回 null，表示取不到有效值。
        :type FromIp: str
        :param SessTime: 该命令所属会话的会话开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessTime: str
        :param ConfirmTime: 复核时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfirmTime: str
        :param UserDepartmentId: 用户部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDepartmentId: str
        :param UserDepartmentName: 用户部门name
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDepartmentName: str
        :param DeviceDepartmentId: 设备部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceDepartmentId: str
        :param DeviceDepartmentName: 设备部门name
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceDepartmentName: str
        """
        self.Cmd = None
        self.Time = None
        self.TimeOffset = None
        self.Action = None
        self.Sid = None
        self.UserName = None
        self.Account = None
        self.InstanceId = None
        self.FromIp = None
        self.SessTime = None
        self.ConfirmTime = None
        self.UserDepartmentId = None
        self.UserDepartmentName = None
        self.DeviceDepartmentId = None
        self.DeviceDepartmentName = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Time = params.get("Time")
        self.TimeOffset = params.get("TimeOffset")
        self.Action = params.get("Action")
        self.Sid = params.get("Sid")
        self.UserName = params.get("UserName")
        self.Account = params.get("Account")
        self.InstanceId = params.get("InstanceId")
        self.FromIp = params.get("FromIp")
        self.SessTime = params.get("SessTime")
        self.ConfirmTime = params.get("ConfirmTime")
        self.UserDepartmentId = params.get("UserDepartmentId")
        self.UserDepartmentName = params.get("UserDepartmentName")
        self.DeviceDepartmentId = params.get("DeviceDepartmentId")
        self.DeviceDepartmentName = params.get("DeviceDepartmentName")
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
        :param ACTemplateIdSet: 关联高危DB模板ID
        :type ACTemplateIdSet: list of str
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
        self.ACTemplateIdSet = None
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
        self.ACTemplateIdSet = params.get("ACTemplateIdSet")
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


class CreateAssetSyncJobRequest(AbstractModel):
    """CreateAssetSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param Category: 同步资产类别，1 - 主机资产, 2 - 数据库资产
        :type Category: int
        """
        self.Category = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetSyncJobResponse(AbstractModel):
    """CreateAssetSyncJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCmdTemplateRequest(AbstractModel):
    """CreateCmdTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 模板名，最大长度32字符，不能包含空白字符
        :type Name: str
        :param CmdList: 命令列表，\n分隔，最大长度32768字节
        :type CmdList: str
        :param Encoding: 标识cmdlist字段前端是否为base64加密传值.
0:表示非base64加密
1:表示是base64加密
        :type Encoding: int
        """
        self.Name = None
        self.CmdList = None
        self.Encoding = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CmdList = params.get("CmdList")
        self.Encoding = params.get("Encoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmdTemplateResponse(AbstractModel):
    """CreateCmdTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 新建成功后返回的记录ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateDeviceAccountRequest(AbstractModel):
    """CreateDeviceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 主机记录ID
        :type DeviceId: int
        :param Account: 账号名
        :type Account: str
        """
        self.DeviceId = None
        self.Account = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Account = params.get("Account")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceAccountResponse(AbstractModel):
    """CreateDeviceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 新建成功后返回的记录ID
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


class DeleteCmdTemplatesRequest(AbstractModel):
    """DeleteCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的ID集合
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
        


class DeleteCmdTemplatesResponse(AbstractModel):
    """DeleteCmdTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceAccountsRequest(AbstractModel):
    """DeleteDeviceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的ID集合
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
        


class DeleteDeviceAccountsResponse(AbstractModel):
    """DeleteDeviceAccounts返回参数结构体

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


class DeleteDevicesRequest(AbstractModel):
    """DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 待删除的ID集合
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
        


class DeleteDevicesResponse(AbstractModel):
    """DeleteDevices返回参数结构体

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
        


class DeployResourceRequest(AbstractModel):
    """DeployResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 需要开通服务的资源ID
        :type ResourceId: str
        :param ApCode: 需要开通服务的地域
        :type ApCode: str
        :param Zone: 子网所在可用区
        :type Zone: str
        :param VpcId: 需要开通服务的VPC
        :type VpcId: str
        :param SubnetId: 需要开通服务的子网ID
        :type SubnetId: str
        :param CidrBlock: 需要开通服务的子网网段
        :type CidrBlock: str
        :param VpcName: 需要开通服务的VPC名称
        :type VpcName: str
        :param VpcCidrBlock: 需要开通服务的VPC对应的网段
        :type VpcCidrBlock: str
        :param SubnetName: 需要开通服务的子网名称
        :type SubnetName: str
        """
        self.ResourceId = None
        self.ApCode = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.CidrBlock = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ApCode = params.get("ApCode")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CidrBlock = params.get("CidrBlock")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetName = params.get("SubnetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployResourceResponse(AbstractModel):
    """DeployResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAclsRequest(AbstractModel):
    """DescribeAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 访问权限ID集合
        :type IdSet: list of int non-negative
        :param Name: 访问权限名称，模糊查询，最长64字符
        :type Name: str
        :param Offset: 分页偏移位置，默认值为0
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


class DescribeAssetSyncStatusRequest(AbstractModel):
    """DescribeAssetSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Category: 查询的资产同步类型。1 -主机资产， 2 - 数据库资产
        :type Category: int
        """
        self.Category = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetSyncStatusResponse(AbstractModel):
    """DescribeAssetSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 资产同步结果
        :type Status: :class:`tencentcloud.dasb.v20191018.models.AssetSyncStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self.Status = AssetSyncStatus()
            self.Status._deserialize(params.get("Status"))
        self.RequestId = params.get("RequestId")


class DescribeCmdTemplatesRequest(AbstractModel):
    """DescribeCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 命令模板ID集合，非必需
        :type IdSet: list of int non-negative
        :param Name: 命令模板名，模糊查询，最大长度64字符
        :type Name: str
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmdTemplatesResponse(AbstractModel):
    """DescribeCmdTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param CmdTemplateSet: 命令模板列表
        :type CmdTemplateSet: list of CmdTemplate
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CmdTemplateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CmdTemplateSet") is not None:
            self.CmdTemplateSet = []
            for item in params.get("CmdTemplateSet"):
                obj = CmdTemplate()
                obj._deserialize(item)
                self.CmdTemplateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
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


class DescribeDeviceAccountsRequest(AbstractModel):
    """DescribeDeviceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 主机账号ID集合，非必需，如果使用IdSet则忽略其他过滤参数
        :type IdSet: list of int non-negative
        :param Account: 主机账号名，模糊查询，不能单独出现，必须于DeviceId一起提交
        :type Account: str
        :param DeviceId: 主机ID，未使用IdSet时必须携带
        :type DeviceId: int
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self.IdSet = None
        self.Account = None
        self.DeviceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Account = params.get("Account")
        self.DeviceId = params.get("DeviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceAccountsResponse(AbstractModel):
    """DescribeDeviceAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param DeviceAccountSet: 账号信息列表
        :type DeviceAccountSet: list of DeviceAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceAccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceAccountSet") is not None:
            self.DeviceAccountSet = []
            for item in params.get("DeviceAccountSet"):
                obj = DeviceAccount()
                obj._deserialize(item)
                self.DeviceAccountSet.append(obj)
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
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 每页条目数，默认20, 最大500
        :type Limit: int
        :param Kind: 资产类型，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :type Kind: int
        :param DepartmentId: 所属部门ID
        :type DepartmentId: str
        :param TagFilters: 过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :type TagFilters: list of TagFilter
        """
        self.Id = None
        self.Bound = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.Kind = None
        self.DepartmentId = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Bound = params.get("Bound")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Kind = params.get("Kind")
        self.DepartmentId = params.get("DepartmentId")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
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
        :param Offset: 分页偏移位置，默认值为0
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
        :param Offset: 分页偏移位置，默认值为0
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
        :param TagFilters: 过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :type TagFilters: list of TagFilter
        :param Filters: 过滤数组。支持的Name：
BindingStatus 绑定状态
        :type Filters: list of Filter
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
        self.TagFilters = None
        self.Filters = None


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
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
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


class DescribeLoginEventRequest(AbstractModel):
    """DescribeLoginEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserName: 用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :type UserName: str
        :param RealName: 姓名，模糊查询
        :type RealName: str
        :param StartTime: 查询时间范围，起始时间
        :type StartTime: str
        :param EndTime: 查询时间范围，结束时间
        :type EndTime: str
        :param SourceIp: 来源IP，模糊查询
        :type SourceIp: str
        :param Entry: 登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :type Entry: int
        :param Result: 操作结果，1-成功，2-失败
        :type Result: int
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 分页每页记录数，默认20
        :type Limit: int
        """
        self.UserName = None
        self.RealName = None
        self.StartTime = None
        self.EndTime = None
        self.SourceIp = None
        self.Entry = None
        self.Result = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SourceIp = params.get("SourceIp")
        self.Entry = params.get("Entry")
        self.Result = params.get("Result")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginEventResponse(AbstractModel):
    """DescribeLoginEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoginEventSet: 登录日志列表
        :type LoginEventSet: list of LoginEvent
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginEventSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginEventSet") is not None:
            self.LoginEventSet = []
            for item in params.get("LoginEventSet"):
                obj = LoginEvent()
                obj._deserialize(item)
                self.LoginEventSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOperationEventRequest(AbstractModel):
    """DescribeOperationEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserName: 用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :type UserName: str
        :param RealName: 姓名，模糊查询
        :type RealName: str
        :param StartTime: 查询时间范围，起始时间
        :type StartTime: str
        :param EndTime: 查询时间范围，结束时间
        :type EndTime: str
        :param SourceIp: 来源IP，模糊查询
        :type SourceIp: str
        :param Kind: 操作类型，参考DescribeOperationType返回结果
        :type Kind: int
        :param Result: 操作结果，1-成功，2-失败
        :type Result: int
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 分页每页记录数，默认20
        :type Limit: int
        """
        self.UserName = None
        self.RealName = None
        self.StartTime = None
        self.EndTime = None
        self.SourceIp = None
        self.Kind = None
        self.Result = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SourceIp = params.get("SourceIp")
        self.Kind = params.get("Kind")
        self.Result = params.get("Result")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOperationEventResponse(AbstractModel):
    """DescribeOperationEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param OperationEventSet: 操作日志列表
        :type OperationEventSet: list of OperationEvent
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OperationEventSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OperationEventSet") is not None:
            self.OperationEventSet = []
            for item in params.get("OperationEventSet"):
                obj = OperationEvent()
                obj._deserialize(item)
                self.OperationEventSet.append(obj)
        self.TotalCount = params.get("TotalCount")
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
        :param Offset: 分页偏移位置，默认值为0
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
        :param Offset: 分页偏移位置，默认值为0
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
        :param Offset: 分页偏移位置，默认值为0
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
        


class DeviceAccount(AbstractModel):
    """主机账号

    """

    def __init__(self):
        r"""
        :param Id: 账号ID
        :type Id: int
        :param DeviceId: 主机ID
        :type DeviceId: int
        :param Account: 账号名
        :type Account: str
        :param BoundPassword: true-已托管密码，false-未托管密码
        :type BoundPassword: bool
        :param BoundPrivateKey: true-已托管私钥，false-未托管私钥
        :type BoundPrivateKey: bool
        """
        self.Id = None
        self.DeviceId = None
        self.Account = None
        self.BoundPassword = None
        self.BoundPrivateKey = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DeviceId = params.get("DeviceId")
        self.Account = params.get("Account")
        self.BoundPassword = params.get("BoundPassword")
        self.BoundPrivateKey = params.get("BoundPrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalDevice(AbstractModel):
    """主机参数，导入外部主机时使用

    """

    def __init__(self):
        r"""
        :param OsName: 操作系统名称，只能是Linux、Windows或MySQL
        :type OsName: str
        :param Ip: IP地址
        :type Ip: str
        :param Port: 管理端口
        :type Port: int
        :param Name: 主机名，可为空
        :type Name: str
        :param DepartmentId: 资产所属的部门ID
        :type DepartmentId: str
        """
        self.OsName = None
        self.Ip = None
        self.Port = None
        self.Name = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Name = params.get("Name")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
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
        :param Count: 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.Id = None
        self.Name = None
        self.Department = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportExternalDeviceRequest(AbstractModel):
    """ImportExternalDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceSet: 资产参数列表
        :type DeviceSet: list of ExternalDevice
        """
        self.DeviceSet = None


    def _deserialize(self, params):
        if params.get("DeviceSet") is not None:
            self.DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = ExternalDevice()
                obj._deserialize(item)
                self.DeviceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportExternalDeviceResponse(AbstractModel):
    """ImportExternalDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class LoginEvent(AbstractModel):
    """登录日志

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param Time: 操作时间
        :type Time: str
        :param SourceIp: 来源IP
        :type SourceIp: str
        :param Entry: 登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :type Entry: int
        :param Result: 操作结果，1-成功，2-失败
        :type Result: int
        """
        self.UserName = None
        self.RealName = None
        self.Time = None
        self.SourceIp = None
        self.Entry = None
        self.Result = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.Time = params.get("Time")
        self.SourceIp = params.get("SourceIp")
        self.Entry = params.get("Entry")
        self.Result = params.get("Result")
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
        :param ACTemplateIdSet: 关联高危DB模板ID
        :type ACTemplateIdSet: list of str
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
        self.ACTemplateIdSet = None
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
        self.ACTemplateIdSet = params.get("ACTemplateIdSet")
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


class ModifyDeviceGroupRequest(AbstractModel):
    """ModifyDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 资产组名，最大长度32字符，不能为空
        :type Name: str
        :param Id: 资产组ID
        :type Id: int
        :param DepartmentId: 资产组所属部门ID，如：1.2.3
        :type DepartmentId: str
        """
        self.Name = None
        self.Id = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceGroupResponse(AbstractModel):
    """ModifyDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 资产记录ID
        :type Id: int
        :param Port: 管理端口
        :type Port: int
        :param GroupIdSet: 资产所属组ID集合
        :type GroupIdSet: list of int non-negative
        :param DepartmentId: 资产所属部门ID
        :type DepartmentId: str
        """
        self.Id = None
        self.Port = None
        self.GroupIdSet = None
        self.DepartmentId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Port = params.get("Port")
        self.GroupIdSet = params.get("GroupIdSet")
        self.DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

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


class OperationEvent(AbstractModel):
    """操作日志

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param Time: 操作时间
        :type Time: str
        :param SourceIp: 来源IP
        :type SourceIp: str
        :param Kind: 操作类型
        :type Kind: int
        :param Operation: 具体操作内容
        :type Operation: str
        :param Result: 操作结果，1-成功，2-失败
        :type Result: int
        """
        self.UserName = None
        self.RealName = None
        self.Time = None
        self.SourceIp = None
        self.Kind = None
        self.Operation = None
        self.Result = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.Time = params.get("Time")
        self.SourceIp = params.get("SourceIp")
        self.Kind = params.get("Kind")
        self.Operation = params.get("Operation")
        self.Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceAccountPasswordRequest(AbstractModel):
    """ResetDeviceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: ID集合
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
        


class ResetDeviceAccountPasswordResponse(AbstractModel):
    """ResetDeviceAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceAccountPrivateKeyRequest(AbstractModel):
    """ResetDeviceAccountPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: ID集合
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
        


class ResetDeviceAccountPrivateKeyResponse(AbstractModel):
    """ResetDeviceAccountPrivateKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetUserRequest(AbstractModel):
    """ResetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 用户ID集合
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
        


class ResetUserResponse(AbstractModel):
    """ResetUser返回参数结构体

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
        :param LogDeliveryArgs: 日志投递规格信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LogDeliveryArgs: str
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
        self.LogDeliveryArgs = None


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
        self.LogDeliveryArgs = params.get("LogDeliveryArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAuditLogRequest(AbstractModel):
    """SearchAuditLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间，不得早于当前时间的180天前
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每页容量，默认为20，最大200
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAuditLogResponse(AbstractModel):
    """SearchAuditLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuditLogSet: 审计日志
        :type AuditLogSet: list of AuditLogResult
        :param TotalCount: 日志总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuditLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuditLogSet") is not None:
            self.AuditLogSet = []
            for item in params.get("AuditLogSet"):
                obj = AuditLogResult()
                obj._deserialize(item)
                self.AuditLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SearchCommandBySidRequest(AbstractModel):
    """SearchCommandBySid请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sid: 会话Id
        :type Sid: str
        :param Cmd: 命令，可模糊搜索
        :type Cmd: str
        :param Encoding: Cmd字段是前端传值是否进行base64.
0:否，1：是
        :type Encoding: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每页容量，默认20，最大200
        :type Limit: int
        :param AuditAction: 根据拦截状态进行过滤
        :type AuditAction: list of int non-negative
        """
        self.Sid = None
        self.Cmd = None
        self.Encoding = None
        self.Offset = None
        self.Limit = None
        self.AuditAction = None


    def _deserialize(self, params):
        self.Sid = params.get("Sid")
        self.Cmd = params.get("Cmd")
        self.Encoding = params.get("Encoding")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AuditAction = params.get("AuditAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCommandBySidResponse(AbstractModel):
    """SearchCommandBySid返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param CommandSet: 命令列表
        :type CommandSet: list of Command
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CommandSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CommandSet") is not None:
            self.CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self.CommandSet.append(obj)
        self.RequestId = params.get("RequestId")


class SearchCommandRequest(AbstractModel):
    """SearchCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 搜索区间的开始时间
        :type StartTime: str
        :param EndTime: 搜索区间的结束时间，不填默认为开始时间到现在为止
        :type EndTime: str
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param InstanceId: 资产实例ID
        :type InstanceId: str
        :param DeviceName: 资产名称
        :type DeviceName: str
        :param PublicIp: 资产的公网IP
        :type PublicIp: str
        :param PrivateIp: 资产的内网IP
        :type PrivateIp: str
        :param Cmd: 执行的命令
        :type Cmd: str
        :param Encoding: Cmd字段是前端传值是否进行base64.
0:否，1：是
        :type Encoding: int
        :param AuditAction: 根据拦截状态进行过滤：1 - 已执行，2 - 被阻断
        :type AuditAction: list of int non-negative
        :param Limit: 每页容量，默认20，最大200
        :type Limit: int
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.UserName = None
        self.RealName = None
        self.InstanceId = None
        self.DeviceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Cmd = None
        self.Encoding = None
        self.AuditAction = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Cmd = params.get("Cmd")
        self.Encoding = params.get("Encoding")
        self.AuditAction = params.get("AuditAction")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCommandResponse(AbstractModel):
    """SearchCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Commands: 命令列表
        :type Commands: list of SearchCommandResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Commands = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Commands") is not None:
            self.Commands = []
            for item in params.get("Commands"):
                obj = SearchCommandResult()
                obj._deserialize(item)
                self.Commands.append(obj)
        self.RequestId = params.get("RequestId")


class SearchCommandResult(AbstractModel):
    """命令执行检索结果

    """

    def __init__(self):
        r"""
        :param Time: 命令输入的时间
        :type Time: str
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param InstanceId: 资产ID
        :type InstanceId: str
        :param DeviceName: 资产名称
        :type DeviceName: str
        :param PublicIp: 资产公网IP
        :type PublicIp: str
        :param PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param Cmd: 命令
        :type Cmd: str
        :param Action: 命令执行情况，1--允许，2--拒绝
        :type Action: int
        :param Sid: 命令所属的会话ID
        :type Sid: str
        :param TimeOffset: 命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :type TimeOffset: int
        :param Account: 账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param FromIp: source ip
注意：此字段可能返回 null，表示取不到有效值。
        :type FromIp: str
        :param SessTime: 该命令所属会话的会话开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessTime: str
        :param ConfirmTime: 复核时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfirmTime: str
        :param UserDepartmentId: 部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDepartmentId: str
        :param UserDepartmentName: 用户部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDepartmentName: str
        :param DeviceDepartmentId: 设备部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceDepartmentId: str
        :param DeviceDepartmentName: 设备部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceDepartmentName: str
        """
        self.Time = None
        self.UserName = None
        self.RealName = None
        self.InstanceId = None
        self.DeviceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Cmd = None
        self.Action = None
        self.Sid = None
        self.TimeOffset = None
        self.Account = None
        self.FromIp = None
        self.SessTime = None
        self.ConfirmTime = None
        self.UserDepartmentId = None
        self.UserDepartmentName = None
        self.DeviceDepartmentId = None
        self.DeviceDepartmentName = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Cmd = params.get("Cmd")
        self.Action = params.get("Action")
        self.Sid = params.get("Sid")
        self.TimeOffset = params.get("TimeOffset")
        self.Account = params.get("Account")
        self.FromIp = params.get("FromIp")
        self.SessTime = params.get("SessTime")
        self.ConfirmTime = params.get("ConfirmTime")
        self.UserDepartmentId = params.get("UserDepartmentId")
        self.UserDepartmentName = params.get("UserDepartmentName")
        self.DeviceDepartmentId = params.get("DeviceDepartmentId")
        self.DeviceDepartmentName = params.get("DeviceDepartmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileBySidRequest(AbstractModel):
    """SearchFileBySid请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sid: 若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :type Sid: str
        :param AuditLog: 是否创建审计日志,通过查看按钮调用时为true,其他为false
        :type AuditLog: bool
        :param Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param FileName: 可填写路径名或文件名
        :type FileName: str
        :param Offset: 分页用偏移量
        :type Offset: int
        :param AuditAction: 1-已执行，  2-被阻断
        :type AuditAction: int
        :param TypeFilters: 以Protocol和Method为条件查询
        :type TypeFilters: list of SearchFileTypeFilter
        """
        self.Sid = None
        self.AuditLog = None
        self.Limit = None
        self.FileName = None
        self.Offset = None
        self.AuditAction = None
        self.TypeFilters = None


    def _deserialize(self, params):
        self.Sid = params.get("Sid")
        self.AuditLog = params.get("AuditLog")
        self.Limit = params.get("Limit")
        self.FileName = params.get("FileName")
        self.Offset = params.get("Offset")
        self.AuditAction = params.get("AuditAction")
        if params.get("TypeFilters") is not None:
            self.TypeFilters = []
            for item in params.get("TypeFilters"):
                obj = SearchFileTypeFilter()
                obj._deserialize(item)
                self.TypeFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileBySidResponse(AbstractModel):
    """SearchFileBySid返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
        :type TotalCount: int
        :param SearchFileBySidResult: 某会话的文件操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchFileBySidResult: list of SearchFileBySidResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SearchFileBySidResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SearchFileBySidResult") is not None:
            self.SearchFileBySidResult = []
            for item in params.get("SearchFileBySidResult"):
                obj = SearchFileBySidResult()
                obj._deserialize(item)
                self.SearchFileBySidResult.append(obj)
        self.RequestId = params.get("RequestId")


class SearchFileBySidResult(AbstractModel):
    """文件操作搜索结果

    """

    def __init__(self):
        r"""
        :param Time: 文件操作时间
        :type Time: str
        :param Method: 1-上传文件 2-下载文件 3-删除文件 4-移动文件 5-重命名文件 6-新建文件夹 7-移动文件夹 8-重命名文件夹 9-删除文件夹
        :type Method: int
        :param Protocol: 文件传输协议
        :type Protocol: str
        :param FileCurr: method为上传、下载、删除时文件在服务器上的位置, 或重命名、移动文件前文件的位置
        :type FileCurr: str
        :param FileNew: method为重命名、移动文件时代表移动后的新位置.其他情况为null
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNew: str
        :param Size: method为上传文件、下载文件、删除文件时显示文件大小。其他情况为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Action: 堡垒机拦截情况, 1-已执行，  2-被阻断
        :type Action: int
        """
        self.Time = None
        self.Method = None
        self.Protocol = None
        self.FileCurr = None
        self.FileNew = None
        self.Size = None
        self.Action = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Method = params.get("Method")
        self.Protocol = params.get("Protocol")
        self.FileCurr = params.get("FileCurr")
        self.FileNew = params.get("FileNew")
        self.Size = params.get("Size")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileRequest(AbstractModel):
    """SearchFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param InstanceId: 资产ID
        :type InstanceId: str
        :param DeviceName: 资产名称
        :type DeviceName: str
        :param PublicIp: 资产公网IP
        :type PublicIp: str
        :param PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param Method: 操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :type Method: list of int non-negative
        :param FileName: 可填写路径名或文件（夹）名
        :type FileName: str
        :param AuditAction: 1-已执行，  2-被阻断
        :type AuditAction: list of int non-negative
        :param Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.UserName = None
        self.RealName = None
        self.InstanceId = None
        self.DeviceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Method = None
        self.FileName = None
        self.AuditAction = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Method = params.get("Method")
        self.FileName = params.get("FileName")
        self.AuditAction = params.get("AuditAction")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileResponse(AbstractModel):
    """SearchFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
        :type TotalCount: int
        :param Files: 文件操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Files: list of SearchFileResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = SearchFileResult()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class SearchFileResult(AbstractModel):
    """文件传输检索结果

    """

    def __init__(self):
        r"""
        :param Time: 文件传输的时间
        :type Time: str
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param InstanceId: 资产ID
        :type InstanceId: str
        :param DeviceName: 资产名称
        :type DeviceName: str
        :param PublicIp: 资产公网IP
        :type PublicIp: str
        :param PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param Action: 操作结果：1 - 已执行，2 - 已阻断
        :type Action: int
        :param Method: 操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :type Method: int
        :param FileCurr: 下载的文件（夹）路径及名称
        :type FileCurr: str
        :param FileNew: 上传或新建文件（夹）路径及名称
        :type FileNew: str
        """
        self.Time = None
        self.UserName = None
        self.RealName = None
        self.InstanceId = None
        self.DeviceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Action = None
        self.Method = None
        self.FileCurr = None
        self.FileNew = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Action = params.get("Action")
        self.Method = params.get("Method")
        self.FileCurr = params.get("FileCurr")
        self.FileNew = params.get("FileNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileTypeFilter(AbstractModel):
    """用于搜索文件传输记录等日志时按照protocol和method进行过滤

    """

    def __init__(self):
        r"""
        :param Protocol: 需要查询的文件传输类型，如SFTP/CLIP/RDP/RZSZ
        :type Protocol: str
        :param Method: 在当前指定的protocol下进一步过滤具体操作类型,如剪贴板文件上传，剪贴板文件下载等
        :type Method: list of int
        """
        self.Protocol = None
        self.Method = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionCommandRequest(AbstractModel):
    """SearchSessionCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param Cmd: 检索的目标命令，为模糊搜索
        :type Cmd: str
        :param StartTime: 开始时间，不得早于当前时间的180天前
        :type StartTime: str
        :param Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param Limit: 默认值为20，最大200
        :type Limit: int
        :param Encoding: Cmd字段前端是否做base64加密
0：否，1：是
        :type Encoding: int
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Cmd = None
        self.StartTime = None
        self.Offset = None
        self.Limit = None
        self.Encoding = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.StartTime = params.get("StartTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Encoding = params.get("Encoding")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionCommandResponse(AbstractModel):
    """SearchSessionCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param CommandSessionSet: 命令和所属会话
        :type CommandSessionSet: list of SessionCommand
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CommandSessionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CommandSessionSet") is not None:
            self.CommandSessionSet = []
            for item in params.get("CommandSessionSet"):
                obj = SessionCommand()
                obj._deserialize(item)
                self.CommandSessionSet.append(obj)
        self.RequestId = params.get("RequestId")


class SearchSessionRequest(AbstractModel):
    """SearchSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param PrivateIp: 内部Ip
        :type PrivateIp: str
        :param PublicIp: 外部Ip
        :type PublicIp: str
        :param UserName: 用户名，长度不超过20
        :type UserName: str
        :param Account: 账号，长度不超过64
        :type Account: str
        :param FromIp: 来源Ip
        :type FromIp: str
        :param StartTime: 搜索区间的开始时间。若入参是Id，则非必传，否则为必传。
        :type StartTime: str
        :param EndTime: 搜索区间的结束时间
        :type EndTime: str
        :param Kind: 会话协议类型，只能是1、2、3或4 对应关系为1-tui 2-gui 3-file 4-数据库。若入参是Id，则非必传，否则为必传。
        :type Kind: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param RealName: 姓名，长度不超过20
        :type RealName: str
        :param DeviceName: 主机名，长度不超过64
        :type DeviceName: str
        :param Status: 状态，1为活跃，2为结束，3为强制离线，4为其他错误
        :type Status: int
        :param Id: 若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :type Id: str
        """
        self.PrivateIp = None
        self.PublicIp = None
        self.UserName = None
        self.Account = None
        self.FromIp = None
        self.StartTime = None
        self.EndTime = None
        self.Kind = None
        self.Offset = None
        self.Limit = None
        self.RealName = None
        self.DeviceName = None
        self.Status = None
        self.Id = None


    def _deserialize(self, params):
        self.PrivateIp = params.get("PrivateIp")
        self.PublicIp = params.get("PublicIp")
        self.UserName = params.get("UserName")
        self.Account = params.get("Account")
        self.FromIp = params.get("FromIp")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Kind = params.get("Kind")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RealName = params.get("RealName")
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionResponse(AbstractModel):
    """SearchSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数
        :type TotalCount: int
        :param SessionSet: 会话信息列表
        :type SessionSet: list of SessionResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SessionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SessionSet") is not None:
            self.SessionSet = []
            for item in params.get("SessionSet"):
                obj = SessionResult()
                obj._deserialize(item)
                self.SessionSet.append(obj)
        self.RequestId = params.get("RequestId")


class SessionCommand(AbstractModel):
    """命令和所属会话

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 账号
        :type RealName: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param PrivateIp: 内部Ip
        :type PrivateIp: str
        :param PublicIp: 外部Ip
        :type PublicIp: str
        :param Commands: 命令列表
        :type Commands: list of Command
        :param Count: 记录数
        :type Count: int
        :param Id: 会话Id
        :type Id: str
        :param InstanceId: 设备id
        :type InstanceId: str
        :param ApCode: 设备所属的地域
        :type ApCode: str
        """
        self.StartTime = None
        self.EndTime = None
        self.UserName = None
        self.RealName = None
        self.DeviceName = None
        self.PrivateIp = None
        self.PublicIp = None
        self.Commands = None
        self.Count = None
        self.Id = None
        self.InstanceId = None
        self.ApCode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.DeviceName = params.get("DeviceName")
        self.PrivateIp = params.get("PrivateIp")
        self.PublicIp = params.get("PublicIp")
        if params.get("Commands") is not None:
            self.Commands = []
            for item in params.get("Commands"):
                obj = Command()
                obj._deserialize(item)
                self.Commands.append(obj)
        self.Count = params.get("Count")
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.ApCode = params.get("ApCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionResult(AbstractModel):
    """搜索字符或图形会话时返回的SessionResul结构体

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 姓名
        :type RealName: str
        :param Account: 主机账号
        :type Account: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Size: 会话大小
        :type Size: int
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        :param PrivateIp: 内部Ip
        :type PrivateIp: str
        :param PublicIp: 外部Ip
        :type PublicIp: str
        :param FromIp: 来源Ip
        :type FromIp: str
        :param Duration: 会话持续时长
        :type Duration: float
        :param Count: 该会话内命令数量 ，搜索图形会话时该字段无意义
        :type Count: int
        :param DangerCount: 该会话内高危命令数，搜索图形时该字段无意义
        :type DangerCount: int
        :param Status: 会话状态，如1会话活跃  2会话结束  3强制离线  4其他错误
        :type Status: int
        :param Id: 会话Id
        :type Id: str
        :param ApCode: 设备所属的地域
        :type ApCode: str
        :param Protocol: 会话协议
        :type Protocol: str
        """
        self.UserName = None
        self.RealName = None
        self.Account = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.InstanceId = None
        self.DeviceName = None
        self.PrivateIp = None
        self.PublicIp = None
        self.FromIp = None
        self.Duration = None
        self.Count = None
        self.DangerCount = None
        self.Status = None
        self.Id = None
        self.ApCode = None
        self.Protocol = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.RealName = params.get("RealName")
        self.Account = params.get("Account")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.InstanceId = params.get("InstanceId")
        self.DeviceName = params.get("DeviceName")
        self.PrivateIp = params.get("PrivateIp")
        self.PublicIp = params.get("PublicIp")
        self.FromIp = params.get("FromIp")
        self.Duration = params.get("Duration")
        self.Count = params.get("Count")
        self.DangerCount = params.get("DangerCount")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        self.ApCode = params.get("ApCode")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """资产标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
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
        