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


class AKInfo(AbstractModel):
    r"""AK简要信息

    """

    def __init__(self):
        r"""
        :param _ID: ak对应id
        :type ID: int
        :param _Name: ak具体值 临时密钥时返回临时密钥
        :type Name: str
        :param _User: 所属账号
        :type User: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._ID = None
        self._Name = None
        self._User = None
        self._Remark = None

    @property
    def ID(self):
        r"""ak对应id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""ak具体值 临时密钥时返回临时密钥
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def User(self):
        r"""所属账号
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._User = params.get("User")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarm(AbstractModel):
    r"""访问密钥告警记录

    """

    def __init__(self):
        r"""
        :param _Name: 告警名称
        :type Name: str
        :param _Level: 告警等级
0-无效 1-提示 2-低危 3-中危 4-高危 5-严重
        :type Level: int
        :param _ID: 告警记录ID
        :type ID: int
        :param _AlarmRuleID: 告警规则ID
        :type AlarmRuleID: int
        :param _AlarmType: 告警类型
0 异常调用
1 泄漏监测
        :type AlarmType: int
        :param _AccessKey: 访问密钥
        :type AccessKey: str
        :param _AccessKeyID: 访问密钥ID
        :type AccessKeyID: int
        :param _AccessKeyRemark: 访问密钥备注
        :type AccessKeyRemark: str
        :param _LastAlarmTime: 最后告警时间
        :type LastAlarmTime: str
        :param _Status: 告警状态
0-未处理 1-已处理 2-已忽略
        :type Status: int
        :param _Date: 聚合日期
        :type Date: str
        :param _Tag: 告警标签
        :type Tag: list of str
        :param _Uin: 所属主账号Uin
        :type Uin: str
        :param _Nickname: 所属主账号昵称
        :type Nickname: str
        :param _SubUin: 所属子账号Uin
        :type SubUin: str
        :param _SubNickname: 所属子账号昵称
        :type SubNickname: str
        :param _Type: 账号类型
0 主账号AK 1 子账号AK 2 临时密钥
        :type Type: int
        :param _AppID: 所属appid
        :type AppID: int
        :param _LeakEvidence: 泄漏证据
        :type LeakEvidence: list of str
        :param _IsSupportEditWhiteAccount: 是否支持编辑信任账号
        :type IsSupportEditWhiteAccount: bool
        :param _Evidence: 告警证据
        :type Evidence: str
        :param _RuleKey: 告警规则标识
        :type RuleKey: str
        :param _CloudType: 云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :type CloudType: int
        """
        self._Name = None
        self._Level = None
        self._ID = None
        self._AlarmRuleID = None
        self._AlarmType = None
        self._AccessKey = None
        self._AccessKeyID = None
        self._AccessKeyRemark = None
        self._LastAlarmTime = None
        self._Status = None
        self._Date = None
        self._Tag = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._AppID = None
        self._LeakEvidence = None
        self._IsSupportEditWhiteAccount = None
        self._Evidence = None
        self._RuleKey = None
        self._CloudType = None

    @property
    def Name(self):
        r"""告警名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        r"""告警等级
0-无效 1-提示 2-低危 3-中危 4-高危 5-严重
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def ID(self):
        r"""告警记录ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AlarmRuleID(self):
        r"""告警规则ID
        :rtype: int
        """
        return self._AlarmRuleID

    @AlarmRuleID.setter
    def AlarmRuleID(self, AlarmRuleID):
        self._AlarmRuleID = AlarmRuleID

    @property
    def AlarmType(self):
        r"""告警类型
0 异常调用
1 泄漏监测
        :rtype: int
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AccessKey(self):
        r"""访问密钥
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyID(self):
        r"""访问密钥ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def AccessKeyRemark(self):
        r"""访问密钥备注
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def LastAlarmTime(self):
        r"""最后告警时间
        :rtype: str
        """
        return self._LastAlarmTime

    @LastAlarmTime.setter
    def LastAlarmTime(self, LastAlarmTime):
        self._LastAlarmTime = LastAlarmTime

    @property
    def Status(self):
        r"""告警状态
0-未处理 1-已处理 2-已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Date(self):
        r"""聚合日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Tag(self):
        r"""告警标签
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Uin(self):
        r"""所属主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""所属主账号昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""所属子账号Uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""所属子账号昵称
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""账号类型
0 主账号AK 1 子账号AK 2 临时密钥
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppID(self):
        r"""所属appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def LeakEvidence(self):
        r"""泄漏证据
        :rtype: list of str
        """
        return self._LeakEvidence

    @LeakEvidence.setter
    def LeakEvidence(self, LeakEvidence):
        self._LeakEvidence = LeakEvidence

    @property
    def IsSupportEditWhiteAccount(self):
        r"""是否支持编辑信任账号
        :rtype: bool
        """
        return self._IsSupportEditWhiteAccount

    @IsSupportEditWhiteAccount.setter
    def IsSupportEditWhiteAccount(self, IsSupportEditWhiteAccount):
        self._IsSupportEditWhiteAccount = IsSupportEditWhiteAccount

    @property
    def Evidence(self):
        r"""告警证据
        :rtype: str
        """
        return self._Evidence

    @Evidence.setter
    def Evidence(self, Evidence):
        self._Evidence = Evidence

    @property
    def RuleKey(self):
        r"""告警规则标识
        :rtype: str
        """
        return self._RuleKey

    @RuleKey.setter
    def RuleKey(self, RuleKey):
        self._RuleKey = RuleKey

    @property
    def CloudType(self):
        r"""云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._ID = params.get("ID")
        self._AlarmRuleID = params.get("AlarmRuleID")
        self._AlarmType = params.get("AlarmType")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyID = params.get("AccessKeyID")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._LastAlarmTime = params.get("LastAlarmTime")
        self._Status = params.get("Status")
        self._Date = params.get("Date")
        self._Tag = params.get("Tag")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._AppID = params.get("AppID")
        self._LeakEvidence = params.get("LeakEvidence")
        self._IsSupportEditWhiteAccount = params.get("IsSupportEditWhiteAccount")
        self._Evidence = params.get("Evidence")
        self._RuleKey = params.get("RuleKey")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarmCount(AbstractModel):
    r"""访问密钥告警数量

    """

    def __init__(self):
        r"""
        :param _ID: 访问密钥的ID
        :type ID: int
        :param _AccessKey: 访问密钥
        :type AccessKey: str
        :param _AlarmCount: 告警数量
        :type AlarmCount: int
        """
        self._ID = None
        self._AccessKey = None
        self._AlarmCount = None

    @property
    def ID(self):
        r"""访问密钥的ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AccessKey(self):
        r"""访问密钥
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AlarmCount(self):
        r"""告警数量
        :rtype: int
        """
        return self._AlarmCount

    @AlarmCount.setter
    def AlarmCount(self, AlarmCount):
        self._AlarmCount = AlarmCount


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AccessKey = params.get("AccessKey")
        self._AlarmCount = params.get("AlarmCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarmInfo(AbstractModel):
    r"""访问密钥资产告警信息

    """

    def __init__(self):
        r"""
        :param _Type: 告警类型/风险类型
告警类型：
0异常调用
1泄漏检测
2自定义

风险类型：
0：配置风险
1: 自定义风险
        :type Type: int
        :param _Count: 告警数量/风险数量
        :type Count: int
        """
        self._Type = None
        self._Count = None

    @property
    def Type(self):
        r"""告警类型/风险类型
告警类型：
0异常调用
1泄漏检测
2自定义

风险类型：
0：配置风险
1: 自定义风险
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""告警数量/风险数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAsset(AbstractModel):
    r"""访问密钥资产信息

    """

    def __init__(self):
        r"""
        :param _ID: AK 的id
        :type ID: int
        :param _Name: AK名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _AppID: 账号所属APPID
        :type AppID: int
        :param _Uin: 所属主账号Uin
        :type Uin: str
        :param _Nickname: 主账号昵称
        :type Nickname: str
        :param _SubUin: 所属子账号Uin
        :type SubUin: str
        :param _SubNickname: 所属子账号昵称
        :type SubNickname: str
        :param _Type: 0 主账号AK
1 子账号AK
2 临时密钥
        :type Type: int
        :param _Advice: 安全建议 枚举
0 正常
1 立即处理
2 建议加固
        :type Advice: int
        :param _AccessKeyAlarmList: 告警信息列表
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AccessKeyRiskList: 风险信息列表
        :type AccessKeyRiskList: list of AccessKeyAlarmInfo
        :param _IPCount: 源IP数量
        :type IPCount: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _LastAccessTime: 最近访问时间
        :type LastAccessTime: str
        :param _Status: AK状态 
0:禁用
1:已启用
2:已删除(已在cam侧删除，安全中心仍然存留之前的记录)
        :type Status: int
        :param _CheckStatus: 0 表示已检测
1 表示检测中
        :type CheckStatus: int
        :param _CloudType: 云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :type CloudType: int
        """
        self._ID = None
        self._Name = None
        self._Remark = None
        self._AppID = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._Advice = None
        self._AccessKeyAlarmList = None
        self._AccessKeyRiskList = None
        self._IPCount = None
        self._CreateTime = None
        self._LastAccessTime = None
        self._Status = None
        self._CheckStatus = None
        self._CloudType = None

    @property
    def ID(self):
        r"""AK 的id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""AK名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AppID(self):
        r"""账号所属APPID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""所属主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""主账号昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""所属子账号Uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""所属子账号昵称
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""0 主账号AK
1 子账号AK
2 临时密钥
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Advice(self):
        r"""安全建议 枚举
0 正常
1 立即处理
2 建议加固
        :rtype: int
        """
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def AccessKeyAlarmList(self):
        r"""告警信息列表
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AccessKeyRiskList(self):
        r"""风险信息列表
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyRiskList

    @AccessKeyRiskList.setter
    def AccessKeyRiskList(self, AccessKeyRiskList):
        self._AccessKeyRiskList = AccessKeyRiskList

    @property
    def IPCount(self):
        r"""源IP数量
        :rtype: int
        """
        return self._IPCount

    @IPCount.setter
    def IPCount(self, IPCount):
        self._IPCount = IPCount

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastAccessTime(self):
        r"""最近访问时间
        :rtype: str
        """
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def Status(self):
        r"""AK状态 
0:禁用
1:已启用
2:已删除(已在cam侧删除，安全中心仍然存留之前的记录)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CheckStatus(self):
        r"""0 表示已检测
1 表示检测中
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def CloudType(self):
        r"""云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._Advice = params.get("Advice")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AccessKeyRiskList") is not None:
            self._AccessKeyRiskList = []
            for item in params.get("AccessKeyRiskList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyRiskList.append(obj)
        self._IPCount = params.get("IPCount")
        self._CreateTime = params.get("CreateTime")
        self._LastAccessTime = params.get("LastAccessTime")
        self._Status = params.get("Status")
        self._CheckStatus = params.get("CheckStatus")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyRisk(AbstractModel):
    r"""访问密钥风险记录

    """

    def __init__(self):
        r"""
        :param _Name: 风险名称
        :type Name: str
        :param _Level: 风险等级
0-无效 1-提示 2-低危 3-中危 4-高危 5-严重
        :type Level: int
        :param _ID: 风险记录ID
        :type ID: int
        :param _RiskRuleID: 风险规则ID
        :type RiskRuleID: int
        :param _RiskType: 风险类型
0-配置风险
        :type RiskType: int
        :param _AccessKey: 访问密钥
        :type AccessKey: str
        :param _AccessKeyID: 访问密钥ID
        :type AccessKeyID: int
        :param _AccessKeyRemark: 访问密钥备注
        :type AccessKeyRemark: str
        :param _RiskTime: 风险检出时间
        :type RiskTime: str
        :param _Status: 风险状态
0-未处理 2-已忽略 3-已收敛
        :type Status: int
        :param _Tag: 风险标签
        :type Tag: list of str
        :param _Evidence: 风险证据
        :type Evidence: str
        :param _Description: 风险描述
        :type Description: str
        :param _Uin: 所属主账号Uin
        :type Uin: str
        :param _Nickname: 所属主账号昵称
        :type Nickname: str
        :param _SubUin: 所属子账号Uin
        :type SubUin: str
        :param _SubNickname: 所属子账号昵称
        :type SubNickname: str
        :param _Type: 账号类型
0 主账号AK 1子账号AK
2 临时密钥
        :type Type: int
        :param _CheckStatus: 检测状态
0表示 已检测
1表示 检测中
        :type CheckStatus: int
        :param _AppID: 所属appid
        :type AppID: int
        :param _QueryParam: 对应风险的查询参数
        :type QueryParam: str
        """
        self._Name = None
        self._Level = None
        self._ID = None
        self._RiskRuleID = None
        self._RiskType = None
        self._AccessKey = None
        self._AccessKeyID = None
        self._AccessKeyRemark = None
        self._RiskTime = None
        self._Status = None
        self._Tag = None
        self._Evidence = None
        self._Description = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._CheckStatus = None
        self._AppID = None
        self._QueryParam = None

    @property
    def Name(self):
        r"""风险名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        r"""风险等级
0-无效 1-提示 2-低危 3-中危 4-高危 5-严重
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def ID(self):
        r"""风险记录ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def RiskRuleID(self):
        r"""风险规则ID
        :rtype: int
        """
        return self._RiskRuleID

    @RiskRuleID.setter
    def RiskRuleID(self, RiskRuleID):
        self._RiskRuleID = RiskRuleID

    @property
    def RiskType(self):
        r"""风险类型
0-配置风险
        :rtype: int
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def AccessKey(self):
        r"""访问密钥
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyID(self):
        r"""访问密钥ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def AccessKeyRemark(self):
        r"""访问密钥备注
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def RiskTime(self):
        r"""风险检出时间
        :rtype: str
        """
        return self._RiskTime

    @RiskTime.setter
    def RiskTime(self, RiskTime):
        self._RiskTime = RiskTime

    @property
    def Status(self):
        r"""风险状态
0-未处理 2-已忽略 3-已收敛
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tag(self):
        r"""风险标签
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Evidence(self):
        r"""风险证据
        :rtype: str
        """
        return self._Evidence

    @Evidence.setter
    def Evidence(self, Evidence):
        self._Evidence = Evidence

    @property
    def Description(self):
        r"""风险描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Uin(self):
        r"""所属主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""所属主账号昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""所属子账号Uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""所属子账号昵称
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""账号类型
0 主账号AK 1子账号AK
2 临时密钥
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CheckStatus(self):
        r"""检测状态
0表示 已检测
1表示 检测中
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def AppID(self):
        r"""所属appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def QueryParam(self):
        r"""对应风险的查询参数
        :rtype: str
        """
        return self._QueryParam

    @QueryParam.setter
    def QueryParam(self, QueryParam):
        self._QueryParam = QueryParam


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._ID = params.get("ID")
        self._RiskRuleID = params.get("RiskRuleID")
        self._RiskType = params.get("RiskType")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyID = params.get("AccessKeyID")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._RiskTime = params.get("RiskTime")
        self._Status = params.get("Status")
        self._Tag = params.get("Tag")
        self._Evidence = params.get("Evidence")
        self._Description = params.get("Description")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._CheckStatus = params.get("CheckStatus")
        self._AppID = params.get("AppID")
        self._QueryParam = params.get("QueryParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyUser(AbstractModel):
    r"""访问密钥账号信息

    """

    def __init__(self):
        r"""
        :param _ID: 账号ID
        :type ID: int
        :param _Name: 账号名称
        :type Name: str
        :param _Type: 0 主账号 1子账号
        :type Type: int
        :param _AccessType: 访问方式
0 API
1 控制台与API
        :type AccessType: int
        :param _Advice: 安全建议 枚举 0 正常 1 立即处理 2 建议加固
        :type Advice: int
        :param _AccessKeyAlarmList: 告警信息列表
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AccessKeyRiskList: 风险信息列表
        :type AccessKeyRiskList: list of AccessKeyAlarmInfo
        :param _AppID: 账号所属APPID
        :type AppID: int
        :param _Nickname: 主账号昵称
        :type Nickname: str
        :param _SubNickname: 子账号昵称
        :type SubNickname: str
        :param _Uin: 账号所属主账号Uin
        :type Uin: str
        :param _SubUin: 账号自身uin，主账号时与主账号uin一致
        :type SubUin: str
        :param _LoginIP: 登录IP
        :type LoginIP: str
        :param _LoginLocation: 登录地址
        :type LoginLocation: str
        :param _LoginTime: 登录时间
        :type LoginTime: str
        :param _ISP: 运营商名称
        :type ISP: str
        :param _ActionFlag: 操作保护是否开启
0 未开启
1 已开启
        :type ActionFlag: int
        :param _LoginFlag: 登录保护是否开启
0 未开启
1 已开启
        :type LoginFlag: int
        :param _CheckStatus: 0 表示已检测 1 表示检测中
        :type CheckStatus: int
        :param _CloudType: 云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :type CloudType: int
        """
        self._ID = None
        self._Name = None
        self._Type = None
        self._AccessType = None
        self._Advice = None
        self._AccessKeyAlarmList = None
        self._AccessKeyRiskList = None
        self._AppID = None
        self._Nickname = None
        self._SubNickname = None
        self._Uin = None
        self._SubUin = None
        self._LoginIP = None
        self._LoginLocation = None
        self._LoginTime = None
        self._ISP = None
        self._ActionFlag = None
        self._LoginFlag = None
        self._CheckStatus = None
        self._CloudType = None

    @property
    def ID(self):
        r"""账号ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""账号名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""0 主账号 1子账号
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AccessType(self):
        r"""访问方式
0 API
1 控制台与API
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Advice(self):
        r"""安全建议 枚举 0 正常 1 立即处理 2 建议加固
        :rtype: int
        """
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def AccessKeyAlarmList(self):
        r"""告警信息列表
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AccessKeyRiskList(self):
        r"""风险信息列表
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyRiskList

    @AccessKeyRiskList.setter
    def AccessKeyRiskList(self, AccessKeyRiskList):
        self._AccessKeyRiskList = AccessKeyRiskList

    @property
    def AppID(self):
        r"""账号所属APPID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Nickname(self):
        r"""主账号昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubNickname(self):
        r"""子账号昵称
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Uin(self):
        r"""账号所属主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""账号自身uin，主账号时与主账号uin一致
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def LoginIP(self):
        r"""登录IP
        :rtype: str
        """
        return self._LoginIP

    @LoginIP.setter
    def LoginIP(self, LoginIP):
        self._LoginIP = LoginIP

    @property
    def LoginLocation(self):
        r"""登录地址
        :rtype: str
        """
        return self._LoginLocation

    @LoginLocation.setter
    def LoginLocation(self, LoginLocation):
        self._LoginLocation = LoginLocation

    @property
    def LoginTime(self):
        r"""登录时间
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def ISP(self):
        r"""运营商名称
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def ActionFlag(self):
        r"""操作保护是否开启
0 未开启
1 已开启
        :rtype: int
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def LoginFlag(self):
        r"""登录保护是否开启
0 未开启
1 已开启
        :rtype: int
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def CheckStatus(self):
        r"""0 表示已检测 1 表示检测中
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def CloudType(self):
        r"""云厂商类型 0:腾讯云 1:亚马逊云 2:微软云 3:谷歌云 4:阿里云 5:华为云
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._AccessType = params.get("AccessType")
        self._Advice = params.get("Advice")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AccessKeyRiskList") is not None:
            self._AccessKeyRiskList = []
            for item in params.get("AccessKeyRiskList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyRiskList.append(obj)
        self._AppID = params.get("AppID")
        self._Nickname = params.get("Nickname")
        self._SubNickname = params.get("SubNickname")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._LoginIP = params.get("LoginIP")
        self._LoginLocation = params.get("LoginLocation")
        self._LoginTime = params.get("LoginTime")
        self._ISP = params.get("ISP")
        self._ActionFlag = params.get("ActionFlag")
        self._LoginFlag = params.get("LoginFlag")
        self._CheckStatus = params.get("CheckStatus")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNewBindRoleUserRequest(AbstractModel):
    r"""AddNewBindRoleUser请求参数结构体

    """


class AddNewBindRoleUserResponse(AbstractModel):
    r"""AddNewBindRoleUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0成功，其他失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""0成功，其他失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class AlertExtraInfo(AbstractModel):
    r"""告警下拉字段

    """

    def __init__(self):
        r"""
        :param _RelateEvent: 相关攻击事件
        :type RelateEvent: :class:`tencentcloud.csip.v20221121.models.RelatedEvent`
        :param _LeakContent: 泄漏内容
        :type LeakContent: str
        :param _LeakAPI: 泄漏API
        :type LeakAPI: str
        :param _SecretID: secretID
        :type SecretID: str
        :param _Rule: 命中规则
        :type Rule: str
        :param _RuleDesc: 规则描述
        :type RuleDesc: str
        :param _ProtocolPort: 协议端口
        :type ProtocolPort: str
        :param _AttackContent: 攻击内容
        :type AttackContent: str
        :param _AttackIPProfile: 攻击IP画像
        :type AttackIPProfile: str
        :param _AttackIPTags: 攻击IP标签
        :type AttackIPTags: str
        :param _RequestMethod: 请求方式
        :type RequestMethod: str
        :param _HttpLog: HTTP日志
        :type HttpLog: str
        :param _AttackDomain: 被攻击域名
        :type AttackDomain: str
        :param _FilePath: 文件路径
        :type FilePath: str
        :param _UserAgent: user_agent
        :type UserAgent: str
        :param _RequestHeaders: 请求头
        :type RequestHeaders: str
        :param _LoginUserName: 登录用户名
        :type LoginUserName: str
        :param _VulnerabilityName: 漏洞名称
        :type VulnerabilityName: str
        :param _CVE: 公共漏洞和暴露
        :type CVE: str
        :param _ServiceProcess: 服务进程
        :type ServiceProcess: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小
        :type FileSize: str
        :param _FileMD5: 文件MD5
        :type FileMD5: str
        :param _FileLastAccessTime: 文件最近访问时间
        :type FileLastAccessTime: str
        :param _FileModifyTime: 文件修改时间
        :type FileModifyTime: str
        :param _RecentAccessTime: 最近访问时间
        :type RecentAccessTime: str
        :param _RecentModifyTime: 最近修改时间
        :type RecentModifyTime: str
        :param _VirusName: 病毒名
        :type VirusName: str
        :param _VirusFileTags: 病毒文件标签
        :type VirusFileTags: str
        :param _BehavioralCharacteristics: 行为特征
        :type BehavioralCharacteristics: str
        :param _ProcessNamePID: 进程名（PID）
        :type ProcessNamePID: str
        :param _ProcessPath: 进程路径
        :type ProcessPath: str
        :param _ProcessCommandLine: 进程命令行
        :type ProcessCommandLine: str
        :param _ProcessPermissions: 进程权限
        :type ProcessPermissions: str
        :param _ExecutedCommand: 执行命令
        :type ExecutedCommand: str
        :param _AffectedFileName: 受影响文件名
        :type AffectedFileName: str
        :param _DecoyPath: 诱饵路径
        :type DecoyPath: str
        :param _MaliciousProcessFileSize: 恶意进程文件大小
        :type MaliciousProcessFileSize: str
        :param _MaliciousProcessFileMD5: 恶意进程文件MD5
        :type MaliciousProcessFileMD5: str
        :param _MaliciousProcessNamePID: 恶意进程名（PID）
        :type MaliciousProcessNamePID: str
        :param _MaliciousProcessPath: 恶意进程路径
        :type MaliciousProcessPath: str
        :param _MaliciousProcessStartTime: 恶意进程启动时间
        :type MaliciousProcessStartTime: str
        :param _CommandContent: 命令内容
        :type CommandContent: str
        :param _StartupUser: 启动用户
        :type StartupUser: str
        :param _UserGroup: 用户所属组
        :type UserGroup: str
        :param _NewPermissions: 新增权限
        :type NewPermissions: str
        :param _ParentProcess: 父进程
        :type ParentProcess: str
        :param _ClassName: 类名
        :type ClassName: str
        :param _ClassLoader: 所属类加载器
        :type ClassLoader: str
        :param _ClassFileSize: 类文件大小
        :type ClassFileSize: str
        :param _ClassFileMD5: 类文件MD5
        :type ClassFileMD5: str
        :param _ParentClassName: 父类名
        :type ParentClassName: str
        :param _InheritedInterface: 继承接口
        :type InheritedInterface: str
        :param _Comment: 注释
        :type Comment: str
        :param _PayloadContent: 载荷内容
        :type PayloadContent: str
        :param _CallbackAddressPortrait: 回连地址画像
        :type CallbackAddressPortrait: str
        :param _CallbackAddressTag: 回连地址标签
        :type CallbackAddressTag: str
        :param _ProcessMD5: 进程MD5
        :type ProcessMD5: str
        :param _FilePermission: 文件权限
        :type FilePermission: str
        :param _FromLogAnalysisData: 来源于日志分析的信息字段
        :type FromLogAnalysisData: list of KeyValue
        :param _HitProbe: 命中探针
        :type HitProbe: str
        :param _HitHoneyPot: 命中蜜罐

        :type HitHoneyPot: str
        :param _CommandList: 命令列表
        :type CommandList: str
        :param _AttackEventDesc: 攻击事件描述

        :type AttackEventDesc: str
        :param _ProcessInfo: 进程信息
        :type ProcessInfo: str
        :param _UserNameAndPwd: 使用用户名&密码
        :type UserNameAndPwd: str
        :param _StrategyID: 主机防护策略ID
        :type StrategyID: str
        :param _StrategyName: 主机防护策略名称
        :type StrategyName: str
        :param _HitStrategy: 主机防护命中策略，是策略ID和策略名称的组合
        :type HitStrategy: str
        :param _ProcessName: 进程名
        :type ProcessName: str
        :param _PID: PID
        :type PID: str
        :param _PodName: 容器Pod名
        :type PodName: str
        :param _PodID: 容器PodID
        :type PodID: str
        :param _Response: Http响应
        :type Response: str
        :param _SystemCall: 系统调用
        :type SystemCall: str
        :param _Verb: 操作类型verb
        :type Verb: str
        :param _LogID: 日志ID
        :type LogID: str
        :param _Different: 变更内容
        :type Different: str
        :param _EventType: 事件类型
        :type EventType: str
        :param _Description: 事件描述
        :type Description: str
        :param _TargetAddress: 目标地址(容器反弹shell)
        :type TargetAddress: str
        :param _MaliciousRequestDomain: 恶意请求域名(容器恶意外联)
        :type MaliciousRequestDomain: str
        :param _RuleType: 规则类型(容器K8sAPI异常请求)
        :type RuleType: str
        :param _RequestURI: 请求资源(容器K8sAPI异常请求)
        :type RequestURI: str
        :param _RequestUser: 发起请求用户(容器K8sAPI异常请求)
        :type RequestUser: str
        :param _RequestObject: 请求对象(容器K8sAPI异常请求)
        :type RequestObject: str
        :param _ResponseObject: 响应对象(容器K8sAPI异常请求)
        :type ResponseObject: str
        :param _FileType: 文件类型(容器文件篡改)
        :type FileType: str
        :param _TIType: 标签特征(容器恶意外联)
        :type TIType: str
        :param _SourceIP: 来源IP(容器K8sAPI异常请求)
        :type SourceIP: str
        """
        self._RelateEvent = None
        self._LeakContent = None
        self._LeakAPI = None
        self._SecretID = None
        self._Rule = None
        self._RuleDesc = None
        self._ProtocolPort = None
        self._AttackContent = None
        self._AttackIPProfile = None
        self._AttackIPTags = None
        self._RequestMethod = None
        self._HttpLog = None
        self._AttackDomain = None
        self._FilePath = None
        self._UserAgent = None
        self._RequestHeaders = None
        self._LoginUserName = None
        self._VulnerabilityName = None
        self._CVE = None
        self._ServiceProcess = None
        self._FileName = None
        self._FileSize = None
        self._FileMD5 = None
        self._FileLastAccessTime = None
        self._FileModifyTime = None
        self._RecentAccessTime = None
        self._RecentModifyTime = None
        self._VirusName = None
        self._VirusFileTags = None
        self._BehavioralCharacteristics = None
        self._ProcessNamePID = None
        self._ProcessPath = None
        self._ProcessCommandLine = None
        self._ProcessPermissions = None
        self._ExecutedCommand = None
        self._AffectedFileName = None
        self._DecoyPath = None
        self._MaliciousProcessFileSize = None
        self._MaliciousProcessFileMD5 = None
        self._MaliciousProcessNamePID = None
        self._MaliciousProcessPath = None
        self._MaliciousProcessStartTime = None
        self._CommandContent = None
        self._StartupUser = None
        self._UserGroup = None
        self._NewPermissions = None
        self._ParentProcess = None
        self._ClassName = None
        self._ClassLoader = None
        self._ClassFileSize = None
        self._ClassFileMD5 = None
        self._ParentClassName = None
        self._InheritedInterface = None
        self._Comment = None
        self._PayloadContent = None
        self._CallbackAddressPortrait = None
        self._CallbackAddressTag = None
        self._ProcessMD5 = None
        self._FilePermission = None
        self._FromLogAnalysisData = None
        self._HitProbe = None
        self._HitHoneyPot = None
        self._CommandList = None
        self._AttackEventDesc = None
        self._ProcessInfo = None
        self._UserNameAndPwd = None
        self._StrategyID = None
        self._StrategyName = None
        self._HitStrategy = None
        self._ProcessName = None
        self._PID = None
        self._PodName = None
        self._PodID = None
        self._Response = None
        self._SystemCall = None
        self._Verb = None
        self._LogID = None
        self._Different = None
        self._EventType = None
        self._Description = None
        self._TargetAddress = None
        self._MaliciousRequestDomain = None
        self._RuleType = None
        self._RequestURI = None
        self._RequestUser = None
        self._RequestObject = None
        self._ResponseObject = None
        self._FileType = None
        self._TIType = None
        self._SourceIP = None

    @property
    def RelateEvent(self):
        r"""相关攻击事件
        :rtype: :class:`tencentcloud.csip.v20221121.models.RelatedEvent`
        """
        return self._RelateEvent

    @RelateEvent.setter
    def RelateEvent(self, RelateEvent):
        self._RelateEvent = RelateEvent

    @property
    def LeakContent(self):
        r"""泄漏内容
        :rtype: str
        """
        return self._LeakContent

    @LeakContent.setter
    def LeakContent(self, LeakContent):
        self._LeakContent = LeakContent

    @property
    def LeakAPI(self):
        r"""泄漏API
        :rtype: str
        """
        return self._LeakAPI

    @LeakAPI.setter
    def LeakAPI(self, LeakAPI):
        self._LeakAPI = LeakAPI

    @property
    def SecretID(self):
        r"""secretID
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def Rule(self):
        r"""命中规则
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RuleDesc(self):
        r"""规则描述
        :rtype: str
        """
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def ProtocolPort(self):
        r"""协议端口
        :rtype: str
        """
        return self._ProtocolPort

    @ProtocolPort.setter
    def ProtocolPort(self, ProtocolPort):
        self._ProtocolPort = ProtocolPort

    @property
    def AttackContent(self):
        r"""攻击内容
        :rtype: str
        """
        return self._AttackContent

    @AttackContent.setter
    def AttackContent(self, AttackContent):
        self._AttackContent = AttackContent

    @property
    def AttackIPProfile(self):
        r"""攻击IP画像
        :rtype: str
        """
        return self._AttackIPProfile

    @AttackIPProfile.setter
    def AttackIPProfile(self, AttackIPProfile):
        self._AttackIPProfile = AttackIPProfile

    @property
    def AttackIPTags(self):
        r"""攻击IP标签
        :rtype: str
        """
        return self._AttackIPTags

    @AttackIPTags.setter
    def AttackIPTags(self, AttackIPTags):
        self._AttackIPTags = AttackIPTags

    @property
    def RequestMethod(self):
        r"""请求方式
        :rtype: str
        """
        return self._RequestMethod

    @RequestMethod.setter
    def RequestMethod(self, RequestMethod):
        self._RequestMethod = RequestMethod

    @property
    def HttpLog(self):
        r"""HTTP日志
        :rtype: str
        """
        return self._HttpLog

    @HttpLog.setter
    def HttpLog(self, HttpLog):
        self._HttpLog = HttpLog

    @property
    def AttackDomain(self):
        r"""被攻击域名
        :rtype: str
        """
        return self._AttackDomain

    @AttackDomain.setter
    def AttackDomain(self, AttackDomain):
        self._AttackDomain = AttackDomain

    @property
    def FilePath(self):
        r"""文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def UserAgent(self):
        r"""user_agent
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def RequestHeaders(self):
        r"""请求头
        :rtype: str
        """
        return self._RequestHeaders

    @RequestHeaders.setter
    def RequestHeaders(self, RequestHeaders):
        self._RequestHeaders = RequestHeaders

    @property
    def LoginUserName(self):
        r"""登录用户名
        :rtype: str
        """
        return self._LoginUserName

    @LoginUserName.setter
    def LoginUserName(self, LoginUserName):
        self._LoginUserName = LoginUserName

    @property
    def VulnerabilityName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VulnerabilityName

    @VulnerabilityName.setter
    def VulnerabilityName(self, VulnerabilityName):
        self._VulnerabilityName = VulnerabilityName

    @property
    def CVE(self):
        r"""公共漏洞和暴露
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def ServiceProcess(self):
        r"""服务进程
        :rtype: str
        """
        return self._ServiceProcess

    @ServiceProcess.setter
    def ServiceProcess(self, ServiceProcess):
        self._ServiceProcess = ServiceProcess

    @property
    def FileName(self):
        r"""文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""文件大小
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileMD5(self):
        r"""文件MD5
        :rtype: str
        """
        return self._FileMD5

    @FileMD5.setter
    def FileMD5(self, FileMD5):
        self._FileMD5 = FileMD5

    @property
    def FileLastAccessTime(self):
        r"""文件最近访问时间
        :rtype: str
        """
        return self._FileLastAccessTime

    @FileLastAccessTime.setter
    def FileLastAccessTime(self, FileLastAccessTime):
        self._FileLastAccessTime = FileLastAccessTime

    @property
    def FileModifyTime(self):
        r"""文件修改时间
        :rtype: str
        """
        return self._FileModifyTime

    @FileModifyTime.setter
    def FileModifyTime(self, FileModifyTime):
        self._FileModifyTime = FileModifyTime

    @property
    def RecentAccessTime(self):
        r"""最近访问时间
        :rtype: str
        """
        return self._RecentAccessTime

    @RecentAccessTime.setter
    def RecentAccessTime(self, RecentAccessTime):
        self._RecentAccessTime = RecentAccessTime

    @property
    def RecentModifyTime(self):
        r"""最近修改时间
        :rtype: str
        """
        return self._RecentModifyTime

    @RecentModifyTime.setter
    def RecentModifyTime(self, RecentModifyTime):
        self._RecentModifyTime = RecentModifyTime

    @property
    def VirusName(self):
        r"""病毒名
        :rtype: str
        """
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def VirusFileTags(self):
        r"""病毒文件标签
        :rtype: str
        """
        return self._VirusFileTags

    @VirusFileTags.setter
    def VirusFileTags(self, VirusFileTags):
        self._VirusFileTags = VirusFileTags

    @property
    def BehavioralCharacteristics(self):
        r"""行为特征
        :rtype: str
        """
        return self._BehavioralCharacteristics

    @BehavioralCharacteristics.setter
    def BehavioralCharacteristics(self, BehavioralCharacteristics):
        self._BehavioralCharacteristics = BehavioralCharacteristics

    @property
    def ProcessNamePID(self):
        r"""进程名（PID）
        :rtype: str
        """
        return self._ProcessNamePID

    @ProcessNamePID.setter
    def ProcessNamePID(self, ProcessNamePID):
        self._ProcessNamePID = ProcessNamePID

    @property
    def ProcessPath(self):
        r"""进程路径
        :rtype: str
        """
        return self._ProcessPath

    @ProcessPath.setter
    def ProcessPath(self, ProcessPath):
        self._ProcessPath = ProcessPath

    @property
    def ProcessCommandLine(self):
        r"""进程命令行
        :rtype: str
        """
        return self._ProcessCommandLine

    @ProcessCommandLine.setter
    def ProcessCommandLine(self, ProcessCommandLine):
        self._ProcessCommandLine = ProcessCommandLine

    @property
    def ProcessPermissions(self):
        r"""进程权限
        :rtype: str
        """
        return self._ProcessPermissions

    @ProcessPermissions.setter
    def ProcessPermissions(self, ProcessPermissions):
        self._ProcessPermissions = ProcessPermissions

    @property
    def ExecutedCommand(self):
        r"""执行命令
        :rtype: str
        """
        return self._ExecutedCommand

    @ExecutedCommand.setter
    def ExecutedCommand(self, ExecutedCommand):
        self._ExecutedCommand = ExecutedCommand

    @property
    def AffectedFileName(self):
        r"""受影响文件名
        :rtype: str
        """
        return self._AffectedFileName

    @AffectedFileName.setter
    def AffectedFileName(self, AffectedFileName):
        self._AffectedFileName = AffectedFileName

    @property
    def DecoyPath(self):
        r"""诱饵路径
        :rtype: str
        """
        return self._DecoyPath

    @DecoyPath.setter
    def DecoyPath(self, DecoyPath):
        self._DecoyPath = DecoyPath

    @property
    def MaliciousProcessFileSize(self):
        r"""恶意进程文件大小
        :rtype: str
        """
        return self._MaliciousProcessFileSize

    @MaliciousProcessFileSize.setter
    def MaliciousProcessFileSize(self, MaliciousProcessFileSize):
        self._MaliciousProcessFileSize = MaliciousProcessFileSize

    @property
    def MaliciousProcessFileMD5(self):
        r"""恶意进程文件MD5
        :rtype: str
        """
        return self._MaliciousProcessFileMD5

    @MaliciousProcessFileMD5.setter
    def MaliciousProcessFileMD5(self, MaliciousProcessFileMD5):
        self._MaliciousProcessFileMD5 = MaliciousProcessFileMD5

    @property
    def MaliciousProcessNamePID(self):
        r"""恶意进程名（PID）
        :rtype: str
        """
        return self._MaliciousProcessNamePID

    @MaliciousProcessNamePID.setter
    def MaliciousProcessNamePID(self, MaliciousProcessNamePID):
        self._MaliciousProcessNamePID = MaliciousProcessNamePID

    @property
    def MaliciousProcessPath(self):
        r"""恶意进程路径
        :rtype: str
        """
        return self._MaliciousProcessPath

    @MaliciousProcessPath.setter
    def MaliciousProcessPath(self, MaliciousProcessPath):
        self._MaliciousProcessPath = MaliciousProcessPath

    @property
    def MaliciousProcessStartTime(self):
        r"""恶意进程启动时间
        :rtype: str
        """
        return self._MaliciousProcessStartTime

    @MaliciousProcessStartTime.setter
    def MaliciousProcessStartTime(self, MaliciousProcessStartTime):
        self._MaliciousProcessStartTime = MaliciousProcessStartTime

    @property
    def CommandContent(self):
        r"""命令内容
        :rtype: str
        """
        return self._CommandContent

    @CommandContent.setter
    def CommandContent(self, CommandContent):
        self._CommandContent = CommandContent

    @property
    def StartupUser(self):
        r"""启动用户
        :rtype: str
        """
        return self._StartupUser

    @StartupUser.setter
    def StartupUser(self, StartupUser):
        self._StartupUser = StartupUser

    @property
    def UserGroup(self):
        r"""用户所属组
        :rtype: str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def NewPermissions(self):
        r"""新增权限
        :rtype: str
        """
        return self._NewPermissions

    @NewPermissions.setter
    def NewPermissions(self, NewPermissions):
        self._NewPermissions = NewPermissions

    @property
    def ParentProcess(self):
        r"""父进程
        :rtype: str
        """
        return self._ParentProcess

    @ParentProcess.setter
    def ParentProcess(self, ParentProcess):
        self._ParentProcess = ParentProcess

    @property
    def ClassName(self):
        r"""类名
        :rtype: str
        """
        return self._ClassName

    @ClassName.setter
    def ClassName(self, ClassName):
        self._ClassName = ClassName

    @property
    def ClassLoader(self):
        r"""所属类加载器
        :rtype: str
        """
        return self._ClassLoader

    @ClassLoader.setter
    def ClassLoader(self, ClassLoader):
        self._ClassLoader = ClassLoader

    @property
    def ClassFileSize(self):
        r"""类文件大小
        :rtype: str
        """
        return self._ClassFileSize

    @ClassFileSize.setter
    def ClassFileSize(self, ClassFileSize):
        self._ClassFileSize = ClassFileSize

    @property
    def ClassFileMD5(self):
        r"""类文件MD5
        :rtype: str
        """
        return self._ClassFileMD5

    @ClassFileMD5.setter
    def ClassFileMD5(self, ClassFileMD5):
        self._ClassFileMD5 = ClassFileMD5

    @property
    def ParentClassName(self):
        r"""父类名
        :rtype: str
        """
        return self._ParentClassName

    @ParentClassName.setter
    def ParentClassName(self, ParentClassName):
        self._ParentClassName = ParentClassName

    @property
    def InheritedInterface(self):
        r"""继承接口
        :rtype: str
        """
        return self._InheritedInterface

    @InheritedInterface.setter
    def InheritedInterface(self, InheritedInterface):
        self._InheritedInterface = InheritedInterface

    @property
    def Comment(self):
        r"""注释
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def PayloadContent(self):
        r"""载荷内容
        :rtype: str
        """
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def CallbackAddressPortrait(self):
        r"""回连地址画像
        :rtype: str
        """
        return self._CallbackAddressPortrait

    @CallbackAddressPortrait.setter
    def CallbackAddressPortrait(self, CallbackAddressPortrait):
        self._CallbackAddressPortrait = CallbackAddressPortrait

    @property
    def CallbackAddressTag(self):
        r"""回连地址标签
        :rtype: str
        """
        return self._CallbackAddressTag

    @CallbackAddressTag.setter
    def CallbackAddressTag(self, CallbackAddressTag):
        self._CallbackAddressTag = CallbackAddressTag

    @property
    def ProcessMD5(self):
        r"""进程MD5
        :rtype: str
        """
        return self._ProcessMD5

    @ProcessMD5.setter
    def ProcessMD5(self, ProcessMD5):
        self._ProcessMD5 = ProcessMD5

    @property
    def FilePermission(self):
        r"""文件权限
        :rtype: str
        """
        return self._FilePermission

    @FilePermission.setter
    def FilePermission(self, FilePermission):
        self._FilePermission = FilePermission

    @property
    def FromLogAnalysisData(self):
        r"""来源于日志分析的信息字段
        :rtype: list of KeyValue
        """
        return self._FromLogAnalysisData

    @FromLogAnalysisData.setter
    def FromLogAnalysisData(self, FromLogAnalysisData):
        self._FromLogAnalysisData = FromLogAnalysisData

    @property
    def HitProbe(self):
        r"""命中探针
        :rtype: str
        """
        return self._HitProbe

    @HitProbe.setter
    def HitProbe(self, HitProbe):
        self._HitProbe = HitProbe

    @property
    def HitHoneyPot(self):
        r"""命中蜜罐

        :rtype: str
        """
        return self._HitHoneyPot

    @HitHoneyPot.setter
    def HitHoneyPot(self, HitHoneyPot):
        self._HitHoneyPot = HitHoneyPot

    @property
    def CommandList(self):
        r"""命令列表
        :rtype: str
        """
        return self._CommandList

    @CommandList.setter
    def CommandList(self, CommandList):
        self._CommandList = CommandList

    @property
    def AttackEventDesc(self):
        r"""攻击事件描述

        :rtype: str
        """
        return self._AttackEventDesc

    @AttackEventDesc.setter
    def AttackEventDesc(self, AttackEventDesc):
        self._AttackEventDesc = AttackEventDesc

    @property
    def ProcessInfo(self):
        r"""进程信息
        :rtype: str
        """
        return self._ProcessInfo

    @ProcessInfo.setter
    def ProcessInfo(self, ProcessInfo):
        self._ProcessInfo = ProcessInfo

    @property
    def UserNameAndPwd(self):
        r"""使用用户名&密码
        :rtype: str
        """
        return self._UserNameAndPwd

    @UserNameAndPwd.setter
    def UserNameAndPwd(self, UserNameAndPwd):
        self._UserNameAndPwd = UserNameAndPwd

    @property
    def StrategyID(self):
        r"""主机防护策略ID
        :rtype: str
        """
        return self._StrategyID

    @StrategyID.setter
    def StrategyID(self, StrategyID):
        self._StrategyID = StrategyID

    @property
    def StrategyName(self):
        r"""主机防护策略名称
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def HitStrategy(self):
        r"""主机防护命中策略，是策略ID和策略名称的组合
        :rtype: str
        """
        return self._HitStrategy

    @HitStrategy.setter
    def HitStrategy(self, HitStrategy):
        self._HitStrategy = HitStrategy

    @property
    def ProcessName(self):
        r"""进程名
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def PID(self):
        r"""PID
        :rtype: str
        """
        return self._PID

    @PID.setter
    def PID(self, PID):
        self._PID = PID

    @property
    def PodName(self):
        r"""容器Pod名
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def PodID(self):
        r"""容器PodID
        :rtype: str
        """
        return self._PodID

    @PodID.setter
    def PodID(self, PodID):
        self._PodID = PodID

    @property
    def Response(self):
        r"""Http响应
        :rtype: str
        """
        return self._Response

    @Response.setter
    def Response(self, Response):
        self._Response = Response

    @property
    def SystemCall(self):
        r"""系统调用
        :rtype: str
        """
        return self._SystemCall

    @SystemCall.setter
    def SystemCall(self, SystemCall):
        self._SystemCall = SystemCall

    @property
    def Verb(self):
        r"""操作类型verb
        :rtype: str
        """
        return self._Verb

    @Verb.setter
    def Verb(self, Verb):
        self._Verb = Verb

    @property
    def LogID(self):
        r"""日志ID
        :rtype: str
        """
        return self._LogID

    @LogID.setter
    def LogID(self, LogID):
        self._LogID = LogID

    @property
    def Different(self):
        r"""变更内容
        :rtype: str
        """
        return self._Different

    @Different.setter
    def Different(self, Different):
        self._Different = Different

    @property
    def EventType(self):
        r"""事件类型
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Description(self):
        r"""事件描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TargetAddress(self):
        r"""目标地址(容器反弹shell)
        :rtype: str
        """
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def MaliciousRequestDomain(self):
        r"""恶意请求域名(容器恶意外联)
        :rtype: str
        """
        return self._MaliciousRequestDomain

    @MaliciousRequestDomain.setter
    def MaliciousRequestDomain(self, MaliciousRequestDomain):
        self._MaliciousRequestDomain = MaliciousRequestDomain

    @property
    def RuleType(self):
        r"""规则类型(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RequestURI(self):
        r"""请求资源(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._RequestURI

    @RequestURI.setter
    def RequestURI(self, RequestURI):
        self._RequestURI = RequestURI

    @property
    def RequestUser(self):
        r"""发起请求用户(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._RequestUser

    @RequestUser.setter
    def RequestUser(self, RequestUser):
        self._RequestUser = RequestUser

    @property
    def RequestObject(self):
        r"""请求对象(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._RequestObject

    @RequestObject.setter
    def RequestObject(self, RequestObject):
        self._RequestObject = RequestObject

    @property
    def ResponseObject(self):
        r"""响应对象(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._ResponseObject

    @ResponseObject.setter
    def ResponseObject(self, ResponseObject):
        self._ResponseObject = ResponseObject

    @property
    def FileType(self):
        r"""文件类型(容器文件篡改)
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def TIType(self):
        r"""标签特征(容器恶意外联)
        :rtype: str
        """
        return self._TIType

    @TIType.setter
    def TIType(self, TIType):
        self._TIType = TIType

    @property
    def SourceIP(self):
        r"""来源IP(容器K8sAPI异常请求)
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP


    def _deserialize(self, params):
        if params.get("RelateEvent") is not None:
            self._RelateEvent = RelatedEvent()
            self._RelateEvent._deserialize(params.get("RelateEvent"))
        self._LeakContent = params.get("LeakContent")
        self._LeakAPI = params.get("LeakAPI")
        self._SecretID = params.get("SecretID")
        self._Rule = params.get("Rule")
        self._RuleDesc = params.get("RuleDesc")
        self._ProtocolPort = params.get("ProtocolPort")
        self._AttackContent = params.get("AttackContent")
        self._AttackIPProfile = params.get("AttackIPProfile")
        self._AttackIPTags = params.get("AttackIPTags")
        self._RequestMethod = params.get("RequestMethod")
        self._HttpLog = params.get("HttpLog")
        self._AttackDomain = params.get("AttackDomain")
        self._FilePath = params.get("FilePath")
        self._UserAgent = params.get("UserAgent")
        self._RequestHeaders = params.get("RequestHeaders")
        self._LoginUserName = params.get("LoginUserName")
        self._VulnerabilityName = params.get("VulnerabilityName")
        self._CVE = params.get("CVE")
        self._ServiceProcess = params.get("ServiceProcess")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileMD5 = params.get("FileMD5")
        self._FileLastAccessTime = params.get("FileLastAccessTime")
        self._FileModifyTime = params.get("FileModifyTime")
        self._RecentAccessTime = params.get("RecentAccessTime")
        self._RecentModifyTime = params.get("RecentModifyTime")
        self._VirusName = params.get("VirusName")
        self._VirusFileTags = params.get("VirusFileTags")
        self._BehavioralCharacteristics = params.get("BehavioralCharacteristics")
        self._ProcessNamePID = params.get("ProcessNamePID")
        self._ProcessPath = params.get("ProcessPath")
        self._ProcessCommandLine = params.get("ProcessCommandLine")
        self._ProcessPermissions = params.get("ProcessPermissions")
        self._ExecutedCommand = params.get("ExecutedCommand")
        self._AffectedFileName = params.get("AffectedFileName")
        self._DecoyPath = params.get("DecoyPath")
        self._MaliciousProcessFileSize = params.get("MaliciousProcessFileSize")
        self._MaliciousProcessFileMD5 = params.get("MaliciousProcessFileMD5")
        self._MaliciousProcessNamePID = params.get("MaliciousProcessNamePID")
        self._MaliciousProcessPath = params.get("MaliciousProcessPath")
        self._MaliciousProcessStartTime = params.get("MaliciousProcessStartTime")
        self._CommandContent = params.get("CommandContent")
        self._StartupUser = params.get("StartupUser")
        self._UserGroup = params.get("UserGroup")
        self._NewPermissions = params.get("NewPermissions")
        self._ParentProcess = params.get("ParentProcess")
        self._ClassName = params.get("ClassName")
        self._ClassLoader = params.get("ClassLoader")
        self._ClassFileSize = params.get("ClassFileSize")
        self._ClassFileMD5 = params.get("ClassFileMD5")
        self._ParentClassName = params.get("ParentClassName")
        self._InheritedInterface = params.get("InheritedInterface")
        self._Comment = params.get("Comment")
        self._PayloadContent = params.get("PayloadContent")
        self._CallbackAddressPortrait = params.get("CallbackAddressPortrait")
        self._CallbackAddressTag = params.get("CallbackAddressTag")
        self._ProcessMD5 = params.get("ProcessMD5")
        self._FilePermission = params.get("FilePermission")
        if params.get("FromLogAnalysisData") is not None:
            self._FromLogAnalysisData = []
            for item in params.get("FromLogAnalysisData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FromLogAnalysisData.append(obj)
        self._HitProbe = params.get("HitProbe")
        self._HitHoneyPot = params.get("HitHoneyPot")
        self._CommandList = params.get("CommandList")
        self._AttackEventDesc = params.get("AttackEventDesc")
        self._ProcessInfo = params.get("ProcessInfo")
        self._UserNameAndPwd = params.get("UserNameAndPwd")
        self._StrategyID = params.get("StrategyID")
        self._StrategyName = params.get("StrategyName")
        self._HitStrategy = params.get("HitStrategy")
        self._ProcessName = params.get("ProcessName")
        self._PID = params.get("PID")
        self._PodName = params.get("PodName")
        self._PodID = params.get("PodID")
        self._Response = params.get("Response")
        self._SystemCall = params.get("SystemCall")
        self._Verb = params.get("Verb")
        self._LogID = params.get("LogID")
        self._Different = params.get("Different")
        self._EventType = params.get("EventType")
        self._Description = params.get("Description")
        self._TargetAddress = params.get("TargetAddress")
        self._MaliciousRequestDomain = params.get("MaliciousRequestDomain")
        self._RuleType = params.get("RuleType")
        self._RequestURI = params.get("RequestURI")
        self._RequestUser = params.get("RequestUser")
        self._RequestObject = params.get("RequestObject")
        self._ResponseObject = params.get("ResponseObject")
        self._FileType = params.get("FileType")
        self._TIType = params.get("TIType")
        self._SourceIP = params.get("SourceIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertInfo(AbstractModel):
    r"""告警中心全量告警列表数据

    """

    def __init__(self):
        r"""
        :param _ID: 告警ID
        :type ID: str
        :param _Name: 告警名称
        :type Name: str
        :param _Source: 告警来源
CFW:云防火墙
WAF:Web应用防火墙
CWP:主机安全
CSIP:云安全中心
        :type Source: str
        :param _Level: 告警等级
1:提示
2:低危
3:中危
4:高危
5:严重
        :type Level: int
        :param _Attacker: 攻击者
        :type Attacker: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        :param _Victim: 受害者
        :type Victim: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        :param _EvidenceData: 证据数据(例如攻击内容等，base64编码)
        :type EvidenceData: str
        :param _EvidenceLocation: 证据位置(例如协议端口)
        :type EvidenceLocation: str
        :param _EvidencePath: 证据路径
        :type EvidencePath: str
        :param _CreateTime: 首次告警时间
        :type CreateTime: str
        :param _UpdateTime: 最近告警时间
        :type UpdateTime: str
        :param _Count: 告警次数
        :type Count: int
        :param _UrgentSuggestion: 紧急缓解建议
        :type UrgentSuggestion: str
        :param _RemediationSuggestion: 根治建议
        :type RemediationSuggestion: str
        :param _Status: 处理状态
0：未处置，1：已忽略，2：已处置
        :type Status: int
        :param _ProcessType: 告警处理类型
        :type ProcessType: str
        :param _Type: 告警大类
        :type Type: str
        :param _SubType: 告警小类
        :type SubType: str
        :param _ExtraInfo: 下拉字段
        :type ExtraInfo: :class:`tencentcloud.csip.v20221121.models.AlertExtraInfo`
        :param _Key: 聚合字段
        :type Key: str
        :param _Date: 告警日期
        :type Date: str
        :param _AppID: appid
        :type AppID: str
        :param _NickName: 账户名称
        :type NickName: str
        :param _Uin: 账户ID
        :type Uin: str
        :param _Action: 行为
        :type Action: int
        :param _RiskInvestigation: 风险排查
        :type RiskInvestigation: str
        :param _RiskTreatment: 风险处置
        :type RiskTreatment: str
        :param _LogType: 日志类型
        :type LogType: str
        :param _LogSearch: 语句检索
        :type LogSearch: str
        """
        self._ID = None
        self._Name = None
        self._Source = None
        self._Level = None
        self._Attacker = None
        self._Victim = None
        self._EvidenceData = None
        self._EvidenceLocation = None
        self._EvidencePath = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Count = None
        self._UrgentSuggestion = None
        self._RemediationSuggestion = None
        self._Status = None
        self._ProcessType = None
        self._Type = None
        self._SubType = None
        self._ExtraInfo = None
        self._Key = None
        self._Date = None
        self._AppID = None
        self._NickName = None
        self._Uin = None
        self._Action = None
        self._RiskInvestigation = None
        self._RiskTreatment = None
        self._LogType = None
        self._LogSearch = None

    @property
    def ID(self):
        r"""告警ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""告警名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        r"""告警来源
CFW:云防火墙
WAF:Web应用防火墙
CWP:主机安全
CSIP:云安全中心
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Level(self):
        r"""告警等级
1:提示
2:低危
3:中危
4:高危
5:严重
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Attacker(self):
        r"""攻击者
        :rtype: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        """
        return self._Attacker

    @Attacker.setter
    def Attacker(self, Attacker):
        self._Attacker = Attacker

    @property
    def Victim(self):
        r"""受害者
        :rtype: :class:`tencentcloud.csip.v20221121.models.RoleInfo`
        """
        return self._Victim

    @Victim.setter
    def Victim(self, Victim):
        self._Victim = Victim

    @property
    def EvidenceData(self):
        r"""证据数据(例如攻击内容等，base64编码)
        :rtype: str
        """
        return self._EvidenceData

    @EvidenceData.setter
    def EvidenceData(self, EvidenceData):
        self._EvidenceData = EvidenceData

    @property
    def EvidenceLocation(self):
        r"""证据位置(例如协议端口)
        :rtype: str
        """
        return self._EvidenceLocation

    @EvidenceLocation.setter
    def EvidenceLocation(self, EvidenceLocation):
        self._EvidenceLocation = EvidenceLocation

    @property
    def EvidencePath(self):
        r"""证据路径
        :rtype: str
        """
        return self._EvidencePath

    @EvidencePath.setter
    def EvidencePath(self, EvidencePath):
        self._EvidencePath = EvidencePath

    @property
    def CreateTime(self):
        r"""首次告警时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最近告警时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Count(self):
        r"""告警次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def UrgentSuggestion(self):
        r"""紧急缓解建议
        :rtype: str
        """
        return self._UrgentSuggestion

    @UrgentSuggestion.setter
    def UrgentSuggestion(self, UrgentSuggestion):
        self._UrgentSuggestion = UrgentSuggestion

    @property
    def RemediationSuggestion(self):
        r"""根治建议
        :rtype: str
        """
        return self._RemediationSuggestion

    @RemediationSuggestion.setter
    def RemediationSuggestion(self, RemediationSuggestion):
        self._RemediationSuggestion = RemediationSuggestion

    @property
    def Status(self):
        r"""处理状态
0：未处置，1：已忽略，2：已处置
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProcessType(self):
        r"""告警处理类型
        :rtype: str
        """
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def Type(self):
        r"""告警大类
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubType(self):
        r"""告警小类
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def ExtraInfo(self):
        r"""下拉字段
        :rtype: :class:`tencentcloud.csip.v20221121.models.AlertExtraInfo`
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def Key(self):
        r"""聚合字段
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Date(self):
        r"""告警日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        r"""appid
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def NickName(self):
        r"""账户名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Uin(self):
        r"""账户ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Action(self):
        r"""行为
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RiskInvestigation(self):
        r"""风险排查
        :rtype: str
        """
        return self._RiskInvestigation

    @RiskInvestigation.setter
    def RiskInvestigation(self, RiskInvestigation):
        self._RiskInvestigation = RiskInvestigation

    @property
    def RiskTreatment(self):
        r"""风险处置
        :rtype: str
        """
        return self._RiskTreatment

    @RiskTreatment.setter
    def RiskTreatment(self, RiskTreatment):
        self._RiskTreatment = RiskTreatment

    @property
    def LogType(self):
        r"""日志类型
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogSearch(self):
        r"""语句检索
        :rtype: str
        """
        return self._LogSearch

    @LogSearch.setter
    def LogSearch(self, LogSearch):
        self._LogSearch = LogSearch


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._Level = params.get("Level")
        if params.get("Attacker") is not None:
            self._Attacker = RoleInfo()
            self._Attacker._deserialize(params.get("Attacker"))
        if params.get("Victim") is not None:
            self._Victim = RoleInfo()
            self._Victim._deserialize(params.get("Victim"))
        self._EvidenceData = params.get("EvidenceData")
        self._EvidenceLocation = params.get("EvidenceLocation")
        self._EvidencePath = params.get("EvidencePath")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Count = params.get("Count")
        self._UrgentSuggestion = params.get("UrgentSuggestion")
        self._RemediationSuggestion = params.get("RemediationSuggestion")
        self._Status = params.get("Status")
        self._ProcessType = params.get("ProcessType")
        self._Type = params.get("Type")
        self._SubType = params.get("SubType")
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = AlertExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._Key = params.get("Key")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._NickName = params.get("NickName")
        self._Uin = params.get("Uin")
        self._Action = params.get("Action")
        self._RiskInvestigation = params.get("RiskInvestigation")
        self._RiskTreatment = params.get("RiskTreatment")
        self._LogType = params.get("LogType")
        self._LogSearch = params.get("LogSearch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetBaseInfoResponse(AbstractModel):
    r"""主机资产详情

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc-id
        :type VpcId: str
        :param _VpcName: vpc-name
        :type VpcName: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _Os: 操作系统
        :type Os: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _PrivateIp: 内网ip
        :type PrivateIp: str
        :param _Region: 地域
        :type Region: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _AssetId: 资产id
        :type AssetId: str
        :param _AccountNum: 账号数量
        :type AccountNum: int
        :param _PortNum: 端口数量
        :type PortNum: int
        :param _ProcessNum: 进程数量
        :type ProcessNum: int
        :param _SoftApplicationNum: 软件应用数量
        :type SoftApplicationNum: int
        :param _DatabaseNum: 数据库数量
        :type DatabaseNum: int
        :param _WebApplicationNum: Web应用数量
        :type WebApplicationNum: int
        :param _ServiceNum: 服务数量
        :type ServiceNum: int
        :param _WebFrameworkNum: web框架数量
        :type WebFrameworkNum: int
        :param _WebSiteNum: Web站点数量
        :type WebSiteNum: int
        :param _JarPackageNum: Jar包数量
        :type JarPackageNum: int
        :param _StartServiceNum: 启动服务数量
        :type StartServiceNum: int
        :param _ScheduledTaskNum: 计划任务数量
        :type ScheduledTaskNum: int
        :param _EnvironmentVariableNum: 环境变量数量
        :type EnvironmentVariableNum: int
        :param _KernelModuleNum: 内核模块数量
        :type KernelModuleNum: int
        :param _SystemInstallationPackageNum: 系统安装包数量
        :type SystemInstallationPackageNum: int
        :param _SurplusProtectDay: 剩余防护时长
        :type SurplusProtectDay: int
        :param _CWPStatus: 客户端是否安装  1 已安装 0 未安装
        :type CWPStatus: int
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _ProtectLevel: 防护等级
        :type ProtectLevel: str
        :param _ProtectedDay: 防护时长
        :type ProtectedDay: int
        """
        self._VpcId = None
        self._VpcName = None
        self._AssetName = None
        self._Os = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._AssetType = None
        self._AssetId = None
        self._AccountNum = None
        self._PortNum = None
        self._ProcessNum = None
        self._SoftApplicationNum = None
        self._DatabaseNum = None
        self._WebApplicationNum = None
        self._ServiceNum = None
        self._WebFrameworkNum = None
        self._WebSiteNum = None
        self._JarPackageNum = None
        self._StartServiceNum = None
        self._ScheduledTaskNum = None
        self._EnvironmentVariableNum = None
        self._KernelModuleNum = None
        self._SystemInstallationPackageNum = None
        self._SurplusProtectDay = None
        self._CWPStatus = None
        self._Tag = None
        self._ProtectLevel = None
        self._ProtectedDay = None

    @property
    def VpcId(self):
        r"""vpc-id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc-name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""内网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AccountNum(self):
        r"""账号数量
        :rtype: int
        """
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def PortNum(self):
        r"""端口数量
        :rtype: int
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def ProcessNum(self):
        r"""进程数量
        :rtype: int
        """
        return self._ProcessNum

    @ProcessNum.setter
    def ProcessNum(self, ProcessNum):
        self._ProcessNum = ProcessNum

    @property
    def SoftApplicationNum(self):
        r"""软件应用数量
        :rtype: int
        """
        return self._SoftApplicationNum

    @SoftApplicationNum.setter
    def SoftApplicationNum(self, SoftApplicationNum):
        self._SoftApplicationNum = SoftApplicationNum

    @property
    def DatabaseNum(self):
        r"""数据库数量
        :rtype: int
        """
        return self._DatabaseNum

    @DatabaseNum.setter
    def DatabaseNum(self, DatabaseNum):
        self._DatabaseNum = DatabaseNum

    @property
    def WebApplicationNum(self):
        r"""Web应用数量
        :rtype: int
        """
        return self._WebApplicationNum

    @WebApplicationNum.setter
    def WebApplicationNum(self, WebApplicationNum):
        self._WebApplicationNum = WebApplicationNum

    @property
    def ServiceNum(self):
        r"""服务数量
        :rtype: int
        """
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def WebFrameworkNum(self):
        r"""web框架数量
        :rtype: int
        """
        return self._WebFrameworkNum

    @WebFrameworkNum.setter
    def WebFrameworkNum(self, WebFrameworkNum):
        self._WebFrameworkNum = WebFrameworkNum

    @property
    def WebSiteNum(self):
        r"""Web站点数量
        :rtype: int
        """
        return self._WebSiteNum

    @WebSiteNum.setter
    def WebSiteNum(self, WebSiteNum):
        self._WebSiteNum = WebSiteNum

    @property
    def JarPackageNum(self):
        r"""Jar包数量
        :rtype: int
        """
        return self._JarPackageNum

    @JarPackageNum.setter
    def JarPackageNum(self, JarPackageNum):
        self._JarPackageNum = JarPackageNum

    @property
    def StartServiceNum(self):
        r"""启动服务数量
        :rtype: int
        """
        return self._StartServiceNum

    @StartServiceNum.setter
    def StartServiceNum(self, StartServiceNum):
        self._StartServiceNum = StartServiceNum

    @property
    def ScheduledTaskNum(self):
        r"""计划任务数量
        :rtype: int
        """
        return self._ScheduledTaskNum

    @ScheduledTaskNum.setter
    def ScheduledTaskNum(self, ScheduledTaskNum):
        self._ScheduledTaskNum = ScheduledTaskNum

    @property
    def EnvironmentVariableNum(self):
        r"""环境变量数量
        :rtype: int
        """
        return self._EnvironmentVariableNum

    @EnvironmentVariableNum.setter
    def EnvironmentVariableNum(self, EnvironmentVariableNum):
        self._EnvironmentVariableNum = EnvironmentVariableNum

    @property
    def KernelModuleNum(self):
        r"""内核模块数量
        :rtype: int
        """
        return self._KernelModuleNum

    @KernelModuleNum.setter
    def KernelModuleNum(self, KernelModuleNum):
        self._KernelModuleNum = KernelModuleNum

    @property
    def SystemInstallationPackageNum(self):
        r"""系统安装包数量
        :rtype: int
        """
        return self._SystemInstallationPackageNum

    @SystemInstallationPackageNum.setter
    def SystemInstallationPackageNum(self, SystemInstallationPackageNum):
        self._SystemInstallationPackageNum = SystemInstallationPackageNum

    @property
    def SurplusProtectDay(self):
        r"""剩余防护时长
        :rtype: int
        """
        return self._SurplusProtectDay

    @SurplusProtectDay.setter
    def SurplusProtectDay(self, SurplusProtectDay):
        self._SurplusProtectDay = SurplusProtectDay

    @property
    def CWPStatus(self):
        r"""客户端是否安装  1 已安装 0 未安装
        :rtype: int
        """
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProtectLevel(self):
        r"""防护等级
        :rtype: str
        """
        return self._ProtectLevel

    @ProtectLevel.setter
    def ProtectLevel(self, ProtectLevel):
        self._ProtectLevel = ProtectLevel

    @property
    def ProtectedDay(self):
        r"""防护时长
        :rtype: int
        """
        return self._ProtectedDay

    @ProtectedDay.setter
    def ProtectedDay(self, ProtectedDay):
        self._ProtectedDay = ProtectedDay


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AssetName = params.get("AssetName")
        self._Os = params.get("Os")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._AssetType = params.get("AssetType")
        self._AssetId = params.get("AssetId")
        self._AccountNum = params.get("AccountNum")
        self._PortNum = params.get("PortNum")
        self._ProcessNum = params.get("ProcessNum")
        self._SoftApplicationNum = params.get("SoftApplicationNum")
        self._DatabaseNum = params.get("DatabaseNum")
        self._WebApplicationNum = params.get("WebApplicationNum")
        self._ServiceNum = params.get("ServiceNum")
        self._WebFrameworkNum = params.get("WebFrameworkNum")
        self._WebSiteNum = params.get("WebSiteNum")
        self._JarPackageNum = params.get("JarPackageNum")
        self._StartServiceNum = params.get("StartServiceNum")
        self._ScheduledTaskNum = params.get("ScheduledTaskNum")
        self._EnvironmentVariableNum = params.get("EnvironmentVariableNum")
        self._KernelModuleNum = params.get("KernelModuleNum")
        self._SystemInstallationPackageNum = params.get("SystemInstallationPackageNum")
        self._SurplusProtectDay = params.get("SurplusProtectDay")
        self._CWPStatus = params.get("CWPStatus")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProtectLevel = params.get("ProtectLevel")
        self._ProtectedDay = params.get("ProtectedDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCluster(AbstractModel):
    r"""集群列表

    集群防护状态，左边枚举,右边为显示
    集群防护状态
    0:未接入
    1:未防护
    2:部分防护
    3:防护中
    4:接入异常
    5:接入中
    6:卸载中
    7:卸载异常

    """

    def __init__(self):
        r"""
        :param _AppId: 租户id
        :type AppId: int
        :param _Uin: 租户uin
        :type Uin: str
        :param _Nick: 租户昵称
        :type Nick: str
        :param _Region: 地域
        :type Region: str
        :param _AssetId: 集群id
        :type AssetId: str
        :param _AssetName: 集群名称
        :type AssetName: str
        :param _AssetType: 集群类型
        :type AssetType: str
        :param _InstanceCreateTime: 集群创建时间
        :type InstanceCreateTime: str
        :param _Status: 状态
        :type Status: str
        :param _ProtectStatus: 集群防护状态，左边枚举,右边为显示
集群防护状态 
0:未接入
1:未防护 
2:部分防护 
3:防护中 
4:接入异常 
5:接入中 
6:卸载中 
7:卸载异常
        :type ProtectStatus: int
        :param _ProtectInfo: 接入信息，不为空表示有接入异常信息
        :type ProtectInfo: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _KubernetesVersion: kubernetes版本
        :type KubernetesVersion: str
        :param _Component: 运行时组件
        :type Component: str
        :param _ComponentVersion: 运行时组件版本
        :type ComponentVersion: str
        :param _ComponentStatus: 组件状态
        :type ComponentStatus: str
        :param _CheckTime: 体检时间
        :type CheckTime: str
        :param _MachineCount: 关联主机数
        :type MachineCount: int
        :param _PodCount: 关联pod数
        :type PodCount: int
        :param _ServiceCount: 关联service数
        :type ServiceCount: int
        :param _VulRisk: 漏洞风险
        :type VulRisk: int
        :param _CFGRisk: 配置风险
        :type CFGRisk: int
        :param _CheckCount: 体检数
        :type CheckCount: int
        :param _IsCore: 是否核心：1:核心，2:非核心
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        :param _CloudType: 云资产类型：0：腾讯云，1：aws，2：azure
        :type CloudType: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._InstanceCreateTime = None
        self._Status = None
        self._ProtectStatus = None
        self._ProtectInfo = None
        self._VpcId = None
        self._VpcName = None
        self._KubernetesVersion = None
        self._Component = None
        self._ComponentVersion = None
        self._ComponentStatus = None
        self._CheckTime = None
        self._MachineCount = None
        self._PodCount = None
        self._ServiceCount = None
        self._VulRisk = None
        self._CFGRisk = None
        self._CheckCount = None
        self._IsCore = None
        self._IsNewAsset = None
        self._CloudType = None

    @property
    def AppId(self):
        r"""租户id
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""租户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""租户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        r"""集群id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""集群名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""集群类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def InstanceCreateTime(self):
        r"""集群创建时间
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

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
    def ProtectStatus(self):
        r"""集群防护状态，左边枚举,右边为显示
集群防护状态 
0:未接入
1:未防护 
2:部分防护 
3:防护中 
4:接入异常 
5:接入中 
6:卸载中 
7:卸载异常
        :rtype: int
        """
        return self._ProtectStatus

    @ProtectStatus.setter
    def ProtectStatus(self, ProtectStatus):
        self._ProtectStatus = ProtectStatus

    @property
    def ProtectInfo(self):
        r"""接入信息，不为空表示有接入异常信息
        :rtype: str
        """
        return self._ProtectInfo

    @ProtectInfo.setter
    def ProtectInfo(self, ProtectInfo):
        self._ProtectInfo = ProtectInfo

    @property
    def VpcId(self):
        r"""私有网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""私有网络名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def KubernetesVersion(self):
        r"""kubernetes版本
        :rtype: str
        """
        return self._KubernetesVersion

    @KubernetesVersion.setter
    def KubernetesVersion(self, KubernetesVersion):
        self._KubernetesVersion = KubernetesVersion

    @property
    def Component(self):
        r"""运行时组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def ComponentVersion(self):
        r"""运行时组件版本
        :rtype: str
        """
        return self._ComponentVersion

    @ComponentVersion.setter
    def ComponentVersion(self, ComponentVersion):
        self._ComponentVersion = ComponentVersion

    @property
    def ComponentStatus(self):
        r"""组件状态
        :rtype: str
        """
        return self._ComponentStatus

    @ComponentStatus.setter
    def ComponentStatus(self, ComponentStatus):
        self._ComponentStatus = ComponentStatus

    @property
    def CheckTime(self):
        r"""体检时间
        :rtype: str
        """
        return self._CheckTime

    @CheckTime.setter
    def CheckTime(self, CheckTime):
        self._CheckTime = CheckTime

    @property
    def MachineCount(self):
        r"""关联主机数
        :rtype: int
        """
        return self._MachineCount

    @MachineCount.setter
    def MachineCount(self, MachineCount):
        self._MachineCount = MachineCount

    @property
    def PodCount(self):
        r"""关联pod数
        :rtype: int
        """
        return self._PodCount

    @PodCount.setter
    def PodCount(self, PodCount):
        self._PodCount = PodCount

    @property
    def ServiceCount(self):
        r"""关联service数
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def VulRisk(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def CFGRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk

    @property
    def CheckCount(self):
        r"""体检数
        :rtype: int
        """
        return self._CheckCount

    @CheckCount.setter
    def CheckCount(self, CheckCount):
        self._CheckCount = CheckCount

    @property
    def IsCore(self):
        r"""是否核心：1:核心，2:非核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def CloudType(self):
        r"""云资产类型：0：腾讯云，1：aws，2：azure
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Status = params.get("Status")
        self._ProtectStatus = params.get("ProtectStatus")
        self._ProtectInfo = params.get("ProtectInfo")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._KubernetesVersion = params.get("KubernetesVersion")
        self._Component = params.get("Component")
        self._ComponentVersion = params.get("ComponentVersion")
        self._ComponentStatus = params.get("ComponentStatus")
        self._CheckTime = params.get("CheckTime")
        self._MachineCount = params.get("MachineCount")
        self._PodCount = params.get("PodCount")
        self._ServiceCount = params.get("ServiceCount")
        self._VulRisk = params.get("VulRisk")
        self._CFGRisk = params.get("CFGRisk")
        self._CheckCount = params.get("CheckCount")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetClusterPod(AbstractModel):
    r"""集群pod列表

    """

    def __init__(self):
        r"""
        :param _AppId: 租户id
        :type AppId: int
        :param _Uin: 租户uin
        :type Uin: str
        :param _Nick: 租户昵称
        :type Nick: str
        :param _Region: 地域
        :type Region: str
        :param _AssetId: pod id
        :type AssetId: str
        :param _AssetName: pod名称
        :type AssetName: str
        :param _InstanceCreateTime: pod创建时间
        :type InstanceCreateTime: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Status: 状态
        :type Status: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _MachineId: 主机id
        :type MachineId: str
        :param _MachineName: 主机名
        :type MachineName: str
        :param _PodIp: pod ip
        :type PodIp: str
        :param _ServiceCount: 关联service数
        :type ServiceCount: int
        :param _ContainerCount: 关联容器数
        :type ContainerCount: int
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _PrivateIp: 内网ip
        :type PrivateIp: str
        :param _IsCore: 是否核心：1:核心，2:非核心
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._InstanceCreateTime = None
        self._Namespace = None
        self._Status = None
        self._ClusterId = None
        self._ClusterName = None
        self._MachineId = None
        self._MachineName = None
        self._PodIp = None
        self._ServiceCount = None
        self._ContainerCount = None
        self._PublicIp = None
        self._PrivateIp = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""租户id
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""租户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""租户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        r"""pod id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""pod名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceCreateTime(self):
        r"""pod创建时间
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def Namespace(self):
        r"""命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

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
    def ClusterId(self):
        r"""集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MachineId(self):
        r"""主机id
        :rtype: str
        """
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def MachineName(self):
        r"""主机名
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def PodIp(self):
        r"""pod ip
        :rtype: str
        """
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def ServiceCount(self):
        r"""关联service数
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def ContainerCount(self):
        r"""关联容器数
        :rtype: int
        """
        return self._ContainerCount

    @ContainerCount.setter
    def ContainerCount(self, ContainerCount):
        self._ContainerCount = ContainerCount

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""内网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def IsCore(self):
        r"""是否核心：1:核心，2:非核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MachineId = params.get("MachineId")
        self._MachineName = params.get("MachineName")
        self._PodIp = params.get("PodIp")
        self._ServiceCount = params.get("ServiceCount")
        self._ContainerCount = params.get("ContainerCount")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInfoDetail(AbstractModel):
    r"""资产扫描结构细节

    """

    def __init__(self):
        r"""
        :param _AppID: 用户appid
        :type AppID: str
        :param _CVEId: CVE编号
        :type CVEId: str
        :param _IsScan: 是扫描，0默认未扫描，1正在扫描，2扫描完成，3扫描出错
        :type IsScan: int
        :param _InfluenceAsset: 影响资产数目
        :type InfluenceAsset: int
        :param _NotRepairAsset: 未修复资产数目
        :type NotRepairAsset: int
        :param _NotProtectAsset: 未防护资产数目
        :type NotProtectAsset: int
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskPercent: 任务百分比
        :type TaskPercent: int
        :param _TaskTime: 任务时间
        :type TaskTime: int
        :param _ScanTime: 扫描时间
        :type ScanTime: str
        """
        self._AppID = None
        self._CVEId = None
        self._IsScan = None
        self._InfluenceAsset = None
        self._NotRepairAsset = None
        self._NotProtectAsset = None
        self._TaskId = None
        self._TaskPercent = None
        self._TaskTime = None
        self._ScanTime = None

    @property
    def AppID(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CVEId(self):
        r"""CVE编号
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def IsScan(self):
        r"""是扫描，0默认未扫描，1正在扫描，2扫描完成，3扫描出错
        :rtype: int
        """
        return self._IsScan

    @IsScan.setter
    def IsScan(self, IsScan):
        self._IsScan = IsScan

    @property
    def InfluenceAsset(self):
        r"""影响资产数目
        :rtype: int
        """
        return self._InfluenceAsset

    @InfluenceAsset.setter
    def InfluenceAsset(self, InfluenceAsset):
        self._InfluenceAsset = InfluenceAsset

    @property
    def NotRepairAsset(self):
        r"""未修复资产数目
        :rtype: int
        """
        return self._NotRepairAsset

    @NotRepairAsset.setter
    def NotRepairAsset(self, NotRepairAsset):
        self._NotRepairAsset = NotRepairAsset

    @property
    def NotProtectAsset(self):
        r"""未防护资产数目
        :rtype: int
        """
        return self._NotProtectAsset

    @NotProtectAsset.setter
    def NotProtectAsset(self, NotProtectAsset):
        self._NotProtectAsset = NotProtectAsset

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskPercent(self):
        r"""任务百分比
        :rtype: int
        """
        return self._TaskPercent

    @TaskPercent.setter
    def TaskPercent(self, TaskPercent):
        self._TaskPercent = TaskPercent

    @property
    def TaskTime(self):
        r"""任务时间
        :rtype: int
        """
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ScanTime(self):
        r"""扫描时间
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._CVEId = params.get("CVEId")
        self._IsScan = params.get("IsScan")
        self._InfluenceAsset = params.get("InfluenceAsset")
        self._NotRepairAsset = params.get("NotRepairAsset")
        self._NotProtectAsset = params.get("NotProtectAsset")
        self._TaskId = params.get("TaskId")
        self._TaskPercent = params.get("TaskPercent")
        self._TaskTime = params.get("TaskTime")
        self._ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInstanceTypeMap(AbstractModel):
    r"""资产类型和实例类型的映射

    """

    def __init__(self):
        r"""
        :param _Text: 资产类型
        :type Text: str
        :param _Value: 资产类型
        :type Value: str
        :param _InstanceTypeList: 资产类型和实例类型映射关系
        :type InstanceTypeList: list of FilterDataObject
        """
        self._Text = None
        self._Value = None
        self._InstanceTypeList = None

    @property
    def Text(self):
        r"""资产类型
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        r"""资产类型
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def InstanceTypeList(self):
        r"""资产类型和实例类型映射关系
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeList

    @InstanceTypeList.setter
    def InstanceTypeList(self, InstanceTypeList):
        self._InstanceTypeList = InstanceTypeList


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        if params.get("InstanceTypeList") is not None:
            self._InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetProcessItem(AbstractModel):
    r"""主机进程内容

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: 云账号ID
        :type CloudAccountID: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _AppID: 租户ID
        :type AppID: int
        :param _CloudAccountName: 云账号名称
        :type CloudAccountName: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _PrivateIp: 内网IP
        :type PrivateIp: str
        :param _ProcessID: 进程ID
        :type ProcessID: str
        :param _ProcessName: 进程名称
        :type ProcessName: str
        :param _CmdLine: 命令行
        :type CmdLine: str
        :param _Port: 监听端口列表
        :type Port: str
        """
        self._CloudAccountID = None
        self._InstanceName = None
        self._AppID = None
        self._CloudAccountName = None
        self._InstanceID = None
        self._PublicIp = None
        self._PrivateIp = None
        self._ProcessID = None
        self._ProcessName = None
        self._CmdLine = None
        self._Port = None

    @property
    def CloudAccountID(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppID(self):
        r"""租户ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

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
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

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
    def ProcessID(self):
        r"""进程ID
        :rtype: str
        """
        return self._ProcessID

    @ProcessID.setter
    def ProcessID(self, ProcessID):
        self._ProcessID = ProcessID

    @property
    def ProcessName(self):
        r"""进程名称
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def CmdLine(self):
        r"""命令行
        :rtype: str
        """
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Port(self):
        r"""监听端口列表
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._InstanceName = params.get("InstanceName")
        self._AppID = params.get("AppID")
        self._CloudAccountName = params.get("CloudAccountName")
        self._InstanceID = params.get("InstanceID")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._ProcessID = params.get("ProcessID")
        self._ProcessName = params.get("ProcessName")
        self._CmdLine = params.get("CmdLine")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetRiskItem(AbstractModel):
    r"""资产视角风险项

    """

    def __init__(self):
        r"""
        :param _AppId: 租户ID
        :type AppId: int
        :param _Provider: 云厂商
        :type Provider: str
        :param _ProviderName: 云厂商名称
        :type ProviderName: str
        :param _CloudAccountName: 云账号名称
        :type CloudAccountName: str
        :param _CloudAccountId: 云账号ID
        :type CloudAccountId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CreateTime: 首次发现时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RiskStatus: 风险状态
        :type RiskStatus: int
        :param _RiskTitle: 风险名称
        :type RiskTitle: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _Severity: 风险等级
        :type Severity: str
        :param _RiskRuleId: 风险规则ID
        :type RiskRuleId: str
        :param _Classify: 处置分类
        :type Classify: str
        :param _StandardTerms: 等保合规
        :type StandardTerms: list of StandardTerm
        """
        self._AppId = None
        self._Provider = None
        self._ProviderName = None
        self._CloudAccountName = None
        self._CloudAccountId = None
        self._InstanceName = None
        self._InstanceId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RiskStatus = None
        self._RiskTitle = None
        self._CheckType = None
        self._Severity = None
        self._RiskRuleId = None
        self._Classify = None
        self._StandardTerms = None

    @property
    def AppId(self):
        r"""租户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

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
    def CloudAccountName(self):
        r"""云账号名称
        :rtype: str
        """
        return self._CloudAccountName

    @CloudAccountName.setter
    def CloudAccountName(self, CloudAccountName):
        self._CloudAccountName = CloudAccountName

    @property
    def CloudAccountId(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountId

    @CloudAccountId.setter
    def CloudAccountId(self, CloudAccountId):
        self._CloudAccountId = CloudAccountId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateTime(self):
        r"""首次发现时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RiskStatus(self):
        r"""风险状态
        :rtype: int
        """
        return self._RiskStatus

    @RiskStatus.setter
    def RiskStatus(self, RiskStatus):
        self._RiskStatus = RiskStatus

    @property
    def RiskTitle(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskTitle

    @RiskTitle.setter
    def RiskTitle(self, RiskTitle):
        self._RiskTitle = RiskTitle

    @property
    def CheckType(self):
        r"""检查类型
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Severity(self):
        r"""风险等级
        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def RiskRuleId(self):
        r"""风险规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId

    @property
    def Classify(self):
        r"""处置分类
        :rtype: str
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify

    @property
    def StandardTerms(self):
        r"""等保合规
        :rtype: list of StandardTerm
        """
        return self._StandardTerms

    @StandardTerms.setter
    def StandardTerms(self, StandardTerms):
        self._StandardTerms = StandardTerms


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Provider = params.get("Provider")
        self._ProviderName = params.get("ProviderName")
        self._CloudAccountName = params.get("CloudAccountName")
        self._CloudAccountId = params.get("CloudAccountId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RiskStatus = params.get("RiskStatus")
        self._RiskTitle = params.get("RiskTitle")
        self._CheckType = params.get("CheckType")
        self._Severity = params.get("Severity")
        self._RiskRuleId = params.get("RiskRuleId")
        self._Classify = params.get("Classify")
        if params.get("StandardTerms") is not None:
            self._StandardTerms = []
            for item in params.get("StandardTerms"):
                obj = StandardTerm()
                obj._deserialize(item)
                self._StandardTerms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetTag(AbstractModel):
    r"""安全中心资产标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的key值,可以是字母、数字、下划线
        :type TagKey: str
        :param _TagValue: 标签的vale值,可以是字母、数字、下划线
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签的key值,可以是字母、数字、下划线
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签的vale值,可以是字母、数字、下划线
        :rtype: str
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
        


class AssetViewCFGRisk(AbstractModel):
    r"""资产视角配置风险

    """

    def __init__(self):
        r"""
        :param _Id: 唯一id
        :type Id: str
        :param _CFGName: 配置名
        :type CFGName: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _From: 来源
        :type From: str
        :param _Status: 状态
        :type Status: int
        :param _CFGSTD: 相关规范
        :type CFGSTD: str
        :param _CFGDescribe: 配置详情
        :type CFGDescribe: str
        :param _CFGFix: 修复建议
        :type CFGFix: str
        :param _CFGHelpURL: 帮助文档链接
        :type CFGHelpURL: str
        :param _Index: 前端使用索引
        :type Index: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _ClbId: 当资产类型为LBL的时候，展示该字段，方便定位具体的LB
        :type ClbId: str
        """
        self._Id = None
        self._CFGName = None
        self._CheckType = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._AffectAsset = None
        self._Level = None
        self._FirstTime = None
        self._RecentTime = None
        self._From = None
        self._Status = None
        self._CFGSTD = None
        self._CFGDescribe = None
        self._CFGFix = None
        self._CFGHelpURL = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._ClbId = None

    @property
    def Id(self):
        r"""唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CFGName(self):
        r"""配置名
        :rtype: str
        """
        return self._CFGName

    @CFGName.setter
    def CFGName(self, CFGName):
        self._CFGName = CFGName

    @property
    def CheckType(self):
        r"""检查类型
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def From(self):
        r"""来源
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CFGSTD(self):
        r"""相关规范
        :rtype: str
        """
        return self._CFGSTD

    @CFGSTD.setter
    def CFGSTD(self, CFGSTD):
        self._CFGSTD = CFGSTD

    @property
    def CFGDescribe(self):
        r"""配置详情
        :rtype: str
        """
        return self._CFGDescribe

    @CFGDescribe.setter
    def CFGDescribe(self, CFGDescribe):
        self._CFGDescribe = CFGDescribe

    @property
    def CFGFix(self):
        r"""修复建议
        :rtype: str
        """
        return self._CFGFix

    @CFGFix.setter
    def CFGFix(self, CFGFix):
        self._CFGFix = CFGFix

    @property
    def CFGHelpURL(self):
        r"""帮助文档链接
        :rtype: str
        """
        return self._CFGHelpURL

    @CFGHelpURL.setter
    def CFGHelpURL(self, CFGHelpURL):
        self._CFGHelpURL = CFGHelpURL

    @property
    def Index(self):
        r"""前端使用索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ClbId(self):
        r"""当资产类型为LBL的时候，展示该字段，方便定位具体的LB
        :rtype: str
        """
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CFGName = params.get("CFGName")
        self._CheckType = params.get("CheckType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._FirstTime = params.get("FirstTime")
        self._RecentTime = params.get("RecentTime")
        self._From = params.get("From")
        self._Status = params.get("Status")
        self._CFGSTD = params.get("CFGSTD")
        self._CFGDescribe = params.get("CFGDescribe")
        self._CFGFix = params.get("CFGFix")
        self._CFGHelpURL = params.get("CFGHelpURL")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._ClbId = params.get("ClbId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewPortRisk(AbstractModel):
    r"""资产视角的端口风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Suggestion: 处置建议,0保持现状、1限制访问、2封禁端口
        :type Suggestion: int
        :param _Status: 状态，0未处理、1已处置、2已忽略、3云防已防护
        :type Status: int
        :param _Id: 风险ID
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _From: 识别来源，详细看枚举返回。
        :type From: str
        :param _ServiceJudge: 服务判定,high_risk_service 高危服务 web_service web服务 other_service 其他服务
        :type ServiceJudge: str
        :param _XspmStatus: 状态，0未处理、1已处置、2已忽略、3云防已防护、4无需处理
        :type XspmStatus: int
        """
        self._Port = None
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._From = None
        self._ServiceJudge = None
        self._XspmStatus = None

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
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

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
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""服务
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        r"""处置建议,0保持现状、1限制访问、2封禁端口
        :rtype: int
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        r"""状态，0未处理、1已处置、2已忽略、3云防已防护
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""风险ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def From(self):
        r"""识别来源，详细看枚举返回。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def ServiceJudge(self):
        r"""服务判定,high_risk_service 高危服务 web_service web服务 other_service 其他服务
        :rtype: str
        """
        return self._ServiceJudge

    @ServiceJudge.setter
    def ServiceJudge(self, ServiceJudge):
        self._ServiceJudge = ServiceJudge

    @property
    def XspmStatus(self):
        r"""状态，0未处理、1已处置、2已忽略、3云防已防护、4无需处理
        :rtype: int
        """
        return self._XspmStatus

    @XspmStatus.setter
    def XspmStatus(self, XspmStatus):
        self._XspmStatus = XspmStatus


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._From = params.get("From")
        self._ServiceJudge = params.get("ServiceJudge")
        self._XspmStatus = params.get("XspmStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRisk(AbstractModel):
    r"""资产视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。

        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: 风险ID
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _Port: 端口
        :type Port: str
        :param _Describe: 漏洞描述
        :type Describe: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _References: 技术参考
        :type References: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Fix: 修复方案
        :type Fix: str
        :param _POCId: pocid
        :type POCId: str
        :param _From: 扫描来源
        :type From: str
        :param _CWPVersion: 主机版本
        :type CWPVersion: int
        :param _IsSupportRepair: 是否支持修复
        :type IsSupportRepair: bool
        :param _IsSupportDetect: 是否支持扫描
        :type IsSupportDetect: bool
        :param _InstanceUUID: 实例uuid
        :type InstanceUUID: str
        :param _Payload: 攻击载荷
        :type Payload: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :type EMGCVulType: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._Describe = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._Fix = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._IsSupportRepair = None
        self._IsSupportDetect = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None

    @property
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。

        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""服务
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""状态，0未处理、1已处置、2已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""风险ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        r"""端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Describe(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def AppName(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""技术参考
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""风险点
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Fix(self):
        r"""修复方案
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def POCId(self):
        r"""pocid
        :rtype: str
        """
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        r"""扫描来源
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        r"""主机版本
        :rtype: int
        """
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def IsSupportRepair(self):
        r"""是否支持修复
        :rtype: bool
        """
        return self._IsSupportRepair

    @IsSupportRepair.setter
    def IsSupportRepair(self, IsSupportRepair):
        self._IsSupportRepair = IsSupportRepair

    @property
    def IsSupportDetect(self):
        r"""是否支持扫描
        :rtype: bool
        """
        return self._IsSupportDetect

    @IsSupportDetect.setter
    def IsSupportDetect(self, IsSupportDetect):
        self._IsSupportDetect = IsSupportDetect

    @property
    def InstanceUUID(self):
        r"""实例uuid
        :rtype: str
        """
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        r"""攻击载荷
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._Describe = params.get("Describe")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Fix = params.get("Fix")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._IsSupportRepair = params.get("IsSupportRepair")
        self._IsSupportDetect = params.get("IsSupportDetect")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRiskData(AbstractModel):
    r"""资产视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1标记已处置、2已忽略，3已处置 ，4 处置中 ，5 检测中 ，6部分已处置
        :type Status: int
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _Port: 端口
        :type Port: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _POCId: pocid
        :type POCId: str
        :param _From: 扫描来源
        :type From: str
        :param _CWPVersion: 主机版本
        :type CWPVersion: int
        :param _InstanceUUID: 实例uuid
        :type InstanceUUID: str
        :param _Payload: 攻击载荷
        :type Payload: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :type EMGCVulType: int
        :param _CVSS: CVSS评分
        :type CVSS: float
        :param _Index: 前端索引id
        :type Index: str
        :param _PCMGRId: pcmgrId
        :type PCMGRId: str
        :param _LogId: 报告id
        :type LogId: str
        :param _TaskId: 任务id
        :type TaskId: str
        :param _VulTag: 漏洞标签
        :type VulTag: list of str
        :param _DisclosureTime: 漏洞披露时间
        :type DisclosureTime: str
        :param _AttackHeat: 攻击热度
        :type AttackHeat: int
        :param _IsSuggest: 是否必修漏洞1是，0不是
        :type IsSuggest: int
        :param _HandleTaskId: 处置任务ID
        :type HandleTaskId: str
        :param _EngineSource: 引擎来源
        :type EngineSource: str
        :param _VulRiskId: 新的漏洞风险id(同全网漏洞表的RiskId)
        :type VulRiskId: str
        :param _TvdID: 新版漏洞id
        :type TvdID: str
        :param _IsOneClick: 是否可以一键体检，1-可以，0-不可以
        :type IsOneClick: int
        :param _IsPOC: 是否POC扫描，0-非POC，1-POC
        :type IsPOC: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._RiskId = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._AppName = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None
        self._CVSS = None
        self._Index = None
        self._PCMGRId = None
        self._LogId = None
        self._TaskId = None
        self._VulTag = None
        self._DisclosureTime = None
        self._AttackHeat = None
        self._IsSuggest = None
        self._HandleTaskId = None
        self._EngineSource = None
        self._VulRiskId = None
        self._TvdID = None
        self._IsOneClick = None
        self._IsPOC = None

    @property
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""状态，0未处理、1标记已处置、2已忽略，3已处置 ，4 处置中 ，5 检测中 ，6部分已处置
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        r"""端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AppName(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""风险点
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def POCId(self):
        r"""pocid
        :rtype: str
        """
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        r"""扫描来源
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        r"""主机版本
        :rtype: int
        """
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def InstanceUUID(self):
        r"""实例uuid
        :rtype: str
        """
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        r"""攻击载荷
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        r"""CVSS评分
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def Index(self):
        r"""前端索引id
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def PCMGRId(self):
        r"""pcmgrId
        :rtype: str
        """
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId

    @property
    def LogId(self):
        r"""报告id
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskId(self):
        r"""任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VulTag(self):
        r"""漏洞标签
        :rtype: list of str
        """
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def DisclosureTime(self):
        r"""漏洞披露时间
        :rtype: str
        """
        return self._DisclosureTime

    @DisclosureTime.setter
    def DisclosureTime(self, DisclosureTime):
        self._DisclosureTime = DisclosureTime

    @property
    def AttackHeat(self):
        r"""攻击热度
        :rtype: int
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def IsSuggest(self):
        r"""是否必修漏洞1是，0不是
        :rtype: int
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def HandleTaskId(self):
        r"""处置任务ID
        :rtype: str
        """
        return self._HandleTaskId

    @HandleTaskId.setter
    def HandleTaskId(self, HandleTaskId):
        self._HandleTaskId = HandleTaskId

    @property
    def EngineSource(self):
        r"""引擎来源
        :rtype: str
        """
        return self._EngineSource

    @EngineSource.setter
    def EngineSource(self, EngineSource):
        self._EngineSource = EngineSource

    @property
    def VulRiskId(self):
        r"""新的漏洞风险id(同全网漏洞表的RiskId)
        :rtype: str
        """
        return self._VulRiskId

    @VulRiskId.setter
    def VulRiskId(self, VulRiskId):
        self._VulRiskId = VulRiskId

    @property
    def TvdID(self):
        r"""新版漏洞id
        :rtype: str
        """
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID

    @property
    def IsOneClick(self):
        r"""是否可以一键体检，1-可以，0-不可以
        :rtype: int
        """
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick

    @property
    def IsPOC(self):
        r"""是否POC扫描，0-非POC，1-POC
        :rtype: int
        """
        return self._IsPOC

    @IsPOC.setter
    def IsPOC(self, IsPOC):
        self._IsPOC = IsPOC


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._RiskId = params.get("RiskId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._Index = params.get("Index")
        self._PCMGRId = params.get("PCMGRId")
        self._LogId = params.get("LogId")
        self._TaskId = params.get("TaskId")
        self._VulTag = params.get("VulTag")
        self._DisclosureTime = params.get("DisclosureTime")
        self._AttackHeat = params.get("AttackHeat")
        self._IsSuggest = params.get("IsSuggest")
        self._HandleTaskId = params.get("HandleTaskId")
        self._EngineSource = params.get("EngineSource")
        self._VulRiskId = params.get("VulRiskId")
        self._TvdID = params.get("TvdID")
        self._IsOneClick = params.get("IsOneClick")
        self._IsPOC = params.get("IsPOC")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewWeakPassRisk(AbstractModel):
    r"""资产视角的弱口令风险

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: ID，处理风险使用
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _PasswordType: 弱口令类型
        :type PasswordType: str
        :param _From: 来源
        :type From: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULURL: 漏洞url
        :type VULURL: str
        :param _Fix: 修复建议
        :type Fix: str
        :param _Payload: 证明
        :type Payload: str
        :param _Port: 端口
        :type Port: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._PasswordType = None
        self._From = None
        self._VULType = None
        self._VULURL = None
        self._Fix = None
        self._Payload = None
        self._Port = None

    @property
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""服务
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""状态，0未处理、1已处置、2已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""ID，处理风险使用
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def PasswordType(self):
        r"""弱口令类型
        :rtype: str
        """
        return self._PasswordType

    @PasswordType.setter
    def PasswordType(self, PasswordType):
        self._PasswordType = PasswordType

    @property
    def From(self):
        r"""来源
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULURL(self):
        r"""漏洞url
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Fix(self):
        r"""修复建议
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def Payload(self):
        r"""证明
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Port(self):
        r"""端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._PasswordType = params.get("PasswordType")
        self._From = params.get("From")
        self._VULType = params.get("VULType")
        self._VULURL = params.get("VULURL")
        self._Fix = params.get("Fix")
        self._Payload = params.get("Payload")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeOptionSet(AbstractModel):
    r"""通用的下拉框列表

    """

    def __init__(self):
        r"""
        :param _Text: cvm实例类型
        :type Text: str
        :param _Value: cvm实例名称
        :type Value: str
        """
        self._Text = None
        self._Value = None

    @property
    def Text(self):
        r"""cvm实例类型
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        r"""cvm实例名称
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BugInfoDetail(AbstractModel):
    r"""漏洞详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞编号
        :type Id: int
        :param _PatchId: 漏洞对应pocId
        :type PatchId: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _Level: 漏洞严重性：high,middle，low，info
        :type Level: str
        :param _CVSSScore: cvss评分
        :type CVSSScore: str
        :param _CVEId: cve编号
        :type CVEId: str
        :param _Tag: 漏洞标签
        :type Tag: str
        :param _VULCategory: 漏洞种类，1:web应用，2:系统组件漏洞，3:配置风险
        :type VULCategory: int
        :param _ImpactOs: 漏洞影响系统
        :type ImpactOs: str
        :param _ImpactCOMPENT: 漏洞影响组件
        :type ImpactCOMPENT: str
        :param _ImpactVersion: 漏洞影响版本
        :type ImpactVersion: str
        :param _Reference: 链接
        :type Reference: str
        :param _VULDescribe: 漏洞描述
        :type VULDescribe: str
        :param _Fix: 修复建议
        :type Fix: str
        :param _ProSupport: 产品支持状态，实时返回
        :type ProSupport: int
        :param _IsPublish: 是否公开，0为未发布，1为发布
        :type IsPublish: int
        :param _ReleaseTime: 释放时间
        :type ReleaseTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _SubCategory: 漏洞子类别
        :type SubCategory: str
        """
        self._Id = None
        self._PatchId = None
        self._VULName = None
        self._Level = None
        self._CVSSScore = None
        self._CVEId = None
        self._Tag = None
        self._VULCategory = None
        self._ImpactOs = None
        self._ImpactCOMPENT = None
        self._ImpactVersion = None
        self._Reference = None
        self._VULDescribe = None
        self._Fix = None
        self._ProSupport = None
        self._IsPublish = None
        self._ReleaseTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubCategory = None

    @property
    def Id(self):
        r"""漏洞编号
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PatchId(self):
        r"""漏洞对应pocId
        :rtype: str
        """
        return self._PatchId

    @PatchId.setter
    def PatchId(self, PatchId):
        self._PatchId = PatchId

    @property
    def VULName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def Level(self):
        r"""漏洞严重性：high,middle，low，info
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CVSSScore(self):
        r"""cvss评分
        :rtype: str
        """
        return self._CVSSScore

    @CVSSScore.setter
    def CVSSScore(self, CVSSScore):
        self._CVSSScore = CVSSScore

    @property
    def CVEId(self):
        r"""cve编号
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def Tag(self):
        r"""漏洞标签
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def VULCategory(self):
        r"""漏洞种类，1:web应用，2:系统组件漏洞，3:配置风险
        :rtype: int
        """
        return self._VULCategory

    @VULCategory.setter
    def VULCategory(self, VULCategory):
        self._VULCategory = VULCategory

    @property
    def ImpactOs(self):
        r"""漏洞影响系统
        :rtype: str
        """
        return self._ImpactOs

    @ImpactOs.setter
    def ImpactOs(self, ImpactOs):
        self._ImpactOs = ImpactOs

    @property
    def ImpactCOMPENT(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._ImpactCOMPENT

    @ImpactCOMPENT.setter
    def ImpactCOMPENT(self, ImpactCOMPENT):
        self._ImpactCOMPENT = ImpactCOMPENT

    @property
    def ImpactVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def Reference(self):
        r"""链接
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def VULDescribe(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def Fix(self):
        r"""修复建议
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def ProSupport(self):
        r"""产品支持状态，实时返回
        :rtype: int
        """
        return self._ProSupport

    @ProSupport.setter
    def ProSupport(self, ProSupport):
        self._ProSupport = ProSupport

    @property
    def IsPublish(self):
        r"""是否公开，0为未发布，1为发布
        :rtype: int
        """
        return self._IsPublish

    @IsPublish.setter
    def IsPublish(self, IsPublish):
        self._IsPublish = IsPublish

    @property
    def ReleaseTime(self):
        r"""释放时间
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SubCategory(self):
        r"""漏洞子类别
        :rtype: str
        """
        return self._SubCategory

    @SubCategory.setter
    def SubCategory(self, SubCategory):
        self._SubCategory = SubCategory


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PatchId = params.get("PatchId")
        self._VULName = params.get("VULName")
        self._Level = params.get("Level")
        self._CVSSScore = params.get("CVSSScore")
        self._CVEId = params.get("CVEId")
        self._Tag = params.get("Tag")
        self._VULCategory = params.get("VULCategory")
        self._ImpactOs = params.get("ImpactOs")
        self._ImpactCOMPENT = params.get("ImpactCOMPENT")
        self._ImpactVersion = params.get("ImpactVersion")
        self._Reference = params.get("Reference")
        self._VULDescribe = params.get("VULDescribe")
        self._Fix = params.get("Fix")
        self._ProSupport = params.get("ProSupport")
        self._IsPublish = params.get("IsPublish")
        self._ReleaseTime = params.get("ReleaseTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubCategory = params.get("SubCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFGViewCFGRisk(AbstractModel):
    r"""配置视角的配置风险对象

    """

    def __init__(self):
        r"""
        :param _NoHandleCount: 影响资产
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _AffectAssetCount: 状态，0未处理、1已处置、2已忽略
        :type AffectAssetCount: int
        :param _Id: 资产唯一id
        :type Id: str
        :param _From: 资产子类型
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _CFGName: 配置名
注意：此字段可能返回 null，表示取不到有效值。
        :type CFGName: str
        :param _CheckType: 检查类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckType: str
        :param _CFGSTD: -
注意：此字段可能返回 null，表示取不到有效值。
        :type CFGSTD: str
        :param _CFGDescribe: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type CFGDescribe: str
        :param _CFGFix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type CFGFix: str
        :param _CFGHelpURL: 帮助文档
注意：此字段可能返回 null，表示取不到有效值。
        :type CFGHelpURL: str
        """
        self._NoHandleCount = None
        self._Level = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._CFGName = None
        self._CheckType = None
        self._CFGSTD = None
        self._CFGDescribe = None
        self._CFGFix = None
        self._CFGHelpURL = None

    @property
    def NoHandleCount(self):
        r"""影响资产
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""状态，0未处理、1已处置、2已忽略
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""资产唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""资产子类型
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CFGName(self):
        r"""配置名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CFGName

    @CFGName.setter
    def CFGName(self, CFGName):
        self._CFGName = CFGName

    @property
    def CheckType(self):
        r"""检查类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CFGSTD(self):
        r"""-
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CFGSTD

    @CFGSTD.setter
    def CFGSTD(self, CFGSTD):
        self._CFGSTD = CFGSTD

    @property
    def CFGDescribe(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CFGDescribe

    @CFGDescribe.setter
    def CFGDescribe(self, CFGDescribe):
        self._CFGDescribe = CFGDescribe

    @property
    def CFGFix(self):
        r"""修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CFGFix

    @CFGFix.setter
    def CFGFix(self, CFGFix):
        self._CFGFix = CFGFix

    @property
    def CFGHelpURL(self):
        r"""帮助文档
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CFGHelpURL

    @CFGHelpURL.setter
    def CFGHelpURL(self, CFGHelpURL):
        self._CFGHelpURL = CFGHelpURL


    def _deserialize(self, params):
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._CFGName = params.get("CFGName")
        self._CheckType = params.get("CheckType")
        self._CFGSTD = params.get("CFGSTD")
        self._CFGDescribe = params.get("CFGDescribe")
        self._CFGFix = params.get("CFGFix")
        self._CFGHelpURL = params.get("CFGHelpURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMAssetVO(AbstractModel):
    r"""主机资产信息

    主机防护状态枚举，左边是常量，右边是显示
    0：未安装
    1：基础版防护中
    2：普惠版防护中
    3：专业版防护中
    4：旗舰版防护中
    5：已离线
    6：已关机

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Region: 地域
        :type Region: str
        :param _CWPStatus: 防护状态
        :type CWPStatus: int
        :param _AssetCreateTime: 资产创建时间
        :type AssetCreateTime: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _PrivateIp: 私网IP
        :type PrivateIp: str
        :param _VpcId: vpc id
        :type VpcId: str
        :param _VpcName: vpc 名
        :type VpcName: str
        :param _AppId: appid信息
        :type AppId: int
        :param _Uin: 用户uin
        :type Uin: str
        :param _NickName: 昵称
        :type NickName: str
        :param _AvailableArea: 可用区
        :type AvailableArea: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _SubnetName: 子网名
        :type SubnetName: str
        :param _InstanceUuid: 主机安全Agent UUID
        :type InstanceUuid: str
        :param _InstanceQUuid: 云主机 CVM UUID
        :type InstanceQUuid: str
        :param _OsName: os名
        :type OsName: str
        :param _PartitionCount: 分区
        :type PartitionCount: int
        :param _CPUInfo: cpu信息
        :type CPUInfo: str
        :param _CPUSize: cpu大小
        :type CPUSize: int
        :param _CPULoad: cpu负载
        :type CPULoad: str
        :param _MemorySize: 内存大小
        :type MemorySize: str
        :param _MemoryLoad: 内存负载
        :type MemoryLoad: str
        :param _DiskSize: 硬盘大小
        :type DiskSize: str
        :param _DiskLoad: 硬盘负载
        :type DiskLoad: str
        :param _AccountCount: 账号数
        :type AccountCount: str
        :param _ProcessCount: 进程数
        :type ProcessCount: str
        :param _AppCount: 软件应用
        :type AppCount: str
        :param _PortCount: 监听端口
        :type PortCount: int
        :param _Attack: 网络攻击
        :type Attack: int
        :param _Access: 网络访问
        :type Access: int
        :param _Intercept: 网络拦截
        :type Intercept: int
        :param _InBandwidth: 入向峰值带宽
        :type InBandwidth: str
        :param _OutBandwidth: 出向峰值带宽
        :type OutBandwidth: str
        :param _InFlow: 入向累计流量
        :type InFlow: str
        :param _OutFlow: 出向累计流量
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _NetWorkOut: 恶意主动外联
        :type NetWorkOut: int
        :param _PortRisk: 端口风险
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务数
        :type ScanTask: int
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _MemberId: memberId
        :type MemberId: str
        :param _Os: os全称
        :type Os: str
        :param _RiskExposure: 风险服务暴露
        :type RiskExposure: int
        :param _BASAgentStatus: 模拟攻击工具状态。0代表未安装，1代表已安装，2代表已离线
        :type BASAgentStatus: int
        :param _IsNewAsset: 1新资产；0 非新资产
        :type IsNewAsset: int
        :param _CVMAgentStatus: 0 未安装  1安装 2:安装中
        :type CVMAgentStatus: int
        :param _CVMStatus: 1:开启 0:未开启
        :type CVMStatus: int
        :param _DefenseModel: 1:客户端已安装 0：未安装 2: Agentless
        :type DefenseModel: int
        :param _TatStatus: 1:已安装 0:未安装
        :type TatStatus: int
        :param _CpuTrend: cpu趋势图
        :type CpuTrend: list of Element
        :param _MemoryTrend: 内存趋势图
        :type MemoryTrend: list of Element
        :param _AgentStatus: 1:agent在线 0:agent离线 2:主机离线
        :type AgentStatus: int
        :param _CloseDefenseCount: 本月防护关闭次数
        :type CloseDefenseCount: int
        :param _InstanceState: 运行状态
        :type InstanceState: str
        :param _SecurityGroupIds: 安全组数据
        :type SecurityGroupIds: list of str
        :param _AgentMemRss: 物理内存占用KB
        :type AgentMemRss: int
        :param _AgentCpuPer: CPU使用率百分比
        :type AgentCpuPer: float
        :param _RealAppid: cvm真正所属的appid
        :type RealAppid: int
        :param _CloudType: 云资产类型：0：腾讯云，1：aws，2：azure
        :type CloudType: int
        :param _ProtectStatus: 主机防护状态枚举
0：未安装
1：基础版防护中
2：普惠版防护中
3：专业版防护中
4：旗舰版防护中
5：已离线
6：已关机
        :type ProtectStatus: int
        :param _OfflineTime: 最后离线时间
        :type OfflineTime: str
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CWPStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PrivateIp = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._AvailableArea = None
        self._IsCore = None
        self._SubnetId = None
        self._SubnetName = None
        self._InstanceUuid = None
        self._InstanceQUuid = None
        self._OsName = None
        self._PartitionCount = None
        self._CPUInfo = None
        self._CPUSize = None
        self._CPULoad = None
        self._MemorySize = None
        self._MemoryLoad = None
        self._DiskSize = None
        self._DiskLoad = None
        self._AccountCount = None
        self._ProcessCount = None
        self._AppCount = None
        self._PortCount = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._NetWorkOut = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._Tag = None
        self._MemberId = None
        self._Os = None
        self._RiskExposure = None
        self._BASAgentStatus = None
        self._IsNewAsset = None
        self._CVMAgentStatus = None
        self._CVMStatus = None
        self._DefenseModel = None
        self._TatStatus = None
        self._CpuTrend = None
        self._MemoryTrend = None
        self._AgentStatus = None
        self._CloseDefenseCount = None
        self._InstanceState = None
        self._SecurityGroupIds = None
        self._AgentMemRss = None
        self._AgentCpuPer = None
        self._RealAppid = None
        self._CloudType = None
        self._ProtectStatus = None
        self._OfflineTime = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CWPStatus(self):
        r"""防护状态
        :rtype: int
        """
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def AssetCreateTime(self):
        r"""资产创建时间
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

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
        r"""私网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def VpcId(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc 名
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        r"""appid信息
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def AvailableArea(self):
        r"""可用区
        :rtype: str
        """
        return self._AvailableArea

    @AvailableArea.setter
    def AvailableArea(self, AvailableArea):
        self._AvailableArea = AvailableArea

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def SubnetId(self):
        r"""子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""子网名
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def InstanceUuid(self):
        r"""主机安全Agent UUID
        :rtype: str
        """
        return self._InstanceUuid

    @InstanceUuid.setter
    def InstanceUuid(self, InstanceUuid):
        self._InstanceUuid = InstanceUuid

    @property
    def InstanceQUuid(self):
        r"""云主机 CVM UUID
        :rtype: str
        """
        return self._InstanceQUuid

    @InstanceQUuid.setter
    def InstanceQUuid(self, InstanceQUuid):
        self._InstanceQUuid = InstanceQUuid

    @property
    def OsName(self):
        r"""os名
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def PartitionCount(self):
        r"""分区
        :rtype: int
        """
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def CPUInfo(self):
        r"""cpu信息
        :rtype: str
        """
        return self._CPUInfo

    @CPUInfo.setter
    def CPUInfo(self, CPUInfo):
        self._CPUInfo = CPUInfo

    @property
    def CPUSize(self):
        r"""cpu大小
        :rtype: int
        """
        return self._CPUSize

    @CPUSize.setter
    def CPUSize(self, CPUSize):
        self._CPUSize = CPUSize

    @property
    def CPULoad(self):
        r"""cpu负载
        :rtype: str
        """
        return self._CPULoad

    @CPULoad.setter
    def CPULoad(self, CPULoad):
        self._CPULoad = CPULoad

    @property
    def MemorySize(self):
        r"""内存大小
        :rtype: str
        """
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def MemoryLoad(self):
        r"""内存负载
        :rtype: str
        """
        return self._MemoryLoad

    @MemoryLoad.setter
    def MemoryLoad(self, MemoryLoad):
        self._MemoryLoad = MemoryLoad

    @property
    def DiskSize(self):
        r"""硬盘大小
        :rtype: str
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskLoad(self):
        r"""硬盘负载
        :rtype: str
        """
        return self._DiskLoad

    @DiskLoad.setter
    def DiskLoad(self, DiskLoad):
        self._DiskLoad = DiskLoad

    @property
    def AccountCount(self):
        r"""账号数
        :rtype: str
        """
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def ProcessCount(self):
        r"""进程数
        :rtype: str
        """
        return self._ProcessCount

    @ProcessCount.setter
    def ProcessCount(self, ProcessCount):
        self._ProcessCount = ProcessCount

    @property
    def AppCount(self):
        r"""软件应用
        :rtype: str
        """
        return self._AppCount

    @AppCount.setter
    def AppCount(self, AppCount):
        self._AppCount = AppCount

    @property
    def PortCount(self):
        r"""监听端口
        :rtype: int
        """
        return self._PortCount

    @PortCount.setter
    def PortCount(self, PortCount):
        self._PortCount = PortCount

    @property
    def Attack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""网络访问
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""网络拦截
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""入向峰值带宽
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""出向峰值带宽
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""入向累计流量
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""出向累计流量
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def NetWorkOut(self):
        r"""恶意主动外联
        :rtype: int
        """
        return self._NetWorkOut

    @NetWorkOut.setter
    def NetWorkOut(self, NetWorkOut):
        self._NetWorkOut = NetWorkOut

    @property
    def PortRisk(self):
        r"""端口风险
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""扫描任务数
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MemberId(self):
        r"""memberId
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Os(self):
        r"""os全称
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def RiskExposure(self):
        r"""风险服务暴露
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def BASAgentStatus(self):
        r"""模拟攻击工具状态。0代表未安装，1代表已安装，2代表已离线
        :rtype: int
        """
        return self._BASAgentStatus

    @BASAgentStatus.setter
    def BASAgentStatus(self, BASAgentStatus):
        self._BASAgentStatus = BASAgentStatus

    @property
    def IsNewAsset(self):
        r"""1新资产；0 非新资产
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def CVMAgentStatus(self):
        r"""0 未安装  1安装 2:安装中
        :rtype: int
        """
        return self._CVMAgentStatus

    @CVMAgentStatus.setter
    def CVMAgentStatus(self, CVMAgentStatus):
        self._CVMAgentStatus = CVMAgentStatus

    @property
    def CVMStatus(self):
        r"""1:开启 0:未开启
        :rtype: int
        """
        return self._CVMStatus

    @CVMStatus.setter
    def CVMStatus(self, CVMStatus):
        self._CVMStatus = CVMStatus

    @property
    def DefenseModel(self):
        r"""1:客户端已安装 0：未安装 2: Agentless
        :rtype: int
        """
        return self._DefenseModel

    @DefenseModel.setter
    def DefenseModel(self, DefenseModel):
        self._DefenseModel = DefenseModel

    @property
    def TatStatus(self):
        r"""1:已安装 0:未安装
        :rtype: int
        """
        return self._TatStatus

    @TatStatus.setter
    def TatStatus(self, TatStatus):
        self._TatStatus = TatStatus

    @property
    def CpuTrend(self):
        r"""cpu趋势图
        :rtype: list of Element
        """
        return self._CpuTrend

    @CpuTrend.setter
    def CpuTrend(self, CpuTrend):
        self._CpuTrend = CpuTrend

    @property
    def MemoryTrend(self):
        r"""内存趋势图
        :rtype: list of Element
        """
        return self._MemoryTrend

    @MemoryTrend.setter
    def MemoryTrend(self, MemoryTrend):
        self._MemoryTrend = MemoryTrend

    @property
    def AgentStatus(self):
        r"""1:agent在线 0:agent离线 2:主机离线
        :rtype: int
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def CloseDefenseCount(self):
        r"""本月防护关闭次数
        :rtype: int
        """
        return self._CloseDefenseCount

    @CloseDefenseCount.setter
    def CloseDefenseCount(self, CloseDefenseCount):
        self._CloseDefenseCount = CloseDefenseCount

    @property
    def InstanceState(self):
        r"""运行状态
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def SecurityGroupIds(self):
        r"""安全组数据
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AgentMemRss(self):
        r"""物理内存占用KB
        :rtype: int
        """
        return self._AgentMemRss

    @AgentMemRss.setter
    def AgentMemRss(self, AgentMemRss):
        self._AgentMemRss = AgentMemRss

    @property
    def AgentCpuPer(self):
        r"""CPU使用率百分比
        :rtype: float
        """
        return self._AgentCpuPer

    @AgentCpuPer.setter
    def AgentCpuPer(self, AgentCpuPer):
        self._AgentCpuPer = AgentCpuPer

    @property
    def RealAppid(self):
        r"""cvm真正所属的appid
        :rtype: int
        """
        return self._RealAppid

    @RealAppid.setter
    def RealAppid(self, RealAppid):
        self._RealAppid = RealAppid

    @property
    def CloudType(self):
        r"""云资产类型：0：腾讯云，1：aws，2：azure
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def ProtectStatus(self):
        r"""主机防护状态枚举
0：未安装
1：基础版防护中
2：普惠版防护中
3：专业版防护中
4：旗舰版防护中
5：已离线
6：已关机
        :rtype: int
        """
        return self._ProtectStatus

    @ProtectStatus.setter
    def ProtectStatus(self, ProtectStatus):
        self._ProtectStatus = ProtectStatus

    @property
    def OfflineTime(self):
        r"""最后离线时间
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CWPStatus = params.get("CWPStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._AvailableArea = params.get("AvailableArea")
        self._IsCore = params.get("IsCore")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._InstanceUuid = params.get("InstanceUuid")
        self._InstanceQUuid = params.get("InstanceQUuid")
        self._OsName = params.get("OsName")
        self._PartitionCount = params.get("PartitionCount")
        self._CPUInfo = params.get("CPUInfo")
        self._CPUSize = params.get("CPUSize")
        self._CPULoad = params.get("CPULoad")
        self._MemorySize = params.get("MemorySize")
        self._MemoryLoad = params.get("MemoryLoad")
        self._DiskSize = params.get("DiskSize")
        self._DiskLoad = params.get("DiskLoad")
        self._AccountCount = params.get("AccountCount")
        self._ProcessCount = params.get("ProcessCount")
        self._AppCount = params.get("AppCount")
        self._PortCount = params.get("PortCount")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._NetWorkOut = params.get("NetWorkOut")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._MemberId = params.get("MemberId")
        self._Os = params.get("Os")
        self._RiskExposure = params.get("RiskExposure")
        self._BASAgentStatus = params.get("BASAgentStatus")
        self._IsNewAsset = params.get("IsNewAsset")
        self._CVMAgentStatus = params.get("CVMAgentStatus")
        self._CVMStatus = params.get("CVMStatus")
        self._DefenseModel = params.get("DefenseModel")
        self._TatStatus = params.get("TatStatus")
        if params.get("CpuTrend") is not None:
            self._CpuTrend = []
            for item in params.get("CpuTrend"):
                obj = Element()
                obj._deserialize(item)
                self._CpuTrend.append(obj)
        if params.get("MemoryTrend") is not None:
            self._MemoryTrend = []
            for item in params.get("MemoryTrend"):
                obj = Element()
                obj._deserialize(item)
                self._MemoryTrend.append(obj)
        self._AgentStatus = params.get("AgentStatus")
        self._CloseDefenseCount = params.get("CloseDefenseCount")
        self._InstanceState = params.get("InstanceState")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AgentMemRss = params.get("AgentMemRss")
        self._AgentCpuPer = params.get("AgentCpuPer")
        self._RealAppid = params.get("RealAppid")
        self._CloudType = params.get("CloudType")
        self._ProtectStatus = params.get("ProtectStatus")
        self._OfflineTime = params.get("OfflineTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallRecord(AbstractModel):
    r"""调用记录详情

    """

    def __init__(self):
        r"""
        :param _CallID: 调用记录ID
        :type CallID: str
        :param _AccessKey: 访问密钥
        :type AccessKey: str
        :param _AccessKeyRemark: 访问密钥备注
        :type AccessKeyRemark: str
        :param _AccessKeyID: 访问密钥ID
        :type AccessKeyID: int
        :param _SourceIP: 调用源IP
        :type SourceIP: str
        :param _SourceIPRemark: 调用源IP备注
        :type SourceIPRemark: str
        :param _Region: 调用源IP地域
        :type Region: str
        :param _IPType: IP类型 0:账号内（未备注） 1:账号外（未备注） 2:账号内 (已备注) 3:账号外 (已备注)
        :type IPType: int
        :param _EventName: 调用接口名称
        :type EventName: str
        :param _ProductName: 调用产品名称
        :type ProductName: str
        :param _EventType: 调用类型
0:控制台调用
1:API
        :type EventType: int
        :param _UserType: 用户类型CAMUser/root/AssumedRole

        :type UserType: str
        :param _UserName: 用户/角色名称
        :type UserName: str
        :param _PolicySet: 策略列表
        :type PolicySet: list of str
        :param _CallCount: 调用次数
        :type CallCount: int
        :param _Code: 调用错误码
0表示成功
        :type Code: int
        :param _FirstCallTime: 首次调用时间
        :type FirstCallTime: str
        :param _LastCallTime: 最后调用时间
        :type LastCallTime: str
        :param _InstanceID: IP关联资产ID，如果为空字符串，表示没有关联
        :type InstanceID: str
        :param _InstanceName: IP关联资产名称
        :type InstanceName: str
        :param _Date: 聚合日期
        :type Date: str
        :param _AppID: appid
        :type AppID: int
        :param _ShowStatus: 展示状态
        :type ShowStatus: bool
        :param _ISP: 运营商
        :type ISP: str
        :param _VpcInfo: 账号外vpc信息列表
        :type VpcInfo: list of SourceIPVpcInfo
        :param _ReqClient: 调用请求客户端列表
        :type ReqClient: list of str
        """
        self._CallID = None
        self._AccessKey = None
        self._AccessKeyRemark = None
        self._AccessKeyID = None
        self._SourceIP = None
        self._SourceIPRemark = None
        self._Region = None
        self._IPType = None
        self._EventName = None
        self._ProductName = None
        self._EventType = None
        self._UserType = None
        self._UserName = None
        self._PolicySet = None
        self._CallCount = None
        self._Code = None
        self._FirstCallTime = None
        self._LastCallTime = None
        self._InstanceID = None
        self._InstanceName = None
        self._Date = None
        self._AppID = None
        self._ShowStatus = None
        self._ISP = None
        self._VpcInfo = None
        self._ReqClient = None

    @property
    def CallID(self):
        r"""调用记录ID
        :rtype: str
        """
        return self._CallID

    @CallID.setter
    def CallID(self, CallID):
        self._CallID = CallID

    @property
    def AccessKey(self):
        r"""访问密钥
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyRemark(self):
        r"""访问密钥备注
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def AccessKeyID(self):
        r"""访问密钥ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIP(self):
        r"""调用源IP
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def SourceIPRemark(self):
        r"""调用源IP备注
        :rtype: str
        """
        return self._SourceIPRemark

    @SourceIPRemark.setter
    def SourceIPRemark(self, SourceIPRemark):
        self._SourceIPRemark = SourceIPRemark

    @property
    def Region(self):
        r"""调用源IP地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IPType(self):
        r"""IP类型 0:账号内（未备注） 1:账号外（未备注） 2:账号内 (已备注) 3:账号外 (已备注)
        :rtype: int
        """
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def EventName(self):
        r"""调用接口名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def ProductName(self):
        r"""调用产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EventType(self):
        r"""调用类型
0:控制台调用
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def UserType(self):
        r"""用户类型CAMUser/root/AssumedRole

        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserName(self):
        r"""用户/角色名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PolicySet(self):
        r"""策略列表
        :rtype: list of str
        """
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def CallCount(self):
        r"""调用次数
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def Code(self):
        r"""调用错误码
0表示成功
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def FirstCallTime(self):
        r"""首次调用时间
        :rtype: str
        """
        return self._FirstCallTime

    @FirstCallTime.setter
    def FirstCallTime(self, FirstCallTime):
        self._FirstCallTime = FirstCallTime

    @property
    def LastCallTime(self):
        r"""最后调用时间
        :rtype: str
        """
        return self._LastCallTime

    @LastCallTime.setter
    def LastCallTime(self, LastCallTime):
        self._LastCallTime = LastCallTime

    @property
    def InstanceID(self):
        r"""IP关联资产ID，如果为空字符串，表示没有关联
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def InstanceName(self):
        r"""IP关联资产名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Date(self):
        r"""聚合日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        r"""appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ShowStatus(self):
        r"""展示状态
        :rtype: bool
        """
        return self._ShowStatus

    @ShowStatus.setter
    def ShowStatus(self, ShowStatus):
        self._ShowStatus = ShowStatus

    @property
    def ISP(self):
        r"""运营商
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcInfo(self):
        r"""账号外vpc信息列表
        :rtype: list of SourceIPVpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def ReqClient(self):
        r"""调用请求客户端列表
        :rtype: list of str
        """
        return self._ReqClient

    @ReqClient.setter
    def ReqClient(self, ReqClient):
        self._ReqClient = ReqClient


    def _deserialize(self, params):
        self._CallID = params.get("CallID")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIP = params.get("SourceIP")
        self._SourceIPRemark = params.get("SourceIPRemark")
        self._Region = params.get("Region")
        self._IPType = params.get("IPType")
        self._EventName = params.get("EventName")
        self._ProductName = params.get("ProductName")
        self._EventType = params.get("EventType")
        self._UserType = params.get("UserType")
        self._UserName = params.get("UserName")
        self._PolicySet = params.get("PolicySet")
        self._CallCount = params.get("CallCount")
        self._Code = params.get("Code")
        self._FirstCallTime = params.get("FirstCallTime")
        self._LastCallTime = params.get("LastCallTime")
        self._InstanceID = params.get("InstanceID")
        self._InstanceName = params.get("InstanceName")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._ShowStatus = params.get("ShowStatus")
        self._ISP = params.get("ISP")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = SourceIPVpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._ReqClient = params.get("ReqClient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckViewRiskItem(AbstractModel):
    r"""检查项视角风险

    """

    def __init__(self):
        r"""
        :param _RiskRuleId: 检查项规则ID
        :type RiskRuleId: str
        :param _RiskTitle: 风险名称
        :type RiskTitle: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _Severity: 风险等级
        :type Severity: str
        :param _RiskDesc: 存在1个风险项
        :type RiskDesc: str
        :param _CreateTime: 首次发现时间
        :type CreateTime: str
        :param _UpdateTime: 风险更新时间
        :type UpdateTime: str
        :param _Provider: 云厂商
        :type Provider: str
        :param _RiskStatus: 风险状态
        :type RiskStatus: int
        :param _AssetCount: 受影响资产数量
        :type AssetCount: int
        :param _RiskCount: 风险数量
        :type RiskCount: int
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _EventType: 事件类型
        :type EventType: str
        :param _Classify: 处置分类
        :type Classify: str
        :param _StandardTerms: cspm规范条款
        :type StandardTerms: list of StandardTerm
        """
        self._RiskRuleId = None
        self._RiskTitle = None
        self._CheckType = None
        self._Severity = None
        self._RiskDesc = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Provider = None
        self._RiskStatus = None
        self._AssetCount = None
        self._RiskCount = None
        self._AssetType = None
        self._EventType = None
        self._Classify = None
        self._StandardTerms = None

    @property
    def RiskRuleId(self):
        r"""检查项规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId

    @property
    def RiskTitle(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskTitle

    @RiskTitle.setter
    def RiskTitle(self, RiskTitle):
        self._RiskTitle = RiskTitle

    @property
    def CheckType(self):
        r"""检查类型
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Severity(self):
        r"""风险等级
        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def RiskDesc(self):
        r"""存在1个风险项
        :rtype: str
        """
        return self._RiskDesc

    @RiskDesc.setter
    def RiskDesc(self, RiskDesc):
        self._RiskDesc = RiskDesc

    @property
    def CreateTime(self):
        r"""首次发现时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""风险更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def RiskStatus(self):
        r"""风险状态
        :rtype: int
        """
        return self._RiskStatus

    @RiskStatus.setter
    def RiskStatus(self, RiskStatus):
        self._RiskStatus = RiskStatus

    @property
    def AssetCount(self):
        r"""受影响资产数量
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def RiskCount(self):
        r"""风险数量
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def EventType(self):
        r"""事件类型
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Classify(self):
        r"""处置分类
        :rtype: str
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify

    @property
    def StandardTerms(self):
        r"""cspm规范条款
        :rtype: list of StandardTerm
        """
        return self._StandardTerms

    @StandardTerms.setter
    def StandardTerms(self, StandardTerms):
        self._StandardTerms = StandardTerms


    def _deserialize(self, params):
        self._RiskRuleId = params.get("RiskRuleId")
        self._RiskTitle = params.get("RiskTitle")
        self._CheckType = params.get("CheckType")
        self._Severity = params.get("Severity")
        self._RiskDesc = params.get("RiskDesc")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Provider = params.get("Provider")
        self._RiskStatus = params.get("RiskStatus")
        self._AssetCount = params.get("AssetCount")
        self._RiskCount = params.get("RiskCount")
        self._AssetType = params.get("AssetType")
        self._EventType = params.get("EventType")
        self._Classify = params.get("Classify")
        if params.get("StandardTerms") is not None:
            self._StandardTerms = []
            for item in params.get("StandardTerms"):
                obj = StandardTerm()
                obj._deserialize(item)
                self._StandardTerms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerListInfo(AbstractModel):
    r"""clb实例和监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器id
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _LoadBalancerId: 负载均衡Id
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名称
        :type LoadBalancerName: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Region: 地域
        :type Region: str
        :param _Vip: 负载均衡ip
        :type Vip: str
        :param _VPort: 端口
        :type VPort: int
        :param _Zone: 区域
        :type Zone: str
        :param _NumericalVpcId: 私有网络id
        :type NumericalVpcId: int
        :param _LoadBalancerType: 负载均衡类型
        :type LoadBalancerType: str
        :param _Domain: 监听器域名
        :type Domain: str
        :param _LoadBalancerDomain: 负载均衡域名
        :type LoadBalancerDomain: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Protocol = None
        self._Region = None
        self._Vip = None
        self._VPort = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._Domain = None
        self._LoadBalancerDomain = None

    @property
    def ListenerId(self):
        r"""监听器id
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def LoadBalancerId(self):
        r"""负载均衡Id
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""负载均衡名称
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

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
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        r"""负载均衡ip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        r"""端口
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Zone(self):
        r"""区域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        r"""私有网络id
        :rtype: int
        """
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        r"""负载均衡类型
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Domain(self):
        r"""监听器域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerDomain(self):
        r"""负载均衡域名
        :rtype: str
        """
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Protocol = params.get("Protocol")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Domain = params.get("Domain")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudCountDesc(AbstractModel):
    r"""多云账户统计信息

    """

    def __init__(self):
        r"""
        :param _CloudType: 0表示腾讯云
1表示AWS
        :type CloudType: int
        :param _CloudCount: 账户数量
        :type CloudCount: int
        :param _CloudDesc: 该云账号类型描述
        :type CloudDesc: str
        """
        self._CloudType = None
        self._CloudCount = None
        self._CloudDesc = None

    @property
    def CloudType(self):
        r"""0表示腾讯云
1表示AWS
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def CloudCount(self):
        r"""账户数量
        :rtype: int
        """
        return self._CloudCount

    @CloudCount.setter
    def CloudCount(self, CloudCount):
        self._CloudCount = CloudCount

    @property
    def CloudDesc(self):
        r"""该云账号类型描述
        :rtype: str
        """
        return self._CloudDesc

    @CloudDesc.setter
    def CloudDesc(self, CloudDesc):
        self._CloudDesc = CloudDesc


    def _deserialize(self, params):
        self._CloudType = params.get("CloudType")
        self._CloudCount = params.get("CloudCount")
        self._CloudDesc = params.get("CloudDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyCheckTaskRequest(AbstractModel):
    r"""CreateAccessKeyCheckTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _RiskIDList: 风险列表
        :type RiskIDList: list of int
        :param _AccessKeyList: 访问密钥列表
        :type AccessKeyList: list of str
        :param _SubUinList: 账号uin列表
        :type SubUinList: list of str
        :param _RiskRuleIDList: 风险规则id列表
        :type RiskRuleIDList: list of int
        """
        self._MemberId = None
        self._RiskIDList = None
        self._AccessKeyList = None
        self._SubUinList = None
        self._RiskRuleIDList = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskIDList(self):
        r"""风险列表
        :rtype: list of int
        """
        return self._RiskIDList

    @RiskIDList.setter
    def RiskIDList(self, RiskIDList):
        self._RiskIDList = RiskIDList

    @property
    def AccessKeyList(self):
        r"""访问密钥列表
        :rtype: list of str
        """
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList

    @property
    def SubUinList(self):
        r"""账号uin列表
        :rtype: list of str
        """
        return self._SubUinList

    @SubUinList.setter
    def SubUinList(self, SubUinList):
        self._SubUinList = SubUinList

    @property
    def RiskRuleIDList(self):
        r"""风险规则id列表
        :rtype: list of int
        """
        return self._RiskRuleIDList

    @RiskRuleIDList.setter
    def RiskRuleIDList(self, RiskRuleIDList):
        self._RiskRuleIDList = RiskRuleIDList


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._RiskIDList = params.get("RiskIDList")
        self._AccessKeyList = params.get("AccessKeyList")
        self._SubUinList = params.get("SubUinList")
        self._RiskRuleIDList = params.get("RiskRuleIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyCheckTaskResponse(AbstractModel):
    r"""CreateAccessKeyCheckTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 0表示成功 1表示失败
        :type Code: int
        :param _Msg: 错误信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0表示成功 1表示失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""错误信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateAccessKeySyncTaskRequest(AbstractModel):
    r"""CreateAccessKeySyncTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeySyncTaskResponse(AbstractModel):
    r"""CreateAccessKeySyncTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 发起同步任务
        :type TaskID: int
        :param _Code: 0成功 1失败
        :type Code: int
        :param _Msg: 错误信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def TaskID(self):
        r"""发起同步任务
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Code(self):
        r"""0成功 1失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""错误信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._TaskID = params.get("TaskID")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateDomainAndIpRequest(AbstractModel):
    r"""CreateDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 公网IP/域名
        :type Content: list of str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._Content = None
        self._MemberId = None
        self._Tags = None

    @property
    def Content(self):
        r"""公网IP/域名
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._MemberId = params.get("MemberId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpResponse(AbstractModel):
    r"""CreateDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回创建成功的数量
        :type Data: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回创建成功的数量
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateRiskCenterScanTaskRequest(AbstractModel):
    r"""CreateRiskCenterScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :type ScanAssetType: int
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk/exposedserver
        :type ScanItem: list of str
        :param _ScanPlanType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :type ScanPlanType: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Assets: 扫描资产信息列表
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: 扫描计划详情
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: ip/域名/url数组
        :type SelfDefiningAssets: list of str
        :param _ScanFrom: 请求发起源，vss表示漏洞扫描服务，云安全中心的用户请填充csip，默认csip
        :type ScanFrom: str
        :param _TaskAdvanceCFG: 高级配置
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :type TaskMode: int
        :param _Tags: 资产标签
        :type Tags: :class:`tencentcloud.csip.v20221121.models.AssetTag`
        :param _FinishWebHook: 任务完成回调webhook地址
        :type FinishWebHook: str
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._MemberId = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._ScanFrom = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._Tags = None
        self._FinishWebHook = None

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
    def ScanAssetType(self):
        r"""0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        r"""扫描项目；port/poc/weakpass/webcontent/configrisk/exposedserver
        :rtype: list of str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        r"""0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :rtype: int
        """
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Assets(self):
        r"""扫描资产信息列表
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        r"""扫描计划详情
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        r"""ip/域名/url数组
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def ScanFrom(self):
        r"""请求发起源，vss表示漏洞扫描服务，云安全中心的用户请填充csip，默认csip
        :rtype: str
        """
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def TaskAdvanceCFG(self):
        r"""高级配置
        :rtype: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        """
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        r"""体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def Tags(self):
        r"""资产标签
        :rtype: :class:`tencentcloud.csip.v20221121.models.AssetTag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FinishWebHook(self):
        r"""任务完成回调webhook地址
        :rtype: str
        """
        return self._FinishWebHook

    @FinishWebHook.setter
    def FinishWebHook(self, FinishWebHook):
        self._FinishWebHook = FinishWebHook


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        self._MemberId = params.get("MemberId")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._ScanFrom = params.get("ScanFrom")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        if params.get("Tags") is not None:
            self._Tags = AssetTag()
            self._Tags._deserialize(params.get("Tags"))
        self._FinishWebHook = params.get("FinishWebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRiskCenterScanTaskResponse(AbstractModel):
    r"""CreateRiskCenterScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Status: 0,任务创建成功；小于0失败；-1为存在资产未认证
        :type Status: int
        :param _UnAuthAsset: 未认证资产列表
        :type UnAuthAsset: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""0,任务创建成功；小于0失败；-1为存在资产未认证
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        r"""未认证资产列表
        :rtype: list of str
        """
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

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
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class CsipRiskCenterStatistics(AbstractModel):
    r"""风险中心风险概览统计数据

    """

    def __init__(self):
        r"""
        :param _PortTotal: 端口风险总数
        :type PortTotal: int
        :param _PortHighLevel: 端口风险高危数量
        :type PortHighLevel: int
        :param _WeakPasswordTotal: 	弱口令风险总数
        :type WeakPasswordTotal: int
        :param _WeakPasswordHighLevel: 弱口令风险高危数量
        :type WeakPasswordHighLevel: int
        :param _WebsiteTotal: 网站风险数量
        :type WebsiteTotal: int
        :param _WebsiteHighLevel: 网站高危风险数量
        :type WebsiteHighLevel: int
        :param _LastScanTime: 最新的扫描时间
        :type LastScanTime: str
        :param _VULTotal: 漏洞风险数
        :type VULTotal: int
        :param _VULHighLevel: 高危漏洞风险数
        :type VULHighLevel: int
        :param _CFGTotal: 配置项风险数量
        :type CFGTotal: int
        :param _CFGHighLevel: 高危配置项风险数量
        :type CFGHighLevel: int
        :param _ServerTotal: 测绘服务风险数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerTotal: int
        :param _ServerHighLevel: 测绘服务高危数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerHighLevel: int
        :param _HostBaseLineRiskTotal: 主机基线风险数量
        :type HostBaseLineRiskTotal: int
        :param _HostBaseLineRiskHighLevel: 主机基线高危风险数量
        :type HostBaseLineRiskHighLevel: int
        :param _PodBaseLineRiskTotal: 容器基线风险数量
        :type PodBaseLineRiskTotal: int
        :param _PodBaseLineRiskHighLevel: 容器基线高危风险数量
        :type PodBaseLineRiskHighLevel: int
        """
        self._PortTotal = None
        self._PortHighLevel = None
        self._WeakPasswordTotal = None
        self._WeakPasswordHighLevel = None
        self._WebsiteTotal = None
        self._WebsiteHighLevel = None
        self._LastScanTime = None
        self._VULTotal = None
        self._VULHighLevel = None
        self._CFGTotal = None
        self._CFGHighLevel = None
        self._ServerTotal = None
        self._ServerHighLevel = None
        self._HostBaseLineRiskTotal = None
        self._HostBaseLineRiskHighLevel = None
        self._PodBaseLineRiskTotal = None
        self._PodBaseLineRiskHighLevel = None

    @property
    def PortTotal(self):
        r"""端口风险总数
        :rtype: int
        """
        return self._PortTotal

    @PortTotal.setter
    def PortTotal(self, PortTotal):
        self._PortTotal = PortTotal

    @property
    def PortHighLevel(self):
        r"""端口风险高危数量
        :rtype: int
        """
        return self._PortHighLevel

    @PortHighLevel.setter
    def PortHighLevel(self, PortHighLevel):
        self._PortHighLevel = PortHighLevel

    @property
    def WeakPasswordTotal(self):
        r"""	弱口令风险总数
        :rtype: int
        """
        return self._WeakPasswordTotal

    @WeakPasswordTotal.setter
    def WeakPasswordTotal(self, WeakPasswordTotal):
        self._WeakPasswordTotal = WeakPasswordTotal

    @property
    def WeakPasswordHighLevel(self):
        r"""弱口令风险高危数量
        :rtype: int
        """
        return self._WeakPasswordHighLevel

    @WeakPasswordHighLevel.setter
    def WeakPasswordHighLevel(self, WeakPasswordHighLevel):
        self._WeakPasswordHighLevel = WeakPasswordHighLevel

    @property
    def WebsiteTotal(self):
        r"""网站风险数量
        :rtype: int
        """
        return self._WebsiteTotal

    @WebsiteTotal.setter
    def WebsiteTotal(self, WebsiteTotal):
        self._WebsiteTotal = WebsiteTotal

    @property
    def WebsiteHighLevel(self):
        r"""网站高危风险数量
        :rtype: int
        """
        return self._WebsiteHighLevel

    @WebsiteHighLevel.setter
    def WebsiteHighLevel(self, WebsiteHighLevel):
        self._WebsiteHighLevel = WebsiteHighLevel

    @property
    def LastScanTime(self):
        r"""最新的扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def VULTotal(self):
        r"""漏洞风险数
        :rtype: int
        """
        return self._VULTotal

    @VULTotal.setter
    def VULTotal(self, VULTotal):
        self._VULTotal = VULTotal

    @property
    def VULHighLevel(self):
        r"""高危漏洞风险数
        :rtype: int
        """
        return self._VULHighLevel

    @VULHighLevel.setter
    def VULHighLevel(self, VULHighLevel):
        self._VULHighLevel = VULHighLevel

    @property
    def CFGTotal(self):
        r"""配置项风险数量
        :rtype: int
        """
        return self._CFGTotal

    @CFGTotal.setter
    def CFGTotal(self, CFGTotal):
        self._CFGTotal = CFGTotal

    @property
    def CFGHighLevel(self):
        r"""高危配置项风险数量
        :rtype: int
        """
        return self._CFGHighLevel

    @CFGHighLevel.setter
    def CFGHighLevel(self, CFGHighLevel):
        self._CFGHighLevel = CFGHighLevel

    @property
    def ServerTotal(self):
        r"""测绘服务风险数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ServerTotal

    @ServerTotal.setter
    def ServerTotal(self, ServerTotal):
        self._ServerTotal = ServerTotal

    @property
    def ServerHighLevel(self):
        r"""测绘服务高危数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ServerHighLevel

    @ServerHighLevel.setter
    def ServerHighLevel(self, ServerHighLevel):
        self._ServerHighLevel = ServerHighLevel

    @property
    def HostBaseLineRiskTotal(self):
        r"""主机基线风险数量
        :rtype: int
        """
        return self._HostBaseLineRiskTotal

    @HostBaseLineRiskTotal.setter
    def HostBaseLineRiskTotal(self, HostBaseLineRiskTotal):
        self._HostBaseLineRiskTotal = HostBaseLineRiskTotal

    @property
    def HostBaseLineRiskHighLevel(self):
        r"""主机基线高危风险数量
        :rtype: int
        """
        return self._HostBaseLineRiskHighLevel

    @HostBaseLineRiskHighLevel.setter
    def HostBaseLineRiskHighLevel(self, HostBaseLineRiskHighLevel):
        self._HostBaseLineRiskHighLevel = HostBaseLineRiskHighLevel

    @property
    def PodBaseLineRiskTotal(self):
        r"""容器基线风险数量
        :rtype: int
        """
        return self._PodBaseLineRiskTotal

    @PodBaseLineRiskTotal.setter
    def PodBaseLineRiskTotal(self, PodBaseLineRiskTotal):
        self._PodBaseLineRiskTotal = PodBaseLineRiskTotal

    @property
    def PodBaseLineRiskHighLevel(self):
        r"""容器基线高危风险数量
        :rtype: int
        """
        return self._PodBaseLineRiskHighLevel

    @PodBaseLineRiskHighLevel.setter
    def PodBaseLineRiskHighLevel(self, PodBaseLineRiskHighLevel):
        self._PodBaseLineRiskHighLevel = PodBaseLineRiskHighLevel


    def _deserialize(self, params):
        self._PortTotal = params.get("PortTotal")
        self._PortHighLevel = params.get("PortHighLevel")
        self._WeakPasswordTotal = params.get("WeakPasswordTotal")
        self._WeakPasswordHighLevel = params.get("WeakPasswordHighLevel")
        self._WebsiteTotal = params.get("WebsiteTotal")
        self._WebsiteHighLevel = params.get("WebsiteHighLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._VULTotal = params.get("VULTotal")
        self._VULHighLevel = params.get("VULHighLevel")
        self._CFGTotal = params.get("CFGTotal")
        self._CFGHighLevel = params.get("CFGHighLevel")
        self._ServerTotal = params.get("ServerTotal")
        self._ServerHighLevel = params.get("ServerHighLevel")
        self._HostBaseLineRiskTotal = params.get("HostBaseLineRiskTotal")
        self._HostBaseLineRiskHighLevel = params.get("HostBaseLineRiskHighLevel")
        self._PodBaseLineRiskTotal = params.get("PodBaseLineRiskTotal")
        self._PodBaseLineRiskHighLevel = params.get("PodBaseLineRiskHighLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBAssetVO(AbstractModel):
    r"""db资产输出字段

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _VpcId: vpcid
        :type VpcId: str
        :param _VpcName: vpc标签
        :type VpcName: str
        :param _Region: 地域
        :type Region: str
        :param _Domain: 域名
        :type Domain: str
        :param _AssetCreateTime: 资产创建时间
        :type AssetCreateTime: str
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _ConfigurationRisk: 配置风险
        :type ConfigurationRisk: int
        :param _Attack: 网络攻击
        :type Attack: int
        :param _Access: 网络访问
        :type Access: int
        :param _ScanTask: 扫描任务
        :type ScanTask: int
        :param _AppId: 用户appid
        :type AppId: int
        :param _Uin: 用户uin
        :type Uin: str
        :param _NickName: 昵称别名
        :type NickName: str
        :param _Port: 端口
        :type Port: int
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _PrivateIp: 内网ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Status: 状态
        :type Status: int
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _IsNewAsset: 是否新资产: 1新
        :type IsNewAsset: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._VpcId = None
        self._VpcName = None
        self._Region = None
        self._Domain = None
        self._AssetCreateTime = None
        self._LastScanTime = None
        self._ConfigurationRisk = None
        self._Attack = None
        self._Access = None
        self._ScanTask = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._Port = None
        self._Tag = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Status = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def VpcId(self):
        r"""vpcid
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc标签
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AssetCreateTime(self):
        r"""资产创建时间
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def LastScanTime(self):
        r"""最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ConfigurationRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def Attack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""网络访问
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def ScanTask(self):
        r"""扫描任务
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def AppId(self):
        r"""用户appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""昵称别名
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

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
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def PrivateIp(self):
        r"""内网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""是否新资产: 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._LastScanTime = params.get("LastScanTime")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._ScanTask = params.get("ScanTask")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._Port = params.get("Port")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Status = params.get("Status")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchBug(AbstractModel):
    r"""漏洞和资产信息

    """

    def __init__(self):
        r"""
        :param _StateCode: 返回查询状态
        :type StateCode: str
        :param _DataBug: 漏洞详情
        :type DataBug: list of BugInfoDetail
        :param _DataAsset: 漏洞影响资产详情
        :type DataAsset: list of AssetInfoDetail
        :param _VSSScan: true支持扫描。false不支持扫描
        :type VSSScan: bool
        :param _CWPScan: 0不支持，1支持
        :type CWPScan: str
        :param _CFWPatch: 1支持虚拟补丁，0或空不支持
        :type CFWPatch: str
        :param _WafPatch: 0不支持，1支持
        :type WafPatch: int
        :param _CWPFix: 0不支持，1支持
        :type CWPFix: int
        :param _DataSupport: 产品支持状态
        :type DataSupport: list of ProductSupport
        :param _CveId: cveId
        :type CveId: str
        """
        self._StateCode = None
        self._DataBug = None
        self._DataAsset = None
        self._VSSScan = None
        self._CWPScan = None
        self._CFWPatch = None
        self._WafPatch = None
        self._CWPFix = None
        self._DataSupport = None
        self._CveId = None

    @property
    def StateCode(self):
        r"""返回查询状态
        :rtype: str
        """
        return self._StateCode

    @StateCode.setter
    def StateCode(self, StateCode):
        self._StateCode = StateCode

    @property
    def DataBug(self):
        r"""漏洞详情
        :rtype: list of BugInfoDetail
        """
        return self._DataBug

    @DataBug.setter
    def DataBug(self, DataBug):
        self._DataBug = DataBug

    @property
    def DataAsset(self):
        r"""漏洞影响资产详情
        :rtype: list of AssetInfoDetail
        """
        return self._DataAsset

    @DataAsset.setter
    def DataAsset(self, DataAsset):
        self._DataAsset = DataAsset

    @property
    def VSSScan(self):
        r"""true支持扫描。false不支持扫描
        :rtype: bool
        """
        return self._VSSScan

    @VSSScan.setter
    def VSSScan(self, VSSScan):
        self._VSSScan = VSSScan

    @property
    def CWPScan(self):
        r"""0不支持，1支持
        :rtype: str
        """
        return self._CWPScan

    @CWPScan.setter
    def CWPScan(self, CWPScan):
        self._CWPScan = CWPScan

    @property
    def CFWPatch(self):
        r"""1支持虚拟补丁，0或空不支持
        :rtype: str
        """
        return self._CFWPatch

    @CFWPatch.setter
    def CFWPatch(self, CFWPatch):
        self._CFWPatch = CFWPatch

    @property
    def WafPatch(self):
        r"""0不支持，1支持
        :rtype: int
        """
        return self._WafPatch

    @WafPatch.setter
    def WafPatch(self, WafPatch):
        self._WafPatch = WafPatch

    @property
    def CWPFix(self):
        r"""0不支持，1支持
        :rtype: int
        """
        return self._CWPFix

    @CWPFix.setter
    def CWPFix(self, CWPFix):
        self._CWPFix = CWPFix

    @property
    def DataSupport(self):
        r"""产品支持状态
        :rtype: list of ProductSupport
        """
        return self._DataSupport

    @DataSupport.setter
    def DataSupport(self, DataSupport):
        self._DataSupport = DataSupport

    @property
    def CveId(self):
        r"""cveId
        :rtype: str
        """
        return self._CveId

    @CveId.setter
    def CveId(self, CveId):
        self._CveId = CveId


    def _deserialize(self, params):
        self._StateCode = params.get("StateCode")
        if params.get("DataBug") is not None:
            self._DataBug = []
            for item in params.get("DataBug"):
                obj = BugInfoDetail()
                obj._deserialize(item)
                self._DataBug.append(obj)
        if params.get("DataAsset") is not None:
            self._DataAsset = []
            for item in params.get("DataAsset"):
                obj = AssetInfoDetail()
                obj._deserialize(item)
                self._DataAsset.append(obj)
        self._VSSScan = params.get("VSSScan")
        self._CWPScan = params.get("CWPScan")
        self._CFWPatch = params.get("CFWPatch")
        self._WafPatch = params.get("WafPatch")
        self._CWPFix = params.get("CWPFix")
        if params.get("DataSupport") is not None:
            self._DataSupport = []
            for item in params.get("DataSupport"):
                obj = ProductSupport()
                obj._deserialize(item)
                self._DataSupport.append(obj)
        self._CveId = params.get("CveId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbAssetInfo(AbstractModel):
    r"""db资产详情

    """

    def __init__(self):
        r"""
        :param _CFWStatus: 云防状态
        :type CFWStatus: int
        :param _AssetId: 资产id
        :type AssetId: str
        :param _VpcName: vpc信息
        :type VpcName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _PrivateIp: 私网ip
        :type PrivateIp: str
        :param _Region: 地域
        :type Region: str
        :param _VpcId: vpc信息
        :type VpcId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _CFWProtectLevel: 云防保护版本
        :type CFWProtectLevel: int
        :param _Tag: tag信息
        :type Tag: list of Tag
        """
        self._CFWStatus = None
        self._AssetId = None
        self._VpcName = None
        self._AssetType = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._VpcId = None
        self._AssetName = None
        self._CFWProtectLevel = None
        self._Tag = None

    @property
    def CFWStatus(self):
        r"""云防状态
        :rtype: int
        """
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def VpcName(self):
        r"""vpc信息
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""私网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""vpc信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CFWProtectLevel(self):
        r"""云防保护版本
        :rtype: int
        """
        return self._CFWProtectLevel

    @CFWProtectLevel.setter
    def CFWProtectLevel(self, CFWProtectLevel):
        self._CFWProtectLevel = CFWProtectLevel

    @property
    def Tag(self):
        r"""tag信息
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._CFWStatus = params.get("CFWStatus")
        self._AssetId = params.get("AssetId")
        self._VpcName = params.get("VpcName")
        self._AssetType = params.get("AssetType")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._AssetName = params.get("AssetName")
        self._CFWProtectLevel = params.get("CFWProtectLevel")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpRequest(AbstractModel):
    r"""DeleteDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Content: 资产
        :type Content: list of PublicIpDomainListKey
        :param _RetainPath: 是否保留路径配置，1：保留，其他：不保留，默认不传为不保留
        :type RetainPath: int
        :param _IgnoreAsset: 以后是否忽略该资产，，1：忽略，其他：不忽略，默认不传为忽略
        :type IgnoreAsset: int
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        :param _Type: 删除类型，取值： ALL， 删除全部，将直接忽略Content的内容；                                           其他值 ,非全部，则Centent必填，  默认为其他值。
        :type Type: str
        """
        self._MemberId = None
        self._Content = None
        self._RetainPath = None
        self._IgnoreAsset = None
        self._Tags = None
        self._Type = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Content(self):
        r"""资产
        :rtype: list of PublicIpDomainListKey
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RetainPath(self):
        r"""是否保留路径配置，1：保留，其他：不保留，默认不传为不保留
        :rtype: int
        """
        return self._RetainPath

    @RetainPath.setter
    def RetainPath(self, RetainPath):
        self._RetainPath = RetainPath

    @property
    def IgnoreAsset(self):
        r"""以后是否忽略该资产，，1：忽略，其他：不忽略，默认不传为忽略
        :rtype: int
        """
        return self._IgnoreAsset

    @IgnoreAsset.setter
    def IgnoreAsset(self, IgnoreAsset):
        self._IgnoreAsset = IgnoreAsset

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        r"""删除类型，取值： ALL， 删除全部，将直接忽略Content的内容；                                           其他值 ,非全部，则Centent必填，  默认为其他值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = PublicIpDomainListKey()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RetainPath = params.get("RetainPath")
        self._IgnoreAsset = params.get("IgnoreAsset")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpResponse(AbstractModel):
    r"""DeleteDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除的资产数量
        :type Data: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""删除的资产数量
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DeleteRiskScanTaskRequest(AbstractModel):
    r"""DeleteRiskScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id 和目标AppID列表
        :type TaskIdList: list of TaskIdListKey
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._TaskIdList = None
        self._MemberId = None

    @property
    def TaskIdList(self):
        r"""任务id 和目标AppID列表
        :rtype: list of TaskIdListKey
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRiskScanTaskResponse(AbstractModel):
    r"""DeleteRiskScanTask返回参数结构体

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


class DescribeAbnormalCallRecordRequest(AbstractModel):
    r"""DescribeAbnormalCallRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmRuleID: 告警规则ID
        :type AlarmRuleID: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AccessKey: 访问密钥
        :type AccessKey: str
        :param _SourceIP: 调用源IP
        :type SourceIP: str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._AlarmRuleID = None
        self._MemberId = None
        self._AccessKey = None
        self._SourceIP = None
        self._Filter = None

    @property
    def AlarmRuleID(self):
        r"""告警规则ID
        :rtype: int
        """
        return self._AlarmRuleID

    @AlarmRuleID.setter
    def AlarmRuleID(self, AlarmRuleID):
        self._AlarmRuleID = AlarmRuleID

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKey(self):
        r"""访问密钥
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SourceIP(self):
        r"""调用源IP
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._AlarmRuleID = params.get("AlarmRuleID")
        self._MemberId = params.get("MemberId")
        self._AccessKey = params.get("AccessKey")
        self._SourceIP = params.get("SourceIP")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalCallRecordResponse(AbstractModel):
    r"""DescribeAbnormalCallRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 调用记录列表
        :type Data: list of CallRecord
        :param _Total: 调用记录总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""调用记录列表
        :rtype: list of CallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""调用记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAlarmDetailRequest(AbstractModel):
    r"""DescribeAccessKeyAlarmDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 告警记录ID
        :type ID: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._ID = None
        self._MemberId = None

    @property
    def ID(self):
        r"""告警记录ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAlarmDetailResponse(AbstractModel):
    r"""DescribeAccessKeyAlarmDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmInfo: 告警信息
        :type AlarmInfo: :class:`tencentcloud.csip.v20221121.models.AccessKeyAlarm`
        :param _CamCount: 所属账号CAM策略数量
        :type CamCount: int
        :param _RiskCount: AK风险数量
        :type RiskCount: int
        :param _AlarmDesc: 告警策略描述
        :type AlarmDesc: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmInfo = None
        self._CamCount = None
        self._RiskCount = None
        self._AlarmDesc = None
        self._RequestId = None

    @property
    def AlarmInfo(self):
        r"""告警信息
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyAlarm`
        """
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def CamCount(self):
        r"""所属账号CAM策略数量
        :rtype: int
        """
        return self._CamCount

    @CamCount.setter
    def CamCount(self, CamCount):
        self._CamCount = CamCount

    @property
    def RiskCount(self):
        r"""AK风险数量
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AlarmDesc(self):
        r"""告警策略描述
        :rtype: str
        """
        return self._AlarmDesc

    @AlarmDesc.setter
    def AlarmDesc(self, AlarmDesc):
        self._AlarmDesc = AlarmDesc

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
        if params.get("AlarmInfo") is not None:
            self._AlarmInfo = AccessKeyAlarm()
            self._AlarmInfo._deserialize(params.get("AlarmInfo"))
        self._CamCount = params.get("CamCount")
        self._RiskCount = params.get("RiskCount")
        self._AlarmDesc = params.get("AlarmDesc")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAlarmRequest(AbstractModel):
    r"""DescribeAccessKeyAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AccessKeyID: 访问密钥的ID
        :type AccessKeyID: int
        :param _SourceIPID: 源IP的ID
        :type SourceIPID: int
        :param _SubUin: 账号uin
        :type SubUin: str
        """
        self._Filter = None
        self._MemberId = None
        self._AccessKeyID = None
        self._SourceIPID = None
        self._SubUin = None

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""访问密钥的ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIPID(self):
        r"""源IP的ID
        :rtype: int
        """
        return self._SourceIPID

    @SourceIPID.setter
    def SourceIPID(self, SourceIPID):
        self._SourceIPID = SourceIPID

    @property
    def SubUin(self):
        r"""账号uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIPID = params.get("SourceIPID")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAlarmResponse(AbstractModel):
    r"""DescribeAccessKeyAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警列表
        :type Data: list of AccessKeyAlarm
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""告警列表
        :rtype: list of AccessKeyAlarm
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyAlarm()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAssetRequest(AbstractModel):
    r"""DescribeAccessKeyAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAssetResponse(AbstractModel):
    r"""DescribeAccessKeyAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问密钥资产列表
        :type Data: list of AccessKeyAsset
        :param _Total: 全部数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""访问密钥资产列表
        :rtype: list of AccessKeyAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""全部数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyRiskDetailRequest(AbstractModel):
    r"""DescribeAccessKeyRiskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 风险记录ID
        :type ID: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._ID = None
        self._MemberId = None

    @property
    def ID(self):
        r"""风险记录ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyRiskDetailResponse(AbstractModel):
    r"""DescribeAccessKeyRiskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskInfo: 风险列表
        :type RiskInfo: :class:`tencentcloud.csip.v20221121.models.AccessKeyRisk`
        :param _CamCount: CAM策略总数
        :type CamCount: int
        :param _AlarmCount: 账号关联告警数量
        :type AlarmCount: int
        :param _AccessType: 访问方式 0 API 1 控制台与API
        :type AccessType: int
        :param _AccessKeyAlarmCount: 访问密钥告警数量列表
        :type AccessKeyAlarmCount: list of AccessKeyAlarmCount
        :param _ActionFlag: 操作保护是否开启 0 未开启 1 已开启
        :type ActionFlag: int
        :param _LoginFlag: 登录保护是否开启 0 未开启 1 已开启
        :type LoginFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskInfo = None
        self._CamCount = None
        self._AlarmCount = None
        self._AccessType = None
        self._AccessKeyAlarmCount = None
        self._ActionFlag = None
        self._LoginFlag = None
        self._RequestId = None

    @property
    def RiskInfo(self):
        r"""风险列表
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyRisk`
        """
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def CamCount(self):
        r"""CAM策略总数
        :rtype: int
        """
        return self._CamCount

    @CamCount.setter
    def CamCount(self, CamCount):
        self._CamCount = CamCount

    @property
    def AlarmCount(self):
        r"""账号关联告警数量
        :rtype: int
        """
        return self._AlarmCount

    @AlarmCount.setter
    def AlarmCount(self, AlarmCount):
        self._AlarmCount = AlarmCount

    @property
    def AccessType(self):
        r"""访问方式 0 API 1 控制台与API
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AccessKeyAlarmCount(self):
        r"""访问密钥告警数量列表
        :rtype: list of AccessKeyAlarmCount
        """
        return self._AccessKeyAlarmCount

    @AccessKeyAlarmCount.setter
    def AccessKeyAlarmCount(self, AccessKeyAlarmCount):
        self._AccessKeyAlarmCount = AccessKeyAlarmCount

    @property
    def ActionFlag(self):
        r"""操作保护是否开启 0 未开启 1 已开启
        :rtype: int
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def LoginFlag(self):
        r"""登录保护是否开启 0 未开启 1 已开启
        :rtype: int
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

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
        if params.get("RiskInfo") is not None:
            self._RiskInfo = AccessKeyRisk()
            self._RiskInfo._deserialize(params.get("RiskInfo"))
        self._CamCount = params.get("CamCount")
        self._AlarmCount = params.get("AlarmCount")
        self._AccessType = params.get("AccessType")
        if params.get("AccessKeyAlarmCount") is not None:
            self._AccessKeyAlarmCount = []
            for item in params.get("AccessKeyAlarmCount"):
                obj = AccessKeyAlarmCount()
                obj._deserialize(item)
                self._AccessKeyAlarmCount.append(obj)
        self._ActionFlag = params.get("ActionFlag")
        self._LoginFlag = params.get("LoginFlag")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyRiskRequest(AbstractModel):
    r"""DescribeAccessKeyRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AccessKeyID: 访问密钥的ID
        :type AccessKeyID: int
        :param _SubUin: 账号uin
        :type SubUin: str
        """
        self._Filter = None
        self._MemberId = None
        self._AccessKeyID = None
        self._SubUin = None

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""访问密钥的ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SubUin(self):
        r"""账号uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyRiskResponse(AbstractModel):
    r"""DescribeAccessKeyRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 风险列表
        :type Data: list of AccessKeyRisk
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""风险列表
        :rtype: list of AccessKeyRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyUserDetailRequest(AbstractModel):
    r"""DescribeAccessKeyUserDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubUin: 账号自身uin
        :type SubUin: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._SubUin = None
        self._MemberId = None

    @property
    def SubUin(self):
        r"""账号自身uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyUserDetailResponse(AbstractModel):
    r"""DescribeAccessKeyUserDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _User: 账号详情信息
        :type User: :class:`tencentcloud.csip.v20221121.models.AccessKeyUser`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""账号详情信息
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyUser`
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
            self._User = AccessKeyUser()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyUserListRequest(AbstractModel):
    r"""DescribeAccessKeyUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyUserListResponse(AbstractModel):
    r"""DescribeAccessKeyUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号列表
        :type Data: list of AccessKeyUser
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""账号列表
        :rtype: list of AccessKeyUser
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyUser()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAlertListRequest(AbstractModel):
    r"""DescribeAlertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 标签搜索筛选
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        :param _AssetType: 0:默认全部 1:资产ID 2:域名
        :type AssetType: int
        """
        self._Filter = None
        self._MemberId = None
        self._OperatedMemberId = None
        self._AssetType = None

    @property
    def Filter(self):
        r"""标签搜索筛选
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def OperatedMemberId(self):
        r"""被调用的集团账号的成员id
        :rtype: list of str
        """
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId

    @property
    def AssetType(self):
        r"""0:默认全部 1:资产ID 2:域名
        :rtype: int
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._OperatedMemberId = params.get("OperatedMemberId")
        self._AssetType = params.get("AssetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertListResponse(AbstractModel):
    r"""DescribeAlertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertList: 全量告警列表
        :type AlertList: list of AlertInfo
        :param _AlertTypeCount: 告警大类数量
        :type AlertTypeCount: list of TagCount
        :param _TotalCount: 告警总数
        :type TotalCount: int
        :param _ReturnCode: 0：succeed 1：timeout
        :type ReturnCode: int
        :param _ReturnMsg: 返回状态信息
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertList = None
        self._AlertTypeCount = None
        self._TotalCount = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def AlertList(self):
        r"""全量告警列表
        :rtype: list of AlertInfo
        """
        return self._AlertList

    @AlertList.setter
    def AlertList(self, AlertList):
        self._AlertList = AlertList

    @property
    def AlertTypeCount(self):
        r"""告警大类数量
        :rtype: list of TagCount
        """
        return self._AlertTypeCount

    @AlertTypeCount.setter
    def AlertTypeCount(self, AlertTypeCount):
        self._AlertTypeCount = AlertTypeCount

    @property
    def TotalCount(self):
        r"""告警总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReturnCode(self):
        r"""0：succeed 1：timeout
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        r"""返回状态信息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        if params.get("AlertList") is not None:
            self._AlertList = []
            for item in params.get("AlertList"):
                obj = AlertInfo()
                obj._deserialize(item)
                self._AlertList.append(obj)
        if params.get("AlertTypeCount") is not None:
            self._AlertTypeCount = []
            for item in params.get("AlertTypeCount"):
                obj = TagCount()
                obj._deserialize(item)
                self._AlertTypeCount.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeAssetProcessListRequest(AbstractModel):
    r"""DescribeAssetProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _Provider: 云厂商
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetProcessListResponse(AbstractModel):
    r"""DescribeAssetProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 进程数量
        :type TotalCount: int
        :param _AssetProcessList: 进程列表
        :type AssetProcessList: list of AssetProcessItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AssetProcessList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""进程数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AssetProcessList(self):
        r"""进程列表
        :rtype: list of AssetProcessItem
        """
        return self._AssetProcessList

    @AssetProcessList.setter
    def AssetProcessList(self, AssetProcessList):
        self._AssetProcessList = AssetProcessList

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
        if params.get("AssetProcessList") is not None:
            self._AssetProcessList = []
            for item in params.get("AssetProcessList"):
                obj = AssetProcessItem()
                obj._deserialize(item)
                self._AssetProcessList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetRiskListRequest(AbstractModel):
    r"""DescribeAssetRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetRiskListResponse(AbstractModel):
    r"""DescribeAssetRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资产视角下风险数量
        :type TotalCount: int
        :param _AssetRiskList: 资产视角下风险列表
        :type AssetRiskList: list of AssetRiskItem
        :param _StandardNameList: 等保规范名称集合
        :type StandardNameList: list of StandardItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AssetRiskList = None
        self._StandardNameList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""资产视角下风险数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AssetRiskList(self):
        r"""资产视角下风险列表
        :rtype: list of AssetRiskItem
        """
        return self._AssetRiskList

    @AssetRiskList.setter
    def AssetRiskList(self, AssetRiskList):
        self._AssetRiskList = AssetRiskList

    @property
    def StandardNameList(self):
        r"""等保规范名称集合
        :rtype: list of StandardItem
        """
        return self._StandardNameList

    @StandardNameList.setter
    def StandardNameList(self, StandardNameList):
        self._StandardNameList = StandardNameList

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
        if params.get("AssetRiskList") is not None:
            self._AssetRiskList = []
            for item in params.get("AssetRiskList"):
                obj = AssetRiskItem()
                obj._deserialize(item)
                self._AssetRiskList.append(obj)
        if params.get("StandardNameList") is not None:
            self._StandardNameList = []
            for item in params.get("StandardNameList"):
                obj = StandardItem()
                obj._deserialize(item)
                self._StandardNameList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetViewVulRiskListRequest(AbstractModel):
    r"""DescribeAssetViewVulRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetViewVulRiskListResponse(AbstractModel):
    r"""DescribeAssetViewVulRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的漏洞风险列表
        :type Data: list of AssetViewVULRiskData
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _Tags: tag枚举
        :type Tags: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""资产视角的漏洞风险列表
        :rtype: list of AssetViewVULRiskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""漏洞类型列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def Tags(self):
        r"""tag枚举
        :rtype: list of FilterDataObject
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRiskData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCFWAssetStatisticsRequest(AbstractModel):
    r"""DescribeCFWAssetStatistics请求参数结构体

    """


class DescribeCFWAssetStatisticsResponse(AbstractModel):
    r"""DescribeCFWAssetStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkTotal: 网络资产总数
        :type NetworkTotal: int
        :param _ClbTotal: 资产clb数量
        :type ClbTotal: int
        :param _NatTotal: nat数量
        :type NatTotal: int
        :param _PublicAssetTotal: 公网ip数量
        :type PublicAssetTotal: int
        :param _CVMAssetTotal: 主机数量
        :type CVMAssetTotal: int
        :param _CFGTotal: 配置风险
        :type CFGTotal: int
        :param _PortTotal: 端口风险
        :type PortTotal: int
        :param _WebsiteTotal: 内容风险
        :type WebsiteTotal: int
        :param _ServerTotal: 风险服务暴露
        :type ServerTotal: int
        :param _WeakPasswordTotal: 弱口令风险
        :type WeakPasswordTotal: int
        :param _VULTotal: 漏洞风险
        :type VULTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkTotal = None
        self._ClbTotal = None
        self._NatTotal = None
        self._PublicAssetTotal = None
        self._CVMAssetTotal = None
        self._CFGTotal = None
        self._PortTotal = None
        self._WebsiteTotal = None
        self._ServerTotal = None
        self._WeakPasswordTotal = None
        self._VULTotal = None
        self._RequestId = None

    @property
    def NetworkTotal(self):
        r"""网络资产总数
        :rtype: int
        """
        return self._NetworkTotal

    @NetworkTotal.setter
    def NetworkTotal(self, NetworkTotal):
        self._NetworkTotal = NetworkTotal

    @property
    def ClbTotal(self):
        r"""资产clb数量
        :rtype: int
        """
        return self._ClbTotal

    @ClbTotal.setter
    def ClbTotal(self, ClbTotal):
        self._ClbTotal = ClbTotal

    @property
    def NatTotal(self):
        r"""nat数量
        :rtype: int
        """
        return self._NatTotal

    @NatTotal.setter
    def NatTotal(self, NatTotal):
        self._NatTotal = NatTotal

    @property
    def PublicAssetTotal(self):
        r"""公网ip数量
        :rtype: int
        """
        return self._PublicAssetTotal

    @PublicAssetTotal.setter
    def PublicAssetTotal(self, PublicAssetTotal):
        self._PublicAssetTotal = PublicAssetTotal

    @property
    def CVMAssetTotal(self):
        r"""主机数量
        :rtype: int
        """
        return self._CVMAssetTotal

    @CVMAssetTotal.setter
    def CVMAssetTotal(self, CVMAssetTotal):
        self._CVMAssetTotal = CVMAssetTotal

    @property
    def CFGTotal(self):
        r"""配置风险
        :rtype: int
        """
        return self._CFGTotal

    @CFGTotal.setter
    def CFGTotal(self, CFGTotal):
        self._CFGTotal = CFGTotal

    @property
    def PortTotal(self):
        r"""端口风险
        :rtype: int
        """
        return self._PortTotal

    @PortTotal.setter
    def PortTotal(self, PortTotal):
        self._PortTotal = PortTotal

    @property
    def WebsiteTotal(self):
        r"""内容风险
        :rtype: int
        """
        return self._WebsiteTotal

    @WebsiteTotal.setter
    def WebsiteTotal(self, WebsiteTotal):
        self._WebsiteTotal = WebsiteTotal

    @property
    def ServerTotal(self):
        r"""风险服务暴露
        :rtype: int
        """
        return self._ServerTotal

    @ServerTotal.setter
    def ServerTotal(self, ServerTotal):
        self._ServerTotal = ServerTotal

    @property
    def WeakPasswordTotal(self):
        r"""弱口令风险
        :rtype: int
        """
        return self._WeakPasswordTotal

    @WeakPasswordTotal.setter
    def WeakPasswordTotal(self, WeakPasswordTotal):
        self._WeakPasswordTotal = WeakPasswordTotal

    @property
    def VULTotal(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VULTotal

    @VULTotal.setter
    def VULTotal(self, VULTotal):
        self._VULTotal = VULTotal

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
        self._NetworkTotal = params.get("NetworkTotal")
        self._ClbTotal = params.get("ClbTotal")
        self._NatTotal = params.get("NatTotal")
        self._PublicAssetTotal = params.get("PublicAssetTotal")
        self._CVMAssetTotal = params.get("CVMAssetTotal")
        self._CFGTotal = params.get("CFGTotal")
        self._PortTotal = params.get("PortTotal")
        self._WebsiteTotal = params.get("WebsiteTotal")
        self._ServerTotal = params.get("ServerTotal")
        self._WeakPasswordTotal = params.get("WeakPasswordTotal")
        self._VULTotal = params.get("VULTotal")
        self._RequestId = params.get("RequestId")


class DescribeCSIPRiskStatisticsRequest(AbstractModel):
    r"""DescribeCSIPRiskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCSIPRiskStatisticsResponse(AbstractModel):
    r"""DescribeCSIPRiskStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 资产概况数据
        :type Data: :class:`tencentcloud.csip.v20221121.models.CsipRiskCenterStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""资产概况数据
        :rtype: :class:`tencentcloud.csip.v20221121.models.CsipRiskCenterStatistics`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CsipRiskCenterStatistics()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetInfoRequest(AbstractModel):
    r"""DescribeCVMAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoResponse(AbstractModel):
    r"""DescribeCVMAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据
        :type Data: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据
        :rtype: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AssetBaseInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetsRequest(AbstractModel):
    r"""DescribeCVMAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetsResponse(AbstractModel):
    r"""DescribeCVMAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 机器列表
        :type Data: list of CVMAssetVO
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护状态
        :type DefenseStatusList: list of FilterDataObject
        :param _VpcList: vpc枚举
        :type VpcList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
        :type AssetTypeList: list of FilterDataObject
        :param _SystemTypeList: 操作系统枚举
        :type SystemTypeList: list of FilterDataObject
        :param _IpTypeList: ip列表
        :type IpTypeList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
        :type ZoneList: list of FilterDataObject
        :param _OsList: os列表
        :type OsList: list of FilterDataObject
        :param _AssetMapInstanceTypeList: 资产类型和实例类型的对应关系
        :type AssetMapInstanceTypeList: list of AssetInstanceTypeMap
        :param _PublicPrivateAttr: 公网内网枚举
        :type PublicPrivateAttr: list of FilterDataObject
        :param _ProtectStatusList: 主机防护状态
        :type ProtectStatusList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._VpcList = None
        self._AssetTypeList = None
        self._SystemTypeList = None
        self._IpTypeList = None
        self._AppIdList = None
        self._ZoneList = None
        self._OsList = None
        self._AssetMapInstanceTypeList = None
        self._PublicPrivateAttr = None
        self._ProtectStatusList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""机器列表
        :rtype: list of CVMAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        r"""防护状态
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def VpcList(self):
        r"""vpc枚举
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AssetTypeList(self):
        r"""资产类型枚举
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def SystemTypeList(self):
        r"""操作系统枚举
        :rtype: list of FilterDataObject
        """
        return self._SystemTypeList

    @SystemTypeList.setter
    def SystemTypeList(self, SystemTypeList):
        self._SystemTypeList = SystemTypeList

    @property
    def IpTypeList(self):
        r"""ip列表
        :rtype: list of FilterDataObject
        """
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def AppIdList(self):
        r"""appid列表
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        r"""可用区列表
        :rtype: list of FilterDataObject
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def OsList(self):
        r"""os列表
        :rtype: list of FilterDataObject
        """
        return self._OsList

    @OsList.setter
    def OsList(self, OsList):
        self._OsList = OsList

    @property
    def AssetMapInstanceTypeList(self):
        r"""资产类型和实例类型的对应关系
        :rtype: list of AssetInstanceTypeMap
        """
        return self._AssetMapInstanceTypeList

    @AssetMapInstanceTypeList.setter
    def AssetMapInstanceTypeList(self, AssetMapInstanceTypeList):
        self._AssetMapInstanceTypeList = AssetMapInstanceTypeList

    @property
    def PublicPrivateAttr(self):
        r"""公网内网枚举
        :rtype: list of FilterDataObject
        """
        return self._PublicPrivateAttr

    @PublicPrivateAttr.setter
    def PublicPrivateAttr(self, PublicPrivateAttr):
        self._PublicPrivateAttr = PublicPrivateAttr

    @property
    def ProtectStatusList(self):
        r"""主机防护状态
        :rtype: list of FilterDataObject
        """
        return self._ProtectStatusList

    @ProtectStatusList.setter
    def ProtectStatusList(self, ProtectStatusList):
        self._ProtectStatusList = ProtectStatusList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CVMAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("SystemTypeList") is not None:
            self._SystemTypeList = []
            for item in params.get("SystemTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SystemTypeList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("OsList") is not None:
            self._OsList = []
            for item in params.get("OsList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OsList.append(obj)
        if params.get("AssetMapInstanceTypeList") is not None:
            self._AssetMapInstanceTypeList = []
            for item in params.get("AssetMapInstanceTypeList"):
                obj = AssetInstanceTypeMap()
                obj._deserialize(item)
                self._AssetMapInstanceTypeList.append(obj)
        if params.get("PublicPrivateAttr") is not None:
            self._PublicPrivateAttr = []
            for item in params.get("PublicPrivateAttr"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PublicPrivateAttr.append(obj)
        if params.get("ProtectStatusList") is not None:
            self._ProtectStatusList = []
            for item in params.get("ProtectStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProtectStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallRecordRequest(AbstractModel):
    r"""DescribeCallRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AccessKeyID: 访问密钥的ID
        :type AccessKeyID: int
        :param _SourceIPID: 调用源IP的ID
        :type SourceIPID: int
        :param _AccUin: 访问账号uin
        :type AccUin: str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._AccessKeyID = None
        self._SourceIPID = None
        self._AccUin = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""访问密钥的ID
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIPID(self):
        r"""调用源IP的ID
        :rtype: int
        """
        return self._SourceIPID

    @SourceIPID.setter
    def SourceIPID(self, SourceIPID):
        self._SourceIPID = SourceIPID

    @property
    def AccUin(self):
        r"""访问账号uin
        :rtype: str
        """
        return self._AccUin

    @AccUin.setter
    def AccUin(self, AccUin):
        self._AccUin = AccUin

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIPID = params.get("SourceIPID")
        self._AccUin = params.get("AccUin")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallRecordResponse(AbstractModel):
    r"""DescribeCallRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 调用记录列表
        :type Data: list of CallRecord
        :param _Total: 调用记录总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""调用记录列表
        :rtype: list of CallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""调用记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCheckViewRisksRequest(AbstractModel):
    r"""DescribeCheckViewRisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckViewRisksResponse(AbstractModel):
    r"""DescribeCheckViewRisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 检查视角下风险数量
        :type TotalCount: int
        :param _CheckViewRiskList: 检查视角下风险列表
        :type CheckViewRiskList: list of CheckViewRiskItem
        :param _StandardNameList: 检查视角下cspm规范标签列表
        :type StandardNameList: list of StandardItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CheckViewRiskList = None
        self._StandardNameList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""检查视角下风险数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CheckViewRiskList(self):
        r"""检查视角下风险列表
        :rtype: list of CheckViewRiskItem
        """
        return self._CheckViewRiskList

    @CheckViewRiskList.setter
    def CheckViewRiskList(self, CheckViewRiskList):
        self._CheckViewRiskList = CheckViewRiskList

    @property
    def StandardNameList(self):
        r"""检查视角下cspm规范标签列表
        :rtype: list of StandardItem
        """
        return self._StandardNameList

    @StandardNameList.setter
    def StandardNameList(self, StandardNameList):
        self._StandardNameList = StandardNameList

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
        if params.get("CheckViewRiskList") is not None:
            self._CheckViewRiskList = []
            for item in params.get("CheckViewRiskList"):
                obj = CheckViewRiskItem()
                obj._deserialize(item)
                self._CheckViewRiskList.append(obj)
        if params.get("StandardNameList") is not None:
            self._StandardNameList = []
            for item in params.get("StandardNameList"):
                obj = StandardItem()
                obj._deserialize(item)
                self._StandardNameList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterAssetsRequest(AbstractModel):
    r"""DescribeClusterAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAssetsResponse(AbstractModel):
    r"""DescribeClusterAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of AssetCluster
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _ClusterTypeList: 集群类型枚举
        :type ClusterTypeList: list of FilterDataObject
        :param _ClusterStatusList: 集群状态枚举
        :type ClusterStatusList: list of FilterDataObject
        :param _ComponentStatusList: 组件状态枚举
        :type ComponentStatusList: list of FilterDataObject
        :param _VpcList: 私有网络枚举
        :type VpcList: list of FilterDataObject
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AppIdList: 租户枚举
        :type AppIdList: list of FilterDataObject
        :param _ProtectStatusList: 集群防护状态枚举
        :type ProtectStatusList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._ClusterTypeList = None
        self._ClusterStatusList = None
        self._ComponentStatusList = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._ProtectStatusList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of AssetCluster
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def ClusterTypeList(self):
        r"""集群类型枚举
        :rtype: list of FilterDataObject
        """
        return self._ClusterTypeList

    @ClusterTypeList.setter
    def ClusterTypeList(self, ClusterTypeList):
        self._ClusterTypeList = ClusterTypeList

    @property
    def ClusterStatusList(self):
        r"""集群状态枚举
        :rtype: list of FilterDataObject
        """
        return self._ClusterStatusList

    @ClusterStatusList.setter
    def ClusterStatusList(self, ClusterStatusList):
        self._ClusterStatusList = ClusterStatusList

    @property
    def ComponentStatusList(self):
        r"""组件状态枚举
        :rtype: list of FilterDataObject
        """
        return self._ComponentStatusList

    @ComponentStatusList.setter
    def ComponentStatusList(self, ComponentStatusList):
        self._ComponentStatusList = ComponentStatusList

    @property
    def VpcList(self):
        r"""私有网络枚举
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        r"""地域枚举
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""租户枚举
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ProtectStatusList(self):
        r"""集群防护状态枚举
        :rtype: list of FilterDataObject
        """
        return self._ProtectStatusList

    @ProtectStatusList.setter
    def ProtectStatusList(self, ProtectStatusList):
        self._ProtectStatusList = ProtectStatusList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetCluster()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterTypeList") is not None:
            self._ClusterTypeList = []
            for item in params.get("ClusterTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ClusterTypeList.append(obj)
        if params.get("ClusterStatusList") is not None:
            self._ClusterStatusList = []
            for item in params.get("ClusterStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ClusterStatusList.append(obj)
        if params.get("ComponentStatusList") is not None:
            self._ComponentStatusList = []
            for item in params.get("ComponentStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ComponentStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ProtectStatusList") is not None:
            self._ProtectStatusList = []
            for item in params.get("ProtectStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProtectStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPodAssetsRequest(AbstractModel):
    r"""DescribeClusterPodAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPodAssetsResponse(AbstractModel):
    r"""DescribeClusterPodAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of AssetClusterPod
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PodStatusList: 集群pod状态枚举
        :type PodStatusList: list of FilterDataObject
        :param _NamespaceList: 命名空间枚举
        :type NamespaceList: list of FilterDataObject
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AppIdList: 租户枚举
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._PodStatusList = None
        self._NamespaceList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of AssetClusterPod
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def PodStatusList(self):
        r"""集群pod状态枚举
        :rtype: list of FilterDataObject
        """
        return self._PodStatusList

    @PodStatusList.setter
    def PodStatusList(self, PodStatusList):
        self._PodStatusList = PodStatusList

    @property
    def NamespaceList(self):
        r"""命名空间枚举
        :rtype: list of FilterDataObject
        """
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def RegionList(self):
        r"""地域枚举
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""租户枚举
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetClusterPod()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("PodStatusList") is not None:
            self._PodStatusList = []
            for item in params.get("PodStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PodStatusList.append(obj)
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigCheckRulesRequest(AbstractModel):
    r"""DescribeConfigCheckRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigCheckRulesResponse(AbstractModel):
    r"""DescribeConfigCheckRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 风险规则数量
        :type TotalCount: int
        :param _RuleList: 风险规则列表
        :type RuleList: list of RiskRuleInfo
        :param _ProviderList: 云厂商类型选项
        :type ProviderList: list of AttributeOptionSet
        :param _RiskLevelList: 风险等级类型选项
        :type RiskLevelList: list of AttributeOptionSet
        :param _DispositionTypeList: 处置分类选项
        :type DispositionTypeList: list of AttributeOptionSet
        :param _CheckTypeList: 检查类型选项
        :type CheckTypeList: list of AttributeOptionSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RuleList = None
        self._ProviderList = None
        self._RiskLevelList = None
        self._DispositionTypeList = None
        self._CheckTypeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""风险规则数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RuleList(self):
        r"""风险规则列表
        :rtype: list of RiskRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def ProviderList(self):
        r"""云厂商类型选项
        :rtype: list of AttributeOptionSet
        """
        return self._ProviderList

    @ProviderList.setter
    def ProviderList(self, ProviderList):
        self._ProviderList = ProviderList

    @property
    def RiskLevelList(self):
        r"""风险等级类型选项
        :rtype: list of AttributeOptionSet
        """
        return self._RiskLevelList

    @RiskLevelList.setter
    def RiskLevelList(self, RiskLevelList):
        self._RiskLevelList = RiskLevelList

    @property
    def DispositionTypeList(self):
        r"""处置分类选项
        :rtype: list of AttributeOptionSet
        """
        return self._DispositionTypeList

    @DispositionTypeList.setter
    def DispositionTypeList(self, DispositionTypeList):
        self._DispositionTypeList = DispositionTypeList

    @property
    def CheckTypeList(self):
        r"""检查类型选项
        :rtype: list of AttributeOptionSet
        """
        return self._CheckTypeList

    @CheckTypeList.setter
    def CheckTypeList(self, CheckTypeList):
        self._CheckTypeList = CheckTypeList

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
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = RiskRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        if params.get("ProviderList") is not None:
            self._ProviderList = []
            for item in params.get("ProviderList"):
                obj = AttributeOptionSet()
                obj._deserialize(item)
                self._ProviderList.append(obj)
        if params.get("RiskLevelList") is not None:
            self._RiskLevelList = []
            for item in params.get("RiskLevelList"):
                obj = AttributeOptionSet()
                obj._deserialize(item)
                self._RiskLevelList.append(obj)
        if params.get("DispositionTypeList") is not None:
            self._DispositionTypeList = []
            for item in params.get("DispositionTypeList"):
                obj = AttributeOptionSet()
                obj._deserialize(item)
                self._DispositionTypeList.append(obj)
        if params.get("CheckTypeList") is not None:
            self._CheckTypeList = []
            for item in params.get("CheckTypeList"):
                obj = AttributeOptionSet()
                obj._deserialize(item)
                self._CheckTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbAssetInfoRequest(AbstractModel):
    r"""DescribeDbAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetInfoResponse(AbstractModel):
    r"""DescribeDbAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: db资产详情
        :type Data: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""db资产详情
        :rtype: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DbAssetInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDbAssetsRequest(AbstractModel):
    r"""DescribeDbAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _AssetTypes: 资产类型:MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :type AssetTypes: list of str
        """
        self._MemberId = None
        self._Filter = None
        self._AssetTypes = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AssetTypes(self):
        r"""资产类型:MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :rtype: list of str
        """
        return self._AssetTypes

    @AssetTypes.setter
    def AssetTypes(self, AssetTypes):
        self._AssetTypes = AssetTypes


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._AssetTypes = params.get("AssetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetsResponse(AbstractModel):
    r"""DescribeDbAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 资产总数
        :type Data: list of DBAssetVO
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: Vpc枚举
        :type VpcList: list of FilterDataObject
        :param _AppIdList: Appid枚举
        :type AppIdList: list of FilterDataObject
        :param _PublicPrivateAttr: 公网内网枚举
        :type PublicPrivateAttr: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._PublicPrivateAttr = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""资产总数
        :rtype: list of DBAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""地域枚举
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""资产类型枚举
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""Vpc枚举
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""Appid枚举
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def PublicPrivateAttr(self):
        r"""公网内网枚举
        :rtype: list of FilterDataObject
        """
        return self._PublicPrivateAttr

    @PublicPrivateAttr.setter
    def PublicPrivateAttr(self, PublicPrivateAttr):
        self._PublicPrivateAttr = PublicPrivateAttr

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("PublicPrivateAttr") is not None:
            self._PublicPrivateAttr = []
            for item in params.get("PublicPrivateAttr"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PublicPrivateAttr.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainAssetsRequest(AbstractModel):
    r"""DescribeDomainAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 安全中心自定义标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""安全中心自定义标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAssetsResponse(AbstractModel):
    r"""DescribeDomainAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 域名列表
        :type Data: list of DomainAssetVO
        :param _DefenseStatusList: 防护状态列表
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetLocationList: 资产归属地列表
        :type AssetLocationList: list of FilterDataObject
        :param _SourceTypeList: 资产类型列表
        :type SourceTypeList: list of FilterDataObject
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._DefenseStatusList = None
        self._AssetLocationList = None
        self._SourceTypeList = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""域名列表
        :rtype: list of DomainAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DefenseStatusList(self):
        r"""防护状态列表
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetLocationList(self):
        r"""资产归属地列表
        :rtype: list of FilterDataObject
        """
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def SourceTypeList(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._SourceTypeList

    @SourceTypeList.setter
    def SourceTypeList(self, SourceTypeList):
        self._SourceTypeList = SourceTypeList

    @property
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("SourceTypeList") is not None:
            self._SourceTypeList = []
            for item in params.get("SourceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SourceTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExposeAssetCategoryRequest(AbstractModel):
    r"""DescribeExposeAssetCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposeAssetCategoryResponse(AbstractModel):
    r"""DescribeExposeAssetCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExposeAssetTypeList: 云边界分析资产分类列表
        :type ExposeAssetTypeList: list of ExposeAssetTypeItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExposeAssetTypeList = None
        self._RequestId = None

    @property
    def ExposeAssetTypeList(self):
        r"""云边界分析资产分类列表
        :rtype: list of ExposeAssetTypeItem
        """
        return self._ExposeAssetTypeList

    @ExposeAssetTypeList.setter
    def ExposeAssetTypeList(self, ExposeAssetTypeList):
        self._ExposeAssetTypeList = ExposeAssetTypeList

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
        if params.get("ExposeAssetTypeList") is not None:
            self._ExposeAssetTypeList = []
            for item in params.get("ExposeAssetTypeList"):
                obj = ExposeAssetTypeItem()
                obj._deserialize(item)
                self._ExposeAssetTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExposePathRequest(AbstractModel):
    r"""DescribeExposePath请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _Ip: 资产IP
        :type Ip: str
        :param _Domain: 资产域名
        :type Domain: str
        :param _Port: 端口或端口范围
        :type Port: str
        """
        self._MemberId = None
        self._AssetId = None
        self._Ip = None
        self._Domain = None
        self._Port = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AssetId(self):
        r"""资产ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Ip(self):
        r"""资产IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        r"""资产域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Port(self):
        r"""端口或端口范围
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._AssetId = params.get("AssetId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposePathResponse(AbstractModel):
    r"""DescribeExposePath返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 云边界分析路径节点内容
        :type Content: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._RequestId = None

    @property
    def Content(self):
        r"""云边界分析路径节点内容
        :rtype: str
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
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class DescribeExposuresRequest(AbstractModel):
    r"""DescribeExposures请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposuresResponse(AbstractModel):
    r"""DescribeExposures返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 云边界分析资产数量
        :type TotalCount: int
        :param _ExposeList: 云边界分析资产列表
        :type ExposeList: list of ExposesItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ExposeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""云边界分析资产数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExposeList(self):
        r"""云边界分析资产列表
        :rtype: list of ExposesItem
        """
        return self._ExposeList

    @ExposeList.setter
    def ExposeList(self, ExposeList):
        self._ExposeList = ExposeList

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
        if params.get("ExposeList") is not None:
            self._ExposeList = []
            for item in params.get("ExposeList"):
                obj = ExposesItem()
                obj._deserialize(item)
                self._ExposeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayAssetsRequest(AbstractModel):
    r"""DescribeGatewayAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayAssetsResponse(AbstractModel):
    r"""DescribeGatewayAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of GateWayAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型列表
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of GateWayAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""vpc列表
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""appid列表
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = GateWayAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHighBaseLineRiskListRequest(AbstractModel):
    r"""DescribeHighBaseLineRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _CloudAccountID: 云账号ID
        :type CloudAccountID: str
        :param _Provider: 云厂商
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._CloudAccountID = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def CloudAccountID(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._CloudAccountID = params.get("CloudAccountID")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHighBaseLineRiskListResponse(AbstractModel):
    r"""DescribeHighBaseLineRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 高危基线风险数量
        :type TotalCount: int
        :param _HighBaseLineRiskList: 高危基线风险列表
        :type HighBaseLineRiskList: list of HighBaseLineRiskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HighBaseLineRiskList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""高危基线风险数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HighBaseLineRiskList(self):
        r"""高危基线风险列表
        :rtype: list of HighBaseLineRiskItem
        """
        return self._HighBaseLineRiskList

    @HighBaseLineRiskList.setter
    def HighBaseLineRiskList(self, HighBaseLineRiskList):
        self._HighBaseLineRiskList = HighBaseLineRiskList

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
        if params.get("HighBaseLineRiskList") is not None:
            self._HighBaseLineRiskList = []
            for item in params.get("HighBaseLineRiskList"):
                obj = HighBaseLineRiskItem()
                obj._deserialize(item)
                self._HighBaseLineRiskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerListRequest(AbstractModel):
    r"""DescribeListenerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerListResponse(AbstractModel):
    r"""DescribeListenerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 监听器列表
        :type Data: list of ClbListenerListInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""监听器列表
        :rtype: list of ClbListenerListInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ClbListenerListInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNICAssetsRequest(AbstractModel):
    r"""DescribeNICAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNICAssetsResponse(AbstractModel):
    r"""DescribeNICAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of NICAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型列表
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of NICAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""vpc列表
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""appid列表
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = NICAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationInfoRequest(AbstractModel):
    r"""DescribeOrganizationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationInfoResponse(AbstractModel):
    r"""DescribeOrganizationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 集团用户列表
        :type Data: list of OrganizationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""集团用户列表
        :rtype: list of OrganizationInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OrganizationInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationUserInfoRequest(AbstractModel):
    r"""DescribeOrganizationUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _NotSupportCloud: 不支持多云
        :type NotSupportCloud: bool
        """
        self._MemberId = None
        self._Filter = None
        self._NotSupportCloud = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def NotSupportCloud(self):
        r"""不支持多云
        :rtype: bool
        """
        return self._NotSupportCloud

    @NotSupportCloud.setter
    def NotSupportCloud(self, NotSupportCloud):
        self._NotSupportCloud = NotSupportCloud


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._NotSupportCloud = params.get("NotSupportCloud")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationUserInfoResponse(AbstractModel):
    r"""DescribeOrganizationUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 集团用户列表
        :type Data: list of OrganizationUserInfo
        :param _JoinTypeLst: 加入方式枚举
        :type JoinTypeLst: list of FilterDataObject
        :param _CloudTypeLst: 云厂商枚举
        :type CloudTypeLst: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._JoinTypeLst = None
        self._CloudTypeLst = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""集团用户列表
        :rtype: list of OrganizationUserInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def JoinTypeLst(self):
        r"""加入方式枚举
        :rtype: list of FilterDataObject
        """
        return self._JoinTypeLst

    @JoinTypeLst.setter
    def JoinTypeLst(self, JoinTypeLst):
        self._JoinTypeLst = JoinTypeLst

    @property
    def CloudTypeLst(self):
        r"""云厂商枚举
        :rtype: list of FilterDataObject
        """
        return self._CloudTypeLst

    @CloudTypeLst.setter
    def CloudTypeLst(self, CloudTypeLst):
        self._CloudTypeLst = CloudTypeLst

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OrganizationUserInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("JoinTypeLst") is not None:
            self._JoinTypeLst = []
            for item in params.get("JoinTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._JoinTypeLst.append(obj)
        if params.get("CloudTypeLst") is not None:
            self._CloudTypeLst = []
            for item in params.get("CloudTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CloudTypeLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOtherCloudAssetsRequest(AbstractModel):
    r"""DescribeOtherCloudAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _AssetTypes: 资产类型:MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :type AssetTypes: list of str
        """
        self._MemberId = None
        self._Filter = None
        self._AssetTypes = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AssetTypes(self):
        r"""资产类型:MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :rtype: list of str
        """
        return self._AssetTypes

    @AssetTypes.setter
    def AssetTypes(self, AssetTypes):
        self._AssetTypes = AssetTypes


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._AssetTypes = params.get("AssetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOtherCloudAssetsResponse(AbstractModel):
    r"""DescribeOtherCloudAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 资产总数
        :type Data: list of DBAssetVO
        :param _RegionList: 地域枚举
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: Vpc枚举
        :type VpcList: list of FilterDataObject
        :param _AppIdList: Appid枚举
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""资产总数
        :rtype: list of DBAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""地域枚举
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""资产类型枚举
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""Vpc枚举
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""Appid枚举
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicIpAssetsRequest(AbstractModel):
    r"""DescribePublicIpAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 安全中心自定义标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""安全中心自定义标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicIpAssetsResponse(AbstractModel):
    r"""DescribePublicIpAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of IpAssetListVO
        :param _Total: 总数
        :type Total: int
        :param _AssetLocationList: 资产归属地
        :type AssetLocationList: list of FilterDataObject
        :param _IpTypeList: ip列表枚举
        :type IpTypeList: list of FilterDataObject
        :param _RegionList: 地域列表枚举
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: 防护枚举
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetTypeList: 资产类型枚举
        :type AssetTypeList: list of FilterDataObject
        :param _AppIdList: AppId枚举
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._AssetLocationList = None
        self._IpTypeList = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._AssetTypeList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of IpAssetListVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AssetLocationList(self):
        r"""资产归属地
        :rtype: list of FilterDataObject
        """
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def IpTypeList(self):
        r"""ip列表枚举
        :rtype: list of FilterDataObject
        """
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def RegionList(self):
        r"""地域列表枚举
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        r"""防护枚举
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetTypeList(self):
        r"""资产类型枚举
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def AppIdList(self):
        r"""AppId枚举
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IpAssetListVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRepositoryImageAssetsRequest(AbstractModel):
    r"""DescribeRepositoryImageAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: filter过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""filter过滤条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryImageAssetsResponse(AbstractModel):
    r"""DescribeRepositoryImageAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 仓库镜像列表
        :type Data: list of RepositoryImageVO
        :param _Total: 总数
        :type Total: int
        :param _RegionList: region列表
        :type RegionList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""仓库镜像列表
        :rtype: list of RepositoryImageVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RegionList(self):
        r"""region列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RepositoryImageVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCallRecordRequest(AbstractModel):
    r"""DescribeRiskCallRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskID: 风险记录ID
        :type RiskID: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._RiskID = None
        self._MemberId = None
        self._Filter = None

    @property
    def RiskID(self):
        r"""风险记录ID
        :rtype: int
        """
        return self._RiskID

    @RiskID.setter
    def RiskID(self, RiskID):
        self._RiskID = RiskID

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._RiskID = params.get("RiskID")
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCallRecordResponse(AbstractModel):
    r"""DescribeRiskCallRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 风险调用记录列表
        :type Data: list of RiskCallRecord
        :param _Total: 调用记录总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""风险调用记录列表
        :rtype: list of RiskCallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""调用记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RiskCallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewCFGRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewCFGRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewCFGRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewCFGRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of AssetViewCFGRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _CFGNameLists: 配置名列表
        :type CFGNameLists: list of FilterDataObject
        :param _CheckTypeLists: 检查类型列表
        :type CheckTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._CFGNameLists = None
        self._CheckTypeLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""资产视角的配置风险列表
        :rtype: list of AssetViewCFGRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def CFGNameLists(self):
        r"""配置名列表
        :rtype: list of FilterDataObject
        """
        return self._CFGNameLists

    @CFGNameLists.setter
    def CFGNameLists(self, CFGNameLists):
        self._CFGNameLists = CFGNameLists

    @property
    def CheckTypeLists(self):
        r"""检查类型列表
        :rtype: list of FilterDataObject
        """
        return self._CheckTypeLists

    @CheckTypeLists.setter
    def CheckTypeLists(self, CheckTypeLists):
        self._CheckTypeLists = CheckTypeLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewCFGRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("CFGNameLists") is not None:
            self._CFGNameLists = []
            for item in params.get("CFGNameLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CFGNameLists.append(obj)
        if params.get("CheckTypeLists") is not None:
            self._CheckTypeLists = []
            for item in params.get("CheckTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewPortRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewPortRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewPortRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewPortRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of AssetViewPortRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: 建议列表
        :type SuggestionLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""资产视角的配置风险列表
        :rtype: list of AssetViewPortRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        r"""建议列表
        :rtype: list of FilterDataObject
        """
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewVULRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewVULRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewVULRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewVULRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的漏洞风险列表
        :type Data: list of AssetViewVULRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""资产视角的漏洞风险列表
        :rtype: list of AssetViewVULRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""漏洞类型列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewWeakPasswordRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewWeakPasswordRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewWeakPasswordRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewWeakPasswordRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 风险列表
        :type Data: list of AssetViewWeakPassRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _PasswordTypeLists: 弱口令类型列表
        :type PasswordTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._InstanceTypeLists = None
        self._PasswordTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""风险列表
        :rtype: list of AssetViewWeakPassRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def PasswordTypeLists(self):
        r"""弱口令类型列表
        :rtype: list of FilterDataObject
        """
        return self._PasswordTypeLists

    @PasswordTypeLists.setter
    def PasswordTypeLists(self, PasswordTypeLists):
        self._PasswordTypeLists = PasswordTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewWeakPassRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("PasswordTypeLists") is not None:
            self._PasswordTypeLists = []
            for item in params.get("PasswordTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PasswordTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterCFGViewCFGRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterCFGViewCFGRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterCFGViewCFGRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterCFGViewCFGRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 资产视角的配置风险列表
        :type Data: list of CFGViewCFGRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _CFGNameLists: 配置名列表
        :type CFGNameLists: list of FilterDataObject
        :param _CheckTypeLists: 检查类型列表
        :type CheckTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._CFGNameLists = None
        self._CheckTypeLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""资产视角的配置风险列表
        :rtype: list of CFGViewCFGRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def CFGNameLists(self):
        r"""配置名列表
        :rtype: list of FilterDataObject
        """
        return self._CFGNameLists

    @CFGNameLists.setter
    def CFGNameLists(self, CFGNameLists):
        self._CFGNameLists = CFGNameLists

    @property
    def CheckTypeLists(self):
        r"""检查类型列表
        :rtype: list of FilterDataObject
        """
        return self._CheckTypeLists

    @CheckTypeLists.setter
    def CheckTypeLists(self, CheckTypeLists):
        self._CheckTypeLists = CheckTypeLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CFGViewCFGRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("CFGNameLists") is not None:
            self._CFGNameLists = []
            for item in params.get("CFGNameLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CFGNameLists.append(obj)
        if params.get("CheckTypeLists") is not None:
            self._CheckTypeLists = []
            for item in params.get("CheckTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterPortViewPortRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterPortViewPortRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterPortViewPortRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterPortViewPortRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 端口视角的端口风险列表
        :type Data: list of PortViewPortRisk
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: 处置建议列表
        :type SuggestionLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""端口视角的端口风险列表
        :rtype: list of PortViewPortRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        r"""处置建议列表
        :rtype: list of FilterDataObject
        """
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PortViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterServerRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterServerRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterServerRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterServerRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 风险服务列表
        :type Data: list of ServerRisk
        :param _InstanceTypeLists: 资产类型枚举
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""风险服务列表
        :rtype: list of ServerRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def InstanceTypeLists(self):
        r"""资产类型枚举
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ServerRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterVULViewVULRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterVULViewVULRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterVULViewVULRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterVULViewVULRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 漏洞产视角的漏洞风险列表
        :type Data: list of VULViewVULRisk
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""漏洞产视角的漏洞风险列表
        :rtype: list of VULViewVULRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""漏洞类型列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterWebsiteRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterWebsiteRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterWebsiteRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterWebsiteRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 内容风险列表
        :type Data: list of WebsiteRisk
        :param _StatusLists: 状态列表
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _InstanceTypeLists: 资产类型列表
        :type InstanceTypeLists: list of FilterDataObject
        :param _DetectEngineLists: 风险类型列表
        :type DetectEngineLists: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._InstanceTypeLists = None
        self._DetectEngineLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""内容风险列表
        :rtype: list of WebsiteRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""状态列表
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def InstanceTypeLists(self):
        r"""资产类型列表
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def DetectEngineLists(self):
        r"""风险类型列表
        :rtype: list of FilterDataObject
        """
        return self._DetectEngineLists

    @DetectEngineLists.setter
    def DetectEngineLists(self, DetectEngineLists):
        self._DetectEngineLists = DetectEngineLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WebsiteRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("DetectEngineLists") is not None:
            self._DetectEngineLists = []
            for item in params.get("DetectEngineLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DetectEngineLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskDetailListRequest(AbstractModel):
    r"""DescribeRiskDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskRuleId: 风险规则ID
        :type RiskRuleId: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._RiskRuleId = None
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._InstanceId = None

    @property
    def RiskRuleId(self):
        r"""风险规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._RiskRuleId = params.get("RiskRuleId")
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskDetailListResponse(AbstractModel):
    r"""DescribeRiskDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资产视角下风险详情数量
        :type TotalCount: int
        :param _AssetRiskDetailList: 资产视角下风险详情列表
        :type AssetRiskDetailList: list of RiskDetailItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AssetRiskDetailList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""资产视角下风险详情数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AssetRiskDetailList(self):
        r"""资产视角下风险详情列表
        :rtype: list of RiskDetailItem
        """
        return self._AssetRiskDetailList

    @AssetRiskDetailList.setter
    def AssetRiskDetailList(self, AssetRiskDetailList):
        self._AssetRiskDetailList = AssetRiskDetailList

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
        if params.get("AssetRiskDetailList") is not None:
            self._AssetRiskDetailList = []
            for item in params.get("AssetRiskDetailList"):
                obj = RiskDetailItem()
                obj._deserialize(item)
                self._AssetRiskDetailList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskRuleDetailRequest(AbstractModel):
    r"""DescribeRiskRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskRuleId: 风险规则ID
        :type RiskRuleId: str
        """
        self._RiskRuleId = None

    @property
    def RiskRuleId(self):
        r"""风险规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId


    def _deserialize(self, params):
        self._RiskRuleId = params.get("RiskRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskRuleDetailResponse(AbstractModel):
    r"""DescribeRiskRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskRuleId: 风险规则ID
        :type RiskRuleId: str
        :param _Provider: 云厂商
        :type Provider: str
        :param _RiskName: 风险名称
        :type RiskName: str
        :param _RiskInfluence: 风险危害
        :type RiskInfluence: str
        :param _RiskFixAdvice: 修复指引
        :type RiskFixAdvice: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskRuleId = None
        self._Provider = None
        self._RiskName = None
        self._RiskInfluence = None
        self._RiskFixAdvice = None
        self._RequestId = None

    @property
    def RiskRuleId(self):
        r"""风险规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def RiskName(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskInfluence(self):
        r"""风险危害
        :rtype: str
        """
        return self._RiskInfluence

    @RiskInfluence.setter
    def RiskInfluence(self, RiskInfluence):
        self._RiskInfluence = RiskInfluence

    @property
    def RiskFixAdvice(self):
        r"""修复指引
        :rtype: str
        """
        return self._RiskFixAdvice

    @RiskFixAdvice.setter
    def RiskFixAdvice(self, RiskFixAdvice):
        self._RiskFixAdvice = RiskFixAdvice

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
        self._RiskRuleId = params.get("RiskRuleId")
        self._Provider = params.get("Provider")
        self._RiskName = params.get("RiskName")
        self._RiskInfluence = params.get("RiskInfluence")
        self._RiskFixAdvice = params.get("RiskFixAdvice")
        self._RequestId = params.get("RequestId")


class DescribeRiskRulesRequest(AbstractModel):
    r"""DescribeRiskRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskRulesResponse(AbstractModel):
    r"""DescribeRiskRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 风险规则数量
        :type TotalCount: int
        :param _RiskRuleList: 风险规则列表
        :type RiskRuleList: list of RiskRuleItem
        :param _InstanceTypeList: 实例类型选项
        :type InstanceTypeList: list of AttributeOptionSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RiskRuleList = None
        self._InstanceTypeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""风险规则数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RiskRuleList(self):
        r"""风险规则列表
        :rtype: list of RiskRuleItem
        """
        return self._RiskRuleList

    @RiskRuleList.setter
    def RiskRuleList(self, RiskRuleList):
        self._RiskRuleList = RiskRuleList

    @property
    def InstanceTypeList(self):
        r"""实例类型选项
        :rtype: list of AttributeOptionSet
        """
        return self._InstanceTypeList

    @InstanceTypeList.setter
    def InstanceTypeList(self, InstanceTypeList):
        self._InstanceTypeList = InstanceTypeList

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
        if params.get("RiskRuleList") is not None:
            self._RiskRuleList = []
            for item in params.get("RiskRuleList"):
                obj = RiskRuleItem()
                obj._deserialize(item)
                self._RiskRuleList.append(obj)
        if params.get("InstanceTypeList") is not None:
            self._InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = AttributeOptionSet()
                obj._deserialize(item)
                self._InstanceTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanReportListRequest(AbstractModel):
    r"""DescribeScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 列表过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""列表过滤条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanReportListResponse(AbstractModel):
    r"""DescribeScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 任务日志列表
        :type Data: list of ScanTaskInfo
        :param _UINList: 主账户ID列表
        :type UINList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""任务日志列表
        :rtype: list of ScanTaskInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        r"""主账户ID列表
        :rtype: list of str
        """
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        self._RequestId = params.get("RequestId")


class DescribeScanStatisticRequest(AbstractModel):
    r"""DescribeScanStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _TaskLogId: 体检任务id
        :type TaskLogId: str
        """
        self._MemberId = None
        self._TaskLogId = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def TaskLogId(self):
        r"""体检任务id
        :rtype: str
        """
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._TaskLogId = params.get("TaskLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanStatisticResponse(AbstractModel):
    r"""DescribeScanStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PortServiceCount: 端口服务数量
        :type PortServiceCount: int
        :param _WebAppCount: Web服务数量
        :type WebAppCount: int
        :param _WeakPasswordCount: 弱口令风险数量
        :type WeakPasswordCount: int
        :param _VulCount: 漏洞风险数量
        :type VulCount: int
        :param _HighRiskPortServiceCount: 高危端口服务数量
        :type HighRiskPortServiceCount: int
        :param _RiskWebAppCount: 风险Web服务数量
        :type RiskWebAppCount: int
        :param _PortServiceIncrement: 端口服务近7天新增数量
        :type PortServiceIncrement: int
        :param _WebAppIncrement: Web服务近7天新增数量
        :type WebAppIncrement: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PortServiceCount = None
        self._WebAppCount = None
        self._WeakPasswordCount = None
        self._VulCount = None
        self._HighRiskPortServiceCount = None
        self._RiskWebAppCount = None
        self._PortServiceIncrement = None
        self._WebAppIncrement = None
        self._RequestId = None

    @property
    def PortServiceCount(self):
        r"""端口服务数量
        :rtype: int
        """
        return self._PortServiceCount

    @PortServiceCount.setter
    def PortServiceCount(self, PortServiceCount):
        self._PortServiceCount = PortServiceCount

    @property
    def WebAppCount(self):
        r"""Web服务数量
        :rtype: int
        """
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def WeakPasswordCount(self):
        r"""弱口令风险数量
        :rtype: int
        """
        return self._WeakPasswordCount

    @WeakPasswordCount.setter
    def WeakPasswordCount(self, WeakPasswordCount):
        self._WeakPasswordCount = WeakPasswordCount

    @property
    def VulCount(self):
        r"""漏洞风险数量
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def HighRiskPortServiceCount(self):
        r"""高危端口服务数量
        :rtype: int
        """
        return self._HighRiskPortServiceCount

    @HighRiskPortServiceCount.setter
    def HighRiskPortServiceCount(self, HighRiskPortServiceCount):
        self._HighRiskPortServiceCount = HighRiskPortServiceCount

    @property
    def RiskWebAppCount(self):
        r"""风险Web服务数量
        :rtype: int
        """
        return self._RiskWebAppCount

    @RiskWebAppCount.setter
    def RiskWebAppCount(self, RiskWebAppCount):
        self._RiskWebAppCount = RiskWebAppCount

    @property
    def PortServiceIncrement(self):
        r"""端口服务近7天新增数量
        :rtype: int
        """
        return self._PortServiceIncrement

    @PortServiceIncrement.setter
    def PortServiceIncrement(self, PortServiceIncrement):
        self._PortServiceIncrement = PortServiceIncrement

    @property
    def WebAppIncrement(self):
        r"""Web服务近7天新增数量
        :rtype: int
        """
        return self._WebAppIncrement

    @WebAppIncrement.setter
    def WebAppIncrement(self, WebAppIncrement):
        self._WebAppIncrement = WebAppIncrement

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
        self._PortServiceCount = params.get("PortServiceCount")
        self._WebAppCount = params.get("WebAppCount")
        self._WeakPasswordCount = params.get("WeakPasswordCount")
        self._VulCount = params.get("VulCount")
        self._HighRiskPortServiceCount = params.get("HighRiskPortServiceCount")
        self._RiskWebAppCount = params.get("RiskWebAppCount")
        self._PortServiceIncrement = params.get("PortServiceIncrement")
        self._WebAppIncrement = params.get("WebAppIncrement")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    r"""DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 标签
        :type Tags: list of Tags
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""标签
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskListResponse(AbstractModel):
    r"""DescribeScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 任务日志列表
        :type Data: list of ScanTaskInfoList
        :param _UINList: 主账户ID列表
        :type UINList: list of str
        :param _TaskModeList: 体检模式过滤列表
        :type TaskModeList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._TaskModeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""任务日志列表
        :rtype: list of ScanTaskInfoList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        r"""主账户ID列表
        :rtype: list of str
        """
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

    @property
    def TaskModeList(self):
        r"""体检模式过滤列表
        :rtype: list of FilterDataObject
        """
        return self._TaskModeList

    @TaskModeList.setter
    def TaskModeList(self, TaskModeList):
        self._TaskModeList = TaskModeList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfoList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        if params.get("TaskModeList") is not None:
            self._TaskModeList = []
            for item in params.get("TaskModeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._TaskModeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSearchBugInfoRequest(AbstractModel):
    r"""DescribeSearchBugInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 1的时候返回应急漏洞，2的时候返回应急漏洞列表，3的时候搭配输入CVEId字段展示该漏洞数据
        :type Id: str
        :param _CVEId: id=3时传入该参数
        :type CVEId: str
        """
        self._Id = None
        self._CVEId = None

    @property
    def Id(self):
        r"""1的时候返回应急漏洞，2的时候返回应急漏洞列表，3的时候搭配输入CVEId字段展示该漏洞数据
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CVEId(self):
        r"""id=3时传入该参数
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CVEId = params.get("CVEId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchBugInfoResponse(AbstractModel):
    r"""DescribeSearchBugInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 漏洞信息和资产信息
        :type Data: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        :param _ReturnCode: 状态值，0：查询成功，非0：查询失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""漏洞信息和资产信息
        :rtype: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        r"""状态值，0：查询成功，非0：查询失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        r"""状态信息，success：查询成功，fail：查询失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        if params.get("Data") is not None:
            self._Data = DataSearchBug()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeSourceIPAssetRequest(AbstractModel):
    r"""DescribeSourceIPAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIPAssetResponse(AbstractModel):
    r"""DescribeSourceIPAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 访问密钥资产列表
        :type Data: list of SourceIPAsset
        :param _Total: 全部数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""访问密钥资产列表
        :rtype: list of SourceIPAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""全部数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceIPAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSubUserInfoRequest(AbstractModel):
    r"""DescribeSubUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubUserInfoResponse(AbstractModel):
    r"""DescribeSubUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 子用户列表
        :type Data: list of SubUserInfo
        :param _CloudTypeLst: 厂商枚举列表
        :type CloudTypeLst: list of FilterDataObject
        :param _OwnerAppIDLst: 所属主账号appid枚举
        :type OwnerAppIDLst: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._CloudTypeLst = None
        self._OwnerAppIDLst = None
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
    def Data(self):
        r"""子用户列表
        :rtype: list of SubUserInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CloudTypeLst(self):
        r"""厂商枚举列表
        :rtype: list of FilterDataObject
        """
        return self._CloudTypeLst

    @CloudTypeLst.setter
    def CloudTypeLst(self, CloudTypeLst):
        self._CloudTypeLst = CloudTypeLst

    @property
    def OwnerAppIDLst(self):
        r"""所属主账号appid枚举
        :rtype: list of FilterDataObject
        """
        return self._OwnerAppIDLst

    @OwnerAppIDLst.setter
    def OwnerAppIDLst(self, OwnerAppIDLst):
        self._OwnerAppIDLst = OwnerAppIDLst

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubUserInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("CloudTypeLst") is not None:
            self._CloudTypeLst = []
            for item in params.get("CloudTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CloudTypeLst.append(obj)
        if params.get("OwnerAppIDLst") is not None:
            self._OwnerAppIDLst = []
            for item in params.get("OwnerAppIDLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OwnerAppIDLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetAssetsRequest(AbstractModel):
    r"""DescribeSubnetAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAssetsResponse(AbstractModel):
    r"""DescribeSubnetAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of SubnetAsset
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: 可用区列表
        :type ZoneList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._VpcList = None
        self._AppIdList = None
        self._ZoneList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of SubnetAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def VpcList(self):
        r"""vpc列表
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""appid列表
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        r"""可用区列表
        :rtype: list of FilterDataObject
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskLogListRequest(AbstractModel):
    r"""DescribeTaskLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogListResponse(AbstractModel):
    r"""DescribeTaskLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 报告列表
        :type Data: list of TaskLogInfo
        :param _NotViewNumber: 待查看数量
        :type NotViewNumber: int
        :param _ReportTemplateNumber: 报告模板数
        :type ReportTemplateNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._NotViewNumber = None
        self._ReportTemplateNumber = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""报告列表
        :rtype: list of TaskLogInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def NotViewNumber(self):
        r"""待查看数量
        :rtype: int
        """
        return self._NotViewNumber

    @NotViewNumber.setter
    def NotViewNumber(self, NotViewNumber):
        self._NotViewNumber = NotViewNumber

    @property
    def ReportTemplateNumber(self):
        r"""报告模板数
        :rtype: int
        """
        return self._ReportTemplateNumber

    @ReportTemplateNumber.setter
    def ReportTemplateNumber(self, ReportTemplateNumber):
        self._ReportTemplateNumber = ReportTemplateNumber

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._NotViewNumber = params.get("NotViewNumber")
        self._ReportTemplateNumber = params.get("ReportTemplateNumber")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogURLRequest(AbstractModel):
    r"""DescribeTaskLogURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 0: 预览， 1: 下载
        :type Type: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _ReportItemKeyList: 任务报告Id 列表
        :type ReportItemKeyList: list of ReportItemKey
        :param _ReportTaskIdList: 报告中任务id列表
        :type ReportTaskIdList: list of ReportTaskIdList
        """
        self._Type = None
        self._MemberId = None
        self._ReportItemKeyList = None
        self._ReportTaskIdList = None

    @property
    def Type(self):
        r"""0: 预览， 1: 下载
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ReportItemKeyList(self):
        r"""任务报告Id 列表
        :rtype: list of ReportItemKey
        """
        return self._ReportItemKeyList

    @ReportItemKeyList.setter
    def ReportItemKeyList(self, ReportItemKeyList):
        self._ReportItemKeyList = ReportItemKeyList

    @property
    def ReportTaskIdList(self):
        r"""报告中任务id列表
        :rtype: list of ReportTaskIdList
        """
        return self._ReportTaskIdList

    @ReportTaskIdList.setter
    def ReportTaskIdList(self, ReportTaskIdList):
        self._ReportTaskIdList = ReportTaskIdList


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._MemberId = params.get("MemberId")
        if params.get("ReportItemKeyList") is not None:
            self._ReportItemKeyList = []
            for item in params.get("ReportItemKeyList"):
                obj = ReportItemKey()
                obj._deserialize(item)
                self._ReportItemKeyList.append(obj)
        if params.get("ReportTaskIdList") is not None:
            self._ReportTaskIdList = []
            for item in params.get("ReportTaskIdList"):
                obj = ReportTaskIdList()
                obj._deserialize(item)
                self._ReportTaskIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogURLResponse(AbstractModel):
    r"""DescribeTaskLogURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回报告临时下载url
        :type Data: list of TaskLogURL
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回报告临时下载url
        :rtype: list of TaskLogURL
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogURL()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopAttackInfoRequest(AbstractModel):
    r"""DescribeTopAttackInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _QueryType: 1:攻击类型 2:攻击者
        :type QueryType: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _AssetType: 0: 默认全部 1:资产ID 2:域名
        :type AssetType: int
        """
        self._StartTime = None
        self._EndTime = None
        self._QueryType = None
        self._MemberId = None
        self._OperatedMemberId = None
        self._AssetName = None
        self._AssetType = None

    @property
    def StartTime(self):
        r"""起始时间
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
    def QueryType(self):
        r"""1:攻击类型 2:攻击者
        :rtype: int
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def OperatedMemberId(self):
        r"""被调用的集团账号的成员id
        :rtype: list of str
        """
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId

    @property
    def AssetName(self):
        r"""资产名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""0: 默认全部 1:资产ID 2:域名
        :rtype: int
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._MemberId = params.get("MemberId")
        self._OperatedMemberId = params.get("OperatedMemberId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopAttackInfoResponse(AbstractModel):
    r"""DescribeTopAttackInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopAttackInfo: Top攻击类型/攻击者次数
        :type TopAttackInfo: list of TagCount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopAttackInfo = None
        self._RequestId = None

    @property
    def TopAttackInfo(self):
        r"""Top攻击类型/攻击者次数
        :rtype: list of TagCount
        """
        return self._TopAttackInfo

    @TopAttackInfo.setter
    def TopAttackInfo(self, TopAttackInfo):
        self._TopAttackInfo = TopAttackInfo

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
        if params.get("TopAttackInfo") is not None:
            self._TopAttackInfo = []
            for item in params.get("TopAttackInfo"):
                obj = TagCount()
                obj._deserialize(item)
                self._TopAttackInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUebaRuleRequest(AbstractModel):
    r"""DescribeUebaRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUebaRuleResponse(AbstractModel):
    r"""DescribeUebaRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 策略列表
        :type Data: list of UebaRule
        :param _AlterType: 自定义策略对应的告警类别枚举
        :type AlterType: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._AlterType = None
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
    def Data(self):
        r"""策略列表
        :rtype: list of UebaRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AlterType(self):
        r"""自定义策略对应的告警类别枚举
        :rtype: list of FilterDataObject
        """
        return self._AlterType

    @AlterType.setter
    def AlterType(self, AlterType):
        self._AlterType = AlterType

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = UebaRule()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("AlterType") is not None:
            self._AlterType = []
            for item in params.get("AlterType"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AlterType.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserCallRecordRequest(AbstractModel):
    r"""DescribeUserCallRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubUin: 账号uin
        :type SubUin: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤器
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._SubUin = None
        self._MemberId = None
        self._Filter = None

    @property
    def SubUin(self):
        r"""账号uin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤器
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCallRecordResponse(AbstractModel):
    r"""DescribeUserCallRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 账号调用记录列表
        :type Data: list of UserCallRecord
        :param _Total: 调用记录总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""账号调用记录列表
        :rtype: list of UserCallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""调用记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = UserCallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeVULListRequest(AbstractModel):
    r"""DescribeVULList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 查询条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""查询条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULListResponse(AbstractModel):
    r"""DescribeVULList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 漏洞列表
        :type Data: list of VULBaseInfo
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _RiskLevels: 风险等级列表
        :type RiskLevels: list of FilterDataObject
        :param _Tags: 标签
        :type Tags: list of FilterDataObject
        :param _ProductSupport: 产品支持情况
        :type ProductSupport: list of FilterDataObject
        :param _CheckStatus: 产品支持情况
        :type CheckStatus: list of FilterDataObject
        :param _AttackHeat: 攻击热度枚举
        :type AttackHeat: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._VULTypeLists = None
        self._RiskLevels = None
        self._Tags = None
        self._ProductSupport = None
        self._CheckStatus = None
        self._AttackHeat = None
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
    def Data(self):
        r"""漏洞列表
        :rtype: list of VULBaseInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def VULTypeLists(self):
        r"""漏洞类型列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def RiskLevels(self):
        r"""风险等级列表
        :rtype: list of FilterDataObject
        """
        return self._RiskLevels

    @RiskLevels.setter
    def RiskLevels(self, RiskLevels):
        self._RiskLevels = RiskLevels

    @property
    def Tags(self):
        r"""标签
        :rtype: list of FilterDataObject
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProductSupport(self):
        r"""产品支持情况
        :rtype: list of FilterDataObject
        """
        return self._ProductSupport

    @ProductSupport.setter
    def ProductSupport(self, ProductSupport):
        self._ProductSupport = ProductSupport

    @property
    def CheckStatus(self):
        r"""产品支持情况
        :rtype: list of FilterDataObject
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def AttackHeat(self):
        r"""攻击热度枚举
        :rtype: list of FilterDataObject
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULBaseInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("RiskLevels") is not None:
            self._RiskLevels = []
            for item in params.get("RiskLevels"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RiskLevels.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ProductSupport") is not None:
            self._ProductSupport = []
            for item in params.get("ProductSupport"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProductSupport.append(obj)
        if params.get("CheckStatus") is not None:
            self._CheckStatus = []
            for item in params.get("CheckStatus"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckStatus.append(obj)
        if params.get("AttackHeat") is not None:
            self._AttackHeat = []
            for item in params.get("AttackHeat"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AttackHeat.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskAdvanceCFGListRequest(AbstractModel):
    r"""DescribeVULRiskAdvanceCFGList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Filter: 过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._TaskId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._TaskId = params.get("TaskId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskAdvanceCFGListResponse(AbstractModel):
    r"""DescribeVULRiskAdvanceCFGList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 配置项列表
        :type Data: list of VULRiskAdvanceCFGList
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RiskLevelLists: 风险等级过滤列表
        :type RiskLevelLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型过滤列表
        :type VULTypeLists: list of FilterDataObject
        :param _CheckFromLists: 识别来源过滤列表
        :type CheckFromLists: list of FilterDataObject
        :param _VulTagList: 漏洞标签列表
        :type VulTagList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RiskLevelLists = None
        self._VULTypeLists = None
        self._CheckFromLists = None
        self._VulTagList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""配置项列表
        :rtype: list of VULRiskAdvanceCFGList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def RiskLevelLists(self):
        r"""风险等级过滤列表
        :rtype: list of FilterDataObject
        """
        return self._RiskLevelLists

    @RiskLevelLists.setter
    def RiskLevelLists(self, RiskLevelLists):
        self._RiskLevelLists = RiskLevelLists

    @property
    def VULTypeLists(self):
        r"""漏洞类型过滤列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def CheckFromLists(self):
        r"""识别来源过滤列表
        :rtype: list of FilterDataObject
        """
        return self._CheckFromLists

    @CheckFromLists.setter
    def CheckFromLists(self, CheckFromLists):
        self._CheckFromLists = CheckFromLists

    @property
    def VulTagList(self):
        r"""漏洞标签列表
        :rtype: list of FilterDataObject
        """
        return self._VulTagList

    @VulTagList.setter
    def VulTagList(self, VulTagList):
        self._VulTagList = VulTagList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULRiskAdvanceCFGList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RiskLevelLists") is not None:
            self._RiskLevelLists = []
            for item in params.get("RiskLevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RiskLevelLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("CheckFromLists") is not None:
            self._CheckFromLists = []
            for item in params.get("CheckFromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckFromLists.append(obj)
        if params.get("VulTagList") is not None:
            self._VulTagList = []
            for item in params.get("VulTagList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VulTagList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskDetailRequest(AbstractModel):
    r"""DescribeVULRiskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _RiskId: 风险id
        :type RiskId: str
        :param _PCMGRId: pcMgrId
        :type PCMGRId: str
        """
        self._MemberId = None
        self._RiskId = None
        self._PCMGRId = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskId(self):
        r"""风险id
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def PCMGRId(self):
        r"""pcMgrId
        :rtype: str
        """
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._RiskId = params.get("RiskId")
        self._PCMGRId = params.get("PCMGRId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskDetailResponse(AbstractModel):
    r"""DescribeVULRiskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceSupport: 安全产品支持情况
        :type ServiceSupport: list of ServiceSupport
        :param _VulTrend: 漏洞趋势
        :type VulTrend: list of VulTrend
        :param _VulData: 漏洞补充信息
        :type VulData: :class:`tencentcloud.csip.v20221121.models.VULRiskInfo`
        :param _QuestionId: 小助手问答id
        :type QuestionId: str
        :param _SessionId: 会话id
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceSupport = None
        self._VulTrend = None
        self._VulData = None
        self._QuestionId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def ServiceSupport(self):
        r"""安全产品支持情况
        :rtype: list of ServiceSupport
        """
        return self._ServiceSupport

    @ServiceSupport.setter
    def ServiceSupport(self, ServiceSupport):
        self._ServiceSupport = ServiceSupport

    @property
    def VulTrend(self):
        r"""漏洞趋势
        :rtype: list of VulTrend
        """
        return self._VulTrend

    @VulTrend.setter
    def VulTrend(self, VulTrend):
        self._VulTrend = VulTrend

    @property
    def VulData(self):
        r"""漏洞补充信息
        :rtype: :class:`tencentcloud.csip.v20221121.models.VULRiskInfo`
        """
        return self._VulData

    @VulData.setter
    def VulData(self, VulData):
        self._VulData = VulData

    @property
    def QuestionId(self):
        r"""小助手问答id
        :rtype: str
        """
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def SessionId(self):
        r"""会话id
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        if params.get("ServiceSupport") is not None:
            self._ServiceSupport = []
            for item in params.get("ServiceSupport"):
                obj = ServiceSupport()
                obj._deserialize(item)
                self._ServiceSupport.append(obj)
        if params.get("VulTrend") is not None:
            self._VulTrend = []
            for item in params.get("VulTrend"):
                obj = VulTrend()
                obj._deserialize(item)
                self._VulTrend.append(obj)
        if params.get("VulData") is not None:
            self._VulData = VULRiskInfo()
            self._VulData._deserialize(params.get("VulData"))
        self._QuestionId = params.get("QuestionId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeVpcAssetsRequest(AbstractModel):
    r"""DescribeVpcAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤参数
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAssetsResponse(AbstractModel):
    r"""DescribeVpcAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: list of Vpc
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param _RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param _AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: list of Vpc
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
    def VpcList(self):
        r"""vpc列表
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        r"""地域列表
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""appid列表
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Vpc()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulRiskListRequest(AbstractModel):
    r"""DescribeVulRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filters: 过滤内容
        :type Filters: list of Filters
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Order: 排序类型
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _CloudAccountID: 云账号ID
        :type CloudAccountID: str
        :param _Provider: 云厂商
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._CloudAccountID = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""过滤内容
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序类型
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def CloudAccountID(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._CloudAccountID = params.get("CloudAccountID")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulRiskListResponse(AbstractModel):
    r"""DescribeVulRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 漏洞数量
        :type TotalCount: int
        :param _VulRiskList: 漏洞列表
        :type VulRiskList: list of VulRiskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VulRiskList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""漏洞数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VulRiskList(self):
        r"""漏洞列表
        :rtype: list of VulRiskItem
        """
        return self._VulRiskList

    @VulRiskList.setter
    def VulRiskList(self, VulRiskList):
        self._VulRiskList = VulRiskList

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
        if params.get("VulRiskList") is not None:
            self._VulRiskList = []
            for item in params.get("VulRiskList"):
                obj = VulRiskItem()
                obj._deserialize(item)
                self._VulRiskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulViewVulRiskListRequest(AbstractModel):
    r"""DescribeVulViewVulRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Filter: 过滤内容
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: 资产标签
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""过滤内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""资产标签
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulViewVulRiskListResponse(AbstractModel):
    r"""DescribeVulViewVulRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Data: 漏洞产视角的漏洞风险列表
        :type Data: list of VULViewVULRiskData
        :param _LevelLists: 危险等级列表
        :type LevelLists: list of FilterDataObject
        :param _FromLists: 来源列表
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: 漏洞类型列表
        :type VULTypeLists: list of FilterDataObject
        :param _Tags: tag枚举
        :type Tags: list of FilterDataObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""漏洞产视角的漏洞风险列表
        :rtype: list of VULViewVULRiskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""危险等级列表
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""来源列表
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""漏洞类型列表
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def Tags(self):
        r"""tag枚举
        :rtype: list of FilterDataObject
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRiskData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAssetVO(AbstractModel):
    r"""域名资产

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: list of str
        :param _AssetName: 资产名
        :type AssetName: list of str
        :param _AssetType: 资产类型
        :type AssetType: list of str
        :param _Region: 地域
        :type Region: list of str
        :param _WAFStatus: Waf状态
        :type WAFStatus: int
        :param _AssetCreateTime: 资产创建时间
        :type AssetCreateTime: str
        :param _AppId: Appid
        :type AppId: int
        :param _Uin: 账号id
        :type Uin: str
        :param _NickName: 账号名称
        :type NickName: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _IsCloud: 是否云上资产
        :type IsCloud: int
        :param _Attack: 网络攻击
        :type Attack: int
        :param _Access: 网络访问
        :type Access: int
        :param _Intercept: 网络拦截
        :type Intercept: int
        :param _InBandwidth: 入站峰值带宽
        :type InBandwidth: str
        :param _OutBandwidth: 出站峰值带宽
        :type OutBandwidth: str
        :param _InFlow: 入站累计流量
        :type InFlow: str
        :param _OutFlow: 出站累计流量
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _PortRisk: 端口风险
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
        :type ScanTask: int
        :param _SubDomain: 域名
        :type SubDomain: str
        :param _SeverIp: 解析ip
        :type SeverIp: list of str
        :param _BotCount: bot攻击数量
        :type BotCount: int
        :param _WeakPassword: 弱口令风险
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
        :type WebContentRisk: int
        :param _Tag: tag标签
        :type Tag: list of Tag
        :param _SourceType: 关联实例类型
        :type SourceType: str
        :param _MemberId: memberId信息
        :type MemberId: str
        :param _CCAttack: cc攻击
        :type CCAttack: int
        :param _WebAttack: web攻击
        :type WebAttack: int
        :param _ServiceRisk: 风险服务暴露数量
        :type ServiceRisk: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        :param _VerifyDomain: 待确认资产的随机三级域名
        :type VerifyDomain: str
        :param _VerifyTXTRecord: 待确认资产的TXT记录内容
        :type VerifyTXTRecord: str
        :param _VerifyStatus: 待确认资产的认证状态，0-待认证，1-认证成功，2-认证中，3-txt认证失败，4-人工认证失败
        :type VerifyStatus: int
        :param _BotAccessCount: bot访问数量
        :type BotAccessCount: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._WAFStatus = None
        self._AssetCreateTime = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._SubDomain = None
        self._SeverIp = None
        self._BotCount = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._SourceType = None
        self._MemberId = None
        self._CCAttack = None
        self._WebAttack = None
        self._ServiceRisk = None
        self._IsNewAsset = None
        self._VerifyDomain = None
        self._VerifyTXTRecord = None
        self._VerifyStatus = None
        self._BotAccessCount = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: list of str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: list of str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: list of str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""地域
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WAFStatus(self):
        r"""Waf状态
        :rtype: int
        """
        return self._WAFStatus

    @WAFStatus.setter
    def WAFStatus(self, WAFStatus):
        self._WAFStatus = WAFStatus

    @property
    def AssetCreateTime(self):
        r"""资产创建时间
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def AppId(self):
        r"""Appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""账号id
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""账号名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        r"""是否云上资产
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""网络访问
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""网络拦截
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""入站峰值带宽
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""出站峰值带宽
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""入站累计流量
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""出站累计流量
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        r"""端口风险
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""扫描任务
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def SubDomain(self):
        r"""域名
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def SeverIp(self):
        r"""解析ip
        :rtype: list of str
        """
        return self._SeverIp

    @SeverIp.setter
    def SeverIp(self, SeverIp):
        self._SeverIp = SeverIp

    @property
    def BotCount(self):
        r"""bot攻击数量
        :rtype: int
        """
        return self._BotCount

    @BotCount.setter
    def BotCount(self, BotCount):
        self._BotCount = BotCount

    @property
    def WeakPassword(self):
        r"""弱口令风险
        :rtype: int
        """
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        r"""内容风险
        :rtype: int
        """
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        r"""tag标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SourceType(self):
        r"""关联实例类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def MemberId(self):
        r"""memberId信息
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def CCAttack(self):
        r"""cc攻击
        :rtype: int
        """
        return self._CCAttack

    @CCAttack.setter
    def CCAttack(self, CCAttack):
        self._CCAttack = CCAttack

    @property
    def WebAttack(self):
        r"""web攻击
        :rtype: int
        """
        return self._WebAttack

    @WebAttack.setter
    def WebAttack(self, WebAttack):
        self._WebAttack = WebAttack

    @property
    def ServiceRisk(self):
        r"""风险服务暴露数量
        :rtype: int
        """
        return self._ServiceRisk

    @ServiceRisk.setter
    def ServiceRisk(self, ServiceRisk):
        self._ServiceRisk = ServiceRisk

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyDomain(self):
        r"""待确认资产的随机三级域名
        :rtype: str
        """
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyTXTRecord(self):
        r"""待确认资产的TXT记录内容
        :rtype: str
        """
        return self._VerifyTXTRecord

    @VerifyTXTRecord.setter
    def VerifyTXTRecord(self, VerifyTXTRecord):
        self._VerifyTXTRecord = VerifyTXTRecord

    @property
    def VerifyStatus(self):
        r"""待确认资产的认证状态，0-待认证，1-认证成功，2-认证中，3-txt认证失败，4-人工认证失败
        :rtype: int
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def BotAccessCount(self):
        r"""bot访问数量
        :rtype: int
        """
        return self._BotAccessCount

    @BotAccessCount.setter
    def BotAccessCount(self, BotAccessCount):
        self._BotAccessCount = BotAccessCount


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._WAFStatus = params.get("WAFStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._SubDomain = params.get("SubDomain")
        self._SeverIp = params.get("SeverIp")
        self._BotCount = params.get("BotCount")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._SourceType = params.get("SourceType")
        self._MemberId = params.get("MemberId")
        self._CCAttack = params.get("CCAttack")
        self._WebAttack = params.get("WebAttack")
        self._ServiceRisk = params.get("ServiceRisk")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyTXTRecord = params.get("VerifyTXTRecord")
        self._VerifyStatus = params.get("VerifyStatus")
        self._BotAccessCount = params.get("BotAccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Element(AbstractModel):
    r"""统计条目

    """

    def __init__(self):
        r"""
        :param _Key: 统计类型
        :type Key: str
        :param _Value: 统计对象
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""统计类型
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""统计对象
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
        


class ExposeAssetTypeItem(AbstractModel):
    r"""暴露资产分类

    """

    def __init__(self):
        r"""
        :param _Provider: 云厂商
        :type Provider: str
        :param _ProviderName: 云厂商名称
        :type ProviderName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _AssetTypeName: 资产类型名称
        :type AssetTypeName: str
        """
        self._Provider = None
        self._ProviderName = None
        self._AssetType = None
        self._AssetTypeName = None

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

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
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetTypeName(self):
        r"""资产类型名称
        :rtype: str
        """
        return self._AssetTypeName

    @AssetTypeName.setter
    def AssetTypeName(self, AssetTypeName):
        self._AssetTypeName = AssetTypeName


    def _deserialize(self, params):
        self._Provider = params.get("Provider")
        self._ProviderName = params.get("ProviderName")
        self._AssetType = params.get("AssetType")
        self._AssetTypeName = params.get("AssetTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposesItem(AbstractModel):
    r"""暴露资产

    """

    def __init__(self):
        r"""
        :param _Provider: 云厂商
        :type Provider: str
        :param _CloudAccountName: 云账号名称
        :type CloudAccountName: str
        :param _CloudAccountId: 云账号
        :type CloudAccountId: str
        :param _Domain: 域名
        :type Domain: str
        :param _Ip: IP
        :type Ip: str
        :param _Port: 端口或者端口范围
        :type Port: str
        :param _Status: 开放
        :type Status: str
        :param _RiskType: 风险类型
        :type RiskType: str
        :param _AclType: acl类型
        :type AclType: str
        :param _AclList: acl列表
        :type AclList: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PortServiceCount: 端口服务数量
        :type PortServiceCount: int
        :param _HighRiskPortServiceCount: 高危端口数量
        :type HighRiskPortServiceCount: int
        :param _WebAppCount: web应用数量
        :type WebAppCount: int
        :param _RiskWebAppCount: 有风险web应用数量
        :type RiskWebAppCount: int
        :param _WeakPasswordCount: 弱口令数量
        :type WeakPasswordCount: int
        :param _VulCount: 漏洞数量
        :type VulCount: int
        :param _CreateTime: 首次发现时间
        :type CreateTime: str
        :param _UpdateTime: 最近更新时间
        :type UpdateTime: str
        :param _AssetTypeName: 实例类型名称
        :type AssetTypeName: str
        :param _DisplayStatus: 开放状态
        :type DisplayStatus: str
        :param _DisplayRiskType: 端口状态
        :type DisplayRiskType: str
        :param _ScanTaskStatus: 扫描任务状态
        :type ScanTaskStatus: str
        :param _Uuid: uuid
        :type Uuid: str
        :param _HasScan: 是否进行过安全体检
        :type HasScan: str
        :param _AppId: 租户ID
        :type AppId: int
        :param _AppIdStr: 租户ID字符串
        :type AppIdStr: str
        :param _ExposureID: 记录ID
        :type ExposureID: int
        :param _PortDetectCount: 端口开放数量
        :type PortDetectCount: int
        :param _PortDetectResult: 端口开放结果
        :type PortDetectResult: str
        :param _Tag: 标签
        :type Tag: str
        :param _Comment: 备注
        :type Comment: str
        :param _ToGovernedRiskCount: 待治理风险数量
        :type ToGovernedRiskCount: int
        :param _ToGovernedRiskContent: 待治理风险内容
        :type ToGovernedRiskContent: str
        """
        self._Provider = None
        self._CloudAccountName = None
        self._CloudAccountId = None
        self._Domain = None
        self._Ip = None
        self._Port = None
        self._Status = None
        self._RiskType = None
        self._AclType = None
        self._AclList = None
        self._AssetId = None
        self._InstanceName = None
        self._AssetType = None
        self._PortServiceCount = None
        self._HighRiskPortServiceCount = None
        self._WebAppCount = None
        self._RiskWebAppCount = None
        self._WeakPasswordCount = None
        self._VulCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AssetTypeName = None
        self._DisplayStatus = None
        self._DisplayRiskType = None
        self._ScanTaskStatus = None
        self._Uuid = None
        self._HasScan = None
        self._AppId = None
        self._AppIdStr = None
        self._ExposureID = None
        self._PortDetectCount = None
        self._PortDetectResult = None
        self._Tag = None
        self._Comment = None
        self._ToGovernedRiskCount = None
        self._ToGovernedRiskContent = None

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

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
    def CloudAccountId(self):
        r"""云账号
        :rtype: str
        """
        return self._CloudAccountId

    @CloudAccountId.setter
    def CloudAccountId(self, CloudAccountId):
        self._CloudAccountId = CloudAccountId

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        r"""IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""端口或者端口范围
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        r"""开放
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskType(self):
        r"""风险类型
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def AclType(self):
        r"""acl类型
        :rtype: str
        """
        return self._AclType

    @AclType.setter
    def AclType(self, AclType):
        self._AclType = AclType

    @property
    def AclList(self):
        r"""acl列表
        :rtype: str
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def AssetId(self):
        r"""资产ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PortServiceCount(self):
        r"""端口服务数量
        :rtype: int
        """
        return self._PortServiceCount

    @PortServiceCount.setter
    def PortServiceCount(self, PortServiceCount):
        self._PortServiceCount = PortServiceCount

    @property
    def HighRiskPortServiceCount(self):
        r"""高危端口数量
        :rtype: int
        """
        return self._HighRiskPortServiceCount

    @HighRiskPortServiceCount.setter
    def HighRiskPortServiceCount(self, HighRiskPortServiceCount):
        self._HighRiskPortServiceCount = HighRiskPortServiceCount

    @property
    def WebAppCount(self):
        r"""web应用数量
        :rtype: int
        """
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def RiskWebAppCount(self):
        r"""有风险web应用数量
        :rtype: int
        """
        return self._RiskWebAppCount

    @RiskWebAppCount.setter
    def RiskWebAppCount(self, RiskWebAppCount):
        self._RiskWebAppCount = RiskWebAppCount

    @property
    def WeakPasswordCount(self):
        r"""弱口令数量
        :rtype: int
        """
        return self._WeakPasswordCount

    @WeakPasswordCount.setter
    def WeakPasswordCount(self, WeakPasswordCount):
        self._WeakPasswordCount = WeakPasswordCount

    @property
    def VulCount(self):
        r"""漏洞数量
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def CreateTime(self):
        r"""首次发现时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最近更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AssetTypeName(self):
        r"""实例类型名称
        :rtype: str
        """
        return self._AssetTypeName

    @AssetTypeName.setter
    def AssetTypeName(self, AssetTypeName):
        self._AssetTypeName = AssetTypeName

    @property
    def DisplayStatus(self):
        r"""开放状态
        :rtype: str
        """
        return self._DisplayStatus

    @DisplayStatus.setter
    def DisplayStatus(self, DisplayStatus):
        self._DisplayStatus = DisplayStatus

    @property
    def DisplayRiskType(self):
        r"""端口状态
        :rtype: str
        """
        return self._DisplayRiskType

    @DisplayRiskType.setter
    def DisplayRiskType(self, DisplayRiskType):
        self._DisplayRiskType = DisplayRiskType

    @property
    def ScanTaskStatus(self):
        r"""扫描任务状态
        :rtype: str
        """
        return self._ScanTaskStatus

    @ScanTaskStatus.setter
    def ScanTaskStatus(self, ScanTaskStatus):
        self._ScanTaskStatus = ScanTaskStatus

    @property
    def Uuid(self):
        r"""uuid
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def HasScan(self):
        r"""是否进行过安全体检
        :rtype: str
        """
        return self._HasScan

    @HasScan.setter
    def HasScan(self, HasScan):
        self._HasScan = HasScan

    @property
    def AppId(self):
        r"""租户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppIdStr(self):
        r"""租户ID字符串
        :rtype: str
        """
        return self._AppIdStr

    @AppIdStr.setter
    def AppIdStr(self, AppIdStr):
        self._AppIdStr = AppIdStr

    @property
    def ExposureID(self):
        r"""记录ID
        :rtype: int
        """
        return self._ExposureID

    @ExposureID.setter
    def ExposureID(self, ExposureID):
        self._ExposureID = ExposureID

    @property
    def PortDetectCount(self):
        r"""端口开放数量
        :rtype: int
        """
        return self._PortDetectCount

    @PortDetectCount.setter
    def PortDetectCount(self, PortDetectCount):
        self._PortDetectCount = PortDetectCount

    @property
    def PortDetectResult(self):
        r"""端口开放结果
        :rtype: str
        """
        return self._PortDetectResult

    @PortDetectResult.setter
    def PortDetectResult(self, PortDetectResult):
        self._PortDetectResult = PortDetectResult

    @property
    def Tag(self):
        r"""标签
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Comment(self):
        r"""备注
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def ToGovernedRiskCount(self):
        r"""待治理风险数量
        :rtype: int
        """
        return self._ToGovernedRiskCount

    @ToGovernedRiskCount.setter
    def ToGovernedRiskCount(self, ToGovernedRiskCount):
        self._ToGovernedRiskCount = ToGovernedRiskCount

    @property
    def ToGovernedRiskContent(self):
        r"""待治理风险内容
        :rtype: str
        """
        return self._ToGovernedRiskContent

    @ToGovernedRiskContent.setter
    def ToGovernedRiskContent(self, ToGovernedRiskContent):
        self._ToGovernedRiskContent = ToGovernedRiskContent


    def _deserialize(self, params):
        self._Provider = params.get("Provider")
        self._CloudAccountName = params.get("CloudAccountName")
        self._CloudAccountId = params.get("CloudAccountId")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._RiskType = params.get("RiskType")
        self._AclType = params.get("AclType")
        self._AclList = params.get("AclList")
        self._AssetId = params.get("AssetId")
        self._InstanceName = params.get("InstanceName")
        self._AssetType = params.get("AssetType")
        self._PortServiceCount = params.get("PortServiceCount")
        self._HighRiskPortServiceCount = params.get("HighRiskPortServiceCount")
        self._WebAppCount = params.get("WebAppCount")
        self._RiskWebAppCount = params.get("RiskWebAppCount")
        self._WeakPasswordCount = params.get("WeakPasswordCount")
        self._VulCount = params.get("VulCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AssetTypeName = params.get("AssetTypeName")
        self._DisplayStatus = params.get("DisplayStatus")
        self._DisplayRiskType = params.get("DisplayRiskType")
        self._ScanTaskStatus = params.get("ScanTaskStatus")
        self._Uuid = params.get("Uuid")
        self._HasScan = params.get("HasScan")
        self._AppId = params.get("AppId")
        self._AppIdStr = params.get("AppIdStr")
        self._ExposureID = params.get("ExposureID")
        self._PortDetectCount = params.get("PortDetectCount")
        self._PortDetectResult = params.get("PortDetectResult")
        self._Tag = params.get("Tag")
        self._Comment = params.get("Comment")
        self._ToGovernedRiskCount = params.get("ToGovernedRiskCount")
        self._ToGovernedRiskContent = params.get("ToGovernedRiskContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""列表查询接口采用新filter 接口，直接传给后台供后台查询过滤

    """

    def __init__(self):
        r"""
        :param _Limit: 查询数量限制
        :type Limit: int
        :param _Offset: 查询偏移位置
        :type Offset: int
        :param _Order: 排序采用升序还是降序 升:asc 降 desc
        :type Order: str
        :param _By: 需排序的字段
        :type By: str
        :param _Filters: 过滤的列及内容
        :type Filters: list of WhereFilter
        :param _StartTime: 可填无， 日志使用查询时间
        :type StartTime: str
        :param _EndTime: 可填无， 日志使用查询时间
        :type EndTime: str
        """
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Limit(self):
        r"""查询数量限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""查询偏移位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序采用升序还是降序 升:asc 降 desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""需排序的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Filters(self):
        r"""过滤的列及内容
        :rtype: list of WhereFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        r"""可填无， 日志使用查询时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""可填无， 日志使用查询时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterDataObject(AbstractModel):
    r"""过滤数据对象

    """

    def __init__(self):
        r"""
        :param _Value: 英文翻译
        :type Value: str
        :param _Text: 中文翻译
        :type Text: str
        """
        self._Value = None
        self._Text = None

    @property
    def Value(self):
        r"""英文翻译
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Text(self):
        r"""中文翻译
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    r"""filter过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Values: 实例ID内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param _ExactMatch: 模糊匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type ExactMatch: str
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""实例ID内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        r"""模糊匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GateWayAsset(AbstractModel):
    r"""网关资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PrivateIp: 私有ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: 出向峰值带宽
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: 入向峰值带宽
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: 出站累计流量
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: 入站累计流量
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: 网络攻击
        :type NetworkAttack: int
        :param _ExposedPort: 暴露端口
        :type ExposedPort: int
        :param _ExposedVUL: 暴露漏洞
        :type ExposedVUL: int
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _Nick: 昵称
        :type Nick: str
        :param _AddressIPV6: ipv6地址
        :type AddressIPV6: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _RiskExposure: 风险服务暴露
        :type RiskExposure: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        :param _Status: 网关状态
        :type Status: str
        :param _EngineRegion: TSE的网关真实地域
        :type EngineRegion: str
        :param _WeakPasswordRisk: 弱口令风险
        :type WeakPasswordRisk: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._AddressIPV6 = None
        self._IsCore = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._Status = None
        self._EngineRegion = None
        self._WeakPasswordRisk = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""资产ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        r"""私有ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""私有网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""私有网络名
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        r"""出向峰值带宽
        :rtype: str
        """
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        r"""入向峰值带宽
        :rtype: str
        """
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        r"""出站累计流量
        :rtype: str
        """
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        r"""入站累计流量
        :rtype: str
        """
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        r"""暴露端口
        :rtype: int
        """
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        r"""暴露漏洞
        :rtype: int
        """
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ScanTask(self):
        r"""任务数
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""最后扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        r"""昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AddressIPV6(self):
        r"""ipv6地址
        :rtype: str
        """
        return self._AddressIPV6

    @AddressIPV6.setter
    def AddressIPV6(self, AddressIPV6):
        self._AddressIPV6 = AddressIPV6

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def RiskExposure(self):
        r"""风险服务暴露
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def Status(self):
        r"""网关状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineRegion(self):
        r"""TSE的网关真实地域
        :rtype: str
        """
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def WeakPasswordRisk(self):
        r"""弱口令风险
        :rtype: int
        """
        return self._WeakPasswordRisk

    @WeakPasswordRisk.setter
    def WeakPasswordRisk(self, WeakPasswordRisk):
        self._WeakPasswordRisk = WeakPasswordRisk


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._AddressIPV6 = params.get("AddressIPV6")
        self._IsCore = params.get("IsCore")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._Status = params.get("Status")
        self._EngineRegion = params.get("EngineRegion")
        self._WeakPasswordRisk = params.get("WeakPasswordRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighBaseLineRiskItem(AbstractModel):
    r"""高危基线风险内容

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: 云账号ID
        :type CloudAccountID: str
        :param _AssetID: 实例ID
        :type AssetID: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _RiskName: 风险名称
        :type RiskName: str
        :param _RiskCategory: 风险分类
        :type RiskCategory: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _RiskDesc: 风险描述
        :type RiskDesc: str
        :param _RiskResult: 风险结果
        :type RiskResult: str
        :param _FixAdvice: 修复建议
        :type FixAdvice: str
        :param _RiskCategoryName: Linux漏洞
        :type RiskCategoryName: str
        :param _RiskLevelName: 风险等级名称
        :type RiskLevelName: str
        :param _InstanceStatusName: 实例状态
        :type InstanceStatusName: str
        :param _CreateTime: 首次发现时间
        :type CreateTime: str
        :param _UpdateTime: 最近发现时间
        :type UpdateTime: str
        :param _AppID: 租户ID
        :type AppID: int
        """
        self._CloudAccountID = None
        self._AssetID = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._RiskName = None
        self._RiskCategory = None
        self._RiskLevel = None
        self._RiskDesc = None
        self._RiskResult = None
        self._FixAdvice = None
        self._RiskCategoryName = None
        self._RiskLevelName = None
        self._InstanceStatusName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppID = None

    @property
    def CloudAccountID(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def AssetID(self):
        r"""实例ID
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID

    @property
    def InstanceStatus(self):
        r"""实例状态
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RiskName(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskCategory(self):
        r"""风险分类
        :rtype: str
        """
        return self._RiskCategory

    @RiskCategory.setter
    def RiskCategory(self, RiskCategory):
        self._RiskCategory = RiskCategory

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskDesc(self):
        r"""风险描述
        :rtype: str
        """
        return self._RiskDesc

    @RiskDesc.setter
    def RiskDesc(self, RiskDesc):
        self._RiskDesc = RiskDesc

    @property
    def RiskResult(self):
        r"""风险结果
        :rtype: str
        """
        return self._RiskResult

    @RiskResult.setter
    def RiskResult(self, RiskResult):
        self._RiskResult = RiskResult

    @property
    def FixAdvice(self):
        r"""修复建议
        :rtype: str
        """
        return self._FixAdvice

    @FixAdvice.setter
    def FixAdvice(self, FixAdvice):
        self._FixAdvice = FixAdvice

    @property
    def RiskCategoryName(self):
        r"""Linux漏洞
        :rtype: str
        """
        return self._RiskCategoryName

    @RiskCategoryName.setter
    def RiskCategoryName(self, RiskCategoryName):
        self._RiskCategoryName = RiskCategoryName

    @property
    def RiskLevelName(self):
        r"""风险等级名称
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def InstanceStatusName(self):
        r"""实例状态
        :rtype: str
        """
        return self._InstanceStatusName

    @InstanceStatusName.setter
    def InstanceStatusName(self, InstanceStatusName):
        self._InstanceStatusName = InstanceStatusName

    @property
    def CreateTime(self):
        r"""首次发现时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最近发现时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppID(self):
        r"""租户ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._AssetID = params.get("AssetID")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._RiskName = params.get("RiskName")
        self._RiskCategory = params.get("RiskCategory")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskDesc = params.get("RiskDesc")
        self._RiskResult = params.get("RiskResult")
        self._FixAdvice = params.get("FixAdvice")
        self._RiskCategoryName = params.get("RiskCategoryName")
        self._RiskLevelName = params.get("RiskLevelName")
        self._InstanceStatusName = params.get("InstanceStatusName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppID = params.get("AppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAssetListVO(AbstractModel):
    r"""ip列表

    """

    def __init__(self):
        r"""
        :param _AssetId: 资产id
        :type AssetId: str
        :param _AssetName: 资产name
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Region: 地域
        :type Region: str
        :param _CFWStatus: 云防状态
        :type CFWStatus: int
        :param _AssetCreateTime: 资产创建时间
        :type AssetCreateTime: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _PublicIpType: 公网ip类型
        :type PublicIpType: int
        :param _VpcId: vpc
        :type VpcId: str
        :param _VpcName: vpc名
        :type VpcName: str
        :param _AppId: appid
        :type AppId: int
        :param _Uin: 用户uin
        :type Uin: str
        :param _NickName: 名称
        :type NickName: str
        :param _IsCore: 核心
        :type IsCore: int
        :param _IsCloud: 云上
        :type IsCloud: int
        :param _Attack: 网络攻击
        :type Attack: int
        :param _Access: 网络访问
        :type Access: int
        :param _Intercept: 网络拦截
        :type Intercept: int
        :param _InBandwidth: 入向带宽
        :type InBandwidth: str
        :param _OutBandwidth: 出向带宽
        :type OutBandwidth: str
        :param _InFlow: 入向流量
        :type InFlow: str
        :param _OutFlow: 出向流量
        :type OutFlow: str
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _PortRisk: 端口风险
        :type PortRisk: int
        :param _VulnerabilityRisk: 漏洞风险
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: 配置风险
        :type ConfigurationRisk: int
        :param _ScanTask: 扫描任务
        :type ScanTask: int
        :param _WeakPassword: 弱口令
        :type WeakPassword: int
        :param _WebContentRisk: 内容风险
        :type WebContentRisk: int
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _AddressId: eip主键
        :type AddressId: str
        :param _MemberId: MemberId信息
        :type MemberId: str
        :param _RiskExposure: 风险服务暴露
        :type RiskExposure: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        :param _VerifyStatus: 资产认证状态，0-待认证，1-认证成功，2-认证中，3+-认证失败
        :type VerifyStatus: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CFWStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PublicIpType = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._AddressId = None
        self._MemberId = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._VerifyStatus = None

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产name
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CFWStatus(self):
        r"""云防状态
        :rtype: int
        """
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetCreateTime(self):
        r"""资产创建时间
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

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
    def PublicIpType(self):
        r"""公网ip类型
        :rtype: int
        """
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def VpcId(self):
        r"""vpc
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc名
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        r"""appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        r"""核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        r"""云上
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""网络访问
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""网络拦截
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""入向带宽
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""出向带宽
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""入向流量
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""出向流量
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        r"""端口风险
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""扫描任务
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def WeakPassword(self):
        r"""弱口令
        :rtype: int
        """
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        r"""内容风险
        :rtype: int
        """
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AddressId(self):
        r"""eip主键
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def MemberId(self):
        r"""MemberId信息
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskExposure(self):
        r"""风险服务暴露
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyStatus(self):
        r"""资产认证状态，0-待认证，1-认证成功，2-认证中，3+-认证失败
        :rtype: int
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CFWStatus = params.get("CFWStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PublicIpType = params.get("PublicIpType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._AddressId = params.get("AddressId")
        self._MemberId = params.get("MemberId")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyStatus = params.get("VerifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    r"""KeyValue对

    """

    def __init__(self):
        r"""
        :param _Key: 字段
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""字段
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
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
        


class ModifyOrganizationAccountStatusRequest(AbstractModel):
    r"""ModifyOrganizationAccountStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 修改集团账号状态，1 开启， 2关闭
        :type Status: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._Status = None
        self._MemberId = None

    @property
    def Status(self):
        r"""修改集团账号状态，1 开启， 2关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationAccountStatusResponse(AbstractModel):
    r"""ModifyOrganizationAccountStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回值为0，则修改成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""返回值为0，则修改成功
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyRiskCenterRiskStatusRequest(AbstractModel):
    r"""ModifyRiskCenterRiskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskStatusKeys: 风险资产相关数据
        :type RiskStatusKeys: list of RiskCenterStatusKey
        :param _Status: 处置状态，1为已处置、2为已忽略，3为取消已处置，4为取消已忽略
        :type Status: int
        :param _Type: 风险类型，0-端口风险， 1-漏洞风险，2-弱口令风险， 3-网站内容风险，4-配置风险，5-风险服务暴露
        :type Type: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._RiskStatusKeys = None
        self._Status = None
        self._Type = None
        self._MemberId = None

    @property
    def RiskStatusKeys(self):
        r"""风险资产相关数据
        :rtype: list of RiskCenterStatusKey
        """
        return self._RiskStatusKeys

    @RiskStatusKeys.setter
    def RiskStatusKeys(self, RiskStatusKeys):
        self._RiskStatusKeys = RiskStatusKeys

    @property
    def Status(self):
        r"""处置状态，1为已处置、2为已忽略，3为取消已处置，4为取消已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""风险类型，0-端口风险， 1-漏洞风险，2-弱口令风险， 3-网站内容风险，4-配置风险，5-风险服务暴露
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("RiskStatusKeys") is not None:
            self._RiskStatusKeys = []
            for item in params.get("RiskStatusKeys"):
                obj = RiskCenterStatusKey()
                obj._deserialize(item)
                self._RiskStatusKeys.append(obj)
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterRiskStatusResponse(AbstractModel):
    r"""ModifyRiskCenterRiskStatus返回参数结构体

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


class ModifyRiskCenterScanTaskRequest(AbstractModel):
    r"""ModifyRiskCenterScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :type ScanAssetType: int
        :param _ScanItem: 扫描项目；port/poc/weakpass/webcontent/configrisk
        :type ScanItem: list of str
        :param _ScanPlanType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :type ScanPlanType: int
        :param _TaskId: 要修改的任务id
        :type TaskId: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _Assets: 扫描资产信息列表
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: 扫描计划详情
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: ip/域名/url数组
        :type SelfDefiningAssets: list of str
        :param _TaskAdvanceCFG: 高级配置
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :type TaskMode: int
        :param _FinishWebHook: 任务完成回调webhook地址
        :type FinishWebHook: str
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._TaskId = None
        self._MemberId = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._FinishWebHook = None

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
    def ScanAssetType(self):
        r"""0-全扫，1-指定资产扫，2-排除资产扫，3-手动填写扫；1和2则Assets字段必填，3则SelfDefiningAssets必填
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        r"""扫描项目；port/poc/weakpass/webcontent/configrisk
        :rtype: list of str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        r"""0-周期任务,1-立即扫描,2-定时扫描,3-自定义；0,2,3则ScanPlanContent必填
        :rtype: int
        """
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def TaskId(self):
        r"""要修改的任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Assets(self):
        r"""扫描资产信息列表
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        r"""扫描计划详情
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        r"""ip/域名/url数组
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def TaskAdvanceCFG(self):
        r"""高级配置
        :rtype: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        """
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        r"""体检模式，0-标准模式，1-快速模式，2-高级模式，默认标准模式
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def FinishWebHook(self):
        r"""任务完成回调webhook地址
        :rtype: str
        """
        return self._FinishWebHook

    @FinishWebHook.setter
    def FinishWebHook(self, FinishWebHook):
        self._FinishWebHook = FinishWebHook


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        self._TaskId = params.get("TaskId")
        self._MemberId = params.get("MemberId")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        self._FinishWebHook = params.get("FinishWebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterScanTaskResponse(AbstractModel):
    r"""ModifyRiskCenterScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Status: 0，修改成功，其他失败；-1为存在资产未认证
        :type Status: int
        :param _UnAuthAsset: 未认证资产列表
        :type UnAuthAsset: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""0，修改成功，其他失败；-1为存在资产未认证
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        r"""未认证资产列表
        :rtype: list of str
        """
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

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
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class ModifyUebaRuleSwitchRequest(AbstractModel):
    r"""ModifyUebaRuleSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleID: 策略ID
        :type RuleID: str
        :param _Status: 开关状态
        :type Status: bool
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._RuleID = None
        self._Status = None
        self._MemberId = None

    @property
    def RuleID(self):
        r"""策略ID
        :rtype: str
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Status(self):
        r"""开关状态
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._Status = params.get("Status")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUebaRuleSwitchResponse(AbstractModel):
    r"""ModifyUebaRuleSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 0成功，1失败
        :type Code: int
        :param _Msg: 返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0成功，1失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""返回信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class NICAsset(AbstractModel):
    r"""网卡资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _PrivateIp: 私有ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: 出向峰值带宽
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: 入向峰值带宽
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: 出站累计流量
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: 入站累计流量
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: 网络攻击
        :type NetworkAttack: int
        :param _ExposedPort: 暴露端口
        :type ExposedPort: int
        :param _ExposedVUL: 暴露漏洞
        :type ExposedVUL: int
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _Nick: 昵称
        :type Nick: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""资产ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        r"""私有ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""私有网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""私有网络名
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        r"""出向峰值带宽
        :rtype: str
        """
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        r"""入向峰值带宽
        :rtype: str
        """
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        r"""出站累计流量
        :rtype: str
        """
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        r"""入站累计流量
        :rtype: str
        """
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        r"""网络攻击
        :rtype: int
        """
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        r"""暴露端口
        :rtype: int
        """
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        r"""暴露漏洞
        :rtype: int
        """
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ScanTask(self):
        r"""任务数
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""最后扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        r"""昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAlertKey(AbstractModel):
    r"""该结构体用来传入告警的key，以更新告警的status

    """

    def __init__(self):
        r"""
        :param _AppId: 需要更改的用户appid
        :type AppId: str
        :param _Type: 告警类别
        :type Type: str
        :param _SubType: 告警子类别
        :type SubType: str
        :param _Source: 告警来源
        :type Source: str
        :param _Name: 告警名称
        :type Name: str
        :param _Key: 告警key
        :type Key: str
        :param _Date: 时间
        :type Date: str
        :param _Status: 状态
        :type Status: int
        """
        self._AppId = None
        self._Type = None
        self._SubType = None
        self._Source = None
        self._Name = None
        self._Key = None
        self._Date = None
        self._Status = None

    @property
    def AppId(self):
        r"""需要更改的用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Type(self):
        r"""告警类别
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubType(self):
        r"""告警子类别
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def Source(self):
        r"""告警来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        r"""告警名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        r"""告警key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Date(self):
        r"""时间
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Type = params.get("Type")
        self._SubType = params.get("SubType")
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Date = params.get("Date")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationInfo(AbstractModel):
    r"""集团账号详情

    """

    def __init__(self):
        r"""
        :param _NickName: 成员账号名称
        :type NickName: str
        :param _NodeName: 部门节点名称，账号所属部门
        :type NodeName: str
        :param _Role: Member/Admin/DelegatedAdmin/EntityAdmin; 成员/管理员/委派管理员/主体管理员
        :type Role: str
        :param _MemberId: 成员账号id
        :type MemberId: str
        :param _JoinType: 账号加入方式,create/invite
        :type JoinType: str
        :param _GroupName: 集团名称
        :type GroupName: str
        :param _AdminName: 管理员账号名称
        :type AdminName: str
        :param _AdminUin: 管理员Uin
        :type AdminUin: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _NodeCount: 部门数
        :type NodeCount: int
        :param _MemberCount: 成员数
        :type MemberCount: int
        :param _SubAccountCount: 子账号数
        :type SubAccountCount: int
        :param _AbnormalSubUserCount: 异常子账号数量
        :type AbnormalSubUserCount: int
        :param _GroupPermission: 集团关系策略权限
        :type GroupPermission: list of str
        :param _MemberPermission: 成员关系策略权限
        :type MemberPermission: list of str
        :param _GroupPayMode: 集团付费模式；0/自付费，1/代付费
        :type GroupPayMode: int
        :param _MemberPayMode: 个人付费模式；0/自付费，1/代付费
        :type MemberPayMode: int
        :param _CFWProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type CFWProtect: str
        :param _WAFProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type WAFProtect: str
        :param _CWPProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type CWPProtect: str
        :param _Departments: 所有部门的集合数组
        :type Departments: list of str
        :param _MemberCreateTime: 成员创建时间
        :type MemberCreateTime: str
        :param _CSIPProtect: Advanced/Enterprise/Ultimate 
        :type CSIPProtect: str
        :param _QuotaConsumer: 1表示配额消耗方
        :type QuotaConsumer: int
        :param _EnableAdminCount: 管理员/委派管理员 已开启数量
        :type EnableAdminCount: int
        :param _CloudCountDesc: 账户多云信息统计，数组形式，具体参考CloudCountDesc描述
        :type CloudCountDesc: list of CloudCountDesc
        :param _AdminCount: 管理员/委派管理员 总数量
        :type AdminCount: int
        """
        self._NickName = None
        self._NodeName = None
        self._Role = None
        self._MemberId = None
        self._JoinType = None
        self._GroupName = None
        self._AdminName = None
        self._AdminUin = None
        self._CreateTime = None
        self._NodeCount = None
        self._MemberCount = None
        self._SubAccountCount = None
        self._AbnormalSubUserCount = None
        self._GroupPermission = None
        self._MemberPermission = None
        self._GroupPayMode = None
        self._MemberPayMode = None
        self._CFWProtect = None
        self._WAFProtect = None
        self._CWPProtect = None
        self._Departments = None
        self._MemberCreateTime = None
        self._CSIPProtect = None
        self._QuotaConsumer = None
        self._EnableAdminCount = None
        self._CloudCountDesc = None
        self._AdminCount = None

    @property
    def NickName(self):
        r"""成员账号名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def NodeName(self):
        r"""部门节点名称，账号所属部门
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Role(self):
        r"""Member/Admin/DelegatedAdmin/EntityAdmin; 成员/管理员/委派管理员/主体管理员
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def MemberId(self):
        r"""成员账号id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def JoinType(self):
        r"""账号加入方式,create/invite
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def GroupName(self):
        r"""集团名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def AdminName(self):
        r"""管理员账号名称
        :rtype: str
        """
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminUin(self):
        r"""管理员Uin
        :rtype: str
        """
        return self._AdminUin

    @AdminUin.setter
    def AdminUin(self, AdminUin):
        self._AdminUin = AdminUin

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NodeCount(self):
        r"""部门数
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def MemberCount(self):
        r"""成员数
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def SubAccountCount(self):
        r"""子账号数
        :rtype: int
        """
        return self._SubAccountCount

    @SubAccountCount.setter
    def SubAccountCount(self, SubAccountCount):
        self._SubAccountCount = SubAccountCount

    @property
    def AbnormalSubUserCount(self):
        r"""异常子账号数量
        :rtype: int
        """
        return self._AbnormalSubUserCount

    @AbnormalSubUserCount.setter
    def AbnormalSubUserCount(self, AbnormalSubUserCount):
        self._AbnormalSubUserCount = AbnormalSubUserCount

    @property
    def GroupPermission(self):
        r"""集团关系策略权限
        :rtype: list of str
        """
        return self._GroupPermission

    @GroupPermission.setter
    def GroupPermission(self, GroupPermission):
        self._GroupPermission = GroupPermission

    @property
    def MemberPermission(self):
        r"""成员关系策略权限
        :rtype: list of str
        """
        return self._MemberPermission

    @MemberPermission.setter
    def MemberPermission(self, MemberPermission):
        self._MemberPermission = MemberPermission

    @property
    def GroupPayMode(self):
        r"""集团付费模式；0/自付费，1/代付费
        :rtype: int
        """
        return self._GroupPayMode

    @GroupPayMode.setter
    def GroupPayMode(self, GroupPayMode):
        self._GroupPayMode = GroupPayMode

    @property
    def MemberPayMode(self):
        r"""个人付费模式；0/自付费，1/代付费
        :rtype: int
        """
        return self._MemberPayMode

    @MemberPayMode.setter
    def MemberPayMode(self, MemberPayMode):
        self._MemberPayMode = MemberPayMode

    @property
    def CFWProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._CFWProtect

    @CFWProtect.setter
    def CFWProtect(self, CFWProtect):
        self._CFWProtect = CFWProtect

    @property
    def WAFProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._WAFProtect

    @WAFProtect.setter
    def WAFProtect(self, WAFProtect):
        self._WAFProtect = WAFProtect

    @property
    def CWPProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._CWPProtect

    @CWPProtect.setter
    def CWPProtect(self, CWPProtect):
        self._CWPProtect = CWPProtect

    @property
    def Departments(self):
        r"""所有部门的集合数组
        :rtype: list of str
        """
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments

    @property
    def MemberCreateTime(self):
        r"""成员创建时间
        :rtype: str
        """
        return self._MemberCreateTime

    @MemberCreateTime.setter
    def MemberCreateTime(self, MemberCreateTime):
        self._MemberCreateTime = MemberCreateTime

    @property
    def CSIPProtect(self):
        r"""Advanced/Enterprise/Ultimate 
        :rtype: str
        """
        return self._CSIPProtect

    @CSIPProtect.setter
    def CSIPProtect(self, CSIPProtect):
        self._CSIPProtect = CSIPProtect

    @property
    def QuotaConsumer(self):
        r"""1表示配额消耗方
        :rtype: int
        """
        return self._QuotaConsumer

    @QuotaConsumer.setter
    def QuotaConsumer(self, QuotaConsumer):
        self._QuotaConsumer = QuotaConsumer

    @property
    def EnableAdminCount(self):
        r"""管理员/委派管理员 已开启数量
        :rtype: int
        """
        return self._EnableAdminCount

    @EnableAdminCount.setter
    def EnableAdminCount(self, EnableAdminCount):
        self._EnableAdminCount = EnableAdminCount

    @property
    def CloudCountDesc(self):
        r"""账户多云信息统计，数组形式，具体参考CloudCountDesc描述
        :rtype: list of CloudCountDesc
        """
        return self._CloudCountDesc

    @CloudCountDesc.setter
    def CloudCountDesc(self, CloudCountDesc):
        self._CloudCountDesc = CloudCountDesc

    @property
    def AdminCount(self):
        r"""管理员/委派管理员 总数量
        :rtype: int
        """
        return self._AdminCount

    @AdminCount.setter
    def AdminCount(self, AdminCount):
        self._AdminCount = AdminCount


    def _deserialize(self, params):
        self._NickName = params.get("NickName")
        self._NodeName = params.get("NodeName")
        self._Role = params.get("Role")
        self._MemberId = params.get("MemberId")
        self._JoinType = params.get("JoinType")
        self._GroupName = params.get("GroupName")
        self._AdminName = params.get("AdminName")
        self._AdminUin = params.get("AdminUin")
        self._CreateTime = params.get("CreateTime")
        self._NodeCount = params.get("NodeCount")
        self._MemberCount = params.get("MemberCount")
        self._SubAccountCount = params.get("SubAccountCount")
        self._AbnormalSubUserCount = params.get("AbnormalSubUserCount")
        self._GroupPermission = params.get("GroupPermission")
        self._MemberPermission = params.get("MemberPermission")
        self._GroupPayMode = params.get("GroupPayMode")
        self._MemberPayMode = params.get("MemberPayMode")
        self._CFWProtect = params.get("CFWProtect")
        self._WAFProtect = params.get("WAFProtect")
        self._CWPProtect = params.get("CWPProtect")
        self._Departments = params.get("Departments")
        self._MemberCreateTime = params.get("MemberCreateTime")
        self._CSIPProtect = params.get("CSIPProtect")
        self._QuotaConsumer = params.get("QuotaConsumer")
        self._EnableAdminCount = params.get("EnableAdminCount")
        if params.get("CloudCountDesc") is not None:
            self._CloudCountDesc = []
            for item in params.get("CloudCountDesc"):
                obj = CloudCountDesc()
                obj._deserialize(item)
                self._CloudCountDesc.append(obj)
        self._AdminCount = params.get("AdminCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationUserInfo(AbstractModel):
    r"""集团账号成员详情

    """

    def __init__(self):
        r"""
        :param _Uin: 成员账号Uin
        :type Uin: str
        :param _NickName: 成员账号名称
        :type NickName: str
        :param _NodeName: 部门节点名称，账号所属部门
        :type NodeName: str
        :param _AssetCount: 资产数量
        :type AssetCount: int
        :param _RiskCount: 风险数量
        :type RiskCount: int
        :param _AttackCount: 攻击数量
        :type AttackCount: int
        :param _Role: Member/Admin/;成员或者管理员
        :type Role: str
        :param _MemberId: 成员账号id
        :type MemberId: str
        :param _AppId: 成员账号Appid
        :type AppId: str
        :param _JoinType: 账号加入方式,create/invite
        :type JoinType: str
        :param _CFWProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type CFWProtect: str
        :param _WAFProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type WAFProtect: str
        :param _CWPProtect: 空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :type CWPProtect: str
        :param _Enable: 1启用，0未启用
        :type Enable: int
        :param _CSIPProtect: "Free"       //免费版  "Advanced"   //高级版 "Enterprise" //企业版 "Ultimate"   //旗舰版
        :type CSIPProtect: str
        :param _QuotaConsumer: 1为配额消耗者
        :type QuotaConsumer: int
        :param _CloudType: 账户类型，0为腾讯云账户，1为AWS账户
        :type CloudType: int
        :param _SyncFrequency: 0为缺省值，1为10分钟，2为1小时，3为24小时
        :type SyncFrequency: int
        :param _IsExpired: 多云账户是否过期
        :type IsExpired: bool
        :param _PermissionList: 多云账户 权限列表
        :type PermissionList: list of str
        :param _AuthType: 1
        :type AuthType: int
        :param _TcMemberType: 0 腾讯云集团账户
1 腾讯云接入账户
2 非腾讯云
        :type TcMemberType: int
        :param _SubUserCount: 子账号数量
        :type SubUserCount: int
        :param _JoinTypeInfo: 加入方式详细信息
        :type JoinTypeInfo: str
        """
        self._Uin = None
        self._NickName = None
        self._NodeName = None
        self._AssetCount = None
        self._RiskCount = None
        self._AttackCount = None
        self._Role = None
        self._MemberId = None
        self._AppId = None
        self._JoinType = None
        self._CFWProtect = None
        self._WAFProtect = None
        self._CWPProtect = None
        self._Enable = None
        self._CSIPProtect = None
        self._QuotaConsumer = None
        self._CloudType = None
        self._SyncFrequency = None
        self._IsExpired = None
        self._PermissionList = None
        self._AuthType = None
        self._TcMemberType = None
        self._SubUserCount = None
        self._JoinTypeInfo = None

    @property
    def Uin(self):
        r"""成员账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""成员账号名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def NodeName(self):
        r"""部门节点名称，账号所属部门
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def AssetCount(self):
        r"""资产数量
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def RiskCount(self):
        r"""风险数量
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AttackCount(self):
        r"""攻击数量
        :rtype: int
        """
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Role(self):
        r"""Member/Admin/;成员或者管理员
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def MemberId(self):
        r"""成员账号id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AppId(self):
        r"""成员账号Appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def JoinType(self):
        r"""账号加入方式,create/invite
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def CFWProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._CFWProtect

    @CFWProtect.setter
    def CFWProtect(self, CFWProtect):
        self._CFWProtect = CFWProtect

    @property
    def WAFProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._WAFProtect

    @WAFProtect.setter
    def WAFProtect(self, WAFProtect):
        self._WAFProtect = WAFProtect

    @property
    def CWPProtect(self):
        r"""空则未开启，否则不同字符串对应不同版本，common为通用，不区分版本
        :rtype: str
        """
        return self._CWPProtect

    @CWPProtect.setter
    def CWPProtect(self, CWPProtect):
        self._CWPProtect = CWPProtect

    @property
    def Enable(self):
        r"""1启用，0未启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CSIPProtect(self):
        r""""Free"       //免费版  "Advanced"   //高级版 "Enterprise" //企业版 "Ultimate"   //旗舰版
        :rtype: str
        """
        return self._CSIPProtect

    @CSIPProtect.setter
    def CSIPProtect(self, CSIPProtect):
        self._CSIPProtect = CSIPProtect

    @property
    def QuotaConsumer(self):
        r"""1为配额消耗者
        :rtype: int
        """
        return self._QuotaConsumer

    @QuotaConsumer.setter
    def QuotaConsumer(self, QuotaConsumer):
        self._QuotaConsumer = QuotaConsumer

    @property
    def CloudType(self):
        r"""账户类型，0为腾讯云账户，1为AWS账户
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def SyncFrequency(self):
        r"""0为缺省值，1为10分钟，2为1小时，3为24小时
        :rtype: int
        """
        return self._SyncFrequency

    @SyncFrequency.setter
    def SyncFrequency(self, SyncFrequency):
        self._SyncFrequency = SyncFrequency

    @property
    def IsExpired(self):
        r"""多云账户是否过期
        :rtype: bool
        """
        return self._IsExpired

    @IsExpired.setter
    def IsExpired(self, IsExpired):
        self._IsExpired = IsExpired

    @property
    def PermissionList(self):
        r"""多云账户 权限列表
        :rtype: list of str
        """
        return self._PermissionList

    @PermissionList.setter
    def PermissionList(self, PermissionList):
        self._PermissionList = PermissionList

    @property
    def AuthType(self):
        r"""1
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def TcMemberType(self):
        r"""0 腾讯云集团账户
1 腾讯云接入账户
2 非腾讯云
        :rtype: int
        """
        return self._TcMemberType

    @TcMemberType.setter
    def TcMemberType(self, TcMemberType):
        self._TcMemberType = TcMemberType

    @property
    def SubUserCount(self):
        r"""子账号数量
        :rtype: int
        """
        return self._SubUserCount

    @SubUserCount.setter
    def SubUserCount(self, SubUserCount):
        self._SubUserCount = SubUserCount

    @property
    def JoinTypeInfo(self):
        r"""加入方式详细信息
        :rtype: str
        """
        return self._JoinTypeInfo

    @JoinTypeInfo.setter
    def JoinTypeInfo(self, JoinTypeInfo):
        self._JoinTypeInfo = JoinTypeInfo


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._NodeName = params.get("NodeName")
        self._AssetCount = params.get("AssetCount")
        self._RiskCount = params.get("RiskCount")
        self._AttackCount = params.get("AttackCount")
        self._Role = params.get("Role")
        self._MemberId = params.get("MemberId")
        self._AppId = params.get("AppId")
        self._JoinType = params.get("JoinType")
        self._CFWProtect = params.get("CFWProtect")
        self._WAFProtect = params.get("WAFProtect")
        self._CWPProtect = params.get("CWPProtect")
        self._Enable = params.get("Enable")
        self._CSIPProtect = params.get("CSIPProtect")
        self._QuotaConsumer = params.get("QuotaConsumer")
        self._CloudType = params.get("CloudType")
        self._SyncFrequency = params.get("SyncFrequency")
        self._IsExpired = params.get("IsExpired")
        self._PermissionList = params.get("PermissionList")
        self._AuthType = params.get("AuthType")
        self._TcMemberType = params.get("TcMemberType")
        self._SubUserCount = params.get("SubUserCount")
        self._JoinTypeInfo = params.get("JoinTypeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRiskAdvanceCFGParamItem(AbstractModel):
    r"""端口风险高级配置项

    """

    def __init__(self):
        r"""
        :param _PortSets: 端口集合,以逗号分隔
        :type PortSets: str
        :param _CheckType: 检测项类型，0-系统定义，1-用户自定义
        :type CheckType: int
        :param _Detail: 检测项描述
        :type Detail: str
        :param _Enable: 是否启用，1-启用，0-禁用
        :type Enable: int
        """
        self._PortSets = None
        self._CheckType = None
        self._Detail = None
        self._Enable = None

    @property
    def PortSets(self):
        r"""端口集合,以逗号分隔
        :rtype: str
        """
        return self._PortSets

    @PortSets.setter
    def PortSets(self, PortSets):
        self._PortSets = PortSets

    @property
    def CheckType(self):
        r"""检测项类型，0-系统定义，1-用户自定义
        :rtype: int
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Detail(self):
        r"""检测项描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Enable(self):
        r"""是否启用，1-启用，0-禁用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._PortSets = params.get("PortSets")
        self._CheckType = params.get("CheckType")
        self._Detail = params.get("Detail")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortViewPortRisk(AbstractModel):
    r"""端口视角的端口风险对象

    """

    def __init__(self):
        r"""
        :param _NoHandleCount: 未处理数量
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Port: 端口
        :type Port: int
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Suggestion: 处置建议,0保持现状、1限制访问、2封禁端口
        :type Suggestion: int
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: str
        :param _Id: ID
        :type Id: str
        :param _From: 识别来源
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _Service: 服务
        :type Service: str
        """
        self._NoHandleCount = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Port = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._Service = None

    @property
    def NoHandleCount(self):
        r"""未处理数量
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

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
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

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
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        r"""处置建议,0保持现状、1限制访问、2封禁端口
        :rtype: int
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def AffectAssetCount(self):
        r"""影响资产数量
        :rtype: str
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""识别来源
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Service(self):
        r"""服务
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Port = params.get("Port")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductSupport(AbstractModel):
    r"""漏洞信息产品支持状态

    """

    def __init__(self):
        r"""
        :param _VSSScan: true支持扫描。false不支持扫描
        :type VSSScan: bool
        :param _CWPScan: 0不支持，1支持
        :type CWPScan: str
        :param _CFWPatch: 1支持虚拟补丁，0或空不支持
        :type CFWPatch: str
        :param _WafPatch: 0不支持，1支持	
        :type WafPatch: int
        :param _CWPFix: 0不支持，1支持	
        :type CWPFix: int
        :param _CveId: cveid
        :type CveId: str
        """
        self._VSSScan = None
        self._CWPScan = None
        self._CFWPatch = None
        self._WafPatch = None
        self._CWPFix = None
        self._CveId = None

    @property
    def VSSScan(self):
        r"""true支持扫描。false不支持扫描
        :rtype: bool
        """
        return self._VSSScan

    @VSSScan.setter
    def VSSScan(self, VSSScan):
        self._VSSScan = VSSScan

    @property
    def CWPScan(self):
        r"""0不支持，1支持
        :rtype: str
        """
        return self._CWPScan

    @CWPScan.setter
    def CWPScan(self, CWPScan):
        self._CWPScan = CWPScan

    @property
    def CFWPatch(self):
        r"""1支持虚拟补丁，0或空不支持
        :rtype: str
        """
        return self._CFWPatch

    @CFWPatch.setter
    def CFWPatch(self, CFWPatch):
        self._CFWPatch = CFWPatch

    @property
    def WafPatch(self):
        r"""0不支持，1支持	
        :rtype: int
        """
        return self._WafPatch

    @WafPatch.setter
    def WafPatch(self, WafPatch):
        self._WafPatch = WafPatch

    @property
    def CWPFix(self):
        r"""0不支持，1支持	
        :rtype: int
        """
        return self._CWPFix

    @CWPFix.setter
    def CWPFix(self, CWPFix):
        self._CWPFix = CWPFix

    @property
    def CveId(self):
        r"""cveid
        :rtype: str
        """
        return self._CveId

    @CveId.setter
    def CveId(self, CveId):
        self._CveId = CveId


    def _deserialize(self, params):
        self._VSSScan = params.get("VSSScan")
        self._CWPScan = params.get("CWPScan")
        self._CFWPatch = params.get("CFWPatch")
        self._WafPatch = params.get("WafPatch")
        self._CWPFix = params.get("CWPFix")
        self._CveId = params.get("CveId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIpDomainListKey(AbstractModel):
    r"""公网IP和域名资产列表key

    """

    def __init__(self):
        r"""
        :param _Asset: 资产值
        :type Asset: str
        """
        self._Asset = None

    @property
    def Asset(self):
        r"""资产值
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset


    def _deserialize(self, params):
        self._Asset = params.get("Asset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedEvent(AbstractModel):
    r"""相关攻击事件结构

    """

    def __init__(self):
        r"""
        :param _EventID: 事件ID
        :type EventID: str
        :param _Description: 事件描述
        :type Description: str
        :param _RelatedCount: 与事件关联的告警数量
        :type RelatedCount: int
        """
        self._EventID = None
        self._Description = None
        self._RelatedCount = None

    @property
    def EventID(self):
        r"""事件ID
        :rtype: str
        """
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def Description(self):
        r"""事件描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RelatedCount(self):
        r"""与事件关联的告警数量
        :rtype: int
        """
        return self._RelatedCount

    @RelatedCount.setter
    def RelatedCount(self, RelatedCount):
        self._RelatedCount = RelatedCount


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._Description = params.get("Description")
        self._RelatedCount = params.get("RelatedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportItemKey(AbstractModel):
    r"""报告项key

    """

    def __init__(self):
        r"""
        :param _TaskLogList: 日志Id列表
        :type TaskLogList: list of str
        """
        self._TaskLogList = None

    @property
    def TaskLogList(self):
        r"""日志Id列表
        :rtype: list of str
        """
        return self._TaskLogList

    @TaskLogList.setter
    def TaskLogList(self, TaskLogList):
        self._TaskLogList = TaskLogList


    def _deserialize(self, params):
        self._TaskLogList = params.get("TaskLogList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTaskIdList(AbstractModel):
    r"""报告中的task_id list

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id列表
        :type TaskIdList: list of str
        :param _AppId: 租户ID
        :type AppId: str
        """
        self._TaskIdList = None
        self._AppId = None

    @property
    def TaskIdList(self):
        r"""任务id列表
        :rtype: list of str
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def AppId(self):
        r"""租户ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._TaskIdList = params.get("TaskIdList")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryImageVO(AbstractModel):
    r"""仓库镜像列表

    """

    def __init__(self):
        r"""
        :param _AppId: 用户appid
        :type AppId: int
        :param _Uin: 用户uin
        :type Uin: str
        :param _NickName: 昵称
        :type NickName: str
        :param _InstanceId: 镜像id
        :type InstanceId: str
        :param _InstanceName: 镜像名称
        :type InstanceName: str
        :param _InstanceCreateTime: 镜像创建时间
        :type InstanceCreateTime: str
        :param _InstanceSize: 镜像大小带单位
        :type InstanceSize: str
        :param _BuildCount: 构建次数
        :type BuildCount: int
        :param _InstanceType: 镜像类型
        :type InstanceType: str
        :param _AuthStatus: 授权状态
        :type AuthStatus: int
        :param _InstanceVersion: 镜像版本
        :type InstanceVersion: str
        :param _Region: 地域
        :type Region: str
        :param _RepositoryUrl: 仓库地址
        :type RepositoryUrl: str
        :param _RepositoryName: 仓库名称
        :type RepositoryName: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _VulRisk: 漏洞风险
        :type VulRisk: int
        :param _CheckCount: 检查任务
        :type CheckCount: int
        :param _CheckTime: 体检时间
        :type CheckTime: str
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceCreateTime = None
        self._InstanceSize = None
        self._BuildCount = None
        self._InstanceType = None
        self._AuthStatus = None
        self._InstanceVersion = None
        self._Region = None
        self._RepositoryUrl = None
        self._RepositoryName = None
        self._IsCore = None
        self._VulRisk = None
        self._CheckCount = None
        self._CheckTime = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""用户appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def InstanceId(self):
        r"""镜像id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""镜像名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCreateTime(self):
        r"""镜像创建时间
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def InstanceSize(self):
        r"""镜像大小带单位
        :rtype: str
        """
        return self._InstanceSize

    @InstanceSize.setter
    def InstanceSize(self, InstanceSize):
        self._InstanceSize = InstanceSize

    @property
    def BuildCount(self):
        r"""构建次数
        :rtype: int
        """
        return self._BuildCount

    @BuildCount.setter
    def BuildCount(self, BuildCount):
        self._BuildCount = BuildCount

    @property
    def InstanceType(self):
        r"""镜像类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AuthStatus(self):
        r"""授权状态
        :rtype: int
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def InstanceVersion(self):
        r"""镜像版本
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RepositoryUrl(self):
        r"""仓库地址
        :rtype: str
        """
        return self._RepositoryUrl

    @RepositoryUrl.setter
    def RepositoryUrl(self, RepositoryUrl):
        self._RepositoryUrl = RepositoryUrl

    @property
    def RepositoryName(self):
        r"""仓库名称
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def VulRisk(self):
        r"""漏洞风险
        :rtype: int
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def CheckCount(self):
        r"""检查任务
        :rtype: int
        """
        return self._CheckCount

    @CheckCount.setter
    def CheckCount(self, CheckCount):
        self._CheckCount = CheckCount

    @property
    def CheckTime(self):
        r"""体检时间
        :rtype: str
        """
        return self._CheckTime

    @CheckTime.setter
    def CheckTime(self, CheckTime):
        self._CheckTime = CheckTime

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._InstanceSize = params.get("InstanceSize")
        self._BuildCount = params.get("BuildCount")
        self._InstanceType = params.get("InstanceType")
        self._AuthStatus = params.get("AuthStatus")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Region = params.get("Region")
        self._RepositoryUrl = params.get("RepositoryUrl")
        self._RepositoryName = params.get("RepositoryName")
        self._IsCore = params.get("IsCore")
        self._VulRisk = params.get("VulRisk")
        self._CheckCount = params.get("CheckCount")
        self._CheckTime = params.get("CheckTime")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskCallRecord(AbstractModel):
    r"""风险调用记录详情

    """

    def __init__(self):
        r"""
        :param _EventName: 接口名称
        :type EventName: str
        :param _EventDescCN: 接口中文描述
        :type EventDescCN: str
        :param _EventDescEN: 接口英文描述
        :type EventDescEN: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductNameCN: 产品中文名称
        :type ProductNameCN: str
        :param _CallCount: 调用次数
        :type CallCount: int
        """
        self._EventName = None
        self._EventDescCN = None
        self._EventDescEN = None
        self._ProductName = None
        self._ProductNameCN = None
        self._CallCount = None

    @property
    def EventName(self):
        r"""接口名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventDescCN(self):
        r"""接口中文描述
        :rtype: str
        """
        return self._EventDescCN

    @EventDescCN.setter
    def EventDescCN(self, EventDescCN):
        self._EventDescCN = EventDescCN

    @property
    def EventDescEN(self):
        r"""接口英文描述
        :rtype: str
        """
        return self._EventDescEN

    @EventDescEN.setter
    def EventDescEN(self, EventDescEN):
        self._EventDescEN = EventDescEN

    @property
    def ProductName(self):
        r"""产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductNameCN(self):
        r"""产品中文名称
        :rtype: str
        """
        return self._ProductNameCN

    @ProductNameCN.setter
    def ProductNameCN(self, ProductNameCN):
        self._ProductNameCN = ProductNameCN

    @property
    def CallCount(self):
        r"""调用次数
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._EventDescCN = params.get("EventDescCN")
        self._EventDescEN = params.get("EventDescEN")
        self._ProductName = params.get("ProductName")
        self._ProductNameCN = params.get("ProductNameCN")
        self._CallCount = params.get("CallCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskCenterStatusKey(AbstractModel):
    r"""风险中心状态处理Key

    """

    def __init__(self):
        r"""
        :param _Id: 风险ID
        :type Id: str
        :param _PublicIPDomain: 公网IP/域名
        :type PublicIPDomain: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AppId: APP ID
        :type AppId: str
        """
        self._Id = None
        self._PublicIPDomain = None
        self._InstanceId = None
        self._AppId = None

    @property
    def Id(self):
        r"""风险ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PublicIPDomain(self):
        r"""公网IP/域名
        :rtype: str
        """
        return self._PublicIPDomain

    @PublicIPDomain.setter
    def PublicIPDomain(self, PublicIPDomain):
        self._PublicIPDomain = PublicIPDomain

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        r"""APP ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PublicIPDomain = params.get("PublicIPDomain")
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetailItem(AbstractModel):
    r"""风险详情

    """

    def __init__(self):
        r"""
        :param _CreateTime: 首次发现时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RiskStatus: 风险状态
        :type RiskStatus: int
        :param _RiskContent: 风险内容
        :type RiskContent: str
        :param _Provider: 云厂商
        :type Provider: str
        :param _ProviderName: 云厂商名称
        :type ProviderName: str
        :param _CloudAccountId: 云账号
        :type CloudAccountId: str
        :param _CloudAccountName: 云账号名称
        :type CloudAccountName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _RiskId: 风险ID
        :type RiskId: int
        :param _RiskRuleId: 风险规则ID
        :type RiskRuleId: str
        :param _CheckStatus: 风险验证状态
        :type CheckStatus: str
        """
        self._CreateTime = None
        self._UpdateTime = None
        self._RiskStatus = None
        self._RiskContent = None
        self._Provider = None
        self._ProviderName = None
        self._CloudAccountId = None
        self._CloudAccountName = None
        self._InstanceId = None
        self._InstanceName = None
        self._RiskId = None
        self._RiskRuleId = None
        self._CheckStatus = None

    @property
    def CreateTime(self):
        r"""首次发现时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RiskStatus(self):
        r"""风险状态
        :rtype: int
        """
        return self._RiskStatus

    @RiskStatus.setter
    def RiskStatus(self, RiskStatus):
        self._RiskStatus = RiskStatus

    @property
    def RiskContent(self):
        r"""风险内容
        :rtype: str
        """
        return self._RiskContent

    @RiskContent.setter
    def RiskContent(self, RiskContent):
        self._RiskContent = RiskContent

    @property
    def Provider(self):
        r"""云厂商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

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
    def CloudAccountId(self):
        r"""云账号
        :rtype: str
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
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: int
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def RiskRuleId(self):
        r"""风险规则ID
        :rtype: str
        """
        return self._RiskRuleId

    @RiskRuleId.setter
    def RiskRuleId(self, RiskRuleId):
        self._RiskRuleId = RiskRuleId

    @property
    def CheckStatus(self):
        r"""风险验证状态
        :rtype: str
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RiskStatus = params.get("RiskStatus")
        self._RiskContent = params.get("RiskContent")
        self._Provider = params.get("Provider")
        self._ProviderName = params.get("ProviderName")
        self._CloudAccountId = params.get("CloudAccountId")
        self._CloudAccountName = params.get("CloudAccountName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._RiskId = params.get("RiskId")
        self._RiskRuleId = params.get("RiskRuleId")
        self._CheckStatus = params.get("CheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskRuleInfo(AbstractModel):
    r"""风险规则

    """

    def __init__(self):
        r"""
        :param _RuleID: 风险检查项ID
        :type RuleID: str
        :param _Provider: 云厂商名称
        :type Provider: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _RiskTitle: 风险名称
        :type RiskTitle: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _RiskInfluence: 风险危害
        :type RiskInfluence: str
        :param _RiskFixAdvance: 风险修复指引报告链接
        :type RiskFixAdvance: str
        :param _DispositionType: 边界管控
        :type DispositionType: str
        """
        self._RuleID = None
        self._Provider = None
        self._InstanceType = None
        self._RiskTitle = None
        self._CheckType = None
        self._RiskLevel = None
        self._RiskInfluence = None
        self._RiskFixAdvance = None
        self._DispositionType = None

    @property
    def RuleID(self):
        r"""风险检查项ID
        :rtype: str
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Provider(self):
        r"""云厂商名称
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def RiskTitle(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskTitle

    @RiskTitle.setter
    def RiskTitle(self, RiskTitle):
        self._RiskTitle = RiskTitle

    @property
    def CheckType(self):
        r"""检查类型
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskInfluence(self):
        r"""风险危害
        :rtype: str
        """
        return self._RiskInfluence

    @RiskInfluence.setter
    def RiskInfluence(self, RiskInfluence):
        self._RiskInfluence = RiskInfluence

    @property
    def RiskFixAdvance(self):
        r"""风险修复指引报告链接
        :rtype: str
        """
        return self._RiskFixAdvance

    @RiskFixAdvance.setter
    def RiskFixAdvance(self, RiskFixAdvance):
        self._RiskFixAdvance = RiskFixAdvance

    @property
    def DispositionType(self):
        r"""边界管控
        :rtype: str
        """
        return self._DispositionType

    @DispositionType.setter
    def DispositionType(self, DispositionType):
        self._DispositionType = DispositionType


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._Provider = params.get("Provider")
        self._InstanceType = params.get("InstanceType")
        self._RiskTitle = params.get("RiskTitle")
        self._CheckType = params.get("CheckType")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskInfluence = params.get("RiskInfluence")
        self._RiskFixAdvance = params.get("RiskFixAdvance")
        self._DispositionType = params.get("DispositionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskRuleItem(AbstractModel):
    r"""风险规则

    """

    def __init__(self):
        r"""
        :param _ItemId: 风险检查项ID
        :type ItemId: str
        :param _Provider: 云厂商名称
        :type Provider: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _InstanceName: 实例类型名称
        :type InstanceName: str
        :param _RiskTitle: 风险名称
        :type RiskTitle: str
        :param _CheckType: 检查类型
        :type CheckType: str
        :param _Severity: 风险等级
        :type Severity: str
        :param _RiskInfluence: 风险危害
        :type RiskInfluence: str
        """
        self._ItemId = None
        self._Provider = None
        self._InstanceType = None
        self._InstanceName = None
        self._RiskTitle = None
        self._CheckType = None
        self._Severity = None
        self._RiskInfluence = None

    @property
    def ItemId(self):
        r"""风险检查项ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def Provider(self):
        r"""云厂商名称
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        r"""实例类型名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RiskTitle(self):
        r"""风险名称
        :rtype: str
        """
        return self._RiskTitle

    @RiskTitle.setter
    def RiskTitle(self, RiskTitle):
        self._RiskTitle = RiskTitle

    @property
    def CheckType(self):
        r"""检查类型
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Severity(self):
        r"""风险等级
        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def RiskInfluence(self):
        r"""风险危害
        :rtype: str
        """
        return self._RiskInfluence

    @RiskInfluence.setter
    def RiskInfluence(self, RiskInfluence):
        self._RiskInfluence = RiskInfluence


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._Provider = params.get("Provider")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._RiskTitle = params.get("RiskTitle")
        self._CheckType = params.get("CheckType")
        self._Severity = params.get("Severity")
        self._RiskInfluence = params.get("RiskInfluence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleInfo(AbstractModel):
    r"""告警数据攻击者或受害者信息

    """

    def __init__(self):
        r"""
        :param _IP: IP
        :type IP: str
        :param _HostIP: HostIP
        :type HostIP: str
        :param _OriginIP: 原始IP
        :type OriginIP: str
        :param _Port: 端口
        :type Port: int
        :param _InstanceID: 资产ID
        :type InstanceID: str
        :param _City: 城市
        :type City: str
        :param _Province: 省份
        :type Province: str
        :param _Country: 国家
        :type Country: str
        :param _Address: 地址
        :type Address: str
        :param _Latitude: 纬度
        :type Latitude: str
        :param _Longitude: 经度
        :type Longitude: str
        :param _Info: 信息
        :type Info: str
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 企业名称
        :type Name: str
        :param _Account: 账号
        :type Account: str
        :param _Family: 家族团伙
        :type Family: str
        :param _VirusName: 病毒名
        :type VirusName: str
        :param _MD5: MD5值
        :type MD5: str
        :param _FileName: 恶意进程文件名
        :type FileName: str
        :param _AssetType: 1:主机资产 2:域名资产 3:网络资产
        :type AssetType: int
        :param _FromLogAnalysisData: 来源日志分析的信息字段
        :type FromLogAnalysisData: list of KeyValue
        :param _ContainerName: 容器名
        :type ContainerName: str
        :param _ContainerID: 容器ID
        :type ContainerID: str
        """
        self._IP = None
        self._HostIP = None
        self._OriginIP = None
        self._Port = None
        self._InstanceID = None
        self._City = None
        self._Province = None
        self._Country = None
        self._Address = None
        self._Latitude = None
        self._Longitude = None
        self._Info = None
        self._Domain = None
        self._Name = None
        self._Account = None
        self._Family = None
        self._VirusName = None
        self._MD5 = None
        self._FileName = None
        self._AssetType = None
        self._FromLogAnalysisData = None
        self._ContainerName = None
        self._ContainerID = None

    @property
    def IP(self):
        r"""IP
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def HostIP(self):
        r"""HostIP
        :rtype: str
        """
        return self._HostIP

    @HostIP.setter
    def HostIP(self, HostIP):
        self._HostIP = HostIP

    @property
    def OriginIP(self):
        r"""原始IP
        :rtype: str
        """
        return self._OriginIP

    @OriginIP.setter
    def OriginIP(self, OriginIP):
        self._OriginIP = OriginIP

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
    def InstanceID(self):
        r"""资产ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def City(self):
        r"""城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Province(self):
        r"""省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Country(self):
        r"""国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

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
    def Latitude(self):
        r"""纬度
        :rtype: str
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Longitude(self):
        r"""经度
        :rtype: str
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Info(self):
        r"""信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        r"""企业名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Family(self):
        r"""家族团伙
        :rtype: str
        """
        return self._Family

    @Family.setter
    def Family(self, Family):
        self._Family = Family

    @property
    def VirusName(self):
        r"""病毒名
        :rtype: str
        """
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def MD5(self):
        r"""MD5值
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def FileName(self):
        r"""恶意进程文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AssetType(self):
        r"""1:主机资产 2:域名资产 3:网络资产
        :rtype: int
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def FromLogAnalysisData(self):
        r"""来源日志分析的信息字段
        :rtype: list of KeyValue
        """
        return self._FromLogAnalysisData

    @FromLogAnalysisData.setter
    def FromLogAnalysisData(self, FromLogAnalysisData):
        self._FromLogAnalysisData = FromLogAnalysisData

    @property
    def ContainerName(self):
        r"""容器名
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ContainerID(self):
        r"""容器ID
        :rtype: str
        """
        return self._ContainerID

    @ContainerID.setter
    def ContainerID(self, ContainerID):
        self._ContainerID = ContainerID


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._HostIP = params.get("HostIP")
        self._OriginIP = params.get("OriginIP")
        self._Port = params.get("Port")
        self._InstanceID = params.get("InstanceID")
        self._City = params.get("City")
        self._Province = params.get("Province")
        self._Country = params.get("Country")
        self._Address = params.get("Address")
        self._Latitude = params.get("Latitude")
        self._Longitude = params.get("Longitude")
        self._Info = params.get("Info")
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Account = params.get("Account")
        self._Family = params.get("Family")
        self._VirusName = params.get("VirusName")
        self._MD5 = params.get("MD5")
        self._FileName = params.get("FileName")
        self._AssetType = params.get("AssetType")
        if params.get("FromLogAnalysisData") is not None:
            self._FromLogAnalysisData = []
            for item in params.get("FromLogAnalysisData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FromLogAnalysisData.append(obj)
        self._ContainerName = params.get("ContainerName")
        self._ContainerID = params.get("ContainerID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfo(AbstractModel):
    r"""扫描任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _Status: 任务状态码：1等待开始  2正在扫描  3扫描出错 4扫描完成
        :type Status: int
        :param _Progress: 任务进度
        :type Progress: int
        :param _TaskTime: 任务完成时间
        :type TaskTime: str
        :param _ReportId: 报告ID
        :type ReportId: str
        :param _ReportName: 报告名称
        :type ReportName: str
        :param _ScanPlan: 扫描计划，0-周期任务,1-立即扫描,2-定时扫描,3-自定义
        :type ScanPlan: int
        :param _AssetCount: 关联的资产数
        :type AssetCount: int
        :param _AppId: APP ID
        :type AppId: str
        :param _UIN: 用户主账户ID
        :type UIN: str
        :param _UserName: 用户名称
        :type UserName: str
        """
        self._TaskId = None
        self._TaskName = None
        self._Status = None
        self._Progress = None
        self._TaskTime = None
        self._ReportId = None
        self._ReportName = None
        self._ScanPlan = None
        self._AssetCount = None
        self._AppId = None
        self._UIN = None
        self._UserName = None

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def Status(self):
        r"""任务状态码：1等待开始  2正在扫描  3扫描出错 4扫描完成
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""任务进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskTime(self):
        r"""任务完成时间
        :rtype: str
        """
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ReportId(self):
        r"""报告ID
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ReportName(self):
        r"""报告名称
        :rtype: str
        """
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def ScanPlan(self):
        r"""扫描计划，0-周期任务,1-立即扫描,2-定时扫描,3-自定义
        :rtype: int
        """
        return self._ScanPlan

    @ScanPlan.setter
    def ScanPlan(self, ScanPlan):
        self._ScanPlan = ScanPlan

    @property
    def AssetCount(self):
        r"""关联的资产数
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def AppId(self):
        r"""APP ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""用户主账户ID
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        r"""用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._TaskTime = params.get("TaskTime")
        self._ReportId = params.get("ReportId")
        self._ReportName = params.get("ReportName")
        self._ScanPlan = params.get("ScanPlan")
        self._AssetCount = params.get("AssetCount")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfoList(AbstractModel):
    r"""扫描任务列表展示信息

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _StartTime: 任务开始时间
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _ScanPlanContent: cron格式
        :type ScanPlanContent: str
        :param _TaskType: 0-周期任务,1-立即扫描,2-定时扫描,3-自定义
        :type TaskType: int
        :param _InsertTime: 创建时间
        :type InsertTime: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _SelfDefiningAssets: 自定义指定扫描资产信息
        :type SelfDefiningAssets: list of str
        :param _PredictTime: 预估时间
        :type PredictTime: int
        :param _PredictEndTime: 预估完成时间
        :type PredictEndTime: str
        :param _ReportNumber: 报告数量
        :type ReportNumber: int
        :param _AssetNumber: 资产数量
        :type AssetNumber: int
        :param _ScanStatus: 扫描状态, 0-初始值，1-正在扫描，2-扫描完成，3-扫描出错，4-停止扫描
        :type ScanStatus: int
        :param _Percent: 任务进度
        :type Percent: float
        :param _ScanItem: port/poc/weakpass/webcontent/configrisk
        :type ScanItem: str
        :param _ScanAssetType: 0-全扫，1-指定资产扫，2-排除资产扫，3-自定义指定资产扫描
        :type ScanAssetType: int
        :param _VSSTaskId: vss子任务id
        :type VSSTaskId: str
        :param _CSPMTaskId: cspm子任务id
        :type CSPMTaskId: str
        :param _CWPPOCId: 主机漏扫子任务id
        :type CWPPOCId: str
        :param _CWPBlId: 主机基线子任务id
        :type CWPBlId: str
        :param _VSSTaskProcess: vss子任务进度
        :type VSSTaskProcess: int
        :param _CSPMTaskProcess: cspm子任务进度
        :type CSPMTaskProcess: int
        :param _CWPPOCProcess: 主机漏扫子任务进度
        :type CWPPOCProcess: int
        :param _CWPBlProcess: 主机基线子任务进度
        :type CWPBlProcess: int
        :param _ErrorCode: 异常状态码
        :type ErrorCode: int
        :param _ErrorInfo: 异常信息
        :type ErrorInfo: str
        :param _StartDay: 周期任务开始的天数
        :type StartDay: int
        :param _Frequency: 扫描频率,单位天,1-每天,7-每周,30-月,0-扫描一次
        :type Frequency: int
        :param _CompleteNumber: 完成次数
        :type CompleteNumber: int
        :param _CompleteAssetNumber: 已完成资产个数
        :type CompleteAssetNumber: int
        :param _RiskCount: 风险数
        :type RiskCount: int
        :param _Assets: 资产
        :type Assets: list of TaskAssetObject
        :param _AppId: 用户Appid
        :type AppId: str
        :param _UIN: 用户主账户ID
        :type UIN: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _TaskMode: 体检模式，0-标准模式，1-快速模式，2-高级模式
        :type TaskMode: int
        :param _ScanFrom: 扫描来源
        :type ScanFrom: str
        :param _IsFree: 是否限免体检0不是，1是
        :type IsFree: int
        :param _IsDelete: 是否可以删除，1-可以，0-不可以，对应多账户管理使用
        :type IsDelete: int
        :param _SourceType: 任务源类型，0-默认，1-小助手，2-体检项
        :type SourceType: int
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._ScanPlanContent = None
        self._TaskType = None
        self._InsertTime = None
        self._TaskId = None
        self._SelfDefiningAssets = None
        self._PredictTime = None
        self._PredictEndTime = None
        self._ReportNumber = None
        self._AssetNumber = None
        self._ScanStatus = None
        self._Percent = None
        self._ScanItem = None
        self._ScanAssetType = None
        self._VSSTaskId = None
        self._CSPMTaskId = None
        self._CWPPOCId = None
        self._CWPBlId = None
        self._VSSTaskProcess = None
        self._CSPMTaskProcess = None
        self._CWPPOCProcess = None
        self._CWPBlProcess = None
        self._ErrorCode = None
        self._ErrorInfo = None
        self._StartDay = None
        self._Frequency = None
        self._CompleteNumber = None
        self._CompleteAssetNumber = None
        self._RiskCount = None
        self._Assets = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._TaskMode = None
        self._ScanFrom = None
        self._IsFree = None
        self._IsDelete = None
        self._SourceType = None

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
    def StartTime(self):
        r"""任务开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ScanPlanContent(self):
        r"""cron格式
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def TaskType(self):
        r"""0-周期任务,1-立即扫描,2-定时扫描,3-自定义
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InsertTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SelfDefiningAssets(self):
        r"""自定义指定扫描资产信息
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def PredictTime(self):
        r"""预估时间
        :rtype: int
        """
        return self._PredictTime

    @PredictTime.setter
    def PredictTime(self, PredictTime):
        self._PredictTime = PredictTime

    @property
    def PredictEndTime(self):
        r"""预估完成时间
        :rtype: str
        """
        return self._PredictEndTime

    @PredictEndTime.setter
    def PredictEndTime(self, PredictEndTime):
        self._PredictEndTime = PredictEndTime

    @property
    def ReportNumber(self):
        r"""报告数量
        :rtype: int
        """
        return self._ReportNumber

    @ReportNumber.setter
    def ReportNumber(self, ReportNumber):
        self._ReportNumber = ReportNumber

    @property
    def AssetNumber(self):
        r"""资产数量
        :rtype: int
        """
        return self._AssetNumber

    @AssetNumber.setter
    def AssetNumber(self, AssetNumber):
        self._AssetNumber = AssetNumber

    @property
    def ScanStatus(self):
        r"""扫描状态, 0-初始值，1-正在扫描，2-扫描完成，3-扫描出错，4-停止扫描
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def Percent(self):
        r"""任务进度
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanItem(self):
        r"""port/poc/weakpass/webcontent/configrisk
        :rtype: str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanAssetType(self):
        r"""0-全扫，1-指定资产扫，2-排除资产扫，3-自定义指定资产扫描
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def VSSTaskId(self):
        r"""vss子任务id
        :rtype: str
        """
        return self._VSSTaskId

    @VSSTaskId.setter
    def VSSTaskId(self, VSSTaskId):
        self._VSSTaskId = VSSTaskId

    @property
    def CSPMTaskId(self):
        r"""cspm子任务id
        :rtype: str
        """
        return self._CSPMTaskId

    @CSPMTaskId.setter
    def CSPMTaskId(self, CSPMTaskId):
        self._CSPMTaskId = CSPMTaskId

    @property
    def CWPPOCId(self):
        r"""主机漏扫子任务id
        :rtype: str
        """
        return self._CWPPOCId

    @CWPPOCId.setter
    def CWPPOCId(self, CWPPOCId):
        self._CWPPOCId = CWPPOCId

    @property
    def CWPBlId(self):
        r"""主机基线子任务id
        :rtype: str
        """
        return self._CWPBlId

    @CWPBlId.setter
    def CWPBlId(self, CWPBlId):
        self._CWPBlId = CWPBlId

    @property
    def VSSTaskProcess(self):
        r"""vss子任务进度
        :rtype: int
        """
        return self._VSSTaskProcess

    @VSSTaskProcess.setter
    def VSSTaskProcess(self, VSSTaskProcess):
        self._VSSTaskProcess = VSSTaskProcess

    @property
    def CSPMTaskProcess(self):
        r"""cspm子任务进度
        :rtype: int
        """
        return self._CSPMTaskProcess

    @CSPMTaskProcess.setter
    def CSPMTaskProcess(self, CSPMTaskProcess):
        self._CSPMTaskProcess = CSPMTaskProcess

    @property
    def CWPPOCProcess(self):
        r"""主机漏扫子任务进度
        :rtype: int
        """
        return self._CWPPOCProcess

    @CWPPOCProcess.setter
    def CWPPOCProcess(self, CWPPOCProcess):
        self._CWPPOCProcess = CWPPOCProcess

    @property
    def CWPBlProcess(self):
        r"""主机基线子任务进度
        :rtype: int
        """
        return self._CWPBlProcess

    @CWPBlProcess.setter
    def CWPBlProcess(self, CWPBlProcess):
        self._CWPBlProcess = CWPBlProcess

    @property
    def ErrorCode(self):
        r"""异常状态码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        r"""异常信息
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def StartDay(self):
        r"""周期任务开始的天数
        :rtype: int
        """
        return self._StartDay

    @StartDay.setter
    def StartDay(self, StartDay):
        self._StartDay = StartDay

    @property
    def Frequency(self):
        r"""扫描频率,单位天,1-每天,7-每周,30-月,0-扫描一次
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CompleteNumber(self):
        r"""完成次数
        :rtype: int
        """
        return self._CompleteNumber

    @CompleteNumber.setter
    def CompleteNumber(self, CompleteNumber):
        self._CompleteNumber = CompleteNumber

    @property
    def CompleteAssetNumber(self):
        r"""已完成资产个数
        :rtype: int
        """
        return self._CompleteAssetNumber

    @CompleteAssetNumber.setter
    def CompleteAssetNumber(self, CompleteAssetNumber):
        self._CompleteAssetNumber = CompleteAssetNumber

    @property
    def RiskCount(self):
        r"""风险数
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def Assets(self):
        r"""资产
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def AppId(self):
        r"""用户Appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""用户主账户ID
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

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
    def TaskMode(self):
        r"""体检模式，0-标准模式，1-快速模式，2-高级模式
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def ScanFrom(self):
        r"""扫描来源
        :rtype: str
        """
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def IsFree(self):
        r"""是否限免体检0不是，1是
        :rtype: int
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def IsDelete(self):
        r"""是否可以删除，1-可以，0-不可以，对应多账户管理使用
        :rtype: int
        """
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete

    @property
    def SourceType(self):
        r"""任务源类型，0-默认，1-小助手，2-体检项
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._TaskType = params.get("TaskType")
        self._InsertTime = params.get("InsertTime")
        self._TaskId = params.get("TaskId")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._PredictTime = params.get("PredictTime")
        self._PredictEndTime = params.get("PredictEndTime")
        self._ReportNumber = params.get("ReportNumber")
        self._AssetNumber = params.get("AssetNumber")
        self._ScanStatus = params.get("ScanStatus")
        self._Percent = params.get("Percent")
        self._ScanItem = params.get("ScanItem")
        self._ScanAssetType = params.get("ScanAssetType")
        self._VSSTaskId = params.get("VSSTaskId")
        self._CSPMTaskId = params.get("CSPMTaskId")
        self._CWPPOCId = params.get("CWPPOCId")
        self._CWPBlId = params.get("CWPBlId")
        self._VSSTaskProcess = params.get("VSSTaskProcess")
        self._CSPMTaskProcess = params.get("CSPMTaskProcess")
        self._CWPPOCProcess = params.get("CWPPOCProcess")
        self._CWPBlProcess = params.get("CWPBlProcess")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        self._StartDay = params.get("StartDay")
        self._Frequency = params.get("Frequency")
        self._CompleteNumber = params.get("CompleteNumber")
        self._CompleteAssetNumber = params.get("CompleteAssetNumber")
        self._RiskCount = params.get("RiskCount")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._TaskMode = params.get("TaskMode")
        self._ScanFrom = params.get("ScanFrom")
        self._IsFree = params.get("IsFree")
        self._IsDelete = params.get("IsDelete")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRisk(AbstractModel):
    r"""服务风险

    """

    def __init__(self):
        r"""
        :param _ServiceTag: 测绘标签
        :type ServiceTag: str
        :param _Port: 端口
        :type Port: int
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _Level: 风险等级 low:低危 high:高危 middle:中危 info:提示 extreme:严重
        :type Level: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Component: 组件
        :type Component: str
        :param _Service: 服务
        :type Service: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _RiskDetails: 风险详情
        :type RiskDetails: str
        :param _Suggestion: 处置建议
        :type Suggestion: str
        :param _Status: 状态，0未处理、1已处置、2已忽略、3云防已防护
        :type Status: int
        :param _Id: 资产唯一id
        :type Id: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _ServiceSnapshot: 服务快照
        :type ServiceSnapshot: str
        :param _Url: 服务访问的url
        :type Url: str
        :param _Index: 列表索引值
        :type Index: str
        :param _RiskList: 风险列表
        :type RiskList: list of ServerRiskSuggestion
        :param _SuggestionList: 建议列表
        :type SuggestionList: list of ServerRiskSuggestion
        :param _StatusCode: HTTP响应状态码
        :type StatusCode: str
        :param _NewLevel: 新风险等级,high_risk 高危 suspect 疑似 Normal 暂无风险
        :type NewLevel: str
        :param _XspmStatus: 状态，0未处理、1已处置、2已忽略、3云防已防护、4无需处理
        :type XspmStatus: int
        """
        self._ServiceTag = None
        self._Port = None
        self._AffectAsset = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._RiskDetails = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._ServiceSnapshot = None
        self._Url = None
        self._Index = None
        self._RiskList = None
        self._SuggestionList = None
        self._StatusCode = None
        self._NewLevel = None
        self._XspmStatus = None

    @property
    def ServiceTag(self):
        r"""测绘标签
        :rtype: str
        """
        return self._ServiceTag

    @ServiceTag.setter
    def ServiceTag(self, ServiceTag):
        self._ServiceTag = ServiceTag

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
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Level(self):
        r"""风险等级 low:低危 high:高危 middle:中危 info:提示 extreme:严重
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

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
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""服务
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RiskDetails(self):
        r"""风险详情
        :rtype: str
        """
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Suggestion(self):
        r"""处置建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        r"""状态，0未处理、1已处置、2已忽略、3云防已防护
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""资产唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ServiceSnapshot(self):
        r"""服务快照
        :rtype: str
        """
        return self._ServiceSnapshot

    @ServiceSnapshot.setter
    def ServiceSnapshot(self, ServiceSnapshot):
        self._ServiceSnapshot = ServiceSnapshot

    @property
    def Url(self):
        r"""服务访问的url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Index(self):
        r"""列表索引值
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RiskList(self):
        r"""风险列表
        :rtype: list of ServerRiskSuggestion
        """
        return self._RiskList

    @RiskList.setter
    def RiskList(self, RiskList):
        self._RiskList = RiskList

    @property
    def SuggestionList(self):
        r"""建议列表
        :rtype: list of ServerRiskSuggestion
        """
        return self._SuggestionList

    @SuggestionList.setter
    def SuggestionList(self, SuggestionList):
        self._SuggestionList = SuggestionList

    @property
    def StatusCode(self):
        r"""HTTP响应状态码
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def NewLevel(self):
        r"""新风险等级,high_risk 高危 suspect 疑似 Normal 暂无风险
        :rtype: str
        """
        return self._NewLevel

    @NewLevel.setter
    def NewLevel(self, NewLevel):
        self._NewLevel = NewLevel

    @property
    def XspmStatus(self):
        r"""状态，0未处理、1已处置、2已忽略、3云防已防护、4无需处理
        :rtype: int
        """
        return self._XspmStatus

    @XspmStatus.setter
    def XspmStatus(self, XspmStatus):
        self._XspmStatus = XspmStatus


    def _deserialize(self, params):
        self._ServiceTag = params.get("ServiceTag")
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._RiskDetails = params.get("RiskDetails")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._ServiceSnapshot = params.get("ServiceSnapshot")
        self._Url = params.get("Url")
        self._Index = params.get("Index")
        if params.get("RiskList") is not None:
            self._RiskList = []
            for item in params.get("RiskList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._RiskList.append(obj)
        if params.get("SuggestionList") is not None:
            self._SuggestionList = []
            for item in params.get("SuggestionList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._SuggestionList.append(obj)
        self._StatusCode = params.get("StatusCode")
        self._NewLevel = params.get("NewLevel")
        self._XspmStatus = params.get("XspmStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRiskSuggestion(AbstractModel):
    r"""风险详情

    """

    def __init__(self):
        r"""
        :param _Title: 标题
        :type Title: str
        :param _Body: 详情
        :type Body: str
        """
        self._Title = None
        self._Body = None

    @property
    def Title(self):
        r"""标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Body(self):
        r"""详情
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSupport(AbstractModel):
    r"""产品支持情况

    """

    def __init__(self):
        r"""
        :param _ServiceName: 产品名称:
"cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
        :type ServiceName: str
        :param _SupportHandledCount: 已处理的资产总数
        :type SupportHandledCount: int
        :param _SupportTotalCount: 支持的资产总数
        :type SupportTotalCount: int
        :param _IsSupport: 是否支持该产品1支持；0不支持
        :type IsSupport: bool
        """
        self._ServiceName = None
        self._SupportHandledCount = None
        self._SupportTotalCount = None
        self._IsSupport = None

    @property
    def ServiceName(self):
        r"""产品名称:
"cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SupportHandledCount(self):
        r"""已处理的资产总数
        :rtype: int
        """
        return self._SupportHandledCount

    @SupportHandledCount.setter
    def SupportHandledCount(self, SupportHandledCount):
        self._SupportHandledCount = SupportHandledCount

    @property
    def SupportTotalCount(self):
        r"""支持的资产总数
        :rtype: int
        """
        return self._SupportTotalCount

    @SupportTotalCount.setter
    def SupportTotalCount(self, SupportTotalCount):
        self._SupportTotalCount = SupportTotalCount

    @property
    def IsSupport(self):
        r"""是否支持该产品1支持；0不支持
        :rtype: bool
        """
        return self._IsSupport

    @IsSupport.setter
    def IsSupport(self, IsSupport):
        self._IsSupport = IsSupport


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._SupportHandledCount = params.get("SupportHandledCount")
        self._SupportTotalCount = params.get("SupportTotalCount")
        self._IsSupport = params.get("IsSupport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceIPAsset(AbstractModel):
    r"""访问密钥资产信息（源IP角度）

    """

    def __init__(self):
        r"""
        :param _ID: 源IP id
        :type ID: int
        :param _SourceIP: 源IP
        :type SourceIP: str
        :param _Remark: 备注
        :type Remark: str
        :param _AppID: 账号所属APPID
        :type AppID: int
        :param _Region: IP地域
        :type Region: str
        :param _EventType: 调用方式
-1:未统计
0:控制台调用
1:API
        :type EventType: int
        :param _IPType: IP类型
0:账号内（未备注）
1:账号外（未备注）
2:账号内   (已备注)
3:账号外   (已备注)
        :type IPType: int
        :param _AccessKeyAlarmList: 告警信息列表
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AKInfo: ak信息列表
        :type AKInfo: list of AKInfo
        :param _ActionCount: 调用接口数量
        :type ActionCount: int
        :param _LastAccessTime: 最近访问时间
        :type LastAccessTime: str
        :param _InstanceID: IP关联实例ID，如果为空字符串，代表非账号内资产
        :type InstanceID: str
        :param _InstanceName: IP关联实例名称
        :type InstanceName: str
        :param _Uin: 账号所属Uin
        :type Uin: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _ShowStatus: 展示状态
        :type ShowStatus: bool
        :param _ISP: 运营商字段
        :type ISP: str
        :param _VpcInfo: 账号外vpc信息
        :type VpcInfo: list of SourceIPVpcInfo
        :param _CloudType: 云类型
0为腾讯云
        :type CloudType: int
        """
        self._ID = None
        self._SourceIP = None
        self._Remark = None
        self._AppID = None
        self._Region = None
        self._EventType = None
        self._IPType = None
        self._AccessKeyAlarmList = None
        self._AKInfo = None
        self._ActionCount = None
        self._LastAccessTime = None
        self._InstanceID = None
        self._InstanceName = None
        self._Uin = None
        self._Nickname = None
        self._ShowStatus = None
        self._ISP = None
        self._VpcInfo = None
        self._CloudType = None

    @property
    def ID(self):
        r"""源IP id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def SourceIP(self):
        r"""源IP
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AppID(self):
        r"""账号所属APPID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Region(self):
        r"""IP地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EventType(self):
        r"""调用方式
-1:未统计
0:控制台调用
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def IPType(self):
        r"""IP类型
0:账号内（未备注）
1:账号外（未备注）
2:账号内   (已备注)
3:账号外   (已备注)
        :rtype: int
        """
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def AccessKeyAlarmList(self):
        r"""告警信息列表
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AKInfo(self):
        r"""ak信息列表
        :rtype: list of AKInfo
        """
        return self._AKInfo

    @AKInfo.setter
    def AKInfo(self, AKInfo):
        self._AKInfo = AKInfo

    @property
    def ActionCount(self):
        r"""调用接口数量
        :rtype: int
        """
        return self._ActionCount

    @ActionCount.setter
    def ActionCount(self, ActionCount):
        self._ActionCount = ActionCount

    @property
    def LastAccessTime(self):
        r"""最近访问时间
        :rtype: str
        """
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def InstanceID(self):
        r"""IP关联实例ID，如果为空字符串，代表非账号内资产
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def InstanceName(self):
        r"""IP关联实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Uin(self):
        r"""账号所属Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
    def ShowStatus(self):
        r"""展示状态
        :rtype: bool
        """
        return self._ShowStatus

    @ShowStatus.setter
    def ShowStatus(self, ShowStatus):
        self._ShowStatus = ShowStatus

    @property
    def ISP(self):
        r"""运营商字段
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcInfo(self):
        r"""账号外vpc信息
        :rtype: list of SourceIPVpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def CloudType(self):
        r"""云类型
0为腾讯云
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._SourceIP = params.get("SourceIP")
        self._Remark = params.get("Remark")
        self._AppID = params.get("AppID")
        self._Region = params.get("Region")
        self._EventType = params.get("EventType")
        self._IPType = params.get("IPType")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AKInfo") is not None:
            self._AKInfo = []
            for item in params.get("AKInfo"):
                obj = AKInfo()
                obj._deserialize(item)
                self._AKInfo.append(obj)
        self._ActionCount = params.get("ActionCount")
        self._LastAccessTime = params.get("LastAccessTime")
        self._InstanceID = params.get("InstanceID")
        self._InstanceName = params.get("InstanceName")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._ShowStatus = params.get("ShowStatus")
        self._ISP = params.get("ISP")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = SourceIPVpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceIPVpcInfo(AbstractModel):
    r"""调用源IP 外部账号信息

    """

    def __init__(self):
        r"""
        :param _Name: 账号名称
        :type Name: str
        :param _AppID: vpc所属appid
        :type AppID: int
        :param _VpcID: vpc id
        :type VpcID: str
        :param _VpcName: vpc 名称
        :type VpcName: str
        """
        self._Name = None
        self._AppID = None
        self._VpcID = None
        self._VpcName = None

    @property
    def Name(self):
        r"""账号名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppID(self):
        r"""vpc所属appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def VpcID(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def VpcName(self):
        r"""vpc 名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AppID = params.get("AppID")
        self._VpcID = params.get("VpcID")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardItem(AbstractModel):
    r"""CSPM规范

    """

    def __init__(self):
        r"""
        :param _ID: 规范ID
        :type ID: int
        :param _Name: 规范名称
        :type Name: str
        """
        self._ID = None
        self._Name = None

    @property
    def ID(self):
        r"""规范ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""规范名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardTerm(AbstractModel):
    r"""CSPM条款

    """

    def __init__(self):
        r"""
        :param _Tag: 标签
        :type Tag: str
        :param _Terms: 条款
        :type Terms: list of str
        """
        self._Tag = None
        self._Terms = None

    @property
    def Tag(self):
        r"""标签
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Terms(self):
        r"""条款
        :rtype: list of str
        """
        return self._Terms

    @Terms.setter
    def Terms(self, Terms):
        self._Terms = Terms


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Terms = params.get("Terms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticalFilter(AbstractModel):
    r"""用户行为分析 统计条件

    """

    def __init__(self):
        r"""
        :param _OperatorType: 0:不基于统计检测
1:发生次数高于固定值
2:发生次数高于周期平均值的百分之
3:发生次数高于用户平均值的百分之
        :type OperatorType: int
        :param _Value: 统计值
        :type Value: float
        """
        self._OperatorType = None
        self._Value = None

    @property
    def OperatorType(self):
        r"""0:不基于统计检测
1:发生次数高于固定值
2:发生次数高于周期平均值的百分之
3:发生次数高于用户平均值的百分之
        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType

    @property
    def Value(self):
        r"""统计值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._OperatorType = params.get("OperatorType")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskRequest(AbstractModel):
    r"""StopRiskCenterTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIdList: 任务id 列表
        :type TaskIdList: list of TaskIdListKey
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        """
        self._TaskIdList = None
        self._MemberId = None

    @property
    def TaskIdList(self):
        r"""任务id 列表
        :rtype: list of TaskIdListKey
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskResponse(AbstractModel):
    r"""StopRiskCenterTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Status为0， 停止成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Status为0， 停止成功
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SubUserInfo(AbstractModel):
    r"""子账号详情

    """

    def __init__(self):
        r"""
        :param _ID: 主键ID，无业务意义仅作为唯一键
        :type ID: int
        :param _AppID: 子账号Appid
        :type AppID: str
        :param _Uin: 子账号UIn
        :type Uin: str
        :param _NickName: 子账号名称
        :type NickName: str
        :param _OwnerAppID: 主账号Appid
        :type OwnerAppID: str
        :param _OwnerUin: 主账号Uin
        :type OwnerUin: str
        :param _OwnerNickName: 主账号名称
        :type OwnerNickName: str
        :param _OwnerMemberID: 所属主账号memberId信息
        :type OwnerMemberID: str
        :param _CloudType: 账户类型，0为腾讯云账户，1为AWS账户
        :type CloudType: int
        :param _ServiceCount: 可访问服务数量
        :type ServiceCount: int
        :param _InterfaceCount: 可访问接口数量
        :type InterfaceCount: int
        :param _AssetCount: 可访问资源数量
        :type AssetCount: int
        :param _LogCount: 访问/行为日志数量
        :type LogCount: int
        :param _ConfigRiskCount: 权限配置风险
        :type ConfigRiskCount: int
        :param _ActionRiskCount: 危险行为告警
        :type ActionRiskCount: int
        :param _IsAccessCloudAudit: 是否接入操作审计日志
        :type IsAccessCloudAudit: bool
        :param _IsAccessCheck: 是否配置风险的安全体检
        :type IsAccessCheck: bool
        :param _IsAccessUeba: 是否配置用户行为管理策略
        :type IsAccessUeba: bool
        """
        self._ID = None
        self._AppID = None
        self._Uin = None
        self._NickName = None
        self._OwnerAppID = None
        self._OwnerUin = None
        self._OwnerNickName = None
        self._OwnerMemberID = None
        self._CloudType = None
        self._ServiceCount = None
        self._InterfaceCount = None
        self._AssetCount = None
        self._LogCount = None
        self._ConfigRiskCount = None
        self._ActionRiskCount = None
        self._IsAccessCloudAudit = None
        self._IsAccessCheck = None
        self._IsAccessUeba = None

    @property
    def ID(self):
        r"""主键ID，无业务意义仅作为唯一键
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AppID(self):
        r"""子账号Appid
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""子账号UIn
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""子账号名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def OwnerAppID(self):
        r"""主账号Appid
        :rtype: str
        """
        return self._OwnerAppID

    @OwnerAppID.setter
    def OwnerAppID(self, OwnerAppID):
        self._OwnerAppID = OwnerAppID

    @property
    def OwnerUin(self):
        r"""主账号Uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OwnerNickName(self):
        r"""主账号名称
        :rtype: str
        """
        return self._OwnerNickName

    @OwnerNickName.setter
    def OwnerNickName(self, OwnerNickName):
        self._OwnerNickName = OwnerNickName

    @property
    def OwnerMemberID(self):
        r"""所属主账号memberId信息
        :rtype: str
        """
        return self._OwnerMemberID

    @OwnerMemberID.setter
    def OwnerMemberID(self, OwnerMemberID):
        self._OwnerMemberID = OwnerMemberID

    @property
    def CloudType(self):
        r"""账户类型，0为腾讯云账户，1为AWS账户
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def ServiceCount(self):
        r"""可访问服务数量
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def InterfaceCount(self):
        r"""可访问接口数量
        :rtype: int
        """
        return self._InterfaceCount

    @InterfaceCount.setter
    def InterfaceCount(self, InterfaceCount):
        self._InterfaceCount = InterfaceCount

    @property
    def AssetCount(self):
        r"""可访问资源数量
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def LogCount(self):
        r"""访问/行为日志数量
        :rtype: int
        """
        return self._LogCount

    @LogCount.setter
    def LogCount(self, LogCount):
        self._LogCount = LogCount

    @property
    def ConfigRiskCount(self):
        r"""权限配置风险
        :rtype: int
        """
        return self._ConfigRiskCount

    @ConfigRiskCount.setter
    def ConfigRiskCount(self, ConfigRiskCount):
        self._ConfigRiskCount = ConfigRiskCount

    @property
    def ActionRiskCount(self):
        r"""危险行为告警
        :rtype: int
        """
        return self._ActionRiskCount

    @ActionRiskCount.setter
    def ActionRiskCount(self, ActionRiskCount):
        self._ActionRiskCount = ActionRiskCount

    @property
    def IsAccessCloudAudit(self):
        r"""是否接入操作审计日志
        :rtype: bool
        """
        return self._IsAccessCloudAudit

    @IsAccessCloudAudit.setter
    def IsAccessCloudAudit(self, IsAccessCloudAudit):
        self._IsAccessCloudAudit = IsAccessCloudAudit

    @property
    def IsAccessCheck(self):
        r"""是否配置风险的安全体检
        :rtype: bool
        """
        return self._IsAccessCheck

    @IsAccessCheck.setter
    def IsAccessCheck(self, IsAccessCheck):
        self._IsAccessCheck = IsAccessCheck

    @property
    def IsAccessUeba(self):
        r"""是否配置用户行为管理策略
        :rtype: bool
        """
        return self._IsAccessUeba

    @IsAccessUeba.setter
    def IsAccessUeba(self, IsAccessUeba):
        self._IsAccessUeba = IsAccessUeba


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._OwnerAppID = params.get("OwnerAppID")
        self._OwnerUin = params.get("OwnerUin")
        self._OwnerNickName = params.get("OwnerNickName")
        self._OwnerMemberID = params.get("OwnerMemberID")
        self._CloudType = params.get("CloudType")
        self._ServiceCount = params.get("ServiceCount")
        self._InterfaceCount = params.get("InterfaceCount")
        self._AssetCount = params.get("AssetCount")
        self._LogCount = params.get("LogCount")
        self._ConfigRiskCount = params.get("ConfigRiskCount")
        self._ActionRiskCount = params.get("ActionRiskCount")
        self._IsAccessCloudAudit = params.get("IsAccessCloudAudit")
        self._IsAccessCheck = params.get("IsAccessCheck")
        self._IsAccessUeba = params.get("IsAccessUeba")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetAsset(AbstractModel):
    r"""子网资产

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: 资产ID
        :type AssetId: str
        :param _AssetName: 资产名
        :type AssetName: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 私有网络id
        :type VpcId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _Nick: 昵称
        :type Nick: str
        :param _CIDR: cidr
        :type CIDR: str
        :param _Zone: 可用区
        :type Zone: str
        :param _CVM: cvm数
        :type CVM: int
        :param _AvailableIp: 可用ip数
        :type AvailableIp: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param _ScanTask: 任务数
        :type ScanTask: int
        :param _LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param _IsCore: 是否核心
        :type IsCore: int
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._Nick = None
        self._CIDR = None
        self._Zone = None
        self._CVM = None
        self._AvailableIp = None
        self._CreateTime = None
        self._ConfigureRisk = None
        self._ScanTask = None
        self._LastScanTime = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""资产ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""私有网络id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""私有网络名
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Nick(self):
        r"""昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def CIDR(self):
        r"""cidr
        :rtype: str
        """
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

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
    def CVM(self):
        r"""cvm数
        :rtype: int
        """
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def AvailableIp(self):
        r"""可用ip数
        :rtype: int
        """
        return self._AvailableIp

    @AvailableIp.setter
    def AvailableIp(self, AvailableIp):
        self._AvailableIp = AvailableIp

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConfigureRisk(self):
        r"""配置风险
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def ScanTask(self):
        r"""任务数
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""最后扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def IsCore(self):
        r"""是否核心
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._Nick = params.get("Nick")
        self._CIDR = params.get("CIDR")
        self._Zone = params.get("Zone")
        self._CVM = params.get("CVM")
        self._AvailableIp = params.get("AvailableIp")
        self._CreateTime = params.get("CreateTime")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
        :type Name: str
        :param _Value: 标签内容
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""标签名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""标签内容
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagCount(AbstractModel):
    r"""产品日志条数

    """

    def __init__(self):
        r"""
        :param _Name: 产品名
        :type Name: str
        :param _Count: 日志条数
        :type Count: int
        """
        self._Name = None
        self._Count = None

    @property
    def Name(self):
        r"""产品名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        r"""日志条数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    r"""主机标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 主机标签key
        :type TagKey: str
        :param _TagValue: 主机标签value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""主机标签key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""主机标签value
        :rtype: str
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
        


class TaskAdvanceCFG(AbstractModel):
    r"""任务高级配置

    """

    def __init__(self):
        r"""
        :param _PortRisk: 端口风险高级配置
        :type PortRisk: list of PortRiskAdvanceCFGParamItem
        :param _VulRisk: 漏洞风险高级配置
        :type VulRisk: list of TaskCenterVulRiskInputParam
        :param _WeakPwdRisk: 弱口令风险高级配置
        :type WeakPwdRisk: list of TaskCenterWeakPwdRiskInputParam
        :param _CFGRisk: 配置风险高级配置
        :type CFGRisk: list of TaskCenterCFGRiskInputParam
        """
        self._PortRisk = None
        self._VulRisk = None
        self._WeakPwdRisk = None
        self._CFGRisk = None

    @property
    def PortRisk(self):
        r"""端口风险高级配置
        :rtype: list of PortRiskAdvanceCFGParamItem
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulRisk(self):
        r"""漏洞风险高级配置
        :rtype: list of TaskCenterVulRiskInputParam
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def WeakPwdRisk(self):
        r"""弱口令风险高级配置
        :rtype: list of TaskCenterWeakPwdRiskInputParam
        """
        return self._WeakPwdRisk

    @WeakPwdRisk.setter
    def WeakPwdRisk(self, WeakPwdRisk):
        self._WeakPwdRisk = WeakPwdRisk

    @property
    def CFGRisk(self):
        r"""配置风险高级配置
        :rtype: list of TaskCenterCFGRiskInputParam
        """
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk


    def _deserialize(self, params):
        if params.get("PortRisk") is not None:
            self._PortRisk = []
            for item in params.get("PortRisk"):
                obj = PortRiskAdvanceCFGParamItem()
                obj._deserialize(item)
                self._PortRisk.append(obj)
        if params.get("VulRisk") is not None:
            self._VulRisk = []
            for item in params.get("VulRisk"):
                obj = TaskCenterVulRiskInputParam()
                obj._deserialize(item)
                self._VulRisk.append(obj)
        if params.get("WeakPwdRisk") is not None:
            self._WeakPwdRisk = []
            for item in params.get("WeakPwdRisk"):
                obj = TaskCenterWeakPwdRiskInputParam()
                obj._deserialize(item)
                self._WeakPwdRisk.append(obj)
        if params.get("CFGRisk") is not None:
            self._CFGRisk = []
            for item in params.get("CFGRisk"):
                obj = TaskCenterCFGRiskInputParam()
                obj._deserialize(item)
                self._CFGRisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAssetObject(AbstractModel):
    r"""任务资产项

    """

    def __init__(self):
        r"""
        :param _AssetName: 资产名
        :type AssetName: str
        :param _InstanceType: 资产类型
        :type InstanceType: str
        :param _AssetType: 资产分类
        :type AssetType: str
        :param _Asset: ip/域名/资产id，数据库id等
        :type Asset: str
        :param _Region: 地域
        :type Region: str
        :param _Arn: 多云资产唯一id
        :type Arn: str
        """
        self._AssetName = None
        self._InstanceType = None
        self._AssetType = None
        self._Asset = None
        self._Region = None
        self._Arn = None

    @property
    def AssetName(self):
        r"""资产名
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceType(self):
        r"""资产类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AssetType(self):
        r"""资产分类
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Asset(self):
        r"""ip/域名/资产id，数据库id等
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Arn(self):
        r"""多云资产唯一id
        :rtype: str
        """
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._InstanceType = params.get("InstanceType")
        self._AssetType = params.get("AssetType")
        self._Asset = params.get("Asset")
        self._Region = params.get("Region")
        self._Arn = params.get("Arn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterCFGRiskInputParam(AbstractModel):
    r"""配置风险高级配置

    """

    def __init__(self):
        r"""
        :param _ItemId: 检测项ID
        :type ItemId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        :param _ResourceType: 资源类型
        :type ResourceType: str
        """
        self._ItemId = None
        self._Enable = None
        self._ResourceType = None

    @property
    def ItemId(self):
        r"""检测项ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def Enable(self):
        r"""是否开启，0-不开启，1-开启
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._Enable = params.get("Enable")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterVulRiskInputParam(AbstractModel):
    r"""漏洞风险高级配置

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._RiskId = None
        self._Enable = None

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def Enable(self):
        r"""是否开启，0-不开启，1-开启
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterWeakPwdRiskInputParam(AbstractModel):
    r"""弱口令风险高级配置

    """

    def __init__(self):
        r"""
        :param _CheckItemId: 检测项ID
        :type CheckItemId: int
        :param _Enable: 是否开启，0-不开启，1-开启
        :type Enable: int
        """
        self._CheckItemId = None
        self._Enable = None

    @property
    def CheckItemId(self):
        r"""检测项ID
        :rtype: int
        """
        return self._CheckItemId

    @CheckItemId.setter
    def CheckItemId(self, CheckItemId):
        self._CheckItemId = CheckItemId

    @property
    def Enable(self):
        r"""是否开启，0-不开启，1-开启
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._CheckItemId = params.get("CheckItemId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskIdListKey(AbstractModel):
    r"""任务ID列表Key

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TargetAppId: APP ID
        :type TargetAppId: str
        """
        self._TaskId = None
        self._TargetAppId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TargetAppId(self):
        r"""APP ID
        :rtype: str
        """
        return self._TargetAppId

    @TargetAppId.setter
    def TargetAppId(self, TargetAppId):
        self._TargetAppId = TargetAppId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TargetAppId = params.get("TargetAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogInfo(AbstractModel):
    r"""任务报告信息

    """

    def __init__(self):
        r"""
        :param _TaskLogName: 报告名称
        :type TaskLogName: str
        :param _TaskLogId: 报告ID
        :type TaskLogId: str
        :param _AssetsNumber: 关联资产个数
        :type AssetsNumber: int
        :param _RiskNumber: 安全风险数量
        :type RiskNumber: int
        :param _Time: 报告生成时间
        :type Time: str
        :param _Status: 任务状态码：0 初始值  1正在扫描  2扫描完成  3扫描出错，4停止，5暂停，6该任务已被重启过
        :type Status: int
        :param _TaskName: 关联任务名称
        :type TaskName: str
        :param _StartTime: 扫描开始时间
        :type StartTime: str
        :param _TaskCenterTaskId: 任务中心扫描任务ID
        :type TaskCenterTaskId: str
        :param _AppId: 租户ID
        :type AppId: str
        :param _UIN: 主账户ID
        :type UIN: str
        :param _UserName: 用户名称
        :type UserName: str
        :param _ReportType: 报告类型： 1安全体检 2日报 3周报 4月报
        :type ReportType: int
        :param _TemplateId: 报告模板id
        :type TemplateId: int
        """
        self._TaskLogName = None
        self._TaskLogId = None
        self._AssetsNumber = None
        self._RiskNumber = None
        self._Time = None
        self._Status = None
        self._TaskName = None
        self._StartTime = None
        self._TaskCenterTaskId = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._ReportType = None
        self._TemplateId = None

    @property
    def TaskLogName(self):
        r"""报告名称
        :rtype: str
        """
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def TaskLogId(self):
        r"""报告ID
        :rtype: str
        """
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId

    @property
    def AssetsNumber(self):
        r"""关联资产个数
        :rtype: int
        """
        return self._AssetsNumber

    @AssetsNumber.setter
    def AssetsNumber(self, AssetsNumber):
        self._AssetsNumber = AssetsNumber

    @property
    def RiskNumber(self):
        r"""安全风险数量
        :rtype: int
        """
        return self._RiskNumber

    @RiskNumber.setter
    def RiskNumber(self, RiskNumber):
        self._RiskNumber = RiskNumber

    @property
    def Time(self):
        r"""报告生成时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        r"""任务状态码：0 初始值  1正在扫描  2扫描完成  3扫描出错，4停止，5暂停，6该任务已被重启过
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskName(self):
        r"""关联任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""扫描开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskCenterTaskId(self):
        r"""任务中心扫描任务ID
        :rtype: str
        """
        return self._TaskCenterTaskId

    @TaskCenterTaskId.setter
    def TaskCenterTaskId(self, TaskCenterTaskId):
        self._TaskCenterTaskId = TaskCenterTaskId

    @property
    def AppId(self):
        r"""租户ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""主账户ID
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

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
    def ReportType(self):
        r"""报告类型： 1安全体检 2日报 3周报 4月报
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def TemplateId(self):
        r"""报告模板id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TaskLogName = params.get("TaskLogName")
        self._TaskLogId = params.get("TaskLogId")
        self._AssetsNumber = params.get("AssetsNumber")
        self._RiskNumber = params.get("RiskNumber")
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._TaskCenterTaskId = params.get("TaskCenterTaskId")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._ReportType = params.get("ReportType")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogURL(AbstractModel):
    r"""报告pdf下载的临时链接

    """

    def __init__(self):
        r"""
        :param _URL: 报告下载临时链接
        :type URL: str
        :param _LogId: 任务报告id
        :type LogId: str
        :param _TaskLogName: 任务报告名称
        :type TaskLogName: str
        :param _AppId: APP ID
        :type AppId: str
        """
        self._URL = None
        self._LogId = None
        self._TaskLogName = None
        self._AppId = None

    @property
    def URL(self):
        r"""报告下载临时链接
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def LogId(self):
        r"""任务报告id
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskLogName(self):
        r"""任务报告名称
        :rtype: str
        """
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def AppId(self):
        r"""APP ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._LogId = params.get("LogId")
        self._TaskLogName = params.get("TaskLogName")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UebaCustomRule(AbstractModel):
    r"""用户行为分析  自定义策略结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 策略名称
        :type RuleName: str
        :param _UserType: 1: 云账号
2: 自定义用户
        :type UserType: int
        :param _TimeInterval: 发生时间
1：10分钟
2：1小时
3：一天
4：一周
5：一个月
        :type TimeInterval: int
        :param _EventContent: 发生事件
        :type EventContent: :class:`tencentcloud.csip.v20221121.models.UebaEventContent`
        :param _AlertName: 告警名称
        :type AlertName: str
        :param _AlterLevel: 告警类型
0:  提示
1:  低危
2:  中危
3:  高危
4:  严重
        :type AlterLevel: int
        :param _Operator: 操作者
        :type Operator: list of str
        :param _OperateObject: 操作对象
        :type OperateObject: list of str
        :param _OperateMethod: 操作方式
        :type OperateMethod: list of str
        :param _LogType: 日志类型
        :type LogType: str
        :param _LogTypeStr: 日志中文名
        :type LogTypeStr: str
        """
        self._RuleName = None
        self._UserType = None
        self._TimeInterval = None
        self._EventContent = None
        self._AlertName = None
        self._AlterLevel = None
        self._Operator = None
        self._OperateObject = None
        self._OperateMethod = None
        self._LogType = None
        self._LogTypeStr = None

    @property
    def RuleName(self):
        r"""策略名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def UserType(self):
        r"""1: 云账号
2: 自定义用户
        :rtype: int
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TimeInterval(self):
        r"""发生时间
1：10分钟
2：1小时
3：一天
4：一周
5：一个月
        :rtype: int
        """
        return self._TimeInterval

    @TimeInterval.setter
    def TimeInterval(self, TimeInterval):
        self._TimeInterval = TimeInterval

    @property
    def EventContent(self):
        r"""发生事件
        :rtype: :class:`tencentcloud.csip.v20221121.models.UebaEventContent`
        """
        return self._EventContent

    @EventContent.setter
    def EventContent(self, EventContent):
        self._EventContent = EventContent

    @property
    def AlertName(self):
        r"""告警名称
        :rtype: str
        """
        return self._AlertName

    @AlertName.setter
    def AlertName(self, AlertName):
        self._AlertName = AlertName

    @property
    def AlterLevel(self):
        r"""告警类型
0:  提示
1:  低危
2:  中危
3:  高危
4:  严重
        :rtype: int
        """
        return self._AlterLevel

    @AlterLevel.setter
    def AlterLevel(self, AlterLevel):
        self._AlterLevel = AlterLevel

    @property
    def Operator(self):
        r"""操作者
        :rtype: list of str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def OperateObject(self):
        r"""操作对象
        :rtype: list of str
        """
        return self._OperateObject

    @OperateObject.setter
    def OperateObject(self, OperateObject):
        self._OperateObject = OperateObject

    @property
    def OperateMethod(self):
        r"""操作方式
        :rtype: list of str
        """
        return self._OperateMethod

    @OperateMethod.setter
    def OperateMethod(self, OperateMethod):
        self._OperateMethod = OperateMethod

    @property
    def LogType(self):
        r"""日志类型
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def LogTypeStr(self):
        r"""日志中文名
        :rtype: str
        """
        return self._LogTypeStr

    @LogTypeStr.setter
    def LogTypeStr(self, LogTypeStr):
        self._LogTypeStr = LogTypeStr


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._UserType = params.get("UserType")
        self._TimeInterval = params.get("TimeInterval")
        if params.get("EventContent") is not None:
            self._EventContent = UebaEventContent()
            self._EventContent._deserialize(params.get("EventContent"))
        self._AlertName = params.get("AlertName")
        self._AlterLevel = params.get("AlterLevel")
        self._Operator = params.get("Operator")
        self._OperateObject = params.get("OperateObject")
        self._OperateMethod = params.get("OperateMethod")
        self._LogType = params.get("LogType")
        self._LogTypeStr = params.get("LogTypeStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UebaEventContent(AbstractModel):
    r"""用户行为分析 发生事件结构体

    """

    def __init__(self):
        r"""
        :param _EventType: 发生事件类型
1:语句检索
2:过滤检索
        :type EventType: int
        :param _Content: 语句检索内容
        :type Content: str
        :param _Filters: 检索条件

        :type Filters: list of WhereFilter
        :param _StatisticalFilter: 统计条件
        :type StatisticalFilter: :class:`tencentcloud.csip.v20221121.models.StatisticalFilter`
        """
        self._EventType = None
        self._Content = None
        self._Filters = None
        self._StatisticalFilter = None

    @property
    def EventType(self):
        r"""发生事件类型
1:语句检索
2:过滤检索
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Content(self):
        r"""语句检索内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Filters(self):
        r"""检索条件

        :rtype: list of WhereFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StatisticalFilter(self):
        r"""统计条件
        :rtype: :class:`tencentcloud.csip.v20221121.models.StatisticalFilter`
        """
        return self._StatisticalFilter

    @StatisticalFilter.setter
    def StatisticalFilter(self, StatisticalFilter):
        self._StatisticalFilter = StatisticalFilter


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._Content = params.get("Content")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("StatisticalFilter") is not None:
            self._StatisticalFilter = StatisticalFilter()
            self._StatisticalFilter._deserialize(params.get("StatisticalFilter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UebaRule(AbstractModel):
    r"""用户行为分析策略

    """

    def __init__(self):
        r"""
        :param _RuleID: 策略id
        :type RuleID: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleType: 策略类型
0:系统策略
1:自定义策略
        :type RuleType: int
        :param _RuleLevel: 策略等级
0:提示
1:低危
2:中危
3:高危
4:严重
        :type RuleLevel: int
        :param _RuleContent: 策略内容
        :type RuleContent: str
        :param _RuleStatus: 策略开关
        :type RuleStatus: bool
        :param _HitCount: 命中次数
        :type HitCount: int
        :param _AppID: 所属账号Appid
        :type AppID: str
        :param _MemberID: 多账号，成员ID
        :type MemberID: str
        :param _Uin: Uin
        :type Uin: str
        :param _Nickname: 昵称
        :type Nickname: str
        :param _CustomRuleDetail: 自定义规则具体内容
        :type CustomRuleDetail: :class:`tencentcloud.csip.v20221121.models.UebaCustomRule`
        :param _CloudType: 云类型
腾讯云：0
aws：1
        :type CloudType: int
        """
        self._RuleID = None
        self._RuleName = None
        self._RuleType = None
        self._RuleLevel = None
        self._RuleContent = None
        self._RuleStatus = None
        self._HitCount = None
        self._AppID = None
        self._MemberID = None
        self._Uin = None
        self._Nickname = None
        self._CustomRuleDetail = None
        self._CloudType = None

    @property
    def RuleID(self):
        r"""策略id
        :rtype: str
        """
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleType(self):
        r"""策略类型
0:系统策略
1:自定义策略
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleLevel(self):
        r"""策略等级
0:提示
1:低危
2:中危
3:高危
4:严重
        :rtype: int
        """
        return self._RuleLevel

    @RuleLevel.setter
    def RuleLevel(self, RuleLevel):
        self._RuleLevel = RuleLevel

    @property
    def RuleContent(self):
        r"""策略内容
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def RuleStatus(self):
        r"""策略开关
        :rtype: bool
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def HitCount(self):
        r"""命中次数
        :rtype: int
        """
        return self._HitCount

    @HitCount.setter
    def HitCount(self, HitCount):
        self._HitCount = HitCount

    @property
    def AppID(self):
        r"""所属账号Appid
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def MemberID(self):
        r"""多账号，成员ID
        :rtype: str
        """
        return self._MemberID

    @MemberID.setter
    def MemberID(self, MemberID):
        self._MemberID = MemberID

    @property
    def Uin(self):
        r"""Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
    def CustomRuleDetail(self):
        r"""自定义规则具体内容
        :rtype: :class:`tencentcloud.csip.v20221121.models.UebaCustomRule`
        """
        return self._CustomRuleDetail

    @CustomRuleDetail.setter
    def CustomRuleDetail(self, CustomRuleDetail):
        self._CustomRuleDetail = CustomRuleDetail

    @property
    def CloudType(self):
        r"""云类型
腾讯云：0
aws：1
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._RuleName = params.get("RuleName")
        self._RuleType = params.get("RuleType")
        self._RuleLevel = params.get("RuleLevel")
        self._RuleContent = params.get("RuleContent")
        self._RuleStatus = params.get("RuleStatus")
        self._HitCount = params.get("HitCount")
        self._AppID = params.get("AppID")
        self._MemberID = params.get("MemberID")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        if params.get("CustomRuleDetail") is not None:
            self._CustomRuleDetail = UebaCustomRule()
            self._CustomRuleDetail._deserialize(params.get("CustomRuleDetail"))
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyAlarmStatusRequest(AbstractModel):
    r"""UpdateAccessKeyAlarmStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态  0:未处理 1:已处理 2:已忽略
        :type Status: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _AlarmIDList: 告警ID列表
        :type AlarmIDList: list of int
        :param _RiskIDList: 风险ID列表
        :type RiskIDList: list of int
        """
        self._Status = None
        self._MemberId = None
        self._AlarmIDList = None
        self._RiskIDList = None

    @property
    def Status(self):
        r"""状态  0:未处理 1:已处理 2:已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AlarmIDList(self):
        r"""告警ID列表
        :rtype: list of int
        """
        return self._AlarmIDList

    @AlarmIDList.setter
    def AlarmIDList(self, AlarmIDList):
        self._AlarmIDList = AlarmIDList

    @property
    def RiskIDList(self):
        r"""风险ID列表
        :rtype: list of int
        """
        return self._RiskIDList

    @RiskIDList.setter
    def RiskIDList(self, RiskIDList):
        self._RiskIDList = RiskIDList


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MemberId = params.get("MemberId")
        self._AlarmIDList = params.get("AlarmIDList")
        self._RiskIDList = params.get("RiskIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyAlarmStatusResponse(AbstractModel):
    r"""UpdateAccessKeyAlarmStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 0成功，1失败
        :type Code: int
        :param _Msg: 错误信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0成功，1失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""错误信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class UpdateAccessKeyRemarkRequest(AbstractModel):
    r"""UpdateAccessKeyRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Remark: 备注
        :type Remark: str
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _SourceIPList: 源IP 名称
        :type SourceIPList: list of str
        :param _AccessKeyList: ak名称
        :type AccessKeyList: list of str
        :param _SourceIPIDList: 源IP的ID
        :type SourceIPIDList: list of int non-negative
        :param _AccessKeyIDList: AK的ID
        :type AccessKeyIDList: list of int non-negative
        """
        self._Remark = None
        self._MemberId = None
        self._SourceIPList = None
        self._AccessKeyList = None
        self._SourceIPIDList = None
        self._AccessKeyIDList = None

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def SourceIPList(self):
        r"""源IP 名称
        :rtype: list of str
        """
        return self._SourceIPList

    @SourceIPList.setter
    def SourceIPList(self, SourceIPList):
        self._SourceIPList = SourceIPList

    @property
    def AccessKeyList(self):
        r"""ak名称
        :rtype: list of str
        """
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList

    @property
    def SourceIPIDList(self):
        r"""源IP的ID
        :rtype: list of int non-negative
        """
        return self._SourceIPIDList

    @SourceIPIDList.setter
    def SourceIPIDList(self, SourceIPIDList):
        self._SourceIPIDList = SourceIPIDList

    @property
    def AccessKeyIDList(self):
        r"""AK的ID
        :rtype: list of int non-negative
        """
        return self._AccessKeyIDList

    @AccessKeyIDList.setter
    def AccessKeyIDList(self, AccessKeyIDList):
        self._AccessKeyIDList = AccessKeyIDList


    def _deserialize(self, params):
        self._Remark = params.get("Remark")
        self._MemberId = params.get("MemberId")
        self._SourceIPList = params.get("SourceIPList")
        self._AccessKeyList = params.get("AccessKeyList")
        self._SourceIPIDList = params.get("SourceIPIDList")
        self._AccessKeyIDList = params.get("AccessKeyIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyRemarkResponse(AbstractModel):
    r"""UpdateAccessKeyRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 0:成功 1:失败
        :type Code: int
        :param _Msg: 错误信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0:成功 1:失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""错误信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class UpdateAlertStatusListRequest(AbstractModel):
    r"""UpdateAlertStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 告警ID列表
        :type ID: list of NewAlertKey
        :param _OperateType: 操作类型 
1:撤销处置 
2:标记为已处置 
3:标记忽略 
4:取消标记处置
5:取消标记忽略
        :type OperateType: int
        :param _MemberId: 集团账号的成员id
        :type MemberId: list of str
        :param _OperatedMemberId: 被调用的集团账号的成员id
        :type OperatedMemberId: list of str
        """
        self._ID = None
        self._OperateType = None
        self._MemberId = None
        self._OperatedMemberId = None

    @property
    def ID(self):
        r"""告警ID列表
        :rtype: list of NewAlertKey
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def OperateType(self):
        r"""操作类型 
1:撤销处置 
2:标记为已处置 
3:标记忽略 
4:取消标记处置
5:取消标记忽略
        :rtype: int
        """
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def MemberId(self):
        r"""集团账号的成员id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def OperatedMemberId(self):
        r"""被调用的集团账号的成员id
        :rtype: list of str
        """
        return self._OperatedMemberId

    @OperatedMemberId.setter
    def OperatedMemberId(self, OperatedMemberId):
        self._OperatedMemberId = OperatedMemberId


    def _deserialize(self, params):
        if params.get("ID") is not None:
            self._ID = []
            for item in params.get("ID"):
                obj = NewAlertKey()
                obj._deserialize(item)
                self._ID.append(obj)
        self._OperateType = params.get("OperateType")
        self._MemberId = params.get("MemberId")
        self._OperatedMemberId = params.get("OperatedMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertStatusListResponse(AbstractModel):
    r"""UpdateAlertStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 结果信息
        :type Msg: str
        :param _Code: 结果代码
        :type Code: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._Code = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""结果信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        r"""结果代码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class UserCallRecord(AbstractModel):
    r"""调用记录详情

    """

    def __init__(self):
        r"""
        :param _SourceIP: 调用源IP
        :type SourceIP: str
        :param _EventType: 调用类型
0:控制台调用
1:API
        :type EventType: int
        :param _CallCount: 调用次数
        :type CallCount: int
        :param _Code: 调用错误码
0表示成功
        :type Code: int
        :param _FirstCallTime: 首次调用时间
        :type FirstCallTime: str
        :param _LastCallTime: 最后调用时间
        :type LastCallTime: str
        :param _SourceIPRemark: 调用源IP备注
        :type SourceIPRemark: str
        :param _Region: 调用源IP地域
        :type Region: str
        :param _UserName: 用户/角色名称
        :type UserName: str
        :param _Date: 聚合日期
        :type Date: str
        :param _AppID: appid
        :type AppID: int
        :param _ISP: 运营商
        :type ISP: str
        """
        self._SourceIP = None
        self._EventType = None
        self._CallCount = None
        self._Code = None
        self._FirstCallTime = None
        self._LastCallTime = None
        self._SourceIPRemark = None
        self._Region = None
        self._UserName = None
        self._Date = None
        self._AppID = None
        self._ISP = None

    @property
    def SourceIP(self):
        r"""调用源IP
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def EventType(self):
        r"""调用类型
0:控制台调用
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def CallCount(self):
        r"""调用次数
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def Code(self):
        r"""调用错误码
0表示成功
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def FirstCallTime(self):
        r"""首次调用时间
        :rtype: str
        """
        return self._FirstCallTime

    @FirstCallTime.setter
    def FirstCallTime(self, FirstCallTime):
        self._FirstCallTime = FirstCallTime

    @property
    def LastCallTime(self):
        r"""最后调用时间
        :rtype: str
        """
        return self._LastCallTime

    @LastCallTime.setter
    def LastCallTime(self, LastCallTime):
        self._LastCallTime = LastCallTime

    @property
    def SourceIPRemark(self):
        r"""调用源IP备注
        :rtype: str
        """
        return self._SourceIPRemark

    @SourceIPRemark.setter
    def SourceIPRemark(self, SourceIPRemark):
        self._SourceIPRemark = SourceIPRemark

    @property
    def Region(self):
        r"""调用源IP地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UserName(self):
        r"""用户/角色名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Date(self):
        r"""聚合日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        r"""appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ISP(self):
        r"""运营商
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP


    def _deserialize(self, params):
        self._SourceIP = params.get("SourceIP")
        self._EventType = params.get("EventType")
        self._CallCount = params.get("CallCount")
        self._Code = params.get("Code")
        self._FirstCallTime = params.get("FirstCallTime")
        self._LastCallTime = params.get("LastCallTime")
        self._SourceIPRemark = params.get("SourceIPRemark")
        self._Region = params.get("Region")
        self._UserName = params.get("UserName")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._ISP = params.get("ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULBaseInfo(AbstractModel):
    r"""应急漏洞基本数据

    """

    def __init__(self):
        r"""
        :param _Level: 风险等级
high 高危/ middle 中危 / low 低危 /info 提示
        :type Level: str
        :param _Component: 组件
        :type Component: str
        :param _PublishTime: 漏洞发布时间
        :type PublishTime: str
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: int
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULName: 漏洞名
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Describe: 描述
        :type Describe: str
        :param _Payload: 漏洞payload
        :type Payload: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _References: 技术参考
        :type References: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type EMGCVulType: int
        :param _CVSS: CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: float
        :param _AttackHeat: 攻击热度
0/1/2/3 
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackHeat: int
        :param _ScanStatus: 检测状态 0 未扫描 1扫描中 2 扫描完成
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: int
        :param _IsSuggest: 1/0是否必修
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSuggest: int
        :param _VulTag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VulTag: list of str
        :param _SupportProduct: 支持产品 逗号分隔  "cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportProduct: str
        :param _TaskId: 漏洞检测任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Index: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _PcmgrID: 漏洞id 旧版
注意：此字段可能返回 null，表示取不到有效值。
        :type PcmgrID: str
        :param _TvdID: 漏洞id  新版
注意：此字段可能返回 null，表示取不到有效值。
        :type TvdID: str
        """
        self._Level = None
        self._Component = None
        self._PublishTime = None
        self._LastScanTime = None
        self._AffectAssetCount = None
        self._RiskId = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Describe = None
        self._Payload = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._Fix = None
        self._EMGCVulType = None
        self._CVSS = None
        self._AttackHeat = None
        self._ScanStatus = None
        self._IsSuggest = None
        self._VulTag = None
        self._SupportProduct = None
        self._TaskId = None
        self._Index = None
        self._PcmgrID = None
        self._TvdID = None

    @property
    def Level(self):
        r"""风险等级
high 高危/ middle 中危 / low 低危 /info 提示
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def PublishTime(self):
        r"""漏洞发布时间
        :rtype: str
        """
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime

    @property
    def LastScanTime(self):
        r"""最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def AffectAssetCount(self):
        r"""影响资产数量
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""漏洞名
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Describe(self):
        r"""描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Payload(self):
        r"""漏洞payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""技术参考
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""风险点
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Fix(self):
        r"""修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        r"""CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AttackHeat(self):
        r"""攻击热度
0/1/2/3 
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def ScanStatus(self):
        r"""检测状态 0 未扫描 1扫描中 2 扫描完成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def IsSuggest(self):
        r"""1/0是否必修
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def VulTag(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def SupportProduct(self):
        r"""支持产品 逗号分隔  "cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SupportProduct

    @SupportProduct.setter
    def SupportProduct(self, SupportProduct):
        self._SupportProduct = SupportProduct

    @property
    def TaskId(self):
        r"""漏洞检测任务id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Index(self):
        r"""主键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def PcmgrID(self):
        r"""漏洞id 旧版
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PcmgrID

    @PcmgrID.setter
    def PcmgrID(self, PcmgrID):
        self._PcmgrID = PcmgrID

    @property
    def TvdID(self):
        r"""漏洞id  新版
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._PublishTime = params.get("PublishTime")
        self._LastScanTime = params.get("LastScanTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._RiskId = params.get("RiskId")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Describe = params.get("Describe")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Fix = params.get("Fix")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._AttackHeat = params.get("AttackHeat")
        self._ScanStatus = params.get("ScanStatus")
        self._IsSuggest = params.get("IsSuggest")
        self._VulTag = params.get("VulTag")
        self._SupportProduct = params.get("SupportProduct")
        self._TaskId = params.get("TaskId")
        self._Index = params.get("Index")
        self._PcmgrID = params.get("PcmgrID")
        self._TvdID = params.get("TvdID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULRiskAdvanceCFGList(AbstractModel):
    r"""漏洞风险高级配置列表

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _VULName: 漏洞名称
        :type VULName: str
        :param _RiskLevel: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type RiskLevel: str
        :param _CheckFrom: 识别来源
        :type CheckFrom: str
        :param _Enable: 是否启用，1-启用，0-禁用
        :type Enable: int
        :param _VULType: 风险类型
        :type VULType: str
        :param _ImpactVersion: 影响版本
        :type ImpactVersion: str
        :param _CVE: CVE
        :type CVE: str
        :param _VULTag: 漏洞标签
        :type VULTag: list of str
        :param _FixMethod: 修复方式
        :type FixMethod: list of str
        :param _ReleaseTime: 披露时间
        :type ReleaseTime: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :type EMGCVulType: int
        :param _VULDescribe: 漏洞描述
        :type VULDescribe: str
        :param _ImpactComponent: 影响组件
        :type ImpactComponent: str
        :param _Payload: 漏洞Payload
        :type Payload: str
        :param _References: 技术参考
        :type References: str
        :param _CVSS: cvss评分
        :type CVSS: str
        :param _AttackHeat: 攻击热度
        :type AttackHeat: str
        :param _ServiceSupport: 安全产品支持情况
        :type ServiceSupport: list of ServiceSupport
        :param _RecentScanTime: 最新检测时间
        :type RecentScanTime: str
        """
        self._RiskId = None
        self._VULName = None
        self._RiskLevel = None
        self._CheckFrom = None
        self._Enable = None
        self._VULType = None
        self._ImpactVersion = None
        self._CVE = None
        self._VULTag = None
        self._FixMethod = None
        self._ReleaseTime = None
        self._EMGCVulType = None
        self._VULDescribe = None
        self._ImpactComponent = None
        self._Payload = None
        self._References = None
        self._CVSS = None
        self._AttackHeat = None
        self._ServiceSupport = None
        self._RecentScanTime = None

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def VULName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def RiskLevel(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CheckFrom(self):
        r"""识别来源
        :rtype: str
        """
        return self._CheckFrom

    @CheckFrom.setter
    def CheckFrom(self, CheckFrom):
        self._CheckFrom = CheckFrom

    @property
    def Enable(self):
        r"""是否启用，1-启用，0-禁用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def VULType(self):
        r"""风险类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def ImpactVersion(self):
        r"""影响版本
        :rtype: str
        """
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def CVE(self):
        r"""CVE
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def VULTag(self):
        r"""漏洞标签
        :rtype: list of str
        """
        return self._VULTag

    @VULTag.setter
    def VULTag(self, VULTag):
        self._VULTag = VULTag

    @property
    def FixMethod(self):
        r"""修复方式
        :rtype: list of str
        """
        return self._FixMethod

    @FixMethod.setter
    def FixMethod(self, FixMethod):
        self._FixMethod = FixMethod

    @property
    def ReleaseTime(self):
        r"""披露时间
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def VULDescribe(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def ImpactComponent(self):
        r"""影响组件
        :rtype: str
        """
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent

    @property
    def Payload(self):
        r"""漏洞Payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def References(self):
        r"""技术参考
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def CVSS(self):
        r"""cvss评分
        :rtype: str
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AttackHeat(self):
        r"""攻击热度
        :rtype: str
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def ServiceSupport(self):
        r"""安全产品支持情况
        :rtype: list of ServiceSupport
        """
        return self._ServiceSupport

    @ServiceSupport.setter
    def ServiceSupport(self, ServiceSupport):
        self._ServiceSupport = ServiceSupport

    @property
    def RecentScanTime(self):
        r"""最新检测时间
        :rtype: str
        """
        return self._RecentScanTime

    @RecentScanTime.setter
    def RecentScanTime(self, RecentScanTime):
        self._RecentScanTime = RecentScanTime


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._VULName = params.get("VULName")
        self._RiskLevel = params.get("RiskLevel")
        self._CheckFrom = params.get("CheckFrom")
        self._Enable = params.get("Enable")
        self._VULType = params.get("VULType")
        self._ImpactVersion = params.get("ImpactVersion")
        self._CVE = params.get("CVE")
        self._VULTag = params.get("VULTag")
        self._FixMethod = params.get("FixMethod")
        self._ReleaseTime = params.get("ReleaseTime")
        self._EMGCVulType = params.get("EMGCVulType")
        self._VULDescribe = params.get("VULDescribe")
        self._ImpactComponent = params.get("ImpactComponent")
        self._Payload = params.get("Payload")
        self._References = params.get("References")
        self._CVSS = params.get("CVSS")
        self._AttackHeat = params.get("AttackHeat")
        if params.get("ServiceSupport") is not None:
            self._ServiceSupport = []
            for item in params.get("ServiceSupport"):
                obj = ServiceSupport()
                obj._deserialize(item)
                self._ServiceSupport.append(obj)
        self._RecentScanTime = params.get("RecentScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULRiskInfo(AbstractModel):
    r"""漏洞风险信息

    """

    def __init__(self):
        r"""
        :param _Fix: 修复建议
        :type Fix: str
        :param _References: 技术参考/参考链接
        :type References: str
        :param _Describe: 漏洞描述
        :type Describe: str
        :param _ImpactComponent: 受影响组件
        :type ImpactComponent: list of VulImpactComponentInfo
        """
        self._Fix = None
        self._References = None
        self._Describe = None
        self._ImpactComponent = None

    @property
    def Fix(self):
        r"""修复建议
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def References(self):
        r"""技术参考/参考链接
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Describe(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ImpactComponent(self):
        r"""受影响组件
        :rtype: list of VulImpactComponentInfo
        """
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent


    def _deserialize(self, params):
        self._Fix = params.get("Fix")
        self._References = params.get("References")
        self._Describe = params.get("Describe")
        if params.get("ImpactComponent") is not None:
            self._ImpactComponent = []
            for item in params.get("ImpactComponent"):
                obj = VulImpactComponentInfo()
                obj._deserialize(item)
                self._ImpactComponent.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRisk(AbstractModel):
    r"""漏洞视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: str
        :param _NoHandleCount: 影响资产
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: int
        :param _Id: 风险ID
        :type Id: str
        :param _From: 扫描来源，具体看接口返回枚举类型
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULName: 漏洞名
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Describe: 描述
        :type Describe: str
        :param _Payload: 漏洞payload
        :type Payload: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _References: 技术参考
        :type References: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _Fix: 修复建议
        :type Fix: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :type EMGCVulType: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Describe = None
        self._Payload = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._Fix = None
        self._EMGCVulType = None

    @property
    def Port(self):
        r"""端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        r"""影响资产
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""影响资产数量
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""风险ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""扫描来源，具体看接口返回枚举类型
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""漏洞名
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Describe(self):
        r"""描述
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Payload(self):
        r"""漏洞payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""技术参考
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""风险点
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Fix(self):
        r"""修复建议
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Describe = params.get("Describe")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Fix = params.get("Fix")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRiskData(AbstractModel):
    r"""漏洞视角的漏洞风险对象

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: str
        :param _NoHandleCount: 影响资产
        :type NoHandleCount: int
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _Component: 组件
        :type Component: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _AffectAssetCount: 影响资产数量
        :type AffectAssetCount: int
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _From: 扫描来源，具体看接口返回枚举类型
        :type From: str
        :param _Index: 前端索引
        :type Index: str
        :param _VULType: 漏洞类型
        :type VULType: str
        :param _VULName: 漏洞名
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Payload: 漏洞payload
        :type Payload: str
        :param _AppName: 漏洞影响组件
        :type AppName: str
        :param _AppVersion: 漏洞影响版本
        :type AppVersion: str
        :param _VULURL: 风险点
        :type VULURL: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _EMGCVulType: 应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :type EMGCVulType: int
        :param _CVSS: CVSS评分
        :type CVSS: float
        :param _PCMGRId: PCMGRId
        :type PCMGRId: str
        :param _VulTag: 漏洞标签。搜索时应急 必修传参VulTag=SuggestRepair/EMGCVul
        :type VulTag: list of str
        :param _DisclosureTime: 漏洞披露时间
        :type DisclosureTime: str
        :param _AttackHeat: 攻击热度
        :type AttackHeat: int
        :param _IsSuggest: 是否必修漏洞，1-是，0-不是
        :type IsSuggest: int
        :param _HandleTaskId: 处置任务id
        :type HandleTaskId: str
        :param _EngineSource: 引擎来源
        :type EngineSource: str
        :param _VulRiskId: 新的漏洞风险id
        :type VulRiskId: str
        :param _TvdID: 新版漏洞id
        :type TvdID: str
        :param _IsOneClick: 是否可以一键体检，1-可以，0-不可以
        :type IsOneClick: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._RiskId = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Payload = None
        self._AppName = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._EMGCVulType = None
        self._CVSS = None
        self._PCMGRId = None
        self._VulTag = None
        self._DisclosureTime = None
        self._AttackHeat = None
        self._IsSuggest = None
        self._HandleTaskId = None
        self._EngineSource = None
        self._VulRiskId = None
        self._TvdID = None
        self._IsOneClick = None

    @property
    def Port(self):
        r"""端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        r"""影响资产
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""组件
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""影响资产数量
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def From(self):
        r"""扫描来源，具体看接口返回枚举类型
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""漏洞名
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Payload(self):
        r"""漏洞payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""漏洞影响组件
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        r"""漏洞影响版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""风险点
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def EMGCVulType(self):
        r"""应急漏洞类型，1-应急漏洞，0-非应急漏洞
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        r"""CVSS评分
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def PCMGRId(self):
        r"""PCMGRId
        :rtype: str
        """
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId

    @property
    def VulTag(self):
        r"""漏洞标签。搜索时应急 必修传参VulTag=SuggestRepair/EMGCVul
        :rtype: list of str
        """
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def DisclosureTime(self):
        r"""漏洞披露时间
        :rtype: str
        """
        return self._DisclosureTime

    @DisclosureTime.setter
    def DisclosureTime(self, DisclosureTime):
        self._DisclosureTime = DisclosureTime

    @property
    def AttackHeat(self):
        r"""攻击热度
        :rtype: int
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def IsSuggest(self):
        r"""是否必修漏洞，1-是，0-不是
        :rtype: int
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def HandleTaskId(self):
        r"""处置任务id
        :rtype: str
        """
        return self._HandleTaskId

    @HandleTaskId.setter
    def HandleTaskId(self, HandleTaskId):
        self._HandleTaskId = HandleTaskId

    @property
    def EngineSource(self):
        r"""引擎来源
        :rtype: str
        """
        return self._EngineSource

    @EngineSource.setter
    def EngineSource(self, EngineSource):
        self._EngineSource = EngineSource

    @property
    def VulRiskId(self):
        r"""新的漏洞风险id
        :rtype: str
        """
        return self._VulRiskId

    @VulRiskId.setter
    def VulRiskId(self, VulRiskId):
        self._VulRiskId = VulRiskId

    @property
    def TvdID(self):
        r"""新版漏洞id
        :rtype: str
        """
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID

    @property
    def IsOneClick(self):
        r"""是否可以一键体检，1-可以，0-不可以
        :rtype: int
        """
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._RiskId = params.get("RiskId")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._PCMGRId = params.get("PCMGRId")
        self._VulTag = params.get("VulTag")
        self._DisclosureTime = params.get("DisclosureTime")
        self._AttackHeat = params.get("AttackHeat")
        self._IsSuggest = params.get("IsSuggest")
        self._HandleTaskId = params.get("HandleTaskId")
        self._EngineSource = params.get("EngineSource")
        self._VulRiskId = params.get("VulRiskId")
        self._TvdID = params.get("TvdID")
        self._IsOneClick = params.get("IsOneClick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    r"""vpc列表数据

    """

    def __init__(self):
        r"""
        :param _Subnet: 子网(只支持32位)
        :type Subnet: int
        :param _ConnectedVpc: 互通vpc(只支持32位)
        :type ConnectedVpc: int
        :param _AssetId: 资产id
        :type AssetId: str
        :param _Region: region区域
        :type Region: str
        :param _CVM: 云服务器(只支持32位)
        :type CVM: int
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _DNS: dns域名
        :type DNS: list of str
        :param _AssetName: 资产名称
        :type AssetName: str
        :param _CIDR: cidr网段
        :type CIDR: str
        :param _CreateTime: 资产创建时间
        :type CreateTime: str
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _Nick: 昵称
        :type Nick: str
        :param _IsNewAsset: 是否新资产 1新
        :type IsNewAsset: int
        :param _IsCore: 是否核心资产1是 2不是
        :type IsCore: int
        """
        self._Subnet = None
        self._ConnectedVpc = None
        self._AssetId = None
        self._Region = None
        self._CVM = None
        self._Tag = None
        self._DNS = None
        self._AssetName = None
        self._CIDR = None
        self._CreateTime = None
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._IsNewAsset = None
        self._IsCore = None

    @property
    def Subnet(self):
        r"""子网(只支持32位)
        :rtype: int
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def ConnectedVpc(self):
        r"""互通vpc(只支持32位)
        :rtype: int
        """
        return self._ConnectedVpc

    @ConnectedVpc.setter
    def ConnectedVpc(self, ConnectedVpc):
        self._ConnectedVpc = ConnectedVpc

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Region(self):
        r"""region区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CVM(self):
        r"""云服务器(只支持32位)
        :rtype: int
        """
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DNS(self):
        r"""dns域名
        :rtype: list of str
        """
        return self._DNS

    @DNS.setter
    def DNS(self, DNS):
        self._DNS = DNS

    @property
    def AssetName(self):
        r"""资产名称
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CIDR(self):
        r"""cidr网段
        :rtype: str
        """
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def CreateTime(self):
        r"""资产创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsNewAsset(self):
        r"""是否新资产 1新
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def IsCore(self):
        r"""是否核心资产1是 2不是
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._Subnet = params.get("Subnet")
        self._ConnectedVpc = params.get("ConnectedVpc")
        self._AssetId = params.get("AssetId")
        self._Region = params.get("Region")
        self._CVM = params.get("CVM")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._DNS = params.get("DNS")
        self._AssetName = params.get("AssetName")
        self._CIDR = params.get("CIDR")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._IsNewAsset = params.get("IsNewAsset")
        self._IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulImpactComponentInfo(AbstractModel):
    r"""漏洞影响组件信息

    """

    def __init__(self):
        r"""
        :param _Component: 组件名称
        :type Component: str
        :param _Version: 版本名称
        :type Version: str
        """
        self._Component = None
        self._Version = None

    @property
    def Component(self):
        r"""组件名称
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Version(self):
        r"""版本名称
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Component = params.get("Component")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulRiskItem(AbstractModel):
    r"""主机漏洞风险内容

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: 云账号ID
        :type CloudAccountID: str
        :param _AssetID: 实例ID
        :type AssetID: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _VulName: 漏洞名称
        :type VulName: str
        :param _VulCategory: 漏洞类型
        :type VulCategory: str
        :param _VulLevel: 漏洞等级
        :type VulLevel: str
        :param _CveID: CVE编号
        :type CveID: str
        :param _Description: 漏洞描述
        :type Description: str
        :param _ContainerID: 容器ID
        :type ContainerID: str
        :param _Fix: 漏洞风险修复建议
        :type Fix: str
        :param _VulCategoryName: Linux漏洞
        :type VulCategoryName: str
        :param _VulLevelName: 漏洞等级名称
        :type VulLevelName: str
        :param _InstanceStatusName: 实例状态中文信息
        :type InstanceStatusName: str
        :param _AppID: 租户ID
        :type AppID: int
        """
        self._CloudAccountID = None
        self._AssetID = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._VulName = None
        self._VulCategory = None
        self._VulLevel = None
        self._CveID = None
        self._Description = None
        self._ContainerID = None
        self._Fix = None
        self._VulCategoryName = None
        self._VulLevelName = None
        self._InstanceStatusName = None
        self._AppID = None

    @property
    def CloudAccountID(self):
        r"""云账号ID
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def AssetID(self):
        r"""实例ID
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID

    @property
    def InstanceStatus(self):
        r"""实例状态
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def VulName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulCategory(self):
        r"""漏洞类型
        :rtype: str
        """
        return self._VulCategory

    @VulCategory.setter
    def VulCategory(self, VulCategory):
        self._VulCategory = VulCategory

    @property
    def VulLevel(self):
        r"""漏洞等级
        :rtype: str
        """
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def CveID(self):
        r"""CVE编号
        :rtype: str
        """
        return self._CveID

    @CveID.setter
    def CveID(self, CveID):
        self._CveID = CveID

    @property
    def Description(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ContainerID(self):
        r"""容器ID
        :rtype: str
        """
        return self._ContainerID

    @ContainerID.setter
    def ContainerID(self, ContainerID):
        self._ContainerID = ContainerID

    @property
    def Fix(self):
        r"""漏洞风险修复建议
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def VulCategoryName(self):
        r"""Linux漏洞
        :rtype: str
        """
        return self._VulCategoryName

    @VulCategoryName.setter
    def VulCategoryName(self, VulCategoryName):
        self._VulCategoryName = VulCategoryName

    @property
    def VulLevelName(self):
        r"""漏洞等级名称
        :rtype: str
        """
        return self._VulLevelName

    @VulLevelName.setter
    def VulLevelName(self, VulLevelName):
        self._VulLevelName = VulLevelName

    @property
    def InstanceStatusName(self):
        r"""实例状态中文信息
        :rtype: str
        """
        return self._InstanceStatusName

    @InstanceStatusName.setter
    def InstanceStatusName(self, InstanceStatusName):
        self._InstanceStatusName = InstanceStatusName

    @property
    def AppID(self):
        r"""租户ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._AssetID = params.get("AssetID")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._VulName = params.get("VulName")
        self._VulCategory = params.get("VulCategory")
        self._VulLevel = params.get("VulLevel")
        self._CveID = params.get("CveID")
        self._Description = params.get("Description")
        self._ContainerID = params.get("ContainerID")
        self._Fix = params.get("Fix")
        self._VulCategoryName = params.get("VulCategoryName")
        self._VulLevelName = params.get("VulLevelName")
        self._InstanceStatusName = params.get("InstanceStatusName")
        self._AppID = params.get("AppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTrend(AbstractModel):
    r"""漏洞趋势-攻击趋势、影响用户、影响资产

    """

    def __init__(self):
        r"""
        :param _AffectAssetCount: 影响的资产数
        :type AffectAssetCount: int
        :param _AffectUserCount: 影响的用户数
        :type AffectUserCount: int
        :param _AttackCount: 攻击数
        :type AttackCount: int
        :param _Date: 时间
        :type Date: str
        """
        self._AffectAssetCount = None
        self._AffectUserCount = None
        self._AttackCount = None
        self._Date = None

    @property
    def AffectAssetCount(self):
        r"""影响的资产数
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def AffectUserCount(self):
        r"""影响的用户数
        :rtype: int
        """
        return self._AffectUserCount

    @AffectUserCount.setter
    def AffectUserCount(self, AffectUserCount):
        self._AffectUserCount = AffectUserCount

    @property
    def AttackCount(self):
        r"""攻击数
        :rtype: int
        """
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Date(self):
        r"""时间
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._AffectUserCount = params.get("AffectUserCount")
        self._AttackCount = params.get("AttackCount")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebsiteRisk(AbstractModel):
    r"""网站风险对象

    """

    def __init__(self):
        r"""
        :param _AffectAsset: 影响资产
        :type AffectAsset: str
        :param _Level: 风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :type Level: str
        :param _RecentTime: 最近识别时间
        :type RecentTime: str
        :param _FirstTime: 首次识别时间
        :type FirstTime: str
        :param _Status: 状态，0未处理、1已处置、2已忽略
        :type Status: int
        :param _Id: ID,处理风险使用
        :type Id: str
        :param _Index: 前端索引
        :type Index: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _AppId: 用户appid
        :type AppId: str
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Uin: 用户uin
        :type Uin: str
        :param _URL: 风险链接
        :type URL: str
        :param _URLPath: 风险文件地址
        :type URLPath: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _DetectEngine: 类型
        :type DetectEngine: str
        :param _ResultDescribe: 结果描述
        :type ResultDescribe: str
        :param _SourceURL: 源地址url
        :type SourceURL: str
        :param _SourceURLPath: 源文件地址
        :type SourceURLPath: str
        """
        self._AffectAsset = None
        self._Level = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._URL = None
        self._URLPath = None
        self._InstanceType = None
        self._DetectEngine = None
        self._ResultDescribe = None
        self._SourceURL = None
        self._SourceURLPath = None

    @property
    def AffectAsset(self):
        r"""影响资产
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""风险等级，low-低危，high-高危，middle-中危，info-提示，extreme-严重。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RecentTime(self):
        r"""最近识别时间
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""首次识别时间
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""状态，0未处理、1已处置、2已忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""ID,处理风险使用
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""前端索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

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
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""用户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def URL(self):
        r"""风险链接
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def URLPath(self):
        r"""风险文件地址
        :rtype: str
        """
        return self._URLPath

    @URLPath.setter
    def URLPath(self, URLPath):
        self._URLPath = URLPath

    @property
    def InstanceType(self):
        r"""实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DetectEngine(self):
        r"""类型
        :rtype: str
        """
        return self._DetectEngine

    @DetectEngine.setter
    def DetectEngine(self, DetectEngine):
        self._DetectEngine = DetectEngine

    @property
    def ResultDescribe(self):
        r"""结果描述
        :rtype: str
        """
        return self._ResultDescribe

    @ResultDescribe.setter
    def ResultDescribe(self, ResultDescribe):
        self._ResultDescribe = ResultDescribe

    @property
    def SourceURL(self):
        r"""源地址url
        :rtype: str
        """
        return self._SourceURL

    @SourceURL.setter
    def SourceURL(self, SourceURL):
        self._SourceURL = SourceURL

    @property
    def SourceURLPath(self):
        r"""源文件地址
        :rtype: str
        """
        return self._SourceURLPath

    @SourceURLPath.setter
    def SourceURLPath(self, SourceURLPath):
        self._SourceURLPath = SourceURLPath


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._URL = params.get("URL")
        self._URLPath = params.get("URLPath")
        self._InstanceType = params.get("InstanceType")
        self._DetectEngine = params.get("DetectEngine")
        self._ResultDescribe = params.get("ResultDescribe")
        self._SourceURL = params.get("SourceURL")
        self._SourceURLPath = params.get("SourceURLPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhereFilter(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤的项
        :type Name: str
        :param _Values: 过滤的值
        :type Values: list of str
        :param _OperatorType: 中台定义：
1等于 2大于 3小于 4大于等于 5小于等于 6不等于 9模糊匹配 13非模糊匹配 14按位与
精确匹配填 7 模糊匹配填9 

        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        r"""过滤的项
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤的值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        r"""中台定义：
1等于 2大于 3小于 4大于等于 5小于等于 6不等于 9模糊匹配 13非模糊匹配 14按位与
精确匹配填 7 模糊匹配填9 

        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        