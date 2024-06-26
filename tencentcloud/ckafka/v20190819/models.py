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
注意：此字段可能返回 null，表示取不到有效值。
        :type Principal: str
        :param _Host: 默认\*,表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Principal(self):
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type AclList: list of Acl
        """
        self._TotalCount = None
        self._AclList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclList(self):
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
        :param _RuleName: Acl规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _PatternType: 匹配类型，目前只支持前缀匹配，枚举值列表：PREFIXED
注意：此字段可能返回 null，表示取不到有效值。
        :type PatternType: str
        :param _Pattern: 表示前缀匹配的前缀的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Pattern: str
        :param _ResourceType: Acl资源类型,目前只支持Topic,枚举值列表：Topic
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _AclList: 该规则所包含的ACL信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AclList: str
        :param _CreateTimeStamp: 规则所创建的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTimeStamp: str
        :param _IsApplied: 预设ACL规则是否应用到新增的topic中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsApplied: int
        :param _UpdateTimeStamp: 规则更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTimeStamp: str
        :param _Comment: 规则的备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _TopicName: 其中一个显示的对应的TopicName
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _TopicCount: 应用该ACL规则的Topic数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicCount: int
        :param _PatternTypeTitle: patternType的中文显示
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PatternType(self):
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def AclList(self):
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def CreateTimeStamp(self):
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def IsApplied(self):
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def UpdateTimeStamp(self):
        return self._UpdateTimeStamp

    @UpdateTimeStamp.setter
    def UpdateTimeStamp(self, UpdateTimeStamp):
        self._UpdateTimeStamp = UpdateTimeStamp

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicCount(self):
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def PatternTypeTitle(self):
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
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type AclRuleList: list of AclRule
        """
        self._TotalCount = None
        self._AclRuleList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AclRuleList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        :param _InputValueType: 需再次处理的KEY——模式
