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
    """ACL对象实体

    """

    def __init__(self):
        r"""
        :param _ResourceType: Acl资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）当前只有TOPIC，
        :type ResourceType: int
        :param _ResourceName: 资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param _Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :type Principal: str
        :param _Host: 默认\*,表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param _Operation: Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)
        :type Operation: int
        :param _PermissionType: 权限类型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)
        :type PermissionType: int
        """
        self._ResourceType = None
        self._ResourceName = None
        self._Principal = None
        self._Host = None
        self._Operation = None
        self._PermissionType = None

    @property
    def ResourceType(self):
        """Acl资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）当前只有TOPIC，
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Principal(self):
        """用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def Host(self):
        """默认\*,表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Operation(self):
        """Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """权限类型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Principal = params.get("Principal")
        self._Host = params.get("Host")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclResponse(AbstractModel):
    """ACL返回结果集

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总数据条数
        :type TotalCount: int
        :param _AclList: ACL列表
        :type AclList: list of Acl
        """
        self._TotalCount = None
        self._AclList = None

    @property
    def TotalCount(self):
        """符合条件的总数据条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclList(self):
        """ACL列表
        :rtype: list of Acl
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self._AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self._AclList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRule(AbstractModel):
    """AclRule列表接口出参

    """

    def __init__(self):
        r"""
        :param _RuleName: ACL规则名
        :type RuleName: str
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _PatternType: ACL规则匹配类型，目前只支持前缀匹配，枚举值列表：PREFIXED
        :type PatternType: str
        :param _Pattern: 表示前缀匹配的前缀的值
        :type Pattern: str
        :param _ResourceType: Acl资源类型,目前只支持Topic,枚举值列表：Topic
        :type ResourceType: str
        :param _AclList: 该规则所包含的ACL信息
        :type AclList: str
        :param _CreateTimeStamp: 规则所创建的时间
        :type CreateTimeStamp: str
        :param _IsApplied: 预设ACL规则是否应用到新增的topic中
        :type IsApplied: int
        :param _UpdateTimeStamp: 规则更新时间
        :type UpdateTimeStamp: str
        :param _Comment: 规则的备注
        :type Comment: str
        :param _TopicName: 其中一个显示的对应的TopicName
        :type TopicName: str
        :param _TopicCount: 应用该ACL规则的Topic数
        :type TopicCount: int
        :param _PatternTypeTitle: patternType的中文显示
        :type PatternTypeTitle: str
        """
        self._RuleName = None
        self._InstanceId = None
        self._PatternType = None
        self._Pattern = None
        self._ResourceType = None
        self._AclList = None
        self._CreateTimeStamp = None
        self._IsApplied = None
        self._UpdateTimeStamp = None
        self._Comment = None
        self._TopicName = None
        self._TopicCount = None
        self._PatternTypeTitle = None

    @property
    def RuleName(self):
        """ACL规则名
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PatternType(self):
        """ACL规则匹配类型，目前只支持前缀匹配，枚举值列表：PREFIXED
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def Pattern(self):
        """表示前缀匹配的前缀的值
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ResourceType(self):
        """Acl资源类型,目前只支持Topic,枚举值列表：Topic
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def AclList(self):
        """该规则所包含的ACL信息
        :rtype: str
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def CreateTimeStamp(self):
        """规则所创建的时间
        :rtype: str
        """
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def IsApplied(self):
        """预设ACL规则是否应用到新增的topic中
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def UpdateTimeStamp(self):
        """规则更新时间
        :rtype: str
        """
        return self._UpdateTimeStamp

    @UpdateTimeStamp.setter
    def UpdateTimeStamp(self, UpdateTimeStamp):
        self._UpdateTimeStamp = UpdateTimeStamp

    @property
    def Comment(self):
        """规则的备注
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def TopicName(self):
        """其中一个显示的对应的TopicName
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicCount(self):
        """应用该ACL规则的Topic数
        :rtype: int
        """
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def PatternTypeTitle(self):
        """patternType的中文显示
        :rtype: str
        """
        return self._PatternTypeTitle

    @PatternTypeTitle.setter
    def PatternTypeTitle(self, PatternTypeTitle):
        self._PatternTypeTitle = PatternTypeTitle


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._InstanceId = params.get("InstanceId")
        self._PatternType = params.get("PatternType")
        self._Pattern = params.get("Pattern")
        self._ResourceType = params.get("ResourceType")
        self._AclList = params.get("AclList")
        self._CreateTimeStamp = params.get("CreateTimeStamp")
        self._IsApplied = params.get("IsApplied")
        self._UpdateTimeStamp = params.get("UpdateTimeStamp")
        self._Comment = params.get("Comment")
        self._TopicName = params.get("TopicName")
        self._TopicCount = params.get("TopicCount")
        self._PatternTypeTitle = params.get("PatternTypeTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRuleInfo(AbstractModel):
    """表示ACL 规则的四元组信息

    """

    def __init__(self):
        r"""
        :param _Operation: Acl操作方式，枚举值(所有操作: All, 读：Read，写：Write)
        :type Operation: str
        :param _PermissionType: 权限类型，(Deny，Allow)
        :type PermissionType: str
        :param _Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\* 和 ip网段
        :type Host: str
        :param _Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入格式需要带【User:】前缀。例如用户A，传入为User:A。
        :type Principal: str
        """
        self._Operation = None
        self._PermissionType = None
        self._Host = None
        self._Principal = None

    @property
    def Operation(self):
        """Acl操作方式，枚举值(所有操作: All, 读：Read，写：Write)
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """权限类型，(Deny，Allow)
        :rtype: str
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        """默认为\*，表示任何host都可以访问，当前ckafka不支持host为\* 和 ip网段
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入格式需要带【User:】前缀。例如用户A，传入为User:A。
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclRuleResp(AbstractModel):
    """AclRule列表接口返回结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数据条数
        :type TotalCount: int
        :param _AclRuleList: AclRule列表
        :type AclRuleList: list of AclRule
        """
        self._TotalCount = None
        self._AclRuleList = None

    @property
    def TotalCount(self):
        """总数据条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclRuleList(self):
        """AclRule列表
        :rtype: list of AclRule
        """
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AclRuleList") is not None:
            self._AclRuleList = []
            for item in params.get("AclRuleList"):
                obj = AclRule()
                obj._deserialize(item)
                self._AclRuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyseParam(AbstractModel):
    """数据处理-解析参数

    """

    def __init__(self):
        r"""
        :param _Format: 解析格式，JSON，DELIMITER分隔符，REGULAR正则提取，SOURCE处理上层所有结果
        :type Format: str
        :param _Regex: 分隔符、正则表达式
        :type Regex: str
        :param _InputValueType: 需再次处理的KEY——模式
        :type InputValueType: str
        :param _InputValue: 需再次处理的KEY——KEY表达式
        :type InputValue: str
        """
        self._Format = None
        self._Regex = None
        self._InputValueType = None
        self._InputValue = None

    @property
    def Format(self):
        """解析格式，JSON，DELIMITER分隔符，REGULAR正则提取，SOURCE处理上层所有结果
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Regex(self):
        """分隔符、正则表达式
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def InputValueType(self):
        """需再次处理的KEY——模式
        :rtype: str
        """
        return self._InputValueType

    @InputValueType.setter
    def InputValueType(self, InputValueType):
        self._InputValueType = InputValueType

    @property
    def InputValue(self):
        """需再次处理的KEY——KEY表达式
        :rtype: str
        """
        return self._InputValue

    @InputValue.setter
    def InputValue(self, InputValue):
        self._InputValue = InputValue


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._Regex = params.get("Regex")
        self._InputValueType = params.get("InputValueType")
        self._InputValue = params.get("InputValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIdResponse(AbstractModel):
    """AppId的查询结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合要求的所有AppId数量
        :type TotalCount: int
        :param _AppIdList: 符合要求的App Id列表
        :type AppIdList: list of int
        """
        self._TotalCount = None
        self._AppIdList = None

    @property
    def TotalCount(self):
        """符合要求的所有AppId数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AppIdList(self):
        """符合要求的App Id列表
        :rtype: list of int
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._AppIdList = params.get("AppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Assignment(AbstractModel):
    """存储着分配给该消费者的 partition 信息

    """

    def __init__(self):
        r"""
        :param _Version: assingment版本信息
        :type Version: int
        :param _Topics: topic信息列表
        :type Topics: list of GroupInfoTopics
        """
        self._Version = None
        self._Topics = None

    @property
    def Version(self):
        """assingment版本信息
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Topics(self):
        """topic信息列表
        :rtype: list of GroupInfoTopics
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        self._Version = params.get("Version")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeTokenRequest(AbstractModel):
    """AuthorizeToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _User: 用户
        :type User: str
        :param _Tokens: token串
        :type Tokens: str
        """
        self._InstanceId = None
        self._User = None
        self._Tokens = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tokens(self):
        """token串
        :rtype: str
        """
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Tokens = params.get("Tokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizeTokenResponse(AbstractModel):
    """AuthorizeToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 0 成功
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """0 成功
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BatchAnalyseParam(AbstractModel):
    """批量解析

    """

    def __init__(self):
        r"""
        :param _Format: ONE_BY_ONE单条输出，MERGE合并输出
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
        """ONE_BY_ONE单条输出，MERGE合并输出
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchContent(AbstractModel):
    """批量发送消息内容

    """

    def __init__(self):
        r"""
        :param _Body: 发送的消息体
        :type Body: str
        :param _Key: 发送消息的键名
        :type Key: str
        """
        self._Body = None
        self._Key = None

    @property
    def Body(self):
        """发送的消息体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
        """发送消息的键名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclRequest(AbstractModel):
    """BatchCreateAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC）
        :type ResourceType: int
        :param _ResourceNames: 资源列表数组
        :type ResourceNames: list of str
        :param _RuleList: 设置的ACL规则列表
        :type RuleList: list of AclRuleInfo
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceNames = None
        self._RuleList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """Acl资源类型，(2:TOPIC）
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceNames(self):
        """资源列表数组
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def RuleList(self):
        """设置的ACL规则列表
        :rtype: list of AclRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceNames = params.get("ResourceNames")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = AclRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateAclResponse(AbstractModel):
    """BatchCreateAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 状态码：0-修改成功，否则修改失败
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """状态码：0-修改成功，否则修改失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BatchModifyGroupOffsetsRequest(AbstractModel):
    """BatchModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 消费分组名称
        :type GroupName: str
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Partitions: partition信息
        :type Partitions: list of Partitions
        :param _TopicName: 指定topic，默认所有topic
        :type TopicName: list of str
        """
        self._GroupName = None
        self._InstanceId = None
        self._Partitions = None
        self._TopicName = None

    @property
    def GroupName(self):
        """消费分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Partitions(self):
        """partition信息
        :rtype: list of Partitions
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def TopicName(self):
        """指定topic，默认所有topic
        :rtype: list of str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._InstanceId = params.get("InstanceId")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = Partitions()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyGroupOffsetsResponse(AbstractModel):
    """BatchModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchModifyTopicAttributesRequest(AbstractModel):
    """BatchModifyTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Topic: 主题属性列表 (同一个批次最多支持10个)
        :type Topic: list of BatchModifyTopicInfo
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题属性列表 (同一个批次最多支持10个)
        :rtype: list of BatchModifyTopicInfo
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Topic") is not None:
            self._Topic = []
            for item in params.get("Topic"):
                obj = BatchModifyTopicInfo()
                obj._deserialize(item)
                self._Topic.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicAttributesResponse(AbstractModel):
    """BatchModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: list of BatchModifyTopicResultDTO
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: list of BatchModifyTopicResultDTO
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = BatchModifyTopicResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class BatchModifyTopicInfo(AbstractModel):
    """批量修改topic参数

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
        :type TopicName: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _Note: 备注
        :type Note: str
        :param _ReplicaNum: 副本数
        :type ReplicaNum: int
        :param _CleanUpPolicy: 消息删除策略，可以选择delete 或者compact
        :type CleanUpPolicy: str
        :param _MinInsyncReplicas: 当producer设置request.required.acks为-1时，min.insync.replicas指定replicas的最小数目
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: 是否允许非ISR的副本成为Leader
        :type UncleanLeaderElectionEnable: bool
        :param _RetentionMs: topic维度的消息保留时间（毫秒）范围1 分钟到90 天
        :type RetentionMs: int
        :param _RetentionBytes: topic维度的消息保留大小，范围1 MB到1024 GB
        :type RetentionBytes: int
        :param _SegmentMs: Segment分片滚动的时长（毫秒），范围1 到90 天
        :type SegmentMs: int
        :param _MaxMessageBytes: 批次的消息大小，范围1 KB到12 MB
        :type MaxMessageBytes: int
        :param _LogMsgTimestampType: 消息保存的时间类型：CreateTime/LogAppendTime
        :type LogMsgTimestampType: str
        """
        self._TopicName = None
        self._PartitionNum = None
        self._Note = None
        self._ReplicaNum = None
        self._CleanUpPolicy = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._RetentionBytes = None
        self._SegmentMs = None
        self._MaxMessageBytes = None
        self._LogMsgTimestampType = None

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ReplicaNum(self):
        """副本数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def CleanUpPolicy(self):
        """消息删除策略，可以选择delete 或者compact
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def MinInsyncReplicas(self):
        """当producer设置request.required.acks为-1时，min.insync.replicas指定replicas的最小数目
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """是否允许非ISR的副本成为Leader
        :rtype: bool
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """topic维度的消息保留时间（毫秒）范围1 分钟到90 天
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def RetentionBytes(self):
        """topic维度的消息保留大小，范围1 MB到1024 GB
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def SegmentMs(self):
        """Segment分片滚动的时长（毫秒），范围1 到90 天
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        """批次的消息大小，范围1 KB到12 MB
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def LogMsgTimestampType(self):
        """消息保存的时间类型：CreateTime/LogAppendTime
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._Note = params.get("Note")
        self._ReplicaNum = params.get("ReplicaNum")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._RetentionBytes = params.get("RetentionBytes")
        self._SegmentMs = params.get("SegmentMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTopicResultDTO(AbstractModel):
    """批量修改topic属性结果

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        :param _ReturnCode: 操作返回码
        :type ReturnCode: str
        :param _Message: 操作返回信息
        :type Message: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._ReturnCode = None
        self._Message = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ReturnCode(self):
        """操作返回码
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Message(self):
        """操作返回信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._ReturnCode = params.get("ReturnCode")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrokerTopicData(AbstractModel):
    """主题占用Broker磁盘大小

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _TopicId: 主题Id
        :type TopicId: str
        :param _DataSize: 主题占用Broker 容量大小
        :type DataSize: int
        """
        self._TopicName = None
        self._TopicId = None
        self._DataSize = None

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DataSize(self):
        """主题占用Broker 容量大小
        :rtype: int
        """
        return self._DataSize

    @DataSize.setter
    def DataSize(self, DataSize):
        self._DataSize = DataSize


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._DataSize = params.get("DataSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrokerTopicFlowData(AbstractModel):
    """broker维度topic 流量排行指标

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
        :type TopicName: str
        :param _TopicId: 主题Id
        :type TopicId: str
        :param _TopicTraffic: Topic 流量(MB)
        :type TopicTraffic: str
        """
        self._TopicName = None
        self._TopicId = None
        self._TopicTraffic = None

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicTraffic(self):
        """Topic 流量(MB)
        :rtype: str
        """
        return self._TopicTraffic

    @TopicTraffic.setter
    def TopicTraffic(self, TopicTraffic):
        self._TopicTraffic = TopicTraffic


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._TopicTraffic = params.get("TopicTraffic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorizationTokenRequest(AbstractModel):
    """CancelAuthorizationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _User: 用户
        :type User: str
        :param _Tokens: token串
        :type Tokens: str
        """
        self._InstanceId = None
        self._User = None
        self._Tokens = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tokens(self):
        """token串
        :rtype: str
        """
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Tokens = params.get("Tokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorizationTokenResponse(AbstractModel):
    """CancelAuthorizationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 0 成功 非0 失败
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """0 成功 非0 失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CdcClusterResponse(AbstractModel):
    """创建CDC 标准版共享集群出参

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCdcClusterRequest(AbstractModel):
    """CheckCdcCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCdcClusterResponse(AbstractModel):
    """CheckCdcCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果状态Success
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果状态Success
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ClickHouseConnectParam(AbstractModel):
    """ClickHouse连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: ClickHouse的连接port
        :type Port: int
        :param _UserName: ClickHouse连接源的用户名
        :type UserName: str
        :param _Password: ClickHouse连接源的密码
        :type Password: str
        :param _Resource: ClickHouse连接源的实例资源
        :type Resource: str
        :param _SelfBuilt: ClickHouse连接源是否为自建集群
        :type SelfBuilt: bool
        :param _ServiceVip: ClickHouse连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: ClickHouse连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._SelfBuilt = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None

    @property
    def Port(self):
        """ClickHouse的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """ClickHouse连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """ClickHouse连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """ClickHouse连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        """ClickHouse连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        """ClickHouse连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """ClickHouse连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._SelfBuilt = params.get("SelfBuilt")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClickHouseModifyConnectParam(AbstractModel):
    """ClickHouse修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: ClickHouse连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: ClickHouse的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: ClickHouse连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: ClickHouse连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: ClickHouse连接源的用户名
        :type UserName: str
        :param _Password: ClickHouse连接源的密码
        :type Password: str
        :param _SelfBuilt: ClickHouse连接源是否为自建集群【不支持修改】
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务，默认为true
        :type IsUpdate: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._SelfBuilt = None
        self._IsUpdate = None

    @property
    def Resource(self):
        """ClickHouse连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """ClickHouse的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """ClickHouse连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """ClickHouse连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """ClickHouse连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """ClickHouse连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        """ClickHouse连接源是否为自建集群【不支持修改】
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务，默认为true
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._SelfBuilt = params.get("SelfBuilt")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClickHouseParam(AbstractModel):
    """ClickHouse类型入参

    """

    def __init__(self):
        r"""
        :param _Cluster: ClickHouse的集群
        :type Cluster: str
        :param _Database: ClickHouse的数据库名
        :type Database: str
        :param _Table: ClickHouse的数据表名
        :type Table: str
        :param _Schema: ClickHouse的schema
        :type Schema: list of ClickHouseSchema
        :param _Resource: 实例资源
        :type Resource: str
        :param _Ip: ClickHouse的连接ip
        :type Ip: str
        :param _Port: ClickHouse的连接port
        :type Port: int
        :param _UserName: ClickHouse的用户名
        :type UserName: str
        :param _Password: ClickHouse的密码
        :type Password: str
        :param _ServiceVip: 实例vip
        :type ServiceVip: str
        :param _UniqVpcId: 实例的vpcId
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _DropInvalidMessage: ClickHouse是否抛弃解析失败的消息，默认为true
        :type DropInvalidMessage: bool
        :param _Type: ClickHouse 类型，emr-clickhouse : "emr";cdw-clickhouse : "cdwch";自建 : ""
        :type Type: str
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _BatchSize: 每批次投递到 ClickHouse 表消息数量，默认为 1000 条。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :type BatchSize: int
        :param _ConsumerFetchMinBytes: 每次从 topic 中拉取消息大小，默认为 1MB，即至少要从 topic 中批量拉取 1MB 消息，才进行数据投递到 ClickHouse 操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :type ConsumerFetchMinBytes: int
        :param _ConsumerFetchMaxWaitMs: 每次从 topic 拉取消息最大等待时间，当超过当前最大等待时间时，即使没有拉取到 ConsumerFetchMinBytes 大小，也将进行 ClickHouse 投递操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :type ConsumerFetchMaxWaitMs: int
        """
        self._Cluster = None
        self._Database = None
        self._Table = None
        self._Schema = None
        self._Resource = None
        self._Ip = None
        self._Port = None
        self._UserName = None
        self._Password = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._SelfBuilt = None
        self._DropInvalidMessage = None
        self._Type = None
        self._DropCls = None
        self._BatchSize = None
        self._ConsumerFetchMinBytes = None
        self._ConsumerFetchMaxWaitMs = None

    @property
    def Cluster(self):
        """ClickHouse的集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Database(self):
        """ClickHouse的数据库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """ClickHouse的数据表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Schema(self):
        """ClickHouse的schema
        :rtype: list of ClickHouseSchema
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Resource(self):
        """实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        """ClickHouse的连接ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """ClickHouse的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """ClickHouse的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """ClickHouse的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ServiceVip(self):
        """实例vip
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """实例的vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def DropInvalidMessage(self):
        """ClickHouse是否抛弃解析失败的消息，默认为true
        :rtype: bool
        """
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def Type(self):
        """ClickHouse 类型，emr-clickhouse : "emr";cdw-clickhouse : "cdwch";自建 : ""
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DropCls(self):
        """当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        """
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def BatchSize(self):
        """每批次投递到 ClickHouse 表消息数量，默认为 1000 条。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def ConsumerFetchMinBytes(self):
        """每次从 topic 中拉取消息大小，默认为 1MB，即至少要从 topic 中批量拉取 1MB 消息，才进行数据投递到 ClickHouse 操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :rtype: int
        """
        return self._ConsumerFetchMinBytes

    @ConsumerFetchMinBytes.setter
    def ConsumerFetchMinBytes(self, ConsumerFetchMinBytes):
        self._ConsumerFetchMinBytes = ConsumerFetchMinBytes

    @property
    def ConsumerFetchMaxWaitMs(self):
        """每次从 topic 拉取消息最大等待时间，当超过当前最大等待时间时，即使没有拉取到 ConsumerFetchMinBytes 大小，也将进行 ClickHouse 投递操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
        :rtype: int
        """
        return self._ConsumerFetchMaxWaitMs

    @ConsumerFetchMaxWaitMs.setter
    def ConsumerFetchMaxWaitMs(self, ConsumerFetchMaxWaitMs):
        self._ConsumerFetchMaxWaitMs = ConsumerFetchMaxWaitMs


    def _deserialize(self, params):
        self._Cluster = params.get("Cluster")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        if params.get("Schema") is not None:
            self._Schema = []
            for item in params.get("Schema"):
                obj = ClickHouseSchema()
                obj._deserialize(item)
                self._Schema.append(obj)
        self._Resource = params.get("Resource")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._SelfBuilt = params.get("SelfBuilt")
        self._DropInvalidMessage = params.get("DropInvalidMessage")
        self._Type = params.get("Type")
        if params.get("DropCls") is not None:
            self._DropCls = DropCls()
            self._DropCls._deserialize(params.get("DropCls"))
        self._BatchSize = params.get("BatchSize")
        self._ConsumerFetchMinBytes = params.get("ConsumerFetchMinBytes")
        self._ConsumerFetchMaxWaitMs = params.get("ConsumerFetchMaxWaitMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClickHouseSchema(AbstractModel):
    """ClickHouse的Schema

    """

    def __init__(self):
        r"""
        :param _ColumnName: 表的列名
        :type ColumnName: str
        :param _JsonKey: 该列对应的jsonKey名
        :type JsonKey: str
        :param _Type: 表列项的类型
        :type Type: str
        :param _AllowNull: 列项是否允许为空
        :type AllowNull: bool
        """
        self._ColumnName = None
        self._JsonKey = None
        self._Type = None
        self._AllowNull = None

    @property
    def ColumnName(self):
        """表的列名
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def JsonKey(self):
        """该列对应的jsonKey名
        :rtype: str
        """
        return self._JsonKey

    @JsonKey.setter
    def JsonKey(self, JsonKey):
        self._JsonKey = JsonKey

    @property
    def Type(self):
        """表列项的类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowNull(self):
        """列项是否允许为空
        :rtype: bool
        """
        return self._AllowNull

    @AllowNull.setter
    def AllowNull(self, AllowNull):
        self._AllowNull = AllowNull


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._JsonKey = params.get("JsonKey")
        self._Type = params.get("Type")
        self._AllowNull = params.get("AllowNull")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsParam(AbstractModel):
    """Cls类型入参

    """

    def __init__(self):
        r"""
        :param _DecodeJson: 生产的信息是否为json格式
        :type DecodeJson: bool
        :param _Resource: cls日志主题id
        :type Resource: str
        :param _LogSet: cls日志集id
        :type LogSet: str
        :param _ContentKey: 当DecodeJson为false时必填
        :type ContentKey: str
        :param _TimeField: 指定消息中的某字段内容作为cls日志的时间。
字段内容格式需要是秒级时间戳
        :type TimeField: str
        """
        self._DecodeJson = None
        self._Resource = None
        self._LogSet = None
        self._ContentKey = None
        self._TimeField = None

    @property
    def DecodeJson(self):
        """生产的信息是否为json格式
        :rtype: bool
        """
        return self._DecodeJson

    @DecodeJson.setter
    def DecodeJson(self, DecodeJson):
        self._DecodeJson = DecodeJson

    @property
    def Resource(self):
        """cls日志主题id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def LogSet(self):
        """cls日志集id
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def ContentKey(self):
        """当DecodeJson为false时必填
        :rtype: str
        """
        return self._ContentKey

    @ContentKey.setter
    def ContentKey(self, ContentKey):
        self._ContentKey = ContentKey

    @property
    def TimeField(self):
        """指定消息中的某字段内容作为cls日志的时间。
字段内容格式需要是秒级时间戳
        :rtype: str
        """
        return self._TimeField

    @TimeField.setter
    def TimeField(self, TimeField):
        self._TimeField = TimeField


    def _deserialize(self, params):
        self._DecodeJson = params.get("DecodeJson")
        self._Resource = params.get("Resource")
        self._LogSet = params.get("LogSet")
        self._ContentKey = params.get("ContentKey")
        self._TimeField = params.get("TimeField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """集群信息实体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: int
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _MaxDiskSize: 集群最大磁盘 单位GB
        :type MaxDiskSize: int
        :param _MaxBandWidth: 集群最大带宽 单位MB/s
        :type MaxBandWidth: int
        :param _AvailableDiskSize: 集群当前可用磁盘  单位GB
        :type AvailableDiskSize: int
        :param _AvailableBandWidth: 集群当前可用带宽 单位MB/s
        :type AvailableBandWidth: int
        :param _ZoneId: 集群所属可用区，表明集群归属的可用区
        :type ZoneId: int
        :param _ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
        :type ZoneIds: list of int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._MaxDiskSize = None
        self._MaxBandWidth = None
        self._AvailableDiskSize = None
        self._AvailableBandWidth = None
        self._ZoneId = None
        self._ZoneIds = None

    @property
    def ClusterId(self):
        """集群Id
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MaxDiskSize(self):
        """集群最大磁盘 单位GB
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MaxBandWidth(self):
        """集群最大带宽 单位MB/s
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def AvailableDiskSize(self):
        """集群当前可用磁盘  单位GB
        :rtype: int
        """
        return self._AvailableDiskSize

    @AvailableDiskSize.setter
    def AvailableDiskSize(self, AvailableDiskSize):
        self._AvailableDiskSize = AvailableDiskSize

    @property
    def AvailableBandWidth(self):
        """集群当前可用带宽 单位MB/s
        :rtype: int
        """
        return self._AvailableBandWidth

    @AvailableBandWidth.setter
    def AvailableBandWidth(self, AvailableBandWidth):
        self._AvailableBandWidth = AvailableBandWidth

    @property
    def ZoneId(self):
        """集群所属可用区，表明集群归属的可用区
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIds(self):
        """集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._AvailableDiskSize = params.get("AvailableDiskSize")
        self._AvailableBandWidth = params.get("AvailableBandWidth")
        self._ZoneId = params.get("ZoneId")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """高级配置对象

    """

    def __init__(self):
        r"""
        :param _Retention: 消息保留时间
        :type Retention: int
        :param _MinInsyncReplicas: 最小同步复制数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinInsyncReplicas: int
        :param _CleanUpPolicy: 日志清理模式，默认 delete。
delete：日志按保存时间删除；compact：日志按 key 压缩；compact, delete：日志按 key 压缩且会保存时间删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type CleanUpPolicy: str
        :param _SegmentMs: Segment 分片滚动的时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentMs: int
        :param _UncleanLeaderElectionEnable: 0表示 false。 1表示 true。
注意：此字段可能返回 null，表示取不到有效值。
        :type UncleanLeaderElectionEnable: int
        :param _SegmentBytes: Segment 分片滚动的字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentBytes: int
        :param _MaxMessageBytes: 最大消息字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageBytes: int
        :param _RetentionBytes: 消息保留文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionBytes: int
        :param _LogMsgTimestampType: 消息保存的时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LogMsgTimestampType: str
        """
        self._Retention = None
        self._MinInsyncReplicas = None
        self._CleanUpPolicy = None
        self._SegmentMs = None
        self._UncleanLeaderElectionEnable = None
        self._SegmentBytes = None
        self._MaxMessageBytes = None
        self._RetentionBytes = None
        self._LogMsgTimestampType = None

    @property
    def Retention(self):
        """消息保留时间
        :rtype: int
        """
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def MinInsyncReplicas(self):
        """最小同步复制数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def CleanUpPolicy(self):
        """日志清理模式，默认 delete。
delete：日志按保存时间删除；compact：日志按 key 压缩；compact, delete：日志按 key 压缩且会保存时间删除。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def SegmentMs(self):
        """Segment 分片滚动的时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def UncleanLeaderElectionEnable(self):
        """0表示 false。 1表示 true。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def SegmentBytes(self):
        """Segment 分片滚动的字节数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SegmentBytes

    @SegmentBytes.setter
    def SegmentBytes(self, SegmentBytes):
        self._SegmentBytes = SegmentBytes

    @property
    def MaxMessageBytes(self):
        """最大消息字节数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def RetentionBytes(self):
        """消息保留文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def LogMsgTimestampType(self):
        """消息保存的时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogMsgTimestampType

    @LogMsgTimestampType.setter
    def LogMsgTimestampType(self, LogMsgTimestampType):
        self._LogMsgTimestampType = LogMsgTimestampType


    def _deserialize(self, params):
        self._Retention = params.get("Retention")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._SegmentMs = params.get("SegmentMs")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._SegmentBytes = params.get("SegmentBytes")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._RetentionBytes = params.get("RetentionBytes")
        self._LogMsgTimestampType = params.get("LogMsgTimestampType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectResourceResourceIdResp(AbstractModel):
    """返回连接源的Id

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        """连接源的Id
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
        


class Connection(AbstractModel):
    """Connection信息

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
        :type TopicName: str
        :param _GroupId: 消费组ID
        :type GroupId: str
        :param _TopicId: 主题Id
        :type TopicId: str
        """
        self._TopicName = None
        self._GroupId = None
        self._TopicId = None

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def GroupId(self):
        """消费组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._GroupId = params.get("GroupId")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    """用户组实体

    """

    def __init__(self):
        r"""
        :param _ConsumerGroupName: 用户组名称
        :type ConsumerGroupName: str
        :param _SubscribedInfo: 订阅信息实体
        :type SubscribedInfo: list of SubscribedInfo
        """
        self._ConsumerGroupName = None
        self._SubscribedInfo = None

    @property
    def ConsumerGroupName(self):
        """用户组名称
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def SubscribedInfo(self):
        """订阅信息实体
        :rtype: list of SubscribedInfo
        """
        return self._SubscribedInfo

    @SubscribedInfo.setter
    def SubscribedInfo(self, SubscribedInfo):
        self._SubscribedInfo = SubscribedInfo


    def _deserialize(self, params):
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self._SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self._SubscribedInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupResponse(AbstractModel):
    """消费组返回结果实体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的消费组数量
        :type TotalCount: int
        :param _TopicList: 主题列表
        :type TopicList: list of ConsumerGroupTopic
        :param _GroupList: 消费分组List
        :type GroupList: list of ConsumerGroup
        :param _TotalPartition: 所有分区数量
        :type TotalPartition: int
        :param _PartitionListForMonitor: 监控的分区列表
        :type PartitionListForMonitor: list of Partition
        :param _TotalTopic: 主题总数
        :type TotalTopic: int
        :param _TopicListForMonitor: 监控的主题列表
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param _GroupListForMonitor: 监控的组列表
        :type GroupListForMonitor: list of Group
        """
        self._TotalCount = None
        self._TopicList = None
        self._GroupList = None
        self._TotalPartition = None
        self._PartitionListForMonitor = None
        self._TotalTopic = None
        self._TopicListForMonitor = None
        self._GroupListForMonitor = None

    @property
    def TotalCount(self):
        """符合条件的消费组数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """主题列表
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def GroupList(self):
        """消费分组List
        :rtype: list of ConsumerGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def TotalPartition(self):
        """所有分区数量
        :rtype: int
        """
        return self._TotalPartition

    @TotalPartition.setter
    def TotalPartition(self, TotalPartition):
        self._TotalPartition = TotalPartition

    @property
    def PartitionListForMonitor(self):
        """监控的分区列表
        :rtype: list of Partition
        """
        return self._PartitionListForMonitor

    @PartitionListForMonitor.setter
    def PartitionListForMonitor(self, PartitionListForMonitor):
        self._PartitionListForMonitor = PartitionListForMonitor

    @property
    def TotalTopic(self):
        """主题总数
        :rtype: int
        """
        return self._TotalTopic

    @TotalTopic.setter
    def TotalTopic(self, TotalTopic):
        self._TotalTopic = TotalTopic

    @property
    def TopicListForMonitor(self):
        """监控的主题列表
        :rtype: list of ConsumerGroupTopic
        """
        return self._TopicListForMonitor

    @TopicListForMonitor.setter
    def TopicListForMonitor(self, TopicListForMonitor):
        self._TopicListForMonitor = TopicListForMonitor

    @property
    def GroupListForMonitor(self):
        """监控的组列表
        :rtype: list of Group
        """
        return self._GroupListForMonitor

    @GroupListForMonitor.setter
    def GroupListForMonitor(self, GroupListForMonitor):
        self._GroupListForMonitor = GroupListForMonitor


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self._PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self._PartitionListForMonitor.append(obj)
        self._TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self._TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self._TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self._GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self._GroupListForMonitor.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupSpeed(AbstractModel):
    """消费者组消费速度排行

    """

    def __init__(self):
        r"""
        :param _ConsumerGroupName: 消费者组名称
        :type ConsumerGroupName: str
        :param _Speed: 消费速度 Count/Minute
        :type Speed: int
        """
        self._ConsumerGroupName = None
        self._Speed = None

    @property
    def ConsumerGroupName(self):
        """消费者组名称
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Speed(self):
        """消费速度 Count/Minute
        :rtype: int
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed


    def _deserialize(self, params):
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Speed = params.get("Speed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupTopic(AbstractModel):
    """消费组主题对象

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        """
        self._TopicId = None
        self._TopicName = None

    @property
    def TopicId(self):
        """主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerRecord(AbstractModel):
    """消息记录

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名
        :type Topic: str
        :param _Partition: 分区id
        :type Partition: int
        :param _Offset: 位点
        :type Offset: int
        :param _Key: 消息key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 消息value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Timestamp: 消息时间戳
        :type Timestamp: int
        :param _Headers: 消息headers
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: str
        """
        self._Topic = None
        self._Partition = None
        self._Offset = None
        self._Key = None
        self._Value = None
        self._Timestamp = None
        self._Headers = None

    @property
    def Topic(self):
        """主题名
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Key(self):
        """消息key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """消息value
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Timestamp(self):
        """消息时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Headers(self):
        """消息headers
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Timestamp = params.get("Timestamp")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosParam(AbstractModel):
    """Cos Datahub 任务接入参数

    """

    def __init__(self):
        r"""
        :param _BucketName: cos 存储桶名称
        :type BucketName: str
        :param _Region: 地域代码
        :type Region: str
        :param _ObjectKey: 对象名称
        :type ObjectKey: str
        :param _AggregateBatchSize: 汇聚消息量的大小（单位：MB)
        :type AggregateBatchSize: int
        :param _AggregateInterval: 汇聚的时间间隔（单位：小时）
        :type AggregateInterval: int
        :param _FormatOutputType: 消息汇聚后的文件格式（支持csv, json）
        :type FormatOutputType: str
        :param _ObjectKeyPrefix: 转储的对象目录前缀
        :type ObjectKeyPrefix: str
        :param _DirectoryTimeFormat: 根据strptime 时间格式化的分区格式
        :type DirectoryTimeFormat: str
        """
        self._BucketName = None
        self._Region = None
        self._ObjectKey = None
        self._AggregateBatchSize = None
        self._AggregateInterval = None
        self._FormatOutputType = None
        self._ObjectKeyPrefix = None
        self._DirectoryTimeFormat = None

    @property
    def BucketName(self):
        """cos 存储桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        """地域代码
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ObjectKey(self):
        """对象名称
        :rtype: str
        """
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def AggregateBatchSize(self):
        """汇聚消息量的大小（单位：MB)
        :rtype: int
        """
        return self._AggregateBatchSize

    @AggregateBatchSize.setter
    def AggregateBatchSize(self, AggregateBatchSize):
        self._AggregateBatchSize = AggregateBatchSize

    @property
    def AggregateInterval(self):
        """汇聚的时间间隔（单位：小时）
        :rtype: int
        """
        return self._AggregateInterval

    @AggregateInterval.setter
    def AggregateInterval(self, AggregateInterval):
        self._AggregateInterval = AggregateInterval

    @property
    def FormatOutputType(self):
        """消息汇聚后的文件格式（支持csv, json）
        :rtype: str
        """
        return self._FormatOutputType

    @FormatOutputType.setter
    def FormatOutputType(self, FormatOutputType):
        self._FormatOutputType = FormatOutputType

    @property
    def ObjectKeyPrefix(self):
        """转储的对象目录前缀
        :rtype: str
        """
        return self._ObjectKeyPrefix

    @ObjectKeyPrefix.setter
    def ObjectKeyPrefix(self, ObjectKeyPrefix):
        self._ObjectKeyPrefix = ObjectKeyPrefix

    @property
    def DirectoryTimeFormat(self):
        """根据strptime 时间格式化的分区格式
        :rtype: str
        """
        return self._DirectoryTimeFormat

    @DirectoryTimeFormat.setter
    def DirectoryTimeFormat(self, DirectoryTimeFormat):
        self._DirectoryTimeFormat = DirectoryTimeFormat


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._Region = params.get("Region")
        self._ObjectKey = params.get("ObjectKey")
        self._AggregateBatchSize = params.get("AggregateBatchSize")
        self._AggregateInterval = params.get("AggregateInterval")
        self._FormatOutputType = params.get("FormatOutputType")
        self._ObjectKeyPrefix = params.get("ObjectKeyPrefix")
        self._DirectoryTimeFormat = params.get("DirectoryTimeFormat")
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
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param _Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param _PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckafka支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param _ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param _Host: 默认为*，表示任何host都可以访问。支持填写IP或网段，支持“;”分隔。
        :type Host: str
        :param _Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入时需要加 User: 前缀,如用户A则传入User:A。
        :type Principal: str
        :param _ResourceNameList: 资源名称列表,Json字符串格式。ResourceName和resourceNameList只能指定其中一个。
        :type ResourceNameList: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._Operation = None
        self._PermissionType = None
        self._ResourceName = None
        self._Host = None
        self._Principal = None
        self._ResourceNameList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Operation(self):
        """Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """权限类型，(2:DENY，3:ALLOW)，当前ckafka支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def ResourceName(self):
        """资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Host(self):
        """默认为*，表示任何host都可以访问。支持填写IP或网段，支持“;”分隔。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入时需要加 User: 前缀,如用户A则传入User:A。
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def ResourceNameList(self):
        """资源名称列表,Json字符串格式。ResourceName和resourceNameList只能指定其中一个。
        :rtype: str
        """
        return self._ResourceNameList

    @ResourceNameList.setter
    def ResourceNameList(self, ResourceNameList):
        self._ResourceNameList = ResourceNameList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._ResourceName = params.get("ResourceName")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        self._ResourceNameList = params.get("ResourceNameList")
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
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateAclRuleRequest(AbstractModel):
    """CreateAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _ResourceType: Acl资源类型,目前只支持Topic,枚举值列表：Topic
        :type ResourceType: str
        :param _PatternType: ACL规则匹配类型，目前支持前缀匹配与预设策略，枚举值列表：PREFIXED/PRESET
        :type PatternType: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RuleList: 设置的ACL规则列表
        :type RuleList: list of AclRuleInfo
        :param _Pattern: 表示前缀匹配的前缀的值
        :type Pattern: str
        :param _IsApplied: 预设ACL规则是否应用到新增的topic中
        :type IsApplied: int
        :param _Comment: ACL规则的备注
        :type Comment: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._PatternType = None
        self._RuleName = None
        self._RuleList = None
        self._Pattern = None
        self._IsApplied = None
        self._Comment = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """Acl资源类型,目前只支持Topic,枚举值列表：Topic
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def PatternType(self):
        """ACL规则匹配类型，目前支持前缀匹配与预设策略，枚举值列表：PREFIXED/PRESET
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleList(self):
        """设置的ACL规则列表
        :rtype: list of AclRuleInfo
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Pattern(self):
        """表示前缀匹配的前缀的值
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def IsApplied(self):
        """预设ACL规则是否应用到新增的topic中
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def Comment(self):
        """ACL规则的备注
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._PatternType = params.get("PatternType")
        self._RuleName = params.get("RuleName")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = AclRuleInfo()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._Pattern = params.get("Pattern")
        self._IsApplied = params.get("IsApplied")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRuleResponse(AbstractModel):
    """CreateAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 规则的唯一表示Key
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """规则的唯一表示Key
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateCdcClusterRequest(AbstractModel):
    """CreateCdcCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CdcId: cdc的id
        :type CdcId: str
        :param _CdcVpcId: vpcId,一个地域只有唯一一个vpcid用于CDC
        :type CdcVpcId: str
        :param _CdcSubnetId: 每个CDC集群有唯一一个子网ID
        :type CdcSubnetId: str
        :param _ZoneId: 所在可用区ID
        :type ZoneId: int
        :param _Bandwidth: 实例带宽,单位MB/s; 最小值:20MB/s, 高级版最大值:360MB/s,专业版最大值:100000MB/s  标准版固定带宽规格: 40MB/s, 100MB/s, 150MB/s
        :type Bandwidth: int
        :param _DiskSize: cdc集群的总磁盘
        :type DiskSize: int
        :param _DiskType: ckafka集群实例磁盘类型
        :type DiskType: str
        :param _SystemDiskType: 系统盘类型
        :type SystemDiskType: str
        """
        self._CdcId = None
        self._CdcVpcId = None
        self._CdcSubnetId = None
        self._ZoneId = None
        self._Bandwidth = None
        self._DiskSize = None
        self._DiskType = None
        self._SystemDiskType = None

    @property
    def CdcId(self):
        """cdc的id
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def CdcVpcId(self):
        """vpcId,一个地域只有唯一一个vpcid用于CDC
        :rtype: str
        """
        return self._CdcVpcId

    @CdcVpcId.setter
    def CdcVpcId(self, CdcVpcId):
        self._CdcVpcId = CdcVpcId

    @property
    def CdcSubnetId(self):
        """每个CDC集群有唯一一个子网ID
        :rtype: str
        """
        return self._CdcSubnetId

    @CdcSubnetId.setter
    def CdcSubnetId(self, CdcSubnetId):
        self._CdcSubnetId = CdcSubnetId

    @property
    def ZoneId(self):
        """所在可用区ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Bandwidth(self):
        """实例带宽,单位MB/s; 最小值:20MB/s, 高级版最大值:360MB/s,专业版最大值:100000MB/s  标准版固定带宽规格: 40MB/s, 100MB/s, 150MB/s
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        """cdc集群的总磁盘
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """ckafka集群实例磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def SystemDiskType(self):
        """系统盘类型
        :rtype: str
        """
        return self._SystemDiskType

    @SystemDiskType.setter
    def SystemDiskType(self, SystemDiskType):
        self._SystemDiskType = SystemDiskType


    def _deserialize(self, params):
        self._CdcId = params.get("CdcId")
        self._CdcVpcId = params.get("CdcVpcId")
        self._CdcSubnetId = params.get("CdcSubnetId")
        self._ZoneId = params.get("ZoneId")
        self._Bandwidth = params.get("Bandwidth")
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._SystemDiskType = params.get("SystemDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdcClusterResponse(AbstractModel):
    """CreateCdcCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CdcClusterResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """无
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CdcClusterResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CdcClusterResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateConnectResourceRequest(AbstractModel):
    """CreateConnectResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceName: 连接源名称
        :type ResourceName: str
        :param _Type: 连接源类型
        :type Type: str
        :param _Description: 连接源描述
        :type Description: str
        :param _DtsConnectParam: Dts配置，Type为DTS时必填
        :type DtsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        :param _MongoDBConnectParam: MongoDB配置，Type为MONGODB时必填
        :type MongoDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        :param _EsConnectParam: Es配置，Type为ES时必填
        :type EsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        :param _ClickHouseConnectParam: ClickHouse配置，Type为CLICKHOUSE时必填
        :type ClickHouseConnectParam: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        :param _MySQLConnectParam: MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时必填
        :type MySQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        :param _PostgreSQLConnectParam: PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
        :type PostgreSQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        :param _MariaDBConnectParam: MariaDB配置，Type为MARIADB时必填
        :type MariaDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        :param _SQLServerConnectParam: SQLServer配置，Type为SQLSERVER时必填
        :type SQLServerConnectParam: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        :param _DorisConnectParam: Doris 配置，Type为 DORIS 时必填
        :type DorisConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        :param _KafkaConnectParam: Kafka配置，Type为 KAFKA 时必填
        :type KafkaConnectParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        :param _MqttConnectParam: MQTT配置，Type为 MQTT 时必填
        :type MqttConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        self._ResourceName = None
        self._Type = None
        self._Description = None
        self._DtsConnectParam = None
        self._MongoDBConnectParam = None
        self._EsConnectParam = None
        self._ClickHouseConnectParam = None
        self._MySQLConnectParam = None
        self._PostgreSQLConnectParam = None
        self._MariaDBConnectParam = None
        self._SQLServerConnectParam = None
        self._DorisConnectParam = None
        self._KafkaConnectParam = None
        self._MqttConnectParam = None

    @property
    def ResourceName(self):
        """连接源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Type(self):
        """连接源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        """连接源描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DtsConnectParam(self):
        """Dts配置，Type为DTS时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        """
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        """MongoDB配置，Type为MONGODB时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        """
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        """Es配置，Type为ES时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        """
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        """ClickHouse配置，Type为CLICKHOUSE时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        """
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        """MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        """
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        """PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        """
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        """MariaDB配置，Type为MARIADB时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        """
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        """SQLServer配置，Type为SQLSERVER时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        """
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def DorisConnectParam(self):
        """Doris 配置，Type为 DORIS 时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        """
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        """Kafka配置，Type为 KAFKA 时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        """
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
        """MQTT配置，Type为 MQTT 时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        return self._MqttConnectParam

    @MqttConnectParam.setter
    def MqttConnectParam(self, MqttConnectParam):
        self._MqttConnectParam = MqttConnectParam


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        if params.get("DtsConnectParam") is not None:
            self._DtsConnectParam = DtsConnectParam()
            self._DtsConnectParam._deserialize(params.get("DtsConnectParam"))
        if params.get("MongoDBConnectParam") is not None:
            self._MongoDBConnectParam = MongoDBConnectParam()
            self._MongoDBConnectParam._deserialize(params.get("MongoDBConnectParam"))
        if params.get("EsConnectParam") is not None:
            self._EsConnectParam = EsConnectParam()
            self._EsConnectParam._deserialize(params.get("EsConnectParam"))
        if params.get("ClickHouseConnectParam") is not None:
            self._ClickHouseConnectParam = ClickHouseConnectParam()
            self._ClickHouseConnectParam._deserialize(params.get("ClickHouseConnectParam"))
        if params.get("MySQLConnectParam") is not None:
            self._MySQLConnectParam = MySQLConnectParam()
            self._MySQLConnectParam._deserialize(params.get("MySQLConnectParam"))
        if params.get("PostgreSQLConnectParam") is not None:
            self._PostgreSQLConnectParam = PostgreSQLConnectParam()
            self._PostgreSQLConnectParam._deserialize(params.get("PostgreSQLConnectParam"))
        if params.get("MariaDBConnectParam") is not None:
            self._MariaDBConnectParam = MariaDBConnectParam()
            self._MariaDBConnectParam._deserialize(params.get("MariaDBConnectParam"))
        if params.get("SQLServerConnectParam") is not None:
            self._SQLServerConnectParam = SQLServerConnectParam()
            self._SQLServerConnectParam._deserialize(params.get("SQLServerConnectParam"))
        if params.get("DorisConnectParam") is not None:
            self._DorisConnectParam = DorisConnectParam()
            self._DorisConnectParam._deserialize(params.get("DorisConnectParam"))
        if params.get("KafkaConnectParam") is not None:
            self._KafkaConnectParam = KafkaConnectParam()
            self._KafkaConnectParam._deserialize(params.get("KafkaConnectParam"))
        if params.get("MqttConnectParam") is not None:
            self._MqttConnectParam = MqttConnectParam()
            self._MqttConnectParam._deserialize(params.get("MqttConnectParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectResourceResponse(AbstractModel):
    """CreateConnectResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 连接源的Id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """连接源的Id
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConnectResourceResourceIdResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _GroupName: 消费分组名称
        :type GroupName: str
        :param _TopicName: 主题名，TopicName、TopicNameList 需要显示指定一个存在的主题名
        :type TopicName: str
        :param _TopicNameList: 主题名列表
        :type TopicNameList: list of str
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._TopicNameList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        """消费分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        """主题名，TopicName、TopicNameList 需要显示指定一个存在的主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
        """主题名列表
        :rtype: list of str
        """
        return self._TopicNameList

    @TopicNameList.setter
    def TopicNameList(self, TopicNameList):
        self._TopicNameList = TopicNameList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._TopicName = params.get("TopicName")
        self._TopicNameList = params.get("TopicNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建消费者组返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建消费者组返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateDatahubTaskRequest(AbstractModel):
    """CreateDatahubTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskType: 任务类型，SOURCE数据接入，SINK数据流出
        :type TaskType: str
        :param _SourceResource: 数据源
        :type SourceResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TargetResource: 数据目标
        :type TargetResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TransformParam: 数据处理规则
        :type TransformParam: :class:`tencentcloud.ckafka.v20190819.models.TransformParam`
        :param _PrivateLinkParam: 实例连接参数【已废弃】
        :type PrivateLinkParam: :class:`tencentcloud.ckafka.v20190819.models.PrivateLinkParam`
        :param _SchemaId: 选择所要绑定的SchemaId
        :type SchemaId: str
        :param _TransformsParam: 数据处理规则
        :type TransformsParam: :class:`tencentcloud.ckafka.v20190819.models.TransformsParam`
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._TaskName = None
        self._TaskType = None
        self._SourceResource = None
        self._TargetResource = None
        self._TransformParam = None
        self._PrivateLinkParam = None
        self._SchemaId = None
        self._TransformsParam = None
        self._TaskId = None
        self._Tags = None

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
    def TaskType(self):
        """任务类型，SOURCE数据接入，SINK数据流出
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def SourceResource(self):
        """数据源
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        """数据目标
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def TransformParam(self):
        """数据处理规则
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TransformParam`
        """
        return self._TransformParam

    @TransformParam.setter
    def TransformParam(self, TransformParam):
        self._TransformParam = TransformParam

    @property
    def PrivateLinkParam(self):
        """实例连接参数【已废弃】
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PrivateLinkParam`
        """
        return self._PrivateLinkParam

    @PrivateLinkParam.setter
    def PrivateLinkParam(self, PrivateLinkParam):
        self._PrivateLinkParam = PrivateLinkParam

    @property
    def SchemaId(self):
        """选择所要绑定的SchemaId
        :rtype: str
        """
        return self._SchemaId

    @SchemaId.setter
    def SchemaId(self, SchemaId):
        self._SchemaId = SchemaId

    @property
    def TransformsParam(self):
        """数据处理规则
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TransformsParam`
        """
        return self._TransformsParam

    @TransformsParam.setter
    def TransformsParam(self, TransformsParam):
        self._TransformsParam = TransformsParam

    @property
    def TaskId(self):
        """任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        if params.get("SourceResource") is not None:
            self._SourceResource = DatahubResource()
            self._SourceResource._deserialize(params.get("SourceResource"))
        if params.get("TargetResource") is not None:
            self._TargetResource = DatahubResource()
            self._TargetResource._deserialize(params.get("TargetResource"))
        if params.get("TransformParam") is not None:
            self._TransformParam = TransformParam()
            self._TransformParam._deserialize(params.get("TransformParam"))
        if params.get("PrivateLinkParam") is not None:
            self._PrivateLinkParam = PrivateLinkParam()
            self._PrivateLinkParam._deserialize(params.get("PrivateLinkParam"))
        self._SchemaId = params.get("SchemaId")
        if params.get("TransformsParam") is not None:
            self._TransformsParam = TransformsParam()
            self._TransformsParam._deserialize(params.get("TransformsParam"))
        self._TaskId = params.get("TaskId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatahubTaskRes(AbstractModel):
    """创建数据转储返回值

    """

    def __init__(self):
        r"""
        :param _TaskId: 转储任务id
        :type TaskId: str
        :param _DatahubId: 数据转储Id
        :type DatahubId: str
        """
        self._TaskId = None
        self._DatahubId = None

    @property
    def TaskId(self):
        """转储任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DatahubId(self):
        """数据转储Id
        :rtype: str
        """
        return self._DatahubId

    @DatahubId.setter
    def DatahubId(self, DatahubId):
        self._DatahubId = DatahubId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DatahubId = params.get("DatahubId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatahubTaskResponse(AbstractModel):
    """CreateDatahubTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTaskRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTaskRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateDatahubTaskRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateDatahubTopicRequest(AbstractModel):
    """CreateDatahubTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称，是一个不超过 128 个字符的字符串，必须以“AppId-”为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type Name: str
        :param _PartitionNum: Partition个数，大于0
        :type PartitionNum: int
        :param _RetentionMs: 消息保留时间，单位ms，当前最小值为60000ms
        :type RetentionMs: int
        :param _Note: 主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type Note: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._Name = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._Tags = None

    @property
    def Name(self):
        """名称，是一个不超过 128 个字符的字符串，必须以“AppId-”为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PartitionNum(self):
        """Partition个数，大于0
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """消息保留时间，单位ms，当前最小值为60000ms
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatahubTopicResponse(AbstractModel):
    """CreateDatahubTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回创建结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回创建结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateInstancePostData(AbstractModel):
    """创建后付费接口返回的 Data 数据结构

    """

    def __init__(self):
        r"""
        :param _FlowId: CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
        :type FlowId: int
        :param _DealNames: 订单号列表
        :type DealNames: list of str
        :param _InstanceId: ckafka集群实例Id，当购买多个实例时，默认返回购买的第一个实例 id
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: 订单和购买实例对应映射列表
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        """CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        """ckafka集群实例Id，当购买多个实例时，默认返回购买的第一个实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        """订单和购买实例对应映射列表
        :rtype: list of DealInstanceDTO
        """
        return self._DealNameInstanceIdMapping

    @DealNameInstanceIdMapping.setter
    def DealNameInstanceIdMapping(self, DealNameInstanceIdMapping):
        self._DealNameInstanceIdMapping = DealNameInstanceIdMapping


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._InstanceId = params.get("InstanceId")
        if params.get("DealNameInstanceIdMapping") is not None:
            self._DealNameInstanceIdMapping = []
            for item in params.get("DealNameInstanceIdMapping"):
                obj = DealInstanceDTO()
                obj._deserialize(item)
                self._DealNameInstanceIdMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostRequest(AbstractModel):
    """CreateInstancePost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: ckafka集群实例Name，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _VpcId: 私有网络Id 创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
        :type VpcId: str
        :param _SubnetId: 子网id。创建实例默认接入点所在的子网对应的子网 id
        :type SubnetId: str
        :param _BandWidth: 实例内网峰值带宽。单位 MB/s。标准版需传入当前实例规格所对应的峰值带宽。注意如果创建的实例为专业版实例，峰值带宽，分区数等参数配置需要满足专业版的计费规格。
        :type BandWidth: int
        :param _InstanceType: 国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :type InstanceType: int
        :param _MsgRetentionTime: 实例日志的默认最长保留时间，单位分钟。不传入该参数时默认为 1440 分钟（1天），最大30天。当 topic 显式设置消息保留时间时，以 topic 保留时间为准
        :type MsgRetentionTime: int
        :param _ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id。不指定实例所在集群则不传入该参数
        :type ClusterId: int
        :param _KafkaVersion: 实例版本。目前支持 "0.10.2","1.1.1","2.4.1","2.4.2","2.8.1"。"2.4.1" 与 "2.4.2" 属于同一个版本，传任意一个均可。
        :type KafkaVersion: str
        :param _SpecificationsType: 实例类型。"standard"：标准版，"profession"：专业版
        :type SpecificationsType: str
        :param _DiskType: 专业版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认值为 "CLOUD_BASIC"
        :type DiskType: str
        :param _DiskSize: 实例硬盘大小，需要满足当前实例的计费规格
        :type DiskSize: int
        :param _Partition: 实例最大分区数量，需要满足当前实例的计费规格
        :type Partition: int
        :param _TopicNum: 实例最大 topic 数量，需要满足当前实例的计费规格
        :type TopicNum: int
        :param _ZoneId: 实例所在的可用区。当创建多可用区实例时，该参数为创建的默认接入点所在子网的可用区 id
        :type ZoneId: int
        :param _MultiZoneFlag: 当前实例是否为多可用区实例。
        :type MultiZoneFlag: bool
        :param _ZoneIds: 当实例为多可用区实例时，多可用区 id 列表。注意参数 ZoneId 对应的多可用区需要包含在该参数数组中
        :type ZoneIds: list of int
        :param _InstanceNum: 购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :type InstanceNum: int
        :param _PublicNetworkMonthly: 公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。需要保证传入参数为 3 的整数倍
        :type PublicNetworkMonthly: int
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _ElasticBandwidthSwitch: 弹性带宽开关 0不开启  1开启（0默认）
        :type ElasticBandwidthSwitch: int
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._BandWidth = None
        self._InstanceType = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskType = None
        self._DiskSize = None
        self._Partition = None
        self._TopicNum = None
        self._ZoneId = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._InstanceNum = None
        self._PublicNetworkMonthly = None
        self._Tags = None
        self._ElasticBandwidthSwitch = None

    @property
    def InstanceName(self):
        """ckafka集群实例Name，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        """私有网络Id 创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id。创建实例默认接入点所在的子网对应的子网 id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def BandWidth(self):
        """实例内网峰值带宽。单位 MB/s。标准版需传入当前实例规格所对应的峰值带宽。注意如果创建的实例为专业版实例，峰值带宽，分区数等参数配置需要满足专业版的计费规格。
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def InstanceType(self):
        """国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        """实例日志的默认最长保留时间，单位分钟。不传入该参数时默认为 1440 分钟（1天），最大30天。当 topic 显式设置消息保留时间时，以 topic 保留时间为准
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        """创建实例时可以选择集群Id, 该入参表示集群Id。不指定实例所在集群则不传入该参数
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        """实例版本。目前支持 "0.10.2","1.1.1","2.4.1","2.4.2","2.8.1"。"2.4.1" 与 "2.4.2" 属于同一个版本，传任意一个均可。
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        """实例类型。"standard"：标准版，"profession"：专业版
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        """专业版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认值为 "CLOUD_BASIC"
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """实例硬盘大小，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        """实例最大分区数量，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        """实例最大 topic 数量，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        """实例所在的可用区。当创建多可用区实例时，该参数为创建的默认接入点所在子网的可用区 id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        """当前实例是否为多可用区实例。
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        """当实例为多可用区实例时，多可用区 id 列表。注意参数 ZoneId 对应的多可用区需要包含在该参数数组中
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        """购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        """公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。需要保证传入参数为 3 的整数倍
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ElasticBandwidthSwitch(self):
        """弹性带宽开关 0不开启  1开启（0默认）
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._BandWidth = params.get("BandWidth")
        self._InstanceType = params.get("InstanceType")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._Partition = params.get("Partition")
        self._TopicNum = params.get("TopicNum")
        self._ZoneId = params.get("ZoneId")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceNum = params.get("InstanceNum")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostResp(AbstractModel):
    """后付费实例相关接口返回结构

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param _ReturnMessage: 接口返回消息，当接口报错时提示错误信息
        :type ReturnMessage: str
        :param _Data: 返回的Data数据
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        """返回的code，0为正常，非0为错误
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """接口返回消息，当接口报错时提示错误信息
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """返回的Data数据
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = CreateInstancePostData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePostResponse(AbstractModel):
    """CreateInstancePost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateInstancePreData(AbstractModel):
    """创建预付费接口返回的Data

    """

    def __init__(self):
        r"""
        :param _FlowId: CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
        :type FlowId: int
        :param _DealNames: 订单号列表
        :type DealNames: list of str
        :param _InstanceId: ckafka集群实例Id，当购买多个实例时，默认返回购买的第一个实例 id
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: 订单和购买实例对应映射列表
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        """CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        """订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        """ckafka集群实例Id，当购买多个实例时，默认返回购买的第一个实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
        """订单和购买实例对应映射列表
        :rtype: list of DealInstanceDTO
        """
        return self._DealNameInstanceIdMapping

    @DealNameInstanceIdMapping.setter
    def DealNameInstanceIdMapping(self, DealNameInstanceIdMapping):
        self._DealNameInstanceIdMapping = DealNameInstanceIdMapping


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._DealNames = params.get("DealNames")
        self._InstanceId = params.get("InstanceId")
        if params.get("DealNameInstanceIdMapping") is not None:
            self._DealNameInstanceIdMapping = []
            for item in params.get("DealNameInstanceIdMapping"):
                obj = DealInstanceDTO()
                obj._deserialize(item)
                self._DealNameInstanceIdMapping.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreRequest(AbstractModel):
    """CreateInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: ckafka集群实例Name，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _ZoneId: 可用区。当购买多可用区实例时，当前参数为主可用区。  [查看可用区](https://cloud.tencent.com/document/product/597/55246)
        :type ZoneId: int
        :param _Period: 预付费购买时长，例如 "1m",就是一个月
        :type Period: str
        :param _InstanceType: 国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :type InstanceType: int
        :param _VpcId: 私有网络Id，必填
        :type VpcId: str
        :param _SubnetId: 子网id，必填
        :type SubnetId: str
        :param _MsgRetentionTime: 可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param _ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id
        :type ClusterId: int
        :param _RenewFlag: 预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type RenewFlag: int
        :param _KafkaVersion: CKafka版本号[0.10.2、1.1.1、2.4.1、2.4.2、2.8.1、3.2.3], 默认是1.1.1。2.4.1 与 2.4.2 属于同一个版本，传任意一个均可。
        :type KafkaVersion: str
        :param _SpecificationsType: 实例类型: [标准版实例]填写 "standard" (默认), [专业版实例]填写 "profession",[高级版实例]填写"premium"
        :type SpecificationsType: str
        :param _DiskSize: 磁盘大小，如果跟控制台规格配比不相符，则无法创建成功
        :type DiskSize: int
        :param _BandWidth: 实例带宽,单位MB/s; 最小值:20MB/s, 高级版最大值:360MB/s,专业版最大值:100000MB/s  标准版固定带宽规格: 40MB/s, 100MB/s, 150MB/s
        :type BandWidth: int
        :param _Partition: 分区大小，如果跟控制台规格配比不相符，则无法创建成功
        :type Partition: int
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _DiskType: 专业版/高级版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认为 "CLOUD_BASIC"
        :type DiskType: str
        :param _MultiZoneFlag: 是否创建跨可用区实例，当前参数为 true 时，zoneIds必填
        :type MultiZoneFlag: bool
        :param _ZoneIds: 可用区列表，购买多可用区实例时为必填项
        :type ZoneIds: list of int
        :param _PublicNetworkMonthly: 公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。默认值为 0。需要保证传入参数为 3 的整数倍
        :type PublicNetworkMonthly: int
        :param _InstanceNum: 购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :type InstanceNum: int
        :param _AutoVoucher: 是否自动选择代金券:1-是;0否。默认为0
        :type AutoVoucher: int
        :param _ElasticBandwidthSwitch: 弹性带宽开关 0不开启  1开启（0默认）
        :type ElasticBandwidthSwitch: int
        """
        self._InstanceName = None
        self._ZoneId = None
        self._Period = None
        self._InstanceType = None
        self._VpcId = None
        self._SubnetId = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._RenewFlag = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None
        self._Tags = None
        self._DiskType = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._PublicNetworkMonthly = None
        self._InstanceNum = None
        self._AutoVoucher = None
        self._ElasticBandwidthSwitch = None

    @property
    def InstanceName(self):
        """ckafka集群实例Name，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ZoneId(self):
        """可用区。当购买多可用区实例时，当前参数为主可用区。  [查看可用区](https://cloud.tencent.com/document/product/597/55246)
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Period(self):
        """预付费购买时长，例如 "1m",就是一个月
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceType(self):
        """国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VpcId(self):
        """私有网络Id，必填
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id，必填
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MsgRetentionTime(self):
        """可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        """创建实例时可以选择集群Id, 该入参表示集群Id
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RenewFlag(self):
        """预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def KafkaVersion(self):
        """CKafka版本号[0.10.2、1.1.1、2.4.1、2.4.2、2.8.1、3.2.3], 默认是1.1.1。2.4.1 与 2.4.2 属于同一个版本，传任意一个均可。
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        """实例类型: [标准版实例]填写 "standard" (默认), [专业版实例]填写 "profession",[高级版实例]填写"premium"
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskSize(self):
        """磁盘大小，如果跟控制台规格配比不相符，则无法创建成功
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        """实例带宽,单位MB/s; 最小值:20MB/s, 高级版最大值:360MB/s,专业版最大值:100000MB/s  标准版固定带宽规格: 40MB/s, 100MB/s, 150MB/s
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        """分区大小，如果跟控制台规格配比不相符，则无法创建成功
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskType(self):
        """专业版/高级版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认为 "CLOUD_BASIC"
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MultiZoneFlag(self):
        """是否创建跨可用区实例，当前参数为 true 时，zoneIds必填
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        """可用区列表，购买多可用区实例时为必填项
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PublicNetworkMonthly(self):
        """公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。默认值为 0。需要保证传入参数为 3 的整数倍
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def InstanceNum(self):
        """购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def AutoVoucher(self):
        """是否自动选择代金券:1-是;0否。默认为0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def ElasticBandwidthSwitch(self):
        """弹性带宽开关 0不开启  1开启（0默认）
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Period = params.get("Period")
        self._InstanceType = params.get("InstanceType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._RenewFlag = params.get("RenewFlag")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskSize = params.get("DiskSize")
        self._BandWidth = params.get("BandWidth")
        self._Partition = params.get("Partition")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DiskType = params.get("DiskType")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        self._InstanceNum = params.get("InstanceNum")
        self._AutoVoucher = params.get("AutoVoucher")
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResp(AbstractModel):
    """预付费实例相关接口返回结构

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param _ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param _Data: 操作型返回的Data数据
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        :param _DeleteRouteTimestamp: 删除时间。目前该参数字段已废弃，将会在未来被删除
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteRouteTimestamp: str
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None
        self._DeleteRouteTimestamp = None

    @property
    def ReturnCode(self):
        """返回的code，0为正常，非0为错误
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """成功消息
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """操作型返回的Data数据
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DeleteRouteTimestamp(self):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

        """删除时间。目前该参数字段已废弃，将会在未来被删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

        self._DeleteRouteTimestamp = DeleteRouteTimestamp


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = CreateInstancePreData()
            self._Data._deserialize(params.get("Data"))
        self._DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResponse(AbstractModel):
    """CreateInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePartitionRequest(AbstractModel):
    """CreatePartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _PartitionNum: 主题分区个数
        :type PartitionNum: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._PartitionNum = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """主题分区个数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionResponse(AbstractModel):
    """CreatePartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果集
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePostPaidInstanceRequest(AbstractModel):
    """CreatePostPaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: ckafka集群实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _VpcId: 私有网络Id  创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
        :type VpcId: str
        :param _SubnetId: 子网id。创建实例默认接入点所在的子网对应的子网 id
        :type SubnetId: str
        :param _InstanceType: 国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :type InstanceType: int
        :param _MsgRetentionTime: 实例日志的默认最长保留时间，单位分钟。不传入该参数时默认为 1440 分钟（1天），最大30天。当 topic 显式设置消息保留时间时，以 topic 保留时间为准
        :type MsgRetentionTime: int
        :param _ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id。不指定实例所在集群则不传入该参数
        :type ClusterId: int
        :param _KafkaVersion: 实例版本。目前支持 "0.10.2","1.1.1","2.4.1","2.4.2","2.8.1"。"2.4.1" 与 "2.4.2" 属于同一个版本，传任意一个均可。
        :type KafkaVersion: str
        :param _SpecificationsType: 实例类型。"standard"：标准版，"profession"：专业版。  (标准版仅国际站支持，国内站目前支持专业版)
        :type SpecificationsType: str
        :param _DiskType: 专业版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认值为 "CLOUD_BASIC"
        :type DiskType: str
        :param _BandWidth: 实例内网峰值带宽。单位 MB/s。标准版需传入当前实例规格所对应的峰值带宽。注意如果创建的实例为专业版实例，峰值带宽，分区数等参数配置需要满足专业版的计费规格。
        :type BandWidth: int
        :param _DiskSize: 实例硬盘大小，需要满足当前实例的计费规格
        :type DiskSize: int
        :param _Partition: 实例最大分区数量，需要满足当前实例的计费规格
        :type Partition: int
        :param _TopicNum: 实例最大 topic 数量，需要满足当前实例的计费规格
        :type TopicNum: int
        :param _ZoneId: 实例所在的可用区。当创建多可用区实例时，该参数为创建的默认接入点所在子网的可用区 id
        :type ZoneId: int
        :param _MultiZoneFlag: 当前实例是否为多可用区实例。
        :type MultiZoneFlag: bool
        :param _ZoneIds: 当实例为多可用区实例时，多可用区 id 列表。注意参数 ZoneId 对应的多可用区需要包含在该参数数组中
        :type ZoneIds: list of int
        :param _InstanceNum: 购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :type InstanceNum: int
        :param _PublicNetworkMonthly: 公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。需要保证传入参数为 3 的整数倍
        :type PublicNetworkMonthly: int
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _ElasticBandwidthSwitch: 弹性带宽开关 0不开启  1开启（0默认)
        :type ElasticBandwidthSwitch: int
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceType = None
        self._MsgRetentionTime = None
        self._ClusterId = None
        self._KafkaVersion = None
        self._SpecificationsType = None
        self._DiskType = None
        self._BandWidth = None
        self._DiskSize = None
        self._Partition = None
        self._TopicNum = None
        self._ZoneId = None
        self._MultiZoneFlag = None
        self._ZoneIds = None
        self._InstanceNum = None
        self._PublicNetworkMonthly = None
        self._Tags = None
        self._ElasticBandwidthSwitch = None

    @property
    def InstanceName(self):
        """ckafka集群实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        """私有网络Id  创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id。创建实例默认接入点所在的子网对应的子网 id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        """国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        """实例日志的默认最长保留时间，单位分钟。不传入该参数时默认为 1440 分钟（1天），最大30天。当 topic 显式设置消息保留时间时，以 topic 保留时间为准
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        """创建实例时可以选择集群Id, 该入参表示集群Id。不指定实例所在集群则不传入该参数
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        """实例版本。目前支持 "0.10.2","1.1.1","2.4.1","2.4.2","2.8.1"。"2.4.1" 与 "2.4.2" 属于同一个版本，传任意一个均可。
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        """实例类型。"standard"：标准版，"profession"：专业版。  (标准版仅国际站支持，国内站目前支持专业版)
        :rtype: str
        """
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        """专业版实例磁盘类型，标准版实例不需要填写。"CLOUD_SSD"：SSD云硬盘；"CLOUD_BASIC"：高性能云硬盘。不传默认值为 "CLOUD_BASIC"
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BandWidth(self):
        """实例内网峰值带宽。单位 MB/s。标准版需传入当前实例规格所对应的峰值带宽。注意如果创建的实例为专业版实例，峰值带宽，分区数等参数配置需要满足专业版的计费规格。
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def DiskSize(self):
        """实例硬盘大小，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        """实例最大分区数量，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        """实例最大 topic 数量，需要满足当前实例的计费规格
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        """实例所在的可用区。当创建多可用区实例时，该参数为创建的默认接入点所在子网的可用区 id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        """当前实例是否为多可用区实例。
        :rtype: bool
        """
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        """当实例为多可用区实例时，多可用区 id 列表。注意参数 ZoneId 对应的多可用区需要包含在该参数数组中
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        """购买实例数量。非必填，默认值为 1。当传入该参数时，会创建多个 instanceName 加后缀区分的实例
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        """公网带宽大小，单位 Mbps。默认是没有加上免费 3Mbps 带宽。例如总共需要 3Mbps 公网带宽，此处传 0；总共需要 6Mbps 公网带宽，此处传 3。需要保证传入参数为 3 的整数倍
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ElasticBandwidthSwitch(self):
        """弹性带宽开关 0不开启  1开启（0默认)
        :rtype: int
        """
        return self._ElasticBandwidthSwitch

    @ElasticBandwidthSwitch.setter
    def ElasticBandwidthSwitch(self, ElasticBandwidthSwitch):
        self._ElasticBandwidthSwitch = ElasticBandwidthSwitch


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceType = params.get("InstanceType")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._ClusterId = params.get("ClusterId")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SpecificationsType = params.get("SpecificationsType")
        self._DiskType = params.get("DiskType")
        self._BandWidth = params.get("BandWidth")
        self._DiskSize = params.get("DiskSize")
        self._Partition = params.get("Partition")
        self._TopicNum = params.get("TopicNum")
        self._ZoneId = params.get("ZoneId")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._ZoneIds = params.get("ZoneIds")
        self._InstanceNum = params.get("InstanceNum")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ElasticBandwidthSwitch = params.get("ElasticBandwidthSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePostPaidInstanceResponse(AbstractModel):
    """CreatePostPaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateInstancePostResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePrometheusRequest(AbstractModel):
    """CreatePrometheus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _VpcId: 私有网络Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """私有网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusResponse(AbstractModel):
    """CreatePrometheus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 打通普罗米修斯
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.PrometheusResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """打通普罗米修斯
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PrometheusResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = PrometheusResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateRouteRequest(AbstractModel):
    """CreateRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例唯一id
        :type InstanceId: str
        :param _VipType: 路由网络类型(3:vpc路由;7:内部支撑路由)
        :type VipType: int
        :param _VpcId: vpc网络Id
        :type VpcId: str
        :param _SubnetId: vpc子网id
        :type SubnetId: str
        :param _AccessType: 访问类型：0-plaintext；1-sasl_plaintext；2-ssl；3-sasl_ssl
        :type AccessType: int
        :param _AuthFlag: 是否需要权限管理
        :type AuthFlag: int
        :param _CallerAppid: 调用方appId
        :type CallerAppid: int
        :param _PublicNetwork: 公网带宽
        :type PublicNetwork: int
        :param _Ip: vip地址
        :type Ip: str
        """
        self._InstanceId = None
        self._VipType = None
        self._VpcId = None
        self._SubnetId = None
        self._AccessType = None
        self._AuthFlag = None
        self._CallerAppid = None
        self._PublicNetwork = None
        self._Ip = None

    @property
    def InstanceId(self):
        """实例唯一id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VipType(self):
        """路由网络类型(3:vpc路由;7:内部支撑路由)
        :rtype: int
        """
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VpcId(self):
        """vpc网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """vpc子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AccessType(self):
        """访问类型：0-plaintext；1-sasl_plaintext；2-ssl；3-sasl_ssl
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AuthFlag(self):
        """是否需要权限管理
        :rtype: int
        """
        return self._AuthFlag

    @AuthFlag.setter
    def AuthFlag(self, AuthFlag):
        self._AuthFlag = AuthFlag

    @property
    def CallerAppid(self):
        """调用方appId
        :rtype: int
        """
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def PublicNetwork(self):
        """公网带宽
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def Ip(self):
        """vip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VipType = params.get("VipType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AccessType = params.get("AccessType")
        self._AuthFlag = params.get("AuthFlag")
        self._CallerAppid = params.get("CallerAppid")
        self._PublicNetwork = params.get("PublicNetwork")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteResponse(AbstractModel):
    """CreateRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTokenRequest(AbstractModel):
    """CreateToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _User: 用户名
        :type User: str
        """
        self._InstanceId = None
        self._User = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenResponse(AbstractModel):
    """CreateToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: token串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """token串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        """ip白名单列表
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """删除主题IP白名单结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _TopicName: 主题名称，是一个不超过 128 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type TopicName: str
        :param _PartitionNum: Partition个数，大于0
        :type PartitionNum: int
        :param _ReplicaNum: 副本个数，不能多于 broker 数，最大为3
        :type ReplicaNum: int
        :param _EnableWhiteList: ip白名单开关, 1:打开  0:关闭，默认不打开
        :type EnableWhiteList: int
        :param _IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选
        :type IpWhiteList: list of str
        :param _CleanUpPolicy: 清理日志策略，日志清理模式，默认为"delete"。"delete"：日志按保存时间删除，"compact"：日志按 key 压缩，"compact, delete"：日志按 key 压缩且会按保存时间删除。
        :type CleanUpPolicy: str
        :param _Note: 主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type Note: str
        :param _MinInsyncReplicas: 默认为1
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: 是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许
        :type UncleanLeaderElectionEnable: int
        :param _RetentionMs: 可选参数。消息保留时间，单位ms，当前最小值为60000ms
        :type RetentionMs: int
        :param _SegmentMs: Segment分片滚动的时长，单位ms，当前最小为3600000ms
        :type SegmentMs: int
        :param _MaxMessageBytes: 主题消息最大值，单位为 Byte，最小值1024Byte(即1KB)，最大值为12582912Byte（即12MB）
        :type MaxMessageBytes: int
        :param _EnableAclRule: 预设ACL规则, 1:打开  0:关闭，默认不打开
        :type EnableAclRule: int
        :param _AclRuleName: 预设ACL规则的名称
        :type AclRuleName: str
        :param _RetentionBytes: 可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :type RetentionBytes: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._InstanceId = None
        self._TopicName = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._EnableWhiteList = None
        self._IpWhiteList = None
        self._CleanUpPolicy = None
        self._Note = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._SegmentMs = None
        self._MaxMessageBytes = None
        self._EnableAclRule = None
        self._AclRuleName = None
        self._RetentionBytes = None
        self._Tags = None

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
    def TopicName(self):
        """主题名称，是一个不超过 128 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """Partition个数，大于0
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """副本个数，不能多于 broker 数，最大为3
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def EnableWhiteList(self):
        """ip白名单开关, 1:打开  0:关闭，默认不打开
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        """Ip白名单列表，配额限制，enableWhileList=1时必选
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def CleanUpPolicy(self):
        """清理日志策略，日志清理模式，默认为"delete"。"delete"：日志按保存时间删除，"compact"：日志按 key 压缩，"compact, delete"：日志按 key 压缩且会按保存时间删除。
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def Note(self):
        """主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def MinInsyncReplicas(self):
        """默认为1
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """可选参数。消息保留时间，单位ms，当前最小值为60000ms
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def SegmentMs(self):
        """Segment分片滚动的时长，单位ms，当前最小为3600000ms
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        """主题消息最大值，单位为 Byte，最小值1024Byte(即1KB)，最大值为12582912Byte（即12MB）
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def EnableAclRule(self):
        """预设ACL规则, 1:打开  0:关闭，默认不打开
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        """预设ACL规则的名称
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        """可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteList = params.get("IpWhiteList")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._Note = params.get("Note")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._SegmentMs = params.get("SegmentMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._EnableAclRule = params.get("EnableAclRule")
        self._AclRuleName = params.get("AclRuleName")
        self._RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    """创建主题返回

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题Id
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回创建结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回创建结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Name: 用户名称
        :type Name: str
        :param _Password: 用户密码
        :type Password: str
        """
        self._InstanceId = None
        self._Name = None
        self._Password = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """用户名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """用户密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
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
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CtsdbConnectParam(AbstractModel):
    """Ctsdb连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: Ctsdb的连接port
        :type Port: int
        :param _ServiceVip: Ctsdb连接源的实例vip
        :type ServiceVip: str
        :param _UniqVpcId: Ctsdb连接源的vpcId
        :type UniqVpcId: str
        :param _UserName: Ctsdb连接源的用户名
        :type UserName: str
        :param _Password: Ctsdb连接源的密码
        :type Password: str
        :param _Resource: Ctsdb连接源的实例资源
        :type Resource: str
        """
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._Resource = None

    @property
    def Port(self):
        """Ctsdb的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """Ctsdb连接源的实例vip
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Ctsdb连接源的vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """Ctsdb连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Ctsdb连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """Ctsdb连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CtsdbModifyConnectParam(AbstractModel):
    """Ctsdb连接源参数(更新)

    """

    def __init__(self):
        r"""
        :param _Port: Ctsdb的连接port
        :type Port: int
        :param _ServiceVip: Ctsdb连接源的实例vip
        :type ServiceVip: str
        :param _UniqVpcId: Ctsdb连接源的vpcId
        :type UniqVpcId: str
        :param _UserName: Ctsdb连接源的用户名
        :type UserName: str
        :param _Password: Ctsdb连接源的密码
        :type Password: str
        :param _Resource: Ctsdb连接源的实例资源
        :type Resource: str
        """
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._Resource = None

    @property
    def Port(self):
        """Ctsdb的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """Ctsdb连接源的实例vip
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Ctsdb连接源的vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """Ctsdb连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Ctsdb连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """Ctsdb连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CtsdbParam(AbstractModel):
    """Ctsdb类型入参

    """

    def __init__(self):
        r"""
        :param _Resource: 连接管理实例资源
        :type Resource: str
        :param _CtsdbMetric: Ctsdb的metric
        :type CtsdbMetric: str
        """
        self._Resource = None
        self._CtsdbMetric = None

    @property
    def Resource(self):
        """连接管理实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def CtsdbMetric(self):
        """Ctsdb的metric
        :rtype: str
        """
        return self._CtsdbMetric

    @CtsdbMetric.setter
    def CtsdbMetric(self, CtsdbMetric):
        self._CtsdbMetric = CtsdbMetric


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._CtsdbMetric = params.get("CtsdbMetric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubResource(AbstractModel):
    """Datahub资源配置

    """

    def __init__(self):
        r"""
        :param _Type: 资源类型
        :type Type: str
        :param _KafkaParam: ckafka配置，Type为KAFKA时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaParam`
        :param _EventBusParam: EB配置，Type为EB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type EventBusParam: :class:`tencentcloud.ckafka.v20190819.models.EventBusParam`
        :param _MongoDBParam: MongoDB配置，Type为MONGODB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type MongoDBParam: :class:`tencentcloud.ckafka.v20190819.models.MongoDBParam`
        :param _EsParam: Es配置，Type为ES时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type EsParam: :class:`tencentcloud.ckafka.v20190819.models.EsParam`
        :param _TdwParam: Tdw配置，Type为TDW时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TdwParam: :class:`tencentcloud.ckafka.v20190819.models.TdwParam`
        :param _DtsParam: Dts配置，Type为DTS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsParam: :class:`tencentcloud.ckafka.v20190819.models.DtsParam`
        :param _ClickHouseParam: ClickHouse配置，Type为CLICKHOUSE时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ClickHouseParam: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseParam`
        :param _ClsParam: Cls配置，Type为CLS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsParam: :class:`tencentcloud.ckafka.v20190819.models.ClsParam`
        :param _CosParam: Cos配置，Type为COS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type CosParam: :class:`tencentcloud.ckafka.v20190819.models.CosParam`
        :param _MySQLParam: MySQL配置，Type为MYSQL时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type MySQLParam: :class:`tencentcloud.ckafka.v20190819.models.MySQLParam`
        :param _PostgreSQLParam: PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type PostgreSQLParam: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLParam`
        :param _TopicParam: Topic配置，Type为Topic时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicParam: :class:`tencentcloud.ckafka.v20190819.models.TopicParam`
        :param _MariaDBParam: MariaDB配置，Type为MARIADB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type MariaDBParam: :class:`tencentcloud.ckafka.v20190819.models.MariaDBParam`
        :param _SQLServerParam: SQLServer配置，Type为SQLSERVER时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLServerParam: :class:`tencentcloud.ckafka.v20190819.models.SQLServerParam`
        :param _CtsdbParam: Ctsdb配置，Type为CTSDB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type CtsdbParam: :class:`tencentcloud.ckafka.v20190819.models.CtsdbParam`
        :param _ScfParam: Scf配置，Type为SCF时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfParam: :class:`tencentcloud.ckafka.v20190819.models.ScfParam`
        :param _MqttParam: MQTT配置，Type为 MQTT 时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type MqttParam: :class:`tencentcloud.ckafka.v20190819.models.MqttParam`
        """
        self._Type = None
        self._KafkaParam = None
        self._EventBusParam = None
        self._MongoDBParam = None
        self._EsParam = None
        self._TdwParam = None
        self._DtsParam = None
        self._ClickHouseParam = None
        self._ClsParam = None
        self._CosParam = None
        self._MySQLParam = None
        self._PostgreSQLParam = None
        self._TopicParam = None
        self._MariaDBParam = None
        self._SQLServerParam = None
        self._CtsdbParam = None
        self._ScfParam = None
        self._MqttParam = None

    @property
    def Type(self):
        """资源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def KafkaParam(self):
        """ckafka配置，Type为KAFKA时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaParam`
        """
        return self._KafkaParam

    @KafkaParam.setter
    def KafkaParam(self, KafkaParam):
        self._KafkaParam = KafkaParam

    @property
    def EventBusParam(self):
        """EB配置，Type为EB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EventBusParam`
        """
        return self._EventBusParam

    @EventBusParam.setter
    def EventBusParam(self, EventBusParam):
        self._EventBusParam = EventBusParam

    @property
    def MongoDBParam(self):
        """MongoDB配置，Type为MONGODB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MongoDBParam`
        """
        return self._MongoDBParam

    @MongoDBParam.setter
    def MongoDBParam(self, MongoDBParam):
        self._MongoDBParam = MongoDBParam

    @property
    def EsParam(self):
        """Es配置，Type为ES时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EsParam`
        """
        return self._EsParam

    @EsParam.setter
    def EsParam(self, EsParam):
        self._EsParam = EsParam

    @property
    def TdwParam(self):
        """Tdw配置，Type为TDW时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TdwParam`
        """
        return self._TdwParam

    @TdwParam.setter
    def TdwParam(self, TdwParam):
        self._TdwParam = TdwParam

    @property
    def DtsParam(self):
        """Dts配置，Type为DTS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DtsParam`
        """
        return self._DtsParam

    @DtsParam.setter
    def DtsParam(self, DtsParam):
        self._DtsParam = DtsParam

    @property
    def ClickHouseParam(self):
        """ClickHouse配置，Type为CLICKHOUSE时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseParam`
        """
        return self._ClickHouseParam

    @ClickHouseParam.setter
    def ClickHouseParam(self, ClickHouseParam):
        self._ClickHouseParam = ClickHouseParam

    @property
    def ClsParam(self):
        """Cls配置，Type为CLS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClsParam`
        """
        return self._ClsParam

    @ClsParam.setter
    def ClsParam(self, ClsParam):
        self._ClsParam = ClsParam

    @property
    def CosParam(self):
        """Cos配置，Type为COS时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CosParam`
        """
        return self._CosParam

    @CosParam.setter
    def CosParam(self, CosParam):
        self._CosParam = CosParam

    @property
    def MySQLParam(self):
        """MySQL配置，Type为MYSQL时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MySQLParam`
        """
        return self._MySQLParam

    @MySQLParam.setter
    def MySQLParam(self, MySQLParam):
        self._MySQLParam = MySQLParam

    @property
    def PostgreSQLParam(self):
        """PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLParam`
        """
        return self._PostgreSQLParam

    @PostgreSQLParam.setter
    def PostgreSQLParam(self, PostgreSQLParam):
        self._PostgreSQLParam = PostgreSQLParam

    @property
    def TopicParam(self):
        """Topic配置，Type为Topic时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicParam`
        """
        return self._TopicParam

    @TopicParam.setter
    def TopicParam(self, TopicParam):
        self._TopicParam = TopicParam

    @property
    def MariaDBParam(self):
        """MariaDB配置，Type为MARIADB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MariaDBParam`
        """
        return self._MariaDBParam

    @MariaDBParam.setter
    def MariaDBParam(self, MariaDBParam):
        self._MariaDBParam = MariaDBParam

    @property
    def SQLServerParam(self):
        """SQLServer配置，Type为SQLSERVER时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SQLServerParam`
        """
        return self._SQLServerParam

    @SQLServerParam.setter
    def SQLServerParam(self, SQLServerParam):
        self._SQLServerParam = SQLServerParam

    @property
    def CtsdbParam(self):
        """Ctsdb配置，Type为CTSDB时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CtsdbParam`
        """
        return self._CtsdbParam

    @CtsdbParam.setter
    def CtsdbParam(self, CtsdbParam):
        self._CtsdbParam = CtsdbParam

    @property
    def ScfParam(self):
        """Scf配置，Type为SCF时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ScfParam`
        """
        return self._ScfParam

    @ScfParam.setter
    def ScfParam(self, ScfParam):
        self._ScfParam = ScfParam

    @property
    def MqttParam(self):
        """MQTT配置，Type为 MQTT 时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MqttParam`
        """
        return self._MqttParam

    @MqttParam.setter
    def MqttParam(self, MqttParam):
        self._MqttParam = MqttParam


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("KafkaParam") is not None:
            self._KafkaParam = KafkaParam()
            self._KafkaParam._deserialize(params.get("KafkaParam"))
        if params.get("EventBusParam") is not None:
            self._EventBusParam = EventBusParam()
            self._EventBusParam._deserialize(params.get("EventBusParam"))
        if params.get("MongoDBParam") is not None:
            self._MongoDBParam = MongoDBParam()
            self._MongoDBParam._deserialize(params.get("MongoDBParam"))
        if params.get("EsParam") is not None:
            self._EsParam = EsParam()
            self._EsParam._deserialize(params.get("EsParam"))
        if params.get("TdwParam") is not None:
            self._TdwParam = TdwParam()
            self._TdwParam._deserialize(params.get("TdwParam"))
        if params.get("DtsParam") is not None:
            self._DtsParam = DtsParam()
            self._DtsParam._deserialize(params.get("DtsParam"))
        if params.get("ClickHouseParam") is not None:
            self._ClickHouseParam = ClickHouseParam()
            self._ClickHouseParam._deserialize(params.get("ClickHouseParam"))
        if params.get("ClsParam") is not None:
            self._ClsParam = ClsParam()
            self._ClsParam._deserialize(params.get("ClsParam"))
        if params.get("CosParam") is not None:
            self._CosParam = CosParam()
            self._CosParam._deserialize(params.get("CosParam"))
        if params.get("MySQLParam") is not None:
            self._MySQLParam = MySQLParam()
            self._MySQLParam._deserialize(params.get("MySQLParam"))
        if params.get("PostgreSQLParam") is not None:
            self._PostgreSQLParam = PostgreSQLParam()
            self._PostgreSQLParam._deserialize(params.get("PostgreSQLParam"))
        if params.get("TopicParam") is not None:
            self._TopicParam = TopicParam()
            self._TopicParam._deserialize(params.get("TopicParam"))
        if params.get("MariaDBParam") is not None:
            self._MariaDBParam = MariaDBParam()
            self._MariaDBParam._deserialize(params.get("MariaDBParam"))
        if params.get("SQLServerParam") is not None:
            self._SQLServerParam = SQLServerParam()
            self._SQLServerParam._deserialize(params.get("SQLServerParam"))
        if params.get("CtsdbParam") is not None:
            self._CtsdbParam = CtsdbParam()
            self._CtsdbParam._deserialize(params.get("CtsdbParam"))
        if params.get("ScfParam") is not None:
            self._ScfParam = ScfParam()
            self._ScfParam._deserialize(params.get("ScfParam"))
        if params.get("MqttParam") is not None:
            self._MqttParam = MqttParam()
            self._MqttParam._deserialize(params.get("MqttParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTaskIdRes(AbstractModel):
    """Datahub请求的taskid

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTaskInfo(AbstractModel):
    """Datahub任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskType: 任务类型，SOURCE数据接入，SINK数据流出
        :type TaskType: str
        :param _Status: 状态，-1创建失败，0创建中，1运行中，2删除中，3已删除，4删除失败，5暂停中，6已暂停，7暂停失败，8恢复中，9恢复失败
        :type Status: int
        :param _SourceResource: 数据源
        :type SourceResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TargetResource: 数据目标
        :type TargetResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _ErrorMessage: 异常信息
        :type ErrorMessage: str
        :param _TaskProgress: 创建进度百分比
        :type TaskProgress: float
        :param _TaskCurrentStep: 任务当前处于的步骤
        :type TaskCurrentStep: str
        :param _DatahubId: Datahub转储Id
        :type DatahubId: str
        :param _StepList: 步骤列表
        :type StepList: list of str
        """
        self._TaskId = None
        self._TaskName = None
        self._TaskType = None
        self._Status = None
        self._SourceResource = None
        self._TargetResource = None
        self._CreateTime = None
        self._ErrorMessage = None
        self._TaskProgress = None
        self._TaskCurrentStep = None
        self._DatahubId = None
        self._StepList = None

    @property
    def TaskId(self):
        """任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def TaskType(self):
        """任务类型，SOURCE数据接入，SINK数据流出
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        """状态，-1创建失败，0创建中，1运行中，2删除中，3已删除，4删除失败，5暂停中，6已暂停，7暂停失败，8恢复中，9恢复失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceResource(self):
        """数据源
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        """数据目标
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ErrorMessage(self):
        """异常信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def TaskProgress(self):
        """创建进度百分比
        :rtype: float
        """
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def TaskCurrentStep(self):
        """任务当前处于的步骤
        :rtype: str
        """
        return self._TaskCurrentStep

    @TaskCurrentStep.setter
    def TaskCurrentStep(self, TaskCurrentStep):
        self._TaskCurrentStep = TaskCurrentStep

    @property
    def DatahubId(self):
        """Datahub转储Id
        :rtype: str
        """
        return self._DatahubId

    @DatahubId.setter
    def DatahubId(self, DatahubId):
        self._DatahubId = DatahubId

    @property
    def StepList(self):
        """步骤列表
        :rtype: list of str
        """
        return self._StepList

    @StepList.setter
    def StepList(self, StepList):
        self._StepList = StepList


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        if params.get("SourceResource") is not None:
            self._SourceResource = DatahubResource()
            self._SourceResource._deserialize(params.get("SourceResource"))
        if params.get("TargetResource") is not None:
            self._TargetResource = DatahubResource()
            self._TargetResource._deserialize(params.get("TargetResource"))
        self._CreateTime = params.get("CreateTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._TaskProgress = params.get("TaskProgress")
        self._TaskCurrentStep = params.get("TaskCurrentStep")
        self._DatahubId = params.get("DatahubId")
        self._StepList = params.get("StepList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTopicDTO(AbstractModel):
    """Datahub主题

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _TopicId: Topic Id
        :type TopicId: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _RetentionMs: 过期时间
        :type RetentionMs: int
        :param _Note: 备注
        :type Note: str
        :param _Status: 状态，1使用中，2删除中
        :type Status: int
        """
        self._Name = None
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._Status = None

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
    def TopicName(self):
        """Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """Topic Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """过期时间
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Status(self):
        """状态，1使用中，2删除中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatahubTopicResp(AbstractModel):
    """Datahub Topic 响应

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _TopicId: 主题Id
        :type TopicId: str
        """
        self._TopicName = None
        self._TopicId = None

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DateParam(AbstractModel):
    """数据处理——Value处理参数——转换时间格式参数

    """

    def __init__(self):
        r"""
        :param _Format: 时间格式
        :type Format: str
        :param _TargetType: 输入类型，string，unix时间戳，默认string
        :type TargetType: str
        :param _TimeZone: 时区，默认GMT+8
        :type TimeZone: str
        """
        self._Format = None
        self._TargetType = None
        self._TimeZone = None

    @property
    def Format(self):
        """时间格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TargetType(self):
        """输入类型，string，unix时间戳，默认string
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TimeZone(self):
        """时区，默认GMT+8
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._TargetType = params.get("TargetType")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealInstanceDTO(AbstractModel):
    """预付费/后付费接口中，订单和 CKafka 实例映射数据结构

    """

    def __init__(self):
        r"""
        :param _DealName: 订单流水
        :type DealName: str
        :param _InstanceIdList: 订单流水对应购买的 CKafka 实例 id 列表
        :type InstanceIdList: list of str
        """
        self._DealName = None
        self._InstanceIdList = None

    @property
    def DealName(self):
        """订单流水
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIdList(self):
        """订单流水对应购买的 CKafka 实例 id 列表
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRequest(AbstractModel):
    """DeleteAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param _ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param _Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param _PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckafka支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param _Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param _Principal: 用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :type Principal: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._Operation = None
        self._PermissionType = None
        self._Host = None
        self._Principal = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Operation(self):
        """Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :rtype: int
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        """权限类型，(2:DENY，3:ALLOW)，当前ckafka支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :rtype: int
        """
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        """默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        """用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :rtype: str
        """
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Operation = params.get("Operation")
        self._PermissionType = params.get("PermissionType")
        self._Host = params.get("Host")
        self._Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclResponse(AbstractModel):
    """DeleteAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteAclRuleRequest(AbstractModel):
    """DeleteAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id信息
        :type InstanceId: str
        :param _RuleName: acl规则名称
        :type RuleName: str
        """
        self._InstanceId = None
        self._RuleName = None

    @property
    def InstanceId(self):
        """实例id信息
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        """acl规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRuleResponse(AbstractModel):
    """DeleteAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回被删除的规则的ID
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回被删除的规则的ID
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteConnectResourceRequest(AbstractModel):
    """DeleteConnectResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        """连接源的Id
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
        


class DeleteConnectResourceResponse(AbstractModel):
    """DeleteConnectResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 连接源的Id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """连接源的Id
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConnectResourceResourceIdResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteDatahubTaskRequest(AbstractModel):
    """DeleteDatahubTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatahubTaskResponse(AbstractModel):
    """DeleteDatahubTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """操作结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DatahubTaskIdRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteDatahubTopicRequest(AbstractModel):
    """DeleteDatahubTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: Topic名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Topic名称
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
        


class DeleteDatahubTopicResponse(AbstractModel):
    """DeleteDatahubTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果集
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Group: 消费分组
        :type Group: str
        """
        self._InstanceId = None
        self._Group = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        """消费分组
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
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
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteInstancePostRequest(AbstractModel):
    """DeleteInstancePost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstancePostResponse(AbstractModel):
    """DeleteInstancePost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDeleteResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceDeleteResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = InstanceDeleteResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteInstancePreRequest(AbstractModel):
    """DeleteInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstancePreResponse(AbstractModel):
    """DeleteInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteRequest(AbstractModel):
    """DeleteRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _RouteId: 路由id
        :type RouteId: int
        :param _CallerAppid: 调用方appId
        :type CallerAppid: int
        :param _DeleteRouteTime: 设置定时删除路由时间,若DeleteRouteTime < now ,设置时间小于当前接口提交时间则立即执行;DeleteRouteTime > now,设置时间大于当前接口提交时间,则按照设置的时间,定时执行删除;  该参数设置提交后,无法撤销!!!
        :type DeleteRouteTime: str
        """
        self._InstanceId = None
        self._RouteId = None
        self._CallerAppid = None
        self._DeleteRouteTime = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        """路由id
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def CallerAppid(self):
        """调用方appId
        :rtype: int
        """
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def DeleteRouteTime(self):
        """设置定时删除路由时间,若DeleteRouteTime < now ,设置时间小于当前接口提交时间则立即执行;DeleteRouteTime > now,设置时间大于当前接口提交时间,则按照设置的时间,定时执行删除;  该参数设置提交后,无法撤销!!!
        :rtype: str
        """
        return self._DeleteRouteTime

    @DeleteRouteTime.setter
    def DeleteRouteTime(self, DeleteRouteTime):
        self._DeleteRouteTime = DeleteRouteTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RouteId = params.get("RouteId")
        self._CallerAppid = params.get("CallerAppid")
        self._DeleteRouteTime = params.get("DeleteRouteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteResponse(AbstractModel):
    """DeleteRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteRouteTriggerTimeRequest(AbstractModel):
    """DeleteRouteTriggerTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _DelayTime: 修改删除路由的定时时间
        :type DelayTime: str
        """
        self._InstanceId = None
        self._DelayTime = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DelayTime(self):
        """修改删除路由的定时时间
        :rtype: str
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DelayTime = params.get("DelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTriggerTimeResponse(AbstractModel):
    """DeleteRouteTriggerTime返回参数结构体

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


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        :param _IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self._InstanceId = None
        self._TopicName = None
        self._IpWhiteList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
        """ip白名单列表
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """删除主题IP白名单结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka 实例Id
        :type InstanceId: str
        :param _TopicName: ckafka 主题名称
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        """ckafka 实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """ckafka 主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果集
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Name: 用户名称
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """用户名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
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
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param _ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param _Offset: 偏移位置
        :type Offset: int
        :param _Limit: 个数限制
        :type Limit: int
        :param _SearchWord: 关键字匹配
        :type SearchWord: str
        """
        self._InstanceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        """Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Offset(self):
        """偏移位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """个数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """关键字匹配
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeACLResponse(AbstractModel):
    """DescribeACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的ACL结果集对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的ACL结果集对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AclResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAclRuleRequest(AbstractModel):
    """DescribeAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _RuleName: ACL规则名
        :type RuleName: str
        :param _PatternType: ACL规则匹配类型
        :type PatternType: str
        :param _IsSimplified: 是否读取简略的ACL规则
        :type IsSimplified: bool
        """
        self._InstanceId = None
        self._RuleName = None
        self._PatternType = None
        self._IsSimplified = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        """ACL规则名
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def PatternType(self):
        """ACL规则匹配类型
        :rtype: str
        """
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def IsSimplified(self):
        """是否读取简略的ACL规则
        :rtype: bool
        """
        return self._IsSimplified

    @IsSimplified.setter
    def IsSimplified(self, IsSimplified):
        self._IsSimplified = IsSimplified


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._PatternType = params.get("PatternType")
        self._IsSimplified = params.get("IsSimplified")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAclRuleResponse(AbstractModel):
    """DescribeAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的AclRule结果集对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的AclRule结果集对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AclRuleResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AclRuleResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移位置
        :type Offset: int
        :param _Limit: 本次查询用户数目最大数量限制，最大值为50，默认50
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """偏移位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """本次查询用户数目最大数量限制，最大值为50，默认50
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
        


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的符合要求的App Id列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的符合要求的App Id列表
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = AppIdResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCkafkaZoneRequest(AbstractModel):
    """DescribeCkafkaZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CdcId: cdc集群Id
        :type CdcId: str
        """
        self._CdcId = None

    @property
    def CdcId(self):
        """cdc集群Id
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkafkaZoneResponse(AbstractModel):
    """DescribeCkafkaZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询结果复杂对象实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询结果复杂对象实体
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ZoneResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConnectInfoResultDTO(AbstractModel):
    """topic链接信息

    """

    def __init__(self):
        r"""
        :param _IpAddr: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddr: str
        :param _Time: 连结时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _IsUnSupportVersion: 是否支持的版本
        :type IsUnSupportVersion: bool
        """
        self._IpAddr = None
        self._Time = None
        self._IsUnSupportVersion = None

    @property
    def IpAddr(self):
        """ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpAddr

    @IpAddr.setter
    def IpAddr(self, IpAddr):
        self._IpAddr = IpAddr

    @property
    def Time(self):
        """连结时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def IsUnSupportVersion(self):
        """是否支持的版本
        :rtype: bool
        """
        return self._IsUnSupportVersion

    @IsUnSupportVersion.setter
    def IsUnSupportVersion(self, IsUnSupportVersion):
        self._IsUnSupportVersion = IsUnSupportVersion


    def _deserialize(self, params):
        self._IpAddr = params.get("IpAddr")
        self._Time = params.get("Time")
        self._IsUnSupportVersion = params.get("IsUnSupportVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectResource(AbstractModel):
    """查询连接源具体数据的返参

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        :param _ResourceName: 连接源名称
        :type ResourceName: str
        :param _Description: 连接源描述
        :type Description: str
        :param _Type: 连接源类型
        :type Type: str
        :param _Status: 连接源的状态
        :type Status: int
        :param _CreateTime: 连接源的创建时间
        :type CreateTime: str
        :param _ErrorMessage: 连接源的异常信息
        :type ErrorMessage: str
        :param _DatahubTaskCount: 该连接源关联的Datahub任务数
        :type DatahubTaskCount: int
        :param _CurrentStep: 连接源的当前所处步骤
        :type CurrentStep: str
        :param _TaskProgress: 创建进度百分比
        :type TaskProgress: float
        :param _StepList: 步骤列表
        :type StepList: list of str
        :param _DtsConnectParam: Dts配置，Type为DTS时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        :param _MongoDBConnectParam: MongoDB配置，Type为MONGODB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MongoDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        :param _EsConnectParam: Es配置，Type为ES时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        :param _ClickHouseConnectParam: ClickHouse配置，Type为CLICKHOUSE时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ClickHouseConnectParam: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        :param _MySQLConnectParam: MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MySQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        :param _PostgreSQLConnectParam: PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PostgreSQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        :param _MariaDBConnectParam: MariaDB配置，Type为MARIADB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MariaDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        :param _SQLServerConnectParam: SQLServer配置，Type为SQLSERVER时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLServerConnectParam: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        :param _CtsdbConnectParam: Ctsdb配置，Type为CTSDB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type CtsdbConnectParam: :class:`tencentcloud.ckafka.v20190819.models.CtsdbConnectParam`
        :param _DorisConnectParam: Doris 配置，Type 为 DORIS 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DorisConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        :param _KafkaConnectParam: Kafka配置，Type 为 KAFKA 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaConnectParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        :param _MqttConnectParam: MQTT配置，Type 为 MQTT 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MqttConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        self._ResourceId = None
        self._ResourceName = None
        self._Description = None
        self._Type = None
        self._Status = None
        self._CreateTime = None
        self._ErrorMessage = None
        self._DatahubTaskCount = None
        self._CurrentStep = None
        self._TaskProgress = None
        self._StepList = None
        self._DtsConnectParam = None
        self._MongoDBConnectParam = None
        self._EsConnectParam = None
        self._ClickHouseConnectParam = None
        self._MySQLConnectParam = None
        self._PostgreSQLConnectParam = None
        self._MariaDBConnectParam = None
        self._SQLServerConnectParam = None
        self._CtsdbConnectParam = None
        self._DorisConnectParam = None
        self._KafkaConnectParam = None
        self._MqttConnectParam = None

    @property
    def ResourceId(self):
        """连接源的Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """连接源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        """连接源描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        """连接源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """连接源的状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """连接源的创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ErrorMessage(self):
        """连接源的异常信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def DatahubTaskCount(self):
        """该连接源关联的Datahub任务数
        :rtype: int
        """
        return self._DatahubTaskCount

    @DatahubTaskCount.setter
    def DatahubTaskCount(self, DatahubTaskCount):
        self._DatahubTaskCount = DatahubTaskCount

    @property
    def CurrentStep(self):
        """连接源的当前所处步骤
        :rtype: str
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def TaskProgress(self):
        """创建进度百分比
        :rtype: float
        """
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def StepList(self):
        """步骤列表
        :rtype: list of str
        """
        return self._StepList

    @StepList.setter
    def StepList(self, StepList):
        self._StepList = StepList

    @property
    def DtsConnectParam(self):
        """Dts配置，Type为DTS时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        """
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        """MongoDB配置，Type为MONGODB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        """
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        """Es配置，Type为ES时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        """
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        """ClickHouse配置，Type为CLICKHOUSE时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        """
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        """MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        """
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        """PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        """
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        """MariaDB配置，Type为MARIADB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        """
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        """SQLServer配置，Type为SQLSERVER时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        """
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        """Ctsdb配置，Type为CTSDB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CtsdbConnectParam`
        """
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        """Doris 配置，Type 为 DORIS 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        """
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        """Kafka配置，Type 为 KAFKA 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        """
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
        """MQTT配置，Type 为 MQTT 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        return self._MqttConnectParam

    @MqttConnectParam.setter
    def MqttConnectParam(self, MqttConnectParam):
        self._MqttConnectParam = MqttConnectParam


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._DatahubTaskCount = params.get("DatahubTaskCount")
        self._CurrentStep = params.get("CurrentStep")
        self._TaskProgress = params.get("TaskProgress")
        self._StepList = params.get("StepList")
        if params.get("DtsConnectParam") is not None:
            self._DtsConnectParam = DtsConnectParam()
            self._DtsConnectParam._deserialize(params.get("DtsConnectParam"))
        if params.get("MongoDBConnectParam") is not None:
            self._MongoDBConnectParam = MongoDBConnectParam()
            self._MongoDBConnectParam._deserialize(params.get("MongoDBConnectParam"))
        if params.get("EsConnectParam") is not None:
            self._EsConnectParam = EsConnectParam()
            self._EsConnectParam._deserialize(params.get("EsConnectParam"))
        if params.get("ClickHouseConnectParam") is not None:
            self._ClickHouseConnectParam = ClickHouseConnectParam()
            self._ClickHouseConnectParam._deserialize(params.get("ClickHouseConnectParam"))
        if params.get("MySQLConnectParam") is not None:
            self._MySQLConnectParam = MySQLConnectParam()
            self._MySQLConnectParam._deserialize(params.get("MySQLConnectParam"))
        if params.get("PostgreSQLConnectParam") is not None:
            self._PostgreSQLConnectParam = PostgreSQLConnectParam()
            self._PostgreSQLConnectParam._deserialize(params.get("PostgreSQLConnectParam"))
        if params.get("MariaDBConnectParam") is not None:
            self._MariaDBConnectParam = MariaDBConnectParam()
            self._MariaDBConnectParam._deserialize(params.get("MariaDBConnectParam"))
        if params.get("SQLServerConnectParam") is not None:
            self._SQLServerConnectParam = SQLServerConnectParam()
            self._SQLServerConnectParam._deserialize(params.get("SQLServerConnectParam"))
        if params.get("CtsdbConnectParam") is not None:
            self._CtsdbConnectParam = CtsdbConnectParam()
            self._CtsdbConnectParam._deserialize(params.get("CtsdbConnectParam"))
        if params.get("DorisConnectParam") is not None:
            self._DorisConnectParam = DorisConnectParam()
            self._DorisConnectParam._deserialize(params.get("DorisConnectParam"))
        if params.get("KafkaConnectParam") is not None:
            self._KafkaConnectParam = KafkaConnectParam()
            self._KafkaConnectParam._deserialize(params.get("KafkaConnectParam"))
        if params.get("MqttConnectParam") is not None:
            self._MqttConnectParam = MqttConnectParam()
            self._MqttConnectParam._deserialize(params.get("MqttConnectParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectResourceRequest(AbstractModel):
    """DescribeConnectResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        """连接源的Id
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
        


class DescribeConnectResourceResp(AbstractModel):
    """查询连接源具体数据的返参

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        :param _ResourceName: 连接源名称
        :type ResourceName: str
        :param _Description: 连接源描述
        :type Description: str
        :param _Type: 连接源类型
        :type Type: str
        :param _Status: 连接源的状态
        :type Status: int
        :param _CreateTime: 连接源的创建时间
        :type CreateTime: str
        :param _ErrorMessage: 连接源的异常信息
        :type ErrorMessage: str
        :param _CurrentStep: 连接源的当前所处步骤
        :type CurrentStep: str
        :param _StepList: 步骤列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StepList: list of str
        :param _MySQLConnectParam: MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MySQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        :param _PostgreSQLConnectParam: PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PostgreSQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        :param _DtsConnectParam: Dts配置，Type为DTS时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        :param _MongoDBConnectParam: MongoDB配置，Type为MONGODB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MongoDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        :param _EsConnectParam: Es配置，Type为ES时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        :param _ClickHouseConnectParam: ClickHouse配置，Type为CLICKHOUSE时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ClickHouseConnectParam: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        :param _MariaDBConnectParam: MariaDB配置，Type为MARIADB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MariaDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        :param _SQLServerConnectParam: SQLServer配置，Type为SQLSERVER时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SQLServerConnectParam: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        :param _CtsdbConnectParam: Ctsdb配置，Type为CTSDB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type CtsdbConnectParam: :class:`tencentcloud.ckafka.v20190819.models.CtsdbConnectParam`
        :param _DorisConnectParam: Doris 配置，Type 为 DORIS 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type DorisConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        :param _KafkaConnectParam: Kafka配置，Type 为 KAFKA 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type KafkaConnectParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        :param _MqttConnectParam: MQTT配置，Type 为 MQTT 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MqttConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        self._ResourceId = None
        self._ResourceName = None
        self._Description = None
        self._Type = None
        self._Status = None
        self._CreateTime = None
        self._ErrorMessage = None
        self._CurrentStep = None
        self._StepList = None
        self._MySQLConnectParam = None
        self._PostgreSQLConnectParam = None
        self._DtsConnectParam = None
        self._MongoDBConnectParam = None
        self._EsConnectParam = None
        self._ClickHouseConnectParam = None
        self._MariaDBConnectParam = None
        self._SQLServerConnectParam = None
        self._CtsdbConnectParam = None
        self._DorisConnectParam = None
        self._KafkaConnectParam = None
        self._MqttConnectParam = None

    @property
    def ResourceId(self):
        """连接源的Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """连接源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        """连接源描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        """连接源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """连接源的状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """连接源的创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ErrorMessage(self):
        """连接源的异常信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def CurrentStep(self):
        """连接源的当前所处步骤
        :rtype: str
        """
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def StepList(self):
        """步骤列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._StepList

    @StepList.setter
    def StepList(self, StepList):
        self._StepList = StepList

    @property
    def MySQLConnectParam(self):
        """MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MySQLConnectParam`
        """
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        """PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLConnectParam`
        """
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def DtsConnectParam(self):
        """Dts配置，Type为DTS时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DtsConnectParam`
        """
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        """MongoDB配置，Type为MONGODB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MongoDBConnectParam`
        """
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        """Es配置，Type为ES时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EsConnectParam`
        """
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        """ClickHouse配置，Type为CLICKHOUSE时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseConnectParam`
        """
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MariaDBConnectParam(self):
        """MariaDB配置，Type为MARIADB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MariaDBConnectParam`
        """
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        """SQLServer配置，Type为SQLSERVER时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SQLServerConnectParam`
        """
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        """Ctsdb配置，Type为CTSDB时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CtsdbConnectParam`
        """
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        """Doris 配置，Type 为 DORIS 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DorisConnectParam`
        """
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        """Kafka配置，Type 为 KAFKA 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        """
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
        """MQTT配置，Type 为 MQTT 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        return self._MqttConnectParam

    @MqttConnectParam.setter
    def MqttConnectParam(self, MqttConnectParam):
        self._MqttConnectParam = MqttConnectParam


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._CurrentStep = params.get("CurrentStep")
        self._StepList = params.get("StepList")
        if params.get("MySQLConnectParam") is not None:
            self._MySQLConnectParam = MySQLConnectParam()
            self._MySQLConnectParam._deserialize(params.get("MySQLConnectParam"))
        if params.get("PostgreSQLConnectParam") is not None:
            self._PostgreSQLConnectParam = PostgreSQLConnectParam()
            self._PostgreSQLConnectParam._deserialize(params.get("PostgreSQLConnectParam"))
        if params.get("DtsConnectParam") is not None:
            self._DtsConnectParam = DtsConnectParam()
            self._DtsConnectParam._deserialize(params.get("DtsConnectParam"))
        if params.get("MongoDBConnectParam") is not None:
            self._MongoDBConnectParam = MongoDBConnectParam()
            self._MongoDBConnectParam._deserialize(params.get("MongoDBConnectParam"))
        if params.get("EsConnectParam") is not None:
            self._EsConnectParam = EsConnectParam()
            self._EsConnectParam._deserialize(params.get("EsConnectParam"))
        if params.get("ClickHouseConnectParam") is not None:
            self._ClickHouseConnectParam = ClickHouseConnectParam()
            self._ClickHouseConnectParam._deserialize(params.get("ClickHouseConnectParam"))
        if params.get("MariaDBConnectParam") is not None:
            self._MariaDBConnectParam = MariaDBConnectParam()
            self._MariaDBConnectParam._deserialize(params.get("MariaDBConnectParam"))
        if params.get("SQLServerConnectParam") is not None:
            self._SQLServerConnectParam = SQLServerConnectParam()
            self._SQLServerConnectParam._deserialize(params.get("SQLServerConnectParam"))
        if params.get("CtsdbConnectParam") is not None:
            self._CtsdbConnectParam = CtsdbConnectParam()
            self._CtsdbConnectParam._deserialize(params.get("CtsdbConnectParam"))
        if params.get("DorisConnectParam") is not None:
            self._DorisConnectParam = DorisConnectParam()
            self._DorisConnectParam._deserialize(params.get("DorisConnectParam"))
        if params.get("KafkaConnectParam") is not None:
            self._KafkaConnectParam = KafkaConnectParam()
            self._KafkaConnectParam._deserialize(params.get("KafkaConnectParam"))
        if params.get("MqttConnectParam") is not None:
            self._MqttConnectParam = MqttConnectParam()
            self._MqttConnectParam._deserialize(params.get("MqttConnectParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectResourceResponse(AbstractModel):
    """DescribeConnectResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 连接源的Id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourceResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """连接源的Id
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourceResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeConnectResourceResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConnectResourcesRequest(AbstractModel):
    """DescribeConnectResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 连接源类型
        :type Type: str
        :param _SearchWord: 连接源名称的关键字查询
        :type SearchWord: str
        :param _Offset: 分页偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _ResourceRegion: 连接源的关键字查询, 根据地域查询本地域内连接管理列表中的连接(仅支持包含region输入的连接源)
        :type ResourceRegion: str
        """
        self._Type = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._ResourceRegion = None

    @property
    def Type(self):
        """连接源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchWord(self):
        """连接源名称的关键字查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """分页偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceRegion(self):
        """连接源的关键字查询, 根据地域查询本地域内连接管理列表中的连接(仅支持包含region输入的连接源)
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectResourcesResp(AbstractModel):
    """查询连接源列表的返参

    """

    def __init__(self):
        r"""
        :param _TotalCount: 连接源个数
        :type TotalCount: int
        :param _ConnectResourceList: 连接源数据
        :type ConnectResourceList: list of DescribeConnectResource
        """
        self._TotalCount = None
        self._ConnectResourceList = None

    @property
    def TotalCount(self):
        """连接源个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConnectResourceList(self):
        """连接源数据
        :rtype: list of DescribeConnectResource
        """
        return self._ConnectResourceList

    @ConnectResourceList.setter
    def ConnectResourceList(self, ConnectResourceList):
        self._ConnectResourceList = ConnectResourceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConnectResourceList") is not None:
            self._ConnectResourceList = []
            for item in params.get("ConnectResourceList"):
                obj = DescribeConnectResource()
                obj._deserialize(item)
                self._ConnectResourceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectResourcesResponse(AbstractModel):
    """DescribeConnectResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 连接源列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourcesResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """连接源列表
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourcesResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeConnectResourcesResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _GroupName: 可选，用户需要查询的group名称。
        :type GroupName: str
        :param _TopicName: 可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。
        :type TopicName: str
        :param _Limit: 本次返回个数限制，最大支持50
        :type Limit: int
        :param _Offset: 偏移位置
        :type Offset: int
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        """可选，用户需要查询的group名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        """可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Limit(self):
        """本次返回个数限制，最大支持50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupName = params.get("GroupName")
        self._TopicName = params.get("TopicName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的消费分组信息
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的消费分组信息
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConsumerGroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubGroupOffsetsRequest(AbstractModel):
    """DescribeDatahubGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: （过滤条件）按照实例 ID 过滤
        :type Name: str
        :param _Group: Kafka 消费分组
        :type Group: str
        :param _SearchWord: 模糊匹配 topicName
        :type SearchWord: str
        :param _Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param _Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        """
        self._Name = None
        self._Group = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def Name(self):
        """（过滤条件）按照实例 ID 过滤
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        """Kafka 消费分组
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def SearchWord(self):
        """模糊匹配 topicName
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """本次查询的偏移位置，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """本次返回结果的最大个数，默认为50，最大值为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubGroupOffsetsResponse(AbstractModel):
    """DescribeDatahubGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = GroupOffsetResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTaskRequest(AbstractModel):
    """DescribeDatahubTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTaskRes(AbstractModel):
    """查询Datahub任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskType: 任务类型，SOURCE数据接入，SINK数据流出
        :type TaskType: str
        :param _Status: 状态，-1创建失败，0创建中，1运行中，2删除中，3已删除，4删除失败，5暂停中，6已暂停，7暂停失败，8恢复中，9恢复失败
        :type Status: int
        :param _SourceResource: 数据源
        :type SourceResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TargetResource: 数据目标
        :type TargetResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _Connections: Connection列表
        :type Connections: list of Connection
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _TransformParam: 消息处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformParam: :class:`tencentcloud.ckafka.v20190819.models.TransformParam`
        :param _DatahubId: 数据接入ID
        :type DatahubId: str
        :param _SchemaId: 绑定的SchemaId
        :type SchemaId: str
        :param _SchemaName: 绑定的Schema名称
        :type SchemaName: str
        :param _TransformsParam: 数据处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformsParam: :class:`tencentcloud.ckafka.v20190819.models.TransformsParam`
        :param _ErrorMessage: 异常信息
        :type ErrorMessage: str
        :param _Tags: 任务标签列表
        :type Tags: list of Tag
        """
        self._TaskId = None
        self._TaskName = None
        self._TaskType = None
        self._Status = None
        self._SourceResource = None
        self._TargetResource = None
        self._Connections = None
        self._CreateTime = None
        self._TransformParam = None
        self._DatahubId = None
        self._SchemaId = None
        self._SchemaName = None
        self._TransformsParam = None
        self._ErrorMessage = None
        self._Tags = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def TaskType(self):
        """任务类型，SOURCE数据接入，SINK数据流出
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        """状态，-1创建失败，0创建中，1运行中，2删除中，3已删除，4删除失败，5暂停中，6已暂停，7暂停失败，8恢复中，9恢复失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceResource(self):
        """数据源
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        """数据目标
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        """
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def Connections(self):
        """Connection列表
        :rtype: list of Connection
        """
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TransformParam(self):
        """消息处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TransformParam`
        """
        return self._TransformParam

    @TransformParam.setter
    def TransformParam(self, TransformParam):
        self._TransformParam = TransformParam

    @property
    def DatahubId(self):
        """数据接入ID
        :rtype: str
        """
        return self._DatahubId

    @DatahubId.setter
    def DatahubId(self, DatahubId):
        self._DatahubId = DatahubId

    @property
    def SchemaId(self):
        """绑定的SchemaId
        :rtype: str
        """
        return self._SchemaId

    @SchemaId.setter
    def SchemaId(self, SchemaId):
        self._SchemaId = SchemaId

    @property
    def SchemaName(self):
        """绑定的Schema名称
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TransformsParam(self):
        """数据处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TransformsParam`
        """
        return self._TransformsParam

    @TransformsParam.setter
    def TransformsParam(self, TransformsParam):
        self._TransformsParam = TransformsParam

    @property
    def ErrorMessage(self):
        """异常信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Tags(self):
        """任务标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        if params.get("SourceResource") is not None:
            self._SourceResource = DatahubResource()
            self._SourceResource._deserialize(params.get("SourceResource"))
        if params.get("TargetResource") is not None:
            self._TargetResource = DatahubResource()
            self._TargetResource._deserialize(params.get("TargetResource"))
        if params.get("Connections") is not None:
            self._Connections = []
            for item in params.get("Connections"):
                obj = Connection()
                obj._deserialize(item)
                self._Connections.append(obj)
        self._CreateTime = params.get("CreateTime")
        if params.get("TransformParam") is not None:
            self._TransformParam = TransformParam()
            self._TransformParam._deserialize(params.get("TransformParam"))
        self._DatahubId = params.get("DatahubId")
        self._SchemaId = params.get("SchemaId")
        self._SchemaName = params.get("SchemaName")
        if params.get("TransformsParam") is not None:
            self._TransformsParam = TransformsParam()
            self._TransformsParam._deserialize(params.get("TransformsParam"))
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTaskResponse(AbstractModel):
    """DescribeDatahubTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTaskRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTaskRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTaskRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTasksRequest(AbstractModel):
    """DescribeDatahubTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Offset: 分页偏移量，默认为0
        :type Offset: int
        :param _SearchWord: 过滤条件，按照 TaskName 过滤，支持模糊查询
        :type SearchWord: str
        :param _TargetType: 转储的目标类型
        :type TargetType: str
        :param _TaskType: 任务类型，SOURCE数据接入，SINK数据流出
        :type TaskType: str
        :param _SourceType: 转储的源类型
        :type SourceType: str
        :param _Resource: 转储的资源
        :type Resource: str
        """
        self._Limit = None
        self._Offset = None
        self._SearchWord = None
        self._TargetType = None
        self._TaskType = None
        self._SourceType = None
        self._Resource = None

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SearchWord(self):
        """过滤条件，按照 TaskName 过滤，支持模糊查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def TargetType(self):
        """转储的目标类型
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TaskType(self):
        """任务类型，SOURCE数据接入，SINK数据流出
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def SourceType(self):
        """转储的源类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Resource(self):
        """转储的资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SearchWord = params.get("SearchWord")
        self._TargetType = params.get("TargetType")
        self._TaskType = params.get("TaskType")
        self._SourceType = params.get("SourceType")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTasksRes(AbstractModel):
    """查询Datahub任务列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _TaskList: Datahub任务信息列表
        :type TaskList: list of DatahubTaskInfo
        """
        self._TotalCount = None
        self._TaskList = None

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
    def TaskList(self):
        """Datahub任务信息列表
        :rtype: list of DatahubTaskInfo
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = DatahubTaskInfo()
                obj._deserialize(item)
                self._TaskList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTasksResponse(AbstractModel):
    """DescribeDatahubTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回任务查询结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTasksRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回任务查询结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTasksRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTasksRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicRequest(AbstractModel):
    """DescribeDatahubTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 弹性topic名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """弹性topic名称
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
        


class DescribeDatahubTopicResp(AbstractModel):
    """Datahub Topic详情

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _TopicId: Topic Id
        :type TopicId: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _RetentionMs: 过期时间
        :type RetentionMs: int
        :param _Note: 备注
        :type Note: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        :param _Status: 状态，1使用中，2删除中
        :type Status: int
        :param _Address: 服务路由地址
        :type Address: str
        """
        self._Name = None
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._RetentionMs = None
        self._Note = None
        self._UserName = None
        self._Password = None
        self._Status = None
        self._Address = None

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
    def TopicName(self):
        """Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """Topic Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        """过期时间
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

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
    def Password(self):
        """密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Status(self):
        """状态，1使用中，2删除中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
        """服务路由地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Status = params.get("Status")
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicResponse(AbstractModel):
    """DescribeDatahubTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTopicResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDatahubTopicsRequest(AbstractModel):
    """DescribeDatahubTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchWord: 搜索词
        :type SearchWord: str
        :param _Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param _Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        :param _QueryFromConnectResource: 是否从连接查询topic列表
        :type QueryFromConnectResource: bool
        :param _ConnectResourceId: 连接的ID
        :type ConnectResourceId: str
        :param _TopicRegularExpression: topic资源表达式
        :type TopicRegularExpression: str
        """
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._QueryFromConnectResource = None
        self._ConnectResourceId = None
        self._TopicRegularExpression = None

    @property
    def SearchWord(self):
        """搜索词
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """本次查询的偏移位置，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """本次返回结果的最大个数，默认为50，最大值为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueryFromConnectResource(self):
        """是否从连接查询topic列表
        :rtype: bool
        """
        return self._QueryFromConnectResource

    @QueryFromConnectResource.setter
    def QueryFromConnectResource(self, QueryFromConnectResource):
        self._QueryFromConnectResource = QueryFromConnectResource

    @property
    def ConnectResourceId(self):
        """连接的ID
        :rtype: str
        """
        return self._ConnectResourceId

    @ConnectResourceId.setter
    def ConnectResourceId(self, ConnectResourceId):
        self._ConnectResourceId = ConnectResourceId

    @property
    def TopicRegularExpression(self):
        """topic资源表达式
        :rtype: str
        """
        return self._TopicRegularExpression

    @TopicRegularExpression.setter
    def TopicRegularExpression(self, TopicRegularExpression):
        self._TopicRegularExpression = TopicRegularExpression


    def _deserialize(self, params):
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueryFromConnectResource = params.get("QueryFromConnectResource")
        self._ConnectResourceId = params.get("ConnectResourceId")
        self._TopicRegularExpression = params.get("TopicRegularExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicsResp(AbstractModel):
    """Datahub主题列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _TopicList: Topic列表
        :type TopicList: list of DatahubTopicDTO
        """
        self._TotalCount = None
        self._TopicList = None

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
    def TopicList(self):
        """Topic列表
        :rtype: list of DatahubTopicDTO
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = DatahubTopicDTO()
                obj._deserialize(item)
                self._TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatahubTopicsResponse(AbstractModel):
    """DescribeDatahubTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 主题列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """主题列表
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDatahubTopicsResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """DescribeGroup返回实体

    """

    def __init__(self):
        r"""
        :param _Group: 消费分组名称
        :type Group: str
        :param _Protocol: 该 group 使用的协议。
        :type Protocol: str
        """
        self._Group = None
        self._Protocol = None

    @property
    def Group(self):
        """消费分组名称
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Protocol(self):
        """该 group 使用的协议。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Group = params.get("Group")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _GroupList: Kafka 消费分组列表
        :type GroupList: list of str
        """
        self._InstanceId = None
        self._GroupList = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupList(self):
        """Kafka 消费分组列表
        :rtype: list of str
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupList = params.get("GroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果
        :type Result: list of GroupInfoResponse
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果
        :rtype: list of GroupInfoResponse
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Group: Kafka 消费分组
        :type Group: str
        :param _Topics: group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息
        :type Topics: list of str
        :param _SearchWord: 模糊匹配 topicName
        :type SearchWord: str
        :param _Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param _Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        """
        self._InstanceId = None
        self._Group = None
        self._Topics = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        """Kafka 消费分组
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Topics(self):
        """group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def SearchWord(self):
        """模糊匹配 topicName
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """本次查询的偏移位置，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """本次返回结果的最大个数，默认为50，最大值为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        self._Topics = params.get("Topics")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = GroupOffsetResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _SearchWord: 搜索关键字
        :type SearchWord: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 最大返回数量
        :type Limit: int
        :param _Filters: 仅支持 GroupState 筛选,   支持的筛选状态有 Empty/Stable  注意：该参数只能在2.8/3.2 版本生效
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """搜索关键字
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

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
        """最大返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """仅支持 GroupState 筛选,   支持的筛选状态有 Empty/Stable  注意：该参数只能在2.8/3.2 版本生效
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = GroupResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 实例属性返回结果对象。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """实例属性返回结果对象。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = InstanceAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param _SearchWord: （过滤条件）按照实例名,实例Id,可用区,私有网络id,子网id 过滤，支持模糊查询
        :type SearchWord: str
        :param _Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param _Offset: 偏移量，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认10，最大值20。
        :type Limit: int
        :param _TagKey: 匹配标签key值。
        :type TagKey: str
        :param _Filters: 过滤器。filter.Name 支持('Ip', 'VpcId', 'SubNetId', 'InstanceType','InstanceId') ,filter.Values最多传递10个值.
        :type Filters: list of Filter
        :param _InstanceIds: 已经废弃， 使用InstanceIdList
        :type InstanceIds: str
        :param _InstanceIdList: 按照实例ID过滤
        :type InstanceIdList: list of str
        :param _TagList: 根据标签列表过滤实例（取交集）
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TagKey = None
        self._Filters = None
        self._InstanceIds = None
        self._InstanceIdList = None
        self._TagList = None

    @property
    def InstanceId(self):
        """（过滤条件）按照实例ID过滤
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """（过滤条件）按照实例名,实例Id,可用区,私有网络id,子网id 过滤，支持模糊查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        """（过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """偏移量，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认10，最大值20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        """匹配标签key值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Filters(self):
        """过滤器。filter.Name 支持('Ip', 'VpcId', 'SubNetId', 'InstanceType','InstanceId') ,filter.Values最多传递10个值.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def InstanceIds(self):
        """已经废弃， 使用InstanceIdList
        :rtype: str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceIdList(self):
        """按照实例ID过滤
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def TagList(self):
        """根据标签列表过滤实例（取交集）
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceIdList = params.get("InstanceIdList")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的实例详情结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的实例详情结果对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = InstanceDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: （查询条件）按照ckafka集群实例Id过滤
        :type InstanceId: str
        :param _SearchWord: 搜索词   ex:（查询条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param _Status: （查询条件）实例的状态  0：创建中，1：运行中，2：删除中，5: 隔离中,  7:升级中 不填默认返回全部
        :type Status: list of int
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认10，最大值100
        :type Limit: int
        :param _TagKey: 已废弃。匹配标签key值。
        :type TagKey: str
        :param _VpcId: （查询条件）私有网络Id
        :type VpcId: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TagKey = None
        self._VpcId = None

    @property
    def InstanceId(self):
        """（查询条件）按照ckafka集群实例Id过滤
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """搜索词   ex:（查询条件）按照实例名称过滤，支持模糊查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        """（查询条件）实例的状态  0：创建中，1：运行中，2：删除中，5: 隔离中,  7:升级中 不填默认返回全部
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """偏移量，不填默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认10，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        """已废弃。匹配标签key值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def VpcId(self):
        """（查询条件）私有网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TagKey = params.get("TagKey")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = InstanceResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePrometheusRequest(AbstractModel):
    """DescribePrometheus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusResponse(AbstractModel):
    """DescribePrometheus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Prometheus监控映射列表
        :type Result: list of PrometheusDTO
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Prometheus监控映射列表
        :rtype: list of PrometheusDTO
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = PrometheusDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    """DescribeRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回最大结果数
        :type Limit: int
        :param _Business: 业务字段，可忽略
        :type Business: str
        :param _CdcId: cdc专有集群业务字段，可忽略
        :type CdcId: str
        """
        self._Offset = None
        self._Limit = None
        self._Business = None
        self._CdcId = None

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
        """返回最大结果数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Business(self):
        """业务字段，可忽略
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CdcId(self):
        """cdc专有集群业务字段，可忽略
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Business = params.get("Business")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回地域枚举结果列表
        :type Result: list of Region
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回地域枚举结果列表
        :rtype: list of Region
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _RouteId: 路由Id
        :type RouteId: int
        """
        self._InstanceId = None
        self._RouteId = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        """路由Id
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的路由信息结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的路由信息结果集
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = RouteResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程Id
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TaskStatusResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TaskStatusResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果对象
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicAttributesResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _SearchWord: （过滤条件）按照topicName过滤，支持模糊查询
        :type SearchWord: str
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认 10，最大值20，取值要大于0
        :type Limit: int
        :param _AclRuleName: Acl预设策略名称
        :type AclRuleName: str
        :param _OrderBy: 根据特定的属性排序(目前支持PartitionNum/CreateTime)
        :type OrderBy: str
        :param _OrderType: 0-顺序、1-倒序
        :type OrderType: int
        :param _Filters: 目前支持 ReplicaNum （副本数）筛选
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._AclRuleName = None
        self._OrderBy = None
        self._OrderType = None
        self._Filters = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """（过滤条件）按照topicName过滤，支持模糊查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """偏移量，不填默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认 10，最大值20，取值要大于0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        """Acl预设策略名称
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def OrderBy(self):
        """根据特定的属性排序(目前支持PartitionNum/CreateTime)
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        """0-顺序、1-倒序
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Filters(self):
        """目前支持 ReplicaNum （副本数）筛选
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AclRuleName = params.get("AclRuleName")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
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
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的主题详情实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的主题详情实体
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicDetailResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicFlowRankingRequest(AbstractModel):
    """DescribeTopicFlowRanking请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _RankingType: 排行类别，PRO：Topic生产流量；CON：Topic消费流量
        :type RankingType: str
        :param _BeginDate: 排行起始日期
        :type BeginDate: str
        :param _EndDate: 排行结束日期
        :type EndDate: str
        :param _BrokerIp: Broker IP 地址
        :type BrokerIp: str
        """
        self._InstanceId = None
        self._RankingType = None
        self._BeginDate = None
        self._EndDate = None
        self._BrokerIp = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RankingType(self):
        """排行类别，PRO：Topic生产流量；CON：Topic消费流量
        :rtype: str
        """
        return self._RankingType

    @RankingType.setter
    def RankingType(self, RankingType):
        self._RankingType = RankingType

    @property
    def BeginDate(self):
        """排行起始日期
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """排行结束日期
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def BrokerIp(self):
        """Broker IP 地址
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RankingType = params.get("RankingType")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._BrokerIp = params.get("BrokerIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicFlowRankingResponse(AbstractModel):
    """DescribeTopicFlowRanking返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 流量排行返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicFlowRankingResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """流量排行返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicFlowRankingResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicFlowRankingResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicProduceConnectionRequest(AbstractModel):
    """DescribeTopicProduceConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicProduceConnectionResponse(AbstractModel):
    """DescribeTopicProduceConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 链接信息返回结果集
        :type Result: list of DescribeConnectInfoResultDTO
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """链接信息返回结果集
        :rtype: list of DescribeConnectInfoResultDTO
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = DescribeConnectInfoResultDTO()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _SearchWord: 过滤条件，按照 topicName 过滤，支持模糊查询
        :type SearchWord: str
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为20，最大值为50
        :type Limit: int
        :param _AclRuleName: Acl预设策略名称
        :type AclRuleName: str
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None
        self._AclRuleName = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """过滤条件，按照 topicName 过滤，支持模糊查询
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        """偏移量，不填默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为20，最大值为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
        """Acl预设策略名称
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AclRuleName = params.get("AclRuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回的结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSubscribeGroupRequest(AbstractModel):
    """DescribeTopicSubscribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        :param _Offset: 分页时的起始位置
        :type Offset: int
        :param _Limit: 分页时的个数
        :type Limit: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """分页时的起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页时的个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSubscribeGroupResponse(AbstractModel):
    """DescribeTopicSubscribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicSubscribeGroup`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicSubscribeGroup()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTopicSyncReplicaRequest(AbstractModel):
    """DescribeTopicSyncReplica请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认10，最大值20。
        :type Limit: int
        :param _OutOfSyncReplicaOnly: 仅筛选未同步副本
        :type OutOfSyncReplicaOnly: bool
        """
        self._InstanceId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._OutOfSyncReplicaOnly = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """偏移量，不填默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认10，最大值20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OutOfSyncReplicaOnly(self):
        """仅筛选未同步副本
        :rtype: bool
        """
        return self._OutOfSyncReplicaOnly

    @OutOfSyncReplicaOnly.setter
    def OutOfSyncReplicaOnly(self, OutOfSyncReplicaOnly):
        self._OutOfSyncReplicaOnly = OutOfSyncReplicaOnly


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OutOfSyncReplicaOnly = params.get("OutOfSyncReplicaOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicSyncReplicaResponse(AbstractModel):
    """DescribeTopicSyncReplica返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回topic 副本详情
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回topic 副本详情
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicInSyncReplicaResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = TopicInSyncReplicaResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _SearchWord: 按照名称过滤
        :type SearchWord: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        """按照名称过滤
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

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
        """返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchWord = params.get("SearchWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = UserResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DorisConnectParam(AbstractModel):
    """Doris 连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: Doris jdbc 负载均衡连接 port，通常映射到 fe 的 9030 端口
        :type Port: int
        :param _UserName: Doris 连接源的用户名
        :type UserName: str
        :param _Password: Doris 连接源的密码
        :type Password: str
        :param _Resource: Doris 连接源的实例资源
        :type Resource: str
        :param _ServiceVip: Doris 连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: Doris 连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        :param _SelfBuilt: Doris 连接源是否为自建集群
        :type SelfBuilt: bool
        :param _BePort: Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
        :type BePort: int
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None
        self._SelfBuilt = None
        self._BePort = None

    @property
    def Port(self):
        """Doris jdbc 负载均衡连接 port，通常映射到 fe 的 9030 端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """Doris 连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Doris 连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """Doris 连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        """Doris 连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Doris 连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        """Doris 连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def BePort(self):
        """Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
        :rtype: int
        """
        return self._BePort

    @BePort.setter
    def BePort(self, BePort):
        self._BePort = BePort


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        self._SelfBuilt = params.get("SelfBuilt")
        self._BePort = params.get("BePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DorisModifyConnectParam(AbstractModel):
    """Doris 连接源修改参数

    """

    def __init__(self):
        r"""
        :param _Resource: Doris 连接源的实例资源
        :type Resource: str
        :param _Port: Doris jdbc 负载均衡连接 port，通常映射到 fe 的 9030 端口
        :type Port: int
        :param _ServiceVip: Doris 连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: Doris 连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _UserName: Doris 连接源的用户名
        :type UserName: str
        :param _Password: Doris 连接源的密码
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        :param _SelfBuilt: Doris 连接源是否为自建集群
        :type SelfBuilt: bool
        :param _BePort: Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
        :type BePort: int
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._IsUpdate = None
        self._SelfBuilt = None
        self._BePort = None

    @property
    def Resource(self):
        """Doris 连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """Doris jdbc 负载均衡连接 port，通常映射到 fe 的 9030 端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """Doris 连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Doris 连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """Doris 连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Doris 连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        """Doris 连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def BePort(self):
        """Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
        :rtype: int
        """
        return self._BePort

    @BePort.setter
    def BePort(self, BePort):
        self._BePort = BePort


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._IsUpdate = params.get("IsUpdate")
        self._SelfBuilt = params.get("SelfBuilt")
        self._BePort = params.get("BePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropCls(AbstractModel):
    """dip失败消息写入cls的配置

    """

    def __init__(self):
        r"""
        :param _DropInvalidMessageToCls: 是否投递到cls
        :type DropInvalidMessageToCls: bool
        :param _DropClsRegion: 投递cls的地域
        :type DropClsRegion: str
        :param _DropClsOwneruin: 投递cls的账号
        :type DropClsOwneruin: str
        :param _DropClsTopicId: 投递cls的主题
        :type DropClsTopicId: str
        :param _DropClsLogSet: 投递cls的日志集id
        :type DropClsLogSet: str
        """
        self._DropInvalidMessageToCls = None
        self._DropClsRegion = None
        self._DropClsOwneruin = None
        self._DropClsTopicId = None
        self._DropClsLogSet = None

    @property
    def DropInvalidMessageToCls(self):
        """是否投递到cls
        :rtype: bool
        """
        return self._DropInvalidMessageToCls

    @DropInvalidMessageToCls.setter
    def DropInvalidMessageToCls(self, DropInvalidMessageToCls):
        self._DropInvalidMessageToCls = DropInvalidMessageToCls

    @property
    def DropClsRegion(self):
        """投递cls的地域
        :rtype: str
        """
        return self._DropClsRegion

    @DropClsRegion.setter
    def DropClsRegion(self, DropClsRegion):
        self._DropClsRegion = DropClsRegion

    @property
    def DropClsOwneruin(self):
        """投递cls的账号
        :rtype: str
        """
        return self._DropClsOwneruin

    @DropClsOwneruin.setter
    def DropClsOwneruin(self, DropClsOwneruin):
        self._DropClsOwneruin = DropClsOwneruin

    @property
    def DropClsTopicId(self):
        """投递cls的主题
        :rtype: str
        """
        return self._DropClsTopicId

    @DropClsTopicId.setter
    def DropClsTopicId(self, DropClsTopicId):
        self._DropClsTopicId = DropClsTopicId

    @property
    def DropClsLogSet(self):
        """投递cls的日志集id
        :rtype: str
        """
        return self._DropClsLogSet

    @DropClsLogSet.setter
    def DropClsLogSet(self, DropClsLogSet):
        self._DropClsLogSet = DropClsLogSet


    def _deserialize(self, params):
        self._DropInvalidMessageToCls = params.get("DropInvalidMessageToCls")
        self._DropClsRegion = params.get("DropClsRegion")
        self._DropClsOwneruin = params.get("DropClsOwneruin")
        self._DropClsTopicId = params.get("DropClsTopicId")
        self._DropClsLogSet = params.get("DropClsLogSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DtsConnectParam(AbstractModel):
    """Dts连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: Dts的连接port
        :type Port: int
        :param _GroupId: Dts消费分组的Id
        :type GroupId: str
        :param _UserName: Dts消费分组的账号
        :type UserName: str
        :param _Password: Dts消费分组的密码
        :type Password: str
        :param _Resource: Dts实例Id
        :type Resource: str
        :param _Topic: Dts订阅的topic
        :type Topic: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Port = None
        self._GroupId = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._Topic = None
        self._IsUpdate = None

    @property
    def Port(self):
        """Dts的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupId(self):
        """Dts消费分组的Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserName(self):
        """Dts消费分组的账号
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Dts消费分组的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """Dts实例Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Topic(self):
        """Dts订阅的topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._GroupId = params.get("GroupId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._Topic = params.get("Topic")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DtsModifyConnectParam(AbstractModel):
    """Dts修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: Dts实例Id【不支持修改】
        :type Resource: str
        :param _Port: Dts的连接port【不支持修改】
        :type Port: int
        :param _GroupId: Dts消费分组的Id
        :type GroupId: str
        :param _UserName: Dts消费分组的账号
        :type UserName: str
        :param _Password: Dts消费分组的密码
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务，默认为true
        :type IsUpdate: bool
        :param _Topic: Dts订阅的topic【不支持修改】
        :type Topic: str
        """
        self._Resource = None
        self._Port = None
        self._GroupId = None
        self._UserName = None
        self._Password = None
        self._IsUpdate = None
        self._Topic = None

    @property
    def Resource(self):
        """Dts实例Id【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """Dts的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupId(self):
        """Dts消费分组的Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserName(self):
        """Dts消费分组的账号
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Dts消费分组的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务，默认为true
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def Topic(self):
        """Dts订阅的topic【不支持修改】
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._GroupId = params.get("GroupId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._IsUpdate = params.get("IsUpdate")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DtsParam(AbstractModel):
    """Dts类型入参

    """

    def __init__(self):
        r"""
        :param _Resource: Dts实例Id
        :type Resource: str
        :param _Ip: Dts的连接ip
        :type Ip: str
        :param _Port: Dts的连接port
        :type Port: int
        :param _Topic: Dts订阅的topic
        :type Topic: str
        :param _GroupId: Dts消费分组的Id
        :type GroupId: str
        :param _GroupUser: Dts消费分组的账号
        :type GroupUser: str
        :param _GroupPassword: Dts消费分组的密码
        :type GroupPassword: str
        :param _TranSql: false同步原始数据，true同步解析后的json格式数据,默认true
        :type TranSql: bool
        """
        self._Resource = None
        self._Ip = None
        self._Port = None
        self._Topic = None
        self._GroupId = None
        self._GroupUser = None
        self._GroupPassword = None
        self._TranSql = None

    @property
    def Resource(self):
        """Dts实例Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        """Dts的连接ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Dts的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Topic(self):
        """Dts订阅的topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def GroupId(self):
        """Dts消费分组的Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupUser(self):
        """Dts消费分组的账号
        :rtype: str
        """
        return self._GroupUser

    @GroupUser.setter
    def GroupUser(self, GroupUser):
        self._GroupUser = GroupUser

    @property
    def GroupPassword(self):
        """Dts消费分组的密码
        :rtype: str
        """
        return self._GroupPassword

    @GroupPassword.setter
    def GroupPassword(self, GroupPassword):
        self._GroupPassword = GroupPassword

    @property
    def TranSql(self):
        """false同步原始数据，true同步解析后的json格式数据,默认true
        :rtype: bool
        """
        return self._TranSql

    @TranSql.setter
    def TranSql(self, TranSql):
        self._TranSql = TranSql


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Topic = params.get("Topic")
        self._GroupId = params.get("GroupId")
        self._GroupUser = params.get("GroupUser")
        self._GroupPassword = params.get("GroupPassword")
        self._TranSql = params.get("TranSql")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicDiskConfig(AbstractModel):
    """动态硬盘扩容配置

    """

    def __init__(self):
        r"""
        :param _Enable: 动态硬盘扩容配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _StepForwardPercentage: 每次磁盘动态扩容大小百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type StepForwardPercentage: int
        :param _DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发硬盘自动扩容事件
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskQuotaPercentage: int
        :param _MaxDiskSpace: 最大扩容硬盘大小，以 GB 为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSpace: int
        """
        self._Enable = None
        self._StepForwardPercentage = None
        self._DiskQuotaPercentage = None
        self._MaxDiskSpace = None

    @property
    def Enable(self):
        """动态硬盘扩容配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def StepForwardPercentage(self):
        """每次磁盘动态扩容大小百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def DiskQuotaPercentage(self):
        """磁盘配额百分比触发条件，即消息达到此值触发硬盘自动扩容事件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def MaxDiskSpace(self):
        """最大扩容硬盘大小，以 GB 为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxDiskSpace

    @MaxDiskSpace.setter
    def MaxDiskSpace(self, MaxDiskSpace):
        self._MaxDiskSpace = MaxDiskSpace


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._StepForwardPercentage = params.get("StepForwardPercentage")
        self._DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self._MaxDiskSpace = params.get("MaxDiskSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicRetentionTime(AbstractModel):
    """动态消息保留时间配置

    """

    def __init__(self):
        r"""
        :param _Enable: 动态消息保留时间配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param _DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发消息保留时间变更事件
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskQuotaPercentage: int
        :param _StepForwardPercentage: 每次向前调整消息保留时间百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type StepForwardPercentage: int
        :param _BottomRetention: 保底时长，单位分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type BottomRetention: int
        """
        self._Enable = None
        self._DiskQuotaPercentage = None
        self._StepForwardPercentage = None
        self._BottomRetention = None

    @property
    def Enable(self):
        """动态消息保留时间配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DiskQuotaPercentage(self):
        """磁盘配额百分比触发条件，即消息达到此值触发消息保留时间变更事件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def StepForwardPercentage(self):
        """每次向前调整消息保留时间百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def BottomRetention(self):
        """保底时长，单位分钟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BottomRetention

    @BottomRetention.setter
    def BottomRetention(self, BottomRetention):
        self._BottomRetention = BottomRetention


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self._StepForwardPercentage = params.get("StepForwardPercentage")
        self._BottomRetention = params.get("BottomRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsConnectParam(AbstractModel):
    """Es连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: Es的连接port
        :type Port: int
        :param _UserName: Es连接源的用户名
        :type UserName: str
        :param _Password: Es连接源的密码
        :type Password: str
        :param _Resource: Es连接源的实例资源
        :type Resource: str
        :param _SelfBuilt: Es连接源是否为自建集群
        :type SelfBuilt: bool
        :param _ServiceVip: Es连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: Es连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._SelfBuilt = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None

    @property
    def Port(self):
        """Es的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """Es连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Es连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """Es连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        """Es连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        """Es连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Es连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._SelfBuilt = params.get("SelfBuilt")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsModifyConnectParam(AbstractModel):
    """Es修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: Es连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: Es的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: Es连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: Es连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: Es连接源的用户名
        :type UserName: str
        :param _Password: Es连接源的密码
        :type Password: str
        :param _SelfBuilt: Es连接源是否为自建集群【不支持修改】
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._SelfBuilt = None
        self._IsUpdate = None

    @property
    def Resource(self):
        """Es连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """Es的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """Es连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """Es连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """Es连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Es连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        """Es连接源是否为自建集群【不支持修改】
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._SelfBuilt = params.get("SelfBuilt")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsParam(AbstractModel):
    """Es类型入参

    """

    def __init__(self):
        r"""
        :param _Resource: Es实例资源Id
        :type Resource: str
        :param _Port: Es的连接port
        :type Port: int
        :param _UserName: Es用户名
        :type UserName: str
        :param _Password: Es密码
        :type Password: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _ServiceVip: 实例vip
        :type ServiceVip: str
        :param _UniqVpcId: 实例的vpcId
        :type UniqVpcId: str
        :param _DropInvalidMessage: Es是否抛弃解析失败的消息
        :type DropInvalidMessage: bool
        :param _Index: Es自定义index名称
        :type Index: str
        :param _DateFormat: Es自定义日期后缀
        :type DateFormat: str
        :param _ContentKey: 非json格式数据的自定义key
        :type ContentKey: str
        :param _DropInvalidJsonMessage: Es是否抛弃非json格式的消息
        :type DropInvalidJsonMessage: bool
        :param _DocumentIdField: 转储到Es中的文档ID取值字段名
        :type DocumentIdField: str
        :param _IndexType: Es自定义index名称的类型，STRING，JSONPATH，默认为STRING
        :type IndexType: str
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _DatabasePrimaryKey: 转储到ES的消息为Database的binlog时，如果需要同步数据库操作，即增删改的操作到ES时填写数据库表主键
        :type DatabasePrimaryKey: str
        :param _DropDlq: 死信队列
        :type DropDlq: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        :param _RecordMappingList: 使用数据订阅格式导入 es 时，消息与 es 索引字段映射关系。不填默认为默认字段匹配
        :type RecordMappingList: list of EsRecordMapping
        :param _DateField: 消息要映射为 es 索引中 @timestamp 的字段，如果当前配置为空，则使用消息的时间戳进行映射
        :type DateField: str
        :param _RecordMappingMode: 用来区分当前索引映射，属于新建索引还是存量索引。"EXIST_MAPPING"：从存量索引中选择；"NEW_MAPPING"：新建索引
        :type RecordMappingMode: str
        """
        self._Resource = None
        self._Port = None
        self._UserName = None
        self._Password = None
        self._SelfBuilt = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._DropInvalidMessage = None
        self._Index = None
        self._DateFormat = None
        self._ContentKey = None
        self._DropInvalidJsonMessage = None
        self._DocumentIdField = None
        self._IndexType = None
        self._DropCls = None
        self._DatabasePrimaryKey = None
        self._DropDlq = None
        self._RecordMappingList = None
        self._DateField = None
        self._RecordMappingMode = None

    @property
    def Resource(self):
        """Es实例资源Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """Es的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """Es用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """Es密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        """实例vip
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """实例的vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def DropInvalidMessage(self):
        """Es是否抛弃解析失败的消息
        :rtype: bool
        """
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def Index(self):
        """Es自定义index名称
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def DateFormat(self):
        """Es自定义日期后缀
        :rtype: str
        """
        return self._DateFormat

    @DateFormat.setter
    def DateFormat(self, DateFormat):
        self._DateFormat = DateFormat

    @property
    def ContentKey(self):
        """非json格式数据的自定义key
        :rtype: str
        """
        return self._ContentKey

    @ContentKey.setter
    def ContentKey(self, ContentKey):
        self._ContentKey = ContentKey

    @property
    def DropInvalidJsonMessage(self):
        """Es是否抛弃非json格式的消息
        :rtype: bool
        """
        return self._DropInvalidJsonMessage

    @DropInvalidJsonMessage.setter
    def DropInvalidJsonMessage(self, DropInvalidJsonMessage):
        self._DropInvalidJsonMessage = DropInvalidJsonMessage

    @property
    def DocumentIdField(self):
        """转储到Es中的文档ID取值字段名
        :rtype: str
        """
        return self._DocumentIdField

    @DocumentIdField.setter
    def DocumentIdField(self, DocumentIdField):
        self._DocumentIdField = DocumentIdField

    @property
    def IndexType(self):
        """Es自定义index名称的类型，STRING，JSONPATH，默认为STRING
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def DropCls(self):
        """当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        """
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def DatabasePrimaryKey(self):
        """转储到ES的消息为Database的binlog时，如果需要同步数据库操作，即增删改的操作到ES时填写数据库表主键
        :rtype: str
        """
        return self._DatabasePrimaryKey

    @DatabasePrimaryKey.setter
    def DatabasePrimaryKey(self, DatabasePrimaryKey):
        self._DatabasePrimaryKey = DatabasePrimaryKey

    @property
    def DropDlq(self):
        """死信队列
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        """
        return self._DropDlq

    @DropDlq.setter
    def DropDlq(self, DropDlq):
        self._DropDlq = DropDlq

    @property
    def RecordMappingList(self):
        """使用数据订阅格式导入 es 时，消息与 es 索引字段映射关系。不填默认为默认字段匹配
        :rtype: list of EsRecordMapping
        """
        return self._RecordMappingList

    @RecordMappingList.setter
    def RecordMappingList(self, RecordMappingList):
        self._RecordMappingList = RecordMappingList

    @property
    def DateField(self):
        """消息要映射为 es 索引中 @timestamp 的字段，如果当前配置为空，则使用消息的时间戳进行映射
        :rtype: str
        """
        return self._DateField

    @DateField.setter
    def DateField(self, DateField):
        self._DateField = DateField

    @property
    def RecordMappingMode(self):
        """用来区分当前索引映射，属于新建索引还是存量索引。"EXIST_MAPPING"：从存量索引中选择；"NEW_MAPPING"：新建索引
        :rtype: str
        """
        return self._RecordMappingMode

    @RecordMappingMode.setter
    def RecordMappingMode(self, RecordMappingMode):
        self._RecordMappingMode = RecordMappingMode


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._SelfBuilt = params.get("SelfBuilt")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._DropInvalidMessage = params.get("DropInvalidMessage")
        self._Index = params.get("Index")
        self._DateFormat = params.get("DateFormat")
        self._ContentKey = params.get("ContentKey")
        self._DropInvalidJsonMessage = params.get("DropInvalidJsonMessage")
        self._DocumentIdField = params.get("DocumentIdField")
        self._IndexType = params.get("IndexType")
        if params.get("DropCls") is not None:
            self._DropCls = DropCls()
            self._DropCls._deserialize(params.get("DropCls"))
        self._DatabasePrimaryKey = params.get("DatabasePrimaryKey")
        if params.get("DropDlq") is not None:
            self._DropDlq = FailureParam()
            self._DropDlq._deserialize(params.get("DropDlq"))
        if params.get("RecordMappingList") is not None:
            self._RecordMappingList = []
            for item in params.get("RecordMappingList"):
                obj = EsRecordMapping()
                obj._deserialize(item)
                self._RecordMappingList.append(obj)
        self._DateField = params.get("DateField")
        self._RecordMappingMode = params.get("RecordMappingMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsRecordMapping(AbstractModel):
    """消息字段与 es 索引的映射关系

    """

    def __init__(self):
        r"""
        :param _ColumnName: es 索引成员名称
        :type ColumnName: str
        :param _JsonKey: 消息字段名称
        :type JsonKey: str
        """
        self._ColumnName = None
        self._JsonKey = None

    @property
    def ColumnName(self):
        """es 索引成员名称
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def JsonKey(self):
        """消息字段名称
        :rtype: str
        """
        return self._JsonKey

    @JsonKey.setter
    def JsonKey(self, JsonKey):
        self._JsonKey = JsonKey


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._JsonKey = params.get("JsonKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventBusParam(AbstractModel):
    """EventBus配置

    """

    def __init__(self):
        r"""
        :param _Type: 资源类型。COS/ES/CLS
        :type Type: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _Resource: 实例资源
        :type Resource: str
        :param _Namespace: SCF云函数命名空间
        :type Namespace: str
        :param _FunctionName: SCF云函数函数名
        :type FunctionName: str
        :param _Qualifier: SCF云函数版本及别名
        :type Qualifier: str
        """
        self._Type = None
        self._SelfBuilt = None
        self._Resource = None
        self._Namespace = None
        self._FunctionName = None
        self._Qualifier = None

    @property
    def Type(self):
        """资源类型。COS/ES/CLS
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def Resource(self):
        """实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Namespace(self):
        """SCF云函数命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionName(self):
        """SCF云函数函数名
        :rtype: str
        """
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        """SCF云函数版本及别名
        :rtype: str
        """
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SelfBuilt = params.get("SelfBuilt")
        self._Resource = params.get("Resource")
        self._Namespace = params.get("Namespace")
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailureParam(AbstractModel):
    """数据处理规则失败处理

    """

    def __init__(self):
        r"""
        :param _Type: 类型，DLQ死信队列，IGNORE_ERROR保留，DROP废弃
        :type Type: str
        :param _KafkaParam: Ckafka类型死信队列
        :type KafkaParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaParam`
        :param _RetryInterval: 重试间隔
        :type RetryInterval: int
        :param _MaxRetryAttempts: 重试次数
        :type MaxRetryAttempts: int
        :param _TopicParam: DIP Topic类型死信队列
        :type TopicParam: :class:`tencentcloud.ckafka.v20190819.models.TopicParam`
        :param _DlqType: 死信队列类型，CKAFKA，TOPIC
        :type DlqType: str
        """
        self._Type = None
        self._KafkaParam = None
        self._RetryInterval = None
        self._MaxRetryAttempts = None
        self._TopicParam = None
        self._DlqType = None

    @property
    def Type(self):
        """类型，DLQ死信队列，IGNORE_ERROR保留，DROP废弃
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def KafkaParam(self):
        """Ckafka类型死信队列
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaParam`
        """
        return self._KafkaParam

    @KafkaParam.setter
    def KafkaParam(self, KafkaParam):
        self._KafkaParam = KafkaParam

    @property
    def RetryInterval(self):
        """重试间隔
        :rtype: int
        """
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def MaxRetryAttempts(self):
        """重试次数
        :rtype: int
        """
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def TopicParam(self):
        """DIP Topic类型死信队列
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicParam`
        """
        return self._TopicParam

    @TopicParam.setter
    def TopicParam(self, TopicParam):
        self._TopicParam = TopicParam

    @property
    def DlqType(self):
        """死信队列类型，CKAFKA，TOPIC
        :rtype: str
        """
        return self._DlqType

    @DlqType.setter
    def DlqType(self, DlqType):
        self._DlqType = DlqType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("KafkaParam") is not None:
            self._KafkaParam = KafkaParam()
            self._KafkaParam._deserialize(params.get("KafkaParam"))
        self._RetryInterval = params.get("RetryInterval")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        if params.get("TopicParam") is not None:
            self._TopicParam = TopicParam()
            self._TopicParam._deserialize(params.get("TopicParam"))
        self._DlqType = params.get("DlqType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchDatahubMessageByOffsetRequest(AbstractModel):
    """FetchDatahubMessageByOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 弹性topic名称
        :type Name: str
        :param _Partition: 分区id
        :type Partition: int
        :param _Offset: 位点信息，必填
        :type Offset: int
        """
        self._Name = None
        self._Partition = None
        self._Offset = None

    @property
    def Name(self):
        """弹性topic名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点信息，必填
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchDatahubMessageByOffsetResponse(AbstractModel):
    """FetchDatahubMessageByOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConsumerRecord()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class FetchLatestDatahubMessageListRequest(AbstractModel):
    """FetchLatestDatahubMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 弹性topic名称
        :type Name: str
        :param _Partition: 分区id
        :type Partition: int
        :param _Offset: 位点信息
        :type Offset: int
        :param _MessageCount: 最大查询条数，最小1，最大100
        :type MessageCount: int
        """
        self._Name = None
        self._Partition = None
        self._Offset = None
        self._MessageCount = None

    @property
    def Name(self):
        """弹性topic名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点信息
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def MessageCount(self):
        """最大查询条数，最小1，最大100
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._MessageCount = params.get("MessageCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchLatestDatahubMessageListResponse(AbstractModel):
    """FetchLatestDatahubMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果。
        :type Result: list of ConsumerRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果。
        :rtype: list of ConsumerRecord
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class FetchMessageByOffsetRequest(AbstractModel):
    """FetchMessageByOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Topic: 主题名
        :type Topic: str
        :param _Partition: 分区id
        :type Partition: int
        :param _Offset: 位点信息，必填
        :type Offset: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._Offset = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题名
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点信息，必填
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetResponse(AbstractModel):
    """FetchMessageByOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConsumerRecord()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class FetchMessageListByOffsetRequest(AbstractModel):
    """FetchMessageListByOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Topic: 主题名
        :type Topic: str
        :param _Partition: 分区id
        :type Partition: int
        :param _Offset: 位点信息
        :type Offset: int
        :param _SinglePartitionRecordNumber: 最大查询条数，默认20，最大20
        :type SinglePartitionRecordNumber: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._Offset = None
        self._SinglePartitionRecordNumber = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题名
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点信息
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SinglePartitionRecordNumber(self):
        """最大查询条数，默认20，最大20
        :rtype: int
        """
        return self._SinglePartitionRecordNumber

    @SinglePartitionRecordNumber.setter
    def SinglePartitionRecordNumber(self, SinglePartitionRecordNumber):
        self._SinglePartitionRecordNumber = SinglePartitionRecordNumber


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._SinglePartitionRecordNumber = params.get("SinglePartitionRecordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageListByOffsetResponse(AbstractModel):
    """FetchMessageListByOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果。注意，列表中不返回具体的消息内容（key、value），如果需要查询具体消息内容，请使用FetchMessageByOffset接口
        :type Result: list of ConsumerRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果。注意，列表中不返回具体的消息内容（key、value），如果需要查询具体消息内容，请使用FetchMessageByOffset接口
        :rtype: list of ConsumerRecord
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class FetchMessageListByTimestampRequest(AbstractModel):
    """FetchMessageListByTimestamp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Topic: 主题名
        :type Topic: str
        :param _Partition: 分区id
        :type Partition: int
        :param _StartTime: 查询开始时间，13位时间戳
        :type StartTime: int
        :param _SinglePartitionRecordNumber: 最大查询条数，默认20，最大20, 最小1
        :type SinglePartitionRecordNumber: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Partition = None
        self._StartTime = None
        self._SinglePartitionRecordNumber = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题名
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """分区id
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def StartTime(self):
        """查询开始时间，13位时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SinglePartitionRecordNumber(self):
        """最大查询条数，默认20，最大20, 最小1
        :rtype: int
        """
        return self._SinglePartitionRecordNumber

    @SinglePartitionRecordNumber.setter
    def SinglePartitionRecordNumber(self, SinglePartitionRecordNumber):
        self._SinglePartitionRecordNumber = SinglePartitionRecordNumber


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._StartTime = params.get("StartTime")
        self._SinglePartitionRecordNumber = params.get("SinglePartitionRecordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageListByTimestampResponse(AbstractModel):
    """FetchMessageListByTimestamp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果。注意，列表中不返回具体的消息内容（key、value），如果需要查询具体消息内容，请使用FetchMessageByOffset接口
        :type Result: list of ConsumerRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果。注意，列表中不返回具体的消息内容（key、value），如果需要查询具体消息内容，请使用FetchMessageByOffset接口
        :rtype: list of ConsumerRecord
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ConsumerRecord()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class FieldParam(AbstractModel):
    """数据处理——处理链

    """

    def __init__(self):
        r"""
        :param _Analyse: 解析
        :type Analyse: :class:`tencentcloud.ckafka.v20190819.models.AnalyseParam`
        :param _SecondaryAnalyse: 二次解析
        :type SecondaryAnalyse: :class:`tencentcloud.ckafka.v20190819.models.SecondaryAnalyseParam`
        :param _SMT: 数据处理
        :type SMT: list of SMTParam
        :param _Result: 测试结果
        :type Result: str
        :param _AnalyseResult: 解析结果
        :type AnalyseResult: list of SMTParam
        :param _SecondaryAnalyseResult: 二次解析结果
        :type SecondaryAnalyseResult: list of SMTParam
        :param _AnalyseJsonResult: JSON格式解析结果
        :type AnalyseJsonResult: str
        :param _SecondaryAnalyseJsonResult: JSON格式二次解析结果
        :type SecondaryAnalyseJsonResult: str
        """
        self._Analyse = None
        self._SecondaryAnalyse = None
        self._SMT = None
        self._Result = None
        self._AnalyseResult = None
        self._SecondaryAnalyseResult = None
        self._AnalyseJsonResult = None
        self._SecondaryAnalyseJsonResult = None

    @property
    def Analyse(self):
        """解析
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AnalyseParam`
        """
        return self._Analyse

    @Analyse.setter
    def Analyse(self, Analyse):
        self._Analyse = Analyse

    @property
    def SecondaryAnalyse(self):
        """二次解析
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SecondaryAnalyseParam`
        """
        return self._SecondaryAnalyse

    @SecondaryAnalyse.setter
    def SecondaryAnalyse(self, SecondaryAnalyse):
        self._SecondaryAnalyse = SecondaryAnalyse

    @property
    def SMT(self):
        """数据处理
        :rtype: list of SMTParam
        """
        return self._SMT

    @SMT.setter
    def SMT(self, SMT):
        self._SMT = SMT

    @property
    def Result(self):
        """测试结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AnalyseResult(self):
        """解析结果
        :rtype: list of SMTParam
        """
        return self._AnalyseResult

    @AnalyseResult.setter
    def AnalyseResult(self, AnalyseResult):
        self._AnalyseResult = AnalyseResult

    @property
    def SecondaryAnalyseResult(self):
        """二次解析结果
        :rtype: list of SMTParam
        """
        return self._SecondaryAnalyseResult

    @SecondaryAnalyseResult.setter
    def SecondaryAnalyseResult(self, SecondaryAnalyseResult):
        self._SecondaryAnalyseResult = SecondaryAnalyseResult

    @property
    def AnalyseJsonResult(self):
        """JSON格式解析结果
        :rtype: str
        """
        return self._AnalyseJsonResult

    @AnalyseJsonResult.setter
    def AnalyseJsonResult(self, AnalyseJsonResult):
        self._AnalyseJsonResult = AnalyseJsonResult

    @property
    def SecondaryAnalyseJsonResult(self):
        """JSON格式二次解析结果
        :rtype: str
        """
        return self._SecondaryAnalyseJsonResult

    @SecondaryAnalyseJsonResult.setter
    def SecondaryAnalyseJsonResult(self, SecondaryAnalyseJsonResult):
        self._SecondaryAnalyseJsonResult = SecondaryAnalyseJsonResult


    def _deserialize(self, params):
        if params.get("Analyse") is not None:
            self._Analyse = AnalyseParam()
            self._Analyse._deserialize(params.get("Analyse"))
        if params.get("SecondaryAnalyse") is not None:
            self._SecondaryAnalyse = SecondaryAnalyseParam()
            self._SecondaryAnalyse._deserialize(params.get("SecondaryAnalyse"))
        if params.get("SMT") is not None:
            self._SMT = []
            for item in params.get("SMT"):
                obj = SMTParam()
                obj._deserialize(item)
                self._SMT.append(obj)
        self._Result = params.get("Result")
        if params.get("AnalyseResult") is not None:
            self._AnalyseResult = []
            for item in params.get("AnalyseResult"):
                obj = SMTParam()
                obj._deserialize(item)
                self._AnalyseResult.append(obj)
        if params.get("SecondaryAnalyseResult") is not None:
            self._SecondaryAnalyseResult = []
            for item in params.get("SecondaryAnalyseResult"):
                obj = SMTParam()
                obj._deserialize(item)
                self._SecondaryAnalyseResult.append(obj)
        self._AnalyseJsonResult = params.get("AnalyseJsonResult")
        self._SecondaryAnalyseJsonResult = params.get("SecondaryAnalyseJsonResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤器
    >描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
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
        


class FilterMapParam(AbstractModel):
    """过滤器参数

    """

    def __init__(self):
        r"""
        :param _Key: Key值
        :type Key: str
        :param _MatchMode: 匹配模式，前缀匹配PREFIX，后缀匹配SUFFIX，包含匹配CONTAINS，EXCEPT除外匹配，数值匹配NUMBER，IP匹配IP
        :type MatchMode: str
        :param _Value: Value值
        :type Value: str
        :param _Type: 固定REGULAR
        :type Type: str
        """
        self._Key = None
        self._MatchMode = None
        self._Value = None
        self._Type = None

    @property
    def Key(self):
        """Key值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def MatchMode(self):
        """匹配模式，前缀匹配PREFIX，后缀匹配SUFFIX，包含匹配CONTAINS，EXCEPT除外匹配，数值匹配NUMBER，IP匹配IP
        :rtype: str
        """
        return self._MatchMode

    @MatchMode.setter
    def MatchMode(self, MatchMode):
        self._MatchMode = MatchMode

    @property
    def Value(self):
        """Value值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        """固定REGULAR
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._MatchMode = params.get("MatchMode")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Group(AbstractModel):
    """组实体

    """

    def __init__(self):
        r"""
        :param _GroupName: 消费分组名称
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
        """消费分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoMember(AbstractModel):
    """consumer信息

    """

    def __init__(self):
        r"""
        :param _MemberId: coordinator 为消费分组中的消费者生成的唯一 ID
        :type MemberId: str
        :param _ClientId: 客户消费者 SDK 自己设置的 client.id 信息
        :type ClientId: str
        :param _ClientHost: 一般存储客户的 IP 地址
        :type ClientHost: str
        :param _Assignment: 存储着分配给该消费者的 partition 信息
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self._MemberId = None
        self._ClientId = None
        self._ClientHost = None
        self._Assignment = None

    @property
    def MemberId(self):
        """coordinator 为消费分组中的消费者生成的唯一 ID
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ClientId(self):
        """客户消费者 SDK 自己设置的 client.id 信息
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientHost(self):
        """一般存储客户的 IP 地址
        :rtype: str
        """
        return self._ClientHost

    @ClientHost.setter
    def ClientHost(self, ClientHost):
        self._ClientHost = ClientHost

    @property
    def Assignment(self):
        """存储着分配给该消费者的 partition 信息
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        return self._Assignment

    @Assignment.setter
    def Assignment(self, Assignment):
        self._Assignment = Assignment


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._ClientId = params.get("ClientId")
        self._ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self._Assignment = Assignment()
            self._Assignment._deserialize(params.get("Assignment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoResponse(AbstractModel):
    """GroupInfo返回数据的实体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码，正常为0
        :type ErrorCode: str
        :param _State: group 状态描述（常见的为 Empty、Stable、Dead 三种状态）：
Dead：消费分组不存在
Empty：消费分组，当前没有任何消费者订阅
PreparingRebalance：消费分组处于 rebalance 状态
CompletingRebalance：消费分组处于 rebalance 状态
Stable：消费分组中各个消费者已经加入，处于稳定状态
        :type State: str
        :param _ProtocolType: 消费分组选择的协议类型正常的消费者一般为 consumer 但有些系统采用了自己的协议如 kafka-connect 用的就是 connect。只有标准的 consumer 协议，本接口才知道具体的分配方式的格式，才能解析到具体的 partition 的分配情况
        :type ProtocolType: str
        :param _Protocol: 消费者 partition 分配算法常见的有如下几种(Kafka 消费者 SDK 默认的选择项为 range)：range、 roundrobin、 sticky
        :type Protocol: str
        :param _Members: 仅当 state 为 Stable 且 protocol_type 为 consumer 时， 该数组才包含信息
        :type Members: list of GroupInfoMember
        :param _Group: 消费分组名称
        :type Group: str
        """
        self._ErrorCode = None
        self._State = None
        self._ProtocolType = None
        self._Protocol = None
        self._Members = None
        self._Group = None

    @property
    def ErrorCode(self):
        """错误码，正常为0
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def State(self):
        """group 状态描述（常见的为 Empty、Stable、Dead 三种状态）：
Dead：消费分组不存在
Empty：消费分组，当前没有任何消费者订阅
PreparingRebalance：消费分组处于 rebalance 状态
CompletingRebalance：消费分组处于 rebalance 状态
Stable：消费分组中各个消费者已经加入，处于稳定状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ProtocolType(self):
        """消费分组选择的协议类型正常的消费者一般为 consumer 但有些系统采用了自己的协议如 kafka-connect 用的就是 connect。只有标准的 consumer 协议，本接口才知道具体的分配方式的格式，才能解析到具体的 partition 的分配情况
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Protocol(self):
        """消费者 partition 分配算法常见的有如下几种(Kafka 消费者 SDK 默认的选择项为 range)：range、 roundrobin、 sticky
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Members(self):
        """仅当 state 为 Stable 且 protocol_type 为 consumer 时， 该数组才包含信息
        :rtype: list of GroupInfoMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def Group(self):
        """消费分组名称
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._State = params.get("State")
        self._ProtocolType = params.get("ProtocolType")
        self._Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self._Members.append(obj)
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoTopics(AbstractModel):
    """GroupInfo内部topic对象

    """

    def __init__(self):
        r"""
        :param _Topic: 分配的 topic 名称
        :type Topic: str
        :param _Partitions: 分配的 partition 信息
        :type Partitions: list of int
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        """分配的 topic 名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        """分配的 partition 信息
        :rtype: list of int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetPartition(AbstractModel):
    """组偏移量分区对象

    """

    def __init__(self):
        r"""
        :param _Partition: topic 的 partitionId
        :type Partition: int
        :param _Offset: consumer 提交的 offset 位置
        :type Offset: int
        :param _Metadata: 支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串
        :type Metadata: str
        :param _ErrorCode: 错误码
        :type ErrorCode: int
        :param _LogEndOffset: 当前 partition 最新的 offset
        :type LogEndOffset: int
        :param _Lag: 未消费的消息个数
        :type Lag: int
        """
        self._Partition = None
        self._Offset = None
        self._Metadata = None
        self._ErrorCode = None
        self._LogEndOffset = None
        self._Lag = None

    @property
    def Partition(self):
        """topic 的 partitionId
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """consumer 提交的 offset 位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Metadata(self):
        """支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串
        :rtype: str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def ErrorCode(self):
        """错误码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def LogEndOffset(self):
        """当前 partition 最新的 offset
        :rtype: int
        """
        return self._LogEndOffset

    @LogEndOffset.setter
    def LogEndOffset(self, LogEndOffset):
        self._LogEndOffset = LogEndOffset

    @property
    def Lag(self):
        """未消费的消息个数
        :rtype: int
        """
        return self._Lag

    @Lag.setter
    def Lag(self, Lag):
        self._Lag = Lag


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        self._Metadata = params.get("Metadata")
        self._ErrorCode = params.get("ErrorCode")
        self._LogEndOffset = params.get("LogEndOffset")
        self._Lag = params.get("Lag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetResponse(AbstractModel):
    """消费组偏移量返回结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合调节的总结果数
        :type TotalCount: int
        :param _TopicList: 该主题分区数组，其中每个元素为一个 json object
        :type TopicList: list of GroupOffsetTopic
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        """符合调节的总结果数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """该主题分区数组，其中每个元素为一个 json object
        :rtype: list of GroupOffsetTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetTopic(AbstractModel):
    """消费分组主题对象

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名称
        :type Topic: str
        :param _Partitions: 该主题分区数组，其中每个元素为一个 json object
        :type Partitions: list of GroupOffsetPartition
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
        """该主题分区数组，其中每个元素为一个 json object
        :rtype: list of GroupOffsetPartition
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResponse(AbstractModel):
    """DescribeGroup的返回

    """

    def __init__(self):
        r"""
        :param _TotalCount: 计数
        :type TotalCount: int
        :param _GroupList: GroupList
        :type GroupList: list of DescribeGroup
        :param _GroupCountQuota: 消费分组配额
        :type GroupCountQuota: int
        """
        self._TotalCount = None
        self._GroupList = None
        self._GroupCountQuota = None

    @property
    def TotalCount(self):
        """计数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupList(self):
        """GroupList
        :rtype: list of DescribeGroup
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def GroupCountQuota(self):
        """消费分组配额
        :rtype: int
        """
        return self._GroupCountQuota

    @GroupCountQuota.setter
    def GroupCountQuota(self, GroupCountQuota):
        self._GroupCountQuota = GroupCountQuota


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._GroupCountQuota = params.get("GroupCountQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceRequest(AbstractModel):
    """InquireCkafkaPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 国内站标准版填写standards2, 国际站标准版填写standard,专业版填写profession,高级版填写premium
        :type InstanceType: str
        :param _InstanceChargeParam: 购买/续费付费类型(购买时不填的话, 默认获取购买包年包月一个月的费用)
        :type InstanceChargeParam: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        :param _InstanceNum: 购买/续费时购买的实例数量(不填时, 默认为1个)
        :type InstanceNum: int
        :param _Bandwidth: 实例内网带宽大小, 单位MB/s (购买时必填，专业版/高级版询价时带宽信息必填)
        :type Bandwidth: int
        :param _InquiryDiskParam: 实例的硬盘购买类型以及大小 (购买时必填，专业版/高级版询价时磁盘信息必填)
        :type InquiryDiskParam: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        :param _MessageRetention: 实例消息保留时间大小, 单位小时 (购买时必填)
        :type MessageRetention: int
        :param _Topic: 购买实例topic数, 单位个 (购买时必填)
        :type Topic: int
        :param _Partition: 购买实例分区数, 单位个 (购买时必填，专业版/高级版询价时带宽信息必填)
        :type Partition: int
        :param _ZoneIds: 购买地域, 可通过查看DescribeCkafkaZone这个接口获取ZoneId
        :type ZoneIds: list of int
        :param _CategoryAction: 标记操作, 新购填写purchase, 续费填写renew, (不填时, 默认为purchase)
        :type CategoryAction: str
        :param _BillType: 国内站购买的版本, sv_ckafka_instance_s2_1(入门型), sv_ckafka_instance_s2_2(标准版), sv_ckafka_instance_s2_3(进阶型), 如果instanceType为standards2, 但该参数为空, 则默认值为sv_ckafka_instance_s2_1
        :type BillType: str
        :param _PublicNetworkParam: 公网带宽计费模式, 目前只有专业版支持公网带宽 (购买公网带宽时必填)
        :type PublicNetworkParam: :class:`tencentcloud.ckafka.v20190819.models.InquiryPublicNetworkParam`
        :param _InstanceId: 续费时的实例id, 续费时填写
        :type InstanceId: str
        """
        self._InstanceType = None
        self._InstanceChargeParam = None
        self._InstanceNum = None
        self._Bandwidth = None
        self._InquiryDiskParam = None
        self._MessageRetention = None
        self._Topic = None
        self._Partition = None
        self._ZoneIds = None
        self._CategoryAction = None
        self._BillType = None
        self._PublicNetworkParam = None
        self._InstanceId = None

    @property
    def InstanceType(self):
        """国内站标准版填写standards2, 国际站标准版填写standard,专业版填写profession,高级版填写premium
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeParam(self):
        """购买/续费付费类型(购买时不填的话, 默认获取购买包年包月一个月的费用)
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceChargeParam`
        """
        return self._InstanceChargeParam

    @InstanceChargeParam.setter
    def InstanceChargeParam(self, InstanceChargeParam):
        self._InstanceChargeParam = InstanceChargeParam

    @property
    def InstanceNum(self):
        """购买/续费时购买的实例数量(不填时, 默认为1个)
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Bandwidth(self):
        """实例内网带宽大小, 单位MB/s (购买时必填，专业版/高级版询价时带宽信息必填)
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def InquiryDiskParam(self):
        """实例的硬盘购买类型以及大小 (购买时必填，专业版/高级版询价时磁盘信息必填)
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryDiskParam`
        """
        return self._InquiryDiskParam

    @InquiryDiskParam.setter
    def InquiryDiskParam(self, InquiryDiskParam):
        self._InquiryDiskParam = InquiryDiskParam

    @property
    def MessageRetention(self):
        """实例消息保留时间大小, 单位小时 (购买时必填)
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def Topic(self):
        """购买实例topic数, 单位个 (购买时必填)
        :rtype: int
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        """购买实例分区数, 单位个 (购买时必填，专业版/高级版询价时带宽信息必填)
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def ZoneIds(self):
        """购买地域, 可通过查看DescribeCkafkaZone这个接口获取ZoneId
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def CategoryAction(self):
        """标记操作, 新购填写purchase, 续费填写renew, (不填时, 默认为purchase)
        :rtype: str
        """
        return self._CategoryAction

    @CategoryAction.setter
    def CategoryAction(self, CategoryAction):
        self._CategoryAction = CategoryAction

    @property
    def BillType(self):
        """国内站购买的版本, sv_ckafka_instance_s2_1(入门型), sv_ckafka_instance_s2_2(标准版), sv_ckafka_instance_s2_3(进阶型), 如果instanceType为standards2, 但该参数为空, 则默认值为sv_ckafka_instance_s2_1
        :rtype: str
        """
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PublicNetworkParam(self):
        """公网带宽计费模式, 目前只有专业版支持公网带宽 (购买公网带宽时必填)
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPublicNetworkParam`
        """
        return self._PublicNetworkParam

    @PublicNetworkParam.setter
    def PublicNetworkParam(self, PublicNetworkParam):
        self._PublicNetworkParam = PublicNetworkParam

    @property
    def InstanceId(self):
        """续费时的实例id, 续费时填写
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("InstanceChargeParam") is not None:
            self._InstanceChargeParam = InstanceChargeParam()
            self._InstanceChargeParam._deserialize(params.get("InstanceChargeParam"))
        self._InstanceNum = params.get("InstanceNum")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("InquiryDiskParam") is not None:
            self._InquiryDiskParam = InquiryDiskParam()
            self._InquiryDiskParam._deserialize(params.get("InquiryDiskParam"))
        self._MessageRetention = params.get("MessageRetention")
        self._Topic = params.get("Topic")
        self._Partition = params.get("Partition")
        self._ZoneIds = params.get("ZoneIds")
        self._CategoryAction = params.get("CategoryAction")
        self._BillType = params.get("BillType")
        if params.get("PublicNetworkParam") is not None:
            self._PublicNetworkParam = InquiryPublicNetworkParam()
            self._PublicNetworkParam._deserialize(params.get("PublicNetworkParam"))
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceResp(AbstractModel):
    """InquireCkafkaPrice接口询价返回值

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格
        :type InstancePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        :param _PublicNetworkBandwidthPrice: 公网带宽价格
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkBandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        self._InstancePrice = None
        self._PublicNetworkBandwidthPrice = None

    @property
    def InstancePrice(self):
        """实例价格
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def PublicNetworkBandwidthPrice(self):
        """公网带宽价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        return self._PublicNetworkBandwidthPrice

    @PublicNetworkBandwidthPrice.setter
    def PublicNetworkBandwidthPrice(self, PublicNetworkBandwidthPrice):
        self._PublicNetworkBandwidthPrice = PublicNetworkBandwidthPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InquiryPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("PublicNetworkBandwidthPrice") is not None:
            self._PublicNetworkBandwidthPrice = InquiryPrice()
            self._PublicNetworkBandwidthPrice._deserialize(params.get("PublicNetworkBandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquireCkafkaPriceResponse(AbstractModel):
    """InquireCkafkaPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = InquireCkafkaPriceResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InquiryBasePrice(AbstractModel):
    """询价返回参数

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 单位原价
        :type UnitPrice: float
        :param _UnitPriceDiscount: 折扣单位价格
        :type UnitPriceDiscount: float
        :param _OriginalPrice: 合计原价
        :type OriginalPrice: float
        :param _DiscountPrice: 折扣合计价格
        :type DiscountPrice: float
        :param _Discount: 折扣(单位是%)
        :type Discount: float
        :param _GoodsNum: 商品数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        :param _Currency: 付费货币
注意：此字段可能返回 null，表示取不到有效值。
        :type Currency: str
        :param _DiskType: 硬盘专用返回参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _TimeSpan: 购买时长
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位("m"按月, "h"按小时)
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _Value: 购买数量
        :type Value: int
        """
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._GoodsNum = None
        self._Currency = None
        self._DiskType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Value = None

    @property
    def UnitPrice(self):
        """单位原价
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        """折扣单位价格
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        """合计原价
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """折扣合计价格
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """折扣(单位是%)
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        """商品数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        """付费货币
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        """硬盘专用返回参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        """购买时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """购买时长单位("m"按月, "h"按小时)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        """购买数量
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._GoodsNum = params.get("GoodsNum")
        self._Currency = params.get("Currency")
        self._DiskType = params.get("DiskType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryDetailPrice(AbstractModel):
    """详细类别的价格

    """

    def __init__(self):
        r"""
        :param _BandwidthPrice: 额外内网带宽价格
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _DiskPrice: 硬盘价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _PartitionPrice: 额外分区价格
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _TopicPrice: 额外Topic价格
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        :param _InstanceTypePrice: 实例套餐价格
        :type InstanceTypePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        self._BandwidthPrice = None
        self._DiskPrice = None
        self._PartitionPrice = None
        self._TopicPrice = None
        self._InstanceTypePrice = None

    @property
    def BandwidthPrice(self):
        """额外内网带宽价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def DiskPrice(self):
        """硬盘价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def PartitionPrice(self):
        """额外分区价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._PartitionPrice

    @PartitionPrice.setter
    def PartitionPrice(self, PartitionPrice):
        self._PartitionPrice = PartitionPrice

    @property
    def TopicPrice(self):
        """额外Topic价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._TopicPrice

    @TopicPrice.setter
    def TopicPrice(self, TopicPrice):
        self._TopicPrice = TopicPrice

    @property
    def InstanceTypePrice(self):
        """实例套餐价格
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        return self._InstanceTypePrice

    @InstanceTypePrice.setter
    def InstanceTypePrice(self, InstanceTypePrice):
        self._InstanceTypePrice = InstanceTypePrice


    def _deserialize(self, params):
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = InquiryBasePrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        if params.get("DiskPrice") is not None:
            self._DiskPrice = InquiryBasePrice()
            self._DiskPrice._deserialize(params.get("DiskPrice"))
        if params.get("PartitionPrice") is not None:
            self._PartitionPrice = InquiryBasePrice()
            self._PartitionPrice._deserialize(params.get("PartitionPrice"))
        if params.get("TopicPrice") is not None:
            self._TopicPrice = InquiryBasePrice()
            self._TopicPrice._deserialize(params.get("TopicPrice"))
        if params.get("InstanceTypePrice") is not None:
            self._InstanceTypePrice = InquiryBasePrice()
            self._InstanceTypePrice._deserialize(params.get("InstanceTypePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryDiskParam(AbstractModel):
    """购买硬盘参数

    """

    def __init__(self):
        r"""
        :param _DiskType: 购买硬盘类型: SSD(SSD), CLOUD_SSD(SSD云硬盘), CLOUD_PREMIUM(高性能云硬盘), CLOUD_BASIC(云盘)
        :type DiskType: str
        :param _DiskSize: 购买硬盘大小: 单位GB
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """购买硬盘类型: SSD(SSD), CLOUD_SSD(SSD云硬盘), CLOUD_PREMIUM(高性能云硬盘), CLOUD_BASIC(云盘)
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """购买硬盘大小: 单位GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPrice(AbstractModel):
    """询价返回参数

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 单位原价
        :type UnitPrice: float
        :param _UnitPriceDiscount: 折扣单位价格
        :type UnitPriceDiscount: float
        :param _OriginalPrice: 合计原价
        :type OriginalPrice: float
        :param _DiscountPrice: 折扣合计价格
        :type DiscountPrice: float
        :param _Discount: 折扣(单位是%)
        :type Discount: float
        :param _GoodsNum: 商品数量
        :type GoodsNum: int
        :param _Currency: 付费货币
        :type Currency: str
        :param _DiskType: 硬盘专用返回参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _TimeSpan: 购买时长
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位("m"按月, "h"按小时)
        :type TimeUnit: str
        :param _Value: 购买数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        :param _DetailPrices: 详细类别的价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailPrices: :class:`tencentcloud.ckafka.v20190819.models.InquiryDetailPrice`
        """
        self._UnitPrice = None
        self._UnitPriceDiscount = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._GoodsNum = None
        self._Currency = None
        self._DiskType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Value = None
        self._DetailPrices = None

    @property
    def UnitPrice(self):
        """单位原价
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        """折扣单位价格
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def OriginalPrice(self):
        """合计原价
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """折扣合计价格
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """折扣(单位是%)
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        """商品数量
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        """付费货币
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        """硬盘专用返回参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        """购买时长
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """购买时长单位("m"按月, "h"按小时)
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        """购买数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DetailPrices(self):
        """详细类别的价格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquiryDetailPrice`
        """
        return self._DetailPrices

    @DetailPrices.setter
    def DetailPrices(self, DetailPrices):
        self._DetailPrices = DetailPrices


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._GoodsNum = params.get("GoodsNum")
        self._Currency = params.get("Currency")
        self._DiskType = params.get("DiskType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Value = params.get("Value")
        if params.get("DetailPrices") is not None:
            self._DetailPrices = InquiryDetailPrice()
            self._DetailPrices._deserialize(params.get("DetailPrices"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPublicNetworkParam(AbstractModel):
    """公网带宽参数

    """

    def __init__(self):
        r"""
        :param _PublicNetworkChargeType: 公网计费模式: BANDWIDTH_PREPAID(包年包月), BANDWIDTH_POSTPAID_BY_HOUR(带宽按小时计费)
        :type PublicNetworkChargeType: str
        :param _PublicNetworkMonthly: 公网带宽, 单位MB
        :type PublicNetworkMonthly: int
        """
        self._PublicNetworkChargeType = None
        self._PublicNetworkMonthly = None

    @property
    def PublicNetworkChargeType(self):
        """公网计费模式: BANDWIDTH_PREPAID(包年包月), BANDWIDTH_POSTPAID_BY_HOUR(带宽按小时计费)
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetworkMonthly(self):
        """公网带宽, 单位MB
        :rtype: int
        """
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


    def _deserialize(self, params):
        self._PublicNetworkChargeType = params.get("PublicNetworkChargeType")
        self._PublicNetworkMonthly = params.get("PublicNetworkMonthly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例对象

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _InstanceName: ckafka集群实例Name
        :type InstanceName: str
        :param _Status: 实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :type Status: int
        :param _IfCommunity: 是否开源实例。开源：true，不开源：false
        :type IfCommunity: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._IfCommunity = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """ckafka集群实例Name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IfCommunity(self):
        """是否开源实例。开源：true，不开源：false
        :rtype: bool
        """
        return self._IfCommunity

    @IfCommunity.setter
    def IfCommunity(self, IfCommunity):
        self._IfCommunity = IfCommunity


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._IfCommunity = params.get("IfCommunity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAttributesResponse(AbstractModel):
    """实例属性返回结果对象

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _InstanceName: ckafka集群实例Name
        :type InstanceName: str
        :param _VipList: 接入点 VIP 列表信息
        :type VipList: list of VipEntity
        :param _Vip: 虚拟IP
        :type Vip: str
        :param _Vport: 虚拟端口
        :type Vport: str
        :param _Status: 实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :type Status: int
        :param _Bandwidth: 实例带宽，单位：Mbps
        :type Bandwidth: int
        :param _DiskSize: 实例的存储大小，单位：GB
        :type DiskSize: int
        :param _ZoneId: 可用区
        :type ZoneId: int
        :param _VpcId: VPC 的 ID，为空表示是基础网络
        :type VpcId: str
        :param _SubnetId: 子网 ID， 为空表示基础网络
        :type SubnetId: str
        :param _Healthy: 实例健康状态， 1：健康，2：告警，3：异常
        :type Healthy: int
        :param _HealthyMessage: 实例健康信息，当前会展示磁盘利用率，最大长度为256
        :type HealthyMessage: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _MsgRetentionTime: 消息保存时间,单位为分钟
        :type MsgRetentionTime: int
        :param _Config: 自动创建 Topic 配置， 若该字段为空，则表示未开启自动创建
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param _RemainderPartitions: 剩余创建分区数
        :type RemainderPartitions: int
        :param _RemainderTopics: 剩余创建主题数
        :type RemainderTopics: int
        :param _CreatedPartitions: 当前创建分区数
        :type CreatedPartitions: int
        :param _CreatedTopics: 当前创建主题数
        :type CreatedTopics: int
        :param _Tags: 标签数组
        :type Tags: list of Tag
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        :param _ZoneIds: 可用区列表
        :type ZoneIds: list of int
        :param _Version: ckafka集群实例版本
        :type Version: str
        :param _MaxGroupNum: 最大分组数
        :type MaxGroupNum: int
        :param _Cvm: 售卖类型,0:标准版,1:专业版
        :type Cvm: int
        :param _InstanceType: 类型
        :type InstanceType: str
        :param _Features: 表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
        :type Features: list of str
        :param _RetentionTimeConfig: 动态消息保留策略
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _MaxConnection: 最大连接数
        :type MaxConnection: int
        :param _PublicNetwork: 公网带宽
        :type PublicNetwork: int
        :param _DeleteRouteTimestamp: 时间
        :type DeleteRouteTimestamp: str
        :param _RemainingPartitions: 剩余创建分区数
        :type RemainingPartitions: int
        :param _RemainingTopics: 剩余创建主题数
        :type RemainingTopics: int
        :param _DynamicDiskConfig: 动态硬盘扩容策略
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _InstanceChargeType: 实例计费类型
        :type InstanceChargeType: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _FreePartitionNumber: 免费分区数量
        :type FreePartitionNumber: int
        :param _ElasticFloatBandwidth: 弹性带宽上浮值
        :type ElasticFloatBandwidth: int
        :param _CustomCertId: ssl自定义证书id
        :type CustomCertId: str
        :param _UncleanLeaderElectionEnable: 集群topic默认 unclean.leader.election.enable配置: 1 开启 0 关闭
        :type UncleanLeaderElectionEnable: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VipList = None
        self._Vip = None
        self._Vport = None
        self._Status = None
        self._Bandwidth = None
        self._DiskSize = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Healthy = None
        self._HealthyMessage = None
        self._CreateTime = None
        self._MsgRetentionTime = None
        self._Config = None
        self._RemainderPartitions = None
        self._RemainderTopics = None
        self._CreatedPartitions = None
        self._CreatedTopics = None
        self._Tags = None
        self._ExpireTime = None
        self._ZoneIds = None
        self._Version = None
        self._MaxGroupNum = None
        self._Cvm = None
        self._InstanceType = None
        self._Features = None
        self._RetentionTimeConfig = None
        self._MaxConnection = None
        self._PublicNetwork = None
        self._DeleteRouteTimestamp = None
        self._RemainingPartitions = None
        self._RemainingTopics = None
        self._DynamicDiskConfig = None
        self._InstanceChargeType = None
        self._ClusterType = None
        self._FreePartitionNumber = None
        self._ElasticFloatBandwidth = None
        self._CustomCertId = None
        self._UncleanLeaderElectionEnable = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """ckafka集群实例Name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VipList(self):
        """接入点 VIP 列表信息
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Vip(self):
        """虚拟IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """虚拟端口
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        """实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        """实例带宽，单位：Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        """实例的存储大小，单位：GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        """可用区
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """VPC 的 ID，为空表示是基础网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网 ID， 为空表示基础网络
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Healthy(self):
        """实例健康状态， 1：健康，2：告警，3：异常
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        """实例健康信息，当前会展示磁盘利用率，最大长度为256
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MsgRetentionTime(self):
        """消息保存时间,单位为分钟
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def Config(self):
        """自动创建 Topic 配置， 若该字段为空，则表示未开启自动创建
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RemainderPartitions(self):
        """剩余创建分区数
        :rtype: int
        """
        return self._RemainderPartitions

    @RemainderPartitions.setter
    def RemainderPartitions(self, RemainderPartitions):
        self._RemainderPartitions = RemainderPartitions

    @property
    def RemainderTopics(self):
        """剩余创建主题数
        :rtype: int
        """
        return self._RemainderTopics

    @RemainderTopics.setter
    def RemainderTopics(self, RemainderTopics):
        self._RemainderTopics = RemainderTopics

    @property
    def CreatedPartitions(self):
        """当前创建分区数
        :rtype: int
        """
        return self._CreatedPartitions

    @CreatedPartitions.setter
    def CreatedPartitions(self, CreatedPartitions):
        self._CreatedPartitions = CreatedPartitions

    @property
    def CreatedTopics(self):
        """当前创建主题数
        :rtype: int
        """
        return self._CreatedTopics

    @CreatedTopics.setter
    def CreatedTopics(self, CreatedTopics):
        self._CreatedTopics = CreatedTopics

    @property
    def Tags(self):
        """标签数组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ZoneIds(self):
        """可用区列表
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Version(self):
        """ckafka集群实例版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def MaxGroupNum(self):
        """最大分组数
        :rtype: int
        """
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def Cvm(self):
        """售卖类型,0:标准版,1:专业版
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        """类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Features(self):
        """表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def RetentionTimeConfig(self):
        """动态消息保留策略
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def MaxConnection(self):
        """最大连接数
        :rtype: int
        """
        return self._MaxConnection

    @MaxConnection.setter
    def MaxConnection(self, MaxConnection):
        self._MaxConnection = MaxConnection

    @property
    def PublicNetwork(self):
        """公网带宽
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DeleteRouteTimestamp(self):
        """时间
        :rtype: str
        """
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        self._DeleteRouteTimestamp = DeleteRouteTimestamp

    @property
    def RemainingPartitions(self):
        """剩余创建分区数
        :rtype: int
        """
        return self._RemainingPartitions

    @RemainingPartitions.setter
    def RemainingPartitions(self, RemainingPartitions):
        self._RemainingPartitions = RemainingPartitions

    @property
    def RemainingTopics(self):
        """剩余创建主题数
        :rtype: int
        """
        return self._RemainingTopics

    @RemainingTopics.setter
    def RemainingTopics(self, RemainingTopics):
        self._RemainingTopics = RemainingTopics

    @property
    def DynamicDiskConfig(self):
        """动态硬盘扩容策略
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def InstanceChargeType(self):
        """实例计费类型
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def ClusterType(self):
        """集群类型
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def FreePartitionNumber(self):
        """免费分区数量
        :rtype: int
        """
        return self._FreePartitionNumber

    @FreePartitionNumber.setter
    def FreePartitionNumber(self, FreePartitionNumber):
        self._FreePartitionNumber = FreePartitionNumber

    @property
    def ElasticFloatBandwidth(self):
        """弹性带宽上浮值
        :rtype: int
        """
        return self._ElasticFloatBandwidth

    @ElasticFloatBandwidth.setter
    def ElasticFloatBandwidth(self, ElasticFloatBandwidth):
        self._ElasticFloatBandwidth = ElasticFloatBandwidth

    @property
    def CustomCertId(self):
        """ssl自定义证书id
        :rtype: str
        """
        return self._CustomCertId

    @CustomCertId.setter
    def CustomCertId(self, CustomCertId):
        self._CustomCertId = CustomCertId

    @property
    def UncleanLeaderElectionEnable(self):
        """集群topic默认 unclean.leader.election.enable配置: 1 开启 0 关闭
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._Bandwidth = params.get("Bandwidth")
        self._DiskSize = params.get("DiskSize")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Healthy = params.get("Healthy")
        self._HealthyMessage = params.get("HealthyMessage")
        self._CreateTime = params.get("CreateTime")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self._Config = InstanceConfigDO()
            self._Config._deserialize(params.get("Config"))
        self._RemainderPartitions = params.get("RemainderPartitions")
        self._RemainderTopics = params.get("RemainderTopics")
        self._CreatedPartitions = params.get("CreatedPartitions")
        self._CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ExpireTime = params.get("ExpireTime")
        self._ZoneIds = params.get("ZoneIds")
        self._Version = params.get("Version")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._Cvm = params.get("Cvm")
        self._InstanceType = params.get("InstanceType")
        self._Features = params.get("Features")
        if params.get("RetentionTimeConfig") is not None:
            self._RetentionTimeConfig = DynamicRetentionTime()
            self._RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self._MaxConnection = params.get("MaxConnection")
        self._PublicNetwork = params.get("PublicNetwork")
        self._DeleteRouteTimestamp = params.get("DeleteRouteTimestamp")
        self._RemainingPartitions = params.get("RemainingPartitions")
        self._RemainingTopics = params.get("RemainingTopics")
        if params.get("DynamicDiskConfig") is not None:
            self._DynamicDiskConfig = DynamicDiskConfig()
            self._DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._ClusterType = params.get("ClusterType")
        self._FreePartitionNumber = params.get("FreePartitionNumber")
        self._ElasticFloatBandwidth = params.get("ElasticFloatBandwidth")
        self._CustomCertId = params.get("CustomCertId")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargeParam(AbstractModel):
    """实例购买付费参数

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 实例付费类型: PREPAID(包年包月), POSTPAID_BY_HOUR(按量付费)
        :type InstanceChargeType: str
        :param _InstanceChargePeriod: 购买时长: 包年包月时需要填写, 按量计费无需填写
        :type InstanceChargePeriod: int
        """
        self._InstanceChargeType = None
        self._InstanceChargePeriod = None

    @property
    def InstanceChargeType(self):
        """实例付费类型: PREPAID(包年包月), POSTPAID_BY_HOUR(按量付费)
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePeriod(self):
        """购买时长: 包年包月时需要填写, 按量计费无需填写
        :rtype: int
        """
        return self._InstanceChargePeriod

    @InstanceChargePeriod.setter
    def InstanceChargePeriod(self, InstanceChargePeriod):
        self._InstanceChargePeriod = InstanceChargePeriod


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceChargePeriod = params.get("InstanceChargePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigDO(AbstractModel):
    """实例配置实体

    """

    def __init__(self):
        r"""
        :param _AutoCreateTopicsEnable: 是否自动创建主题
        :type AutoCreateTopicsEnable: bool
        :param _DefaultNumPartitions: 分区数
        :type DefaultNumPartitions: int
        :param _DefaultReplicationFactor: 默认的复制Factor
        :type DefaultReplicationFactor: int
        """
        self._AutoCreateTopicsEnable = None
        self._DefaultNumPartitions = None
        self._DefaultReplicationFactor = None

    @property
    def AutoCreateTopicsEnable(self):
        """是否自动创建主题
        :rtype: bool
        """
        return self._AutoCreateTopicsEnable

    @AutoCreateTopicsEnable.setter
    def AutoCreateTopicsEnable(self, AutoCreateTopicsEnable):
        self._AutoCreateTopicsEnable = AutoCreateTopicsEnable

    @property
    def DefaultNumPartitions(self):
        """分区数
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        """默认的复制Factor
        :rtype: int
        """
        return self._DefaultReplicationFactor

    @DefaultReplicationFactor.setter
    def DefaultReplicationFactor(self, DefaultReplicationFactor):
        self._DefaultReplicationFactor = DefaultReplicationFactor


    def _deserialize(self, params):
        self._AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self._DefaultNumPartitions = params.get("DefaultNumPartitions")
        self._DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeleteResponse(AbstractModel):
    """删除实例返回任务

    """

    def __init__(self):
        r"""
        :param _FlowId: 删除实例返回的任务Id
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """删除实例返回的任务Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _InstanceName: ckafka集群实例名称
        :type InstanceName: str
        :param _Vip: 访问实例的vip 信息
        :type Vip: str
        :param _Vport: 访问实例的端口信息
        :type Vport: str
        :param _VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param _Status: 实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :type Status: int
        :param _Bandwidth: 实例带宽，单位Mbps
        :type Bandwidth: int
        :param _DiskSize: ckafka集群实例磁盘大小，单位G
        :type DiskSize: int
        :param _ZoneId: 可用区域ID
        :type ZoneId: int
        :param _VpcId: vpcId，如果为空，说明是基础网络
        :type VpcId: str
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _RenewFlag: 实例是否续费，int  枚举值：1表示自动续费，2表示明确不自动续费
        :type RenewFlag: int
        :param _Healthy: 实例状态 int：1表示健康，2表示告警，3 表示实例状态异常
        :type Healthy: int
        :param _HealthyMessage: 实例状态信息
        :type HealthyMessage: str
        :param _CreateTime: 实例创建时间
        :type CreateTime: int
        :param _ExpireTime: 实例过期时间
        :type ExpireTime: int
        :param _IsInternal: 是否为内部客户。值为1 表示内部客户
        :type IsInternal: int
        :param _TopicNum: Topic个数
        :type TopicNum: int
        :param _Tags: 标识tag
        :type Tags: list of Tag
        :param _Version: kafka版本信息
        :type Version: str
        :param _ZoneIds: 跨可用区
        :type ZoneIds: list of int
        :param _Cvm: ckafka售卖类型
        :type Cvm: int
        :param _InstanceType: ckafka集群实例类型
        :type InstanceType: str
        :param _DiskType: ckafka集群实例磁盘类型
        :type DiskType: str
        :param _MaxTopicNumber: 当前规格最大Topic数
        :type MaxTopicNumber: int
        :param _MaxPartitionNumber: 当前规格最大Partition数
        :type MaxPartitionNumber: int
        :param _RebalanceTime: 计划升级配置时间
        :type RebalanceTime: str
        :param _PartitionNumber: 实例当前partition数量
        :type PartitionNumber: int
        :param _PublicNetworkChargeType: ckafka集群实例公网带宽类型
        :type PublicNetworkChargeType: str
        :param _PublicNetwork: 公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :type PublicNetwork: int
        :param _ClusterType: ckafka集群实例底层集群类型
        :type ClusterType: str
        :param _Features: 实例功能列表
        :type Features: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._VipList = None
        self._Status = None
        self._Bandwidth = None
        self._DiskSize = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._RenewFlag = None
        self._Healthy = None
        self._HealthyMessage = None
        self._CreateTime = None
        self._ExpireTime = None
        self._IsInternal = None
        self._TopicNum = None
        self._Tags = None
        self._Version = None
        self._ZoneIds = None
        self._Cvm = None
        self._InstanceType = None
        self._DiskType = None
        self._MaxTopicNumber = None
        self._MaxPartitionNumber = None
        self._RebalanceTime = None
        self._PartitionNumber = None
        self._PublicNetworkChargeType = None
        self._PublicNetwork = None
        self._ClusterType = None
        self._Features = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """ckafka集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """访问实例的vip 信息
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """访问实例的端口信息
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VipList(self):
        """虚拟IP列表
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Status(self):
        """实例的状态。0: 创建中，1: 运行中，2: 删除中,  3: 已删除,  5: 隔离中,  7: 升级中,  -1: 创建失败 
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        """实例带宽，单位Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        """ckafka集群实例磁盘大小，单位G
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        """可用区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """vpcId，如果为空，说明是基础网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RenewFlag(self):
        """实例是否续费，int  枚举值：1表示自动续费，2表示明确不自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Healthy(self):
        """实例状态 int：1表示健康，2表示告警，3 表示实例状态异常
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        """实例状态信息
        :rtype: str
        """
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        """实例创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """实例过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsInternal(self):
        """是否为内部客户。值为1 表示内部客户
        :rtype: int
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def TopicNum(self):
        """Topic个数
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def Tags(self):
        """标识tag
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        """kafka版本信息
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneIds(self):
        """跨可用区
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Cvm(self):
        """ckafka售卖类型
        :rtype: int
        """
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        """ckafka集群实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DiskType(self):
        """ckafka集群实例磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MaxTopicNumber(self):
        """当前规格最大Topic数
        :rtype: int
        """
        return self._MaxTopicNumber

    @MaxTopicNumber.setter
    def MaxTopicNumber(self, MaxTopicNumber):
        self._MaxTopicNumber = MaxTopicNumber

    @property
    def MaxPartitionNumber(self):
        """当前规格最大Partition数
        :rtype: int
        """
        return self._MaxPartitionNumber

    @MaxPartitionNumber.setter
    def MaxPartitionNumber(self, MaxPartitionNumber):
        self._MaxPartitionNumber = MaxPartitionNumber

    @property
    def RebalanceTime(self):
        """计划升级配置时间
        :rtype: str
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PartitionNumber(self):
        """实例当前partition数量
        :rtype: int
        """
        return self._PartitionNumber

    @PartitionNumber.setter
    def PartitionNumber(self, PartitionNumber):
        self._PartitionNumber = PartitionNumber

    @property
    def PublicNetworkChargeType(self):
        """ckafka集群实例公网带宽类型
        :rtype: str
        """
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetwork(self):
        """公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def ClusterType(self):
        """ckafka集群实例底层集群类型
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Features(self):
        """实例功能列表
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Status = params.get("Status")
        self._Bandwidth = params.get("Bandwidth")
        self._DiskSize = params.get("DiskSize")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._RenewFlag = params.get("RenewFlag")
        self._Healthy = params.get("Healthy")
        self._HealthyMessage = params.get("HealthyMessage")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._IsInternal = params.get("IsInternal")
        self._TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Version = params.get("Version")
        self._ZoneIds = params.get("ZoneIds")
        self._Cvm = params.get("Cvm")
        self._InstanceType = params.get("InstanceType")
        self._DiskType = params.get("DiskType")
        self._MaxTopicNumber = params.get("MaxTopicNumber")
        self._MaxPartitionNumber = params.get("MaxPartitionNumber")
        self._RebalanceTime = params.get("RebalanceTime")
        self._PartitionNumber = params.get("PartitionNumber")
        self._PublicNetworkChargeType = params.get("PublicNetworkChargeType")
        self._PublicNetwork = params.get("PublicNetwork")
        self._ClusterType = params.get("ClusterType")
        self._Features = params.get("Features")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetailResponse(AbstractModel):
    """实例详情返回结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例总数
        :type TotalCount: int
        :param _InstanceList: 符合条件的实例详情列表
        :type InstanceList: list of InstanceDetail
        """
        self._TotalCount = None
        self._InstanceList = None

    @property
    def TotalCount(self):
        """符合条件的实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """符合条件的实例详情列表
        :rtype: list of InstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceQuotaConfigResp(AbstractModel):
    """实例 / topic 维度限流策略

    """

    def __init__(self):
        r"""
        :param _QuotaProducerByteRate: 生产限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: 消费限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaConsumerByteRate: int
        """
        self._QuotaProducerByteRate = None
        self._QuotaConsumerByteRate = None

    @property
    def QuotaProducerByteRate(self):
        """生产限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        """消费限流大小，单位 MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate


    def _deserialize(self, params):
        self._QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self._QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceResponse(AbstractModel):
    """聚合的实例状态返回结果

    """

    def __init__(self):
        r"""
        :param _InstanceList: 符合条件的实例列表
        :type InstanceList: list of Instance
        :param _TotalCount: 符合条件的结果总数
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        """符合条件的实例列表
        :rtype: list of Instance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """符合条件的结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceScalingDownRequest(AbstractModel):
    """InstanceScalingDown请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _UpgradeStrategy: 缩容模式  1:稳定变配 
2.高速变配
        :type UpgradeStrategy: int
        :param _DiskSize: 磁盘大小 单位 GB
        :type DiskSize: int
        :param _BandWidth: 峰值带宽 单位 MB/s
        :type BandWidth: int
        :param _Partition: 分区上限
        :type Partition: int
        """
        self._InstanceId = None
        self._UpgradeStrategy = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeStrategy(self):
        """缩容模式  1:稳定变配 
2.高速变配
        :rtype: int
        """
        return self._UpgradeStrategy

    @UpgradeStrategy.setter
    def UpgradeStrategy(self, UpgradeStrategy):
        self._UpgradeStrategy = UpgradeStrategy

    @property
    def DiskSize(self):
        """磁盘大小 单位 GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        """峰值带宽 单位 MB/s
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        """分区上限
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeStrategy = params.get("UpgradeStrategy")
        self._DiskSize = params.get("DiskSize")
        self._BandWidth = params.get("BandWidth")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceScalingDownResponse(AbstractModel):
    """InstanceScalingDown返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ScalingDownResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ScalingDownResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ScalingDownResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class JgwOperateResponse(AbstractModel):
    """操作型结果返回值

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param _ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param _Data: 操作型返回的Data数据,可能有flowId等
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        """返回的code，0为正常，非0为错误
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """成功消息
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """操作型返回的Data数据,可能有flowId等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = OperateResponseData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonPathReplaceParam(AbstractModel):
    """数据处理——Value处理参数——Jsonpath替换参数

    """

    def __init__(self):
        r"""
        :param _OldValue: 被替换值，Jsonpath表达式
        :type OldValue: str
        :param _NewValue: 替换值，Jsonpath表达式或字符串
        :type NewValue: str
        """
        self._OldValue = None
        self._NewValue = None

    @property
    def OldValue(self):
        """被替换值，Jsonpath表达式
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        """替换值，Jsonpath表达式或字符串
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVParam(AbstractModel):
    """key-value二次解析

    """

    def __init__(self):
        r"""
        :param _Delimiter: 分隔符
        :type Delimiter: str
        :param _Regex: key-value二次解析分隔符
        :type Regex: str
        :param _KeepOriginalKey: 保留源Key，默认为false不保留
        :type KeepOriginalKey: str
        """
        self._Delimiter = None
        self._Regex = None
        self._KeepOriginalKey = None

    @property
    def Delimiter(self):
        """分隔符
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def Regex(self):
        """key-value二次解析分隔符
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def KeepOriginalKey(self):
        """保留源Key，默认为false不保留
        :rtype: str
        """
        return self._KeepOriginalKey

    @KeepOriginalKey.setter
    def KeepOriginalKey(self, KeepOriginalKey):
        self._KeepOriginalKey = KeepOriginalKey


    def _deserialize(self, params):
        self._Delimiter = params.get("Delimiter")
        self._Regex = params.get("Regex")
        self._KeepOriginalKey = params.get("KeepOriginalKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaConnectParam(AbstractModel):
    """Kafka连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: Kafka连接源的实例资源, 非自建时必填，NetworkType=VPC时传clb实例id
        :type Resource: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _BrokerAddress: Kafka连接的broker地址, NetworkType=PUBLIC公网时必填
        :type BrokerAddress: str
        :param _Region: CKafka连接源的实例资源地域, 跨地域时必填
        :type Region: str
        """
        self._Resource = None
        self._SelfBuilt = None
        self._IsUpdate = None
        self._BrokerAddress = None
        self._Region = None

    @property
    def Resource(self):
        """Kafka连接源的实例资源, 非自建时必填，NetworkType=VPC时传clb实例id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        """是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def BrokerAddress(self):
        """Kafka连接的broker地址, NetworkType=PUBLIC公网时必填
        :rtype: str
        """
        return self._BrokerAddress

    @BrokerAddress.setter
    def BrokerAddress(self, BrokerAddress):
        self._BrokerAddress = BrokerAddress

    @property
    def Region(self):
        """CKafka连接源的实例资源地域, 跨地域时必填
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._SelfBuilt = params.get("SelfBuilt")
        self._IsUpdate = params.get("IsUpdate")
        self._BrokerAddress = params.get("BrokerAddress")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaParam(AbstractModel):
    """Ckafka配置

    """

    def __init__(self):
        r"""
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _Resource: ckafka集群实例Id
        :type Resource: str
        :param _Topic: 主题名，多个以“,”分隔
        :type Topic: str
        :param _OffsetType: Offset类型，最开始位置earliest，最新位置latest，时间点位置timestamp
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetType: str
        :param _StartTime: Offset类型为timestamp时必传，传时间戳，精确到秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _ResourceName: 实例资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _ZoneId: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _TopicId: 主题Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _PartitionNum: Topic的分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNum: int
        :param _EnableToleration: 启用容错实例/开启死信队列
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableToleration: bool
        :param _QpsLimit: Qps 限制
        :type QpsLimit: int
        :param _TableMappings: Table到Topic的路由，「分发到多个topic」开关打开时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMappings: list of TableMapping
        :param _UseTableMapping: 「分发到多个topic」开关，默认为false
        :type UseTableMapping: bool
        :param _UseAutoCreateTopic: 使用的Topic是否需要自动创建（目前只支持SOURCE流入任务，如果不使用分发到多个topic，需要在Topic字段填写需要自动创建的topic名）
        :type UseAutoCreateTopic: bool
        :param _CompressionType: 写入Topic时是否进行压缩，不开启填"none"，开启的话，填写"open"。
        :type CompressionType: str
        :param _MsgMultiple: 源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
        :type MsgMultiple: int
        :param _ConnectorSyncType: 数据同步专用参数, 正常数据处理可为空, 实例级别同步: 仅同步元数据填写"META_SYNC_INSTANCE_TYPE", 同步元数据及全部topic内消息的填写"META_AND_DATA_SYNC_INSTANCE_TYPE"; topic级别同步: 选中的源和目标topic中的消息(需要目标实例也包含该topic)填写"DATA_SYNC_TYPE"
        :type ConnectorSyncType: str
        :param _KeepPartition: 数据同步专用参数, 当通过时,希望下游的消息写入分区与上游的一致,则填true,但下游分区小于上游时,会报错; 不需要一致则为false, 默认为false
        :type KeepPartition: bool
        :param _TopicRegularExpression: 正则匹配Topic列表
        :type TopicRegularExpression: str
        """
        self._SelfBuilt = None
        self._Resource = None
        self._Topic = None
        self._OffsetType = None
        self._StartTime = None
        self._ResourceName = None
        self._ZoneId = None
        self._TopicId = None
        self._PartitionNum = None
        self._EnableToleration = None
        self._QpsLimit = None
        self._TableMappings = None
        self._UseTableMapping = None
        self._UseAutoCreateTopic = None
        self._CompressionType = None
        self._MsgMultiple = None
        self._ConnectorSyncType = None
        self._KeepPartition = None
        self._TopicRegularExpression = None

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def Resource(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Topic(self):
        """主题名，多个以“,”分隔
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def OffsetType(self):
        """Offset类型，最开始位置earliest，最新位置latest，时间点位置timestamp
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OffsetType

    @OffsetType.setter
    def OffsetType(self, OffsetType):
        self._OffsetType = OffsetType

    @property
    def StartTime(self):
        """Offset类型为timestamp时必传，传时间戳，精确到秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ResourceName(self):
        """实例资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ZoneId(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TopicId(self):
        """主题Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """Topic的分区数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableToleration(self):
        """启用容错实例/开启死信队列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableToleration

    @EnableToleration.setter
    def EnableToleration(self, EnableToleration):
        self._EnableToleration = EnableToleration

    @property
    def QpsLimit(self):
        """Qps 限制
        :rtype: int
        """
        return self._QpsLimit

    @QpsLimit.setter
    def QpsLimit(self, QpsLimit):
        self._QpsLimit = QpsLimit

    @property
    def TableMappings(self):
        """Table到Topic的路由，「分发到多个topic」开关打开时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TableMapping
        """
        return self._TableMappings

    @TableMappings.setter
    def TableMappings(self, TableMappings):
        self._TableMappings = TableMappings

    @property
    def UseTableMapping(self):
        """「分发到多个topic」开关，默认为false
        :rtype: bool
        """
        return self._UseTableMapping

    @UseTableMapping.setter
    def UseTableMapping(self, UseTableMapping):
        self._UseTableMapping = UseTableMapping

    @property
    def UseAutoCreateTopic(self):
        """使用的Topic是否需要自动创建（目前只支持SOURCE流入任务，如果不使用分发到多个topic，需要在Topic字段填写需要自动创建的topic名）
        :rtype: bool
        """
        return self._UseAutoCreateTopic

    @UseAutoCreateTopic.setter
    def UseAutoCreateTopic(self, UseAutoCreateTopic):
        self._UseAutoCreateTopic = UseAutoCreateTopic

    @property
    def CompressionType(self):
        """写入Topic时是否进行压缩，不开启填"none"，开启的话，填写"open"。
        :rtype: str
        """
        return self._CompressionType

    @CompressionType.setter
    def CompressionType(self, CompressionType):
        self._CompressionType = CompressionType

    @property
    def MsgMultiple(self):
        """源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
        :rtype: int
        """
        return self._MsgMultiple

    @MsgMultiple.setter
    def MsgMultiple(self, MsgMultiple):
        self._MsgMultiple = MsgMultiple

    @property
    def ConnectorSyncType(self):
        """数据同步专用参数, 正常数据处理可为空, 实例级别同步: 仅同步元数据填写"META_SYNC_INSTANCE_TYPE", 同步元数据及全部topic内消息的填写"META_AND_DATA_SYNC_INSTANCE_TYPE"; topic级别同步: 选中的源和目标topic中的消息(需要目标实例也包含该topic)填写"DATA_SYNC_TYPE"
        :rtype: str
        """
        return self._ConnectorSyncType

    @ConnectorSyncType.setter
    def ConnectorSyncType(self, ConnectorSyncType):
        self._ConnectorSyncType = ConnectorSyncType

    @property
    def KeepPartition(self):
        """数据同步专用参数, 当通过时,希望下游的消息写入分区与上游的一致,则填true,但下游分区小于上游时,会报错; 不需要一致则为false, 默认为false
        :rtype: bool
        """
        return self._KeepPartition

    @KeepPartition.setter
    def KeepPartition(self, KeepPartition):
        self._KeepPartition = KeepPartition

    @property
    def TopicRegularExpression(self):
        """正则匹配Topic列表
        :rtype: str
        """
        return self._TopicRegularExpression

    @TopicRegularExpression.setter
    def TopicRegularExpression(self, TopicRegularExpression):
        self._TopicRegularExpression = TopicRegularExpression


    def _deserialize(self, params):
        self._SelfBuilt = params.get("SelfBuilt")
        self._Resource = params.get("Resource")
        self._Topic = params.get("Topic")
        self._OffsetType = params.get("OffsetType")
        self._StartTime = params.get("StartTime")
        self._ResourceName = params.get("ResourceName")
        self._ZoneId = params.get("ZoneId")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._EnableToleration = params.get("EnableToleration")
        self._QpsLimit = params.get("QpsLimit")
        if params.get("TableMappings") is not None:
            self._TableMappings = []
            for item in params.get("TableMappings"):
                obj = TableMapping()
                obj._deserialize(item)
                self._TableMappings.append(obj)
        self._UseTableMapping = params.get("UseTableMapping")
        self._UseAutoCreateTopic = params.get("UseAutoCreateTopic")
        self._CompressionType = params.get("CompressionType")
        self._MsgMultiple = params.get("MsgMultiple")
        self._ConnectorSyncType = params.get("ConnectorSyncType")
        self._KeepPartition = params.get("KeepPartition")
        self._TopicRegularExpression = params.get("TopicRegularExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowercaseParam(AbstractModel):
    """小写字符解析

    """


class MapParam(AbstractModel):
    """Map参数

    """

    def __init__(self):
        r"""
        :param _Key: key值
        :type Key: str
        :param _Type: 类型，DEFAULT默认，DATE系统预设-时间戳，CUSTOMIZE自定义，MAPPING映射
        :type Type: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Type = None
        self._Value = None

    @property
    def Key(self):
        """key值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        """类型，DEFAULT默认，DATE系统预设-时间戳，CUSTOMIZE自定义，MAPPING映射
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MariaDBConnectParam(AbstractModel):
    """MariaDB连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: MariaDB的连接port
        :type Port: int
        :param _UserName: MariaDB连接源的用户名
        :type UserName: str
        :param _Password: MariaDB连接源的密码
        :type Password: str
        :param _Resource: MariaDB连接源的实例资源
        :type Resource: str
        :param _ServiceVip: MariaDB连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: MariaDB连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None

    @property
    def Port(self):
        """MariaDB的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """MariaDB连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MariaDB连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """MariaDB连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        """MariaDB连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MariaDB连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MariaDBModifyConnectParam(AbstractModel):
    """MariaDB连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: MariaDB连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: MariaDB的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: MariaDB连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: MariaDB连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: MariaDB连接源的用户名
        :type UserName: str
        :param _Password: MariaDB连接源的密码
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._IsUpdate = None

    @property
    def Resource(self):
        """MariaDB连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """MariaDB的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """MariaDB连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MariaDB连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """MariaDB连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MariaDB连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MariaDBParam(AbstractModel):
    """MariaDB类型入参

    """

    def __init__(self):
        r"""
        :param _Database: MariaDB的数据库名称，"*"为全数据库
        :type Database: str
        :param _Table: MariaDB的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
        :type Table: str
        :param _Resource: 该MariaDB在连接管理内的Id
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only不复制, initial全量)，默认值initial
        :type SnapshotMode: str
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :type KeyColumns: str
        :param _IsTablePrefix: 当Table输入的是前缀时，该项值为true，否则为false
        :type IsTablePrefix: bool
        :param _OutputFormat: 输出格式，DEFAULT、CANAL_1、CANAL_2
        :type OutputFormat: str
        :param _IncludeContentChanges: 如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
        :type IncludeContentChanges: str
        :param _IncludeQuery: 如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
        :type IncludeQuery: bool
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :type RecordWithSchema: bool
        """
        self._Database = None
        self._Table = None
        self._Resource = None
        self._SnapshotMode = None
        self._KeyColumns = None
        self._IsTablePrefix = None
        self._OutputFormat = None
        self._IncludeContentChanges = None
        self._IncludeQuery = None
        self._RecordWithSchema = None

    @property
    def Database(self):
        """MariaDB的数据库名称，"*"为全数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """MariaDB的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        """该MariaDB在连接管理内的Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
        """复制存量信息(schema_only不复制, initial全量)，默认值initial
        :rtype: str
        """
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def KeyColumns(self):
        """格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :rtype: str
        """
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def IsTablePrefix(self):
        """当Table输入的是前缀时，该项值为true，否则为false
        :rtype: bool
        """
        return self._IsTablePrefix

    @IsTablePrefix.setter
    def IsTablePrefix(self, IsTablePrefix):
        self._IsTablePrefix = IsTablePrefix

    @property
    def OutputFormat(self):
        """输出格式，DEFAULT、CANAL_1、CANAL_2
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def IncludeContentChanges(self):
        """如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
        :rtype: str
        """
        return self._IncludeContentChanges

    @IncludeContentChanges.setter
    def IncludeContentChanges(self, IncludeContentChanges):
        self._IncludeContentChanges = IncludeContentChanges

    @property
    def IncludeQuery(self):
        """如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
        :rtype: bool
        """
        return self._IncludeQuery

    @IncludeQuery.setter
    def IncludeQuery(self, IncludeQuery):
        self._IncludeQuery = IncludeQuery

    @property
    def RecordWithSchema(self):
        """如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :rtype: bool
        """
        return self._RecordWithSchema

    @RecordWithSchema.setter
    def RecordWithSchema(self, RecordWithSchema):
        self._RecordWithSchema = RecordWithSchema


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Resource = params.get("Resource")
        self._SnapshotMode = params.get("SnapshotMode")
        self._KeyColumns = params.get("KeyColumns")
        self._IsTablePrefix = params.get("IsTablePrefix")
        self._OutputFormat = params.get("OutputFormat")
        self._IncludeContentChanges = params.get("IncludeContentChanges")
        self._IncludeQuery = params.get("IncludeQuery")
        self._RecordWithSchema = params.get("RecordWithSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRuleRequest(AbstractModel):
    """ModifyAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _RuleName: ACL规则名
        :type RuleName: str
        :param _IsApplied: 修改预设规则时传入,是否应用到新增的Topic
        :type IsApplied: int
        """
        self._InstanceId = None
        self._RuleName = None
        self._IsApplied = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        """ACL规则名
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def IsApplied(self):
        """修改预设规则时传入,是否应用到新增的Topic
        :rtype: int
        """
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._IsApplied = params.get("IsApplied")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAclRuleResponse(AbstractModel):
    """ModifyAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 规则的唯一表示Key
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """规则的唯一表示Key
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyConnectResourceRequest(AbstractModel):
    """ModifyConnectResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 连接源的Id
        :type ResourceId: str
        :param _ResourceName: 连接源名称，为空时不修改
        :type ResourceName: str
        :param _Description: 连接源描述，为空时不修改
        :type Description: str
        :param _Type: 连接源类型，修改数据源参数时，需要与原Type相同，否则编辑数据源无效
        :type Type: str
        :param _DtsConnectParam: Dts配置，Type为DTS时必填
        :type DtsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DtsModifyConnectParam`
        :param _MongoDBConnectParam: MongoDB配置，Type为MONGODB时必填
        :type MongoDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MongoDBModifyConnectParam`
        :param _EsConnectParam: Es配置，Type为ES时必填
        :type EsConnectParam: :class:`tencentcloud.ckafka.v20190819.models.EsModifyConnectParam`
        :param _ClickHouseConnectParam: ClickHouse配置，Type为CLICKHOUSE时必填
        :type ClickHouseConnectParam: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseModifyConnectParam`
        :param _MySQLConnectParam: MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时必填
        :type MySQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MySQLModifyConnectParam`
        :param _PostgreSQLConnectParam: PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
        :type PostgreSQLConnectParam: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLModifyConnectParam`
        :param _MariaDBConnectParam: MariaDB配置，Type为MARIADB时必填
        :type MariaDBConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MariaDBModifyConnectParam`
        :param _SQLServerConnectParam: SQLServer配置，Type为SQLSERVER时必填
        :type SQLServerConnectParam: :class:`tencentcloud.ckafka.v20190819.models.SQLServerModifyConnectParam`
        :param _CtsdbConnectParam: Ctsdb配置，Type为CTSDB
        :type CtsdbConnectParam: :class:`tencentcloud.ckafka.v20190819.models.CtsdbModifyConnectParam`
        :param _DorisConnectParam: Doris配置，Type为DORIS
        :type DorisConnectParam: :class:`tencentcloud.ckafka.v20190819.models.DorisModifyConnectParam`
        :param _KafkaConnectParam: Kafka配置，Type为 KAFKA 时必填
        :type KafkaConnectParam: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        :param _MqttConnectParam: MQTT配置，Type为 MQTT 时必填
        :type MqttConnectParam: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        self._ResourceId = None
        self._ResourceName = None
        self._Description = None
        self._Type = None
        self._DtsConnectParam = None
        self._MongoDBConnectParam = None
        self._EsConnectParam = None
        self._ClickHouseConnectParam = None
        self._MySQLConnectParam = None
        self._PostgreSQLConnectParam = None
        self._MariaDBConnectParam = None
        self._SQLServerConnectParam = None
        self._CtsdbConnectParam = None
        self._DorisConnectParam = None
        self._KafkaConnectParam = None
        self._MqttConnectParam = None

    @property
    def ResourceId(self):
        """连接源的Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """连接源名称，为空时不修改
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        """连接源描述，为空时不修改
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        """连接源类型，修改数据源参数时，需要与原Type相同，否则编辑数据源无效
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DtsConnectParam(self):
        """Dts配置，Type为DTS时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DtsModifyConnectParam`
        """
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        """MongoDB配置，Type为MONGODB时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MongoDBModifyConnectParam`
        """
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        """Es配置，Type为ES时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.EsModifyConnectParam`
        """
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        """ClickHouse配置，Type为CLICKHOUSE时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ClickHouseModifyConnectParam`
        """
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        """MySQL配置，Type为MYSQL或TDSQL_C_MYSQL时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MySQLModifyConnectParam`
        """
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        """PostgreSQL配置，Type为POSTGRESQL或TDSQL_C_POSTGRESQL时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.PostgreSQLModifyConnectParam`
        """
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        """MariaDB配置，Type为MARIADB时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MariaDBModifyConnectParam`
        """
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        """SQLServer配置，Type为SQLSERVER时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SQLServerModifyConnectParam`
        """
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        """Ctsdb配置，Type为CTSDB
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CtsdbModifyConnectParam`
        """
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        """Doris配置，Type为DORIS
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DorisModifyConnectParam`
        """
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        """Kafka配置，Type为 KAFKA 时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KafkaConnectParam`
        """
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
        """MQTT配置，Type为 MQTT 时必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.MqttConnectParam`
        """
        return self._MqttConnectParam

    @MqttConnectParam.setter
    def MqttConnectParam(self, MqttConnectParam):
        self._MqttConnectParam = MqttConnectParam


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("DtsConnectParam") is not None:
            self._DtsConnectParam = DtsModifyConnectParam()
            self._DtsConnectParam._deserialize(params.get("DtsConnectParam"))
        if params.get("MongoDBConnectParam") is not None:
            self._MongoDBConnectParam = MongoDBModifyConnectParam()
            self._MongoDBConnectParam._deserialize(params.get("MongoDBConnectParam"))
        if params.get("EsConnectParam") is not None:
            self._EsConnectParam = EsModifyConnectParam()
            self._EsConnectParam._deserialize(params.get("EsConnectParam"))
        if params.get("ClickHouseConnectParam") is not None:
            self._ClickHouseConnectParam = ClickHouseModifyConnectParam()
            self._ClickHouseConnectParam._deserialize(params.get("ClickHouseConnectParam"))
        if params.get("MySQLConnectParam") is not None:
            self._MySQLConnectParam = MySQLModifyConnectParam()
            self._MySQLConnectParam._deserialize(params.get("MySQLConnectParam"))
        if params.get("PostgreSQLConnectParam") is not None:
            self._PostgreSQLConnectParam = PostgreSQLModifyConnectParam()
            self._PostgreSQLConnectParam._deserialize(params.get("PostgreSQLConnectParam"))
        if params.get("MariaDBConnectParam") is not None:
            self._MariaDBConnectParam = MariaDBModifyConnectParam()
            self._MariaDBConnectParam._deserialize(params.get("MariaDBConnectParam"))
        if params.get("SQLServerConnectParam") is not None:
            self._SQLServerConnectParam = SQLServerModifyConnectParam()
            self._SQLServerConnectParam._deserialize(params.get("SQLServerConnectParam"))
        if params.get("CtsdbConnectParam") is not None:
            self._CtsdbConnectParam = CtsdbModifyConnectParam()
            self._CtsdbConnectParam._deserialize(params.get("CtsdbConnectParam"))
        if params.get("DorisConnectParam") is not None:
            self._DorisConnectParam = DorisModifyConnectParam()
            self._DorisConnectParam._deserialize(params.get("DorisConnectParam"))
        if params.get("KafkaConnectParam") is not None:
            self._KafkaConnectParam = KafkaConnectParam()
            self._KafkaConnectParam._deserialize(params.get("KafkaConnectParam"))
        if params.get("MqttConnectParam") is not None:
            self._MqttConnectParam = MqttConnectParam()
            self._MqttConnectParam._deserialize(params.get("MqttConnectParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConnectResourceResponse(AbstractModel):
    """ModifyConnectResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 连接源的Id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """连接源的Id
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ConnectResourceResourceIdResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ConnectResourceResourceIdResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDatahubTaskRequest(AbstractModel):
    """ModifyDatahubTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        """
        self._TaskId = None
        self._TaskName = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatahubTaskResponse(AbstractModel):
    """ModifyDatahubTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 任务id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """任务id
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DatahubTaskIdRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDatahubTopicRequest(AbstractModel):
    """ModifyDatahubTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 弹性topic名称
        :type Name: str
        :param _RetentionMs: 消息保留时间，单位：ms，当前最小值为60000ms。
        :type RetentionMs: int
        :param _Note: 主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :type Note: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._Name = None
        self._RetentionMs = None
        self._Note = None
        self._Tags = None

    @property
    def Name(self):
        """弹性topic名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RetentionMs(self):
        """消息保留时间，单位：ms，当前最小值为60000ms。
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        """主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RetentionMs = params.get("RetentionMs")
        self._Note = params.get("Note")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatahubTopicResponse(AbstractModel):
    """ModifyDatahubTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果集
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _Group: 消费分组名称
        :type Group: str
        :param _Strategy: 重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置
        :type Strategy: int
        :param _Topics: 需要重置的主题名列表， 不填表示全部
        :type Topics: list of str
        :param _Shift: 当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest
        :type Shift: int
        :param _ShiftTimestamp: 单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。
        :type ShiftTimestamp: int
        :param _Offset: 需要重新设置的offset位置。当strategy为2，必须包含该字段。
        :type Offset: int
        :param _Partitions: 需要重新设置的partition的列表，如果没有指定Topics参数。则重置全部topics的对应的Partition列表里的partition。指定Topics时则重置指定的topic列表的对应的Partitions列表的partition。
        :type Partitions: list of int
        """
        self._InstanceId = None
        self._Group = None
        self._Strategy = None
        self._Topics = None
        self._Shift = None
        self._ShiftTimestamp = None
        self._Offset = None
        self._Partitions = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        """消费分组名称
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Strategy(self):
        """重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Topics(self):
        """需要重置的主题名列表， 不填表示全部
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Shift(self):
        """当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest
        :rtype: int
        """
        return self._Shift

    @Shift.setter
    def Shift(self, Shift):
        self._Shift = Shift

    @property
    def ShiftTimestamp(self):
        """单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。
        :rtype: int
        """
        return self._ShiftTimestamp

    @ShiftTimestamp.setter
    def ShiftTimestamp(self, ShiftTimestamp):
        self._ShiftTimestamp = ShiftTimestamp

    @property
    def Offset(self):
        """需要重新设置的offset位置。当strategy为2，必须包含该字段。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Partitions(self):
        """需要重新设置的partition的列表，如果没有指定Topics参数。则重置全部topics的对应的Partition列表里的partition。指定Topics时则重置指定的topic列表的对应的Partitions列表的partition。
        :rtype: list of int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        self._Strategy = params.get("Strategy")
        self._Topics = params.get("Topics")
        self._Shift = params.get("Shift")
        self._ShiftTimestamp = params.get("ShiftTimestamp")
        self._Offset = params.get("Offset")
        self._Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """修改实例属性的配置对象

    """

    def __init__(self):
        r"""
        :param _AutoCreateTopicEnable: 自动创建 true 表示开启，false 表示不开启
        :type AutoCreateTopicEnable: bool
        :param _DefaultNumPartitions: 可选，如果auto.create.topic.enable设置为true没有设置该值时，默认设置为3
        :type DefaultNumPartitions: int
        :param _DefaultReplicationFactor: 如果auto.create.topic.enable设置为true没有指定该值时默认设置为2
        :type DefaultReplicationFactor: int
        """
        self._AutoCreateTopicEnable = None
        self._DefaultNumPartitions = None
        self._DefaultReplicationFactor = None

    @property
    def AutoCreateTopicEnable(self):
        """自动创建 true 表示开启，false 表示不开启
        :rtype: bool
        """
        return self._AutoCreateTopicEnable

    @AutoCreateTopicEnable.setter
    def AutoCreateTopicEnable(self, AutoCreateTopicEnable):
        self._AutoCreateTopicEnable = AutoCreateTopicEnable

    @property
    def DefaultNumPartitions(self):
        """可选，如果auto.create.topic.enable设置为true没有设置该值时，默认设置为3
        :rtype: int
        """
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
        """如果auto.create.topic.enable设置为true没有指定该值时默认设置为2
        :rtype: int
        """
        return self._DefaultReplicationFactor

    @DefaultReplicationFactor.setter
    def DefaultReplicationFactor(self, DefaultReplicationFactor):
        self._DefaultReplicationFactor = DefaultReplicationFactor


    def _deserialize(self, params):
        self._AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self._DefaultNumPartitions = params.get("DefaultNumPartitions")
        self._DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _MsgRetentionTime: 实例日志的最长保留时间，单位分钟，最大90天，0代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param _InstanceName: ckafka集群实例Name
        :type InstanceName: str
        :param _Config: 实例配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param _DynamicRetentionConfig: 动态消息保留策略配置
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _RebalanceTime: 用于修改升级版本或升配定时任务的执行时间，Unix时间戳，精确到秒
        :type RebalanceTime: int
        :param _PublicNetwork: 公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :type PublicNetwork: int
        :param _DynamicDiskConfig: 动态硬盘扩容策略配置
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _MaxMessageByte: 实例级别单条消息大小（单位byte)  最大 12582912(不包含)  最小1024(不包含)
        :type MaxMessageByte: int
        :param _UncleanLeaderElectionEnable: 集群topic默认 unclean.leader.election.enable配置: 1 开启  0 关闭
        :type UncleanLeaderElectionEnable: int
        """
        self._InstanceId = None
        self._MsgRetentionTime = None
        self._InstanceName = None
        self._Config = None
        self._DynamicRetentionConfig = None
        self._RebalanceTime = None
        self._PublicNetwork = None
        self._DynamicDiskConfig = None
        self._MaxMessageByte = None
        self._UncleanLeaderElectionEnable = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MsgRetentionTime(self):
        """实例日志的最长保留时间，单位分钟，最大90天，0代表不开启日志保留时间回收策略
        :rtype: int
        """
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def InstanceName(self):
        """ckafka集群实例Name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Config(self):
        """实例配置
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def DynamicRetentionConfig(self):
        """动态消息保留策略配置
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        return self._DynamicRetentionConfig

    @DynamicRetentionConfig.setter
    def DynamicRetentionConfig(self, DynamicRetentionConfig):
        self._DynamicRetentionConfig = DynamicRetentionConfig

    @property
    def RebalanceTime(self):
        """用于修改升级版本或升配定时任务的执行时间，Unix时间戳，精确到秒
        :rtype: int
        """
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PublicNetwork(self):
        """公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :rtype: int
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DynamicDiskConfig(self):
        warnings.warn("parameter `DynamicDiskConfig` is deprecated", DeprecationWarning) 

        """动态硬盘扩容策略配置
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        """
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        warnings.warn("parameter `DynamicDiskConfig` is deprecated", DeprecationWarning) 

        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def MaxMessageByte(self):
        """实例级别单条消息大小（单位byte)  最大 12582912(不包含)  最小1024(不包含)
        :rtype: int
        """
        return self._MaxMessageByte

    @MaxMessageByte.setter
    def MaxMessageByte(self, MaxMessageByte):
        self._MaxMessageByte = MaxMessageByte

    @property
    def UncleanLeaderElectionEnable(self):
        """集群topic默认 unclean.leader.election.enable配置: 1 开启  0 关闭
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MsgRetentionTime = params.get("MsgRetentionTime")
        self._InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self._Config = ModifyInstanceAttributesConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("DynamicRetentionConfig") is not None:
            self._DynamicRetentionConfig = DynamicRetentionTime()
            self._DynamicRetentionConfig._deserialize(params.get("DynamicRetentionConfig"))
        self._RebalanceTime = params.get("RebalanceTime")
        self._PublicNetwork = params.get("PublicNetwork")
        if params.get("DynamicDiskConfig") is not None:
            self._DynamicDiskConfig = DynamicDiskConfig()
            self._DynamicDiskConfig._deserialize(params.get("DynamicDiskConfig"))
        self._MaxMessageByte = params.get("MaxMessageByte")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyInstancePreRequest(AbstractModel):
    """ModifyInstancePre请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _DiskSize: 预计磁盘，根据磁盘步长，规格向上调整。
        :type DiskSize: int
        :param _BandWidth: 预计带宽，根据带宽步长，规格向上调整。
        :type BandWidth: int
        :param _Partition: 预计分区，根据带宽步长，规格向上调整。
        :type Partition: int
        """
        self._InstanceId = None
        self._DiskSize = None
        self._BandWidth = None
        self._Partition = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskSize(self):
        """预计磁盘，根据磁盘步长，规格向上调整。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        """预计带宽，根据带宽步长，规格向上调整。
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        """预计分区，根据带宽步长，规格向上调整。
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskSize = params.get("DiskSize")
        self._BandWidth = params.get("BandWidth")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePreResponse(AbstractModel):
    """ModifyInstancePre返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 变更预付费实例配置返回结构
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """变更预付费实例配置返回结构
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CreateInstancePreResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Name: 用户名称
        :type Name: str
        :param _Password: 用户当前密码
        :type Password: str
        :param _PasswordNew: 用户新密码
        :type PasswordNew: str
        """
        self._InstanceId = None
        self._Name = None
        self._Password = None
        self._PasswordNew = None

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
    def Name(self):
        """用户名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """用户当前密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordNew(self):
        """用户新密码
        :rtype: str
        """
        return self._PasswordNew

    @PasswordNew.setter
    def PasswordNew(self, PasswordNew):
        self._PasswordNew = PasswordNew


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._PasswordNew = params.get("PasswordNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyRoutineMaintenanceTaskRequest(AbstractModel):
    """ModifyRoutineMaintenanceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _MaintenanceType: 自动化运维类别
        :type MaintenanceType: str
        :param _MaintenanceSubtype: INSTANCE_STORAGE_CAPACITY(磁盘自动扩容)/MESSAGE_RETENTION_PERIOD(磁盘动态消息保留策略)
        :type MaintenanceSubtype: str
        :param _TopicName: 主题名
        :type TopicName: str
        :param _ConfigureThreshold: 任务触发阈值
        :type ConfigureThreshold: int
        :param _ConfigureStepSize: 任务调整步长
        :type ConfigureStepSize: int
        :param _ConfigureLimit: 任务调整上限
        :type ConfigureLimit: int
        :param _PlannedTime: 任务预期触发时间，存储从当日 0AM 开始偏移的秒数
        :type PlannedTime: int
        :param _ExtraConfig: 任务额外信息
        :type ExtraConfig: str
        :param _Status: 任务状态
        :type Status: int
        :param _Week: 执行week day
        :type Week: str
        """
        self._InstanceId = None
        self._MaintenanceType = None
        self._MaintenanceSubtype = None
        self._TopicName = None
        self._ConfigureThreshold = None
        self._ConfigureStepSize = None
        self._ConfigureLimit = None
        self._PlannedTime = None
        self._ExtraConfig = None
        self._Status = None
        self._Week = None

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
    def MaintenanceType(self):
        """自动化运维类别
        :rtype: str
        """
        return self._MaintenanceType

    @MaintenanceType.setter
    def MaintenanceType(self, MaintenanceType):
        self._MaintenanceType = MaintenanceType

    @property
    def MaintenanceSubtype(self):
        """INSTANCE_STORAGE_CAPACITY(磁盘自动扩容)/MESSAGE_RETENTION_PERIOD(磁盘动态消息保留策略)
        :rtype: str
        """
        return self._MaintenanceSubtype

    @MaintenanceSubtype.setter
    def MaintenanceSubtype(self, MaintenanceSubtype):
        self._MaintenanceSubtype = MaintenanceSubtype

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ConfigureThreshold(self):
        """任务触发阈值
        :rtype: int
        """
        return self._ConfigureThreshold

    @ConfigureThreshold.setter
    def ConfigureThreshold(self, ConfigureThreshold):
        self._ConfigureThreshold = ConfigureThreshold

    @property
    def ConfigureStepSize(self):
        """任务调整步长
        :rtype: int
        """
        return self._ConfigureStepSize

    @ConfigureStepSize.setter
    def ConfigureStepSize(self, ConfigureStepSize):
        self._ConfigureStepSize = ConfigureStepSize

    @property
    def ConfigureLimit(self):
        """任务调整上限
        :rtype: int
        """
        return self._ConfigureLimit

    @ConfigureLimit.setter
    def ConfigureLimit(self, ConfigureLimit):
        self._ConfigureLimit = ConfigureLimit

    @property
    def PlannedTime(self):
        """任务预期触发时间，存储从当日 0AM 开始偏移的秒数
        :rtype: int
        """
        return self._PlannedTime

    @PlannedTime.setter
    def PlannedTime(self, PlannedTime):
        self._PlannedTime = PlannedTime

    @property
    def ExtraConfig(self):
        """任务额外信息
        :rtype: str
        """
        return self._ExtraConfig

    @ExtraConfig.setter
    def ExtraConfig(self, ExtraConfig):
        self._ExtraConfig = ExtraConfig

    @property
    def Status(self):
        """任务状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Week(self):
        """执行week day
        :rtype: str
        """
        return self._Week

    @Week.setter
    def Week(self, Week):
        self._Week = Week


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaintenanceType = params.get("MaintenanceType")
        self._MaintenanceSubtype = params.get("MaintenanceSubtype")
        self._TopicName = params.get("TopicName")
        self._ConfigureThreshold = params.get("ConfigureThreshold")
        self._ConfigureStepSize = params.get("ConfigureStepSize")
        self._ConfigureLimit = params.get("ConfigureLimit")
        self._PlannedTime = params.get("PlannedTime")
        self._ExtraConfig = params.get("ExtraConfig")
        self._Status = params.get("Status")
        self._Week = params.get("Week")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoutineMaintenanceTaskResponse(AbstractModel):
    """ModifyRoutineMaintenanceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        :param _Note: 主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :type Note: str
        :param _EnableWhiteList: IP 白名单开关，1：打开；0：关闭。
        :type EnableWhiteList: int
        :param _MinInsyncReplicas: 默认为1。
        :type MinInsyncReplicas: int
        :param _UncleanLeaderElectionEnable: 默认为 0，0：false；1：true。
        :type UncleanLeaderElectionEnable: int
        :param _RetentionMs: 消息保留时间，单位：ms，当前最小值为60000ms。
        :type RetentionMs: int
        :param _MaxMessageBytes: 主题消息最大值，单位为 Byte，最大值为12582912Byte（即12MB）。
        :type MaxMessageBytes: int
        :param _SegmentMs: Segment 分片滚动的时长，单位：ms，当前最小为300000ms。
        :type SegmentMs: int
        :param _CleanUpPolicy: 消息删除策略，可以选择delete 或者compact
        :type CleanUpPolicy: str
        :param _IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选
        :type IpWhiteList: list of str
        :param _EnableAclRule: 预设ACL规则, 1:打开  0:关闭，默认不打开
        :type EnableAclRule: int
        :param _AclRuleName: ACL规则名
        :type AclRuleName: str
        :param _RetentionBytes: 可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :type RetentionBytes: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _QuotaProducerByteRate: 生产限流，单位 MB/s
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: 消费限流，单位 MB/s
        :type QuotaConsumerByteRate: int
        :param _ReplicaNum: topic副本数  最小值 1,最大值 3
        :type ReplicaNum: int
        """
        self._InstanceId = None
        self._TopicName = None
        self._Note = None
        self._EnableWhiteList = None
        self._MinInsyncReplicas = None
        self._UncleanLeaderElectionEnable = None
        self._RetentionMs = None
        self._MaxMessageBytes = None
        self._SegmentMs = None
        self._CleanUpPolicy = None
        self._IpWhiteList = None
        self._EnableAclRule = None
        self._AclRuleName = None
        self._RetentionBytes = None
        self._Tags = None
        self._QuotaProducerByteRate = None
        self._QuotaConsumerByteRate = None
        self._ReplicaNum = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        """主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def EnableWhiteList(self):
        """IP 白名单开关，1：打开；0：关闭。
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def MinInsyncReplicas(self):
        """默认为1。
        :rtype: int
        """
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        """默认为 0，0：false；1：true。
        :rtype: int
        """
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        """消息保留时间，单位：ms，当前最小值为60000ms。
        :rtype: int
        """
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def MaxMessageBytes(self):
        """主题消息最大值，单位为 Byte，最大值为12582912Byte（即12MB）。
        :rtype: int
        """
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def SegmentMs(self):
        """Segment 分片滚动的时长，单位：ms，当前最小为300000ms。
        :rtype: int
        """
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def CleanUpPolicy(self):
        """消息删除策略，可以选择delete 或者compact
        :rtype: str
        """
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def IpWhiteList(self):
        """Ip白名单列表，配额限制，enableWhileList=1时必选
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def EnableAclRule(self):
        """预设ACL规则, 1:打开  0:关闭，默认不打开
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        """ACL规则名
        :rtype: str
        """
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        """可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :rtype: int
        """
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def QuotaProducerByteRate(self):
        """生产限流，单位 MB/s
        :rtype: int
        """
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        """消费限流，单位 MB/s
        :rtype: int
        """
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate

    @property
    def ReplicaNum(self):
        """topic副本数  最小值 1,最大值 3
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Note = params.get("Note")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._RetentionMs = params.get("RetentionMs")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._SegmentMs = params.get("SegmentMs")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._IpWhiteList = params.get("IpWhiteList")
        self._EnableAclRule = params.get("EnableAclRule")
        self._AclRuleName = params.get("AclRuleName")
        self._RetentionBytes = params.get("RetentionBytes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._QuotaProducerByteRate = params.get("QuotaProducerByteRate")
        self._QuotaConsumerByteRate = params.get("QuotaConsumerByteRate")
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = JgwOperateResponse()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class MongoDBConnectParam(AbstractModel):
    """MongoDB连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: MongoDB的连接port
        :type Port: int
        :param _UserName: MongoDB连接源的用户名
        :type UserName: str
        :param _Password: MongoDB连接源的密码
        :type Password: str
        :param _Resource: MongoDB连接源的实例资源
        :type Resource: str
        :param _SelfBuilt: MongoDB连接源是否为自建集群
        :type SelfBuilt: bool
        :param _ServiceVip: MongoDB连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: MongoDB连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._SelfBuilt = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None

    @property
    def Port(self):
        """MongoDB的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """MongoDB连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MongoDB连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """MongoDB连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        """MongoDB连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        """MongoDB连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MongoDB连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._SelfBuilt = params.get("SelfBuilt")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MongoDBModifyConnectParam(AbstractModel):
    """MongoDB修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: MongoDB连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: MongoDB的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: MongoDB连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: MongoDB连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: MongoDB连接源的用户名
        :type UserName: str
        :param _Password: MongoDB连接源的密码
        :type Password: str
        :param _SelfBuilt: MongoDB连接源是否为自建集群【不支持修改】
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._SelfBuilt = None
        self._IsUpdate = None

    @property
    def Resource(self):
        """MongoDB连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """MongoDB的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """MongoDB连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MongoDB连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """MongoDB连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MongoDB连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        """MongoDB连接源是否为自建集群【不支持修改】
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._SelfBuilt = params.get("SelfBuilt")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MongoDBParam(AbstractModel):
    """MongoDB类型入参

    """

    def __init__(self):
        r"""
        :param _Database: MongoDB的数据库名称
        :type Database: str
        :param _Collection: MongoDB的集群
        :type Collection: str
        :param _CopyExisting: 是否复制存量数据，默认传参true
        :type CopyExisting: bool
        :param _Resource: 实例资源
        :type Resource: str
        :param _Ip: MongoDB的连接ip
        :type Ip: str
        :param _Port: MongoDB的连接port
        :type Port: int
        :param _UserName: MongoDB数据库用户名
        :type UserName: str
        :param _Password: MongoDB数据库密码
        :type Password: str
        :param _ListeningEvent: 监听事件类型，为空时表示全选。取值包括insert,update,replace,delete,invalidate,drop,dropdatabase,rename，多个类型间使用,逗号分隔
        :type ListeningEvent: str
        :param _ReadPreference: 主从优先级，默认主节点
        :type ReadPreference: str
        :param _Pipeline: 聚合管道
        :type Pipeline: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        """
        self._Database = None
        self._Collection = None
        self._CopyExisting = None
        self._Resource = None
        self._Ip = None
        self._Port = None
        self._UserName = None
        self._Password = None
        self._ListeningEvent = None
        self._ReadPreference = None
        self._Pipeline = None
        self._SelfBuilt = None

    @property
    def Database(self):
        """MongoDB的数据库名称
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Collection(self):
        """MongoDB的集群
        :rtype: str
        """
        return self._Collection

    @Collection.setter
    def Collection(self, Collection):
        self._Collection = Collection

    @property
    def CopyExisting(self):
        """是否复制存量数据，默认传参true
        :rtype: bool
        """
        return self._CopyExisting

    @CopyExisting.setter
    def CopyExisting(self, CopyExisting):
        self._CopyExisting = CopyExisting

    @property
    def Resource(self):
        """实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        """MongoDB的连接ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """MongoDB的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """MongoDB数据库用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MongoDB数据库密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ListeningEvent(self):
        """监听事件类型，为空时表示全选。取值包括insert,update,replace,delete,invalidate,drop,dropdatabase,rename，多个类型间使用,逗号分隔
        :rtype: str
        """
        return self._ListeningEvent

    @ListeningEvent.setter
    def ListeningEvent(self, ListeningEvent):
        self._ListeningEvent = ListeningEvent

    @property
    def ReadPreference(self):
        """主从优先级，默认主节点
        :rtype: str
        """
        return self._ReadPreference

    @ReadPreference.setter
    def ReadPreference(self, ReadPreference):
        self._ReadPreference = ReadPreference

    @property
    def Pipeline(self):
        """聚合管道
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Collection = params.get("Collection")
        self._CopyExisting = params.get("CopyExisting")
        self._Resource = params.get("Resource")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._ListeningEvent = params.get("ListeningEvent")
        self._ReadPreference = params.get("ReadPreference")
        self._Pipeline = params.get("Pipeline")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MqttConnectParam(AbstractModel):
    """MQTT连接源参数

    """

    def __init__(self):
        r"""
        :param _UserName: MQTT连接源的用户名
        :type UserName: str
        :param _Password: MQTT连接源的密码
        :type Password: str
        :param _Resource: MQTT连接源的实例资源
        :type Resource: str
        :param _UniqVpcId: MQTT Instance vpc-id
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Dip任务
        :type IsUpdate: bool
        :param _Region: MQTT连接源的实例资源地域, 跨地域时必填
        :type Region: str
        """
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._UniqVpcId = None
        self._SelfBuilt = None
        self._IsUpdate = None
        self._Region = None

    @property
    def UserName(self):
        """MQTT连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MQTT连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """MQTT连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def UniqVpcId(self):
        """MQTT Instance vpc-id
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        """是否更新到关联的Dip任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def Region(self):
        """MQTT连接源的实例资源地域, 跨地域时必填
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._UniqVpcId = params.get("UniqVpcId")
        self._SelfBuilt = params.get("SelfBuilt")
        self._IsUpdate = params.get("IsUpdate")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MqttParam(AbstractModel):
    """创建MQTT 为Source的Data Hub Task参数

    """

    def __init__(self):
        r"""
        :param _Topics: 需要同步的MQTT Topic列表, CSV格式
        :type Topics: str
        :param _CleanSession: MQTT clean-session
        :type CleanSession: bool
        :param _Resource: MQTT instance-id
        :type Resource: str
        :param _Ip: MQTT实例VIP
        :type Ip: str
        :param _Port: MQTT VIP 端口
        :type Port: int
        :param _UserName: MQTT实例用户名
        :type UserName: str
        :param _Password: MQTT实例内账户密码
        :type Password: str
        :param _Qos: QoS
        :type Qos: int
        :param _MaxTasks: tasks.max 订阅Topic的并发Task个数, 默认为1; 当设置大于1时, 使用Shared Subscription
        :type MaxTasks: int
        :param _ServiceVip: MQTT 实例的Service VIP
        :type ServiceVip: str
        :param _UniqVpcId: MQTT实例的VPC ID
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群, MQTT只支持非自建集群
        :type SelfBuilt: bool
        """
        self._Topics = None
        self._CleanSession = None
        self._Resource = None
        self._Ip = None
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Qos = None
        self._MaxTasks = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._SelfBuilt = None

    @property
    def Topics(self):
        """需要同步的MQTT Topic列表, CSV格式
        :rtype: str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def CleanSession(self):
        """MQTT clean-session
        :rtype: bool
        """
        return self._CleanSession

    @CleanSession.setter
    def CleanSession(self, CleanSession):
        self._CleanSession = CleanSession

    @property
    def Resource(self):
        """MQTT instance-id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        """MQTT实例VIP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """MQTT VIP 端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """MQTT实例用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MQTT实例内账户密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Qos(self):
        """QoS
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def MaxTasks(self):
        """tasks.max 订阅Topic的并发Task个数, 默认为1; 当设置大于1时, 使用Shared Subscription
        :rtype: int
        """
        return self._MaxTasks

    @MaxTasks.setter
    def MaxTasks(self, MaxTasks):
        self._MaxTasks = MaxTasks

    @property
    def ServiceVip(self):
        """MQTT 实例的Service VIP
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MQTT实例的VPC ID
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
        """是否为自建集群, MQTT只支持非自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Topics = params.get("Topics")
        self._CleanSession = params.get("CleanSession")
        self._Resource = params.get("Resource")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Qos = params.get("Qos")
        self._MaxTasks = params.get("MaxTasks")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLConnectParam(AbstractModel):
    """MySQL连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: MySQL的连接port
        :type Port: int
        :param _UserName: MySQL连接源的用户名
        :type UserName: str
        :param _Password: MySQL连接源的密码
        :type Password: str
        :param _Resource: MySQL连接源的实例资源
        :type Resource: str
        :param _ServiceVip: MySQL连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: MySQL连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _ClusterId: 当type为TDSQL_C_MYSQL时，必填
        :type ClusterId: str
        :param _SelfBuilt: Mysql 连接源是否为自建集群
        :type SelfBuilt: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None
        self._ClusterId = None
        self._SelfBuilt = None

    @property
    def Port(self):
        """MySQL的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """MySQL连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MySQL连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """MySQL连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        """MySQL连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MySQL连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def ClusterId(self):
        """当type为TDSQL_C_MYSQL时，必填
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelfBuilt(self):
        """Mysql 连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        self._ClusterId = params.get("ClusterId")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLModifyConnectParam(AbstractModel):
    """MySQL修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: MySQL连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: MySQL的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: MySQL连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: MySQL连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: MySQL连接源的用户名
        :type UserName: str
        :param _Password: MySQL连接源的密码
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        :param _ClusterId: 当type为TDSQL_C_MYSQL时
        :type ClusterId: str
        :param _SelfBuilt: 是否是自建的集群
        :type SelfBuilt: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._IsUpdate = None
        self._ClusterId = None
        self._SelfBuilt = None

    @property
    def Resource(self):
        """MySQL连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """MySQL的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """MySQL连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """MySQL连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """MySQL连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """MySQL连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def ClusterId(self):
        """当type为TDSQL_C_MYSQL时
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelfBuilt(self):
        """是否是自建的集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._IsUpdate = params.get("IsUpdate")
        self._ClusterId = params.get("ClusterId")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLParam(AbstractModel):
    """MySQL类型入参

    """

    def __init__(self):
        r"""
        :param _Database: MySQL的数据库名称，"*"为全数据库
        :type Database: str
        :param _Table: MySQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"数据库名\\.数据表名"
        :type Table: str
        :param _Resource: 该MySQL在连接管理内的Id
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only不复制, initial全量)，默认值initial
        :type SnapshotMode: str
        :param _DdlTopic: 存放MySQL的Ddl信息的Topic，为空则默认不存放
        :type DdlTopic: str
        :param _DataSourceMonitorMode: "TABLE" 表示读取项为 table，"QUERY" 表示读取项为 query
        :type DataSourceMonitorMode: str
        :param _DataSourceMonitorResource: 当 "DataMonitorMode"="TABLE" 时，传入需要读取的 Table；当 "DataMonitorMode"="QUERY" 时，传入需要读取的查询 sql 语句
        :type DataSourceMonitorResource: str
        :param _DataSourceIncrementMode: "TIMESTAMP" 表示增量列为时间戳类型，"INCREMENT" 表示增量列为自增 id 类型
        :type DataSourceIncrementMode: str
        :param _DataSourceIncrementColumn: 传入需要监听的列名称
        :type DataSourceIncrementColumn: str
        :param _DataSourceStartFrom: "HEAD" 表示复制存量 + 增量数据，"TAIL" 表示只复制增量数据
        :type DataSourceStartFrom: str
        :param _DataTargetInsertMode: "INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
        :type DataTargetInsertMode: str
        :param _DataTargetPrimaryKeyField: 当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
        :type DataTargetPrimaryKeyField: str
        :param _DataTargetRecordMapping: 表与消息间的映射关系
        :type DataTargetRecordMapping: list of RecordMapping
        :param _TopicRegex: 事件路由到特定主题的正则表达式，默认为(.*)
        :type TopicRegex: str
        :param _TopicReplacement: TopicRegex的引用组，指定$1、$2等
        :type TopicReplacement: str
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :type KeyColumns: str
        :param _DropInvalidMessage: Mysql 是否抛弃解析失败的消息，默认为true
        :type DropInvalidMessage: bool
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _OutputFormat: 输出格式，DEFAULT、CANAL_1、CANAL_2
        :type OutputFormat: str
        :param _IsTablePrefix: 当Table输入的是前缀时，该项值为true，否则为false
        :type IsTablePrefix: bool
        :param _IncludeContentChanges: 如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
        :type IncludeContentChanges: str
        :param _IncludeQuery: 如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
        :type IncludeQuery: bool
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :type RecordWithSchema: bool
        :param _SignalDatabase: 存放信令表的数据库名称
        :type SignalDatabase: str
        :param _IsTableRegular: 输入的table是否为正则表达式，如果该选项以及IsTablePrefix同时为true，该选项的判断优先级高于IsTablePrefix
        :type IsTableRegular: bool
        :param _SignalTable: 信号表
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalTable: str
        :param _DateTimeZone: datetime 类型字段转换为时间戳的时区
        :type DateTimeZone: str
        :param _SelfBuilt: 自建
        :type SelfBuilt: bool
        """
        self._Database = None
        self._Table = None
        self._Resource = None
        self._SnapshotMode = None
        self._DdlTopic = None
        self._DataSourceMonitorMode = None
        self._DataSourceMonitorResource = None
        self._DataSourceIncrementMode = None
        self._DataSourceIncrementColumn = None
        self._DataSourceStartFrom = None
        self._DataTargetInsertMode = None
        self._DataTargetPrimaryKeyField = None
        self._DataTargetRecordMapping = None
        self._TopicRegex = None
        self._TopicReplacement = None
        self._KeyColumns = None
        self._DropInvalidMessage = None
        self._DropCls = None
        self._OutputFormat = None
        self._IsTablePrefix = None
        self._IncludeContentChanges = None
        self._IncludeQuery = None
        self._RecordWithSchema = None
        self._SignalDatabase = None
        self._IsTableRegular = None
        self._SignalTable = None
        self._DateTimeZone = None
        self._SelfBuilt = None

    @property
    def Database(self):
        """MySQL的数据库名称，"*"为全数据库
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """MySQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"数据库名\\.数据表名"
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        """该MySQL在连接管理内的Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
        """复制存量信息(schema_only不复制, initial全量)，默认值initial
        :rtype: str
        """
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def DdlTopic(self):
        """存放MySQL的Ddl信息的Topic，为空则默认不存放
        :rtype: str
        """
        return self._DdlTopic

    @DdlTopic.setter
    def DdlTopic(self, DdlTopic):
        self._DdlTopic = DdlTopic

    @property
    def DataSourceMonitorMode(self):
        """"TABLE" 表示读取项为 table，"QUERY" 表示读取项为 query
        :rtype: str
        """
        return self._DataSourceMonitorMode

    @DataSourceMonitorMode.setter
    def DataSourceMonitorMode(self, DataSourceMonitorMode):
        self._DataSourceMonitorMode = DataSourceMonitorMode

    @property
    def DataSourceMonitorResource(self):
        """当 "DataMonitorMode"="TABLE" 时，传入需要读取的 Table；当 "DataMonitorMode"="QUERY" 时，传入需要读取的查询 sql 语句
        :rtype: str
        """
        return self._DataSourceMonitorResource

    @DataSourceMonitorResource.setter
    def DataSourceMonitorResource(self, DataSourceMonitorResource):
        self._DataSourceMonitorResource = DataSourceMonitorResource

    @property
    def DataSourceIncrementMode(self):
        """"TIMESTAMP" 表示增量列为时间戳类型，"INCREMENT" 表示增量列为自增 id 类型
        :rtype: str
        """
        return self._DataSourceIncrementMode

    @DataSourceIncrementMode.setter
    def DataSourceIncrementMode(self, DataSourceIncrementMode):
        self._DataSourceIncrementMode = DataSourceIncrementMode

    @property
    def DataSourceIncrementColumn(self):
        """传入需要监听的列名称
        :rtype: str
        """
        return self._DataSourceIncrementColumn

    @DataSourceIncrementColumn.setter
    def DataSourceIncrementColumn(self, DataSourceIncrementColumn):
        self._DataSourceIncrementColumn = DataSourceIncrementColumn

    @property
    def DataSourceStartFrom(self):
        """"HEAD" 表示复制存量 + 增量数据，"TAIL" 表示只复制增量数据
        :rtype: str
        """
        return self._DataSourceStartFrom

    @DataSourceStartFrom.setter
    def DataSourceStartFrom(self, DataSourceStartFrom):
        self._DataSourceStartFrom = DataSourceStartFrom

    @property
    def DataTargetInsertMode(self):
        """"INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
        :rtype: str
        """
        return self._DataTargetInsertMode

    @DataTargetInsertMode.setter
    def DataTargetInsertMode(self, DataTargetInsertMode):
        self._DataTargetInsertMode = DataTargetInsertMode

    @property
    def DataTargetPrimaryKeyField(self):
        """当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
        :rtype: str
        """
        return self._DataTargetPrimaryKeyField

    @DataTargetPrimaryKeyField.setter
    def DataTargetPrimaryKeyField(self, DataTargetPrimaryKeyField):
        self._DataTargetPrimaryKeyField = DataTargetPrimaryKeyField

    @property
    def DataTargetRecordMapping(self):
        """表与消息间的映射关系
        :rtype: list of RecordMapping
        """
        return self._DataTargetRecordMapping

    @DataTargetRecordMapping.setter
    def DataTargetRecordMapping(self, DataTargetRecordMapping):
        self._DataTargetRecordMapping = DataTargetRecordMapping

    @property
    def TopicRegex(self):
        """事件路由到特定主题的正则表达式，默认为(.*)
        :rtype: str
        """
        return self._TopicRegex

    @TopicRegex.setter
    def TopicRegex(self, TopicRegex):
        self._TopicRegex = TopicRegex

    @property
    def TopicReplacement(self):
        """TopicRegex的引用组，指定$1、$2等
        :rtype: str
        """
        return self._TopicReplacement

    @TopicReplacement.setter
    def TopicReplacement(self, TopicReplacement):
        self._TopicReplacement = TopicReplacement

    @property
    def KeyColumns(self):
        """格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :rtype: str
        """
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def DropInvalidMessage(self):
        """Mysql 是否抛弃解析失败的消息，默认为true
        :rtype: bool
        """
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def DropCls(self):
        """当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        """
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def OutputFormat(self):
        """输出格式，DEFAULT、CANAL_1、CANAL_2
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def IsTablePrefix(self):
        """当Table输入的是前缀时，该项值为true，否则为false
        :rtype: bool
        """
        return self._IsTablePrefix

    @IsTablePrefix.setter
    def IsTablePrefix(self, IsTablePrefix):
        self._IsTablePrefix = IsTablePrefix

    @property
    def IncludeContentChanges(self):
        """如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
        :rtype: str
        """
        return self._IncludeContentChanges

    @IncludeContentChanges.setter
    def IncludeContentChanges(self, IncludeContentChanges):
        self._IncludeContentChanges = IncludeContentChanges

    @property
    def IncludeQuery(self):
        """如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
        :rtype: bool
        """
        return self._IncludeQuery

    @IncludeQuery.setter
    def IncludeQuery(self, IncludeQuery):
        self._IncludeQuery = IncludeQuery

    @property
    def RecordWithSchema(self):
        """如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :rtype: bool
        """
        return self._RecordWithSchema

    @RecordWithSchema.setter
    def RecordWithSchema(self, RecordWithSchema):
        self._RecordWithSchema = RecordWithSchema

    @property
    def SignalDatabase(self):
        """存放信令表的数据库名称
        :rtype: str
        """
        return self._SignalDatabase

    @SignalDatabase.setter
    def SignalDatabase(self, SignalDatabase):
        self._SignalDatabase = SignalDatabase

    @property
    def IsTableRegular(self):
        """输入的table是否为正则表达式，如果该选项以及IsTablePrefix同时为true，该选项的判断优先级高于IsTablePrefix
        :rtype: bool
        """
        return self._IsTableRegular

    @IsTableRegular.setter
    def IsTableRegular(self, IsTableRegular):
        self._IsTableRegular = IsTableRegular

    @property
    def SignalTable(self):
        """信号表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SignalTable

    @SignalTable.setter
    def SignalTable(self, SignalTable):
        self._SignalTable = SignalTable

    @property
    def DateTimeZone(self):
        """datetime 类型字段转换为时间戳的时区
        :rtype: str
        """
        return self._DateTimeZone

    @DateTimeZone.setter
    def DateTimeZone(self, DateTimeZone):
        self._DateTimeZone = DateTimeZone

    @property
    def SelfBuilt(self):
        """自建
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Resource = params.get("Resource")
        self._SnapshotMode = params.get("SnapshotMode")
        self._DdlTopic = params.get("DdlTopic")
        self._DataSourceMonitorMode = params.get("DataSourceMonitorMode")
        self._DataSourceMonitorResource = params.get("DataSourceMonitorResource")
        self._DataSourceIncrementMode = params.get("DataSourceIncrementMode")
        self._DataSourceIncrementColumn = params.get("DataSourceIncrementColumn")
        self._DataSourceStartFrom = params.get("DataSourceStartFrom")
        self._DataTargetInsertMode = params.get("DataTargetInsertMode")
        self._DataTargetPrimaryKeyField = params.get("DataTargetPrimaryKeyField")
        if params.get("DataTargetRecordMapping") is not None:
            self._DataTargetRecordMapping = []
            for item in params.get("DataTargetRecordMapping"):
                obj = RecordMapping()
                obj._deserialize(item)
                self._DataTargetRecordMapping.append(obj)
        self._TopicRegex = params.get("TopicRegex")
        self._TopicReplacement = params.get("TopicReplacement")
        self._KeyColumns = params.get("KeyColumns")
        self._DropInvalidMessage = params.get("DropInvalidMessage")
        if params.get("DropCls") is not None:
            self._DropCls = DropCls()
            self._DropCls._deserialize(params.get("DropCls"))
        self._OutputFormat = params.get("OutputFormat")
        self._IsTablePrefix = params.get("IsTablePrefix")
        self._IncludeContentChanges = params.get("IncludeContentChanges")
        self._IncludeQuery = params.get("IncludeQuery")
        self._RecordWithSchema = params.get("RecordWithSchema")
        self._SignalDatabase = params.get("SignalDatabase")
        self._IsTableRegular = params.get("IsTableRegular")
        self._SignalTable = params.get("SignalTable")
        self._DateTimeZone = params.get("DateTimeZone")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateResponseData(AbstractModel):
    """操作类型返回的Data结构

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程Id
        :type FlowId: int
        :param _RouteDTO: RouteIdDto
        :type RouteDTO: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        self._FlowId = None
        self._RouteDTO = None

    @property
    def FlowId(self):
        """流程Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RouteDTO(self):
        """RouteIdDto
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        return self._RouteDTO

    @RouteDTO.setter
    def RouteDTO(self, RouteDTO):
        self._RouteDTO = RouteDTO


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("RouteDTO") is not None:
            self._RouteDTO = RouteDTO()
            self._RouteDTO._deserialize(params.get("RouteDTO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """分区实体

    """

    def __init__(self):
        r"""
        :param _PartitionId: 分区ID
        :type PartitionId: int
        """
        self._PartitionId = None

    @property
    def PartitionId(self):
        """分区ID
        :rtype: int
        """
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId


    def _deserialize(self, params):
        self._PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionOffset(AbstractModel):
    """分区和位移

    """

    def __init__(self):
        r"""
        :param _Partition: 分区
        :type Partition: str
        :param _Offset: 位点偏移量
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        """分区
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """位点偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partitions(AbstractModel):
    """partition信息

    """

    def __init__(self):
        r"""
        :param _Partition: 分区
        :type Partition: int
        :param _Offset: partition 消费位移
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        """分区
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        """partition 消费位移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostgreSQLConnectParam(AbstractModel):
    """PostgreSQL连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: PostgreSQL的连接port
        :type Port: int
        :param _UserName: PostgreSQL连接源的用户名
        :type UserName: str
        :param _Password: PostgreSQL连接源的密码
        :type Password: str
        :param _Resource: PostgreSQL连接源的实例资源
        :type Resource: str
        :param _ServiceVip: PostgreSQL连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: PostgreSQL连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _ClusterId: 当type为TDSQL_C_POSTGRESQL时，必填
        :type ClusterId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        :param _SelfBuilt: PostgreSQL连接源是否为自建集群
        :type SelfBuilt: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._ClusterId = None
        self._IsUpdate = None
        self._SelfBuilt = None

    @property
    def Port(self):
        """PostgreSQL的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """PostgreSQL连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """PostgreSQL连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """PostgreSQL连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        """PostgreSQL连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """PostgreSQL连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ClusterId(self):
        """当type为TDSQL_C_POSTGRESQL时，必填
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        """PostgreSQL连接源是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ClusterId = params.get("ClusterId")
        self._IsUpdate = params.get("IsUpdate")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostgreSQLModifyConnectParam(AbstractModel):
    """PostgreSQL修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: PostgreSQL连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: PostgreSQL的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: PostgreSQL连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: PostgreSQL连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: PostgreSQL连接源的用户名
        :type UserName: str
        :param _Password: PostgreSQL连接源的密码
        :type Password: str
        :param _ClusterId: 当type为TDSQL_C_POSTGRESQL时，该参数才有值【不支持修改】
        :type ClusterId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
        :type IsUpdate: bool
        :param _SelfBuilt: 是否为自建集群
        :type SelfBuilt: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._ClusterId = None
        self._IsUpdate = None
        self._SelfBuilt = None

    @property
    def Resource(self):
        """PostgreSQL连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """PostgreSQL的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """PostgreSQL连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """PostgreSQL连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """PostgreSQL连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """PostgreSQL连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ClusterId(self):
        """当type为TDSQL_C_POSTGRESQL时，该参数才有值【不支持修改】
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsUpdate(self):
        """是否更新到关联的Datahub任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        """是否为自建集群
        :rtype: bool
        """
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._ClusterId = params.get("ClusterId")
        self._IsUpdate = params.get("IsUpdate")
        self._SelfBuilt = params.get("SelfBuilt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostgreSQLParam(AbstractModel):
    """PostgreSQL类型入参

    """

    def __init__(self):
        r"""
        :param _Database: PostgreSQL的数据库名称
        :type Database: str
        :param _Table: PostgreSQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"Schema名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"Schema名\\.数据表名"
        :type Table: str
        :param _Resource: 该PostgreSQL在连接管理内的Id
        :type Resource: str
        :param _PluginName: 插件名(decoderbufs/pgoutput)，默认为decoderbufs
        :type PluginName: str
        :param _SnapshotMode: 复制存量信息(never增量, initial全量)，默认为initial
        :type SnapshotMode: str
        :param _DataFormat: 上游数据格式(JSON/Debezium), 当数据库同步模式为默认字段匹配时,必填
        :type DataFormat: str
        :param _DataTargetInsertMode: "INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
        :type DataTargetInsertMode: str
        :param _DataTargetPrimaryKeyField: 当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
        :type DataTargetPrimaryKeyField: str
        :param _DataTargetRecordMapping: 表与消息间的映射关系
        :type DataTargetRecordMapping: list of RecordMapping
        :param _DropInvalidMessage: 是否抛弃解析失败的消息，默认为true
        :type DropInvalidMessage: bool
        :param _IsTableRegular: 输入的table是否为正则表达式
        :type IsTableRegular: bool
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :type KeyColumns: str
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :type RecordWithSchema: bool
        """
        self._Database = None
        self._Table = None
        self._Resource = None
        self._PluginName = None
        self._SnapshotMode = None
        self._DataFormat = None
        self._DataTargetInsertMode = None
        self._DataTargetPrimaryKeyField = None
        self._DataTargetRecordMapping = None
        self._DropInvalidMessage = None
        self._IsTableRegular = None
        self._KeyColumns = None
        self._RecordWithSchema = None

    @property
    def Database(self):
        """PostgreSQL的数据库名称
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """PostgreSQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"Schema名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"Schema名\\.数据表名"
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        """该PostgreSQL在连接管理内的Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def PluginName(self):
        """插件名(decoderbufs/pgoutput)，默认为decoderbufs
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def SnapshotMode(self):
        """复制存量信息(never增量, initial全量)，默认为initial
        :rtype: str
        """
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def DataFormat(self):
        """上游数据格式(JSON/Debezium), 当数据库同步模式为默认字段匹配时,必填
        :rtype: str
        """
        return self._DataFormat

    @DataFormat.setter
    def DataFormat(self, DataFormat):
        self._DataFormat = DataFormat

    @property
    def DataTargetInsertMode(self):
        """"INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
        :rtype: str
        """
        return self._DataTargetInsertMode

    @DataTargetInsertMode.setter
    def DataTargetInsertMode(self, DataTargetInsertMode):
        self._DataTargetInsertMode = DataTargetInsertMode

    @property
    def DataTargetPrimaryKeyField(self):
        """当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
        :rtype: str
        """
        return self._DataTargetPrimaryKeyField

    @DataTargetPrimaryKeyField.setter
    def DataTargetPrimaryKeyField(self, DataTargetPrimaryKeyField):
        self._DataTargetPrimaryKeyField = DataTargetPrimaryKeyField

    @property
    def DataTargetRecordMapping(self):
        """表与消息间的映射关系
        :rtype: list of RecordMapping
        """
        return self._DataTargetRecordMapping

    @DataTargetRecordMapping.setter
    def DataTargetRecordMapping(self, DataTargetRecordMapping):
        self._DataTargetRecordMapping = DataTargetRecordMapping

    @property
    def DropInvalidMessage(self):
        """是否抛弃解析失败的消息，默认为true
        :rtype: bool
        """
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def IsTableRegular(self):
        """输入的table是否为正则表达式
        :rtype: bool
        """
        return self._IsTableRegular

    @IsTableRegular.setter
    def IsTableRegular(self, IsTableRegular):
        self._IsTableRegular = IsTableRegular

    @property
    def KeyColumns(self):
        """格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
        :rtype: str
        """
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def RecordWithSchema(self):
        """如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
        :rtype: bool
        """
        return self._RecordWithSchema

    @RecordWithSchema.setter
    def RecordWithSchema(self, RecordWithSchema):
        self._RecordWithSchema = RecordWithSchema


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Resource = params.get("Resource")
        self._PluginName = params.get("PluginName")
        self._SnapshotMode = params.get("SnapshotMode")
        self._DataFormat = params.get("DataFormat")
        self._DataTargetInsertMode = params.get("DataTargetInsertMode")
        self._DataTargetPrimaryKeyField = params.get("DataTargetPrimaryKeyField")
        if params.get("DataTargetRecordMapping") is not None:
            self._DataTargetRecordMapping = []
            for item in params.get("DataTargetRecordMapping"):
                obj = RecordMapping()
                obj._deserialize(item)
                self._DataTargetRecordMapping.append(obj)
        self._DropInvalidMessage = params.get("DropInvalidMessage")
        self._IsTableRegular = params.get("IsTableRegular")
        self._KeyColumns = params.get("KeyColumns")
        self._RecordWithSchema = params.get("RecordWithSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """消息价格实体

    """

    def __init__(self):
        r"""
        :param _RealTotalCost: 折扣价
        :type RealTotalCost: float
        :param _TotalCost: 原价
        :type TotalCost: float
        """
        self._RealTotalCost = None
        self._TotalCost = None

    @property
    def RealTotalCost(self):
        """折扣价
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
        """原价
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._RealTotalCost = params.get("RealTotalCost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateLinkParam(AbstractModel):
    """建立私有连接的参数

    """

    def __init__(self):
        r"""
        :param _ServiceVip: 客户实例的vip
        :type ServiceVip: str
        :param _UniqVpcId: 客户实例的vpcId
        :type UniqVpcId: str
        """
        self._ServiceVip = None
        self._UniqVpcId = None

    @property
    def ServiceVip(self):
        """客户实例的vip
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """客户实例的vpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusDTO(AbstractModel):
    """普罗米修斯打通的vipVport

    """

    def __init__(self):
        r"""
        :param _Type: export类型（jmx_export\node_export）
        :type Type: str
        :param _SourceIp: vip
        :type SourceIp: str
        :param _SourcePort: vport
        :type SourcePort: int
        :param _BrokerIp: broker地址
        :type BrokerIp: str
        :param _VpcId: VPC ID信息
        :type VpcId: str
        :param _SubnetId: 子网ID信息
        :type SubnetId: str
        """
        self._Type = None
        self._SourceIp = None
        self._SourcePort = None
        self._BrokerIp = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def Type(self):
        """export类型（jmx_export\node_export）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SourceIp(self):
        """vip
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SourcePort(self):
        """vport
        :rtype: int
        """
        return self._SourcePort

    @SourcePort.setter
    def SourcePort(self, SourcePort):
        self._SourcePort = SourcePort

    @property
    def BrokerIp(self):
        """broker地址
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def VpcId(self):
        """VPC ID信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID信息
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SourceIp = params.get("SourceIp")
        self._SourcePort = params.get("SourcePort")
        self._BrokerIp = params.get("BrokerIp")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusResult(AbstractModel):
    """Prometheus 监控返回

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param _ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param _Data: 操作型返回的Data数据,可能有flowId等
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        """返回的code，0为正常，非0为错误
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        """成功消息
        :rtype: str
        """
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        """操作型返回的Data数据,可能有flowId等
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self._Data = OperateResponseData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordMapping(AbstractModel):
    """record 与数据库表的映射关系

    """

    def __init__(self):
        r"""
        :param _JsonKey: 消息的 key 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonKey: str
        :param _Type: 消息类型
        :type Type: str
        :param _AllowNull: 消息是否允许为空
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowNull: bool
        :param _ColumnName: 对应映射列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnName: str
        :param _ExtraInfo: 数据库表额外字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: str
        :param _ColumnSize: 当前列大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnSize: str
        :param _DecimalDigits: 当前列精度
注意：此字段可能返回 null，表示取不到有效值。
        :type DecimalDigits: str
        :param _AutoIncrement: 是否为自增列
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoIncrement: bool
        :param _DefaultValue: 数据库表默认参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        """
        self._JsonKey = None
        self._Type = None
        self._AllowNull = None
        self._ColumnName = None
        self._ExtraInfo = None
        self._ColumnSize = None
        self._DecimalDigits = None
        self._AutoIncrement = None
        self._DefaultValue = None

    @property
    def JsonKey(self):
        """消息的 key 名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JsonKey

    @JsonKey.setter
    def JsonKey(self, JsonKey):
        self._JsonKey = JsonKey

    @property
    def Type(self):
        """消息类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowNull(self):
        """消息是否允许为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AllowNull

    @AllowNull.setter
    def AllowNull(self, AllowNull):
        self._AllowNull = AllowNull

    @property
    def ColumnName(self):
        """对应映射列名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def ExtraInfo(self):
        """数据库表额外字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def ColumnSize(self):
        """当前列大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColumnSize

    @ColumnSize.setter
    def ColumnSize(self, ColumnSize):
        self._ColumnSize = ColumnSize

    @property
    def DecimalDigits(self):
        """当前列精度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DecimalDigits

    @DecimalDigits.setter
    def DecimalDigits(self, DecimalDigits):
        self._DecimalDigits = DecimalDigits

    @property
    def AutoIncrement(self):
        """是否为自增列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoIncrement

    @AutoIncrement.setter
    def AutoIncrement(self, AutoIncrement):
        self._AutoIncrement = AutoIncrement

    @property
    def DefaultValue(self):
        """数据库表默认参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue


    def _deserialize(self, params):
        self._JsonKey = params.get("JsonKey")
        self._Type = params.get("Type")
        self._AllowNull = params.get("AllowNull")
        self._ColumnName = params.get("ColumnName")
        self._ExtraInfo = params.get("ExtraInfo")
        self._ColumnSize = params.get("ColumnSize")
        self._DecimalDigits = params.get("DecimalDigits")
        self._AutoIncrement = params.get("AutoIncrement")
        self._DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegexReplaceParam(AbstractModel):
    """数据处理——Value处理参数——正则替换参数

    """

    def __init__(self):
        r"""
        :param _Regex: 正则表达式
        :type Regex: str
        :param _NewValue: 替换新值
        :type NewValue: str
        """
        self._Regex = None
        self._NewValue = None

    @property
    def Regex(self):
        """正则表达式
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def NewValue(self):
        """替换新值
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """地域实体对象

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _AreaName: 区域名称
        :type AreaName: str
        :param _RegionCode: 地域代码
        :type RegionCode: str
        :param _RegionCodeV3: 地域代码（V3版本）
        :type RegionCodeV3: str
        :param _Support: NONE:默认值不支持任何特殊类型 实例类型
        :type Support: str
        :param _Ipv6: 是否支持ipv6, 0：表示不支持，1：表示支持
        :type Ipv6: int
        :param _MultiZone: 是否支持跨可用区, 0：表示不支持，1：表示支持
        :type MultiZone: int
        """
        self._RegionId = None
        self._RegionName = None
        self._AreaName = None
        self._RegionCode = None
        self._RegionCodeV3 = None
        self._Support = None
        self._Ipv6 = None
        self._MultiZone = None

    @property
    def RegionId(self):
        """地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def AreaName(self):
        """区域名称
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def RegionCode(self):
        """地域代码
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def RegionCodeV3(self):
        """地域代码（V3版本）
        :rtype: str
        """
        return self._RegionCodeV3

    @RegionCodeV3.setter
    def RegionCodeV3(self, RegionCodeV3):
        self._RegionCodeV3 = RegionCodeV3

    @property
    def Support(self):
        """NONE:默认值不支持任何特殊类型 实例类型
        :rtype: str
        """
        return self._Support

    @Support.setter
    def Support(self, Support):
        self._Support = Support

    @property
    def Ipv6(self):
        """是否支持ipv6, 0：表示不支持，1：表示支持
        :rtype: int
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def MultiZone(self):
        """是否支持跨可用区, 0：表示不支持，1：表示支持
        :rtype: int
        """
        return self._MultiZone

    @MultiZone.setter
    def MultiZone(self, MultiZone):
        self._MultiZone = MultiZone


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._AreaName = params.get("AreaName")
        self._RegionCode = params.get("RegionCode")
        self._RegionCodeV3 = params.get("RegionCodeV3")
        self._Support = params.get("Support")
        self._Ipv6 = params.get("Ipv6")
        self._MultiZone = params.get("MultiZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCkafkaInstanceRequest(AbstractModel):
    """RenewCkafkaInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ckafka集群实例Id
        :type InstanceId: str
        :param _TimeSpan: 续费时长, 默认为1, 单位是月
        :type TimeSpan: int
        """
        self._InstanceId = None
        self._TimeSpan = None

    @property
    def InstanceId(self):
        """ckafka集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeSpan(self):
        """续费时长, 默认为1, 单位是月
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCkafkaInstanceResp(AbstractModel):
    """RenewCkafkaInstance接口出参bigDealIds

    """

    def __init__(self):
        r"""
        :param _BigDealId: 订单号
        :type BigDealId: str
        :param _DealName: 子订单号
        :type DealName: str
        """
        self._BigDealId = None
        self._DealName = None

    @property
    def BigDealId(self):
        """订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def DealName(self):
        """子订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._BigDealId = params.get("BigDealId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCkafkaInstanceResponse(AbstractModel):
    """RenewCkafkaInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RenewCkafkaInstanceResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回值
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RenewCkafkaInstanceResp`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = RenewCkafkaInstanceResp()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ReplaceParam(AbstractModel):
    """数据处理——Value处理参数——替换参数

    """

    def __init__(self):
        r"""
        :param _OldValue: 被替换值
        :type OldValue: str
        :param _NewValue: 替换值
        :type NewValue: str
        """
        self._OldValue = None
        self._NewValue = None

    @property
    def OldValue(self):
        """被替换值
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        """替换值
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """路由实体对象

    """

    def __init__(self):
        r"""
        :param _AccessType: 实例接入方式
0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
        :type AccessType: int
        :param _RouteId: 路由Id
        :type RouteId: int
        :param _VipType: vip网络类型（1:外网TGW  2:基础网络 3:VPC网络 4:支撑网络(idc 环境) 5:SSL外网访问方式访问 6:黑石环境vpc 7:支撑网络(cvm 环境）
        :type VipType: int
        :param _VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _DomainPort: 域名port
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainPort: int
        :param _DeleteTimestamp: 时间戳
        :type DeleteTimestamp: str
        :param _Subnet: 子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Subnet: str
        :param _BrokerVipList: 虚拟IP列表(1对1 broker节点)
        :type BrokerVipList: list of VipEntity
        :param _VpcId: 私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._AccessType = None
        self._RouteId = None
        self._VipType = None
        self._VipList = None
        self._Domain = None
        self._DomainPort = None
        self._DeleteTimestamp = None
        self._Subnet = None
        self._BrokerVipList = None
        self._VpcId = None

    @property
    def AccessType(self):
        """实例接入方式
0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def RouteId(self):
        """路由Id
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def VipType(self):
        """vip网络类型（1:外网TGW  2:基础网络 3:VPC网络 4:支撑网络(idc 环境) 5:SSL外网访问方式访问 6:黑石环境vpc 7:支撑网络(cvm 环境）
        :rtype: int
        """
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VipList(self):
        """虚拟IP列表
        :rtype: list of VipEntity
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Domain(self):
        """域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainPort(self):
        """域名port
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DomainPort

    @DomainPort.setter
    def DomainPort(self, DomainPort):
        self._DomainPort = DomainPort

    @property
    def DeleteTimestamp(self):
        """时间戳
        :rtype: str
        """
        return self._DeleteTimestamp

    @DeleteTimestamp.setter
    def DeleteTimestamp(self, DeleteTimestamp):
        self._DeleteTimestamp = DeleteTimestamp

    @property
    def Subnet(self):
        """子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def BrokerVipList(self):
        """虚拟IP列表(1对1 broker节点)
        :rtype: list of VipEntity
        """
        return self._BrokerVipList

    @BrokerVipList.setter
    def BrokerVipList(self, BrokerVipList):
        self._BrokerVipList = BrokerVipList

    @property
    def VpcId(self):
        """私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._RouteId = params.get("RouteId")
        self._VipType = params.get("VipType")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._Domain = params.get("Domain")
        self._DomainPort = params.get("DomainPort")
        self._DeleteTimestamp = params.get("DeleteTimestamp")
        self._Subnet = params.get("Subnet")
        if params.get("BrokerVipList") is not None:
            self._BrokerVipList = []
            for item in params.get("BrokerVipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self._BrokerVipList.append(obj)
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteDTO(AbstractModel):
    """RouteDTO

    """

    def __init__(self):
        r"""
        :param _RouteId: 路由Id
        :type RouteId: int
        """
        self._RouteId = None

    @property
    def RouteId(self):
        """路由Id
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId


    def _deserialize(self, params):
        self._RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    """路由信息返回对象

    """

    def __init__(self):
        r"""
        :param _Routers: 路由信息列表
        :type Routers: list of Route
        """
        self._Routers = None

    @property
    def Routers(self):
        """路由信息列表
        :rtype: list of Route
        """
        return self._Routers

    @Routers.setter
    def Routers(self, Routers):
        self._Routers = Routers


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self._Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self._Routers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowParam(AbstractModel):
    """数据处理ROW输出格式配置

    """

    def __init__(self):
        r"""
        :param _RowContent: 行内容，KEY_VALUE，VALUE
        :type RowContent: str
        :param _KeyValueDelimiter: key和value间的分隔符
        :type KeyValueDelimiter: str
        :param _EntryDelimiter: 元素建的分隔符
        :type EntryDelimiter: str
        """
        self._RowContent = None
        self._KeyValueDelimiter = None
        self._EntryDelimiter = None

    @property
    def RowContent(self):
        """行内容，KEY_VALUE，VALUE
        :rtype: str
        """
        return self._RowContent

    @RowContent.setter
    def RowContent(self, RowContent):
        self._RowContent = RowContent

    @property
    def KeyValueDelimiter(self):
        """key和value间的分隔符
        :rtype: str
        """
        return self._KeyValueDelimiter

    @KeyValueDelimiter.setter
    def KeyValueDelimiter(self, KeyValueDelimiter):
        self._KeyValueDelimiter = KeyValueDelimiter

    @property
    def EntryDelimiter(self):
        """元素建的分隔符
        :rtype: str
        """
        return self._EntryDelimiter

    @EntryDelimiter.setter
    def EntryDelimiter(self, EntryDelimiter):
        self._EntryDelimiter = EntryDelimiter


    def _deserialize(self, params):
        self._RowContent = params.get("RowContent")
        self._KeyValueDelimiter = params.get("KeyValueDelimiter")
        self._EntryDelimiter = params.get("EntryDelimiter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SMTParam(AbstractModel):
    """数据处理——数据处理参数

    """

    def __init__(self):
        r"""
        :param _Key: 数据处理KEY
        :type Key: str
        :param _Operate: 操作，DATE系统预设-时间戳，CUSTOMIZE自定义，MAPPING映射，JSONPATH
        :type Operate: str
        :param _SchemeType: 数据类型，ORIGINAL原始，STRING，INT64，FLOAT64，BOOLEAN，MAP，ARRAY
        :type SchemeType: str
        :param _Value: 数据处理VALUE
        :type Value: str
        :param _ValueOperate: VALUE处理
        :type ValueOperate: :class:`tencentcloud.ckafka.v20190819.models.ValueParam`
        :param _OriginalValue: 原始VALUE
        :type OriginalValue: str
        :param _ValueOperates: VALUE处理链
        :type ValueOperates: list of ValueParam
        """
        self._Key = None
        self._Operate = None
        self._SchemeType = None
        self._Value = None
        self._ValueOperate = None
        self._OriginalValue = None
        self._ValueOperates = None

    @property
    def Key(self):
        """数据处理KEY
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operate(self):
        """操作，DATE系统预设-时间戳，CUSTOMIZE自定义，MAPPING映射，JSONPATH
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def SchemeType(self):
        """数据类型，ORIGINAL原始，STRING，INT64，FLOAT64，BOOLEAN，MAP，ARRAY
        :rtype: str
        """
        return self._SchemeType

    @SchemeType.setter
    def SchemeType(self, SchemeType):
        self._SchemeType = SchemeType

    @property
    def Value(self):
        """数据处理VALUE
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueOperate(self):
        """VALUE处理
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ValueParam`
        """
        return self._ValueOperate

    @ValueOperate.setter
    def ValueOperate(self, ValueOperate):
        self._ValueOperate = ValueOperate

    @property
    def OriginalValue(self):
        """原始VALUE
        :rtype: str
        """
        return self._OriginalValue

    @OriginalValue.setter
    def OriginalValue(self, OriginalValue):
        self._OriginalValue = OriginalValue

    @property
    def ValueOperates(self):
        """VALUE处理链
        :rtype: list of ValueParam
        """
        return self._ValueOperates

    @ValueOperates.setter
    def ValueOperates(self, ValueOperates):
        self._ValueOperates = ValueOperates


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operate = params.get("Operate")
        self._SchemeType = params.get("SchemeType")
        self._Value = params.get("Value")
        if params.get("ValueOperate") is not None:
            self._ValueOperate = ValueParam()
            self._ValueOperate._deserialize(params.get("ValueOperate"))
        self._OriginalValue = params.get("OriginalValue")
        if params.get("ValueOperates") is not None:
            self._ValueOperates = []
            for item in params.get("ValueOperates"):
                obj = ValueParam()
                obj._deserialize(item)
                self._ValueOperates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLServerConnectParam(AbstractModel):
    """SQLServer连接源参数

    """

    def __init__(self):
        r"""
        :param _Port: SQLServer的连接port
        :type Port: int
        :param _UserName: SQLServer连接源的用户名
        :type UserName: str
        :param _Password: SQLServer连接源的密码
        :type Password: str
        :param _Resource: SQLServer连接源的实例资源
        :type Resource: str
        :param _ServiceVip: SQLServer连接源的实例vip，当为腾讯云实例时，必填
        :type ServiceVip: str
        :param _UniqVpcId: SQLServer连接源的vpcId，当为腾讯云实例时，必填
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Dip任务
        :type IsUpdate: bool
        """
        self._Port = None
        self._UserName = None
        self._Password = None
        self._Resource = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._IsUpdate = None

    @property
    def Port(self):
        """SQLServer的连接port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        """SQLServer连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """SQLServer连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        """SQLServer连接源的实例资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        """SQLServer连接源的实例vip，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """SQLServer连接源的vpcId，当为腾讯云实例时，必填
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        """是否更新到关联的Dip任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Resource = params.get("Resource")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLServerModifyConnectParam(AbstractModel):
    """SQLServer修改连接源参数

    """

    def __init__(self):
        r"""
        :param _Resource: SQLServer连接源的实例资源【不支持修改】
        :type Resource: str
        :param _Port: SQLServer的连接port【不支持修改】
        :type Port: int
        :param _ServiceVip: SQLServer连接源的实例vip【不支持修改】
        :type ServiceVip: str
        :param _UniqVpcId: SQLServer连接源的vpcId【不支持修改】
        :type UniqVpcId: str
        :param _UserName: SQLServer连接源的用户名
        :type UserName: str
        :param _Password: SQLServer连接源的密码
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Dip任务
        :type IsUpdate: bool
        """
        self._Resource = None
        self._Port = None
        self._ServiceVip = None
        self._UniqVpcId = None
        self._UserName = None
        self._Password = None
        self._IsUpdate = None

    @property
    def Resource(self):
        """SQLServer连接源的实例资源【不支持修改】
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        """SQLServer的连接port【不支持修改】
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        """SQLServer连接源的实例vip【不支持修改】
        :rtype: str
        """
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        """SQLServer连接源的vpcId【不支持修改】
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        """SQLServer连接源的用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        """SQLServer连接源的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        """是否更新到关联的Dip任务
        :rtype: bool
        """
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Port = params.get("Port")
        self._ServiceVip = params.get("ServiceVip")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._IsUpdate = params.get("IsUpdate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLServerParam(AbstractModel):
    """SQLServer类型入参

    """

    def __init__(self):
        r"""
        :param _Database: SQLServer的数据库名称
        :type Database: str
        :param _Table: SQLServer的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
        :type Table: str
        :param _Resource: 该SQLServer在连接管理内的Id
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only增量, initial全量)，默认为initial
        :type SnapshotMode: str
        """
        self._Database = None
        self._Table = None
        self._Resource = None
        self._SnapshotMode = None

    @property
    def Database(self):
        """SQLServer的数据库名称
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """SQLServer的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        """该SQLServer在连接管理内的Id
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
        """复制存量信息(schema_only增量, initial全量)，默认为initial
        :rtype: str
        """
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Resource = params.get("Resource")
        self._SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleInfo(AbstractModel):
    """标准版销售信息

    """

    def __init__(self):
        r"""
        :param _Flag: 手动设置的flag标志
        :type Flag: bool
        :param _Version: ckafka版本号(1.1.1/2.4.2/0.10.2)
        :type Version: str
        :param _Platform: 专业版、标准版标志
        :type Platform: str
        :param _SoldOut: 售罄标志：true售罄
        :type SoldOut: bool
        """
        self._Flag = None
        self._Version = None
        self._Platform = None
        self._SoldOut = None

    @property
    def Flag(self):
        """手动设置的flag标志
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Version(self):
        """ckafka版本号(1.1.1/2.4.2/0.10.2)
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Platform(self):
        """专业版、标准版标志
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SoldOut(self):
        """售罄标志：true售罄
        :rtype: bool
        """
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut


    def _deserialize(self, params):
        self._Flag = params.get("Flag")
        self._Version = params.get("Version")
        self._Platform = params.get("Platform")
        self._SoldOut = params.get("SoldOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScalingDownResp(AbstractModel):
    """实例缩容应答

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单号列表
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
        """订单号列表
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScfParam(AbstractModel):
    """Scf类型入参

    """

    def __init__(self):
        r"""
        :param _FunctionName: SCF云函数函数名
        :type FunctionName: str
        :param _Namespace: SCF云函数命名空间, 默认为default
        :type Namespace: str
        :param _Qualifier: SCF云函数版本及别名, 默认为$DEFAULT
        :type Qualifier: str
        :param _BatchSize: 每批最大发送消息数, 默认为1000
        :type BatchSize: int
        :param _MaxRetries: SCF调用失败后重试次数, 默认为5
        :type MaxRetries: int
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None
        self._BatchSize = None
        self._MaxRetries = None

    @property
    def FunctionName(self):
        """SCF云函数函数名
        :rtype: str
        """
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        """SCF云函数命名空间, 默认为default
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        """SCF云函数版本及别名, 默认为$DEFAULT
        :rtype: str
        """
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def BatchSize(self):
        """每批最大发送消息数, 默认为1000
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def MaxRetries(self):
        """SCF调用失败后重试次数, 默认为5
        :rtype: int
        """
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._BatchSize = params.get("BatchSize")
        self._MaxRetries = params.get("MaxRetries")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecondaryAnalyseParam(AbstractModel):
    """数据处理——二次解析参数

    """

    def __init__(self):
        r"""
        :param _Regex: 分隔符
        :type Regex: str
        """
        self._Regex = None

    @property
    def Regex(self):
        """分隔符
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataHubId: DataHub接入ID
        :type DataHubId: str
        :param _Message: 发送消息内容(单次请求最多500条)
        :type Message: list of BatchContent
        """
        self._DataHubId = None
        self._Message = None

    @property
    def DataHubId(self):
        """DataHub接入ID
        :rtype: str
        """
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
        """发送消息内容(单次请求最多500条)
        :rtype: list of BatchContent
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self._Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self._Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 消息ID列表
        :type MessageId: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        """消息ID列表
        :rtype: list of str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

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
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")


class SplitParam(AbstractModel):
    """值支持一拆多，即将一个值拆为一个数组

    """

    def __init__(self):
        r"""
        :param _Regex: 分隔符
        :type Regex: str
        """
        self._Regex = None

    @property
    def Regex(self):
        """分隔符
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribedInfo(AbstractModel):
    """订阅信息实体

    """

    def __init__(self):
        r"""
        :param _TopicName: 订阅的主题名
        :type TopicName: str
        :param _Partition: 订阅的分区
        :type Partition: list of int
        :param _PartitionOffset: 分区offset信息
        :type PartitionOffset: list of PartitionOffset
        :param _TopicId: 订阅的主题ID
        :type TopicId: str
        """
        self._TopicName = None
        self._Partition = None
        self._PartitionOffset = None
        self._TopicId = None

    @property
    def TopicName(self):
        """订阅的主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partition(self):
        """订阅的分区
        :rtype: list of int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def PartitionOffset(self):
        """分区offset信息
        :rtype: list of PartitionOffset
        """
        return self._PartitionOffset

    @PartitionOffset.setter
    def PartitionOffset(self, PartitionOffset):
        self._PartitionOffset = PartitionOffset

    @property
    def TopicId(self):
        """订阅的主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self._PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self._PartitionOffset.append(obj)
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubstrParam(AbstractModel):
    """数据处理——Value处理参数——截取参数

    """

    def __init__(self):
        r"""
        :param _Start: 截取起始位置
        :type Start: int
        :param _End: 截取截止位置
        :type End: int
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        """截取起始位置
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        """截取截止位置
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableMapping(AbstractModel):
    """Table、Topic路由

    """

    def __init__(self):
        r"""
        :param _Database: 库名
        :type Database: str
        :param _Table: 表名，多个表,（逗号）隔开
        :type Table: str
        :param _Topic: Topic名称
        :type Topic: str
        :param _TopicId: Topic ID
        :type TopicId: str
        """
        self._Database = None
        self._Table = None
        self._Topic = None
        self._TopicId = None

    @property
    def Database(self):
        """库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """表名，多个表,（逗号）隔开
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Topic(self):
        """Topic名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicId(self):
        """Topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Topic = params.get("Topic")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """实例详情中的标签对象

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的key
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签的key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值
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
        


class TaskStatusResponse(AbstractModel):
    """任务状态返回对象

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态:
0 成功
1 失败
2 进行中
        :type Status: int
        :param _Output: 输出信息
        :type Output: str
        """
        self._Status = None
        self._Output = None

    @property
    def Status(self):
        """任务状态:
0 成功
1 失败
2 进行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
        """输出信息
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Output = params.get("Output")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TdwParam(AbstractModel):
    """Tdw类型入参

    """

    def __init__(self):
        r"""
        :param _Bid: Tdw的bid
        :type Bid: str
        :param _Tid: Tdw的tid
        :type Tid: str
        :param _IsDomestic: 默认true
        :type IsDomestic: bool
        :param _TdwHost: TDW地址，默认tl-tdbank-tdmanager.tencent-distribute.com
        :type TdwHost: str
        :param _TdwPort: TDW端口，默认8099
        :type TdwPort: int
        """
        self._Bid = None
        self._Tid = None
        self._IsDomestic = None
        self._TdwHost = None
        self._TdwPort = None

    @property
    def Bid(self):
        """Tdw的bid
        :rtype: str
        """
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def Tid(self):
        """Tdw的tid
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def IsDomestic(self):
        """默认true
        :rtype: bool
        """
        return self._IsDomestic

    @IsDomestic.setter
    def IsDomestic(self, IsDomestic):
        self._IsDomestic = IsDomestic

    @property
    def TdwHost(self):
        """TDW地址，默认tl-tdbank-tdmanager.tencent-distribute.com
        :rtype: str
        """
        return self._TdwHost

    @TdwHost.setter
    def TdwHost(self, TdwHost):
        self._TdwHost = TdwHost

    @property
    def TdwPort(self):
        """TDW端口，默认8099
        :rtype: int
        """
        return self._TdwPort

    @TdwPort.setter
    def TdwPort(self, TdwPort):
        self._TdwPort = TdwPort


    def _deserialize(self, params):
        self._Bid = params.get("Bid")
        self._Tid = params.get("Tid")
        self._IsDomestic = params.get("IsDomestic")
        self._TdwHost = params.get("TdwHost")
        self._TdwPort = params.get("TdwPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic(AbstractModel):
    """返回的topic对象

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题的ID
        :type TopicId: str
        :param _TopicName: 主题的名称
        :type TopicName: str
        :param _Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Note = None

    @property
    def TopicId(self):
        """主题的ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题的名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAttributesResponse(AbstractModel):
    """主题属性返回结果实体

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题 ID
        :type TopicId: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _Note: 主题备注
        :type Note: str
        :param _PartitionNum: 分区个数
        :type PartitionNum: int
        :param _EnableWhiteList: IP 白名单开关，1：打开； 0：关闭
        :type EnableWhiteList: int
        :param _IpWhiteList: IP 白名单列表
        :type IpWhiteList: list of str
        :param _Config: topic 配置数组
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _Partitions: 分区详情
        :type Partitions: list of TopicPartitionDO
        :param _EnableAclRule: ACL预设策略开关，1：打开； 0：关闭
        :type EnableAclRule: int
        :param _AclRuleList: 预设策略列表
        :type AclRuleList: list of AclRule
        :param _QuotaConfig: topic 限流策略
        :type QuotaConfig: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        :param _ReplicaNum: 副本数
        :type ReplicaNum: int
        """
        self._TopicId = None
        self._CreateTime = None
        self._Note = None
        self._PartitionNum = None
        self._EnableWhiteList = None
        self._IpWhiteList = None
        self._Config = None
        self._Partitions = None
        self._EnableAclRule = None
        self._AclRuleList = None
        self._QuotaConfig = None
        self._ReplicaNum = None

    @property
    def TopicId(self):
        """主题 ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Note(self):
        """主题备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def PartitionNum(self):
        """分区个数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableWhiteList(self):
        """IP 白名单开关，1：打开； 0：关闭
        :rtype: int
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        """IP 白名单列表
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def Config(self):
        """topic 配置数组
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Partitions(self):
        """分区详情
        :rtype: list of TopicPartitionDO
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def EnableAclRule(self):
        """ACL预设策略开关，1：打开； 0：关闭
        :rtype: int
        """
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleList(self):
        """预设策略列表
        :rtype: list of AclRule
        """
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList

    @property
    def QuotaConfig(self):
        """topic 限流策略
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        """
        return self._QuotaConfig

    @QuotaConfig.setter
    def QuotaConfig(self, QuotaConfig):
        self._QuotaConfig = QuotaConfig

    @property
    def ReplicaNum(self):
        """副本数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._CreateTime = params.get("CreateTime")
        self._Note = params.get("Note")
        self._PartitionNum = params.get("PartitionNum")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self._Config = Config()
            self._Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._EnableAclRule = params.get("EnableAclRule")
        if params.get("AclRuleList") is not None:
            self._AclRuleList = []
            for item in params.get("AclRuleList"):
                obj = AclRule()
                obj._deserialize(item)
                self._AclRuleList.append(obj)
        if params.get("QuotaConfig") is not None:
            self._QuotaConfig = InstanceQuotaConfigResp()
            self._QuotaConfig._deserialize(params.get("QuotaConfig"))
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetail(AbstractModel):
    """主题详情

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
        :type TopicName: str
        :param _TopicId: 主题Id
        :type TopicId: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _ReplicaNum: topic副本数  最小值 1,最大值 3
        :type ReplicaNum: int
        :param _Note: 备注
        :type Note: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _EnableWhiteList: 是否开启ip鉴权白名单，true表示开启，false表示不开启
        :type EnableWhiteList: bool
        :param _IpWhiteListCount: ip白名单中ip个数
        :type IpWhiteListCount: int
        :param _ForwardCosBucket: 数据备份cos bucket: 转存到cos 的bucket地址
        :type ForwardCosBucket: str
        :param _ForwardStatus: 数据备份cos 状态： 1 不开启数据备份，0 开启数据备份
        :type ForwardStatus: int
        :param _ForwardInterval: 数据备份到cos的周期频率
        :type ForwardInterval: int
        :param _Config: 高级配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _RetentionTimeConfig: 消息保留时间配置(用于动态配置变更记录)
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        :param _Status: 0:正常，1：已删除，2：删除中
        :type Status: int
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._TopicName = None
        self._TopicId = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._Note = None
        self._CreateTime = None
        self._EnableWhiteList = None
        self._IpWhiteListCount = None
        self._ForwardCosBucket = None
        self._ForwardStatus = None
        self._ForwardInterval = None
        self._Config = None
        self._RetentionTimeConfig = None
        self._Status = None
        self._Tags = None

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """topic副本数  最小值 1,最大值 3
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Note(self):
        """备注
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableWhiteList(self):
        """是否开启ip鉴权白名单，true表示开启，false表示不开启
        :rtype: bool
        """
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteListCount(self):
        """ip白名单中ip个数
        :rtype: int
        """
        return self._IpWhiteListCount

    @IpWhiteListCount.setter
    def IpWhiteListCount(self, IpWhiteListCount):
        self._IpWhiteListCount = IpWhiteListCount

    @property
    def ForwardCosBucket(self):
        """数据备份cos bucket: 转存到cos 的bucket地址
        :rtype: str
        """
        return self._ForwardCosBucket

    @ForwardCosBucket.setter
    def ForwardCosBucket(self, ForwardCosBucket):
        self._ForwardCosBucket = ForwardCosBucket

    @property
    def ForwardStatus(self):
        """数据备份cos 状态： 1 不开启数据备份，0 开启数据备份
        :rtype: int
        """
        return self._ForwardStatus

    @ForwardStatus.setter
    def ForwardStatus(self, ForwardStatus):
        self._ForwardStatus = ForwardStatus

    @property
    def ForwardInterval(self):
        """数据备份到cos的周期频率
        :rtype: int
        """
        return self._ForwardInterval

    @ForwardInterval.setter
    def ForwardInterval(self, ForwardInterval):
        self._ForwardInterval = ForwardInterval

    @property
    def Config(self):
        """高级配置
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RetentionTimeConfig(self):
        """消息保留时间配置(用于动态配置变更记录)
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        """
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def Status(self):
        """0:正常，1：已删除，2：删除中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        """标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._Note = params.get("Note")
        self._CreateTime = params.get("CreateTime")
        self._EnableWhiteList = params.get("EnableWhiteList")
        self._IpWhiteListCount = params.get("IpWhiteListCount")
        self._ForwardCosBucket = params.get("ForwardCosBucket")
        self._ForwardStatus = params.get("ForwardStatus")
        self._ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self._Config = Config()
            self._Config._deserialize(params.get("Config"))
        if params.get("RetentionTimeConfig") is not None:
            self._RetentionTimeConfig = TopicRetentionTimeConfigRsp()
            self._RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetailResponse(AbstractModel):
    """主题详情返回实体

    """

    def __init__(self):
        r"""
        :param _TopicList: 返回的主题详情列表
        :type TopicList: list of TopicDetail
        :param _TotalCount: 符合条件的所有主题详情数量
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        """返回的主题详情列表
        :rtype: list of TopicDetail
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        """符合条件的所有主题详情数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicFlowRanking(AbstractModel):
    """topic 流量排行

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题Id
        :type TopicId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _ReplicaNum: 副本数
        :type ReplicaNum: int
        :param _TopicTraffic: Topic 流量,单位MB(设置date时以sum方式聚合)
        :type TopicTraffic: str
        :param _MessageHeap: Topic 消息堆积
        :type MessageHeap: int
        """
        self._TopicId = None
        self._TopicName = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._TopicTraffic = None
        self._MessageHeap = None

    @property
    def TopicId(self):
        """主题Id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """副本数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def TopicTraffic(self):
        """Topic 流量,单位MB(设置date时以sum方式聚合)
        :rtype: str
        """
        return self._TopicTraffic

    @TopicTraffic.setter
    def TopicTraffic(self, TopicTraffic):
        self._TopicTraffic = TopicTraffic

    @property
    def MessageHeap(self):
        """Topic 消息堆积
        :rtype: int
        """
        return self._MessageHeap

    @MessageHeap.setter
    def MessageHeap(self, MessageHeap):
        self._MessageHeap = MessageHeap


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._TopicTraffic = params.get("TopicTraffic")
        self._MessageHeap = params.get("MessageHeap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicFlowRankingResult(AbstractModel):
    """topic 生产消息数据，消费者数据

    """

    def __init__(self):
        r"""
        :param _TopicFlow: Topic 流量数组
        :type TopicFlow: list of TopicFlowRanking
        :param _ConsumeSpeed: 消费者组消费速度排行速度
        :type ConsumeSpeed: list of ConsumerGroupSpeed
        :param _TopicMessageHeap: Topic 消息堆积/占用磁盘排行
        :type TopicMessageHeap: list of TopicMessageHeapRanking
        :param _BrokerIp: Broker Ip 列表
        :type BrokerIp: list of str
        :param _BrokerTopicData: 单个broker 节点 Topic占用的数据大小
        :type BrokerTopicData: list of BrokerTopicData
        :param _BrokerTopicFlowData: 单个Broker 节点Topic 流量的大小(单位MB)
        :type BrokerTopicFlowData: list of BrokerTopicFlowData
        """
        self._TopicFlow = None
        self._ConsumeSpeed = None
        self._TopicMessageHeap = None
        self._BrokerIp = None
        self._BrokerTopicData = None
        self._BrokerTopicFlowData = None

    @property
    def TopicFlow(self):
        """Topic 流量数组
        :rtype: list of TopicFlowRanking
        """
        return self._TopicFlow

    @TopicFlow.setter
    def TopicFlow(self, TopicFlow):
        self._TopicFlow = TopicFlow

    @property
    def ConsumeSpeed(self):
        """消费者组消费速度排行速度
        :rtype: list of ConsumerGroupSpeed
        """
        return self._ConsumeSpeed

    @ConsumeSpeed.setter
    def ConsumeSpeed(self, ConsumeSpeed):
        self._ConsumeSpeed = ConsumeSpeed

    @property
    def TopicMessageHeap(self):
        """Topic 消息堆积/占用磁盘排行
        :rtype: list of TopicMessageHeapRanking
        """
        return self._TopicMessageHeap

    @TopicMessageHeap.setter
    def TopicMessageHeap(self, TopicMessageHeap):
        self._TopicMessageHeap = TopicMessageHeap

    @property
    def BrokerIp(self):
        """Broker Ip 列表
        :rtype: list of str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def BrokerTopicData(self):
        """单个broker 节点 Topic占用的数据大小
        :rtype: list of BrokerTopicData
        """
        return self._BrokerTopicData

    @BrokerTopicData.setter
    def BrokerTopicData(self, BrokerTopicData):
        self._BrokerTopicData = BrokerTopicData

    @property
    def BrokerTopicFlowData(self):
        """单个Broker 节点Topic 流量的大小(单位MB)
        :rtype: list of BrokerTopicFlowData
        """
        return self._BrokerTopicFlowData

    @BrokerTopicFlowData.setter
    def BrokerTopicFlowData(self, BrokerTopicFlowData):
        self._BrokerTopicFlowData = BrokerTopicFlowData


    def _deserialize(self, params):
        if params.get("TopicFlow") is not None:
            self._TopicFlow = []
            for item in params.get("TopicFlow"):
                obj = TopicFlowRanking()
                obj._deserialize(item)
                self._TopicFlow.append(obj)
        if params.get("ConsumeSpeed") is not None:
            self._ConsumeSpeed = []
            for item in params.get("ConsumeSpeed"):
                obj = ConsumerGroupSpeed()
                obj._deserialize(item)
                self._ConsumeSpeed.append(obj)
        if params.get("TopicMessageHeap") is not None:
            self._TopicMessageHeap = []
            for item in params.get("TopicMessageHeap"):
                obj = TopicMessageHeapRanking()
                obj._deserialize(item)
                self._TopicMessageHeap.append(obj)
        self._BrokerIp = params.get("BrokerIp")
        if params.get("BrokerTopicData") is not None:
            self._BrokerTopicData = []
            for item in params.get("BrokerTopicData"):
                obj = BrokerTopicData()
                obj._deserialize(item)
                self._BrokerTopicData.append(obj)
        if params.get("BrokerTopicFlowData") is not None:
            self._BrokerTopicFlowData = []
            for item in params.get("BrokerTopicFlowData"):
                obj = BrokerTopicFlowData()
                obj._deserialize(item)
                self._BrokerTopicFlowData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaInfo(AbstractModel):
    """topic副本及详细信息

    """

    def __init__(self):
        r"""
        :param _Partition: 分区名称
        :type Partition: str
        :param _Leader: Leader Id
        :type Leader: int
        :param _Replica: 副本集
        :type Replica: str
        :param _InSyncReplica: ISR
        :type InSyncReplica: str
        :param _BeginOffset: 起始Offset
        :type BeginOffset: int
        :param _EndOffset: 末端Offset
        :type EndOffset: int
        :param _MessageCount: 消息数
        :type MessageCount: int
        :param _OutOfSyncReplica: 未同步副本集
        :type OutOfSyncReplica: str
        """
        self._Partition = None
        self._Leader = None
        self._Replica = None
        self._InSyncReplica = None
        self._BeginOffset = None
        self._EndOffset = None
        self._MessageCount = None
        self._OutOfSyncReplica = None

    @property
    def Partition(self):
        """分区名称
        :rtype: str
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Leader(self):
        """Leader Id
        :rtype: int
        """
        return self._Leader

    @Leader.setter
    def Leader(self, Leader):
        self._Leader = Leader

    @property
    def Replica(self):
        """副本集
        :rtype: str
        """
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def InSyncReplica(self):
        """ISR
        :rtype: str
        """
        return self._InSyncReplica

    @InSyncReplica.setter
    def InSyncReplica(self, InSyncReplica):
        self._InSyncReplica = InSyncReplica

    @property
    def BeginOffset(self):
        """起始Offset
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def EndOffset(self):
        """末端Offset
        :rtype: int
        """
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def MessageCount(self):
        """消息数
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def OutOfSyncReplica(self):
        """未同步副本集
        :rtype: str
        """
        return self._OutOfSyncReplica

    @OutOfSyncReplica.setter
    def OutOfSyncReplica(self, OutOfSyncReplica):
        self._OutOfSyncReplica = OutOfSyncReplica


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._Leader = params.get("Leader")
        self._Replica = params.get("Replica")
        self._InSyncReplica = params.get("InSyncReplica")
        self._BeginOffset = params.get("BeginOffset")
        self._EndOffset = params.get("EndOffset")
        self._MessageCount = params.get("MessageCount")
        self._OutOfSyncReplica = params.get("OutOfSyncReplica")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInSyncReplicaResult(AbstractModel):
    """Topic 副本及详情数据集合

    """

    def __init__(self):
        r"""
        :param _TopicInSyncReplicaList: Topic详情及副本合集
        :type TopicInSyncReplicaList: list of TopicInSyncReplicaInfo
        :param _TotalCount: 总计个数
        :type TotalCount: int
        """
        self._TopicInSyncReplicaList = None
        self._TotalCount = None

    @property
    def TopicInSyncReplicaList(self):
        """Topic详情及副本合集
        :rtype: list of TopicInSyncReplicaInfo
        """
        return self._TopicInSyncReplicaList

    @TopicInSyncReplicaList.setter
    def TopicInSyncReplicaList(self, TopicInSyncReplicaList):
        self._TopicInSyncReplicaList = TopicInSyncReplicaList

    @property
    def TotalCount(self):
        """总计个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicInSyncReplicaList") is not None:
            self._TopicInSyncReplicaList = []
            for item in params.get("TopicInSyncReplicaList"):
                obj = TopicInSyncReplicaInfo()
                obj._deserialize(item)
                self._TopicInSyncReplicaList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicMessageHeapRanking(AbstractModel):
    """topic消息堆积、占用磁盘排行

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _ReplicaNum: 副本数
        :type ReplicaNum: int
        :param _TopicTraffic: Topic 流量
        :type TopicTraffic: str
        :param _MessageHeap: topic消息堆积/占用磁盘
        :type MessageHeap: int
        """
        self._TopicId = None
        self._TopicName = None
        self._PartitionNum = None
        self._ReplicaNum = None
        self._TopicTraffic = None
        self._MessageHeap = None

    @property
    def TopicId(self):
        """主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        """副本数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def TopicTraffic(self):
        """Topic 流量
        :rtype: str
        """
        return self._TopicTraffic

    @TopicTraffic.setter
    def TopicTraffic(self, TopicTraffic):
        self._TopicTraffic = TopicTraffic

    @property
    def MessageHeap(self):
        """topic消息堆积/占用磁盘
        :rtype: int
        """
        return self._MessageHeap

    @MessageHeap.setter
    def MessageHeap(self, MessageHeap):
        self._MessageHeap = MessageHeap


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._PartitionNum = params.get("PartitionNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._TopicTraffic = params.get("TopicTraffic")
        self._MessageHeap = params.get("MessageHeap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicParam(AbstractModel):
    """Topic配置

    """

    def __init__(self):
        r"""
        :param _Resource: 单独售卖Topic的Topic名称
        :type Resource: str
        :param _OffsetType: Offset类型，最开始位置earliest，最新位置latest，时间点位置timestamp
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetType: str
        :param _StartTime: Offset类型为timestamp时必传，传时间戳，精确到秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _TopicId: Topic的TopicId【出参】
        :type TopicId: str
        :param _CompressionType: 写入Topic时是否进行压缩，不开启填"none"，开启的话，可选择"gzip", "snappy", "lz4"中的一个进行填写。
        :type CompressionType: str
        :param _UseAutoCreateTopic: 使用的Topic是否需要自动创建（目前只支持SOURCE流入任务）
        :type UseAutoCreateTopic: bool
        :param _MsgMultiple: 源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
        :type MsgMultiple: int
        """
        self._Resource = None
        self._OffsetType = None
        self._StartTime = None
        self._TopicId = None
        self._CompressionType = None
        self._UseAutoCreateTopic = None
        self._MsgMultiple = None

    @property
    def Resource(self):
        """单独售卖Topic的Topic名称
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def OffsetType(self):
        """Offset类型，最开始位置earliest，最新位置latest，时间点位置timestamp
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OffsetType

    @OffsetType.setter
    def OffsetType(self, OffsetType):
        self._OffsetType = OffsetType

    @property
    def StartTime(self):
        """Offset类型为timestamp时必传，传时间戳，精确到秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TopicId(self):
        """Topic的TopicId【出参】
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CompressionType(self):
        """写入Topic时是否进行压缩，不开启填"none"，开启的话，可选择"gzip", "snappy", "lz4"中的一个进行填写。
        :rtype: str
        """
        return self._CompressionType

    @CompressionType.setter
    def CompressionType(self, CompressionType):
        self._CompressionType = CompressionType

    @property
    def UseAutoCreateTopic(self):
        """使用的Topic是否需要自动创建（目前只支持SOURCE流入任务）
        :rtype: bool
        """
        return self._UseAutoCreateTopic

    @UseAutoCreateTopic.setter
    def UseAutoCreateTopic(self, UseAutoCreateTopic):
        self._UseAutoCreateTopic = UseAutoCreateTopic

    @property
    def MsgMultiple(self):
        """源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
        :rtype: int
        """
        return self._MsgMultiple

    @MsgMultiple.setter
    def MsgMultiple(self, MsgMultiple):
        self._MsgMultiple = MsgMultiple


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._OffsetType = params.get("OffsetType")
        self._StartTime = params.get("StartTime")
        self._TopicId = params.get("TopicId")
        self._CompressionType = params.get("CompressionType")
        self._UseAutoCreateTopic = params.get("UseAutoCreateTopic")
        self._MsgMultiple = params.get("MsgMultiple")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicPartitionDO(AbstractModel):
    """分区详情

    """

    def __init__(self):
        r"""
        :param _Partition: Partition 分区ID
        :type Partition: int
        :param _LeaderStatus: Leader 运行状态
        :type LeaderStatus: int
        :param _IsrNum: ISR 个数
        :type IsrNum: int
        :param _ReplicaNum: 副本个数
        :type ReplicaNum: int
        """
        self._Partition = None
        self._LeaderStatus = None
        self._IsrNum = None
        self._ReplicaNum = None

    @property
    def Partition(self):
        """Partition 分区ID
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def LeaderStatus(self):
        """Leader 运行状态
        :rtype: int
        """
        return self._LeaderStatus

    @LeaderStatus.setter
    def LeaderStatus(self, LeaderStatus):
        self._LeaderStatus = LeaderStatus

    @property
    def IsrNum(self):
        """ISR 个数
        :rtype: int
        """
        return self._IsrNum

    @IsrNum.setter
    def IsrNum(self, IsrNum):
        self._IsrNum = IsrNum

    @property
    def ReplicaNum(self):
        """副本个数
        :rtype: int
        """
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum


    def _deserialize(self, params):
        self._Partition = params.get("Partition")
        self._LeaderStatus = params.get("LeaderStatus")
        self._IsrNum = params.get("IsrNum")
        self._ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicResult(AbstractModel):
    """统一返回的TopicResponse

    """

    def __init__(self):
        r"""
        :param _TopicList: 返回的主题信息列表
        :type TopicList: list of Topic
        :param _TotalCount: 符合条件的 topic 数量
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        """返回的主题信息列表
        :rtype: list of Topic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        """符合条件的 topic 数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Topic消息保留时间配置返回信息

    """

    def __init__(self):
        r"""
        :param _Expect: 期望值，即用户配置的Topic消息保留时间(单位分钟)
        :type Expect: int
        :param _Current: 当前值，即当前生效值(可能存在动态调整，单位分钟)
        :type Current: int
        :param _ModTimeStamp: 最近变更时间
        :type ModTimeStamp: int
        """
        self._Expect = None
        self._Current = None
        self._ModTimeStamp = None

    @property
    def Expect(self):
        """期望值，即用户配置的Topic消息保留时间(单位分钟)
        :rtype: int
        """
        return self._Expect

    @Expect.setter
    def Expect(self, Expect):
        self._Expect = Expect

    @property
    def Current(self):
        """当前值，即当前生效值(可能存在动态调整，单位分钟)
        :rtype: int
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def ModTimeStamp(self):
        """最近变更时间
        :rtype: int
        """
        return self._ModTimeStamp

    @ModTimeStamp.setter
    def ModTimeStamp(self, ModTimeStamp):
        self._ModTimeStamp = ModTimeStamp


    def _deserialize(self, params):
        self._Expect = params.get("Expect")
        self._Current = params.get("Current")
        self._ModTimeStamp = params.get("ModTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSubscribeGroup(AbstractModel):
    """DescribeTopicSubscribeGroup接口出参

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _StatusCountInfo: 消费分组状态数量信息
        :type StatusCountInfo: str
        :param _GroupsInfo: 消费分组信息
        :type GroupsInfo: list of GroupInfoResponse
        :param _Status: 此次请求是否异步的状态。实例里分组较少的会直接返回结果,Status为1。当分组较多时,会异步更新缓存，Status为0时不会返回分组信息，直至Status为1更新完毕返回结果。
        :type Status: int
        """
        self._TotalCount = None
        self._StatusCountInfo = None
        self._GroupsInfo = None
        self._Status = None

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
    def StatusCountInfo(self):
        """消费分组状态数量信息
        :rtype: str
        """
        return self._StatusCountInfo

    @StatusCountInfo.setter
    def StatusCountInfo(self, StatusCountInfo):
        self._StatusCountInfo = StatusCountInfo

    @property
    def GroupsInfo(self):
        """消费分组信息
        :rtype: list of GroupInfoResponse
        """
        return self._GroupsInfo

    @GroupsInfo.setter
    def GroupsInfo(self, GroupsInfo):
        self._GroupsInfo = GroupsInfo

    @property
    def Status(self):
        """此次请求是否异步的状态。实例里分组较少的会直接返回结果,Status为1。当分组较多时,会异步更新缓存，Status为0时不会返回分组信息，直至Status为1更新完毕返回结果。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._StatusCountInfo = params.get("StatusCountInfo")
        if params.get("GroupsInfo") is not None:
            self._GroupsInfo = []
            for item in params.get("GroupsInfo"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self._GroupsInfo.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformParam(AbstractModel):
    """数据处理参数

    """

    def __init__(self):
        r"""
        :param _AnalysisFormat: 解析格式，JSON，DELIMITER分隔符，REGULAR正则提取
        :type AnalysisFormat: str
        :param _OutputFormat: 输出格式
        :type OutputFormat: str
        :param _FailureParam: 是否保留解析失败数据
        :type FailureParam: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        :param _Content: 原始数据
        :type Content: str
        :param _SourceType: 数据来源，TOPIC从源topic拉取，CUSTOMIZE自定义
        :type SourceType: str
        :param _Regex: 分隔符、正则表达式
        :type Regex: str
        :param _MapParam: Map
        :type MapParam: list of MapParam
        :param _FilterParam: 过滤器
        :type FilterParam: list of FilterMapParam
        :param _Result: 测试结果
        :type Result: str
        :param _AnalyseResult: 解析结果
        :type AnalyseResult: list of MapParam
        :param _UseEventBus: 底层引擎是否使用eb
        :type UseEventBus: bool
        """
        self._AnalysisFormat = None
        self._OutputFormat = None
        self._FailureParam = None
        self._Content = None
        self._SourceType = None
        self._Regex = None
        self._MapParam = None
        self._FilterParam = None
        self._Result = None
        self._AnalyseResult = None
        self._UseEventBus = None

    @property
    def AnalysisFormat(self):
        """解析格式，JSON，DELIMITER分隔符，REGULAR正则提取
        :rtype: str
        """
        return self._AnalysisFormat

    @AnalysisFormat.setter
    def AnalysisFormat(self, AnalysisFormat):
        self._AnalysisFormat = AnalysisFormat

    @property
    def OutputFormat(self):
        """输出格式
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def FailureParam(self):
        """是否保留解析失败数据
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        """
        return self._FailureParam

    @FailureParam.setter
    def FailureParam(self, FailureParam):
        self._FailureParam = FailureParam

    @property
    def Content(self):
        """原始数据
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SourceType(self):
        """数据来源，TOPIC从源topic拉取，CUSTOMIZE自定义
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Regex(self):
        """分隔符、正则表达式
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def MapParam(self):
        """Map
        :rtype: list of MapParam
        """
        return self._MapParam

    @MapParam.setter
    def MapParam(self, MapParam):
        self._MapParam = MapParam

    @property
    def FilterParam(self):
        """过滤器
        :rtype: list of FilterMapParam
        """
        return self._FilterParam

    @FilterParam.setter
    def FilterParam(self, FilterParam):
        self._FilterParam = FilterParam

    @property
    def Result(self):
        """测试结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AnalyseResult(self):
        """解析结果
        :rtype: list of MapParam
        """
        return self._AnalyseResult

    @AnalyseResult.setter
    def AnalyseResult(self, AnalyseResult):
        self._AnalyseResult = AnalyseResult

    @property
    def UseEventBus(self):
        """底层引擎是否使用eb
        :rtype: bool
        """
        return self._UseEventBus

    @UseEventBus.setter
    def UseEventBus(self, UseEventBus):
        self._UseEventBus = UseEventBus


    def _deserialize(self, params):
        self._AnalysisFormat = params.get("AnalysisFormat")
        self._OutputFormat = params.get("OutputFormat")
        if params.get("FailureParam") is not None:
            self._FailureParam = FailureParam()
            self._FailureParam._deserialize(params.get("FailureParam"))
        self._Content = params.get("Content")
        self._SourceType = params.get("SourceType")
        self._Regex = params.get("Regex")
        if params.get("MapParam") is not None:
            self._MapParam = []
            for item in params.get("MapParam"):
                obj = MapParam()
                obj._deserialize(item)
                self._MapParam.append(obj)
        if params.get("FilterParam") is not None:
            self._FilterParam = []
            for item in params.get("FilterParam"):
                obj = FilterMapParam()
                obj._deserialize(item)
                self._FilterParam.append(obj)
        self._Result = params.get("Result")
        if params.get("AnalyseResult") is not None:
            self._AnalyseResult = []
            for item in params.get("AnalyseResult"):
                obj = MapParam()
                obj._deserialize(item)
                self._AnalyseResult.append(obj)
        self._UseEventBus = params.get("UseEventBus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformsParam(AbstractModel):
    """数据处理参数

    """

    def __init__(self):
        r"""
        :param _Content: 原始数据
        :type Content: str
        :param _FieldChain: 处理链
        :type FieldChain: list of FieldParam
        :param _FilterParam: 过滤器
        :type FilterParam: list of FilterMapParam
        :param _FailureParam: 失败处理
        :type FailureParam: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        :param _Result: 测试结果
        :type Result: str
        :param _SourceType: 数据来源
        :type SourceType: str
        :param _OutputFormat: 输出格式，JSON，ROW，默认为JSON
        :type OutputFormat: str
        :param _RowParam: 输出格式为ROW必填
        :type RowParam: :class:`tencentcloud.ckafka.v20190819.models.RowParam`
        :param _KeepMetadata: 是否保留数据源Topic元数据信息（源Topic、Partition、Offset），默认为false
        :type KeepMetadata: bool
        :param _BatchAnalyse: 数组解析
        :type BatchAnalyse: :class:`tencentcloud.ckafka.v20190819.models.BatchAnalyseParam`
        """
        self._Content = None
        self._FieldChain = None
        self._FilterParam = None
        self._FailureParam = None
        self._Result = None
        self._SourceType = None
        self._OutputFormat = None
        self._RowParam = None
        self._KeepMetadata = None
        self._BatchAnalyse = None

    @property
    def Content(self):
        """原始数据
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FieldChain(self):
        """处理链
        :rtype: list of FieldParam
        """
        return self._FieldChain

    @FieldChain.setter
    def FieldChain(self, FieldChain):
        self._FieldChain = FieldChain

    @property
    def FilterParam(self):
        """过滤器
        :rtype: list of FilterMapParam
        """
        return self._FilterParam

    @FilterParam.setter
    def FilterParam(self, FilterParam):
        self._FilterParam = FilterParam

    @property
    def FailureParam(self):
        """失败处理
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        """
        return self._FailureParam

    @FailureParam.setter
    def FailureParam(self, FailureParam):
        self._FailureParam = FailureParam

    @property
    def Result(self):
        """测试结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SourceType(self):
        """数据来源
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def OutputFormat(self):
        """输出格式，JSON，ROW，默认为JSON
        :rtype: str
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def RowParam(self):
        """输出格式为ROW必填
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RowParam`
        """
        return self._RowParam

    @RowParam.setter
    def RowParam(self, RowParam):
        self._RowParam = RowParam

    @property
    def KeepMetadata(self):
        """是否保留数据源Topic元数据信息（源Topic、Partition、Offset），默认为false
        :rtype: bool
        """
        return self._KeepMetadata

    @KeepMetadata.setter
    def KeepMetadata(self, KeepMetadata):
        self._KeepMetadata = KeepMetadata

    @property
    def BatchAnalyse(self):
        """数组解析
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchAnalyseParam`
        """
        return self._BatchAnalyse

    @BatchAnalyse.setter
    def BatchAnalyse(self, BatchAnalyse):
        self._BatchAnalyse = BatchAnalyse


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("FieldChain") is not None:
            self._FieldChain = []
            for item in params.get("FieldChain"):
                obj = FieldParam()
                obj._deserialize(item)
                self._FieldChain.append(obj)
        if params.get("FilterParam") is not None:
            self._FilterParam = []
            for item in params.get("FilterParam"):
                obj = FilterMapParam()
                obj._deserialize(item)
                self._FilterParam.append(obj)
        if params.get("FailureParam") is not None:
            self._FailureParam = FailureParam()
            self._FailureParam._deserialize(params.get("FailureParam"))
        self._Result = params.get("Result")
        self._SourceType = params.get("SourceType")
        self._OutputFormat = params.get("OutputFormat")
        if params.get("RowParam") is not None:
            self._RowParam = RowParam()
            self._RowParam._deserialize(params.get("RowParam"))
        self._KeepMetadata = params.get("KeepMetadata")
        if params.get("BatchAnalyse") is not None:
            self._BatchAnalyse = BatchAnalyseParam()
            self._BatchAnalyse._deserialize(params.get("BatchAnalyse"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlDecodeParam(AbstractModel):
    """Url解析

    """

    def __init__(self):
        r"""
        :param _CharsetName: 编码
        :type CharsetName: str
        """
        self._CharsetName = None

    @property
    def CharsetName(self):
        """编码
        :rtype: str
        """
        return self._CharsetName

    @CharsetName.setter
    def CharsetName(self, CharsetName):
        self._CharsetName = CharsetName


    def _deserialize(self, params):
        self._CharsetName = params.get("CharsetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户实体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户id
        :type UserId: int
        :param _Name: 用户名称
        :type Name: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后更新时间
        :type UpdateTime: str
        """
        self._UserId = None
        self._Name = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def UserId(self):
        """用户id
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        """用户名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def UpdateTime(self):
        """最后更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResponse(AbstractModel):
    """用户返回实体

    """

    def __init__(self):
        r"""
        :param _Users: 符合条件的用户列表
        :type Users: list of User
        :param _TotalCount: 符合条件的总用户数
        :type TotalCount: int
        """
        self._Users = None
        self._TotalCount = None

    @property
    def Users(self):
        """符合条件的用户列表
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def TotalCount(self):
        """符合条件的总用户数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueParam(AbstractModel):
    """数据处理——Value处理参数

    """

    def __init__(self):
        r"""
        :param _Type: 处理模式，REPLACE替换，SUBSTR截取，DATE日期转换，TRIM去除前后空格，REGEX_REPLACE正则替换，URL_DECODE，LOWERCASE转换为小写
        :type Type: str
        :param _Replace: 替换，TYPE=REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type Replace: :class:`tencentcloud.ckafka.v20190819.models.ReplaceParam`
        :param _Substr: 截取，TYPE=SUBSTR时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type Substr: :class:`tencentcloud.ckafka.v20190819.models.SubstrParam`
        :param _Date: 时间转换，TYPE=DATE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: :class:`tencentcloud.ckafka.v20190819.models.DateParam`
        :param _RegexReplace: 正则替换，TYPE=REGEX_REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type RegexReplace: :class:`tencentcloud.ckafka.v20190819.models.RegexReplaceParam`
        :param _Split: 值支持一拆多，TYPE=SPLIT时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type Split: :class:`tencentcloud.ckafka.v20190819.models.SplitParam`
        :param _KV: key-value二次解析，TYPE=KV时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type KV: :class:`tencentcloud.ckafka.v20190819.models.KVParam`
        :param _Result: 处理结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _JsonPathReplace: JsonPath替换，TYPE=JSON_PATH_REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonPathReplace: :class:`tencentcloud.ckafka.v20190819.models.JsonPathReplaceParam`
        :param _UrlDecode: Url解析
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlDecode: :class:`tencentcloud.ckafka.v20190819.models.UrlDecodeParam`
        :param _Lowercase: 小写字符解析
注意：此字段可能返回 null，表示取不到有效值。
        :type Lowercase: :class:`tencentcloud.ckafka.v20190819.models.LowercaseParam`
        """
        self._Type = None
        self._Replace = None
        self._Substr = None
        self._Date = None
        self._RegexReplace = None
        self._Split = None
        self._KV = None
        self._Result = None
        self._JsonPathReplace = None
        self._UrlDecode = None
        self._Lowercase = None

    @property
    def Type(self):
        """处理模式，REPLACE替换，SUBSTR截取，DATE日期转换，TRIM去除前后空格，REGEX_REPLACE正则替换，URL_DECODE，LOWERCASE转换为小写
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Replace(self):
        """替换，TYPE=REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ReplaceParam`
        """
        return self._Replace

    @Replace.setter
    def Replace(self, Replace):
        self._Replace = Replace

    @property
    def Substr(self):
        """截取，TYPE=SUBSTR时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SubstrParam`
        """
        return self._Substr

    @Substr.setter
    def Substr(self, Substr):
        self._Substr = Substr

    @property
    def Date(self):
        """时间转换，TYPE=DATE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DateParam`
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def RegexReplace(self):
        """正则替换，TYPE=REGEX_REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RegexReplaceParam`
        """
        return self._RegexReplace

    @RegexReplace.setter
    def RegexReplace(self, RegexReplace):
        self._RegexReplace = RegexReplace

    @property
    def Split(self):
        """值支持一拆多，TYPE=SPLIT时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SplitParam`
        """
        return self._Split

    @Split.setter
    def Split(self, Split):
        self._Split = Split

    @property
    def KV(self):
        """key-value二次解析，TYPE=KV时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.KVParam`
        """
        return self._KV

    @KV.setter
    def KV(self, KV):
        self._KV = KV

    @property
    def Result(self):
        """处理结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def JsonPathReplace(self):
        """JsonPath替换，TYPE=JSON_PATH_REPLACE时必传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.JsonPathReplaceParam`
        """
        return self._JsonPathReplace

    @JsonPathReplace.setter
    def JsonPathReplace(self, JsonPathReplace):
        self._JsonPathReplace = JsonPathReplace

    @property
    def UrlDecode(self):
        """Url解析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.UrlDecodeParam`
        """
        return self._UrlDecode

    @UrlDecode.setter
    def UrlDecode(self, UrlDecode):
        self._UrlDecode = UrlDecode

    @property
    def Lowercase(self):
        """小写字符解析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.LowercaseParam`
        """
        return self._Lowercase

    @Lowercase.setter
    def Lowercase(self, Lowercase):
        self._Lowercase = Lowercase


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Replace") is not None:
            self._Replace = ReplaceParam()
            self._Replace._deserialize(params.get("Replace"))
        if params.get("Substr") is not None:
            self._Substr = SubstrParam()
            self._Substr._deserialize(params.get("Substr"))
        if params.get("Date") is not None:
            self._Date = DateParam()
            self._Date._deserialize(params.get("Date"))
        if params.get("RegexReplace") is not None:
            self._RegexReplace = RegexReplaceParam()
            self._RegexReplace._deserialize(params.get("RegexReplace"))
        if params.get("Split") is not None:
            self._Split = SplitParam()
            self._Split._deserialize(params.get("Split"))
        if params.get("KV") is not None:
            self._KV = KVParam()
            self._KV._deserialize(params.get("KV"))
        self._Result = params.get("Result")
        if params.get("JsonPathReplace") is not None:
            self._JsonPathReplace = JsonPathReplaceParam()
            self._JsonPathReplace._deserialize(params.get("JsonPathReplace"))
        if params.get("UrlDecode") is not None:
            self._UrlDecode = UrlDecodeParam()
            self._UrlDecode._deserialize(params.get("UrlDecode"))
        if params.get("Lowercase") is not None:
            self._Lowercase = LowercaseParam()
            self._Lowercase._deserialize(params.get("Lowercase"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipEntity(AbstractModel):
    """虚拟IP实体

    """

    def __init__(self):
        r"""
        :param _Vip: 虚拟IP
        :type Vip: str
        :param _Vport: 虚拟端口
        :type Vport: str
        """
        self._Vip = None
        self._Vport = None

    @property
    def Vip(self):
        """虚拟IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """虚拟端口
        :rtype: str
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """zone信息实体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区
        :type ZoneId: str
        :param _IsInternalApp: 是否内部APP
        :type IsInternalApp: int
        :param _AppId: 应用标识
        :type AppId: int
        :param _Flag: 标识
        :type Flag: bool
        :param _ZoneName: 可用区名称
        :type ZoneName: str
        :param _ZoneStatus: 可用区状态
        :type ZoneStatus: int
        :param _Exflag: 额外标识
        :type Exflag: str
        :param _SoldOut: true为售罄，false为未售罄
        :type SoldOut: str
        :param _SalesInfo: 标准版售罄信息
        :type SalesInfo: list of SaleInfo
        :param _ExtraFlag: 额外标识
        :type ExtraFlag: str
        """
        self._ZoneId = None
        self._IsInternalApp = None
        self._AppId = None
        self._Flag = None
        self._ZoneName = None
        self._ZoneStatus = None
        self._Exflag = None
        self._SoldOut = None
        self._SalesInfo = None
        self._ExtraFlag = None

    @property
    def ZoneId(self):
        """可用区
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsInternalApp(self):
        """是否内部APP
        :rtype: int
        """
        return self._IsInternalApp

    @IsInternalApp.setter
    def IsInternalApp(self, IsInternalApp):
        self._IsInternalApp = IsInternalApp

    @property
    def AppId(self):
        """应用标识
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Flag(self):
        """标识
        :rtype: bool
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ZoneName(self):
        """可用区名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneStatus(self):
        """可用区状态
        :rtype: int
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus

    @property
    def Exflag(self):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        """额外标识
        :rtype: str
        """
        return self._Exflag

    @Exflag.setter
    def Exflag(self, Exflag):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        self._Exflag = Exflag

    @property
    def SoldOut(self):
        """true为售罄，false为未售罄
        :rtype: str
        """
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut

    @property
    def SalesInfo(self):
        """标准版售罄信息
        :rtype: list of SaleInfo
        """
        return self._SalesInfo

    @SalesInfo.setter
    def SalesInfo(self, SalesInfo):
        self._SalesInfo = SalesInfo

    @property
    def ExtraFlag(self):
        """额外标识
        :rtype: str
        """
        return self._ExtraFlag

    @ExtraFlag.setter
    def ExtraFlag(self, ExtraFlag):
        self._ExtraFlag = ExtraFlag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._IsInternalApp = params.get("IsInternalApp")
        self._AppId = params.get("AppId")
        self._Flag = params.get("Flag")
        self._ZoneName = params.get("ZoneName")
        self._ZoneStatus = params.get("ZoneStatus")
        self._Exflag = params.get("Exflag")
        self._SoldOut = params.get("SoldOut")
        if params.get("SalesInfo") is not None:
            self._SalesInfo = []
            for item in params.get("SalesInfo"):
                obj = SaleInfo()
                obj._deserialize(item)
                self._SalesInfo.append(obj)
        self._ExtraFlag = params.get("ExtraFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    """查询kafka的zone信息返回的实体

    """

    def __init__(self):
        r"""
        :param _ZoneList: zone列表
        :type ZoneList: list of ZoneInfo
        :param _MaxBuyInstanceNum: 最大购买实例个数
        :type MaxBuyInstanceNum: int
        :param _MaxBandwidth: 最大购买带宽 单位Mb/s
        :type MaxBandwidth: int
        :param _UnitPrice: 后付费单位价格
        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _MessagePrice: 后付费消息单价
        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param _ClusterInfo: 用户独占集群信息
        :type ClusterInfo: list of ClusterInfo
        :param _Standard: 购买标准版配置
        :type Standard: str
        :param _StandardS2: 购买标准版S2配置
        :type StandardS2: str
        :param _Profession: 购买专业版配置
        :type Profession: str
        :param _Physical: 购买物理独占版配置
        :type Physical: str
        :param _PublicNetwork: 公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :type PublicNetwork: str
        :param _PublicNetworkLimit: 公网带宽配置
        :type PublicNetworkLimit: str
        :param _RequestId: 请求Id
        :type RequestId: str
        :param _Version: 版本
        :type Version: str
        :param _Offset: 分页offset
        :type Offset: int
        :param _Limit: 分页limit
        :type Limit: int
        :param _ForceCheckTag: 是否必须录入tag
        :type ForceCheckTag: bool
        """
        self._ZoneList = None
        self._MaxBuyInstanceNum = None
        self._MaxBandwidth = None
        self._UnitPrice = None
        self._MessagePrice = None
        self._ClusterInfo = None
        self._Standard = None
        self._StandardS2 = None
        self._Profession = None
        self._Physical = None
        self._PublicNetwork = None
        self._PublicNetworkLimit = None
        self._RequestId = None
        self._Version = None
        self._Offset = None
        self._Limit = None
        self._ForceCheckTag = None

    @property
    def ZoneList(self):
        """zone列表
        :rtype: list of ZoneInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def MaxBuyInstanceNum(self):
        """最大购买实例个数
        :rtype: int
        """
        return self._MaxBuyInstanceNum

    @MaxBuyInstanceNum.setter
    def MaxBuyInstanceNum(self, MaxBuyInstanceNum):
        self._MaxBuyInstanceNum = MaxBuyInstanceNum

    @property
    def MaxBandwidth(self):
        """最大购买带宽 单位Mb/s
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def UnitPrice(self):
        """后付费单位价格
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def MessagePrice(self):
        """后付费消息单价
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.Price`
        """
        return self._MessagePrice

    @MessagePrice.setter
    def MessagePrice(self, MessagePrice):
        self._MessagePrice = MessagePrice

    @property
    def ClusterInfo(self):
        """用户独占集群信息
        :rtype: list of ClusterInfo
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def Standard(self):
        """购买标准版配置
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def StandardS2(self):
        """购买标准版S2配置
        :rtype: str
        """
        return self._StandardS2

    @StandardS2.setter
    def StandardS2(self, StandardS2):
        self._StandardS2 = StandardS2

    @property
    def Profession(self):
        """购买专业版配置
        :rtype: str
        """
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def Physical(self):
        """购买物理独占版配置
        :rtype: str
        """
        return self._Physical

    @Physical.setter
    def Physical(self, Physical):
        self._Physical = Physical

    @property
    def PublicNetwork(self):
        """公网带宽 最小3Mbps  最大999Mbps 仅专业版支持填写
        :rtype: str
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def PublicNetworkLimit(self):
        """公网带宽配置
        :rtype: str
        """
        return self._PublicNetworkLimit

    @PublicNetworkLimit.setter
    def PublicNetworkLimit(self, PublicNetworkLimit):
        self._PublicNetworkLimit = PublicNetworkLimit

    @property
    def RequestId(self):
        """请求Id
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Version(self):
        """版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Offset(self):
        """分页offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ForceCheckTag(self):
        """是否必须录入tag
        :rtype: bool
        """
        return self._ForceCheckTag

    @ForceCheckTag.setter
    def ForceCheckTag(self, ForceCheckTag):
        self._ForceCheckTag = ForceCheckTag


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._MaxBuyInstanceNum = params.get("MaxBuyInstanceNum")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("UnitPrice") is not None:
            self._UnitPrice = Price()
            self._UnitPrice._deserialize(params.get("UnitPrice"))
        if params.get("MessagePrice") is not None:
            self._MessagePrice = Price()
            self._MessagePrice._deserialize(params.get("MessagePrice"))
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = []
            for item in params.get("ClusterInfo"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self._ClusterInfo.append(obj)
        self._Standard = params.get("Standard")
        self._StandardS2 = params.get("StandardS2")
        self._Profession = params.get("Profession")
        self._Physical = params.get("Physical")
        self._PublicNetwork = params.get("PublicNetwork")
        self._PublicNetworkLimit = params.get("PublicNetworkLimit")
        self._RequestId = params.get("RequestId")
        self._Version = params.get("Version")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ForceCheckTag = params.get("ForceCheckTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        