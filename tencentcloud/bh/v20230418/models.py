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


class ACTemplate(AbstractModel):
    r"""权限控制模板对象

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _Description: 模板描述
        :type Description: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None

    @property
    def TemplateId(self):
        r"""模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        r"""模板描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessDevicesRequest(AbstractModel):
    r"""AccessDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 资产的登录账号
        :type Account: str
        :param _LoginAccount: 运维端登录账号
        :type LoginAccount: str
        :param _LoginPassword: 运维端登录密码
        :type LoginPassword: str
        :param _DeviceId: 资产ID
        :type DeviceId: int
        :param _InstanceId: 资源id(优先使用DeviceId)
        :type InstanceId: str
        :param _Password: 未托管密码私钥时，填入
        :type Password: str
        :param _PrivateKey: 未托管密码私钥时，填入
        :type PrivateKey: str
        :param _PrivateKeyPassword: 未托管密码私钥时，填入
        :type PrivateKeyPassword: str
        :param _Exe: 客户端工具
        :type Exe: str
        :param _Drivers: RDP挂载盘符驱动（mstsc支持）
        :type Drivers: list of str
        :param _Width: 窗口宽度（RDP支持）
        :type Width: int
        :param _Height: 窗口高度（RDP支持）
        :type Height: int
        :param _IntranetAccess: 是否内网访问（默认不是）
        :type IntranetAccess: bool
        :param _AutoManageAccessCredential: 是否自动管理访问串，删掉过期的，新建可用的（默认false）
        :type AutoManageAccessCredential: bool
        """
        self._Account = None
        self._LoginAccount = None
        self._LoginPassword = None
        self._DeviceId = None
        self._InstanceId = None
        self._Password = None
        self._PrivateKey = None
        self._PrivateKeyPassword = None
        self._Exe = None
        self._Drivers = None
        self._Width = None
        self._Height = None
        self._IntranetAccess = None
        self._AutoManageAccessCredential = None

    @property
    def Account(self):
        r"""资产的登录账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def LoginAccount(self):
        warnings.warn("parameter `LoginAccount` is deprecated", DeprecationWarning) 

        r"""运维端登录账号
        :rtype: str
        """
        return self._LoginAccount

    @LoginAccount.setter
    def LoginAccount(self, LoginAccount):
        warnings.warn("parameter `LoginAccount` is deprecated", DeprecationWarning) 

        self._LoginAccount = LoginAccount

    @property
    def LoginPassword(self):
        warnings.warn("parameter `LoginPassword` is deprecated", DeprecationWarning) 

        r"""运维端登录密码
        :rtype: str
        """
        return self._LoginPassword

    @LoginPassword.setter
    def LoginPassword(self, LoginPassword):
        warnings.warn("parameter `LoginPassword` is deprecated", DeprecationWarning) 

        self._LoginPassword = LoginPassword

    @property
    def DeviceId(self):
        r"""资产ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def InstanceId(self):
        r"""资源id(优先使用DeviceId)
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        r"""未托管密码私钥时，填入
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PrivateKey(self):
        r"""未托管密码私钥时，填入
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def PrivateKeyPassword(self):
        r"""未托管密码私钥时，填入
        :rtype: str
        """
        return self._PrivateKeyPassword

    @PrivateKeyPassword.setter
    def PrivateKeyPassword(self, PrivateKeyPassword):
        self._PrivateKeyPassword = PrivateKeyPassword

    @property
    def Exe(self):
        r"""客户端工具
        :rtype: str
        """
        return self._Exe

    @Exe.setter
    def Exe(self, Exe):
        self._Exe = Exe

    @property
    def Drivers(self):
        r"""RDP挂载盘符驱动（mstsc支持）
        :rtype: list of str
        """
        return self._Drivers

    @Drivers.setter
    def Drivers(self, Drivers):
        self._Drivers = Drivers

    @property
    def Width(self):
        r"""窗口宽度（RDP支持）
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""窗口高度（RDP支持）
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def IntranetAccess(self):
        r"""是否内网访问（默认不是）
        :rtype: bool
        """
        return self._IntranetAccess

    @IntranetAccess.setter
    def IntranetAccess(self, IntranetAccess):
        self._IntranetAccess = IntranetAccess

    @property
    def AutoManageAccessCredential(self):
        r"""是否自动管理访问串，删掉过期的，新建可用的（默认false）
        :rtype: bool
        """
        return self._AutoManageAccessCredential

    @AutoManageAccessCredential.setter
    def AutoManageAccessCredential(self, AutoManageAccessCredential):
        self._AutoManageAccessCredential = AutoManageAccessCredential


    def _deserialize(self, params):
        self._Account = params.get("Account")
        self._LoginAccount = params.get("LoginAccount")
        self._LoginPassword = params.get("LoginPassword")
        self._DeviceId = params.get("DeviceId")
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._PrivateKey = params.get("PrivateKey")
        self._PrivateKeyPassword = params.get("PrivateKeyPassword")
        self._Exe = params.get("Exe")
        self._Drivers = params.get("Drivers")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._IntranetAccess = params.get("IntranetAccess")
        self._AutoManageAccessCredential = params.get("AutoManageAccessCredential")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessDevicesResponse(AbstractModel):
    r"""AccessDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessInfo: 认证信息
        :type AccessInfo: :class:`tencentcloud.bh.v20230418.models.AccessInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessInfo = None
        self._RequestId = None

    @property
    def AccessInfo(self):
        r"""认证信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.AccessInfo`
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

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
        if params.get("AccessInfo") is not None:
            self._AccessInfo = AccessInfo()
            self._AccessInfo._deserialize(params.get("AccessInfo"))
        self._RequestId = params.get("RequestId")


