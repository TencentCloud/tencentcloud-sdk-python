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


class Account(AbstractModel):
    """帐号列表信息数据。

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一Uuid
        :type Uuid: str
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _Username: 帐号名。
        :type Username: str
        :param _Groups: 帐号所属组。
        :type Groups: str
        :param _Privilege: 帐号类型。
<li>ORDINARY：普通帐号</li>
<li>SUPPER：超级管理员帐号</li>
        :type Privilege: str
        :param _AccountCreateTime: 帐号创建时间。
        :type AccountCreateTime: str
        :param _LastLoginTime: 帐号最后登录时间。
        :type LastLoginTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Username = None
        self._Groups = None
        self._Privilege = None
        self._AccountCreateTime = None
        self._LastLoginTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def AccountCreateTime(self):
        return self._AccountCreateTime

    @AccountCreateTime.setter
    def AccountCreateTime(self, AccountCreateTime):
        self._AccountCreateTime = AccountCreateTime

    @property
    def LastLoginTime(self):
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Username = params.get("Username")
        self._Groups = params.get("Groups")
        self._Privilege = params.get("Privilege")
        self._AccountCreateTime = params.get("AccountCreateTime")
        self._LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountStatistics(AbstractModel):
    """帐号统计数据。

    """

    def __init__(self):
        r"""
        :param _Username: 用户名。
        :type Username: str
        :param _MachineNum: 主机数量。
        :type MachineNum: int
        """
        self._Username = None
        self._MachineNum = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListRequest(AbstractModel):
    """AddLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 白名单规则
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self._Rules = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = LoginWhiteListsRule()
            self._Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListResponse(AbstractModel):
    """AddLoginWhiteList返回参数结构体

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


class AddMachineTagRequest(AbstractModel):
    """AddMachineTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Quuid: 云服务器ID
        :type Quuid: str
        :param _TagId: 标签ID
        :type TagId: int
        :param _MRegion: 云服务器地区
        :type MRegion: str
        :param _MArea: 云服务器类型(CVM|BM)
        :type MArea: str
        """
        self._Quuid = None
        self._TagId = None
        self._MRegion = None
        self._MArea = None

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def MRegion(self):
        return self._MRegion

    @MRegion.setter
    def MRegion(self, MRegion):
        self._MRegion = MRegion

    @property
    def MArea(self):
        return self._MArea

    @MArea.setter
    def MArea(self, MArea):
        self._MArea = MArea


    def _deserialize(self, params):
        self._Quuid = params.get("Quuid")
        self._TagId = params.get("TagId")
        self._MRegion = params.get("MRegion")
        self._MArea = params.get("MArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineTagResponse(AbstractModel):
    """AddMachineTag返回参数结构体

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


class AgentVul(AbstractModel):
    """主机漏洞信息

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞ID。
        :type Id: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _VulName: 漏洞名称。
        :type VulName: str
        :param _VulLevel: 漏洞危害等级。
<li>HIGH：高危</li>
<li>MIDDLE：中危</li>
<li>LOW：低危</li>
<li>NOTICE：提示</li>
        :type VulLevel: str
        :param _LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        :param _Description: 漏洞描述。
        :type Description: str
        :param _VulId: 漏洞种类ID。
        :type VulId: int
        :param _VulStatus: 漏洞状态。
<li>UN_OPERATED : 待处理</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        """
        self._Id = None
        self._MachineIp = None
        self._VulName = None
        self._VulLevel = None
        self._LastScanTime = None
        self._Description = None
        self._VulId = None
        self._VulStatus = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def VulName(self):
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulStatus(self):
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._Description = params.get("Description")
        self._VulId = params.get("VulId")
        self._VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashEvent(AbstractModel):
    """高危命令数据

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _Uuid: 云镜ID
        :type Uuid: str
        :param _Quuid: 主机ID
        :type Quuid: str
        :param _Hostip: 主机内网IP
        :type Hostip: str
        :param _User: 执行用户名
        :type User: str
        :param _Platform: 平台类型
        :type Platform: int
        :param _BashCmd: 执行命令
        :type BashCmd: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleLevel: 规则等级
        :type RuleLevel: int
        :param _Status: 处理状态
        :type Status: int
        :param _CreateTime: 发生时间
        :type CreateTime: str
        :param _MachineName: 主机名
        :type MachineName: str
        """
        self._Id = None
        self._Uuid = None
        self._Quuid = None
        self._Hostip = None
        self._User = None
        self._Platform = None
        self._BashCmd = None
        self._RuleId = None
        self._RuleName = None
        self._RuleLevel = None
        self._Status = None
        self._CreateTime = None
        self._MachineName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def BashCmd(self):
        return self._BashCmd

    @BashCmd.setter
    def BashCmd(self, BashCmd):
        self._BashCmd = BashCmd

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleLevel(self):
        return self._RuleLevel

    @RuleLevel.setter
    def RuleLevel(self, RuleLevel):
        self._RuleLevel = RuleLevel

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        self._Hostip = params.get("Hostip")
        self._User = params.get("User")
        self._Platform = params.get("Platform")
        self._BashCmd = params.get("BashCmd")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleLevel = params.get("RuleLevel")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashRule(AbstractModel):
    """高危命令规则

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _Uuid: 客户端ID
        :type Uuid: str
        :param _Name: 规则名称
        :type Name: str
        :param _Level: 危险等级(1: 高危 2:中危 3: 低危)
        :type Level: int
        :param _Rule: 正则表达式
        :type Rule: str
        :param _Decription: 规则描述
        :type Decription: str
        :param _Operator: 操作人
        :type Operator: str
        :param _IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param _Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Hostip: 主机IP
        :type Hostip: str
        """
        self._Id = None
        self._Uuid = None
        self._Name = None
        self._Level = None
        self._Rule = None
        self._Decription = None
        self._Operator = None
        self._IsGlobal = None
        self._Status = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Hostip = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Decription(self):
        return self._Decription

    @Decription.setter
    def Decription(self, Decription):
        self._Decription = Decription

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Rule = params.get("Rule")
        self._Decription = params.get("Decription")
        self._Operator = params.get("Operator")
        self._IsGlobal = params.get("IsGlobal")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttack(AbstractModel):
    """暴力破解列表

    """

    def __init__(self):
        r"""
        :param _Id: 事件ID。
        :type Id: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _Status: 破解事件状态
<li>BRUTEATTACK_FAIL_ACCOUNT： 暴力破解事件-失败(存在帐号)  </li>
<li>BRUTEATTACK_FAIL_NOACCOUNT：暴力破解事件-失败(帐号不存在)</li>
<li>BRUTEATTACK_SUCCESS：暴力破解事件-成功</li>
        :type Status: str
        :param _UserName: 用户名称。
        :type UserName: str
        :param _City: 城市ID。
        :type City: int
        :param _Country: 国家ID。
        :type Country: int
        :param _Province: 省份ID。
        :type Province: int
        :param _SrcIp: 来源IP。
        :type SrcIp: str
        :param _Count: 尝试破解次数。
        :type Count: int
        :param _CreateTime: 发生时间。
        :type CreateTime: str
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param _IsProVersion: 是否专业版。
        :type IsProVersion: bool
        :param _BanStatus: 阻断状态。
        :type BanStatus: str
        :param _Quuid: 机器UUID
        :type Quuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._UserName = None
        self._City = None
        self._Country = None
        self._Province = None
        self._SrcIp = None
        self._Count = None
        self._CreateTime = None
        self._MachineName = None
        self._Uuid = None
        self._IsProVersion = None
        self._BanStatus = None
        self._Quuid = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def IsProVersion(self):
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def BanStatus(self):
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._SrcIp = params.get("SrcIp")
        self._Count = params.get("Count")
        self._CreateTime = params.get("CreateTime")
        self._MachineName = params.get("MachineName")
        self._Uuid = params.get("Uuid")
        self._IsProVersion = params.get("IsProVersion")
        self._BanStatus = params.get("BanStatus")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargePrepaid(AbstractModel):
    """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self._Quuid = None

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion返回参数结构体

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


class Component(AbstractModel):
    """组件列表数据。

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _MachineName: 主机名。
        :type MachineName: str
        :param _ComponentVersion: 组件版本号。
        :type ComponentVersion: str
        :param _ComponentType: 组件类型。
<li>SYSTEM：系统组件</li>
<li>WEB：Web组件</li>
        :type ComponentType: str
        :param _ComponentName: 组件名称。
        :type ComponentName: str
        :param _ModifyTime: 组件检测更新时间。
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._ComponentVersion = None
        self._ComponentType = None
        self._ComponentName = None
        self._ModifyTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def ComponentVersion(self):
        return self._ComponentVersion

    @ComponentVersion.setter
    def ComponentVersion(self, ComponentVersion):
        self._ComponentVersion = ComponentVersion

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._ComponentVersion = params.get("ComponentVersion")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentStatistics(AbstractModel):
    """组件统计数据。

    """

    def __init__(self):
        r"""
        :param _Id: 组件ID。
        :type Id: int
        :param _MachineNum: 主机数量。
        :type MachineNum: int
        :param _ComponentName: 组件名称。
        :type ComponentName: str
        :param _ComponentType: 组件类型。
<li>WEB：Web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param _Description: 组件描述。
        :type Description: str
        """
        self._Id = None
        self._MachineNum = None
        self._ComponentName = None
        self._ComponentType = None
        self._Description = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineNum = params.get("MachineNum")
        self._ComponentName = params.get("ComponentName")
        self._ComponentType = params.get("ComponentType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyRequest(AbstractModel):
    """CreateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyName: 策略名称
        :type StrategyName: str
        :param _ScanCycle: 检测周期, 表示每隔多少天进行检测.示例: 2, 表示每2天进行检测一次.
        :type ScanCycle: int
        :param _ScanAt: 定期检测时间，该时间下发扫描. 示例:“22:00”, 表示在22:00下发检测
        :type ScanAt: str
        :param _CategoryIds: 该策略下选择的基线id数组. 示例: [1,3,5,7]
        :type CategoryIds: list of int non-negative
        :param _IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param _MachineType: 云主机类型：“CVM”：虚拟主机，"BMS"：裸金属，"ECM"：边缘计算主机
        :type MachineType: str
        :param _RegionCode: 主机地域. 示例: "ap-bj"
        :type RegionCode: str
        :param _Quuids: 主机id数组. 示例: ["quuid1","quuid2"]
        :type Quuids: list of str
        """
        self._StrategyName = None
        self._ScanCycle = None
        self._ScanAt = None
        self._CategoryIds = None
        self._IsGlobal = None
        self._MachineType = None
        self._RegionCode = None
        self._Quuids = None

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def ScanCycle(self):
        return self._ScanCycle

    @ScanCycle.setter
    def ScanCycle(self, ScanCycle):
        self._ScanCycle = ScanCycle

    @property
    def ScanAt(self):
        return self._ScanAt

    @ScanAt.setter
    def ScanAt(self, ScanAt):
        self._ScanAt = ScanAt

    @property
    def CategoryIds(self):
        return self._CategoryIds

    @CategoryIds.setter
    def CategoryIds(self, CategoryIds):
        self._CategoryIds = CategoryIds

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def RegionCode(self):
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def Quuids(self):
        return self._Quuids

    @Quuids.setter
    def Quuids(self, Quuids):
        self._Quuids = Quuids


    def _deserialize(self, params):
        self._StrategyName = params.get("StrategyName")
        self._ScanCycle = params.get("ScanCycle")
        self._ScanAt = params.get("ScanAt")
        self._CategoryIds = params.get("CategoryIds")
        self._IsGlobal = params.get("IsGlobal")
        self._MachineType = params.get("MachineType")
        self._RegionCode = params.get("RegionCode")
        self._Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyResponse(AbstractModel):
    """CreateBaselineStrategy返回参数结构体

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