注意：此字段可能返回 null，表示取不到有效值。
        :type InputValueType: str
        :param _InputValue: 需再次处理的KEY——KEY表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type InputValue: str
        """
        self._Format = None
        self._Regex = None
        self._InputValueType = None
        self._InputValue = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def InputValueType(self):
        return self._InputValueType

    @InputValueType.setter
    def InputValueType(self, InputValueType):
        self._InputValueType = InputValueType

    @property
    def InputValue(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of int
        """
        self._TotalCount = None
        self._AppIdList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AppIdList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of GroupInfoTopics
        """
        self._Version = None
        self._Topics = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Topics(self):
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
        :param _InstanceId: 实例ID
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tokens(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
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
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
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
        :param _InstanceId: 实例ID
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceNames(self):
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def RuleList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例名称
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
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def TopicName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Topic: 主题属性列表
        :type Topic: list of BatchModifyTopicInfo
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _TopicName: topic名称
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

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def CleanUpPolicy(self):
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def MinInsyncReplicas(self):
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def RetentionBytes(self):
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def SegmentMs(self):
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes


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
        :param _InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _TopicName: topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _ReturnCode: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: str
        :param _Message: 状态消息
        :type Message: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._ReturnCode = None
        self._Message = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Message(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _TopicId: 主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _DataSize: 主题占用Broker 容量大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSize: int
        """
        self._TopicName = None
        self._TopicId = None
        self._DataSize = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DataSize(self):
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
        :param _TopicName: Topic 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _TopicId: Topic Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicTraffic: Topic 流量(MB)
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicTraffic: str
        """
        self._TopicName = None
        self._TopicId = None
        self._TopicTraffic = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicTraffic(self):
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
        :param _InstanceId: 实例ID
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tokens(self):
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
        :param _Result: 0 成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: ClickHouse连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: ClickHouse连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: ClickHouse连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SelfBuilt: ClickHouse连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _ServiceVip: ClickHouse连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: ClickHouse连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: ClickHouse的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: ClickHouse连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: ClickHouse连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: ClickHouse连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: ClickHouse连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _SelfBuilt: ClickHouse连接源是否为自建集群【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务，默认为true
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param _Database: ClickHouse的数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: ClickHouse的数据表名
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Schema: ClickHouse的schema
注意：此字段可能返回 null，表示取不到有效值。
        :type Schema: list of ClickHouseSchema
        :param _Resource: 实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Ip: ClickHouse的连接ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: ClickHouse的连接port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: ClickHouse的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: ClickHouse的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _ServiceVip: 实例vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: 实例的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _DropInvalidMessage: ClickHouse是否抛弃解析失败的消息，默认为true
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidMessage: bool
        :param _Type: ClickHouse 类型，emr-clickhouse : "emr";cdw-clickhouse : "cdwch";自建 : ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
注意：此字段可能返回 null，表示取不到有效值。
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _BatchSize: 每批次投递到 ClickHouse 表消息数量，默认为 1000 条。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _ConsumerFetchMinBytes: 每次从 topic 中拉取消息大小，默认为 1MB，即至少要从 topic 中批量拉取 1MB 消息，才进行数据投递到 ClickHouse 操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerFetchMinBytes: int
        :param _ConsumerFetchMaxWaitMs: 每次从 topic 拉取消息最大等待时间，当超过当前最大等待时间时，即使没有拉取到 ConsumerFetchMinBytes 大小，也将进行 ClickHouse 投递操作。
提高该参数值，有利于减少往  ClickHouse 投递的次数，但在错误消息过多及网络不稳定等极端情况下时，可能导致频繁重试影响效率。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def DropInvalidMessage(self):
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DropCls(self):
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def BatchSize(self):
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def ConsumerFetchMinBytes(self):
        return self._ConsumerFetchMinBytes

    @ConsumerFetchMinBytes.setter
    def ConsumerFetchMinBytes(self, ConsumerFetchMinBytes):
        self._ConsumerFetchMinBytes = ConsumerFetchMinBytes

    @property
    def ConsumerFetchMaxWaitMs(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnName: str
        :param _JsonKey: 该列对应的jsonKey名
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonKey: str
        :param _Type: 表列项的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _AllowNull: 列项是否允许为空
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowNull: bool
        """
        self._ColumnName = None
        self._JsonKey = None
        self._Type = None
        self._AllowNull = None

    @property
    def ColumnName(self):
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def JsonKey(self):
        return self._JsonKey

    @JsonKey.setter
    def JsonKey(self, JsonKey):
        self._JsonKey = JsonKey

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowNull(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DecodeJson: bool
        :param _Resource: cls日志主题id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _LogSet: cls日志集id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSet: str
        :param _ContentKey: 当DecodeJson为false时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentKey: str
        :param _TimeField: 指定消息中的某字段内容作为cls日志的时间。
字段内容格式需要是秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeField: str
        """
        self._DecodeJson = None
        self._Resource = None
        self._LogSet = None
        self._ContentKey = None
        self._TimeField = None

    @property
    def DecodeJson(self):
        return self._DecodeJson

    @DecodeJson.setter
    def DecodeJson(self, DecodeJson):
        self._DecodeJson = DecodeJson

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def ContentKey(self):
        return self._ContentKey

    @ContentKey.setter
    def ContentKey(self, ContentKey):
        self._ContentKey = ContentKey

    @property
    def TimeField(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSize: int
        :param _MaxBandWidth: 集群最大带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBandWidth: int
        :param _AvailableDiskSize: 集群当前可用磁盘  单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableDiskSize: int
        :param _AvailableBandWidth: 集群当前可用带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableBandWidth: int
        :param _ZoneId: 集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MaxDiskSize(self):
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MaxBandWidth(self):
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def AvailableDiskSize(self):
        return self._AvailableDiskSize

    @AvailableDiskSize.setter
    def AvailableDiskSize(self, AvailableDiskSize):
        self._AvailableDiskSize = AvailableDiskSize

    @property
    def AvailableBandWidth(self):
        return self._AvailableBandWidth

    @AvailableBandWidth.setter
    def AvailableBandWidth(self, AvailableBandWidth):
        self._AvailableBandWidth = AvailableBandWidth

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIds(self):
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
注意：此字段可能返回 null，表示取不到有效值。
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
        """
        self._Retention = None
        self._MinInsyncReplicas = None
        self._CleanUpPolicy = None
        self._SegmentMs = None
        self._UncleanLeaderElectionEnable = None
        self._SegmentBytes = None
        self._MaxMessageBytes = None
        self._RetentionBytes = None

    @property
    def Retention(self):
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def MinInsyncReplicas(self):
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def CleanUpPolicy(self):
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def SegmentMs(self):
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def UncleanLeaderElectionEnable(self):
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def SegmentBytes(self):
        return self._SegmentBytes

    @SegmentBytes.setter
    def SegmentBytes(self, SegmentBytes):
        self._SegmentBytes = SegmentBytes

    @property
    def MaxMessageBytes(self):
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def RetentionBytes(self):
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes


    def _deserialize(self, params):
        self._Retention = params.get("Retention")
        self._MinInsyncReplicas = params.get("MinInsyncReplicas")
        self._CleanUpPolicy = params.get("CleanUpPolicy")
        self._SegmentMs = params.get("SegmentMs")
        self._UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self._SegmentBytes = params.get("SegmentBytes")
        self._MaxMessageBytes = params.get("MaxMessageBytes")
        self._RetentionBytes = params.get("RetentionBytes")
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
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
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _GroupId: 消费组ID
        :type GroupId: str
        :param _TopicId: Topic的Id
        :type TopicId: str
        """
        self._TopicName = None
        self._GroupId = None
        self._TopicId = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TopicId(self):
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
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def SubscribedInfo(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of ConsumerGroupTopic
        :param _GroupList: 消费分组List
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of ConsumerGroup
        :param _TotalPartition: 所有分区数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPartition: int
        :param _PartitionListForMonitor: 监控的分区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionListForMonitor: list of Partition
        :param _TotalTopic: 主题总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTopic: int
        :param _TopicListForMonitor: 监控的主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param _GroupListForMonitor: 监控的组列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def TotalPartition(self):
        return self._TotalPartition

    @TotalPartition.setter
    def TotalPartition(self, TotalPartition):
        self._TotalPartition = TotalPartition

    @property
    def PartitionListForMonitor(self):
        return self._PartitionListForMonitor

    @PartitionListForMonitor.setter
    def PartitionListForMonitor(self, PartitionListForMonitor):
        self._PartitionListForMonitor = PartitionListForMonitor

    @property
    def TotalTopic(self):
        return self._TotalTopic

    @TotalTopic.setter
    def TotalTopic(self, TotalTopic):
        self._TotalTopic = TotalTopic

    @property
    def TopicListForMonitor(self):
        return self._TopicListForMonitor

    @TopicListForMonitor.setter
    def TopicListForMonitor(self, TopicListForMonitor):
        self._TopicListForMonitor = TopicListForMonitor

    @property
    def GroupListForMonitor(self):
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
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Speed(self):
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
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Headers(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketName: str
        :param _Region: 地域代码
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _ObjectKey: 对象名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectKey: str
        :param _AggregateBatchSize: 汇聚消息量的大小（单位：MB)
注意：此字段可能返回 null，表示取不到有效值。
        :type AggregateBatchSize: int
        :param _AggregateInterval: 汇聚的时间间隔（单位：小时）
注意：此字段可能返回 null，表示取不到有效值。
        :type AggregateInterval: int
        :param _FormatOutputType: 消息汇聚后的文件格式（支持csv, json）
注意：此字段可能返回 null，表示取不到有效值。
        :type FormatOutputType: str
        :param _ObjectKeyPrefix: 转储的对象目录前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectKeyPrefix: str
        :param _DirectoryTimeFormat: 根据strptime 时间格式化的分区格式
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ObjectKey(self):
        return self._ObjectKey

    @ObjectKey.setter
    def ObjectKey(self, ObjectKey):
        self._ObjectKey = ObjectKey

    @property
    def AggregateBatchSize(self):
        return self._AggregateBatchSize

    @AggregateBatchSize.setter
    def AggregateBatchSize(self, AggregateBatchSize):
        self._AggregateBatchSize = AggregateBatchSize

    @property
    def AggregateInterval(self):
        return self._AggregateInterval

    @AggregateInterval.setter
    def AggregateInterval(self, AggregateInterval):
        self._AggregateInterval = AggregateInterval

    @property
    def FormatOutputType(self):
        return self._FormatOutputType

    @FormatOutputType.setter
    def FormatOutputType(self, FormatOutputType):
        self._FormatOutputType = FormatOutputType

    @property
    def ObjectKeyPrefix(self):
        return self._ObjectKeyPrefix

    @ObjectKeyPrefix.setter
    def ObjectKeyPrefix(self, ObjectKeyPrefix):
        self._ObjectKeyPrefix = ObjectKeyPrefix

    @property
    def DirectoryTimeFormat(self):
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
        :param _InstanceId: 实例id信息
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param _Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param _PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
        return self._Principal

    @Principal.setter
    def Principal(self, Principal):
        self._Principal = Principal

    @property
    def ResourceNameList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id信息
        :type InstanceId: str
        :param _ResourceType: Acl资源类型,目前只支持Topic,枚举值列表：Topic
        :type ResourceType: str
        :param _PatternType: 匹配类型，目前支持前缀匹配与预设策略，枚举值列表：PREFIXED/PRESET
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def PatternType(self):
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def IsApplied(self):
        return self._IsApplied

    @IsApplied.setter
    def IsApplied(self, IsApplied):
        self._IsApplied = IsApplied

    @property
    def Comment(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Bandwidth: cdc集群的总带宽
        :type Bandwidth: int
        :param _DiskSize: cdc集群的总磁盘
        :type DiskSize: int
        :param _DiskType: 数据盘类型
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
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def CdcVpcId(self):
        return self._CdcVpcId

    @CdcVpcId.setter
    def CdcVpcId(self, CdcVpcId):
        self._CdcVpcId = CdcVpcId

    @property
    def CdcSubnetId(self):
        return self._CdcSubnetId

    @CdcSubnetId.setter
    def CdcSubnetId(self, CdcSubnetId):
        self._CdcSubnetId = CdcSubnetId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def SystemDiskType(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DtsConnectParam(self):
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def DorisConnectParam(self):
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _GroupName: group名称
        :type GroupName: str
        :param _TopicName: topic名称，TopicName、TopicNameList 需要显示指定一个存在的topic名称
        :type TopicName: str
        :param _TopicNameList: topic名称数组
        :type TopicNameList: list of str
        """
        self._InstanceId = None
        self._GroupName = None
        self._TopicName = None
        self._TopicNameList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
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
        :param _Result: 创建group描述
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _TaskId: 任务ID
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
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def SourceResource(self):
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def TransformParam(self):
        return self._TransformParam

    @TransformParam.setter
    def TransformParam(self, TransformParam):
        self._TransformParam = TransformParam

    @property
    def PrivateLinkParam(self):
        return self._PrivateLinkParam

    @PrivateLinkParam.setter
    def PrivateLinkParam(self, PrivateLinkParam):
        self._PrivateLinkParam = PrivateLinkParam

    @property
    def SchemaId(self):
        return self._SchemaId

    @SchemaId.setter
    def SchemaId(self, SchemaId):
        self._SchemaId = SchemaId

    @property
    def TransformsParam(self):
        return self._TransformsParam

    @TransformsParam.setter
    def TransformsParam(self, TransformsParam):
        self._TransformsParam = TransformsParam

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Tags(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DatahubId: str
        """
        self._TaskId = None
        self._DatahubId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DatahubId(self):
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
        :param _Result: 任务id
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTaskRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _DealNames: 订单号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _InstanceId: 实例Id，当购买多个实例时，默认返回购买的第一个实例 id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: 订单和购买实例对应映射列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
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
        :param _InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _VpcId: 创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
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

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def BandWidth(self):
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


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
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostData`
        """
        self._ReturnCode = None
        self._ReturnMessage = None
        self._Data = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _DealNames: 订单号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _InstanceId: 实例Id，当购买多个实例时，默认返回购买的第一个实例 id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _DealNameInstanceIdMapping: 订单和购买实例对应映射列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNameInstanceIdMapping: list of DealInstanceDTO
        """
        self._FlowId = None
        self._DealNames = None
        self._InstanceId = None
        self._DealNameInstanceIdMapping = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNameInstanceIdMapping(self):
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
        :param _InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _ZoneId: 可用区。当购买多可用区实例时，当前参数为主可用区。需要保证传入的参数和 SubnetId 所在子网属于同一个可用区
        :type ZoneId: int
        :param _Period: 预付费购买时长，例如 "1m",就是一个月
        :type Period: str
        :param _InstanceType: 国际站标准版实例规格。目前只有国际站标准版使用当前字段区分规格，国内站标准版使用峰值带宽区分规格。除了国际站标准版外的所有实例填写 1 即可。国际站标准版实例：入门型(general)]填写1；[标准型(standard)]填写2；[进阶型(advanced)]填写3；[容量型(capacity)]填写4；[高阶型1(specialized-1)]填写5；[高阶型2(specialized-2)]填写6；[高阶型3(specialized-3)]填写7；[高阶型4(specialized-4)]填写8。
        :type InstanceType: int
        :param _VpcId: vpcId，必填
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
        :param _BandWidth: 带宽，如果跟控制台规格配比不相符，则无法创建成功
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

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MsgRetentionTime(self):
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def KafkaVersion(self):
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MultiZoneFlag(self):
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PublicNetworkMonthly(self):
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def AutoVoucher(self):
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DeleteRouteTimestamp(self):
        warnings.warn("parameter `DeleteRouteTimestamp` is deprecated", DeprecationWarning) 

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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _VpcId: 创建的实例默认接入点所在的 vpc 对应 vpcId。目前不支持创建基础网络实例，因此该参数必填
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
        :param _SpecificationsType: 实例类型。"standard"：标准版，"profession"：专业版
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

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MsgRetentionTime(self):
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def KafkaVersion(self):
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SpecificationsType(self):
        return self._SpecificationsType

    @SpecificationsType.setter
    def SpecificationsType(self, SpecificationsType):
        self._SpecificationsType = SpecificationsType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def BandWidth(self):
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def MultiZoneFlag(self):
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def PublicNetworkMonthly(self):
        return self._PublicNetworkMonthly

    @PublicNetworkMonthly.setter
    def PublicNetworkMonthly(self, PublicNetworkMonthly):
        self._PublicNetworkMonthly = PublicNetworkMonthly


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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: ckafka实例id
        :type InstanceId: str
        :param _VpcId: vpc地址
        :type VpcId: str
        :param _SubnetId: 子网地址
        :type SubnetId: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VipType(self):
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AuthFlag(self):
        return self._AuthFlag

    @AuthFlag.setter
    def AuthFlag(self, AuthFlag):
        self._AuthFlag = AuthFlag

    @property
    def CallerAppid(self):
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def Ip(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _User: 用户名
        :type User: str
        """
        self._InstanceId = None
        self._User = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _MaxMessageBytes: 主题消息最大值，单位为 Byte，最小值1024Byte(即1KB)，最大值为8388608Byte（即8MB）。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def EnableWhiteList(self):
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def CleanUpPolicy(self):
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def MinInsyncReplicas(self):
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def SegmentMs(self):
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def MaxMessageBytes(self):
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def EnableAclRule(self):
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
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
        :param _Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: Ctsdb连接源的实例vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Ctsdb连接源的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: Ctsdb连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Ctsdb连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: Ctsdb连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: Ctsdb连接源的实例vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Ctsdb连接源的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: Ctsdb连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Ctsdb连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: Ctsdb连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _CtsdbMetric: Ctsdb的metric
注意：此字段可能返回 null，表示取不到有效值。
        :type CtsdbMetric: str
        """
        self._Resource = None
        self._CtsdbMetric = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def CtsdbMetric(self):
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def KafkaParam(self):
        return self._KafkaParam

    @KafkaParam.setter
    def KafkaParam(self, KafkaParam):
        self._KafkaParam = KafkaParam

    @property
    def EventBusParam(self):
        return self._EventBusParam

    @EventBusParam.setter
    def EventBusParam(self, EventBusParam):
        self._EventBusParam = EventBusParam

    @property
    def MongoDBParam(self):
        return self._MongoDBParam

    @MongoDBParam.setter
    def MongoDBParam(self, MongoDBParam):
        self._MongoDBParam = MongoDBParam

    @property
    def EsParam(self):
        return self._EsParam

    @EsParam.setter
    def EsParam(self, EsParam):
        self._EsParam = EsParam

    @property
    def TdwParam(self):
        return self._TdwParam

    @TdwParam.setter
    def TdwParam(self, TdwParam):
        self._TdwParam = TdwParam

    @property
    def DtsParam(self):
        return self._DtsParam

    @DtsParam.setter
    def DtsParam(self, DtsParam):
        self._DtsParam = DtsParam

    @property
    def ClickHouseParam(self):
        return self._ClickHouseParam

    @ClickHouseParam.setter
    def ClickHouseParam(self, ClickHouseParam):
        self._ClickHouseParam = ClickHouseParam

    @property
    def ClsParam(self):
        return self._ClsParam

    @ClsParam.setter
    def ClsParam(self, ClsParam):
        self._ClsParam = ClsParam

    @property
    def CosParam(self):
        return self._CosParam

    @CosParam.setter
    def CosParam(self, CosParam):
        self._CosParam = CosParam

    @property
    def MySQLParam(self):
        return self._MySQLParam

    @MySQLParam.setter
    def MySQLParam(self, MySQLParam):
        self._MySQLParam = MySQLParam

    @property
    def PostgreSQLParam(self):
        return self._PostgreSQLParam

    @PostgreSQLParam.setter
    def PostgreSQLParam(self, PostgreSQLParam):
        self._PostgreSQLParam = PostgreSQLParam

    @property
    def TopicParam(self):
        return self._TopicParam

    @TopicParam.setter
    def TopicParam(self, TopicParam):
        self._TopicParam = TopicParam

    @property
    def MariaDBParam(self):
        return self._MariaDBParam

    @MariaDBParam.setter
    def MariaDBParam(self, MariaDBParam):
        self._MariaDBParam = MariaDBParam

    @property
    def SQLServerParam(self):
        return self._SQLServerParam

    @SQLServerParam.setter
    def SQLServerParam(self, SQLServerParam):
        self._SQLServerParam = SQLServerParam

    @property
    def CtsdbParam(self):
        return self._CtsdbParam

    @CtsdbParam.setter
    def CtsdbParam(self, CtsdbParam):
        self._CtsdbParam = CtsdbParam

    @property
    def ScfParam(self):
        return self._ScfParam

    @ScfParam.setter
    def ScfParam(self, ScfParam):
        self._ScfParam = ScfParam

    @property
    def MqttParam(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskType: 任务类型，SOURCE数据接入，SINK数据流出
        :type TaskType: str
        :param _Status: 状态，-1创建失败，0创建中，1运行中，2删除中，3已删除，4删除失败，5暂停中，6已暂停，7暂停失败，8恢复中，9恢复失败
        :type Status: int
        :param _SourceResource: 数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TargetResource: 数据目标
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ErrorMessage: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _TaskProgress: 创建进度百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: float
        :param _TaskCurrentStep: 任务当前处于的步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCurrentStep: str
        :param _DatahubId: Datahub转储Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatahubId: str
        :param _StepList: 步骤列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceResource(self):
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def TaskProgress(self):
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def TaskCurrentStep(self):
        return self._TaskCurrentStep

    @TaskCurrentStep.setter
    def TaskCurrentStep(self, TaskCurrentStep):
        self._TaskCurrentStep = TaskCurrentStep

    @property
    def DatahubId(self):
        return self._DatahubId

    @DatahubId.setter
    def DatahubId(self, DatahubId):
        self._DatahubId = DatahubId

    @property
    def StepList(self):
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Status(self):
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
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _TopicId: TopicId
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self._TopicName = None
        self._TopicId = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetType: str
        :param _TimeZone: 时区，默认GMT+8
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeZone: str
        """
        self._Format = None
        self._TargetType = None
        self._TimeZone = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TimeZone(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _InstanceIdList: 订单流水对应购买的 CKafka 实例 id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIdList: list of str
        """
        self._DealName = None
        self._InstanceIdList = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def InstanceIdList(self):
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
        :param _InstanceId: 实例id信息
        :type InstanceId: str
        :param _ResourceType: Acl资源类型，(2:TOPIC，3:GROUP，4:CLUSTER)
        :type ResourceType: int
        :param _ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称，当resourceType为CLUSTER时，该字段可为空。
        :type ResourceName: str
        :param _Operation: Acl操作方式，(2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTENT_WRITE)
        :type Operation: int
        :param _PermissionType: 权限类型，(2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PermissionType(self):
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Principal(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Result: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Group: 消费分组
        :type Group: str
        """
        self._InstanceId = None
        self._Group = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        :param _Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDeleteResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例唯一id
        :type InstanceId: str
        :param _RouteId: 路由id
        :type RouteId: int
        :param _CallerAppid: 调用方appId
        :type CallerAppid: int
        :param _DeleteRouteTime: 删除路由时间
        :type DeleteRouteTime: str
        """
        self._InstanceId = None
        self._RouteId = None
        self._CallerAppid = None
        self._DeleteRouteTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def CallerAppid(self):
        return self._CallerAppid

    @CallerAppid.setter
    def CallerAppid(self, CallerAppid):
        self._CallerAppid = CallerAppid

    @property
    def DeleteRouteTime(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _DelayTime: 修改时间
        :type DelayTime: str
        """
        self._DelayTime = None

    @property
    def DelayTime(self):
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime


    def _deserialize(self, params):
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
        :param _InstanceId: 实例ID
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IpWhiteList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Name: 用户名称
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def PatternType(self):
        return self._PatternType

    @PatternType.setter
    def PatternType(self, PatternType):
        self._PatternType = PatternType

    @property
    def IsSimplified(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _CdcId: cdc专业集群业务参数
        :type CdcId: str
        """
        self._CdcId = None

    @property
    def CdcId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnSupportVersion: bool
        """
        self._IpAddr = None
        self._Time = None
        self._IsUnSupportVersion = None

    @property
    def IpAddr(self):
        return self._IpAddr

    @IpAddr.setter
    def IpAddr(self, IpAddr):
        self._IpAddr = IpAddr

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def IsUnSupportVersion(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceName: 连接源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _Description: 连接源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Type: 连接源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 连接源的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 连接源的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ErrorMessage: 连接源的异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _DatahubTaskCount: 该连接源关联的Datahub任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type DatahubTaskCount: int
        :param _CurrentStep: 连接源的当前所处步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentStep: str
        :param _TaskProgress: 创建进度百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: float
        :param _StepList: 步骤列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def DatahubTaskCount(self):
        return self._DatahubTaskCount

    @DatahubTaskCount.setter
    def DatahubTaskCount(self, DatahubTaskCount):
        self._DatahubTaskCount = DatahubTaskCount

    @property
    def CurrentStep(self):
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def TaskProgress(self):
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def StepList(self):
        return self._StepList

    @StepList.setter
    def StepList(self, StepList):
        self._StepList = StepList

    @property
    def DtsConnectParam(self):
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceName: 连接源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _Description: 连接源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Type: 连接源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 连接源的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 连接源的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ErrorMessage: 连接源的异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _CurrentStep: 连接源的当前所处步骤
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def CurrentStep(self):
        return self._CurrentStep

    @CurrentStep.setter
    def CurrentStep(self, CurrentStep):
        self._CurrentStep = CurrentStep

    @property
    def StepList(self):
        return self._StepList

    @StepList.setter
    def StepList(self, StepList):
        self._StepList = StepList

    @property
    def MySQLConnectParam(self):
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def DtsConnectParam(self):
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MariaDBConnectParam(self):
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourceResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceRegion(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectResourceList: list of DescribeConnectResource
        """
        self._TotalCount = None
        self._ConnectResourceList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConnectResourceList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: ckafka实例id。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _TargetResource: 数据目标
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetResource: :class:`tencentcloud.ckafka.v20190819.models.DatahubResource`
        :param _Connections: Connection列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Connections: list of Connection
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _TransformParam: 消息处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformParam: :class:`tencentcloud.ckafka.v20190819.models.TransformParam`
        :param _DatahubId: 数据接入ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatahubId: str
        :param _SchemaId: 绑定的SchemaId
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaId: str
        :param _SchemaName: 绑定的Schema名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaName: str
        :param _TransformsParam: 数据处理规则
注意：此字段可能返回 null，表示取不到有效值。
        :type TransformsParam: :class:`tencentcloud.ckafka.v20190819.models.TransformsParam`
        :param _ErrorMessage: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _Tags: 任务标签列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceResource(self):
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def TargetResource(self):
        return self._TargetResource

    @TargetResource.setter
    def TargetResource(self, TargetResource):
        self._TargetResource = TargetResource

    @property
    def Connections(self):
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TransformParam(self):
        return self._TransformParam

    @TransformParam.setter
    def TransformParam(self, TransformParam):
        self._TransformParam = TransformParam

    @property
    def DatahubId(self):
        return self._DatahubId

    @DatahubId.setter
    def DatahubId(self, DatahubId):
        self._DatahubId = DatahubId

    @property
    def SchemaId(self):
        return self._SchemaId

    @SchemaId.setter
    def SchemaId(self, SchemaId):
        self._SchemaId = SchemaId

    @property
    def SchemaName(self):
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TransformsParam(self):
        return self._TransformsParam

    @TransformsParam.setter
    def TransformsParam(self, TransformsParam):
        self._TransformsParam = TransformsParam

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Tags(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Resource(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskList: list of DatahubTaskInfo
        """
        self._TotalCount = None
        self._TaskList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Name: 名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        :param _Status: 状态，1使用中，2删除中
        :type Status: int
        :param _Address: 服务路由地址
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Address(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _SearchWord: 查询值
        :type SearchWord: str
        :param _Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param _Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        """
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
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
        


class DescribeDatahubTopicsResp(AbstractModel):
    """Datahub主题列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _TopicList: Topic列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of DatahubTopicDTO
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Group: groupId
        :type Group: str
        :param _Protocol: 该 group 使用的协议。
        :type Protocol: str
        """
        self._Group = None
        self._Protocol = None

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Protocol(self):
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
        :param _InstanceId: （过滤条件）按照实例 ID 过滤。
        :type InstanceId: str
        :param _GroupList: Kafka 消费分组，Consumer-group，这里是数组形式，示例：["xxx","yyy"]
        :type GroupList: list of str
        """
        self._InstanceId = None
        self._GroupList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of GroupInfoResponse
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: （过滤条件）按照实例 ID 过滤
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SearchWord: 搜索关键字
        :type SearchWord: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 最大返回数量
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果集列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def TagList(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param _SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param _Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认10，最大值100
        :type Limit: int
        :param _TagKey: 已废弃。匹配标签key值。
        :type TagKey: str
        :param _VpcId: 私有网络Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def VpcId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: ckafka实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CdcId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of Region
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例唯一id
        :type InstanceId: str
        :param _RouteId: 路由id
        :type RouteId: int
        """
        self._InstanceId = None
        self._RouteId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _FlowId: 任务唯一标记
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _SearchWord: （过滤条件）按照topicName过滤，支持模糊查询
        :type SearchWord: str
        :param _Offset: 偏移量，不填默认为0
        :type Offset: int
        :param _Limit: 返回数量，不填则默认 10，最大值20，取值要大于0
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RankingType: 排行类别(PRO-Topic生产流量/CON-Topic消费流量)
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RankingType(self):
        return self._RankingType

    @RankingType.setter
    def RankingType(self, RankingType):
        self._RankingType = RankingType

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
    def BrokerIp(self):
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
        :param _Result: 流量排行
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicFlowRankingResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _TopicName: topic名称
        :type TopicName: str
        """
        self._InstanceId = None
        self._TopicName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例 ID
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AclRuleName(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _TopicName: 主题名称
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OutOfSyncReplicaOnly(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _SearchWord: 按照名称过滤
        :type SearchWord: str
        :param _Offset: 偏移
        :type Offset: int
        :param _Limit: 本次返回个数
        :type Limit: int
        """
        self._InstanceId = None
        self._SearchWord = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _Result: 返回结果列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: Doris 连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Doris 连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: Doris 连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ServiceVip: Doris 连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Doris 连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _SelfBuilt: Doris 连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _BePort: Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def BePort(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: Doris jdbc 负载均衡连接 port，通常映射到 fe 的 9030 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: Doris 连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Doris 连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: Doris 连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Doris 连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _SelfBuilt: Doris 连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _BePort: Doris 的 http 负载均衡连接 port，通常映射到 be 的 8040 端口
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def BePort(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidMessageToCls: bool
        :param _DropClsRegion: 投递cls的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type DropClsRegion: str
        :param _DropClsOwneruin: 投递cls的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type DropClsOwneruin: str
        :param _DropClsTopicId: 投递cls的主题
注意：此字段可能返回 null，表示取不到有效值。
        :type DropClsTopicId: str
        :param _DropClsLogSet: 投递cls的日志集id
注意：此字段可能返回 null，表示取不到有效值。
        :type DropClsLogSet: str
        """
        self._DropInvalidMessageToCls = None
        self._DropClsRegion = None
        self._DropClsOwneruin = None
        self._DropClsTopicId = None
        self._DropClsLogSet = None

    @property
    def DropInvalidMessageToCls(self):
        return self._DropInvalidMessageToCls

    @DropInvalidMessageToCls.setter
    def DropInvalidMessageToCls(self, DropInvalidMessageToCls):
        self._DropInvalidMessageToCls = DropInvalidMessageToCls

    @property
    def DropClsRegion(self):
        return self._DropClsRegion

    @DropClsRegion.setter
    def DropClsRegion(self, DropClsRegion):
        self._DropClsRegion = DropClsRegion

    @property
    def DropClsOwneruin(self):
        return self._DropClsOwneruin

    @DropClsOwneruin.setter
    def DropClsOwneruin(self, DropClsOwneruin):
        self._DropClsOwneruin = DropClsOwneruin

    @property
    def DropClsTopicId(self):
        return self._DropClsTopicId

    @DropClsTopicId.setter
    def DropClsTopicId(self, DropClsTopicId):
        self._DropClsTopicId = DropClsTopicId

    @property
    def DropClsLogSet(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _GroupId: Dts消费分组的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _UserName: Dts消费分组的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Dts消费分组的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: Dts实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Topic: Dts订阅的topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def IsUpdate(self):
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def Topic(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Ip: Dts的连接ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: Dts的连接port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Topic: Dts订阅的topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _GroupId: Dts消费分组的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupUser: Dts消费分组的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupUser: str
        :param _GroupPassword: Dts消费分组的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupPassword: str
        :param _TranSql: false同步原始数据，true同步解析后的json格式数据,默认true
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupUser(self):
        return self._GroupUser

    @GroupUser.setter
    def GroupUser(self, GroupUser):
        self._GroupUser = GroupUser

    @property
    def GroupPassword(self):
        return self._GroupPassword

    @GroupPassword.setter
    def GroupPassword(self, GroupPassword):
        self._GroupPassword = GroupPassword

    @property
    def TranSql(self):
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
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def StepForwardPercentage(self):
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def DiskQuotaPercentage(self):
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def MaxDiskSpace(self):
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
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def DiskQuotaPercentage(self):
        return self._DiskQuotaPercentage

    @DiskQuotaPercentage.setter
    def DiskQuotaPercentage(self, DiskQuotaPercentage):
        self._DiskQuotaPercentage = DiskQuotaPercentage

    @property
    def StepForwardPercentage(self):
        return self._StepForwardPercentage

    @StepForwardPercentage.setter
    def StepForwardPercentage(self, StepForwardPercentage):
        self._StepForwardPercentage = StepForwardPercentage

    @property
    def BottomRetention(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: Es连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Es连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: Es连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SelfBuilt: Es连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _ServiceVip: Es连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Es连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: Es的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: Es连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: Es连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: Es连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Es连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _SelfBuilt: Es连接源是否为自建集群【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
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
        :param _Resource: 实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: Es的连接port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: Es用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: Es密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _ServiceVip: 实例vip
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: 实例的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _DropInvalidMessage: Es是否抛弃解析失败的消息
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidMessage: bool
        :param _Index: Es自定义index名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _DateFormat: Es自定义日期后缀
注意：此字段可能返回 null，表示取不到有效值。
        :type DateFormat: str
        :param _ContentKey: 非json格式数据的自定义key
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentKey: str
        :param _DropInvalidJsonMessage: Es是否抛弃非json格式的消息
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidJsonMessage: bool
        :param _DocumentIdField: 转储到Es中的文档ID取值字段名
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentIdField: str
        :param _IndexType: Es自定义index名称的类型，STRING，JSONPATH，默认为STRING
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexType: str
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
注意：此字段可能返回 null，表示取不到有效值。
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _DatabasePrimaryKey: 转储到ES的消息为Database的binlog时，如果需要同步数据库操作，即增删改的操作到ES时填写数据库表主键
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabasePrimaryKey: str
        :param _DropDlq: 死信队列
注意：此字段可能返回 null，表示取不到有效值。
        :type DropDlq: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        :param _RecordMappingList: 使用数据订阅格式导入 es 时，消息与 es 索引字段映射关系。不填默认为默认字段匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordMappingList: list of EsRecordMapping
        :param _DateField: 消息要映射为 es 索引中 @timestamp 的字段，如果当前配置为空，则使用消息的时间戳进行映射
注意：此字段可能返回 null，表示取不到有效值。
        :type DateField: str
        :param _RecordMappingMode: 用来区分当前索引映射，属于新建索引还是存量索引。"EXIST_MAPPING"：从存量索引中选择；"NEW_MAPPING"：新建索引
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def DropInvalidMessage(self):
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def DateFormat(self):
        return self._DateFormat

    @DateFormat.setter
    def DateFormat(self, DateFormat):
        self._DateFormat = DateFormat

    @property
    def ContentKey(self):
        return self._ContentKey

    @ContentKey.setter
    def ContentKey(self, ContentKey):
        self._ContentKey = ContentKey

    @property
    def DropInvalidJsonMessage(self):
        return self._DropInvalidJsonMessage

    @DropInvalidJsonMessage.setter
    def DropInvalidJsonMessage(self, DropInvalidJsonMessage):
        self._DropInvalidJsonMessage = DropInvalidJsonMessage

    @property
    def DocumentIdField(self):
        return self._DocumentIdField

    @DocumentIdField.setter
    def DocumentIdField(self, DocumentIdField):
        self._DocumentIdField = DocumentIdField

    @property
    def IndexType(self):
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def DropCls(self):
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def DatabasePrimaryKey(self):
        return self._DatabasePrimaryKey

    @DatabasePrimaryKey.setter
    def DatabasePrimaryKey(self, DatabasePrimaryKey):
        self._DatabasePrimaryKey = DatabasePrimaryKey

    @property
    def DropDlq(self):
        return self._DropDlq

    @DropDlq.setter
    def DropDlq(self, DropDlq):
        self._DropDlq = DropDlq

    @property
    def RecordMappingList(self):
        return self._RecordMappingList

    @RecordMappingList.setter
    def RecordMappingList(self, RecordMappingList):
        self._RecordMappingList = RecordMappingList

    @property
    def DateField(self):
        return self._DateField

    @DateField.setter
    def DateField(self, DateField):
        self._DateField = DateField

    @property
    def RecordMappingMode(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnName: str
        :param _JsonKey: 消息字段名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JsonKey: str
        """
        self._ColumnName = None
        self._JsonKey = None

    @property
    def ColumnName(self):
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def JsonKey(self):
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
        :param _Type: 资源类型。EB_COS/EB_ES/EB_CLS
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicParam: :class:`tencentcloud.ckafka.v20190819.models.TopicParam`
        :param _DlqType: 死信队列类型，CKAFKA，TOPIC
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def KafkaParam(self):
        return self._KafkaParam

    @KafkaParam.setter
    def KafkaParam(self, KafkaParam):
        self._KafkaParam = KafkaParam

    @property
    def RetryInterval(self):
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def MaxRetryAttempts(self):
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def TopicParam(self):
        return self._TopicParam

    @TopicParam.setter
    def TopicParam(self, TopicParam):
        self._TopicParam = TopicParam

    @property
    def DlqType(self):
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
        :param _Name: 主题名
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Name: 主题名
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def MessageCount(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例Id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SinglePartitionRecordNumber(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryAnalyse: :class:`tencentcloud.ckafka.v20190819.models.SecondaryAnalyseParam`
        :param _SMT: 数据处理
注意：此字段可能返回 null，表示取不到有效值。
        :type SMT: list of SMTParam
        :param _Result: 测试结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _AnalyseResult: 解析结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalyseResult: list of SMTParam
        :param _SecondaryAnalyseResult: 二次解析结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryAnalyseResult: list of SMTParam
        :param _AnalyseJsonResult: JSON格式解析结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalyseJsonResult: str
        :param _SecondaryAnalyseJsonResult: JSON格式二次解析结果
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Analyse

    @Analyse.setter
    def Analyse(self, Analyse):
        self._Analyse = Analyse

    @property
    def SecondaryAnalyse(self):
        return self._SecondaryAnalyse

    @SecondaryAnalyse.setter
    def SecondaryAnalyse(self, SecondaryAnalyse):
        self._SecondaryAnalyse = SecondaryAnalyse

    @property
    def SMT(self):
        return self._SMT

    @SMT.setter
    def SMT(self, SMT):
        self._SMT = SMT

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AnalyseResult(self):
        return self._AnalyseResult

    @AnalyseResult.setter
    def AnalyseResult(self, AnalyseResult):
        self._AnalyseResult = AnalyseResult

    @property
    def SecondaryAnalyseResult(self):
        return self._SecondaryAnalyseResult

    @SecondaryAnalyseResult.setter
    def SecondaryAnalyseResult(self, SecondaryAnalyseResult):
        self._SecondaryAnalyseResult = SecondaryAnalyseResult

    @property
    def AnalyseJsonResult(self):
        return self._AnalyseJsonResult

    @AnalyseJsonResult.setter
    def AnalyseJsonResult(self, AnalyseJsonResult):
        self._AnalyseJsonResult = AnalyseJsonResult

    @property
    def SecondaryAnalyseJsonResult(self):
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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def MatchMode(self):
        return self._MatchMode

    @MatchMode.setter
    def MatchMode(self, MatchMode):
        self._MatchMode = MatchMode

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
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
        :param _GroupName: 组名称
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
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
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientHost(self):
        return self._ClientHost

    @ClientHost.setter
    def ClientHost(self, ClientHost):
        self._ClientHost = ClientHost

    @property
    def Assignment(self):
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
        :param _Group: Kafka 消费分组
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
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Members(self):
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def Group(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of int
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def LogEndOffset(self):
        return self._LogEndOffset

    @LogEndOffset.setter
    def LogEndOffset(self, LogEndOffset):
        self._LogEndOffset = LogEndOffset

    @property
    def Lag(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of GroupOffsetTopic
        """
        self._TotalCount = None
        self._TopicList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of GroupOffsetPartition
        """
        self._Topic = None
        self._Partitions = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partitions(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _GroupList: GroupList
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribeGroup
        :param _GroupCountQuota: 消费分组配额
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupCountQuota: int
        """
        self._TotalCount = None
        self._GroupList = None
        self._GroupCountQuota = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def GroupCountQuota(self):
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
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeParam(self):
        return self._InstanceChargeParam

    @InstanceChargeParam.setter
    def InstanceChargeParam(self, InstanceChargeParam):
        self._InstanceChargeParam = InstanceChargeParam

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def InquiryDiskParam(self):
        return self._InquiryDiskParam

    @InquiryDiskParam.setter
    def InquiryDiskParam(self, InquiryDiskParam):
        self._InquiryDiskParam = InquiryDiskParam

    @property
    def MessageRetention(self):
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def CategoryAction(self):
        return self._CategoryAction

    @CategoryAction.setter
    def CategoryAction(self, CategoryAction):
        self._CategoryAction = CategoryAction

    @property
    def BillType(self):
        return self._BillType

    @BillType.setter
    def BillType(self, BillType):
        self._BillType = BillType

    @property
    def PublicNetworkParam(self):
        return self._PublicNetworkParam

    @PublicNetworkParam.setter
    def PublicNetworkParam(self, PublicNetworkParam):
        self._PublicNetworkParam = PublicNetworkParam

    @property
    def InstanceId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        :param _PublicNetworkBandwidthPrice: 公网带宽价格
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkBandwidthPrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryPrice`
        """
        self._InstancePrice = None
        self._PublicNetworkBandwidthPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def PublicNetworkBandwidthPrice(self):
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
        :param _Result: 出参
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceDiscount: 折扣单位价格
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _OriginalPrice: 合计原价
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 折扣合计价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _Discount: 折扣(单位是%)
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

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
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypePrice: :class:`tencentcloud.ckafka.v20190819.models.InquiryBasePrice`
        """
        self._BandwidthPrice = None
        self._DiskPrice = None
        self._PartitionPrice = None
        self._TopicPrice = None
        self._InstanceTypePrice = None

    @property
    def BandwidthPrice(self):
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice

    @property
    def DiskPrice(self):
        return self._DiskPrice

    @DiskPrice.setter
    def DiskPrice(self, DiskPrice):
        self._DiskPrice = DiskPrice

    @property
    def PartitionPrice(self):
        return self._PartitionPrice

    @PartitionPrice.setter
    def PartitionPrice(self, PartitionPrice):
        self._PartitionPrice = PartitionPrice

    @property
    def TopicPrice(self):
        return self._TopicPrice

    @TopicPrice.setter
    def TopicPrice(self, TopicPrice):
        self._TopicPrice = TopicPrice

    @property
    def InstanceTypePrice(self):
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
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceDiscount: 折扣单位价格
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _OriginalPrice: 合计原价
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 折扣合计价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _Discount: 折扣(单位是%)
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

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
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DetailPrices(self):
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
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetworkMonthly(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Status: 实例的状态。0：创建中，1：运行中，2：删除中 ， 5 隔离中，-1 创建失败
        :type Status: int
        :param _IfCommunity: 是否开源实例。开源：true，不开源：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IfCommunity: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._IfCommunity = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IfCommunity(self):
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _VipList: 接入点 VIP 列表信息
        :type VipList: list of VipEntity
        :param _Vip: 虚拟IP
        :type Vip: str
        :param _Vport: 虚拟端口
        :type Vport: str
        :param _Status: 实例的状态。0：创建中，1：运行中，2：删除中
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param _Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _MaxGroupNum: 最大分组数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxGroupNum: int
        :param _Cvm: 售卖类型,0:标准版,1:专业版
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param _InstanceType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Features: 表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param _RetentionTimeConfig: 动态消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _MaxConnection: 最大连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConnection: int
        :param _PublicNetwork: 公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: int
        :param _DeleteRouteTimestamp: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteRouteTimestamp: str
        :param _RemainingPartitions: 剩余创建分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingPartitions: int
        :param _RemainingTopics: 剩余创建主题数
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingTopics: int
        :param _DynamicDiskConfig: 动态硬盘扩容策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _InstanceChargeType: 实例计费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MsgRetentionTime(self):
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RemainderPartitions(self):
        return self._RemainderPartitions

    @RemainderPartitions.setter
    def RemainderPartitions(self, RemainderPartitions):
        self._RemainderPartitions = RemainderPartitions

    @property
    def RemainderTopics(self):
        return self._RemainderTopics

    @RemainderTopics.setter
    def RemainderTopics(self, RemainderTopics):
        self._RemainderTopics = RemainderTopics

    @property
    def CreatedPartitions(self):
        return self._CreatedPartitions

    @CreatedPartitions.setter
    def CreatedPartitions(self, CreatedPartitions):
        self._CreatedPartitions = CreatedPartitions

    @property
    def CreatedTopics(self):
        return self._CreatedTopics

    @CreatedTopics.setter
    def CreatedTopics(self, CreatedTopics):
        self._CreatedTopics = CreatedTopics

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def MaxGroupNum(self):
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def Cvm(self):
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def RetentionTimeConfig(self):
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def MaxConnection(self):
        return self._MaxConnection

    @MaxConnection.setter
    def MaxConnection(self, MaxConnection):
        self._MaxConnection = MaxConnection

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DeleteRouteTimestamp(self):
        return self._DeleteRouteTimestamp

    @DeleteRouteTimestamp.setter
    def DeleteRouteTimestamp(self, DeleteRouteTimestamp):
        self._DeleteRouteTimestamp = DeleteRouteTimestamp

    @property
    def RemainingPartitions(self):
        return self._RemainingPartitions

    @RemainingPartitions.setter
    def RemainingPartitions(self, RemainingPartitions):
        self._RemainingPartitions = RemainingPartitions

    @property
    def RemainingTopics(self):
        return self._RemainingTopics

    @RemainingTopics.setter
    def RemainingTopics(self, RemainingTopics):
        self._RemainingTopics = RemainingTopics

    @property
    def DynamicDiskConfig(self):
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


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
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePeriod(self):
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
        return self._AutoCreateTopicsEnable

    @AutoCreateTopicsEnable.setter
    def AutoCreateTopicsEnable(self, AutoCreateTopicsEnable):
        self._AutoCreateTopicsEnable = AutoCreateTopicsEnable

    @property
    def DefaultNumPartitions(self):
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        """
        self._FlowId = None

    @property
    def FlowId(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Vip: 访问实例的vip 信息
        :type Vip: str
        :param _Vport: 访问实例的端口信息
        :type Vport: str
        :param _VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param _Status: 实例的状态。0：创建中，1：运行中，2：删除中：5隔离中， -1 创建失败
        :type Status: int
        :param _Bandwidth: 实例带宽，单位Mbps
        :type Bandwidth: int
        :param _DiskSize: 实例的存储大小，单位GB
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param _Cvm: ckafka售卖类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param _InstanceType: ckafka实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _MaxTopicNumber: 当前规格最大Topic数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTopicNumber: int
        :param _MaxPartitionNumber: 当前规格最大Partition数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPartitionNumber: int
        :param _RebalanceTime: 计划升级配置时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RebalanceTime: str
        :param _PartitionNumber: 实例当前partition数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNumber: int
        :param _PublicNetworkChargeType: 公网带宽类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkChargeType: str
        :param _PublicNetwork: 公网带宽值
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: int
        :param _ClusterType: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param _Features: 实例功能列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyMessage(self):
        return self._HealthyMessage

    @HealthyMessage.setter
    def HealthyMessage(self, HealthyMessage):
        self._HealthyMessage = HealthyMessage

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsInternal(self):
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Cvm(self):
        return self._Cvm

    @Cvm.setter
    def Cvm(self, Cvm):
        self._Cvm = Cvm

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MaxTopicNumber(self):
        return self._MaxTopicNumber

    @MaxTopicNumber.setter
    def MaxTopicNumber(self, MaxTopicNumber):
        self._MaxTopicNumber = MaxTopicNumber

    @property
    def MaxPartitionNumber(self):
        return self._MaxPartitionNumber

    @MaxPartitionNumber.setter
    def MaxPartitionNumber(self, MaxPartitionNumber):
        self._MaxPartitionNumber = MaxPartitionNumber

    @property
    def RebalanceTime(self):
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PartitionNumber(self):
        return self._PartitionNumber

    @PartitionNumber.setter
    def PartitionNumber(self, PartitionNumber):
        self._PartitionNumber = PartitionNumber

    @property
    def PublicNetworkChargeType(self):
        return self._PublicNetworkChargeType

    @PublicNetworkChargeType.setter
    def PublicNetworkChargeType(self, PublicNetworkChargeType):
        self._PublicNetworkChargeType = PublicNetworkChargeType

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Features(self):
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
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
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of Instance
        :param _TotalCount: 符合条件的结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
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
        :param _InstanceId: 实例id
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeStrategy(self):
        return self._UpgradeStrategy

    @UpgradeStrategy.setter
    def UpgradeStrategy(self, UpgradeStrategy):
        self._UpgradeStrategy = UpgradeStrategy

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
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
        :param _Result: 缩容应答
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ScalingDownResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
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
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepOriginalKey: str
        """
        self._Delimiter = None
        self._Regex = None
        self._KeepOriginalKey = None

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def KeepOriginalKey(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _BrokerAddress: Kafka连接的broker地址, NetworkType=PUBLIC公网时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerAddress: str
        :param _Region: CKafka连接源的实例资源地域, 跨地域时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Resource = None
        self._SelfBuilt = None
        self._IsUpdate = None
        self._BrokerAddress = None
        self._Region = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def BrokerAddress(self):
        return self._BrokerAddress

    @BrokerAddress.setter
    def BrokerAddress(self, BrokerAddress):
        self._BrokerAddress = BrokerAddress

    @property
    def Region(self):
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
        :param _Resource: 实例资源
        :type Resource: str
        :param _Topic: Topic名称，多个以“,”分隔
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
        :param _ZoneId: Zone ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _TopicId: Topic的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _PartitionNum: Topic的分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNum: int
        :param _EnableToleration: 启用容错实例/开启死信队列
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableToleration: bool
        :param _QpsLimit: Qps 限制
注意：此字段可能返回 null，表示取不到有效值。
        :type QpsLimit: int
        :param _TableMappings: Table到Topic的路由，「分发到多个topic」开关打开时必传
注意：此字段可能返回 null，表示取不到有效值。
        :type TableMappings: list of TableMapping
        :param _UseTableMapping: 「分发到多个topic」开关，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type UseTableMapping: bool
        :param _UseAutoCreateTopic: 使用的Topic是否需要自动创建（目前只支持SOURCE流入任务，如果不使用分发到多个topic，需要在Topic字段填写需要自动创建的topic名）
注意：此字段可能返回 null，表示取不到有效值。
        :type UseAutoCreateTopic: bool
        :param _CompressionType: 写入Topic时是否进行压缩，不开启填"none"，开启的话，填写"open"。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompressionType: str
        :param _MsgMultiple: 源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgMultiple: int
        :param _ConnectorSyncType: 数据同步专用参数, 正常数据处理可为空, 实例级别同步: 仅同步元数据填写"META_SYNC_INSTANCE_TYPE", 同步元数据及全部topic内消息的填写"META_AND_DATA_SYNC_INSTANCE_TYPE"; topic级别同步: 选中的源和目标topic中的消息(需要目标实例也包含该topic)填写"DATA_SYNC_TYPE"
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectorSyncType: str
        :param _KeepPartition: 数据同步专用参数, 当通过时,希望下游的消息写入分区与上游的一致,则填true,但下游分区小于上游时,会报错; 不需要一致则为false, 默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepPartition: bool
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

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def OffsetType(self):
        return self._OffsetType

    @OffsetType.setter
    def OffsetType(self, OffsetType):
        self._OffsetType = OffsetType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableToleration(self):
        return self._EnableToleration

    @EnableToleration.setter
    def EnableToleration(self, EnableToleration):
        self._EnableToleration = EnableToleration

    @property
    def QpsLimit(self):
        return self._QpsLimit

    @QpsLimit.setter
    def QpsLimit(self, QpsLimit):
        self._QpsLimit = QpsLimit

    @property
    def TableMappings(self):
        return self._TableMappings

    @TableMappings.setter
    def TableMappings(self, TableMappings):
        self._TableMappings = TableMappings

    @property
    def UseTableMapping(self):
        return self._UseTableMapping

    @UseTableMapping.setter
    def UseTableMapping(self, UseTableMapping):
        self._UseTableMapping = UseTableMapping

    @property
    def UseAutoCreateTopic(self):
        return self._UseAutoCreateTopic

    @UseAutoCreateTopic.setter
    def UseAutoCreateTopic(self, UseAutoCreateTopic):
        self._UseAutoCreateTopic = UseAutoCreateTopic

    @property
    def CompressionType(self):
        return self._CompressionType

    @CompressionType.setter
    def CompressionType(self, CompressionType):
        self._CompressionType = CompressionType

    @property
    def MsgMultiple(self):
        return self._MsgMultiple

    @MsgMultiple.setter
    def MsgMultiple(self, MsgMultiple):
        self._MsgMultiple = MsgMultiple

    @property
    def ConnectorSyncType(self):
        return self._ConnectorSyncType

    @ConnectorSyncType.setter
    def ConnectorSyncType(self, ConnectorSyncType):
        self._ConnectorSyncType = ConnectorSyncType

    @property
    def KeepPartition(self):
        return self._KeepPartition

    @KeepPartition.setter
    def KeepPartition(self, KeepPartition):
        self._KeepPartition = KeepPartition


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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: MariaDB连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MariaDB连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: MariaDB连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ServiceVip: MariaDB连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MariaDB连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: MariaDB的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: MariaDB连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MariaDB连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: MariaDB连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MariaDB连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: MariaDB的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Resource: 该MariaDB在连接管理内的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only不复制, initial全量)，默认位initial
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotMode: str
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyColumns: str
        :param _IsTablePrefix: 当Table输入的是前缀时，该项值为true，否则为false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTablePrefix: bool
        :param _OutputFormat: 输出格式，DEFAULT、CANAL_1、CANAL_2
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param _IncludeContentChanges: 如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeContentChanges: str
        :param _IncludeQuery: 如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeQuery: bool
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def KeyColumns(self):
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def IsTablePrefix(self):
        return self._IsTablePrefix

    @IsTablePrefix.setter
    def IsTablePrefix(self, IsTablePrefix):
        self._IsTablePrefix = IsTablePrefix

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def IncludeContentChanges(self):
        return self._IncludeContentChanges

    @IncludeContentChanges.setter
    def IncludeContentChanges(self, IncludeContentChanges):
        self._IncludeContentChanges = IncludeContentChanges

    @property
    def IncludeQuery(self):
        return self._IncludeQuery

    @IncludeQuery.setter
    def IncludeQuery(self, IncludeQuery):
        self._IncludeQuery = IncludeQuery

    @property
    def RecordWithSchema(self):
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
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _RuleName: ACL策略名
        :type RuleName: str
        :param _IsApplied: 修改预设规则时传入,是否应用到新增的Topic
        :type IsApplied: int
        """
        self._InstanceId = None
        self._RuleName = None
        self._IsApplied = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def IsApplied(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DtsConnectParam(self):
        return self._DtsConnectParam

    @DtsConnectParam.setter
    def DtsConnectParam(self, DtsConnectParam):
        self._DtsConnectParam = DtsConnectParam

    @property
    def MongoDBConnectParam(self):
        return self._MongoDBConnectParam

    @MongoDBConnectParam.setter
    def MongoDBConnectParam(self, MongoDBConnectParam):
        self._MongoDBConnectParam = MongoDBConnectParam

    @property
    def EsConnectParam(self):
        return self._EsConnectParam

    @EsConnectParam.setter
    def EsConnectParam(self, EsConnectParam):
        self._EsConnectParam = EsConnectParam

    @property
    def ClickHouseConnectParam(self):
        return self._ClickHouseConnectParam

    @ClickHouseConnectParam.setter
    def ClickHouseConnectParam(self, ClickHouseConnectParam):
        self._ClickHouseConnectParam = ClickHouseConnectParam

    @property
    def MySQLConnectParam(self):
        return self._MySQLConnectParam

    @MySQLConnectParam.setter
    def MySQLConnectParam(self, MySQLConnectParam):
        self._MySQLConnectParam = MySQLConnectParam

    @property
    def PostgreSQLConnectParam(self):
        return self._PostgreSQLConnectParam

    @PostgreSQLConnectParam.setter
    def PostgreSQLConnectParam(self, PostgreSQLConnectParam):
        self._PostgreSQLConnectParam = PostgreSQLConnectParam

    @property
    def MariaDBConnectParam(self):
        return self._MariaDBConnectParam

    @MariaDBConnectParam.setter
    def MariaDBConnectParam(self, MariaDBConnectParam):
        self._MariaDBConnectParam = MariaDBConnectParam

    @property
    def SQLServerConnectParam(self):
        return self._SQLServerConnectParam

    @SQLServerConnectParam.setter
    def SQLServerConnectParam(self, SQLServerConnectParam):
        self._SQLServerConnectParam = SQLServerConnectParam

    @property
    def CtsdbConnectParam(self):
        return self._CtsdbConnectParam

    @CtsdbConnectParam.setter
    def CtsdbConnectParam(self, CtsdbConnectParam):
        self._CtsdbConnectParam = CtsdbConnectParam

    @property
    def DorisConnectParam(self):
        return self._DorisConnectParam

    @DorisConnectParam.setter
    def DorisConnectParam(self, DorisConnectParam):
        self._DorisConnectParam = DorisConnectParam

    @property
    def KafkaConnectParam(self):
        return self._KafkaConnectParam

    @KafkaConnectParam.setter
    def KafkaConnectParam(self, KafkaConnectParam):
        self._KafkaConnectParam = KafkaConnectParam

    @property
    def MqttConnectParam(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.DatahubTaskIdRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Name: 名称
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Tags(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: kafka实例id
        :type InstanceId: str
        :param _Group: kafka 消费分组
        :type Group: str
        :param _Strategy: 重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置
        :type Strategy: int
        :param _Topics: 表示需要重置的topics， 不填表示全部
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Shift(self):
        return self._Shift

    @Shift.setter
    def Shift(self, Shift):
        self._Shift = Shift

    @property
    def ShiftTimestamp(self):
        return self._ShiftTimestamp

    @ShiftTimestamp.setter
    def ShiftTimestamp(self, ShiftTimestamp):
        self._ShiftTimestamp = ShiftTimestamp

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Partitions(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._AutoCreateTopicEnable

    @AutoCreateTopicEnable.setter
    def AutoCreateTopicEnable(self, AutoCreateTopicEnable):
        self._AutoCreateTopicEnable = AutoCreateTopicEnable

    @property
    def DefaultNumPartitions(self):
        return self._DefaultNumPartitions

    @DefaultNumPartitions.setter
    def DefaultNumPartitions(self, DefaultNumPartitions):
        self._DefaultNumPartitions = DefaultNumPartitions

    @property
    def DefaultReplicationFactor(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _MsgRetentionTime: 实例日志的最长保留时间，单位分钟，最大30天，0代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param _InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param _Config: 实例配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param _DynamicRetentionConfig: 动态消息保留策略配置
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param _RebalanceTime: 升配Rebalance时间
        :type RebalanceTime: int
        :param _PublicNetwork: 公网带宽
        :type PublicNetwork: int
        :param _DynamicDiskConfig: 动态硬盘扩容策略配置
        :type DynamicDiskConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicDiskConfig`
        :param _MaxMessageByte: 实例级别单条消息大小（单位byte)
        :type MaxMessageByte: int
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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MsgRetentionTime(self):
        return self._MsgRetentionTime

    @MsgRetentionTime.setter
    def MsgRetentionTime(self, MsgRetentionTime):
        self._MsgRetentionTime = MsgRetentionTime

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def DynamicRetentionConfig(self):
        return self._DynamicRetentionConfig

    @DynamicRetentionConfig.setter
    def DynamicRetentionConfig(self, DynamicRetentionConfig):
        self._DynamicRetentionConfig = DynamicRetentionConfig

    @property
    def RebalanceTime(self):
        return self._RebalanceTime

    @RebalanceTime.setter
    def RebalanceTime(self, RebalanceTime):
        self._RebalanceTime = RebalanceTime

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def DynamicDiskConfig(self):
        return self._DynamicDiskConfig

    @DynamicDiskConfig.setter
    def DynamicDiskConfig(self, DynamicDiskConfig):
        self._DynamicDiskConfig = DynamicDiskConfig

    @property
    def MaxMessageByte(self):
        return self._MaxMessageByte

    @MaxMessageByte.setter
    def MaxMessageByte(self, MaxMessageByte):
        self._MaxMessageByte = MaxMessageByte


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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例名称
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def BandWidth(self):
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Partition(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PasswordNew(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _TopicName: 主题名称。
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
        :param _AclRuleName: 预设ACL规则的名称
        :type AclRuleName: str
        :param _RetentionBytes: 可选, 保留文件大小. 默认为-1,单位bytes, 当前最小值为1048576B
        :type RetentionBytes: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _QuotaProducerByteRate: 生产限流，单位 MB/s
        :type QuotaProducerByteRate: int
        :param _QuotaConsumerByteRate: 消费限流，单位 MB/s
        :type QuotaConsumerByteRate: int
        :param _ReplicaNum: 调整topic副本数
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def EnableWhiteList(self):
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def MinInsyncReplicas(self):
        return self._MinInsyncReplicas

    @MinInsyncReplicas.setter
    def MinInsyncReplicas(self, MinInsyncReplicas):
        self._MinInsyncReplicas = MinInsyncReplicas

    @property
    def UncleanLeaderElectionEnable(self):
        return self._UncleanLeaderElectionEnable

    @UncleanLeaderElectionEnable.setter
    def UncleanLeaderElectionEnable(self, UncleanLeaderElectionEnable):
        self._UncleanLeaderElectionEnable = UncleanLeaderElectionEnable

    @property
    def RetentionMs(self):
        return self._RetentionMs

    @RetentionMs.setter
    def RetentionMs(self, RetentionMs):
        self._RetentionMs = RetentionMs

    @property
    def MaxMessageBytes(self):
        return self._MaxMessageBytes

    @MaxMessageBytes.setter
    def MaxMessageBytes(self, MaxMessageBytes):
        self._MaxMessageBytes = MaxMessageBytes

    @property
    def SegmentMs(self):
        return self._SegmentMs

    @SegmentMs.setter
    def SegmentMs(self, SegmentMs):
        self._SegmentMs = SegmentMs

    @property
    def CleanUpPolicy(self):
        return self._CleanUpPolicy

    @CleanUpPolicy.setter
    def CleanUpPolicy(self, CleanUpPolicy):
        self._CleanUpPolicy = CleanUpPolicy

    @property
    def IpWhiteList(self):
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def EnableAclRule(self):
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleName(self):
        return self._AclRuleName

    @AclRuleName.setter
    def AclRuleName(self, AclRuleName):
        self._AclRuleName = AclRuleName

    @property
    def RetentionBytes(self):
        return self._RetentionBytes

    @RetentionBytes.setter
    def RetentionBytes(self, RetentionBytes):
        self._RetentionBytes = RetentionBytes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def QuotaProducerByteRate(self):
        return self._QuotaProducerByteRate

    @QuotaProducerByteRate.setter
    def QuotaProducerByteRate(self, QuotaProducerByteRate):
        self._QuotaProducerByteRate = QuotaProducerByteRate

    @property
    def QuotaConsumerByteRate(self):
        return self._QuotaConsumerByteRate

    @QuotaConsumerByteRate.setter
    def QuotaConsumerByteRate(self, QuotaConsumerByteRate):
        self._QuotaConsumerByteRate = QuotaConsumerByteRate

    @property
    def ReplicaNum(self):
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
        :param _Result: 返回结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: MongoDB连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MongoDB连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: MongoDB连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SelfBuilt: MongoDB连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _ServiceVip: MongoDB连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MongoDB连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: MongoDB的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: MongoDB连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MongoDB连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: MongoDB连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MongoDB连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _SelfBuilt: MongoDB连接源是否为自建集群【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Collection: MongoDB的集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Collection: str
        :param _CopyExisting: 是否复制存量数据，默认传参true
注意：此字段可能返回 null，表示取不到有效值。
        :type CopyExisting: bool
        :param _Resource: 实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Ip: MongoDB的连接ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: MongoDB的连接port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: MongoDB数据库用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MongoDB数据库密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _ListeningEvent: 监听事件类型，为空时表示全选。取值包括insert,update,replace,delete,invalidate,drop,dropdatabase,rename，多个类型间使用,逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type ListeningEvent: str
        :param _ReadPreference: 主从优先级，默认主节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadPreference: str
        :param _Pipeline: 聚合管道
注意：此字段可能返回 null，表示取不到有效值。
        :type Pipeline: str
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Collection(self):
        return self._Collection

    @Collection.setter
    def Collection(self, Collection):
        self._Collection = Collection

    @property
    def CopyExisting(self):
        return self._CopyExisting

    @CopyExisting.setter
    def CopyExisting(self, CopyExisting):
        self._CopyExisting = CopyExisting

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ListeningEvent(self):
        return self._ListeningEvent

    @ListeningEvent.setter
    def ListeningEvent(self, ListeningEvent):
        self._ListeningEvent = ListeningEvent

    @property
    def ReadPreference(self):
        return self._ReadPreference

    @ReadPreference.setter
    def ReadPreference(self, ReadPreference):
        self._ReadPreference = ReadPreference

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MQTT连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: MQTT连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _UniqVpcId: MQTT Instance vpc-id
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SelfBuilt: bool
        :param _IsUpdate: 是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _Region: MQTT连接源的实例资源地域, 跨地域时必填
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
        return self._SelfBuilt

    @SelfBuilt.setter
    def SelfBuilt(self, SelfBuilt):
        self._SelfBuilt = SelfBuilt

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def Region(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: str
        :param _CleanSession: MQTT clean-session
注意：此字段可能返回 null，表示取不到有效值。
        :type CleanSession: bool
        :param _Resource: MQTT instance-id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Ip: MQTT实例VIP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: MQTT VIP 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: MQTT实例用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MQTT实例内账户密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Qos: QoS
注意：此字段可能返回 null，表示取不到有效值。
        :type Qos: int
        :param _MaxTasks: tasks.max 订阅Topic的并发Task个数, 默认为1; 当设置大于1时, 使用Shared Subscription
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTasks: int
        :param _ServiceVip: MQTT 实例的Service VIP
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MQTT实例的VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _SelfBuilt: 是否为自建集群, MQTT只支持非自建集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def CleanSession(self):
        return self._CleanSession

    @CleanSession.setter
    def CleanSession(self, CleanSession):
        self._CleanSession = CleanSession

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def MaxTasks(self):
        return self._MaxTasks

    @MaxTasks.setter
    def MaxTasks(self, MaxTasks):
        self._MaxTasks = MaxTasks

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: MySQL连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MySQL连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: MySQL连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ServiceVip: MySQL连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MySQL连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _ClusterId: 当type为TDSQL_C_MYSQL时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _SelfBuilt: Mysql 连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: MySQL的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: MySQL连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: MySQL连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: MySQL连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: MySQL连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _ClusterId: 当type为TDSQL_C_MYSQL时
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _SelfBuilt: 是否是自建的集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: MySQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"数据库名\\.数据表名"
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Resource: 该MySQL在连接管理内的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only不复制, initial全量)，默认位initial
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotMode: str
        :param _DdlTopic: 存放MySQL的Ddl信息的Topic，为空则默认不存放
注意：此字段可能返回 null，表示取不到有效值。
        :type DdlTopic: str
        :param _DataSourceMonitorMode: "TABLE" 表示读取项为 table，"QUERY" 表示读取项为 query
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceMonitorMode: str
        :param _DataSourceMonitorResource: 当 "DataMonitorMode"="TABLE" 时，传入需要读取的 Table；当 "DataMonitorMode"="QUERY" 时，传入需要读取的查询 sql 语句
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceMonitorResource: str
        :param _DataSourceIncrementMode: "TIMESTAMP" 表示增量列为时间戳类型，"INCREMENT" 表示增量列为自增 id 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceIncrementMode: str
        :param _DataSourceIncrementColumn: 传入需要监听的列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceIncrementColumn: str
        :param _DataSourceStartFrom: "HEAD" 表示复制存量 + 增量数据，"TAIL" 表示只复制增量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceStartFrom: str
        :param _DataTargetInsertMode: "INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetInsertMode: str
        :param _DataTargetPrimaryKeyField: 当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetPrimaryKeyField: str
        :param _DataTargetRecordMapping: 表与消息间的映射关系
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetRecordMapping: list of RecordMapping
        :param _TopicRegex: 事件路由到特定主题的正则表达式，默认为(.*)
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicRegex: str
        :param _TopicReplacement: TopicRegex的引用组，指定$1、$2等
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicReplacement: str
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyColumns: str
        :param _DropInvalidMessage: Mysql 是否抛弃解析失败的消息，默认为true
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidMessage: bool
        :param _DropCls: 当设置成员参数DropInvalidMessageToCls设置为true时,DropInvalidMessage参数失效
注意：此字段可能返回 null，表示取不到有效值。
        :type DropCls: :class:`tencentcloud.ckafka.v20190819.models.DropCls`
        :param _OutputFormat: 输出格式，DEFAULT、CANAL_1、CANAL_2
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param _IsTablePrefix: 当Table输入的是前缀时，该项值为true，否则为false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTablePrefix: bool
        :param _IncludeContentChanges: 如果该值为all，则DDL数据以及DML数据也会写入到选中的topic；若该值为dml，则只有DML数据写入到选中的topic
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeContentChanges: str
        :param _IncludeQuery: 如果该值为true，且MySQL中"binlog_rows_query_log_events"配置项的值为"ON"，则流入到topic的数据包含原SQL语句；若该值为false，流入到topic的数据不包含原SQL语句
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeQuery: bool
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordWithSchema: bool
        :param _SignalDatabase: 存放信令表的数据库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalDatabase: str
        :param _IsTableRegular: 输入的table是否为正则表达式，如果该选项以及IsTablePrefix同时为true，该选项的判断优先级高于IsTablePrefix
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTableRegular: bool
        :param _SignalTable: 信号表
注意：此字段可能返回 null，表示取不到有效值。
        :type SignalTable: str
        :param _DateTimeZone: datetime 类型字段转换为时间戳的时区
注意：此字段可能返回 null，表示取不到有效值。
        :type DateTimeZone: str
        :param _SelfBuilt: 自建
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def DdlTopic(self):
        return self._DdlTopic

    @DdlTopic.setter
    def DdlTopic(self, DdlTopic):
        self._DdlTopic = DdlTopic

    @property
    def DataSourceMonitorMode(self):
        return self._DataSourceMonitorMode

    @DataSourceMonitorMode.setter
    def DataSourceMonitorMode(self, DataSourceMonitorMode):
        self._DataSourceMonitorMode = DataSourceMonitorMode

    @property
    def DataSourceMonitorResource(self):
        return self._DataSourceMonitorResource

    @DataSourceMonitorResource.setter
    def DataSourceMonitorResource(self, DataSourceMonitorResource):
        self._DataSourceMonitorResource = DataSourceMonitorResource

    @property
    def DataSourceIncrementMode(self):
        return self._DataSourceIncrementMode

    @DataSourceIncrementMode.setter
    def DataSourceIncrementMode(self, DataSourceIncrementMode):
        self._DataSourceIncrementMode = DataSourceIncrementMode

    @property
    def DataSourceIncrementColumn(self):
        return self._DataSourceIncrementColumn

    @DataSourceIncrementColumn.setter
    def DataSourceIncrementColumn(self, DataSourceIncrementColumn):
        self._DataSourceIncrementColumn = DataSourceIncrementColumn

    @property
    def DataSourceStartFrom(self):
        return self._DataSourceStartFrom

    @DataSourceStartFrom.setter
    def DataSourceStartFrom(self, DataSourceStartFrom):
        self._DataSourceStartFrom = DataSourceStartFrom

    @property
    def DataTargetInsertMode(self):
        return self._DataTargetInsertMode

    @DataTargetInsertMode.setter
    def DataTargetInsertMode(self, DataTargetInsertMode):
        self._DataTargetInsertMode = DataTargetInsertMode

    @property
    def DataTargetPrimaryKeyField(self):
        return self._DataTargetPrimaryKeyField

    @DataTargetPrimaryKeyField.setter
    def DataTargetPrimaryKeyField(self, DataTargetPrimaryKeyField):
        self._DataTargetPrimaryKeyField = DataTargetPrimaryKeyField

    @property
    def DataTargetRecordMapping(self):
        return self._DataTargetRecordMapping

    @DataTargetRecordMapping.setter
    def DataTargetRecordMapping(self, DataTargetRecordMapping):
        self._DataTargetRecordMapping = DataTargetRecordMapping

    @property
    def TopicRegex(self):
        return self._TopicRegex

    @TopicRegex.setter
    def TopicRegex(self, TopicRegex):
        self._TopicRegex = TopicRegex

    @property
    def TopicReplacement(self):
        return self._TopicReplacement

    @TopicReplacement.setter
    def TopicReplacement(self, TopicReplacement):
        self._TopicReplacement = TopicReplacement

    @property
    def KeyColumns(self):
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def DropInvalidMessage(self):
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def DropCls(self):
        return self._DropCls

    @DropCls.setter
    def DropCls(self, DropCls):
        self._DropCls = DropCls

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def IsTablePrefix(self):
        return self._IsTablePrefix

    @IsTablePrefix.setter
    def IsTablePrefix(self, IsTablePrefix):
        self._IsTablePrefix = IsTablePrefix

    @property
    def IncludeContentChanges(self):
        return self._IncludeContentChanges

    @IncludeContentChanges.setter
    def IncludeContentChanges(self, IncludeContentChanges):
        self._IncludeContentChanges = IncludeContentChanges

    @property
    def IncludeQuery(self):
        return self._IncludeQuery

    @IncludeQuery.setter
    def IncludeQuery(self, IncludeQuery):
        self._IncludeQuery = IncludeQuery

    @property
    def RecordWithSchema(self):
        return self._RecordWithSchema

    @RecordWithSchema.setter
    def RecordWithSchema(self, RecordWithSchema):
        self._RecordWithSchema = RecordWithSchema

    @property
    def SignalDatabase(self):
        return self._SignalDatabase

    @SignalDatabase.setter
    def SignalDatabase(self, SignalDatabase):
        self._SignalDatabase = SignalDatabase

    @property
    def IsTableRegular(self):
        return self._IsTableRegular

    @IsTableRegular.setter
    def IsTableRegular(self, IsTableRegular):
        self._IsTableRegular = IsTableRegular

    @property
    def SignalTable(self):
        return self._SignalTable

    @SignalTable.setter
    def SignalTable(self, SignalTable):
        self._SignalTable = SignalTable

    @property
    def DateTimeZone(self):
        return self._DateTimeZone

    @DateTimeZone.setter
    def DateTimeZone(self, DateTimeZone):
        self._DateTimeZone = DateTimeZone

    @property
    def SelfBuilt(self):
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
        :param _FlowId: FlowId11
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _RouteDTO: RouteIdDto
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteDTO: :class:`tencentcloud.ckafka.v20190819.models.RouteDTO`
        """
        self._FlowId = None
        self._RouteDTO = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RouteDTO(self):
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
        :param _Partition: Partition,例如"0"或"1"
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: str
        :param _Offset: Offset,例如100
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        """
        self._Partition = None
        self._Offset = None

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
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
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Offset(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: PostgreSQL连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: PostgreSQL连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: PostgreSQL连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ServiceVip: PostgreSQL连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: PostgreSQL连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _ClusterId: 当type为TDSQL_C_POSTGRESQL时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _SelfBuilt: PostgreSQL连接源是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: PostgreSQL的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: PostgreSQL连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: PostgreSQL连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: PostgreSQL连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: PostgreSQL连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _ClusterId: 当type为TDSQL_C_POSTGRESQL时，该参数才有值【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _IsUpdate: 是否更新到关联的Datahub任务
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _SelfBuilt: 是否为自建集群
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def SelfBuilt(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: PostgreSQL的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"Schema名.数据表名"的格式进行填写，需要填入正则表达式时，格式为"Schema名\\.数据表名"
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Resource: 该PostgreSQL在连接管理内的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _PluginName: 插件名(decoderbufs/pgoutput)，默认为decoderbufs
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginName: str
        :param _SnapshotMode: 复制存量信息(never增量, initial全量)，默认为initial
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotMode: str
        :param _DataFormat: 上游数据格式(JSON/Debezium), 当数据库同步模式为默认字段匹配时,必填
注意：此字段可能返回 null，表示取不到有效值。
        :type DataFormat: str
        :param _DataTargetInsertMode: "INSERT" 表示使用 Insert 模式插入，"UPSERT" 表示使用 Upsert 模式插入
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetInsertMode: str
        :param _DataTargetPrimaryKeyField: 当 "DataInsertMode"="UPSERT" 时，传入当前 upsert 时依赖的主键
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetPrimaryKeyField: str
        :param _DataTargetRecordMapping: 表与消息间的映射关系
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTargetRecordMapping: list of RecordMapping
        :param _DropInvalidMessage: 是否抛弃解析失败的消息，默认为true
注意：此字段可能返回 null，表示取不到有效值。
        :type DropInvalidMessage: bool
        :param _IsTableRegular: 输入的table是否为正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTableRegular: bool
        :param _KeyColumns: 格式：库1.表1:字段1,字段2;库2.表2:字段2，表之间;（分号）隔开，字段之间,（逗号）隔开。不指定的表默认取表的主键
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyColumns: str
        :param _RecordWithSchema: 如果该值为 true，则消息中会携带消息结构体对应的schema，如果该值为false则不会携带
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def SnapshotMode(self):
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode

    @property
    def DataFormat(self):
        return self._DataFormat

    @DataFormat.setter
    def DataFormat(self, DataFormat):
        self._DataFormat = DataFormat

    @property
    def DataTargetInsertMode(self):
        return self._DataTargetInsertMode

    @DataTargetInsertMode.setter
    def DataTargetInsertMode(self, DataTargetInsertMode):
        self._DataTargetInsertMode = DataTargetInsertMode

    @property
    def DataTargetPrimaryKeyField(self):
        return self._DataTargetPrimaryKeyField

    @DataTargetPrimaryKeyField.setter
    def DataTargetPrimaryKeyField(self, DataTargetPrimaryKeyField):
        self._DataTargetPrimaryKeyField = DataTargetPrimaryKeyField

    @property
    def DataTargetRecordMapping(self):
        return self._DataTargetRecordMapping

    @DataTargetRecordMapping.setter
    def DataTargetRecordMapping(self, DataTargetRecordMapping):
        self._DataTargetRecordMapping = DataTargetRecordMapping

    @property
    def DropInvalidMessage(self):
        return self._DropInvalidMessage

    @DropInvalidMessage.setter
    def DropInvalidMessage(self, DropInvalidMessage):
        self._DropInvalidMessage = DropInvalidMessage

    @property
    def IsTableRegular(self):
        return self._IsTableRegular

    @IsTableRegular.setter
    def IsTableRegular(self, IsTableRegular):
        self._IsTableRegular = IsTableRegular

    @property
    def KeyColumns(self):
        return self._KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns):
        self._KeyColumns = KeyColumns

    @property
    def RecordWithSchema(self):
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
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TotalCost(self):
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
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerIp: str
        :param _VpcId: VPC ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID信息
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SourceIp(self):
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SourcePort(self):
        return self._SourcePort

    @SourcePort.setter
    def SourcePort(self, SourcePort):
        self._SourcePort = SourcePort

    @property
    def BrokerIp(self):
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
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
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMessage(self):
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

    @property
    def Data(self):
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
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._JsonKey

    @JsonKey.setter
    def JsonKey(self, JsonKey):
        self._JsonKey = JsonKey

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AllowNull(self):
        return self._AllowNull

    @AllowNull.setter
    def AllowNull(self, AllowNull):
        self._AllowNull = AllowNull

    @property
    def ColumnName(self):
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def ColumnSize(self):
        return self._ColumnSize

    @ColumnSize.setter
    def ColumnSize(self, ColumnSize):
        self._ColumnSize = ColumnSize

    @property
    def DecimalDigits(self):
        return self._DecimalDigits

    @DecimalDigits.setter
    def DecimalDigits(self, DecimalDigits):
        self._DecimalDigits = DecimalDigits

    @property
    def AutoIncrement(self):
        return self._AutoIncrement

    @AutoIncrement.setter
    def AutoIncrement(self, AutoIncrement):
        self._AutoIncrement = AutoIncrement

    @property
    def DefaultValue(self):
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
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def NewValue(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCode: str
        :param _RegionCodeV3: 地域代码（V3版本）
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCodeV3: str
        :param _Support: NONE:默认值不支持任何特殊机型\nCVM:支持CVM类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Support: str
        :param _Ipv6: 是否支持ipv6, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: int
        :param _MultiZone: 是否支持跨可用区, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def AreaName(self):
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def RegionCode(self):
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def RegionCodeV3(self):
        return self._RegionCodeV3

    @RegionCodeV3.setter
    def RegionCodeV3(self, RegionCodeV3):
        self._RegionCodeV3 = RegionCodeV3

    @property
    def Support(self):
        return self._Support

    @Support.setter
    def Support(self, Support):
        self._Support = Support

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def MultiZone(self):
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
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _TimeSpan: 续费时长, 默认为1, 单位是月
        :type TimeSpan: int
        """
        self._InstanceId = None
        self._TimeSpan = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeSpan(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param _DealName: 子订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        """
        self._BigDealId = None
        self._DealName = None

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def DealName(self):
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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
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
        :param _RouteId: 路由ID
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteTimestamp: str
        :param _Subnet: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Subnet: str
        :param _BrokerVipList: 虚拟IP列表(1对1 broker节点)
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerVipList: list of VipEntity
        :param _VpcId: vpc信息
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
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def RouteId(self):
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def VipType(self):
        return self._VipType

    @VipType.setter
    def VipType(self, VipType):
        self._VipType = VipType

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainPort(self):
        return self._DomainPort

    @DomainPort.setter
    def DomainPort(self, DomainPort):
        self._DomainPort = DomainPort

    @property
    def DeleteTimestamp(self):
        return self._DeleteTimestamp

    @DeleteTimestamp.setter
    def DeleteTimestamp(self, DeleteTimestamp):
        self._DeleteTimestamp = DeleteTimestamp

    @property
    def Subnet(self):
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def BrokerVipList(self):
        return self._BrokerVipList

    @BrokerVipList.setter
    def BrokerVipList(self, BrokerVipList):
        self._BrokerVipList = BrokerVipList

    @property
    def VpcId(self):
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
        :param _RouteId: RouteId11
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteId: int
        """
        self._RouteId = None

    @property
    def RouteId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Routers: list of Route
        """
        self._Routers = None

    @property
    def Routers(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValueDelimiter: str
        :param _EntryDelimiter: 元素建的分隔符
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryDelimiter: str
        """
        self._RowContent = None
        self._KeyValueDelimiter = None
        self._EntryDelimiter = None

    @property
    def RowContent(self):
        return self._RowContent

    @RowContent.setter
    def RowContent(self, RowContent):
        self._RowContent = RowContent

    @property
    def KeyValueDelimiter(self):
        return self._KeyValueDelimiter

    @KeyValueDelimiter.setter
    def KeyValueDelimiter(self, KeyValueDelimiter):
        self._KeyValueDelimiter = KeyValueDelimiter

    @property
    def EntryDelimiter(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _ValueOperate: VALUE处理
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueOperate: :class:`tencentcloud.ckafka.v20190819.models.ValueParam`
        :param _OriginalValue: 原始VALUE
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalValue: str
        :param _ValueOperates: VALUE处理链
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def SchemeType(self):
        return self._SchemeType

    @SchemeType.setter
    def SchemeType(self, SchemeType):
        self._SchemeType = SchemeType

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueOperate(self):
        return self._ValueOperate

    @ValueOperate.setter
    def ValueOperate(self, ValueOperate):
        self._ValueOperate = ValueOperate

    @property
    def OriginalValue(self):
        return self._OriginalValue

    @OriginalValue.setter
    def OriginalValue(self, OriginalValue):
        self._OriginalValue = OriginalValue

    @property
    def ValueOperates(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _UserName: SQLServer连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: SQLServer连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Resource: SQLServer连接源的实例资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _ServiceVip: SQLServer连接源的实例vip，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: SQLServer连接源的vpcId，当为腾讯云实例时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _IsUpdate: 是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _Port: SQLServer的连接port【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ServiceVip: SQLServer连接源的实例vip【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceVip: str
        :param _UniqVpcId: SQLServer连接源的vpcId【不支持修改】
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UserName: SQLServer连接源的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _Password: SQLServer连接源的密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _IsUpdate: 是否更新到关联的Dip任务
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceVip(self):
        return self._ServiceVip

    @ServiceVip.setter
    def ServiceVip(self, ServiceVip):
        self._ServiceVip = ServiceVip

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IsUpdate(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param _Table: SQLServer的数据表名称，"*"为所监听的所有数据库中的非系统表，可以","间隔，监听多个数据表，但数据表需要以"数据库名.数据表名"的格式进行填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param _Resource: 该SQLServer在连接管理内的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        :param _SnapshotMode: 复制存量信息(schema_only增量, initial全量)，默认为initial
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotMode: str
        """
        self._Database = None
        self._Table = None
        self._Resource = None
        self._SnapshotMode = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def SnapshotMode(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: bool
        :param _Version: ckakfa版本号(1.1.1/2.4.2/0.10.2)
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Platform: 专业版、标准版标志
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param _SoldOut: 售罄标志：true售罄
注意：此字段可能返回 null，表示取不到有效值。
        :type SoldOut: bool
        """
        self._Flag = None
        self._Version = None
        self._Platform = None
        self._SoldOut = None

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SoldOut(self):
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
        :param _DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        """
        self._DealNames = None

    @property
    def DealNames(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionName: str
        :param _Namespace: SCF云函数命名空间, 默认为default
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Qualifier: SCF云函数版本及别名, 默认为$DEFAULT
注意：此字段可能返回 null，表示取不到有效值。
        :type Qualifier: str
        :param _BatchSize: 每批最大发送消息数, 默认为1000
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _MaxRetries: SCF调用失败后重试次数, 默认为5
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetries: int
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None
        self._BatchSize = None
        self._MaxRetries = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def BatchSize(self):
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def MaxRetries(self):
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
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
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
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: list of int
        :param _PartitionOffset: 分区offset信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionOffset: list of PartitionOffset
        :param _TopicId: 订阅的主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self._TopicName = None
        self._Partition = None
        self._PartitionOffset = None
        self._TopicId = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def PartitionOffset(self):
        return self._PartitionOffset

    @PartitionOffset.setter
    def PartitionOffset(self, PartitionOffset):
        self._PartitionOffset = PartitionOffset

    @property
    def TopicId(self):
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
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
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
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicId(self):
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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: str
        """
        self._Status = None
        self._Output = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Bid: str
        :param _Tid: Tdw的tid
注意：此字段可能返回 null，表示取不到有效值。
        :type Tid: str
        :param _IsDomestic: 默认true
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDomestic: bool
        :param _TdwHost: TDW地址，默认tl-tdbank-tdmanager.tencent-distribute.com
注意：此字段可能返回 null，表示取不到有效值。
        :type TdwHost: str
        :param _TdwPort: TDW端口，默认8099
注意：此字段可能返回 null，表示取不到有效值。
        :type TdwPort: int
        """
        self._Bid = None
        self._Tid = None
        self._IsDomestic = None
        self._TdwHost = None
        self._TdwPort = None

    @property
    def Bid(self):
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def Tid(self):
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def IsDomestic(self):
        return self._IsDomestic

    @IsDomestic.setter
    def IsDomestic(self, IsDomestic):
        self._IsDomestic = IsDomestic

    @property
    def TdwHost(self):
        return self._TdwHost

    @TdwHost.setter
    def TdwHost(self, TdwHost):
        self._TdwHost = TdwHost

    @property
    def TdwPort(self):
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
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Note(self):
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableAclRule: int
        :param _AclRuleList: 预设策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AclRuleList: list of AclRule
        :param _QuotaConfig: topic 限流策略
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaConfig: :class:`tencentcloud.ckafka.v20190819.models.InstanceQuotaConfigResp`
        :param _ReplicaNum: 副本数
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def EnableWhiteList(self):
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteList(self):
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def EnableAclRule(self):
        return self._EnableAclRule

    @EnableAclRule.setter
    def EnableAclRule(self, EnableAclRule):
        self._EnableAclRule = EnableAclRule

    @property
    def AclRuleList(self):
        return self._AclRuleList

    @AclRuleList.setter
    def AclRuleList(self, AclRuleList):
        self._AclRuleList = AclRuleList

    @property
    def QuotaConfig(self):
        return self._QuotaConfig

    @QuotaConfig.setter
    def QuotaConfig(self, QuotaConfig):
        self._QuotaConfig = QuotaConfig

    @property
    def ReplicaNum(self):
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
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _ReplicaNum: 副本数
        :type ReplicaNum: int
        :param _Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _EnableWhiteList: 是否开启ip鉴权白名单，true表示开启，false表示不开启
        :type EnableWhiteList: bool
        :param _IpWhiteListCount: ip白名单中ip个数
        :type IpWhiteListCount: int
        :param _ForwardCosBucket: 数据备份cos bucket: 转存到cos 的bucket地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardCosBucket: str
        :param _ForwardStatus: 数据备份cos 状态： 1 不开启数据备份，0 开启数据备份
        :type ForwardStatus: int
        :param _ForwardInterval: 数据备份到cos的周期频率
        :type ForwardInterval: int
        :param _Config: 高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param _RetentionTimeConfig: 消息保留时间配置(用于动态配置变更记录)
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        :param _Status: 0:正常，1：已删除，2：删除中
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableWhiteList(self):
        return self._EnableWhiteList

    @EnableWhiteList.setter
    def EnableWhiteList(self, EnableWhiteList):
        self._EnableWhiteList = EnableWhiteList

    @property
    def IpWhiteListCount(self):
        return self._IpWhiteListCount

    @IpWhiteListCount.setter
    def IpWhiteListCount(self, IpWhiteListCount):
        self._IpWhiteListCount = IpWhiteListCount

    @property
    def ForwardCosBucket(self):
        return self._ForwardCosBucket

    @ForwardCosBucket.setter
    def ForwardCosBucket(self, ForwardCosBucket):
        self._ForwardCosBucket = ForwardCosBucket

    @property
    def ForwardStatus(self):
        return self._ForwardStatus

    @ForwardStatus.setter
    def ForwardStatus(self, ForwardStatus):
        self._ForwardStatus = ForwardStatus

    @property
    def ForwardInterval(self):
        return self._ForwardInterval

    @ForwardInterval.setter
    def ForwardInterval(self, ForwardInterval):
        self._ForwardInterval = ForwardInterval

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RetentionTimeConfig(self):
        return self._RetentionTimeConfig

    @RetentionTimeConfig.setter
    def RetentionTimeConfig(self, RetentionTimeConfig):
        self._RetentionTimeConfig = RetentionTimeConfig

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of TopicDetail
        :param _TotalCount: 符合条件的所有主题详情数量
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
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
        :param _TopicTraffic: Topic 流量
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
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def TopicTraffic(self):
        return self._TopicTraffic

    @TopicTraffic.setter
    def TopicTraffic(self, TopicTraffic):
        self._TopicTraffic = TopicTraffic

    @property
    def MessageHeap(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicMessageHeap: list of TopicMessageHeapRanking
        :param _BrokerIp: Broker Ip 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerIp: list of str
        :param _BrokerTopicData: 单个broker 节点 Topic占用的数据大小
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TopicFlow

    @TopicFlow.setter
    def TopicFlow(self, TopicFlow):
        self._TopicFlow = TopicFlow

    @property
    def ConsumeSpeed(self):
        return self._ConsumeSpeed

    @ConsumeSpeed.setter
    def ConsumeSpeed(self, ConsumeSpeed):
        self._ConsumeSpeed = ConsumeSpeed

    @property
    def TopicMessageHeap(self):
        return self._TopicMessageHeap

    @TopicMessageHeap.setter
    def TopicMessageHeap(self, TopicMessageHeap):
        self._TopicMessageHeap = TopicMessageHeap

    @property
    def BrokerIp(self):
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def BrokerTopicData(self):
        return self._BrokerTopicData

    @BrokerTopicData.setter
    def BrokerTopicData(self, BrokerTopicData):
        self._BrokerTopicData = BrokerTopicData

    @property
    def BrokerTopicFlowData(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginOffset: int
        :param _EndOffset: 末端Offset
注意：此字段可能返回 null，表示取不到有效值。
        :type EndOffset: int
        :param _MessageCount: 消息数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageCount: int
        :param _OutOfSyncReplica: 未同步副本集
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Leader(self):
        return self._Leader

    @Leader.setter
    def Leader(self, Leader):
        self._Leader = Leader

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def InSyncReplica(self):
        return self._InSyncReplica

    @InSyncReplica.setter
    def InSyncReplica(self, InSyncReplica):
        self._InSyncReplica = InSyncReplica

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def EndOffset(self):
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def MessageCount(self):
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def OutOfSyncReplica(self):
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
        return self._TopicInSyncReplicaList

    @TopicInSyncReplicaList.setter
    def TopicInSyncReplicaList(self, TopicInSyncReplicaList):
        self._TopicInSyncReplicaList = TopicInSyncReplicaList

    @property
    def TotalCount(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _PartitionNum: 分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNum: int
        :param _ReplicaNum: 副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicaNum: int
        :param _TopicTraffic: Topic 流量
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicTraffic: str
        :param _MessageHeap: topic消息堆积/占用磁盘
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def TopicTraffic(self):
        return self._TopicTraffic

    @TopicTraffic.setter
    def TopicTraffic(self, TopicTraffic):
        self._TopicTraffic = TopicTraffic

    @property
    def MessageHeap(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _CompressionType: 写入Topic时是否进行压缩，不开启填"none"，开启的话，可选择"gzip", "snappy", "lz4"中的一个进行填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompressionType: str
        :param _UseAutoCreateTopic: 使用的Topic是否需要自动创建（目前只支持SOURCE流入任务）
注意：此字段可能返回 null，表示取不到有效值。
        :type UseAutoCreateTopic: bool
        :param _MsgMultiple: 源topic消息1条扩增成msgMultiple条写入目标topic(该参数目前只有ckafka流入ckafka适用)
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def OffsetType(self):
        return self._OffsetType

    @OffsetType.setter
    def OffsetType(self, OffsetType):
        self._OffsetType = OffsetType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CompressionType(self):
        return self._CompressionType

    @CompressionType.setter
    def CompressionType(self, CompressionType):
        self._CompressionType = CompressionType

    @property
    def UseAutoCreateTopic(self):
        return self._UseAutoCreateTopic

    @UseAutoCreateTopic.setter
    def UseAutoCreateTopic(self, UseAutoCreateTopic):
        self._UseAutoCreateTopic = UseAutoCreateTopic

    @property
    def MsgMultiple(self):
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
        :param _Partition: Partition ID
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
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def LeaderStatus(self):
        return self._LeaderStatus

    @LeaderStatus.setter
    def LeaderStatus(self, LeaderStatus):
        self._LeaderStatus = LeaderStatus

    @property
    def IsrNum(self):
        return self._IsrNum

    @IsrNum.setter
    def IsrNum(self, IsrNum):
        self._IsrNum = IsrNum

    @property
    def ReplicaNum(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of Topic
        :param _TotalCount: 符合条件的 topic 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._TopicList = None
        self._TotalCount = None

    @property
    def TopicList(self):
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Expect: int
        :param _Current: 当前值，即当前生效值(可能存在动态调整，单位分钟)
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        :param _ModTimeStamp: 最近变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTimeStamp: int
        """
        self._Expect = None
        self._Current = None
        self._ModTimeStamp = None

    @property
    def Expect(self):
        return self._Expect

    @Expect.setter
    def Expect(self, Expect):
        self._Expect = Expect

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def ModTimeStamp(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupsInfo: list of GroupInfoResponse
        :param _Status: 此次请求是否异步的状态。实例里分组较少的会直接返回结果,Status为1。当分组较多时,会异步更新缓存，Status为0时不会返回分组信息，直至Status为1更新完毕返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._TotalCount = None
        self._StatusCountInfo = None
        self._GroupsInfo = None
        self._Status = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StatusCountInfo(self):
        return self._StatusCountInfo

    @StatusCountInfo.setter
    def StatusCountInfo(self, StatusCountInfo):
        self._StatusCountInfo = StatusCountInfo

    @property
    def GroupsInfo(self):
        return self._GroupsInfo

    @GroupsInfo.setter
    def GroupsInfo(self, GroupsInfo):
        self._GroupsInfo = GroupsInfo

    @property
    def Status(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _AnalyseResult: 解析结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalyseResult: list of MapParam
        :param _UseEventBus: 底层引擎是否使用eb
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._AnalysisFormat

    @AnalysisFormat.setter
    def AnalysisFormat(self, AnalysisFormat):
        self._AnalysisFormat = AnalysisFormat

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def FailureParam(self):
        return self._FailureParam

    @FailureParam.setter
    def FailureParam(self, FailureParam):
        self._FailureParam = FailureParam

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def MapParam(self):
        return self._MapParam

    @MapParam.setter
    def MapParam(self, MapParam):
        self._MapParam = MapParam

    @property
    def FilterParam(self):
        return self._FilterParam

    @FilterParam.setter
    def FilterParam(self, FilterParam):
        self._FilterParam = FilterParam

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def AnalyseResult(self):
        return self._AnalyseResult

    @AnalyseResult.setter
    def AnalyseResult(self, AnalyseResult):
        self._AnalyseResult = AnalyseResult

    @property
    def UseEventBus(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterParam: list of FilterMapParam
        :param _FailureParam: 失败处理
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureParam: :class:`tencentcloud.ckafka.v20190819.models.FailureParam`
        :param _Result: 测试结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _SourceType: 数据来源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _OutputFormat: 输出格式，JSON，ROW，默认为JSON
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputFormat: str
        :param _RowParam: 输出格式为ROW必填
注意：此字段可能返回 null，表示取不到有效值。
        :type RowParam: :class:`tencentcloud.ckafka.v20190819.models.RowParam`
        :param _KeepMetadata: 是否保留数据源Topic元数据信息（源Topic、Partition、Offset），默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepMetadata: bool
        :param _BatchAnalyse: 数组解析
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FieldChain(self):
        return self._FieldChain

    @FieldChain.setter
    def FieldChain(self, FieldChain):
        self._FieldChain = FieldChain

    @property
    def FilterParam(self):
        return self._FilterParam

    @FilterParam.setter
    def FilterParam(self, FilterParam):
        self._FilterParam = FilterParam

    @property
    def FailureParam(self):
        return self._FailureParam

    @FailureParam.setter
    def FailureParam(self, FailureParam):
        self._FailureParam = FailureParam

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def RowParam(self):
        return self._RowParam

    @RowParam.setter
    def RowParam(self, RowParam):
        self._RowParam = RowParam

    @property
    def KeepMetadata(self):
        return self._KeepMetadata

    @KeepMetadata.setter
    def KeepMetadata(self, KeepMetadata):
        self._KeepMetadata = KeepMetadata

    @property
    def BatchAnalyse(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type CharsetName: str
        """
        self._CharsetName = None

    @property
    def CharsetName(self):
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of User
        :param _TotalCount: 符合条件的总用户数
        :type TotalCount: int
        """
        self._Users = None
        self._TotalCount = None

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def TotalCount(self):
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Replace(self):
        return self._Replace

    @Replace.setter
    def Replace(self, Replace):
        self._Replace = Replace

    @property
    def Substr(self):
        return self._Substr

    @Substr.setter
    def Substr(self, Substr):
        self._Substr = Substr

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def RegexReplace(self):
        return self._RegexReplace

    @RegexReplace.setter
    def RegexReplace(self, RegexReplace):
        self._RegexReplace = RegexReplace

    @property
    def Split(self):
        return self._Split

    @Split.setter
    def Split(self, Split):
        self._Split = Split

    @property
    def KV(self):
        return self._KV

    @KV.setter
    def KV(self, KV):
        self._KV = KV

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def JsonPathReplace(self):
        return self._JsonPathReplace

    @JsonPathReplace.setter
    def JsonPathReplace(self, JsonPathReplace):
        self._JsonPathReplace = JsonPathReplace

    @property
    def UrlDecode(self):
        return self._UrlDecode

    @UrlDecode.setter
    def UrlDecode(self, UrlDecode):
        self._UrlDecode = UrlDecode

    @property
    def Lowercase(self):
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
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
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
        :param _ZoneId: zone的id
        :type ZoneId: str
        :param _IsInternalApp: 是否内部APP
        :type IsInternalApp: int
        :param _AppId: app id
        :type AppId: int
        :param _Flag: 标识
        :type Flag: bool
        :param _ZoneName: zone名称
        :type ZoneName: str
        :param _ZoneStatus: zone状态
        :type ZoneStatus: int
        :param _Exflag: 额外标识
        :type Exflag: str
        :param _SoldOut: json对象，key为机型，value true为售罄，false为未售罄
        :type SoldOut: str
        :param _SalesInfo: 标准版售罄信息
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsInternalApp(self):
        return self._IsInternalApp

    @IsInternalApp.setter
    def IsInternalApp(self, IsInternalApp):
        self._IsInternalApp = IsInternalApp

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneStatus(self):
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus

    @property
    def Exflag(self):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        return self._Exflag

    @Exflag.setter
    def Exflag(self, Exflag):
        warnings.warn("parameter `Exflag` is deprecated", DeprecationWarning) 

        self._Exflag = Exflag

    @property
    def SoldOut(self):
        return self._SoldOut

    @SoldOut.setter
    def SoldOut(self, SoldOut):
        self._SoldOut = SoldOut

    @property
    def SalesInfo(self):
        return self._SalesInfo

    @SalesInfo.setter
    def SalesInfo(self, SalesInfo):
        self._SalesInfo = SalesInfo

    @property
    def ExtraFlag(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterInfo: list of ClusterInfo
        :param _Standard: 购买标准版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        :param _StandardS2: 购买标准版S2配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardS2: str
        :param _Profession: 购买专业版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param _Physical: 购买物理独占版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Physical: str
        :param _PublicNetwork: 公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: str
        :param _PublicNetworkLimit: 公网带宽配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetworkLimit: str
        :param _RequestId: 请求ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Offset: 分页offset
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 分页limit
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _ForceCheckTag: 是否必须录入tag
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def MaxBuyInstanceNum(self):
        return self._MaxBuyInstanceNum

    @MaxBuyInstanceNum.setter
    def MaxBuyInstanceNum(self, MaxBuyInstanceNum):
        self._MaxBuyInstanceNum = MaxBuyInstanceNum

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def MessagePrice(self):
        return self._MessagePrice

    @MessagePrice.setter
    def MessagePrice(self, MessagePrice):
        self._MessagePrice = MessagePrice

    @property
    def ClusterInfo(self):
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def Standard(self):
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def StandardS2(self):
        return self._StandardS2

    @StandardS2.setter
    def StandardS2(self, StandardS2):
        self._StandardS2 = StandardS2

    @property
    def Profession(self):
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def Physical(self):
        return self._Physical

    @Physical.setter
    def Physical(self, Physical):
        self._Physical = Physical

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def PublicNetworkLimit(self):
        return self._PublicNetworkLimit

    @PublicNetworkLimit.setter
    def PublicNetworkLimit(self, PublicNetworkLimit):
        self._PublicNetworkLimit = PublicNetworkLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ForceCheckTag(self):
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
        