class AccessInfo(AbstractModel):
    r"""认证信息

    """

    def __init__(self):
        r"""
        :param _Ip: 地址
        :type Ip: str
        :param _Port: 端口
        :type Port: int
        :param _User: 账号
        :type User: str
        :param _Password: 密码
        :type Password: str
        :param _AccessURL: 唤起链接｜wss链接
        :type AccessURL: str
        """
        self._Ip = None
        self._Port = None
        self._User = None
        self._Password = None
        self._AccessURL = None

    @property
    def Ip(self):
        r"""地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        r"""账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

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
    def AccessURL(self):
        r"""唤起链接｜wss链接
        :rtype: str
        """
        return self._AccessURL

    @AccessURL.setter
    def AccessURL(self, AccessURL):
        self._AccessURL = AccessURL


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._AccessURL = params.get("AccessURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessWhiteListRule(AbstractModel):
    r"""访问白名单规则

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _Source: IP或者网段
        :type Source: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._Id = None
        self._Source = None
        self._Remark = None
        self._ModifyTime = None

    @property
    def Id(self):
        r"""规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Source(self):
        r"""IP或者网段
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ModifyTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Source = params.get("Source")
        self._Remark = params.get("Remark")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroup(AbstractModel):
    r"""ioa账号组

    """

    def __init__(self):
        r"""
        :param _Id: 账号组id
        :type Id: int
        :param _Name: 账号组名称
        :type Name: str
        :param _IdPath: 账号组id路径
        :type IdPath: str
        :param _NamePath: 账号组名称路径
        :type NamePath: str
        :param _ParentId: 父账号组id
        :type ParentId: int
        :param _Source: 账号组来源
        :type Source: int
        :param _UserTotal: 账号组下用户总数
        :type UserTotal: int
        :param _IsLeaf: 是否叶子节点
        :type IsLeaf: bool
        :param _ImportType: 账号组导入类型
        :type ImportType: str
        :param _Description: 账号组描述
        :type Description: str
        :param _ParentOrgId: 父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type ParentOrgId: str
        :param _OrgId: 源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :type OrgId: str
        :param _Status: 账号组是否已经接入，0表示未接入，1表示接入
        :type Status: int
        """
        self._Id = None
        self._Name = None
        self._IdPath = None
        self._NamePath = None
        self._ParentId = None
        self._Source = None
        self._UserTotal = None
        self._IsLeaf = None
        self._ImportType = None
        self._Description = None
        self._ParentOrgId = None
        self._OrgId = None
        self._Status = None

    @property
    def Id(self):
        r"""账号组id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""账号组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdPath(self):
        r"""账号组id路径
        :rtype: str
        """
        return self._IdPath

    @IdPath.setter
    def IdPath(self, IdPath):
        self._IdPath = IdPath

    @property
    def NamePath(self):
        r"""账号组名称路径
        :rtype: str
        """
        return self._NamePath

    @NamePath.setter
    def NamePath(self, NamePath):
        self._NamePath = NamePath

    @property
    def ParentId(self):
        r"""父账号组id
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Source(self):
        r"""账号组来源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UserTotal(self):
        r"""账号组下用户总数
        :rtype: int
        """
        return self._UserTotal

    @UserTotal.setter
    def UserTotal(self, UserTotal):
        self._UserTotal = UserTotal

    @property
    def IsLeaf(self):
        r"""是否叶子节点
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def ImportType(self):
        r"""账号组导入类型
        :rtype: str
        """
        return self._ImportType

    @ImportType.setter
    def ImportType(self, ImportType):
        self._ImportType = ImportType

    @property
    def Description(self):
        r"""账号组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParentOrgId(self):
        r"""父源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._ParentOrgId

    @ParentOrgId.setter
    def ParentOrgId(self, ParentOrgId):
        self._ParentOrgId = ParentOrgId

    @property
    def OrgId(self):
        r"""源账号组织ID。使用第三方导入用户源时，记录该分组在源组织架构下的分组ID
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Status(self):
        r"""账号组是否已经接入，0表示未接入，1表示接入
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._IdPath = params.get("IdPath")
        self._NamePath = params.get("NamePath")
        self._ParentId = params.get("ParentId")
        self._Source = params.get("Source")
        self._UserTotal = params.get("UserTotal")
        self._IsLeaf = params.get("IsLeaf")
        self._ImportType = params.get("ImportType")
        self._Description = params.get("Description")
        self._ParentOrgId = params.get("ParentOrgId")
        self._OrgId = params.get("OrgId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Acl(AbstractModel):
    r"""访问权限

    """

    def __init__(self):
        r"""
        :param _Id: 访问权限ID
        :type Id: int
        :param _Name: 访问权限名称
        :type Name: str
        :param _AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param _AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param _AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param _AllowClipTextUp: 是否开启剪贴板文本（目前含图片）上行
        :type AllowClipTextUp: bool
        :param _AllowClipTextDown: 是否开启剪贴板文本（目前含图片）下行
        :type AllowClipTextDown: bool
        :param _AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param _MaxFileUpSize: 文件传输上传大小限制（预留参数，暂未启用）
        :type MaxFileUpSize: int
        :param _AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param _MaxFileDownSize: 文件传输下载大小限制（预留参数，暂未启用）
        :type MaxFileDownSize: int
        :param _AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param _UserSet: 关联的用户列表
        :type UserSet: list of User
        :param _UserGroupSet: 关联的用户组列表
        :type UserGroupSet: list of Group
        :param _DeviceSet: 关联的资产列表
        :type DeviceSet: list of Device
        :param _DeviceGroupSet: 关联的资产组列表
        :type DeviceGroupSet: list of Group
        :param _AccountSet: 关联的账号列表
        :type AccountSet: list of str
        :param _CmdTemplateSet: 关联的高危命令模板列表
        :type CmdTemplateSet: list of CmdTemplate
        :param _AllowDiskFileUp: 是否开启 RDP 磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param _AllowDiskFileDown: 是否开启 RDP 磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param _AllowShellFileUp: 是否开启 rz sz 文件上传
        :type AllowShellFileUp: bool
        :param _AllowShellFileDown: 是否开启 rz sz 文件下载
        :type AllowShellFileDown: bool
        :param _AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param _ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param _Status: 访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :type Status: int
        :param _Department: 所属部门的信息
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        :param _AllowAccessCredential: 是否允许使用访问串，默认允许
        :type AllowAccessCredential: bool
        :param _ACTemplateSet: 关联的数据库高危命令列表
        :type ACTemplateSet: list of ACTemplate
        :param _WhiteCmds: 关联的白命令命令
        :type WhiteCmds: list of str
        :param _AllowKeyboardLogger: 是否允许记录键盘
        :type AllowKeyboardLogger: bool
        :param _AppAssetSet: 关联的应用资产列表
        :type AppAssetSet: list of AppAsset
        :param _AclType: 权限类型 0-默认普通权限 1-工单权限,2-权限工单权限
        :type AclType: int
        :param _TicketId: 权限所属工单id
        :type TicketId: str
        :param _TicketName: 权限所属工单名称
        :type TicketName: str
        """
        self._Id = None
        self._Name = None
        self._AllowDiskRedirect = None
        self._AllowClipFileUp = None
        self._AllowClipFileDown = None
        self._AllowClipTextUp = None
        self._AllowClipTextDown = None
        self._AllowFileUp = None
        self._MaxFileUpSize = None
        self._AllowFileDown = None
        self._MaxFileDownSize = None
        self._AllowAnyAccount = None
        self._UserSet = None
        self._UserGroupSet = None
        self._DeviceSet = None
        self._DeviceGroupSet = None
        self._AccountSet = None
        self._CmdTemplateSet = None
        self._AllowDiskFileUp = None
        self._AllowDiskFileDown = None
        self._AllowShellFileUp = None
        self._AllowShellFileDown = None
        self._AllowFileDel = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._Status = None
        self._Department = None
        self._AllowAccessCredential = None
        self._ACTemplateSet = None
        self._WhiteCmds = None
        self._AllowKeyboardLogger = None
        self._AppAssetSet = None
        self._AclType = None
        self._TicketId = None
        self._TicketName = None

    @property
    def Id(self):
        r"""访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""访问权限名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        r"""是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowClipFileUp(self):
        r"""是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        r"""是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        r"""是否开启剪贴板文本（目前含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        r"""是否开启剪贴板文本（目前含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        r"""是否开启文件传输上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        r"""文件传输上传大小限制（预留参数，暂未启用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        r"""是否开启文件传输下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        r"""文件传输下载大小限制（预留参数，暂未启用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def AllowAnyAccount(self):
        r"""是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def UserSet(self):
        r"""关联的用户列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

    @property
    def UserGroupSet(self):
        r"""关联的用户组列表
        :rtype: list of Group
        """
        return self._UserGroupSet

    @UserGroupSet.setter
    def UserGroupSet(self, UserGroupSet):
        self._UserGroupSet = UserGroupSet

    @property
    def DeviceSet(self):
        r"""关联的资产列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def DeviceGroupSet(self):
        r"""关联的资产组列表
        :rtype: list of Group
        """
        return self._DeviceGroupSet

    @DeviceGroupSet.setter
    def DeviceGroupSet(self, DeviceGroupSet):
        self._DeviceGroupSet = DeviceGroupSet

    @property
    def AccountSet(self):
        r"""关联的账号列表
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateSet(self):
        r"""关联的高危命令模板列表
        :rtype: list of CmdTemplate
        """
        return self._CmdTemplateSet

    @CmdTemplateSet.setter
    def CmdTemplateSet(self, CmdTemplateSet):
        self._CmdTemplateSet = CmdTemplateSet

    @property
    def AllowDiskFileUp(self):
        r"""是否开启 RDP 磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        r"""是否开启 RDP 磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        r"""是否开启 rz sz 文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        r"""是否开启 rz sz 文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        r"""是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        r"""访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def Status(self):
        r"""访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Department(self):
        r"""所属部门的信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def AllowAccessCredential(self):
        r"""是否允许使用访问串，默认允许
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def ACTemplateSet(self):
        r"""关联的数据库高危命令列表
        :rtype: list of ACTemplate
        """
        return self._ACTemplateSet

    @ACTemplateSet.setter
    def ACTemplateSet(self, ACTemplateSet):
        self._ACTemplateSet = ACTemplateSet

    @property
    def WhiteCmds(self):
        r"""关联的白命令命令
        :rtype: list of str
        """
        return self._WhiteCmds

    @WhiteCmds.setter
    def WhiteCmds(self, WhiteCmds):
        self._WhiteCmds = WhiteCmds

    @property
    def AllowKeyboardLogger(self):
        r"""是否允许记录键盘
        :rtype: bool
        """
        return self._AllowKeyboardLogger

    @AllowKeyboardLogger.setter
    def AllowKeyboardLogger(self, AllowKeyboardLogger):
        self._AllowKeyboardLogger = AllowKeyboardLogger

    @property
    def AppAssetSet(self):
        r"""关联的应用资产列表
        :rtype: list of AppAsset
        """
        return self._AppAssetSet

    @AppAssetSet.setter
    def AppAssetSet(self, AppAssetSet):
        self._AppAssetSet = AppAssetSet

    @property
    def AclType(self):
        r"""权限类型 0-默认普通权限 1-工单权限,2-权限工单权限
        :rtype: int
        """
        return self._AclType

    @AclType.setter
    def AclType(self, AclType):
        self._AclType = AclType

    @property
    def TicketId(self):
        r"""权限所属工单id
        :rtype: str
        """
        return self._TicketId

    @TicketId.setter
    def TicketId(self, TicketId):
        self._TicketId = TicketId

    @property
    def TicketName(self):
        r"""权限所属工单名称
        :rtype: str
        """
        return self._TicketName

    @TicketName.setter
    def TicketName(self, TicketName):
        self._TicketName = TicketName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._AllowDiskRedirect = params.get("AllowDiskRedirect")
        self._AllowClipFileUp = params.get("AllowClipFileUp")
        self._AllowClipFileDown = params.get("AllowClipFileDown")
        self._AllowClipTextUp = params.get("AllowClipTextUp")
        self._AllowClipTextDown = params.get("AllowClipTextDown")
        self._AllowFileUp = params.get("AllowFileUp")
        self._MaxFileUpSize = params.get("MaxFileUpSize")
        self._AllowFileDown = params.get("AllowFileDown")
        self._MaxFileDownSize = params.get("MaxFileDownSize")
        self._AllowAnyAccount = params.get("AllowAnyAccount")
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self._UserSet.append(obj)
        if params.get("UserGroupSet") is not None:
            self._UserGroupSet = []
            for item in params.get("UserGroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._UserGroupSet.append(obj)
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        if params.get("DeviceGroupSet") is not None:
            self._DeviceGroupSet = []
            for item in params.get("DeviceGroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._DeviceGroupSet.append(obj)
        self._AccountSet = params.get("AccountSet")
        if params.get("CmdTemplateSet") is not None:
            self._CmdTemplateSet = []
            for item in params.get("CmdTemplateSet"):
                obj = CmdTemplate()
                obj._deserialize(item)
                self._CmdTemplateSet.append(obj)
        self._AllowDiskFileUp = params.get("AllowDiskFileUp")
        self._AllowDiskFileDown = params.get("AllowDiskFileDown")
        self._AllowShellFileUp = params.get("AllowShellFileUp")
        self._AllowShellFileDown = params.get("AllowShellFileDown")
        self._AllowFileDel = params.get("AllowFileDel")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        self._Status = params.get("Status")
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._AllowAccessCredential = params.get("AllowAccessCredential")
        if params.get("ACTemplateSet") is not None:
            self._ACTemplateSet = []
            for item in params.get("ACTemplateSet"):
                obj = ACTemplate()
                obj._deserialize(item)
                self._ACTemplateSet.append(obj)
        self._WhiteCmds = params.get("WhiteCmds")
        self._AllowKeyboardLogger = params.get("AllowKeyboardLogger")
        if params.get("AppAssetSet") is not None:
            self._AppAssetSet = []
            for item in params.get("AppAssetSet"):
                obj = AppAsset()
                obj._deserialize(item)
                self._AppAssetSet.append(obj)
        self._AclType = params.get("AclType")
        self._TicketId = params.get("TicketId")
        self._TicketName = params.get("TicketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceGroupMembersRequest(AbstractModel):
    r"""AddDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 资产组ID
        :type Id: int
        :param _MemberIdSet: 需要添加到资产组的资产ID集合
        :type MemberIdSet: list of int non-negative
        """
        self._Id = None
        self._MemberIdSet = None

    @property
    def Id(self):
        r"""资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        r"""需要添加到资产组的资产ID集合
        :rtype: list of int non-negative
        """
        return self._MemberIdSet

    @MemberIdSet.setter
    def MemberIdSet(self, MemberIdSet):
        self._MemberIdSet = MemberIdSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceGroupMembersResponse(AbstractModel):
    r"""AddDeviceGroupMembers返回参数结构体

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


class AddUserGroupMembersRequest(AbstractModel):
    r"""AddUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 用户组ID
        :type Id: int
        :param _MemberIdSet: 成员用户ID集合
        :type MemberIdSet: list of int non-negative
        """
        self._Id = None
        self._MemberIdSet = None

    @property
    def Id(self):
        r"""用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        r"""成员用户ID集合
        :rtype: list of int non-negative
        """
        return self._MemberIdSet

    @MemberIdSet.setter
    def MemberIdSet(self, MemberIdSet):
        self._MemberIdSet = MemberIdSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserGroupMembersResponse(AbstractModel):
    r"""AddUserGroupMembers返回参数结构体

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


class AppAsset(AbstractModel):
    r"""应用资产信息

    """

    def __init__(self):
        r"""
        :param _Id: 应用资产id
        :type Id: int
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Name: 资产名称
        :type Name: str
        :param _DeviceId: 应用服务器id
        :type DeviceId: int
        :param _DeviceAccountId: 应用服务器账号id
        :type DeviceAccountId: int
        :param _Kind: 应用资产类型。1-web应用
        :type Kind: int
        :param _ClientAppPath: 客户端工具路径
        :type ClientAppPath: str
        :param _ClientAppKind: 客户端工具类型
        :type ClientAppKind: str
        :param _Url: 应用资产url
        :type Url: str
        :param _BindStatus: 托管状态。0-未托管，1-已托管
        :type BindStatus: int
        :param _DeviceInstanceId: 应用服务器实例id
        :type DeviceInstanceId: str
        :param _DeviceName: 应用服务器名称
        :type DeviceName: str
        :param _DeviceAccountName: 应用服务器账号名称
        :type DeviceAccountName: str
        :param _ResourceId: 堡垒机实例id
        :type ResourceId: str
        :param _Resource: 堡垒机实例信息
        :type Resource: :class:`tencentcloud.bh.v20230418.models.Resource`
        :param _DomainId: 网络域id
        :type DomainId: str
        :param _DomainName: 网络域名称
        :type DomainName: str
        :param _GroupSet: 资产组信息
        :type GroupSet: list of Group
        :param _Department: 资产所属部门
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        self._Id = None
        self._InstanceId = None
        self._Name = None
        self._DeviceId = None
        self._DeviceAccountId = None
        self._Kind = None
        self._ClientAppPath = None
        self._ClientAppKind = None
        self._Url = None
        self._BindStatus = None
        self._DeviceInstanceId = None
        self._DeviceName = None
        self._DeviceAccountName = None
        self._ResourceId = None
        self._Resource = None
        self._DomainId = None
        self._DomainName = None
        self._GroupSet = None
        self._Department = None

    @property
    def Id(self):
        r"""应用资产id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""资产名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceId(self):
        r"""应用服务器id
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceAccountId(self):
        r"""应用服务器账号id
        :rtype: int
        """
        return self._DeviceAccountId

    @DeviceAccountId.setter
    def DeviceAccountId(self, DeviceAccountId):
        self._DeviceAccountId = DeviceAccountId

    @property
    def Kind(self):
        r"""应用资产类型。1-web应用
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def ClientAppPath(self):
        r"""客户端工具路径
        :rtype: str
        """
        return self._ClientAppPath

    @ClientAppPath.setter
    def ClientAppPath(self, ClientAppPath):
        self._ClientAppPath = ClientAppPath

    @property
    def ClientAppKind(self):
        r"""客户端工具类型
        :rtype: str
        """
        return self._ClientAppKind

    @ClientAppKind.setter
    def ClientAppKind(self, ClientAppKind):
        self._ClientAppKind = ClientAppKind

    @property
    def Url(self):
        r"""应用资产url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BindStatus(self):
        r"""托管状态。0-未托管，1-已托管
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def DeviceInstanceId(self):
        r"""应用服务器实例id
        :rtype: str
        """
        return self._DeviceInstanceId

    @DeviceInstanceId.setter
    def DeviceInstanceId(self, DeviceInstanceId):
        self._DeviceInstanceId = DeviceInstanceId

    @property
    def DeviceName(self):
        r"""应用服务器名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceAccountName(self):
        r"""应用服务器账号名称
        :rtype: str
        """
        return self._DeviceAccountName

    @DeviceAccountName.setter
    def DeviceAccountName(self, DeviceAccountName):
        self._DeviceAccountName = DeviceAccountName

    @property
    def ResourceId(self):
        r"""堡垒机实例id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        r"""堡垒机实例信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DomainId(self):
        r"""网络域id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        r"""网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def GroupSet(self):
        r"""资产组信息
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def Department(self):
        r"""资产所属部门
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._DeviceId = params.get("DeviceId")
        self._DeviceAccountId = params.get("DeviceAccountId")
        self._Kind = params.get("Kind")
        self._ClientAppPath = params.get("ClientAppPath")
        self._ClientAppKind = params.get("ClientAppKind")
        self._Url = params.get("Url")
        self._BindStatus = params.get("BindStatus")
        self._DeviceInstanceId = params.get("DeviceInstanceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceAccountName = params.get("DeviceAccountName")
        self._ResourceId = params.get("ResourceId")
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        self._DomainId = params.get("DomainId")
        self._DomainName = params.get("DomainName")
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSyncFlags(AbstractModel):
    r"""资产同步标志

    """

    def __init__(self):
        r"""
        :param _RoleGranted: 是否已完成角色授权
        :type RoleGranted: bool
        :param _AutoSync: 是否已开启自动资产同步
        :type AutoSync: bool
        """
        self._RoleGranted = None
        self._AutoSync = None

    @property
    def RoleGranted(self):
        r"""是否已完成角色授权
        :rtype: bool
        """
        return self._RoleGranted

    @RoleGranted.setter
    def RoleGranted(self, RoleGranted):
        self._RoleGranted = RoleGranted

    @property
    def AutoSync(self):
        r"""是否已开启自动资产同步
        :rtype: bool
        """
        return self._AutoSync

    @AutoSync.setter
    def AutoSync(self, AutoSync):
        self._AutoSync = AutoSync


    def _deserialize(self, params):
        self._RoleGranted = params.get("RoleGranted")
        self._AutoSync = params.get("AutoSync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSyncStatus(AbstractModel):
    r"""资产同步状态

    """

    def __init__(self):
        r"""
        :param _LastTime: 上一次同步完成的时间
        :type LastTime: str
        :param _LastStatus: 上一次同步的结果。 0 - 从未进行, 1 - 成功， 2 - 失败
        :type LastStatus: int
        :param _InProcess: 同步任务是否正在进行中
        :type InProcess: bool
        :param _ErrMsg: 任务错误消息
        :type ErrMsg: str
        """
        self._LastTime = None
        self._LastStatus = None
        self._InProcess = None
        self._ErrMsg = None

    @property
    def LastTime(self):
        r"""上一次同步完成的时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def LastStatus(self):
        r"""上一次同步的结果。 0 - 从未进行, 1 - 成功， 2 - 失败
        :rtype: int
        """
        return self._LastStatus

    @LastStatus.setter
    def LastStatus(self, LastStatus):
        self._LastStatus = LastStatus

    @property
    def InProcess(self):
        r"""同步任务是否正在进行中
        :rtype: bool
        """
        return self._InProcess

    @InProcess.setter
    def InProcess(self, InProcess):
        self._InProcess = InProcess

    @property
    def ErrMsg(self):
        r"""任务错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._LastTime = params.get("LastTime")
        self._LastStatus = params.get("LastStatus")
        self._InProcess = params.get("InProcess")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthModeSetting(AbstractModel):
    r"""认证方式设置

    """

    def __init__(self):
        r"""
        :param _AuthMode: 双因子认证，0-不开启，1-OTP，2-短信
        :type AuthMode: int
        """
        self._AuthMode = None

    @property
    def AuthMode(self):
        r"""双因子认证，0-不开启，1-OTP，2-短信
        :rtype: int
        """
        return self._AuthMode

    @AuthMode.setter
    def AuthMode(self, AuthMode):
        self._AuthMode = AuthMode


    def _deserialize(self, params):
        self._AuthMode = params.get("AuthMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPasswordRequest(AbstractModel):
    r"""BindDeviceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 主机账号ID
        :type Id: int
        :param _Password: 主机账号密码
        :type Password: str
        """
        self._Id = None
        self._Password = None

    @property
    def Id(self):
        r"""主机账号ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Password(self):
        r"""主机账号密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPasswordResponse(AbstractModel):
    r"""BindDeviceAccountPassword返回参数结构体

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


class BindDeviceAccountPrivateKeyRequest(AbstractModel):
    r"""BindDeviceAccountPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 主机账号ID
        :type Id: int
        :param _PrivateKey: 主机账号私钥，最小长度128字节，最大长度8192字节
        :type PrivateKey: str
        :param _PrivateKeyPassword: 主机账号私钥口令，最大长度256字节
        :type PrivateKeyPassword: str
        """
        self._Id = None
        self._PrivateKey = None
        self._PrivateKeyPassword = None

    @property
    def Id(self):
        r"""主机账号ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PrivateKey(self):
        r"""主机账号私钥，最小长度128字节，最大长度8192字节
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def PrivateKeyPassword(self):
        r"""主机账号私钥口令，最大长度256字节
        :rtype: str
        """
        return self._PrivateKeyPassword

    @PrivateKeyPassword.setter
    def PrivateKeyPassword(self, PrivateKeyPassword):
        self._PrivateKeyPassword = PrivateKeyPassword


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PrivateKey = params.get("PrivateKey")
        self._PrivateKeyPassword = params.get("PrivateKeyPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPrivateKeyResponse(AbstractModel):
    r"""BindDeviceAccountPrivateKey返回参数结构体

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


class BindDeviceResourceRequest(AbstractModel):
    r"""BindDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdSet: 资产ID集合
        :type DeviceIdSet: list of int non-negative
        :param _ResourceId: 堡垒机服务ID
        :type ResourceId: str
        :param _DomainId: 网络域ID
        :type DomainId: str
        :param _ManageDimension: K8S集群托管账号维度。1-集群，2-命名空间，3-工作负载
        :type ManageDimension: int
        :param _ManageAccountId: K8S集群托管账号id
        :type ManageAccountId: int
        :param _ManageAccount: K8S集群托管账号名称
        :type ManageAccount: str
        :param _ManageKubeconfig: K8S集群托管账号凭证
        :type ManageKubeconfig: str
        :param _Namespace: K8S集群托管的namespace
        :type Namespace: str
        :param _Workload: K8S集群托管的workload
        :type Workload: str
        """
        self._DeviceIdSet = None
        self._ResourceId = None
        self._DomainId = None
        self._ManageDimension = None
        self._ManageAccountId = None
        self._ManageAccount = None
        self._ManageKubeconfig = None
        self._Namespace = None
        self._Workload = None

    @property
    def DeviceIdSet(self):
        r"""资产ID集合
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def ResourceId(self):
        r"""堡垒机服务ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DomainId(self):
        r"""网络域ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def ManageDimension(self):
        r"""K8S集群托管账号维度。1-集群，2-命名空间，3-工作负载
        :rtype: int
        """
        return self._ManageDimension

    @ManageDimension.setter
    def ManageDimension(self, ManageDimension):
        self._ManageDimension = ManageDimension

    @property
    def ManageAccountId(self):
        r"""K8S集群托管账号id
        :rtype: int
        """
        return self._ManageAccountId

    @ManageAccountId.setter
    def ManageAccountId(self, ManageAccountId):
        self._ManageAccountId = ManageAccountId

    @property
    def ManageAccount(self):
        r"""K8S集群托管账号名称
        :rtype: str
        """
        return self._ManageAccount

    @ManageAccount.setter
    def ManageAccount(self, ManageAccount):
        self._ManageAccount = ManageAccount

    @property
    def ManageKubeconfig(self):
        r"""K8S集群托管账号凭证
        :rtype: str
        """
        return self._ManageKubeconfig

    @ManageKubeconfig.setter
    def ManageKubeconfig(self, ManageKubeconfig):
        self._ManageKubeconfig = ManageKubeconfig

    @property
    def Namespace(self):
        r"""K8S集群托管的namespace
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Workload(self):
        r"""K8S集群托管的workload
        :rtype: str
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload


    def _deserialize(self, params):
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._ResourceId = params.get("ResourceId")
        self._DomainId = params.get("DomainId")
        self._ManageDimension = params.get("ManageDimension")
        self._ManageAccountId = params.get("ManageAccountId")
        self._ManageAccount = params.get("ManageAccount")
        self._ManageKubeconfig = params.get("ManageKubeconfig")
        self._Namespace = params.get("Namespace")
        self._Workload = params.get("Workload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceResourceResponse(AbstractModel):
    r"""BindDeviceResource返回参数结构体

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


class ChangePwdTaskDetail(AbstractModel):
    r"""查询改密计划详情

    """

    def __init__(self):
        r"""
        :param _Device: 资产信息
        :type Device: :class:`tencentcloud.bh.v20230418.models.Device`
        :param _Account: 资产账号
        :type Account: str
        :param _LastChangeStatus: 上次改密结果。0-未改密  1-改密成功 2-改密失败
        :type LastChangeStatus: int
        """
        self._Device = None
        self._Account = None
        self._LastChangeStatus = None

    @property
    def Device(self):
        r"""资产信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Account(self):
        r"""资产账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def LastChangeStatus(self):
        r"""上次改密结果。0-未改密  1-改密成功 2-改密失败
        :rtype: int
        """
        return self._LastChangeStatus

    @LastChangeStatus.setter
    def LastChangeStatus(self, LastChangeStatus):
        self._LastChangeStatus = LastChangeStatus


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._Account = params.get("Account")
        self._LastChangeStatus = params.get("LastChangeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangePwdTaskInfo(AbstractModel):
    r"""修改密码任务信息

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _OperationId: 任务id
        :type OperationId: str
        :param _TaskName: 任务名
        :type TaskName: str
        :param _Department: 所属部门信息
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        :param _ChangeMethod: 改密方式。1：使用执行账号。2：修改自身密码
        :type ChangeMethod: int
        :param _RunAccount: 执行账号
        :type RunAccount: str
        :param _AuthGenerationStrategy: 密码生成策略
        :type AuthGenerationStrategy: int
        :param _PasswordLength: 密码长度
        :type PasswordLength: int
        :param _SmallLetter: 包含小写字母
        :type SmallLetter: int
        :param _BigLetter: 包含大写字母
        :type BigLetter: int
        :param _Digit: 包含数字
        :type Digit: int
        :param _Symbol: 包含的特殊字符，入参base64
        :type Symbol: str
        :param _CompleteNotify: 改密完成通知。0-通知，1-不通知
        :type CompleteNotify: int
        :param _NotifyEmails: 通知人邮箱
        :type NotifyEmails: list of str
        :param _FilePassword: 加密附件密码
        :type FilePassword: str
        :param _AccountSet: 需要改密的账户
        :type AccountSet: list of str
        :param _DeviceSet: 需要改密的主机
        :type DeviceSet: list of Device
        :param _Type: 任务类型：4手动，5自动
        :type Type: int
        :param _Period: 周期
        :type Period: int
        :param _FirstTime: 首次执行时间
        :type FirstTime: str
        :param _NextTime: 下次执行时间
        :type NextTime: str
        :param _LastTime: 上次执行时间
        :type LastTime: str
        """
        self._Id = None
        self._OperationId = None
        self._TaskName = None
        self._Department = None
        self._ChangeMethod = None
        self._RunAccount = None
        self._AuthGenerationStrategy = None
        self._PasswordLength = None
        self._SmallLetter = None
        self._BigLetter = None
        self._Digit = None
        self._Symbol = None
        self._CompleteNotify = None
        self._NotifyEmails = None
        self._FilePassword = None
        self._AccountSet = None
        self._DeviceSet = None
        self._Type = None
        self._Period = None
        self._FirstTime = None
        self._NextTime = None
        self._LastTime = None

    @property
    def Id(self):
        r"""id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationId(self):
        r"""任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def TaskName(self):
        r"""任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Department(self):
        r"""所属部门信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def ChangeMethod(self):
        r"""改密方式。1：使用执行账号。2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def RunAccount(self):
        r"""执行账号
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def AuthGenerationStrategy(self):
        r"""密码生成策略
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def PasswordLength(self):
        r"""密码长度
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        r"""包含小写字母
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        r"""包含大写字母
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        r"""包含数字
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        r"""包含的特殊字符，入参base64
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        r"""改密完成通知。0-通知，1-不通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        r"""通知人邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        r"""加密附件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def AccountSet(self):
        r"""需要改密的账户
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def DeviceSet(self):
        r"""需要改密的主机
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def Type(self):
        r"""任务类型：4手动，5自动
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        r"""周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        r"""首次执行时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def NextTime(self):
        r"""下次执行时间
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        self._NextTime = NextTime

    @property
    def LastTime(self):
        r"""上次执行时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OperationId = params.get("OperationId")
        self._TaskName = params.get("TaskName")
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._ChangeMethod = params.get("ChangeMethod")
        self._RunAccount = params.get("RunAccount")
        self._AuthGenerationStrategy = params.get("AuthGenerationStrategy")
        self._PasswordLength = params.get("PasswordLength")
        self._SmallLetter = params.get("SmallLetter")
        self._BigLetter = params.get("BigLetter")
        self._Digit = params.get("Digit")
        self._Symbol = params.get("Symbol")
        self._CompleteNotify = params.get("CompleteNotify")
        self._NotifyEmails = params.get("NotifyEmails")
        self._FilePassword = params.get("FilePassword")
        self._AccountSet = params.get("AccountSet")
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        self._FirstTime = params.get("FirstTime")
        self._NextTime = params.get("NextTime")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckLDAPConnectionRequest(AbstractModel):
    r"""CheckLDAPConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启LDAP认证，必须为true
        :type Enable: bool
        :param _Ip: 服务器地址
        :type Ip: str
        :param _Port: 服务端口
        :type Port: int
        :param _EnableSSL: 是否开启SSL，false-不开启，true-开启
        :type EnableSSL: bool
        :param _BaseDN: Base DN
        :type BaseDN: str
        :param _AdminAccount: 管理员账号
        :type AdminAccount: str
        :param _AdminPassword: 管理员密码
        :type AdminPassword: str
        :param _IpBackup: 备用服务器地址
        :type IpBackup: str
        :param _DomainId: 网络域id
        :type DomainId: str
        :param _AttributeUserName: 用户名称映射属性
        :type AttributeUserName: str
        """
        self._Enable = None
        self._Ip = None
        self._Port = None
        self._EnableSSL = None
        self._BaseDN = None
        self._AdminAccount = None
        self._AdminPassword = None
        self._IpBackup = None
        self._DomainId = None
        self._AttributeUserName = None

    @property
    def Enable(self):
        r"""是否开启LDAP认证，必须为true
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Ip(self):
        r"""服务器地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""服务端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EnableSSL(self):
        r"""是否开启SSL，false-不开启，true-开启
        :rtype: bool
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def BaseDN(self):
        r"""Base DN
        :rtype: str
        """
        return self._BaseDN

    @BaseDN.setter
    def BaseDN(self, BaseDN):
        self._BaseDN = BaseDN

    @property
    def AdminAccount(self):
        r"""管理员账号
        :rtype: str
        """
        return self._AdminAccount

    @AdminAccount.setter
    def AdminAccount(self, AdminAccount):
        self._AdminAccount = AdminAccount

    @property
    def AdminPassword(self):
        r"""管理员密码
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def IpBackup(self):
        r"""备用服务器地址
        :rtype: str
        """
        return self._IpBackup

    @IpBackup.setter
    def IpBackup(self, IpBackup):
        self._IpBackup = IpBackup

    @property
    def DomainId(self):
        r"""网络域id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def AttributeUserName(self):
        r"""用户名称映射属性
        :rtype: str
        """
        return self._AttributeUserName

    @AttributeUserName.setter
    def AttributeUserName(self, AttributeUserName):
        self._AttributeUserName = AttributeUserName


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._EnableSSL = params.get("EnableSSL")
        self._BaseDN = params.get("BaseDN")
        self._AdminAccount = params.get("AdminAccount")
        self._AdminPassword = params.get("AdminPassword")
        self._IpBackup = params.get("IpBackup")
        self._DomainId = params.get("DomainId")
        self._AttributeUserName = params.get("AttributeUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckLDAPConnectionResponse(AbstractModel):
    r"""CheckLDAPConnection返回参数结构体

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


class Clb(AbstractModel):
    r"""负载均衡

    """

    def __init__(self):
        r"""
        :param _ClbIp: 负载均衡IP	
        :type ClbIp: str
        """
        self._ClbIp = None

    @property
    def ClbIp(self):
        r"""负载均衡IP	
        :rtype: str
        """
        return self._ClbIp

    @ClbIp.setter
    def ClbIp(self, ClbIp):
        self._ClbIp = ClbIp


    def _deserialize(self, params):
        self._ClbIp = params.get("ClbIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmdTemplate(AbstractModel):
    r"""高危命令模板

    """

    def __init__(self):
        r"""
        :param _Id: 高危命令模板ID
        :type Id: int
        :param _Name: 高危命令模板名称
        :type Name: str
        :param _CmdList: 命令列表，命令之间用换行符（"\n"）分隔
        :type CmdList: str
        :param _Type: 命令模板类型 1-内置 2-自定义
        :type Type: int
        """
        self._Id = None
        self._Name = None
        self._CmdList = None
        self._Type = None

    @property
    def Id(self):
        r"""高危命令模板ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""高危命令模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        r"""命令列表，命令之间用换行符（"\n"）分隔
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Type(self):
        r"""命令模板类型 1-内置 2-自定义
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._CmdList = params.get("CmdList")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Command(AbstractModel):
    r"""命令集合

    """

    def __init__(self):
        r"""
        :param _Cmd: 命令
        :type Cmd: str
        :param _Time: 命令输入的时间
        :type Time: str
        :param _TimeOffset: 命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :type TimeOffset: int
        :param _Action: 命令执行情况，1--允许，2--拒绝，3--确认
        :type Action: int
        :param _Sid: 会话id
        :type Sid: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Account: 设备account
        :type Account: str
        :param _InstanceId: 设备ip
        :type InstanceId: str
        :param _FromIp: source ip
        :type FromIp: str
        :param _SessTime: 该命令所属会话的会话开始时间
        :type SessTime: str
        :param _SessionTime: 该命令所属会话的会话开始时间
        :type SessionTime: str
        :param _ConfirmTime: 复核时间
        :type ConfirmTime: str
        :param _UserDepartmentId: 用户部门id
        :type UserDepartmentId: str
        :param _UserDepartmentName: 用户部门name
        :type UserDepartmentName: str
        :param _DeviceDepartmentId: 设备部门id
        :type DeviceDepartmentId: str
        :param _DeviceDepartmentName: 设备部门name
        :type DeviceDepartmentName: str
        :param _Size: 会话大小
        :type Size: int
        :param _SignValue: 签名值
        :type SignValue: str
        :param _DeviceKind: 资产类型
        :type DeviceKind: str
        """
        self._Cmd = None
        self._Time = None
        self._TimeOffset = None
        self._Action = None
        self._Sid = None
        self._UserName = None
        self._Account = None
        self._InstanceId = None
        self._FromIp = None
        self._SessTime = None
        self._SessionTime = None
        self._ConfirmTime = None
        self._UserDepartmentId = None
        self._UserDepartmentName = None
        self._DeviceDepartmentId = None
        self._DeviceDepartmentName = None
        self._Size = None
        self._SignValue = None
        self._DeviceKind = None

    @property
    def Cmd(self):
        r"""命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Time(self):
        r"""命令输入的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TimeOffset(self):
        r"""命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :rtype: int
        """
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset

    @property
    def Action(self):
        r"""命令执行情况，1--允许，2--拒绝，3--确认
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Sid(self):
        r"""会话id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

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
    def Account(self):
        r"""设备account
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def InstanceId(self):
        r"""设备ip
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FromIp(self):
        r"""source ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def SessTime(self):
        r"""该命令所属会话的会话开始时间
        :rtype: str
        """
        return self._SessTime

    @SessTime.setter
    def SessTime(self, SessTime):
        self._SessTime = SessTime

    @property
    def SessionTime(self):
        r"""该命令所属会话的会话开始时间
        :rtype: str
        """
        return self._SessionTime

    @SessionTime.setter
    def SessionTime(self, SessionTime):
        self._SessionTime = SessionTime

    @property
    def ConfirmTime(self):
        r"""复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        r"""用户部门id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        r"""用户部门name
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        r"""设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        r"""设备部门name
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def Size(self):
        r"""会话大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SignValue(self):
        r"""签名值
        :rtype: str
        """
        return self._SignValue

    @SignValue.setter
    def SignValue(self, SignValue):
        self._SignValue = SignValue

    @property
    def DeviceKind(self):
        r"""资产类型
        :rtype: str
        """
        return self._DeviceKind

    @DeviceKind.setter
    def DeviceKind(self, DeviceKind):
        self._DeviceKind = DeviceKind


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Time = params.get("Time")
        self._TimeOffset = params.get("TimeOffset")
        self._Action = params.get("Action")
        self._Sid = params.get("Sid")
        self._UserName = params.get("UserName")
        self._Account = params.get("Account")
        self._InstanceId = params.get("InstanceId")
        self._FromIp = params.get("FromIp")
        self._SessTime = params.get("SessTime")
        self._SessionTime = params.get("SessionTime")
        self._ConfirmTime = params.get("ConfirmTime")
        self._UserDepartmentId = params.get("UserDepartmentId")
        self._UserDepartmentName = params.get("UserDepartmentName")
        self._DeviceDepartmentId = params.get("DeviceDepartmentId")
        self._DeviceDepartmentName = params.get("DeviceDepartmentName")
        self._Size = params.get("Size")
        self._SignValue = params.get("SignValue")
        self._DeviceKind = params.get("DeviceKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessWhiteListRuleRequest(AbstractModel):
    r"""CreateAccessWhiteListRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: ip 10.10.10.1或者网段10.10.10.0/24，最小长度4字节，最大长度40字节。
        :type Source: str
        :param _Remark: 备注信息，最小长度0字符，最大长度40字符。
        :type Remark: str
        """
        self._Source = None
        self._Remark = None

    @property
    def Source(self):
        r"""ip 10.10.10.1或者网段10.10.10.0/24，最小长度4字节，最大长度40字节。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Remark(self):
        r"""备注信息，最小长度0字符，最大长度40字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessWhiteListRuleResponse(AbstractModel):
    r"""CreateAccessWhiteListRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 新建成功后返回的记录ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功后返回的记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateAclRequest(AbstractModel):
    r"""CreateAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 权限名称，最大32字符，不能包含空白字符
        :type Name: str
        :param _AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param _AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param _AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param _AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param _AllowClipTextUp: 是否开启剪贴板文本（含图片）上行
        :type AllowClipTextUp: bool
        :param _AllowClipTextDown: 是否开启剪贴板文本（含图片）下行
        :type AllowClipTextDown: bool
        :param _AllowFileUp: 是否开启 SFTP 文件上传
        :type AllowFileUp: bool
        :param _MaxFileUpSize: 文件传输上传大小限制（预留参数，目前暂未使用）
        :type MaxFileUpSize: int
        :param _AllowFileDown: 是否开启 SFTP 文件下载
        :type AllowFileDown: bool
        :param _MaxFileDownSize: 文件传输下载大小限制（预留参数，目前暂未使用）
        :type MaxFileDownSize: int
        :param _UserIdSet: 关联的用户ID集合
        :type UserIdSet: list of int non-negative
        :param _UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param _DeviceIdSet: 关联的资产ID集合
        :type DeviceIdSet: list of int non-negative
        :param _AppAssetIdSet: 关联的应用资产ID集合
        :type AppAssetIdSet: list of int non-negative
        :param _DeviceGroupIdSet: 关联的资产组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param _AccountSet: 关联的账号
        :type AccountSet: list of str
        :param _CmdTemplateIdSet: 关联的高危命令模板ID
        :type CmdTemplateIdSet: list of int non-negative
        :param _ACTemplateIdSet: 关联高危DB模板ID
        :type ACTemplateIdSet: list of str
        :param _AllowDiskFileUp: 是否开启rdp磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param _AllowDiskFileDown: 是否开启rdp磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param _AllowShellFileUp: 是否开启rz sz文件上传
        :type AllowShellFileUp: bool
        :param _AllowShellFileDown: 是否开启rz sz文件下载
        :type AllowShellFileDown: bool
        :param _AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param _ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param _DepartmentId: 访问权限所属部门的ID
        :type DepartmentId: str
        :param _AllowAccessCredential: 是否允许使用访问串，默认允许
        :type AllowAccessCredential: bool
        :param _AllowKeyboardLogger: 是否允许键盘记录
        :type AllowKeyboardLogger: bool
        """
        self._Name = None
        self._AllowDiskRedirect = None
        self._AllowAnyAccount = None
        self._AllowClipFileUp = None
        self._AllowClipFileDown = None
        self._AllowClipTextUp = None
        self._AllowClipTextDown = None
        self._AllowFileUp = None
        self._MaxFileUpSize = None
        self._AllowFileDown = None
        self._MaxFileDownSize = None
        self._UserIdSet = None
        self._UserGroupIdSet = None
        self._DeviceIdSet = None
        self._AppAssetIdSet = None
        self._DeviceGroupIdSet = None
        self._AccountSet = None
        self._CmdTemplateIdSet = None
        self._ACTemplateIdSet = None
        self._AllowDiskFileUp = None
        self._AllowDiskFileDown = None
        self._AllowShellFileUp = None
        self._AllowShellFileDown = None
        self._AllowFileDel = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._DepartmentId = None
        self._AllowAccessCredential = None
        self._AllowKeyboardLogger = None

    @property
    def Name(self):
        r"""权限名称，最大32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        r"""是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowAnyAccount(self):
        r"""是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def AllowClipFileUp(self):
        r"""是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        r"""是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        r"""是否开启剪贴板文本（含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        r"""是否开启剪贴板文本（含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        r"""是否开启 SFTP 文件上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        r"""文件传输上传大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        r"""是否开启 SFTP 文件下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        r"""文件传输下载大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def UserIdSet(self):
        r"""关联的用户ID集合
        :rtype: list of int non-negative
        """
        return self._UserIdSet

    @UserIdSet.setter
    def UserIdSet(self, UserIdSet):
        self._UserIdSet = UserIdSet

    @property
    def UserGroupIdSet(self):
        r"""关联的用户组ID
        :rtype: list of int non-negative
        """
        return self._UserGroupIdSet

    @UserGroupIdSet.setter
    def UserGroupIdSet(self, UserGroupIdSet):
        self._UserGroupIdSet = UserGroupIdSet

    @property
    def DeviceIdSet(self):
        r"""关联的资产ID集合
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AppAssetIdSet(self):
        r"""关联的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AppAssetIdSet

    @AppAssetIdSet.setter
    def AppAssetIdSet(self, AppAssetIdSet):
        self._AppAssetIdSet = AppAssetIdSet

    @property
    def DeviceGroupIdSet(self):
        r"""关联的资产组ID
        :rtype: list of int non-negative
        """
        return self._DeviceGroupIdSet

    @DeviceGroupIdSet.setter
    def DeviceGroupIdSet(self, DeviceGroupIdSet):
        self._DeviceGroupIdSet = DeviceGroupIdSet

    @property
    def AccountSet(self):
        r"""关联的账号
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateIdSet(self):
        r"""关联的高危命令模板ID
        :rtype: list of int non-negative
        """
        return self._CmdTemplateIdSet

    @CmdTemplateIdSet.setter
    def CmdTemplateIdSet(self, CmdTemplateIdSet):
        self._CmdTemplateIdSet = CmdTemplateIdSet

    @property
    def ACTemplateIdSet(self):
        r"""关联高危DB模板ID
        :rtype: list of str
        """
        return self._ACTemplateIdSet

    @ACTemplateIdSet.setter
    def ACTemplateIdSet(self, ACTemplateIdSet):
        self._ACTemplateIdSet = ACTemplateIdSet

    @property
    def AllowDiskFileUp(self):
        r"""是否开启rdp磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        r"""是否开启rdp磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        r"""是否开启rz sz文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        r"""是否开启rz sz文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        r"""是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        r"""访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def DepartmentId(self):
        r"""访问权限所属部门的ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def AllowAccessCredential(self):
        r"""是否允许使用访问串，默认允许
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def AllowKeyboardLogger(self):
        r"""是否允许键盘记录
        :rtype: bool
        """
        return self._AllowKeyboardLogger

    @AllowKeyboardLogger.setter
    def AllowKeyboardLogger(self, AllowKeyboardLogger):
        self._AllowKeyboardLogger = AllowKeyboardLogger


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AllowDiskRedirect = params.get("AllowDiskRedirect")
        self._AllowAnyAccount = params.get("AllowAnyAccount")
        self._AllowClipFileUp = params.get("AllowClipFileUp")
        self._AllowClipFileDown = params.get("AllowClipFileDown")
        self._AllowClipTextUp = params.get("AllowClipTextUp")
        self._AllowClipTextDown = params.get("AllowClipTextDown")
        self._AllowFileUp = params.get("AllowFileUp")
        self._MaxFileUpSize = params.get("MaxFileUpSize")
        self._AllowFileDown = params.get("AllowFileDown")
        self._MaxFileDownSize = params.get("MaxFileDownSize")
        self._UserIdSet = params.get("UserIdSet")
        self._UserGroupIdSet = params.get("UserGroupIdSet")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._AppAssetIdSet = params.get("AppAssetIdSet")
        self._DeviceGroupIdSet = params.get("DeviceGroupIdSet")
        self._AccountSet = params.get("AccountSet")
        self._CmdTemplateIdSet = params.get("CmdTemplateIdSet")
        self._ACTemplateIdSet = params.get("ACTemplateIdSet")
        self._AllowDiskFileUp = params.get("AllowDiskFileUp")
        self._AllowDiskFileDown = params.get("AllowDiskFileDown")
        self._AllowShellFileUp = params.get("AllowShellFileUp")
        self._AllowShellFileDown = params.get("AllowShellFileDown")
        self._AllowFileDel = params.get("AllowFileDel")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        self._DepartmentId = params.get("DepartmentId")
        self._AllowAccessCredential = params.get("AllowAccessCredential")
        self._AllowKeyboardLogger = params.get("AllowKeyboardLogger")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    r"""CreateAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 新建成功的访问权限ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功的访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateAssetSyncJobRequest(AbstractModel):
    r"""CreateAssetSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Category: 同步资产类别，1 - 主机资产, 2 - 数据库资产
        :type Category: int
        """
        self._Category = None

    @property
    def Category(self):
        r"""同步资产类别，1 - 主机资产, 2 - 数据库资产
        :rtype: int
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetSyncJobResponse(AbstractModel):
    r"""CreateAssetSyncJob返回参数结构体

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


class CreateChangePwdTaskRequest(AbstractModel):
    r"""CreateChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名
        :type TaskName: str
        :param _DeviceIdSet: 资产id数组
        :type DeviceIdSet: list of int non-negative
        :param _AccountSet: 修改的账户数组
        :type AccountSet: list of str
        :param _ChangeMethod: 改密方式。1：使用执行账号修改密码；2：修改自身密码
        :type ChangeMethod: int
        :param _AuthGenerationStrategy: 认证生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :type AuthGenerationStrategy: int
        :param _RunAccount: 执行账号
        :type RunAccount: str
        :param _Password: 手动指定密码时必传
        :type Password: str
        :param _PasswordLength: 密码限制长度，长度大于 12 位
        :type PasswordLength: int
        :param _SmallLetter: 密码包含小写字母。0：否，1：是
        :type SmallLetter: int
        :param _BigLetter: 密码包含大写字母。0：否，1：是
        :type BigLetter: int
        :param _Digit: 密码包含数字。0：否，1：是
        :type Digit: int
        :param _Symbol: 密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :type Symbol: str
        :param _CompleteNotify: 改密完成通知。0：不通知 
  1：通知
        :type CompleteNotify: int
        :param _NotifyEmails: 通知邮箱
        :type NotifyEmails: list of str
        :param _FilePassword: 加密压缩文件密码
        :type FilePassword: str
        :param _DepartmentId: 所属部门id。“1.2.3”
        :type DepartmentId: str
        :param _Type: 任务类型  4-手工执行  5-周期自动执行
        :type Type: int
        :param _Period: 执行周期，单位天（大于等于 1，小于等于 365）
        :type Period: int
        :param _FirstTime: 周期任务首次执行时间
        :type FirstTime: str
        """
        self._TaskName = None
        self._DeviceIdSet = None
        self._AccountSet = None
        self._ChangeMethod = None
        self._AuthGenerationStrategy = None
        self._RunAccount = None
        self._Password = None
        self._PasswordLength = None
        self._SmallLetter = None
        self._BigLetter = None
        self._Digit = None
        self._Symbol = None
        self._CompleteNotify = None
        self._NotifyEmails = None
        self._FilePassword = None
        self._DepartmentId = None
        self._Type = None
        self._Period = None
        self._FirstTime = None

    @property
    def TaskName(self):
        r"""任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DeviceIdSet(self):
        r"""资产id数组
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AccountSet(self):
        r"""修改的账户数组
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def ChangeMethod(self):
        r"""改密方式。1：使用执行账号修改密码；2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def AuthGenerationStrategy(self):
        r"""认证生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def RunAccount(self):
        r"""执行账号
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def Password(self):
        r"""手动指定密码时必传
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordLength(self):
        r"""密码限制长度，长度大于 12 位
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        r"""密码包含小写字母。0：否，1：是
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        r"""密码包含大写字母。0：否，1：是
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        r"""密码包含数字。0：否，1：是
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        r"""密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        r"""改密完成通知。0：不通知 
  1：通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        r"""通知邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        r"""加密压缩文件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def DepartmentId(self):
        r"""所属部门id。“1.2.3”
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Type(self):
        r"""任务类型  4-手工执行  5-周期自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        r"""执行周期，单位天（大于等于 1，小于等于 365）
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        r"""周期任务首次执行时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._AccountSet = params.get("AccountSet")
        self._ChangeMethod = params.get("ChangeMethod")
        self._AuthGenerationStrategy = params.get("AuthGenerationStrategy")
        self._RunAccount = params.get("RunAccount")
        self._Password = params.get("Password")
        self._PasswordLength = params.get("PasswordLength")
        self._SmallLetter = params.get("SmallLetter")
        self._BigLetter = params.get("BigLetter")
        self._Digit = params.get("Digit")
        self._Symbol = params.get("Symbol")
        self._CompleteNotify = params.get("CompleteNotify")
        self._NotifyEmails = params.get("NotifyEmails")
        self._FilePassword = params.get("FilePassword")
        self._DepartmentId = params.get("DepartmentId")
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        self._FirstTime = params.get("FirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChangePwdTaskResponse(AbstractModel):
    r"""CreateChangePwdTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationId: 任务id
        :type OperationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperationId = None
        self._RequestId = None

    @property
    def OperationId(self):
        r"""任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

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
        self._OperationId = params.get("OperationId")
        self._RequestId = params.get("RequestId")


class CreateCmdTemplateRequest(AbstractModel):
    r"""CreateCmdTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模板名，最大长度32字符，不能包含空白字符
        :type Name: str
        :param _CmdList: 命令列表，\n分隔，最大长度32768字节
        :type CmdList: str
        :param _Encoding: 标识CmdList字段前端是否为base64加密传值.0:表示非base64加密1:表示是base64加密
        :type Encoding: int
        """
        self._Name = None
        self._CmdList = None
        self._Encoding = None

    @property
    def Name(self):
        r"""模板名，最大长度32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        r"""命令列表，\n分隔，最大长度32768字节
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Encoding(self):
        r"""标识CmdList字段前端是否为base64加密传值.0:表示非base64加密1:表示是base64加密
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CmdList = params.get("CmdList")
        self._Encoding = params.get("Encoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmdTemplateResponse(AbstractModel):
    r"""CreateCmdTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 新建成功后返回的记录ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功后返回的记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDeviceAccountRequest(AbstractModel):
    r"""CreateDeviceAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 主机记录ID
        :type DeviceId: int
        :param _Account: 账号名
        :type Account: str
        """
        self._DeviceId = None
        self._Account = None

    @property
    def DeviceId(self):
        r"""主机记录ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Account(self):
        r"""账号名
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Account = params.get("Account")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceAccountResponse(AbstractModel):
    r"""CreateDeviceAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 新建成功后返回的记录ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功后返回的记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDeviceGroupRequest(AbstractModel):
    r"""CreateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 资产组名，最大长度32字符
        :type Name: str
        :param _DepartmentId: 资产组所属部门ID，如：1.2.3
        :type DepartmentId: str
        """
        self._Name = None
        self._DepartmentId = None

    @property
    def Name(self):
        r"""资产组名，最大长度32字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        r"""资产组所属部门ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceGroupResponse(AbstractModel):
    r"""CreateDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 新建成功的资产组ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功的资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateOperationTaskRequest(AbstractModel):
    r"""CreateOperationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 运维任务名称
        :type Name: str
        :param _Type: 运维任务类型,1 - 手工执行, 2 - 周期性自动执行
        :type Type: int
        :param _Account: 执行账号
        :type Account: str
        :param _Timeout: 超时时间,单位秒
        :type Timeout: int
        :param _Script: 执行脚本内容
        :type Script: str
        :param _DeviceIdSet: 执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :type DeviceIdSet: list of int non-negative
        :param _Period: 执行间隔，单位天. 手工执行时无需传入
        :type Period: int
        :param _FirstTime: 首次执行日期 默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :type FirstTime: str
        :param _Encoding: Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
        :type Encoding: int
        """
        self._Name = None
        self._Type = None
        self._Account = None
        self._Timeout = None
        self._Script = None
        self._DeviceIdSet = None
        self._Period = None
        self._FirstTime = None
        self._Encoding = None

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""运维任务类型,1 - 手工执行, 2 - 周期性自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Account(self):
        r"""执行账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Timeout(self):
        r"""超时时间,单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Script(self):
        r"""执行脚本内容
        :rtype: str
        """
        return self._Script

    @Script.setter
    def Script(self, Script):
        self._Script = Script

    @property
    def DeviceIdSet(self):
        r"""执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def Period(self):
        r"""执行间隔，单位天. 手工执行时无需传入
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        r"""首次执行日期 默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Encoding(self):
        r"""Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Account = params.get("Account")
        self._Timeout = params.get("Timeout")
        self._Script = params.get("Script")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._Period = params.get("Period")
        self._FirstTime = params.get("FirstTime")
        self._Encoding = params.get("Encoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOperationTaskResponse(AbstractModel):
    r"""CreateOperationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 运维任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""运维任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    r"""CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRegion: 部署region
        :type DeployRegion: str
        :param _VpcId: 部署堡垒机的VpcId
        :type VpcId: str
        :param _SubnetId: 部署堡垒机的SubnetId
        :type SubnetId: str
        :param _ResourceEdition: 资源类型。取值:standard/pro
        :type ResourceEdition: str
        :param _ResourceNode: 资源节点数
        :type ResourceNode: int
        :param _TimeUnit: 计费周期
        :type TimeUnit: str
        :param _TimeSpan: 计费时长
        :type TimeSpan: int
        :param _PayMode: 计费模式 1预付费
        :type PayMode: int
        :param _AutoRenewFlag: 自动续费
        :type AutoRenewFlag: int
        :param _DeployZone: 部署zone
        :type DeployZone: str
        :param _Trial: 0非试用版，1试用版
        :type Trial: int
        :param _ShareClb: 是否共享clb，0：不共享，1：共享
        :type ShareClb: int
        """
        self._DeployRegion = None
        self._VpcId = None
        self._SubnetId = None
        self._ResourceEdition = None
        self._ResourceNode = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PayMode = None
        self._AutoRenewFlag = None
        self._DeployZone = None
        self._Trial = None
        self._ShareClb = None

    @property
    def DeployRegion(self):
        r"""部署region
        :rtype: str
        """
        return self._DeployRegion

    @DeployRegion.setter
    def DeployRegion(self, DeployRegion):
        self._DeployRegion = DeployRegion

    @property
    def VpcId(self):
        r"""部署堡垒机的VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""部署堡垒机的SubnetId
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ResourceEdition(self):
        r"""资源类型。取值:standard/pro
        :rtype: str
        """
        return self._ResourceEdition

    @ResourceEdition.setter
    def ResourceEdition(self, ResourceEdition):
        self._ResourceEdition = ResourceEdition

    @property
    def ResourceNode(self):
        r"""资源节点数
        :rtype: int
        """
        return self._ResourceNode

    @ResourceNode.setter
    def ResourceNode(self, ResourceNode):
        self._ResourceNode = ResourceNode

    @property
    def TimeUnit(self):
        r"""计费周期
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        r"""计费时长
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PayMode(self):
        r"""计费模式 1预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        r"""自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeployZone(self):
        r"""部署zone
        :rtype: str
        """
        return self._DeployZone

    @DeployZone.setter
    def DeployZone(self, DeployZone):
        self._DeployZone = DeployZone

    @property
    def Trial(self):
        r"""0非试用版，1试用版
        :rtype: int
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def ShareClb(self):
        r"""是否共享clb，0：不共享，1：共享
        :rtype: int
        """
        return self._ShareClb

    @ShareClb.setter
    def ShareClb(self, ShareClb):
        self._ShareClb = ShareClb


    def _deserialize(self, params):
        self._DeployRegion = params.get("DeployRegion")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ResourceEdition = params.get("ResourceEdition")
        self._ResourceNode = params.get("ResourceNode")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._PayMode = params.get("PayMode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DeployZone = params.get("DeployZone")
        self._Trial = params.get("Trial")
        self._ShareClb = params.get("ShareClb")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    r"""CreateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 实例Id
        :type ResourceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._RequestId = None

    @property
    def ResourceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

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
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


class CreateSyncUserTaskRequest(AbstractModel):
    r"""CreateSyncUserTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserKind: 同步用户类型, 1-同步ioa用户
        :type UserKind: int
        """
        self._UserKind = None

    @property
    def UserKind(self):
        r"""同步用户类型, 1-同步ioa用户
        :rtype: int
        """
        return self._UserKind

    @UserKind.setter
    def UserKind(self, UserKind):
        self._UserKind = UserKind


    def _deserialize(self, params):
        self._UserKind = params.get("UserKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncUserTaskResponse(AbstractModel):
    r"""CreateSyncUserTask返回参数结构体

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


class CreateUserDirectoryRequest(AbstractModel):
    r"""CreateUserDirectory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirId: 目录id
        :type DirId: int
        :param _DirName: 目录名称
        :type DirName: str
        :param _UserOrgSet: ioa分组信息
        :type UserOrgSet: list of UserOrg
        :param _Source: ioa关联用户源类型
        :type Source: int
        :param _SourceName: ioa关联用户源名称
        :type SourceName: str
        :param _UserCount: 目录包含用户数
        :type UserCount: int
        """
        self._DirId = None
        self._DirName = None
        self._UserOrgSet = None
        self._Source = None
        self._SourceName = None
        self._UserCount = None

    @property
    def DirId(self):
        r"""目录id
        :rtype: int
        """
        return self._DirId

    @DirId.setter
    def DirId(self, DirId):
        self._DirId = DirId

    @property
    def DirName(self):
        r"""目录名称
        :rtype: str
        """
        return self._DirName

    @DirName.setter
    def DirName(self, DirName):
        self._DirName = DirName

    @property
    def UserOrgSet(self):
        r"""ioa分组信息
        :rtype: list of UserOrg
        """
        return self._UserOrgSet

    @UserOrgSet.setter
    def UserOrgSet(self, UserOrgSet):
        self._UserOrgSet = UserOrgSet

    @property
    def Source(self):
        r"""ioa关联用户源类型
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceName(self):
        r"""ioa关联用户源名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def UserCount(self):
        r"""目录包含用户数
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount


    def _deserialize(self, params):
        self._DirId = params.get("DirId")
        self._DirName = params.get("DirName")
        if params.get("UserOrgSet") is not None:
            self._UserOrgSet = []
            for item in params.get("UserOrgSet"):
                obj = UserOrg()
                obj._deserialize(item)
                self._UserOrgSet.append(obj)
        self._Source = params.get("Source")
        self._SourceName = params.get("SourceName")
        self._UserCount = params.get("UserCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserDirectoryResponse(AbstractModel):
    r"""CreateUserDirectory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 目录Id
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""目录Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    r"""CreateUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 用户组名，最大长度32字符
        :type Name: str
        :param _DepartmentId: 用户组所属部门的ID，如：1.2.3
        :type DepartmentId: str
        """
        self._Name = None
        self._DepartmentId = None

    @property
    def Name(self):
        r"""用户组名，最大长度32字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        r"""用户组所属部门的ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DepartmentId = params.get("DepartmentId")
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
        :param _Id: 新建成功的用户组ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建成功的用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    r"""CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名, 3-20个字符, 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :type UserName: str
        :param _RealName: 用户姓名，最大长度20个字符，不能包含空白字符
        :type RealName: str
        :param _Phone: 按照"国家地区代码|手机号"的格式输入，如: "+86|xxxxxxxx"。手机号和邮箱参数至少传一项
        :type Phone: str
        :param _Email: 电子邮件。手机号和邮箱参数至少传一项
        :type Email: str
        :param _ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param _GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param _AuthType: 认证方式，0 - 本地， 1 - LDAP， 2 - OAuth 不传则默认为0
        :type AuthType: int
        :param _ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param _DepartmentId: 所属部门ID，如：“1.2.3”
        :type DepartmentId: str
        """
        self._UserName = None
        self._RealName = None
        self._Phone = None
        self._Email = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._GroupIdSet = None
        self._AuthType = None
        self._ValidateTime = None
        self._DepartmentId = None

    @property
    def UserName(self):
        r"""用户名, 3-20个字符, 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""用户姓名，最大长度20个字符，不能包含空白字符
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Phone(self):
        r"""按照"国家地区代码|手机号"的格式输入，如: "+86|xxxxxxxx"。手机号和邮箱参数至少传一项
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""电子邮件。手机号和邮箱参数至少传一项
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        r"""用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupIdSet(self):
        r"""所属用户组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def AuthType(self):
        r"""认证方式，0 - 本地， 1 - LDAP， 2 - OAuth 不传则默认为0
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        r"""访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def DepartmentId(self):
        r"""所属部门ID，如：“1.2.3”
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        self._GroupIdSet = params.get("GroupIdSet")
        self._AuthType = params.get("AuthType")
        self._ValidateTime = params.get("ValidateTime")
        self._DepartmentId = params.get("DepartmentId")
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
        :param _Id: 新建用户的ID
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""新建用户的ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class DeleteAccessWhiteListRulesRequest(AbstractModel):
    r"""DeleteAccessWhiteListRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessWhiteListRulesResponse(AbstractModel):
    r"""DeleteAccessWhiteListRules返回参数结构体

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


class DeleteAclsRequest(AbstractModel):
    r"""DeleteAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的权限ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的权限ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclsResponse(AbstractModel):
    r"""DeleteAcls返回参数结构体

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


class DeleteChangePwdTaskRequest(AbstractModel):
    r"""DeleteChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 改密任务id列表
        :type IdSet: list of int
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""改密任务id列表
        :rtype: list of int
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteChangePwdTaskResponse(AbstractModel):
    r"""DeleteChangePwdTask返回参数结构体

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


class DeleteCmdTemplatesRequest(AbstractModel):
    r"""DeleteCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmdTemplatesResponse(AbstractModel):
    r"""DeleteCmdTemplates返回参数结构体

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


class DeleteDeviceAccountsRequest(AbstractModel):
    r"""DeleteDeviceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceAccountsResponse(AbstractModel):
    r"""DeleteDeviceAccounts返回参数结构体

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


class DeleteDeviceGroupMembersRequest(AbstractModel):
    r"""DeleteDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 资产组ID
        :type Id: int
        :param _MemberIdSet: 需要删除的资产ID集合
        :type MemberIdSet: list of int non-negative
        """
        self._Id = None
        self._MemberIdSet = None

    @property
    def Id(self):
        r"""资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        r"""需要删除的资产ID集合
        :rtype: list of int non-negative
        """
        return self._MemberIdSet

    @MemberIdSet.setter
    def MemberIdSet(self, MemberIdSet):
        self._MemberIdSet = MemberIdSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupMembersResponse(AbstractModel):
    r"""DeleteDeviceGroupMembers返回参数结构体

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


class DeleteDeviceGroupsRequest(AbstractModel):
    r"""DeleteDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的资产组ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的资产组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupsResponse(AbstractModel):
    r"""DeleteDeviceGroups返回参数结构体

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


class DeleteDevicesRequest(AbstractModel):
    r"""DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDevicesResponse(AbstractModel):
    r"""DeleteDevices返回参数结构体

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


class DeleteOperationTasksRequest(AbstractModel):
    r"""DeleteOperationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 运维任务ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""运维任务ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOperationTasksResponse(AbstractModel):
    r"""DeleteOperationTasks返回参数结构体

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


class DeleteUserDirectoryRequest(AbstractModel):
    r"""DeleteUserDirectory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 目录id集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""目录id集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserDirectoryResponse(AbstractModel):
    r"""DeleteUserDirectory返回参数结构体

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


class DeleteUserGroupMembersRequest(AbstractModel):
    r"""DeleteUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 用户组ID
        :type Id: int
        :param _MemberIdSet: 需删除的成员用户ID集合
        :type MemberIdSet: list of int non-negative
        """
        self._Id = None
        self._MemberIdSet = None

    @property
    def Id(self):
        r"""用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        r"""需删除的成员用户ID集合
        :rtype: list of int non-negative
        """
        return self._MemberIdSet

    @MemberIdSet.setter
    def MemberIdSet(self, MemberIdSet):
        self._MemberIdSet = MemberIdSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserGroupMembersResponse(AbstractModel):
    r"""DeleteUserGroupMembers返回参数结构体

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


class DeleteUserGroupsRequest(AbstractModel):
    r"""DeleteUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的用户组ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的用户组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
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
        :param _IdSet: 待删除的用户ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""待删除的用户ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
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


class Department(AbstractModel):
    r"""部门信息

    """

    def __init__(self):
        r"""
        :param _Id: 部门ID
        :type Id: str
        :param _Name: 部门名称，1 - 256个字符
        :type Name: str
        :param _Managers: 部门管理员账号ID
        :type Managers: list of str
        :param _ManagerUsers: 管理员用户
        :type ManagerUsers: list of DepartmentManagerUser
        """
        self._Id = None
        self._Name = None
        self._Managers = None
        self._ManagerUsers = None

    @property
    def Id(self):
        r"""部门ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""部门名称，1 - 256个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Managers(self):
        r"""部门管理员账号ID
        :rtype: list of str
        """
        return self._Managers

    @Managers.setter
    def Managers(self, Managers):
        self._Managers = Managers

    @property
    def ManagerUsers(self):
        r"""管理员用户
        :rtype: list of DepartmentManagerUser
        """
        return self._ManagerUsers

    @ManagerUsers.setter
    def ManagerUsers(self, ManagerUsers):
        self._ManagerUsers = ManagerUsers


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Managers = params.get("Managers")
        if params.get("ManagerUsers") is not None:
            self._ManagerUsers = []
            for item in params.get("ManagerUsers"):
                obj = DepartmentManagerUser()
                obj._deserialize(item)
                self._ManagerUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DepartmentManagerUser(AbstractModel):
    r"""部门管理员信息

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理员Id
        :type ManagerId: str
        :param _ManagerName: 管理员姓名
        :type ManagerName: str
        """
        self._ManagerId = None
        self._ManagerName = None

    @property
    def ManagerId(self):
        r"""管理员Id
        :rtype: str
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def ManagerName(self):
        r"""管理员姓名
        :rtype: str
        """
        return self._ManagerName

    @ManagerName.setter
    def ManagerName(self, ManagerName):
        self._ManagerName = ManagerName


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._ManagerName = params.get("ManagerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Departments(AbstractModel):
    r"""部门列表

    """

    def __init__(self):
        r"""
        :param _DepartmentSet: 部门列表
        :type DepartmentSet: list of Department
        :param _Enabled: 是否开启了部门管理 true - 已开启, false - 未开启
        :type Enabled: bool
        :param _RootManager: 当前操作UIN是否是根部门管理员
        :type RootManager: bool
        """
        self._DepartmentSet = None
        self._Enabled = None
        self._RootManager = None

    @property
    def DepartmentSet(self):
        r"""部门列表
        :rtype: list of Department
        """
        return self._DepartmentSet

    @DepartmentSet.setter
    def DepartmentSet(self, DepartmentSet):
        self._DepartmentSet = DepartmentSet

    @property
    def Enabled(self):
        r"""是否开启了部门管理 true - 已开启, false - 未开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RootManager(self):
        r"""当前操作UIN是否是根部门管理员
        :rtype: bool
        """
        return self._RootManager

    @RootManager.setter
    def RootManager(self, RootManager):
        self._RootManager = RootManager


    def _deserialize(self, params):
        if params.get("DepartmentSet") is not None:
            self._DepartmentSet = []
            for item in params.get("DepartmentSet"):
                obj = Department()
                obj._deserialize(item)
                self._DepartmentSet.append(obj)
        self._Enabled = params.get("Enabled")
        self._RootManager = params.get("RootManager")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployResourceRequest(AbstractModel):
    r"""DeployResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 需要开通服务的资源ID
        :type ResourceId: str
        :param _ApCode: 需要开通服务的地域
        :type ApCode: str
        :param _Zone: 子网所在可用区
        :type Zone: str
        :param _VpcId: 需要开通服务的VPC
        :type VpcId: str
        :param _SubnetId: 需要开通服务的子网ID
        :type SubnetId: str
        :param _CidrBlock: 需要开通服务的子网网段
        :type CidrBlock: str
        :param _VpcName: 需要开通服务的VPC名称
        :type VpcName: str
        :param _VpcCidrBlock: 需要开通服务的VPC对应的网段
        :type VpcCidrBlock: str
        :param _SubnetName: 需要开通服务的子网名称
        :type SubnetName: str
        :param _CdcClusterId: 需要开通实例所属的CDC集群ID
        :type CdcClusterId: str
        :param _ShareClbId: 开通堡垒机指定共享的clbId
        :type ShareClbId: str
        :param _WebAccess: 0-关闭web访问堡垒机，1-开启web访问堡垒机
        :type WebAccess: int
        :param _ClientAccess: 0-关闭客户端访问堡垒机，1-开启客户端访问堡垒机
        :type ClientAccess: int
        :param _IntranetAccess: 0-关闭内网访问堡垒机，1-开启内网访问堡垒机
        :type IntranetAccess: int
        :param _ExternalAccess: 0-关闭公网访问堡垒机，1-开启公网访问堡垒机
        :type ExternalAccess: int
        """
        self._ResourceId = None
        self._ApCode = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._CidrBlock = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._SubnetName = None
        self._CdcClusterId = None
        self._ShareClbId = None
        self._WebAccess = None
        self._ClientAccess = None
        self._IntranetAccess = None
        self._ExternalAccess = None

    @property
    def ResourceId(self):
        r"""需要开通服务的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ApCode(self):
        r"""需要开通服务的地域
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def Zone(self):
        r"""子网所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""需要开通服务的VPC
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""需要开通服务的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CidrBlock(self):
        r"""需要开通服务的子网网段
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def VpcName(self):
        r"""需要开通服务的VPC名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""需要开通服务的VPC对应的网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetName(self):
        r"""需要开通服务的子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CdcClusterId(self):
        r"""需要开通实例所属的CDC集群ID
        :rtype: str
        """
        return self._CdcClusterId

    @CdcClusterId.setter
    def CdcClusterId(self, CdcClusterId):
        self._CdcClusterId = CdcClusterId

    @property
    def ShareClbId(self):
        r"""开通堡垒机指定共享的clbId
        :rtype: str
        """
        return self._ShareClbId

    @ShareClbId.setter
    def ShareClbId(self, ShareClbId):
        self._ShareClbId = ShareClbId

    @property
    def WebAccess(self):
        r"""0-关闭web访问堡垒机，1-开启web访问堡垒机
        :rtype: int
        """
        return self._WebAccess

    @WebAccess.setter
    def WebAccess(self, WebAccess):
        self._WebAccess = WebAccess

    @property
    def ClientAccess(self):
        r"""0-关闭客户端访问堡垒机，1-开启客户端访问堡垒机
        :rtype: int
        """
        return self._ClientAccess

    @ClientAccess.setter
    def ClientAccess(self, ClientAccess):
        self._ClientAccess = ClientAccess

    @property
    def IntranetAccess(self):
        r"""0-关闭内网访问堡垒机，1-开启内网访问堡垒机
        :rtype: int
        """
        return self._IntranetAccess

    @IntranetAccess.setter
    def IntranetAccess(self, IntranetAccess):
        self._IntranetAccess = IntranetAccess

    @property
    def ExternalAccess(self):
        r"""0-关闭公网访问堡垒机，1-开启公网访问堡垒机
        :rtype: int
        """
        return self._ExternalAccess

    @ExternalAccess.setter
    def ExternalAccess(self, ExternalAccess):
        self._ExternalAccess = ExternalAccess


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ApCode = params.get("ApCode")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CidrBlock = params.get("CidrBlock")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetName = params.get("SubnetName")
        self._CdcClusterId = params.get("CdcClusterId")
        self._ShareClbId = params.get("ShareClbId")
        self._WebAccess = params.get("WebAccess")
        self._ClientAccess = params.get("ClientAccess")
        self._IntranetAccess = params.get("IntranetAccess")
        self._ExternalAccess = params.get("ExternalAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployResourceResponse(AbstractModel):
    r"""DeployResource返回参数结构体

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


class DescribeAccessWhiteListRulesRequest(AbstractModel):
    r"""DescribeAccessWhiteListRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 用户ID集合，非必需，如果使用IdSet参数则忽略Name参数
        :type IdSet: list of int non-negative
        :param _Name: 来源IP或网段，模糊查询，最大长度64字符
        :type Name: str
        :param _Offset: 分页偏移位置，默认0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def IdSet(self):
        r"""用户ID集合，非必需，如果使用IdSet参数则忽略Name参数
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""来源IP或网段，模糊查询，最大长度64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessWhiteListRulesResponse(AbstractModel):
    r"""DescribeAccessWhiteListRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _AccessWhiteListRuleSet: 访问白名单规则列表
        :type AccessWhiteListRuleSet: list of AccessWhiteListRule
        :param _AllowAny: 是否放开全部来源IP，如果为true，TotalCount为0，AccessWhiteListRuleSet为空
        :type AllowAny: bool
        :param _AllowAuto: 是否开启自动添加来源IP, 如果为true, 在开启访问白名单的情况下将自动添加来源IP
        :type AllowAuto: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccessWhiteListRuleSet = None
        self._AllowAny = None
        self._AllowAuto = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessWhiteListRuleSet(self):
        r"""访问白名单规则列表
        :rtype: list of AccessWhiteListRule
        """
        return self._AccessWhiteListRuleSet

    @AccessWhiteListRuleSet.setter
    def AccessWhiteListRuleSet(self, AccessWhiteListRuleSet):
        self._AccessWhiteListRuleSet = AccessWhiteListRuleSet

    @property
    def AllowAny(self):
        r"""是否放开全部来源IP，如果为true，TotalCount为0，AccessWhiteListRuleSet为空
        :rtype: bool
        """
        return self._AllowAny

    @AllowAny.setter
    def AllowAny(self, AllowAny):
        self._AllowAny = AllowAny

    @property
    def AllowAuto(self):
        r"""是否开启自动添加来源IP, 如果为true, 在开启访问白名单的情况下将自动添加来源IP
        :rtype: bool
        """
        return self._AllowAuto

    @AllowAuto.setter
    def AllowAuto(self, AllowAuto):
        self._AllowAuto = AllowAuto

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AccessWhiteListRuleSet") is not None:
            self._AccessWhiteListRuleSet = []
            for item in params.get("AccessWhiteListRuleSet"):
                obj = AccessWhiteListRule()
                obj._deserialize(item)
                self._AccessWhiteListRuleSet.append(obj)
        self._AllowAny = params.get("AllowAny")
        self._AllowAuto = params.get("AllowAuto")
        self._RequestId = params.get("RequestId")


class DescribeAccountGroupsRequest(AbstractModel):
    r"""DescribeAccountGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeepIn: 是否递归查询，0为不递归，1为递归
        :type DeepIn: int
        :param _ParentId: 父账号组ID, 默认0,查询根账号组下所有分组 
        :type ParentId: int
        :param _GroupName: 账号组名称，模糊查询
        :type GroupName: str
        :param _PageSize: 分页查询，每页条数
        :type PageSize: int
        :param _PageNum: 获取第几页的数据
        :type PageNum: int
        """
        self._DeepIn = None
        self._ParentId = None
        self._GroupName = None
        self._PageSize = None
        self._PageNum = None

    @property
    def DeepIn(self):
        r"""是否递归查询，0为不递归，1为递归
        :rtype: int
        """
        return self._DeepIn

    @DeepIn.setter
    def DeepIn(self, DeepIn):
        self._DeepIn = DeepIn

    @property
    def ParentId(self):
        r"""父账号组ID, 默认0,查询根账号组下所有分组 
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def GroupName(self):
        r"""账号组名称，模糊查询
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def PageSize(self):
        r"""分页查询，每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""获取第几页的数据
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._DeepIn = params.get("DeepIn")
        self._ParentId = params.get("ParentId")
        self._GroupName = params.get("GroupName")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountGroupsResponse(AbstractModel):
    r"""DescribeAccountGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 账号组总数
        :type TotalCount: int
        :param _AccountGroupSet: 账号组信息
        :type AccountGroupSet: list of AccountGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""账号组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountGroupSet(self):
        r"""账号组信息
        :rtype: list of AccountGroup
        """
        return self._AccountGroupSet

    @AccountGroupSet.setter
    def AccountGroupSet(self, AccountGroupSet):
        self._AccountGroupSet = AccountGroupSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountGroupSet") is not None:
            self._AccountGroupSet = []
            for item in params.get("AccountGroupSet"):
                obj = AccountGroup()
                obj._deserialize(item)
                self._AccountGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAclsRequest(AbstractModel):
    r"""DescribeAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 访问权限ID集合
        :type IdSet: list of int non-negative
        :param _Name: 访问权限名称，模糊查询，最长64字符
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20，最大500
        :type Limit: int
        :param _Exact: 是否根据Name进行精确查询，默认值false
        :type Exact: bool
        :param _AuthorizedUserIdSet: 有访问权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param _AuthorizedDeviceIdSet: 有访问权限的资产ID集合
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param _AuthorizedAppAssetIdSet: 有访问权限的应用资产ID集合
        :type AuthorizedAppAssetIdSet: list of int non-negative
        :param _Status: 访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :type Status: int
        :param _StatusSet: 访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :type StatusSet: list of int non-negative
        :param _DepartmentId: 部门ID，用于过滤属于某个部门的访问权限
        :type DepartmentId: str
        :param _ExactAccount: 是否根据AuthorizedDeviceIdSet,对资产账号进行精确匹配，默认false, 设置true时，确保AuthorizedDeviceIdSet只有一个元素
        :type ExactAccount: bool
        :param _Filters: 过滤数组
        :type Filters: list of Filter
        """
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._Exact = None
        self._AuthorizedUserIdSet = None
        self._AuthorizedDeviceIdSet = None
        self._AuthorizedAppAssetIdSet = None
        self._Status = None
        self._StatusSet = None
        self._DepartmentId = None
        self._ExactAccount = None
        self._Filters = None

    @property
    def IdSet(self):
        r"""访问权限ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""访问权限名称，模糊查询，最长64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Exact(self):
        r"""是否根据Name进行精确查询，默认值false
        :rtype: bool
        """
        return self._Exact

    @Exact.setter
    def Exact(self, Exact):
        self._Exact = Exact

    @property
    def AuthorizedUserIdSet(self):
        r"""有访问权限的用户ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedUserIdSet

    @AuthorizedUserIdSet.setter
    def AuthorizedUserIdSet(self, AuthorizedUserIdSet):
        self._AuthorizedUserIdSet = AuthorizedUserIdSet

    @property
    def AuthorizedDeviceIdSet(self):
        r"""有访问权限的资产ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedDeviceIdSet

    @AuthorizedDeviceIdSet.setter
    def AuthorizedDeviceIdSet(self, AuthorizedDeviceIdSet):
        self._AuthorizedDeviceIdSet = AuthorizedDeviceIdSet

    @property
    def AuthorizedAppAssetIdSet(self):
        r"""有访问权限的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedAppAssetIdSet

    @AuthorizedAppAssetIdSet.setter
    def AuthorizedAppAssetIdSet(self, AuthorizedAppAssetIdSet):
        self._AuthorizedAppAssetIdSet = AuthorizedAppAssetIdSet

    @property
    def Status(self):
        r"""访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusSet(self):
        r"""访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :rtype: list of int non-negative
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def DepartmentId(self):
        r"""部门ID，用于过滤属于某个部门的访问权限
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def ExactAccount(self):
        r"""是否根据AuthorizedDeviceIdSet,对资产账号进行精确匹配，默认false, 设置true时，确保AuthorizedDeviceIdSet只有一个元素
        :rtype: bool
        """
        return self._ExactAccount

    @ExactAccount.setter
    def ExactAccount(self, ExactAccount):
        self._ExactAccount = ExactAccount

    @property
    def Filters(self):
        r"""过滤数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Exact = params.get("Exact")
        self._AuthorizedUserIdSet = params.get("AuthorizedUserIdSet")
        self._AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self._AuthorizedAppAssetIdSet = params.get("AuthorizedAppAssetIdSet")
        self._Status = params.get("Status")
        self._StatusSet = params.get("StatusSet")
        self._DepartmentId = params.get("DepartmentId")
        self._ExactAccount = params.get("ExactAccount")
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
        


class DescribeAclsResponse(AbstractModel):
    r"""DescribeAcls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 访问权限总数
        :type TotalCount: int
        :param _AclSet: 访问权限列表
        :type AclSet: list of Acl
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AclSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""访问权限总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclSet(self):
        r"""访问权限列表
        :rtype: list of Acl
        """
        return self._AclSet

    @AclSet.setter
    def AclSet(self, AclSet):
        self._AclSet = AclSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AclSet") is not None:
            self._AclSet = []
            for item in params.get("AclSet"):
                obj = Acl()
                obj._deserialize(item)
                self._AclSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetSyncFlagRequest(AbstractModel):
    r"""DescribeAssetSyncFlag请求参数结构体

    """


class DescribeAssetSyncFlagResponse(AbstractModel):
    r"""DescribeAssetSyncFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetSyncFlags: 资产同步标志
        :type AssetSyncFlags: :class:`tencentcloud.bh.v20230418.models.AssetSyncFlags`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetSyncFlags = None
        self._RequestId = None

    @property
    def AssetSyncFlags(self):
        r"""资产同步标志
        :rtype: :class:`tencentcloud.bh.v20230418.models.AssetSyncFlags`
        """
        return self._AssetSyncFlags

    @AssetSyncFlags.setter
    def AssetSyncFlags(self, AssetSyncFlags):
        self._AssetSyncFlags = AssetSyncFlags

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
        if params.get("AssetSyncFlags") is not None:
            self._AssetSyncFlags = AssetSyncFlags()
            self._AssetSyncFlags._deserialize(params.get("AssetSyncFlags"))
        self._RequestId = params.get("RequestId")


class DescribeAssetSyncStatusRequest(AbstractModel):
    r"""DescribeAssetSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Category: 查询的资产同步类型。1 -主机资产， 2 - 数据库资产
        :type Category: int
        """
        self._Category = None

    @property
    def Category(self):
        r"""查询的资产同步类型。1 -主机资产， 2 - 数据库资产
        :rtype: int
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetSyncStatusResponse(AbstractModel):
    r"""DescribeAssetSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 资产同步结果
        :type Status: :class:`tencentcloud.bh.v20230418.models.AssetSyncStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""资产同步结果
        :rtype: :class:`tencentcloud.bh.v20230418.models.AssetSyncStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Status") is not None:
            self._Status = AssetSyncStatus()
            self._Status._deserialize(params.get("Status"))
        self._RequestId = params.get("RequestId")


class DescribeChangePwdTaskDetailRequest(AbstractModel):
    r"""DescribeChangePwdTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationId: 改密任务Id
        :type OperationId: str
        :param _DepartmentId: 所属部门ID，如：“1.2.3”
        :type DepartmentId: str
        :param _Filters: 过滤数组，支持：InstanceId 资产ID，DeviceName 资产名称，Ip 内外IP，Account 资产账号，LastChangeStatus 上次改密状态。
        :type Filters: list of Filter
        :param _Offset: 分页偏移位置，默认0
        :type Offset: int
        :param _Limit: 每页条目。默认20
        :type Limit: int
        """
        self._OperationId = None
        self._DepartmentId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def OperationId(self):
        r"""改密任务Id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DepartmentId(self):
        r"""所属部门ID，如：“1.2.3”
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Filters(self):
        r"""过滤数组，支持：InstanceId 资产ID，DeviceName 资产名称，Ip 内外IP，Account 资产账号，LastChangeStatus 上次改密状态。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""分页偏移位置，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目。默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._OperationId = params.get("OperationId")
        self._DepartmentId = params.get("DepartmentId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChangePwdTaskDetailResponse(AbstractModel):
    r"""DescribeChangePwdTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Details: 任务详情
        :type Details: list of ChangePwdTaskDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""任务详情
        :rtype: list of ChangePwdTaskDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ChangePwdTaskDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChangePwdTaskRequest(AbstractModel):
    r"""DescribeChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤数组。过滤数组。Name支持以下值: OperationId 任务ID TaskName 任务名
        :type Filters: list of Filter
        :param _DepartmentId: 所属部门ID
        :type DepartmentId: str
        :param _Offset: 分页偏移量，默认0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self._Filters = None
        self._DepartmentId = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""过滤数组。过滤数组。Name支持以下值: OperationId 任务ID TaskName 任务名
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DepartmentId(self):
        r"""所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Offset(self):
        r"""分页偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DepartmentId = params.get("DepartmentId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChangePwdTaskResponse(AbstractModel):
    r"""DescribeChangePwdTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务详情
        :type Tasks: list of ChangePwdTaskInfo
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""任务详情
        :rtype: list of ChangePwdTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        r"""任务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ChangePwdTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCmdTemplatesRequest(AbstractModel):
    r"""DescribeCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 命令模板ID集合，非必需
        :type IdSet: list of int non-negative
        :param _Name: 命令模板名，模糊查询，最大长度64字符
        :type Name: str
        :param _Type: 命令模板类型 1-内置模板 2-自定义模板
        :type Type: int
        :param _TypeSet: 命令模板类型 1-内置模板 2-自定义模板
        :type TypeSet: list of int non-negative
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self._IdSet = None
        self._Name = None
        self._Type = None
        self._TypeSet = None
        self._Offset = None
        self._Limit = None

    @property
    def IdSet(self):
        r"""命令模板ID集合，非必需
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""命令模板名，模糊查询，最大长度64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""命令模板类型 1-内置模板 2-自定义模板
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeSet(self):
        r"""命令模板类型 1-内置模板 2-自定义模板
        :rtype: list of int non-negative
        """
        return self._TypeSet

    @TypeSet.setter
    def TypeSet(self, TypeSet):
        self._TypeSet = TypeSet

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._TypeSet = params.get("TypeSet")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmdTemplatesResponse(AbstractModel):
    r"""DescribeCmdTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdTemplateSet: 命令模板列表
        :type CmdTemplateSet: list of CmdTemplate
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CmdTemplateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CmdTemplateSet(self):
        r"""命令模板列表
        :rtype: list of CmdTemplate
        """
        return self._CmdTemplateSet

    @CmdTemplateSet.setter
    def CmdTemplateSet(self, CmdTemplateSet):
        self._CmdTemplateSet = CmdTemplateSet

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("CmdTemplateSet") is not None:
            self._CmdTemplateSet = []
            for item in params.get("CmdTemplateSet"):
                obj = CmdTemplate()
                obj._deserialize(item)
                self._CmdTemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDepartmentsRequest(AbstractModel):
    r"""DescribeDepartments请求参数结构体

    """


class DescribeDepartmentsResponse(AbstractModel):
    r"""DescribeDepartments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Departments: 部门列表
        :type Departments: :class:`tencentcloud.bh.v20230418.models.Departments`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Departments = None
        self._RequestId = None

    @property
    def Departments(self):
        r"""部门列表
        :rtype: :class:`tencentcloud.bh.v20230418.models.Departments`
        """
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments

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
        if params.get("Departments") is not None:
            self._Departments = Departments()
            self._Departments._deserialize(params.get("Departments"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceAccountsRequest(AbstractModel):
    r"""DescribeDeviceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 主机账号ID集合，非必需，如果使用IdSet则忽略其他过滤参数
        :type IdSet: list of int non-negative
        :param _Account: 主机账号名，模糊查询，不能单独出现，必须于DeviceId一起提交
        :type Account: str
        :param _DeviceId: 主机ID，未使用IdSet时必须携带
        :type DeviceId: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self._IdSet = None
        self._Account = None
        self._DeviceId = None
        self._Offset = None
        self._Limit = None

    @property
    def IdSet(self):
        r"""主机账号ID集合，非必需，如果使用IdSet则忽略其他过滤参数
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Account(self):
        r"""主机账号名，模糊查询，不能单独出现，必须于DeviceId一起提交
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DeviceId(self):
        r"""主机ID，未使用IdSet时必须携带
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Account = params.get("Account")
        self._DeviceId = params.get("DeviceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceAccountsResponse(AbstractModel):
    r"""DescribeDeviceAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _DeviceAccountSet: 账号信息列表
        :type DeviceAccountSet: list of DeviceAccount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceAccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceAccountSet(self):
        r"""账号信息列表
        :rtype: list of DeviceAccount
        """
        return self._DeviceAccountSet

    @DeviceAccountSet.setter
    def DeviceAccountSet(self, DeviceAccountSet):
        self._DeviceAccountSet = DeviceAccountSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceAccountSet") is not None:
            self._DeviceAccountSet = []
            for item in params.get("DeviceAccountSet"):
                obj = DeviceAccount()
                obj._deserialize(item)
                self._DeviceAccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupMembersRequest(AbstractModel):
    r"""DescribeDeviceGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bound: true - 查询已在该资产组的资产，false - 查询未在该资产组的资产
        :type Bound: bool
        :param _Id: 资产组ID，Id和IdSet二选一
        :type Id: int
        :param _IdSet: 资产组ID集合，传Id，IdSet不生效。
        :type IdSet: list of int non-negative
        :param _Name: 资产名或资产IP，模糊查询
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数，默认20, 最大500
        :type Limit: int
        :param _Kind: 资产类型，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :type Kind: int
        :param _KindSet: 资产类型集合，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :type KindSet: list of int non-negative
        :param _DepartmentId: 所属部门ID
        :type DepartmentId: str
        :param _TagFilters: 过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :type TagFilters: list of TagFilter
        """
        self._Bound = None
        self._Id = None
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._Kind = None
        self._KindSet = None
        self._DepartmentId = None
        self._TagFilters = None

    @property
    def Bound(self):
        r"""true - 查询已在该资产组的资产，false - 查询未在该资产组的资产
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def Id(self):
        r"""资产组ID，Id和IdSet二选一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IdSet(self):
        r"""资产组ID集合，传Id，IdSet不生效。
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""资产名或资产IP，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Kind(self):
        r"""资产类型，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def KindSet(self):
        r"""资产类型集合，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :rtype: list of int non-negative
        """
        return self._KindSet

    @KindSet.setter
    def KindSet(self, KindSet):
        self._KindSet = KindSet

    @property
    def DepartmentId(self):
        r"""所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def TagFilters(self):
        r"""过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Bound = params.get("Bound")
        self._Id = params.get("Id")
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Kind = params.get("Kind")
        self._KindSet = params.get("KindSet")
        self._DepartmentId = params.get("DepartmentId")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupMembersResponse(AbstractModel):
    r"""DescribeDeviceGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资产组成员总数
        :type TotalCount: int
        :param _DeviceSet: 资产组成员列表
        :type DeviceSet: list of Device
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""资产组成员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceSet(self):
        r"""资产组成员列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupsRequest(AbstractModel):
    r"""DescribeDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 资产组ID集合
        :type IdSet: list of int non-negative
        :param _Name: 资产组名，最长64个字符，模糊查询
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，缺省20，最大500
        :type Limit: int
        :param _DepartmentId: 部门ID，用于过滤属于某个部门的资产组
        :type DepartmentId: str
        """
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._DepartmentId = None

    @property
    def IdSet(self):
        r"""资产组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""资产组名，最长64个字符，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，缺省20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        r"""部门ID，用于过滤属于某个部门的资产组
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupsResponse(AbstractModel):
    r"""DescribeDeviceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资产组总数
        :type TotalCount: int
        :param _GroupSet: 资产组列表
        :type GroupSet: list of Group
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._GroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""资产组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupSet(self):
        r"""资产组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    r"""DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 资产ID集合
        :type IdSet: list of int non-negative
        :param _Name: 资产名或资产IP，模糊查询
        :type Name: str
        :param _Ip: 暂未使用
        :type Ip: str
        :param _ApCodeSet: 地域码集合
        :type ApCodeSet: list of str
        :param _Kind: 操作系统类型, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type Kind: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        :param _AuthorizedUserIdSet: 有该资产访问权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param _ResourceIdSet: 过滤条件，资产绑定的堡垒机服务ID集合
        :type ResourceIdSet: list of str
        :param _KindSet: 可提供按照多种类型过滤, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type KindSet: list of int non-negative
        :param _ManagedAccount: 资产是否包含托管账号。1，包含；0，不包含
        :type ManagedAccount: str
        :param _DepartmentId: 过滤条件，可按照部门ID进行过滤
        :type DepartmentId: str
        :param _AccountIdSet: 资产所属云账号id
        :type AccountIdSet: list of int non-negative
        :param _ProviderTypeSet: 云厂商类型，1-腾讯云，2-阿里云
        :type ProviderTypeSet: list of int non-negative
        :param _CloudDeviceStatusSet: 同步的云资产状态，标记同步的资产的状态情况，0-已删除,1-正常,2-已隔离,3-已过期
        :type CloudDeviceStatusSet: list of int non-negative
        :param _TagFilters: 过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :type TagFilters: list of TagFilter
        :param _Filters: 过滤数组。支持的Name：
BindingStatus 绑定状态
        :type Filters: list of Filter
        """
        self._IdSet = None
        self._Name = None
        self._Ip = None
        self._ApCodeSet = None
        self._Kind = None
        self._Offset = None
        self._Limit = None
        self._AuthorizedUserIdSet = None
        self._ResourceIdSet = None
        self._KindSet = None
        self._ManagedAccount = None
        self._DepartmentId = None
        self._AccountIdSet = None
        self._ProviderTypeSet = None
        self._CloudDeviceStatusSet = None
        self._TagFilters = None
        self._Filters = None

    @property
    def IdSet(self):
        r"""资产ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""资产名或资产IP，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ip(self):
        r"""暂未使用
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ApCodeSet(self):
        r"""地域码集合
        :rtype: list of str
        """
        return self._ApCodeSet

    @ApCodeSet.setter
    def ApCodeSet(self, ApCodeSet):
        self._ApCodeSet = ApCodeSet

    @property
    def Kind(self):
        r"""操作系统类型, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AuthorizedUserIdSet(self):
        r"""有该资产访问权限的用户ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedUserIdSet

    @AuthorizedUserIdSet.setter
    def AuthorizedUserIdSet(self, AuthorizedUserIdSet):
        self._AuthorizedUserIdSet = AuthorizedUserIdSet

    @property
    def ResourceIdSet(self):
        r"""过滤条件，资产绑定的堡垒机服务ID集合
        :rtype: list of str
        """
        return self._ResourceIdSet

    @ResourceIdSet.setter
    def ResourceIdSet(self, ResourceIdSet):
        self._ResourceIdSet = ResourceIdSet

    @property
    def KindSet(self):
        r"""可提供按照多种类型过滤, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: list of int non-negative
        """
        return self._KindSet

    @KindSet.setter
    def KindSet(self, KindSet):
        self._KindSet = KindSet

    @property
    def ManagedAccount(self):
        r"""资产是否包含托管账号。1，包含；0，不包含
        :rtype: str
        """
        return self._ManagedAccount

    @ManagedAccount.setter
    def ManagedAccount(self, ManagedAccount):
        self._ManagedAccount = ManagedAccount

    @property
    def DepartmentId(self):
        r"""过滤条件，可按照部门ID进行过滤
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def AccountIdSet(self):
        r"""资产所属云账号id
        :rtype: list of int non-negative
        """
        return self._AccountIdSet

    @AccountIdSet.setter
    def AccountIdSet(self, AccountIdSet):
        self._AccountIdSet = AccountIdSet

    @property
    def ProviderTypeSet(self):
        r"""云厂商类型，1-腾讯云，2-阿里云
        :rtype: list of int non-negative
        """
        return self._ProviderTypeSet

    @ProviderTypeSet.setter
    def ProviderTypeSet(self, ProviderTypeSet):
        self._ProviderTypeSet = ProviderTypeSet

    @property
    def CloudDeviceStatusSet(self):
        r"""同步的云资产状态，标记同步的资产的状态情况，0-已删除,1-正常,2-已隔离,3-已过期
        :rtype: list of int non-negative
        """
        return self._CloudDeviceStatusSet

    @CloudDeviceStatusSet.setter
    def CloudDeviceStatusSet(self, CloudDeviceStatusSet):
        self._CloudDeviceStatusSet = CloudDeviceStatusSet

    @property
    def TagFilters(self):
        r"""过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Filters(self):
        r"""过滤数组。支持的Name：
BindingStatus 绑定状态
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Ip = params.get("Ip")
        self._ApCodeSet = params.get("ApCodeSet")
        self._Kind = params.get("Kind")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AuthorizedUserIdSet = params.get("AuthorizedUserIdSet")
        self._ResourceIdSet = params.get("ResourceIdSet")
        self._KindSet = params.get("KindSet")
        self._ManagedAccount = params.get("ManagedAccount")
        self._DepartmentId = params.get("DepartmentId")
        self._AccountIdSet = params.get("AccountIdSet")
        self._ProviderTypeSet = params.get("ProviderTypeSet")
        self._CloudDeviceStatusSet = params.get("CloudDeviceStatusSet")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
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
        


class DescribeDevicesResponse(AbstractModel):
    r"""DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资产总数
        :type TotalCount: int
        :param _DeviceSet: 资产信息列表
        :type DeviceSet: list of Device
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""资产总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceSet(self):
        r"""资产信息列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    r"""DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条目数量，默认20，最大500
        :type Limit: int
        :param _Filters: 过滤数组
        :type Filters: list of Filter
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        """
        self._Limit = None
        self._Filters = None
        self._Offset = None

    @property
    def Limit(self):
        r"""每页条目数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    r"""DescribeDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 网络域总数
        :type TotalCount: int
        :param _DomainSet: 网络域列表
        :type DomainSet: list of Domain
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DomainSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""网络域总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DomainSet(self):
        r"""网络域列表
        :rtype: list of Domain
        """
        return self._DomainSet

    @DomainSet.setter
    def DomainSet(self, DomainSet):
        self._DomainSet = DomainSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self._DomainSet = []
            for item in params.get("DomainSet"):
                obj = Domain()
                obj._deserialize(item)
                self._DomainSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLDAPUnitSetRequest(AbstractModel):
    r"""DescribeLDAPUnitSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启LDAP认证，true-开启
        :type Enable: bool
        :param _Ip: 服务器地址
        :type Ip: str
        :param _Port: 服务端口
        :type Port: int
        :param _EnableSSL: 是否开启SSL，false-不开启，true-开启
        :type EnableSSL: bool
        :param _BaseDN: Base DN
        :type BaseDN: str
        :param _AdminAccount: 管理员账号
        :type AdminAccount: str
        :param _AdminPassword: 管理员密码
        :type AdminPassword: str
        :param _AttributeUserName: 用户名映射属性
        :type AttributeUserName: str
        :param _AttributeUnit: 部门过滤
        :type AttributeUnit: str
        :param _IpBackup: 备用服务器地址
        :type IpBackup: str
        :param _DomainId: 网络域Id
        :type DomainId: str
        """
        self._Enable = None
        self._Ip = None
        self._Port = None
        self._EnableSSL = None
        self._BaseDN = None
        self._AdminAccount = None
        self._AdminPassword = None
        self._AttributeUserName = None
        self._AttributeUnit = None
        self._IpBackup = None
        self._DomainId = None

    @property
    def Enable(self):
        r"""是否开启LDAP认证，true-开启
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Ip(self):
        r"""服务器地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""服务端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EnableSSL(self):
        r"""是否开启SSL，false-不开启，true-开启
        :rtype: bool
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def BaseDN(self):
        r"""Base DN
        :rtype: str
        """
        return self._BaseDN

    @BaseDN.setter
    def BaseDN(self, BaseDN):
        self._BaseDN = BaseDN

    @property
    def AdminAccount(self):
        r"""管理员账号
        :rtype: str
        """
        return self._AdminAccount

    @AdminAccount.setter
    def AdminAccount(self, AdminAccount):
        self._AdminAccount = AdminAccount

    @property
    def AdminPassword(self):
        r"""管理员密码
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def AttributeUserName(self):
        r"""用户名映射属性
        :rtype: str
        """
        return self._AttributeUserName

    @AttributeUserName.setter
    def AttributeUserName(self, AttributeUserName):
        self._AttributeUserName = AttributeUserName

    @property
    def AttributeUnit(self):
        r"""部门过滤
        :rtype: str
        """
        return self._AttributeUnit

    @AttributeUnit.setter
    def AttributeUnit(self, AttributeUnit):
        self._AttributeUnit = AttributeUnit

    @property
    def IpBackup(self):
        r"""备用服务器地址
        :rtype: str
        """
        return self._IpBackup

    @IpBackup.setter
    def IpBackup(self, IpBackup):
        self._IpBackup = IpBackup

    @property
    def DomainId(self):
        r"""网络域Id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._EnableSSL = params.get("EnableSSL")
        self._BaseDN = params.get("BaseDN")
        self._AdminAccount = params.get("AdminAccount")
        self._AdminPassword = params.get("AdminPassword")
        self._AttributeUserName = params.get("AttributeUserName")
        self._AttributeUnit = params.get("AttributeUnit")
        self._IpBackup = params.get("IpBackup")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLDAPUnitSetResponse(AbstractModel):
    r"""DescribeLDAPUnitSet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitSet: ou 列表
        :type UnitSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnitSet = None
        self._RequestId = None

    @property
    def UnitSet(self):
        r"""ou 列表
        :rtype: list of str
        """
        return self._UnitSet

    @UnitSet.setter
    def UnitSet(self, UnitSet):
        self._UnitSet = UnitSet

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
        self._UnitSet = params.get("UnitSet")
        self._RequestId = params.get("RequestId")


class DescribeLoginEventRequest(AbstractModel):
    r"""DescribeLoginEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :type UserName: str
        :param _RealName: 姓名，模糊查询
        :type RealName: str
        :param _StartTime: 查询时间范围，起始时间
        :type StartTime: str
        :param _EndTime: 查询时间范围，结束时间
        :type EndTime: str
        :param _SourceIp: 来源IP，模糊查询
        :type SourceIp: str
        :param _Entry: 登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :type Entry: int
        :param _EntrySet: 登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :type EntrySet: list of int non-negative
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
        :param _ResultSet: 操作结果，1-成功，2-失败
        :type ResultSet: list of int non-negative
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 分页每页记录数，默认20
        :type Limit: int
        """
        self._UserName = None
        self._RealName = None
        self._StartTime = None
        self._EndTime = None
        self._SourceIp = None
        self._Entry = None
        self._EntrySet = None
        self._Result = None
        self._ResultSet = None
        self._Offset = None
        self._Limit = None

    @property
    def UserName(self):
        r"""用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""姓名，模糊查询
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def StartTime(self):
        r"""查询时间范围，起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询时间范围，结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SourceIp(self):
        r"""来源IP，模糊查询
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Entry(self):
        r"""登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :rtype: int
        """
        return self._Entry

    @Entry.setter
    def Entry(self, Entry):
        self._Entry = Entry

    @property
    def EntrySet(self):
        r"""登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :rtype: list of int non-negative
        """
        return self._EntrySet

    @EntrySet.setter
    def EntrySet(self, EntrySet):
        self._EntrySet = EntrySet

    @property
    def Result(self):
        r"""操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultSet(self):
        r"""操作结果，1-成功，2-失败
        :rtype: list of int non-negative
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页每页记录数，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SourceIp = params.get("SourceIp")
        self._Entry = params.get("Entry")
        self._EntrySet = params.get("EntrySet")
        self._Result = params.get("Result")
        self._ResultSet = params.get("ResultSet")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginEventResponse(AbstractModel):
    r"""DescribeLoginEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginEventSet: 登录日志列表
        :type LoginEventSet: list of LoginEvent
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginEventSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LoginEventSet(self):
        r"""登录日志列表
        :rtype: list of LoginEvent
        """
        return self._LoginEventSet

    @LoginEventSet.setter
    def LoginEventSet(self, LoginEventSet):
        self._LoginEventSet = LoginEventSet

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("LoginEventSet") is not None:
            self._LoginEventSet = []
            for item in params.get("LoginEventSet"):
                obj = LoginEvent()
                obj._deserialize(item)
                self._LoginEventSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOperationEventRequest(AbstractModel):
    r"""DescribeOperationEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :type UserName: str
        :param _RealName: 姓名，模糊查询
        :type RealName: str
        :param _StartTime: 查询时间范围，起始时间
        :type StartTime: str
        :param _EndTime: 查询时间范围，结束时间
        :type EndTime: str
        :param _SourceIp: 来源IP，模糊查询
        :type SourceIp: str
        :param _Kind: 操作类型，参考DescribeOperationType返回结果
        :type Kind: int
        :param _KindSet: 操作类型，参考DescribeOperationType返回结果
        :type KindSet: list of int non-negative
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
        :param _ResultSet: 操作结果，1-成功，2-失败
        :type ResultSet: list of int non-negative
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 分页每页记录数，默认20
        :type Limit: int
        """
        self._UserName = None
        self._RealName = None
        self._StartTime = None
        self._EndTime = None
        self._SourceIp = None
        self._Kind = None
        self._KindSet = None
        self._Result = None
        self._ResultSet = None
        self._Offset = None
        self._Limit = None

    @property
    def UserName(self):
        r"""用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""姓名，模糊查询
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def StartTime(self):
        r"""查询时间范围，起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询时间范围，结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SourceIp(self):
        r"""来源IP，模糊查询
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Kind(self):
        r"""操作类型，参考DescribeOperationType返回结果
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def KindSet(self):
        r"""操作类型，参考DescribeOperationType返回结果
        :rtype: list of int non-negative
        """
        return self._KindSet

    @KindSet.setter
    def KindSet(self, KindSet):
        self._KindSet = KindSet

    @property
    def Result(self):
        r"""操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ResultSet(self):
        r"""操作结果，1-成功，2-失败
        :rtype: list of int non-negative
        """
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页每页记录数，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SourceIp = params.get("SourceIp")
        self._Kind = params.get("Kind")
        self._KindSet = params.get("KindSet")
        self._Result = params.get("Result")
        self._ResultSet = params.get("ResultSet")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOperationEventResponse(AbstractModel):
    r"""DescribeOperationEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationEventSet: 操作日志列表
        :type OperationEventSet: list of OperationEvent
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperationEventSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def OperationEventSet(self):
        r"""操作日志列表
        :rtype: list of OperationEvent
        """
        return self._OperationEventSet

    @OperationEventSet.setter
    def OperationEventSet(self, OperationEventSet):
        self._OperationEventSet = OperationEventSet

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("OperationEventSet") is not None:
            self._OperationEventSet = []
            for item in params.get("OperationEventSet"):
                obj = OperationEvent()
                obj._deserialize(item)
                self._OperationEventSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOperationTaskRequest(AbstractModel):
    r"""DescribeOperationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 运维任务名称
        :type Name: str
        :param _Type: 运维任务类型，1 - 手工执行任务， 2 - 周期性任务
        :type Type: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数，默认20
        :type Limit: int
        """
        self._Name = None
        self._Type = None
        self._Offset = None
        self._Limit = None

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""运维任务类型，1 - 手工执行任务， 2 - 周期性任务
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOperationTaskResponse(AbstractModel):
    r"""DescribeOperationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationTasks: 运维任务列表
        :type OperationTasks: list of OperationTask
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperationTasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def OperationTasks(self):
        r"""运维任务列表
        :rtype: list of OperationTask
        """
        return self._OperationTasks

    @OperationTasks.setter
    def OperationTasks(self, OperationTasks):
        self._OperationTasks = OperationTasks

    @property
    def TotalCount(self):
        r"""任务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("OperationTasks") is not None:
            self._OperationTasks = []
            for item in params.get("OperationTasks"):
                obj = OperationTask()
                obj._deserialize(item)
                self._OperationTasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    r"""DescribeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApCode: 地域码, 如: ap-guangzhou
        :type ApCode: str
        :param _VpcId: 按照堡垒机开通的 VPC 实例ID查询
        :type VpcId: str
        :param _ResourceIds: 资源ID集合，当传入ID集合时忽略 ApCode 和 VpcId
        :type ResourceIds: list of str
        :param _Limit: 每页条目数量
        :type Limit: int
        :param _Offset: 分页偏移位置
        :type Offset: int
        """
        self._ApCode = None
        self._VpcId = None
        self._ResourceIds = None
        self._Limit = None
        self._Offset = None

    @property
    def ApCode(self):
        r"""地域码, 如: ap-guangzhou
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def VpcId(self):
        r"""按照堡垒机开通的 VPC 实例ID查询
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ResourceIds(self):
        r"""资源ID集合，当传入ID集合时忽略 ApCode 和 VpcId
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Limit(self):
        r"""每页条目数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ApCode = params.get("ApCode")
        self._VpcId = params.get("VpcId")
        self._ResourceIds = params.get("ResourceIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesResponse(AbstractModel):
    r"""DescribeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSet: 堡垒机资源列表
        :type ResourceSet: list of Resource
        :param _TotalCount: 堡垒机资源数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResourceSet(self):
        r"""堡垒机资源列表
        :rtype: list of Resource
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def TotalCount(self):
        r"""堡垒机资源数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecuritySettingRequest(AbstractModel):
    r"""DescribeSecuritySetting请求参数结构体

    """


class DescribeSecuritySettingResponse(AbstractModel):
    r"""DescribeSecuritySetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecuritySetting: 无
        :type SecuritySetting: :class:`tencentcloud.bh.v20230418.models.SecuritySetting`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecuritySetting = None
        self._RequestId = None

    @property
    def SecuritySetting(self):
        r"""无
        :rtype: :class:`tencentcloud.bh.v20230418.models.SecuritySetting`
        """
        return self._SecuritySetting

    @SecuritySetting.setter
    def SecuritySetting(self, SecuritySetting):
        self._SecuritySetting = SecuritySetting

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
        if params.get("SecuritySetting") is not None:
            self._SecuritySetting = SecuritySetting()
            self._SecuritySetting._deserialize(params.get("SecuritySetting"))
        self._RequestId = params.get("RequestId")


class DescribeSourceTypesRequest(AbstractModel):
    r"""DescribeSourceTypes请求参数结构体

    """


class DescribeSourceTypesResponse(AbstractModel):
    r"""DescribeSourceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 认证源总数
        :type TotalCount: int
        :param _SourceTypeSet: 认证源信息
        :type SourceTypeSet: list of SourceType
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SourceTypeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""认证源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SourceTypeSet(self):
        r"""认证源信息
        :rtype: list of SourceType
        """
        return self._SourceTypeSet

    @SourceTypeSet.setter
    def SourceTypeSet(self, SourceTypeSet):
        self._SourceTypeSet = SourceTypeSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SourceTypeSet") is not None:
            self._SourceTypeSet = []
            for item in params.get("SourceTypeSet"):
                obj = SourceType()
                obj._deserialize(item)
                self._SourceTypeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserDirectoryRequest(AbstractModel):
    r"""DescribeUserDirectory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移
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
        


class DescribeUserDirectoryResponse(AbstractModel):
    r"""DescribeUserDirectory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserDirSet: 用户目录集
        :type UserDirSet: list of UserDirectory
        :param _TotalCount: 用户目录集总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserDirSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UserDirSet(self):
        r"""用户目录集
        :rtype: list of UserDirectory
        """
        return self._UserDirSet

    @UserDirSet.setter
    def UserDirSet(self, UserDirSet):
        self._UserDirSet = UserDirSet

    @property
    def TotalCount(self):
        r"""用户目录集总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("UserDirSet") is not None:
            self._UserDirSet = []
            for item in params.get("UserDirSet"):
                obj = UserDirectory()
                obj._deserialize(item)
                self._UserDirSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserGroupMembersRequest(AbstractModel):
    r"""DescribeUserGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 用户组ID
        :type Id: int
        :param _Bound: true - 查询已添加到该用户组的用户，false - 查询未添加到该用户组的用户
        :type Bound: bool
        :param _Name: 用户名或用户姓名，最长64个字符，模糊查询
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20, 最大500
        :type Limit: int
        :param _DepartmentId: 所属部门ID
        :type DepartmentId: str
        """
        self._Id = None
        self._Bound = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._DepartmentId = None

    @property
    def Id(self):
        r"""用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Bound(self):
        r"""true - 查询已添加到该用户组的用户，false - 查询未添加到该用户组的用户
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def Name(self):
        r"""用户名或用户姓名，最长64个字符，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        r"""所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Bound = params.get("Bound")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupMembersResponse(AbstractModel):
    r"""DescribeUserGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户组成员总数
        :type TotalCount: int
        :param _UserSet: 用户组成员列表
        :type UserSet: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""用户组成员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserSet(self):
        r"""用户组成员列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserGroupsRequest(AbstractModel):
    r"""DescribeUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 用户组ID集合
        :type IdSet: list of int non-negative
        :param _Name: 用户组名，模糊查询,长度：0-64字符
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，缺省20，最大500
        :type Limit: int
        :param _DepartmentId: 部门ID，用于过滤属于某个部门的用户组
        :type DepartmentId: str
        """
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._DepartmentId = None

    @property
    def IdSet(self):
        r"""用户组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""用户组名，模糊查询,长度：0-64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，缺省20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        r"""部门ID，用于过滤属于某个部门的用户组
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserGroupsResponse(AbstractModel):
    r"""DescribeUserGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户组总数
        :type TotalCount: int
        :param _GroupSet: 用户组列表
        :type GroupSet: list of Group
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._GroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""用户组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupSet(self):
        r"""用户组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserSyncStatusRequest(AbstractModel):
    r"""DescribeUserSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserKind: 获取用户同步状态， 1-获取ioa用户同步状态
        :type UserKind: int
        """
        self._UserKind = None

    @property
    def UserKind(self):
        r"""获取用户同步状态， 1-获取ioa用户同步状态
        :rtype: int
        """
        return self._UserKind

    @UserKind.setter
    def UserKind(self, UserKind):
        self._UserKind = UserKind


    def _deserialize(self, params):
        self._UserKind = params.get("UserKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSyncStatusResponse(AbstractModel):
    r"""DescribeUserSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 用户同步状态
        :type Status: :class:`tencentcloud.bh.v20230418.models.AssetSyncStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""用户同步状态
        :rtype: :class:`tencentcloud.bh.v20230418.models.AssetSyncStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Status") is not None:
            self._Status = AssetSyncStatus()
            self._Status._deserialize(params.get("Status"))
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    r"""DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 如果IdSet不为空，则忽略其他参数
        :type IdSet: list of int non-negative
        :param _Name: 模糊查询，IdSet、UserName、Phone为空时才生效，对用户名和姓名进行模糊查询
        :type Name: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20, 最大500
        :type Limit: int
        :param _UserName: 精确查询，IdSet为空时才生效
        :type UserName: str
        :param _Phone: 精确查询，IdSet、UserName为空时才生效。
大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param _Email: 邮箱，精确查询
        :type Email: str
        :param _AuthorizedDeviceIdSet: 查询具有指定资产ID访问权限的用户
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param _AuthorizedAppAssetIdSet: 查询具有指定应用资产ID访问权限的用户
        :type AuthorizedAppAssetIdSet: list of int non-negative
        :param _AuthTypeSet: 认证方式，0 - 本地, 1 - LDAP, 2 - OAuth, 3-ioa 不传为全部
        :type AuthTypeSet: list of int non-negative
        :param _DepartmentId: 部门ID，用于过滤属于某个部门的用户
        :type DepartmentId: str
        :param _Filters: 参数过滤数组

        :type Filters: list of Filter
        :param _IsCamUser: 是否获取cam用户, 0-否，1-是
        :type IsCamUser: int
        :param _UserFromSet: 用户来源，0-bh，1-ioa,不传为全部
        :type UserFromSet: list of int non-negative
        """
        self._IdSet = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._UserName = None
        self._Phone = None
        self._Email = None
        self._AuthorizedDeviceIdSet = None
        self._AuthorizedAppAssetIdSet = None
        self._AuthTypeSet = None
        self._DepartmentId = None
        self._Filters = None
        self._IsCamUser = None
        self._UserFromSet = None

    @property
    def IdSet(self):
        r"""如果IdSet不为空，则忽略其他参数
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        r"""模糊查询，IdSet、UserName、Phone为空时才生效，对用户名和姓名进行模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页条目数量，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserName(self):
        r"""精确查询，IdSet为空时才生效
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        r"""精确查询，IdSet、UserName为空时才生效。
大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""邮箱，精确查询
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AuthorizedDeviceIdSet(self):
        r"""查询具有指定资产ID访问权限的用户
        :rtype: list of int non-negative
        """
        return self._AuthorizedDeviceIdSet

    @AuthorizedDeviceIdSet.setter
    def AuthorizedDeviceIdSet(self, AuthorizedDeviceIdSet):
        self._AuthorizedDeviceIdSet = AuthorizedDeviceIdSet

    @property
    def AuthorizedAppAssetIdSet(self):
        r"""查询具有指定应用资产ID访问权限的用户
        :rtype: list of int non-negative
        """
        return self._AuthorizedAppAssetIdSet

    @AuthorizedAppAssetIdSet.setter
    def AuthorizedAppAssetIdSet(self, AuthorizedAppAssetIdSet):
        self._AuthorizedAppAssetIdSet = AuthorizedAppAssetIdSet

    @property
    def AuthTypeSet(self):
        r"""认证方式，0 - 本地, 1 - LDAP, 2 - OAuth, 3-ioa 不传为全部
        :rtype: list of int non-negative
        """
        return self._AuthTypeSet

    @AuthTypeSet.setter
    def AuthTypeSet(self, AuthTypeSet):
        self._AuthTypeSet = AuthTypeSet

    @property
    def DepartmentId(self):
        r"""部门ID，用于过滤属于某个部门的用户
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Filters(self):
        r"""参数过滤数组

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsCamUser(self):
        r"""是否获取cam用户, 0-否，1-是
        :rtype: int
        """
        return self._IsCamUser

    @IsCamUser.setter
    def IsCamUser(self, IsCamUser):
        self._IsCamUser = IsCamUser

    @property
    def UserFromSet(self):
        r"""用户来源，0-bh，1-ioa,不传为全部
        :rtype: list of int non-negative
        """
        return self._UserFromSet

    @UserFromSet.setter
    def UserFromSet(self, UserFromSet):
        self._UserFromSet = UserFromSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self._AuthorizedAppAssetIdSet = params.get("AuthorizedAppAssetIdSet")
        self._AuthTypeSet = params.get("AuthTypeSet")
        self._DepartmentId = params.get("DepartmentId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsCamUser = params.get("IsCamUser")
        self._UserFromSet = params.get("UserFromSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    r"""DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户总数
        :type TotalCount: int
        :param _UserSet: 用户列表
        :type UserSet: list of User
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""用户总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserSet(self):
        r"""用户列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    r"""资产信息

    """

    def __init__(self):
        r"""
        :param _Id: 资产ID
        :type Id: int
        :param _InstanceId: 实例ID，对应CVM、CDB等实例ID
        :type InstanceId: str
        :param _Name: 资产名
        :type Name: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _PrivateIp: 内网IP
        :type PrivateIp: str
        :param _ApCode: 地域编码
        :type ApCode: str
        :param _ApName: 地域名称
        :type ApName: str
        :param _OsName: 操作系统名称
        :type OsName: str
        :param _Kind: 资产类型 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :type Kind: int
        :param _Port: 管理端口
        :type Port: int
        :param _GroupSet: 所属资产组列表
        :type GroupSet: list of Group
        :param _AccountCount: 资产绑定的账号数
        :type AccountCount: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Resource: 堡垒机服务信息，注意没有绑定服务时为null
        :type Resource: :class:`tencentcloud.bh.v20230418.models.Resource`
        :param _Department: 资产所属部门
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        :param _IpPortSet: 数据库资产的多节点
        :type IpPortSet: list of str
        :param _DomainId: 网络域Id
        :type DomainId: str
        :param _DomainName: 网络域名称
        :type DomainName: str
        :param _EnableSSL: 是否启用SSL，仅支持Redis资产。0：禁用 1：启用
        :type EnableSSL: int
        :param _SSLCertName: 已上传的SSL证书名称
        :type SSLCertName: str
        :param _IOAId: IOA侧的资源ID
        :type IOAId: int
        :param _ManageDimension: K8S集群托管维度。1-集群，2-命名空间，3-工作负载
        :type ManageDimension: int
        :param _ManageAccountId: K8S集群托管账号id	
        :type ManageAccountId: int
        :param _Namespace: K8S集群命名空间	
        :type Namespace: str
        :param _Workload: K8S集群工作负载	
        :type Workload: str
        :param _SyncPodCount: K8S集群pod已同步数量
        :type SyncPodCount: int
        :param _TotalPodCount: K8S集群pod总数量	
        :type TotalPodCount: int
        :param _CloudAccountId: 云账号id
        :type CloudAccountId: int
        :param _CloudAccountName: 云账号名称
        :type CloudAccountName: str
        :param _ProviderType: 云厂商类型1-腾讯云，2-阿里云
        :type ProviderType: int
        :param _ProviderName: 云厂商名称
        :type ProviderName: str
        :param _SyncCloudDeviceStatus: 同步的云资产状态，标记同步的资产的状态情况，0-已删除,1-正常,2-已隔离,3-已过期
        :type SyncCloudDeviceStatus: int
        """
        self._Id = None
        self._InstanceId = None
        self._Name = None
        self._PublicIp = None
        self._PrivateIp = None
        self._ApCode = None
        self._ApName = None
        self._OsName = None
        self._Kind = None
        self._Port = None
        self._GroupSet = None
        self._AccountCount = None
        self._VpcId = None
        self._SubnetId = None
        self._Resource = None
        self._Department = None
        self._IpPortSet = None
        self._DomainId = None
        self._DomainName = None
        self._EnableSSL = None
        self._SSLCertName = None
        self._IOAId = None
        self._ManageDimension = None
        self._ManageAccountId = None
        self._Namespace = None
        self._Workload = None
        self._SyncPodCount = None
        self._TotalPodCount = None
        self._CloudAccountId = None
        self._CloudAccountName = None
        self._ProviderType = None
        self._ProviderName = None
        self._SyncCloudDeviceStatus = None

    @property
    def Id(self):
        r"""资产ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""实例ID，对应CVM、CDB等实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""资产名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PublicIp(self):
        r"""公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def ApCode(self):
        r"""地域编码
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def ApName(self):
        r"""地域名称
        :rtype: str
        """
        return self._ApName

    @ApName.setter
    def ApName(self, ApName):
        self._ApName = ApName

    @property
    def OsName(self):
        r"""操作系统名称
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Kind(self):
        r"""资产类型 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Port(self):
        r"""管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupSet(self):
        r"""所属资产组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def AccountCount(self):
        r"""资产绑定的账号数
        :rtype: int
        """
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Resource(self):
        r"""堡垒机服务信息，注意没有绑定服务时为null
        :rtype: :class:`tencentcloud.bh.v20230418.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Department(self):
        r"""资产所属部门
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def IpPortSet(self):
        r"""数据库资产的多节点
        :rtype: list of str
        """
        return self._IpPortSet

    @IpPortSet.setter
    def IpPortSet(self, IpPortSet):
        self._IpPortSet = IpPortSet

    @property
    def DomainId(self):
        r"""网络域Id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        r"""网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def EnableSSL(self):
        r"""是否启用SSL，仅支持Redis资产。0：禁用 1：启用
        :rtype: int
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def SSLCertName(self):
        r"""已上传的SSL证书名称
        :rtype: str
        """
        return self._SSLCertName

    @SSLCertName.setter
    def SSLCertName(self, SSLCertName):
        self._SSLCertName = SSLCertName

    @property
    def IOAId(self):
        r"""IOA侧的资源ID
        :rtype: int
        """
        return self._IOAId

    @IOAId.setter
    def IOAId(self, IOAId):
        self._IOAId = IOAId

    @property
    def ManageDimension(self):
        r"""K8S集群托管维度。1-集群，2-命名空间，3-工作负载
        :rtype: int
        """
        return self._ManageDimension

    @ManageDimension.setter
    def ManageDimension(self, ManageDimension):
        self._ManageDimension = ManageDimension

    @property
    def ManageAccountId(self):
        r"""K8S集群托管账号id	
        :rtype: int
        """
        return self._ManageAccountId

    @ManageAccountId.setter
    def ManageAccountId(self, ManageAccountId):
        self._ManageAccountId = ManageAccountId

    @property
    def Namespace(self):
        r"""K8S集群命名空间	
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Workload(self):
        r"""K8S集群工作负载	
        :rtype: str
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def SyncPodCount(self):
        r"""K8S集群pod已同步数量
        :rtype: int
        """
        return self._SyncPodCount

    @SyncPodCount.setter
    def SyncPodCount(self, SyncPodCount):
        self._SyncPodCount = SyncPodCount

    @property
    def TotalPodCount(self):
        r"""K8S集群pod总数量	
        :rtype: int
        """
        return self._TotalPodCount

    @TotalPodCount.setter
    def TotalPodCount(self, TotalPodCount):
        self._TotalPodCount = TotalPodCount

    @property
    def CloudAccountId(self):
        r"""云账号id
        :rtype: int
        """
        return self._CloudAccountId

    @CloudAccountId.setter
    def CloudAccountId(self, CloudAccountId):
        self._CloudAccountId = CloudAccountId

    @property
    def CloudAccountName(self):
        r"""云账号名称
        :rtype: str
        """
        return self._CloudAccountName

    @CloudAccountName.setter
    def CloudAccountName(self, CloudAccountName):
        self._CloudAccountName = CloudAccountName

    @property
    def ProviderType(self):
        r"""云厂商类型1-腾讯云，2-阿里云
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def ProviderName(self):
        r"""云厂商名称
        :rtype: str
        """
        return self._ProviderName

    @ProviderName.setter
    def ProviderName(self, ProviderName):
        self._ProviderName = ProviderName

    @property
    def SyncCloudDeviceStatus(self):
        r"""同步的云资产状态，标记同步的资产的状态情况，0-已删除,1-正常,2-已隔离,3-已过期
        :rtype: int
        """
        return self._SyncCloudDeviceStatus

    @SyncCloudDeviceStatus.setter
    def SyncCloudDeviceStatus(self, SyncCloudDeviceStatus):
        self._SyncCloudDeviceStatus = SyncCloudDeviceStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._ApCode = params.get("ApCode")
        self._ApName = params.get("ApName")
        self._OsName = params.get("OsName")
        self._Kind = params.get("Kind")
        self._Port = params.get("Port")
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._AccountCount = params.get("AccountCount")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._IpPortSet = params.get("IpPortSet")
        self._DomainId = params.get("DomainId")
        self._DomainName = params.get("DomainName")
        self._EnableSSL = params.get("EnableSSL")
        self._SSLCertName = params.get("SSLCertName")
        self._IOAId = params.get("IOAId")
        self._ManageDimension = params.get("ManageDimension")
        self._ManageAccountId = params.get("ManageAccountId")
        self._Namespace = params.get("Namespace")
        self._Workload = params.get("Workload")
        self._SyncPodCount = params.get("SyncPodCount")
        self._TotalPodCount = params.get("TotalPodCount")
        self._CloudAccountId = params.get("CloudAccountId")
        self._CloudAccountName = params.get("CloudAccountName")
        self._ProviderType = params.get("ProviderType")
        self._ProviderName = params.get("ProviderName")
        self._SyncCloudDeviceStatus = params.get("SyncCloudDeviceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceAccount(AbstractModel):
    r"""主机账号

    """

    def __init__(self):
        r"""
        :param _Id: 账号ID
        :type Id: int
        :param _DeviceId: 主机ID
        :type DeviceId: int
        :param _Account: 账号名
        :type Account: str
        :param _BoundPassword: true-已托管密码，false-未托管密码
        :type BoundPassword: bool
        :param _BoundPrivateKey: true-已托管私钥，false-未托管私钥
        :type BoundPrivateKey: bool
        :param _BoundKubeconfig: 是否托管凭证, true-托管，false-未托管
        :type BoundKubeconfig: bool
        :param _IsK8SManageAccount: 是否为k8s资产管理账号	
        :type IsK8SManageAccount: bool
        """
        self._Id = None
        self._DeviceId = None
        self._Account = None
        self._BoundPassword = None
        self._BoundPrivateKey = None
        self._BoundKubeconfig = None
        self._IsK8SManageAccount = None

    @property
    def Id(self):
        r"""账号ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DeviceId(self):
        r"""主机ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Account(self):
        r"""账号名
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def BoundPassword(self):
        r"""true-已托管密码，false-未托管密码
        :rtype: bool
        """
        return self._BoundPassword

    @BoundPassword.setter
    def BoundPassword(self, BoundPassword):
        self._BoundPassword = BoundPassword

    @property
    def BoundPrivateKey(self):
        r"""true-已托管私钥，false-未托管私钥
        :rtype: bool
        """
        return self._BoundPrivateKey

    @BoundPrivateKey.setter
    def BoundPrivateKey(self, BoundPrivateKey):
        self._BoundPrivateKey = BoundPrivateKey

    @property
    def BoundKubeconfig(self):
        r"""是否托管凭证, true-托管，false-未托管
        :rtype: bool
        """
        return self._BoundKubeconfig

    @BoundKubeconfig.setter
    def BoundKubeconfig(self, BoundKubeconfig):
        self._BoundKubeconfig = BoundKubeconfig

    @property
    def IsK8SManageAccount(self):
        r"""是否为k8s资产管理账号	
        :rtype: bool
        """
        return self._IsK8SManageAccount

    @IsK8SManageAccount.setter
    def IsK8SManageAccount(self, IsK8SManageAccount):
        self._IsK8SManageAccount = IsK8SManageAccount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DeviceId = params.get("DeviceId")
        self._Account = params.get("Account")
        self._BoundPassword = params.get("BoundPassword")
        self._BoundPrivateKey = params.get("BoundPrivateKey")
        self._BoundKubeconfig = params.get("BoundKubeconfig")
        self._IsK8SManageAccount = params.get("IsK8SManageAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableExternalAccessRequest(AbstractModel):
    r"""DisableExternalAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 堡垒机id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""堡垒机id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableExternalAccessResponse(AbstractModel):
    r"""DisableExternalAccess返回参数结构体

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


class DisableIntranetAccessRequest(AbstractModel):
    r"""DisableIntranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 堡垒机id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""堡垒机id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableIntranetAccessResponse(AbstractModel):
    r"""DisableIntranetAccess返回参数结构体

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


class Domain(AbstractModel):
    r"""网络域

    """

    def __init__(self):
        r"""
        :param _Id: 自增id
        :type Id: int
        :param _DomainId: 网络域id
        :type DomainId: str
        :param _DomainName: 网络域名称
        :type DomainName: str
        :param _ResourceId: 堡垒机id
        :type ResourceId: str
        :param _WhiteIpSet: ip，网段
        :type WhiteIpSet: list of str
        :param _Enabled: 是否启用  默认 1启用 0禁用
        :type Enabled: int
        :param _Status: 状态 0-已断开  1-已连接
        :type Status: int
        :param _CreateTime: 网络域创建时间
        :type CreateTime: str
        :param _Default: 是否资源默认网络域 1-资源默认网络域 0-用户添加网络域
        :type Default: int
        """
        self._Id = None
        self._DomainId = None
        self._DomainName = None
        self._ResourceId = None
        self._WhiteIpSet = None
        self._Enabled = None
        self._Status = None
        self._CreateTime = None
        self._Default = None

    @property
    def Id(self):
        r"""自增id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DomainId(self):
        r"""网络域id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        r"""网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ResourceId(self):
        r"""堡垒机id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def WhiteIpSet(self):
        r"""ip，网段
        :rtype: list of str
        """
        return self._WhiteIpSet

    @WhiteIpSet.setter
    def WhiteIpSet(self, WhiteIpSet):
        self._WhiteIpSet = WhiteIpSet

    @property
    def Enabled(self):
        r"""是否启用  默认 1启用 0禁用
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Status(self):
        r"""状态 0-已断开  1-已连接
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""网络域创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Default(self):
        r"""是否资源默认网络域 1-资源默认网络域 0-用户添加网络域
        :rtype: int
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DomainId = params.get("DomainId")
        self._DomainName = params.get("DomainName")
        self._ResourceId = params.get("ResourceId")
        self._WhiteIpSet = params.get("WhiteIpSet")
        self._Enabled = params.get("Enabled")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Default = params.get("Default")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableExternalAccessRequest(AbstractModel):
    r"""EnableExternalAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 堡垒机id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""堡垒机id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableExternalAccessResponse(AbstractModel):
    r"""EnableExternalAccess返回参数结构体

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


class EnableIntranetAccessRequest(AbstractModel):
    r"""EnableIntranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 堡垒机实例id
        :type ResourceId: str
        :param _VpcId: 开通内网访问的vpc id
        :type VpcId: str
        :param _VpcCidrBlock: vpc的网段
        :type VpcCidrBlock: str
        :param _SubnetId: 开通内网访问的subnet id
        :type SubnetId: str
        :param _DomainName: 内网ip的自定义域名，可为空
        :type DomainName: str
        """
        self._ResourceId = None
        self._VpcId = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._DomainName = None

    @property
    def ResourceId(self):
        r"""堡垒机实例id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def VpcId(self):
        r"""开通内网访问的vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        r"""vpc的网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        r"""开通内网访问的subnet id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DomainName(self):
        r"""内网ip的自定义域名，可为空
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableIntranetAccessResponse(AbstractModel):
    r"""EnableIntranetAccess返回参数结构体

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


class EnvInternetAccessSetting(AbstractModel):
    r"""大区环境网络配置

    """

    def __init__(self):
        r"""
        :param _DisableExternalAccess: true：不能访问公网
        :type DisableExternalAccess: bool
        :param _DisableDownloadDataAcl: true：不能创建数据下载权限
        :type DisableDownloadDataAcl: bool
        """
        self._DisableExternalAccess = None
        self._DisableDownloadDataAcl = None

    @property
    def DisableExternalAccess(self):
        r"""true：不能访问公网
        :rtype: bool
        """
        return self._DisableExternalAccess

    @DisableExternalAccess.setter
    def DisableExternalAccess(self, DisableExternalAccess):
        self._DisableExternalAccess = DisableExternalAccess

    @property
    def DisableDownloadDataAcl(self):
        r"""true：不能创建数据下载权限
        :rtype: bool
        """
        return self._DisableDownloadDataAcl

    @DisableDownloadDataAcl.setter
    def DisableDownloadDataAcl(self, DisableDownloadDataAcl):
        self._DisableDownloadDataAcl = DisableDownloadDataAcl


    def _deserialize(self, params):
        self._DisableExternalAccess = params.get("DisableExternalAccess")
        self._DisableDownloadDataAcl = params.get("DisableDownloadDataAcl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalDevice(AbstractModel):
    r"""主机参数，导入外部主机时使用

    """

    def __init__(self):
        r"""
        :param _OsName: 操作系统名称，只能是Linux、Windows或MySQL
        :type OsName: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Port: 管理端口
        :type Port: int
        :param _Name: 主机名，可为空
        :type Name: str
        :param _DepartmentId: 资产所属的部门ID
        :type DepartmentId: str
        :param _IpPortSet: 资产多节点：字段ip和端口
        :type IpPortSet: list of str
        :param _EnableSSL: 是否启用SSL,1:启用 0：禁用，仅支持Redis资产
        :type EnableSSL: int
        :param _SSLCert: SSL证书，EnableSSL时必填
        :type SSLCert: str
        :param _SSLCertName: SSL证书名称，EnableSSL时必填
        :type SSLCertName: str
        :param _InstanceId: 资产实例id
        :type InstanceId: str
        :param _ApCode: 资产所属地域
        :type ApCode: str
        :param _ApName: 地域名称
        :type ApName: str
        :param _VpcId: 资产所属VPC
        :type VpcId: str
        :param _SubnetId: 资产所属子网
        :type SubnetId: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        """
        self._OsName = None
        self._Ip = None
        self._Port = None
        self._Name = None
        self._DepartmentId = None
        self._IpPortSet = None
        self._EnableSSL = None
        self._SSLCert = None
        self._SSLCertName = None
        self._InstanceId = None
        self._ApCode = None
        self._ApName = None
        self._VpcId = None
        self._SubnetId = None
        self._PublicIp = None

    @property
    def OsName(self):
        r"""操作系统名称，只能是Linux、Windows或MySQL
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

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
    def Port(self):
        r"""管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Name(self):
        r"""主机名，可为空
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        r"""资产所属的部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def IpPortSet(self):
        r"""资产多节点：字段ip和端口
        :rtype: list of str
        """
        return self._IpPortSet

    @IpPortSet.setter
    def IpPortSet(self, IpPortSet):
        self._IpPortSet = IpPortSet

    @property
    def EnableSSL(self):
        r"""是否启用SSL,1:启用 0：禁用，仅支持Redis资产
        :rtype: int
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def SSLCert(self):
        r"""SSL证书，EnableSSL时必填
        :rtype: str
        """
        return self._SSLCert

    @SSLCert.setter
    def SSLCert(self, SSLCert):
        self._SSLCert = SSLCert

    @property
    def SSLCertName(self):
        r"""SSL证书名称，EnableSSL时必填
        :rtype: str
        """
        return self._SSLCertName

    @SSLCertName.setter
    def SSLCertName(self, SSLCertName):
        self._SSLCertName = SSLCertName

    @property
    def InstanceId(self):
        r"""资产实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApCode(self):
        r"""资产所属地域
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def ApName(self):
        r"""地域名称
        :rtype: str
        """
        return self._ApName

    @ApName.setter
    def ApName(self, ApName):
        self._ApName = ApName

    @property
    def VpcId(self):
        r"""资产所属VPC
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""资产所属子网
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PublicIp(self):
        r"""公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp


    def _deserialize(self, params):
        self._OsName = params.get("OsName")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Name = params.get("Name")
        self._DepartmentId = params.get("DepartmentId")
        self._IpPortSet = params.get("IpPortSet")
        self._EnableSSL = params.get("EnableSSL")
        self._SSLCert = params.get("SSLCert")
        self._SSLCertName = params.get("SSLCertName")
        self._InstanceId = params.get("InstanceId")
        self._ApCode = params.get("ApCode")
        self._ApName = params.get("ApName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PublicIp = params.get("PublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""字段的过滤值。
若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Group(AbstractModel):
    r"""组信息，用于用户组、主机组

    """

    def __init__(self):
        r"""
        :param _Id: 组ID
        :type Id: int
        :param _Name: 组名称
        :type Name: str
        :param _Department: 所属部门信息
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        :param _Count: 个数
        :type Count: int
        """
        self._Id = None
        self._Name = None
        self._Department = None
        self._Count = None

    @property
    def Id(self):
        r"""组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Department(self):
        r"""所属部门信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Count(self):
        r"""个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IOAUserGroup(AbstractModel):
    r"""同步过来的ioa用户分组信息

    """

    def __init__(self):
        r"""
        :param _OrgId: ioa用户组织id
        :type OrgId: int
        :param _OrgName: ioa用户组织名称
        :type OrgName: str
        :param _OrgIdPath: ioa用户组织id路径	
        :type OrgIdPath: str
        :param _OrgNamePath: ioa用户组织名称路径	
        :type OrgNamePath: str
        :param _Source: ioa关联用户源类型
        :type Source: int
        """
        self._OrgId = None
        self._OrgName = None
        self._OrgIdPath = None
        self._OrgNamePath = None
        self._Source = None

    @property
    def OrgId(self):
        r"""ioa用户组织id
        :rtype: int
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def OrgName(self):
        r"""ioa用户组织名称
        :rtype: str
        """
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName

    @property
    def OrgIdPath(self):
        r"""ioa用户组织id路径	
        :rtype: str
        """
        return self._OrgIdPath

    @OrgIdPath.setter
    def OrgIdPath(self, OrgIdPath):
        self._OrgIdPath = OrgIdPath

    @property
    def OrgNamePath(self):
        r"""ioa用户组织名称路径	
        :rtype: str
        """
        return self._OrgNamePath

    @OrgNamePath.setter
    def OrgNamePath(self, OrgNamePath):
        self._OrgNamePath = OrgNamePath

    @property
    def Source(self):
        r"""ioa关联用户源类型
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._OrgName = params.get("OrgName")
        self._OrgIdPath = params.get("OrgIdPath")
        self._OrgNamePath = params.get("OrgNamePath")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportExternalDeviceRequest(AbstractModel):
    r"""ImportExternalDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceSet: 资产参数列表
        :type DeviceSet: list of ExternalDevice
        :param _AccountId:  资产所属云账号id
        :type AccountId: int
        """
        self._DeviceSet = None
        self._AccountId = None

    @property
    def DeviceSet(self):
        r"""资产参数列表
        :rtype: list of ExternalDevice
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def AccountId(self):
        r""" 资产所属云账号id
        :rtype: int
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = ExternalDevice()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportExternalDeviceResponse(AbstractModel):
    r"""ImportExternalDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdSet: 资产ID列表
        :type DeviceIdSet: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceIdSet = None
        self._RequestId = None

    @property
    def DeviceIdSet(self):
        r"""资产ID列表
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

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
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._RequestId = params.get("RequestId")


class LoginEvent(AbstractModel):
    r"""登录日志

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _Time: 操作时间
        :type Time: str
        :param _SourceIp: 来源IP
        :type SourceIp: str
        :param _Entry: 登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :type Entry: int
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
        """
        self._UserName = None
        self._RealName = None
        self._Time = None
        self._SourceIp = None
        self._Entry = None
        self._Result = None

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Time(self):
        r"""操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SourceIp(self):
        r"""来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Entry(self):
        r"""登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :rtype: int
        """
        return self._Entry

    @Entry.setter
    def Entry(self, Entry):
        self._Entry = Entry

    @property
    def Result(self):
        r"""操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Time = params.get("Time")
        self._SourceIp = params.get("SourceIp")
        self._Entry = params.get("Entry")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessWhiteListAutoStatusRequest(AbstractModel):
    r"""ModifyAccessWhiteListAutoStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AllowAuto: true：放开自动添加IP；false：不放开自动添加IP
        :type AllowAuto: bool
        """
        self._AllowAuto = None

    @property
    def AllowAuto(self):
        r"""true：放开自动添加IP；false：不放开自动添加IP
        :rtype: bool
        """
        return self._AllowAuto

    @AllowAuto.setter
    def AllowAuto(self, AllowAuto):
        self._AllowAuto = AllowAuto


    def _deserialize(self, params):
        self._AllowAuto = params.get("AllowAuto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessWhiteListAutoStatusResponse(AbstractModel):
    r"""ModifyAccessWhiteListAutoStatus返回参数结构体

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


class ModifyAccessWhiteListRuleRequest(AbstractModel):
    r"""ModifyAccessWhiteListRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 白名单规则ID
        :type Id: int
        :param _Source: ip或网段信息，如10.10.10.1或10.10.10.0/24，最大长度40字节
        :type Source: str
        :param _Remark: 备注信息，最大长度64字符。
        :type Remark: str
        """
        self._Id = None
        self._Source = None
        self._Remark = None

    @property
    def Id(self):
        r"""白名单规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Source(self):
        r"""ip或网段信息，如10.10.10.1或10.10.10.0/24，最大长度40字节
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Remark(self):
        r"""备注信息，最大长度64字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Source = params.get("Source")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessWhiteListRuleResponse(AbstractModel):
    r"""ModifyAccessWhiteListRule返回参数结构体

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


class ModifyAccessWhiteListStatusRequest(AbstractModel):
    r"""ModifyAccessWhiteListStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AllowAny: true：放开全部来源IP；false：不放开全部来源IP
        :type AllowAny: bool
        """
        self._AllowAny = None

    @property
    def AllowAny(self):
        r"""true：放开全部来源IP；false：不放开全部来源IP
        :rtype: bool
        """
        return self._AllowAny

    @AllowAny.setter
    def AllowAny(self, AllowAny):
        self._AllowAny = AllowAny


    def _deserialize(self, params):
        self._AllowAny = params.get("AllowAny")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessWhiteListStatusResponse(AbstractModel):
    r"""ModifyAccessWhiteListStatus返回参数结构体

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


class ModifyAclRequest(AbstractModel):
    r"""ModifyAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 访问权限名称，最大32字符，不能包含空白字符
        :type Name: str
        :param _AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param _AllowAnyAccount: 是否允许任意账号登录
        :type AllowAnyAccount: bool
        :param _Id: 访问权限ID
        :type Id: int
        :param _AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param _AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param _AllowClipTextUp: 是否开启剪贴板文本（含图片）上行
        :type AllowClipTextUp: bool
        :param _AllowClipTextDown: 是否开启剪贴板文本（含图片）下行
        :type AllowClipTextDown: bool
        :param _AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param _MaxFileUpSize: 文件传输上传大小限制（预留参数，目前暂未使用）
        :type MaxFileUpSize: int
        :param _AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param _MaxFileDownSize: 文件传输下载大小限制（预留参数，目前暂未使用）
        :type MaxFileDownSize: int
        :param _UserIdSet: 关联的用户ID
        :type UserIdSet: list of int non-negative
        :param _UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param _DeviceIdSet: 关联的资产ID
        :type DeviceIdSet: list of int non-negative
        :param _AppAssetIdSet: 关联的应用资产ID集合
        :type AppAssetIdSet: list of int non-negative
        :param _DeviceGroupIdSet: 关联的资产组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param _AccountSet: 关联的账号
        :type AccountSet: list of str
        :param _CmdTemplateIdSet: 关联的高危命令模板ID
        :type CmdTemplateIdSet: list of int non-negative
        :param _ACTemplateIdSet: 关联高危DB模板ID
        :type ACTemplateIdSet: list of str
        :param _AllowDiskFileUp: 是否开启 RDP 磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param _AllowDiskFileDown: 是否开启 RDP 磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param _AllowShellFileUp: 是否开启rz sz文件上传
        :type AllowShellFileUp: bool
        :param _AllowShellFileDown: 是否开启rz sz文件下载
        :type AllowShellFileDown: bool
        :param _AllowFileDel: 是否开启 SFTP 文件删除
        :type AllowFileDel: bool
        :param _ValidateFrom: 访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :type ValidateTo: str
        :param _DepartmentId: 权限所属部门的ID，如：1.2.3
        :type DepartmentId: str
        :param _AllowAccessCredential: 是否允许使用访问串
        :type AllowAccessCredential: bool
        :param _AllowKeyboardLogger: 是否允许键盘记录
        :type AllowKeyboardLogger: bool
        """
        self._Name = None
        self._AllowDiskRedirect = None
        self._AllowAnyAccount = None
        self._Id = None
        self._AllowClipFileUp = None
        self._AllowClipFileDown = None
        self._AllowClipTextUp = None
        self._AllowClipTextDown = None
        self._AllowFileUp = None
        self._MaxFileUpSize = None
        self._AllowFileDown = None
        self._MaxFileDownSize = None
        self._UserIdSet = None
        self._UserGroupIdSet = None
        self._DeviceIdSet = None
        self._AppAssetIdSet = None
        self._DeviceGroupIdSet = None
        self._AccountSet = None
        self._CmdTemplateIdSet = None
        self._ACTemplateIdSet = None
        self._AllowDiskFileUp = None
        self._AllowDiskFileDown = None
        self._AllowShellFileUp = None
        self._AllowShellFileDown = None
        self._AllowFileDel = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._DepartmentId = None
        self._AllowAccessCredential = None
        self._AllowKeyboardLogger = None

    @property
    def Name(self):
        r"""访问权限名称，最大32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        r"""是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowAnyAccount(self):
        r"""是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def Id(self):
        r"""访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AllowClipFileUp(self):
        r"""是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        r"""是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        r"""是否开启剪贴板文本（含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        r"""是否开启剪贴板文本（含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        r"""是否开启文件传输上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        r"""文件传输上传大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        r"""是否开启文件传输下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        r"""文件传输下载大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def UserIdSet(self):
        r"""关联的用户ID
        :rtype: list of int non-negative
        """
        return self._UserIdSet

    @UserIdSet.setter
    def UserIdSet(self, UserIdSet):
        self._UserIdSet = UserIdSet

    @property
    def UserGroupIdSet(self):
        r"""关联的用户组ID
        :rtype: list of int non-negative
        """
        return self._UserGroupIdSet

    @UserGroupIdSet.setter
    def UserGroupIdSet(self, UserGroupIdSet):
        self._UserGroupIdSet = UserGroupIdSet

    @property
    def DeviceIdSet(self):
        r"""关联的资产ID
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AppAssetIdSet(self):
        r"""关联的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AppAssetIdSet

    @AppAssetIdSet.setter
    def AppAssetIdSet(self, AppAssetIdSet):
        self._AppAssetIdSet = AppAssetIdSet

    @property
    def DeviceGroupIdSet(self):
        r"""关联的资产组ID
        :rtype: list of int non-negative
        """
        return self._DeviceGroupIdSet

    @DeviceGroupIdSet.setter
    def DeviceGroupIdSet(self, DeviceGroupIdSet):
        self._DeviceGroupIdSet = DeviceGroupIdSet

    @property
    def AccountSet(self):
        r"""关联的账号
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateIdSet(self):
        r"""关联的高危命令模板ID
        :rtype: list of int non-negative
        """
        return self._CmdTemplateIdSet

    @CmdTemplateIdSet.setter
    def CmdTemplateIdSet(self, CmdTemplateIdSet):
        self._CmdTemplateIdSet = CmdTemplateIdSet

    @property
    def ACTemplateIdSet(self):
        r"""关联高危DB模板ID
        :rtype: list of str
        """
        return self._ACTemplateIdSet

    @ACTemplateIdSet.setter
    def ACTemplateIdSet(self, ACTemplateIdSet):
        self._ACTemplateIdSet = ACTemplateIdSet

    @property
    def AllowDiskFileUp(self):
        r"""是否开启 RDP 磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        r"""是否开启 RDP 磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        r"""是否开启rz sz文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        r"""是否开启rz sz文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        r"""是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        r"""访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def DepartmentId(self):
        r"""权限所属部门的ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def AllowAccessCredential(self):
        r"""是否允许使用访问串
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def AllowKeyboardLogger(self):
        r"""是否允许键盘记录
        :rtype: bool
        """
        return self._AllowKeyboardLogger

    @AllowKeyboardLogger.setter
    def AllowKeyboardLogger(self, AllowKeyboardLogger):
        self._AllowKeyboardLogger = AllowKeyboardLogger


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AllowDiskRedirect = params.get("AllowDiskRedirect")
        self._AllowAnyAccount = params.get("AllowAnyAccount")
        self._Id = params.get("Id")
        self._AllowClipFileUp = params.get("AllowClipFileUp")
        self._AllowClipFileDown = params.get("AllowClipFileDown")
        self._AllowClipTextUp = params.get("AllowClipTextUp")
        self._AllowClipTextDown = params.get("AllowClipTextDown")
        self._AllowFileUp = params.get("AllowFileUp")
        self._MaxFileUpSize = params.get("MaxFileUpSize")
        self._AllowFileDown = params.get("AllowFileDown")
        self._MaxFileDownSize = params.get("MaxFileDownSize")
        self._UserIdSet = params.get("UserIdSet")
        self._UserGroupIdSet = params.get("UserGroupIdSet")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._AppAssetIdSet = params.get("AppAssetIdSet")
        self._DeviceGroupIdSet = params.get("DeviceGroupIdSet")
        self._AccountSet = params.get("AccountSet")
        self._CmdTemplateIdSet = params.get("CmdTemplateIdSet")
        self._ACTemplateIdSet = params.get("ACTemplateIdSet")
        self._AllowDiskFileUp = params.get("AllowDiskFileUp")
        self._AllowDiskFileDown = params.get("AllowDiskFileDown")
        self._AllowShellFileUp = params.get("AllowShellFileUp")
        self._AllowShellFileDown = params.get("AllowShellFileDown")
        self._AllowFileDel = params.get("AllowFileDel")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        self._DepartmentId = params.get("DepartmentId")
        self._AllowAccessCredential = params.get("AllowAccessCredential")
        self._AllowKeyboardLogger = params.get("AllowKeyboardLogger")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclResponse(AbstractModel):
    r"""ModifyAcl返回参数结构体

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


class ModifyAssetSyncFlagRequest(AbstractModel):
    r"""ModifyAssetSyncFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoSync: 是否开启资产自动同步，false-不开启，true-开启
        :type AutoSync: bool
        """
        self._AutoSync = None

    @property
    def AutoSync(self):
        r"""是否开启资产自动同步，false-不开启，true-开启
        :rtype: bool
        """
        return self._AutoSync

    @AutoSync.setter
    def AutoSync(self, AutoSync):
        self._AutoSync = AutoSync


    def _deserialize(self, params):
        self._AutoSync = params.get("AutoSync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetSyncFlagResponse(AbstractModel):
    r"""ModifyAssetSyncFlag返回参数结构体

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


class ModifyAuthModeSettingRequest(AbstractModel):
    r"""ModifyAuthModeSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthMode: 双因子认证，0-不开启，1-OTP，2-短信，3-USB Key
        :type AuthMode: int
        :param _ResourceType: 资源类型，0：普通 1：国密
        :type ResourceType: int
        """
        self._AuthMode = None
        self._ResourceType = None

    @property
    def AuthMode(self):
        r"""双因子认证，0-不开启，1-OTP，2-短信，3-USB Key
        :rtype: int
        """
        return self._AuthMode

    @AuthMode.setter
    def AuthMode(self, AuthMode):
        self._AuthMode = AuthMode

    @property
    def ResourceType(self):
        r"""资源类型，0：普通 1：国密
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._AuthMode = params.get("AuthMode")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuthModeSettingResponse(AbstractModel):
    r"""ModifyAuthModeSetting返回参数结构体

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


class ModifyChangePwdTaskRequest(AbstractModel):
    r"""ModifyChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationId: 改密任务id
        :type OperationId: str
        :param _DeviceIdSet: 改密资产id列表
        :type DeviceIdSet: list of int non-negative
        :param _AccountSet: 改密资产的账号列表
        :type AccountSet: list of str
        :param _ModifyType: 修改类型：1：修改任务信息  2：关联任务资产账号
        :type ModifyType: int
        :param _ChangeMethod: 改密方式。1：使用执行账号修改密码；2：修改自身密码
        :type ChangeMethod: int
        :param _AuthGenerationStrategy: 密码生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :type AuthGenerationStrategy: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _DepartmentId: 所属部门ID，"1,2,3"
        :type DepartmentId: str
        :param _RunAccount: 任务的执行账号	
        :type RunAccount: str
        :param _Password: 密码，手动指定密码时必传。
        :type Password: str
        :param _PasswordLength: 密码限制长度，自动生成密码必传。	
        :type PasswordLength: int
        :param _SmallLetter: 密码包含小写字母，0：否，1：是。
        :type SmallLetter: int
        :param _BigLetter: 密码包含大写字母，0：否，1：是。
        :type BigLetter: int
        :param _Digit: 密码包含数字，0：否，1：是。
        :type Digit: int
        :param _Symbol: 密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :type Symbol: str
        :param _CompleteNotify: 改密完成通知。0：不通知 1：通知
        :type CompleteNotify: int
        :param _NotifyEmails: 通知邮箱
        :type NotifyEmails: list of str
        :param _FilePassword: 加密压缩文件密码
        :type FilePassword: str
        :param _Type: 任务类型， 4：手工执行  5：周期自动执行
        :type Type: int
        :param _Period: 周期任务周期，单位天（大于等于 1，小于等于 365）
        :type Period: int
        :param _FirstTime: 周期任务首次执行时间
        :type FirstTime: str
        """
        self._OperationId = None
        self._DeviceIdSet = None
        self._AccountSet = None
        self._ModifyType = None
        self._ChangeMethod = None
        self._AuthGenerationStrategy = None
        self._TaskName = None
        self._DepartmentId = None
        self._RunAccount = None
        self._Password = None
        self._PasswordLength = None
        self._SmallLetter = None
        self._BigLetter = None
        self._Digit = None
        self._Symbol = None
        self._CompleteNotify = None
        self._NotifyEmails = None
        self._FilePassword = None
        self._Type = None
        self._Period = None
        self._FirstTime = None

    @property
    def OperationId(self):
        r"""改密任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DeviceIdSet(self):
        r"""改密资产id列表
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AccountSet(self):
        r"""改密资产的账号列表
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def ModifyType(self):
        r"""修改类型：1：修改任务信息  2：关联任务资产账号
        :rtype: int
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ChangeMethod(self):
        r"""改密方式。1：使用执行账号修改密码；2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def AuthGenerationStrategy(self):
        r"""密码生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def TaskName(self):
        r"""任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DepartmentId(self):
        r"""所属部门ID，"1,2,3"
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def RunAccount(self):
        r"""任务的执行账号	
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def Password(self):
        r"""密码，手动指定密码时必传。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordLength(self):
        r"""密码限制长度，自动生成密码必传。	
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        r"""密码包含小写字母，0：否，1：是。
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        r"""密码包含大写字母，0：否，1：是。
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        r"""密码包含数字，0：否，1：是。
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        r"""密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        r"""改密完成通知。0：不通知 1：通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        r"""通知邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        r"""加密压缩文件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def Type(self):
        r"""任务类型， 4：手工执行  5：周期自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        r"""周期任务周期，单位天（大于等于 1，小于等于 365）
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        r"""周期任务首次执行时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime


    def _deserialize(self, params):
        self._OperationId = params.get("OperationId")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._AccountSet = params.get("AccountSet")
        self._ModifyType = params.get("ModifyType")
        self._ChangeMethod = params.get("ChangeMethod")
        self._AuthGenerationStrategy = params.get("AuthGenerationStrategy")
        self._TaskName = params.get("TaskName")
        self._DepartmentId = params.get("DepartmentId")
        self._RunAccount = params.get("RunAccount")
        self._Password = params.get("Password")
        self._PasswordLength = params.get("PasswordLength")
        self._SmallLetter = params.get("SmallLetter")
        self._BigLetter = params.get("BigLetter")
        self._Digit = params.get("Digit")
        self._Symbol = params.get("Symbol")
        self._CompleteNotify = params.get("CompleteNotify")
        self._NotifyEmails = params.get("NotifyEmails")
        self._FilePassword = params.get("FilePassword")
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        self._FirstTime = params.get("FirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChangePwdTaskResponse(AbstractModel):
    r"""ModifyChangePwdTask返回参数结构体

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


class ModifyCmdTemplateRequest(AbstractModel):
    r"""ModifyCmdTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模板名，最长32字符，不能包含空白字符
        :type Name: str
        :param _CmdList: 命令列表，\n分隔，最长32768字节
        :type CmdList: str
        :param _Id: 命令模板ID
        :type Id: int
        :param _Encoding: CmdList字段前端是否base64传值。
0：否，1：是
        :type Encoding: int
        :param _Type: 命令模板类型 1-内置模板 2-自定义模板
        :type Type: int
        """
        self._Name = None
        self._CmdList = None
        self._Id = None
        self._Encoding = None
        self._Type = None

    @property
    def Name(self):
        r"""模板名，最长32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        r"""命令列表，\n分隔，最长32768字节
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Id(self):
        r"""命令模板ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Encoding(self):
        r"""CmdList字段前端是否base64传值。
0：否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Type(self):
        r"""命令模板类型 1-内置模板 2-自定义模板
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CmdList = params.get("CmdList")
        self._Id = params.get("Id")
        self._Encoding = params.get("Encoding")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmdTemplateResponse(AbstractModel):
    r"""ModifyCmdTemplate返回参数结构体

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


class ModifyDeviceGroupRequest(AbstractModel):
    r"""ModifyDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 资产组名，最大长度32字符，不能为空
        :type Name: str
        :param _Id: 资产组ID
        :type Id: int
        :param _DepartmentId: 资产组所属部门ID，如：1.2.3
        :type DepartmentId: str
        """
        self._Name = None
        self._Id = None
        self._DepartmentId = None

    @property
    def Name(self):
        r"""资产组名，最大长度32字符，不能为空
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DepartmentId(self):
        r"""资产组所属部门ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceGroupResponse(AbstractModel):
    r"""ModifyDeviceGroup返回参数结构体

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


class ModifyDeviceRequest(AbstractModel):
    r"""ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 资产记录ID
        :type Id: int
        :param _Port: 管理端口
        :type Port: int
        :param _GroupIdSet: 资产所属组ID集合
        :type GroupIdSet: list of int non-negative
        :param _DepartmentId: 资产所属部门ID
        :type DepartmentId: str
        :param _DomainId: 网络域Id
        :type DomainId: str
        """
        self._Id = None
        self._Port = None
        self._GroupIdSet = None
        self._DepartmentId = None
        self._DomainId = None

    @property
    def Id(self):
        r"""资产记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Port(self):
        r"""管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupIdSet(self):
        r"""资产所属组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def DepartmentId(self):
        r"""资产所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DomainId(self):
        r"""网络域Id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Port = params.get("Port")
        self._GroupIdSet = params.get("GroupIdSet")
        self._DepartmentId = params.get("DepartmentId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    r"""ModifyDevice返回参数结构体

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


class ModifyLDAPSettingRequest(AbstractModel):
    r"""ModifyLDAPSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启LDAP认证，false-不开启，true-开启
        :type Enable: bool
        :param _Ip: 服务器地址
        :type Ip: str
        :param _IpBackup: 备用服务器地址
        :type IpBackup: str
        :param _Port: 服务端口
        :type Port: int
        :param _EnableSSL: 是否开启SSL，false-不开启，true-开启
        :type EnableSSL: bool
        :param _BaseDN: Base DN
        :type BaseDN: str
        :param _AdminAccount: 管理员账号
        :type AdminAccount: str
        :param _AdminPassword: 管理员密码
        :type AdminPassword: str
        :param _AttributeUser: 用户属性
        :type AttributeUser: str
        :param _AttributeUserName: 用户名属性
        :type AttributeUserName: str
        :param _AutoSync: 自动同步，false-不开启，true-开启
        :type AutoSync: bool
        :param _Overwrite: 覆盖用户信息，false-不开启，true-开启
        :type Overwrite: bool
        :param _SyncPeriod: 同步周期，30～60000之间的整数
        :type SyncPeriod: int
        :param _SyncAll: 是否同步全部，false-不开启，true-开启
        :type SyncAll: bool
        :param _SyncUnitSet: 同步OU列表，SyncAll为false时必传
        :type SyncUnitSet: list of str
        :param _AttributeUnit: 组织单元属性
        :type AttributeUnit: str
        :param _AttributeRealName: 用户姓名属性
        :type AttributeRealName: str
        :param _AttributePhone: 手机号属性
        :type AttributePhone: str
        :param _AttributeEmail: 邮箱属性
        :type AttributeEmail: str
        :param _DomainId: 网络域Id
        :type DomainId: str
        """
        self._Enable = None
        self._Ip = None
        self._IpBackup = None
        self._Port = None
        self._EnableSSL = None
        self._BaseDN = None
        self._AdminAccount = None
        self._AdminPassword = None
        self._AttributeUser = None
        self._AttributeUserName = None
        self._AutoSync = None
        self._Overwrite = None
        self._SyncPeriod = None
        self._SyncAll = None
        self._SyncUnitSet = None
        self._AttributeUnit = None
        self._AttributeRealName = None
        self._AttributePhone = None
        self._AttributeEmail = None
        self._DomainId = None

    @property
    def Enable(self):
        r"""是否开启LDAP认证，false-不开启，true-开启
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Ip(self):
        r"""服务器地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def IpBackup(self):
        r"""备用服务器地址
        :rtype: str
        """
        return self._IpBackup

    @IpBackup.setter
    def IpBackup(self, IpBackup):
        self._IpBackup = IpBackup

    @property
    def Port(self):
        r"""服务端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EnableSSL(self):
        r"""是否开启SSL，false-不开启，true-开启
        :rtype: bool
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def BaseDN(self):
        r"""Base DN
        :rtype: str
        """
        return self._BaseDN

    @BaseDN.setter
    def BaseDN(self, BaseDN):
        self._BaseDN = BaseDN

    @property
    def AdminAccount(self):
        r"""管理员账号
        :rtype: str
        """
        return self._AdminAccount

    @AdminAccount.setter
    def AdminAccount(self, AdminAccount):
        self._AdminAccount = AdminAccount

    @property
    def AdminPassword(self):
        r"""管理员密码
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def AttributeUser(self):
        r"""用户属性
        :rtype: str
        """
        return self._AttributeUser

    @AttributeUser.setter
    def AttributeUser(self, AttributeUser):
        self._AttributeUser = AttributeUser

    @property
    def AttributeUserName(self):
        r"""用户名属性
        :rtype: str
        """
        return self._AttributeUserName

    @AttributeUserName.setter
    def AttributeUserName(self, AttributeUserName):
        self._AttributeUserName = AttributeUserName

    @property
    def AutoSync(self):
        r"""自动同步，false-不开启，true-开启
        :rtype: bool
        """
        return self._AutoSync

    @AutoSync.setter
    def AutoSync(self, AutoSync):
        self._AutoSync = AutoSync

    @property
    def Overwrite(self):
        r"""覆盖用户信息，false-不开启，true-开启
        :rtype: bool
        """
        return self._Overwrite

    @Overwrite.setter
    def Overwrite(self, Overwrite):
        self._Overwrite = Overwrite

    @property
    def SyncPeriod(self):
        r"""同步周期，30～60000之间的整数
        :rtype: int
        """
        return self._SyncPeriod

    @SyncPeriod.setter
    def SyncPeriod(self, SyncPeriod):
        self._SyncPeriod = SyncPeriod

    @property
    def SyncAll(self):
        r"""是否同步全部，false-不开启，true-开启
        :rtype: bool
        """
        return self._SyncAll

    @SyncAll.setter
    def SyncAll(self, SyncAll):
        self._SyncAll = SyncAll

    @property
    def SyncUnitSet(self):
        r"""同步OU列表，SyncAll为false时必传
        :rtype: list of str
        """
        return self._SyncUnitSet

    @SyncUnitSet.setter
    def SyncUnitSet(self, SyncUnitSet):
        self._SyncUnitSet = SyncUnitSet

    @property
    def AttributeUnit(self):
        r"""组织单元属性
        :rtype: str
        """
        return self._AttributeUnit

    @AttributeUnit.setter
    def AttributeUnit(self, AttributeUnit):
        self._AttributeUnit = AttributeUnit

    @property
    def AttributeRealName(self):
        r"""用户姓名属性
        :rtype: str
        """
        return self._AttributeRealName

    @AttributeRealName.setter
    def AttributeRealName(self, AttributeRealName):
        self._AttributeRealName = AttributeRealName

    @property
    def AttributePhone(self):
        r"""手机号属性
        :rtype: str
        """
        return self._AttributePhone

    @AttributePhone.setter
    def AttributePhone(self, AttributePhone):
        self._AttributePhone = AttributePhone

    @property
    def AttributeEmail(self):
        r"""邮箱属性
        :rtype: str
        """
        return self._AttributeEmail

    @AttributeEmail.setter
    def AttributeEmail(self, AttributeEmail):
        self._AttributeEmail = AttributeEmail

    @property
    def DomainId(self):
        r"""网络域Id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Ip = params.get("Ip")
        self._IpBackup = params.get("IpBackup")
        self._Port = params.get("Port")
        self._EnableSSL = params.get("EnableSSL")
        self._BaseDN = params.get("BaseDN")
        self._AdminAccount = params.get("AdminAccount")
        self._AdminPassword = params.get("AdminPassword")
        self._AttributeUser = params.get("AttributeUser")
        self._AttributeUserName = params.get("AttributeUserName")
        self._AutoSync = params.get("AutoSync")
        self._Overwrite = params.get("Overwrite")
        self._SyncPeriod = params.get("SyncPeriod")
        self._SyncAll = params.get("SyncAll")
        self._SyncUnitSet = params.get("SyncUnitSet")
        self._AttributeUnit = params.get("AttributeUnit")
        self._AttributeRealName = params.get("AttributeRealName")
        self._AttributePhone = params.get("AttributePhone")
        self._AttributeEmail = params.get("AttributeEmail")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLDAPSettingResponse(AbstractModel):
    r"""ModifyLDAPSetting返回参数结构体

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


class ModifyOAuthSettingRequest(AbstractModel):
    r"""ModifyOAuthSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启OAuth认证，false-不开启，true-开启。
        :type Enable: bool
        :param _AuthMethod: OAuth认证方式。
        :type AuthMethod: str
        :param _ClientId: OAuth认证客户端Id
        :type ClientId: str
        :param _ClientSecret: OAuth认证客户端密钥
        :type ClientSecret: str
        :param _CodeUrl: 获取OAuth认证授权码URL
        :type CodeUrl: str
        :param _TokenUrl: 获取OAuth令牌URL
        :type TokenUrl: str
        :param _UserInfoUrl: 获取OAuth用户信息URL
        :type UserInfoUrl: str
        :param _Scopes: 使用Okta认证时指定范围。为空时默认使用 openid、profile、email。
        :type Scopes: list of str
        """
        self._Enable = None
        self._AuthMethod = None
        self._ClientId = None
        self._ClientSecret = None
        self._CodeUrl = None
        self._TokenUrl = None
        self._UserInfoUrl = None
        self._Scopes = None

    @property
    def Enable(self):
        r"""是否开启OAuth认证，false-不开启，true-开启。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AuthMethod(self):
        r"""OAuth认证方式。
        :rtype: str
        """
        return self._AuthMethod

    @AuthMethod.setter
    def AuthMethod(self, AuthMethod):
        self._AuthMethod = AuthMethod

    @property
    def ClientId(self):
        r"""OAuth认证客户端Id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        r"""OAuth认证客户端密钥
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def CodeUrl(self):
        r"""获取OAuth认证授权码URL
        :rtype: str
        """
        return self._CodeUrl

    @CodeUrl.setter
    def CodeUrl(self, CodeUrl):
        self._CodeUrl = CodeUrl

    @property
    def TokenUrl(self):
        r"""获取OAuth令牌URL
        :rtype: str
        """
        return self._TokenUrl

    @TokenUrl.setter
    def TokenUrl(self, TokenUrl):
        self._TokenUrl = TokenUrl

    @property
    def UserInfoUrl(self):
        r"""获取OAuth用户信息URL
        :rtype: str
        """
        return self._UserInfoUrl

    @UserInfoUrl.setter
    def UserInfoUrl(self, UserInfoUrl):
        self._UserInfoUrl = UserInfoUrl

    @property
    def Scopes(self):
        r"""使用Okta认证时指定范围。为空时默认使用 openid、profile、email。
        :rtype: list of str
        """
        return self._Scopes

    @Scopes.setter
    def Scopes(self, Scopes):
        self._Scopes = Scopes


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._AuthMethod = params.get("AuthMethod")
        self._ClientId = params.get("ClientId")
        self._ClientSecret = params.get("ClientSecret")
        self._CodeUrl = params.get("CodeUrl")
        self._TokenUrl = params.get("TokenUrl")
        self._UserInfoUrl = params.get("UserInfoUrl")
        self._Scopes = params.get("Scopes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOAuthSettingResponse(AbstractModel):
    r"""ModifyOAuthSetting返回参数结构体

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


class ModifyOperationTaskRequest(AbstractModel):
    r"""ModifyOperationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务Id
        :type Id: int
        :param _Name: 任务名称
        :type Name: str
        :param _Type: 任务类型, 1 - 手工执行, 2 - 周期性自动执行
        :type Type: int
        :param _Account: 执行账号
        :type Account: str
        :param _Timeout: 超时时间,单位秒
        :type Timeout: int
        :param _Script: 执行脚本内容
        :type Script: str
        :param _DeviceIdSet: 执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :type DeviceIdSet: list of int non-negative
        :param _Period: 执行间隔，单位天. 手工执行时无需传入
        :type Period: int
        :param _FirstTime: 首次执行日期，默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :type FirstTime: str
        :param _Encoding: Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
        :type Encoding: int
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Account = None
        self._Timeout = None
        self._Script = None
        self._DeviceIdSet = None
        self._Period = None
        self._FirstTime = None
        self._Encoding = None

    @property
    def Id(self):
        r"""任务Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""任务类型, 1 - 手工执行, 2 - 周期性自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Account(self):
        r"""执行账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Timeout(self):
        r"""超时时间,单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Script(self):
        r"""执行脚本内容
        :rtype: str
        """
        return self._Script

    @Script.setter
    def Script(self, Script):
        self._Script = Script

    @property
    def DeviceIdSet(self):
        r"""执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def Period(self):
        r"""执行间隔，单位天. 手工执行时无需传入
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        r"""首次执行日期，默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Encoding(self):
        r"""Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Account = params.get("Account")
        self._Timeout = params.get("Timeout")
        self._Script = params.get("Script")
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._Period = params.get("Period")
        self._FirstTime = params.get("FirstTime")
        self._Encoding = params.get("Encoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOperationTaskResponse(AbstractModel):
    r"""ModifyOperationTask返回参数结构体

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


class ModifyReconnectionSettingRequest(AbstractModel):
    r"""ModifyReconnectionSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReconnectionMaxCount: 重试次数,取值范围：0-20
        :type ReconnectionMaxCount: int
        :param _Enable: true：限制重连次数，false：不限制重连次数
        :type Enable: bool
        """
        self._ReconnectionMaxCount = None
        self._Enable = None

    @property
    def ReconnectionMaxCount(self):
        r"""重试次数,取值范围：0-20
        :rtype: int
        """
        return self._ReconnectionMaxCount

    @ReconnectionMaxCount.setter
    def ReconnectionMaxCount(self, ReconnectionMaxCount):
        self._ReconnectionMaxCount = ReconnectionMaxCount

    @property
    def Enable(self):
        r"""true：限制重连次数，false：不限制重连次数
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._ReconnectionMaxCount = params.get("ReconnectionMaxCount")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReconnectionSettingResponse(AbstractModel):
    r"""ModifyReconnectionSetting返回参数结构体

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


class ModifyResourceRequest(AbstractModel):
    r"""ModifyResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 需要开通服务的资源ID
        :type ResourceId: str
        :param _Status: 状态
        :type Status: str
        :param _ResourceEdition: 实例版本
        :type ResourceEdition: str
        :param _ResourceNode: 资源节点数
        :type ResourceNode: int
        :param _AutoRenewFlag: 自动续费
        :type AutoRenewFlag: int
        :param _PackageBandwidth: 带宽扩展包个数(4M)
        :type PackageBandwidth: int
        :param _PackageNode: 授权点数扩展包个数(50点)
        :type PackageNode: int
        :param _LogDelivery: 日志投递
        :type LogDelivery: int
        """
        self._ResourceId = None
        self._Status = None
        self._ResourceEdition = None
        self._ResourceNode = None
        self._AutoRenewFlag = None
        self._PackageBandwidth = None
        self._PackageNode = None
        self._LogDelivery = None

    @property
    def ResourceId(self):
        r"""需要开通服务的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        self._Status = Status

    @property
    def ResourceEdition(self):
        r"""实例版本
        :rtype: str
        """
        return self._ResourceEdition

    @ResourceEdition.setter
    def ResourceEdition(self, ResourceEdition):
        self._ResourceEdition = ResourceEdition

    @property
    def ResourceNode(self):
        r"""资源节点数
        :rtype: int
        """
        return self._ResourceNode

    @ResourceNode.setter
    def ResourceNode(self, ResourceNode):
        self._ResourceNode = ResourceNode

    @property
    def AutoRenewFlag(self):
        r"""自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PackageBandwidth(self):
        r"""带宽扩展包个数(4M)
        :rtype: int
        """
        return self._PackageBandwidth

    @PackageBandwidth.setter
    def PackageBandwidth(self, PackageBandwidth):
        self._PackageBandwidth = PackageBandwidth

    @property
    def PackageNode(self):
        r"""授权点数扩展包个数(50点)
        :rtype: int
        """
        return self._PackageNode

    @PackageNode.setter
    def PackageNode(self, PackageNode):
        self._PackageNode = PackageNode

    @property
    def LogDelivery(self):
        r"""日志投递
        :rtype: int
        """
        return self._LogDelivery

    @LogDelivery.setter
    def LogDelivery(self, LogDelivery):
        self._LogDelivery = LogDelivery


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        self._ResourceEdition = params.get("ResourceEdition")
        self._ResourceNode = params.get("ResourceNode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PackageBandwidth = params.get("PackageBandwidth")
        self._PackageNode = params.get("PackageNode")
        self._LogDelivery = params.get("LogDelivery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceResponse(AbstractModel):
    r"""ModifyResource返回参数结构体

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


class ModifyUserDirectoryRequest(AbstractModel):
    r"""ModifyUserDirectory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 目录id
        :type Id: int
        :param _UserOrgSet: ioa分组信息
        :type UserOrgSet: list of UserOrg
        """
        self._Id = None
        self._UserOrgSet = None

    @property
    def Id(self):
        r"""目录id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserOrgSet(self):
        r"""ioa分组信息
        :rtype: list of UserOrg
        """
        return self._UserOrgSet

    @UserOrgSet.setter
    def UserOrgSet(self, UserOrgSet):
        self._UserOrgSet = UserOrgSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("UserOrgSet") is not None:
            self._UserOrgSet = []
            for item in params.get("UserOrgSet"):
                obj = UserOrg()
                obj._deserialize(item)
                self._UserOrgSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserDirectoryResponse(AbstractModel):
    r"""ModifyUserDirectory返回参数结构体

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


class ModifyUserGroupRequest(AbstractModel):
    r"""ModifyUserGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 用户组ID
        :type Id: int
        :param _Name: 用户组名
        :type Name: str
        :param _DepartmentId: 用户组所属的部门ID，如：1.2.3
        :type DepartmentId: str
        """
        self._Id = None
        self._Name = None
        self._DepartmentId = None

    @property
    def Id(self):
        r"""用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""用户组名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        r"""用户组所属的部门ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserGroupResponse(AbstractModel):
    r"""ModifyUserGroup返回参数结构体

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


class ModifyUserRequest(AbstractModel):
    r"""ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 用户ID
        :type Id: int
        :param _RealName: 用户姓名，最大长度20个字符，不能包含空格
        :type RealName: str
        :param _Phone: 按照"国家地区代码|手机号"的格式输入。如: "+86|xxxxxxxx"
        :type Phone: str
        :param _Email: 电子邮件
        :type Email: str
        :param _ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param _GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param _AuthType: 认证方式，0 - 本地，1 - LDAP，2 - OAuth 不传则默认为0
        :type AuthType: int
        :param _ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param _DepartmentId: 用户所属部门的ID，如1.2.3
        :type DepartmentId: str
        """
        self._Id = None
        self._RealName = None
        self._Phone = None
        self._Email = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._GroupIdSet = None
        self._AuthType = None
        self._ValidateTime = None
        self._DepartmentId = None

    @property
    def Id(self):
        r"""用户ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RealName(self):
        r"""用户姓名，最大长度20个字符，不能包含空格
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Phone(self):
        r"""按照"国家地区代码|手机号"的格式输入。如: "+86|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""电子邮件
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        r"""用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupIdSet(self):
        r"""所属用户组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def AuthType(self):
        r"""认证方式，0 - 本地，1 - LDAP，2 - OAuth 不传则默认为0
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        r"""访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def DepartmentId(self):
        r"""用户所属部门的ID，如1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RealName = params.get("RealName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        self._GroupIdSet = params.get("GroupIdSet")
        self._AuthType = params.get("AuthType")
        self._ValidateTime = params.get("ValidateTime")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    r"""ModifyUser返回参数结构体

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


class OperationEvent(AbstractModel):
    r"""操作日志

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _Time: 操作时间
        :type Time: str
        :param _SourceIp: 来源IP
        :type SourceIp: str
        :param _Kind: 操作类型
        :type Kind: int
        :param _Operation: 具体操作内容
        :type Operation: str
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
        :param _SignValue: 签名值
        :type SignValue: str
        """
        self._UserName = None
        self._RealName = None
        self._Time = None
        self._SourceIp = None
        self._Kind = None
        self._Operation = None
        self._Result = None
        self._SignValue = None

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Time(self):
        r"""操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SourceIp(self):
        r"""来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Kind(self):
        r"""操作类型
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Operation(self):
        r"""具体操作内容
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Result(self):
        r"""操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SignValue(self):
        r"""签名值
        :rtype: str
        """
        return self._SignValue

    @SignValue.setter
    def SignValue(self, SignValue):
        self._SignValue = SignValue


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Time = params.get("Time")
        self._SourceIp = params.get("SourceIp")
        self._Kind = params.get("Kind")
        self._Operation = params.get("Operation")
        self._Result = params.get("Result")
        self._SignValue = params.get("SignValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationTask(AbstractModel):
    r"""运维任务信息

    """

    def __init__(self):
        r"""
        :param _Id: 运维任务主键ID
        :type Id: int
        :param _OperationId: 运维任务ID
        :type OperationId: str
        :param _Name: 运维任务名称
        :type Name: str
        :param _UserName: 创建用户
        :type UserName: str
        :param _RealName: 运维人员姓名
        :type RealName: str
        :param _Type: 任务类型，1 - 手工执行任务， 2 - 周期性任务
        :type Type: int
        :param _Period: 周期性任务执行间隔，单位天
        :type Period: int
        :param _NextTime: 执行账户
        :type NextTime: str
        :param _FirstTime: 下一次执行时间
        :type FirstTime: str
        """
        self._Id = None
        self._OperationId = None
        self._Name = None
        self._UserName = None
        self._RealName = None
        self._Type = None
        self._Period = None
        self._NextTime = None
        self._FirstTime = None

    @property
    def Id(self):
        r"""运维任务主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationId(self):
        r"""运维任务ID
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserName(self):
        r"""创建用户
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""运维人员姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Type(self):
        r"""任务类型，1 - 手工执行任务， 2 - 周期性任务
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        r"""周期性任务执行间隔，单位天
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def NextTime(self):
        r"""执行账户
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        self._NextTime = NextTime

    @property
    def FirstTime(self):
        r"""下一次执行时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OperationId = params.get("OperationId")
        self._Name = params.get("Name")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        self._NextTime = params.get("NextTime")
        self._FirstTime = params.get("FirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconnectionSetting(AbstractModel):
    r"""运维资产重连次数

    """

    def __init__(self):
        r"""
        :param _ReconnectionMaxCount: 重连次数
        :type ReconnectionMaxCount: int
        :param _Enable: true：可以重连，false：不可以重连
        :type Enable: bool
        """
        self._ReconnectionMaxCount = None
        self._Enable = None

    @property
    def ReconnectionMaxCount(self):
        r"""重连次数
        :rtype: int
        """
        return self._ReconnectionMaxCount

    @ReconnectionMaxCount.setter
    def ReconnectionMaxCount(self, ReconnectionMaxCount):
        self._ReconnectionMaxCount = ReconnectionMaxCount

    @property
    def Enable(self):
        r"""true：可以重连，false：不可以重连
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._ReconnectionMaxCount = params.get("ReconnectionMaxCount")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplayInformation(AbstractModel):
    r"""回放所需字段信息

    """

    def __init__(self):
        r"""
        :param _Token: 令牌
        :type Token: str
        :param _StartTime: 会话开始时间
        :type StartTime: str
        :param _Address: 回放链接
        :type Address: str
        :param _ReplayType: 回放类型 ，默认0， 1-rfb 2-mp4 3-ssh
        :type ReplayType: int
        """
        self._Token = None
        self._StartTime = None
        self._Address = None
        self._ReplayType = None

    @property
    def Token(self):
        r"""令牌
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def StartTime(self):
        r"""会话开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Address(self):
        r"""回放链接
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ReplayType(self):
        r"""回放类型 ，默认0， 1-rfb 2-mp4 3-ssh
        :rtype: int
        """
        return self._ReplayType

    @ReplayType.setter
    def ReplayType(self, ReplayType):
        self._ReplayType = ReplayType


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._StartTime = params.get("StartTime")
        self._Address = params.get("Address")
        self._ReplayType = params.get("ReplayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaySessionRequest(AbstractModel):
    r"""ReplaySession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sid: 会话Sid
        :type Sid: str
        """
        self._Sid = None

    @property
    def Sid(self):
        r"""会话Sid
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaySessionResponse(AbstractModel):
    r"""ReplaySession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReplayInfo: 回放所需信息
        :type ReplayInfo: :class:`tencentcloud.bh.v20230418.models.ReplayInformation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReplayInfo = None
        self._RequestId = None

    @property
    def ReplayInfo(self):
        r"""回放所需信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.ReplayInformation`
        """
        return self._ReplayInfo

    @ReplayInfo.setter
    def ReplayInfo(self, ReplayInfo):
        self._ReplayInfo = ReplayInfo

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
        if params.get("ReplayInfo") is not None:
            self._ReplayInfo = ReplayInformation()
            self._ReplayInfo._deserialize(params.get("ReplayInfo"))
        self._RequestId = params.get("RequestId")


class ResetDeviceAccountPasswordRequest(AbstractModel):
    r"""ResetDeviceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceAccountPasswordResponse(AbstractModel):
    r"""ResetDeviceAccountPassword返回参数结构体

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


class ResetDeviceAccountPrivateKeyRequest(AbstractModel):
    r"""ResetDeviceAccountPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceAccountPrivateKeyResponse(AbstractModel):
    r"""ResetDeviceAccountPrivateKey返回参数结构体

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


class ResetUserRequest(AbstractModel):
    r"""ResetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 用户ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""用户ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetUserResponse(AbstractModel):
    r"""ResetUser返回参数结构体

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


class Resource(AbstractModel):
    r"""堡垒机服务信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 服务实例ID，如bh-saas-s3ed4r5e
        :type ResourceId: str
        :param _ApCode: 地域编码
        :type ApCode: str
        :param _SvArgs: 服务实例规格信息
        :type SvArgs: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _Nodes: 服务规格对应的资产数
        :type Nodes: int
        :param _RenewFlag: 自动续费标记，0 - 表示默认状态，1 - 表示自动续费，2 - 表示明确不自动续费
        :type RenewFlag: int
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _Status: 资源状态，0 - 未初始化，1 - 正常，2 - 隔离，3 - 销毁，4 - 初始化失败，5 - 初始化中
        :type Status: int
        :param _ResourceName: 服务实例名，如T-Sec-堡垒机（SaaS型）
        :type ResourceName: str
        :param _Pid: 定价模型ID
        :type Pid: int
        :param _CreateTime: 资源创建时间
        :type CreateTime: str
        :param _ProductCode: 商品码, p_cds_dasb
        :type ProductCode: str
        :param _SubProductCode: 子商品码, sp_cds_dasb_bh_saas
        :type SubProductCode: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Expired: 是否过期，true-过期，false-未过期
        :type Expired: bool
        :param _Deployed: 是否开通，true-开通，false-未开通
        :type Deployed: bool
        :param _VpcName: 开通服务的 VPC 名称
        :type VpcName: str
        :param _VpcCidrBlock: 开通服务的 VPC 对应的网段
        :type VpcCidrBlock: str
        :param _SubnetId: 开通服务的子网ID
        :type SubnetId: str
        :param _SubnetName: 开通服务的子网名称
        :type SubnetName: str
        :param _CidrBlock: 开通服务的子网网段
        :type CidrBlock: str
        :param _PublicIpSet: 外部IP
        :type PublicIpSet: list of str
        :param _PrivateIpSet: 内部IP
        :type PrivateIpSet: list of str
        :param _ModuleSet: 服务开通的高级功能列表，如:[DB]
        :type ModuleSet: list of str
        :param _UsedNodes: 已使用的授权点数
        :type UsedNodes: int
        :param _ExtendPoints: 扩展点数
        :type ExtendPoints: int
        :param _PackageBandwidth: 带宽扩展包个数(4M)
        :type PackageBandwidth: int
        :param _PackageNode: 授权点数扩展包个数(50点)
        :type PackageNode: int
        :param _LogDeliveryArgs: 日志投递规格信息
        :type LogDeliveryArgs: str
        :param _ClbSet: 堡垒机资源LB	
        :type ClbSet: list of Clb
        :param _DomainCount: 网络域个数
        :type DomainCount: int
        :param _UsedDomainCount: 已经使用的网络域个数
        :type UsedDomainCount: int
        :param _Trial: 0 非试用版，1 试用版
        :type Trial: int
        :param _LogDelivery: 日志投递规格信息
        :type LogDelivery: str
        :param _CdcClusterId: cdc集群id
        :type CdcClusterId: str
        :param _DeployModel: 部署模式 默认0 0-cvm 1-tke
        :type DeployModel: int
        :param _IntranetAccess: 0 默认值，非内网访问，1 内网访问，2 内网访问开通中，3 内网访问关闭中
        :type IntranetAccess: int
        :param _IntranetPrivateIpSet: 内网访问的ip
        :type IntranetPrivateIpSet: list of str
        :param _IntranetVpcId: 开通内网访问的vpc
        :type IntranetVpcId: str
        :param _IntranetSubnetId: 开通内网访问的subnetId
        :type IntranetSubnetId: str
        :param _IntranetVpcCidr: 开通内网访问vpc的网段
        :type IntranetVpcCidr: str
        :param _DomainName: 堡垒机内网ip自定义域名
        :type DomainName: str
        :param _ShareClb: 是否共享clb，true-共享clb，false-独享clb
        :type ShareClb: bool
        :param _OpenClbId: 共享clb id
        :type OpenClbId: str
        :param _LbVipIsp: 运营商信息
        :type LbVipIsp: str
        :param _TUICmdPort: linux资产命令行运维端口
        :type TUICmdPort: int
        :param _TUIDirectPort: linux资产直连端口
        :type TUIDirectPort: int
        :param _WebAccess: 1 默认值，web访问开启，0 web访问关闭，2 web访问开通中，3 web访问关闭中
        :type WebAccess: int
        :param _ClientAccess: 1 默认值，客户单访问开启，0 客户端访问关闭，2 客户端访问开通中，3 客户端访问关闭中
        :type ClientAccess: int
        :param _ExternalAccess: 1 默认值，外网访问开启，0 外网访问关闭，2 外网访问开通中，3 外网访问关闭中
        :type ExternalAccess: int
        :param _IOAResource: 0默认值。0-免费版（试用版）ioa，1-付费版ioa
        :type IOAResource: int
        :param _PackageIOAUserCount: 零信任堡垒机用户扩展包个数。1个扩展包对应20个用户数
        :type PackageIOAUserCount: int
        :param _PackageIOABandwidth:  零信任堡垒机带宽扩展包个数。一个扩展包表示4M带宽
        :type PackageIOABandwidth: int
        :param _IOAResourceId: 堡垒机实例对应的零信任实例id
        :type IOAResourceId: str
        """
        self._ResourceId = None
        self._ApCode = None
        self._SvArgs = None
        self._VpcId = None
        self._Nodes = None
        self._RenewFlag = None
        self._ExpireTime = None
        self._Status = None
        self._ResourceName = None
        self._Pid = None
        self._CreateTime = None
        self._ProductCode = None
        self._SubProductCode = None
        self._Zone = None
        self._Expired = None
        self._Deployed = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._PublicIpSet = None
        self._PrivateIpSet = None
        self._ModuleSet = None
        self._UsedNodes = None
        self._ExtendPoints = None
        self._PackageBandwidth = None
        self._PackageNode = None
        self._LogDeliveryArgs = None
        self._ClbSet = None
        self._DomainCount = None
        self._UsedDomainCount = None
        self._Trial = None
        self._LogDelivery = None
        self._CdcClusterId = None
        self._DeployModel = None
        self._IntranetAccess = None
        self._IntranetPrivateIpSet = None
        self._IntranetVpcId = None
        self._IntranetSubnetId = None
        self._IntranetVpcCidr = None
        self._DomainName = None
        self._ShareClb = None
        self._OpenClbId = None
        self._LbVipIsp = None
        self._TUICmdPort = None
        self._TUIDirectPort = None
        self._WebAccess = None
        self._ClientAccess = None
        self._ExternalAccess = None
        self._IOAResource = None
        self._PackageIOAUserCount = None
        self._PackageIOABandwidth = None
        self._IOAResourceId = None

    @property
    def ResourceId(self):
        r"""服务实例ID，如bh-saas-s3ed4r5e
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ApCode(self):
        r"""地域编码
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def SvArgs(self):
        r"""服务实例规格信息
        :rtype: str
        """
        return self._SvArgs

    @SvArgs.setter
    def SvArgs(self, SvArgs):
        self._SvArgs = SvArgs

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Nodes(self):
        r"""服务规格对应的资产数
        :rtype: int
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def RenewFlag(self):
        r"""自动续费标记，0 - 表示默认状态，1 - 表示自动续费，2 - 表示明确不自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireTime(self):
        r"""过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        r"""资源状态，0 - 未初始化，1 - 正常，2 - 隔离，3 - 销毁，4 - 初始化失败，5 - 初始化中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceName(self):
        r"""服务实例名，如T-Sec-堡垒机（SaaS型）
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Pid(self):
        r"""定价模型ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def CreateTime(self):
        r"""资源创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductCode(self):
        r"""商品码, p_cds_dasb
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        r"""子商品码, sp_cds_dasb_bh_saas
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Expired(self):
        r"""是否过期，true-过期，false-未过期
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def Deployed(self):
        r"""是否开通，true-开通，false-未开通
        :rtype: bool
        """
        return self._Deployed

    @Deployed.setter
    def Deployed(self, Deployed):
        self._Deployed = Deployed

    @property
    def VpcName(self):
        r"""开通服务的 VPC 名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        r"""开通服务的 VPC 对应的网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        r"""开通服务的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""开通服务的子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        r"""开通服务的子网网段
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def PublicIpSet(self):
        r"""外部IP
        :rtype: list of str
        """
        return self._PublicIpSet

    @PublicIpSet.setter
    def PublicIpSet(self, PublicIpSet):
        self._PublicIpSet = PublicIpSet

    @property
    def PrivateIpSet(self):
        r"""内部IP
        :rtype: list of str
        """
        return self._PrivateIpSet

    @PrivateIpSet.setter
    def PrivateIpSet(self, PrivateIpSet):
        self._PrivateIpSet = PrivateIpSet

    @property
    def ModuleSet(self):
        r"""服务开通的高级功能列表，如:[DB]
        :rtype: list of str
        """
        return self._ModuleSet

    @ModuleSet.setter
    def ModuleSet(self, ModuleSet):
        self._ModuleSet = ModuleSet

    @property
    def UsedNodes(self):
        r"""已使用的授权点数
        :rtype: int
        """
        return self._UsedNodes

    @UsedNodes.setter
    def UsedNodes(self, UsedNodes):
        self._UsedNodes = UsedNodes

    @property
    def ExtendPoints(self):
        r"""扩展点数
        :rtype: int
        """
        return self._ExtendPoints

    @ExtendPoints.setter
    def ExtendPoints(self, ExtendPoints):
        self._ExtendPoints = ExtendPoints

    @property
    def PackageBandwidth(self):
        r"""带宽扩展包个数(4M)
        :rtype: int
        """
        return self._PackageBandwidth

    @PackageBandwidth.setter
    def PackageBandwidth(self, PackageBandwidth):
        self._PackageBandwidth = PackageBandwidth

    @property
    def PackageNode(self):
        r"""授权点数扩展包个数(50点)
        :rtype: int
        """
        return self._PackageNode

    @PackageNode.setter
    def PackageNode(self, PackageNode):
        self._PackageNode = PackageNode

    @property
    def LogDeliveryArgs(self):
        r"""日志投递规格信息
        :rtype: str
        """
        return self._LogDeliveryArgs

    @LogDeliveryArgs.setter
    def LogDeliveryArgs(self, LogDeliveryArgs):
        self._LogDeliveryArgs = LogDeliveryArgs

    @property
    def ClbSet(self):
        r"""堡垒机资源LB	
        :rtype: list of Clb
        """
        return self._ClbSet

    @ClbSet.setter
    def ClbSet(self, ClbSet):
        self._ClbSet = ClbSet

    @property
    def DomainCount(self):
        r"""网络域个数
        :rtype: int
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def UsedDomainCount(self):
        r"""已经使用的网络域个数
        :rtype: int
        """
        return self._UsedDomainCount

    @UsedDomainCount.setter
    def UsedDomainCount(self, UsedDomainCount):
        self._UsedDomainCount = UsedDomainCount

    @property
    def Trial(self):
        r"""0 非试用版，1 试用版
        :rtype: int
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def LogDelivery(self):
        r"""日志投递规格信息
        :rtype: str
        """
        return self._LogDelivery

    @LogDelivery.setter
    def LogDelivery(self, LogDelivery):
        self._LogDelivery = LogDelivery

    @property
    def CdcClusterId(self):
        r"""cdc集群id
        :rtype: str
        """
        return self._CdcClusterId

    @CdcClusterId.setter
    def CdcClusterId(self, CdcClusterId):
        self._CdcClusterId = CdcClusterId

    @property
    def DeployModel(self):
        r"""部署模式 默认0 0-cvm 1-tke
        :rtype: int
        """
        return self._DeployModel

    @DeployModel.setter
    def DeployModel(self, DeployModel):
        self._DeployModel = DeployModel

    @property
    def IntranetAccess(self):
        r"""0 默认值，非内网访问，1 内网访问，2 内网访问开通中，3 内网访问关闭中
        :rtype: int
        """
        return self._IntranetAccess

    @IntranetAccess.setter
    def IntranetAccess(self, IntranetAccess):
        self._IntranetAccess = IntranetAccess

    @property
    def IntranetPrivateIpSet(self):
        r"""内网访问的ip
        :rtype: list of str
        """
        return self._IntranetPrivateIpSet

    @IntranetPrivateIpSet.setter
    def IntranetPrivateIpSet(self, IntranetPrivateIpSet):
        self._IntranetPrivateIpSet = IntranetPrivateIpSet

    @property
    def IntranetVpcId(self):
        r"""开通内网访问的vpc
        :rtype: str
        """
        return self._IntranetVpcId

    @IntranetVpcId.setter
    def IntranetVpcId(self, IntranetVpcId):
        self._IntranetVpcId = IntranetVpcId

    @property
    def IntranetSubnetId(self):
        r"""开通内网访问的subnetId
        :rtype: str
        """
        return self._IntranetSubnetId

    @IntranetSubnetId.setter
    def IntranetSubnetId(self, IntranetSubnetId):
        self._IntranetSubnetId = IntranetSubnetId

    @property
    def IntranetVpcCidr(self):
        r"""开通内网访问vpc的网段
        :rtype: str
        """
        return self._IntranetVpcCidr

    @IntranetVpcCidr.setter
    def IntranetVpcCidr(self, IntranetVpcCidr):
        self._IntranetVpcCidr = IntranetVpcCidr

    @property
    def DomainName(self):
        r"""堡垒机内网ip自定义域名
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ShareClb(self):
        r"""是否共享clb，true-共享clb，false-独享clb
        :rtype: bool
        """
        return self._ShareClb

    @ShareClb.setter
    def ShareClb(self, ShareClb):
        self._ShareClb = ShareClb

    @property
    def OpenClbId(self):
        r"""共享clb id
        :rtype: str
        """
        return self._OpenClbId

    @OpenClbId.setter
    def OpenClbId(self, OpenClbId):
        self._OpenClbId = OpenClbId

    @property
    def LbVipIsp(self):
        r"""运营商信息
        :rtype: str
        """
        return self._LbVipIsp

    @LbVipIsp.setter
    def LbVipIsp(self, LbVipIsp):
        self._LbVipIsp = LbVipIsp

    @property
    def TUICmdPort(self):
        r"""linux资产命令行运维端口
        :rtype: int
        """
        return self._TUICmdPort

    @TUICmdPort.setter
    def TUICmdPort(self, TUICmdPort):
        self._TUICmdPort = TUICmdPort

    @property
    def TUIDirectPort(self):
        r"""linux资产直连端口
        :rtype: int
        """
        return self._TUIDirectPort

    @TUIDirectPort.setter
    def TUIDirectPort(self, TUIDirectPort):
        self._TUIDirectPort = TUIDirectPort

    @property
    def WebAccess(self):
        r"""1 默认值，web访问开启，0 web访问关闭，2 web访问开通中，3 web访问关闭中
        :rtype: int
        """
        return self._WebAccess

    @WebAccess.setter
    def WebAccess(self, WebAccess):
        self._WebAccess = WebAccess

    @property
    def ClientAccess(self):
        r"""1 默认值，客户单访问开启，0 客户端访问关闭，2 客户端访问开通中，3 客户端访问关闭中
        :rtype: int
        """
        return self._ClientAccess

    @ClientAccess.setter
    def ClientAccess(self, ClientAccess):
        self._ClientAccess = ClientAccess

    @property
    def ExternalAccess(self):
        r"""1 默认值，外网访问开启，0 外网访问关闭，2 外网访问开通中，3 外网访问关闭中
        :rtype: int
        """
        return self._ExternalAccess

    @ExternalAccess.setter
    def ExternalAccess(self, ExternalAccess):
        self._ExternalAccess = ExternalAccess

    @property
    def IOAResource(self):
        r"""0默认值。0-免费版（试用版）ioa，1-付费版ioa
        :rtype: int
        """
        return self._IOAResource

    @IOAResource.setter
    def IOAResource(self, IOAResource):
        self._IOAResource = IOAResource

    @property
    def PackageIOAUserCount(self):
        r"""零信任堡垒机用户扩展包个数。1个扩展包对应20个用户数
        :rtype: int
        """
        return self._PackageIOAUserCount

    @PackageIOAUserCount.setter
    def PackageIOAUserCount(self, PackageIOAUserCount):
        self._PackageIOAUserCount = PackageIOAUserCount

    @property
    def PackageIOABandwidth(self):
        r""" 零信任堡垒机带宽扩展包个数。一个扩展包表示4M带宽
        :rtype: int
        """
        return self._PackageIOABandwidth

    @PackageIOABandwidth.setter
    def PackageIOABandwidth(self, PackageIOABandwidth):
        self._PackageIOABandwidth = PackageIOABandwidth

    @property
    def IOAResourceId(self):
        r"""堡垒机实例对应的零信任实例id
        :rtype: str
        """
        return self._IOAResourceId

    @IOAResourceId.setter
    def IOAResourceId(self, IOAResourceId):
        self._IOAResourceId = IOAResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ApCode = params.get("ApCode")
        self._SvArgs = params.get("SvArgs")
        self._VpcId = params.get("VpcId")
        self._Nodes = params.get("Nodes")
        self._RenewFlag = params.get("RenewFlag")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        self._ResourceName = params.get("ResourceName")
        self._Pid = params.get("Pid")
        self._CreateTime = params.get("CreateTime")
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._Zone = params.get("Zone")
        self._Expired = params.get("Expired")
        self._Deployed = params.get("Deployed")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._PublicIpSet = params.get("PublicIpSet")
        self._PrivateIpSet = params.get("PrivateIpSet")
        self._ModuleSet = params.get("ModuleSet")
        self._UsedNodes = params.get("UsedNodes")
        self._ExtendPoints = params.get("ExtendPoints")
        self._PackageBandwidth = params.get("PackageBandwidth")
        self._PackageNode = params.get("PackageNode")
        self._LogDeliveryArgs = params.get("LogDeliveryArgs")
        if params.get("ClbSet") is not None:
            self._ClbSet = []
            for item in params.get("ClbSet"):
                obj = Clb()
                obj._deserialize(item)
                self._ClbSet.append(obj)
        self._DomainCount = params.get("DomainCount")
        self._UsedDomainCount = params.get("UsedDomainCount")
        self._Trial = params.get("Trial")
        self._LogDelivery = params.get("LogDelivery")
        self._CdcClusterId = params.get("CdcClusterId")
        self._DeployModel = params.get("DeployModel")
        self._IntranetAccess = params.get("IntranetAccess")
        self._IntranetPrivateIpSet = params.get("IntranetPrivateIpSet")
        self._IntranetVpcId = params.get("IntranetVpcId")
        self._IntranetSubnetId = params.get("IntranetSubnetId")
        self._IntranetVpcCidr = params.get("IntranetVpcCidr")
        self._DomainName = params.get("DomainName")
        self._ShareClb = params.get("ShareClb")
        self._OpenClbId = params.get("OpenClbId")
        self._LbVipIsp = params.get("LbVipIsp")
        self._TUICmdPort = params.get("TUICmdPort")
        self._TUIDirectPort = params.get("TUIDirectPort")
        self._WebAccess = params.get("WebAccess")
        self._ClientAccess = params.get("ClientAccess")
        self._ExternalAccess = params.get("ExternalAccess")
        self._IOAResource = params.get("IOAResource")
        self._PackageIOAUserCount = params.get("PackageIOAUserCount")
        self._PackageIOABandwidth = params.get("PackageIOABandwidth")
        self._IOAResourceId = params.get("IOAResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunChangePwdTaskDetail(AbstractModel):
    r"""立即执行改密任务的入参

    """

    def __init__(self):
        r"""
        :param _DeviceId: 资产id
        :type DeviceId: int
        :param _Account: 资产账号
        :type Account: str
        """
        self._DeviceId = None
        self._Account = None

    @property
    def DeviceId(self):
        r"""资产id
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Account(self):
        r"""资产账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Account = params.get("Account")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunChangePwdTaskRequest(AbstractModel):
    r"""RunChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationId: 任务Id
        :type OperationId: str
        :param _DepartmentId: 部门id
        :type DepartmentId: str
        :param _Details: 改密任务详情
        :type Details: list of RunChangePwdTaskDetail
        """
        self._OperationId = None
        self._DepartmentId = None
        self._Details = None

    @property
    def OperationId(self):
        r"""任务Id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DepartmentId(self):
        r"""部门id
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Details(self):
        r"""改密任务详情
        :rtype: list of RunChangePwdTaskDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._OperationId = params.get("OperationId")
        self._DepartmentId = params.get("DepartmentId")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = RunChangePwdTaskDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunChangePwdTaskResponse(AbstractModel):
    r"""RunChangePwdTask返回参数结构体

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


class RunOperationTaskRequest(AbstractModel):
    r"""RunOperationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 运维任务ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""运维任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOperationTaskResponse(AbstractModel):
    r"""RunOperationTask返回参数结构体

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


class SearchAuditLogRequest(AbstractModel):
    r"""SearchAuditLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，不得早于当前时间的180天前
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 每页容量，默认为20，最大200
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        r"""开始时间，不得早于当前时间的180天前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页容量，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAuditLogResponse(AbstractModel):
    r"""SearchAuditLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 日志总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""日志总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchCommandBySidRequest(AbstractModel):
    r"""SearchCommandBySid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sid: 会话Id
        :type Sid: str
        :param _Cmd: 命令，可模糊搜索
        :type Cmd: str
        :param _Encoding: Cmd字段是前端传值是否进行base64.
0:否，1：是
        :type Encoding: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 每页容量，默认20，最大200
        :type Limit: int
        :param _AuditAction: 根据拦截状态进行过滤
        :type AuditAction: list of int non-negative
        """
        self._Sid = None
        self._Cmd = None
        self._Encoding = None
        self._Offset = None
        self._Limit = None
        self._AuditAction = None

    @property
    def Sid(self):
        r"""会话Id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Cmd(self):
        r"""命令，可模糊搜索
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Encoding(self):
        r"""Cmd字段是前端传值是否进行base64.
0:否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页容量，默认20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AuditAction(self):
        r"""根据拦截状态进行过滤
        :rtype: list of int non-negative
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._Cmd = params.get("Cmd")
        self._Encoding = params.get("Encoding")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AuditAction = params.get("AuditAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCommandBySidResponse(AbstractModel):
    r"""SearchCommandBySid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _CommandSet: 命令列表
        :type CommandSet: list of Command
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CommandSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CommandSet(self):
        r"""命令列表
        :rtype: list of Command
        """
        return self._CommandSet

    @CommandSet.setter
    def CommandSet(self, CommandSet):
        self._CommandSet = CommandSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("CommandSet") is not None:
            self._CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self._CommandSet.append(obj)
        self._RequestId = params.get("RequestId")


class SearchCommandRequest(AbstractModel):
    r"""SearchCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 搜索区间的开始时间
        :type StartTime: str
        :param _EndTime: 搜索区间的结束时间，不填默认为开始时间到现在为止
        :type EndTime: str
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _InstanceId: 资产实例ID
        :type InstanceId: str
        :param _DeviceName: 资产名称
        :type DeviceName: str
        :param _PublicIp: 资产的公网IP
        :type PublicIp: str
        :param _PrivateIp: 资产的内网IP
        :type PrivateIp: str
        :param _Cmd: 执行的命令
        :type Cmd: str
        :param _Encoding: Cmd字段是前端传值是否进行base64.
0:否，1：是
        :type Encoding: int
        :param _AuditAction: 根据拦截状态进行过滤：1 - 已执行，2 - 被阻断
        :type AuditAction: list of int non-negative
        :param _Limit: 每页容量，默认20，最大200
        :type Limit: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._UserName = None
        self._RealName = None
        self._InstanceId = None
        self._DeviceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cmd = None
        self._Encoding = None
        self._AuditAction = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        r"""搜索区间的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""搜索区间的结束时间，不填默认为开始时间到现在为止
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        r"""资产实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        r"""资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        r"""资产的公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""资产的内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cmd(self):
        r"""执行的命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Encoding(self):
        r"""Cmd字段是前端传值是否进行base64.
0:否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def AuditAction(self):
        r"""根据拦截状态进行过滤：1 - 已执行，2 - 被阻断
        :rtype: list of int non-negative
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def Limit(self):
        r"""每页容量，默认20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._InstanceId = params.get("InstanceId")
        self._DeviceName = params.get("DeviceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cmd = params.get("Cmd")
        self._Encoding = params.get("Encoding")
        self._AuditAction = params.get("AuditAction")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchCommandResponse(AbstractModel):
    r"""SearchCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Commands: 命令列表
        :type Commands: list of SearchCommandResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Commands = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Commands(self):
        r"""命令列表
        :rtype: list of SearchCommandResult
        """
        return self._Commands

    @Commands.setter
    def Commands(self, Commands):
        self._Commands = Commands

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Commands") is not None:
            self._Commands = []
            for item in params.get("Commands"):
                obj = SearchCommandResult()
                obj._deserialize(item)
                self._Commands.append(obj)
        self._RequestId = params.get("RequestId")


class SearchCommandResult(AbstractModel):
    r"""命令执行检索结果

    """

    def __init__(self):
        r"""
        :param _Time: 命令输入的时间
        :type Time: str
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _InstanceId: 资产ID
        :type InstanceId: str
        :param _DeviceName: 资产名称
        :type DeviceName: str
        :param _PublicIp: 资产公网IP
        :type PublicIp: str
        :param _PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param _Cmd: 命令
        :type Cmd: str
        :param _Action: 命令执行情况，1--允许，2--拒绝
        :type Action: int
        :param _Sid: 命令所属的会话ID
        :type Sid: str
        :param _TimeOffset: 命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :type TimeOffset: int
        :param _Account: 账号
        :type Account: str
        :param _FromIp: source ip
        :type FromIp: str
        :param _SessionTime: 该命令所属会话的会话开始时间
        :type SessionTime: str
        :param _SessTime: 该命令所属会话的会话开始时间（使用SessionTime）
        :type SessTime: str
        :param _ConfirmTime: 复核时间
        :type ConfirmTime: str
        :param _UserDepartmentId: 部门id
        :type UserDepartmentId: str
        :param _UserDepartmentName: 用户部门名称
        :type UserDepartmentName: str
        :param _DeviceDepartmentId: 设备部门id
        :type DeviceDepartmentId: str
        :param _DeviceDepartmentName: 设备部门名称
        :type DeviceDepartmentName: str
        :param _Size: 会话大小
        :type Size: int
        :param _SignValue: 签名值
        :type SignValue: str
        :param _DeviceKind: 资产类型
        :type DeviceKind: str
        """
        self._Time = None
        self._UserName = None
        self._RealName = None
        self._InstanceId = None
        self._DeviceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cmd = None
        self._Action = None
        self._Sid = None
        self._TimeOffset = None
        self._Account = None
        self._FromIp = None
        self._SessionTime = None
        self._SessTime = None
        self._ConfirmTime = None
        self._UserDepartmentId = None
        self._UserDepartmentName = None
        self._DeviceDepartmentId = None
        self._DeviceDepartmentName = None
        self._Size = None
        self._SignValue = None
        self._DeviceKind = None

    @property
    def Time(self):
        r"""命令输入的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        r"""资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        r"""资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        r"""资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cmd(self):
        r"""命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Action(self):
        r"""命令执行情况，1--允许，2--拒绝
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Sid(self):
        r"""命令所属的会话ID
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def TimeOffset(self):
        r"""命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :rtype: int
        """
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset

    @property
    def Account(self):
        r"""账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        r"""source ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def SessionTime(self):
        r"""该命令所属会话的会话开始时间
        :rtype: str
        """
        return self._SessionTime

    @SessionTime.setter
    def SessionTime(self, SessionTime):
        self._SessionTime = SessionTime

    @property
    def SessTime(self):
        r"""该命令所属会话的会话开始时间（使用SessionTime）
        :rtype: str
        """
        return self._SessTime

    @SessTime.setter
    def SessTime(self, SessTime):
        self._SessTime = SessTime

    @property
    def ConfirmTime(self):
        r"""复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        r"""部门id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        r"""用户部门名称
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        r"""设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        r"""设备部门名称
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def Size(self):
        r"""会话大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SignValue(self):
        r"""签名值
        :rtype: str
        """
        return self._SignValue

    @SignValue.setter
    def SignValue(self, SignValue):
        self._SignValue = SignValue

    @property
    def DeviceKind(self):
        r"""资产类型
        :rtype: str
        """
        return self._DeviceKind

    @DeviceKind.setter
    def DeviceKind(self, DeviceKind):
        self._DeviceKind = DeviceKind


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._InstanceId = params.get("InstanceId")
        self._DeviceName = params.get("DeviceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cmd = params.get("Cmd")
        self._Action = params.get("Action")
        self._Sid = params.get("Sid")
        self._TimeOffset = params.get("TimeOffset")
        self._Account = params.get("Account")
        self._FromIp = params.get("FromIp")
        self._SessionTime = params.get("SessionTime")
        self._SessTime = params.get("SessTime")
        self._ConfirmTime = params.get("ConfirmTime")
        self._UserDepartmentId = params.get("UserDepartmentId")
        self._UserDepartmentName = params.get("UserDepartmentName")
        self._DeviceDepartmentId = params.get("DeviceDepartmentId")
        self._DeviceDepartmentName = params.get("DeviceDepartmentName")
        self._Size = params.get("Size")
        self._SignValue = params.get("SignValue")
        self._DeviceKind = params.get("DeviceKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileBySidRequest(AbstractModel):
    r"""SearchFileBySid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sid: 若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :type Sid: str
        :param _AuditLog: 是否创建审计日志,通过查看按钮调用时为true,其他为false
        :type AuditLog: bool
        :param _Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param _FileName: 可填写路径名或文件名
        :type FileName: str
        :param _Offset: 分页用偏移量
        :type Offset: int
        :param _AuditAction: 1-已执行，  2-被阻断
        :type AuditAction: int
        :param _AuditActionSet: 1-已执行，  2-被阻断
        :type AuditActionSet: list of int
        :param _TypeFilters: 以Protocol和Method为条件查询
        :type TypeFilters: list of SearchFileTypeFilter
        """
        self._Sid = None
        self._AuditLog = None
        self._Limit = None
        self._FileName = None
        self._Offset = None
        self._AuditAction = None
        self._AuditActionSet = None
        self._TypeFilters = None

    @property
    def Sid(self):
        r"""若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def AuditLog(self):
        r"""是否创建审计日志,通过查看按钮调用时为true,其他为false
        :rtype: bool
        """
        return self._AuditLog

    @AuditLog.setter
    def AuditLog(self, AuditLog):
        self._AuditLog = AuditLog

    @property
    def Limit(self):
        r"""分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FileName(self):
        r"""可填写路径名或文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Offset(self):
        r"""分页用偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AuditAction(self):
        r"""1-已执行，  2-被阻断
        :rtype: int
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def AuditActionSet(self):
        r"""1-已执行，  2-被阻断
        :rtype: list of int
        """
        return self._AuditActionSet

    @AuditActionSet.setter
    def AuditActionSet(self, AuditActionSet):
        self._AuditActionSet = AuditActionSet

    @property
    def TypeFilters(self):
        r"""以Protocol和Method为条件查询
        :rtype: list of SearchFileTypeFilter
        """
        return self._TypeFilters

    @TypeFilters.setter
    def TypeFilters(self, TypeFilters):
        self._TypeFilters = TypeFilters


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._AuditLog = params.get("AuditLog")
        self._Limit = params.get("Limit")
        self._FileName = params.get("FileName")
        self._Offset = params.get("Offset")
        self._AuditAction = params.get("AuditAction")
        self._AuditActionSet = params.get("AuditActionSet")
        if params.get("TypeFilters") is not None:
            self._TypeFilters = []
            for item in params.get("TypeFilters"):
                obj = SearchFileTypeFilter()
                obj._deserialize(item)
                self._TypeFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileBySidResponse(AbstractModel):
    r"""SearchFileBySid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数
        :type TotalCount: int
        :param _SearchFileBySidResult: 某会话的文件操作列表
        :type SearchFileBySidResult: list of SearchFileBySidResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SearchFileBySidResult = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SearchFileBySidResult(self):
        r"""某会话的文件操作列表
        :rtype: list of SearchFileBySidResult
        """
        return self._SearchFileBySidResult

    @SearchFileBySidResult.setter
    def SearchFileBySidResult(self, SearchFileBySidResult):
        self._SearchFileBySidResult = SearchFileBySidResult

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SearchFileBySidResult") is not None:
            self._SearchFileBySidResult = []
            for item in params.get("SearchFileBySidResult"):
                obj = SearchFileBySidResult()
                obj._deserialize(item)
                self._SearchFileBySidResult.append(obj)
        self._RequestId = params.get("RequestId")


class SearchFileBySidResult(AbstractModel):
    r"""文件操作搜索结果

    """

    def __init__(self):
        r"""
        :param _Sid: 会话Id
        :type Sid: str
        :param _UserName: 用户名
        :type UserName: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Account: 资产账号
        :type Account: str
        :param _FromIp: 来源Ip
        :type FromIp: str
        :param _Time: 文件操作时间
        :type Time: str
        :param _Method: 1-上传文件 2-下载文件 3-删除文件 4-移动文件 5-重命名文件 6-新建文件夹 7-移动文件夹 8-重命名文件夹 9-删除文件夹
        :type Method: int
        :param _Protocol: 文件传输协议
        :type Protocol: str
        :param _FileCurr: method为上传、下载、删除时文件在服务器上的位置, 或重命名、移动文件前文件的位置
        :type FileCurr: str
        :param _FileNew: method为重命名、移动文件时代表移动后的新位置.其他情况为null
        :type FileNew: str
        :param _Size: method为上传文件、下载文件、删除文件时显示文件大小。其他情况为null
        :type Size: int
        :param _Action: 堡垒机拦截情况, 1-已执行，  2-被阻断
        :type Action: int
        :param _ConfirmTime: 复核时间，当Action是3时，需有复核时间
        :type ConfirmTime: str
        :param _UserDepartmentId: 用户部门Id
        :type UserDepartmentId: str
        :param _UserDepartmentName: 用户部门name
        :type UserDepartmentName: str
        :param _DeviceDepartmentId: 设备部门id
        :type DeviceDepartmentId: str
        :param _DeviceDepartmentName: 设备部门name
        :type DeviceDepartmentName: str
        :param _SignValue: 签名值
        :type SignValue: str
        """
        self._Sid = None
        self._UserName = None
        self._InstanceId = None
        self._Account = None
        self._FromIp = None
        self._Time = None
        self._Method = None
        self._Protocol = None
        self._FileCurr = None
        self._FileNew = None
        self._Size = None
        self._Action = None
        self._ConfirmTime = None
        self._UserDepartmentId = None
        self._UserDepartmentName = None
        self._DeviceDepartmentId = None
        self._DeviceDepartmentName = None
        self._SignValue = None

    @property
    def Sid(self):
        r"""会话Id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

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
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Account(self):
        r"""资产账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        r"""来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Time(self):
        r"""文件操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Method(self):
        r"""1-上传文件 2-下载文件 3-删除文件 4-移动文件 5-重命名文件 6-新建文件夹 7-移动文件夹 8-重命名文件夹 9-删除文件夹
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Protocol(self):
        r"""文件传输协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FileCurr(self):
        r"""method为上传、下载、删除时文件在服务器上的位置, 或重命名、移动文件前文件的位置
        :rtype: str
        """
        return self._FileCurr

    @FileCurr.setter
    def FileCurr(self, FileCurr):
        self._FileCurr = FileCurr

    @property
    def FileNew(self):
        r"""method为重命名、移动文件时代表移动后的新位置.其他情况为null
        :rtype: str
        """
        return self._FileNew

    @FileNew.setter
    def FileNew(self, FileNew):
        self._FileNew = FileNew

    @property
    def Size(self):
        r"""method为上传文件、下载文件、删除文件时显示文件大小。其他情况为null
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Action(self):
        r"""堡垒机拦截情况, 1-已执行，  2-被阻断
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ConfirmTime(self):
        r"""复核时间，当Action是3时，需有复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        r"""用户部门Id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        r"""用户部门name
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        r"""设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        r"""设备部门name
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def SignValue(self):
        r"""签名值
        :rtype: str
        """
        return self._SignValue

    @SignValue.setter
    def SignValue(self, SignValue):
        self._SignValue = SignValue


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._UserName = params.get("UserName")
        self._InstanceId = params.get("InstanceId")
        self._Account = params.get("Account")
        self._FromIp = params.get("FromIp")
        self._Time = params.get("Time")
        self._Method = params.get("Method")
        self._Protocol = params.get("Protocol")
        self._FileCurr = params.get("FileCurr")
        self._FileNew = params.get("FileNew")
        self._Size = params.get("Size")
        self._Action = params.get("Action")
        self._ConfirmTime = params.get("ConfirmTime")
        self._UserDepartmentId = params.get("UserDepartmentId")
        self._UserDepartmentName = params.get("UserDepartmentName")
        self._DeviceDepartmentId = params.get("DeviceDepartmentId")
        self._DeviceDepartmentName = params.get("DeviceDepartmentName")
        self._SignValue = params.get("SignValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileRequest(AbstractModel):
    r"""SearchFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _InstanceId: 资产ID
        :type InstanceId: str
        :param _DeviceName: 资产名称
        :type DeviceName: str
        :param _PublicIp: 资产公网IP
        :type PublicIp: str
        :param _PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param _Method: 操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :type Method: list of int non-negative
        :param _FileName: 可填写路径名或文件（夹）名
        :type FileName: str
        :param _AuditAction: 1-已执行，  2-被阻断
        :type AuditAction: list of int non-negative
        :param _Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._UserName = None
        self._RealName = None
        self._InstanceId = None
        self._DeviceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Method = None
        self._FileName = None
        self._AuditAction = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        r"""查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        r"""资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        r"""资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        r"""资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Method(self):
        r"""操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :rtype: list of int non-negative
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def FileName(self):
        r"""可填写路径名或文件（夹）名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AuditAction(self):
        r"""1-已执行，  2-被阻断
        :rtype: list of int non-negative
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def Limit(self):
        r"""分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._InstanceId = params.get("InstanceId")
        self._DeviceName = params.get("DeviceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Method = params.get("Method")
        self._FileName = params.get("FileName")
        self._AuditAction = params.get("AuditAction")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileResponse(AbstractModel):
    r"""SearchFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数
        :type TotalCount: int
        :param _Files: 文件操作列表
        :type Files: list of SearchFileResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Files = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Files(self):
        r"""文件操作列表
        :rtype: list of SearchFileResult
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = SearchFileResult()
                obj._deserialize(item)
                self._Files.append(obj)
        self._RequestId = params.get("RequestId")


class SearchFileResult(AbstractModel):
    r"""文件传输检索结果

    """

    def __init__(self):
        r"""
        :param _Time: 文件传输的时间
        :type Time: str
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _InstanceId: 资产ID
        :type InstanceId: str
        :param _DeviceName: 资产名称
        :type DeviceName: str
        :param _PublicIp: 资产公网IP
        :type PublicIp: str
        :param _PrivateIp: 资产内网IP
        :type PrivateIp: str
        :param _Action: 操作结果：1 - 已执行，2 - 已阻断
        :type Action: int
        :param _Method: 操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :type Method: int
        :param _FileCurr: 下载的文件（夹）路径及名称
        :type FileCurr: str
        :param _FileNew: 上传或新建文件（夹）路径及名称
        :type FileNew: str
        :param _Sid: 会话id
        :type Sid: str
        :param _Account: 账号
        :type Account: str
        :param _FromIp: 来源id
        :type FromIp: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Size: 文件大小
        :type Size: int
        :param _ConfirmTime: 复核时间
        :type ConfirmTime: str
        :param _UserDepartmentId: 用户部门id
        :type UserDepartmentId: str
        :param _UserDepartmentName: 用户部门name
        :type UserDepartmentName: str
        :param _DeviceDepartmentId: 设备部门id
        :type DeviceDepartmentId: str
        :param _DeviceDepartmentName: 设备部门name	
        :type DeviceDepartmentName: str
        :param _SignValue: 签名值
        :type SignValue: str
        """
        self._Time = None
        self._UserName = None
        self._RealName = None
        self._InstanceId = None
        self._DeviceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Action = None
        self._Method = None
        self._FileCurr = None
        self._FileNew = None
        self._Sid = None
        self._Account = None
        self._FromIp = None
        self._Protocol = None
        self._Size = None
        self._ConfirmTime = None
        self._UserDepartmentId = None
        self._UserDepartmentName = None
        self._DeviceDepartmentId = None
        self._DeviceDepartmentName = None
        self._SignValue = None

    @property
    def Time(self):
        r"""文件传输的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        r"""资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        r"""资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        r"""资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Action(self):
        r"""操作结果：1 - 已执行，2 - 已阻断
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Method(self):
        r"""操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def FileCurr(self):
        r"""下载的文件（夹）路径及名称
        :rtype: str
        """
        return self._FileCurr

    @FileCurr.setter
    def FileCurr(self, FileCurr):
        self._FileCurr = FileCurr

    @property
    def FileNew(self):
        r"""上传或新建文件（夹）路径及名称
        :rtype: str
        """
        return self._FileNew

    @FileNew.setter
    def FileNew(self, FileNew):
        self._FileNew = FileNew

    @property
    def Sid(self):
        r"""会话id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Account(self):
        r"""账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        r"""来源id
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Protocol(self):
        r"""协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Size(self):
        r"""文件大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def ConfirmTime(self):
        r"""复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        r"""用户部门id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        r"""用户部门name
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        r"""设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        r"""设备部门name	
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def SignValue(self):
        r"""签名值
        :rtype: str
        """
        return self._SignValue

    @SignValue.setter
    def SignValue(self, SignValue):
        self._SignValue = SignValue


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._InstanceId = params.get("InstanceId")
        self._DeviceName = params.get("DeviceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Action = params.get("Action")
        self._Method = params.get("Method")
        self._FileCurr = params.get("FileCurr")
        self._FileNew = params.get("FileNew")
        self._Sid = params.get("Sid")
        self._Account = params.get("Account")
        self._FromIp = params.get("FromIp")
        self._Protocol = params.get("Protocol")
        self._Size = params.get("Size")
        self._ConfirmTime = params.get("ConfirmTime")
        self._UserDepartmentId = params.get("UserDepartmentId")
        self._UserDepartmentName = params.get("UserDepartmentName")
        self._DeviceDepartmentId = params.get("DeviceDepartmentId")
        self._DeviceDepartmentName = params.get("DeviceDepartmentName")
        self._SignValue = params.get("SignValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileTypeFilter(AbstractModel):
    r"""用于搜索文件传输记录等日志时按照protocol和method进行过滤

    """

    def __init__(self):
        r"""
        :param _Protocol: 需要查询的文件传输类型，如SFTP/CLIP/RDP/RZSZ
        :type Protocol: str
        :param _Method: 在当前指定的protocol下进一步过滤具体操作类型,如剪贴板文件上传，剪贴板文件下载等
        :type Method: list of int
        """
        self._Protocol = None
        self._Method = None

    @property
    def Protocol(self):
        r"""需要查询的文件传输类型，如SFTP/CLIP/RDP/RZSZ
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Method(self):
        r"""在当前指定的protocol下进一步过滤具体操作类型,如剪贴板文件上传，剪贴板文件下载等
        :rtype: list of int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionCommandRequest(AbstractModel):
    r"""SearchSessionCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cmd: 检索的目标命令，为模糊搜索
        :type Cmd: str
        :param _StartTime: 开始时间，不得早于当前时间的180天前
        :type StartTime: str
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 默认值为20，最大200
        :type Limit: int
        :param _Encoding: Cmd字段前端是否做base64加密
0：否，1：是
        :type Encoding: int
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._Cmd = None
        self._StartTime = None
        self._Offset = None
        self._Limit = None
        self._Encoding = None
        self._EndTime = None

    @property
    def Cmd(self):
        r"""检索的目标命令，为模糊搜索
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def StartTime(self):
        r"""开始时间，不得早于当前时间的180天前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        r"""分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""默认值为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Encoding(self):
        r"""Cmd字段前端是否做base64加密
0：否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._StartTime = params.get("StartTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Encoding = params.get("Encoding")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionCommandResponse(AbstractModel):
    r"""SearchSessionCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchSessionRequest(AbstractModel):
    r"""SearchSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateIp: 内部Ip
        :type PrivateIp: str
        :param _PublicIp: 外部Ip
        :type PublicIp: str
        :param _UserName: 用户名，长度不超过20
        :type UserName: str
        :param _Account: 账号，长度不超过64
        :type Account: str
        :param _FromIp: 来源Ip
        :type FromIp: str
        :param _StartTime: 搜索区间的开始时间。若入参是Id，则非必传，否则为必传。
        :type StartTime: str
        :param _EndTime: 搜索区间的结束时间
        :type EndTime: str
        :param _Kind: 会话协议类型，只能是1、2、3或4 对应关系为1-tui 2-gui 3-file 4-数据库。若入参是Id，则非必传，否则为必传。
        :type Kind: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param _RealName: 姓名，长度不超过20
        :type RealName: str
        :param _DeviceName: 主机名，长度不超过64
        :type DeviceName: str
        :param _Status: 状态，1为活跃，2为结束，3为强制离线，4为其他错误
        :type Status: int
        :param _StatusSet: 状态，1为活跃，2为结束，3为强制离线
        :type StatusSet: list of int non-negative
        :param _Id: 若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :type Id: str
        :param _AppAssetKindSet: 应用资产类型, 1-web
        :type AppAssetKindSet: list of int non-negative
        :param _AppAssetUrl: 应用资产Url
        :type AppAssetUrl: str
        :param _DeviceKind: 资产类型
        :type DeviceKind: str
        :param _DeviceKindSet: 资产类型 Linux, EKS,TKE
        :type DeviceKindSet: list of str
        """
        self._PrivateIp = None
        self._PublicIp = None
        self._UserName = None
        self._Account = None
        self._FromIp = None
        self._StartTime = None
        self._EndTime = None
        self._Kind = None
        self._Offset = None
        self._Limit = None
        self._RealName = None
        self._DeviceName = None
        self._Status = None
        self._StatusSet = None
        self._Id = None
        self._AppAssetKindSet = None
        self._AppAssetUrl = None
        self._DeviceKind = None
        self._DeviceKindSet = None

    @property
    def PrivateIp(self):
        r"""内部Ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""外部Ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def UserName(self):
        r"""用户名，长度不超过20
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Account(self):
        r"""账号，长度不超过64
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        r"""来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def StartTime(self):
        r"""搜索区间的开始时间。若入参是Id，则非必传，否则为必传。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""搜索区间的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Kind(self):
        r"""会话协议类型，只能是1、2、3或4 对应关系为1-tui 2-gui 3-file 4-数据库。若入参是Id，则非必传，否则为必传。
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RealName(self):
        r"""姓名，长度不超过20
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def DeviceName(self):
        r"""主机名，长度不超过64
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        r"""状态，1为活跃，2为结束，3为强制离线，4为其他错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusSet(self):
        r"""状态，1为活跃，2为结束，3为强制离线
        :rtype: list of int non-negative
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def Id(self):
        r"""若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppAssetKindSet(self):
        r"""应用资产类型, 1-web
        :rtype: list of int non-negative
        """
        return self._AppAssetKindSet

    @AppAssetKindSet.setter
    def AppAssetKindSet(self, AppAssetKindSet):
        self._AppAssetKindSet = AppAssetKindSet

    @property
    def AppAssetUrl(self):
        r"""应用资产Url
        :rtype: str
        """
        return self._AppAssetUrl

    @AppAssetUrl.setter
    def AppAssetUrl(self, AppAssetUrl):
        self._AppAssetUrl = AppAssetUrl

    @property
    def DeviceKind(self):
        r"""资产类型
        :rtype: str
        """
        return self._DeviceKind

    @DeviceKind.setter
    def DeviceKind(self, DeviceKind):
        self._DeviceKind = DeviceKind

    @property
    def DeviceKindSet(self):
        r"""资产类型 Linux, EKS,TKE
        :rtype: list of str
        """
        return self._DeviceKindSet

    @DeviceKindSet.setter
    def DeviceKindSet(self, DeviceKindSet):
        self._DeviceKindSet = DeviceKindSet


    def _deserialize(self, params):
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._UserName = params.get("UserName")
        self._Account = params.get("Account")
        self._FromIp = params.get("FromIp")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Kind = params.get("Kind")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RealName = params.get("RealName")
        self._DeviceName = params.get("DeviceName")
        self._Status = params.get("Status")
        self._StatusSet = params.get("StatusSet")
        self._Id = params.get("Id")
        self._AppAssetKindSet = params.get("AppAssetKindSet")
        self._AppAssetUrl = params.get("AppAssetUrl")
        self._DeviceKind = params.get("DeviceKind")
        self._DeviceKindSet = params.get("DeviceKindSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionResponse(AbstractModel):
    r"""SearchSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数
        :type TotalCount: int
        :param _SessionSet: 会话信息列表
        :type SessionSet: list of SessionResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SessionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SessionSet(self):
        r"""会话信息列表
        :rtype: list of SessionResult
        """
        return self._SessionSet

    @SessionSet.setter
    def SessionSet(self, SessionSet):
        self._SessionSet = SessionSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SessionSet") is not None:
            self._SessionSet = []
            for item in params.get("SessionSet"):
                obj = SessionResult()
                obj._deserialize(item)
                self._SessionSet.append(obj)
        self._RequestId = params.get("RequestId")


class SearchSubtaskResultByIdRequest(AbstractModel):
    r"""SearchSubtaskResultById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 运维任务名称
        :type Name: str
        :param _Offset: 查询偏移
        :type Offset: int
        :param _Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        :param _Id: 运维父任务执行日志ID
        :type Id: str
        :param _Status: 运维父任务执行状态
        :type Status: list of int non-negative
        """
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._Id = None
        self._Status = None

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""查询偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Id(self):
        r"""运维父任务执行日志ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        r"""运维父任务执行状态
        :rtype: list of int non-negative
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSubtaskResultByIdResponse(AbstractModel):
    r"""SearchSubtaskResultById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchTaskResultRequest(AbstractModel):
    r"""SearchTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 搜索区间的开始时间
        :type StartTime: str
        :param _EndTime: 搜索区间的结束时间
        :type EndTime: str
        :param _OperationId: 运维任务ID
        :type OperationId: str
        :param _Name: 运维任务名称
        :type Name: str
        :param _UserName: 用户名，长度不超过20
        :type UserName: str
        :param _RealName: 姓名，长度不超过20
        :type RealName: str
        :param _TaskType: 任务类型
1 手工运维任务
2 定时任务
3 账号推送任务
        :type TaskType: list of int non-negative
        :param _Offset: 查询偏移
        :type Offset: int
        :param _Limit: 分页的页内记录数，默认为20，最大200
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._OperationId = None
        self._Name = None
        self._UserName = None
        self._RealName = None
        self._TaskType = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        r"""搜索区间的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""搜索区间的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OperationId(self):
        r"""运维任务ID
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserName(self):
        r"""用户名，长度不超过20
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""姓名，长度不超过20
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def TaskType(self):
        r"""任务类型
1 手工运维任务
2 定时任务
3 账号推送任务
        :rtype: list of int non-negative
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Offset(self):
        r"""查询偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._OperationId = params.get("OperationId")
        self._Name = params.get("Name")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._TaskType = params.get("TaskType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTaskResultResponse(AbstractModel):
    r"""SearchTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数
        :type TotalCount: int
        :param _TaskResult: 运维任务执行结果
        :type TaskResult: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskResult = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskResult(self):
        r"""运维任务执行结果
        :rtype: list of TaskResult
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

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
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskResult") is not None:
            self._TaskResult = []
            for item in params.get("TaskResult"):
                obj = TaskResult()
                obj._deserialize(item)
                self._TaskResult.append(obj)
        self._RequestId = params.get("RequestId")


class SecuritySetting(AbstractModel):
    r"""系统安全设置

    """

    def __init__(self):
        r"""
        :param _AuthModeGM: 国密认证方式设置
        :type AuthModeGM: :class:`tencentcloud.bh.v20230418.models.AuthModeSetting`
        :param _Reconnection: 资产重连次数
        :type Reconnection: :class:`tencentcloud.bh.v20230418.models.ReconnectionSetting`
        :param _EnvInternetAccess: 大区环境网络设置
        :type EnvInternetAccess: :class:`tencentcloud.bh.v20230418.models.EnvInternetAccessSetting`
        """
        self._AuthModeGM = None
        self._Reconnection = None
        self._EnvInternetAccess = None

    @property
    def AuthModeGM(self):
        r"""国密认证方式设置
        :rtype: :class:`tencentcloud.bh.v20230418.models.AuthModeSetting`
        """
        return self._AuthModeGM

    @AuthModeGM.setter
    def AuthModeGM(self, AuthModeGM):
        self._AuthModeGM = AuthModeGM

    @property
    def Reconnection(self):
        r"""资产重连次数
        :rtype: :class:`tencentcloud.bh.v20230418.models.ReconnectionSetting`
        """
        return self._Reconnection

    @Reconnection.setter
    def Reconnection(self, Reconnection):
        self._Reconnection = Reconnection

    @property
    def EnvInternetAccess(self):
        r"""大区环境网络设置
        :rtype: :class:`tencentcloud.bh.v20230418.models.EnvInternetAccessSetting`
        """
        return self._EnvInternetAccess

    @EnvInternetAccess.setter
    def EnvInternetAccess(self, EnvInternetAccess):
        self._EnvInternetAccess = EnvInternetAccess


    def _deserialize(self, params):
        if params.get("AuthModeGM") is not None:
            self._AuthModeGM = AuthModeSetting()
            self._AuthModeGM._deserialize(params.get("AuthModeGM"))
        if params.get("Reconnection") is not None:
            self._Reconnection = ReconnectionSetting()
            self._Reconnection._deserialize(params.get("Reconnection"))
        if params.get("EnvInternetAccess") is not None:
            self._EnvInternetAccess = EnvInternetAccessSetting()
            self._EnvInternetAccess._deserialize(params.get("EnvInternetAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionResult(AbstractModel):
    r"""搜索字符或图形会话时返回的SessionResul结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _RealName: 姓名
        :type RealName: str
        :param _Account: 主机账号
        :type Account: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Size: 会话大小
        :type Size: int
        :param _InstanceId: 设备ID
        :type InstanceId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _PrivateIp: 内部Ip
        :type PrivateIp: str
        :param _PublicIp: 外部Ip
        :type PublicIp: str
        :param _FromIp: 来源Ip
        :type FromIp: str
        :param _Duration: 会话持续时长
        :type Duration: float
        :param _Count: 该会话内命令数量 ，搜索图形会话时该字段无意义
        :type Count: int
        :param _DangerCount: 该会话内高危命令数，搜索图形时该字段无意义
        :type DangerCount: int
        :param _Status: 会话状态，如1会话活跃  2会话结束  3强制离线  4其他错误
        :type Status: int
        :param _Id: 会话Id
        :type Id: str
        :param _ApCode: 设备所属的地域
        :type ApCode: str
        :param _Protocol: 会话协议
        :type Protocol: str
        :param _AppAssetKind: 应用资产类型：1-web
        :type AppAssetKind: int
        :param _AppAssetUrl: 应用资产url
        :type AppAssetUrl: str
        :param _ReplayType: 回放类型 默认0, 1-rfb 2-mp4 3-ssh
        :type ReplayType: int
        :param _DeviceKind: 会话资产类型
        :type DeviceKind: str
        :param _Namespace: K8S集群命名空间
        :type Namespace: str
        :param _Workload: K8S集群工作负载
        :type Workload: str
        :param _PodName: K8S集群容器名称
        :type PodName: str
        """
        self._UserName = None
        self._RealName = None
        self._Account = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._InstanceId = None
        self._DeviceName = None
        self._PrivateIp = None
        self._PublicIp = None
        self._FromIp = None
        self._Duration = None
        self._Count = None
        self._DangerCount = None
        self._Status = None
        self._Id = None
        self._ApCode = None
        self._Protocol = None
        self._AppAssetKind = None
        self._AppAssetUrl = None
        self._ReplayType = None
        self._DeviceKind = None
        self._Namespace = None
        self._Workload = None
        self._PodName = None

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
    def RealName(self):
        r"""姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Account(self):
        r"""主机账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""会话大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def InstanceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        r"""设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PrivateIp(self):
        r"""内部Ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""外部Ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def FromIp(self):
        r"""来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Duration(self):
        r"""会话持续时长
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Count(self):
        r"""该会话内命令数量 ，搜索图形会话时该字段无意义
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DangerCount(self):
        r"""该会话内高危命令数，搜索图形时该字段无意义
        :rtype: int
        """
        return self._DangerCount

    @DangerCount.setter
    def DangerCount(self, DangerCount):
        self._DangerCount = DangerCount

    @property
    def Status(self):
        r"""会话状态，如1会话活跃  2会话结束  3强制离线  4其他错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""会话Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ApCode(self):
        r"""设备所属的地域
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def Protocol(self):
        r"""会话协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def AppAssetKind(self):
        r"""应用资产类型：1-web
        :rtype: int
        """
        return self._AppAssetKind

    @AppAssetKind.setter
    def AppAssetKind(self, AppAssetKind):
        self._AppAssetKind = AppAssetKind

    @property
    def AppAssetUrl(self):
        r"""应用资产url
        :rtype: str
        """
        return self._AppAssetUrl

    @AppAssetUrl.setter
    def AppAssetUrl(self, AppAssetUrl):
        self._AppAssetUrl = AppAssetUrl

    @property
    def ReplayType(self):
        r"""回放类型 默认0, 1-rfb 2-mp4 3-ssh
        :rtype: int
        """
        return self._ReplayType

    @ReplayType.setter
    def ReplayType(self, ReplayType):
        self._ReplayType = ReplayType

    @property
    def DeviceKind(self):
        r"""会话资产类型
        :rtype: str
        """
        return self._DeviceKind

    @DeviceKind.setter
    def DeviceKind(self, DeviceKind):
        self._DeviceKind = DeviceKind

    @property
    def Namespace(self):
        r"""K8S集群命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Workload(self):
        r"""K8S集群工作负载
        :rtype: str
        """
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def PodName(self):
        r"""K8S集群容器名称
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Account = params.get("Account")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._InstanceId = params.get("InstanceId")
        self._DeviceName = params.get("DeviceName")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._FromIp = params.get("FromIp")
        self._Duration = params.get("Duration")
        self._Count = params.get("Count")
        self._DangerCount = params.get("DangerCount")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._ApCode = params.get("ApCode")
        self._Protocol = params.get("Protocol")
        self._AppAssetKind = params.get("AppAssetKind")
        self._AppAssetUrl = params.get("AppAssetUrl")
        self._ReplayType = params.get("ReplayType")
        self._DeviceKind = params.get("DeviceKind")
        self._Namespace = params.get("Namespace")
        self._Workload = params.get("Workload")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLDAPSyncFlagRequest(AbstractModel):
    r"""SetLDAPSyncFlag请求参数结构体

    """


class SetLDAPSyncFlagResponse(AbstractModel):
    r"""SetLDAPSyncFlag返回参数结构体

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


class SourceType(AbstractModel):
    r"""ioa用户源信息

    """

    def __init__(self):
        r"""
        :param _Source: 账号组来源
        :type Source: int
        :param _Type: 账号组来源类型
        :type Type: str
        :param _Name: 账号组来源名称
        :type Name: str
        :param _Target: 区分ioa原来和iam-mini
        :type Target: str
        """
        self._Source = None
        self._Type = None
        self._Name = None
        self._Target = None

    @property
    def Source(self):
        r"""账号组来源
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Type(self):
        r"""账号组来源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""账号组来源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Target(self):
        r"""区分ioa原来和iam-mini
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDevicesToIOARequest(AbstractModel):
    r"""SyncDevicesToIOA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdSet: 资产ID集合。资产必须已绑定支持IOA功能的堡垒机实例。每次最多同步200个资产。
        :type DeviceIdSet: list of int non-negative
        """
        self._DeviceIdSet = None

    @property
    def DeviceIdSet(self):
        r"""资产ID集合。资产必须已绑定支持IOA功能的堡垒机实例。每次最多同步200个资产。
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet


    def _deserialize(self, params):
        self._DeviceIdSet = params.get("DeviceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDevicesToIOAResponse(AbstractModel):
    r"""SyncDevicesToIOA返回参数结构体

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


class SyncUserToIOARequest(AbstractModel):
    r"""SyncUserToIOA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIdSet: 需要同步到ioa的本地用户的id集合
        :type UserIdSet: list of int non-negative
        """
        self._UserIdSet = None

    @property
    def UserIdSet(self):
        r"""需要同步到ioa的本地用户的id集合
        :rtype: list of int non-negative
        """
        return self._UserIdSet

    @UserIdSet.setter
    def UserIdSet(self, UserIdSet):
        self._UserIdSet = UserIdSet


    def _deserialize(self, params):
        self._UserIdSet = params.get("UserIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncUserToIOAResponse(AbstractModel):
    r"""SyncUserToIOA返回参数结构体

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


class TagFilter(AbstractModel):
    r"""资产标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: list of str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    r"""运维父任务执行结果

    """

    def __init__(self):
        r"""
        :param _Id: 运维任务结果日志ID
        :type Id: str
        :param _OperationId: 运维任务ID
        :type OperationId: str
        :param _Name: 运维任务名称
        :type Name: str
        :param _FromIp: 执行任务来源IP
        :type FromIp: str
        :param _UserName: 运维任务所属用户
        :type UserName: str
        :param _RealName: 运维任务所属用户的姓名
        :type RealName: str
        :param _Status: 运维任务执行状态 1 - 执行中，2 - 成功，3 - 失败，4 - 部分失败
        :type Status: int
        :param _StartTime: 运维任务开始时间
        :type StartTime: str
        :param _EndTime: 运维任务结束时间
        :type EndTime: str
        """
        self._Id = None
        self._OperationId = None
        self._Name = None
        self._FromIp = None
        self._UserName = None
        self._RealName = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Id(self):
        r"""运维任务结果日志ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationId(self):
        r"""运维任务ID
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Name(self):
        r"""运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FromIp(self):
        r"""执行任务来源IP
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def UserName(self):
        r"""运维任务所属用户
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""运维任务所属用户的姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Status(self):
        r"""运维任务执行状态 1 - 执行中，2 - 成功，3 - 失败，4 - 部分失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""运维任务开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""运维任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OperationId = params.get("OperationId")
        self._Name = params.get("Name")
        self._FromIp = params.get("FromIp")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockUserRequest(AbstractModel):
    r"""UnlockUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 用户id
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        r"""用户id
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnlockUserResponse(AbstractModel):
    r"""UnlockUser返回参数结构体

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
        :param _UserName: 用户名,1 - 128个字符 必须以英文字母开头，只能由a-zA-Z0-9以及+=,.@_-组成，支持邮箱格式

        :type UserName: str
        :param _RealName: 用户姓名， 最大20个字符，不能包含空白字符
        :type RealName: str
        :param _Id: 用户ID
        :type Id: int
        :param _Phone: 手机号码， 大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :type Phone: str
        :param _Email: 电子邮件
        :type Email: str
        :param _ValidateFrom: 用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateFrom: str
        :param _ValidateTo: 用户失效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :type ValidateTo: str
        :param _GroupSet: 所属用户组列表
        :type GroupSet: list of Group
        :param _AuthType: 认证方式，0 - 本地，1 - LDAP，2 - OAuth
        :type AuthType: int
        :param _ValidateTime: 访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :type ValidateTime: str
        :param _Department: 用户所属部门（用于出参）
        :type Department: :class:`tencentcloud.bh.v20230418.models.Department`
        :param _DepartmentId: 用户所属部门（用于入参）
        :type DepartmentId: str
        :param _ActiveStatus: 激活状态 0 - 未激活 1 - 激活
        :type ActiveStatus: int
        :param _LockStatus: 锁定状态 0 - 未锁定 1 - 锁定
        :type LockStatus: int
        :param _UKeyStatus: ukey绑定状态 0 - 未绑定 1 - 已绑定
        :type UKeyStatus: int
        :param _Status: 状态 与Filter中一致
        :type Status: str
        :param _AclVersion: 权限版本
        :type AclVersion: int
        :param _UserFrom: 用户来源，0-bh,1-ioa
        :type UserFrom: int
        :param _IOAUserGroup: ioa同步过来的用户相关信息
        :type IOAUserGroup: :class:`tencentcloud.bh.v20230418.models.IOAUserGroup`
        :param _RoleArn: cam角色用户载体
        :type RoleArn: str
        """
        self._UserName = None
        self._RealName = None
        self._Id = None
        self._Phone = None
        self._Email = None
        self._ValidateFrom = None
        self._ValidateTo = None
        self._GroupSet = None
        self._AuthType = None
        self._ValidateTime = None
        self._Department = None
        self._DepartmentId = None
        self._ActiveStatus = None
        self._LockStatus = None
        self._UKeyStatus = None
        self._Status = None
        self._AclVersion = None
        self._UserFrom = None
        self._IOAUserGroup = None
        self._RoleArn = None

    @property
    def UserName(self):
        r"""用户名,1 - 128个字符 必须以英文字母开头，只能由a-zA-Z0-9以及+=,.@_-组成，支持邮箱格式

        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        r"""用户姓名， 最大20个字符，不能包含空白字符
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Id(self):
        r"""用户ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Phone(self):
        r"""手机号码， 大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""电子邮件
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        r"""用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        r"""用户失效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupSet(self):
        r"""所属用户组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def AuthType(self):
        r"""认证方式，0 - 本地，1 - LDAP，2 - OAuth
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        r"""访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def Department(self):
        r"""用户所属部门（用于出参）
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def DepartmentId(self):
        r"""用户所属部门（用于入参）
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def ActiveStatus(self):
        r"""激活状态 0 - 未激活 1 - 激活
        :rtype: int
        """
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def LockStatus(self):
        r"""锁定状态 0 - 未锁定 1 - 锁定
        :rtype: int
        """
        return self._LockStatus

    @LockStatus.setter
    def LockStatus(self, LockStatus):
        self._LockStatus = LockStatus

    @property
    def UKeyStatus(self):
        r"""ukey绑定状态 0 - 未绑定 1 - 已绑定
        :rtype: int
        """
        return self._UKeyStatus

    @UKeyStatus.setter
    def UKeyStatus(self, UKeyStatus):
        self._UKeyStatus = UKeyStatus

    @property
    def Status(self):
        r"""状态 与Filter中一致
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AclVersion(self):
        r"""权限版本
        :rtype: int
        """
        return self._AclVersion

    @AclVersion.setter
    def AclVersion(self, AclVersion):
        self._AclVersion = AclVersion

    @property
    def UserFrom(self):
        r"""用户来源，0-bh,1-ioa
        :rtype: int
        """
        return self._UserFrom

    @UserFrom.setter
    def UserFrom(self, UserFrom):
        self._UserFrom = UserFrom

    @property
    def IOAUserGroup(self):
        r"""ioa同步过来的用户相关信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.IOAUserGroup`
        """
        return self._IOAUserGroup

    @IOAUserGroup.setter
    def IOAUserGroup(self, IOAUserGroup):
        self._IOAUserGroup = IOAUserGroup

    @property
    def RoleArn(self):
        r"""cam角色用户载体
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._Id = params.get("Id")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._ValidateFrom = params.get("ValidateFrom")
        self._ValidateTo = params.get("ValidateTo")
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._AuthType = params.get("AuthType")
        self._ValidateTime = params.get("ValidateTime")
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._DepartmentId = params.get("DepartmentId")
        self._ActiveStatus = params.get("ActiveStatus")
        self._LockStatus = params.get("LockStatus")
        self._UKeyStatus = params.get("UKeyStatus")
        self._Status = params.get("Status")
        self._AclVersion = params.get("AclVersion")
        self._UserFrom = params.get("UserFrom")
        if params.get("IOAUserGroup") is not None:
            self._IOAUserGroup = IOAUserGroup()
            self._IOAUserGroup._deserialize(params.get("IOAUserGroup"))
        self._RoleArn = params.get("RoleArn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDirectory(AbstractModel):
    r"""用户目录信息

    """

    def __init__(self):
        r"""
        :param _Id: 目录id
        :type Id: int
        :param _DirId: ioa目录id
        :type DirId: int
        :param _DirName: ioa目录名称
        :type DirName: str
        :param _Source: ioa关联用户源类型
        :type Source: int
        :param _SourceName: ioa关联用户源名称
        :type SourceName: str
        :param _UserTotal: 目录包含用户数
        :type UserTotal: int
        :param _CreateTime: 目录接入时间
        :type CreateTime: str
        :param _UserOrgSet: 目录下的组织细节信息
        :type UserOrgSet: list of UserOrg
        """
        self._Id = None
        self._DirId = None
        self._DirName = None
        self._Source = None
        self._SourceName = None
        self._UserTotal = None
        self._CreateTime = None
        self._UserOrgSet = None

    @property
    def Id(self):
        r"""目录id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DirId(self):
        r"""ioa目录id
        :rtype: int
        """
        return self._DirId

    @DirId.setter
    def DirId(self, DirId):
        self._DirId = DirId

    @property
    def DirName(self):
        r"""ioa目录名称
        :rtype: str
        """
        return self._DirName

    @DirName.setter
    def DirName(self, DirName):
        self._DirName = DirName

    @property
    def Source(self):
        r"""ioa关联用户源类型
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceName(self):
        r"""ioa关联用户源名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def UserTotal(self):
        r"""目录包含用户数
        :rtype: int
        """
        return self._UserTotal

    @UserTotal.setter
    def UserTotal(self, UserTotal):
        self._UserTotal = UserTotal

    @property
    def CreateTime(self):
        r"""目录接入时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserOrgSet(self):
        r"""目录下的组织细节信息
        :rtype: list of UserOrg
        """
        return self._UserOrgSet

    @UserOrgSet.setter
    def UserOrgSet(self, UserOrgSet):
        self._UserOrgSet = UserOrgSet


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DirId = params.get("DirId")
        self._DirName = params.get("DirName")
        self._Source = params.get("Source")
        self._SourceName = params.get("SourceName")
        self._UserTotal = params.get("UserTotal")
        self._CreateTime = params.get("CreateTime")
        if params.get("UserOrgSet") is not None:
            self._UserOrgSet = []
            for item in params.get("UserOrgSet"):
                obj = UserOrg()
                obj._deserialize(item)
                self._UserOrgSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserOrg(AbstractModel):
    r"""同步的ioa用户组织信息

    """

    def __init__(self):
        r"""
        :param _OrgId: ioa用户组织id
        :type OrgId: int
        :param _OrgName: ioa用户组织名称
        :type OrgName: str
        :param _OrgIdPath: ioa用户组织id路径
        :type OrgIdPath: str
        :param _OrgNamePath: ioa用户组织名称路径
        :type OrgNamePath: str
        :param _UserTotal: ioa用户组织id下的用户数
        :type UserTotal: int
        """
        self._OrgId = None
        self._OrgName = None
        self._OrgIdPath = None
        self._OrgNamePath = None
        self._UserTotal = None

    @property
    def OrgId(self):
        r"""ioa用户组织id
        :rtype: int
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def OrgName(self):
        r"""ioa用户组织名称
        :rtype: str
        """
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName

    @property
    def OrgIdPath(self):
        r"""ioa用户组织id路径
        :rtype: str
        """
        return self._OrgIdPath

    @OrgIdPath.setter
    def OrgIdPath(self, OrgIdPath):
        self._OrgIdPath = OrgIdPath

    @property
    def OrgNamePath(self):
        r"""ioa用户组织名称路径
        :rtype: str
        """
        return self._OrgNamePath

    @OrgNamePath.setter
    def OrgNamePath(self, OrgNamePath):
        self._OrgNamePath = OrgNamePath

    @property
    def UserTotal(self):
        r"""ioa用户组织id下的用户数
        :rtype: int
        """
        return self._UserTotal

    @UserTotal.setter
    def UserTotal(self, UserTotal):
        self._UserTotal = UserTotal


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._OrgName = params.get("OrgName")
        self._OrgIdPath = params.get("OrgIdPath")
        self._OrgNamePath = params.get("OrgNamePath")
        self._UserTotal = params.get("UserTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        