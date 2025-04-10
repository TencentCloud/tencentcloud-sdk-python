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


class ACTemplate(AbstractModel):
    """权限控制模板对象

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
        """模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        """模板描述
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
    """AccessDevices请求参数结构体

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
        """资产的登录账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def LoginAccount(self):
        warnings.warn("parameter `LoginAccount` is deprecated", DeprecationWarning) 

        """运维端登录账号
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

        """运维端登录密码
        :rtype: str
        """
        return self._LoginPassword

    @LoginPassword.setter
    def LoginPassword(self, LoginPassword):
        warnings.warn("parameter `LoginPassword` is deprecated", DeprecationWarning) 

        self._LoginPassword = LoginPassword

    @property
    def DeviceId(self):
        """资产ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def InstanceId(self):
        """资源id(优先使用DeviceId)
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        """未托管密码私钥时，填入
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PrivateKey(self):
        """未托管密码私钥时，填入
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def PrivateKeyPassword(self):
        """未托管密码私钥时，填入
        :rtype: str
        """
        return self._PrivateKeyPassword

    @PrivateKeyPassword.setter
    def PrivateKeyPassword(self, PrivateKeyPassword):
        self._PrivateKeyPassword = PrivateKeyPassword

    @property
    def Exe(self):
        """客户端工具
        :rtype: str
        """
        return self._Exe

    @Exe.setter
    def Exe(self, Exe):
        self._Exe = Exe

    @property
    def Drivers(self):
        """RDP挂载盘符驱动（mstsc支持）
        :rtype: list of str
        """
        return self._Drivers

    @Drivers.setter
    def Drivers(self, Drivers):
        self._Drivers = Drivers

    @property
    def Width(self):
        """窗口宽度（RDP支持）
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """窗口高度（RDP支持）
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def IntranetAccess(self):
        """是否内网访问（默认不是）
        :rtype: bool
        """
        return self._IntranetAccess

    @IntranetAccess.setter
    def IntranetAccess(self, IntranetAccess):
        self._IntranetAccess = IntranetAccess

    @property
    def AutoManageAccessCredential(self):
        """是否自动管理访问串，删掉过期的，新建可用的（默认false）
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
    """AccessDevices返回参数结构体

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
        """认证信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.AccessInfo`
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

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
        if params.get("AccessInfo") is not None:
            self._AccessInfo = AccessInfo()
            self._AccessInfo._deserialize(params.get("AccessInfo"))
        self._RequestId = params.get("RequestId")


class AccessInfo(AbstractModel):
    """认证信息

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
        """地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AccessURL(self):
        """唤起链接｜wss链接
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
        