class CreateOpenPortTaskRequest(AbstractModel):
    """CreateOpenPortTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenPortTaskResponse(AbstractModel):
    """CreateOpenPortTask返回参数结构体

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


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask返回参数结构体

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


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuids: 云镜客户端UUID数组。
        :type Uuids: list of str
        :param _Places: 登录地域信息数组。
        :type Places: list of Place
        """
        self._Uuids = None
        self._Places = None

    @property
    def Uuids(self):
        return self._Uuids

    @Uuids.setter
    def Uuids(self, Uuids):
        self._Uuids = Uuids

    @property
    def Places(self):
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places


    def _deserialize(self, params):
        self._Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces返回参数结构体

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


class DefendAttackLog(AbstractModel):
    """网络攻击日志

    """

    def __init__(self):
        r"""
        :param _Id: 日志ID
        :type Id: int
        :param _Uuid: 客户端ID
        :type Uuid: str
        :param _SrcIp: 来源IP
        :type SrcIp: str
        :param _SrcPort: 来源端口
        :type SrcPort: int
        :param _HttpMethod: 攻击方式
        :type HttpMethod: str
        :param _HttpCgi: 攻击描述
        :type HttpCgi: str
        :param _HttpParam: 攻击参数
        :type HttpParam: str
        :param _VulType: 威胁类型
        :type VulType: str
        :param _CreatedAt: 攻击时间
        :type CreatedAt: str
        :param _MachineIp: 目标服务器IP
        :type MachineIp: str
        :param _MachineName: 目标服务器名称
        :type MachineName: str
        :param _DstIp: 目标IP
        :type DstIp: str
        :param _DstPort: 目标端口
        :type DstPort: int
        :param _HttpContent: 攻击内容
        :type HttpContent: str
        """
        self._Id = None
        self._Uuid = None
        self._SrcIp = None
        self._SrcPort = None
        self._HttpMethod = None
        self._HttpCgi = None
        self._HttpParam = None
        self._VulType = None
        self._CreatedAt = None
        self._MachineIp = None
        self._MachineName = None
        self._DstIp = None
        self._DstPort = None
        self._HttpContent = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def SrcPort(self):
        return self._SrcPort

    @SrcPort.setter
    def SrcPort(self, SrcPort):
        self._SrcPort = SrcPort

    @property
    def HttpMethod(self):
        return self._HttpMethod

    @HttpMethod.setter
    def HttpMethod(self, HttpMethod):
        self._HttpMethod = HttpMethod

    @property
    def HttpCgi(self):
        return self._HttpCgi

    @HttpCgi.setter
    def HttpCgi(self, HttpCgi):
        self._HttpCgi = HttpCgi

    @property
    def HttpParam(self):
        return self._HttpParam

    @HttpParam.setter
    def HttpParam(self, HttpParam):
        self._HttpParam = HttpParam

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def HttpContent(self):
        return self._HttpContent

    @HttpContent.setter
    def HttpContent(self, HttpContent):
        self._HttpContent = HttpContent


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._SrcIp = params.get("SrcIp")
        self._SrcPort = params.get("SrcPort")
        self._HttpMethod = params.get("HttpMethod")
        self._HttpCgi = params.get("HttpCgi")
        self._HttpParam = params.get("HttpParam")
        self._VulType = params.get("VulType")
        self._CreatedAt = params.get("CreatedAt")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._HttpContent = params.get("HttpContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsRequest(AbstractModel):
    """DeleteAttackLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 日志ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsResponse(AbstractModel):
    """DeleteAttackLogs返回参数结构体

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


class DeleteBashEventsRequest(AbstractModel):
    """DeleteBashEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashEventsResponse(AbstractModel):
    """DeleteBashEvents返回参数结构体

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


class DeleteBashRulesRequest(AbstractModel):
    """DeleteBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashRulesResponse(AbstractModel):
    """DeleteBashRules返回参数结构体

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


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 暴力破解事件Id数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回参数结构体

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


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 白名单ID
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList返回参数结构体

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


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

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


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rid: 关联的标签ID
        :type Rid: int
        """
        self._Rid = None

    @property
    def Rid(self):
        return self._Rid

    @Rid.setter
    def Rid(self, Rid):
        self._Rid = Rid


    def _deserialize(self, params):
        self._Rid = params.get("Rid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag返回参数结构体

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


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 恶意请求记录ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests返回参数结构体

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


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 木马记录ID数组
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回参数结构体

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


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 异地登录事件ID数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回参数结构体

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


class DeletePrivilegeEventsRequest(AbstractModel):
    """DeletePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeEventsResponse(AbstractModel):
    """DeletePrivilegeEvents返回参数结构体

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


class DeletePrivilegeRulesRequest(AbstractModel):
    """DeletePrivilegeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeRulesResponse(AbstractModel):
    """DeletePrivilegeRules返回参数结构体

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


class DeleteReverseShellEventsRequest(AbstractModel):
    """DeleteReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellEventsResponse(AbstractModel):
    """DeleteReverseShellEvents返回参数结构体

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


class DeleteReverseShellRulesRequest(AbstractModel):
    """DeleteReverseShellRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellRulesResponse(AbstractModel):
    """DeleteReverseShellRules返回参数结构体

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


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 标签ID
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

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


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端Uuid
        :type Uuid: str
        :param _CityIds: 已添加常用登录地城市ID数组
        :type CityIds: list of int non-negative
        """
        self._Uuid = None
        self._CityIds = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def CityIds(self):
        return self._CityIds

    @CityIds.setter
    def CityIds(self, CityIds):
        self._CityIds = CityIds


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._CityIds = params.get("CityIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces返回参数结构体

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


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号用户名</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 帐号统计列表记录总数。
        :type TotalCount: int
        :param _AccountStatistics: 帐号统计列表。
        :type AccountStatistics: list of AccountStatistics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountStatistics(self):
        return self._AccountStatistics

    @AccountStatistics.setter
    def AccountStatistics(self, AccountStatistics):
        self._AccountStatistics = AccountStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self._AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self._AccountStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查询该主机下列表信息。
        :type Uuid: str
        :param _Username: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Username表示，查询该用户名下列表信息。
        :type Username: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
<li>Privilege - String - 是否必填：否 - 帐号类型（ORDINARY: 普通帐号 | SUPPER: 超级管理员帐号）</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Username = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Username = params.get("Username")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 帐号列表记录总数。
        :type TotalCount: int
        :param _Accounts: 帐号数据列表。
        :type Accounts: list of Account
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VulType: 漏洞类型。
<li>WEB: Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param _Uuid: 客户端UUID。
        :type Uuid: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）
        :type Filters: list of Filter
        """
        self._VulType = None
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulType = params.get("VulType")
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _AgentVuls: 主机漏洞信息
        :type AgentVuls: list of AgentVul
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentVuls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentVuls(self):
        return self._AgentVuls

    @AgentVuls.setter
    def AgentVuls(self, AgentVuls):
        self._AgentVuls = AgentVuls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self._AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self._AgentVuls.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute请求参数结构体

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offline: 防护软件离线告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Offline: str
        :param _Malware: 发现木马告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type Malware: str
        :param _NonlocalLogin: 发现异地登录告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type NonlocalLogin: str
        :param _CrackSuccess: 被暴力破解成功告警状态：
<li>OPEN：告警已开启</li>
<li>CLOSE： 告警已关闭</li>
        :type CrackSuccess: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offline = None
        self._Malware = None
        self._NonlocalLogin = None
        self._CrackSuccess = None
        self._RequestId = None

    @property
    def Offline(self):
        return self._Offline

    @Offline.setter
    def Offline(self, Offline):
        self._Offline = Offline

    @property
    def Malware(self):
        return self._Malware

    @Malware.setter
    def Malware(self, Malware):
        self._Malware = Malware

    @property
    def NonlocalLogin(self):
        return self._NonlocalLogin

    @NonlocalLogin.setter
    def NonlocalLogin(self, NonlocalLogin):
        self._NonlocalLogin = NonlocalLogin

    @property
    def CrackSuccess(self):
        return self._CrackSuccess

    @CrackSuccess.setter
    def CrackSuccess(self, CrackSuccess):
        self._CrackSuccess = CrackSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offline = params.get("Offline")
        self._Malware = params.get("Malware")
        self._NonlocalLogin = params.get("NonlocalLogin")
        self._CrackSuccess = params.get("CrackSuccess")
        self._RequestId = params.get("RequestId")


class DescribeAttackLogInfoRequest(AbstractModel):
    """DescribeAttackLogInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 日志ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
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
        


class DescribeAttackLogInfoResponse(AbstractModel):
    """DescribeAttackLogInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 日志ID
        :type Id: int
        :param _Quuid: 主机ID
        :type Quuid: str
        :param _SrcPort: 攻击来源端口
        :type SrcPort: int
        :param _SrcIp: 攻击来源IP
        :type SrcIp: str
        :param _DstPort: 攻击目标端口
        :type DstPort: int
        :param _DstIp: 攻击目标IP
        :type DstIp: str
        :param _HttpMethod: 攻击方法
        :type HttpMethod: str
        :param _HttpHost: 攻击目标主机
        :type HttpHost: str
        :param _HttpHead: 攻击头信息
        :type HttpHead: str
        :param _HttpUserAgent: 攻击者浏览器标识
        :type HttpUserAgent: str
        :param _HttpReferer: 请求源
        :type HttpReferer: str
        :param _VulType: 威胁类型
        :type VulType: str
        :param _HttpCgi: 攻击路径
        :type HttpCgi: str
        :param _HttpParam: 攻击参数
        :type HttpParam: str
        :param _CreatedAt: 攻击时间
        :type CreatedAt: str
        :param _HttpContent: 攻击内容
        :type HttpContent: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._Quuid = None
        self._SrcPort = None
        self._SrcIp = None
        self._DstPort = None
        self._DstIp = None
        self._HttpMethod = None
        self._HttpHost = None
        self._HttpHead = None
        self._HttpUserAgent = None
        self._HttpReferer = None
        self._VulType = None
        self._HttpCgi = None
        self._HttpParam = None
        self._CreatedAt = None
        self._HttpContent = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def SrcPort(self):
        return self._SrcPort

    @SrcPort.setter
    def SrcPort(self, SrcPort):
        self._SrcPort = SrcPort

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def HttpMethod(self):
        return self._HttpMethod

    @HttpMethod.setter
    def HttpMethod(self, HttpMethod):
        self._HttpMethod = HttpMethod

    @property
    def HttpHost(self):
        return self._HttpHost

    @HttpHost.setter
    def HttpHost(self, HttpHost):
        self._HttpHost = HttpHost

    @property
    def HttpHead(self):
        return self._HttpHead

    @HttpHead.setter
    def HttpHead(self, HttpHead):
        self._HttpHead = HttpHead

    @property
    def HttpUserAgent(self):
        return self._HttpUserAgent

    @HttpUserAgent.setter
    def HttpUserAgent(self, HttpUserAgent):
        self._HttpUserAgent = HttpUserAgent

    @property
    def HttpReferer(self):
        return self._HttpReferer

    @HttpReferer.setter
    def HttpReferer(self, HttpReferer):
        self._HttpReferer = HttpReferer

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def HttpCgi(self):
        return self._HttpCgi

    @HttpCgi.setter
    def HttpCgi(self, HttpCgi):
        self._HttpCgi = HttpCgi

    @property
    def HttpParam(self):
        return self._HttpParam

    @HttpParam.setter
    def HttpParam(self, HttpParam):
        self._HttpParam = HttpParam

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def HttpContent(self):
        return self._HttpContent

    @HttpContent.setter
    def HttpContent(self, HttpContent):
        self._HttpContent = HttpContent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Quuid = params.get("Quuid")
        self._SrcPort = params.get("SrcPort")
        self._SrcIp = params.get("SrcIp")
        self._DstPort = params.get("DstPort")
        self._DstIp = params.get("DstIp")
        self._HttpMethod = params.get("HttpMethod")
        self._HttpHost = params.get("HttpHost")
        self._HttpHead = params.get("HttpHead")
        self._HttpUserAgent = params.get("HttpUserAgent")
        self._HttpReferer = params.get("HttpReferer")
        self._VulType = params.get("VulType")
        self._HttpCgi = params.get("HttpCgi")
        self._HttpParam = params.get("HttpParam")
        self._CreatedAt = params.get("CreatedAt")
        self._HttpContent = params.get("HttpContent")
        self._RequestId = params.get("RequestId")


class DescribeAttackLogsRequest(AbstractModel):
    """DescribeAttackLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
        :type Filters: list of Filter
        :param _Uuid: 主机安全客户端ID
        :type Uuid: str
        :param _Quuid: 云主机机器ID
        :type Quuid: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Uuid = None
        self._Quuid = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackLogsResponse(AbstractModel):
    """DescribeAttackLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttackLogs: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackLogs: list of DefendAttackLog
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttackLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AttackLogs(self):
        return self._AttackLogs

    @AttackLogs.setter
    def AttackLogs(self, AttackLogs):
        self._AttackLogs = AttackLogs

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
        if params.get("AttackLogs") is not None:
            self._AttackLogs = []
            for item in params.get("AttackLogs"):
                obj = DefendAttackLog()
                obj._deserialize(item)
                self._AttackLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBashEventsRequest(AbstractModel):
    """DescribeBashEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机内网IP)</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeBashEventsResponse(AbstractModel):
    """DescribeBashEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _List: 高危命令事件列表
        :type List: list of BashEvent
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = BashEvent()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBashRulesRequest(AbstractModel):
    """DescribeBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 0-系统规则; 1-用户规则
        :type Type: int
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(规则名称)</li>
        :type Filters: list of Filter
        """
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeBashRulesResponse(AbstractModel):
    """DescribeBashRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表内容
        :type List: list of BashRule
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = BashRule()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  查询状态（FAILED：破解失败 |SUCCESS：破解成功）</li>
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self._Uuid = None
        self._Offset = None
        self._Filters = None
        self._Limit = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 事件数量
        :type TotalCount: int
        :param _BruteAttacks: 暴力破解事件列表
        :type BruteAttacks: list of BruteAttack
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BruteAttacks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BruteAttacks(self):
        return self._BruteAttacks

    @BruteAttacks.setter
    def BruteAttacks(self, BruteAttacks):
        self._BruteAttacks = BruteAttacks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self._BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self._BruteAttacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ComponentId: 组件ID。
        :type ComponentId: int
        """
        self._ComponentId = None

    @property
    def ComponentId(self):
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 组件ID。
        :type Id: int
        :param _ComponentName: 组件名称。
        :type ComponentName: str
        :param _ComponentType: 组件类型。
<li>WEB：web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param _Homepage: 组件官网。
        :type Homepage: str
        :param _Description: 组件描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._ComponentName = None
        self._ComponentType = None
        self._Homepage = None
        self._Description = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def Homepage(self):
        return self._Homepage

    @Homepage.setter
    def Homepage(self, Homepage):
        self._Homepage = Homepage

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
        self._Id = params.get("Id")
        self._ComponentName = params.get("ComponentName")
        self._ComponentType = params.get("ComponentType")
        self._Homepage = params.get("Homepage")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
ComponentName - String - 是否必填：否 - 组件名称
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 组件统计列表记录总数。
        :type TotalCount: int
        :param _ComponentStatistics: 组件统计列表数据数组。
        :type ComponentStatistics: list of ComponentStatistics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ComponentStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ComponentStatistics(self):
        return self._ComponentStatistics

    @ComponentStatistics.setter
    def ComponentStatistics(self, ComponentStatistics):
        self._ComponentStatistics = ComponentStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self._ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self._ComponentStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。Uuid和ComponentId必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param _ComponentId: 组件ID。Uuid和ComponentId必填其一，使用ComponentId表示，查询该组件列表信息。
        :type ComponentId: int
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>ComponentVersion - String - 是否必填：否 - 组件版本号</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._ComponentId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ComponentId(self):
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._ComponentId = params.get("ComponentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 组件列表记录总数。
        :type TotalCount: int
        :param _Components: 组件列表数据。
        :type Components: list of Component
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Components = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 帐号变更历史列表记录总数。
        :type TotalCount: int
        :param _HistoryAccounts: 帐号变更历史数据数组。
        :type HistoryAccounts: list of HistoryAccount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HistoryAccounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistoryAccounts(self):
        return self._HistoryAccounts

    @HistoryAccounts.setter
    def HistoryAccounts(self, HistoryAccounts):
        self._HistoryAccounts = HistoryAccounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self._HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self._HistoryAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VulId: 漏洞种类ID。
        :type VulId: int
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED：待处理 | FIXED：已修复）</li>
        :type Filters: list of Filter
        """
        self._VulId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _ImpactedHosts: 漏洞影响机器列表数组
        :type ImpactedHosts: list of ImpactedHost
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImpactedHosts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImpactedHosts(self):
        return self._ImpactedHosts

    @ImpactedHosts.setter
    def ImpactedHosts(self, ImpactedHosts):
        self._ImpactedHosts = ImpactedHosts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self._ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self._ImpactedHosts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数
        :type TotalCount: int
        :param _LoginWhiteLists: 异地登录白名单数组
        :type LoginWhiteLists: list of LoginWhiteLists
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoginWhiteLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoginWhiteLists(self):
        return self._LoginWhiteLists

    @LoginWhiteLists.setter
    def LoginWhiteLists(self, LoginWhiteLists):
        self._LoginWhiteLists = LoginWhiteLists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self._LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self._LoginWhiteLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineIp: 机器ip。
        :type MachineIp: str
        :param _ProtectDays: 受云镜保护天数。
        :type ProtectDays: int
        :param _MachineOs: 操作系统。
        :type MachineOs: str
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _MachineStatus: 在线状态。
<li>ONLINE： 在线</li>
<li>OFFLINE：离线</li>
        :type MachineStatus: str
        :param _InstanceId: CVM或BM主机唯一标识。
        :type InstanceId: str
        :param _MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param _Quuid: CVM或BM主机唯一Uuid。
        :type Quuid: str
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param _IsProVersion: 是否开通专业版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param _ProVersionOpenDate: 专业版开通时间。
        :type ProVersionOpenDate: str
        :param _MachineType: 云主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param _MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param _PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param _FreeMalwaresLeft: 免费木马剩余检测数量。
        :type FreeMalwaresLeft: int
        :param _FreeVulsLeft: 免费漏洞剩余检测数量。
        :type FreeVulsLeft: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MachineIp = None
        self._ProtectDays = None
        self._MachineOs = None
        self._MachineName = None
        self._MachineStatus = None
        self._InstanceId = None
        self._MachineWanIp = None
        self._Quuid = None
        self._Uuid = None
        self._IsProVersion = None
        self._ProVersionOpenDate = None
        self._MachineType = None
        self._MachineRegion = None
        self._PayMode = None
        self._FreeMalwaresLeft = None
        self._FreeVulsLeft = None
        self._RequestId = None

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def ProtectDays(self):
        return self._ProtectDays

    @ProtectDays.setter
    def ProtectDays(self, ProtectDays):
        self._ProtectDays = ProtectDays

    @property
    def MachineOs(self):
        return self._MachineOs

    @MachineOs.setter
    def MachineOs(self, MachineOs):
        self._MachineOs = MachineOs

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineStatus(self):
        return self._MachineStatus

    @MachineStatus.setter
    def MachineStatus(self, MachineStatus):
        self._MachineStatus = MachineStatus

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MachineWanIp(self):
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def IsProVersion(self):
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def ProVersionOpenDate(self):
        return self._ProVersionOpenDate

    @ProVersionOpenDate.setter
    def ProVersionOpenDate(self, ProVersionOpenDate):
        self._ProVersionOpenDate = ProVersionOpenDate

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def FreeMalwaresLeft(self):
        return self._FreeMalwaresLeft

    @FreeMalwaresLeft.setter
    def FreeMalwaresLeft(self, FreeMalwaresLeft):
        self._FreeMalwaresLeft = FreeMalwaresLeft

    @property
    def FreeVulsLeft(self):
        return self._FreeVulsLeft

    @FreeVulsLeft.setter
    def FreeVulsLeft(self, FreeVulsLeft):
        self._FreeVulsLeft = FreeVulsLeft

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._ProtectDays = params.get("ProtectDays")
        self._MachineOs = params.get("MachineOs")
        self._MachineName = params.get("MachineName")
        self._MachineStatus = params.get("MachineStatus")
        self._InstanceId = params.get("InstanceId")
        self._MachineWanIp = params.get("MachineWanIp")
        self._Quuid = params.get("Quuid")
        self._Uuid = params.get("Uuid")
        self._IsProVersion = params.get("IsProVersion")
        self._ProVersionOpenDate = params.get("ProVersionOpenDate")
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._PayMode = params.get("PayMode")
        self._FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self._FreeVulsLeft = params.get("FreeVulsLeft")
        self._RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param _MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        """
        self._MachineType = None
        self._MachineRegion = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Machines: 主机列表
        :type Machines: list of Machine
        :param _TotalCount: 主机数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Machines = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Machines(self):
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines

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
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self._Machines.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMaliciousRequestsRequest(AbstractModel):
    """DescribeMaliciousRequests请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | TRUSTED：已信任 | UN_TRUSTED：已取消信任）</li>
<li>Domain - String - 是否必填：否 - 恶意请求的域名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        :param _Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Uuid = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _MaliciousRequests: 恶意请求记录数组。
        :type MaliciousRequests: list of MaliciousRequest
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MaliciousRequests = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MaliciousRequests(self):
        return self._MaliciousRequests

    @MaliciousRequests.setter
    def MaliciousRequests(self, MaliciousRequests):
        self._MaliciousRequests = MaliciousRequests

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MaliciousRequests") is not None:
            self._MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = MaliciousRequest()
                obj._deserialize(item)
                self._MaliciousRequests.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 木马状态（UN_OPERATED: 未处理 | SEGREGATED: 已隔离|TRUSTED：信任）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询。
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 木马总数。
        :type TotalCount: int
        :param _Malwares: Malware数组。
        :type Malwares: list of Malware
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Malwares = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Malwares(self):
        return self._Malwares

    @Malwares.setter
    def Malwares(self, Malwares):
        self._Malwares = Malwares

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self._Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self._Malwares.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 客户端唯一Uuid。
        :type Uuid: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 -  查询关键字</li>
<li>Status - String - 是否必填：否 -  登录状态（NON_LOCAL_LOGIN: 异地登录 | NORMAL_LOGIN : 正常登录）</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _NonLocalLoginPlaces: 异地登录信息数组。
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NonLocalLoginPlaces = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NonLocalLoginPlaces(self):
        return self._NonLocalLoginPlaces

    @NonLocalLoginPlaces.setter
    def NonLocalLoginPlaces(self, NonLocalLoginPlaces):
        self._NonLocalLoginPlaces = NonLocalLoginPlaces

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self._NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self._NonLocalLoginPlaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 端口统计列表总数
        :type TotalCount: int
        :param _OpenPortStatistics: 端口统计数据列表
        :type OpenPortStatistics: list of OpenPortStatistics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._OpenPortStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OpenPortStatistics(self):
        return self._OpenPortStatistics

    @OpenPortStatistics.setter
    def OpenPortStatistics(self, OpenPortStatistics):
        self._OpenPortStatistics = OpenPortStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self._OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self._OpenPortStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOpenPortTaskStatusRequest(AbstractModel):
    """DescribeOpenPortTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortTaskStatusResponse(AbstractModel):
    """DescribeOpenPortTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
<li>COMPLETE：完成（此时可以调用DescribeOpenPorts接口获取实时进程列表）</li>
<li>AGENT_OFFLINE：云镜客户端离线</li>
<li>COLLECTING：端口获取中</li>
<li>FAILED：进程获取失败</li>
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。Port和Uuid必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param _Port: 开放端口号。Port和Uuid必填其一，使用Port表示查询该端口的列表信息。
        :type Port: int
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Port = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Port = params.get("Port")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 端口列表记录总数。
        :type TotalCount: int
        :param _OpenPorts: 端口列表。
        :type OpenPorts: list of OpenPort
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._OpenPorts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OpenPorts(self):
        return self._OpenPorts

    @OpenPorts.setter
    def OpenPorts(self, OpenPorts):
        self._OpenPorts = OpenPorts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self._OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self._OpenPorts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics请求参数结构体

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineMachineNum: 服务器在线数。
        :type OnlineMachineNum: int
        :param _ProVersionMachineNum: 专业服务器数。
        :type ProVersionMachineNum: int
        :param _MalwareNum: 木马文件数。
        :type MalwareNum: int
        :param _NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param _BruteAttackSuccessNum: 暴力破解成功数。
        :type BruteAttackSuccessNum: int
        :param _VulNum: 漏洞数。
        :type VulNum: int
        :param _BaseLineNum: 安全基线数。
        :type BaseLineNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OnlineMachineNum = None
        self._ProVersionMachineNum = None
        self._MalwareNum = None
        self._NonlocalLoginNum = None
        self._BruteAttackSuccessNum = None
        self._VulNum = None
        self._BaseLineNum = None
        self._RequestId = None

    @property
    def OnlineMachineNum(self):
        return self._OnlineMachineNum

    @OnlineMachineNum.setter
    def OnlineMachineNum(self, OnlineMachineNum):
        self._OnlineMachineNum = OnlineMachineNum

    @property
    def ProVersionMachineNum(self):
        return self._ProVersionMachineNum

    @ProVersionMachineNum.setter
    def ProVersionMachineNum(self, ProVersionMachineNum):
        self._ProVersionMachineNum = ProVersionMachineNum

    @property
    def MalwareNum(self):
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def NonlocalLoginNum(self):
        return self._NonlocalLoginNum

    @NonlocalLoginNum.setter
    def NonlocalLoginNum(self, NonlocalLoginNum):
        self._NonlocalLoginNum = NonlocalLoginNum

    @property
    def BruteAttackSuccessNum(self):
        return self._BruteAttackSuccessNum

    @BruteAttackSuccessNum.setter
    def BruteAttackSuccessNum(self, BruteAttackSuccessNum):
        self._BruteAttackSuccessNum = BruteAttackSuccessNum

    @property
    def VulNum(self):
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def BaseLineNum(self):
        return self._BaseLineNum

    @BaseLineNum.setter
    def BaseLineNum(self, BaseLineNum):
        self._BaseLineNum = BaseLineNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OnlineMachineNum = params.get("OnlineMachineNum")
        self._ProVersionMachineNum = params.get("ProVersionMachineNum")
        self._MalwareNum = params.get("MalwareNum")
        self._NonlocalLoginNum = params.get("NonlocalLoginNum")
        self._BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self._VulNum = params.get("VulNum")
        self._BaseLineNum = params.get("BaseLineNum")
        self._RequestId = params.get("RequestId")


class DescribePrivilegeEventsRequest(AbstractModel):
    """DescribePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机IP)</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribePrivilegeEventsResponse(AbstractModel):
    """DescribePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 数据列表
        :type List: list of PrivilegeEscalationProcess
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PrivilegeEscalationProcess()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrivilegeRulesRequest(AbstractModel):
    """DescribePrivilegeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribePrivilegeRulesResponse(AbstractModel):
    """DescribePrivilegeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表内容
        :type List: list of PrivilegeRule
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = PrivilegeRule()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PostPayCost: 后付费昨日扣费
        :type PostPayCost: int
        :param _IsAutoOpenProVersion: 新增主机是否自动开通专业版
        :type IsAutoOpenProVersion: bool
        :param _ProVersionNum: 开通专业版主机数
        :type ProVersionNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PostPayCost = None
        self._IsAutoOpenProVersion = None
        self._ProVersionNum = None
        self._RequestId = None

    @property
    def PostPayCost(self):
        return self._PostPayCost

    @PostPayCost.setter
    def PostPayCost(self, PostPayCost):
        self._PostPayCost = PostPayCost

    @property
    def IsAutoOpenProVersion(self):
        return self._IsAutoOpenProVersion

    @IsAutoOpenProVersion.setter
    def IsAutoOpenProVersion(self, IsAutoOpenProVersion):
        self._IsAutoOpenProVersion = IsAutoOpenProVersion

    @property
    def ProVersionNum(self):
        return self._ProVersionNum

    @ProVersionNum.setter
    def ProVersionNum(self, ProVersionNum):
        self._ProVersionNum = ProVersionNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PostPayCost = params.get("PostPayCost")
        self._IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self._ProVersionNum = params.get("ProVersionNum")
        self._RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 进程统计列表记录总数。
        :type TotalCount: int
        :param _ProcessStatistics: 进程统计列表数据数组。
        :type ProcessStatistics: list of ProcessStatistics
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProcessStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProcessStatistics(self):
        return self._ProcessStatistics

    @ProcessStatistics.setter
    def ProcessStatistics(self, ProcessStatistics):
        self._ProcessStatistics = ProcessStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self._ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self._ProcessStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
<li>COMPLETE：完成（此时可以调用DescribeProcesses接口获取实时进程列表）</li>
<li>AGENT_OFFLINE：云镜客户端离线</li>
<li>COLLECTING：进程获取中</li>
<li>FAILED：进程获取失败</li>
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端唯一Uuid。Uuid和ProcessName必填其一，使用Uuid表示，查询该主机列表信息。
        :type Uuid: str
        :param _ProcessName: 进程名。Uuid和ProcessName必填其一，使用ProcessName表示，查询该进程列表信息。
        :type ProcessName: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._ProcessName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._ProcessName = params.get("ProcessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 进程列表记录总数。
        :type TotalCount: int
        :param _Processes: 进程列表数据数组。
        :type Processes: list of Process
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Processes = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Processes(self):
        return self._Processes

    @Processes.setter
    def Processes(self, Processes):
        self._Processes = Processes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self._Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self._Processes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReverseShellEventsRequest(AbstractModel):
    """DescribeReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(主机内网IP|进程名)</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeReverseShellEventsResponse(AbstractModel):
    """DescribeReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表内容
        :type List: list of ReverseShell
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReverseShell()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeReverseShellRulesRequest(AbstractModel):
    """DescribeReverseShellRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeReverseShellRulesResponse(AbstractModel):
    """DescribeReverseShellRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表内容
        :type List: list of ReverseShellRule
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReverseShellRule()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
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
        


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityDynamics: 安全事件消息数组。
        :type SecurityDynamics: list of SecurityDynamic
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityDynamics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SecurityDynamics(self):
        return self._SecurityDynamics

    @SecurityDynamics.setter
    def SecurityDynamics(self, SecurityDynamics):
        self._SecurityDynamics = SecurityDynamics

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
        if params.get("SecurityDynamics") is not None:
            self._SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self._SecurityDynamics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 开始时间。
        :type BeginDate: str
        :param _EndDate: 结束时间。
        :type EndDate: str
        """
        self._BeginDate = None
        self._EndDate = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Malwares: 木马事件统计数据数组。
        :type Malwares: list of SecurityTrend
        :param _NonLocalLoginPlaces: 异地登录事件统计数据数组。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param _BruteAttacks: 密码破解事件统计数据数组。
        :type BruteAttacks: list of SecurityTrend
        :param _Vuls: 漏洞统计数据数组。
        :type Vuls: list of SecurityTrend
        :param _BaseLines: 基线统计数据数组。
        :type BaseLines: list of SecurityTrend
        :param _MaliciousRequests: 恶意请求统计数据数组。
        :type MaliciousRequests: list of SecurityTrend
        :param _HighRiskBashs: 高危命令统计数据数组。
        :type HighRiskBashs: list of SecurityTrend
        :param _ReverseShells: 反弹shell统计数据数组。
        :type ReverseShells: list of SecurityTrend
        :param _PrivilegeEscalations: 本地提权统计数据数组。
        :type PrivilegeEscalations: list of SecurityTrend
        :param _CyberAttacks: 网络攻击统计数据数组。
        :type CyberAttacks: list of SecurityTrend
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Malwares = None
        self._NonLocalLoginPlaces = None
        self._BruteAttacks = None
        self._Vuls = None
        self._BaseLines = None
        self._MaliciousRequests = None
        self._HighRiskBashs = None
        self._ReverseShells = None
        self._PrivilegeEscalations = None
        self._CyberAttacks = None
        self._RequestId = None

    @property
    def Malwares(self):
        return self._Malwares

    @Malwares.setter
    def Malwares(self, Malwares):
        self._Malwares = Malwares

    @property
    def NonLocalLoginPlaces(self):
        return self._NonLocalLoginPlaces

    @NonLocalLoginPlaces.setter
    def NonLocalLoginPlaces(self, NonLocalLoginPlaces):
        self._NonLocalLoginPlaces = NonLocalLoginPlaces

    @property
    def BruteAttacks(self):
        return self._BruteAttacks

    @BruteAttacks.setter
    def BruteAttacks(self, BruteAttacks):
        self._BruteAttacks = BruteAttacks

    @property
    def Vuls(self):
        return self._Vuls

    @Vuls.setter
    def Vuls(self, Vuls):
        self._Vuls = Vuls

    @property
    def BaseLines(self):
        return self._BaseLines

    @BaseLines.setter
    def BaseLines(self, BaseLines):
        self._BaseLines = BaseLines

    @property
    def MaliciousRequests(self):
        return self._MaliciousRequests

    @MaliciousRequests.setter
    def MaliciousRequests(self, MaliciousRequests):
        self._MaliciousRequests = MaliciousRequests

    @property
    def HighRiskBashs(self):
        return self._HighRiskBashs

    @HighRiskBashs.setter
    def HighRiskBashs(self, HighRiskBashs):
        self._HighRiskBashs = HighRiskBashs

    @property
    def ReverseShells(self):
        return self._ReverseShells

    @ReverseShells.setter
    def ReverseShells(self, ReverseShells):
        self._ReverseShells = ReverseShells

    @property
    def PrivilegeEscalations(self):
        return self._PrivilegeEscalations

    @PrivilegeEscalations.setter
    def PrivilegeEscalations(self, PrivilegeEscalations):
        self._PrivilegeEscalations = PrivilegeEscalations

    @property
    def CyberAttacks(self):
        return self._CyberAttacks

    @CyberAttacks.setter
    def CyberAttacks(self, CyberAttacks):
        self._CyberAttacks = CyberAttacks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self._Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self._NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self._BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self._Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self._BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self._MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self._HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self._ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self._PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self._CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._CyberAttacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 标签ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
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
        


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表数据
        :type List: list of TagMachine
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param _MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        """
        self._MachineType = None
        self._MachineRegion = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表信息
        :type List: list of Tag
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端UUID
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsualLoginPlaces: 常用登录地数组
        :type UsualLoginPlaces: list of UsualPlace
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsualLoginPlaces = None
        self._RequestId = None

    @property
    def UsualLoginPlaces(self):
        return self._UsualLoginPlaces

    @UsualLoginPlaces.setter
    def UsualLoginPlaces(self, UsualLoginPlaces):
        self._UsualLoginPlaces = UsualLoginPlaces

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self._UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self._UsualLoginPlaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VulId: 漏洞种类ID。
        :type VulId: int
        """
        self._VulId = None

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VulId: 漏洞种类ID。
        :type VulId: int
        :param _VulName: 漏洞名称。
        :type VulName: str
        :param _VulLevel: 漏洞等级。
        :type VulLevel: str
        :param _VulType: 漏洞类型。
        :type VulType: str
        :param _Description: 漏洞描述。
        :type Description: str
        :param _RepairPlan: 修复方案。
        :type RepairPlan: str
        :param _CveId: 漏洞CVE。
        :type CveId: str
        :param _Reference: 参考链接。
        :type Reference: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VulId = None
        self._VulName = None
        self._VulLevel = None
        self._VulType = None
        self._Description = None
        self._RepairPlan = None
        self._CveId = None
        self._Reference = None
        self._RequestId = None

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulName(self):
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RepairPlan(self):
        return self._RepairPlan

    @RepairPlan.setter
    def RepairPlan(self, RepairPlan):
        self._RepairPlan = RepairPlan

    @property
    def CveId(self):
        return self._CveId

    @CveId.setter
    def CveId(self, CveId):
        self._CveId = CveId

    @property
    def Reference(self):
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._VulType = params.get("VulType")
        self._Description = params.get("Description")
        self._RepairPlan = params.get("RepairPlan")
        self._CveId = params.get("CveId")
        self._Reference = params.get("Reference")
        self._RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult请求参数结构体

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VulNum: 漏洞数量。
        :type VulNum: int
        :param _ProVersionNum: 专业版机器数。
        :type ProVersionNum: int
        :param _ImpactedHostNum: 受影响的专业版主机数。
        :type ImpactedHostNum: int
        :param _HostNum: 主机总数。
        :type HostNum: int
        :param _BasicVersionNum: 基础版机器数。
        :type BasicVersionNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VulNum = None
        self._ProVersionNum = None
        self._ImpactedHostNum = None
        self._HostNum = None
        self._BasicVersionNum = None
        self._RequestId = None

    @property
    def VulNum(self):
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def ProVersionNum(self):
        return self._ProVersionNum

    @ProVersionNum.setter
    def ProVersionNum(self, ProVersionNum):
        self._ProVersionNum = ProVersionNum

    @property
    def ImpactedHostNum(self):
        return self._ImpactedHostNum

    @ImpactedHostNum.setter
    def ImpactedHostNum(self, ImpactedHostNum):
        self._ImpactedHostNum = ImpactedHostNum

    @property
    def HostNum(self):
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def BasicVersionNum(self):
        return self._BasicVersionNum

    @BasicVersionNum.setter
    def BasicVersionNum(self, BasicVersionNum):
        self._BasicVersionNum = BasicVersionNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VulNum = params.get("VulNum")
        self._ProVersionNum = params.get("ProVersionNum")
        self._ImpactedHostNum = params.get("ImpactedHostNum")
        self._HostNum = params.get("HostNum")
        self._BasicVersionNum = params.get("BasicVersionNum")
        self._RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VulType: 漏洞类型。
<li>WEB：Web应用漏洞</li>
<li>SYSTEM：系统组件漏洞</li>
<li>BASELINE：安全基线</li>
        :type VulType: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）

Status过滤条件值只能取其一，不能是“或”逻辑。
        :type Filters: list of Filter
        """
        self._VulType = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulType = params.get("VulType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 漏洞数量。
        :type TotalCount: int
        :param _Vuls: 漏洞列表数组。
        :type Vuls: list of Vul
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Vuls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Vuls(self):
        return self._Vuls

    @Vuls.setter
    def Vuls(self, Vuls):
        self._Vuls = Vuls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self._Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self._Vuls.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeeklyReportBruteAttacks: 专业周报密码破解数组。
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeeklyReportBruteAttacks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportBruteAttacks(self):
        return self._WeeklyReportBruteAttacks

    @WeeklyReportBruteAttacks.setter
    def WeeklyReportBruteAttacks(self, WeeklyReportBruteAttacks):
        self._WeeklyReportBruteAttacks = WeeklyReportBruteAttacks

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
        if params.get("WeeklyReportBruteAttacks") is not None:
            self._WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self._WeeklyReportBruteAttacks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 专业周报开始时间。
        :type BeginDate: str
        """
        self._BeginDate = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyName: 账号所属公司或个人名称。
        :type CompanyName: str
        :param _MachineNum: 机器总数。
        :type MachineNum: int
        :param _OnlineMachineNum: 云镜客户端在线数。
        :type OnlineMachineNum: int
        :param _OfflineMachineNum: 云镜客户端离线数。
        :type OfflineMachineNum: int
        :param _ProVersionMachineNum: 开通云镜专业版数量。
        :type ProVersionMachineNum: int
        :param _BeginDate: 周报开始时间。
        :type BeginDate: str
        :param _EndDate: 周报结束时间。
        :type EndDate: str
        :param _Level: 安全等级。
<li>HIGH：高</li>
<li>MIDDLE：中</li>
<li>LOW：低</li>
        :type Level: str
        :param _MalwareNum: 木马记录数。
        :type MalwareNum: int
        :param _NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param _BruteAttackSuccessNum: 密码破解成功数。
        :type BruteAttackSuccessNum: int
        :param _VulNum: 漏洞数。
        :type VulNum: int
        :param _DownloadUrl: 导出文件下载地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyName = None
        self._MachineNum = None
        self._OnlineMachineNum = None
        self._OfflineMachineNum = None
        self._ProVersionMachineNum = None
        self._BeginDate = None
        self._EndDate = None
        self._Level = None
        self._MalwareNum = None
        self._NonlocalLoginNum = None
        self._BruteAttackSuccessNum = None
        self._VulNum = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum

    @property
    def OnlineMachineNum(self):
        return self._OnlineMachineNum

    @OnlineMachineNum.setter
    def OnlineMachineNum(self, OnlineMachineNum):
        self._OnlineMachineNum = OnlineMachineNum

    @property
    def OfflineMachineNum(self):
        return self._OfflineMachineNum

    @OfflineMachineNum.setter
    def OfflineMachineNum(self, OfflineMachineNum):
        self._OfflineMachineNum = OfflineMachineNum

    @property
    def ProVersionMachineNum(self):
        return self._ProVersionMachineNum

    @ProVersionMachineNum.setter
    def ProVersionMachineNum(self, ProVersionMachineNum):
        self._ProVersionMachineNum = ProVersionMachineNum

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def MalwareNum(self):
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def NonlocalLoginNum(self):
        return self._NonlocalLoginNum

    @NonlocalLoginNum.setter
    def NonlocalLoginNum(self, NonlocalLoginNum):
        self._NonlocalLoginNum = NonlocalLoginNum

    @property
    def BruteAttackSuccessNum(self):
        return self._BruteAttackSuccessNum

    @BruteAttackSuccessNum.setter
    def BruteAttackSuccessNum(self, BruteAttackSuccessNum):
        self._BruteAttackSuccessNum = BruteAttackSuccessNum

    @property
    def VulNum(self):
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._MachineNum = params.get("MachineNum")
        self._OnlineMachineNum = params.get("OnlineMachineNum")
        self._OfflineMachineNum = params.get("OfflineMachineNum")
        self._ProVersionMachineNum = params.get("ProVersionMachineNum")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._Level = params.get("Level")
        self._MalwareNum = params.get("MalwareNum")
        self._NonlocalLoginNum = params.get("NonlocalLoginNum")
        self._BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self._VulNum = params.get("VulNum")
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeeklyReportMalwares: 专业周报木马数据。
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeeklyReportMalwares = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportMalwares(self):
        return self._WeeklyReportMalwares

    @WeeklyReportMalwares.setter
    def WeeklyReportMalwares(self, WeeklyReportMalwares):
        self._WeeklyReportMalwares = WeeklyReportMalwares

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
        if params.get("WeeklyReportMalwares") is not None:
            self._WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self._WeeklyReportMalwares.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 专业周报开始时间。
        :type BeginDate: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeeklyReportNonlocalLoginPlaces: 专业周报异地登录数据。
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeeklyReportNonlocalLoginPlaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportNonlocalLoginPlaces(self):
        return self._WeeklyReportNonlocalLoginPlaces

    @WeeklyReportNonlocalLoginPlaces.setter
    def WeeklyReportNonlocalLoginPlaces(self, WeeklyReportNonlocalLoginPlaces):
        self._WeeklyReportNonlocalLoginPlaces = WeeklyReportNonlocalLoginPlaces

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
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self._WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self._WeeklyReportNonlocalLoginPlaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginDate: 专业版周报开始时间。
        :type BeginDate: str
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeeklyReportVuls: 专业周报漏洞数据数组。
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeeklyReportVuls = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportVuls(self):
        return self._WeeklyReportVuls

    @WeeklyReportVuls.setter
    def WeeklyReportVuls(self, WeeklyReportVuls):
        self._WeeklyReportVuls = WeeklyReportVuls

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
        if params.get("WeeklyReportVuls") is not None:
            self._WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self._WeeklyReportVuls.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
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
        


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeeklyReports: 专业周报列表数组。
        :type WeeklyReports: list of WeeklyReport
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeeklyReports = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReports(self):
        return self._WeeklyReports

    @WeeklyReports.setter
    def WeeklyReports(self, WeeklyReports):
        self._WeeklyReports = WeeklyReports

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
        if params.get("WeeklyReports") is not None:
            self._WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self._WeeklyReports.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class EditBashRuleRequest(AbstractModel):
    """EditBashRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _Level: 危险等级(1: 高危 2:中危 3: 低危)
        :type Level: int
        :param _Rule: 正则表达式
        :type Rule: str
        :param _Id: 规则ID(新增时不填)
        :type Id: int
        :param _Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param _Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param _IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self._Name = None
        self._Level = None
        self._Rule = None
        self._Id = None
        self._Uuid = None
        self._Hostip = None
        self._IsGlobal = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Rule = params.get("Rule")
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Hostip = params.get("Hostip")
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditBashRuleResponse(AbstractModel):
    """EditBashRule返回参数结构体

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


class EditPrivilegeRuleRequest(AbstractModel):
    """EditPrivilegeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID(新增时请留空)
        :type Id: int
        :param _Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param _Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _SMode: 是否S权限进程
        :type SMode: int
        :param _IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self._Id = None
        self._Uuid = None
        self._Hostip = None
        self._ProcessName = None
        self._SMode = None
        self._IsGlobal = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def SMode(self):
        return self._SMode

    @SMode.setter
    def SMode(self, SMode):
        self._SMode = SMode

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Hostip = params.get("Hostip")
        self._ProcessName = params.get("ProcessName")
        self._SMode = params.get("SMode")
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditPrivilegeRuleResponse(AbstractModel):
    """EditPrivilegeRule返回参数结构体

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


class EditReverseShellRuleRequest(AbstractModel):
    """EditReverseShellRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID(新增时请留空)
        :type Id: int
        :param _Uuid: 客户端ID(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Uuid: str
        :param _Hostip: 主机IP(IsGlobal为1时，Uuid或Hostip必填一个)
        :type Hostip: str
        :param _DestIp: 目标IP
        :type DestIp: str
        :param _DestPort: 目标端口
        :type DestPort: str
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _IsGlobal: 是否全局规则(默认否)
        :type IsGlobal: int
        """
        self._Id = None
        self._Uuid = None
        self._Hostip = None
        self._DestIp = None
        self._DestPort = None
        self._ProcessName = None
        self._IsGlobal = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def DestIp(self):
        return self._DestIp

    @DestIp.setter
    def DestIp(self, DestIp):
        self._DestIp = DestIp

    @property
    def DestPort(self):
        return self._DestPort

    @DestPort.setter
    def DestPort(self, DestPort):
        self._DestPort = DestPort

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Hostip = params.get("Hostip")
        self._DestIp = params.get("DestIp")
        self._DestPort = params.get("DestPort")
        self._ProcessName = params.get("ProcessName")
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditReverseShellRuleResponse(AbstractModel):
    """EditReverseShellRule返回参数结构体

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


class EditTagsRequest(AbstractModel):
    """EditTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 标签名
        :type Name: str
        :param _Id: 标签ID
        :type Id: int
        :param _Quuids: CVM主机ID
        :type Quuids: list of str
        """
        self._Name = None
        self._Id = None
        self._Quuids = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Quuids(self):
        return self._Quuids

    @Quuids.setter
    def Quuids(self, Quuids):
        self._Quuids = Quuids


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditTagsResponse(AbstractModel):
    """EditTags返回参数结构体

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


class ExportAttackLogsRequest(AbstractModel):
    """ExportAttackLogs请求参数结构体

    """


class ExportAttackLogsResponse(AbstractModel):
    """ExportAttackLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _TaskId: 导出任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._TaskId = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportBashEventsRequest(AbstractModel):
    """ExportBashEvents请求参数结构体

    """


class ExportBashEventsResponse(AbstractModel):
    """ExportBashEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks请求参数结构体

    """


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests请求参数结构体

    """


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares请求参数结构体

    """


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces请求参数结构体

    """


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _TaskId: 导出任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._TaskId = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportPrivilegeEventsRequest(AbstractModel):
    """ExportPrivilegeEvents请求参数结构体

    """


class ExportPrivilegeEventsResponse(AbstractModel):
    """ExportPrivilegeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportReverseShellEventsRequest(AbstractModel):
    """ExportReverseShellEvents请求参数结构体

    """


class ExportReverseShellEventsResponse(AbstractModel):
    """ExportReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    * 最多只能有5个Filter
    * 同一个Filter存在多个Values，Values值数量最多不能超过5个。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤键的名称。
        :type Name: str
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class HistoryAccount(AbstractModel):
    """账号变更历史数据。

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _MachineName: 主机名。
        :type MachineName: str
        :param _Username: 帐号名。
        :type Username: str
        :param _ModifyType: 帐号变更类型。
<li>CREATE：表示新增帐号</li>
<li>MODIFY：表示修改帐号</li>
<li>DELETE：表示删除帐号</li>
        :type ModifyType: str
        :param _ModifyTime: 变更时间。
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Username = None
        self._ModifyType = None
        self._ModifyTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ModifyType(self):
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Username = params.get("Username")
        self._ModifyType = params.get("ModifyType")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 漏洞ID数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回参数结构体

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


class ImpactedHost(AbstractModel):
    """受影响主机信息

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞ID。
        :type Id: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _LastScanTime: 最后检测时间。
        :type LastScanTime: str
        :param _VulStatus: 漏洞状态。
<li>UN_OPERATED ：待处理</li>
<li>SCANING : 扫描中</li>
<li>FIXED : 已修复</li>
        :type VulStatus: str
        :param _Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param _Description: 漏洞描述。
        :type Description: str
        :param _VulId: 漏洞种类ID。
        :type VulId: int
        :param _IsProVersion: 是否为专业版。
        :type IsProVersion: bool
        """
        self._Id = None
        self._MachineIp = None
        self._MachineName = None
        self._LastScanTime = None
        self._VulStatus = None
        self._Uuid = None
        self._Description = None
        self._VulId = None
        self._IsProVersion = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def VulStatus(self):
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def IsProVersion(self):
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._LastScanTime = params.get("LastScanTime")
        self._VulStatus = params.get("VulStatus")
        self._Uuid = params.get("Uuid")
        self._Description = params.get("Description")
        self._VulId = params.get("VulId")
        self._IsProVersion = params.get("IsProVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceOpenProVersionPrepaidRequest(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargePrepaid: 预付费模式(包年包月)参数设置。
        :type ChargePrepaid: :class:`tencentcloud.yunjing.v20180228.models.ChargePrepaid`
        :param _Machines: 需要开通专业版机器列表数组。
        :type Machines: list of ProVersionMachine
        """
        self._ChargePrepaid = None
        self._Machines = None

    @property
    def ChargePrepaid(self):
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid

    @property
    def Machines(self):
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaid()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self._Machines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceOpenProVersionPrepaidResponse(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 预支费用的原价，单位：元。
        :type OriginalPrice: float
        :param _DiscountPrice: 预支费用的折扣价，单位：元。
        :type DiscountPrice: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._RequestId = params.get("RequestId")


class LoginWhiteLists(AbstractModel):
    """异地登录白名单

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID
        :type Id: int
        :param _Uuid: 云镜客户端ID
        :type Uuid: str
        :param _Places: 白名单地域
        :type Places: list of Place
        :param _UserName: 白名单用户（多个用户逗号隔开）
        :type UserName: str
        :param _SrcIp: 白名单IP（多个IP逗号隔开）
        :type SrcIp: str
        :param _IsGlobal: 是否为全局规则
        :type IsGlobal: bool
        :param _CreateTime: 创建白名单时间
        :type CreateTime: str
        :param _ModifyTime: 修改白名单时间
        :type ModifyTime: str
        :param _MachineName: 机器名
        :type MachineName: str
        :param _HostIp: 机器IP
        :type HostIp: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._Id = None
        self._Uuid = None
        self._Places = None
        self._UserName = None
        self._SrcIp = None
        self._IsGlobal = None
        self._CreateTime = None
        self._ModifyTime = None
        self._MachineName = None
        self._HostIp = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Places(self):
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        self._UserName = params.get("UserName")
        self._SrcIp = params.get("SrcIp")
        self._IsGlobal = params.get("IsGlobal")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._MachineName = params.get("MachineName")
        self._HostIp = params.get("HostIp")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteListsRule(AbstractModel):
    """白名单规则

    """

    def __init__(self):
        r"""
        :param _Places: 加白地域
        :type Places: list of Place
        :param _SrcIp: 加白源IP，支持网段，多个IP以逗号隔开
        :type SrcIp: str
        :param _UserName: 加白用户名，多个用户名以逗号隔开
        :type UserName: str
        :param _IsGlobal: 是否对全局生效
        :type IsGlobal: bool
        :param _HostIp: 白名单生效的机器
        :type HostIp: str
        :param _Id: 规则ID，用于更新规则
        :type Id: int
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._Places = None
        self._SrcIp = None
        self._UserName = None
        self._IsGlobal = None
        self._HostIp = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Places(self):
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        self._SrcIp = params.get("SrcIp")
        self._UserName = params.get("UserName")
        self._IsGlobal = params.get("IsGlobal")
        self._HostIp = params.get("HostIp")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Machine(AbstractModel):
    """主机列表

    """

    def __init__(self):
        r"""
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _MachineOs: 主机系统。
        :type MachineOs: str
        :param _MachineStatus: 主机状态。
<li>OFFLINE: 离线  </li>
<li>ONLINE: 在线</li>
<li>MACHINE_STOPPED: 已关机</li>
        :type MachineStatus: str
        :param _Uuid: 云镜客户端唯一Uuid，若客户端长时间不在线将返回空字符。
        :type Uuid: str
        :param _Quuid: CVM或BM机器唯一Uuid。
        :type Quuid: str
        :param _VulNum: 漏洞数。
        :type VulNum: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _IsProVersion: 是否是专业版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param _MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param _PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param _MalwareNum: 木马数。
        :type MalwareNum: int
        :param _Tag: 标签信息
        :type Tag: list of MachineTag
        :param _BaselineNum: 基线风险数。
        :type BaselineNum: int
        :param _CyberAttackNum: 网络风险数。
        :type CyberAttackNum: int
        :param _SecurityStatus: 风险状态。
<li>SAFE：安全</li>
<li>RISK：风险</li>
<li>UNKNOWN：未知</li>
        :type SecurityStatus: str
        :param _InvasionNum: 入侵事件数
        :type InvasionNum: int
        :param _RegionInfo: 地域信息
        :type RegionInfo: :class:`tencentcloud.yunjing.v20180228.models.RegionInfo`
        """
        self._MachineName = None
        self._MachineOs = None
        self._MachineStatus = None
        self._Uuid = None
        self._Quuid = None
        self._VulNum = None
        self._MachineIp = None
        self._IsProVersion = None
        self._MachineWanIp = None
        self._PayMode = None
        self._MalwareNum = None
        self._Tag = None
        self._BaselineNum = None
        self._CyberAttackNum = None
        self._SecurityStatus = None
        self._InvasionNum = None
        self._RegionInfo = None

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineOs(self):
        return self._MachineOs

    @MachineOs.setter
    def MachineOs(self, MachineOs):
        self._MachineOs = MachineOs

    @property
    def MachineStatus(self):
        return self._MachineStatus

    @MachineStatus.setter
    def MachineStatus(self, MachineStatus):
        self._MachineStatus = MachineStatus

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def VulNum(self):
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def IsProVersion(self):
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def MachineWanIp(self):
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def MalwareNum(self):
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def BaselineNum(self):
        return self._BaselineNum

    @BaselineNum.setter
    def BaselineNum(self, BaselineNum):
        self._BaselineNum = BaselineNum

    @property
    def CyberAttackNum(self):
        return self._CyberAttackNum

    @CyberAttackNum.setter
    def CyberAttackNum(self, CyberAttackNum):
        self._CyberAttackNum = CyberAttackNum

    @property
    def SecurityStatus(self):
        return self._SecurityStatus

    @SecurityStatus.setter
    def SecurityStatus(self, SecurityStatus):
        self._SecurityStatus = SecurityStatus

    @property
    def InvasionNum(self):
        return self._InvasionNum

    @InvasionNum.setter
    def InvasionNum(self, InvasionNum):
        self._InvasionNum = InvasionNum

    @property
    def RegionInfo(self):
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo


    def _deserialize(self, params):
        self._MachineName = params.get("MachineName")
        self._MachineOs = params.get("MachineOs")
        self._MachineStatus = params.get("MachineStatus")
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        self._VulNum = params.get("VulNum")
        self._MachineIp = params.get("MachineIp")
        self._IsProVersion = params.get("IsProVersion")
        self._MachineWanIp = params.get("MachineWanIp")
        self._PayMode = params.get("PayMode")
        self._MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._BaselineNum = params.get("BaselineNum")
        self._CyberAttackNum = params.get("CyberAttackNum")
        self._SecurityStatus = params.get("SecurityStatus")
        self._InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineTag(AbstractModel):
    """服务器标签信息

    """

    def __init__(self):
        r"""
        :param _Rid: 关联标签ID
        :type Rid: int
        :param _Name: 标签名
        :type Name: str
        :param _TagId: 标签ID
        :type TagId: int
        """
        self._Rid = None
        self._Name = None
        self._TagId = None

    @property
    def Rid(self):
        return self._Rid

    @Rid.setter
    def Rid(self, Rid):
        self._Rid = Rid

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._Rid = params.get("Rid")
        self._Name = params.get("Name")
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaliciousRequest(AbstractModel):
    """恶意请求数据。

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID。
        :type Id: int
        :param _Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _MachineName: 主机名。
        :type MachineName: str
        :param _Domain: 恶意请求域名。
        :type Domain: str
        :param _Count: 恶意请求数。
        :type Count: int
        :param _ProcessName: 进程名。
        :type ProcessName: str
        :param _Status: 记录状态。
<li>UN_OPERATED：待处理</li>
<li>TRUSTED：已信任</li>
<li>UN_TRUSTED：已取消信任</li>
        :type Status: str
        :param _Description: 恶意请求域名描述。
        :type Description: str
        :param _Reference: 参考地址。
        :type Reference: str
        :param _CreateTime: 发现时间。
        :type CreateTime: str
        :param _MergeTime: 记录合并时间。
        :type MergeTime: str
        :param _ProcessMd5: 进程MD5
值。
        :type ProcessMd5: str
        :param _CmdLine: 执行命令行。
        :type CmdLine: str
        :param _Pid: 进程PID。
        :type Pid: int
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Domain = None
        self._Count = None
        self._ProcessName = None
        self._Status = None
        self._Description = None
        self._Reference = None
        self._CreateTime = None
        self._MergeTime = None
        self._ProcessMd5 = None
        self._CmdLine = None
        self._Pid = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Reference(self):
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MergeTime(self):
        return self._MergeTime

    @MergeTime.setter
    def MergeTime(self, MergeTime):
        self._MergeTime = MergeTime

    @property
    def ProcessMd5(self):
        return self._ProcessMd5

    @ProcessMd5.setter
    def ProcessMd5(self, ProcessMd5):
        self._ProcessMd5 = ProcessMd5

    @property
    def CmdLine(self):
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Domain = params.get("Domain")
        self._Count = params.get("Count")
        self._ProcessName = params.get("ProcessName")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Reference = params.get("Reference")
        self._CreateTime = params.get("CreateTime")
        self._MergeTime = params.get("MergeTime")
        self._ProcessMd5 = params.get("ProcessMd5")
        self._CmdLine = params.get("CmdLine")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Malware(AbstractModel):
    """木马相关信息

    """

    def __init__(self):
        r"""
        :param _Id: 事件ID。
        :type Id: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _Status: 当前木马状态。
<li>UN_OPERATED：未处理</li><li>SEGREGATED：已隔离</li><li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li><li>RECOVERING：恢复中</li>
        :type Status: str
        :param _FilePath: 木马所在的路径。
        :type FilePath: str
        :param _Description: 木马描述。
        :type Description: str
        :param _MachineName: 主机名称。
        :type MachineName: str
        :param _FileCreateTime: 木马文件创建时间。
        :type FileCreateTime: str
        :param _ModifyTime: 木马文件修改时间。
        :type ModifyTime: str
        :param _Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._FilePath = None
        self._Description = None
        self._MachineName = None
        self._FileCreateTime = None
        self._ModifyTime = None
        self._Uuid = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def FileCreateTime(self):
        return self._FileCreateTime

    @FileCreateTime.setter
    def FileCreateTime(self, FileCreateTime):
        self._FileCreateTime = FileCreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._FilePath = params.get("FilePath")
        self._Description = params.get("Description")
        self._MachineName = params.get("MachineName")
        self._FileCreateTime = params.get("FileCreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 异地登录事件Id数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces返回参数结构体

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


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Attribute: 告警项目。
<li>Offline：防护软件离线</li>
<li>Malware：发现木马文件</li>
<li>NonlocalLogin：发现异地登录行为</li>
<li>CrackSuccess：被暴力破解成功</li>
        :type Attribute: str
        :param _Value: 告警项目属性。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Value: str
        """
        self._Attribute = None
        self._Value = None

    @property
    def Attribute(self):
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Attribute = params.get("Attribute")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute返回参数结构体

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


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 设置自动开通状态。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回参数结构体

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


class ModifyLoginWhiteListRequest(AbstractModel):
    """ModifyLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 白名单规则
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self._Rules = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = LoginWhiteListsRule()
            self._Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoginWhiteListResponse(AbstractModel):
    """ModifyLoginWhiteList返回参数结构体

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


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>
        :type RenewFlag: str
        :param _Quuid: 主机唯一ID，对应CVM的uuid、BM的instanceId。
        :type Quuid: str
        """
        self._RenewFlag = None
        self._Quuid = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag返回参数结构体

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


class NonLocalLoginPlace(AbstractModel):
    """异地登录

    """

    def __init__(self):
        r"""
        :param _Id: 事件ID。
        :type Id: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _Status: 登录状态
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>NORMAL_LOGIN：正常登录</li>
        :type Status: str
        :param _UserName: 用户名。
        :type UserName: str
        :param _City: 城市ID。
        :type City: int
        :param _Country: 国家ID。
        :type Country: int
        :param _Province: 省份ID。
        :type Province: int
        :param _SrcIp: 登录IP。
        :type SrcIp: str
        :param _MachineName: 机器名称。
        :type MachineName: str
        :param _LoginTime: 登录时间。
        :type LoginTime: str
        :param _Uuid: 云镜客户端唯一标识Uuid。
        :type Uuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._UserName = None
        self._City = None
        self._Country = None
        self._Province = None
        self._SrcIp = None
        self._MachineName = None
        self._LoginTime = None
        self._Uuid = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._SrcIp = params.get("SrcIp")
        self._MachineName = params.get("MachineName")
        self._LoginTime = params.get("LoginTime")
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPort(AbstractModel):
    """端口列表

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param _Port: 开放端口号。
        :type Port: int
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _MachineName: 主机名。
        :type MachineName: str
        :param _ProcessName: 端口对应进程名。
        :type ProcessName: str
        :param _Pid: 端口对应进程Pid。
        :type Pid: int
        :param _CreateTime: 记录创建时间。
        :type CreateTime: str
        :param _ModifyTime: 记录更新时间。
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._Port = None
        self._MachineIp = None
        self._MachineName = None
        self._ProcessName = None
        self._Pid = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Port = params.get("Port")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._ProcessName = params.get("ProcessName")
        self._Pid = params.get("Pid")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPortStatistics(AbstractModel):
    """端口统计列表

    """

    def __init__(self):
        r"""
        :param _Port: 端口号
        :type Port: int
        :param _MachineNum: 主机数量
        :type MachineNum: int
        """
        self._Port = None
        self._MachineNum = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionPrepaidRequest(AbstractModel):
    """OpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.yunjing.v20180228.models.ChargePrepaid`
        :param _Machines: 需要开通专业版主机信息数组。
        :type Machines: list of ProVersionMachine
        """
        self._ChargePrepaid = None
        self._Machines = None

    @property
    def ChargePrepaid(self):
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid

    @property
    def Machines(self):
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaid()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self._Machines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionPrepaidResponse(AbstractModel):
    """OpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 订单ID列表。
        :type DealIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealIds = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._RequestId = params.get("RequestId")


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param _MachineRegion: 机器所属地域。
如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param _Quuids: 主机唯一标识Uuid数组。
黑石的InstanceId，CVM的Uuid
        :type Quuids: list of str
        :param _ActivityId: 活动ID。
        :type ActivityId: int
        """
        self._MachineType = None
        self._MachineRegion = None
        self._Quuids = None
        self._ActivityId = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def Quuids(self):
        return self._Quuids

    @Quuids.setter
    def Quuids(self, Quuids):
        self._Quuids = Quuids

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._Quuids = params.get("Quuids")
        self._ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion返回参数结构体

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


class Place(AbstractModel):
    """登录地信息

    """

    def __init__(self):
        r"""
        :param _CityId: 城市 ID。
        :type CityId: int
        :param _ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param _CountryId: 国家ID，暂只支持国内：1。
        :type CountryId: int
        """
        self._CityId = None
        self._ProvinceId = None
        self._CountryId = None

    @property
    def CityId(self):
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId

    @property
    def ProvinceId(self):
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def CountryId(self):
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId


    def _deserialize(self, params):
        self._CityId = params.get("CityId")
        self._ProvinceId = params.get("ProvinceId")
        self._CountryId = params.get("CountryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeEscalationProcess(AbstractModel):
    """本地提权数据

    """

    def __init__(self):
        r"""
        :param _Id: 数据ID
        :type Id: int
        :param _Uuid: 云镜ID
        :type Uuid: str
        :param _Quuid: 主机ID
        :type Quuid: str
        :param _Hostip: 主机内网IP
        :type Hostip: str
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _FullPath: 进程路径
        :type FullPath: str
        :param _CmdLine: 执行命令
        :type CmdLine: str
        :param _UserName: 用户名
        :type UserName: str
        :param _UserGroup: 用户组
        :type UserGroup: str
        :param _ProcFilePrivilege: 进程文件权限
        :type ProcFilePrivilege: str
        :param _ParentProcName: 父进程名
        :type ParentProcName: str
        :param _ParentProcUser: 父进程用户名
        :type ParentProcUser: str
        :param _ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param _ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param _ProcTree: 进程树
        :type ProcTree: str
        :param _Status: 处理状态
        :type Status: int
        :param _CreateTime: 发生时间
        :type CreateTime: str
        :param _MachineName: 机器名
        :type MachineName: str
        """
        self._Id = None
        self._Uuid = None
        self._Quuid = None
        self._Hostip = None
        self._ProcessName = None
        self._FullPath = None
        self._CmdLine = None
        self._UserName = None
        self._UserGroup = None
        self._ProcFilePrivilege = None
        self._ParentProcName = None
        self._ParentProcUser = None
        self._ParentProcGroup = None
        self._ParentProcPath = None
        self._ProcTree = None
        self._Status = None
        self._CreateTime = None
        self._MachineName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def FullPath(self):
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath

    @property
    def CmdLine(self):
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def ProcFilePrivilege(self):
        return self._ProcFilePrivilege

    @ProcFilePrivilege.setter
    def ProcFilePrivilege(self, ProcFilePrivilege):
        self._ProcFilePrivilege = ProcFilePrivilege

    @property
    def ParentProcName(self):
        return self._ParentProcName

    @ParentProcName.setter
    def ParentProcName(self, ParentProcName):
        self._ParentProcName = ParentProcName

    @property
    def ParentProcUser(self):
        return self._ParentProcUser

    @ParentProcUser.setter
    def ParentProcUser(self, ParentProcUser):
        self._ParentProcUser = ParentProcUser

    @property
    def ParentProcGroup(self):
        return self._ParentProcGroup

    @ParentProcGroup.setter
    def ParentProcGroup(self, ParentProcGroup):
        self._ParentProcGroup = ParentProcGroup

    @property
    def ParentProcPath(self):
        return self._ParentProcPath

    @ParentProcPath.setter
    def ParentProcPath(self, ParentProcPath):
        self._ParentProcPath = ParentProcPath

    @property
    def ProcTree(self):
        return self._ProcTree

    @ProcTree.setter
    def ProcTree(self, ProcTree):
        self._ProcTree = ProcTree

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        self._Hostip = params.get("Hostip")
        self._ProcessName = params.get("ProcessName")
        self._FullPath = params.get("FullPath")
        self._CmdLine = params.get("CmdLine")
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._ProcFilePrivilege = params.get("ProcFilePrivilege")
        self._ParentProcName = params.get("ParentProcName")
        self._ParentProcUser = params.get("ParentProcUser")
        self._ParentProcGroup = params.get("ParentProcGroup")
        self._ParentProcPath = params.get("ParentProcPath")
        self._ProcTree = params.get("ProcTree")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeRule(AbstractModel):
    """本地提权规则

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _Uuid: 客户端ID
        :type Uuid: str
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _SMode: 是否S权限
        :type SMode: int
        :param _Operator: 操作人
        :type Operator: str
        :param _IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param _Status: 状态(0: 有效 1: 无效)
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Hostip: 主机IP
        :type Hostip: str
        """
        self._Id = None
        self._Uuid = None
        self._ProcessName = None
        self._SMode = None
        self._Operator = None
        self._IsGlobal = None
        self._Status = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Hostip = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def SMode(self):
        return self._SMode

    @SMode.setter
    def SMode(self, SMode):
        self._SMode = SMode

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._ProcessName = params.get("ProcessName")
        self._SMode = params.get("SMode")
        self._Operator = params.get("Operator")
        self._IsGlobal = params.get("IsGlobal")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProVersionMachine(AbstractModel):
    """需要开通专业版机器信息。

    """

    def __init__(self):
        r"""
        :param _MachineType: 主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param _MachineRegion: 主机所在地域。
如：ap-guangzhou、ap-beijing
        :type MachineRegion: str
        :param _Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self._MachineType = None
        self._MachineRegion = None
        self._Quuid = None

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Process(AbstractModel):
    """进程信息数据。

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一UUID。
        :type Uuid: str
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _MachineName: 主机名。
        :type MachineName: str
        :param _Pid: 进程Pid。
        :type Pid: int
        :param _Ppid: 进程Ppid。
        :type Ppid: int
        :param _ProcessName: 进程名。
        :type ProcessName: str
        :param _Username: 进程用户名。
        :type Username: str
        :param _Platform: 所属平台。
<li>WIN32：windows32位</li>
<li>WIN64：windows64位</li>
<li>LINUX32：Linux32位</li>
<li>LINUX64：Linux64位</li>
        :type Platform: str
        :param _FullPath: 进程路径。
        :type FullPath: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Pid = None
        self._Ppid = None
        self._ProcessName = None
        self._Username = None
        self._Platform = None
        self._FullPath = None
        self._CreateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Ppid(self):
        return self._Ppid

    @Ppid.setter
    def Ppid(self, Ppid):
        self._Ppid = Ppid

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def FullPath(self):
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Pid = params.get("Pid")
        self._Ppid = params.get("Ppid")
        self._ProcessName = params.get("ProcessName")
        self._Username = params.get("Username")
        self._Platform = params.get("Platform")
        self._FullPath = params.get("FullPath")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistics(AbstractModel):
    """进程数据统计数据。

    """

    def __init__(self):
        r"""
        :param _ProcessName: 进程名。
        :type ProcessName: str
        :param _MachineNum: 主机数量。
        :type MachineNum: int
        """
        self._ProcessName = None
        self._MachineNum = None

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def MachineNum(self):
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._ProcessName = params.get("ProcessName")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 木马Id数组,单次最大删除不能超过200条
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessIds: 恢复成功id数组
        :type SuccessIds: list of int non-negative
        :param _FailedIds: 恢复失败id数组
        :type FailedIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessIds = None
        self._FailedIds = None
        self._RequestId = None

    @property
    def SuccessIds(self):
        return self._SuccessIds

    @SuccessIds.setter
    def SuccessIds(self, SuccessIds):
        self._SuccessIds = SuccessIds

    @property
    def FailedIds(self):
        return self._FailedIds

    @FailedIds.setter
    def FailedIds(self, FailedIds):
        self._FailedIds = FailedIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessIds = params.get("SuccessIds")
        self._FailedIds = params.get("FailedIds")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域标志，如 ap-guangzhou，ap-shanghai，ap-beijing
        :type Region: str
        :param _RegionName: 地域中文名，如华南地区（广州），华东地区（上海金融），华北地区（北京）
        :type RegionName: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionCode: 地域代码，如 gz，sh，bj
        :type RegionCode: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionCode = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionCode(self):
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionCode = params.get("RegionCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewProVersionRequest(AbstractModel):
    """RenewProVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.yunjing.v20180228.models.ChargePrepaid`
        :param _Quuid: 主机唯一ID，对应CVM的uuid、BM的InstanceId。
        :type Quuid: str
        """
        self._ChargePrepaid = None
        self._Quuid = None

    @property
    def ChargePrepaid(self):
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaid()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewProVersionResponse(AbstractModel):
    """RenewProVersion返回参数结构体

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


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞ID。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
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
        


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost返回参数结构体

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


class ReverseShell(AbstractModel):
    """反弹Shell数据

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _Uuid: 云镜UUID
        :type Uuid: str
        :param _Quuid: 主机ID
        :type Quuid: str
        :param _Hostip: 主机内网IP
        :type Hostip: str
        :param _DstIp: 目标IP
        :type DstIp: str
        :param _DstPort: 目标端口
        :type DstPort: int
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _FullPath: 进程路径
        :type FullPath: str
        :param _CmdLine: 命令详情
        :type CmdLine: str
        :param _UserName: 执行用户
        :type UserName: str
        :param _UserGroup: 执行用户组
        :type UserGroup: str
        :param _ParentProcName: 父进程名
        :type ParentProcName: str
        :param _ParentProcUser: 父进程用户
        :type ParentProcUser: str
        :param _ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param _ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param _Status: 处理状态
        :type Status: int
        :param _CreateTime: 产生时间
        :type CreateTime: str
        :param _MachineName: 主机名
        :type MachineName: str
        :param _ProcTree: 进程树
        :type ProcTree: str
        """
        self._Id = None
        self._Uuid = None
        self._Quuid = None
        self._Hostip = None
        self._DstIp = None
        self._DstPort = None
        self._ProcessName = None
        self._FullPath = None
        self._CmdLine = None
        self._UserName = None
        self._UserGroup = None
        self._ParentProcName = None
        self._ParentProcUser = None
        self._ParentProcGroup = None
        self._ParentProcPath = None
        self._Status = None
        self._CreateTime = None
        self._MachineName = None
        self._ProcTree = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def FullPath(self):
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath

    @property
    def CmdLine(self):
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def ParentProcName(self):
        return self._ParentProcName

    @ParentProcName.setter
    def ParentProcName(self, ParentProcName):
        self._ParentProcName = ParentProcName

    @property
    def ParentProcUser(self):
        return self._ParentProcUser

    @ParentProcUser.setter
    def ParentProcUser(self, ParentProcUser):
        self._ParentProcUser = ParentProcUser

    @property
    def ParentProcGroup(self):
        return self._ParentProcGroup

    @ParentProcGroup.setter
    def ParentProcGroup(self, ParentProcGroup):
        self._ParentProcGroup = ParentProcGroup

    @property
    def ParentProcPath(self):
        return self._ParentProcPath

    @ParentProcPath.setter
    def ParentProcPath(self, ParentProcPath):
        self._ParentProcPath = ParentProcPath

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def ProcTree(self):
        return self._ProcTree

    @ProcTree.setter
    def ProcTree(self, ProcTree):
        self._ProcTree = ProcTree


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        self._Hostip = params.get("Hostip")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._ProcessName = params.get("ProcessName")
        self._FullPath = params.get("FullPath")
        self._CmdLine = params.get("CmdLine")
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._ParentProcName = params.get("ParentProcName")
        self._ParentProcUser = params.get("ParentProcUser")
        self._ParentProcGroup = params.get("ParentProcGroup")
        self._ParentProcPath = params.get("ParentProcPath")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._MachineName = params.get("MachineName")
        self._ProcTree = params.get("ProcTree")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellRule(AbstractModel):
    """反弹Shell规则

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _Uuid: 客户端ID
        :type Uuid: str
        :param _ProcessName: 进程名称
        :type ProcessName: str
        :param _DestIp: 目标IP
        :type DestIp: str
        :param _DestPort: 目标端口
        :type DestPort: str
        :param _Operator: 操作人
        :type Operator: str
        :param _IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param _Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Hostip: 主机IP
        :type Hostip: str
        """
        self._Id = None
        self._Uuid = None
        self._ProcessName = None
        self._DestIp = None
        self._DestPort = None
        self._Operator = None
        self._IsGlobal = None
        self._Status = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Hostip = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def DestIp(self):
        return self._DestIp

    @DestIp.setter
    def DestIp(self, DestIp):
        self._DestIp = DestIp

    @property
    def DestPort(self):
        return self._DestPort

    @DestPort.setter
    def DestPort(self, DestPort):
        self._DestPort = DestPort

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def IsGlobal(self):
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Hostip(self):
        return self._Hostip

    @Hostip.setter
    def Hostip(self, Hostip):
        self._Hostip = Hostip


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._ProcessName = params.get("ProcessName")
        self._DestIp = params.get("DestIp")
        self._DestPort = params.get("DestPort")
        self._Operator = params.get("Operator")
        self._IsGlobal = params.get("IsGlobal")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityDynamic(AbstractModel):
    """安全事件消息数据。

    """

    def __init__(self):
        r"""
        :param _Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param _EventTime: 安全事件发生事件。
        :type EventTime: str
        :param _EventType: 安全事件类型。
<li>MALWARE：木马事件</li>
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>BRUTEATTACK_SUCCESS：密码破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基线</li>
        :type EventType: str
        :param _Message: 安全事件消息。
        :type Message: str
        :param _SecurityLevel: 安全事件等级。
<li>RISK: 严重</li>
<li>HIGH: 高危</li>
<li>NORMAL: 中危</li>
<li>LOW: 低危</li>
        :type SecurityLevel: str
        """
        self._Uuid = None
        self._EventTime = None
        self._EventType = None
        self._Message = None
        self._SecurityLevel = None

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SecurityLevel(self):
        return self._SecurityLevel

    @SecurityLevel.setter
    def SecurityLevel(self, SecurityLevel):
        self._SecurityLevel = SecurityLevel


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._EventTime = params.get("EventTime")
        self._EventType = params.get("EventType")
        self._Message = params.get("Message")
        self._SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTrend(AbstractModel):
    """安全趋势统计数据。

    """

    def __init__(self):
        r"""
        :param _Date: 事件时间。
        :type Date: str
        :param _EventNum: 事件数量。
        :type EventNum: int
        """
        self._Date = None
        self._EventNum = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def EventNum(self):
        return self._EventNum

    @EventNum.setter
    def EventNum(self, EventNum):
        self._EventNum = EventNum


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._EventNum = params.get("EventNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 木马事件ID数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessIds: 隔离成功的id数组。
        :type SuccessIds: list of int non-negative
        :param _FailedIds: 隔离失败的id数组。
        :type FailedIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessIds = None
        self._FailedIds = None
        self._RequestId = None

    @property
    def SuccessIds(self):
        return self._SuccessIds

    @SuccessIds.setter
    def SuccessIds(self, SuccessIds):
        self._SuccessIds = SuccessIds

    @property
    def FailedIds(self):
        return self._FailedIds

    @FailedIds.setter
    def FailedIds(self, FailedIds):
        self._FailedIds = FailedIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessIds = params.get("SuccessIds")
        self._FailedIds = params.get("FailedIds")
        self._RequestId = params.get("RequestId")


class SetBashEventsStatusRequest(AbstractModel):
    """SetBashEventsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        :param _Status: 新状态(0-待处理 1-高危 2-正常)
        :type Status: int
        """
        self._Ids = None
        self._Status = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBashEventsStatusResponse(AbstractModel):
    """SetBashEventsStatus返回参数结构体

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


class SwitchBashRulesRequest(AbstractModel):
    """SwitchBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _Disabled: 是否禁用
        :type Disabled: int
        """
        self._Id = None
        self._Disabled = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchBashRulesResponse(AbstractModel):
    """SwitchBashRules返回参数结构体

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


class Tag(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _Id: 标签ID
        :type Id: int
        :param _Name: 标签名
        :type Name: str
        :param _Count: 服务器数
        :type Count: int
        """
        self._Id = None
        self._Name = None
        self._Count = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagMachine(AbstractModel):
    """标签相关服务器信息

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: str
        :param _Quuid: 主机ID
        :type Quuid: str
        :param _MachineName: 主机名称
        :type MachineName: str
        :param _MachineIp: 主机内网IP
        :type MachineIp: str
        :param _MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param _MachineRegion: 主机区域
        :type MachineRegion: str
        :param _MachineType: 主机区域类型
        :type MachineType: str
        """
        self._Id = None
        self._Quuid = None
        self._MachineName = None
        self._MachineIp = None
        self._MachineWanIp = None
        self._MachineRegion = None
        self._MachineType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Quuid(self):
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineWanIp(self):
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def MachineRegion(self):
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def MachineType(self):
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Quuid = params.get("Quuid")
        self._MachineName = params.get("MachineName")
        self._MachineIp = params.get("MachineIp")
        self._MachineWanIp = params.get("MachineWanIp")
        self._MachineRegion = params.get("MachineRegion")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 恶意请求记录ID。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
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
        


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest返回参数结构体

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


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 木马ID数组。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回参数结构体

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


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 受信任记录ID。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
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
        


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest返回参数结构体

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


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ids: 木马ID数组，单次最大处理不能超过200条。
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回参数结构体

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


class UsualPlace(AbstractModel):
    """常用登录地

    """

    def __init__(self):
        r"""
        :param _Id: ID。
        :type Id: int
        :param _Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param _CountryId: 国家 ID。
        :type CountryId: int
        :param _ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param _CityId: 城市 ID。
        :type CityId: int
        """
        self._Id = None
        self._Uuid = None
        self._CountryId = None
        self._ProvinceId = None
        self._CityId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def CountryId(self):
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId

    @property
    def ProvinceId(self):
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def CityId(self):
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._CountryId = params.get("CountryId")
        self._ProvinceId = params.get("ProvinceId")
        self._CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vul(AbstractModel):
    """漏洞列表数据

    """

    def __init__(self):
        r"""
        :param _VulId: 漏洞种类ID
        :type VulId: int
        :param _VulName: 漏洞名称
        :type VulName: str
        :param _VulLevel: 漏洞危害等级:
HIGH：高危
MIDDLE：中危
LOW：低危
NOTICE：提示
        :type VulLevel: str
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _ImpactedHostNum: 受影响机器数量
        :type ImpactedHostNum: int
        :param _VulStatus: 漏洞状态
* UN_OPERATED : 待处理
* FIXED : 已修复
        :type VulStatus: str
        """
        self._VulId = None
        self._VulName = None
        self._VulLevel = None
        self._LastScanTime = None
        self._ImpactedHostNum = None
        self._VulStatus = None

    @property
    def VulId(self):
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulName(self):
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ImpactedHostNum(self):
        return self._ImpactedHostNum

    @ImpactedHostNum.setter
    def ImpactedHostNum(self, ImpactedHostNum):
        self._ImpactedHostNum = ImpactedHostNum

    @property
    def VulStatus(self):
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._ImpactedHostNum = params.get("ImpactedHostNum")
        self._VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReport(AbstractModel):
    """周报列表。

    """

    def __init__(self):
        r"""
        :param _BeginDate: 周报开始时间。
        :type BeginDate: str
        :param _EndDate: 周报结束时间。
        :type EndDate: str
        """
        self._BeginDate = None
        self._EndDate = None

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportBruteAttack(AbstractModel):
    """专业周报密码破解数据。

    """

    def __init__(self):
        r"""
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _Username: 被破解用户名。
        :type Username: str
        :param _SrcIp: 源IP。
        :type SrcIp: str
        :param _Count: 尝试次数。
        :type Count: int
        :param _AttackTime: 攻击时间。
        :type AttackTime: str
        """
        self._MachineIp = None
        self._Username = None
        self._SrcIp = None
        self._Count = None
        self._AttackTime = None

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AttackTime(self):
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._Username = params.get("Username")
        self._SrcIp = params.get("SrcIp")
        self._Count = params.get("Count")
        self._AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportMalware(AbstractModel):
    """专业周报木马数据。

    """

    def __init__(self):
        r"""
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _FilePath: 木马文件路径。
        :type FilePath: str
        :param _Md5: 木马文件MD5值。
        :type Md5: str
        :param _FindTime: 木马发现时间。
        :type FindTime: str
        :param _Status: 当前木马状态。
<li>UN_OPERATED：未处理</li>
<li>SEGREGATED：已隔离</li>
<li>TRUSTED：已信任</li>
<li>SEPARATING：隔离中</li>
<li>RECOVERING：恢复中</li>
        :type Status: str
        """
        self._MachineIp = None
        self._FilePath = None
        self._Md5 = None
        self._FindTime = None
        self._Status = None

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def FindTime(self):
        return self._FindTime

    @FindTime.setter
    def FindTime(self, FindTime):
        self._FindTime = FindTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._FilePath = params.get("FilePath")
        self._Md5 = params.get("Md5")
        self._FindTime = params.get("FindTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """专业周报异地登录数据。

    """

    def __init__(self):
        r"""
        :param _MachineIp: 主机IP。
        :type MachineIp: str
        :param _Username: 用户名。
        :type Username: str
        :param _SrcIp: 源IP。
        :type SrcIp: str
        :param _Country: 国家ID。
        :type Country: int
        :param _Province: 省份ID。
        :type Province: int
        :param _City: 城市ID。
        :type City: int
        :param _LoginTime: 登录时间。
        :type LoginTime: str
        """
        self._MachineIp = None
        self._Username = None
        self._SrcIp = None
        self._Country = None
        self._Province = None
        self._City = None
        self._LoginTime = None

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._Username = params.get("Username")
        self._SrcIp = params.get("SrcIp")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._LoginTime = params.get("LoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportVul(AbstractModel):
    """专业版周报漏洞数据。

    """

    def __init__(self):
        r"""
        :param _MachineIp: 主机内网IP。
        :type MachineIp: str
        :param _VulName: 漏洞名称。
        :type VulName: str
        :param _VulType: 漏洞类型。
<li> WEB : Web漏洞</li>
<li> SYSTEM :系统组件漏洞</li>
<li> BASELINE : 安全基线</li>
        :type VulType: str
        :param _Description: 漏洞描述。
        :type Description: str
        :param _VulStatus: 漏洞状态。
<li> UN_OPERATED : 待处理</li>
<li> SCANING : 扫描中</li>
<li> FIXED : 已修复</li>
        :type VulStatus: str
        :param _LastScanTime: 最后扫描时间。
        :type LastScanTime: str
        """
        self._MachineIp = None
        self._VulName = None
        self._VulType = None
        self._Description = None
        self._VulStatus = None
        self._LastScanTime = None

    @property
    def MachineIp(self):
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def VulName(self):
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulType(self):
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulStatus(self):
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus

    @property
    def LastScanTime(self):
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._VulName = params.get("VulName")
        self._VulType = params.get("VulType")
        self._Description = params.get("Description")
        self._VulStatus = params.get("VulStatus")
        self._LastScanTime = params.get("LastScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        