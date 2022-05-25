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
        :param Name: 规则名
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板text（目前含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板text（目前含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制
        :type MaxFileDownSize: int
        :param AllowAnyAccount: 是否允许任意账号登陆
        :type AllowAnyAccount: bool
        :param UserSet: 关联的用户列表
        :type UserSet: list of User
        :param UserGroupSet: 关联的用户组列表
        :type UserGroupSet: list of Group
        :param DeviceSet: 关联的主机列表
        :type DeviceSet: list of Device
        :param DeviceGroupSet: 关联的主机组列表
        :type DeviceGroupSet: list of Group
        :param AccountSet: 关联的账号列表
        :type AccountSet: list of str
        :param CmdTemplateSet: 关联的高危命令模板列表
        :type CmdTemplateSet: list of CmdTemplate
        :param AllowDiskFileUp: 是否开启rdp磁盘映射文件上传
        :type AllowDiskFileUp: bool
        :param AllowDiskFileDown: 是否开启rdp磁盘映射文件下载
        :type AllowDiskFileDown: bool
        :param AllowShellFileUp: 是否开启rz sz文件上传
        :type AllowShellFileUp: bool
        :param AllowShellFileDown: 是否开启rz sz文件下载
        :type AllowShellFileDown: bool
        :param AllowFileDel: 是否开启SFTP文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 生效日期
        :type ValidateFrom: str
        :param ValidateTo: 失效日期
        :type ValidateTo: str
        :param Status: 策略状态，1-已生效，2-未生效，3-已过期
        :type Status: int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmdTemplate(AbstractModel):
    """命令模板

    """

    def __init__(self):
        r"""
        :param Id: 模板ID
        :type Id: int
        :param Name: 模板名称
        :type Name: str
        :param CmdList: 命令列表，\n分隔
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
        :param Name: 权限名称，最大32字符，不能为空，不能包含空白字符
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowAnyAccount: 是否允许任意账号登陆
        :type AllowAnyAccount: bool
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板text（含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板text（含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启SFTP文件上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启SFTP文件下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制
        :type MaxFileDownSize: int
        :param UserIdSet: 关联的用户ID
        :type UserIdSet: list of int non-negative
        :param UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param DeviceIdSet: 关联的主机ID
        :type DeviceIdSet: list of int non-negative
        :param DeviceGroupIdSet: 关联的主机组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param AccountSet: 关联的账号，账号name
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
        :param AllowFileDel: 是否开启SFTP文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 生效日期，如果为空，默认1970-01-01T08:00:01+08:00
        :type ValidateFrom: str
        :param ValidateTo: 失效日期，如果为空，默认1970-01-01T08:00:01+08:00
        :type ValidateTo: str
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
        :param Id: 访问权限ID
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
        :param UserName: 用户名，最大长度32字符，不能为空
        :type UserName: str
        :param RealName: 用户姓名，最大长度32字符，不能为空
        :type RealName: str
        :param Phone: 手机号
        :type Phone: str
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 生效起始时间,不设置则为1970-01-01T08:00:01+08:00
        :type ValidateFrom: str
        :param ValidateTo: 生效结束时间,不设置则为1970-01-01T08:00:01+08:00
        :type ValidateTo: str
        :param GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param AuthType: 认证方式，0-本地 1-ldap 2-oauth,不传则默认为0
        :type AuthType: int
        :param ValidateTime: 生效时间段, 0、1组成的字符串，长度168(7*24), 代表该用户的生效时间. 0 - 未生效，1 - 生效
        :type ValidateTime: str
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


class DescribeAclsRequest(AbstractModel):
    """DescribeAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 访问权限ID集合，非必需
        :type IdSet: list of int non-negative
        :param Name: 访问权限名称，模糊查询，最长64字符
        :type Name: str
        :param Offset: 分页，偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        :param Exact: 是否根据Name进行精确查询,默认值false
        :type Exact: bool
        :param AuthorizedUserIdSet: 有权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param AuthorizedDeviceIdSet: 有权限的主机ID集合
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param Status: 策略状态，0-不限，1-已生效，2-未生效，3-已过期
        :type Status: int
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.Exact = None
        self.AuthorizedUserIdSet = None
        self.AuthorizedDeviceIdSet = None
        self.Status = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Exact = params.get("Exact")
        self.AuthorizedUserIdSet = params.get("AuthorizedUserIdSet")
        self.AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self.Status = params.get("Status")
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
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param AclSet: 访问权限记录集合，当前分页
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


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdSet: 主机ID集合，非必需
        :type IdSet: list of int non-negative
        :param Name: 主机名或主机IP，模糊查询
        :type Name: str
        :param Ip: 暂未使用
        :type Ip: str
        :param ApCodeSet: 地域码集合
        :type ApCodeSet: list of str
        :param Kind: 操作系统类型
        :type Kind: int
        :param Offset: 分页，偏移位置
        :type Offset: int
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        :param AuthorizedUserIdSet: 有该主机访问权限的用户ID集合
        :type AuthorizedUserIdSet: list of int non-negative
        :param ResourceIdSet: 过滤条件，主机绑定的堡垒机服务ID集合
        :type ResourceIdSet: list of str
        :param KindSet: 可提供按照多种类型过滤, 1-Linux, 2-Windows, 3-MySQL
        :type KindSet: list of int non-negative
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
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param DeviceSet: 主机信息列表
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
        :param Limit: 每页条目数量，默认20
        :type Limit: int
        :param UserName: 精确查询，IdSet为空时才生效
        :type UserName: str
        :param Phone: 精确查询，IdSet、UserName为空时才生效
        :type Phone: str
        :param AuthorizedDeviceIdSet: 有访问权限的主机ID集合
        :type AuthorizedDeviceIdSet: list of int non-negative
        :param AuthTypeSet: 认证方式，0-本地，1-ldap, 2-oauth 不传为全部
        :type AuthTypeSet: list of int non-negative
        """
        self.IdSet = None
        self.Name = None
        self.Offset = None
        self.Limit = None
        self.UserName = None
        self.Phone = None
        self.AuthorizedDeviceIdSet = None
        self.AuthTypeSet = None


    def _deserialize(self, params):
        self.IdSet = params.get("IdSet")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UserName = params.get("UserName")
        self.Phone = params.get("Phone")
        self.AuthorizedDeviceIdSet = params.get("AuthorizedDeviceIdSet")
        self.AuthTypeSet = params.get("AuthTypeSet")
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
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param UserSet: 用户信息列表
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
    """主机信息

    """

    def __init__(self):
        r"""
        :param Id: 主机记录ID
        :type Id: int
        :param InstanceId: 主机ID，对应cvm实例id
        :type InstanceId: str
        :param Name: 主机名
        :type Name: str
        :param PublicIp: 公网IP
        :type PublicIp: str
        :param PrivateIp: 内网IP
        :type PrivateIp: str
        :param ApCode: 地域编码
        :type ApCode: str
        :param OsName: 操作系统名称
        :type OsName: str
        :param Kind: 主机类型，1-Linux, 2-Windows
        :type Kind: int
        :param Port: 管理端口
        :type Port: int
        :param GroupSet: 所属主机组信息列表
        :type GroupSet: list of Group
        :param AccountCount: 主机绑定的账号数
        :type AccountCount: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Resource: 堡垒机服务信息，注意没有绑定服务时为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.dasb.v20191018.models.Resource`
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
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
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
        :param Name: 权限名称，最大32字符，不能包含空白字符
        :type Name: str
        :param AllowDiskRedirect: 是否开启磁盘映射
        :type AllowDiskRedirect: bool
        :param AllowAnyAccount: 是否允许任意账号登陆
        :type AllowAnyAccount: bool
        :param Id: 访问权限ID
        :type Id: int
        :param AllowClipFileUp: 是否开启剪贴板文件上行
        :type AllowClipFileUp: bool
        :param AllowClipFileDown: 是否开启剪贴板文件下行
        :type AllowClipFileDown: bool
        :param AllowClipTextUp: 是否开启剪贴板text（含图片）上行
        :type AllowClipTextUp: bool
        :param AllowClipTextDown: 是否开启剪贴板text（含图片）下行
        :type AllowClipTextDown: bool
        :param AllowFileUp: 是否开启文件传输上传
        :type AllowFileUp: bool
        :param MaxFileUpSize: 文件传输上传大小限制
        :type MaxFileUpSize: int
        :param AllowFileDown: 是否开启文件传输下载
        :type AllowFileDown: bool
        :param MaxFileDownSize: 文件传输下载大小限制
        :type MaxFileDownSize: int
        :param UserIdSet: 关联的用户ID
        :type UserIdSet: list of int non-negative
        :param UserGroupIdSet: 关联的用户组ID
        :type UserGroupIdSet: list of int non-negative
        :param DeviceIdSet: 关联的主机ID
        :type DeviceIdSet: list of int non-negative
        :param DeviceGroupIdSet: 关联的主机组ID
        :type DeviceGroupIdSet: list of int non-negative
        :param AccountSet: 关联的账号，账号name
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
        :param AllowFileDel: 是否开启SFTP文件删除
        :type AllowFileDel: bool
        :param ValidateFrom: 生效日期，如果为空，默认1970-01-01T08:00:01+08:00
        :type ValidateFrom: str
        :param ValidateTo: 失效日期，如果为空，默认1970-01-01T08:00:01+08:00
        :type ValidateTo: str
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
        :param RealName: 用户姓名，最大长度32字符，不能为空
        :type RealName: str
        :param Phone: 手机号
        :type Phone: str
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 生效起始时间,不设置则为1970-01-01 08:00:01
        :type ValidateFrom: str
        :param ValidateTo: 生效结束时间,不设置则为1970-01-01 08:00:01
        :type ValidateTo: str
        :param GroupIdSet: 所属用户组ID集合
        :type GroupIdSet: list of int non-negative
        :param AuthType: 认证方式，0-本地 1-ldap, 2-oauth不传则默认为0
        :type AuthType: int
        :param ValidateTime: 生效时间段, 0、1组成的字符串，长度168(7*24), 代表该用户的生效时间. 0 - 未生效，1 - 生效
        :type ValidateTime: str
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
    """用户购买的堡垒机资源信息

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源实例id，如bh-saas-s3ed4r5e
        :type ResourceId: str
        :param ApCode: 地域编码
        :type ApCode: str
        :param SvArgs: 实例规格信息（询价参数）
        :type SvArgs: str
        :param VpcId: vpc id
        :type VpcId: str
        :param Nodes: 堡垒机规格对应的资产数
        :type Nodes: int
        :param RenewFlag: 自动续费标记，0表示默认状态，1表示自动续费，2表示明确不自动续费
        :type RenewFlag: int
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param Status: 资源状态，0未初始化，1正常，2隔离，3销毁，4初始化失败，5初始化中
        :type Status: int
        :param ResourceName: 实例名，如T-Sec-堡垒机（SaaS型）
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
        :param VpcName: 开通服务的VPC名称
        :type VpcName: str
        :param VpcCidrBlock: 开通服务的VPC对应的网段
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
        :param ModuleSet: 资源开通的高级功能列表，如:[DB]
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
        :param UserName: 用户名
        :type UserName: str
        :param RealName: 用户姓名
        :type RealName: str
        :param Phone: 手机号码
        :type Phone: str
        :param Id: 用户ID
        :type Id: int
        :param Email: 电子邮件
        :type Email: str
        :param ValidateFrom: 生效起始时间
        :type ValidateFrom: str
        :param ValidateTo: 生效结束时间
        :type ValidateTo: str
        :param GroupSet: 所属用户组列表
        :type GroupSet: list of Group
        :param AuthType: 认证方式，0-本地 1-ldap
        :type AuthType: int
        :param ValidateTime: 生效时间段, 0、1组成的字符串，长度168(7*24), 代表该用户的生效时间. 0 - 未生效，1 - 生效
        :type ValidateTime: str
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        