class Acl(AbstractModel):
    """访问权限

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

    @property
    def Id(self):
        """访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """访问权限名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        """是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowClipFileUp(self):
        """是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        """是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        """是否开启剪贴板文本（目前含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        """是否开启剪贴板文本（目前含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        """是否开启文件传输上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        """文件传输上传大小限制（预留参数，暂未启用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        """是否开启文件传输下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        """文件传输下载大小限制（预留参数，暂未启用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def AllowAnyAccount(self):
        """是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def UserSet(self):
        """关联的用户列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

    @property
    def UserGroupSet(self):
        """关联的用户组列表
        :rtype: list of Group
        """
        return self._UserGroupSet

    @UserGroupSet.setter
    def UserGroupSet(self, UserGroupSet):
        self._UserGroupSet = UserGroupSet

    @property
    def DeviceSet(self):
        """关联的资产列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def DeviceGroupSet(self):
        """关联的资产组列表
        :rtype: list of Group
        """
        return self._DeviceGroupSet

    @DeviceGroupSet.setter
    def DeviceGroupSet(self, DeviceGroupSet):
        self._DeviceGroupSet = DeviceGroupSet

    @property
    def AccountSet(self):
        """关联的账号列表
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateSet(self):
        """关联的高危命令模板列表
        :rtype: list of CmdTemplate
        """
        return self._CmdTemplateSet

    @CmdTemplateSet.setter
    def CmdTemplateSet(self, CmdTemplateSet):
        self._CmdTemplateSet = CmdTemplateSet

    @property
    def AllowDiskFileUp(self):
        """是否开启 RDP 磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        """是否开启 RDP 磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        """是否开启 rz sz 文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        """是否开启 rz sz 文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        """是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        """访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def Status(self):
        """访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Department(self):
        """所属部门的信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def AllowAccessCredential(self):
        """是否允许使用访问串，默认允许
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def ACTemplateSet(self):
        """关联的数据库高危命令列表
        :rtype: list of ACTemplate
        """
        return self._ACTemplateSet

    @ACTemplateSet.setter
    def ACTemplateSet(self, ACTemplateSet):
        self._ACTemplateSet = ACTemplateSet

    @property
    def WhiteCmds(self):
        """关联的白命令命令
        :rtype: list of str
        """
        return self._WhiteCmds

    @WhiteCmds.setter
    def WhiteCmds(self, WhiteCmds):
        self._WhiteCmds = WhiteCmds

    @property
    def AllowKeyboardLogger(self):
        """是否允许记录键盘
        :rtype: bool
        """
        return self._AllowKeyboardLogger

    @AllowKeyboardLogger.setter
    def AllowKeyboardLogger(self, AllowKeyboardLogger):
        self._AllowKeyboardLogger = AllowKeyboardLogger

    @property
    def AppAssetSet(self):
        """关联的应用资产列表
        :rtype: list of AppAsset
        """
        return self._AppAssetSet

    @AppAssetSet.setter
    def AppAssetSet(self, AppAssetSet):
        self._AppAssetSet = AppAssetSet


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceGroupMembersRequest(AbstractModel):
    """AddDeviceGroupMembers请求参数结构体

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
        """资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        """需要添加到资产组的资产ID集合
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
    """AddDeviceGroupMembers返回参数结构体

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


class AddUserGroupMembersRequest(AbstractModel):
    """AddUserGroupMembers请求参数结构体

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
        """用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        """成员用户ID集合
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
    """AddUserGroupMembers返回参数结构体

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


class AppAsset(AbstractModel):
    """应用资产信息

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
        """应用资产id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """资产名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceId(self):
        """应用服务器id
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceAccountId(self):
        """应用服务器账号id
        :rtype: int
        """
        return self._DeviceAccountId

    @DeviceAccountId.setter
    def DeviceAccountId(self, DeviceAccountId):
        self._DeviceAccountId = DeviceAccountId

    @property
    def Kind(self):
        """应用资产类型。1-web应用
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def ClientAppPath(self):
        """客户端工具路径
        :rtype: str
        """
        return self._ClientAppPath

    @ClientAppPath.setter
    def ClientAppPath(self, ClientAppPath):
        self._ClientAppPath = ClientAppPath

    @property
    def ClientAppKind(self):
        """客户端工具类型
        :rtype: str
        """
        return self._ClientAppKind

    @ClientAppKind.setter
    def ClientAppKind(self, ClientAppKind):
        self._ClientAppKind = ClientAppKind

    @property
    def Url(self):
        """应用资产url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BindStatus(self):
        """托管状态。0-未托管，1-已托管
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def DeviceInstanceId(self):
        """应用服务器实例id
        :rtype: str
        """
        return self._DeviceInstanceId

    @DeviceInstanceId.setter
    def DeviceInstanceId(self, DeviceInstanceId):
        self._DeviceInstanceId = DeviceInstanceId

    @property
    def DeviceName(self):
        """应用服务器名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceAccountName(self):
        """应用服务器账号名称
        :rtype: str
        """
        return self._DeviceAccountName

    @DeviceAccountName.setter
    def DeviceAccountName(self, DeviceAccountName):
        self._DeviceAccountName = DeviceAccountName

    @property
    def ResourceId(self):
        """堡垒机实例id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        """堡垒机实例信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DomainId(self):
        """网络域id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        """网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def GroupSet(self):
        """资产组信息
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def Department(self):
        """资产所属部门
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
        


class AssetSyncStatus(AbstractModel):
    """资产同步状态

    """

    def __init__(self):
        r"""
        :param _LastTime: 上一次同步完成的时间
        :type LastTime: str
        :param _LastStatus: 上一次同步的结果。 0 - 从未进行, 1 - 成功， 2 - 失败
        :type LastStatus: int
        :param _InProcess: 同步任务是否正在进行中
        :type InProcess: bool
        """
        self._LastTime = None
        self._LastStatus = None
        self._InProcess = None

    @property
    def LastTime(self):
        """上一次同步完成的时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def LastStatus(self):
        """上一次同步的结果。 0 - 从未进行, 1 - 成功， 2 - 失败
        :rtype: int
        """
        return self._LastStatus

    @LastStatus.setter
    def LastStatus(self, LastStatus):
        self._LastStatus = LastStatus

    @property
    def InProcess(self):
        """同步任务是否正在进行中
        :rtype: bool
        """
        return self._InProcess

    @InProcess.setter
    def InProcess(self, InProcess):
        self._InProcess = InProcess


    def _deserialize(self, params):
        self._LastTime = params.get("LastTime")
        self._LastStatus = params.get("LastStatus")
        self._InProcess = params.get("InProcess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceAccountPasswordRequest(AbstractModel):
    """BindDeviceAccountPassword请求参数结构体

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
        """主机账号ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Password(self):
        """主机账号密码
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
    """BindDeviceAccountPassword返回参数结构体

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


class BindDeviceAccountPrivateKeyRequest(AbstractModel):
    """BindDeviceAccountPrivateKey请求参数结构体

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
        """主机账号ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PrivateKey(self):
        """主机账号私钥，最小长度128字节，最大长度8192字节
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def PrivateKeyPassword(self):
        """主机账号私钥口令，最大长度256字节
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
    """BindDeviceAccountPrivateKey返回参数结构体

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


class BindDeviceResourceRequest(AbstractModel):
    """BindDeviceResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIdSet: 资产ID集合
        :type DeviceIdSet: list of int non-negative
        :param _ResourceId: 堡垒机服务ID
        :type ResourceId: str
        :param _DomainId: 网络域ID
        :type DomainId: str
        """
        self._DeviceIdSet = None
        self._ResourceId = None
        self._DomainId = None

    @property
    def DeviceIdSet(self):
        """资产ID集合
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def ResourceId(self):
        """堡垒机服务ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DomainId(self):
        """网络域ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._ResourceId = params.get("ResourceId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDeviceResourceResponse(AbstractModel):
    """BindDeviceResource返回参数结构体

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


class ChangePwdTaskDetail(AbstractModel):
    """查询改密计划详情

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
        """资产信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Account(self):
        """资产账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def LastChangeStatus(self):
        """上次改密结果。0-未改密  1-改密成功 2-改密失败
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
    """修改密码任务信息

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

    @property
    def Id(self):
        """id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationId(self):
        """任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def TaskName(self):
        """任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Department(self):
        """所属部门信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def ChangeMethod(self):
        """改密方式。1：使用执行账号。2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def RunAccount(self):
        """执行账号
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def AuthGenerationStrategy(self):
        """密码生成策略
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def PasswordLength(self):
        """密码长度
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        """包含小写字母
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        """包含大写字母
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        """包含数字
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        """包含的特殊字符，入参base64
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        """改密完成通知。0-通知，1-不通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        """通知人邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        """加密附件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def AccountSet(self):
        """需要改密的账户
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def DeviceSet(self):
        """需要改密的主机
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def Type(self):
        """任务类型：4手动，5自动
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        """周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        """首次执行时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def NextTime(self):
        """下次执行时间
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        self._NextTime = NextTime


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Clb(AbstractModel):
    """负载均衡

    """

    def __init__(self):
        r"""
        :param _ClbIp: 负载均衡IP	
        :type ClbIp: str
        """
        self._ClbIp = None

    @property
    def ClbIp(self):
        """负载均衡IP	
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
    """高危命令模板

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
        """高危命令模板ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """高危命令模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        """命令列表，命令之间用换行符（"\n"）分隔
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Type(self):
        """命令模板类型 1-内置 2-自定义
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
        


class CreateAclRequest(AbstractModel):
    """CreateAcl请求参数结构体

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
        """权限名称，最大32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        """是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowAnyAccount(self):
        """是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def AllowClipFileUp(self):
        """是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        """是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        """是否开启剪贴板文本（含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        """是否开启剪贴板文本（含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        """是否开启 SFTP 文件上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        """文件传输上传大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        """是否开启 SFTP 文件下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        """文件传输下载大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def UserIdSet(self):
        """关联的用户ID集合
        :rtype: list of int non-negative
        """
        return self._UserIdSet

    @UserIdSet.setter
    def UserIdSet(self, UserIdSet):
        self._UserIdSet = UserIdSet

    @property
    def UserGroupIdSet(self):
        """关联的用户组ID
        :rtype: list of int non-negative
        """
        return self._UserGroupIdSet

    @UserGroupIdSet.setter
    def UserGroupIdSet(self, UserGroupIdSet):
        self._UserGroupIdSet = UserGroupIdSet

    @property
    def DeviceIdSet(self):
        """关联的资产ID集合
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AppAssetIdSet(self):
        """关联的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AppAssetIdSet

    @AppAssetIdSet.setter
    def AppAssetIdSet(self, AppAssetIdSet):
        self._AppAssetIdSet = AppAssetIdSet

    @property
    def DeviceGroupIdSet(self):
        """关联的资产组ID
        :rtype: list of int non-negative
        """
        return self._DeviceGroupIdSet

    @DeviceGroupIdSet.setter
    def DeviceGroupIdSet(self, DeviceGroupIdSet):
        self._DeviceGroupIdSet = DeviceGroupIdSet

    @property
    def AccountSet(self):
        """关联的账号
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateIdSet(self):
        """关联的高危命令模板ID
        :rtype: list of int non-negative
        """
        return self._CmdTemplateIdSet

    @CmdTemplateIdSet.setter
    def CmdTemplateIdSet(self, CmdTemplateIdSet):
        self._CmdTemplateIdSet = CmdTemplateIdSet

    @property
    def ACTemplateIdSet(self):
        """关联高危DB模板ID
        :rtype: list of str
        """
        return self._ACTemplateIdSet

    @ACTemplateIdSet.setter
    def ACTemplateIdSet(self, ACTemplateIdSet):
        self._ACTemplateIdSet = ACTemplateIdSet

    @property
    def AllowDiskFileUp(self):
        """是否开启rdp磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        """是否开启rdp磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        """是否开启rz sz文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        """是否开启rz sz文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        """是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        """访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def DepartmentId(self):
        """访问权限所属部门的ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def AllowAccessCredential(self):
        """是否允许使用访问串，默认允许
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def AllowKeyboardLogger(self):
        """是否允许键盘记录
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
    """CreateAcl返回参数结构体

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
        """新建成功的访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateAssetSyncJobRequest(AbstractModel):
    """CreateAssetSyncJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Category: 同步资产类别，1 - 主机资产, 2 - 数据库资产
        :type Category: int
        """
        self._Category = None

    @property
    def Category(self):
        """同步资产类别，1 - 主机资产, 2 - 数据库资产
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
    """CreateAssetSyncJob返回参数结构体

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


class CreateChangePwdTaskRequest(AbstractModel):
    """CreateChangePwdTask请求参数结构体

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
        """任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DeviceIdSet(self):
        """资产id数组
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AccountSet(self):
        """修改的账户数组
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def ChangeMethod(self):
        """改密方式。1：使用执行账号修改密码；2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def AuthGenerationStrategy(self):
        """认证生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def RunAccount(self):
        """执行账号
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def Password(self):
        """手动指定密码时必传
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordLength(self):
        """密码限制长度，长度大于 12 位
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        """密码包含小写字母。0：否，1：是
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        """密码包含大写字母。0：否，1：是
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        """密码包含数字。0：否，1：是
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        """密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        """改密完成通知。0：不通知 
  1：通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        """通知邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        """加密压缩文件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def DepartmentId(self):
        """所属部门id。“1.2.3”
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Type(self):
        """任务类型  4-手工执行  5-周期自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        """执行周期，单位天（大于等于 1，小于等于 365）
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        """周期任务首次执行时间
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
    """CreateChangePwdTask返回参数结构体

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
        """任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

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
        self._OperationId = params.get("OperationId")
        self._RequestId = params.get("RequestId")


class CreateCmdTemplateRequest(AbstractModel):
    """CreateCmdTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模板名，最大长度32字符，不能包含空白字符
        :type Name: str
        :param _CmdList: 命令列表，\n分隔，最大长度32768字节
        :type CmdList: str
        :param _Encoding: 标识cmdlist字段前端是否为base64加密传值.
0:表示非base64加密
1:表示是base64加密
        :type Encoding: int
        """
        self._Name = None
        self._CmdList = None
        self._Encoding = None

    @property
    def Name(self):
        """模板名，最大长度32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        """命令列表，\n分隔，最大长度32768字节
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Encoding(self):
        """标识cmdlist字段前端是否为base64加密传值.
0:表示非base64加密
1:表示是base64加密
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
    """CreateCmdTemplate返回参数结构体

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
        """新建成功后返回的记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDeviceAccountRequest(AbstractModel):
    """CreateDeviceAccount请求参数结构体

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
        """主机记录ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Account(self):
        """账号名
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
    """CreateDeviceAccount返回参数结构体

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
        """新建成功后返回的记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDeviceGroupRequest(AbstractModel):
    """CreateDeviceGroup请求参数结构体

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
        """资产组名，最大长度32字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        """资产组所属部门ID，如：1.2.3
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
    """CreateDeviceGroup返回参数结构体

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
        """新建成功的资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateOperationTaskRequest(AbstractModel):
    """CreateOperationTask请求参数结构体

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
        """运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """运维任务类型,1 - 手工执行, 2 - 周期性自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Account(self):
        """执行账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Timeout(self):
        """超时时间,单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Script(self):
        """执行脚本内容
        :rtype: str
        """
        return self._Script

    @Script.setter
    def Script(self, Script):
        self._Script = Script

    @property
    def DeviceIdSet(self):
        """执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def Period(self):
        """执行间隔，单位天. 手工执行时无需传入
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        """首次执行日期 默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Encoding(self):
        """Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
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
    """CreateOperationTask返回参数结构体

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
        """运维任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource请求参数结构体

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

    @property
    def DeployRegion(self):
        """部署region
        :rtype: str
        """
        return self._DeployRegion

    @DeployRegion.setter
    def DeployRegion(self, DeployRegion):
        self._DeployRegion = DeployRegion

    @property
    def VpcId(self):
        """部署堡垒机的VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """部署堡垒机的SubnetId
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ResourceEdition(self):
        """资源类型。取值:standard/pro
        :rtype: str
        """
        return self._ResourceEdition

    @ResourceEdition.setter
    def ResourceEdition(self, ResourceEdition):
        self._ResourceEdition = ResourceEdition

    @property
    def ResourceNode(self):
        """资源节点数
        :rtype: int
        """
        return self._ResourceNode

    @ResourceNode.setter
    def ResourceNode(self, ResourceNode):
        self._ResourceNode = ResourceNode

    @property
    def TimeUnit(self):
        """计费周期
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """计费时长
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PayMode(self):
        """计费模式 1预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        """自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeployZone(self):
        """部署zone
        :rtype: str
        """
        return self._DeployZone

    @DeployZone.setter
    def DeployZone(self, DeployZone):
        self._DeployZone = DeployZone

    @property
    def Trial(self):
        """0非试用版，1试用版
        :rtype: int
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource返回参数结构体

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
        """实例Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

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
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


class CreateUserGroupRequest(AbstractModel):
    """CreateUserGroup请求参数结构体

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
        """用户组名，最大长度32字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        """用户组所属部门的ID，如：1.2.3
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
    """CreateUserGroup返回参数结构体

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
        """新建成功的用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

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
        """用户名, 3-20个字符, 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """用户姓名，最大长度20个字符，不能包含空白字符
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Phone(self):
        """按照"国家地区代码|手机号"的格式输入，如: "+86|xxxxxxxx"。手机号和邮箱参数至少传一项
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        """电子邮件。手机号和邮箱参数至少传一项
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        """用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupIdSet(self):
        """所属用户组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def AuthType(self):
        """认证方式，0 - 本地， 1 - LDAP， 2 - OAuth 不传则默认为0
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        """访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def DepartmentId(self):
        """所属部门ID，如：“1.2.3”
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
    """CreateUser返回参数结构体

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
        """新建用户的ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class DeleteAclsRequest(AbstractModel):
    """DeleteAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的权限ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的权限ID集合
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
    """DeleteAcls返回参数结构体

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


class DeleteChangePwdTaskRequest(AbstractModel):
    """DeleteChangePwdTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 改密任务id列表
        :type IdSet: list of int
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """改密任务id列表
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
    """DeleteChangePwdTask返回参数结构体

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


class DeleteCmdTemplatesRequest(AbstractModel):
    """DeleteCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的ID集合
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
    """DeleteCmdTemplates返回参数结构体

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


class DeleteDeviceAccountsRequest(AbstractModel):
    """DeleteDeviceAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的ID集合
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
    """DeleteDeviceAccounts返回参数结构体

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


class DeleteDeviceGroupMembersRequest(AbstractModel):
    """DeleteDeviceGroupMembers请求参数结构体

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
        """资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        """需要删除的资产ID集合
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
    """DeleteDeviceGroupMembers返回参数结构体

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


class DeleteDeviceGroupsRequest(AbstractModel):
    """DeleteDeviceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的资产组ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的资产组ID集合
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
    """DeleteDeviceGroups返回参数结构体

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


class DeleteDevicesRequest(AbstractModel):
    """DeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的ID集合
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
    """DeleteDevices返回参数结构体

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


class DeleteOperationTasksRequest(AbstractModel):
    """DeleteOperationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 运维任务ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """运维任务ID集合
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
    """DeleteOperationTasks返回参数结构体

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


class DeleteUserGroupMembersRequest(AbstractModel):
    """DeleteUserGroupMembers请求参数结构体

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
        """用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MemberIdSet(self):
        """需删除的成员用户ID集合
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
    """DeleteUserGroupMembers返回参数结构体

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


class DeleteUserGroupsRequest(AbstractModel):
    """DeleteUserGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的用户组ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的用户组ID集合
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
    """DeleteUserGroups返回参数结构体

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


class DeleteUsersRequest(AbstractModel):
    """DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 待删除的用户ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """待删除的用户ID集合
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
    """DeleteUsers返回参数结构体

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


class Department(AbstractModel):
    """部门信息

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
        """部门ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """部门名称，1 - 256个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Managers(self):
        """部门管理员账号ID
        :rtype: list of str
        """
        return self._Managers

    @Managers.setter
    def Managers(self, Managers):
        self._Managers = Managers

    @property
    def ManagerUsers(self):
        """管理员用户
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
    """部门管理员信息

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
        """管理员Id
        :rtype: str
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def ManagerName(self):
        """管理员姓名
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
        


class DeployResourceRequest(AbstractModel):
    """DeployResource请求参数结构体

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

    @property
    def ResourceId(self):
        """需要开通服务的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ApCode(self):
        """需要开通服务的地域
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def Zone(self):
        """子网所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """需要开通服务的VPC
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """需要开通服务的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CidrBlock(self):
        """需要开通服务的子网网段
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def VpcName(self):
        """需要开通服务的VPC名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        """需要开通服务的VPC对应的网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetName(self):
        """需要开通服务的子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CdcClusterId(self):
        """需要开通实例所属的CDC集群ID
        :rtype: str
        """
        return self._CdcClusterId

    @CdcClusterId.setter
    def CdcClusterId(self, CdcClusterId):
        self._CdcClusterId = CdcClusterId


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployResourceResponse(AbstractModel):
    """DeployResource返回参数结构体

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


class DescribeAclsRequest(AbstractModel):
    """DescribeAcls请求参数结构体

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
        self._DepartmentId = None
        self._ExactAccount = None
        self._Filters = None

    @property
    def IdSet(self):
        """访问权限ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """访问权限名称，模糊查询，最长64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Exact(self):
        """是否根据Name进行精确查询，默认值false
        :rtype: bool
        """
        return self._Exact

    @Exact.setter
    def Exact(self, Exact):
        self._Exact = Exact

    @property
    def AuthorizedUserIdSet(self):
        """有访问权限的用户ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedUserIdSet

    @AuthorizedUserIdSet.setter
    def AuthorizedUserIdSet(self, AuthorizedUserIdSet):
        self._AuthorizedUserIdSet = AuthorizedUserIdSet

    @property
    def AuthorizedDeviceIdSet(self):
        """有访问权限的资产ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedDeviceIdSet

    @AuthorizedDeviceIdSet.setter
    def AuthorizedDeviceIdSet(self, AuthorizedDeviceIdSet):
        self._AuthorizedDeviceIdSet = AuthorizedDeviceIdSet

    @property
    def AuthorizedAppAssetIdSet(self):
        """有访问权限的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedAppAssetIdSet

    @AuthorizedAppAssetIdSet.setter
    def AuthorizedAppAssetIdSet(self, AuthorizedAppAssetIdSet):
        self._AuthorizedAppAssetIdSet = AuthorizedAppAssetIdSet

    @property
    def Status(self):
        """访问权限状态，1 - 已生效，2 - 未生效，3 - 已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DepartmentId(self):
        """部门ID，用于过滤属于某个部门的访问权限
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def ExactAccount(self):
        """是否根据AuthorizedDeviceIdSet,对资产账号进行精确匹配，默认false, 设置true时，确保AuthorizedDeviceIdSet只有一个元素
        :rtype: bool
        """
        return self._ExactAccount

    @ExactAccount.setter
    def ExactAccount(self, ExactAccount):
        self._ExactAccount = ExactAccount

    @property
    def Filters(self):
        """过滤数组
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
    """DescribeAcls返回参数结构体

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
        """访问权限总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclSet(self):
        """访问权限列表
        :rtype: list of Acl
        """
        return self._AclSet

    @AclSet.setter
    def AclSet(self, AclSet):
        self._AclSet = AclSet

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
        if params.get("AclSet") is not None:
            self._AclSet = []
            for item in params.get("AclSet"):
                obj = Acl()
                obj._deserialize(item)
                self._AclSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetSyncStatusRequest(AbstractModel):
    """DescribeAssetSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Category: 查询的资产同步类型。1 -主机资产， 2 - 数据库资产
        :type Category: int
        """
        self._Category = None

    @property
    def Category(self):
        """查询的资产同步类型。1 -主机资产， 2 - 数据库资产
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
    """DescribeAssetSyncStatus返回参数结构体

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
        """资产同步结果
        :rtype: :class:`tencentcloud.bh.v20230418.models.AssetSyncStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Status") is not None:
            self._Status = AssetSyncStatus()
            self._Status._deserialize(params.get("Status"))
        self._RequestId = params.get("RequestId")


class DescribeChangePwdTaskDetailRequest(AbstractModel):
    """DescribeChangePwdTaskDetail请求参数结构体

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
        """改密任务Id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DepartmentId(self):
        """所属部门ID，如：“1.2.3”
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Filters(self):
        """过滤数组，支持：InstanceId 资产ID，DeviceName 资产名称，Ip 内外IP，Account 资产账号，LastChangeStatus 上次改密状态。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页偏移位置，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目。默认20
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
    """DescribeChangePwdTaskDetail返回参数结构体

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
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        """任务详情
        :rtype: list of ChangePwdTaskDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ChangePwdTaskDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChangePwdTaskRequest(AbstractModel):
    """DescribeChangePwdTask请求参数结构体

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
        """过滤数组。过滤数组。Name支持以下值: OperationId 任务ID TaskName 任务名
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DepartmentId(self):
        """所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Offset(self):
        """分页偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20
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
    """DescribeChangePwdTask返回参数结构体

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
        """任务详情
        :rtype: list of ChangePwdTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        """任务总数
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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ChangePwdTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCmdTemplatesRequest(AbstractModel):
    """DescribeCmdTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 命令模板ID集合，非必需
        :type IdSet: list of int non-negative
        :param _Name: 命令模板名，模糊查询，最大长度64字符
        :type Name: str
        :param _Type: 命令模板类型 1-内置模板 2-自定义模板
        :type Type: int
        :param _Offset: 分页偏移位置，默认值为0
        :type Offset: int
        :param _Limit: 每页条目数量，默认20
        :type Limit: int
        """
        self._IdSet = None
        self._Name = None
        self._Type = None
        self._Offset = None
        self._Limit = None

    @property
    def IdSet(self):
        """命令模板ID集合，非必需
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """命令模板名，模糊查询，最大长度64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """命令模板类型 1-内置模板 2-自定义模板
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20
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
    """DescribeCmdTemplates返回参数结构体

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
        """命令模板列表
        :rtype: list of CmdTemplate
        """
        return self._CmdTemplateSet

    @CmdTemplateSet.setter
    def CmdTemplateSet(self, CmdTemplateSet):
        self._CmdTemplateSet = CmdTemplateSet

    @property
    def TotalCount(self):
        """总记录数
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
        if params.get("CmdTemplateSet") is not None:
            self._CmdTemplateSet = []
            for item in params.get("CmdTemplateSet"):
                obj = CmdTemplate()
                obj._deserialize(item)
                self._CmdTemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeviceAccountsRequest(AbstractModel):
    """DescribeDeviceAccounts请求参数结构体

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
        """主机账号ID集合，非必需，如果使用IdSet则忽略其他过滤参数
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Account(self):
        """主机账号名，模糊查询，不能单独出现，必须于DeviceId一起提交
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DeviceId(self):
        """主机ID，未使用IdSet时必须携带
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20
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
    """DescribeDeviceAccounts返回参数结构体

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
        """记录总数
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupMembersRequest(AbstractModel):
    """DescribeDeviceGroupMembers请求参数结构体

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
        """true - 查询已在该资产组的资产，false - 查询未在该资产组的资产
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def Id(self):
        """资产组ID，Id和IdSet二选一
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IdSet(self):
        """资产组ID集合，传Id，IdSet不生效。
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """资产名或资产IP，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Kind(self):
        """资产类型，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def KindSet(self):
        """资产类型集合，1 - Linux，2 - Windows，3 - MySQL，4 - SQLServer
        :rtype: list of int non-negative
        """
        return self._KindSet

    @KindSet.setter
    def KindSet(self, KindSet):
        self._KindSet = KindSet

    @property
    def DepartmentId(self):
        """所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def TagFilters(self):
        """过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
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
    """DescribeDeviceGroupMembers返回参数结构体

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
        """资产组成员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceSet(self):
        """资产组成员列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

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
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupsRequest(AbstractModel):
    """DescribeDeviceGroups请求参数结构体

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
        """资产组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """资产组名，最长64个字符，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，缺省20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        """部门ID，用于过滤属于某个部门的资产组
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
    """DescribeDeviceGroups返回参数结构体

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
        """资产组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupSet(self):
        """资产组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

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
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

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
        self._TagFilters = None
        self._Filters = None

    @property
    def IdSet(self):
        """资产ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """资产名或资产IP，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ip(self):
        """暂未使用
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ApCodeSet(self):
        """地域码集合
        :rtype: list of str
        """
        return self._ApCodeSet

    @ApCodeSet.setter
    def ApCodeSet(self, ApCodeSet):
        self._ApCodeSet = ApCodeSet

    @property
    def Kind(self):
        """操作系统类型, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AuthorizedUserIdSet(self):
        """有该资产访问权限的用户ID集合
        :rtype: list of int non-negative
        """
        return self._AuthorizedUserIdSet

    @AuthorizedUserIdSet.setter
    def AuthorizedUserIdSet(self, AuthorizedUserIdSet):
        self._AuthorizedUserIdSet = AuthorizedUserIdSet

    @property
    def ResourceIdSet(self):
        """过滤条件，资产绑定的堡垒机服务ID集合
        :rtype: list of str
        """
        return self._ResourceIdSet

    @ResourceIdSet.setter
    def ResourceIdSet(self, ResourceIdSet):
        self._ResourceIdSet = ResourceIdSet

    @property
    def KindSet(self):
        """可提供按照多种类型过滤, 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: list of int non-negative
        """
        return self._KindSet

    @KindSet.setter
    def KindSet(self, KindSet):
        self._KindSet = KindSet

    @property
    def ManagedAccount(self):
        """资产是否包含托管账号。1，包含；0，不包含
        :rtype: str
        """
        return self._ManagedAccount

    @ManagedAccount.setter
    def ManagedAccount(self, ManagedAccount):
        self._ManagedAccount = ManagedAccount

    @property
    def DepartmentId(self):
        """过滤条件，可按照部门ID进行过滤
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def TagFilters(self):
        """过滤条件，可按照标签键、标签进行过滤。如果同时指定标签键和标签过滤条件，它们之间为“AND”的关系
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Filters(self):
        """过滤数组。支持的Name：
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
    """DescribeDevices返回参数结构体

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
        """资产总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceSet(self):
        """资产信息列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

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
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

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
        """每页条目数量，默认20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤数组
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
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
    """DescribeDomains返回参数结构体

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
        """网络域总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DomainSet(self):
        """网络域列表
        :rtype: list of Domain
        """
        return self._DomainSet

    @DomainSet.setter
    def DomainSet(self, DomainSet):
        self._DomainSet = DomainSet

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
        if params.get("DomainSet") is not None:
            self._DomainSet = []
            for item in params.get("DomainSet"):
                obj = Domain()
                obj._deserialize(item)
                self._DomainSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoginEventRequest(AbstractModel):
    """DescribeLoginEvent请求参数结构体

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
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
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
        self._Result = None
        self._Offset = None
        self._Limit = None

    @property
    def UserName(self):
        """用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名，模糊查询
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def StartTime(self):
        """查询时间范围，起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询时间范围，结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SourceIp(self):
        """来源IP，模糊查询
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Entry(self):
        """登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :rtype: int
        """
        return self._Entry

    @Entry.setter
    def Entry(self, Entry):
        self._Entry = Entry

    @property
    def Result(self):
        """操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页每页记录数，默认20
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
        self._Result = params.get("Result")
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
    """DescribeLoginEvent返回参数结构体

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
        """登录日志列表
        :rtype: list of LoginEvent
        """
        return self._LoginEventSet

    @LoginEventSet.setter
    def LoginEventSet(self, LoginEventSet):
        self._LoginEventSet = LoginEventSet

    @property
    def TotalCount(self):
        """总记录数
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
        if params.get("LoginEventSet") is not None:
            self._LoginEventSet = []
            for item in params.get("LoginEventSet"):
                obj = LoginEvent()
                obj._deserialize(item)
                self._LoginEventSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOperationEventRequest(AbstractModel):
    """DescribeOperationEvent请求参数结构体

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
        :param _Result: 操作结果，1-成功，2-失败
        :type Result: int
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
        self._Result = None
        self._Offset = None
        self._Limit = None

    @property
    def UserName(self):
        """用户名，如果不包含其他条件时对user_name or real_name两个字段模糊查询
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名，模糊查询
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def StartTime(self):
        """查询时间范围，起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询时间范围，结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SourceIp(self):
        """来源IP，模糊查询
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Kind(self):
        """操作类型，参考DescribeOperationType返回结果
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Result(self):
        """操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页每页记录数，默认20
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
        self._Result = params.get("Result")
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
    """DescribeOperationEvent返回参数结构体

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
        """操作日志列表
        :rtype: list of OperationEvent
        """
        return self._OperationEventSet

    @OperationEventSet.setter
    def OperationEventSet(self, OperationEventSet):
        self._OperationEventSet = OperationEventSet

    @property
    def TotalCount(self):
        """总记录数
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
        if params.get("OperationEventSet") is not None:
            self._OperationEventSet = []
            for item in params.get("OperationEventSet"):
                obj = OperationEvent()
                obj._deserialize(item)
                self._OperationEventSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOperationTaskRequest(AbstractModel):
    """DescribeOperationTask请求参数结构体

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
        """运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """运维任务类型，1 - 手工执行任务， 2 - 周期性任务
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数，默认20
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
    """DescribeOperationTask返回参数结构体

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
        """运维任务列表
        :rtype: list of OperationTask
        """
        return self._OperationTasks

    @OperationTasks.setter
    def OperationTasks(self, OperationTasks):
        self._OperationTasks = OperationTasks

    @property
    def TotalCount(self):
        """任务总数
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
        if params.get("OperationTasks") is not None:
            self._OperationTasks = []
            for item in params.get("OperationTasks"):
                obj = OperationTask()
                obj._deserialize(item)
                self._OperationTasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources请求参数结构体

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
        """地域码, 如: ap-guangzhou
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def VpcId(self):
        """按照堡垒机开通的 VPC 实例ID查询
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ResourceIds(self):
        """资源ID集合，当传入ID集合时忽略 ApCode 和 VpcId
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Limit(self):
        """每页条目数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移位置
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
    """DescribeResources返回参数结构体

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
        """堡垒机资源列表
        :rtype: list of Resource
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def TotalCount(self):
        """堡垒机资源数量
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
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserGroupMembersRequest(AbstractModel):
    """DescribeUserGroupMembers请求参数结构体

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
        """用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Bound(self):
        """true - 查询已添加到该用户组的用户，false - 查询未添加到该用户组的用户
        :rtype: bool
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def Name(self):
        """用户名或用户姓名，最长64个字符，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        """所属部门ID
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
    """DescribeUserGroupMembers返回参数结构体

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
        """用户组成员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserSet(self):
        """用户组成员列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

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
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserGroupsRequest(AbstractModel):
    """DescribeUserGroups请求参数结构体

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
        """用户组ID集合
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """用户组名，模糊查询,长度：0-64字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，缺省20，最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DepartmentId(self):
        """部门ID，用于过滤属于某个部门的用户组
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
    """DescribeUserGroups返回参数结构体

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
        """用户组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupSet(self):
        """用户组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

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
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = Group()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

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
        :param _AuthTypeSet: 认证方式，0 - 本地, 1 - LDAP, 2 - OAuth, 不传为全部
        :type AuthTypeSet: list of int non-negative
        :param _DepartmentId: 部门ID，用于过滤属于某个部门的用户
        :type DepartmentId: str
        :param _Filters: 参数过滤数组

        :type Filters: list of Filter
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

    @property
    def IdSet(self):
        """如果IdSet不为空，则忽略其他参数
        :rtype: list of int non-negative
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Name(self):
        """模糊查询，IdSet、UserName、Phone为空时才生效，对用户名和姓名进行模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条目数量，默认20, 最大500
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserName(self):
        """精确查询，IdSet为空时才生效
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        """精确查询，IdSet、UserName为空时才生效。
大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        """邮箱，精确查询
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AuthorizedDeviceIdSet(self):
        """查询具有指定资产ID访问权限的用户
        :rtype: list of int non-negative
        """
        return self._AuthorizedDeviceIdSet

    @AuthorizedDeviceIdSet.setter
    def AuthorizedDeviceIdSet(self, AuthorizedDeviceIdSet):
        self._AuthorizedDeviceIdSet = AuthorizedDeviceIdSet

    @property
    def AuthorizedAppAssetIdSet(self):
        """查询具有指定应用资产ID访问权限的用户
        :rtype: list of int non-negative
        """
        return self._AuthorizedAppAssetIdSet

    @AuthorizedAppAssetIdSet.setter
    def AuthorizedAppAssetIdSet(self, AuthorizedAppAssetIdSet):
        self._AuthorizedAppAssetIdSet = AuthorizedAppAssetIdSet

    @property
    def AuthTypeSet(self):
        """认证方式，0 - 本地, 1 - LDAP, 2 - OAuth, 不传为全部
        :rtype: list of int non-negative
        """
        return self._AuthTypeSet

    @AuthTypeSet.setter
    def AuthTypeSet(self, AuthTypeSet):
        self._AuthTypeSet = AuthTypeSet

    @property
    def DepartmentId(self):
        """部门ID，用于过滤属于某个部门的用户
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Filters(self):
        """参数过滤数组

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

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
        """用户总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserSet(self):
        """用户列表
        :rtype: list of User
        """
        return self._UserSet

    @UserSet.setter
    def UserSet(self, UserSet):
        self._UserSet = UserSet

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
        if params.get("UserSet") is not None:
            self._UserSet = []
            for item in params.get("UserSet"):
                obj = User()
                obj._deserialize(item)
                self._UserSet.append(obj)
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    """资产信息

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
        """
        self._Id = None
        self._InstanceId = None
        self._Name = None
        self._PublicIp = None
        self._PrivateIp = None
        self._ApCode = None
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

    @property
    def Id(self):
        """资产ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """实例ID，对应CVM、CDB等实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """资产名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PublicIp(self):
        """公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def ApCode(self):
        """地域编码
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def OsName(self):
        """操作系统名称
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Kind(self):
        """资产类型 1 - Linux, 2 - Windows, 3 - MySQL, 4 - SQLServer
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Port(self):
        """管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupSet(self):
        """所属资产组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def AccountCount(self):
        """资产绑定的账号数
        :rtype: int
        """
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Resource(self):
        """堡垒机服务信息，注意没有绑定服务时为null
        :rtype: :class:`tencentcloud.bh.v20230418.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Department(self):
        """资产所属部门
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def IpPortSet(self):
        """数据库资产的多节点
        :rtype: list of str
        """
        return self._IpPortSet

    @IpPortSet.setter
    def IpPortSet(self, IpPortSet):
        self._IpPortSet = IpPortSet

    @property
    def DomainId(self):
        """网络域Id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        """网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def EnableSSL(self):
        """是否启用SSL，仅支持Redis资产。0：禁用 1：启用
        :rtype: int
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def SSLCertName(self):
        """已上传的SSL证书名称
        :rtype: str
        """
        return self._SSLCertName

    @SSLCertName.setter
    def SSLCertName(self, SSLCertName):
        self._SSLCertName = SSLCertName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._ApCode = params.get("ApCode")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Domain(AbstractModel):
    """网络域

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
        """自增id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DomainId(self):
        """网络域id
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DomainName(self):
        """网络域名称
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ResourceId(self):
        """堡垒机id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def WhiteIpSet(self):
        """ip，网段
        :rtype: list of str
        """
        return self._WhiteIpSet

    @WhiteIpSet.setter
    def WhiteIpSet(self, WhiteIpSet):
        self._WhiteIpSet = WhiteIpSet

    @property
    def Enabled(self):
        """是否启用  默认 1启用 0禁用
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Status(self):
        """状态 0-已断开  1-已连接
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """网络域创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Default(self):
        """是否资源默认网络域 1-资源默认网络域 0-用户添加网络域
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
        


class ExternalDevice(AbstractModel):
    """主机参数，导入外部主机时使用

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

    @property
    def OsName(self):
        """操作系统名称，只能是Linux、Windows或MySQL
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Name(self):
        """主机名，可为空
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        """资产所属的部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def IpPortSet(self):
        """资产多节点：字段ip和端口
        :rtype: list of str
        """
        return self._IpPortSet

    @IpPortSet.setter
    def IpPortSet(self, IpPortSet):
        self._IpPortSet = IpPortSet

    @property
    def EnableSSL(self):
        """是否启用SSL,1:启用 0：禁用，仅支持Redis资产
        :rtype: int
        """
        return self._EnableSSL

    @EnableSSL.setter
    def EnableSSL(self, EnableSSL):
        self._EnableSSL = EnableSSL

    @property
    def SSLCert(self):
        """SSL证书，EnableSSL时必填
        :rtype: str
        """
        return self._SSLCert

    @SSLCert.setter
    def SSLCert(self, SSLCert):
        self._SSLCert = SSLCert

    @property
    def SSLCertName(self):
        """SSL证书名称，EnableSSL时必填
        :rtype: str
        """
        return self._SSLCertName

    @SSLCertName.setter
    def SSLCertName(self, SSLCertName):
        self._SSLCertName = SSLCertName


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询

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
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
    """组信息，用于用户组、主机组

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
        """组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Department(self):
        """所属部门信息
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Count(self):
        """个数
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
        


class ImportExternalDeviceRequest(AbstractModel):
    """ImportExternalDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceSet: 资产参数列表
        :type DeviceSet: list of ExternalDevice
        """
        self._DeviceSet = None

    @property
    def DeviceSet(self):
        """资产参数列表
        :rtype: list of ExternalDevice
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet


    def _deserialize(self, params):
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = ExternalDevice()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportExternalDeviceResponse(AbstractModel):
    """ImportExternalDevice返回参数结构体

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
        """资产ID列表
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

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
        self._DeviceIdSet = params.get("DeviceIdSet")
        self._RequestId = params.get("RequestId")


class LoginEvent(AbstractModel):
    """登录日志

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
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Time(self):
        """操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SourceIp(self):
        """来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Entry(self):
        """登录入口：1-字符界面,2-图形界面，3-web页面, 4-API
        :rtype: int
        """
        return self._Entry

    @Entry.setter
    def Entry(self, Entry):
        self._Entry = Entry

    @property
    def Result(self):
        """操作结果，1-成功，2-失败
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
        


class ModifyAclRequest(AbstractModel):
    """ModifyAcl请求参数结构体

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
        """访问权限名称，最大32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AllowDiskRedirect(self):
        """是否开启磁盘映射
        :rtype: bool
        """
        return self._AllowDiskRedirect

    @AllowDiskRedirect.setter
    def AllowDiskRedirect(self, AllowDiskRedirect):
        self._AllowDiskRedirect = AllowDiskRedirect

    @property
    def AllowAnyAccount(self):
        """是否允许任意账号登录
        :rtype: bool
        """
        return self._AllowAnyAccount

    @AllowAnyAccount.setter
    def AllowAnyAccount(self, AllowAnyAccount):
        self._AllowAnyAccount = AllowAnyAccount

    @property
    def Id(self):
        """访问权限ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AllowClipFileUp(self):
        """是否开启剪贴板文件上行
        :rtype: bool
        """
        return self._AllowClipFileUp

    @AllowClipFileUp.setter
    def AllowClipFileUp(self, AllowClipFileUp):
        self._AllowClipFileUp = AllowClipFileUp

    @property
    def AllowClipFileDown(self):
        """是否开启剪贴板文件下行
        :rtype: bool
        """
        return self._AllowClipFileDown

    @AllowClipFileDown.setter
    def AllowClipFileDown(self, AllowClipFileDown):
        self._AllowClipFileDown = AllowClipFileDown

    @property
    def AllowClipTextUp(self):
        """是否开启剪贴板文本（含图片）上行
        :rtype: bool
        """
        return self._AllowClipTextUp

    @AllowClipTextUp.setter
    def AllowClipTextUp(self, AllowClipTextUp):
        self._AllowClipTextUp = AllowClipTextUp

    @property
    def AllowClipTextDown(self):
        """是否开启剪贴板文本（含图片）下行
        :rtype: bool
        """
        return self._AllowClipTextDown

    @AllowClipTextDown.setter
    def AllowClipTextDown(self, AllowClipTextDown):
        self._AllowClipTextDown = AllowClipTextDown

    @property
    def AllowFileUp(self):
        """是否开启文件传输上传
        :rtype: bool
        """
        return self._AllowFileUp

    @AllowFileUp.setter
    def AllowFileUp(self, AllowFileUp):
        self._AllowFileUp = AllowFileUp

    @property
    def MaxFileUpSize(self):
        """文件传输上传大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileUpSize

    @MaxFileUpSize.setter
    def MaxFileUpSize(self, MaxFileUpSize):
        self._MaxFileUpSize = MaxFileUpSize

    @property
    def AllowFileDown(self):
        """是否开启文件传输下载
        :rtype: bool
        """
        return self._AllowFileDown

    @AllowFileDown.setter
    def AllowFileDown(self, AllowFileDown):
        self._AllowFileDown = AllowFileDown

    @property
    def MaxFileDownSize(self):
        """文件传输下载大小限制（预留参数，目前暂未使用）
        :rtype: int
        """
        return self._MaxFileDownSize

    @MaxFileDownSize.setter
    def MaxFileDownSize(self, MaxFileDownSize):
        self._MaxFileDownSize = MaxFileDownSize

    @property
    def UserIdSet(self):
        """关联的用户ID
        :rtype: list of int non-negative
        """
        return self._UserIdSet

    @UserIdSet.setter
    def UserIdSet(self, UserIdSet):
        self._UserIdSet = UserIdSet

    @property
    def UserGroupIdSet(self):
        """关联的用户组ID
        :rtype: list of int non-negative
        """
        return self._UserGroupIdSet

    @UserGroupIdSet.setter
    def UserGroupIdSet(self, UserGroupIdSet):
        self._UserGroupIdSet = UserGroupIdSet

    @property
    def DeviceIdSet(self):
        """关联的资产ID
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AppAssetIdSet(self):
        """关联的应用资产ID集合
        :rtype: list of int non-negative
        """
        return self._AppAssetIdSet

    @AppAssetIdSet.setter
    def AppAssetIdSet(self, AppAssetIdSet):
        self._AppAssetIdSet = AppAssetIdSet

    @property
    def DeviceGroupIdSet(self):
        """关联的资产组ID
        :rtype: list of int non-negative
        """
        return self._DeviceGroupIdSet

    @DeviceGroupIdSet.setter
    def DeviceGroupIdSet(self, DeviceGroupIdSet):
        self._DeviceGroupIdSet = DeviceGroupIdSet

    @property
    def AccountSet(self):
        """关联的账号
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def CmdTemplateIdSet(self):
        """关联的高危命令模板ID
        :rtype: list of int non-negative
        """
        return self._CmdTemplateIdSet

    @CmdTemplateIdSet.setter
    def CmdTemplateIdSet(self, CmdTemplateIdSet):
        self._CmdTemplateIdSet = CmdTemplateIdSet

    @property
    def ACTemplateIdSet(self):
        """关联高危DB模板ID
        :rtype: list of str
        """
        return self._ACTemplateIdSet

    @ACTemplateIdSet.setter
    def ACTemplateIdSet(self, ACTemplateIdSet):
        self._ACTemplateIdSet = ACTemplateIdSet

    @property
    def AllowDiskFileUp(self):
        """是否开启 RDP 磁盘映射文件上传
        :rtype: bool
        """
        return self._AllowDiskFileUp

    @AllowDiskFileUp.setter
    def AllowDiskFileUp(self, AllowDiskFileUp):
        self._AllowDiskFileUp = AllowDiskFileUp

    @property
    def AllowDiskFileDown(self):
        """是否开启 RDP 磁盘映射文件下载
        :rtype: bool
        """
        return self._AllowDiskFileDown

    @AllowDiskFileDown.setter
    def AllowDiskFileDown(self, AllowDiskFileDown):
        self._AllowDiskFileDown = AllowDiskFileDown

    @property
    def AllowShellFileUp(self):
        """是否开启rz sz文件上传
        :rtype: bool
        """
        return self._AllowShellFileUp

    @AllowShellFileUp.setter
    def AllowShellFileUp(self, AllowShellFileUp):
        self._AllowShellFileUp = AllowShellFileUp

    @property
    def AllowShellFileDown(self):
        """是否开启rz sz文件下载
        :rtype: bool
        """
        return self._AllowShellFileDown

    @AllowShellFileDown.setter
    def AllowShellFileDown(self, AllowShellFileDown):
        self._AllowShellFileDown = AllowShellFileDown

    @property
    def AllowFileDel(self):
        """是否开启 SFTP 文件删除
        :rtype: bool
        """
        return self._AllowFileDel

    @AllowFileDel.setter
    def AllowFileDel(self, AllowFileDel):
        self._AllowFileDel = AllowFileDel

    @property
    def ValidateFrom(self):
        """访问权限生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """访问权限失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则访问权限长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def DepartmentId(self):
        """权限所属部门的ID，如：1.2.3
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def AllowAccessCredential(self):
        """是否允许使用访问串
        :rtype: bool
        """
        return self._AllowAccessCredential

    @AllowAccessCredential.setter
    def AllowAccessCredential(self, AllowAccessCredential):
        self._AllowAccessCredential = AllowAccessCredential

    @property
    def AllowKeyboardLogger(self):
        """是否允许键盘记录
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
    """ModifyAcl返回参数结构体

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


class ModifyChangePwdTaskRequest(AbstractModel):
    """ModifyChangePwdTask请求参数结构体

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
        """改密任务id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DeviceIdSet(self):
        """改密资产id列表
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def AccountSet(self):
        """改密资产的账号列表
        :rtype: list of str
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def ModifyType(self):
        """修改类型：1：修改任务信息  2：关联任务资产账号
        :rtype: int
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ChangeMethod(self):
        """改密方式。1：使用执行账号修改密码；2：修改自身密码
        :rtype: int
        """
        return self._ChangeMethod

    @ChangeMethod.setter
    def ChangeMethod(self, ChangeMethod):
        self._ChangeMethod = ChangeMethod

    @property
    def AuthGenerationStrategy(self):
        """密码生成方式。 1:自动生成相同密码 2:自动生成不同密码 3:手动指定相同密码
        :rtype: int
        """
        return self._AuthGenerationStrategy

    @AuthGenerationStrategy.setter
    def AuthGenerationStrategy(self, AuthGenerationStrategy):
        self._AuthGenerationStrategy = AuthGenerationStrategy

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DepartmentId(self):
        """所属部门ID，"1,2,3"
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def RunAccount(self):
        """任务的执行账号	
        :rtype: str
        """
        return self._RunAccount

    @RunAccount.setter
    def RunAccount(self, RunAccount):
        self._RunAccount = RunAccount

    @property
    def Password(self):
        """密码，手动指定密码时必传。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordLength(self):
        """密码限制长度，自动生成密码必传。	
        :rtype: int
        """
        return self._PasswordLength

    @PasswordLength.setter
    def PasswordLength(self, PasswordLength):
        self._PasswordLength = PasswordLength

    @property
    def SmallLetter(self):
        """密码包含小写字母，0：否，1：是。
        :rtype: int
        """
        return self._SmallLetter

    @SmallLetter.setter
    def SmallLetter(self, SmallLetter):
        self._SmallLetter = SmallLetter

    @property
    def BigLetter(self):
        """密码包含大写字母，0：否，1：是。
        :rtype: int
        """
        return self._BigLetter

    @BigLetter.setter
    def BigLetter(self, BigLetter):
        self._BigLetter = BigLetter

    @property
    def Digit(self):
        """密码包含数字，0：否，1：是。
        :rtype: int
        """
        return self._Digit

    @Digit.setter
    def Digit(self, Digit):
        self._Digit = Digit

    @property
    def Symbol(self):
        """密码包含的特殊字符（base64编码），包含：^[-_#();%~!+=]*$
        :rtype: str
        """
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def CompleteNotify(self):
        """改密完成通知。0：不通知 1：通知
        :rtype: int
        """
        return self._CompleteNotify

    @CompleteNotify.setter
    def CompleteNotify(self, CompleteNotify):
        self._CompleteNotify = CompleteNotify

    @property
    def NotifyEmails(self):
        """通知邮箱
        :rtype: list of str
        """
        return self._NotifyEmails

    @NotifyEmails.setter
    def NotifyEmails(self, NotifyEmails):
        self._NotifyEmails = NotifyEmails

    @property
    def FilePassword(self):
        """加密压缩文件密码
        :rtype: str
        """
        return self._FilePassword

    @FilePassword.setter
    def FilePassword(self, FilePassword):
        self._FilePassword = FilePassword

    @property
    def Type(self):
        """任务类型， 4：手工执行  5：周期自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        """周期任务周期，单位天（大于等于 1，小于等于 365）
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        """周期任务首次执行时间
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
    """ModifyChangePwdTask返回参数结构体

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


class ModifyCmdTemplateRequest(AbstractModel):
    """ModifyCmdTemplate请求参数结构体

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
        """模板名，最长32字符，不能包含空白字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CmdList(self):
        """命令列表，\n分隔，最长32768字节
        :rtype: str
        """
        return self._CmdList

    @CmdList.setter
    def CmdList(self, CmdList):
        self._CmdList = CmdList

    @property
    def Id(self):
        """命令模板ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Encoding(self):
        """CmdList字段前端是否base64传值。
0：否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Type(self):
        """命令模板类型 1-内置模板 2-自定义模板
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
    """ModifyCmdTemplate返回参数结构体

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


class ModifyDeviceGroupRequest(AbstractModel):
    """ModifyDeviceGroup请求参数结构体

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
        """资产组名，最大长度32字符，不能为空
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        """资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DepartmentId(self):
        """资产组所属部门ID，如：1.2.3
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
    """ModifyDeviceGroup返回参数结构体

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


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

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
        """资产记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Port(self):
        """管理端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupIdSet(self):
        """资产所属组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def DepartmentId(self):
        """资产所属部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DomainId(self):
        """网络域Id
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
    """ModifyDevice返回参数结构体

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


class ModifyOAuthSettingRequest(AbstractModel):
    """ModifyOAuthSetting请求参数结构体

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
        """是否开启OAuth认证，false-不开启，true-开启。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AuthMethod(self):
        """OAuth认证方式。
        :rtype: str
        """
        return self._AuthMethod

    @AuthMethod.setter
    def AuthMethod(self, AuthMethod):
        self._AuthMethod = AuthMethod

    @property
    def ClientId(self):
        """OAuth认证客户端Id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        """OAuth认证客户端密钥
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def CodeUrl(self):
        """获取OAuth认证授权码URL
        :rtype: str
        """
        return self._CodeUrl

    @CodeUrl.setter
    def CodeUrl(self, CodeUrl):
        self._CodeUrl = CodeUrl

    @property
    def TokenUrl(self):
        """获取OAuth令牌URL
        :rtype: str
        """
        return self._TokenUrl

    @TokenUrl.setter
    def TokenUrl(self, TokenUrl):
        self._TokenUrl = TokenUrl

    @property
    def UserInfoUrl(self):
        """获取OAuth用户信息URL
        :rtype: str
        """
        return self._UserInfoUrl

    @UserInfoUrl.setter
    def UserInfoUrl(self, UserInfoUrl):
        self._UserInfoUrl = UserInfoUrl

    @property
    def Scopes(self):
        """使用Okta认证时指定范围。为空时默认使用 openid、profile、email。
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
    """ModifyOAuthSetting返回参数结构体

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


class ModifyOperationTaskRequest(AbstractModel):
    """ModifyOperationTask请求参数结构体

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
        """任务Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """任务类型, 1 - 手工执行, 2 - 周期性自动执行
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Account(self):
        """执行账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Timeout(self):
        """超时时间,单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Script(self):
        """执行脚本内容
        :rtype: str
        """
        return self._Script

    @Script.setter
    def Script(self, Script):
        self._Script = Script

    @property
    def DeviceIdSet(self):
        """执行主机集合，满足条件以下三个条件：1. 资产绑定可用的专业版或国密版堡垒机服务；2、资产类型为linux资产；3、用户具有资产权限，且资产添加了指定执行账号
        :rtype: list of int non-negative
        """
        return self._DeviceIdSet

    @DeviceIdSet.setter
    def DeviceIdSet(self, DeviceIdSet):
        self._DeviceIdSet = DeviceIdSet

    @property
    def Period(self):
        """执行间隔，单位天. 手工执行时无需传入
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def FirstTime(self):
        """首次执行日期，默认1970-01-01T08:00:01+08:00,手工执行时无需传入
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Encoding(self):
        """Script参数是否需要进行base64编码后传递，1-需要进行base64编码后传递，非1值-不需要进行base64编码后传递
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
    """ModifyOperationTask返回参数结构体

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


class ModifyResourceRequest(AbstractModel):
    """ModifyResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 需要开通服务的资源ID
        :type ResourceId: str
        :param _Status: 已废弃
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
        """需要开通服务的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        """已废弃
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceEdition(self):
        """实例版本
        :rtype: str
        """
        return self._ResourceEdition

    @ResourceEdition.setter
    def ResourceEdition(self, ResourceEdition):
        self._ResourceEdition = ResourceEdition

    @property
    def ResourceNode(self):
        """资源节点数
        :rtype: int
        """
        return self._ResourceNode

    @ResourceNode.setter
    def ResourceNode(self, ResourceNode):
        self._ResourceNode = ResourceNode

    @property
    def AutoRenewFlag(self):
        """自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PackageBandwidth(self):
        """带宽扩展包个数(4M)
        :rtype: int
        """
        return self._PackageBandwidth

    @PackageBandwidth.setter
    def PackageBandwidth(self, PackageBandwidth):
        self._PackageBandwidth = PackageBandwidth

    @property
    def PackageNode(self):
        """授权点数扩展包个数(50点)
        :rtype: int
        """
        return self._PackageNode

    @PackageNode.setter
    def PackageNode(self, PackageNode):
        self._PackageNode = PackageNode

    @property
    def LogDelivery(self):
        """日志投递
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
    """ModifyResource返回参数结构体

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


class ModifyUserGroupRequest(AbstractModel):
    """ModifyUserGroup请求参数结构体

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
        """用户组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """用户组名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DepartmentId(self):
        """用户组所属的部门ID，如：1.2.3
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
    """ModifyUserGroup返回参数结构体

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
        """用户ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RealName(self):
        """用户姓名，最大长度20个字符，不能包含空格
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Phone(self):
        """按照"国家地区代码|手机号"的格式输入。如: "+86|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        """电子邮件
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        """用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """用户失效时间，如:"2021-09-23T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupIdSet(self):
        """所属用户组ID集合
        :rtype: list of int non-negative
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def AuthType(self):
        """认证方式，0 - 本地，1 - LDAP，2 - OAuth 不传则默认为0
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        """访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def DepartmentId(self):
        """用户所属部门的ID，如1.2.3
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
    """ModifyUser返回参数结构体

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


class OperationEvent(AbstractModel):
    """操作日志

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
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Time(self):
        """操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SourceIp(self):
        """来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Kind(self):
        """操作类型
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Operation(self):
        """具体操作内容
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Result(self):
        """操作结果，1-成功，2-失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SignValue(self):
        """签名值
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
    """运维任务信息

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
        """运维任务主键ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationId(self):
        """运维任务ID
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def Name(self):
        """运维任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UserName(self):
        """创建用户
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """运维人员姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Type(self):
        """任务类型，1 - 手工执行任务， 2 - 周期性任务
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        """周期性任务执行间隔，单位天
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def NextTime(self):
        """执行账户
        :rtype: str
        """
        return self._NextTime

    @NextTime.setter
    def NextTime(self, NextTime):
        self._NextTime = NextTime

    @property
    def FirstTime(self):
        """下一次执行时间
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
        


class ResetDeviceAccountPasswordRequest(AbstractModel):
    """ResetDeviceAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """ID集合
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
    """ResetDeviceAccountPassword返回参数结构体

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


class ResetDeviceAccountPrivateKeyRequest(AbstractModel):
    """ResetDeviceAccountPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """ID集合
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
    """ResetDeviceAccountPrivateKey返回参数结构体

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


class ResetUserRequest(AbstractModel):
    """ResetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdSet: 用户ID集合
        :type IdSet: list of int non-negative
        """
        self._IdSet = None

    @property
    def IdSet(self):
        """用户ID集合
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
    """ResetUser返回参数结构体

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


class Resource(AbstractModel):
    """堡垒机服务信息

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
        :param _IntranetVpcCidr: 开通内网访问vpc的网段
        :type IntranetVpcCidr: str
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
        self._IntranetVpcCidr = None

    @property
    def ResourceId(self):
        """服务实例ID，如bh-saas-s3ed4r5e
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ApCode(self):
        """地域编码
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def SvArgs(self):
        """服务实例规格信息
        :rtype: str
        """
        return self._SvArgs

    @SvArgs.setter
    def SvArgs(self, SvArgs):
        self._SvArgs = SvArgs

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Nodes(self):
        """服务规格对应的资产数
        :rtype: int
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def RenewFlag(self):
        """自动续费标记，0 - 表示默认状态，1 - 表示自动续费，2 - 表示明确不自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        """资源状态，0 - 未初始化，1 - 正常，2 - 隔离，3 - 销毁，4 - 初始化失败，5 - 初始化中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResourceName(self):
        """服务实例名，如T-Sec-堡垒机（SaaS型）
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Pid(self):
        """定价模型ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def CreateTime(self):
        """资源创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductCode(self):
        """商品码, p_cds_dasb
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        """子商品码, sp_cds_dasb_bh_saas
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Expired(self):
        """是否过期，true-过期，false-未过期
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def Deployed(self):
        """是否开通，true-开通，false-未开通
        :rtype: bool
        """
        return self._Deployed

    @Deployed.setter
    def Deployed(self, Deployed):
        self._Deployed = Deployed

    @property
    def VpcName(self):
        """开通服务的 VPC 名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        """开通服务的 VPC 对应的网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        """开通服务的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        """开通服务的子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """开通服务的子网网段
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def PublicIpSet(self):
        """外部IP
        :rtype: list of str
        """
        return self._PublicIpSet

    @PublicIpSet.setter
    def PublicIpSet(self, PublicIpSet):
        self._PublicIpSet = PublicIpSet

    @property
    def PrivateIpSet(self):
        """内部IP
        :rtype: list of str
        """
        return self._PrivateIpSet

    @PrivateIpSet.setter
    def PrivateIpSet(self, PrivateIpSet):
        self._PrivateIpSet = PrivateIpSet

    @property
    def ModuleSet(self):
        """服务开通的高级功能列表，如:[DB]
        :rtype: list of str
        """
        return self._ModuleSet

    @ModuleSet.setter
    def ModuleSet(self, ModuleSet):
        self._ModuleSet = ModuleSet

    @property
    def UsedNodes(self):
        """已使用的授权点数
        :rtype: int
        """
        return self._UsedNodes

    @UsedNodes.setter
    def UsedNodes(self, UsedNodes):
        self._UsedNodes = UsedNodes

    @property
    def ExtendPoints(self):
        """扩展点数
        :rtype: int
        """
        return self._ExtendPoints

    @ExtendPoints.setter
    def ExtendPoints(self, ExtendPoints):
        self._ExtendPoints = ExtendPoints

    @property
    def PackageBandwidth(self):
        """带宽扩展包个数(4M)
        :rtype: int
        """
        return self._PackageBandwidth

    @PackageBandwidth.setter
    def PackageBandwidth(self, PackageBandwidth):
        self._PackageBandwidth = PackageBandwidth

    @property
    def PackageNode(self):
        """授权点数扩展包个数(50点)
        :rtype: int
        """
        return self._PackageNode

    @PackageNode.setter
    def PackageNode(self, PackageNode):
        self._PackageNode = PackageNode

    @property
    def LogDeliveryArgs(self):
        """日志投递规格信息
        :rtype: str
        """
        return self._LogDeliveryArgs

    @LogDeliveryArgs.setter
    def LogDeliveryArgs(self, LogDeliveryArgs):
        self._LogDeliveryArgs = LogDeliveryArgs

    @property
    def ClbSet(self):
        """堡垒机资源LB	
        :rtype: list of Clb
        """
        return self._ClbSet

    @ClbSet.setter
    def ClbSet(self, ClbSet):
        self._ClbSet = ClbSet

    @property
    def DomainCount(self):
        """网络域个数
        :rtype: int
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def UsedDomainCount(self):
        """已经使用的网络域个数
        :rtype: int
        """
        return self._UsedDomainCount

    @UsedDomainCount.setter
    def UsedDomainCount(self, UsedDomainCount):
        self._UsedDomainCount = UsedDomainCount

    @property
    def Trial(self):
        """0 非试用版，1 试用版
        :rtype: int
        """
        return self._Trial

    @Trial.setter
    def Trial(self, Trial):
        self._Trial = Trial

    @property
    def LogDelivery(self):
        """日志投递规格信息
        :rtype: str
        """
        return self._LogDelivery

    @LogDelivery.setter
    def LogDelivery(self, LogDelivery):
        self._LogDelivery = LogDelivery

    @property
    def CdcClusterId(self):
        """cdc集群id
        :rtype: str
        """
        return self._CdcClusterId

    @CdcClusterId.setter
    def CdcClusterId(self, CdcClusterId):
        self._CdcClusterId = CdcClusterId

    @property
    def DeployModel(self):
        """部署模式 默认0 0-cvm 1-tke
        :rtype: int
        """
        return self._DeployModel

    @DeployModel.setter
    def DeployModel(self, DeployModel):
        self._DeployModel = DeployModel

    @property
    def IntranetAccess(self):
        """0 默认值，非内网访问，1 内网访问，2 内网访问开通中，3 内网访问关闭中
        :rtype: int
        """
        return self._IntranetAccess

    @IntranetAccess.setter
    def IntranetAccess(self, IntranetAccess):
        self._IntranetAccess = IntranetAccess

    @property
    def IntranetPrivateIpSet(self):
        """内网访问的ip
        :rtype: list of str
        """
        return self._IntranetPrivateIpSet

    @IntranetPrivateIpSet.setter
    def IntranetPrivateIpSet(self, IntranetPrivateIpSet):
        self._IntranetPrivateIpSet = IntranetPrivateIpSet

    @property
    def IntranetVpcId(self):
        """开通内网访问的vpc
        :rtype: str
        """
        return self._IntranetVpcId

    @IntranetVpcId.setter
    def IntranetVpcId(self, IntranetVpcId):
        self._IntranetVpcId = IntranetVpcId

    @property
    def IntranetVpcCidr(self):
        """开通内网访问vpc的网段
        :rtype: str
        """
        return self._IntranetVpcCidr

    @IntranetVpcCidr.setter
    def IntranetVpcCidr(self, IntranetVpcCidr):
        self._IntranetVpcCidr = IntranetVpcCidr


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
        self._IntranetVpcCidr = params.get("IntranetVpcCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunChangePwdTaskDetail(AbstractModel):
    """立即执行改密任务的入参

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
        """资产id
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Account(self):
        """资产账号
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
    """RunChangePwdTask请求参数结构体

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
        """任务Id
        :rtype: str
        """
        return self._OperationId

    @OperationId.setter
    def OperationId(self, OperationId):
        self._OperationId = OperationId

    @property
    def DepartmentId(self):
        """部门id
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Details(self):
        """改密任务详情
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
    """RunChangePwdTask返回参数结构体

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


class RunOperationTaskRequest(AbstractModel):
    """RunOperationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 运维任务ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """运维任务ID
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
    """RunOperationTask返回参数结构体

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


class SearchAuditLogRequest(AbstractModel):
    """SearchAuditLog请求参数结构体

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
        """开始时间，不得早于当前时间的180天前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
        """每页容量，默认为20，最大200
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
    """SearchAuditLog返回参数结构体

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
        """日志总数量
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchCommandBySidRequest(AbstractModel):
    """SearchCommandBySid请求参数结构体

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
        """会话Id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Cmd(self):
        """命令，可模糊搜索
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Encoding(self):
        """Cmd字段是前端传值是否进行base64.
0:否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

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
        """每页容量，默认20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AuditAction(self):
        """根据拦截状态进行过滤
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
    """SearchCommandBySid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchCommandRequest(AbstractModel):
    """SearchCommand请求参数结构体

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
        """搜索区间的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """搜索区间的结束时间，不填默认为开始时间到现在为止
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        """资产实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        """资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        """资产的公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """资产的内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cmd(self):
        """执行的命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Encoding(self):
        """Cmd字段是前端传值是否进行base64.
0:否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def AuditAction(self):
        """根据拦截状态进行过滤：1 - 已执行，2 - 被阻断
        :rtype: list of int non-negative
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def Limit(self):
        """每页容量，默认20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
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
    """SearchCommand返回参数结构体

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
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Commands(self):
        """命令列表
        :rtype: list of SearchCommandResult
        """
        return self._Commands

    @Commands.setter
    def Commands(self, Commands):
        self._Commands = Commands

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
        if params.get("Commands") is not None:
            self._Commands = []
            for item in params.get("Commands"):
                obj = SearchCommandResult()
                obj._deserialize(item)
                self._Commands.append(obj)
        self._RequestId = params.get("RequestId")


class SearchCommandResult(AbstractModel):
    """命令执行检索结果

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
        :param _SessTime: 该命令所属会话的会话开始时间（废弃，使用SessionTime）
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

    @property
    def Time(self):
        """命令输入的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        """资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        """资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        """资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cmd(self):
        """命令
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Action(self):
        """命令执行情况，1--允许，2--拒绝
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Sid(self):
        """命令所属的会话ID
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def TimeOffset(self):
        """命令执行时间相对于所属会话开始时间的偏移量，单位ms
        :rtype: int
        """
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset

    @property
    def Account(self):
        """账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        """source ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def SessionTime(self):
        """该命令所属会话的会话开始时间
        :rtype: str
        """
        return self._SessionTime

    @SessionTime.setter
    def SessionTime(self, SessionTime):
        self._SessionTime = SessionTime

    @property
    def SessTime(self):
        """该命令所属会话的会话开始时间（废弃，使用SessionTime）
        :rtype: str
        """
        return self._SessTime

    @SessTime.setter
    def SessTime(self, SessTime):
        self._SessTime = SessTime

    @property
    def ConfirmTime(self):
        """复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        """部门id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        """用户部门名称
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        """设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        """设备部门名称
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def Size(self):
        """会话大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SignValue(self):
        """签名值
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFileBySidRequest(AbstractModel):
    """SearchFileBySid请求参数结构体

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
        :param _TypeFilters: 以Protocol和Method为条件查询
        :type TypeFilters: list of SearchFileTypeFilter
        """
        self._Sid = None
        self._AuditLog = None
        self._Limit = None
        self._FileName = None
        self._Offset = None
        self._AuditAction = None
        self._TypeFilters = None

    @property
    def Sid(self):
        """若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def AuditLog(self):
        """是否创建审计日志,通过查看按钮调用时为true,其他为false
        :rtype: bool
        """
        return self._AuditLog

    @AuditLog.setter
    def AuditLog(self, AuditLog):
        self._AuditLog = AuditLog

    @property
    def Limit(self):
        """分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FileName(self):
        """可填写路径名或文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Offset(self):
        """分页用偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AuditAction(self):
        """1-已执行，  2-被阻断
        :rtype: int
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def TypeFilters(self):
        """以Protocol和Method为条件查询
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
    """SearchFileBySid返回参数结构体

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
        """记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SearchFileBySidResult(self):
        """某会话的文件操作列表
        :rtype: list of SearchFileBySidResult
        """
        return self._SearchFileBySidResult

    @SearchFileBySidResult.setter
    def SearchFileBySidResult(self, SearchFileBySidResult):
        self._SearchFileBySidResult = SearchFileBySidResult

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
        if params.get("SearchFileBySidResult") is not None:
            self._SearchFileBySidResult = []
            for item in params.get("SearchFileBySidResult"):
                obj = SearchFileBySidResult()
                obj._deserialize(item)
                self._SearchFileBySidResult.append(obj)
        self._RequestId = params.get("RequestId")


class SearchFileBySidResult(AbstractModel):
    """文件操作搜索结果

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
        """会话Id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Account(self):
        """资产账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        """来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Time(self):
        """文件操作时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Method(self):
        """1-上传文件 2-下载文件 3-删除文件 4-移动文件 5-重命名文件 6-新建文件夹 7-移动文件夹 8-重命名文件夹 9-删除文件夹
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Protocol(self):
        """文件传输协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FileCurr(self):
        """method为上传、下载、删除时文件在服务器上的位置, 或重命名、移动文件前文件的位置
        :rtype: str
        """
        return self._FileCurr

    @FileCurr.setter
    def FileCurr(self, FileCurr):
        self._FileCurr = FileCurr

    @property
    def FileNew(self):
        """method为重命名、移动文件时代表移动后的新位置.其他情况为null
        :rtype: str
        """
        return self._FileNew

    @FileNew.setter
    def FileNew(self, FileNew):
        self._FileNew = FileNew

    @property
    def Size(self):
        """method为上传文件、下载文件、删除文件时显示文件大小。其他情况为null
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Action(self):
        """堡垒机拦截情况, 1-已执行，  2-被阻断
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ConfirmTime(self):
        """复核时间，当Action是3时，需有复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        """用户部门Id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        """用户部门name
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        """设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        """设备部门name
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def SignValue(self):
        """签名值
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
    """SearchFile请求参数结构体

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
        """查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        """资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        """资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        """资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Method(self):
        """操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :rtype: list of int non-negative
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def FileName(self):
        """可填写路径名或文件（夹）名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AuditAction(self):
        """1-已执行，  2-被阻断
        :rtype: list of int non-negative
        """
        return self._AuditAction

    @AuditAction.setter
    def AuditAction(self, AuditAction):
        self._AuditAction = AuditAction

    @property
    def Limit(self):
        """分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
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
    """SearchFile返回参数结构体

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
        """记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Files(self):
        """文件操作列表
        :rtype: list of SearchFileResult
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = SearchFileResult()
                obj._deserialize(item)
                self._Files.append(obj)
        self._RequestId = params.get("RequestId")


class SearchFileResult(AbstractModel):
    """文件传输检索结果

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
        """文件传输的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def InstanceId(self):
        """资产ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        """资产名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PublicIp(self):
        """资产公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """资产内网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Action(self):
        """操作结果：1 - 已执行，2 - 已阻断
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Method(self):
        """操作类型：1 - 文件上传，2 - 文件下载，3 - 文件删除，4 - 文件(夹)移动，5 - 文件(夹)重命名，6 - 新建文件夹，9 - 删除文件夹
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def FileCurr(self):
        """下载的文件（夹）路径及名称
        :rtype: str
        """
        return self._FileCurr

    @FileCurr.setter
    def FileCurr(self, FileCurr):
        self._FileCurr = FileCurr

    @property
    def FileNew(self):
        """上传或新建文件（夹）路径及名称
        :rtype: str
        """
        return self._FileNew

    @FileNew.setter
    def FileNew(self, FileNew):
        self._FileNew = FileNew

    @property
    def Sid(self):
        """会话id
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Account(self):
        """账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        """来源id
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Size(self):
        """文件大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def ConfirmTime(self):
        """复核时间
        :rtype: str
        """
        return self._ConfirmTime

    @ConfirmTime.setter
    def ConfirmTime(self, ConfirmTime):
        self._ConfirmTime = ConfirmTime

    @property
    def UserDepartmentId(self):
        """用户部门id
        :rtype: str
        """
        return self._UserDepartmentId

    @UserDepartmentId.setter
    def UserDepartmentId(self, UserDepartmentId):
        self._UserDepartmentId = UserDepartmentId

    @property
    def UserDepartmentName(self):
        """用户部门name
        :rtype: str
        """
        return self._UserDepartmentName

    @UserDepartmentName.setter
    def UserDepartmentName(self, UserDepartmentName):
        self._UserDepartmentName = UserDepartmentName

    @property
    def DeviceDepartmentId(self):
        """设备部门id
        :rtype: str
        """
        return self._DeviceDepartmentId

    @DeviceDepartmentId.setter
    def DeviceDepartmentId(self, DeviceDepartmentId):
        self._DeviceDepartmentId = DeviceDepartmentId

    @property
    def DeviceDepartmentName(self):
        """设备部门name	
        :rtype: str
        """
        return self._DeviceDepartmentName

    @DeviceDepartmentName.setter
    def DeviceDepartmentName(self, DeviceDepartmentName):
        self._DeviceDepartmentName = DeviceDepartmentName

    @property
    def SignValue(self):
        """签名值
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
    """用于搜索文件传输记录等日志时按照protocol和method进行过滤

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
        """需要查询的文件传输类型，如SFTP/CLIP/RDP/RZSZ
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Method(self):
        """在当前指定的protocol下进一步过滤具体操作类型,如剪贴板文件上传，剪贴板文件下载等
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
    """SearchSessionCommand请求参数结构体

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
        """检索的目标命令，为模糊搜索
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def StartTime(self):
        """开始时间，不得早于当前时间的180天前
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        """分页偏移位置，默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """默认值为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Encoding(self):
        """Cmd字段前端是否做base64加密
0：否，1：是
        :rtype: int
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def EndTime(self):
        """结束时间
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
    """SearchSessionCommand返回参数结构体

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
        """记录总数
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class SearchSessionRequest(AbstractModel):
    """SearchSession请求参数结构体

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
        :param _Id: 若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :type Id: str
        :param _AppAssetKindSet: 应用资产类型, 1-web
        :type AppAssetKindSet: list of int non-negative
        :param _AppAssetUrl: 应用资产Url
        :type AppAssetUrl: str
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
        self._Id = None
        self._AppAssetKindSet = None
        self._AppAssetUrl = None

    @property
    def PrivateIp(self):
        """内部Ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        """外部Ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def UserName(self):
        """用户名，长度不超过20
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Account(self):
        """账号，长度不超过64
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def FromIp(self):
        """来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def StartTime(self):
        """搜索区间的开始时间。若入参是Id，则非必传，否则为必传。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """搜索区间的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Kind(self):
        """会话协议类型，只能是1、2、3或4 对应关系为1-tui 2-gui 3-file 4-数据库。若入参是Id，则非必传，否则为必传。
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

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
        """分页的页内记录数，默认为20，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RealName(self):
        """姓名，长度不超过20
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def DeviceName(self):
        """主机名，长度不超过64
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        """状态，1为活跃，2为结束，3为强制离线，4为其他错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        """若入参为Id，则其他入参字段不作为搜索依据，仅按照Id来搜索会话
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppAssetKindSet(self):
        """应用资产类型, 1-web
        :rtype: list of int non-negative
        """
        return self._AppAssetKindSet

    @AppAssetKindSet.setter
    def AppAssetKindSet(self, AppAssetKindSet):
        self._AppAssetKindSet = AppAssetKindSet

    @property
    def AppAssetUrl(self):
        """应用资产Url
        :rtype: str
        """
        return self._AppAssetUrl

    @AppAssetUrl.setter
    def AppAssetUrl(self, AppAssetUrl):
        self._AppAssetUrl = AppAssetUrl


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
        self._Id = params.get("Id")
        self._AppAssetKindSet = params.get("AppAssetKindSet")
        self._AppAssetUrl = params.get("AppAssetUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchSessionResponse(AbstractModel):
    """SearchSession返回参数结构体

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
        """记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SessionSet(self):
        """会话信息列表
        :rtype: list of SessionResult
        """
        return self._SessionSet

    @SessionSet.setter
    def SessionSet(self, SessionSet):
        self._SessionSet = SessionSet

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
        if params.get("SessionSet") is not None:
            self._SessionSet = []
            for item in params.get("SessionSet"):
                obj = SessionResult()
                obj._deserialize(item)
                self._SessionSet.append(obj)
        self._RequestId = params.get("RequestId")


class SessionResult(AbstractModel):
    """搜索字符或图形会话时返回的SessionResul结构体

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

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """姓名
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Account(self):
        """主机账号
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        """会话大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def InstanceId(self):
        """设备ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceName(self):
        """设备名
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PrivateIp(self):
        """内部Ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        """外部Ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def FromIp(self):
        """来源Ip
        :rtype: str
        """
        return self._FromIp

    @FromIp.setter
    def FromIp(self, FromIp):
        self._FromIp = FromIp

    @property
    def Duration(self):
        """会话持续时长
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Count(self):
        """该会话内命令数量 ，搜索图形会话时该字段无意义
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DangerCount(self):
        """该会话内高危命令数，搜索图形时该字段无意义
        :rtype: int
        """
        return self._DangerCount

    @DangerCount.setter
    def DangerCount(self, DangerCount):
        self._DangerCount = DangerCount

    @property
    def Status(self):
        """会话状态，如1会话活跃  2会话结束  3强制离线  4其他错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        """会话Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ApCode(self):
        """设备所属的地域
        :rtype: str
        """
        return self._ApCode

    @ApCode.setter
    def ApCode(self, ApCode):
        self._ApCode = ApCode

    @property
    def Protocol(self):
        """会话协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def AppAssetKind(self):
        """应用资产类型：1-web
        :rtype: int
        """
        return self._AppAssetKind

    @AppAssetKind.setter
    def AppAssetKind(self, AppAssetKind):
        self._AppAssetKind = AppAssetKind

    @property
    def AppAssetUrl(self):
        """应用资产url
        :rtype: str
        """
        return self._AppAssetUrl

    @AppAssetUrl.setter
    def AppAssetUrl(self, AppAssetUrl):
        self._AppAssetUrl = AppAssetUrl

    @property
    def ReplayType(self):
        """回放类型 默认0, 1-rfb 2-mp4 3-ssh
        :rtype: int
        """
        return self._ReplayType

    @ReplayType.setter
    def ReplayType(self, ReplayType):
        self._ReplayType = ReplayType


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """资产标签

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
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        


class User(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名, 3-20个字符 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
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

    @property
    def UserName(self):
        """用户名, 3-20个字符 必须以英文字母开头，且不能包含字母、数字、.、_、-以外的字符
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """用户姓名， 最大20个字符，不能包含空白字符
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def Id(self):
        """用户ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Phone(self):
        """手机号码， 大陆手机号直接填写，如果是其他国家、地区号码,按照"国家地区代码|手机号"的格式输入。如: "+852|xxxxxxxx"
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        """电子邮件
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ValidateFrom(self):
        """用户生效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateFrom

    @ValidateFrom.setter
    def ValidateFrom(self, ValidateFrom):
        self._ValidateFrom = ValidateFrom

    @property
    def ValidateTo(self):
        """用户失效时间，如:"2021-09-22T00:00:00+00:00"
生效、失效时间不填则用户长期有效
        :rtype: str
        """
        return self._ValidateTo

    @ValidateTo.setter
    def ValidateTo(self, ValidateTo):
        self._ValidateTo = ValidateTo

    @property
    def GroupSet(self):
        """所属用户组列表
        :rtype: list of Group
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def AuthType(self):
        """认证方式，0 - 本地，1 - LDAP，2 - OAuth
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ValidateTime(self):
        """访问时间段限制， 由0、1组成的字符串，长度168(7 × 24)，代表该用户在一周中允许访问的时间段。字符串中第N个字符代表在一周中的第N个小时， 0 - 代表不允许访问，1 - 代表允许访问
        :rtype: str
        """
        return self._ValidateTime

    @ValidateTime.setter
    def ValidateTime(self, ValidateTime):
        self._ValidateTime = ValidateTime

    @property
    def Department(self):
        """用户所属部门（用于出参）
        :rtype: :class:`tencentcloud.bh.v20230418.models.Department`
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def DepartmentId(self):
        """用户所属部门（用于入参）
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def ActiveStatus(self):
        """激活状态 0 - 未激活 1 - 激活
        :rtype: int
        """
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def LockStatus(self):
        """锁定状态 0 - 未锁定 1 - 锁定
        :rtype: int
        """
        return self._LockStatus

    @LockStatus.setter
    def LockStatus(self, LockStatus):
        self._LockStatus = LockStatus

    @property
    def UKeyStatus(self):
        """ukey绑定状态 0 - 未绑定 1 - 已绑定
        :rtype: int
        """
        return self._UKeyStatus

    @UKeyStatus.setter
    def UKeyStatus(self, UKeyStatus):
        self._UKeyStatus = UKeyStatus

    @property
    def Status(self):
        """状态 与Filter中一致
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AclVersion(self):
        """权限版本
        :rtype: int
        """
        return self._AclVersion

    @AclVersion.setter
    def AclVersion(self, AclVersion):
        self._AclVersion = AclVersion


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        